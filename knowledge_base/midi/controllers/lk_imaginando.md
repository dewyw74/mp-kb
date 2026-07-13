---
title: "LK — Ableton & MIDI Controller (Imaginando) App Profile"
controller_name: "LK - Ableton & Midi Controller"
manufacturer: "Imaginando Lda"
device_type: "iOS/Android touchscreen app functioning as a wireless MIDI/OSC control surface for Ableton Live"
tags:
  - "imaginando"
  - "lk"
  - "ableton-live"
  - "ios"
  - "android"
  - "app-controller"
  - "touchscreen-controller"
  - "wireless-midi"
  - "osc"
  - "control-surface"
  - "xy-pad"
  - "clip-launching"
  - "controller-profile"
---

# LK — Ableton & MIDI Controller (Imaginando) App Profile

LK is a touchscreen control-surface app from Imaginando Lda (iOS and Android) that turns a phone or tablet into a customizable wireless controller for Ableton Live. It differs from every other entry in `knowledge_base/midi/controllers/` in one key way: those are dedicated hardware (keyboards, pad controllers, a groovebox), while LK is software running on a general-purpose touchscreen device, connecting to the DAW over the network rather than USB/MIDI DIN. It is a control-surface tool, not a note-entry keyboard substitute.

## Best roles

- Session/clip launching and mixer control from off the desk — walking the room to judge levels while still triggering clips or riding a fader.
- XY-pad-driven performance moves: filter sweeps, macro throws, send/reverb build-ups mapped to a touch surface rather than a physical knob.
- Device parameter tweaking during a mix pass without reaching for the mouse.
- Giving a performer (drummer, vocalist) their own small control surface for monitor/return levels during a take, independent of the engineer's main controller.
- Building a bespoke, song-specific or set-specific control layout rather than being locked to a fixed hardware grid.

## Connection model: network, not plug-and-play

LK connects to the computer running Ableton Live over Wi-Fi, typically paired with a companion bridge component on the Live side that maps the app's controls to Live's parameters, clips, and mixer more directly than generic MIDI CC messages — closer to controlling the Live Object Model than to sending raw CC numbers. Practically, this means setup is "connect app and Live project over the network" rather than "pick a MIDI input port and go," and it introduces a dependency the hardware controllers in this folder don't have: both devices need to be on the same low-latency Wi-Fi network, and network congestion or a flaky router becomes a live-performance risk in a way a USB cable is not.

## Custom control surfaces

LK is page-based: XY pads, faders, buttons, and knobs can be laid out and assigned per page, so a set can carry a different control surface per song or section instead of being stuck with one fixed hardware layout. This flexibility is the app's main advantage over a hardware controller — the layout is redesigned in software rather than being constrained by physical knob/pad count.

## App vs. hardware controller tradeoffs

A touchscreen has no physical detents, click-stops, or tactile feedback, unlike the physical knobs and faders on the hardware controllers cataloged elsewhere in this folder (KeyStep 25, MPK Mini Plus, APC Key 25). LK is better suited to layout flexibility and mobility around the room than to precise, eyes-free performance where a hand needs to find a control without looking.

## Common mistakes

Relying on it over a congested or unstable Wi-Fi network for a live set — network dropouts mid-performance are a failure mode hardware MIDI controllers don't share.

Trying to improvise control mappings mid-performance instead of building song/genre-specific pages ahead of time, which defeats the point of the app's page-based flexibility.

Treating LK as a substitute for a proper note-entry keyboard or pad controller when the task is actually tracking a keyboard or drum performance — it is a control-surface app, not a velocity-sensitive playing surface.

## Cross-References

- `knowledge_base/daw/ableton/midi_controller_mapping_workflow.md` — Track vs. Remote mapping concepts relevant to any controller feeding Live, including a network-based one
- `knowledge_base/daw/ableton/max_for_live_custom_device_workflow.md` — the Max for Live layer that companion bridge apps like LK typically rely on for deep Live Object Model integration
- `knowledge_base/daw/ableton/racks_macros_and_performance_controls.md` — macro mapping targets well suited to XY-pad performance control
- `knowledge_base/midi/README.md` — overview of the controllers/ subfolder and how it relates to patterns/ and programming/
- `knowledge_base/midi/programming/midi_connectivity_wifi_bluetooth_and_din.md` — the general Wi-Fi/network-MIDI connectivity model this app's connection method is an example of, contrasted with Bluetooth MIDI and 5-pin DIN
