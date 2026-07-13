---
workflow_name: "FL Studio External Hardware Sync and Recording"
daw: "fl_studio"
category: "hardware"
goal: "Sync FL Studio's clock to external hardware (drum machines, synths, modular gear) and record hardware audio and MIDI back into a project cleanly, matching latency and levels correctly."
steps:
  - "Set FL Studio's MIDI Settings to send MIDI clock (or MTC) out to hardware that needs to follow the project's tempo."
  - "For hardware acting as the master clock instead, enable FL Studio's 'Send master sync' off and configure the audio interface/MIDI input to receive external clock if the interface and FL Studio's clock source settings support it."
  - "Route external synth or drum machine audio into dedicated audio interface inputs, then into their own Mixer inserts — never straight to Master."
  - "Record MIDI from external sequencers or controllers directly into a Channel Rack channel's Piano Roll for later editing."
  - "Account for round-trip latency by nudging recorded audio earlier or using FL Studio's audio recording delay compensation settings, then verify alignment by ear against a click or existing drum pattern."
  - "Print a safety take of any hardware performance before further processing, since hardware synths and drum machines aren't recallable the way software instrument state is."
related_plugins:
  - "FL Studio MIDI Settings"
  - "FL Studio Mixer"
  - "FL Studio Audio Recording settings"
tags:
  - "fl-studio"
  - "hardware-sync"
  - "midi-clock"
  - "external-gear"
  - "recording"
  - "workflow"
---

# FL Studio External Hardware Sync and Recording

Bringing external hardware into an FL Studio session — a drum machine, a hardware synth, modular gear — requires getting both clock sync and audio/MIDI routing right, since FL Studio's flexible internal routing doesn't automatically account for the latency and clocking quirks of physical instruments.

## Goal

The goal matches `knowledge_base/daw/ableton/external_hardware_sync_and_recording.md`: make external hardware behave as a reliable, tempo-locked part of the session, and get its output recorded into the project cleanly enough to edit and mix like any other track.

## 1. Decide who is the clock master

Most sessions should keep FL Studio as the master clock, sending MIDI clock (or MTC for gear that needs timecode) out to hardware that needs to follow the project tempo. Reserve making external hardware the master clock for cases where a piece of gear's own internal sequencer or arpeggiator can't usefully follow an external clock — this is less common and adds setup complexity, so default to FL Studio as master unless there's a specific reason not to.

## 2. Route hardware audio into its own inserts

Bring hardware audio in through dedicated audio interface inputs, and assign each incoming source to its own Mixer insert immediately — the same one-source-per-insert discipline documented in `knowledge_base/daw/fl_studio/mixer_routing_resampling_and_freezing.md`. Never leave a live hardware input routed straight to Master, since that removes the ability to process or level it independently once recorded.

## 3. Record MIDI from external sequencers

For hardware that's sequencing itself (a step-sequencer-equipped drum machine, an arpeggiating synth) but should still leave editable MIDI data in the project, record its MIDI output directly into a Channel Rack channel's Piano Roll rather than only capturing its audio — this preserves the ability to edit note placement and velocity later, the same flexibility a fully in-the-box pattern would have.

## 4. Compensate for round-trip latency

Audio recorded from external hardware will typically arrive slightly late relative to FL Studio's internal clock due to D/A and A/D conversion round-trip time. Use FL Studio's audio recording delay compensation setting, or manually nudge the recorded clip earlier, and confirm alignment by ear against the existing drum pattern or a click track before trusting the take is in time.

## 5. Print a safety take

Because hardware synth and drum machine state isn't recallable the way a software instrument's saved project state is, always print (record) a hardware performance to audio as soon as it's finalized, rather than planning to re-trigger the hardware live at every subsequent mix session.

## Common mistakes

Forgetting to compensate for round-trip latency and then fighting a "loose" feeling recording that's actually just a fixed, correctable timing offset rather than a genuine performance issue. Leaving hardware clocked independently with no sync relationship to the FL Studio project, producing tempo drift over the length of a take.

## Alternatives

For hardware with no MIDI clock input at all (some analog drum machines, certain modular sequencers), skip clock sync entirely and instead record the hardware's output as a free-tempo audio take, then time-stretch or edit the FL Studio project's tempo/markers to match the hardware's recorded performance rather than the other way around.
