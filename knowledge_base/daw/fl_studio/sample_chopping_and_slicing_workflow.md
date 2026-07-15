---
workflow_name: "FL Studio Sample Chopping and Slicing Workflow"
daw: "fl_studio"
category: "sampling"
goal: "Chop and slice samples in FL Studio using Slicex and the Playlist's native Slice tool for pad-mapped, rearrangeable chops, and Edison for manual slice-point placement and export, choosing one-shot vs. loop mode correctly once a chop lands in a Sampler channel."
steps:
  - "Drag the source sample onto a Channel Rack slot to load it directly into Slicex, FL Studio's current-generation slicer, for transient-based auto-slicing with per-slice pitch, filter, and effect control."
  - "Let Slicex auto-detect transients as a starting point, then manually add, remove, or nudge slice markers so chops land on musically useful boundaries rather than only where the transient detector fired."
  - "Confirm each Slicex slice is mapped across the keyboard/pad grid correctly, so chops can be re-triggered and re-ordered in the Piano roll or Channel Rack step sequencer like any other instrument."
  - "Alternatively, use the Playlist's Slice tool (toolbar icon, shortcut C) to manually cut an audio clip into separate Playlist-level pieces when the chop should stay as arrangement-timeline audio rather than becoming a pad-mapped instrument."
  - "For manual, sample-accurate slice-point placement or cleanup before chopping, open the source in Edison first — zoom in, place markers by hand, and use Edison's own slicing tools ahead of sending material to Slicex or the Playlist."
  - "Use Edison's region-export function to bounce individual slices out as separate audio files when the chops need to leave FL Studio or be re-imported as standalone one-shots rather than staying inside a slicer instrument."
  - "For any chop or one-shot loaded into a Sampler (Channel Sampler) instrument instead of Slicex, set playback mode explicitly: one-shot for hits and stabs that should always play in full regardless of note length, loop mode (with Loop Start/End points) for sustained or texture material that needs to sustain under a held note."
  - "Route the finished chopped instrument to its own Mixer insert per `knowledge_base/daw/fl_studio/mixer_routing_resampling_and_freezing.md` once slicing is complete."
related_plugins:
  - "Slicex"
  - "Fruity Slicer"
  - "Edison"
  - "FL Studio Sampler"
  - "FL Studio Playlist"
  - "FL Studio Channel Rack"
tags:
  - "fl-studio"
  - "sample-chopping"
  - "slicing"
  - "slicex"
  - "edison"
  - "sampler"
  - "workflow"
---

# FL Studio Sample Chopping and Slicing Workflow

FL Studio offers three distinct routes to a chopped sample, and picking the right one depends on what the chop needs to become: a pad-mapped, re-orderable instrument (Slicex), a manually cut piece of arrangement-timeline audio (the Playlist's Slice tool), or a hand-placed, exportable set of individual audio regions (Edison). This is a different job from `knowledge_base/daw/fl_studio/recording_and_audio_editing_workflow.md`, which covers using Edison to clean up and comp recorded takes — this entry covers chopping source material (breaks, vocal phrases, melodic loops) into new playable or rearrangeable pieces.

## Slicex: transient-based, pad-mapped chopping

Dragging a sample onto the Channel Rack loads Slicex, FL Studio's current-generation slicer, which replaced the older Fruity Slicer for most chopping work. Slicex auto-detects transients and maps each detected slice across the keyboard, so a drum break or vocal phrase becomes an instantly playable, re-orderable instrument — trigger slices in a different order in the Piano roll or step sequencer to flip a break's rhythm, or reprogram a chopped vocal phrase into a new melodic pattern. Slicex's advantage over the legacy Fruity Slicer is per-slice processing: pitch, filter, and effect settings can be adjusted per individual slice without affecting the others, and slices can be pitched independently to build melodic variations from a single chop.

Auto-detected transients are a starting point, not a finished result — manually add missing slice markers, remove false triggers from a busy or noisy source, and nudge marker positions so each chop starts exactly on the transient rather than slightly ahead or behind it.

## The Playlist's native Slice tool

For chopping that should stay as arrangement-timeline audio rather than becoming a pad-mapped instrument — cutting a vocal line into phrase-length pieces for rearranging directly on the Playlist, or trimming a sample into a few large sections — press C (or click the blade/Slice icon in the Playlist toolbar) and click the audio clip at each point that needs a cut. Each click splits the clip into two independently movable Playlist pieces, which is the right tool when the result should behave like arrangement audio (draggable, trimmable, fadeable in place) rather than a re-triggerable instrument.

## Edison: manual slice-point placement and export

Open a sample in Edison when slice points need sample-accurate manual placement — zoomed-in visual editing, placing markers by ear and eye rather than relying on transient detection, or cleaning a source before it's chopped by Slicex or the Slice tool. Edison also has its own slicing tools, useful when the chops need to leave the slicer entirely: use Edison's region-export function to bounce each slice out as its own audio file, for cases where the chopped material needs to be re-imported as standalone one-shots, shared outside the project, or dropped into FPC or a Sampler channel individually rather than staying inside a slicer instrument's pad map.

## One-shot vs. loop mode in the Sampler

Once a chop or any other sample is loaded into a Channel Sampler instrument (rather than staying inside Slicex), its playback mode determines how it responds to note length:

- **One-shot mode** plays the sample through in full regardless of how long the triggering note is held or how short the MIDI note is — correct for drum hits, vocal stabs, and most chopped one-shots, where the chop should always sound complete once triggered.
- **Loop mode** uses Loop Start/End points to sustain a defined region of the sample for as long as the note is held, correct for pad-like, textural, or sustained chops that need to hold under a long note rather than always playing a fixed-length hit.

Getting this wrong is audible immediately: a one-shot chop set to loop mode either cuts short on a short note or (if the region wraps) audibly stutters into a loop when it shouldn't; a genuinely sustained texture left on one-shot mode always plays its fixed length regardless of the note held, which breaks any part that's meant to sustain or fade with the performance.

## Common mistakes

Trusting Slicex's automatic transient detection without manually reviewing slice points on busy or low-transient source material, which produces chops that start slightly off from the actual hit. Using the Playlist's Slice tool when the material actually needed to become a re-triggerable, re-orderable instrument (Slicex was the right tool), leaving the producer manually copy-pasting Playlist clips to achieve what Slicex would have done natively. Leaving a chopped one-shot on loop mode by accident, which is one of the most common causes of an unexpectedly stuttering or unexpectedly-sustaining sample in an otherwise-correct pattern.
