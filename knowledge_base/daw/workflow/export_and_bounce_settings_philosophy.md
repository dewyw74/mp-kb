---
workflow_name: "Export and Bounce Settings Philosophy"
daw: "generic"
category: "mastering"
goal: "Choose sample rate, bit depth, format, dither, and headroom settings for a final export so the file serves its destination — mastering handoff, streaming release, or archival — without introducing avoidable quality loss."
steps:
  - "Identify the destination before choosing any export setting: mastering handoff, direct-to-streaming release, sample/stem library, or session archive each imply different choices."
  - "Export at the session's native sample rate rather than converting, unless the destination explicitly requires a different rate."
  - "Bounce at the highest bit depth the session supports (24-bit or 32-bit float) for any file that will be processed further, and reserve 16-bit for a genuinely final consumer file."
  - "Apply dither only on the final bit-depth reduction step, and only once, at the very end of the processing chain."
  - "Never apply dither on a sample-rate conversion alone if bit depth is not also being reduced in that same step."
  - "Leave 3-6 dB of true-peak headroom under 0 dBFS on any mix bounced for a mastering engineer, and do not place a limiter or peak-hunting maximizer on the master bus before that bounce."
  - "Export uncompressed PCM (WAV or AIFF) for any handoff to another engineer or process; reserve lossy formats for final listener-facing distribution only."
  - "Decide whether the mastering engineer needs a single stereo mixdown, a set of mix stems, or both, and confirm before bouncing rather than after."
  - "Label bounced files with version, date, and content clearly enough that an old bounce can never be mistaken for the current one."
  - "Re-check the bounce by ear against the session, not just by confirming the export completed without errors."
related_plugins: []
tags:
  - "export"
  - "bounce"
  - "mastering"
  - "dither"
  - "headroom"
  - "file-format"
  - "workflow"
  - "generic"
---

# Export and Bounce Settings Philosophy

Export settings are usually treated as an afterthought — a dialog box to click through once the creative work is done — but the choices made there determine whether the effort in the mix survives the handoff intact. Sample rate, bit depth, dither, format, and headroom are not interchangeable defaults; each answers a different question about what the file is for and where it goes next. This entry covers the reasoning behind those choices independent of any one DAW's export dialog.

## Sample Rate: Match the Session, Don't Convert by Default

The safest sample-rate decision is usually the simplest one: export at whatever rate the session was recorded and mixed in. Converting sample rate is a lossy, filtering-heavy operation — it requires a low-pass filter to remove content above the new Nyquist frequency and a resampling algorithm to regenerate the waveform at new time intervals, both of which introduce some error even in well-implemented converters. There is rarely a good reason to convert mid-pipeline. Convert only at the final step, and only when the destination genuinely requires a different rate (a streaming platform's ingest spec, a video project's audio rate, a client's stated requirement). Doing the conversion once, at the end, with a high-quality converter, is far safer than converting early and then processing further at the new rate.

## Bit Depth: 24/32-bit for Anything Still in the Chain, 16-bit Only at the Very End

Any file that will be opened again for further processing — sent to a mastering engineer, reimported as a stem, archived for a future remix — should be bounced at 24-bit or 32-bit float, matching or exceeding the session's working bit depth. Reducing to 16-bit throws away resolution that cannot be recovered later, and unlike sample rate the practical downside is asymmetric: there is essentially no cost to keeping a working file at higher bit depth, but real cost to prematurely truncating it. 16-bit is the correct final choice only for the last step, producing a file intended to be listened to and not touched again (a CD-spec master or a delivery format that requires it).

## When Dither Actually Matters

Dither adds a small amount of shaped noise to mask the quantization distortion that occurs when a signal's bit depth is reduced. It matters specifically and only at that moment: the step where word length is being truncated, for example bouncing a 32-bit float mix down to 16-bit for final delivery. It does not matter for a same-bit-depth file copy, and it is not inherently required by sample-rate conversion — sample rate and bit depth are independent parameters, and resampling alone does not truncate word length. In practice, most sample-rate converters internally produce a longer word length than the source during their calculation, so if a rate conversion and a bit-depth reduction happen in the same export step, the truncation back down still needs dither; the trigger is the bit-depth reduction, not the rate change. Dither should be applied exactly once, at the last bit-depth-reducing step in the chain — applying it more than once, or applying it before further gain or processing is done to the file, defeats its purpose and can audibly degrade the result.

## Format Choice: PCM for Handoff, Compressed Only for Final Distribution

Uncompressed PCM formats (WAV, AIFF) preserve the audio exactly as bounced and should be the default for anything that isn't the literal final consumer-facing file: stems, mixdowns sent to a mastering engineer, samples destined for reuse, and archival copies. Lossy formats (MP3, AAC) throw away audio information permanently through psychoacoustic compression, and that loss compounds if a lossy file is ever decoded, processed, and re-encoded. Lossy formats are appropriate only at the very last step of a distribution chain, generated from a PCM master, never used as an intermediate working format.

## Stems vs. Single Mixdown for Mastering Handoff

A single stereo mixdown gives a mastering engineer one signal to shape with EQ, dynamics, and limiting; mix stems (typically grouped by function — drums, bass, music, vocals) give them the ability to make small balance adjustments as part of the mastering pass. Which one is needed depends on how finished the mix is and how the engineer works: a confident, finished mix usually only needs a stereo bounce, while a mix with a known balance question, or a mastering engineer who explicitly works from stems, benefits from having both. Deciding this before the session ends avoids a second round-trip bounce request later; when in doubt, exporting both a stereo mixdown and a basic stem set costs little extra time and covers either workflow.

## Headroom Before a Mastering Engineer's Limiter

A mix handed off for mastering should leave real peak headroom, typically in the range of 3-6 dB under 0 dBFS, with more dynamic mixes leaning toward the higher end of that range and denser, already-loud mixes needing less. This headroom exists so the mastering engineer's own dynamics processing and true-peak limiting have room to work without immediately hitting the ceiling, and so that inter-sample peaks created by later processing or format conversion do not clip. A limiter or loudness maximizer should not sit on the master bus of a file being bounced for mastering — that pre-squashes the dynamic range the mastering stage exists to shape, and effectively does the mastering engineer's job for them, badly, before they've even opened the file.

## Common Mistakes

**Converting sample rate mid-project instead of only at final export.** Every conversion pass introduces some error; doing it once, at the end, at the destination's actual required rate, minimizes cumulative loss.

**Bouncing working files at 16-bit "to save space."** Storage is cheap; lost resolution in a file meant for further processing is not recoverable.

**Applying dither on every bounce regardless of whether bit depth changed.** Dither is a targeted tool for one specific situation, not a blanket "quality" setting to leave on by default.

**Slamming the master bus with a limiter before a mastering handoff.** This removes the headroom and dynamic range the mastering engineer needs, and often forces them to undo work rather than build on it.

**Exporting only an MP3 for archival or handoff purposes.** A lossy file used as a working intermediate compounds quality loss every time it is reprocessed and re-encoded.

## Cross-References

- `knowledge_base/mastering/` — loudness targets, limiting approach, and platform normalization once the mix reaches the mastering stage this entry's headroom guidance is preparing it for.
- `knowledge_base/daw/workflow/reference_track_ab_comparison_workflow.md` — level-matching principles that apply equally when comparing pre-master bounces against reference material.
- `knowledge_base/daw/ableton/master_bus_chain_and_export_workflow.md` and `knowledge_base/daw/fl_studio/master_bus_chain_and_export_workflow.md` — the DAW-specific master bus chain and export dialog settings that implement the sample-rate, bit-depth, dither, and headroom principles in this entry.
