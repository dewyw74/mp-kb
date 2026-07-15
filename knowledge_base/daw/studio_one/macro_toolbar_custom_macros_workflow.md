---
workflow_name: "Studio One Macro Toolbar Custom Macros"
daw: "studio_one"
category: "macros"
goal: "Build custom multi-step Macros in Studio One's Macro Toolbar to chain repetitive command sequences into a single click or keyboard shortcut, distinct from Ableton-style Macro Knobs which map continuous device parameters rather than chaining discrete commands."
steps:
  - "Open the Macro Organiser via the cog icon next to the Macro page menu, or right-click an existing macro slot and choose Assign > New Macro, to start building a custom macro."
  - "Choose commands one at a time from the full command list on one side of the dialog and add each to the macro's ordered command list on the other side, since Studio One builds macros from manually selected commands rather than recording live actions."
  - "Order the commands deliberately, since a macro executes its command list top-to-bottom in sequence — for example chaining Insert Pattern, then Open Editor, then Loop Selection into one macro that leaves a Pattern ready for step input in a single click."
  - "Test the macro immediately after building it in the context it's meant for, since not every Studio One command behaves identically regardless of what's currently selected or focused."
  - "Assign a keyboard shortcut to a finished macro so it can be triggered without touching the toolbar at all, or map it to a MIDI controller for hands-on triggering during tracking or performance."
  - "Use the Global Macro Toolbar's Actions button, which exposes every raw Studio One command, as the building-block list when a needed command isn't visible in a more focused toolbar."
  - "Organize macros into Studio One's separate, context-specific toolbars (introduced from Studio One 4.5 onward) rather than piling every macro into one global list, so a macro built for Pattern editing doesn't clutter a toolbar meant for mixing tasks."
  - "Undock and float the Macro Toolbar to reposition it — useful when working with a touchscreen or a secondary monitor dedicated to fast-access controls."
  - "Reserve macros for genuinely repetitive multi-step actions (track setup, editor prep, recurring export steps) rather than single commands that already have a direct shortcut, since a macro adds indirection a plain keyboard shortcut doesn't need."
  - "Distinguish a macro's role from a Song template's role: a template (see `knowledge_base/daw/studio_one/song_setup_and_console_routing_workflow.md`) captures a starting session state, while a macro captures a repeatable action sequence performed inside any session."
related_plugins:
  - "Studio One Macro Toolbar"
  - "Studio One Macro Organiser"
tags:
  - "studio_one"
  - "macros"
  - "macro-toolbar"
  - "productivity"
  - "workflow-automation"
  - "custom-commands"
---

# Studio One Macro Toolbar Custom Macros

Studio One's Macro Toolbar chains multiple discrete commands into a single click or keyboard shortcut — inserting an instrument, opening an editor, and setting a loop range, for instance, executed as one action instead of three separate ones. This is a long-standing Studio One feature that was substantially reorganized starting with Studio One 4.5, moving from a single global list into a Global Macro Toolbar plus several focused, context-specific toolbars. It is worth naming precisely because "macro" means something different here than it does in Ableton Live, where Macro Knobs map continuous parameters across a Rack's devices rather than chaining discrete commands — the shared name covers two unrelated concepts.

## Building a macro from commands, not from recorded actions

A new macro is created either through the Macro Organiser (opened via the cog icon next to the Macro page menu) or by right-clicking an existing macro slot and choosing Assign > New Macro. The resulting dialog presents the full list of available Studio One commands on one side; building a macro means selecting commands from that list and adding them, in order, to the macro's own command sequence. There is no "record my actions" button — Studio One requires macros to be built command-by-command, since not every possible user action in the program is something that can be captured and replayed automatically. A practical example is chaining Insert Pattern, Open Editor, and Loop Selection into a single macro that leaves a fresh Pattern ready for step input in one click, replacing three separate manual steps described in `knowledge_base/daw/studio_one/impact_xt_drum_and_pattern_programming_workflow.md`.

## Triggering and organizing macros

A finished macro can be assigned its own keyboard shortcut or mapped to a MIDI controller, so it fires without ever touching the toolbar itself — useful for macros meant to be triggered during tracking or a live performance pass. Since Studio One 4.5, macros are organized into the Global Macro Toolbar (whose Actions button exposes every raw command as a building block) plus additional toolbars scoped to specific tasks, so a Pattern-editing macro doesn't have to sit in the same list as a mixing- or export-related one. The toolbar itself can be undocked and floated, which matters for touchscreen setups or a dedicated fast-access monitor.

## Macros vs. Song templates

A macro and a Song template solve different problems and are easy to conflate. A template, as covered in `knowledge_base/daw/studio_one/song_setup_and_console_routing_workflow.md`, captures a complete starting session state — bus structure, track layout, default plugins — that a new Song is built from. A macro captures a repeatable sequence of commands that can be run inside any session, regardless of its starting state. Reaching for a macro when a template was really needed (or the reverse) produces either a one-off command chain that has to be re-triggered every project, or a rigid starting template that can't adapt to a session already in progress.

## Common mistakes

Expecting Studio One to auto-generate a macro from actions just performed, rather than manually assembling the command list in the Macro Organiser, is the most common point of confusion for anyone coming from a DAW with true macro recording. Confusing Studio One's command-chaining Macros with Ableton's Macro Knobs — a completely different, parameter-mapping concept that happens to share the name — is a second common mix-up when moving between the two DAWs. A third mistake is building a single macro loaded with commands specific to one editing context and then triggering it somewhere unrelated, where some of its chained commands either do nothing or act on the wrong target; scoping macros to the specific context-focused toolbar they belong in avoids this.
