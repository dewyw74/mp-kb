---
workflow_name: "Launchpad and Grid Controller Performance Workflow"
daw: "ableton"
category: "performance"
goal: "Map Ableton Live's Session View to a grid controller such as Novation Launchpad for hands-on clip and scene performance, using the controller's Session Mode, color feedback, and Note Mode alongside macro mapping rather than relying on mouse-driven clip launching."
steps:
  - "Connect the grid controller and select its dedicated Live control-surface script in Preferences > Link/Tempo/MIDI so Session View is mapped automatically without manual MIDI mapping."
  - "Use Session Mode as the default grid state, where each pad corresponds one-to-one to a clip slot in the currently selected 8x8 (or controller-specific) region of Session View."
  - "Use the controller's scene-launch column (or dedicated scene buttons) to fire whole scenes from the hardware instead of reaching for the mouse."
  - "Read pad color feedback as clip state: a lit pad matching the clip's assigned color means loaded and stopped, a flashing pad means queued to launch, and a pulsing pad means currently playing."
  - "Switch to Note Mode when the grid should function as a chromatic or scale-locked playing surface instead of a clip launcher, using the color-coded root-note layout to stay oriented without a keyboard."
  - "Map a bank of hardware knobs or the controller's session overview to Rack macros (per `knowledge_base/daw/ableton/racks_macros_and_performance_controls.md`) so filter, send, and energy moves are performed at the same time as clip launching."
  - "Use the controller's session-overview or navigation pads to scroll the mapped 8x8 window around a larger Session grid, rather than rebuilding the set to fit inside one fixed grid size."
  - "Save a fixed track/scene layout for performance sets so the grid's spatial mapping stays consistent between rehearsal and the show."
related_plugins:
  - "Novation Launchpad X"
  - "Novation Launchpad Pro"
  - "Ableton Session View"
  - "Ableton Instrument Rack"
  - "Ableton MIDI Mapping"
tags:
  - "ableton"
  - "launchpad"
  - "grid-controller"
  - "session-view"
  - "performance"
  - "clip-launching"
  - "macros"
---

# Launchpad and Grid Controller Performance Workflow

A grid controller such as Novation's Launchpad line turns Session View from a mouse-driven interface into a physical instrument: each pad maps to a clip slot, colors mirror clip state, and scenes and tracks can be triggered by hand in real time. This entry covers mapping Session View to a grid controller for performance, building on the general controller-mapping workflow in `knowledge_base/daw/ableton/midi_controller_mapping_workflow.md` and the rack/macro system in `knowledge_base/daw/ableton/racks_macros_and_performance_controls.md`.

## Session Mode and grid mapping

In Session Mode, the controller's grid (commonly 8x8 RGB pads on current Launchpad models) maps directly onto a window of Session View: each pad corresponds to one clip slot, and the controller's own navigation controls scroll that window around a larger set of tracks and scenes. Selecting the correct Live control-surface script for the specific controller model in Live's MIDI preferences maps this automatically, without needing to build the mapping by hand with MIDI Map Mode. This is a meaningfully different setup path than the generic knob/pad mapping covered in `knowledge_base/daw/ableton/midi_controller_mapping_workflow.md`, because a dedicated control-surface script provides two-way communication — Live also sends clip and track state back to the controller for the color feedback below.

## Color feedback as performance information

Because the control-surface script provides two-way communication, pad colors reflect real clip state rather than being static: a pad lit in the clip's assigned color means a clip is loaded and stopped, a flashing pad means the clip has been triggered and is queued to launch on the next quantization boundary, and a pulsing pad means the clip is currently playing. This turns the grid into a readable performance display in its own right — a performer can see what is about to happen without looking at the Live window, which matters when the laptop screen isn't in a convenient sightline on stage.

## Scene triggering from the grid

Most grid controllers dedicate a column or row of buttons to scene launching, separate from the clip grid, so a whole scene (per the scene-triggering logic in `knowledge_base/daw/ableton/session_view_clip_launching_and_follow_actions.md`) can be fired with one press rather than launching each track's clip individually. This is the primary way a grid-controller performance actually gets played live: scenes carry the section changes, and the clip grid is used within a scene for fills, variations, and one-off triggers.

## Note Mode for melodic performance

Switching the controller to Note Mode turns the same physical grid into a chromatic or scale-locked playing surface instead of a clip launcher, with root notes and in-scale notes color-coded differently so a performer can stay oriented visually without needing a piano-style keyboard layout. This is useful for a set that alternates between clip-launched sections and a hands-on melodic performance moment on the same piece of hardware, without needing to bring a second controller.

## Combining grid launching with macro mapping

A grid controller alone only covers triggering — it doesn't expose continuous knobs for filter sweeps, send rides, or macro moves. Pairing the grid with a bank of physical knobs (either on the same controller, if it has one, or a second device) mapped to Rack macros per `knowledge_base/daw/ableton/racks_macros_and_performance_controls.md` lets a performer trigger clips and scenes with one hand while shaping the sound with the other, which is the difference between a set that merely plays back pre-built clips and one that's actually performed.

## Common mistakes

Building a Session View layout that doesn't fit cleanly inside the controller's grid size, forcing constant scrolling mid-performance to reach clips that should have been positioned within the default window. Relying only on clip-grid triggering and never mapping macros to physical knobs, which limits the performance to start/stop control with no expressive shaping. Rehearsing exclusively with the mouse and only switching to the grid controller close to the show, rather than rehearsing with the actual performance surface from the start so the color feedback and spatial layout become second nature.
