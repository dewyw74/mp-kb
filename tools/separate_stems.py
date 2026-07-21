from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "mcp_server"))


def print_result(result: dict) -> None:
    print(f"Source:      {result['source_path']}")
    print(f"Model:       {result['model']}")
    print(f"Output dir:  {result['output_dir']}")
    print()
    print("Stems:")
    for name, path in result["stems"].items():
        print(f"  {name:10s} {path}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Separate a full mix into stems (vocals/drums/bass/other) using a local Demucs model."
    )
    parser.add_argument(
        "file_path",
        help="Path to an audio file (WAV/AIFF native; MP3/M4A/FLAC/OGG/WMA/AAC via ffmpeg)",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help='Directory to write stem WAVs into. Defaults to a new "<input_filename>_stems" '
        "folder next to the input file.",
    )
    parser.add_argument(
        "--model",
        default="htdemucs",
        help='"htdemucs" (default, 4 stems) or "htdemucs_6s" (6 stems, adds guitar/piano - '
        "slower, lower quality on those two per Demucs' own docs).",
    )
    args = parser.parse_args()

    from stem_separation import separate_stems

    print_result(separate_stems(args.file_path, output_dir=args.output_dir, model=args.model))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
