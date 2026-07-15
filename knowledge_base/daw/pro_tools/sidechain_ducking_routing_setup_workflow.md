---
workflow_name: "Pro Tools Sidechain Ducking Routing Setup Workflow"
daw: "pro_tools"
category: "routing"
goal: "Build a sidechain-ducking signal path in Pro Tools using an internal bus, a send, and a dynamics plugin's Key Input selector, since Pro Tools stock dynamics processors take an external key input through explicit bus routing rather than through an Ableton/FL-style sidechain-source dropdown built into the device itself."
steps:
  - "Identify the trigger track (the signal that should do the ducking, e.g. a kick drum) and the target track (the signal that gets ducked, e.g. a bass or pad) before wiring anything."
  - "On the trigger track, click an open send slot and choose an unused internal bus (mono, since a compressor's key input listens to a mono signal) to carry the trigger signal internally — this is the same bus mechanism used for any submix, per `knowledge_base/daw/pro_tools/session_setup_and_routing_workflow.md`."
  - "Option-click (Mac) / Alt-click (Windows) the floating send fader that opens and set it to unity gain (0.0 dB) so the key input receives the trigger at its natural level rather than an arbitrarily trimmed one."
  - "Insert a Dyn3 Compressor/Limiter (or another dynamics plugin with key-input support) on the target track's inserts."
  - "Open the plugin's Key Input selector, set by default to 'no key input,' and choose the same bus the trigger track is sending to."
  - "Enable the plugin's external/key-input switch so the compressor's gain reduction responds to the bus signal instead of the target track's own audio — this explicit enable step is what differs most from a one-menu sidechain setup."
  - "Use the plugin's key-input filtering (high-pass, and on some Dyn3 variants low-pass and additional EQ bands) to shape which part of the trigger's spectrum actually drives gain reduction, e.g. high-passing a kick's sub content out of the key signal if only the transient click should trigger ducking."
  - "Set threshold, ratio, attack, and release on the compressor exactly as for a normal insert — the key input changes what triggers gain reduction, not how the dynamics section itself behaves."
  - "Mute or route the trigger track's own fader output away from Master if the trigger is a reference-only signal (e.g. a scratch click) that should drive ducking but never itself be audible in the mix."
  - "Save a version of this bus/send/key-input setup in a session template if the same ducking relationship (sidechained bass, pumping pad under a kick) recurs across projects of the same genre."
related_plugins:
  - "Dyn3 Compressor/Limiter"
  - "Pro Tools I/O Setup"
  - "Pro Tools Sends"
tags:
  - "pro-tools"
  - "sidechain"
  - "ducking"
  - "routing"
  - "key-input"
  - "dyn3"
  - "compression"
---

# Pro Tools Sidechain Ducking Routing Setup Workflow

Pro Tools has supported sidechain ducking since long before it was a mainstream production technique, but the mechanism is explicit rather than a single dropdown: a trigger signal has to be routed through an internal bus via a send, and a dynamics plugin's Key Input selector has to be pointed at that same bus and then switched on. This is functionally the same result as Ableton's or FL Studio's built-in sidechain-source menu on stock compressors, but it is assembled from three separate pieces — bus, send, key input — rather than chosen from one control, which is the detail most likely to trip up anyone coming from those DAWs. See `knowledge_base/daw/ableton/sidechain_ducking_routing_setup_workflow.md` for the equivalent single-menu version of this same technique.

## Why Pro Tools Needs a Bus and a Send

A dynamics plugin's key input can only listen to something Pro Tools is already routing somewhere — it cannot reach across the session and grab another track's signal directly. An internal bus, the same routing-path concept used for any submix (see `knowledge_base/daw/pro_tools/session_setup_and_routing_workflow.md`), is what carries the trigger signal from the source track to the compressor's key input. The trigger track sends to that bus at unity gain so the key input hears the true level of the trigger, and the target track's compressor is then pointed at the same bus via Key Input.

## Enabling the Key Input

Selecting a bus in the Key Input menu is not enough by itself — the plugin also needs its external/key-input switch enabled, which explicitly tells the dynamics section to react to the bus signal rather than the track's own audio. Skipping this step is the most common reason a sidechain setup appears wired correctly but does nothing: the bus is selected, but the compressor is still listening to itself.

## Shaping the Key Signal

Because the key input is a full audio signal, not a value, it can be filtered before it reaches the dynamics section. High-passing the key input is standard when ducking should respond only to a kick's transient click rather than its low-frequency body; some Dyn3 variants extend this to low-pass and additional EQ bands, which lets an engineer tune exactly which part of the trigger's spectrum causes gain reduction without touching the trigger track's actual audible EQ.

## Common mistakes

Setting the Key Input menu to the correct bus but forgetting to enable the external/key-input switch, so the compressor keeps reacting to its own track instead of the trigger. Leaving the trigger's send at an arbitrary level instead of unity gain, which changes how hard the key input drives gain reduction in a way that has nothing to do with the trigger's actual mix level. Choosing a stereo bus for the key input on a mono-key dynamics plugin, which can cause unexpected phase or level behavior at the key stage. Forgetting that the trigger track, if it's a reference-only click or scratch track, still needs its own output routed away from Master or muted so it doesn't leak into the audible mix.
