# Multitrack Session Analysis — Design

**Date:** 2026-07-20
**Status:** Approved, not yet implemented
**Roadmap link:** Phase 6 (MCP server) marked complete in `README.md`, with this item explicitly deferred as a "future extension": *"analyzing individual tracks within a multitrack session file rather than pre-bounced stems."*

## Problem

`analyze_mix` and `analyze_mix_batch` in `mcp_server/audio_analysis.py` operate on already-bounced individual audio files (one file = one mix, or one file per stem). There is no way to hand the tool a single file that contains multiple tracks and get per-track metrics back.

## Scope

**In scope (this spec):** interleaved multichannel WAV/AIFF — a single file where each channel is one track, produced by a DAW's "bounce tracks to one file" / "export multitrack as interleaved" feature.

**Explicitly out of scope (deferred):** native DAW project files (`.als`, `.flp`, `.logicx`, `.ptx`, etc.). Parsing these is DAW-specific, many are proprietary/binary formats, and tracks are frequently MIDI-only or reference external sample files with no bounced audio to analyze at all. Revisit only if the interleaved-WAV path proves insufficient in practice.

**Explicitly out of scope (V1):** automatic stereo-pair detection (e.g. treating adjacent channels as one stereo track). Every channel is analyzed as an independent mono track. Revisit if this proves painful in practice.

## New MCP tool: `analyze_session`

Mirrors the existing `analyze_mix` / `analyze_mix_batch` pattern in `mcp_server/server.py`.

```python
@mcp.tool()
def analyze_session(file_path: str, genre: str | None = None) -> dict[str, Any]:
    ...
```

### Behavior

1. Read the file via `soundfile` — it already handles arbitrary channel counts natively for WAV/AIFF, no new dependency required.
2. If the file has fewer than 2 channels, raise a `ValueError` directing the caller to `analyze_mix` instead.
3. Best-effort parse an embedded **iXML `TRACK_LIST`** chunk — the metadata field Pro Tools/Nuendo (and similar) write when bouncing an "interleave" multitrack export with per-channel names — to label each channel. Wrapped in try/except; a missing or malformed chunk never fails the analysis, it just falls back to `"Channel N"` (1-indexed).
4. For each channel, extract the mono sample slice and run the shared metrics: LUFS integrated, true-peak dBTP, crest factor (dB), spectral band energy (relative, dB). `stereo_correlation` is omitted (null) per channel — not meaningful for a single mono slice.
5. Assemble and return:
   ```json
   {
     "path": "...",
     "channel_count": 8,
     "tracks": [
       {"channel_index": 0, "name": "Kick", "lufs_integrated": ..., "true_peak_dbtp": ..., "crest_factor_db": ..., "spectral_bands_db": {...}},
       ...
     ],
     "summary": {
       "lufs_integrated": {"min": ..., "max": ..., "range": ...},
       "true_peak_dbtp": {"min": ..., "max": ..., "range": ...},
       "crest_factor_db": {"min": ..., "max": ..., "range": ...}
     },
     "relevant_kb_entries": [...]   // only if genre was passed, same lookup as analyze_mix/analyze_mix_batch
   }
   ```
   The `summary` shape matches `analyze_mix_batch`'s existing summary for consistency.

### Format restriction

`analyze_session` only accepts natively-readable formats (WAV/AIFF) — no ffmpeg transcoding path. Compressed multichannel files are rare for this use case, and iXML metadata realistically only survives in WAV/AIFF anyway. Passing an ffmpeg-only extension raises `UnsupportedAudioFormatError` with a message explaining the restriction.

## Refactor: shared `analyze_samples()` helper

Today, the LUFS/true-peak/crest/spectral logic lives inline inside `analyze_audio_file()` and is only reachable via a file path. `analyze_session` needs to run that same math on in-memory per-channel slices, not whole files.

Extract the metric computation into:

```python
def analyze_samples(samples: np.ndarray, sample_rate: int) -> dict[str, Any]:
    """LUFS/true-peak/crest-factor/stereo-correlation/spectral-bands for an
    in-memory sample array. Shared by analyze_audio_file (whole file) and
    analyze_session (per-channel slices)."""
```

`analyze_audio_file()` becomes: read samples → call `analyze_samples()` → add `path`/`sample_rate`/`channels`/`duration_seconds` wrapper fields. `analyze_session()` calls `analyze_samples()` once per channel slice (mono, so `stereo_correlation` naturally comes back `None` from the existing ndim check — no special-casing needed there).

## iXML `TRACK_LIST` parsing

A small, dependency-free RIFF chunk walker:

1. Open the WAV file's RIFF structure, scan top-level chunks for one named `iXML`.
2. If found, parse its contents as XML (stdlib `xml.etree.ElementTree`).
3. Look for `BWFXML/TRACK_LIST/TRACK` elements, each with a `CHANNEL_INDEX` and `NAME` child. Build a `{channel_index: name}` map.
4. Any failure at any step (chunk not found, malformed XML, missing expected elements) is caught and results in an empty map — callers fall back to `"Channel N"` labels, never an error.

This lives in `audio_analysis.py` as a private helper, e.g. `_read_ixml_track_names(file_path: Path) -> dict[int, str]`.

## Error handling summary

| Condition | Behavior |
|---|---|
| File not found | `FileNotFoundError` (consistent with `analyze_audio_file`) |
| Channel count < 2 | `ValueError`, points to `analyze_mix` |
| Compressed format (mp3/m4a/etc.) | `UnsupportedAudioFormatError`, explains WAV/AIFF-only restriction |
| iXML chunk missing or malformed | Silent fallback to `"Channel N"` labels, no exception |

## Testing

All synthetic, generated in the test itself (numpy + `soundfile.write`) — no binary fixtures needed:

- Multichannel WAV with known per-channel signal levels → verify per-channel LUFS/true-peak are in the expected ballpark.
- Multichannel WAV with a hand-built iXML `TRACK_LIST` chunk → verify names are extracted correctly.
- Multichannel WAV with no iXML chunk → verify `"Channel N"` fallback.
- Mono (1-channel) file passed to `analyze_session` → verify the pointer-to-`analyze_mix` `ValueError`.
- Compressed format passed → verify `UnsupportedAudioFormatError`.

**Flagged for before-ship validation (not a blocking test):** run `analyze_session` against one real DAW-exported interleaved multitrack file (e.g. from Pro Tools or Nuendo), since real-world iXML formatting conventions can vary from the spec and synthetic tests won't catch that.

## Out of scope recap

- Native DAW project file parsing (.als/.flp/.logicx/.ptx) — deferred to a future spec if needed.
- Automatic stereo-pair detection across channels — deferred to a future spec if needed.
