---
workflow_name: "FL Studio Playlist Automation Clips and Modulation Controllers"
daw: "fl_studio"
category: "automation"
goal: "Use Playlist automation clips, Automation Channels, and FL Studio's internal modulation controllers (Peak Controller, Fruity Envelope Controller, Formula Controller) to drive parameter movement from sources other than hand-drawn automation."
steps:
  - "Right-click any automatable parameter and choose 'Create automation clip' to generate a Playlist automation clip with its own editable envelope."
  - "Use hand-drawn automation clips for one-off arrangement moves (filter sweeps into a drop, a slow reverb send build) that don't need to repeat or react to other signals."
  - "Insert Fruity Peak Controller ahead of a target parameter when the modulation should react to another track's volume envelope or its own internal LFO, for sidechain-style pumping or audio-reactive movement."
  - "Insert Fruity Envelope Controller when the modulation source should be a custom-drawn envelope or LFO triggered from the Piano roll or live MIDI input, rather than an audio-reactive signal."
  - "Insert Formula Controller when the modulation needs to blend multiple input sources mathematically, or generate a repeating waveform (sine, square, custom) from a typed formula rather than a drawn shape."
  - "Right-click the target parameter and link it to the chosen internal controller the same way a hardware controller would be linked, then set the amount and direction of modulation."
  - "Automate the internal controllers' own parameters (LFO rate, envelope amount) with a Playlist automation clip if the modulation itself needs to change shape across the arrangement."
  - "Group related automation clips onto dedicated Playlist automation tracks, named by what they control, so the arrangement stays legible as clip count grows."
related_plugins:
  - "FL Studio Playlist"
  - "FL Studio Automation Channel"
  - "Fruity Peak Controller"
  - "Fruity Envelope Controller"
  - "Formula Controller"
tags:
  - "fl-studio"
  - "automation"
  - "modulation"
  - "peak-controller"
  - "envelope-controller"
  - "formula-controller"
  - "workflow"
---

# FL Studio Playlist Automation Clips and Modulation Controllers

FL Studio splits parameter movement into two distinct systems that are easy to conflate: Playlist automation clips, which are hand-drawn or recorded envelopes placed on the arrangement timeline, and internal modulation controllers (Peak Controller, Envelope Controller, Formula Controller), which generate movement from another signal, a custom envelope, or a mathematical formula and route it to a target parameter continuously. Knowing which one to reach for is the core of this workflow.

## Automation clips: arrangement-timeline movement

An automation clip is created by right-clicking any knob, fader, or plugin parameter and choosing 'Create automation clip'. It behaves like any other Playlist clip — it can be dragged, resized, looped, and edited with its own point-based envelope editor. This is the right tool for movement that's tied to a specific point in the arrangement and doesn't need to react to anything else: a filter sweep building into a drop, a slow widening of a reverb send across a breakdown, a one-time volume fade. Automation Channels (the underlying data an automation clip edits) can also be recorded live by moving a mapped controller while the transport runs, capturing a performed automation pass instead of hand-drawing every point.

## Fruity Peak Controller: audio-reactive and LFO modulation

Peak Controller reads the volume envelope of an audio input (its own "Peak" section) and/or generates its own internal LFO, and can output either separately or combined as "Peak+LFO". Routing a kick drum's output through Peak Controller and linking its output to a bass channel's volume or a compressor's threshold is the classic way to build sidechain-pumping behavior without necessarily reaching for a dedicated sidechain compressor plugin. Because Peak Controller's LFO section runs independently of any audio input, it also works as a straightforward free-running modulation source when no audio-reactive behavior is needed.

## Fruity Envelope Controller: custom envelopes from the Piano roll

Envelope Controller generates modulation data from a custom-drawn envelope or LFO shape, triggered from the Piano roll or from live keyboard/MIDI input rather than from an audio signal. This suits modulation that should be performable or note-triggered — a filter opening on every note-on, a custom attack/decay shape applied to a parameter that doesn't have its own built-in envelope, or a manually sculpted LFO shape that doesn't match Peak Controller's simpler LFO waveforms.

## Formula Controller: mathematical and blended modulation

Formula Controller doesn't pass audio or MIDI; instead it evaluates a typed mathematical formula against up to three input sources (A, B, C) or against song time, and outputs the result as a modulation signal. This covers cases the other two controllers can't: blending two existing modulation sources together, generating a precise custom waveform through a formula (a sine or square wave expression, for example), or building modulation logic that depends on a mathematical relationship rather than an audio envelope or a drawn shape. It's the least commonly needed of the three, but it's the only option once the desired modulation behavior can't be expressed as a simple envelope or LFO.

## Choosing between the three

Peak Controller when the source is audio-reactive or a simple LFO is enough. Envelope Controller when the source needs to be a custom-drawn shape triggered by notes or MIDI. Formula Controller when the modulation needs mathematical blending of multiple sources or a precisely specified waveform a simple LFO can't produce. All three link to a target parameter the same way — right-click the parameter and link to the controller's output — so switching between them mid-project doesn't require re-learning the routing step, only the source.

## Common mistakes

Hand-drawing a repeating automation clip shape (a pumping volume envelope, a steady LFO-style wobble) that Peak Controller or Formula Controller would generate more precisely and adjustably from a single knob or formula. Using Envelope Controller for audio-reactive sidechain behavior it isn't designed to read, instead of Peak Controller. Leaving automation clips ungrouped and unnamed on generic Playlist tracks, which becomes unreadable once a project has more than a handful of automated parameters — see the track-naming conventions in `knowledge_base/daw/fl_studio/project_templates_and_mixer_conventions.md`.
