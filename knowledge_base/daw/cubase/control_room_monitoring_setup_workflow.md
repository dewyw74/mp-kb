---
workflow_name: "Cubase Control Room Monitoring Setup Workflow"
daw: "cubase"
category: "monitoring"
goal: "Set up Cubase Pro's Control Room to manage multiple monitor speaker outputs, performer headphone cue mixes, and talkback separately from the main Stereo Out mix bus, so tracking sessions don't require re-routing the mix itself to serve a performer a different monitor balance."
steps:
  - "Confirm the project is running in Cubase Pro, since Control Room is not available in Cubase Artist or Elements — those editions monitor only through the standard Stereo Out bus."
  - "Enable Control Room in Studio Setup and add Control Room Devices for each physical output path needed: one or more Monitor channels (up to four) for control-room speaker sets, a Headphones channel for the engineer, and one or more Cue channels (up to four) for performer headphone mixes."
  - "Add a Talkback bus via Add Channel > Add Talkback and set its Device Port to the physical input the talkback microphone is connected to, so the engineer can communicate with performers without routing a mic through a regular audio track."
  - "Route the Talkback bus to the Cue channels it should reach — Talkback is automatically available to cue busses and can be enabled or muted independently per Cue Channel rather than broadcasting to every performer at once."
  - "Enable the Cue Sends rack in the MixConsole (Racks button > Cue Sends) so each track exposes its own Cue send controls in addition to the regular Sends rack."
  - "Enable each track's Cue send with the Cue section's power button, and set level (upper bar) and pan (lower bar) per track per Cue channel, keeping Cue sends pre-fader by default so a performer's headphone balance doesn't move every time the main fader is adjusted."
  - "Build a distinct cue mix per performer by adjusting each track's send level differently across Cue 1, Cue 2, etc. — a vocalist's cue mix emphasizing their own voice and a click, a drummer's cue mix emphasizing the click and bass, without changing the main Stereo Out mix at all."
  - "Use the Control Room panel's Main Monitor section to switch between connected speaker sets (e.g. mains vs. nearfields) without repatching audio interface outputs by hand."
  - "Route a metronome/click or external input (a DI'd instrument, a phone line) into a Cue channel directly through Control Room's external input handling when a performer needs to hear a source that isn't already a track in the project."
  - "Keep Control Room routing entirely separate from the Stereo Out mix bus in mental model as well as in signal flow — Control Room exists precisely so cue and monitoring changes never touch what's actually being recorded or mixed to the master bus."
related_plugins:
  - "Cubase Control Room"
  - "Cubase Cue Sends"
  - "Cubase Talkback"
  - "Cubase MixConsole"
tags:
  - "cubase"
  - "control-room"
  - "monitoring"
  - "cue-mix"
  - "talkback"
  - "tracking"
  - "routing"
---

# Cubase Control Room Monitoring Setup Workflow

Control Room is a Cubase Pro-only feature (unavailable in Artist and Elements) that adds a dedicated monitoring layer sitting outside the project's mix bus: separate monitor-speaker switching, per-performer headphone cue mixes, and a talkback path, all managed independently of the Stereo Out signal that's actually being recorded or mixed. This is a genuine differentiator among DAWs at this price point — achieving the same result in a DAW without an equivalent typically means building custom aux-bus routing and manually re-patching interface outputs by hand.

## Setting up Control Room devices

Control Room is enabled in Studio Setup, where Control Room Devices are added for each output path a session needs: up to four Monitor channels for control-room speaker sets, a Headphones channel for the engineer's own monitoring, and up to four Cue channels for performer headphone mixes. Each of these is a distinct signal path with its own routing, independent of how tracks are bussed for the main mix.

## Talkback

A Talkback bus is created via Add Channel > Add Talkback, with its Device Port set to whatever physical input the talkback microphone is plugged into. Talkback is automatically available to every Cue channel without additional routing, and can be enabled or muted per Cue channel individually — so an engineer can talk to the drummer's headphones without also cutting into the vocalist's cue mix mid-take.

## Cue Sends: one mix per performer

Enabling the Cue Sends rack in the MixConsole (via the Racks button) adds a Cue section to every channel, functioning much like a standard Send but routed to a Cue channel instead of an FX channel. Each track's Cue send is switched on with its own power button and given an independent level and pan per Cue channel — Cue sends are conventionally kept pre-fader so a performer's monitor balance doesn't shift every time the engineer rides a fader for the main mix. This is what makes distinct per-performer cue mixes possible: a vocalist's headphones can emphasize their own voice and the click while a drummer's headphones emphasize the click and bass, all without touching the Stereo Out mix at all.

## Monitor switching and external sources

The Control Room panel's Main Monitor section switches between connected speaker sets (main monitors vs. nearfields, for instance) without needing to repatch the audio interface's physical outputs. External sources that aren't already project tracks — a click track generator, a DI'd guest instrument, a phone line — can be fed directly into a Cue channel through Control Room's external input handling, keeping them out of the recorded project entirely if they're monitoring-only.

## Why this stays separate from the mix bus

The entire point of Control Room is that monitoring and cue-mix decisions never touch the signal actually being recorded or mixed to Stereo Out. A performer asking for more of themselves in their cans, or an engineer switching from mains to nearfields to check a mix, should never require re-routing or re-balancing what ends up on tape. For the routing conventions Control Room sits alongside once tracking is done, see `knowledge_base/daw/cubase/project_setup_and_mixconsole_routing_workflow.md`; for the general discipline of keeping monitoring changes from contaminating a recorded or mixed signal in any DAW, see `knowledge_base/daw/workflow/reference_track_ab_comparison_workflow.md`.

## Common mistakes

Attempting Control Room setup in Cubase Artist or Elements, where the feature doesn't exist at all. Routing a performer's headphone level from the main fader instead of a pre-fader Cue send, so every main-mix adjustment disrupts their monitor balance mid-take. Leaving Talkback routed to every Cue channel by default instead of scoping it per performer, causing unwanted interruptions in headphone mixes that weren't meant to hear it. Treating Control Room as optional overhead for a simple session and manually re-patching interface outputs instead, which recreates by hand what Control Room already automates.
