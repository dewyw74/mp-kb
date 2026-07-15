---
workflow_name: "Cubase Sampler Track Slicing and Audio-to-MIDI Workflow"
daw: "cubase"
category: "sampling"
goal: "Chop an audio loop or phrase into playable slices using Cubase's Sampler Track, choose the right slicing mode (Transient, Grid, Manual) for the source material, and convert those slices into an editable MIDI phrase that can be rearranged, re-triggered, or layered against the original audio."
steps:
  - "Create a Sampler Track (Project > Add Track > Sampler, or drag an audio file directly onto an empty area of the track list) and drag the target loop or phrase into it rather than editing the source audio event directly."
  - "Open the Sampler Control's playback section and click Slice to enter slicing mode, then choose a Slice Mode appropriate to the material rather than leaving it on the default."
  - "Use Transient Mode for material with clear attack transients (drum loops, plucked or percussive phrases) — Cubase finds each transient and turns it into its own note, mapped sequentially up the keyboard from the root key."
  - "Use Grid Mode for material that should be divided at fixed rhythmic intervals regardless of transient content (a synth loop, a vocal chop meant to be sliced into even sixteenth notes) rather than wherever a transient happens to fall."
  - "Use Manual Mode when neither automatic method produces musically useful slice points, clicking directly in the waveform to place each slice boundary by ear."
  - "Adjust the Sensitivity or grid resolution after an automatic slice pass if it produces too many or too few slices, rather than accepting the first pass and manually deleting or adding slices afterward."
  - "Play the mapped slices from a MIDI keyboard or the Cubase virtual keyboard to audition the chopped material as a playable instrument before committing to any rearrangement."
  - "Click Drag MIDI Phrase to Project and drop it onto the event display to generate a MIDI part reproducing the original slice order and rhythm, giving an editable starting point rather than programming the pattern from scratch."
  - "Open the generated MIDI part in the Key Editor to reorder, requantize, retime, or add/remove notes, turning the original loop into a rearranged or otherwise transformed pattern built from its own slices."
  - "Decide per-project whether to mute the original audio loop and use only the triggered MIDI slices as the new part, or keep the original loop playing underneath and use the sliced MIDI to overdub fills, variations, or layered hits on top of it."
related_plugins:
  - "Cubase Sampler Track"
  - "Cubase Sampler Control"
  - "Cubase Key Editor"
  - "Cubase AudioWarp"
tags:
  - "cubase"
  - "sampler-track"
  - "slicing"
  - "audio-to-midi"
  - "sample-chopping"
  - "beat-slicing"
  - "sampling"
---

# Cubase Sampler Track Slicing and Audio-to-MIDI Workflow

Cubase's Sampler Track turns a dragged-in audio loop or phrase into a playable, sliceable instrument without leaving the main project window or opening a separate sampler plug-in. Slicing breaks the audio into segments mapped across the keyboard, and those slices can then be converted into an editable MIDI phrase — a fast way to chop a break, a vocal phrase, or a synth loop and rearrange it into something new, or to trigger the original material live from a controller.

## Creating a Sampler Track

A Sampler Track is added via Project > Add Track > Sampler, or created directly by dragging an audio file onto an empty part of the track list. Unlike editing an audio event's own clip properties, the Sampler Track treats the dragged-in file as sample content for a playable instrument from the start, which is the right starting point whenever the goal is triggering pieces of the material rather than just trimming or time-stretching the original event.

## Choosing a slicing mode

The Sampler Control's playback section offers a Slice button and a choice of Slice Mode, and picking the right mode for the source material matters more than accepting whatever mode was last used. Transient Mode detects the audio's attack transients and turns each one into its own note mapped sequentially up the keyboard from the root key — the right choice for drum loops or anything percussive where the musically important cut points are already marked by transients. Grid Mode ignores transients and instead divides the sample at fixed rhythmic intervals (sixteenth notes are a common starting resolution), which suits material that should be chopped evenly regardless of where its transients happen to fall — a sustained synth pad or a vocal phrase meant to be diced into regular rhythmic cells. Manual Mode places no automatic slices at all, requiring the user to click directly in the waveform to mark each boundary, useful when neither automatic method lands on musically useful points.

## Tuning the slice count

An automatic Transient- or Grid-mode pass rarely produces exactly the right number of slices on the first try. Adjusting the Sensitivity (Transient Mode) or grid resolution (Grid Mode) and re-running the slice pass is faster and more consistent than accepting an over- or under-sliced result and then manually adding or deleting individual slice points afterward.

## From slices to an editable MIDI phrase

Once slices exist and are mapped to the keyboard, clicking Drag MIDI Phrase to Project and dropping it onto the event display generates a MIDI part reproducing the original material's slice order and rhythm — a programmed starting point rather than a from-scratch pattern. That generated part opens like any other in the Key Editor, where notes can be reordered, requantized, retimed, or added and removed, turning a straight chop of the source loop into a genuinely rearranged pattern built from its own material.

## Layering slices against the original

A sliced Sampler Track can either replace the source loop entirely — muting the original audio and using only the triggered MIDI slices as the new part — or sit alongside it, with the sliced MIDI used to overdub fills, variations, or additional hits on top of the loop still playing underneath. Which approach fits depends on whether the goal is transformation of the original material or augmentation of it.

For the cross-DAW principles behind choosing musically useful slice points and deciding how much to rearrange versus preserve, see `knowledge_base/daw/workflow/sample_chop_selection_and_musicality_philosophy.md`; for the equivalent slicing workflows in other DAWs, see `knowledge_base/daw/ableton/sample_chopping_and_slicing_workflow.md` and `knowledge_base/daw/fl_studio/sample_chopping_and_slicing_workflow.md`.

## Common mistakes

Leaving Slice Mode on Transient for material with a weak or ambiguous attack (a soft pad, a heavily reverberant recording), producing missed or misplaced slice points that Grid Mode would have handled more predictably. Accepting an obviously over- or under-sliced automatic pass and hand-fixing it slice-by-slice instead of simply adjusting Sensitivity or grid resolution and re-running the slice operation. Dragging the MIDI phrase to the project and treating it as a finished part, rather than as an editable starting point meant to be rearranged in the Key Editor. Forgetting to mute the original audio loop when the intent was full replacement, resulting in the source material and the newly triggered slices playing back doubled.
