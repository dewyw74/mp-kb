from __future__ import annotations

import sys
import types
from pathlib import Path

import numpy as np
import pytest
import soundfile as sf

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "mcp_server"))

from stem_separation import (  # noqa: E402
    STEM_NAMES,
    UnsupportedModelError,
    _prepare_wav,
    _resolve_output_dir,
    separate_stems,
)
from audio_analysis import UnsupportedAudioFormatError  # noqa: E402


def _write_wav(path: Path, channels: int = 2, seconds: float = 0.1, sample_rate: int = 44100) -> Path:
    frames = int(seconds * sample_rate)
    samples = np.zeros((frames, channels), dtype=np.float32) if channels > 1 else np.zeros(frames, dtype=np.float32)
    sf.write(str(path), samples, sample_rate)
    return path


# --- pure helpers, no torch/demucs needed ---------------------------------


def test_resolve_output_dir_default_sibling(tmp_path):
    source = tmp_path / "song.wav"
    source.touch()
    out = _resolve_output_dir(source, None)
    assert out == tmp_path / "song_stems"
    assert out.is_dir()


def test_resolve_output_dir_explicit(tmp_path):
    source = tmp_path / "song.wav"
    source.touch()
    explicit = tmp_path / "custom_out"
    out = _resolve_output_dir(source, str(explicit))
    assert out == explicit
    assert out.is_dir()


def test_prepare_wav_mono_duplicated_to_stereo():
    mono = np.linspace(-1.0, 1.0, 100, dtype=np.float32)
    prepared = _prepare_wav(mono)
    assert prepared.shape == (2, 100)
    assert np.array_equal(prepared[0], prepared[1])


def test_prepare_wav_stereo_passthrough_transposed():
    stereo = np.stack([np.ones(50, dtype=np.float32), np.zeros(50, dtype=np.float32)], axis=1)
    prepared = _prepare_wav(stereo)
    assert prepared.shape == (2, 50)
    assert np.allclose(prepared[0], 1.0)
    assert np.allclose(prepared[1], 0.0)


# --- validation errors, raised before any heavy import ---------------------


def test_missing_file_raises_file_not_found(tmp_path):
    with pytest.raises(FileNotFoundError):
        separate_stems(str(tmp_path / "does_not_exist.wav"))


def test_unknown_model_raises_unsupported_model_error(tmp_path):
    wav = _write_wav(tmp_path / "song.wav")
    with pytest.raises(UnsupportedModelError):
        separate_stems(str(wav), model="not_a_real_model")


def test_unsupported_format_raises(tmp_path):
    bogus = tmp_path / "song.xyz"
    bogus.write_bytes(b"not audio")
    with pytest.raises(UnsupportedAudioFormatError):
        separate_stems(str(bogus))


# --- missing torch/demucs dependency, forced deterministically -------------


def test_missing_dependency_wraps_import_error(tmp_path, monkeypatch):
    wav = _write_wav(tmp_path / "song.wav")
    # None in sys.modules forces `import torch` to raise ImportError, regardless
    # of whether torch is actually installed in this environment.
    monkeypatch.setitem(sys.modules, "torch", None)
    with pytest.raises(RuntimeError, match="requirements.txt"):
        separate_stems(str(wav))


# --- happy path + overwrite, with demucs.api mocked (real torch required) --


class _FakeSeparator:
    def __init__(self, model: str, device: str, progress: bool):
        self.model = model
        self.samplerate = 44100

    def separate_tensor(self, wav, sr):
        import torch

        n_frames = wav.shape[-1]
        stems = {name: torch.zeros(2, n_frames) for name in STEM_NAMES[self.model]}
        return wav, stems


def _fake_save_audio(wav, path, samplerate, bits_per_sample=24, **kwargs):
    arr = wav.numpy().T
    sf.write(str(path), arr, samplerate, subtype="PCM_24")


def _install_fake_demucs(monkeypatch):
    fake_pkg = types.ModuleType("demucs")
    fake_api = types.ModuleType("demucs.api")
    fake_api.Separator = _FakeSeparator
    fake_api.save_audio = _fake_save_audio
    fake_pkg.api = fake_api
    monkeypatch.setitem(sys.modules, "demucs", fake_pkg)
    monkeypatch.setitem(sys.modules, "demucs.api", fake_api)


def test_separate_stems_happy_path_writes_files(tmp_path, monkeypatch):
    pytest.importorskip("torch")
    _install_fake_demucs(monkeypatch)

    wav = _write_wav(tmp_path / "song.wav")
    result = separate_stems(str(wav))

    assert result["source_path"] == str(wav)
    assert result["model"] == "htdemucs"
    assert set(result["stems"]) == set(STEM_NAMES["htdemucs"])
    for stem_path in result["stems"].values():
        p = Path(stem_path)
        assert p.is_file()
        assert p.stat().st_size > 0


def test_separate_stems_overwrites_existing(tmp_path, monkeypatch):
    pytest.importorskip("torch")
    _install_fake_demucs(monkeypatch)

    wav = _write_wav(tmp_path / "song.wav")
    first = separate_stems(str(wav))
    vocals_path = Path(first["stems"]["vocals"])
    first_mtime = vocals_path.stat().st_mtime_ns

    second = separate_stems(str(wav))
    assert second["stems"] == first["stems"]
    assert vocals_path.is_file()
    assert vocals_path.stat().st_mtime_ns >= first_mtime
