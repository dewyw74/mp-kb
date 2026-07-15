---
workflow_name: "Reaper Sample Chopping, Slicing, and Audio-to-MIDI Workflow"
daw: "reaper"
category: "sampling"
goal: "Chop a loop or phrase into independent items with Dynamic Split's transient detection, load the resulting slices into ReaSamplomatic5000 for chromatic pad/MIDI triggering, and understand what audio-to-MIDI conversion in Reaper can and can't do natively versus with third-party tools."
steps:
  - "Select the source item and run Item > Dynamic split items (default shortcut D) to split the item at every detected transient, rather than manually cutting at each hit by ear."
  - "Adjust the transient sensitivity/threshold before committing — raising sensitivity catches more, quieter transients, lowering it keeps only the strongest hits — and preview the split points before finalizing."
  - "Treat each resulting slice as an ordinary independent item afterward: it can be moved, deleted, duplicated, or reordered on the timeline exactly like any other item, since Dynamic Split only cuts, it doesn't group the pieces."
  - "Load a single slice into a ReaSamplomatic5000 (RS5K) instance manually by dragging the item onto a track hosting RS5K, for one-off use of a specific hit."
  - "For chopping an entire loop into a chromatic instrument, use a community action such as 'mpl_Export selected items to RS5k instances on selected track' to place each slice into its own RS5K instance and map them across the keyboard in their original left-to-right order."
  - "Re-sequence the mapped slices by rearranging notes in the MIDI item that triggers the RS5K chain, turning the original loop into a new pattern rather than just replaying it as recorded."
  - "For genuine audio-to-MIDI conversion, know that Reaper has no single native 'audio to MIDI' command comparable to a built-in polyphonic transcription feature — the closest native-adjacent path is an SWS Extension-assisted FX-chain conversion action, and it works best on simple, monophonic material."
  - "For monophonic pitched material (bass, lead vocal, monophonic guitar lines), consider a pitch-to-MIDI plugin such as ReaTune as a lighter-weight option than full transcription."
  - "For polyphonic material (chords, full mixes), rely on a dedicated third-party tool (e.g., Melodyne) or an instrument-specific converter (e.g., a MIDI guitar pickup or plugin) rather than expecting Reaper's stock toolset to transcribe chords accurately."
  - "Cross-check any converted MIDI against the source audio by ear before building further parts on top of it — transcription accuracy degrades quickly with polyphony, sustain, and pitch bend."
related_plugins:
  - "ReaSamplomatic5000 (stock)"
  - "SWS/S&M Extension"
  - "ReaTune (stock)"
  - "Melodyne (third-party, polyphonic)"
tags:
  - "reaper"
  - "sampling"
  - "sample-chopping"
  - "dynamic-split"
  - "audio-to-midi"
  - "reasamplomatic5000"
  - "workflow"
---

# Reaper Sample Chopping, Slicing, and Audio-to-MIDI Workflow

Reaper's chopping workflow is built from two separate stock tools rather than one dedicated slicer device: Dynamic Split handles transient-based cutting, and ReaSamplomatic5000 (RS5K) handles chromatic playback of the resulting pieces. Audio-to-MIDI conversion, by contrast, has no equally native path — Reaper leans on the SWS Extension or third-party plugins rather than a single built-in transcription feature.

## Dynamic Split: Transient-Based Chopping

Item > Dynamic split items (shortcut D) analyzes the selected item and splits it at every point it detects as a transient, with an adjustable sensitivity/threshold that determines how many hits get caught. The output is a set of ordinary items sitting where the source item used to be — Dynamic Split only cuts, so each resulting slice is immediately editable, movable, or deletable on its own, the same as any item under Reaper's item-based editing model documented in `knowledge_base/daw/reaper/mixing_automation_and_item_based_editing_workflow.md`.

## Mapping Slices with ReaSamplomatic5000

A single chopped slice can be dragged straight into an RS5K instance for one-off triggering. For chopping a whole loop into a playable instrument, a community action (mpl_Export selected items to RS5k instances on selected track) automates the tedious part: it creates one RS5K instance per slice and maps them chromatically across the keyboard in their original order, so the loop can immediately be re-triggered or re-sequenced via MIDI. This mirrors the musical goal described DAW-agnostically in `knowledge_base/daw/workflow/sample_chop_selection_and_musicality_philosophy.md` and the equivalent Ableton path in `knowledge_base/daw/ableton/sample_chopping_and_slicing_workflow.md`, but Reaper reaches it by combining two independent stock tools rather than one built-in slicing mode.

## Audio-to-MIDI: A Narrower Native Path

Unlike DAWs with a built-in polyphonic audio-to-MIDI feature (see the contrast in `knowledge_base/daw/ableton/warping_and_audio_to_midi_conversion.md`), Reaper does not ship a single command that reliably transcribes chords or full mixes to MIDI. The closest native-adjacent route runs through the SWS Extension's FX-chain-based conversion action, which works acceptably on simple monophonic sources. For monophonic pitched parts, a pitch-to-MIDI plugin like ReaTune is a lighter option; for polyphonic material, a dedicated third-party transcription tool is the realistic choice rather than a stock Reaper feature.

## Common mistakes

Expecting Dynamic Split's sensitivity setting to get chosen correctly on the first try — it almost always needs at least one preview-and-adjust pass, especially on material with inconsistent hit volume. Another common mistake is assuming Reaper can transcribe polyphonic audio to MIDI out of the box the way some competing DAWs do; without SWS or a third-party plugin, there is no equivalent stock feature, and forcing simple monophonic tools onto chordal material produces unusable results.
