---
workflow_name: "Reaper FX Chains and Track Templates Workflow"
daw: "reaper"
category: "templates"
goal: "Use Reaper's two distinct reuse mechanisms correctly — FX Chain presets for a reusable plugin stack, and Track Templates for a full track setup including routing, I/O, and envelopes — instead of treating them as interchangeable."
steps:
  - "Decide scope first: if only the plugin stack needs to be reusable, save an FX Chain; if the whole track (routing, sends, color, envelopes) needs to be reusable, save a Track Template."
  - "Build the plugin chain on a track's FX window, then use the FX window's context menu > 'Save chain...' to store it as a reusable .RfxChain preset."
  - "Load a saved FX Chain onto any track (or FX window) via the FX browser's Chains section, or by dragging the .RfxChain file onto a track."
  - "Save common processing stacks as FX Chains: a vocal chain (gate, EQ, compressor, de-esser), a drum-bus glue chain, or a mastering chain, so they can be dropped onto any track without rebuilding plugin-by-plugin."
  - "To save a full track, right-click the track panel and choose 'Save tracks as track template...', which captures FX, I/O routing, sends/receives, color, and envelopes as an .RTrackTemplate file."
  - "Use the separate 'Save tracks as track template (with items)' action when the media/MIDI items themselves (not just the empty track setup) should be part of the reusable template."
  - "Load a Track Template from the Track Manager or Insert menu to drop a fully configured track — FX chain, routing, and all — into a new or existing project in one step."
  - "Keep FX Chains and Track Templates in their default Reaper resource folders (FXChains/ and TrackTemplates/) so they appear automatically in the relevant browsers across projects."
  - "Periodically re-save a Track Template after a mixing chain or routing convention changes, so old templates don't drift out of sync with current practice."
related_plugins:
  - "Reaper FX Chain (.RfxChain)"
  - "Reaper Track Template (.RTrackTemplate)"
  - "FabFilter Pro-Q 3"
  - "Valhalla VintageVerb"
tags:
  - "reaper"
  - "fx-chains"
  - "track-templates"
  - "templates"
  - "presets"
  - "workflow"
---

# Reaper FX Chains and Track Templates Workflow

Reaper has two genuinely distinct reuse mechanisms that are easy to confuse because both are commonly called "presets": FX Chains, which save only the plugin processing stack, and Track Templates, which save an entire track's configuration — FX chain, I/O routing, sends/receives, color, and envelopes. Picking the wrong one either under-captures what needs to be reused (an FX Chain that leaves routing to rebuild by hand) or over-captures it (a Track Template dropped in for a job that only needed a plugin stack).

## FX Chains: A Reusable Plugin Stack

An FX Chain (.RfxChain) is the ordered stack of plugins loaded into a track's, item's, or take's FX window, saved on its own. It carries plugin choice, order, and all of each plugin's parameter settings, but nothing about the track that hosted it — no routing, no color, no I/O. Save one from the FX window's context menu ("Save chain...") and it becomes available in the FX browser's Chains section or as a draggable file, ready to load onto any track. This is the right tool when the reusable unit is purely "this set of plugins in this order with these settings" — a vocal chain (gate, EQ, compressor, de-esser), a drum-bus glue chain, or a mastering bus chain such as one combining `knowledge_base/vst_database/fabfilter_pro_q_3.md` for tonal shaping with a limiter.

## Track Templates: A Full Track Setup

A Track Template (.RTrackTemplate) captures essentially everything about a track's state: its FX chain, input/output routing, sends and receives, record-arm state, color, name, and envelopes. Save one via right-click on the track panel > "Save tracks as track template...". Because it includes routing and sends, a Track Template can recreate an entire pre-wired signal path — for example a vocal track that already sends to a shared reverb bus and a parallel-compression bus — in one drop, which an FX Chain alone cannot do. A separate action, "Save tracks as track template (with items)," additionally bundles the track's actual media/MIDI items into the template, for cases like a reusable multitrack drum session rather than just an empty, pre-configured track.

## Choosing Between Them

Use an FX Chain when the goal is "apply this processing to a track that already exists" — dropping a vocal chain onto whatever vocal track is already routed correctly in the current session. Use a Track Template when the goal is "add a fully pre-configured track to this project" — inserting a ready-made drum-bus track, complete with its sends to shared drum-room and parallel-compression buses, into a new song. A well-organized producer library typically has both: FX Chains for individual processing stacks, and Track Templates for whole functional units built from those chains plus their routing. This is a narrower, track-level counterpart to whole-project template design — see `knowledge_base/production/templates/reusable_session_and_template_design.md` for the broader philosophy of what belongs in a reusable starting point versus what should stay a fresh creative decision each time.

## Common mistakes

Saving a Track Template when only the plugin chain needed to be reusable, which forces routing decisions (sends, I/O) onto a track that may already have its own correct routing — loading the template can silently overwrite it. The reverse mistake is saving only an FX Chain for something that's really a repeated full track setup (like a drum-bus submix with its parallel-compression sends), which means rebuilding the routing by hand every time despite the plugin chain being reusable. And letting either kind of saved preset go stale: if the standard vocal chain or drum-bus routing changes, the old FX Chain or Track Template should be re-saved, not left as an outdated default that quietly gets reused anyway.
