---
workflow_name: "Reaper JSFX Custom Effect Scripting Workflow"
daw: "reaper"
category: "scripting"
goal: "Write and edit JSFX — Reaper's native, text-file audio/MIDI plugin format written in EEL2 — to build a custom effect that doesn't exist as a stock or commercial plugin, distinct from ReaScript, which automates the application's actions and UI rather than processing the audio/MIDI signal itself."
steps:
  - "Understand the distinction before starting: ReaScript (`knowledge_base/daw/reaper/customization_and_reascript_workflow.md`) automates Reaper's actions, menus, and UI; JSFX is a real-time audio/MIDI effect format that gets inserted into an FX chain and processes the signal itself, exactly like ReaComp or ReaEQ."
  - "Open the Reaper resource path's Effects folder (Options > Show REAPER resource path) to see where JSFX files live as plain, human-readable text — there is no compiled binary step."
  - "Start from an existing JSFX rather than a blank file when possible: because they're distributed as source, any stock or community JSFX can be opened and edited directly to adjust or extend its behavior."
  - "Declare user-facing parameters in the @slider section (or slider1/slider2 lines with range and default), which is what generates the knobs shown in the plugin's UI."
  - "Use @init for setup code that runs once on load, on a sample-rate change, and at the start of playback — buffer allocation and constants belong here."
  - "Use @sample for code that runs on every single audio sample, which is where per-sample DSP (filtering, waveshaping, gain) is written."
  - "Use @block for code that runs once per incoming block of samples, which is the section used for processing MIDI events rather than raw audio."
  - "Add an @gfx section only if a custom visual display or interactive graphic (beyond the auto-generated slider knobs) is needed — it's optional and most simple effects skip it."
  - "Save the file with a .jsfx extension inside the Effects folder (or a subfolder of it) so Reaper's FX browser picks it up automatically alongside stock and installed commercial plugins."
  - "Load the finished JSFX into a track's FX chain exactly like any other plugin, and save it into a reusable FX Chain per `knowledge_base/daw/reaper/fx_chains_and_track_templates_workflow.md` once its settings are dialed in."
related_plugins:
  - "Reaper JSFX SDK (stock)"
  - "ReaComp / ReaEQ (stock JSFX examples to read as references)"
  - "Community JSFX repositories (e.g. chkhld/jsfx, JoepVanlier/JSFX)"
tags:
  - "reaper"
  - "jsfx"
  - "scripting"
  - "eel2"
  - "custom-effects"
  - "sound-design"
  - "workflow"
---

# Reaper JSFX Custom Effect Scripting Workflow

JSFX is Reaper's other scripting surface, easy to confuse with ReaScript because both are written in EEL2 and both live under the same "Reaper lets you write code" umbrella. The difference is what they touch: ReaScript automates the application itself — actions, menus, custom UI panels, batch operations across items and tracks. JSFX is an actual real-time audio/MIDI effect, loaded into an FX chain and processing the signal sample-by-sample, functionally equivalent to a stock plugin like ReaComp or ReaEQ, except you can read and edit its source directly.

## File Structure and Sections

A JSFX file is plain text, stored in the Effects folder under Reaper's resource path, with no separate compile step — Reaper compiles it on the fly when the effect is loaded. Its code is organized into named sections: @init runs once on load, on a sample-rate change, and at the start of playback, and is where buffers and constants get set up. @sample runs on every individual audio sample and is where per-sample DSP — filtering, distortion, gain staging — actually happens. @block runs once per incoming block of samples and is the section typically used to read and generate MIDI events rather than raw audio. An optional @gfx section adds a custom graphical display or interactive control beyond the automatically generated slider knobs, which most simple effects don't need. Sliders declared for user-facing parameters (via @slider and slider1/slider2/... lines with a name, range, and default) are what produce the plugin's visible knobs.

## Editing Existing JSFX Instead of Starting Blank

Because JSFX ships and distributes as readable source rather than a compiled binary, the fastest path to a working custom effect is often to open an existing one — a stock effect or a community-published JSFX from a repository like chkhld/jsfx or JoepVanlier/JSFX — and modify its behavior directly, rather than writing every section from a blank file. This mirrors the "check what already exists first" discipline recommended for ReaScript macros in `knowledge_base/daw/reaper/customization_and_reascript_workflow.md`, applied here to actual signal-processing code instead of application automation.

## Using the Finished Effect

Once saved as a .jsfx file in the Effects folder, the effect appears in Reaper's FX browser automatically and loads into any track's FX chain exactly like a stock or commercial plugin — no separate installation step. A finished custom effect can then be folded into a saved FX Chain alongside other plugins, following the FX Chain conventions in `knowledge_base/daw/reaper/fx_chains_and_track_templates_workflow.md`.

## Common mistakes

Putting per-sample DSP code in @block (or MIDI-handling code in @sample), which either fails to process audio correctly or runs far less often than intended — matching the code to the section that actually executes at the right rate is the first thing to check when a JSFX behaves unexpectedly. Another common mistake is writing a JSFX from scratch for something an existing community effect already does with a small tweak; since JSFX ships as editable source, checking published JSFX libraries first is usually faster than reimplementing standard DSP (a simple gate, a basic LFO, a utility gain-stage) from zero.
