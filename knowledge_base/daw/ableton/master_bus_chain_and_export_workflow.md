---
workflow_name: "Ableton Master-Bus Chain and Export Workflow"
daw: "ableton"
category: "mastering"
goal: "Build a master-bus processing chain in Ableton Live (corrective EQ, glue compression, limiting), insert a loudness and true-peak meter to monitor the result, and choose correct export/render settings for a final delivery bounce."
steps:
  - "Keep master-bus processing off or minimal during mixing, and only build the full master chain once the mix itself is settled, per `knowledge_base/daw/ableton/mixing_bus_routing_and_gain_staging_workflow.md`."
  - "Insert EQ Eight first on the Master Track for broad, corrective tonal moves (not creative sound design) informed by `knowledge_base/mastering/eq/subtractive_mastering_eq_philosophy.md`."
  - "Insert a Compressor or Glue Compressor after the EQ for light mix-bus cohesion, using a low ratio and slow-to-medium attack so gain reduction stays around 1-3dB."
  - "Insert Ableton's stock Limiter (or a third-party mastering limiter) as the final device in the chain, with its ceiling set in True Peak mode rather than a plain sample-peak mode."
  - "Set the Limiter's true-peak ceiling to roughly -1dBTP or lower, independent of whatever integrated loudness target the genre calls for, per `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md`."
  - "Insert a LUFS-capable loudness meter on the Master Track, positioned after the limiter, to read momentary, short-term, and integrated loudness while auditioning the full track."
  - "Gain-stage into the target loudness rather than relying on the limiter alone to carry the whole distance, per `knowledge_base/mastering/loudness/loudness_metering_workflow.md`."
  - "Open Live's Export Audio/Video dialog, match the Sample Rate to the project's working sample rate, and choose 24-bit PCM (WAV or AIFF) as the delivery bit depth rather than converting sample rate unnecessarily."
  - "Leave Normalize off for a mastering export, since the limiter is already controlling the ceiling and a post-limiter normalize pass can undo carefully-set true-peak headroom."
  - "Only apply dithering on the final bit-depth-reducing bounce (e.g. 24-bit to 16-bit for CD delivery), and never on a same-bit-depth or higher-resolution export."
related_plugins:
  - "Ableton EQ Eight"
  - "Ableton Compressor"
  - "Ableton Glue Compressor"
  - "Ableton Limiter"
  - "FabFilter Pro-L 2"
  - "Waves L2 Ultramaximizer"
  - "Youlean Loudness Meter 2"
  - "Voxengo SPAN"
tags:
  - "ableton"
  - "mastering"
  - "master-bus"
  - "limiter"
  - "export"
  - "loudness"
  - "true-peak"
---

# Ableton Master-Bus Chain and Export Workflow

Once a mix is settled, the Master Track becomes a small, dedicated mastering chain rather than a passive summing point. This entry covers building that chain inside Ableton — EQ, glue compression, and limiting in order — inserting a loudness/true-peak meter to monitor it, and choosing export settings that don't quietly undo the work. It assumes the gain-staging discipline documented in `knowledge_base/daw/ableton/mixing_bus_routing_and_gain_staging_workflow.md` is already in place: a master chain built on top of an already-hot, unmanaged mix has far less room to work correctly.

## Building the Chain in Order

**EQ Eight first.** Use it for broad, corrective moves — trimming a resonant low-mid buildup, adding gentle high-frequency air — rather than creative sound design, per `knowledge_base/mastering/eq/subtractive_mastering_eq_philosophy.md` and `knowledge_base/mastering/eq/mastering_eq_vs_mix_eq_role.md`. Mastering-stage EQ moves are typically small and broad-strokes compared to mix-stage EQ.

**Compressor or Glue Compressor second.** A low ratio (roughly 1.5:1 to 2.5:1), slow-to-medium attack, and light gain reduction (1-3dB) links the mix's dynamics together without becoming audible as compression, per `knowledge_base/mixing/compression/bus_glue_compression.md`'s full-mix-bus use case. Push this further only when the genre treats audible glue as part of its identity rather than a transparent finishing step.

**Limiter last.** Ableton's stock Limiter device (Live 12.1 and later) offers Standard and True Peak modes, a Ceiling control, Gain, Lookahead, and Auto Release. Use True Peak mode so the limiter accounts for inter-sample overshoot rather than only sample-accurate peaks — see `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md` for why this matters even after the integrated LUFS target is already met. A third-party limiter such as `knowledge_base/vst_database/fabfilter_pro_l_2.md` or `knowledge_base/vst_database/waves_l2_ultramaximizer.md` can substitute here when its specific character or metering suits the material better than the stock device.

## Loudness and True-Peak Metering

Insert a dedicated LUFS meter after the limiter — `knowledge_base/vst_database/youlean_loudness_meter_2.md` or `knowledge_base/vst_database/voxengo_span.md` (SPAN's loudness module) both work — and leave it running for the whole playback pass rather than checking once at the end. Watch momentary, short-term, and integrated readouts together, per `knowledge_base/mastering/loudness/loudness_metering_workflow.md`: integrated only converges to a trustworthy number once most of the track has played, so short-term and momentary behavior is what actually gets watched moment to moment. Gain-stage toward the genre's documented target (see `knowledge_base/mastering/loudness/lufs_targets_by_genre.md`) before leaning on the limiter, so the limiter is doing comparatively little work rather than carrying the entire loudness gain alone.

## Export and Render Settings

Open Export Audio/Video and match **Sample Rate** to the project's working rate — converting sample rate on export can introduce artifacts that weren't audible during mixing, so avoid changing it unless a specific delivery spec requires it. For **Bit Depth**, 24-bit PCM is the standard choice for a mastering export; Ableton's internal engine runs at 32-bit float, but 24-bit delivery captures effectively all of that resolution without the file-size cost of 32-bit float delivery. Leave **Normalize** off: the limiter's ceiling is already the intended control point, and a normalize pass applied after export defeats the true-peak headroom that was deliberately set on the limiter.

If a lower delivery bit depth is genuinely required (16-bit for legacy CD delivery), apply dither exactly once, at that final bit-depth-reducing bounce only, per `knowledge_base/mastering/format/dithering_and_bit_depth_conversion.md` — never on a 24-to-24 or higher-resolution export, and never with further processing applied afterward.

## Common mistakes

Building the full master chain while still mixing, so EQ and compression decisions get made against a moving target instead of a settled mix. Using the Limiter's Standard (sample-peak) mode instead of True Peak mode, leaving inter-sample overshoot unmanaged even when the integrated loudness reading looks correct. Normalizing after limiting, which silently changes the carefully-set true-peak ceiling. Converting sample rate on export without a delivery reason to do so. Checking the loudness meter only once at the very end of a pass instead of watching it throughout, per `knowledge_base/mastering/loudness/loudness_metering_workflow.md`'s common-mistakes guidance.
