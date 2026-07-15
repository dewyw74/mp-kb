---
workflow_name: "Reaper Sidechain Ducking: Auxiliary-Channel Routing Setup"
daw: "reaper"
category: "routing"
goal: "Set up sidechain compression in Reaper by exposing extra auxiliary input channels on a plugin and feeding them with a send, since Reaper has no dedicated 'sidechain' menu slot — the sidechain input is just another pair of channels on the track's plugin, wired the same way any other send is wired."
steps:
  - "Insert ReaComp (or another sidechain-capable compressor) on the track that should duck — bass, pads, synths — not on the trigger track (kick, 808)."
  - "Open the plugin's I/O button (in the FX chain window) and activate channels 3/4 with the '+' control, exposing an auxiliary input pair the plugin can read from in addition to the track's normal 1/2 input."
  - "In ReaComp, set the Detector Input dropdown to Aux 3/4 In (Auxiliary Input L+R) so gain reduction is triggered by that channel pair instead of the track's own signal."
  - "On the trigger track, open Track Routing and add a new send to the ducking track, then set that send's destination channels to 3/4 rather than the default 1/2 — this is the step that actually delivers the trigger signal to the compressor's detector input."
  - "Leave the send's own audible output routing untouched; channels 3/4 on the destination track are not part of its normal 1/2 output to the master, so the trigger track is not doubled in the mix by adding this send."
  - "Watch ReaComp's gain-reduction meter to confirm it moves only when the trigger track plays, not continuously — if it never moves, recheck that channels 3/4 are activated on both the send and the plugin's I/O."
  - "For third-party compressors without a native Aux-input dropdown, right-click the plugin's title bar and use 'Set sidechain input...', or increase the host track's channel count and route the send into the extra channels the same way as with ReaComp."
  - "For sidechaining the entire mix bus (ducking everything against a click, kick, or voice cue), route the trigger send into extra channels on the Master track and insert the sidechain-capable compressor after the tracks that should be affected, per the pattern in the 2024 Reaper Blog master-bus sidechain guide."
  - "Set attack fast enough to catch the trigger's transient and tempo-sync the release to a musical subdivision so the ducked element recovers before the next hit, applying the general sidechain settings guidance in `knowledge_base/mixing/compression/sidechain_pumping.md`."
  - "Verify the finished routing in the Routing Matrix (`knowledge_base/daw/reaper/project_setup_and_flexible_routing_workflow.md`) before final mixdown, since sidechain sends are easy to lose track of once a project has many tracks."
related_plugins:
  - "ReaComp (stock)"
  - "ReaXcomp (stock)"
  - "FabFilter Pro-C2"
  - "Reaper Track Routing (stock)"
tags:
  - "reaper"
  - "routing"
  - "sidechain"
  - "ducking"
  - "compression"
  - "workflow"
---

# Reaper Sidechain Ducking: Auxiliary-Channel Routing Setup

Reaper has no dedicated "sidechain" selector the way some DAWs expose a fixed slot on a compressor device. Instead, a sidechain input is simply another pair of channels on a track's plugin, and getting a trigger signal into it uses the exact same mechanism as any other send: activate the extra channels, then route a send into them. This is a direct expression of the unified, anything-to-anywhere routing model documented in `knowledge_base/daw/reaper/project_setup_and_flexible_routing_workflow.md` — sidechaining is not a special case, it's ordinary routing applied to a compressor's detector input.

## Activating the Auxiliary Input

A plugin only sees channels the host track has activated for it. Opening ReaComp's I/O button inside the FX chain window and turning on channels 3/4 with the "+" control gives the plugin an auxiliary input pair beyond the track's default 1/2. ReaComp's Detector Input dropdown then lets you tell the plugin to key its gain reduction off "Aux 3/4 In" instead of the track's own 1/2 signal — this is the single setting that turns a normal compressor into a sidechain-triggered one.

## Wiring the Trigger Send

The trigger track (kick, 808, voice cue) needs a send whose destination channels are set to 3/4 on the ducking track, not the default 1/2. Because channels 3/4 aren't part of that track's normal output path to the master, this send delivers a triggering copy of the signal to the compressor without adding an audible extra copy of the trigger to the mix — no muting or extra routing cleanup is required the way it can be in menu-driven sidechain implementations.

## Third-Party Plugins and the Master Bus

Compressors without a native auxiliary-input dropdown can usually still sidechain in Reaper via the plugin's own right-click "Set sidechain input..." option, or by increasing the host track's channel count and routing a send into the added channels — the mechanism is the same regardless of which plugin's UI exposes it differently. The identical technique scales to bus- or master-level ducking: route the trigger into extra channels on the Master track and insert the compressor after whichever tracks should be affected.

## Common mistakes

Forgetting to activate the extra channels on the plugin's I/O before setting the Detector Input, which leaves the dropdown pointing at a channel pair with nothing routed into it and produces no gain reduction at all. Another common mistake is sending the trigger into the ducking track's default 1/2 channels instead of 3/4, which audibly mixes the trigger into the ducked track rather than just feeding its detector. Compare this to Ableton's dropdown-based Sidechain section in `knowledge_base/daw/ableton/sidechain_ducking_routing_setup_workflow.md` — the musical result is the same, but Reaper's version is built entirely from generic routing primitives rather than a purpose-built sidechain control.
