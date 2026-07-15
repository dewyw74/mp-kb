---
workflow_name: "Logic Pro Project Setup and Mixer Routing Workflow"
daw: "logic_pro"
category: "routing"
goal: "Set up a Logic Pro project's channel-strip structure, route audio and MIDI through buses and Aux channel strips, and organize tracks with Folder Stacks and Summing Stacks so the session stays fast to mix as it grows."
steps:
  - "Create audio, software instrument, and external MIDI tracks as needed, letting Logic auto-create the matching channel strip for each."
  - "Group related tracks (all drum mics, all synth layers, a vocal with its doubles) by selecting them and choosing Track > Create Track Stack."
  - "Choose Folder Stack when the goal is organization and unified fader/mute/solo control without changing the underlying audio routing."
  - "Choose Summing Stack when the goal is a real subgroup: the sub-tracks route to a shared bus, land on an Aux channel strip, and can be processed with shared inserts."
  - "Build sends by dragging a channel strip's Send slot to a free bus; Logic creates the destination Aux channel strip automatically unless that bus is already an input elsewhere."
  - "Use Aux channel strips for shared reverb, delay, and parallel-compression returns, keeping their inserts separate from the dry signal path."
  - "Insert corrective and tone-shaping plugins directly on individual channel strips; reserve Summing Stack (subgroup) inserts for glue processing that should affect the whole group."
  - "Route each Summing Stack's Aux output, and any remaining unbused channel strips, to the stereo Output channel strip that feeds the Master."
  - "Re-check gain staging on the stack's Aux fader after adding or muting sub-tracks, since a Summing Stack's level moves with the sum of its inputs."
  - "Save the routed structure as a Logic template once it is reusable across sessions of the same type (band recording, beat-making, mix session)."
related_plugins:
  - "Logic Pro Channel Strip"
  - "Logic Pro Aux Channel Strip"
  - "Logic Pro Track Stack"
  - "Logic Pro Gain"
  - "Ableton EQ Eight"
tags:
  - "logic_pro"
  - "routing"
  - "mixer"
  - "track-stacks"
  - "summing-stack"
  - "folder-stack"
  - "bus-routing"
  - "gain-staging"
---

# Logic Pro Project Setup and Mixer Routing Workflow

Logic Pro's Mixer is built from channel strips: one per audio, software instrument, or external MIDI track, plus Aux channel strips that appear automatically whenever a send or a Summing Stack needs a destination. Getting the routing right early — before a session has forty tracks — is what keeps mixing fast later. This entry covers channel-strip basics, send/Aux routing, and Logic's two Track Stack types, which are the closest thing Logic has to Ableton's group tracks but work differently enough that they should not be assumed to behave the same way.

## Channel strips and signal flow

Every track gets a channel strip with the same basic slots, top to bottom: input, inserts (plug-ins routed in series, each one's output feeding the next), sends, pan, fader, and output. Inserts process the channel's own signal directly. Sends split the signal: the dry path continues to its output as normal, while a copy is routed down a bus to an Aux channel strip, scaled by the Send level knob. Creating a send by dragging it to an unused bus number auto-creates the destination Aux channel strip — Logic only skips that step if the chosen bus is already in use as another channel's input source.

Aux channel strips are the right place for shared effects: one reverb Aux fed by sends from many tracks is far cheaper on CPU than the same reverb inserted separately on each track, and it also gives a single fader to control the overall wet balance.

## Folder Stacks vs. Summing Stacks

Logic has two Track Stack types, created via Track > Create Track Stack (or Control-click a track header) after selecting the tracks to combine. They solve different problems and should not be treated as interchangeable:

- **Folder Stack**: combines tracks for organization and a single fader/mute/solo control, without changing the underlying audio routing of the sub-tracks. The stack's main channel strip acts as a VCA-style master — moving it scales every sub-track's level while preserving their relative balance, but no audio is actually being summed to one strip.
- **Summing Stack**: routes every sub-track's output to a shared bus that lands on an Aux channel strip acting as a real subgroup. Because the signals are actually summed onto one channel strip, that strip's own inserts affect the combined signal — this is the Logic equivalent of an Ableton Group Track's own device chain.

Use a Folder Stack for tidy track management (all rhythm guitar takes collapsed into one row) when no shared processing is needed. Use a Summing Stack when the goal is bus compression, bus EQ, or a single fader that represents genuinely summed audio, matching the drum-bus and mix-bus conventions in `knowledge_base/mixing/compression/bus_glue_compression.md` and `knowledge_base/mixing/compression/drum_bus_compression.md`.

## Building a bus structure

A typical mixing-session structure in Logic mirrors the functional grouping used elsewhere in this knowledge base: drums, bass, harmony/keys, lead/vocal, and FX, each as its own Summing Stack so it has a real subgroup fader and shared inserts. Route each Summing Stack's Aux output to the Output channel strip that feeds the Master, and keep the Master itself close to unprocessed during mixing — save heavier master-bus processing for a dedicated mastering pass, consistent with `knowledge_base/daw/ableton/master_bus_chain_and_export_workflow.md`'s philosophy even though the DAW differs.

## Gain staging across the routing chain

Trim hot sources at the channel strip's Gain or Trim stage before any tone-shaping insert, so compressor thresholds and saturation respond consistently across the session. Watch each Summing Stack's Aux fader after adding, muting, or re-balancing sub-tracks — because a Summing Stack's level is a real sum of its inputs, adding a new sub-track can push the subgroup hotter even though no individual fader changed. Leave headroom into the Output channel strip (comfortably under 0dBFS) throughout the mix rather than only checking at the end.

## Common mistakes

Using a Folder Stack when a Summing Stack was actually needed, then wondering why an insert on the stack's main channel strip has no audible effect — Folder Stacks don't sum audio, so a plug-in placed there never touches the sub-tracks' signal. Building sends to a bus number that's already claimed as another channel's input, which silently reuses that channel instead of creating a fresh Aux. Leaving corrective EQ and compression on individual channel strips inside a Summing Stack and never using the subgroup's own inserts for glue processing, which produces a set of well-treated individual tracks that still don't sit together as a group.
