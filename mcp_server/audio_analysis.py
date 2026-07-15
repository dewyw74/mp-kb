from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import soundfile as sf
from scipy.signal import resample_poly, welch

SPECTRAL_BANDS = [
    ("sub", 20, 60),
    ("bass", 60, 250),
    ("low_mid", 250, 500),
    ("mid", 500, 2000),
    ("high_mid", 2000, 6000),
    ("high", 6000, 20000),
]


def _to_db(value: float, floor: float = 1e-10) -> float:
    return float(20 * np.log10(max(value, floor)))


def _true_peak_dbtp(samples: np.ndarray, sample_rate: int, oversample: int = 4) -> float:
    """4x-oversampled true-peak estimate per ITU-R BS.1770 Annex 2 intent."""
    upsampled = resample_poly(samples, oversample, 1, axis=0)
    peak = float(np.max(np.abs(upsampled))) if upsampled.size else 0.0
    return _to_db(peak)


def _crest_factor_db(samples: np.ndarray, true_peak_dbtp: float) -> float:
    rms = float(np.sqrt(np.mean(np.square(samples)))) if samples.size else 0.0
    return true_peak_dbtp - _to_db(rms)


def _stereo_correlation(samples: np.ndarray) -> float | None:
    if samples.ndim < 2 or samples.shape[1] < 2:
        return None
    left, right = samples[:, 0], samples[:, 1]
    if np.std(left) == 0 or np.std(right) == 0:
        return None
    return float(np.corrcoef(left, right)[0, 1])


def _spectral_bands(samples: np.ndarray, sample_rate: int) -> dict[str, float]:
    mono = samples.mean(axis=1) if samples.ndim > 1 else samples
    freqs, psd = welch(mono, fs=sample_rate, nperseg=min(65536, len(mono)))
    total_power = float(np.sum(psd)) or 1e-10

    bands: dict[str, float] = {}
    for name, low, high in SPECTRAL_BANDS:
        mask = (freqs >= low) & (freqs < high)
        band_power = float(np.sum(psd[mask]))
        bands[name] = round(_to_db(band_power / total_power), 2)
    return bands


def analyze_audio_file(path: str) -> dict[str, Any]:
    """Compute objective mix/master metrics for a WAV/AIFF file.

    Returns LUFS integrated loudness, true-peak (dBTP), crest factor (dB),
    stereo correlation (None if mono), and relative spectral-band energy.
    Stereo correlation and spectral bands are general audio-engineering
    diagnostics, not compared against any knowledge_base-documented target
    (no such numeric target exists in the KB).
    """
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(f"audio file not found: {path}")

    samples, sample_rate = sf.read(str(file_path), always_2d=False)
    samples = np.asarray(samples, dtype=np.float64)

    import pyloudnorm as pyln

    meter = pyln.Meter(sample_rate)
    lufs_integrated = float(meter.integrated_loudness(samples))

    true_peak = _true_peak_dbtp(samples, sample_rate)
    crest_factor = _crest_factor_db(samples, true_peak)
    correlation = _stereo_correlation(samples)
    bands = _spectral_bands(samples, sample_rate)

    return {
        "path": str(file_path),
        "sample_rate": sample_rate,
        "channels": 1 if samples.ndim == 1 else samples.shape[1],
        "duration_seconds": round(len(samples) / sample_rate, 2),
        "lufs_integrated": round(lufs_integrated, 2),
        "true_peak_dbtp": round(true_peak, 2),
        "crest_factor_db": round(crest_factor, 2),
        "stereo_correlation": round(correlation, 3) if correlation is not None else None,
        "spectral_bands_db": bands,
    }
