---
workflow_name: "Cubase MIDI Remote Controller Mapping Workflow"
daw: "cubase"
category: "controller_mapping"
goal: "Map a hardware MIDI controller's knobs, faders, and buttons to Cubase functions using the MIDI Remote Mapping Assistant, understand when Global versus Project mapping scope applies, and use Focus Quick Controls so hardware follows whatever track or plug-in currently has focus."
steps:
  - "Open Studio > MIDI Remote Manager and add the controller, either selecting a ready-made script for a recognized device or creating a new blank Controller Surface Editor mapping for an unrecognized one."
  - "Enter the Mapping Assistant and move a physical control on the hardware — Cubase detects the incoming MIDI message and creates a matching virtual control automatically, rather than requiring manual CC-number entry for every knob."
  - "Drag a Cubase function (channel volume, plug-in parameter, transport command, EQ band) from the Functions Browser onto the newly created virtual control to complete that mapping, one control at a time."
  - "Leave mappings created by dragging a function from the Functions Browser at their default Global scope when the mapping should behave identically in every project (transport controls, general navigation)."
  - "Leave mappings created ad hoc — by using a Cubase function directly while building the map — at their default Project scope when the mapping is specific to the current session's track layout or plug-in chain, and change the Mapping Scope manually in the Mapping Configuration section if a mapping needs to move between Global and Project."
  - "Assign Focus Quick Controls from the Functions Browser's Focus Quick Controls category for hardware knobs that should always control 'whatever is currently focused' rather than one fixed target, then click Apply Mapping."
  - "Configure the Quick Control Focus Setup panel to decide what counts as focus — by default Track and Plug-in Window Focus is active, meaning the hardware follows either the selected track or the active plug-in window automatically."
  - "Build multiple Mapping Pages for a single controller when one control set needs to serve different roles (a mixing page, an instrument-editing page, a transport page) and switch pages instead of re-mapping the same knobs by hand."
  - "Fall back to the legacy Generic Remote (Studio > More Options > Generic Remote) only for a controller or workflow that specifically needs its bank-based, table-driven assignment model, since MIDI Remote is the actively developed system going forward."
  - "Export or share a finished Controller Surface Editor script once tuned, so the same mapping can be reused across machines or installations instead of rebuilding it control-by-control."
related_plugins:
  - "Cubase MIDI Remote Manager"
  - "Cubase MIDI Remote Mapping Assistant"
  - "Cubase Controller Surface Editor"
  - "Cubase Generic Remote"
tags:
  - "cubase"
  - "midi-remote"
  - "controller-mapping"
  - "quick-controls"
  - "generic-remote"
  - "hardware-integration"
  - "workflow"
---

# Cubase MIDI Remote Controller Mapping Workflow

MIDI Remote, introduced in Cubase 12, is Steinberg's modern replacement for the older Generic Remote system, and it changes controller mapping from a table of banked CC-to-parameter assignments into a visual, learn-by-touching process built around a Mapping Assistant. The legacy Generic Remote remains available for backward compatibility, but MIDI Remote is where new development and most controller scripts now live, and it's the tool worth learning first for any new hardware integration.

## Setting up a controller

A controller is added via Studio > MIDI Remote Manager. Many popular controllers ship with a ready-made script that appears automatically once the hardware is detected; for anything unrecognized, a blank mapping can be built from scratch in the Controller Surface Editor. Either way, the end result is a virtual representation of the hardware's knobs, faders, pads, and buttons that Cubase functions get mapped onto.

## The Mapping Assistant: learn, don't type

Inside the Mapping Assistant, moving a physical control on the connected hardware causes Cubase to detect the incoming MIDI message and automatically create a matching virtual control — there's no need to look up or manually enter a CC number the way Generic Remote setup often required. Completing a mapping is then a matter of dragging the desired Cubase function out of the Functions Browser and dropping it onto that virtual control.

## Global vs. Project mapping scope

Every mapping carries a scope. Mappings created by dragging a function directly from the Functions Browser default to Global scope, meaning they behave the same in every project — appropriate for transport controls and general navigation that should never change project to project. Mappings created ad hoc, by using a Cubase function directly while building the mapping in context, default to Project scope instead, tying that mapping to the current session. Either default can be overridden manually from the Mapping Scope menu in the Mapping Configuration section, so a mapping built ad hoc in one project can still be promoted to Global if it turns out to be broadly useful.

## Focus Quick Controls

Focus Quick Controls solve a different problem than a fixed one-to-one mapping: rather than binding a knob to one specific parameter, a Focus Quick Control follows whatever currently has focus, based on the Quick Control Focus Setup panel's configuration (Track and Plug-in Window Focus is the default combination). This is what lets a small hardware controller act as a general-purpose mixing and plug-in-tweaking surface — the same physical knobs control the selected track's parameters, then automatically switch to an opened plug-in's parameters, without a separate mapping pass each time focus changes.

## Mapping Pages and Generic Remote fallback

A single controller can hold multiple Mapping Pages, letting the same physical layout serve different roles (mixing, instrument editing, transport) by switching pages rather than maintaining several controllers' worth of overlapping mappings. The legacy Generic Remote is still worth reaching for only when a specific bank-based, table-driven assignment model is genuinely needed; for everything else, MIDI Remote's learn-based workflow is faster to set up and easier to maintain. For the broader cross-DAW principle of matching a control surface to a task rather than one fixed layout, see `knowledge_base/daw/fl_studio/midi_controller_mapping_workflow.md`; for pad-based performance mapping specifically, see `knowledge_base/daw/ableton/drum_rack_pad_controller_workflow.md`.

## Common mistakes

Rebuilding a controller mapping from scratch when a ready-made script already exists in the MIDI Remote Manager. Leaving every mapping at its ad hoc Project-scope default and finding transport or navigation controls silently disappear in the next project, instead of promoting genuinely universal mappings to Global. Assigning fixed one-to-one mappings for parameters that would be far more useful as Focus Quick Controls, and ending up needing a much larger controller than the workflow actually requires. Reaching for the legacy Generic Remote out of familiarity when MIDI Remote's Mapping Assistant would set up the same control faster and with less manual bookkeeping.
