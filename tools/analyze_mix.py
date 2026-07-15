from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "mcp_server"))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Analyze a WAV/AIFF mix or master file and print objective metrics."
    )
    parser.add_argument("file_path", help="Path to a WAV or AIFF file")
    args = parser.parse_args()

    from audio_analysis import analyze_audio_file

    result = analyze_audio_file(args.file_path)

    print(f"File:              {result['path']}")
    print(f"Sample rate:       {result['sample_rate']} Hz")
    print(f"Channels:          {result['channels']}")
    print(f"Duration:          {result['duration_seconds']}s")
    print()
    print(f"LUFS integrated:   {result['lufs_integrated']} LUFS")
    print(f"True peak:         {result['true_peak_dbtp']} dBTP")
    print(f"Crest factor:      {result['crest_factor_db']} dB")
    correlation = result["stereo_correlation"]
    print(f"Stereo correlation: {correlation if correlation is not None else 'n/a (mono)'}")
    print()
    print("Spectral bands (relative energy, dB):")
    for band, value in result["spectral_bands_db"].items():
        print(f"  {band:10s} {value:8.2f} dB")
    print()
    print(
        "Note: LUFS/true-peak/crest-factor can be compared against genre targets in "
        "knowledge_base/mastering/loudness/ and mastering/dynamics/. Stereo correlation "
        "and spectral bands are general diagnostics - the KB has no numeric target for "
        "either, so interpret them with standard audio-engineering judgment."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
