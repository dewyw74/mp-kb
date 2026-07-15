---
workflow_name: "FL Studio Master Bus Chain and Export Workflow"
daw: "fl_studio"
category: "mastering"
goal: "Build a master-bus processing chain on FL Studio's Master insert using native and third-party EQ, compression, and limiting, monitor loudness and true peak while doing it, and render the final file with export settings appropriate to the delivery target."
steps:
  - "Confirm the mix reaches Master with headroom per `knowledge_base/daw/fl_studio/mixing_bus_routing_and_gain_staging_workflow.md` before adding any master-bus processing."
  - "Insert an EQ first on the Master chain (Fruity Parametric EQ 2, or fabfilter_pro_q_3 if available) for broad tonal correction — a gentle high-pass and any wide corrective moves, not creative sound design."
  - "Insert a compressor or multiband dynamics stage next (Maximus, or fabfilter_pro_mb) to control dynamic range across the mix, watching gain-reduction depth per band rather than compressing uniformly."
  - "Insert a brick-wall limiter last in the chain (Fruity Limiter, or waves_l2_ultramaximizer / fabfilter_pro_l_2) to set the final ceiling and catch transient peaks the earlier stages miss."
  - "Insert a loudness meter (youlean_loudness_meter_2) and/or a true-peak-capable analyzer (voxengo_span) on the Master insert to monitor integrated LUFS and true peak while adjusting the chain, per `knowledge_base/mastering/loudness/loudness_metering_workflow.md`."
  - "Set the limiter's ceiling with true-peak margin rather than a hard 0 dBFS target, per `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md`."
  - "Check the resulting integrated LUFS against the platform or genre target in `knowledge_base/mastering/loudness/lufs_targets_by_genre.md` before finalizing gain-reduction depth."
  - "Open File > Export > Wave file (Ctrl+R) and set sample rate, bit depth, and dithering for the delivery target rather than leaving export settings on their defaults."
  - "Render to disk, then reopen the rendered file to confirm actual peak, loudness, and audible artifacts match what the Master insert's meters showed during mixing."
related_plugins:
  - "FL Studio Mixer"
  - "Fruity Parametric EQ 2"
  - "Maximus"
  - "Fruity Limiter"
  - "fabfilter_pro_q_3"
  - "fabfilter_pro_mb"
  - "fabfilter_pro_l_2"
  - "waves_l2_ultramaximizer"
  - "youlean_loudness_meter_2"
  - "voxengo_span"
tags:
  - "fl-studio"
  - "mastering"
  - "master-bus"
  - "loudness"
  - "true-peak"
  - "export"
  - "render"
  - "workflow"
---

# FL Studio Master Bus Chain and Export Workflow

FL Studio ships enough native mastering-capable plugins — Fruity Parametric EQ 2, Maximus, Fruity Limiter — to build a complete master-bus chain without buying anything, and swapping in third-party equivalents from `knowledge_base/vst_database/` is a drop-in choice at any of the three stages rather than a workflow change. What matters more than which specific plugin fills each slot is chain order, gain-staging discipline going in, and metering discipline going out — the export step is where an otherwise-good master gets undone by wrong render settings.

## Chain order: EQ, then dynamics, then limiter

Put an EQ first (Fruity Parametric EQ 2, or `fabfilter_pro_q_3` for a steeper/cleaner high-pass and more surgical corrective moves) so the dynamics stage downstream reacts to an already-tonally-corrected signal rather than compressing around a problem an EQ move could fix more cheaply. Keep master-bus EQ moves broad and corrective — a high-pass below the musical low end, small wide shelves — not the creative shaping that belongs in the mix itself.

Follow with a compressor or multiband dynamics stage. Maximus is FL Studio's native multiband option, splitting the signal into bands and allowing independent compression/limiting per band; `fabfilter_pro_mb` is a common third-party substitute with a more visual band-editing interface. Watch per-band gain-reduction depth rather than judging the stage by ear alone — more than a few dB of consistent reduction on any one band usually means the mix has an underlying balance problem the master stage shouldn't be asked to fix.

Finish with a brick-wall limiter — Fruity Limiter natively, or `waves_l2_ultramaximizer` / `fabfilter_pro_l_2` as third-party alternatives. The limiter's job is catching whatever peaks the earlier stages didn't already control and setting the final ceiling; it should be doing noticeably less work than the dynamics stage ahead of it if the chain is balanced correctly.

## Metering: loudness and true peak together

Insert `youlean_loudness_meter_2` on the Master chain to read integrated, short-term, and momentary LUFS while adjusting the chain — see `knowledge_base/mastering/loudness/lufs_short_term_vs_integrated_vs_momentary.md` for what each window actually tells you. `voxengo_span` (or any true-peak-capable analyzer) catches inter-sample peaks that a sample-peak-only meter misses, which matters directly at the limiter stage: setting a limiter's ceiling to a hard 0 dBFS sample-peak target routinely still produces true-peak overs after lossy encoding, per `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md`. Leave a small true-peak margin (commonly around -1 dBTP) rather than limiting flush to digital zero.

Check the resulting integrated LUFS against `knowledge_base/mastering/loudness/lufs_targets_by_genre.md` before calling the chain finished — pushing gain reduction deeper to hit a louder number than the target genre or platform actually rewards just trades dynamics for a loudness figure that gets turned down anyway on normalization-aware platforms, per `knowledge_base/mastering/loudness/normalization_aware_mastering_decisions.md`.

## Export settings

`File > Export > Wave file` (or Ctrl+R) opens FL Studio's render window, which handles sample rate, bit depth, and dithering independently of the project's working settings:

- **Sample rate**: match the project's working sample rate unless the delivery target specifically requires a different one (44.1 kHz remains the standard streaming/CD delivery rate).
- **Bit depth**: render at 24-bit for a master/delivery file so there's headroom for any further processing downstream; reserve 16-bit for a genuinely final consumer file.
- **Dithering**: leave off when rendering a 24-bit file that may still be processed further; enable dithering only on the final bit-depth-reducing step (24-bit down to 16-bit), not on every intermediate render.
- **Disk rendering** happens at FL Studio's internal 32-bit floating-point precision regardless of interface settings, so the render quality is not limited by the audio interface's own bit depth.

## Common mistakes

Setting the limiter's output ceiling to exactly 0 dBFS and treating that as safe, when true-peak overs can still occur after the file is encoded or converted — leave true-peak margin instead. Chasing a louder LUFS number than the genre or platform target calls for, which mostly just triggers normalization turn-down and sacrifices dynamics for nothing. Leaving dithering enabled on every render pass instead of only the final bit-depth-reduction step, which stacks unnecessary noise across iterative masters. Never reopening the rendered file to confirm it actually matches what the Master insert's meters showed — export settings and plugin bugs both occasionally produce a rendered file that doesn't match the in-DAW preview.

## Alternatives

For tracks headed to a separate mastering engineer rather than a self-mastered release, skip the limiter/loudness-target stages entirely and export a clean, headroom-preserving stem (per the gain-staging target in `knowledge_base/daw/fl_studio/mixing_bus_routing_and_gain_staging_workflow.md`) instead of a already-limited "mastered" bounce — a pre-limited file gives the mastering engineer nothing to work with.
