from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "mcp_server"))


def print_single(result: dict) -> None:
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


def print_batch(batch: dict) -> None:
    header = f"{'File':40s} {'LUFS':>8s} {'TruePeak':>10s} {'Crest':>8s} {'Corr':>6s}"
    print(header)
    print("-" * len(header))
    for entry in batch["files"]:
        name = Path(entry["path"]).name
        if "error" in entry:
            print(f"{name:40s} ERROR: {entry['error']}")
            continue
        corr = entry["stereo_correlation"]
        corr_str = f"{corr:.2f}" if corr is not None else "n/a"
        print(
            f"{name:40s} {entry['lufs_integrated']:8.2f} {entry['true_peak_dbtp']:10.2f} "
            f"{entry['crest_factor_db']:8.2f} {corr_str:>6s}"
        )
    print()
    print("Summary (across successfully analyzed files):")
    for metric, stats in batch["summary"].items():
        print(f"  {metric:18s} min {stats['min']:8.2f}  max {stats['max']:8.2f}  range {stats['range']:6.2f}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Analyze one or more mix/master files and print objective metrics. "
            "Pass multiple paths (or a single folder) to compare them side by side."
        )
    )
    parser.add_argument(
        "file_paths",
        nargs="+",
        help="Path(s) to audio file(s) (WAV/AIFF native; MP3/M4A/FLAC/OGG/WMA/AAC via ffmpeg), "
        "or a single folder path to analyze every supported file inside it",
    )
    args = parser.parse_args()

    from audio_analysis import analyze_audio_file, analyze_multiple, resolve_batch_paths

    expanded = resolve_batch_paths(args.file_paths)

    if len(expanded) == 1:
        print_single(analyze_audio_file(expanded[0]))
    else:
        print_batch(analyze_multiple(expanded))

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
