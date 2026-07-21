from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np

from audio_analysis import SUPPORTED_EXTENSIONS, UnsupportedAudioFormatError, _read_samples

STEM_NAMES = {
    "htdemucs": ("vocals", "drums", "bass", "other"),
    "htdemucs_6s": ("vocals", "drums", "bass", "guitar", "piano", "other"),
}
SUPPORTED_MODELS = tuple(STEM_NAMES)


class UnsupportedModelError(ValueError):
    pass


def _resolve_output_dir(source: Path, output_dir: str | None) -> Path:
    """Sibling "<source>_stems" folder by default; creates the dir either way."""
    target = Path(output_dir) if output_dir is not None else source.parent / f"{source.stem}_stems"
    target.mkdir(parents=True, exist_ok=True)
    return target


def _prepare_wav(samples: np.ndarray) -> np.ndarray:
    """(frames,) or (frames, channels) -> (channels, frames) float32, duplicating
    mono to stereo since Demucs models expect stereo input."""
    arr = np.asarray(samples, dtype=np.float32)
    if arr.ndim == 1:
        arr = np.stack([arr, arr], axis=1)
    elif arr.shape[1] == 1:
        arr = np.repeat(arr, 2, axis=1)
    return arr.T


def separate_stems(path: str, output_dir: str | None = None, model: str = "htdemucs") -> dict[str, Any]:
    """Separate a full mix into stems using a local Demucs model.

    Decodes via audio_analysis._read_samples() (same WAV/AIFF-native,
    ffmpeg-transcoded MP3/M4A/FLAC/OGG/WMA/AAC support as analyze_mix) rather
    than Demucs' own file-loading path, so this server's stdio JSON-RPC
    stream never risks unexpected stdout output from that internal loader.

    torch/demucs are imported lazily here (not at module top) so importing
    this module, or starting the MCP server, never pays the torch import
    cost unless separate_stems is actually called.
    """
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(f"audio file not found: {path}")

    if model not in STEM_NAMES:
        raise UnsupportedModelError(f"unsupported model {model!r}; supported: {sorted(STEM_NAMES)}")

    suffix = file_path.suffix.lower()
    if suffix not in SUPPORTED_EXTENSIONS:
        raise UnsupportedAudioFormatError(
            f"unsupported audio format {suffix!r} for {file_path}; supported: {sorted(SUPPORTED_EXTENSIONS)}"
        )

    try:
        import torch
        from demucs.api import Separator, save_audio
    except ImportError as exc:
        raise RuntimeError(
            "torch/torchaudio/demucs are required for separate_stems (see requirements.txt "
            "- this is a large install, hundreds of MB). Run `pip install -r requirements.txt`."
        ) from exc

    samples, sample_rate = _read_samples(file_path)
    wav = torch.from_numpy(_prepare_wav(samples))

    try:
        # progress=False: Demucs' progress bar writes to stdout/stderr, which would
        # otherwise risk corrupting this server's stdio JSON-RPC transport.
        separator = Separator(model=model, device="cpu", progress=False)
        _, separated = separator.separate_tensor(wav, sample_rate)
    except Exception as exc:  # noqa: BLE001 - wrap with a clearer, actionable message
        raise RuntimeError(
            f"stem separation failed for model {model!r}: {exc}. If this is the first "
            f"time this model has been used, it needs to download its weights once "
            f"(requires internet access that one time); later runs are fully offline."
        ) from exc

    out_dir = _resolve_output_dir(file_path, output_dir)
    stem_paths: dict[str, str] = {}
    for name, tensor in separated.items():
        stem_path = out_dir / f"{name}.wav"
        save_audio(tensor, str(stem_path), samplerate=separator.samplerate, bits_per_sample=24)
        stem_paths[name] = str(stem_path)

    return {
        "source_path": str(file_path),
        "model": model,
        "output_dir": str(out_dir),
        "stems": stem_paths,
    }
