---
workflow_name: "Cubase Automation Modes and Logical Editor Workflow"
daw: "cubase"
category: "automation"
goal: "Write clean, predictable automation using Cubase's punch-in/punch-out automation modes and Automation Panel, and use the MIDI Logical Editor / Project Logical Editor to apply rule-based, search-and-replace-style edits across MIDI and project data that would be impractical to do by hand."
steps:
  - "Open the Automation Panel and choose a punch-out mode — Touch Fader, Autolatch, or Cross-Over — before recording a live automation pass, matching the mode to how the pass should end rather than defaulting to whichever mode was last used."
  - "Use Touch Fader mode for a pass that should punch out the instant a control is released, holding the value found up to that release point and discarding the movement made while searching for it."
  - "Use Autolatch mode when the written value should keep being recorded even after the control is released, until the transport stops, rather than punching out immediately on release."
  - "Use Cross-Over (X-Over) mode when a new pass should stop overwriting existing automation as soon as it reaches a point where prior automation events already exist, blending a new pass into old data instead of overwriting straight through it."
  - "Use Trim mode to add a relative offset curve on top of an existing automation pass — raising or lowering the original curve by a drawn amount — when the goal is to adjust a previous pass rather than replace it outright."
  - "Open the MIDI Logical Editor for search-and-replace-style edits confined to MIDI data in a part or track (e.g. transposing only the notes at a specific pitch, or scaling velocity only on notes within a given range)."
  - "Open the Project Logical Editor (Cubase Pro) instead when the same kind of rule-based operation needs to apply across the whole project — audio events, MIDI events, and markers together — rather than one MIDI part at a time."
  - "Build a Filter Condition (or combine several with And/Or Boolean operators) that isolates exactly the events to act on by type, attribute, value, or position, before choosing what to do with them."
  - "Choose a Function appropriate to the target — Transform to change a matched event's properties, Delete to remove matched events, Insert to add new events at matched positions (MIDI Logical Editor), or Select to just select matches (Project Logical Editor) — rather than always defaulting to Transform."
  - "Save a working Filter Condition/Function/Action combination as a Logical Editor preset once it does what's needed, so a repeated correction (fixing overlapping legato notes, culling stray low-velocity ghost notes, transposing a specific pitch range) can be re-run as a single command in future sessions."
related_plugins:
  - "Cubase Automation Panel"
  - "Cubase MIDI Logical Editor"
  - "Cubase Project Logical Editor"
tags:
  - "cubase"
  - "automation"
  - "logical-editor"
  - "project-logical-editor"
  - "midi-editing"
  - "touch-fader"
  - "autolatch"
  - "cross-over"
  - "trim"
---

# Cubase Automation Modes and Logical Editor Workflow

Cubase separates two related but distinct power-user disciplines under this workflow: writing clean automation via the Automation Panel's punch-in/punch-out modes, and applying rule-based, search-and-replace-style edits to MIDI or whole-project data via the Logical Editor and its project-wide counterpart. Both reward deliberate mode/tool selection over defaults — the wrong automation mode produces unpredictable overwrites, and the Logical Editor's real power only shows up once filter conditions are built precisely rather than applied loosely.

## Automation punch-out modes

When a fader or other automatable control is touched during playback in an automation-armed track, Cubase begins writing automation data immediately in any mode. The modes differ in what happens at punch-out, once the control is released:

- **Touch Fader**: automation stops being written the instant the control is released. The curve holds the value found at release, and the movement made while searching for that value along the way is discarded — only the final settled value up to the release point survives.
- **Autolatch**: writing continues past the release point and keeps going until the transport is stopped, rather than punching out on release. Useful for a pass meant to hold a new value going forward rather than snapping back to old data.
- **Cross-Over (X-Over)**: behaves like Autolatch after release, but stops overwriting as soon as it reaches a point where automation events already exist on the track — letting a new pass blend into old data at the first point they'd otherwise collide, instead of overwriting straight through it.
- **Trim**: rather than overwriting the underlying curve at all, Trim adds a relative offset on top of an existing pass — drag the trim curve up or down and it raises or lowers the original automation by that amount, preserving the original shape while adjusting its overall level.

Choosing the wrong mode is a common source of automation surprises: Touch Fader discarding what felt like a deliberate move on release, or Autolatch/Cross-Over overwriting further into a track than intended because the transport kept running past where the user mentally "finished" the move.

## MIDI Logical Editor vs. Project Logical Editor

The Logical Editor window lets a user combine filter conditions, functions, and actions into a single rule that finds matching events and does something to them — a search-and-replace tool for musical data rather than text. The MIDI Logical Editor works within MIDI parts and tracks; the Project Logical Editor (Cubase Pro) works at the whole-project level, matching not just MIDI events but audio events and markers as well, which makes it the right tool when an edit needs to apply consistently across the entire session rather than one MIDI part at a time.

## Filter conditions

A filter condition specifies what an event must match — type, attribute, value, or position — to be selected for processing. Multiple conditions can be combined with And/Or Boolean operators to build composite matches: for example, "type is Note AND pitch is C3" isolates only middle-C notes out of a part that also contains controller data, rather than acting on every event in the part indiscriminately. Precise filter conditions are what separate a useful Logical Editor operation from one that accidentally catches unintended events.

## Functions and actions

Once a filter condition defines what to match, a function defines what happens to the matches. The MIDI Logical Editor offers functions including Transform (change properties of matched events — pitch, velocity, position, length), Delete (remove matched events), and Insert (add new events at positions derived from the matches). The Project Logical Editor's function set is narrower — Transform, Delete, and Select — reflecting that it's operating across heterogeneous project-level data rather than only MIDI. The Action List below the filter section specifies the concrete values or offsets the chosen function applies.

## Building reusable presets

A tuned combination of filter conditions, a function, and its actions can be saved as a Logical Editor preset. This turns a one-off cleanup (fixing overlapping legato note timing, removing ghost notes below a velocity threshold, transposing only notes in a specific key-switch range) into a reusable, single-click command for future sessions, rather than rebuilding the same rule from scratch every time the same problem recurs.

## Common mistakes

Recording a live automation pass without first choosing the right punch-out mode, then being surprised that Touch Fader discarded a searching movement or that Autolatch/Cross-Over kept writing further than intended. Reaching for the MIDI Logical Editor for an edit that actually needs to span audio events or markers too, when the Project Logical Editor is the tool built for whole-project scope. Building an overly broad filter condition (matching a type with no further attribute/value/position narrowing) and having the function apply to far more events than intended. Not saving a useful filter/function/action combination as a preset, and rebuilding the same rule by hand the next time the same cleanup is needed.

Related reading: `knowledge_base/daw/workflow/automation_curve_shape_and_musicality.md` for the cross-DAW philosophy of automation-curve musicality this workflow's mode selection serves, and `knowledge_base/midi/programming/humanization_and_groove_timing.md` for the timing/humanization concepts a Logical Editor rule-based cleanup pass often needs to preserve rather than accidentally flatten.
