---
plugin_name: "SPAN"
developer: "Voxengo"
category: "metering"
type: "free real-time FFT spectrum analyzer with loudness, correlation, and true-peak metering"
cpu_usage: "low"
best_genres:
  - techno
  - house
  - dubstep
  - trap
  - ambient
strengths:
  - "Free version is a full-featured real-time FFT spectrum analyzer with configurable Fourier block size, FFT window overlap, and spectrum slope, plus a secondary spectrum display (real-time maximum or all-time maximum) for spotting problem frequencies that appear only briefly."
  - "Includes true peak and clipping statistics, a correlation meter, and EBU R128 LUFS/LU metering at no cost, alongside K-system metering, stereo/multi-channel and mid/side analysis, and 64-bit floating-point internal processing — a broader measurement set than the 'just a spectrum analyzer' reputation suggests."
  - "Multi-channel support lets two different channels or channel groups be displayed as spectrums simultaneously, useful for comparing a processed signal against its source or checking mid/side balance directly in one analyzer window."
  - "Extremely low CPU cost and zero acquisition cost make it practical to instantiate on many channels at once, or leave open on the master bus for the entire duration of a mixing session without hesitation."
weaknesses:
  - "The free version has no multi-track spectrum comparison/import-export, PNG export, static-spectrum overlay, or resizable UI — those workflow features are reserved for the paid SPAN Plus (~$45), so comparing this track's spectrum against a saved reference-track spectrum side by side isn't possible in the free version."
  - "As a spectrum-and-correlation specialist, its LUFS metering is a secondary feature rather than the dedicated momentary/short-term/integrated loudness-history workflow a loudness-specialist meter (`knowledge_base/vst_database/youlean_loudness_meter_2.md`) or a full suite (`knowledge_base/vst_database/izotope_insight_2.md`) provides."
alternatives:
  - "Voxengo SPAN Plus (paid upgrade adding multi-track spectrum comparison, PNG export, and a resizable UI — same core analyzer engine)"
  - "Youlean Loudness Meter 2 (free, loudness-specialist alternative when LUFS/true-peak tracking over time is the primary need — see `knowledge_base/vst_database/youlean_loudness_meter_2.md`)"
  - "iZotope Insight 2 (paid, full suite combining spectrum, spectrogram, loudness, and phase/soundfield metering in one instance — see `knowledge_base/vst_database/izotope_insight_2.md`)"
recommended_settings:
  - "General frequency-balance and masking check on a mix bus: default FFT settings with the secondary spectrum set to real-time maximum, watching for buildup or gaps against the genre's documented `frequency_balance` guidance in the relevant `knowledge_base/genres/` entry."
  - "Mono-compatibility check on a bass/sub channel: mid/side analysis mode engaged alongside the correlation meter, cross-checked against `knowledge_base/mixing/stereo/mid_side_processing_and_mono_compatibility.md`'s club-system-translation guidance."
  - "Quick loudness sanity check without opening a dedicated loudness meter: EBU R128 LUFS/LU readout and true-peak/clipping statistics watched directly, with a true-peak margin of -1dBTP or lower per `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md`."
common_uses:
  - "Real-time frequency-balance and masking diagnosis on individual channels or a mix bus, at effectively zero CPU or monetary cost"
  - "Correlation and mid/side checking for mono-compatibility troubleshooting"
  - "Fast EBU R128 LUFS and true-peak sanity checks without switching to a dedicated loudness meter"
tags: ["voxengo", "span", "metering", "spectrum-analyzer", "fft", "correlation", "free", "mixing"]
---

# SPAN

SPAN (Voxengo) is a free real-time FFT spectrum analyzer plugin, and one of the most widely installed free metering tools in mixing and mastering setups precisely because its free version isn't a stripped-down demo — it includes true peak and clipping statistics, a correlation meter, EBU R128 LUFS/LU metering, K-system metering, and stereo/mid-side multi-channel analysis alongside its core FFT spectrum display, all at 64-bit floating-point internal precision and effectively zero CPU cost. Where `knowledge_base/vst_database/youlean_loudness_meter_2.md` specializes in loudness-over-time tracking, SPAN's center of gravity is real-time spectral and correlation analysis, with loudness metering included as a genuinely useful secondary feature rather than the plugin's main purpose.

