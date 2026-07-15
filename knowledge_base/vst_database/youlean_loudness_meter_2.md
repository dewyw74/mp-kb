---
plugin_name: "Loudness Meter 2"
developer: "Youlean"
category: "metering"
type: "free real-time loudness meter (integrated/short-term/momentary LUFS, loudness range, true peak)"
cpu_usage: "low"
best_genres:
  - pop
  - hip_hop
  - trap
  - k_pop
  - edm
strengths:
  - "Free version measures the full core loudness set — Integrated, Short-term, and Momentary LUFS, Loudness Range, and true peak — compliant with ITU-R BS.1770, EBU R128, and ATSC A/85, without the core measurements themselves being crippled or time-limited."
  - "Ships with built-in target presets for major streaming platforms (Spotify, YouTube, Apple Music) and broadcast delivery, so a track's reading can be checked directly against a specific platform's normalization target rather than a generic number."
  - "A single resizable, real-time scrolling-graph window displays LUFS, loudness range, true peak, and dynamics together, staying legible at any window size — useful for leaving open across an entire mastering pass rather than only glancing at it occasionally."
  - "Extremely low CPU cost and zero cost to acquire have made it one of the most widely installed loudness meters in home and project studios, meaning its readings are a common shared reference point between collaborators even when they're not using the same DAW or paid metering plugin."
weaknesses:
  - "The free version's Dynamics graph, batch loudness analysis across multiple files, timeline markers, loudness-report export, and the full, regularly-updated set of streaming-platform presets are reserved for the paid Pro version — the free tier covers accurate real-time measurement but not deeper file-analysis or documentation workflows."
  - "As a loudness-and-true-peak specialist, it has no spectrum analyzer, phase/correlation, or spectrogram module — it needs to be paired with a separate tool (`knowledge_base/vst_database/voxengo_span.md`) for spectral analysis, unlike an all-in-one suite such as `knowledge_base/vst_database/izotope_insight_2.md`."
alternatives:
  - "iZotope Insight 2 (paid, full metering suite adding spectrum/spectrogram/phase modules alongside loudness — see `knowledge_base/vst_database/izotope_insight_2.md`)"
  - "Voxengo SPAN (free, adds EBU R128 LUFS/LU metering alongside its primary spectrum-analysis focus — see `knowledge_base/vst_database/voxengo_span.md`)"
  - "iZotope Ozone's built-in loudness/codec-preview metering, when checking loudness inside an already-open mastering-suite instance (see `knowledge_base/vst_database/izotope_ozone.md`)"
recommended_settings:
  - "Streaming-competitive master check: Integrated LUFS reading watched against the genre's documented target per `knowledge_base/mastering/loudness/lufs_targets_by_genre.md`, using the built-in Spotify/YouTube/Apple Music presets to compare against each platform's normalization point per `knowledge_base/mastering/streaming/platform_normalization_behavior.md`."
  - "True-peak safety check before export: true-peak readout watched for headroom of -1dBTP or lower per `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md`, independent of whatever the Integrated LUFS reading shows."
  - "Section-level dynamics monitoring on dynamics-preserving genres (post_rock, progressive_rock): Short-term LUFS watched for a clearly visible gap between quiet and loud sections, per the continuous-monitoring approach in `knowledge_base/mastering/loudness/loudness_metering_workflow.md`."
common_uses:
  - "Fast, no-cost integrated/short-term/momentary LUFS and true-peak checking before exporting a mix or master"
  - "Checking a track's loudness against a specific streaming platform's normalization target using the built-in presets"
  - "A shared, zero-cost reference meter between collaborators who may not have access to the same paid metering plugin"
tags: ["youlean", "loudness-meter", "metering", "loudness", "lufs", "true-peak", "free", "mastering"]
---

# Loudness Meter 2

