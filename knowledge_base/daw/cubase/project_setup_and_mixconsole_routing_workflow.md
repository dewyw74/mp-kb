---
workflow_name: "Cubase Project Setup and MixConsole Routing Workflow"
daw: "cubase"
category: "routing"
goal: "Set up a Cubase project's signal flow correctly from the start — audio and instrument tracks into Group Channels, Group Channels into the Stereo Out, and the MixConsole's insert/channel-strip/send racks configured so routing stays predictable as the session grows."
steps:
  - "Create dedicated Group Channels for each instrument category (drums, bass, keys/synths, vocals, FX) via Project > Add Track > Group, rather than routing every track straight to Stereo Out."
  - "Route each audio or instrument track's output to the matching Group Channel instead of leaving it on Stereo Out, so bus-level processing and bus-level fader moves affect the whole category at once."
  - "Open the MixConsole (F3) and use the Select Racks button in the left/right zone to activate only the racks you're actively working with — Inserts, Strip, Sends, Routing — to keep the channel strip readable."
  - "Use the eight-module Channel Strip (Gate, Compressor, Tools, EQ, Transformer, Saturator, Limiter, plus a dedicated Fader) for fast, mixer-native shaping before reaching for a full plug-in insert."
  - "Set the pre-fader/post-fader split for each channel's 16 total insert slots by dragging the pre/post divider, keeping level-dependent effects (most saturation, some distortion) pre-fader and metering/limiting post-fader."
  - "Reposition the Channel Strip itself pre- or post-insert in the signal flow when a channel-strip module (e.g. the Gate) needs to act before or after a plug-in insert rather than in its fixed default slot."
  - "Route the FX Channel Sends (Cubase's aux-send equivalent) from source channels to Group Channels used as return busses for shared reverb/delay, rather than inserting a full reverb on every individual track."
  - "For channels that must move together (a full drum kit, a doubled vocal stack), use Cubase Pro's Linked Channels feature so fader, mute, and EQ moves apply across the whole link instead of matching values by hand."
  - "Add a VCA Fader to control the levels of several Group Channels (e.g. all instrumental busses) as one performable fader without altering their individual balance or their sends."
  - "Save the routed template as a Track Template or full Project Template once the bus structure is confirmed, so new sessions start from the same signal flow instead of being rebuilt per project."
related_plugins:
  - "Cubase MixConsole"
  - "Cubase Channel Strip"
  - "Cubase Group Channel"
  - "Cubase FX Channel"
  - "Cubase VCA Fader"
  - "Steinberg Frequency"
  - "Steinberg Compressor"
tags:
  - "cubase"
  - "routing"
  - "mixconsole"
  - "group-channel"
  - "channel-strip"
  - "inserts"
  - "vca"
  - "templates"
---

# Cubase Project Setup and MixConsole Routing Workflow

Cubase's MixConsole is built around the same signal-flow idea as most DAWs — tracks feed busses, busses feed the master — but its channel strip, insert racks, and Group Channel conventions have their own mechanics that are worth setting up deliberately at the start of a project rather than patched together as tracks accumulate. Getting the routing right early keeps large orchestral, band, or hybrid electronic sessions manageable instead of turning into dozens of tracks dumped straight onto Stereo Out.

## MixConsole layout and racks

The MixConsole (opened with F3) is organized into racks — Inserts, Strip, Equalizers, Sends, Cue Sends, and the Routing rack — that can each be shown or hidden per channel type via the Select Racks control in the left and right zones. A common mistake is leaving every rack visible at once, which turns the MixConsole into a wall of controls; showing only the racks relevant to the current task (usually Inserts and Sends for general mixing, Strip when doing fast channel-native shaping) keeps the view usable in a large session.

## Group Channels as the backbone

Group Channels are Cubase's bus/submix channels, created via Project > Add Track > Group. Route every audio and instrument track's output to a Group Channel that matches its role (drums, bass, keys, vocals, FX) rather than routing tracks straight to Stereo Out. This gives category-level fader control, category-level bus processing (glue compression, bus saturation, bus EQ), and a much simpler final mix stage where the Stereo Out only receives a handful of Group Channel signals instead of the full raw track count.

## The Channel Strip module

Every channel exposes a built-in Channel Strip with up to eight modules: Gate, Compressor, Tools (a small utility section), Equalizer, Transformer, Saturator, Limiter, and the channel Fader. These are separate from plug-in inserts — they live in a dedicated signal-flow slot and can be repositioned pre- or post-insert depending on whether a given module (for example the Gate, which usually wants to act before a compressor plug-in) needs to happen before or after the plug-in chain. Reach for the Channel Strip first for common, fast shaping moves; reach for a full insert plug-in when a job needs more control than the built-in module offers.

## Insert slots: pre-fader and post-fader

Each channel has 16 total insert slots, split between pre-fader and post-fader positions by dragging the divider between them in the Inserts rack. There's no fixed default split — the split is set per channel. Keep the convention consistent: level-and-gain-dependent processing (most saturation and distortion, since their character depends on input level relative to the fader) belongs pre-fader; metering, limiting, and anything that should see the channel's final post-fader level belongs post-fader.

## FX Channels and sends

Cubase's send-based effects live on FX Channels — return-channel busses that source channels feed via Sends, functionally equivalent to an aux/return setup in other DAWs. Use FX Channels for shared reverb, delay, and other effects multiple tracks should draw from at different amounts, rather than inserting a separate instance of the same reverb on every track. This keeps CPU load down and keeps the shared space/ambience consistent across the elements feeding it.

## Linked Channels and VCA Faders

Cubase Pro channels can be combined into Linked Channels so that fader, mute, solo, and (optionally) EQ and insert moves apply to the whole linked set — useful for a multi-mic'd drum kit or a stacked vocal double that should move together. VCA Faders are a separate tool: a VCA controls the levels of the Group Channels or tracks assigned to it as one performable fader without altering their individual relative balance, their sends, or their own automation — closer to a remote level trim than a hard link.

## Common mistakes

Routing every track directly to Stereo Out instead of through Group Channels, which makes category-wide balance changes and bus processing impossible without touching dozens of individual tracks. Leaving all MixConsole racks visible at once instead of using Select Racks to show only what's needed. Putting level-dependent processing in the wrong pre/post-fader slot and getting an inconsistent, fader-position-dependent sound. Confusing a VCA Fader (a level-only remote control) with Linked Channels (which propagate mute, solo, and processing moves) — they solve different problems and using the wrong one either under- or over-couples channels that should or shouldn't move independently.

Related reading: `knowledge_base/daw/ableton/mixing_bus_routing_and_gain_staging_workflow.md` for the cross-DAW bus-routing philosophy this workflow implements in Cubase-specific terms, and `knowledge_base/mixing/` for the frequency and dynamics decisions that happen once the routing itself is in place.
