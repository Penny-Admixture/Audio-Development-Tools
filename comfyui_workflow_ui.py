#!/usr/bin/env python3
"""Autogenerate a simple Tkinter UI from a ComfyUI workflow file.

Given a ComfyUI workflow JSON file or a PNG exported from ComfyUI
containing the workflow metadata, this script extracts the workflow and
creates a Tkinter based form for all node inputs that have constant
values. The intent is to provide a minimal example of how one could
programmatically expose ComfyUI node parameters for modification outside
of the ComfyUI interface.

This script does not attempt to execute the workflow itself – it only
parses the workflow and exposes the adjustable fields. Executing the
workflow would require a full installation of ComfyUI and is outside the
scope of this helper script.
"""

from __future__ import annotations

import argparse
import json
import tkinter as tk
from pathlib import Path
from typing import Any, Dict

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover - handled at runtime
    raise SystemExit("Pillow is required to load workflow PNG files") from exc


# ---------------------------------------------------------------------------
# Workflow loading


def load_workflow(path: Path) -> Dict[str, Any]:
    """Load workflow data from JSON or PNG file.

    Parameters
    ----------
    path: Path
        Path to the workflow file. PNG files are expected to contain the
        workflow JSON in their metadata using the key 'workflow'.
    """

    if path.suffix.lower() == ".png":
        image = Image.open(path)
        meta = image.info
        if "workflow" not in meta:
            raise ValueError("PNG file does not contain workflow metadata")
        return json.loads(meta["workflow"])

    # Assume JSON by default
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# UI generation helpers


def build_ui(workflow: Dict[str, Any]) -> None:
    """Create a Tkinter UI exposing constant inputs for each node."""

    root = tk.Tk()
    root.title("ComfyUI Workflow Parameters")

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
        node_frame = tk.LabelFrame(frame, text=node.get("type", "node"))
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
                label = tk.Label(node_frame, text=name)
                entry = tk.Entry(node_frame, textvariable=var)
                label.pack(anchor="w")
                entry.pack(fill="x")
            entries[f"{node.get('id')}.{name}"] = var

    def dump_values() -> None:
        data = {key: var.get() for key, var in entries.items()}
        print(json.dumps(data, indent=2))

    tk.Button(root, text="Print Values", command=dump_values).pack(pady=10)
    root.mainloop()


# ---------------------------------------------------------------------------
# CLI entry


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "workflow",
        type=Path,
        help="Path to ComfyUI workflow JSON or PNG file",
    )
    args = parser.parse_args()

    workflow = load_workflow(args.workflow)
    build_ui(workflow)


if __name__ == "__main__":
    main()
