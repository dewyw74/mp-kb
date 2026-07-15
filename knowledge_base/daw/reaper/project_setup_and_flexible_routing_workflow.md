---
workflow_name: "Reaper Project Setup and Flexible Routing"
daw: "reaper"
category: "routing"
goal: "Set up a Reaper project using its unified track model, where any track can act as a source, a bus, or both at once, and wire sends/receives and folder structure without being constrained to a fixed channel-strip hierarchy."
steps:
  - "Set project sample rate, bit depth, and default time base before recording (Project Settings), since Reaper does not force these from a template the way some DAWs do."
  - "Decide track/folder structure first: create folder tracks for drums, bass, harmony, vocals, and returns by indenting child tracks under a parent track in the Track Manager or TCP."
  - "Remember folder tracks are an organizational nesting, not a routing requirement — a child track's audio reaches its parent folder automatically only if no other explicit routing overrides it."
  - "Open the Track Routing window (I/O button on a track, or right-click > Routing) to add sends, receives, and hardware outputs on any track."
  - "Use View > Routing Matrix for a grid view of every track's outputs against every possible destination when wiring more than a few sends at once."
  - "Add an aux/bus track (an ordinary track used as a destination) for shared reverb, delay, or parallel-compression processing, and send to it from multiple source tracks pre- or post-fader as needed."
  - "Set up sidechain routing by adding a receive on the processing track (e.g., a compressor's sidechain input) pulling audio from the trigger track, rather than relying on a fixed sidechain slot."
  - "Route to hardware outputs or a mix of hardware and software destinations from the same track when tracking through outboard gear."
  - "Verify routing with the Routing Matrix or by soloing individual sends before committing to final bounces."
related_plugins:
  - "Reaper Routing Matrix (stock)"
  - "ReaInsert (stock hardware insert utility)"
  - "Reaper Track Manager"
tags:
  - "reaper"
  - "routing"
  - "sends-and-receives"
  - "folder-tracks"
  - "project-setup"
  - "workflow"
---

# Reaper Project Setup and Flexible Routing

Reaper's routing model is built around a single idea: every track is the same kind of object. There is no separate "track" class versus "bus" or "return track" class as in many other DAWs — any track can receive audio from other tracks, send audio to multiple destinations, host instruments and effects, and itself be the target of another track's send. This is what people mean when they call Reaper's routing "flexible" or "anything-to-anywhere": the routing graph is not constrained to a fixed hierarchy, it is whatever set of sends and receives you build.

## The Unified Track Model

Because every track can simultaneously function as an audio/MIDI track, a submix bus, a send source, and a receive destination, a "drum bus" in Reaper is not a special track type — it's an ordinary track that other tracks send audio into. This differs from workflows built around a fixed track/return-track split, such as Ableton's separate Return Track lane (see `knowledge_base/daw/ableton/mixing_bus_routing_and_gain_staging_workflow.md`); in Reaper the same track can be a submix bus for one signal path and a send destination for a completely different one at the same time.

## Sends, Receives, and the Routing Matrix

Each track's I/O button opens its Track Routing window, listing every send (audio leaving this track) and receive (audio arriving from another track) attached to it. Sends can be set pre-fader or post-fader, routed to any channel pair, and there is no hard limit on how many sends a track can have. For projects with many cross-connections, View > Routing Matrix shows every track's outputs against every possible destination in one grid, which is faster than opening individual routing windows when wiring complex parallel-processing or multi-bus setups.

## Folder Tracks vs. Routing

Folder tracks (created by indenting a track under another in the track panel) are primarily an organizational and mixing-console convenience — they let you collapse, solo, or gain-stage a group of tracks together, and by default a child track's audio flows up to its parent. But folder membership is not the same mechanism as an explicit send: a child track's output can be redirected elsewhere in the Track Routing window independent of its folder position, and the "Master/Parent Send" toggle on each track determines whether it still reaches its folder parent (or ultimately the master) at all. Treat folders as visual/organizational grouping and sends/receives as the actual audio-signal graph — they usually align but are not the same thing.

## Practical Routing Patterns

Common uses of this flexibility: a parallel-compression bus fed by post-fader sends from several tracks while the dry signal still reaches its folder parent; a sidechain trigger built by giving a compressor's sidechain input a receive from the trigger track rather than a dedicated sidechain menu slot; a submix folder whose parent track hosts a single glue-compressor chain; and multitrack hardware routing, sending the same track to both a software monitor bus and a physical output for tracking through outboard gear.

## Common mistakes

Assuming folder membership alone defines the signal path — a track can be visually nested in a drum folder while its audio actually routes somewhere else entirely if a send or the Master/Parent Send toggle says otherwise. Another common mistake is stacking sends without checking pre/post-fader state, which causes level changes on a source track to unexpectedly double-affect (or fail to affect) a parallel bus. Finally, over-wiring a project with many one-off sends instead of routing through folder buses makes the Routing Matrix hard to read later — build the simplest graph that gets the signal where it needs to go.