Loudness Meter 2 (Youlean) is a free, loudness-specialist metering plugin measuring Integrated, Short-term, and Momentary LUFS, Loudness Range, and true peak, compliant with ITU-R BS.1770, EBU R128, and ATSC A/85. Its combination of free core measurement, extremely low CPU cost, and a clear single-window interface has made it one of the most widely used loudness meters in home and project-studio contexts — for many producers it's the default tool for checking a mix or master's loudness against a target before export, independent of whether they own a paid metering suite.

## Measurement Character and Workflow Strengths

Unlike free spectrum-focused tools that add loudness metering as a secondary feature, Loudness Meter 2 is built around loudness measurement specifically, and its free version doesn't cripple the core numbers to push a Pro upgrade — Integrated, Short-term, and Momentary LUFS, Loudness Range, and true peak are all present and accurate at no cost. Its built-in streaming-platform target presets (Spotify, YouTube, Apple Music, and others) make it fast to check a track's reading directly against a specific platform's normalization point, which is the practical, day-to-day version of the broader mastering-decision framework documented in `knowledge_base/mastering/streaming/platform_normalization_behavior.md`. The single scrolling-graph window keeping LUFS, loudness range, true peak, and dynamics all visible at once supports leaving the meter running continuously through a mastering pass — the workflow `knowledge_base/mastering/loudness/loudness_metering_workflow.md` recommends over a single end-of-chain check — rather than treating loudness metering as a one-time pass/fail gate.

## Weaknesses

The free version's measurement accuracy is real, but the workflow tooling around it is deliberately limited to encourage a Pro upgrade: the Dynamics graph, batch analysis across multiple files, timeline markers, loudness-report export, and the fuller, regularly-updated set of streaming presets all require the paid version. For a single producer checking a single track's loudness before export, the free version is already sufficient; for a mastering engineer documenting loudness compliance across an album or a client roster of files, the Pro version's batch and reporting tools become genuinely necessary. It's also a loudness-only specialist — it has no spectrum, phase/correlation, or spectrogram display, so a separate spectral tool (`knowledge_base/vst_database/voxengo_span.md`) or an all-in-one suite (`knowledge_base/vst_database/izotope_insight_2.md`) is still needed for those measurements.

## Common Mistakes

**Reading only the Integrated LUFS figure and ignoring Short-term and Momentary.** Per `knowledge_base/mastering/loudness/lufs_short_term_vs_integrated_vs_momentary.md`, the Integrated figure only becomes meaningful once a meaningful portion of the track has played, and it can hide section-level or transient-level problems that the Short-term and Momentary windows catch in the moment.

**Treating the built-in streaming-platform presets as the only number that matters, and ignoring the genre's own documented target.** Per `knowledge_base/mastering/loudness/lufs_targets_by_genre.md`, a genre's own loudness convention (a dynamics-preserving post-rock target vs. a club-oriented festival-EDM target) can sit meaningfully above or below a given platform's normalization point — check both rather than mastering to only the platform preset.

**Assuming the free version's true-peak reading substitutes for a true-peak-aware limiter setting.** The meter reports true peak accurately, but it doesn't limit anything itself — the final limiter still needs its own true-peak/ISP-aware ceiling set per `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md`.

## Cross-References

- `knowledge_base/mastering/loudness/lufs_targets_by_genre.md` — the genre-specific Integrated-LUFS targets this meter is used to check a master against
- `knowledge_base/mastering/loudness/lufs_short_term_vs_integrated_vs_momentary.md` — the three loudness windows this meter displays simultaneously
- `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md` — the true-peak/ISP concern this meter's true-peak readout is used to catch
- `knowledge_base/mastering/loudness/loudness_metering_workflow.md` — the continuous, whole-pass metering workflow this meter's always-on scrolling display supports
- `knowledge_base/mastering/streaming/platform_normalization_behavior.md` — the streaming-platform normalization context this meter's built-in presets check against directly
- `knowledge_base/vst_database/izotope_insight_2.md` — a paid, full metering-suite alternative adding spectrum/spectrogram/phase modules alongside loudness
- `knowledge_base/vst_database/voxengo_span.md` — a free spectrum-analysis-focused counterpart, useful alongside this meter for the spectral measurements it doesn't provide
