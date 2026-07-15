---
workflow_name: "Studio One Impact XT Drum and Pattern Programming"
daw: "studio_one"
category: "sampling"
goal: "Program drums in Studio One using Impact XT's pad-based sampler (per-pad insert effects, velocity-switched sample layers, drag-and-drop loop slicing) together with the Pattern editor's step-sequencer workflow, rather than editing MIDI notes directly in the piano roll."
steps:
  - "Load Impact XT on an instrument track and drag samples from the Browser directly onto individual pads to build a kit, using the same drag-and-drop interaction Studio One uses for effects and routing elsewhere in the Console."
  - "Assign multiple sample layers to a single pad with separate velocity ranges (e.g. a body layer triggered at velocities 1-100 and an accent layer added on top at 101-127) so harder hits bring in extra character instead of just playing louder."
  - "Adjust each layer's own volume, pitch, pan, filter, and envelope independently to blend layers, and use each pad's own insert-effects slot to apply processing per drum (EQ on the kick, compression on the snare, saturation on the clap) before it reaches the Console channel."
  - "Drag a full loop onto Impact XT to have it auto-sliced across pads, generating a new MIDI Pattern that triggers the slices in their original order — a fast way to chop a break or vocal sample into a playable, editable kit instead of manually slicing in the audio editor."
  - "Create a Pattern by right-clicking the Impact XT track and choosing New Pattern, or using the pattern icon in the toolbar, then double-click the resulting clip to open the Pattern editor."
  - "Program steps directly in the Pattern editor, where every Impact XT pad automatically maps to its own lane with no manual setup required."
  - "Click-drag vertically on an active step to set its velocity (a taller bar plays louder), using this for hi-hat dynamics, ghost notes, and accents rather than leaving every step at a fixed velocity."
  - "Right-click a step to add repeat (ratchet) or probability settings for rolls, flams, and non-repeating variation without programming duplicate patterns by hand."
  - "Place different Pattern variations across multiple clip instances on the timeline, and stack more than one Pattern on the same track when a polyrhythm or a transition fill needs multiple patterns playing together."
  - "Reserve manual piano-roll MIDI editing for parts that need free-form pitched material Impact XT and Pattern mode aren't built for, keeping drum programming inside the pad/step workflow where velocity layers and per-pad effects are available."
related_plugins:
  - "Studio One Impact XT"
  - "Studio One Pattern Editor"
  - "Studio One Sample One XT"
tags:
  - "studio_one"
  - "impact-xt"
  - "drum-programming"
  - "pattern-editor"
  - "sampler"
  - "step-sequencer"
  - "velocity-layers"
---

# Studio One Impact XT Drum and Pattern Programming

Impact XT is Studio One's native pad-based drum sampler — 8 banks of 16 pads (128 pads total), each one a self-contained instrument with its own insert-effects chain, output routing, and sample layering rather than a single shared sample slot per pad. Paired with Studio One's Pattern editor, a classic drum-machine step-sequencer view that auto-maps every Impact XT pad to its own lane, it forms a drum-programming workflow distinct from editing MIDI notes directly in the piano roll.

## Building a kit with velocity-switched layers

Samples are loaded onto pads by dragging them from the Browser directly onto the pad grid, consistent with Studio One's broader drag-and-drop design philosophy described in `knowledge_base/daw/studio_one/song_setup_and_console_routing_workflow.md`. A single pad can hold multiple sample layers, each assigned its own velocity range — a common setup is a body layer covering velocities 1-100 and an accent layer added only at 101-127, so a hard hit brings in extra transient or harmonic content rather than simply playing the same sample louder. Each layer carries independent volume, pitch, pan, filter, and envelope controls for blending, and every pad has its own insert-effects slot, so a kick can get EQ, a snare compression, and a clap saturation entirely separately before the signal reaches the Console channel.

## Loop slicing as a shortcut to a playable kit

Dragging a full loop onto Impact XT triggers automatic slicing: the loop is chopped and distributed across pads, and Studio One generates a matching MIDI Pattern that triggers the slices in their original sequence. This turns a found break or vocal chop into an editable, re-triggerable kit in one drag, rather than manually slicing the audio in a sample editor and building a MIDI part by hand — see `knowledge_base/daw/workflow/sample_chop_selection_and_musicality_philosophy.md` for the general musical judgment involved in choosing chop points, which applies just as much to Impact XT's automatic slices as to manual ones.

## The Pattern editor

A Pattern is created by right-clicking the Impact XT track and choosing New Pattern, or via the pattern icon in the toolbar; double-clicking the resulting clip opens the step-edit Pattern editor, where every pad already has its own lane without additional configuration. Steps are toggled on by clicking, and clicking-and-dragging vertically on an active step sets that step's velocity — a taller bar plays louder — which is how hi-hat dynamics, ghost notes, and accents get programmed without hand-editing individual MIDI note velocities. Right-clicking a step exposes repeat (ratchet) and probability settings for rolls and non-repeating variation directly in the step grid. Multiple Pattern clips can hold different variations of the same kit, and more than one Pattern can be stacked on a single track to merge simultaneously for polyrhythms or transition fills. This step-based approach is Studio One's equivalent of the pad/step workflows covered for other DAWs in `knowledge_base/daw/ableton/drum_rack_pad_controller_workflow.md` and `knowledge_base/daw/fl_studio/channel_rack_step_sequencer_workflow.md`.

## Common mistakes

Manually recreating a loop's original groove note-by-note instead of using Impact XT's automatic loop-slicing-to-Pattern feature wastes the fastest path from sample to playable kit. Skipping velocity-range assignment when layering samples on a pad is another common gap — without configured ranges, layers either overlap and both trigger together or fail to switch at all, defeating the point of velocity layering. A third mistake is over-using step-level repeat and probability settings until the pattern reads as randomized rather than intentionally varied; both are best applied in small, deliberate amounts rather than maxed out across every step.
