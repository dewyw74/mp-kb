---
plugin_name: "Insight 2"
developer: "iZotope"
category: "metering"
type: "comprehensive real-time metering and analysis suite (loudness, spectrum, phase/soundfield, spectrogram, levels)"
cpu_usage: "medium"
best_genres:
  - pop
  - hip_hop
  - trap
  - post_rock
  - techno
strengths:
  - "Bundles every metering module a mixing/mastering pass typically needs — Loudness (Momentary/Short-term/Integrated/Loudness Range per ITU-R BS.1770), Levels, Spectrum, a 3D-topographical Spectrogram, and a Sound Field/Phase module with Stereo Vectorscope and Surround Scope — into one plugin instance rather than requiring several separate meters."
  - "Fully compliant with ITU-R BS.1770-1/2/3/4 and EBU R128, with adjustable targets for additional broadcast standards (ATSC A/85, OP-59), so the same instance covers music-streaming and broadcast/post-production loudness-compliance work."
  - "Loudness History lets loudness be visualized and inspected over time — in real time during a pass or retrospectively after playback — with an exportable log/graph for documenting a project's loudness data."
  - "Surround support from stereo up to 7.1.2 Atmos makes it one of the few metering suites usable for both a conventional stereo master and an immersive/Atmos mix in the same tool."
weaknesses:
  - "Running Loudness, Spectrum, Spectrogram, and Sound Field modules simultaneously carries meaningfully more CPU and screen-real-estate overhead than a single-purpose loudness meter (Youlean Loudness Meter 2) or spectrum analyzer (Voxengo SPAN) — most mixing/mastering passes don't need every module active at once."
  - "As a paid, full-priced suite, it's a heavier investment than the free loudness- and spectrum-analysis alternatives that cover the same core BS.1770/EBU R128 loudness measurements at no cost."
alternatives:
  - "Youlean Loudness Meter 2 (free, loudness-focused alternative covering the same core LUFS/true-peak measurements — see `knowledge_base/vst_database/youlean_loudness_meter_2.md`)"
  - "Voxengo SPAN (free, spectrum-analysis-focused alternative when only spectral/correlation metering is needed — see `knowledge_base/vst_database/voxengo_span.md`)"
  - "iZotope Ozone's built-in metering and codec-preview tooling, when loudness/true-peak checking is wanted inside an already-open mastering-suite instance rather than a separate meter (see `knowledge_base/vst_database/izotope_ozone.md`)"
recommended_settings:
  - "Streaming-competitive master check: Loudness module set to Integrated + Short-term readouts, target loudness set to the genre's documented figure per `knowledge_base/mastering/loudness/lufs_targets_by_genre.md`, true-peak ceiling alarm set at -1dBTP or lower per `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md`."
  - "Full loudness-metering workflow across a mastering pass: Loudness History left running continuously from initial gain staging through the final limiter, per the step-by-step process in `knowledge_base/mastering/loudness/loudness_metering_workflow.md`, rather than checked only once at the end."
  - "Mono-compatibility and phase troubleshooting: Sound Field module's Stereo Vectorscope watched alongside correlation readout when checking club-system/mono translation per `knowledge_base/mixing/stereo/mid_side_processing_and_mono_compatibility.md`."
common_uses:
  - "All-in-one loudness, true-peak, and spectral verification during a mastering pass, replacing several separate single-purpose meters"
  - "Documenting/archiving a delivered project's loudness compliance data (broadcast delivery, streaming-platform QC) via exportable loudness logs"
  - "Stereo and surround/Atmos phase and spatial-balance diagnosis via the Sound Field module"
tags: ["izotope", "insight-2", "metering", "loudness", "lufs", "true-peak", "spectrum-analyzer", "phase", "mastering"]
---

# Insight 2

Insight 2 (iZotope) is a real-time metering and analysis suite that combines loudness metering (Momentary/Short-term/Integrated/Loudness Range, compliant with ITU-R BS.1770-1/2/3/4 and EBU R128), a true-peak meter, a spectrum analyzer, a 3D topographical spectrogram, and a Sound Field module (Stereo Vectorscope and Surround Scope) into one plugin instance. Unlike the free, single-purpose metering tools documented alongside it in this knowledge base (`knowledge_base/vst_database/youlean_loudness_meter_2.md`, `knowledge_base/vst_database/voxengo_span.md`), Insight 2 doesn't specialize in one measurement — it's built to be the one meter left open across an entire mixing and mastering session, covering loudness compliance, spectral balance, and stereo/surround phase behavior from a single window.

