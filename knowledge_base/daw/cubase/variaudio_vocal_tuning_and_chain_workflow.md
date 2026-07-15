---
workflow_name: "Cubase VariAudio Pitch Correction and Vocal Chain Workflow"
daw: "cubase"
category: "vocal_editing"
goal: "Use Cubase's VariAudio to correct pitch, timing, and formant on monophonic vocal (or solo instrument) recordings directly in the Sample Editor, and place VariAudio in the right position in the vocal signal chain relative to comping and downstream mix processing."
steps:
  - "Select the recorded audio event, open the Sample Editor, and switch to the VariAudio tab in the Inspector so Cubase analyzes the clip and displays detected pitch as movable Segments over the waveform."
  - "For a long or noisy recording, run Audio > Bounce Selection (Replace) on the comped take first so VariAudio analyzes only the final selected audio, reducing analysis time and avoiding pitch-detection errors from discarded takes."
  - "Set the Smart Controls display to Default for common corrective moves, or All Smart Controls when a formant or fine-warp adjustment is needed, since the 12 available handles around a segment's edges change based on this setting."
  - "Drag a segment vertically to move it toward the target pitch — segments snap to the nearest semitone by default, and holding the modifier key gives cent-level fine adjustment instead."
  - "Use the Tilt/Rotate Anchor Point control on a segment to correct pitch drift within a single note without flattening its natural pitch curve entirely."
  - "Apply Quantize Pitch (with the Quantize slider set well short of 100%) to nudge segments toward the nearest scale tone while leaving some natural pitch variation, rather than snapping everything to a dead-flat semitone grid."
  - "Use the Straighten Pitch Curve control, scoped with the Set Range For Straighten Pitch Curve handles, to flatten only the wandering pitch inside a sustained note rather than the whole segment's contour."
  - "Drag a segment's Warp Start / Warp End handles (center-left and center-right of the segment) to time-stretch or time-compress that portion of the waveform when a syllable is early, late, or needs to be lengthened to sit on the beat."
  - "Move the Shift Formant slider (or drag the lower-left smart control when All Smart Controls is active) only when the pitch correction itself has audibly changed the singer's vocal character, since formant shifting is independent of the pitch and timing edits and should be used to restore, not exaggerate, natural timbre."
  - "Finish VariAudio editing and comping before adding corrective EQ, de-essing, compression, or creative pitch-effect plug-ins downstream, since VariAudio works on the raw monophonic recording and later stages assume pitch/timing are already settled."
related_plugins:
  - "Cubase VariAudio (stock)"
  - "Cubase Sample Editor"
  - "Cubase AudioWarp"
  - "Steinberg Frequency"
tags:
  - "cubase"
  - "variaudio"
  - "vocal-tuning"
  - "pitch-correction"
  - "formant"
  - "vocal-chain"
  - "editing"
---

# Cubase VariAudio Pitch Correction and Vocal Chain Workflow

VariAudio is Cubase's built-in pitch- and time-correction tool for monophonic material — lead vocals, doubles, and solo instrument lines. It works by analyzing a recorded audio event and superimposing pitch Segments over the waveform in the Sample Editor, each representing a stretch of audio identified as a single note's pitch content. Correction happens by manipulating these segments directly rather than through a separate plug-in window, which keeps tuning tied to the same audio event a producer is already comping and editing.

## Segment analysis and Smart Controls

Opening the VariAudio tab in the Sample Editor's Inspector triggers Cubase's pitch analysis and displays the result as segments on a piano-roll-style grid behind the waveform. Hovering over a segment reveals up to 12 Smart Controls arranged around its edges; the Smart Controls display can be set to show only the most commonly used handles (Default) or the full set (All), which matters because formant shifting and some warp handles are only visible in the All setting. For long or noisy recordings, bouncing the comped selection first (Audio > Bounce Selection, Replace) speeds up analysis and avoids segment errors carried over from audio that's no longer part of the final take.

## Pitch correction

The core corrective move is dragging a segment vertically toward the target pitch; segments snap to the nearest semitone, with a modifier key held down for cent-level fine-tuning instead. Quantize Pitch automates this across many segments at once, nudging them toward the nearest scale tone by a percentage set on the Quantize slider — keeping that percentage below 100% preserves some of the singer's natural pitch movement rather than producing a flat, robotic result. The Tilt/Rotate Anchor Point and the Set-Range-scoped Straighten Pitch Curve controls handle a different problem: correcting drift or wobble within a single sustained note without discarding its natural pitch curve outside the corrected range.

## Time correction with Warp segments

Independent of pitch, each segment's Warp Start and Warp End handles time-stretch or time-compress the audio bounded by that segment — the tool for nudging a syllable that lands early or late relative to the beat, without touching its pitch. Because pitch and timing controls live on the same segment but are manipulated through different handles, it's possible (and often necessary) to correct one without disturbing the other.

## Formant shifting

Formant shifting adjusts the resonant frequencies that define vocal timbre, independent of both pitch and timing — moving the Shift Formant slider (or dragging the corresponding Smart Control when All Smart Controls is enabled) does not itself change what note is sounding. It exists mainly to correct an artifact of pitch correction itself: shifting a note's pitch can also shift its formants in a way that reads as unnatural (a "chipmunk" or "cartoon" effect on larger corrections), and a small formant-shift adjustment back toward the original can restore a natural-sounding timbre.

## Where VariAudio sits in the chain

VariAudio operates on the raw monophonic recording inside the Sample Editor, before the audio event is bounced to a track and processed by the rest of the vocal chain. Corrective EQ, de-essing, compression, and any creative pitch-effect plug-ins should come after VariAudio editing and comping are finished, since they generally assume pitch and timing have already been settled — running heavy compression or de-essing before tuning makes pitch problems harder to hear and correct accurately. See `knowledge_base/mixing/vocal_processing/vocal_chain_signal_order.md` for the broader signal-order reasoning this applies, and `knowledge_base/daw/workflow/vocal_tuning_naturalness_and_comping_order_philosophy.md` for the cross-DAW philosophy of how much correction to apply before it reads as unnatural. For the equivalent workflow in other DAWs, see `knowledge_base/daw/ableton/vocal_tuning_and_comping_pipeline_workflow.md` and `knowledge_base/daw/fl_studio/vocal_tuning_and_comping_pipeline_workflow.md`.

## Common mistakes

Quantizing pitch to 100% by default and getting a flat, artificial-sounding vocal instead of leaving some natural variation. Correcting pitch on an uncomped, take-heavy audio event instead of bouncing the final comp first, which wastes analysis time and can pull segment data from discarded takes. Pushing a large pitch correction without checking whether formants need a small compensating shift back, and ending up with an unintentionally thin or cartoonish tone. Applying compression or de-essing before finishing VariAudio edits, making pitch problems harder to hear and correct precisely.
