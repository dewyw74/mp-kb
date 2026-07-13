---
workflow_name: "Ableton External Hardware Sync and Recording"
daw: "ableton"
category: "hardware"
goal: "Connect external MIDI hardware such as grooveboxes, drum machines, and synth modules to Ableton Live for clock sync, MIDI sequencing, audio recording, and resampling."
steps:
  - "Connect MIDI out from the interface or controller to the external hardware MIDI input."
  - "Connect the hardware audio outputs to the audio interface inputs."
  - "Enable MIDI Track and Sync settings in Live preferences based on whether Live is sequencing or clocking the hardware."
  - "Create an External Instrument device or separate MIDI and audio tracks."
  - "Set MIDI channel and audio input routing for the hardware."
  - "Measure and adjust hardware latency if timing feels late or early."
  - "Record hardware audio into Arrangement View once the part is stable."
  - "Resample or freeze software layers separately so hardware timing and audio edits stay manageable."
related_plugins:
  - "Ableton External Instrument"
  - "Ableton Utility"
  - "Ableton Tuner"
  - "Ableton Audio Effect Rack"
  - "Ableton Compressor"
tags:
  - "ableton"
  - "external-hardware"
  - "midi-clock"
  - "sync"
  - "recording"
  - "groovebox"
  - "mc-303"
---

# Ableton External Hardware Sync and Recording

External hardware can be used with Ableton Live in two main ways: Live can sequence and clock the hardware, or the hardware can be treated as a performance source that is recorded as audio. For older grooveboxes such as the Roland MC-303, the cleanest modern workflow is often to sync or trigger the hardware, capture audio, then edit the recording in Live.

## MIDI and audio routing

The hardware needs two connections:

- MIDI for notes, clock, transport, or program changes.
- Audio for the actual sound coming back into Live.

Use Ableton's External Instrument device when you want one track to handle both MIDI output and audio return. Use separate MIDI and audio tracks when you want more explicit control over recording, monitoring, and resampling.

## Clock sync

If Live is the master clock, enable Sync on the MIDI output port going to the hardware. Start/stop and tempo will follow Live. This is useful for grooveboxes, arpeggiators, and sequencers that need to stay locked to the project tempo.

If the hardware is the performance brain, record its audio into Live and avoid overcomplicating the sync setup unless transport lock is truly needed.

## Latency

External hardware has round-trip latency: MIDI leaves Live, hardware responds, audio returns through the interface, and Live records it. If the part feels late, adjust track delay or External Instrument hardware latency.

Do not judge timing only by what you hear while monitoring. Record a short transient pattern, zoom in, and check whether the recorded audio lands where expected.

## Recording workflow

Record hardware as audio once the part is musically stable. Audio is easier to edit, warp, reverse, chop, and process than a live external hardware stream.

Useful passes:

- Dry hardware pattern.
- Filter or knob performance pass.
- Alternate pattern variation.
- Long texture or transition pass.
- One-shot hits sampled from the hardware.

## MC-303-style use

For a Roland MC-303, treat the box as a source of patterns, tones, and hands-on performance moves. Sync it to Live if tempo lock matters, then record audio passes and arrange them like sampled material. This preserves the hardware character while letting Ableton handle editing, automation, effects, and final arrangement.

## Common mistakes

Do not leave important hardware parts as live external playback until the final export unless there is a strong reason. Printing audio makes the project portable and protects the arrangement from hardware state changes.

Do not ignore latency. A groovebox pattern can feel wrong simply because the recorded audio is late by a few milliseconds.