## Measurement Character and Workflow Strengths

Insight 2's Loudness module directly supplies the readouts this knowledge base's mastering guidance is built around: `knowledge_base/mastering/loudness/lufs_short_term_vs_integrated_vs_momentary.md`'s three metering windows, and the true-peak/ISP margin discussed in `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md`, are both present simultaneously rather than requiring separate plugins. Loudness History extends that further into a session-length record — a mastering engineer can watch a track's short-term reading diverge between a quiet verse and a loud chorus in real time (the exact contrast `knowledge_base/mastering/loudness/lufs_targets_by_genre.md` warns against flattening in dynamics-preserving genres like post-rock) and export the resulting log as documentation of the delivered master's loudness behavior. The Sound Field module's Stereo Vectorscope and correlation display give a fast, visual read on the mono-compatibility concerns central to `knowledge_base/mixing/stereo/mid_side_processing_and_mono_compatibility.md`, and its surround/Atmos support (up to 7.1.2) extends that same phase and spatial-balance checking to immersive mix formats that a conventional stereo-only meter can't address at all.

## Weaknesses

Running every module (Loudness, Spectrum, Spectrogram, Sound Field, Levels) at once is measurably heavier on CPU and screen space than a single-purpose meter, and for a large fraction of day-to-day mixing/mastering tasks — just checking integrated LUFS and true peak before an export, say — that full module set is more than the task actually needs. Insight 2 is also a paid, full-priced product, where the same core BS.1770/EBU R128 loudness measurement is available at no cost from `knowledge_base/vst_database/youlean_loudness_meter_2.md`, and the same core spectral/correlation measurement is available at no cost from `knowledge_base/vst_database/voxengo_span.md` — Insight 2's value proposition is consolidation and surround support rather than access to measurements otherwise unavailable.

## Common Mistakes

**Leaving every module active and CPU-loaded across a whole session when only one measurement (typically Loudness) is actually needed for the task at hand.** Disabling unused modules, or reaching for a lighter single-purpose meter instead, avoids unnecessary overhead.

**Checking the Loudness module's Integrated reading only once at the very end of a mastering pass**, rather than watching Loudness History continuously through the pass as described in `knowledge_base/mastering/loudness/loudness_metering_workflow.md` — a single end-of-chain check misses problems (an over-limited section, an unexpected true-peak overshoot) that a continuous-monitoring workflow catches while there's still time to fix them.

**Trusting a sample-peak-only reading instead of the true-peak (BS.1770-4-compliant) meter when checking streaming-delivery safety.** Insight 2's true-peak meter exists specifically to catch the inter-sample overshoots a sample-peak meter can't see, per `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md`.

## Cross-References

- `knowledge_base/mastering/loudness/lufs_targets_by_genre.md` — the genre-specific integrated-LUFS targets Insight 2's Loudness module is used to hit
- `knowledge_base/mastering/loudness/lufs_short_term_vs_integrated_vs_momentary.md` — the three loudness-metering windows Insight 2 displays simultaneously
- `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md` — the true-peak/ISP concern Insight 2's BS.1770-4-compliant true-peak meter is built to catch
- `knowledge_base/mastering/loudness/loudness_metering_workflow.md` — the continuous, whole-session metering workflow Insight 2's Loudness History module is suited to
- `knowledge_base/mastering/streaming/platform_normalization_behavior.md` — the streaming-platform normalization context Insight 2's loudness targets are commonly checked against
- `knowledge_base/mixing/stereo/mid_side_processing_and_mono_compatibility.md` — the mono-compatibility concern Insight 2's Sound Field/correlation display is used to diagnose
- `knowledge_base/vst_database/youlean_loudness_meter_2.md` — a free, loudness-focused alternative for the same core BS.1770/EBU R128 measurements without Insight 2's full module set
- `knowledge_base/vst_database/voxengo_span.md` — a free, spectrum-focused alternative when only spectral/correlation metering is needed
- `knowledge_base/vst_database/izotope_ozone.md` — iZotope's mastering-suite plugin, which includes its own lighter-weight loudness/codec-preview metering inside an already-open processing chain
