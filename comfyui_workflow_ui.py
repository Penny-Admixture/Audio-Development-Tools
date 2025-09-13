"""Build a Tkinter UI from a ComfyUI workflow and execute it end‑to‑end.

The script accepts a ComfyUI workflow JSON file or a PNG exported from
ComfyUI containing workflow metadata. It automatically clones the
ComfyUI repository if missing, starts a local ComfyUI server, exposes all
editable node parameters in a Tkinter interface and runs the workflow
through the server. Output images/audio are fetched via the HTTP API and
saved locally. A convenience option is provided to bundle everything into
an executable using PyInstaller.
"""

from __future__ import annotations

import argparse
import io
import json
import os
import subprocess
import sys
import threading
import time
import tkinter as tk
from pathlib import Path
from typing import Any, Dict
from urllib import parse, request

try:
    from PIL import Image, ImageTk
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Pillow is required to load workflow files") from exc

# ---------------------------------------------------------------------------
# ComfyUI bootstrap

COMFY_REPO = Path("ComfyUI")
SERVER_PORT = 8188  # default server port; overridden by --port


def ensure_comfyui() -> None:
    """Clone the ComfyUI repository if it does not exist."""
    if COMFY_REPO.exists():
        return
    subprocess.run([
        "git",
        "clone",
        "https://github.com/comfyanonymous/ComfyUI.git",
        str(COMFY_REPO),
    ], check=True)


def start_server() -> subprocess.Popen[str]:
    """Launch the ComfyUI server if it's not already running."""
    ensure_comfyui()
    env = os.environ.copy()
    cmd = [sys.executable, "main.py", "--port", str(SERVER_PORT), "--no-auth"]
    proc = subprocess.Popen(cmd, cwd=COMFY_REPO, env=env)

    # wait for server to be ready
    for _ in range(60):
        try:
            request.urlopen(f"http://127.0.0.1:{SERVER_PORT}", timeout=1)
            break
        except Exception:
            time.sleep(1)
    return proc

# ---------------------------------------------------------------------------
# Workflow loading


def load_workflow(path: Path) -> Dict[str, Any]:
    """Load workflow data from JSON or PNG file."""
    if path.suffix.lower() == ".png":
        image = Image.open(path)
        meta = image.info
        if "workflow" not in meta:
            raise ValueError("PNG file does not contain workflow metadata")
        return json.loads(meta["workflow"])
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

# ---------------------------------------------------------------------------
# API helpers


def queue_prompt(prompt: Dict[str, Any]) -> str:
    data = json.dumps({"prompt": prompt}).encode("utf-8")
    req = request.Request(
        f"http://127.0.0.1:{SERVER_PORT}/prompt", data=data
    )
    return json.loads(request.urlopen(req).read())["prompt_id"]


def poll_history(prompt_id: str) -> Dict[str, Any]:
    url = f"http://127.0.0.1:{SERVER_PORT}/history/{prompt_id}"
    while True:
        try:
            with request.urlopen(url) as resp:
                data = json.loads(resp.read())
            if data.get("outputs"):
                return data["outputs"]
        except Exception:
            pass
        time.sleep(1)


def fetch_image(info: Dict[str, Any]) -> bytes:
    params = parse.urlencode(
        {
            "filename": info["filename"],
            "subfolder": info.get("subfolder", ""),
            "type": info.get("type", "output"),
        }
    )
    with request.urlopen(
        f"http://127.0.0.1:{SERVER_PORT}/view?{params}"
    ) as resp:
        return resp.read()

# ---------------------------------------------------------------------------
# UI generation and execution


def build_ui(workflow: Dict[str, Any]) -> None:
    root = tk.Tk()
    root.title("ComfyUI Workflow Runner")

    canvas = tk.Canvas(root, borderwidth=0)
    frame = tk.Frame(canvas)
    vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4, 4), window=frame, anchor="nw")

    frame.bind(
        "<Configure>",
        lambda event: canvas.configure(scrollregion=canvas.bbox("all")),
    )

    entries: Dict[str, tk.Variable] = {}

    for node in workflow.get("nodes", []):
        node_frame = tk.LabelFrame(frame, text=f"{node.get('id')} {node.get('type')}")
        node_frame.pack(fill="x", padx=5, pady=5, ipadx=5, ipady=5)
        inputs = node.get("inputs", {})
        for name, value in inputs.items():
            var: tk.Variable
            if isinstance(value, bool):
                var = tk.BooleanVar(value=value)
                widget = tk.Checkbutton(node_frame, text=name, variable=var)
                widget.pack(anchor="w")
            else:
                var = tk.StringVar(value=str(value))
                tk.Label(node_frame, text=name).pack(anchor="w")
                tk.Entry(node_frame, textvariable=var).pack(fill="x")
            entries[f"{node['id']}.{name}"] = var

    output_label = tk.Label(root, text="")
    output_label.pack(pady=5)

    def run_workflow() -> None:
        # update workflow with UI values
        for node in workflow.get("nodes", []):
            inputs = node.get("inputs", {})
            for name in inputs:
                key = f"{node['id']}.{name}"
                if key in entries:
                    val = entries[key].get()
                    try:
                        inputs[name] = json.loads(val)
                    except Exception:
                        inputs[name] = val
        proc = start_server()
        prompt_id = queue_prompt({str(n['id']): {"class_type": n["type"], "inputs": n.get("inputs", {})} for n in workflow.get("nodes", [])})
        outputs = poll_history(prompt_id)
        images = []
        for node_out in outputs.values():
            for info in node_out.get("images", []):
                data = fetch_image(info)
                images.append(Image.open(io.BytesIO(data)))
        if images:
            img = ImageTk.PhotoImage(images[0])
            panel = tk.Label(root, image=img)
            panel.image = img  # keep reference
            panel.pack()
            output_label.config(text=f"Saved {len(images)} image(s)")
        proc.terminate()

    tk.Button(root, text="Run Workflow", command=lambda: threading.Thread(target=run_workflow).start()).pack(pady=10)
    root.mainloop()

# ---------------------------------------------------------------------------
# CLI entry


def build_executable() -> None:
    """Bundle the script into a standalone executable using PyInstaller."""
    subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    subprocess.run(["pyinstaller", "--onefile", Path(__file__).name], check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workflow", type=Path, help="Path to ComfyUI workflow JSON or PNG file")
    parser.add_argument("--build-exe", action="store_true", help="Package the script with PyInstaller")
    parser.add_argument("--port", type=int, default=8188, help="Port for ComfyUI server")
    args = parser.parse_args()

    if args.build_exe:
        build_executable()
        return

    global SERVER_PORT
    SERVER_PORT = args.port

    workflow = load_workflow(args.workflow)
    build_ui(workflow)


if __name__ == "__main__":
    main()