## Measurement Character and Workflow Strengths

SPAN's FFT engine is configurable at a level most free analyzers don't offer — block size, window overlap, and visual slope can all be adjusted, and a secondary spectrum trace (real-time maximum or all-time maximum) can be overlaid on the live spectrum, which is what makes it possible to catch a resonance or masking problem that only appears briefly during a busy section rather than being visible only in an instantaneous snapshot. Its multi-channel and mid/side analysis modes let two signals or a signal's mid and side content be viewed as separate overlaid spectrums in the same window, directly supporting the same mono-compatibility and stereo-image diagnosis documented in `knowledge_base/mixing/stereo/mid_side_processing_and_mono_compatibility.md` that the correlation meter also addresses from a different angle. Because it costs nothing and barely touches CPU, it's realistic to run an instance on several channels simultaneously (a lead, a bass, a mix bus) rather than reserving a single analyzer instance for one channel at a time — a genuine workflow advantage over heavier or licensed-per-machine alternatives.

## Weaknesses

The free version's limits are workflow-shaped rather than measurement-shaped: there's no way to import a saved reference-track spectrum for direct A/B overlay comparison, no PNG export for documentation, and no resizable analyzer window — all reserved for the paid SPAN Plus upgrade. For loudness work specifically, SPAN's EBU R128 LUFS/LU readout is useful as a quick sanity check, but it doesn't provide the dedicated Momentary/Short-term/Integrated breakdown and loudness-history logging that a loudness-specialist tool like `knowledge_base/vst_database/youlean_loudness_meter_2.md` or a full suite like `knowledge_base/vst_database/izotope_insight_2.md` is built around — for an actual mastering-loudness pass, SPAN is a supplement to a dedicated loudness meter, not a replacement for one.

## Common Mistakes

**Using SPAN's LUFS readout as the sole loudness reference during a full mastering pass**, rather than pairing it with a loudness-history-capable meter — SPAN's LUFS display is accurate but lacks the continuous Short-term/Momentary tracking that `knowledge_base/mastering/loudness/loudness_metering_workflow.md` describes as necessary for catching section-level problems, not just an end-of-chain integrated number.

**Reading only the live spectrum trace and ignoring the secondary maximum-hold trace**, which misses transient or intermittent frequency-balance problems (a brief resonance, an occasional masking clash) that don't show up in a single instantaneous snapshot but are clearly visible once the maximum-hold trace accumulates over playback.

**Expecting free-version SPAN to do saved-reference-track spectrum comparison.** That specific workflow — overlaying a reference track's saved spectrum against the current signal — requires SPAN Plus; the free version only compares channels/signals present in the current session in real time.

## Cross-References

- `knowledge_base/mixing/stereo/mid_side_processing_and_mono_compatibility.md` — the mono-compatibility and stereo-image concern SPAN's correlation meter and mid/side analysis mode are used to diagnose
- `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md` — the true-peak/ISP concern SPAN's true-peak and clipping statistics are used to catch
- `knowledge_base/mastering/loudness/loudness_metering_workflow.md` — the continuous, whole-pass loudness-metering workflow SPAN's LUFS readout supplements but doesn't replace
- `knowledge_base/vst_database/youlean_loudness_meter_2.md` — a free, loudness-specialist counterpart with the dedicated Momentary/Short-term/Integrated loudness-history tracking SPAN doesn't provide
- `knowledge_base/vst_database/izotope_insight_2.md` — a paid, full metering-suite alternative combining spectrum, spectrogram, loudness, and phase/soundfield modules in one instance
- `knowledge_base/vst_database/fabfilter_pro_q_3.md` — a commonly paired EQ whose frequency-balance decisions SPAN's spectrum display is often used to inform in real time
