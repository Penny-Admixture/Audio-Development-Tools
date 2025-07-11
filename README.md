# Audio Development Tools (ADT) 🔥

Audio Development Tools (ADT) is a project for advancing sound, speech, and music technologies, featuring components for machine learning, audio generation, audio signal processing, sound synthesis, game audio, digital audio workstation, spatial audio, music information retrieval, music generation, speech recognition, speech synthesis, singing voice synthesis, and more.

## Table of Contents

* [Machine Learning (ML)](#ml)
* [Audio Generation (AG)](#ag)
* [Audio Signal Processing (ASP)](#asp)
* [Sound Synthesis (SS)](#ss)
* [Game Audio (GA)](#ga)
* [Digital Audio Workstation (DAW)](#daw)
* [Spatial Audio (SA)](#sa)
* [Web Audio Processing (WAP)](#wap)
* [Music Information Retrieval (MIR)](#mir)
* [Music Generation (MG)](#mg)
* [Speech Recognition (ASR)](#asr)
* [Speech Synthesis (TTS)](#tts)
* [Singing Voice Synthesis (SVS)](#svs)
* [Audio Evaluation](#ae)


## Project List

### <span id="ml">Machine Learning (ML)</span>

* [librosa](https://librosa.org/doc/latest/index.html) - Librosa is a python package for music and audio analysis. It provides the building blocks necessary to create music information retrieval systems.
* [Essentia](http://essentia.upf.edu/) - Essentia is an open-source C++ library for audio analysis and audio-based music information retrieval released under the Affero GPLv3 license. It contains an extensive collection of reusable algorithms which implement audio input/output functionality, standard digital signal processing blocks, statistical characterization of data, and a large set of spectral, temporal, tonal and high-level music descriptors. C++ library for audio and music analysis, description and synthesis, including Python bindings.
* [DDSP](https://github.com/magenta/ddsp) - DDSP: Differentiable Digital Signal Processing. DDSP is a library of differentiable versions of common DSP functions (such as synthesizers, waveshapers, and filters). This allows these interpretable elements to be used as part of an deep learning model, especially as the output layers for audio generation.
* [MIDI-DDSP](https://github.com/magenta/midi-ddsp) - MIDI-DDSP: Detailed Control of Musical Performance via Hierarchical Modeling. MIDI-DDSP is a hierarchical audio generation model for synthesizing MIDI expanded from DDSP.
* [DDSP-VST](https://github.com/magenta/ddsp-vst) - Realtime DDSP Neural Synthesizer and Effect. VST3/AU plugins and desktop applications built using the JUCE framework and DDSP.
* [torchsynth](https://github.com/torchsynth/torchsynth) - A GPU-optional modular synthesizer in pytorch, 16200x faster than realtime, for audio ML researchers.
* [aubio](https://aubio.org/) - aubio is a tool designed for the extraction of annotations from audio signals. Its features include segmenting a sound file before each of its attacks, performing pitch detection, tapping the beat and producing midi streams from live audio.
* [audioFlux](https://audioflux.top/) - audioFlux is a deep learning tool library for audio and music analysis, feature extraction. It supports dozens of time-frequency analysis transformation methods and hundreds of corresponding time-domain and frequency-domain feature combinations. It can be provided to deep learning networks for training, and is used to study various tasks in the audio field such as Classification, Separation, Music Information Retrieval(MIR) and ASR etc.
* [Polymath](https://github.com/samim23/polymath) - Polymath uses machine learning to convert any music library (e.g from Hard-Drive or YouTube) into a music production sample-library. The tool automatically separates songs into stems (beats, bass, etc.), quantizes them to the same tempo and beat-grid (e.g. 120bpm), analyzes musical structure (e.g. verse, chorus, etc.), key (e.g C4, E3, etc.) and other infos (timbre, loudness, etc.), and converts audio to midi. The result is a searchable sample library that streamlines the workflow for music producers, DJs, and ML audio developers.
* [IPython](https://ipython.readthedocs.io/en/stable/index.html) - IPython provides a rich toolkit to help you make the most of using Python interactively.
* [torchaudio](https://github.com/pytorch/audio) - an audio library for PyTorch. Data manipulation and transformation for audio signal processing, powered by PyTorch.
* [TorchLibrosa](https://github.com/qiuqiangkong/torchlibrosa) - PyTorch implementation of Librosa.
* [torch-audiomentations](https://github.com/asteroid-team/torch-audiomentations) - Fast audio data augmentation in PyTorch. Inspired by audiomentations. Useful for deep learning.
* [PyTorch Audio Augmentations](https://github.com/Spijkervet/torchaudio-augmentations) - Audio data augmentations library for PyTorch for audio in the time-domain. 
* [Asteroid](https://asteroid-team.github.io/) - Asteroid is a Pytorch-based audio source separation toolkit that enables fast experimentation on common datasets. It comes with a source code that supports a large range of datasets and architectures, and a set of recipes to reproduce some important papers.
* [Kapre](https://kapre.readthedocs.io/en/latest/#) - Kapre: Keras Audio Preprocessors. Keras Audio Preprocessors - compute STFT, InverseSTFT, Melspectrogram, and others on GPU real-time.
* [praudio](https://github.com/musikalkemist/praudio) - Audio preprocessing framework for Deep Learning audio applications.
* [automix-toolkit](https://github.com/csteinmetz1/automix-toolkit) - Models and datasets for training deep learning automatic mixing models.
* [DeepAFx](https://github.com/adobe-research/DeepAFx) - DeepAFx: Deep Audio Effects. Audio signal processing effects (FX) are used to manipulate sound characteristics across a variety of media. Many FX, however, can be difficult or tedious to use, particularly for novice users. In our work, we aim to simplify how audio FX are used by training a machine to use FX directly and perform automatic audio production tasks. By using familiar and existing tools for processing and suggesting control parameters, we can create a unique paradigm that blends the power of AI with human creative control to empower creators.
* [nnAudio](https://github.com/KinWaiCheuk/nnAudio) - nnAudio is an audio processing toolbox using PyTorch convolutional neural network as its backend. By doing so, spectrograms can be generated from audio on-the-fly during neural network training and the Fourier kernels (e.g. or CQT kernels) can be trained.
* [WavEncoder](https://github.com/shangeth/wavencoder) - WavEncoder is a Python library for encoding audio signals, transforms for audio augmentation, and training audio classification models with PyTorch backend.
* [SciPy](https://scipy.org/) - SciPy (pronounced "Sigh Pie") is an open-source software for mathematics, science, and engineering. It includes modules for statistics, optimization, integration, linear algebra, Fourier transforms, signal and image processing, ODE solvers, and more.
* [pyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis/) - Python Audio Analysis Library: Feature Extraction, Classification, Segmentation and Applications.
* [Mutagen](https://mutagen.readthedocs.io/en/latest/#) - Mutagen is a Python module to handle audio metadata. It supports ASF, FLAC, MP4, Monkey’s Audio, MP3, Musepack, Ogg Opus, Ogg FLAC, Ogg Speex, Ogg Theora, Ogg Vorbis, True Audio, WavPack, OptimFROG, and AIFF audio files. All versions of ID3v2 are supported, and all standard ID3v2.4 frames are parsed. It can read Xing headers to accurately calculate the bitrate and length of MP3s. ID3 and APEv2 tags can be edited regardless of audio format. It can also manipulate Ogg streams on an individual packet/page level.
* [LibXtract](https://github.com/jamiebullock/LibXtract) - LibXtract is a simple, portable, lightweight library of audio feature extraction functions. The purpose of the library is to provide a relatively exhaustive set of feature extraction primatives that are designed to be 'cascaded' to create a extraction hierarchies.
* [dejavu](https://github.com/worldveil/dejavu) - Audio fingerprinting and recognition in Python. Dejavu can memorize audio by listening to it once and fingerprinting it. Then by playing a song and recording microphone input or reading from disk, Dejavu attempts to match the audio against the fingerprints held in the database, returning the song being played.
* [Matchering](https://github.com/sergree/matchering) - 🎚️ Open Source Audio Matching and Mastering. **[Matchering 2.0](https://github.com/sergree/matchering)** is a novel **[Containerized Web Application](https://github.com/sergree/matchering#docker-image---the-easiest-way)** and **[Python Library](https://pypi.org/project/matchering)** for audio matching and [mastering](https://en.wikipedia.org/wiki/Audio_mastering).
* [TimeSide](https://github.com/Parisson/TimeSide) - TimeSide is a python framework enabling low and high level audio analysis, imaging, transcoding, streaming and labelling. Its high-level API is designed to enable complex processing on very large datasets of any audio or video assets with a plug-in architecture, a secure scalable backend and an extensible dynamic web frontend.
* [Meyda](https://meyda.js.org/) - Meyda is a Javascript audio feature extraction library. Meyda supports both offline feature extraction as well as real-time feature extraction using the [Web Audio API](https://github.com/WebAudio/web-audio-api). We wrote a paper about it, which is available [here](https://wac.ircam.fr/pdf/wac15_submission_17.pdf).
* [Audiomentations](https://github.com/iver56/audiomentations) - A Python library for audio data augmentation. Inspired by albumentations. Useful for deep learning. Runs on CPU. Supports mono audio and multichannel audio. Can be integrated in training pipelines in e.g. Tensorflow/Keras or Pytorch. Has helped people get world-class results in Kaggle competitions. Is used by companies making next-generation audio products.
* [soundata](https://github.com/soundata/soundata) - Python library for downloading, loading & working with sound datasets.
* [auraloss](https://github.com/csteinmetz1/auraloss) - A collection of audio-focused loss functions in PyTorch.
* [Neutone](https://neutone.space/) - AI audio plugin & community. Bridging the gap between AI research and creativity 🚀
* [Waveformer](https://github.com/vb000/Waveformer) - An efficient architecture for real-time target sound extraction.
* [EfficientAT](https://github.com/fschmid56/EfficientAT) - Efficient Large-Scale Audio Tagging. We provide AudioSet pre-trained models ready for downstream training and extraction of audio embeddings.
* [EfficientAT_HEAR](https://github.com/fschmid56/EfficientAT_HEAR) - Evaluate EfficientAT models on the Holistic Evaluation of Audio Representations Benchmark.
* [VAD-python](https://github.com/marsbroshok/VAD-python) - Voice Activity Detector in Python. Python code to apply voice activity detector to wave file. Voice activity detector based on ration between energy in speech band and total energy.
* [Diffsynth](https://github.com/hyakuchiki/diffsynth) - A Differentiable Musical Synthesizer in PyTorch.
* [Realtime DDSP](https://github.com/hyakuchiki/realtimeDDSP) - Realtime (streaming) DDSP in PyTorch compatible with neutone.
* [pc-ddsp](https://github.com/splinter21/pc-ddsp) - Pitch Controllable DDSP Vocoders.
* [SSSSM-DDSP](https://github.com/hyakuchiki/SSSSM-DDSP) - Semi-supervised Synthesizer Sound Matching with Differentiable DSP.
* [GOLF](https://github.com/yoyololicon/golf) - A DDSP-based neural vocoder.
* [audacitorch](https://github.com/audacitorch/audacitorch) - PyTorch wrappers for using your model in audacity!
* [Scyclone](https://github.com/Torsion-Audio/Scyclone) - Scyclone is an audio plugin that utilizes neural timbre transfer technology to offer a new approach to audio production. 
* [Scyclone AI](https://github.com/Torsion-Audio/Scyclone-AI) - Create presets for Scyclone: a Real-time Neural Timbre Transfer Plug-in.
* [Multi Task Automatic-Synthesizer-Programming](https://github.com/dafaronbi/Multi-Task-Automatic-Synthesizer-Programming) - This is the code for the multi VST automatic synthesizer programming project.  
* [NeuralNote](https://github.com/DamRsn/NeuralNote) - Audio Plugin for Audio to MIDI transcription using deep learning.  
* [AudioDec](https://github.com/facebookresearch/AudioDec) - An Open-source Streaming High-fidelity Neural Audio Codec. 
* [PaSST](https://github.com/kkoutini/PaSST) - Efficient Training of Audio Transformers with Patchout.
* [speech_data_augment](https://github.com/zzpDapeng/speech_data_augment) - A summary of speech data augment algorithms.
* [AugLy](https://github.com/facebookresearch/AugLy) - A data augmentations library for audio, image, text, and video.
* [NeuraFuzz](https://github.com/mcomunita/neurafuzz) - Neural audio plugin trained on custom analog fuzz circuit design.
* [Ultimate Vocal Remover GUI](https://github.com/Anjok07/ultimatevocalremovergui) - GUI for a Vocal Remover that uses Deep Neural Networks.
* [Frechet Audio Distance](https://github.com/gudgud96/frechet-audio-distance) - A lightweight library for Frechet Audio Distance calculation.
* [LAPE](https://github.com/Sreyan88/LAPE) - A unified framework for Low-resource Audio Processing and Evaluation (SSL Pre-training and Downstream Fine-tuning).
* [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python) - This repository is for active development of the Azure SDK for Python.
* [Panotti](https://github.com/drscotthawley/panotti) - A multi-channel neural network audio classifier using Keras.
* [Allie](https://github.com/jim-schwoebel/allie) - Allie is a framework for building machine learning models from audio, text, image, video, or .CSV files.
* [Torchplugins](https://github.com/rodrigodzf/torchplugins) - Max/MSP, PureData and Unity plugins to load Pytorch models.
* [aeiou](https://github.com/drscotthawley/aeiou) - (ML) audio engineering i/o utils.
* [BirdNET-Analyzer](https://github.com/kahst/BirdNET-Analyzer) - BirdNET analyzer for scientific audio data processing.
* [spring-reverb-dl-models](https://github.com/francescopapaleo/spring-reverb-dl-models) - Virtual Analog Modelling of the Spring Reverb with Deep Learning.
* [EVAR ~](https://github.com/nttcslab/eval-audio-repr) - EVAR ~ Evaluation package for Audio Representations.
* [Julius](https://github.com/adefossez/julius) - Fast PyTorch based DSP for audio and 1D signals.
* [NeuralDX7](https://github.com/Nintorac/NeuralDX7) - Random machine learning experiments related to the classic Yamaha DX7.
* [HANCE](https://github.com/hance-engine/hance-api) - HANCE offers top-quality signal-processing techniques developed by machine learning specialists, sound engineers, and audio processing experts. Our technology is designed to provide users with the highest possible audio experience by removing noise, reverb, and other signal impairments.
* [IDEAW](https://github.com/PecholaL/IDEAW) - Robust Neural Audio Watermarking with Invertible Dual-Embedding.
* [SyNEThesia](https://github.com/RunOrVeith/SyNEThesia) - SyNEThesia is a deep-learning-based music and sound visualizer, and a play of words on Synesthesia, a neurological condition where one perceives a stimulus in multiple ways (for example seeing sound).
* [Voxaboxen](https://github.com/earthspecies/voxaboxen) - Voxaboxen is a deep learning framework designed to find the start and stop times of (possibly overlapping) sound events in a recording.
* [vocal-separate](https://github.com/jianchang512/vocal-separate) - An extremely simple tool for separating vocals and background music, completely localized for web operation, using 2stems/4stems/5stems models.
* [Speech-enhancement](https://github.com/vbelz/Speech-enhancement) - Deep learning for audio denoising.
* [SNAC](https://github.com/hubertsiuzdak/snac) - Multi-Scale Neural Audio Codec (SNAC) compressess 44.1 kHz audio into discrete codes at a low bitrate.
* [Supervoice GPT](https://github.com/ex3ndr/supervoice-gpt) - A GPT model that converts from text to phonemes with durations that is suitable to feed into voice synthesizer.
* [AudioEditing](https://github.com/HilaManor/AudioEditingCode) - Zero-Shot Unsupervised and Text-Based Audio Editing Using DDPM Inversion.
* [MAX-Audio-Classifier](https://github.com/IBM/MAX-Audio-Classifier) - IBM Developer Model Asset Exchange: Audio Classifier.
* [anira](https://github.com/tu-studio/anira) - an architecture for neural network inference in real-time audio applications.
* [FakeSound](https://github.com/FakeSoundData/FakeSound) - Deepfake General Audio Detection.
* [Audio Mamba](https://github.com/kaistmm/Audio-Mamba-AuM) - Bidirectional State Space Model for Audio Representation Learning.
* [SSAMBA](https://github.com/SiavashShams/ssamba) - SSAMBA: Self-Supervised Audio Representation Learning with Mamba State Space Model.
* [SLAM-LLM](https://github.com/X-LANCE/SLAM-LLM) - SLAM-LLM is a deep learning toolkit that allows researchers and developers to train custom multimodal large language model (MLLM), focusing on Speech, Language, Audio, Music processing.
* [MIDI2vec](https://github.com/midi-ld/midi2vec) - MIDI2vec: Learning Embeddings for MIDI Vector Space Representations.

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>


### <span id="ag">Audio Generation (AG)</span>

* [AudioLCM](https://github.com/liuhuadai/AudioLCM) - Text-to-Audio Generation with Latent Consistency Models.
* [Auffusion](https://github.com/happylittlecat2333/Auffusion) - Auffusion: Leveraging the Power of Diffusion and Large Language Models for Text-to-Audio Generation.
* [Audiobox](https://audiobox.metademolab.com/) - Audiobox: Unified Audio Generation with Natural Language Prompts.
* [Amphion](https://github.com/open-mmlab/Amphion) - Amphion: An Open-Source Audio, Music, and Speech Generation Toolkit.
* [Nendo](https://github.com/okio-ai/nendo) - The Nendo AI Audio Tool Suite.
* [Stable Audio](https://www.stableaudio.com/) - Fast Timing-Conditioned Latent Audio Diffusion.
* [WavJourney](https://github.com/Audio-AGI/WavJourney) - Compositional Audio Creation with Large Language Models.
* [Audiocraft](https://github.com/facebookresearch/audiocraft) - Audiocraft is a PyTorch library for deep learning research on audio generation.
* [vschaos2](https://github.com/acids-ircam/vschaos2) - vschaos2: vintage neural audio synthesis. 
* [Neural Resonator](https://github.com/rodrigodzf/neuralresonator) - Rigid-Body Sound Synthesis with Differentiable Modal Resonators.
* [SoundStorm](https://google-research.github.io/seanet/soundstorm/examples/) - SoundStorm: Efficient Parallel Audio Generation.
* [SpeechGPT](https://github.com/0nutation/SpeechGPT) - SpeechGPT: Empowering Large Language Models with Intrinsic Cross-Modal Conversational Abilities.
* [CLAPSpeech](https://clapspeech.github.io/) - CLAPSpeech: Learning Prosody from Text Context with Contrastive Language-Audio Pre-Training. 
* [AudioGPT](https://github.com/AIGC-Audio/AudioGPT) - AudioGPT: Understanding and Generating Speech, Music, Sound, and Talking Head. 
* [Bark](https://github.com/suno-ai/bark) - Bark is a transformer-based text-to-audio model created by Suno. Bark can generate highly realistic, multilingual speech as well as other audio - including music, background noise and simple sound effects. 
* [TANGO](https://github.com/declare-lab/tango) - TANGO is a latent diffusion model (LDM) for text-to-audio (TTA) generation. TANGO can generate realistic audios including human sounds, animal sounds, natural and artificial sounds and sound effects from textual prompts.  
* [ArchiSound](https://github.com/archinetai/audio-diffusion-pytorch) - Audio generation using diffusion models, in PyTorch.
* [WaveGAN](https://github.com/chrisdonahue/wavegan) - WaveGAN: Learn to synthesize raw audio with generative adversarial networks.
* [NeuralSound](https://github.com/hellojxt/NeuralSound) - Learning-based Modal Sound Synthesis with Acoustic Transfer.
* [RAVE](https://github.com/acids-ircam/RAVE) - RAVE: Realtime Audio Variational autoEncoder. A variational autoencoder for fast and high-quality neural audio synthesis.
* [AudioLDM](https://audioldm.github.io/) - AudioLDM: Text-to-Audio Generation with Latent Diffusion Models.
* [Make-An-Audio](https://text-to-audio.github.io/) - Make-An-Audio: Text-To-Audio Generation with Prompt-Enhanced Diffusion Models.
* [Make-An-Audio 3](https://github.com/Text-to-Audio/Make-An-Audio-3) - Make-An-Audio 3: Transforming Text into Audio via Flow-based Large Diffusion Transformers.
* [Moûsai](https://anonymous0.notion.site/anonymous0/Mo-sai-Text-to-Audio-with-Long-Context-Latent-Diffusion-b43dbc71caf94b5898f9e8de714ab5dc) - Moûsai: Text-to-Audio with Long-Context Latent Diffusion.
* [Im2Wav](https://github.com/RoySheffer/im2wav) - Image Guided Audio Generation. We propose Im2Wav, an image guided open-domain audio generation system. Given an input image or a sequence of images, Im2Wav generates a semantically relevant sound.
* [Oobleck](https://github.com/Harmonai-org/oobleck) - open soundstream-ish VAE codecs for downstream neural audio synthesis.
* [USS](https://github.com/bytedance/uss) - This is the PyTorch implementation of the Universal Source Separation with Weakly labelled Data. The USS system can automatically detect and separate sound classes from a real recording. The USS system can separate up to hundreds of sound classes sound classes in a hierarchical ontology structure. 
* [Diffusers](https://github.com/huggingface/diffusers) - 🤗 Diffusers is the go-to library for state-of-the-art pretrained diffusion models for generating images, audio, and even 3D structures of molecules.
* [ONE-PEACE](https://github.com/OFA-Sys/ONE-PEACE) - A general representation modal across vision, audio, language modalities.
* [tiny-audio-diffusion](https://github.com/crlandsc/tiny-audio-diffusion) - This is a repository for generating short audio samples and training waveform diffusion models on a GPU with less than 2GB VRAM.
* [stable-audio-tools](https://github.com/Stability-AI/stable-audio-tools) - Generative models for conditional audio generation.
* [CTAG](https://github.com/PapayaResearch/ctag) - Creative Text-to-Audio Generation via Synthesizer Programming.
* [Audiogen Codec](https://github.com/AudiogenAI/agc) - A low compression 48khz stereo neural audio codec for general audio, optimizing for audio fidelity 🎵.
* [WavCraft](https://github.com/JinhuaLiang/WavCraft) - WavCraft is an AI agent for audio creation and editing.
* [FoleyCrafter](https://github.com/open-mmlab/FoleyCrafter) - FoleyCrafter: Bring Silent Videos to Life with Lifelike and Synchronized Sounds.

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>


### <span id="asp">Audio Signal Processing (ASP)</span>

* [SouPyX](https://github.com/Yuan-ManX/SouPyX) - SouPyX is a very colourful space for audio exploration, suitable for research and exploration in a variety of audio fields. In SouPyX you can carry out research and exploration in audio processing, sound synthesis, audio effects, spatial audio, audio visualisation, AI audio and much more.
* [SoundFile](https://pysoundfile.readthedocs.io/en/latest/) - SoundFile is an audio library based on libsndfile, CFFI and NumPy.
* [Audio DSPy](https://github.com/jatinchowdhury18/audio_dspy) - audio_dspy is a Python package for audio signal processing tools.
* [pyAudioDspTools](https://pyaudiodsptools.readthedocs.io/en/latest/#) - pyAudioDspTools is a python 3 package for manipulating audio by just using numpy.
* [wave](https://docs.python.org/3/library/wave.html) - The wave module provides a convenient interface to the WAV sound format. It does not support compression/decompression, but it does support mono/stereo.
* [FFmpeg](https://github.com/FFmpeg/FFmpeg) - FFmpeg is a collection of libraries and tools to process multimedia content such as audio, video, subtitles and related metadata.
* [Opus](https://github.com/xiph/opus) - Modern audio compression for the internet.
* [Pedalboard](https://github.com/spotify/pedalboard) - Pedalboard is a Python library for working with audio: reading, writing, adding effects, and more. It supports most popular audio file formats and a number of common audio effects out of the box, and also allows the use of VST3 and Audio Unit formats for third-party plugins.
* [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) - PyAudio provides [Python](http://www.python.org/) bindings for [PortAudio](http://www.portaudio.com/) v19, the cross-platform audio I/O library. With PyAudio, you can easily use Python to play and record audio on a variety of platforms, such as GNU/Linux, Microsoft Windows, and Apple macOS.
* [PortAudio](http://www.portaudio.com/) - PortAudio is a free, cross-platform, [open-source](http://www.portaudio.com/license.html), audio I/O library.  It lets you write simple audio programs in 'C' or C++ that will compile and run on many platforms including Windows, Macintosh OS X, and Unix (OSS/ALSA). It is intended to promote the exchange of audio software between developers on different platforms. Many [applications](http://www.portaudio.com/apps.html) use PortAudio for Audio I/O.
* [Pyo](https://github.com/belangeo/pyo) - pyo is a Python module written in C to help digital signal processing script creation.Python DSP module. With pyo, user will be able to include signal processing chains directly in Python scripts or projects, and to manipulate them in real time through the interpreter
* [tinytag](https://github.com/devsnd/tinytag) - tinytag is a library for reading music meta data of most common audio files in pure python. Read audio and music meta data and duration of MP3, OGG, OPUS, MP4, M4A, FLAC, WMA, Wave and AIFF files with python 2 or 3.
* [Friture](https://friture.org/) - **Friture** is an application to visualize and analyze live audio data in real-time. Friture displays audio data in several widgets, such as a scope, a spectrum analyzer, or a rolling 2D spectrogram.
* [sounddevice](https://pypi.org/project/sounddevice/) - This [Python](https://www.python.org/) module provides bindings for the [PortAudio](http://www.portaudio.com/) library and a few convenience functions to play and record [NumPy](https://numpy.org/) arrays containing audio signals.
* [Pydub](https://github.com/jiaaro/pydub) - Manipulate audio with a simple and easy high level interface.
* [NAudio](https://github.com/naudio/NAudio) - Audio and MIDI library for .NET.
* [SoundCard](https://soundcard.readthedocs.io/en/latest/) - SoundCard is a library for playing and recording audio without resorting to a CPython extension. Instead, it is implemented using the wonderful [CFFI](http://cffi.readthedocs.io/en/latest/) and the native audio libraries of Linux, Windows and macOS.
* [TarsosDSP](https://github.com/JorenSix/TarsosDSP) - TarsosDSP is a Java library for audio processing. Its aim is to provide an easy-to-use interface to practical music processing algorithms implemented, as simply as possible, in pure Java and without any other external dependencies.
* [Maximilian](https://github.com/micknoise/Maximilian) - Maximilian is a cross-platform and multi-target audio synthesis and signal processing library. It was written in C++ and provides bindings to Javascript. 
* [The Synthesis ToolKit in C++ (STK)](https://github.com/thestk/stk) - The Synthesis ToolKit in C++ (STK) is a set of open source audio signal processing and algorithmic synthesis classes written in the C++ programming language.
* [JUCE](https://github.com/juce-framework/JUCE) - JUCE is an open-source cross-platform C++ application framework for creating high quality desktop and mobile applications, including VST, VST3, AU, AUv3, AAX and LV2 audio plug-ins and plug-in hosts. JUCE can be easily integrated with existing projects via CMake, or can be used as a project generation tool via the [Projucer](https://juce.com/discover/projucer), which supports exporting projects for Xcode (macOS and iOS), Visual Studio, Android Studio, Code::Blocks and Linux Makefiles as well as containing a source code editor.
* [iPlug 2](https://github.com/iPlug2/iPlug2) - C++ Audio Plug-in Framework for desktop, mobile and web.
* [CHOC](https://github.com/Tracktion/choc) - A collection of header only classes, permissively licensed, to provide basic useful tasks with the bare-minimum of dependencies.
* [Q](https://cycfi.github.io/q/) - Q is a cross-platform C++ library for Audio Digital Signal Processing. Aptly named after the “Q factor”, a dimensionless parameter that describes the quality of a resonant circuit, the Q DSP Library is designed to be simple and elegant, as the simplicity of its name suggests, and efficient enough to run on small microcontrollers.
* [BasicDSP](https://github.com/trcwm/BasicDSP) - BasicDSP - A tool for processing audio / experimenting with signal processing.
* [DaisySP](https://github.com/electro-smith/DaisySP) - A Powerful, Open Source DSP Library in C++.
* [Speech Signal Processing Toolkit (SPTK)](http://sp-tk.sourceforge.net/) - The Speech Signal Processing Toolkit (SPTK) is a suite of speech signal processing tools for UNIX environments, e.g., LPC analysis, PARCOR analysis, LSP analysis, PARCOR synthesis filter, LSP synthesis filter, vector quantization techniques, and other extended versions of them.
* [eDSP](https://mohabouje.github.io/edsp-docs/) - *eDSP* (easy Digital Signal Processing) is a digital signal processing framework written in modern C++ that implements some of the common functions and algorithms frequently used in digital signal processing, audio engineering & telecommunications systems.
* [KFR](https://github.com/kfrlib/kfr) - KFR is an open source C++ DSP framework that focuses on high performance. Fast, modern C++ DSP framework, FFT, Sample Rate Conversion, FIR/IIR/Biquad Filters (SSE, AVX, AVX-512, ARM NEON).
* [MWEngine](https://github.com/igorski/MWEngine) - Audio engine and DSP for Android, written in C++ providing low latency performance within a musical context, while providing a Java/Kotlin API. Supports both OpenSL and AAudio.
* [LabSound](https://github.com/LabSound/LabSound) - LabSound is a C++ graph-based audio engine. The engine is packaged as a batteries-included static library meant for integration in many types of software: games, visualizers, interactive installations, live coding environments, VST plugins, audio editing/sequencing applications, and more.
* [Gist](https://github.com/adamstark/Gist) - Gist is a C++ based audio analysis library.
* [Realtime_PyAudio_FFT](https://github.com/aiXander/Realtime_PyAudio_FFT) - Realtime audio analysis in Python, using PyAudio and Numpy to extract and visualize FFT features from streaming audio.
* [Spectrum](https://github.com/cokelaer/spectrum) - Spectral Analysis in Python. Spectrum is a Python library that contains tools to estimate Power Spectral Densities based on Fourier transform, Parametric methods or eigenvalues analysis. The Fourier methods are based upon correlogram, periodogram and Welch estimates. Standard tapering windows (Hann, Hamming, Blackman) and more exotic ones are available (DPSS, Taylor, …).
* [tidstream](https://github.com/mitmedialab/tidstream) - Tools for generating and manipulating live Vorbis and Opus streams.
* [AudioTraits](https://github.com/Sidelobe/AudioTraits) - AudioTraits is an abstraction designed to make testing of audio processing more convenient and readable. An 'Audio Trait' analyzes a given audio signal (some or all of its channels) and checks for a certain property. The result of this check is boolean, which allows this to be easily integrated in any unit test framework.
* [genMDM Editor](https://github.com/2xAA/genmdm-editor) - A web-based interface for genMDM, a MIDI controller for the Sega Mega Drive and Genesis. Also supports Mega Drive MIDI Interface.
* [3DAudioVisualizers](https://github.com/TimArt/3DAudioVisualizers) - An OpenGL Audio Visualizer suite in C++ using JUCE for Audio and GUI. 
* [AudioStretchy](https://github.com/twardoch/audiostretchy) - AudioStretchy is a Python library that allows you to time-stretch audio signals without changing their pitch. 
* [SwiftAudio](https://github.com/doublesymmetry/SwiftAudioEx) - SwiftAudioEx is an iOS audio player written in Swift, making it simpler to work with audio playback from streams and files.
* [WaveTools](https://github.com/djehuti/WaveTools) - WaveTools is a framework for manipulating audio files; WAVE files (.wav) in particular.
* [SimplyCoreAudio](https://github.com/rnine/SimplyCoreAudio) - 🔊 A Swift framework that aims to make Core Audio use less tedious in macOS.
* [DPF](https://github.com/DISTRHO/DPF) - DISTRHO Plugin Framework. DPF is designed to make development of new plugins an easy and enjoyable task.
* [Neural Amp Modeler Plug-in](https://github.com/sdatkinson/NeuralAmpModelerPlugin) - A VST3/AudioUnit plug-in for Neural Amp Modeler, built with iPlug2.
* [lsp-dsp-lib](https://github.com/lsp-plugins/lsp-dsp-lib) - DSP library for signal processing.
* [Hip-Hop](https://github.com/lucianoiam/hiphop) - Library for writing audio plugins that run the UI in a web view. Based on DPF.
* [MGT-python](https://github.com/fourMs/MGT-python) - Musical Gestures Toolbox for Python.
* [ASP](https://github.com/TUIlmenauAMS/ASP) - Audio Signal Processing Python Tools.
* [TinyAudio](https://github.com/mrDIMAS/tinyaudio) - TinyAudio is a cross-platform audio output library.
* [pymixconsole](https://github.com/csteinmetz1/pymixconsole) - Headless multitrack mixing console in Python.
* [effects-plugin](https://github.com/elemaudio/effects-plugin) - An audio effects plugin template using Elementary and JUCE.
* [miniaudio](https://github.com/mackron/miniaudio) - Audio playback and capture library written in C, in a single source file.
* [AudioMass](https://github.com/pkalogiros/AudioMass) - Free full-featured web-based audio & waveform editing tool.
* [Universal Android Music Player Sample](https://github.com/android/uamp) - A sample audio app for Android.
* [jsfx](https://github.com/chkhld/jsfx) - A free collection of JS (JesuSonic) plugins for Reaper.
* [Fourier](https://github.com/calebzulawski/fourier) - Fast Fourier transforms (FFTs) in Rust.
* [ProtoFaust](https://github.com/mzuther/ProtoFaust) - DSP prototyping in Faust for the modular synthesizer VCV Rack.
* [Polar](https://github.com/sgmackie/Polar) - Audio engine for CUDA processing (Windows/Linux).
* [Audio-to-MIDI-converter](https://github.com/vaibhavnayel/Audio-to-MIDI-converter) - Program to detect pitch from wav files and write in time quantized MIDI.
* [AudioTSM](https://github.com/Muges/audiotsm) - AudioTSM is a python library for real-time audio time-scale modification procedures, i.e. algorithms that change the speed of an audio signal without changing its pitch.
* [Multi-Filter-Delay](https://github.com/lbros96/Multi-Filter-Delay) - An original digital audio effect programmed through Juce/C++.
* [convoLV2](https://github.com/x42/convoLV2) - convoLV2 is a LV2 plugin to convolve audio signals with zero latency.
* [Cloud Seed](https://github.com/ValdemarOrn/CloudSeed) - Cloud Seed is an algorithmic reverb plugin built in C# and C++ for emulating huge, endless spaces and modulated echoes.
* [Background Music](https://github.com/kyleneideck/BackgroundMusic) - Background Music, a macOS audio utility: automatically pause your music, set individual apps' volumes and record system audio.
* [audiowaveform](https://github.com/bbc/audiowaveform) - C++ program to generate waveform data and render waveform images from audio files.
* [Mutagen](https://github.com/quodlibet/mutagen) - Python module for handling audio metadata.
* [lewton](https://github.com/RustAudio/lewton) - Vorbis decoder written in pure Rust.
* [Hound](https://github.com/ruuda/hound) - A wav encoding and decoding library in Rust.
* [rodio](https://github.com/RustAudio/rodio) - Rust audio playback library.
* [CPAL](https://github.com/RustAudio/cpal) - Cross-platform audio I/O library in pure Rust.
* [CSCore](https://github.com/filoe/cscore) - CSCore is a free .NET audio library which is completely written in C#.
* [TinyOSC](https://github.com/mhroth/tinyosc) - A minimal Open Sound Control (OSC) library written in vanilla C.
* [TinyWav](https://github.com/mhroth/tinywav) - A minimal C library for reading and writing (16b-int & 32b-float) WAV audio files.
* [JAsioHost](https://github.com/mhroth/jasiohost) - A Java-based (Audio Stream Input/Output) ASIO host.
* [PyWavelets](https://github.com/PyWavelets/pywt) - PyWavelets is a free Open Source library for wavelet transforms in Python. Wavelets are mathematical basis functions that are localized in both time and frequency.
* [ChowMultiTool](https://github.com/Chowdhury-DSP/ChowMultiTool) - Multi-Tool Audio Plugin.
* [RE201models](https://github.com/je3928/RE201models) - Digital models of the Roland RE201. VST3, AU plugins and source code.
* [RtAudio](https://github.com/thestk/rtaudio) - A set of C++ classes that provide a common API for realtime audio input/output across Linux (native ALSA, JACK, PulseAudio and OSS), Macintosh OS X (CoreAudio and JACK), and Windows (DirectSound, ASIO, and WASAPI) operating systems.
* [RtAudio-rs](https://github.com/BillyDM/rtaudio-rs) - Safe Rust wrapper and bindings to RtAudio.
* [PFFFT](https://github.com/marton78/pffft) - A pretty fast FFT and fast convolution with PFFASTCONV.
* [SHAART](https://github.com/drscotthawley/SHAART) - SHAART is a Python-based audio analysis toolkit, for educational purposes.
* [TD-JUCE](https://github.com/DBraun/TD-JUCE) - JUCE audio and VSTs in TouchDesigner.
* [JIVE](https://github.com/ImJimmi/JIVE) - JIVE is a bundle of JUCE modules centered around the desire to have a more modern approach to UI development.
* [Amplituda](https://github.com/lincollincol/Amplituda) - Amplituda - an android library based on FFMPEG which process audio file and provide an array of samples.
* [TagLib](https://github.com/taglib/taglib) - TagLib Audio Meta-Data Library.
* [speexdsp](https://github.com/xiongyihui/speexdsp-python) - Speex Echo Canceller Python Library.
* [PyPam](https://github.com/lifewatch/pypam) - Python Passive Acoustic Analysis tool for Passive Acoustic Monitoring (PAM).
* [AudioTools](https://github.com/descriptinc/audiotools) - Object-oriented handling of audio data, with GPU-powered augmentations, and more.
* [Equalize It](https://github.com/SmEgDm/equalize_it) - The project is VST-plugin for equalization. The user interface includes a spectrum analyzer, a filter control panel, frequency response curves, and level meters.
* [JDSP4Linux](https://github.com/Audio4Linux/JDSP4Linux) - An audio effect processor for PipeWire and PulseAudio clients.
* [FIRconv](https://github.com/davircarvalho/FIRconv) - Python implementations of Finite Impulse Response (FIR) filters.
* [OpenDSP](https://github.com/midilab/opendsp) - Headless Linux embedded realtime OS for audio and video DSP.
* [ultralight-juce](https://github.com/maxgraf96/ultralight-juce) - Integrating the Ultralight C++/HTML renderer with JUCE for prettier UIs.
* [Vult](https://github.com/vult-dsp/vult) - Vult is specially useful when programming Digital Signal Processing (DSP) algorithms like audio effects or synthesizers.
* [CloudSeed [JUCE]](https://github.com/njazz/cloudseed-juce) - JUCE-based UI for CloudSeed VST plugin.
* [TFliteTemplatePlugin](https://github.com/domenicostefani/TFlite-VSTplugin-template) - JUCE Template plugins to use TensorFlow lite for deep learning inference.
* [DrumFixer](https://github.com/jatinchowdhury18/DrumFixer) - DrumFixer is an audio plugin designed to help mixing engineers achieve better sounding drums.
* [BasicAudioPlayer](https://github.com/fabiovinotti/BasicAudioPlayer) - A Swift library that makes it easier to create AVAudioEngine-based audio players.
* [PLAudioMixer](https://github.com/PatrickSCLin/PLAudioMixer) - Simple audio mixer based on AVAudioEngine offline rendering mode.
* [estratto](https://github.com/AmberJBlue/estratto) - Estratto is a powerful and user-friendly Rust library designed for extracting rich audio features from digital audio signals.
* [vampy](https://github.com/c4dm/vampy) - A wrapper allowing Vamp audio analysis plugins to be written in Python.
* [SoundWave](https://github.com/bastienFalcou/SoundWave) - SoundWave is a customizable view representing sounds over time.
* [PyAV](https://github.com/PyAV-Org/PyAV) - PyAV is a Pythonic binding for the FFmpeg libraries.
* [audio-dsp](https://github.com/prayash/audio-dsp) - 🎧 Playing around with audio plugin development + DSP.
* [openSMILE](https://github.com/audeering/opensmile) - openSMILE (open-source Speech and Music Interpretation by Large-space Extraction) is a complete and open-source toolkit for audio analysis, processing and classification especially targeted at speech and music applications.
* [Carla](https://github.com/falkTX/Carla) - Carla is a fully-featured audio plugin host, with support for many audio drivers and plugin formats.
* [JUCE-HEAVY](https://github.com/o-g-sus/JUCE-HEAVY) - Template JUCE Project showing how to connect JUCE with Heavy C++ (HVCC) generated Source files.
* [Dplug](https://github.com/AuburnSounds/Dplug) - Audio plugin framework. VST2/VST3/AU/AAX/LV2 for Linux/macOS/Windows.
* [DAWNet](https://github.com/shiehn/dawnet_client) - The DAWNet is a DAW(digit audio workstation) plugin that connects to a remote Google Colab or Script.
* [Fish Audio Preprocessor](https://github.com/fishaudio/audio-preprocess) - Preprocess Audio for training.
* [clap-validator](https://github.com/free-audio/clap-validator) - An automatic CLAP validation and testing tool.
* [DSP Testbench](https://github.com/AndrewJJ/DSP-Testbench) - A DSP Testbench for users of the JUCE framework.
* [Coupler](https://github.com/coupler-rs/coupler) - Coupler is a framework for writing audio plugins in Rust. It currently supports the VST3 and CLAP APIs, with plans to support AUv2 and AAX in the near future.
* [PyOgg](https://github.com/TeamPyOgg/PyOgg) - PyOgg provides Python bindings for Xiph.org’s Opus, Vorbis and FLAC audio file formats as well as their Ogg container format.
* [streamlit-audiorecorder](https://github.com/theevann/streamlit-audiorecorder) - An audio Recorder for streamlit.
* [DtBlkFx](https://github.com/dozius/DtBlkFx) - DtBlkFx is a Fast-Fourier-Transform (FFT) based VST plug-in.
* [Smartelectronix](https://github.com/bdejong/smartelectronix) - Open source versions of all bram @ smartelectronix plugins.
* [Cookiejuce](https://github.com/madskjeldgaard/Cookiejuce) - A command line tool for generating modern JUCE projects with CMake.
* [auglib](https://github.com/audeering/auglib) - auglib is an augmentation library, which provides transforms to modify audio signals and files.
* [klang](https://github.com/nashaudio/klang) - klang is a language for the design and development of realtime audio processes in C++.

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>


### <span id="ss">Sound Synthesis (SS)</span>

* [Csound](https://csound.com/) - Csound is a sound and music computing system which was originally developed by Barry Vercoe in 1985 at MIT Media Lab. Since the 90s, it has been developed by a group of core developers.
* [Pure Data](https://puredata.info/) - **Pure Data** ( **Pd** ) is a [visual programming language](https://en.wikipedia.org/wiki/Visual_programming_language "Visual programming language") developed by [Miller Puckette](https://en.wikipedia.org/wiki/Miller_Puckette "Miller Puckette") in the 1990s for creating [interactive](https://en.wikipedia.org/wiki/Interaction "Interaction") [computer music](https://en.wikipedia.org/wiki/Computer_music "Computer music") and [multimedia](https://en.wikipedia.org/wiki/Multimedia "Multimedia") works. While Puckette is the main author of the program, Pd is an [open-source](https://en.wikipedia.org/wiki/Open-source_software "Open-source software") project with a large developer base working on new extensions. It is released under [BSD-3-Clause](https://en.wikipedia.org/wiki/BSD_licenses "BSD licenses"). It runs on [Linux](https://en.wikipedia.org/wiki/Linux "Linux"), [MacOS](https://en.wikipedia.org/wiki/MacOS "MacOS"), [iOS](https://en.wikipedia.org/wiki/IOS "IOS"), [Android](https://en.wikipedia.org/wiki/Android_(operating_system)) "Android (operating system)") and [Windows](https://en.wikipedia.org/wiki/Windows "Windows"). Ports exist for [FreeBSD](https://en.wikipedia.org/wiki/FreeBSD "FreeBSD") and [IRIX](https://en.wikipedia.org/wiki/IRIX "IRIX").
* [plugdata](https://plugdata.org/) - A visual programming environment for audio experimentation, prototyping and education.
* [Max/MSP/Jitter](https://cycling74.com/) - **Max** , also known as Max/MSP/Jitter, is a [visual programming language](https://en.wikipedia.org/wiki/Visual_programming_language "Visual programming language") for [music](https://en.wikipedia.org/wiki/Music "Music") and [multimedia](https://en.wikipedia.org/wiki/Multimedia "Multimedia") developed and maintained by [San Francisco](https://en.wikipedia.org/wiki/San_Francisco "San Francisco")-based software company [Cycling &#39;74](https://en.wikipedia.org/wiki/Cycling_%2774 "Cycling '74"). Over its more than thirty-year history, it has been used by composers, performers, software designers, researchers, and artists to create recordings, performances, and installations.
* [Kyma (sound design language)](https://kyma.symbolicsound.com/) - **Kyma** is a visual programming language for sound design used by musicians, researchers, and sound designers. In Kyma, a user programs a multiprocessor DSP by graphically connecting modules on the screen of a [Macintosh](https://en.wikipedia.org/wiki/Macintosh "Macintosh") or [Windows](https://en.wikipedia.org/wiki/Microsoft_Windows "Microsoft Windows") computer.
* [SuperCollider](https://supercollider.github.io/) - **SuperCollider** is a platform for audio synthesis and algorithmic composition, used by musicians, artists, and researchers working with sound. An audio server, programming language, and IDE for sound synthesis and algorithmic composition.
* [Sonic Pi](https://sonic-pi.net/) - **Sonic Pi** is a [live coding](https://en.wikipedia.org/wiki/Live_coding "Live coding") environment based on [Ruby](https://en.wikipedia.org/wiki/Ruby_(programming_language)) "Ruby (programming language)"), originally designed to support both computing and music lessons in schools, developed by Sam Aaron in the [University of Cambridge Computer Laboratory](https://en.wikipedia.org/wiki/Computer_Laboratory,_University_of_Cambridge "Computer Laboratory, University of Cambridge") in collaboration with [Raspberry Pi Foundation](https://en.wikipedia.org/wiki/Raspberry_Pi_Foundation "Raspberry Pi Foundation").
* [Reaktor](https://en.wikipedia.org/wiki/Reaktor) - **Reaktor** is a graphical [modular software music studio](https://en.wikipedia.org/wiki/Modular_software_music_studio "Modular software music studio") developed by [Native Instruments](https://en.wikipedia.org/wiki/Native_Instruments "Native Instruments") (NI). It allows musicians and sound specialists to design and build their own instruments, [samplers](https://en.wikipedia.org/wiki/Sampler_(musical_instrument)) "Sampler (musical instrument)"), effects and sound design tools. It is supplied with many ready-to-use instruments and effects, from emulations of classic [synthesizers](https://en.wikipedia.org/wiki/Synthesizer "Synthesizer") to futuristic sound design tools.
* [RTcmix](http://rtcmix.org/) - **RTcmix** is a real-time software "language" for doing digital sound synthesis and signal-processing. It is written in C/C++, and is distributed open-source, free of charge.
* [ChucK](https://chuck.stanford.edu/) - ChucK is a programming language for real-time sound synthesis and music creation. ChucK offers a unique time-based, concurrent programming model that is precise and expressive (we call this strongly-timed), dynamic control rates, and the ability to add and modify code on-the-fly. In addition, ChucK supports MIDI, OpenSoundControl, HID device, and multi-channel audio. It is open-source and freely available on MacOS X, Windows, and Linux. It's fun and easy to learn, and offers composers, researchers, and performers a powerful programming tool for building and experimenting with complex audio synthesis/analysis programs, and real-time interactive music.
* [Faust](https://faust.grame.fr/) - Faust (Functional Audio Stream) is a functional programming language for sound synthesis and audio processing with a strong focus on the design of synthesizers, musical instruments, audio effects, etc. Faust targets high-performance signal processing applications and audio plug-ins for a variety of platforms and standards.
* [SOUL](https://soul.dev/) - The SOUL programming language and API. SOUL (SOUnd Language) is an attempt to modernise and optimise the way high-performance, low-latency audio code is written and executed.
* [Cmajor](https://cmajor.dev/) - Cmajor is a programming language for writing fast, portable audio software. You've heard of C, C++, C#, objective-C... well, C*major* is a C-family language designed specifically for writing DSP signal processing code.
* [VCV Rack](https://github.com/VCVRack/Rack) - Rack is the host application for the VCV virtual Eurorack modular synthesizer platform.
* [Gwion](https://github.com/Gwion/Gwion) - Gwion is a programming language, aimed at making music. **strongly** inspired by [ChucK](http://chuck.stanford.edu/), but adding a bunch *high-level* features; templating, first-class functions and more. It aims to be simple, small, [fast](https://gwion.github.io/Gwion/#Benchmarks/), [extendable](https://github.com/Gwion/Gwion-plug) and [embeddable](https://github.com/Gwion/Gwion/blob/master/src/main.c#L18-L31).
* [Elementary Audio](https://www.elementary.audio/) - Elementary is a JavaScript framework and high performance audio engine that helps you build quickly and ship confidently. Declarative, functional framework for writing audio software on the web or for native apps.
* [Elementary](https://github.com/elemaudio/elementary) - Elementary is a JavaScript/C++ library for building audio applications.
* [Sound2Synth](https://github.com/Sound2Synth/Sound2Synth) - Sound2Synth: Interpreting Sound via FM Synthesizer Parameters Estimation.
* [JSyn](http://www.softsynth.com/jsyn/) - JSyn is a modular audio synthesizer for Java by Phil Burk. JSyn allows you to [develop](http://www.softsynth.com/jsyn/developers/) interactive computer music programs in Java. It can be used to generate sound effects, audio environments, or music. JSyn is based on the traditional model of unit generators which can be connected together to form complex sounds.
* [SynthAX](https://github.com/PapayaResearch/synthax) - A Fast Modular Synthesizer in JAX ⚡️Accelerating audio synthesis far beyond realtime speeds has a significant role to play in advancing intelligent audio production techniques. SynthAX is a fast virtual modular synthesizer written in JAX. At its peak, SynthAX generates audio over 60,000 times faster than realtime, and significantly faster than the state-of-the-art in accelerated sound synthesis.
* [Midica](http://www.midica.org/) - Midica is an interpreter for a Music Programming Language. It translates source code to MIDI. But it can also be used as a MIDI Player, MIDI compiler or decompiler, Karaoke Player, ALDA Player, ABC Player, LilyPond Player or a MIDI File Analyzer. You write music with one of the supported languages (MidicaPL, ALDA or ABC).
* [Mercury](https://www.timohoogland.com/mercury-livecoding/) - Mercury is a minimal and human-readable language for the live coding of algorithmic electronic music. All elements of the language are designed around making code more accessible and less obfuscating for the audience. This motivation stretches down to the coding style itself which uses clear descriptive names for functions and a clear syntax.
* [Alda](https://alda.io/) - Alda is a text-based programming language for music composition. It allows you to write and play back music using only a text editor and the command line. The language’s design equally favors aesthetics, flexibility and ease of use.
* [Platonic Music Engine](https://www.platonicmusicengine.com/) - The *Platonic Music Engine* is an attempt to create computer algorithms that superficially simulate the entirety of creative human culture, past, present, and future. It does so in an interactive manner allowing the user to choose various parameters and settings such that the final result will be unique to the user while still preserving the cultural idea that inspired the work.
* [pyo-tools](https://github.com/belangeo/pyo-tools) - Repository of ready-to-use python classes for building audio effects and synths with pyo.
* [py-modular](https://py-modular.readthedocs.io/en/latest/) - Modular and experimental audio programming framework for Python. py-modular is a small, experimental audio programming environment for python. It is intended to be a base for exploration of new audio technologies and workflows. Most everything in py-modular is built around a node-based workflow, meaning small classes do small tasks and can be patched together to create full synthesizers or larger ideas.
* [Bach: Automated Composer&#39;s Helper ](https://www.bachproject.net/) - a cross-platform set of patches and externals for Max, aimed to bring the richness of computer-aided composition into the real-time world.
* [AudioKit](https://github.com/AudioKit/AudioKit) - AudioKit is an audio synthesis, processing, and analysis platform for iOS, macOS (including Catalyst), and tvOS.
* [Twang](https://github.com/AldaronLau/twang) - Library for pure Rust advanced audio synthesis.
* [Gensound](https://github.com/Quefumas/gensound) - Pythonic audio processing and generation framework. The Python way to audio processing & synthesis.
* [OTTO](https://bitfieldaudio.com/) - The OTTO is a digital hardware groovebox, with synths, samplers, effects and a sequencer with an audio looper. The interface is flat, modular and easy to use, but most of all, it aims to encourage experimentation.
* [Loris](https://github.com/tractal/loris) - Loris is a library for sound analysis, synthesis, and morphing, developed by Kelly Fitz and Lippold Haken at the CERL Sound Group. Loris includes a C++ class library, Python module, C-linkable interface, command line utilities, and documentation.
* [IanniX](https://www.iannix.org/fr/) - IanniX is a graphical open-source sequencer, based on Iannis Xenakis works, for digital art. IanniX syncs via Open Sound Control (OSC) events and curves to your real-time environment.
* [Leipzig](https://github.com/ctford/leipzig) - A music composition library for Clojure and Clojurescript.
* [Nyquist](https://www.cs.cmu.edu/~music/nyquist/) - Nyquist is a sound synthesis and composition language offering a Lisp syntax as well as an imperative language syntax and a powerful integrated development environment.. Nyquist is an elegant and powerful system based on functional programming.
* [OpenMusic (OM)](http://repmus.ircam.fr/openmusic/home) - OpenMusic (OM) is a visual programming language based on [Lisp](http://www.gigamonkeys.com/book/introduction-why-lisp.html "http://www.gigamonkeys.com/book/introduction-why-lisp.html"). Visual programs are created by assembling and connecting icons representing functions and data structures. Most programming and operations are performed by dragging an icon from a particular place and dropping it to an other place. Built-in visual control structures (e.g. loops) are provided, that interface with Lisp ones. Existing CommonLisp/CLOS code can easily be used in OM, and new code can be developed in a visual way.
* [ORCΛ](https://github.com/hundredrabbits/Orca) - Orca is an [esoteric programming language](https://en.wikipedia.org/wiki/Esoteric_programming_language) designed to quickly create procedural sequencers, in which every letter of the alphabet is an operation, where lowercase letters operate on bang, uppercase letters operate each frame.
* [Overtone](http://overtone.github.io/) - Overtone is an open source audio environment designed to explore new musical ideas from synthesis and sampling to instrument building, live-coding and collaborative jamming. We combine the powerful [SuperCollider](http://supercollider.github.io/) audio engine, with [Clojure](http://clojure.org/), a state of-the-art lisp, to create an intoxicating interactive sonic experience.
* [SEAM](https://grammaton.gitbook.io/seam/) - Sustained Electro-Acoustic Music - Base. *Sustained Electro-Acoustic Music* is a project inspired by [Alvise Vidolin and Nicola Bernardini](https://www.academia.edu/16348988/Sustainable_live_electro-acoustic_music).
* [Glicol](https://glicol.org/) - Glicol (an acronym for "graph-oriented live coding language") is a computer music language with both its language and audio engine written in [Rust programming language](https://www.rust-lang.org/), a modern alternative to C/C++. Given this low-level nature, Glicol can run on many different platforms such as browsers, VST plugins and Bela board. Glicol's synth-like syntax and powerful audio engine also make it possible to combine high-level synth or sequencer control with low-level sample-accurate audio synthesis, all in real-time.
* [PaperSynth](https://github.com/Ashvala/PaperSynth) - Handwritten text to synths! PaperSynth is a project that aims to read keywords you've written on a piece of paper and convert it into synthesizers you can play on the phone.
* [Neural Resonator VST](https://github.com/rodrigodzf/NeuralResonatorVST) - This is a VST plugin that uses a neural network to generate filters based on arbitrary 2D shapes and materials. It is possible to use midi to trigger simple impulses to excite these filters. Additionally any audio signal can be used as input to the filters.
* [Scyclone](https://github.com/Torsion-Audio/Scyclone) - Scyclone is an audio plugin that utilizes neural timbre transfer technology to offer a new approach to audio production. The plugin builds upon RAVE methodology, a realtime audio variational auto encoder, facilitating neural timbre transfer in both single and couple inference mode.
* [mlinmax](https://github.com/estine/mlinmax) - ML for sound generation and processing in Cycling '74's Max programming language.
* [ADLplug](https://github.com/jpcima/ADLplug) - FM Chip Synthesizer — OPL & OPN — VST/LV2/Standalone.
* [Surge](https://github.com/surge-synthesizer/surge) - Synthesizer plug-in (previously released as Vember Audio Surge). 
* [cStop](https://github.com/calgoheen/cStop) - cStop is a tape stop audio effect plugin available in AU & VST3 for Mac (Windows coming soon).
* [CompuFart](https://github.com/alexmfink/compufart) - Fart sound synthesizer and algorithm in Cmajor.
* [py-js](https://github.com/shakfu/py-js) - Python3 externals for Max / MSP.
* [pd-lua](https://github.com/agraef/pd-lua) - Lua bindings for Pd, updated for Lua 5.3+.
* [Live 4 Life](https://github.com/Xon77/Live4Life) - A spatial performance tool for SuperCollider.
* [CaesarLooper](https://github.com/X2theL/CaesarLooper) - CaesarLooper is a SuperCollider clone of the Augustus Loop VST plugin by Expert Sleepers.
* [Dexed](https://github.com/asb2m10/dexed) - DX7 FM multi plaform/multi format plugin.
* [Leapmotion For Max](https://github.com/JulesFrancoise/leapmotion-for-max) - Leapmotion external for Cycling'74 Max.
* [Kontakt-Public](https://github.com/Yaron-NI/Kontakt-Public) - Resources for Native Instruments Kontakt builders.
* [PyLive](https://github.com/ideoforms/pylive) - Query and control Ableton Live from Python.
* [ml-lib](https://github.com/irllabs/ml-lib) - A machine learning library for Max and Pure Data.
* [ZenGarden](https://github.com/mhroth/ZenGarden) - ZenGarden is a stand-alone library for running Pure Data patches.
* [Max-SDK](https://github.com/Cycling74/max-sdk) - Software Development Kit for Max by Cycling '74.
* [pd-hvcc](https://github.com/timothyschoen/pd-hvcc) - Creating a gen~-like environment for Pd, based on the Heavy compiler.
* [Kuroscillators](https://github.com/nolanlem/Kuroscillators) - MAX/MSP objects for audio and rhythmic synthesis using networks of coupled oscillators.
* [ascii-audio](https://github.com/kylophone/ascii-audio) - Generates PCM audio from an ASCII string. Text is visible on the spectrogram image.
* [BelaMiniMoogEmulation](https://github.com/lbros96/BelaMiniMoogEmulation) - A digital implementation of the Minimoog analog synthesizer with anti-aliased waveforms and a recreation of the moog ladder filter.
* [Edisyn](https://github.com/eclab/edisyn) - Synthesizer Patch Editor.
* [soundgen](https://github.com/tatters/soundgen) - R package for sound synthesis and acoustic analysis.
* [Cardinal](https://github.com/DISTRHO/Cardinal) - Virtual modular synthesizer plugin.
* [Flutter Echo Modeling](https://github.com/gdalsanto/flutter-echo-modeling) - This repository presents a Matlab demo for the synthesis of flutter echo.
* [OOPS](https://github.com/mulshine/OOPS) - OOPS is now LEAF! A C library for Audio synthesis and processing, intended for embedded applications, written using semi-OOP style.
* [Sonic Pi Tool](https://github.com/emlyn/sonic-pi-tool) - 🎻 Controlling Sonic Pi from the command line, in Python.
* [sonicpi.vim](https://github.com/dermusikman/sonicpi.vim) - Sonic Pi plugin for Vim.
* [Controlled-Chaos](https://github.com/JLenzy/Controlled-Chaos) - Max4Live Euclidian Rhythm Generator.
* [KPStrong](https://github.com/JLenzy/KPStrong) - This is an implementation of a strummed Karplus-Strong synth, which runs as C++ in real-time on the Bela hardware.
* [nn_tilde](https://github.com/acids-ircam/nn_tilde) - A max / Pd external for real-time ai audio processing.
* [gRainbow](https://github.com/bboettcher3/gRainbow) - A synthesizer that uses pitch detection to choose candidates for granular synthesis or sampling.
* [SignalFlow](https://github.com/ideoforms/signalflow) - A sound synthesis framework for Python, designed for clear and concise expression of complex musical ideas.
* [Syntheon](https://github.com/gudgud96/syntheon) - Parameter inference of music synthesizers to simplify sound design process. Supports Vital and Dexed.
* [RnboJuceTemplate](https://github.com/mikegazzaruso/RnboJuceTemplate) - A JUCE Template including a minimal synthesizer created with MaxMSP's rnbo~, that encapsulates rnboObject's state into JUCE's AudioProcessor using modern AudioProcessorTreeValueState fashion.
* [FluidSynth.clap](https://github.com/cannerycoders/fluidsynth.clap) - A clap-plugin bridge to fluidsynth.
* [LaunchpadX](https://github.com/madskjeldgaard/launchpadx-sc) - A Simple SuperCollider interface for the Novation LaunchpadX controller.
* [Faug](https://github.com/t2techno/Faug) - A Minimoog Model D emulation with the DSP portion written in Faust. Moog + Faust = Faug.
* [blocks](https://github.com/dan-german/blocks) - blocks is a modular synthesizer available as standalone, VST3 & AU for Windows and macOS.
* [Bessel's Trick](https://github.com/fcaspe/BesselsTrick) - Bessel's Trick is a Neural Audio Plugin for fast, live Tone Transformation of Musical Instrument sounds using Frequency Modulation (FM) synthesis.

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>


### <span id="ga">Game Audio (GA)</span>

* [Chunity](https://github.com/ccrma/chunity) - ChucK in Unity. Plugin for using ChucK in Unity. Available on the Unity Asset Store.
* [Raveler](https://github.com/usdivad/Raveler) - Wwise plugin that runs RAVE models, enabling real-time timbre transfer via neural audio synthesis in a game audio setting.
* [LASP](https://github.com/keijiro/Lasp) - Low-latency Audio Signal Processing plugin for Unity.
* [pyreaper](https://github.com/r9y9/pyreaper) - A python wrapper for REAPER.
* [Reaper-Keys](https://github.com/gwatcha/reaper-keys) - vim-bindings for Reaper.
* [Reaper Tools](https://github.com/audiokinetic/Reaper-Tools) - Audiokinetic Reaper Tools Repository. Collection of extensions, scripts and tools for Reaper.
* [ReaWwise](https://github.com/audiokinetic/ReaWwise) - ReaWwise is a REAPER extension that sound designers can use to transfer audio files from REAPER into Wwise projects.
* [WWISER](https://github.com/bnnm/wwiser) - A Wwise .bnk parser, to assist in handling audio from games using the Wwise engine.
* [waapi-text-to-speech](https://github.com/decasteljau/waapi-text-to-speech) - Wwise text-to-speech integration using external editors.
* [jsfxr for Wwise](https://github.com/decasteljau/jsfxr-for-wwise) - jsfxr (ported from sfxr) with added Wwise connectivity, embedded into Electron.
* [SoLoud](https://github.com/jarikomppa/soloud) - SoLoud is an easy to use, free, portable c/c++ audio engine for games.
* [AudioToys](https://github.com/sgmackie/AudioToys) - DSP doodles for Unity.
* [Dolby.io Virtual World plugin for Unity](https://github.com/DolbyIO/comms-sdk-unity) - With the Dolby.io Virtual World plugin for Unity, you can easily integrate Dolby.io Spatial Audio, powered by Dolby Atmos technology into your virtual world applications.
* [Dolby.io Virtual Worlds plugin for Unreal Engine](https://github.com/DolbyIO/comms-sdk-unreal) - With the Dolby.io Virtual Worlds plugin for Unreal Engine, you can easily integrate Dolby.io Spatial Audio, powered by Dolby Atmos technology into your virtual world applications.
* [Engine Simulator](https://github.com/ange-yaghi/engine-sim) - Combustion engine simulator that generates realistic audio.
* [Jack Audio For Unity](https://github.com/rodrigodzf/Jack-Audio-For-Unity) - This library/plugin enables multichannel audio routing between Unity3D and JackAudio.
* [Voxel Plugin](https://github.com/Phyronnaz/VoxelPlugin) - Voxel Plugin allows to create fully volumetric, entirely destructible, infinite worlds in Unreal Engine. It is compatible with 4.24, 4.25, 4.26, 4.27 and Unreal 5.
* [REV Unity](https://github.com/CrankcaseAudio/CrankcaseAudioREVUnity) - REV Unity Tachometer Demo.
* [Unity Audio Manager (UAM)](https://github.com/MathewHDYT/Unity-Audio-Manager) - 🔊 Used to play/change/stop/mute/... one or multiple sounds at a certain circumstance or event in 2D and 3D simply via. code.
* [Audio-Manager-for-Unity](https://github.com/microsoft/Audio-Manager-for-Unity) - A tool for defining and executing audio behaviors in Unity in a node based editor.
* [Unity Wwise Addressables](https://github.com/audiokinetic/WwiseUnityAddressables) - This package adds support for distributing and loading Wwise assets using the Unity Addressables System.
* [rFXGen](https://github.com/raysan5/rfxgen) - A simple and easy-to-use fx sounds generator.
* [uLipSync](https://github.com/hecomi/uLipSync) - MFCC-based LipSync plug-in for Unity using Job System and Burst Compiler.
* [godot-fmod-integration](https://github.com/heraldofgargos/godot-fmod-integration) - FMOD Studio middleware integration and scripting API bindings for the Godot game engine.
* [FMOD Audio System](https://github.com/trevermock/fmod-audio-system) - Unity Audio System using FMOD.
* [ww2ogg](https://github.com/hcs64/ww2ogg) - Convert AudioKinetic Wwise RIFF/RIFX Vorbis to standard Ogg Vorbis.
* [Cavern](https://github.com/VoidXH/Cavern) - Object-based audio engine and codec pack with Dolby Atmos rendering, room correction, HRTF, one-click Unity audio takeover, and much more.
* [RNBO Unity Audio Plugin](https://github.com/Cycling74/rnbo.unity.audioplugin) - RNBO Adapter for Unity's Native Audio Plugin.
* [RNBO MetaSounds](https://github.com/Cycling74/RNBOMetasound) - RNBO adapter that implements metasound nodes.

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>


### <span id="daw">Digital Audio Workstation (DAW)</span>

* [Audacity](https://github.com/audacity/audacity) - Audacity is an easy-to-use, multi-track audio editor and recorder for Windows, macOS, GNU/Linux and other operating systems. 
* [Tracktion](https://github.com/Tracktion/tracktion_engine) - Tracktion is a cross-platform based open source audio workstation with an intuitive user interface and powerful audio editing and mixing functions.
* [Pro Tools Scripting SDK](https://developer.avid.com/audio/) - The Pro Tools Scripting SDK allows you to script Pro Tools using a language-independent API to create new automated workflows in Pro Tools. 
* [reapy](https://github.com/RomeoDespres/reapy) - A pythonic wrapper for REAPER's ReaScript Python API.
* [reaper-sdk](https://github.com/justinfrankel/reaper-sdk) - REAPER C/C++ extension SDK.
* [ReaScripts](https://github.com/X-Raym/REAPER-ReaScripts) - X-Raym's Free and Open Source Scripts for Cockos REAPER.
* [ReaScripts](https://github.com/Neutronic/ReaScripts) - Cockos REAPER scripts.
* [ReaBlink](https://github.com/ak5k/reablink) - REAPER plug-in extension providing ReaScript bindings for Ableton Link session, and Ableton Link Test Plan compliant implementations for REAPER. 
* [voodoohop-ableton-tools](https://github.com/voodoohop/voodoohop-ableton-tools) - Ableton Live Harmony and Tempo Tools. Augments Ableton Live with an intuitive visualization of musical harmony as well as allowing a track’s tempo dynamics to control the master tempo in real-time. 
* [AbletonParsing](https://github.com/DBraun/AbletonParsing) - Parse an Ableton ASD clip file (warp markers and more) in Python.
* [Ableton Push](https://github.com/garrensmith/abletonpush) - A library for working with the Ableton Push in the browser.
* [PyFLP](https://github.com/demberto/PyFLP) - FL Studio project file parser.
* [vst3sdk](https://github.com/steinbergmedia/vst3sdk) - VST 3 Plug-In SDK.
* [TuneFlow](https://github.com/tuneflow/tuneflow) - 🧠+🎧 Build your music algorithms and AI models with the next-gen DAW 🔥
* [tuneflow-py](https://github.com/tuneflow/tuneflow-py) - Tuneflow-py is the Python SDK of TuneFlow plugins.
* [so-vits-SVC Plugin for TuneFlow](https://github.com/tuneflow/so-vits-svc-plugin) - so-vits-svc as a TuneFlow plugin.
* [Radium](https://github.com/kmatheussen/radium) - A graphical music editor. A next generation tracker.
* [Bass Studio](https://github.com/nidefawl/bass-studio) - Bass Studio is a Digital Audio Workstation (DAW) written in C++. Windows, MacOS and Linux builds are provided. Both VST2 and CLAP plugin format are supported.
* [GridSound](https://github.com/gridsound/daw) - GridSound is a work-in-progress open-source digital audio workstation developed with HTML5 and more precisely with the new Web Audio API. 
* [Meadowlark](https://github.com/MeadowlarkDAW/Meadowlark) - Meadowlark is a (work in progress) FREE and open-source DAW (Digital Audio Workstation) for Linux, Mac and Windows. It aims to be a powerful recording, composing, editing, sound designing, mixing, and mastering tool for artists around the world, while also being intuitive and customizable.
* [Mixxx](https://github.com/mixxxdj/mixxx) - Mixxx is Free DJ software that gives you everything you need to perform live mixes.
* [Hybrid-DJ-Set](https://github.com/MikeMorenoDSP/Hybrid-DJ-Set) - Synchronize DJ software (Mixxx) with Pure Data for layering virtual instruments in a live performance.
* [LV2](https://github.com/lv2/lv2) - LV2 is a plugin standard for audio systems. It defines an extensible C API for plugins, and a format for self-contained "bundle" directories that contain plugins, metadata, and other resources.
* [Ardour](https://github.com/Ardour/ardour) - Record, Edit, and Mix on Linux, macOS and Windows.
* [LMMS](https://github.com/LMMS/lmms) - LMMS is a free cross-platform alternative to commercial programs like FL Studio®, which allow you to produce music with your computer. This includes the creation of melodies and beats, the synthesis and mixing of sounds, and arranging of samples. 
* [Qtractor](https://github.com/rncbc/qtractor) - Qtractor is an Audio/MIDI multi-track sequencer application written in C++ with the Qt framework. Target platform is Linux, where the Jack Audio Connection Kit (JACK) for audio, and the Advanced Linux Sound Architecture (ALSA) for MIDI, are the main infrastructures to evolve as a fairly-featured Linux desktop audio workstation GUI, specially dedicated to the personal home-studio.
* [smart-audio-mixer](https://github.com/kuouu/smart-audio-mixer) - A modern digital audio workstation(DAW) using C++/JUCE.
* [OpenVINO™ AI Plugins for Audacity](https://github.com/intel/openvino-plugins-ai-audacity) - A set of AI-enabled effects, generators, and analyzers for Audacity.
* [Jackdaw](https://github.com/chvolow24/jackdaw) - A stripped-down, keyboard-focused digital audio workstation (DAW) taking some design cues from non-linear video editors like Avid.
* [ossia score](https://github.com/ossia/score) - An intermedia sequencer supporting audio (VST, VST3, LV2, JSFX, etc.) as well as video and hardware control (OSC, MIDI, DMX, NDI, MQTT, CoAP, etc.) 

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>


### <span id="sa">Spatial Audio (SA)</span>

* [spaudiopy](https://spaudiopy.readthedocs.io/en/latest/index.html) - Spatial Audio Python Package. The focus (so far) is on spatial audio encoders and decoders. The package includes e.g. spherical harmonics processing and (binaural renderings of) loudspeaker decoders, such as VBAP and AllRAD.
* [Spatial_Audio_Framework (SAF)](https://leomccormack.github.io/Spatial_Audio_Framework/) - The Spatial_Audio_Framework (SAF) is an open-source and cross-platform framework for developing spatial audio related algorithms and software in C/C++. Originally intended as a resource for researchers in the field, the framework has gradually grown into a rather large and well-documented codebase comprising a number of distinct [**modules**](https://github.com/leomccormack/Spatial_Audio_Framework/blob/master/framework/modules); with each module targeting a specific sub-field of spatial audio (e.g. Ambisonics encoding/decoding, spherical array processing, amplitude-panning, HRIR processing, room simulation, etc.).
* [HO-SIRR](https://github.com/leomccormack/HO-SIRR) - Higher-order Spatial Impulse Response Rendering (HO-SIRR) is a rendering method, which can synthesise output loudspeaker array room impulse responses (RIRs) using input spherical harmonic (Ambisonic/B-Format) RIRs of arbitrary order. A MATLAB implementation of the Higher-order Spatial Impulse Response Rendering (HO-SIRR) algorithm; an alternative approach for reproducing Ambisonic RIRs over loudspeakers.
* [SpatGRIS](https://github.com/GRIS-UdeM/SpatGRIS) - SpatGRIS is a sound spatialization software that frees composers and sound designers from the constraints of real-world speaker setups. With the ControlGRIS plugin distributed with SpatGRIS, rich spatial trajectories can be composed directly in your DAW and reproduced in real-time on any speaker layout. It is fast, stable, cross-platform, easy to learn and works with the tools you already know. SpatGRIS supports any speaker setup, including 2D layouts like quad, 5.1 or octophonic rings, and 3D layouts like speaker domes, concert halls, theatres, etc. Projects can also be mixed down to stereo using a binaural head-related transfer function or simple stereo panning.
* [Steam Audio](https://github.com/ValveSoftware/steam-audio) - Steam Audio delivers a full-featured audio solution that integrates environment and listener simulation. HRTF significantly improves immersion in VR; physics-based sound propagation completes aural immersion by consistently recreating how sound interacts with the virtual environment.
* [SpatialAudioKit](https://spatialaudiokit.github.io/) - SpatialAudioKit is a Swift package to facilitate authoring of Spatial Audio apps on Apple platforms. 
* [libmysofa](https://github.com/hoene/libmysofa) - Reader for AES SOFA files to get better HRTFs.
* [Omnitone](https://googlechrome.github.io/omnitone/#home) - Omnitone: Spatial Audio Rendering on the Web. Omnitone is a robust implementation of [ambisonic](https://en.wikipedia.org/wiki/Ambisonics) decoding and binaural rendering written in Web Audio API. Its rendering process is powered by the fast native features from Web Audio API (GainNode and Convolver), ensuring the optimum performance. The implementation of Omnitone is based on the [Google spatial media](https://github.com/google/spatial-media) specification and [SADIE&#39;s binaural filters](https://www.york.ac.uk/sadie-project/GoogleVRSADIE.html). It also powers [Resonance Audio SDK](https://github.com/resonance-audio/resonance-audio-web-sdk) for web.
* [Mach1 Spatial](https://www.mach1.tech/) - Mach1 Spatial SDK includes APIs to allow developers to design applications that can encode or pan to a spatial audio render from audio streams and/or playback and decode Mach1Spatial 8channel spatial audio mixes with orientation to decode the correct stereo output sum of the user's current orientation. Additionally the Mach1 Spatial SDK allows users to safely convert surround/spatial audio mixes to and from the Mach1Spatial or Mach1Horizon **VVBP** formats.
* [SoundSpaces](https://github.com/facebookresearch/sound-spaces) - SoundSpaces is a realistic acoustic simulation platform for audio-visual embodied AI research. From audio-visual navigation, audio-visual exploration to echolocation and audio-visual floor plan reconstruction, this platform expands embodied vision research to a broader scope of topics.
* [Visual Acoustic Matching](https://github.com/facebookresearch/visual-acoustic-matching) - We introduce the visual acoustic matching task, in which an audio clip is transformed to sound like it was recorded in a target environment. Given an image of the target environment and a waveform for the source audio, the goal is to re-synthesize the audio to match the target room acoustics as suggested by its visible geometry and materials. 
* [FAST-RIR](https://github.com/anton-jeran/FAST-RIR) - This is the official implementation of our neural-network-based fast diffuse room impulse response generator (FAST-RIR) for generating room impulse responses (RIRs) for a given acoustic environment.
* [pygsound](https://github.com/GAMMA-UMD/pygsound) - Impulse response generation based on state-of-the-art geometric sound propagation engine.
* [RIRIS](https://github.com/eliaszea/RIRIS) - RIRIS is the MATLAB implementation of room impulse response interpolation using fast shearlet transforms.
* [parallel-reverb-raytracer](https://github.com/reuk/parallel-reverb-raytracer) - A raytracer for impulse responses (for reverb), influenced by raster graphics lighting techniques. 
* [Synth 3D](https://github.com/dafaronbi/Synth-3D) - VST Synthesizer with virtual oscillator objects placed in 3D space.
* [libBasicSOFA](https://github.com/superkittens/libBasicSOFA) - A very basic library for reading Spatially Oriented Format for Acoustics (SOFA) files, a format for storing HRTFs and/or BRIRs for binuaral audio reproduction.
* [Mesh2HRTF](https://github.com/Any2HRTF/Mesh2HRTF) - Open software for the numerical calculation of head-related transfer functions.
* [OpenAL Soft](https://github.com/kcat/openal-soft) - OpenAL Soft is a software implementation of the OpenAL 3D audio API.
* [soundscape_IR](https://github.com/meil-brcas-org/soundscape_IR) - soundscape_IR is a python-based toolbox of soundscape information retrieval, aiming to assist in the analysis of soundscape recordings.
* [Sounding Bodies](https://github.com/facebookresearch/SoundingBodies) - We present a model that can generate accurate 3D sound fields of human bodies from headset microphones and body pose as inputs.
* [Soundscapy](https://github.com/MitchellAcoustics/Soundscapy) - A python library for analysing and visualising soundscape assessments.
* [ambiX](https://github.com/kronihias/ambix) - cross-platform Ambisonic VST, LV2 plug-ins with variable order for use in Digital Audio Workstations like Reaper or Ardour or as Jack standalone applications.
* [HOAC](https://github.com/chris-hld/hoac) - Higher-Order Ambisonics Codec for Spatial Audio.
* [OpenSoundLab](https://github.com/ludzeller/OpenSoundLab) - OpenSoundLab (OSL) makes modular sound patching three dimensional in a mixed reality experience using Meta Quest's passthrough mode.
* [SEE-2-SOUND🔊](https://github.com/see2sound/see2sound) - Zero-Shot Spatial Environment-to-Spatial Sound.

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>


### <span id="wap">Web Audio Processing (WAP)</span>

* [WebRTC Audio Processing](https://github.com/xiongyihui/python-webrtc-audio-processing) - Python binding of WebRTC Audio Processing.
* [WebChucK](https://github.com/ccrma/webchuck) - WebChucK brings ChucK, a strongly-timed audio programming language, to the web! ChucK's C++ source code has been compiled down to WebAssembly (WASM) and runs via the AudioWorkletNode interface of the Web Audio API.
* [MIDI.js](https://galactic.ink/midi-js/) - 🎹 Making life easy to create a MIDI-app on the web. Includes a library to program synesthesia into your app for memory recognition or for creating trippy effects. Convert soundfonts for Guitar, Bass, Drums, ect. into code that can be read by the browser. **[MIDI.js](https://github.com/mudcube/MIDI.js)** ties together, and builds upon frameworks that bring MIDI to the browser. Combine it with [jasmid](https://github.com/gasman/jasmid) to create a web-radio MIDI stream similar to this demo, or with [Three.js](https://github.com/mrdoob/three.js/), [Sparks.js](https://github.com/zz85/sparks.js/), or [GLSL](http://glslsandbox.com/) to create Audio/visual experiments.
* [Web Voice Processor](https://github.com/Picovoice/web-voice-processor) - A library for real-time voice processing in web browsers.
* [Tone.js](https://tonejs.github.io/) - Tone.js is a Web Audio framework for creating interactive music in the browser. The architecture of Tone.js aims to be familiar to both musicians and audio programmers creating web-based audio applications. On the high-level, Tone offers common DAW (digital audio workstation) features like a global transport for synchronizing and scheduling events as well as prebuilt synths and effects. Additionally, Tone provides high-performance building blocks to create your own synthesizers, effects, and complex control signals.
* [audio.js](http://kolber.github.io/audiojs/) - audiojs is a drop-in javascript library that allows HTML5's `<audio>` tag to be used anywhere. It uses native `<audio>` where available and falls back to an invisible flash player to emulate it for other browsers. It also serves a consistent html player UI to all browsers which can be styled used standard css.
* [Peaks.js](https://github.com/bbc/peaks.js) - JavaScript UI component for interacting with audio waveforms.
* [howler.js](https://howlerjs.com/) - Javascript audio library for the modern web. howler.js makes working with audio in JavaScript easy and reliable across all platforms. [howler.js](https://howlerjs.com/) is an audio library for the modern web. It defaults to [Web Audio API](http://webaudio.github.io/web-audio-api/) and falls back to [HTML5 Audio](https://html.spec.whatwg.org/multipage/embedded-content.html#the-audio-element). This makes working with audio in JavaScript easy and reliable across all platforms.
* [CoffeeCollider](https://github.com/mohayonao/CoffeeCollider) - CoffeeCollider is a language for real time audio synthesis and algorithmic composition in HTML5. The concept of this project is designed as "write CoffeeScript, and be processed as SuperCollider."
* [pico.js](http://mohayonao.github.io/pico.js/) - Audio processor for the cross-platform.
* [timbre.js](http://mohayonao.github.io/timbre.js/) - Timbre.js provides a functional processing and synthesizing audio in your web apps with modern JavaScript's way like jQuery or node.js. It has many **T-Object** (formally: Timbre Object) that connected together to define the graph-based routing for overall audio rendering. It is a goal of this project to approach the next generation audio processing for web.
* [Rythm.js](https://okazari.github.io/Rythm.js/) - A javascript library that makes your page dance.
* [p5.sound](https://p5js.org/reference/#/libraries/p5.sound) - p5.sound extends p5 with [Web Audio](http://caniuse.com/audio-api) functionality including audio input, playback, analysis and synthesis.
* [WadJS](https://github.com/rserota/wad) - A Javascript library for manipulating audio. Web Audio DAW. Use the Web Audio API for dynamic sound synthesis. It's like jQuery for your ears.
* [Ableton.js](https://github.com/leolabs/ableton-js) - Ableton.js lets you control your instance or instances of Ableton using Node.js. It tries to cover as many functions as possible.
* [Sound.js](https://github.com/kittykatattack/sound.js) - "Sound.js" is micro-library that lets you load, play, and generate sound effects and music for games and interactive applications. It's very small: less than 800 lines of code and no dependencies. [Click here to try an interactive demo](https://cdn.rawgit.com/kittykatattack/sound.js/master/index.html). You can use it as-as, or integrate it into your existing framework.
* [tuna](https://github.com/Theodeus/tuna) - An audio effects library for the Web Audio API.
* [XSound](https://xsound.jp/) - XSound gives Web Developers Powerful Audio Features Easily !
* [Pizzicato](https://alemangui.github.io/pizzicato/) - A web audio Javascript library. Pizzicato aims to simplify the way you create and manipulate sounds via the Web Audio API. Take a look at the [demo site here](https://alemangui.github.io/pizzicato/). Library to simplify the way you create and manipulate sounds with the Web Audio API.
* [AudioMass](https://github.com/pkalogiros/AudioMass) - Free full-featured web-based audio & waveform editing tool.
* [WebPd](https://github.com/sebpiq/WebPd) - Run your Pure Data patches on the web. WebPd is a compiler for the Pure Data audio programming language allowing to run .pd patches in web pages.
* [DX7 Synth JS](https://github.com/mmontag/dx7-synth-js) - DX7 FM synthesis using the Web Audio and Web MIDI API. Works in Chrome and Firefox. Use a MIDI or QWERTY keyboard to play the synth.
* [WEBMIDI.js](https://github.com/djipco/webmidi) - WEBMIDI.js makes it easy to interact with MIDI instruments directly from a web browser or from Node.js. It simplifies the control of physical or virtual MIDI instruments with user-friendly functions such as playNote(), sendPitchBend() or sendControlChange(). It also allows reacting to inbound MIDI messages by adding listeners for events such as "noteon", "pitchbend" or "programchange".
* [web-audio-beat-detector](https://github.com/chrisguttandin/web-audio-beat-detector) - A beat detection utility which is using the Web Audio API.
* [Beep.js](https://github.com/stewdio/beep.js) - Beep is a JavaScript toolkit for building browser-based synthesizers.
* [Rust Web Audio API](https://github.com/orottier/web-audio-api-rs) - A Rust implementation of the Web Audio API, for use in non-browser contexts.
* [WASM Audio Decoders](https://github.com/eshaz/wasm-audio-decoders) - Browser and NodeJS Web Assembly audio decoder libraries that are highly optimized for size and performance.
* [Chrome Music Lab](https://github.com/googlecreativelab/chrome-music-lab) - A collection of experiments for exploring how music works, all built with the Web Audio API.
* [JavaScript Karplus-Strong](https://github.com/mrahtz/javascript-karplus-strong) - JavaScript/Web Audio implementation of Karplus-Strong guitar synthesis.
* [tonejs-instruments](https://github.com/nbrosowsky/tonejs-instruments) - A small instrument sample library with quick-loader for tone.js.
* [wavesurfer.js](https://github.com/wavesurfer-js/wavesurfer.js) - Navigable waveform built on Web Audio and Canvas.
* [Aurora.js](https://github.com/audiocogs/aurora.js) - JavaScript audio decoding framework.
* [Pizzicato](https://github.com/alemangui/pizzicato) - Library to simplify the way you create and manipulate sounds with the Web Audio API.
* [Pitch detection](https://github.com/cwilso/PitchDetect) - Pitch detection in Web Audio using autocorrelation.
* [SAT](https://github.com/RicherMans/SAT) - Streaming Audiotransformers for online Audio tagging.
* [WebAudioXML](https://github.com/hanslindetorp/WebAudioXML) - An XML syntax for building Web Audio API applications.
* [FaustWasm](https://github.com/Fr0stbyteR/faustwasm) - The FaustWasm library presents a convenient, high-level API that wraps around Faust compiler.
* [ContourViz](https://github.com/cjwit/contourviz) - A package that charts musical contours into a web-based interactive using music21 and D3.js.
* [wave-resampler](https://github.com/rochars/wave-resampler) - PCM audio resampler written entirely in JavaScript.
* [useSound](https://github.com/joshwcomeau/use-sound) - A React Hook for playing sound effects.
* [Naph.js](https://github.com/potistudio/naph.js) - Naph is a Node.js Library that Allow Hosting Native Audio Plugins (VST, VST3, AAX, AU).
* [audio-worklet-loader](https://github.com/leviance/audio-worklet-loader) - Audio Worklet loader for webpack.

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>


### <span id="mir">Music Information Retrieval (MIR)</span>

* [Madmom](https://github.com/CPJKU/madmom) - Madmom is an audio signal processing library written in Python with a strong focus on music information retrieval (MIR) tasks.
* [Beets](https://beets.io/) - Beets is the media library management system for obsessive music geeks. music library manager and MusicBrainz tagger.
* [Mido](https://github.com/mido/mido) - MIDI Objects for Python. Mido is a library for working with MIDI messages and ports.
* [mirdata](https://github.com/mir-dataset-loaders/mirdata) - Python library for working with Music Information Retrieval (MIR) datasets.
* [Partitura](https://github.com/CPJKU/partitura) - A python package for handling modern staff notation of music.
* [Midifile](https://midifile.sapp.org/) - C++ classes for reading/writing Standard MIDI Files.
* [MSAF](https://msaf.readthedocs.io/en/latest/#) - Music Structure Analysis Framework. A Python framework to analyze music structure. MSAF is a python package for the analysis of music structural segmentation algorithms. It includes a set of features, algorithms, evaluation metrics, and datasets to experiment with.
* [mxml](https://github.com/Reinvent-Archived-Projects/mxml) - MusicXML parsing and layout library. **mxml** is a C++ parser and layout generator for [MusicXML](http://www.musicxml.com/) files.
* [Open-Unmix](https://sigsep.github.io/open-unmix/) - Open-Unmix, Music Source Separation for PyTorch. **Open-Unmix** , is a deep neural network reference implementation for music source separation, applicable for researchers, audio engineers and artists. **Open-Unmix** provides ready-to-use models that allow users to separate pop music into four stems:  **vocals** ,  **drums** , **bass** and the remaining **other** instruments.
* [Spleeter](https://research.deezer.com/projects/spleeter.html) - **Spleeter** is [Deezer](https://www.deezer.com/) source separation library with pretrained models written in [Python](https://www.python.org/) and uses [Tensorflow](https://tensorflow.org/). It makes it easy to train source separation model (assuming you have a dataset of isolated sources), and provides already trained state of the art model for performing various flavour of separation.
* [AMPACT](https://ampact.tumblr.com/) - Automatic Music Performance Analysis and Comparison Toolkit.
* [Basic Pitch](https://github.com/spotify/basic-pitch) - A lightweight yet powerful audio-to-MIDI converter with pitch bend detection.
* [crema](https://github.com/bmcfee/crema) - convolutional and recurrent estimators for music analysis.
* [MIDIcontroller](https://github.com/joshnishikawa/MIDIcontroller) - A library for creating Teensy MIDI controllers with support for hold or latch buttons, potentiometers, encoders, capacitive sensors, Piezo transducers and other velocity sensitive inputs with aftertouch.
* [MIDI Explorer](https://github.com/EMATech/midiexplorer) - Yet another MIDI monitor, analyzer, debugger and manipulation tool.
* [Music Exploration](https://github.com/MTG/music-explore) - App to explore latent spaces of music collections.
* [LooPy](https://loopy4edm.com/) - A data framework for music information retrieval focusing on electronic music.
* [Automatic Music Transcription (AMT) Tools](https://github.com/cwitkowitz/amt-tools) - Machine learning tools and framework for automatic music transcription.
* [carat](https://github.com/mrocamora/carat) - Computer-aided rhythm analysis toolbox.
* [miditoolkit](https://github.com/YatingMusic/miditoolkit) - A python package for working with MIDI data.
* [Midly](https://github.com/negamartin/midly) - A feature-complete MIDI parser and writer focused on speed.
* [libf0](https://github.com/groupmm/libf0) - A Python Library for Fundamental Frequency Estimation in Music Recordings.
* [PyRoll](https://github.com/loua19/pyroll) - A lightweight research library for processing symbolic music (such as MIDI) into piano-roll format.
* [solfege.ai ✋ 🎹](https://github.com/instrumentbible/solfege.ai) - Detect solfege hand signs using machine learning ✋ 🎹
* [libfmp](https://github.com/meinardmueller/libfmp) - Python package for teaching and learning Fundamentals of Music Processing (FMP).
* [jams](https://github.com/marl/jams) - A JSON Annotated Music Specification for Reproducible MIR Research.
* [Piano Trainer](https://github.com/ZaneH/piano-trainer) - A music practice program with MIDI support.
* [quickly](https://github.com/frescobaldi/quickly) - A LilyPond library for python (slated to become the successor of python-ly).
* [ChordSymbol](https://github.com/no-chris/chord-symbol) - The definitive chord symbol parser and renderer for Javascript/NodeJS.
* [Midi Miner](https://github.com/ruiguo-bio/midi-miner) - Python MIDI track classifier and tonal tension calculation based on spiral array theory.
* [Windows MIDI Services](https://github.com/microsoft/MIDI) - This project is the next-generation MIDI API for Windows, including MIDI 1.0, MIDI CI, and MIDI 2.0. It includes enhancements, a new USB class driver, new transports, and a suite of essential tools.
* [Parangonar](https://github.com/sildater/parangonar) - Parangonar is a Python package for note alignment of symbolic music.
* [musicparser](https://github.com/fosfrancesco/musicparser) - Deep learning based dependency parsing for music sequences.
* [musif](https://github.com/DIDONEproject/musif) - Music Feature Extraction and Analysis.
* [pycompmusic](https://github.com/MTG/pycompmusic) - Tools to help researchers work with Dunya and CompMusic.
* [CREPE notes](https://github.com/xavriley/crepe_notes) - Post-processing for CREPE to turn f0 pitch estimates into discrete notes (MIDI).
* [Piano transcription](https://github.com/bytedance/piano_transcription) - Piano transcription is the task of transcribing piano recordings into MIDI files.
* [pianotrans](https://github.com/azuwis/pianotrans) - Simple GUI for ByteDance's Piano Transcription with Pedals.
* [PyABC](https://github.com/campagnola/pyabc) - Python package for parsing and analyzing ABC music notation.
* [mir_ref](https://github.com/chrispla/mir_ref) - A Representation Evaluation Framework for Music Information Retrieval tasks.
* [MIDITrackView](https://github.com/AudioKit/MIDITrackView) - Displays the notes of a MIDI file and follows along with playback.
* [iimrp](https://github.com/Intelligent-Instruments-Lab/iimrp) - Magnetic Resonator Piano tools from the Intelligent Instruments Lab.
* [Music Encoding Initiative (MEI)](https://github.com/music-encoding/music-encoding) - The Music Encoding Initiative (MEI) is an open-source effort to define a system for encoding musical documents in a machine-readable structure.
* [musical-key-finder](https://github.com/jackmcarthur/musical-key-finder) - A python project that uses Librosa and other libraries to analyze the key that a song (an .mp3) is in, i.e. F major or C# minor, using the Krumhansl-Schmuckler key-finding algorithm.
* [midi-db](https://github.com/ltgcgo/midi-db) - 🎹 Data concerning MIDI standards. 

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>


### <span id="mg">Music Generation (MG)</span>

* [isobar](https://github.com/ideoforms/isobar) - isobar is a Python library for creating and manipulating musical patterns, designed for use in algorithmic composition, generative music and sonification. It makes it quick and easy to express complex musical ideas, and can send and receive events from various different sources including MIDI, MIDI files, and OSC.
* [MusPy](https://salu133445.github.io/muspy/) - MusPy is an open source Python library for symbolic music generation. It provides essential tools for developing a music generation system, including dataset management, data I/O, data preprocessing and model evaluation.
* [music21](https://web.mit.edu/music21/) - music21 is a Toolkit for Computational Musicology.
* [Msanii](https://kinyugo.github.io/msanii-demo/) - Msanii: High Fidelity Music Synthesis on a Shoestring Budget.
* [MusicLM](https://google-research.github.io/seanet/musiclm/examples/) - MusicLM: Generating Music From Text.
* [SingSong](https://storage.googleapis.com/sing-song/index.html) - SingSong: Generating musical accompaniments from singing.
* [Riffusion](https://github.com/riffusion/riffusion) - Riffusion is a library for real-time music and audio generation with stable diffusion.
* [Riffusion App](https://github.com/riffusion/riffusion-app) - Riffusion is an app for real-time music generation with stable diffusion.
* [RiffusionVST](https://github.com/mklingen/RiffusionVST) - A VST3 plugin for Riffusion based on JUCE.
* [riffusionDJ](https://github.com/d3n7/riffusionDJ) - Multichannel Looper/Feedback System for Riffusion (with Automatic1111) made for live performance.
* [Mozart](https://github.com/aashrafh/Mozart) - An optical music recognition (OMR) system. Converts sheet music to a machine-readable version. The aim of this project is to develop a sheet music reader. This is called Optical Music Recognition (OMR). Its objective is to convert sheet music to a machine-readable version. We take a simplified version where we convert an image of sheet music to a textual representation that can be further processed to produce midi files or audio files like wav or mp3.
* [Muzic](https://github.com/microsoft/muzic) - Muzic: Music Understanding and Generation with Artificial Intelligence. **Muzic** is a research project on AI music that empowers music understanding and generation with deep learning and artificial intelligence. Muzic is pronounced as [ˈmjuːzeik] and '谬贼客' (in Chinese).
* [MUSICAIZ](https://github.com/carlosholivan/musicaiz) - A python framework for symbolic music generation, evaluation and analysis.
* [Jukebox](https://openai.com/blog/jukebox/) - Code for the paper "Jukebox: A Generative Model for Music". We’re introducing Jukebox, a neural net that generates music, including rudimentary singing, as raw audio in a variety of genres and artist styles. We’re releasing the model weights and code, along with a tool to explore the generated samples.
* [MidiTok](https://github.com/Natooz/MidiTok) - A convenient MIDI / symbolic music tokenizer for Deep Learning networks, with multiple strategies .🎶
* [SCAMP](http://scamp.marcevanstein.com/#) - SCAMP is an computer-assisted composition framework in Python designed to act as a hub, flexibly connecting the composer-programmer to a wide variety of resources for playback and notation. SCAMP allows the user to manage the flow of musical time, play notes either using [FluidSynth](http://www.fluidsynth.org/) or via MIDI or OSC messages to an external synthesizer, and ultimately quantize and export the result to music notation in the form of MusicXML or Lilypond. Overall, the framework aims to address pervasive technical challenges while imposing as little as possible on the aesthetic choices of the composer-programmer.
* [Facet](https://github.com/mjcella/facet) - Facet is an open-source live coding system for algorithmic music. With a code editor in the browser and a NodeJS server running locally on your machine, Facet can generate and sequence audio and MIDI data in real-time.Facet is a live coding system for algorithmic music.
* [Mingus](https://github.com/bspaans/python-mingus) - Mingus is a music package for Python. Mingus is a package for Python used by programmers, musicians, composers and researchers to make and analyse music.
* [Audeo](http://faculty.washington.edu/shlizee/audeo/) - ***Audeo*** is a novel system that gets as an input video frames of a musician playing the piano and generates the music for that video. Generation of music from visual cues is a challenging problem and it is not clear whether it is an attainable goal at all. Our main aim in this work is to explore the plausibility of such a transformation and to identify cues and components able to carry the association of sounds with visual events. To achieve the transformation we built a full pipeline named *Audeo* containing three components. We first translate the video frames of the keyboard and the musician hand movements into raw mechanical musical symbolic representation Piano-Roll (Roll) for each video frame which represents the keys pressed at each time step. We then adapt the Roll to be amenable for audio synthesis by including temporal correlations. This step turns out to be critical for meaningful audio generation. As a last step, we implement Midi synthesizers to generate realistic music. *Audeo* converts video to audio smoothly and clearly with only a few setup constraints.
* [libatm](https://github.com/allthemusicllc/libatm) - `libatm` is a library for generating and working with MIDI files. It was purpose-built for All the Music, LLC to assist in its mission to enable musicians to make all of their music without the fear of frivolous copyright lawsuits. All code is released into the public domain via the [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). If you're looking for a command line tool to generate and work with MIDI files, check out [the `atm-cli` project](https://github.com/allthemusicllc/atm-cli) that utilizes this library. For more information on All the Music, check out [allthemusic.info](http://allthemusic.info/). For more detailed library documentation, check out the crate documentation [here](https://allthemusicllc.github.io/libatm/libatm/index.html).
* [Davidic](https://github.com/bendious/Davidic) - A minimalist procedural music creator. Randomly generate musical scale, MIDI instrument(s), chord progression, and rhythm, then lock-in what you like and regenerate to refine. Advanced controls: chord progressions and rhythms can be manually specified after selecting the Advanced Controls toggle, but UI support is minimal. Suggested usage is restricted to tweaking randomly-generated starting points.
* [MERT](https://github.com/yizhilll/MERT) - MERT: Acoustic Music Understanding Model with Large-Scale Self-supervised Training.
* [PyMusicLooper](https://github.com/arkrow/PyMusicLooper) - A script for creating seamless music loops, with play/export support.
* [ChatGPT2midi](https://github.com/spcoughlin/ChatGPT2midi) - CLI Program for generating chord progressions with ChatGPT.
* [linuxwave](https://github.com/orhun/linuxwave) - Generate music from the entropy of Linux 🐧🎵
* [Chord2Melody](https://github.com/tanreinama/chord2melody) - Automatic Music Generation AI.
* [symbolic music diffusion](https://github.com/magenta/symbolic-music-diffusion) - Symbolic Music Generation with Diffusion Models.
* [AI-Pokemon-Music](https://github.com/nickd16/AI-Pokemon-Music) - Using AI (Transformers) to make original/ recreate Pokémon music.
* [WalkingBass](https://github.com/philxan/WalkingBass) - A MuseScore 3 plugin that generates a walking bass line.
* [DeBussy](https://github.com/asigalov61/DeBussy) - Solo Piano Music AI Implementation.
* [Writing music with ChatGPT](https://github.com/olaviinha/MusicWithChatGPT) - Tips and tools for writing music with the aid of ChatGPT.
* [Somax 2](https://github.com/DYCI2/Somax2) - Somax 2 is an application for musical improvisation and composition.
* [Polyrhythmix](https://github.com/dredozubov/polyrhythmix) - Polyrhythmix (Poly) is a command-line assistant designed to generate MIDI files from the description of drum parts.
* [LaunchpadGPT](https://github.com/yunlong10/LaunchpadGPT/) - Language Model as Music Visualization Designer on Launchpad.
* [Polyffusion](https://github.com/aik2mlj/polyffusion) - A Diffusion Model for Polyphonic Score Generation with Internal and External Controls.
* [JAMMIN-GPT](https://github.com/supersational/JAMMIN-GPT) - Text-based Improvisation using LLMs in Ableton Live.
* [Anticipatory](https://github.com/jthickstun/anticipation) - Anticipatory Music Transformer.
* [MIDI Language Model](https://github.com/jeremyjordan/midi-lm) - Generative modeling of MIDI files.
* [modulo](https://github.com/francesco-di-maggio/modulo) - A Toolkit for Tinkering with Digital Musical Instruments.
* [MusicLang](https://github.com/MusicLang/musiclang) - MusicLang which simply stands for "music language" is a Python framework implementing a new language for tonal music. This language allows composers to load, write, transform and predict symbolic music in a simple, condensed and high level manner.
* [FluxMusic](https://github.com/feizc/FluxMusic) - FluxMusic: Text-to-Music Generation with Rectified Flow Transformer.

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>


### <span id="asr">Speech Recognition (ASR)</span>

* [Kaldi](http://kaldi-asr.org/) - Kaldi is a toolkit for speech recognition, intended for use by speech recognition researchers and professionals.
* [PaddleSpeech](https://github.com/PaddlePaddle/PaddleSpeech) - Easy-to-use Speech Toolkit including SOTA/Streaming ASR with punctuation, influential TTS with text frontend, Speaker Verification System, End-to-End Speech Translation and Keyword Spotting.
* [NVIDIA NeMo](https://nvidia.github.io/NeMo/) - NVIDIA NeMo is a conversational AI toolkit built for researchers working on automatic speech recognition (ASR), natural language processing (NLP), and text-to-speech synthesis (TTS). The primary objective of NeMo is to help researchers from industry and academia to reuse prior work (code and pretrained models) and make it easier to create new [conversational AI models](https://developer.nvidia.com/conversational-ai#started).
* [Whisper](https://github.com/openai/whisper) - Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multi-task model that can perform multilingual speech recognition as well as speech translation and language identification.
* [WhisperX](https://github.com/m-bain/whisperX) - WhisperX: Automatic Speech Recognition with Word-level Timestamps (& Diarization).
* [Whisper-AT](https://github.com/yuangongnd/whisper-at) - Whisper-AT: Noise-Robust Automatic Speech Recognizers are Also Strong Audio Event Taggers.
* [Transformers](https://huggingface.co/docs/transformers/index) - 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX.
* [Julius](https://github.com/julius-speech/julius) - Open-Source Large Vocabulary Continuous Speech Recognition Engine. "Julius" is a high-performance, small-footprint large vocabulary continuous speech recognition (LVCSR) decoder software for speech-related researchers and developers. The main platform is Linux and other Unix-based system, as well as Windows, Mac, Androids and other platforms.
* [audino](https://github.com/midas-research/audino) - audino is an open source audio annotation tool. It provides features such as transcription and labeling which enables annotation for Voice Activity Detection (VAD), Diarization, Speaker Identification, Automated Speech Recognition, Emotion Recognition tasks and more.
* [Wenet](https://wenet.org.cn/wenet/) - Wenet is an tansformer-based end-to-end ASR toolkit.
* [SpeechBrain](https://speechbrain.github.io/) - SpeechBrain is an **open-source** and **all-in-one** conversational AI toolkit based on PyTorch. The goal is to create a  **single** ,  **flexible** , and **user-friendly** toolkit that can be used to easily develop  **state-of-the-art speech technologies** , including systems for  **speech recognition** ,  **speaker recognition** ,  **speech enhancement** ,  **speech separation** ,  **language identification** ,  **multi-microphone signal processing** , and many others.
* [ESPnet](https://espnet.github.io/espnet/) - ESPnet is an end-to-end speech processing toolkit, mainly focuses on end-to-end speech recognition and end-to-end text-to-speech. ESPnet is an end-to-end speech processing toolkit covering end-to-end speech recognition, text-to-speech, speech translation, speech enhancement, speaker diarization, spoken language understanding, and so on. ESPnet uses [pytorch](http://pytorch.org/) as a deep learning engine and also follows [Kaldi](http://kaldi-asr.org/) style data processing, feature extraction/format, and recipes to provide a complete setup for various speech processing experiments.
* [Espresso](https://github.com/freewym/espresso) - Espresso is an open-source, modular, extensible end-to-end neural automatic speech recognition (ASR) toolkit based on the deep learning library PyTorch and the popular neural machine translation toolkit fairseq. 
* [Leon](https://getleon.ai/) - 🧠 Leon is your open-source personal assistant.
* [DeepSpeech](https://github.com/mozilla/DeepSpeech) - DeepSpeech is an open source embedded (offline, on-device) speech-to-text engine which can run in real time on devices ranging from a Raspberry Pi 4 to high power GPU servers.
* [SpeechRecognition](https://github.com/Uberi/speech_recognition) - Speech recognition module for Python, supporting several engines and APIs, online and offline.
* [annyang](https://www.talater.com/annyang/) - annyang is a tiny javascript library that lets your visitors control your site with voice commands. annyang supports multiple languages, has no dependencies, weighs just 2kb and is free to use.
* [PocketSphinx](https://github.com/cmusphinx/pocketsphinx) - This is PocketSphinx, one of Carnegie Mellon University's open source large vocabulary, speaker-independent continuous speech recognition engines.
* [Kara](https://github.com/emileclarkb/Kara) - Open Source Voice Assistant. Simply put, Kara is a voice assistant that steals 0% of your data so you stay free! She is a actively maintained, modular, and designed to customize.
* [Voice Lab](https://github.com/Voice-Lab/VoiceLab) - Voice Lab is an automated voice analysis software. What this software does is allow you to measure, manipulate, and visualize many voices at once, without messing with analysis parameters. You can also save all of your data, analysis parameters, manipulated voices, and full colour spectrograms and power spectra, with the press of one button.
* [3D-Speaker](https://github.com/alibaba-damo-academy/3D-Speaker) - 3D-Speaker is an open-source toolkit for single- and multi-modal speaker verification, speaker recognition, and speaker diarization. All pretrained models are accessible on ModelScope.
* [FunASR](https://github.com/alibaba-damo-academy/FunASR) - FunASR: A Fundamental End-to-End Speech Recognition Toolkit.
* [Squeezeformer](https://github.com/upskyy/Squeezeformer) - An Efficient Transformer for Automatic Speech Recognition.
* [dejavu](https://github.com/worldveil/dejavu) - Audio fingerprinting and recognition in Python.
* [Vosk Speech Recognition Toolkit](https://github.com/alphacep/vosk-api) - Offline speech recognition API for Android, iOS, Raspberry Pi and servers with Python, Java, C# and Node.
* [OpenAV](https://github.com/DmitryRyumin/OpenAV) - An open-source library for recognition of speech commands in the user dictionary using audiovisual data of the speaker.
* [MiniASR](https://github.com/vectominist/MiniASR) - A mini, simple, and fast end-to-end automatic speech recognition toolkit.
* [UniSpeech](https://github.com/microsoft/UniSpeech) - UniSpeech - Large Scale Self-Supervised Learning for Speech.
* [paasr](https://github.com/rafaelvalle/paasr) - Privacy Aware Automatic Speech Recognition.
* [whisper-timestamped](https://github.com/linto-ai/whisper-timestamped) - Multilingual Automatic Speech Recognition with word-level timestamps and confidence.
* [DisVoice](https://github.com/jcvasquezc/DisVoice) - DisVoice is a python framework designed to compute features from speech files. Disvoice computes glottal, phonation, articulation, prosody, phonological, and features representation learnig strategies using autoencders.
* [pypinyin](https://github.com/mozillazg/python-pinyin) - A Python tool for converting Chinese character to Pinyin.
* [PyShengyun](https://github.com/yuyq96/pyshengyun) - A Python converter for Chinese Pinyin and Shengyun (initials and finals).
* [KaldiFeat](https://github.com/yuyq96/kaldifeat) - A light-weight Python library for computing Kaldi-style acoustic features based on NumPy.
* [Gruut IPA](https://github.com/rhasspy/gruut-ipa) - Python library for manipulating pronunciations using the International Phonetic Alphabet (IPA).
* [SALMONN](https://github.com/bytedance/SALMONN/) - Speech Audio Language Music Open Neural Network.
* [PraatIO](https://github.com/timmahrt/praatIO) - A python library for working with praat, textgrids, time aligned audio transcripts, and audio files. It is primarily used for extracting features from and making manipulations on audio files given hierarchical time-aligned transcriptions (utterance > word > syllable > phone, etc).
* [WhisperKit](https://github.com/argmaxinc/WhisperKit) - WhisperKit is a Swift package that integrates OpenAI's popular Whisper speech recognition model with Apple's CoreML framework for efficient, local inference on Apple devices.
* [Language-Codec](https://github.com/jishengpeng/languagecodec) - Reducing the Gaps Between Discrete Codec Representation and Speech Language Models.
* [PPGs](https://github.com/interactiveaudiolab/ppgs) - Training, evaluation, and inference of neural phonetic posteriorgrams (PPGs) in PyTorch.
* [Whisper Burn](https://github.com/Gadersd/whisper-burn) - Rust Implementation of OpenAI's Whisper Transcription Model.
* [TeleSpeech-ASR](https://github.com/Tele-AI/TeleSpeech-ASR) - TeleSpeech-ASR is pre-trained with 300,000 hours of unlabeled multi-dialect speech data and fine-tuned using 30 types of internal labeled data, breaking the dilemma that a single model can only recognize a specific single dialect.
* [Speech-Emotion-Recognition](https://github.com/Renovamen/Speech-Emotion-Recognition) - Speech emotion recognition implemented in Keras (LSTM, CNN, SVM, MLP).
* [SwiftSpeech](https://github.com/Cay-Zhang/SwiftSpeech) - A speech recognition framework designed for SwiftUI.
* [SenseVoice](https://github.com/FunAudioLLM/SenseVoice) - SenseVoice is a speech foundation model with multiple speech understanding capabilities, including automatic speech recognition (ASR), spoken language identification (LID), speech emotion recognition (SER), and audio event detection (AED).
* [SenseVoice.cpp](https://github.com/lovemefan/SenseVoice.cpp) - Port of Funasr's Sense-voice model in C/C++.

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>


### <span id="tts">Speech Synthesis (TTS)</span>

* [VALL-E](https://valle-demo.github.io/) - VALL-E: Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers.
* [SpeechGPT](https://github.com/0nutation/SpeechGPT) - SpeechGPT: Empowering Large Language Models with Intrinsic Cross-Modal Conversational Abilities.
* [VITS](https://github.com/jaywalnut310/vits) - VITS: Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech. Several recent end-to-end text-to-speech (TTS) models enabling single-stage training and parallel sampling have been proposed, but their sample quality does not match that of two-stage TTS systems. In this work, we present a parallel end-to-end TTS method that generates more natural sounding audio than current two-stage models. Our method adopts variational inference augmented with normalizing flows and an adversarial training process, which improves the expressive power of generative modeling. We also propose a stochastic duration predictor to synthesize speech with diverse rhythms from input text.
* [NeuralSpeech](https://github.com/microsoft/NeuralSpeech) - **NeuralSpeech** is a research project in Microsoft Research Asia focusing on neural network based speech processing, including automatic speech recognition (ASR), text to speech (TTS), etc.
* [Real-Time Voice Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning) - Clone a voice in 5 seconds to generate arbitrary speech in real-time.  This repository is an implementation of [Transfer Learning from Speaker Verification to Multispeaker Text-To-Speech Synthesis](https://arxiv.org/pdf/1806.04558.pdf) (SV2TTS) with a vocoder that works in real-time. SV2TTS is a deep learning framework in three stages. In the first stage, one creates a digital representation of a voice from a few seconds of audio. In the second and third stages, this representation is used as reference to generate speech given arbitrary text.
* [WaveNet](https://github.com/ibab/tensorflow-wavenet) - A TensorFlow implementation of DeepMind's WaveNet paper. The WaveNet neural network architecture directly generates a raw audio waveform, showing excellent results in text-to-speech and general audio generation (see the DeepMind blog post and paper for details).
* [FastSpeech 2](https://github.com/ming024/FastSpeech2) - An implementation of Microsoft's "FastSpeech 2: Fast and High-Quality End-to-End Text to Speech".
* [MelGAN](http://swpark.me/melgan/) - Generative Adversarial Networks for Conditional Waveform Synthesis.
* [HiFi-GAN](https://github.com/jik876/hifi-gan) - HiFi-GAN: Generative Adversarial Networks for Efficient and High Fidelity Speech Synthesis.
* [edge-tts](https://github.com/rany2/edge-tts) - Use Microsoft Edge's online text-to-speech service from Python (without needing Microsoft Edge/Windows or an API key).
* [Vocode](https://docs.vocode.dev/) - Vocode is an open-source library for building voice-based LLM applications.
* [TTS-dataset-tools](https://github.com/youmebangbang/TTS-dataset-tools) - Automatically generates TTS dataset using audio and associated text. Make cuts under a custom length. Uses Google Speech to text API to perform diarization and transcription or aeneas to force align text to audio.
* [Elevenlabs](https://github.com/elevenlabs/elevenlabs-python) - The official Python API for ElevenLabs text-to-speech software. Eleven brings the most compelling, rich and lifelike voices to creators and developers in just a few lines of code.
* [NaturalSpeech 2](https://speechresearch.github.io/naturalspeech2/) - NaturalSpeech 2: Latent Diffusion Models are Natural and Zero-Shot Speech and Singing Synthesizers.
* [TorToiSe](https://github.com/neonbjb/tortoise-tts) - A multi-voice TTS system trained with an emphasis on quality.
* [libvits-ncnn](https://github.com/Sg4Dylan/libvits-ncnn) - libvits-ncnn is an ncnn implementation of the VITS library that enables cross-platform GPU-accelerated speech synthesis.🎙️💻
* [SAM](https://github.com/s-macke/SAM) - Software Automatic Mouth - Tiny Speech Synthesizer. Sam is a very small Text-To-Speech (TTS) program written in C, that runs on most popular platforms. 
* [Lyrebird](https://github.com/lyrebird-voice-changer/lyrebird) - 🦜 Simple and powerful voice changer for Linux, written in GTK 3.
* [Euterpe](https://github.com/tachi-hi/euterpe) - Real-time Audio-to-audio Karaoke Generation System for Monaural Music.
* [YourTTS](https://github.com/Edresson/YourTTS) - Towards Zero-Shot Multi-Speaker TTS and Zero-Shot Voice Conversion for everyone.
* [ElevenLabs](https://github.com/elevenlabs/elevenlabs-python) - The official Python API for ElevenLabs text-to-speech software. Eleven brings the most compelling, rich and lifelike voices to creators and developers in just a few lines of code.
* [Barkify](https://github.com/anyvoiceai/Barkify) - Barkify: an unoffical training implementation of Bark TTS by suno-ai.
* [WeTTS](https://github.com/wenet-e2e/wetts) - Production First and Production Ready End-to-End Text-to-Speech Toolkit.
* [Piper](https://github.com/rhasspy/piper) - A fast, local neural text to speech system that sounds great and is optimized for the Raspberry Pi 4.
* [Voicebox](https://github.com/SpeechifyInc/Meta-voicebox) - The first generative AI model for speech to generalize across tasks with state-of-the-art performance.
* [Fish Diffusion](https://github.com/fishaudio/fish-diffusion) - An easy to understand TTS / SVS / SVC framework.
* [TTS Generation WebUI](https://github.com/rsxdalv/tts-generation-webui) - TTS Generation WebUI (Bark, MusicGen, Tortoise, RVC, Vocos, Demucs).
* [xVA Synth](https://github.com/DanRuta/xVA-Synth) - xVASynth 2.0 is a machine learning based speech synthesis app, using voices from characters/voice sets from video games.
* [PlayHT](https://github.com/playht/pyht) - PlayHT Python SDK -- Text-to-Speech Audio Streaming.
* [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - 1 min voice data can also be used to train a good TTS model! (few shot voice cloning).
* [MetaVoice-1B](https://github.com/metavoiceio/metavoice-src) - MetaVoice-1B is a 1.2B parameter base model trained on 100K hours of speech for TTS (text-to-speech).
* [RAD-MMM](https://github.com/NVIDIA/RAD-MMM) - A TTS model that makes a speaker speak new languages.
* [BUD-E](https://github.com/LAION-AI/natural_voice_assistant) - A conversational and empathic AI Voice Assistant.
* [Bridge-TTS](https://github.com/thu-ml/Bridge-TTS) - Schrodinger Bridges Beat Diffusion Models on Text-to-Speech Synthesis.
* [lina-speech](https://github.com/theodorblackbird/lina-speech) - linear attention based text-to-speech.
* [ZMM-TTS](https://github.com/nii-yamagishilab/ZMM-TTS) - Zero-shot Multilingual and Multispeaker Speech Synthesis Conditioned on Self-supervised Discrete Speech Representations.
* [RealtimeTTS](https://github.com/KoljaB/RealtimeTTS) - RealtimeTTS is a state-of-the-art text-to-speech (TTS) library designed for real-time applications.
* [StableTTS](https://github.com/KdaiP/StableTTS) - Next-generation TTS model using flow-matching and DiT, inspired by Stable Diffusion 3.
* [ChatTTS](https://github.com/2noise/ChatTTS) - ChatTTS is a generative speech model for daily dialogue.
* [StyleTTS 2](https://github.com/yl4579/StyleTTS2) - StyleTTS 2: Towards Human-Level Text-to-Speech through Style Diffusion and Adversarial Training with Large Speech Language Models.
* [Matcha-TTS](https://github.com/shivammehta25/Matcha-TTS) - Matcha-TTS: A fast TTS architecture with conditional flow matching.
* [MahaTTS](https://github.com/dubverse-ai/MahaTTS) - MahaTTS: An Open-Source Large Speech Generation Model.
* [MeloTTS](https://github.com/myshell-ai/MeloTTS) - MeloTTS is a high-quality multi-lingual text-to-speech library by MyShell.ai.
* [OpenVoice](https://github.com/myshell-ai/OpenVoice) - Instant voice cloning by MyShell.
* [MetaVoice-1B](https://github.com/metavoiceio/metavoice-src) - MetaVoice-1B is a 1.2B parameter base model trained on 100K hours of speech for TTS (text-to-speech).
* [DEX-TTS](https://github.com/winddori2002/DEX-TTS) - Diffusion-based EXpressive Text-to-Speech with Style Modeling on Time Variability.
* [CosyVoice](https://github.com/FunAudioLLM/CosyVoice) - Multi-lingual large voice generation model, providing inference, training and deployment full-stack ability.
* [tortoise.cpp](https://github.com/balisujohn/tortoise.cpp) - tortoise.cpp: GGML implementation of tortoise-tts.

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>


### <span id="svs">Singing Voice Synthesis (SVS)</span>

* [NNSVS](https://nnsvs.github.io/) - Neural network-based singing voice synthesis library for research.
* [Muskit](https://github.com/SJTMusicTeam/Muskits) - Muskit is an open-source music processing toolkit. Currently we mostly focus on benchmarking the end-to-end singing voice synthesis and expect to extend more tasks in the future. Muskit employs [pytorch](http://pytorch.org/) as a deep learning engine and also follows [ESPnet](https://github.com/espnet/espnet) and [Kaldi](http://kaldi-asr.org/) style data processing, and recipes to provide a complete setup for various music processing experiments.
* [OpenUtau](http://www.openutau.com/) - Open singing synthesis platform / Open source UTAU successor.
* [so-vits-svc](https://github.com/svc-develop-team/so-vits-svc) - SoftVC VITS Singing Voice Conversion.
* [Real-Time Voice Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning) - Clone a voice in 5 seconds to generate arbitrary speech in real-time.
* [Retrieval-based-Voice-Conversion-WebUI](https://github.com/liujing04/Retrieval-based-Voice-Conversion-WebUI) - An easy-to-use SVC framework based on VITS.
* [Sinsy](http://sinsy.jp/) - Sinsy is an HMM/DNN-based singing voice synthesis system. You can generate a singing voice sample by uploading the musical score (MusicXML) to this website.
* [DiffSinger](https://github.com/MoonInTheRiver/DiffSinger) - DiffSinger: Singing Voice Synthesis via Shallow Diffusion Mechanism.
* [lessampler](https://www.gloomyghost.com/lessampler/#/) - lessampler is a Singing Voice Synthesizer. It provides complete pitch shifting, time stretching and other functions. Support multiple interface calls such as UTAU, Library, and Shine.
* [Mellotron](https://github.com/NVIDIA/mellotron) - Mellotron: a multispeaker voice synthesis model based on Tacotron 2 GST that can make a voice emote and sing without emotive or singing training data.
* [VI-SVS](https://github.com/PlayVoice/VI-SVS) - Use VITS and Opencpop to develop singing voice synthesis; Different from VISinger.
* [midi2voice](https://github.com/mathigatti/midi2voice) - Singing Synthesis from MIDI file.
* [MoeGoe](https://github.com/CjangCjengh/MoeGoe) - Executable file for VITS inference.
* [Voice Conversion](https://github.com/ebadawy/voice_conversion) - Voice Conversion Using Speech-to-Speech Neuro-Style Transfer.
* [WGANSing](https://github.com/MTG/WGANSing) - A Multi-Voice Singing Voice Synthesizer Based on the Wasserstein-GAN.
* [clone-voice](https://github.com/jianchang512/clone-voice) - A sound cloning tool with a web interface to record audio using your patch or any sound.
* [OpenVoice](https://github.com/myshell-ai/OpenVoice) - Instant voice cloning by MyShell.

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>


### <span id="ae">Audio Evaluation</span>

* [JiWER](https://github.com/jitsi/jiwer) - JiWER is a simple and fast python package to evaluate an automatic speech recognition system. It supports the following measures:word error rate (WER)、match error rate (MER)、word information lost (WIL)、word information preserved (WIP)、character error rate (CER). Evaluate your speech-to-text system with similarity measures such as word error rate (WER).
* [librosa](https://librosa.org/doc/latest/index.html) - Librosa is a python package for music and audio analysis. It provides the building blocks necessary to create music information retrieval systems.
* [Parselmouth](https://github.com/YannickJadoul/Parselmouth) - Parselmouth - Praat in Python, the Pythonic way. Parselmouth is a Python library for the Praat software.
* [pystoi](https://github.com/mpariente/pystoi) - pystoi - Implementation of the classical and extended Short Term Objective Intelligibility measures. Intelligibility measure which is highly correlated with the intelligibility of degraded speech signals, e.g., due to additive noise, single/multi-channel noise reduction, binary masking and vocoded speech as in CI simulations. The STOI-measure is intrusive, i.e., a function of the clean and degraded speech signals. STOI may be a good alternative to the speech intelligibility index (SII) or the speech transmission index (STI), when you are interested in the effect of nonlinear processing to noisy speech, e.g., noise reduction, binary masking algorithms, on speech intelligibility.
* [pyworld](https://github.com/JeremyCCHsu/Python-Wrapper-for-World-Vocoder) - pyworld - A Python wrapper for the high-quality vocoder "World". WORLD Vocoder is a fast and high-quality vocoder which parameterizes speech into three components:f0 Pitch contour、sp -  Harmonic spectral envelope、ap - Aperiodic spectral envelope (relative to the harmonic spectral envelope).
* [Resemblyzer](https://github.com/resemble-ai/Resemblyzer) - Resemblyzer allows you to derive a high-level representation of a voice through a deep learning model (referred to as the voice encoder). Given an audio file of speech, it creates a summary vector of 256 values (an embedding, often shortened to "embed" in this repo) that summarizes the characteristics of the voice spoken.
* [SpeechBrain](https://speechbrain.github.io/) - SpeechBrain is an **open-source** and **all-in-one** conversational AI toolkit based on PyTorch. The goal is to create a  **single** ,  **flexible** , and **user-friendly** toolkit that can be used to easily develop  **state-of-the-art speech technologies** , including systems for  **speech recognition** ,  **speaker recognition** ,  **speech enhancement** ,  **speech separation** ,  **language identification** ,  **multi-microphone signal processing** , and many others.
* [speechmetrics](https://github.com/aliutkus/speechmetrics) - speechmetrics is a wrapper around several freely available implementations of objective metrics for estimating the quality of speech signals. It includes both relative and absolute metrics, which means metrics that do or do not need a reference signal, respectively.


<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

