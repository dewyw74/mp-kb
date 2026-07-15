---
workflow_name: "Studio One Project Page Mastering and Export Handoff"
daw: "studio_one"
category: "mastering"
goal: "Use Studio One's Project Page as a real-time-linked mastering environment for a Song, applying a per-track mastering chain, checking loudness against streaming/reference targets, sequencing an album, and exporting to distribution and disc-replication formats without leaving Studio One."
steps:
  - "Add the Song directly to the Project (not a bounced mixdown file) so edits made back on the Song Page — a fader move, an EQ tweak, a re-render — are reflected on the Project Page automatically without re-exporting or re-importing audio."
  - "Import a bounced mixdown instead only when mastering a mix that will not be revisited, since a mixdown-based Project entry has no live link back to a Song."
  - "Load reference tracks alongside the Song entry to A/B perceived loudness and tonal balance before making mastering decisions, rather than mastering in isolation."
  - "Build the per-track processing chain in the standard mastering order: corrective EQ first to fix tonal imbalances, then compression for dynamic consistency, then stereo width processing, then a limiter last to set final loudness."
  - "Monitor the Spectral Meter, Goniometer, and Level meter continuously while processing, using the Goniometer specifically to catch stereo/mono compatibility problems introduced by width processing."
  - "Set a target-loudness preset matching the intended destination (Spotify, Apple Music, YouTube, or a custom LUFS target) so the limiter's output is checked against that platform's normalization behavior instead of just hitting an arbitrary peak level."
  - "Sequence multiple Song entries into an album on the Project Page, setting gaps or crossfades between tracks and adjusting relative levels for consistent perceived loudness across the sequence."
  - "Edit ISRC codes and other metadata per track on the Project Page before export, since distribution and disc-replication formats carry this metadata with the audio."
  - "Export to the format the destination actually requires: MP3/WAV/FLAC for digital distribution, or DDP for physical disc replication — DDP is a disc-image format sent to a manufacturer, not a streaming deliverable."
  - "Use the one-click multi-format export to generate several destination formats from the same finished master in a single pass instead of re-exporting per format by hand."
related_plugins:
  - "Studio One Project Page"
  - "Studio One Spectral Meter"
  - "Studio One Goniometer"
  - "Studio One Level Meter"
tags:
  - "studio_one"
  - "project-page"
  - "mastering"
  - "export"
  - "ddp"
  - "loudness"
  - "album-sequencing"
---

# Studio One Project Page Mastering and Export Handoff

The Project Page is Studio One's dedicated mastering environment, built into the same application as the Song Page rather than requiring a separate mastering DAW or plugin host. Its defining, genuinely distinctive feature is the live link it can maintain back to a Song: adding a Song entry directly to a Project — instead of importing a rendered mixdown file — means a later change on the Song Page (a fader nudge, an EQ correction, a fresh bounce) shows up on the Project Page automatically, without manually re-exporting and re-importing audio. This collapses the usual mix-master-revise-remaster round trip into one continuously updated project.

## Real-time link vs. static mixdown import

A Project entry added as a live Song reference stays connected to that Song file; render changes propagate through automatically. A Project entry added as an imported mixdown is a static audio file with no such connection — perfectly fine for a mix that's genuinely final, but it means every later revision requires a fresh bounce and a fresh import. Choosing which mode to use up front avoids the common mistake of mastering against a mixdown that quietly goes stale as the Song keeps getting tweaked elsewhere.

## Reference-based mastering and the processing chain

Because integrated mastering is fundamentally comparative, the Project Page supports loading reference tracks alongside the Song entry to A/B perceived loudness, tonal balance, and stereo image before committing to processing decisions. The per-track chain itself follows the conventional mastering order — corrective EQ, then compression, then stereo width, then limiting last — with the Spectral Meter, Goniometer, and Level meter available throughout to catch tonal imbalance, phase/mono-compatibility issues, and loudness in real time. This general mastering-chain-ordering logic is covered DAW-agnostically in `knowledge_base/mastering/eq/mastering_eq_vs_mix_eq_role.md` and `knowledge_base/mastering/dynamics/multiband_compression_and_limiter_chain_ordering.md`; the Project Page is simply where Studio One executes it.

## Loudness targets and album sequencing

Target-loudness presets tied to specific streaming destinations let the final limiter stage be checked against that platform's normalization behavior rather than an arbitrary peak or LUFS number chosen without context — see `knowledge_base/mastering/streaming/per_platform_normalization_deep_dive.md` for what each platform actually does to a delivered file. For multi-track releases, the Project Page also handles album-level sequencing: track order, gaps or crossfades between songs, and relative-level matching so perceived loudness stays consistent across the whole release, which is the same problem addressed generally in `knowledge_base/mastering/loudness/album_loudness_consistency.md`.

## Export and delivery formats

A finished Project can export multiple formats in a single pass — MP3, WAV, FLAC, and DDP among them — rather than requiring a separate export operation per destination. DDP (Disc Description Protocol) specifically produces a disc image intended for a replication manufacturer, not a streaming or download deliverable, and metadata such as ISRC codes should be set per track before export since both digital distributors and disc manufacturers expect it attached to the audio. This built-in export handoff is the mastering-side counterpart to the general stem-export and handoff conventions in `knowledge_base/daw/workflow/stem_export_and_session_versioning_conventions_philosophy.md` and the equivalent `knowledge_base/daw/ableton/stem_export_and_collaboration_handoff_workflow.md`.

## Common mistakes

Importing a mixdown when a live Song link was actually needed is the most common Project Page mistake — it silently disconnects the Project from further mix revisions, and any later change requires noticing the drift and re-importing by hand. Mastering without a loaded reference track is another common gap, since perceived-loudness and tonal-balance judgments made in isolation drift more easily than ones checked against a comparable finished record. A third mistake is treating DDP as a general-purpose export option rather than what it actually is — a disc-replication image — and sending it to a streaming distributor that expects WAV or FLAC instead.
