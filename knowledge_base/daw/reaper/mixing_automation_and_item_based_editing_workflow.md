---
workflow_name: "Reaper Mixing Automation and Item-Based Editing Workflow"
daw: "reaper"
category: "automation"
goal: "Use Reaper's automation envelope modes correctly (Trim/Read, Read, Touch, Write, Latch, Latch Preview) and work with Reaper's item-based editing model, where each audio/MIDI clip is an independent item with its own properties rather than a single continuous track lane."
steps:
  - "Understand that a Reaper track's timeline is made of independent items, each with its own gain, pitch, fade, playrate, and take properties, rather than one continuous track-level clip."
  - "Use takes to hold multiple recorded passes inside the same item; only the active take plays, and take lanes let you view/audition all takes stacked at once for comping."
  - "Comp a final take by using Reaper's take-lane comping tools (splitting and switching active takes across regions) rather than manually deleting unwanted recordings."
  - "Choose track-level envelopes (volume, pan, sends, plugin parameters) for automation that should apply across the whole track's timeline regardless of item boundaries."
  - "Choose take/item envelopes (opened by double-clicking an item and selecting 'take envelopes') for automation that must travel with a specific item if it's moved, copied, or resized — most commonly item-level volume or pitch envelopes."
  - "Set each armed envelope's automation mode deliberately: Trim/Read (default) offsets the underlying value without moving the visible fader; Read plays the envelope back without ever recording new changes."
  - "Use Touch mode for real-time mix moves you want to keep only while actively adjusting the control — it stops writing and reverts as soon as you release it."
  - "Use Latch mode when a move should keep recording at the last-set value until playback stops, and Write mode only when you intend to overwrite the entire envelope continuously, including while stopped."
  - "Use Latch Preview when auditioning automation changes without committing them until you explicitly write the previewed value to the envelope."
  - "Render or freeze automation-heavy tracks before final mixdown if the automation set has become CPU-intensive or needs to be locked in for stem export."
related_plugins:
  - "Reaper Track Envelopes (stock)"
  - "Reaper Take Envelopes (stock)"
  - "ReaComp"
  - "ReaEQ"
tags:
  - "reaper"
  - "automation"
  - "envelopes"
  - "item-based-editing"
  - "takes"
  - "comping"
  - "mixing"
  - "workflow"
---

# Reaper Mixing Automation and Item-Based Editing Workflow

Reaper mixes two ideas that are worth understanding separately: an item-based editing model, where each audio or MIDI clip on a track is an independent item carrying its own gain, pitch, fades, and takes rather than being one continuous track-level recording; and a multi-mode automation-envelope system (Trim/Read, Read, Touch, Write, Latch, Latch Preview) that governs how mix moves get written and played back. Both differ enough from track-centric models in other DAWs that assuming direct parity leads to mistakes.

## The Item-Based Editing Model

A Reaper track's timeline is a sequence of items, and each item is its own object with its own properties — gain, fade shapes, pitch/playrate, and, crucially, its own take history. Multiple items can sit end-to-end or overlap on a single track, each edited independently without affecting neighboring items. This differs from a purely track-based model where a recording is one continuous lane; in Reaper, cutting, moving, or adjusting one item never touches the properties of the item next to it.

## Takes and Comping

Each item can hold multiple takes — separate recorded or comped passes stacked inside the same item slot. Only the active take plays back, but take lanes display every take at once so a producer can audition and pick the best passage from each. Comping a final performance in Reaper means splitting across take lanes and switching which take is active in each resulting segment, rather than physically deleting unused recordings — the alternate takes stay available if a comp decision needs revisiting later. This item/take model is what the cross-DAW comping guidance in `knowledge_base/daw/workflow/comping_best_take_selection_philosophy.md` and the Ableton-side comparison in `knowledge_base/daw/ableton/multitrack_recording_and_take_comping_workflow.md` are describing in DAW-agnostic terms.

## Track Envelopes vs. Take/Item Envelopes

Reaper offers automation at two levels. Track envelopes (volume, pan, sends, plugin/FX parameters) apply across the whole track's timeline and are unaffected by item boundaries — this is the standard place for arrangement-level mix automation like a build-up filter sweep or a chorus volume lift. Take envelopes, opened by double-clicking an item and choosing "take envelopes," live inside a specific item and travel with it — move or copy the item to a new position and its take envelope moves too. Take envelopes are the right choice for automation that's really a property of one specific recorded passage (an item-level gain ride to fix an inconsistent take) rather than a property of the arrangement timeline.

## Automation Modes

Every armed envelope in Reaper operates in one of six modes. Trim/Read is the default: it offsets the underlying value by whatever you move a control to, without visibly moving the automation lane itself. Read plays the envelope back exactly as written and never records new automation, even if the envelope is technically armed. Touch records changes only while a control is actively being adjusted, reverting to the existing envelope the instant it's released — the least destructive real-time mode. Latch starts recording at the point a control is moved and keeps writing the held value continuously until playback stops. Write overwrites the entire envelope continuously whenever the track is touched, including while the transport is stopped, making it the most destructive mode if left armed by accident. Latch Preview writes only the final previewed value to the envelope on stop/selection rather than continuously recording, useful for auditioning a change before committing it. For the general principle of shaping automation curves musically once they're written, see `knowledge_base/daw/workflow/automation_curve_shape_and_musicality.md` and `knowledge_base/mixing/automation/automation_vs_static_balance.md`.

## Common mistakes

Leaving a track in Write mode during general mixing — because Write records continuously, even while stopped, an unrelated fader bump can silently overwrite carefully built automation. Another common mistake is building automation on a take/item envelope when it should have been a track envelope (or vice versa): item-level automation disappears or moves unexpectedly if the item is later shifted, comped, or replaced, while track-level automation ignores item boundaries entirely and can end up applied to the wrong take after a comp decision changes which take is active.
