---
workflow_name: "Studio One Sidechain and Ducking Routing"
daw: "studio_one"
category: "dynamics"
goal: "Set up sidechain-triggered compression and frequency-specific ducking in Studio One using the native Compressor's built-in sidechain source selector and Key Filter, choosing correctly between Send-based and Output-based sidechain routing."
steps:
  - "Insert the native Compressor on the track that should be ducked (commonly a bass or pad) and click its Sidechain button, located near the preset menu at the top of the plugin, to enable external sidechain input."
  - "Click the arrow next to the Sidechain button to open a list of available sidechain sources and choose the triggering track (commonly the kick) directly from that list, without building a separate sidechain bus by hand."
  - "Choose Send as the sidechain source mode when the triggering track must keep playing normally in the main mix — Send routes a copy of its signal to the compressor as a key input while the original track's own output is unaffected."
  - "Set the Send as pre-fader when the sidechain trigger should stay constant regardless of the source track's fader position, or post-fader when the trigger should scale with it."
  - "Choose Output as the sidechain source mode only when the triggering track exists purely to serve as a hidden key signal and should not be heard on its own — Output redirects the source track's actual output into the compressor's sidechain input instead of the main mix."
  - "Raise the compressor's Key Filter (a high-pass filter inside the sidechain detection circuit, separate from the main signal path) when the trigger should react only to a narrow high-frequency portion of the source, such as a kick's transient click rather than its full low-end energy."
  - "Use the Key Filter on a track's own signal, rather than an external source, to build an internal de-essing setup where the compressor only reacts to a narrow sibilant frequency band instead of the whole vocal."
  - "Reach for a sidechain-keyed dynamic EQ band instead of the Compressor when only a specific frequency range needs to duck — for example ducking just the bass's low-mid resonance under the kick's fundamental — rather than gain-reducing the whole track."
  - "Automate the compressor's threshold or the dynamic EQ band's depth for sections where the ducking effect should intensify or ease off, rather than leaving one static setting for the whole arrangement."
  - "Confirm the ducked track's fader and any bus processing downstream still leaves headroom for the sidechain's gain-reduction swing, so pumping reads as musical rather than clipping against a limiter later in the chain."
related_plugins:
  - "Studio One Compressor (native)"
  - "Studio One Pro EQ (dynamic EQ)"
  - "Studio One Console"
tags:
  - "studio_one"
  - "sidechain"
  - "ducking"
  - "compression"
  - "dynamic-eq"
  - "routing"
  - "dynamics"
---

# Studio One Sidechain and Ducking Routing

Studio One folds sidechain-source selection directly into the native Compressor's own interface rather than requiring a separately built sidechain bus or an external routing menu elsewhere in the mixer. A Sidechain button near the plugin's preset menu enables external keying, and the arrow beside it opens a list of existing tracks to choose as the trigger — the compressor itself is where the routing decision gets made, consistent with Studio One's broader console-and-drag-first approach to routing described in `knowledge_base/daw/studio_one/song_setup_and_console_routing_workflow.md`.

## Send vs. Output as the sidechain source

Once a source is chosen, Studio One offers two fundamentally different ways to feed it into the compressor. Send behaves like an ordinary effects send: a copy of the source track's signal reaches the compressor as a key input while the source itself keeps playing normally in the main mix, and this send can be set pre-fader (trigger level stays independent of the source track's fader) or post-fader (trigger level follows the fader). Output instead redirects the source track's actual output into the compressor's sidechain input, meaning the source is no longer heard on its own — the right choice specifically when a track exists only to serve as a hidden trigger, such as a MIDI-triggered kick clone used purely to duck a bass part and never meant to be audible itself. Picking the wrong mode either leaves an unwanted track audible in the mix or silences a track that was supposed to play normally.

## The Key Filter and triggering off the right content

The Compressor's Key Filter is a high-pass filter that lives inside the sidechain detection path only — it does not touch the main signal being compressed, just what the detector reacts to. Raising it excludes low-frequency energy from the trigger, which is useful when a kick's low-end thump would otherwise trigger the compressor continuously; filtering it out leaves only the transient click driving the ducking. The same Key Filter mechanism, applied to a track's own signal rather than an external source, is also the basis for an internal de-essing setup: narrowing the filter to a sibilant band means the compressor only reacts to harsh "s" and "t" sounds instead of the vocal's full spectrum. The general mechanics and creative uses of this pumping effect are covered DAW-agnostically in `knowledge_base/mixing/compression/sidechain_pumping.md`.

## When ducking should be frequency-specific instead

Full-band sidechain compression reduces the entire ducked track's gain every time the trigger fires, which is the right tool when the goal is rhythmic pumping (the classic EDM kick-duck). When the actual problem is a narrow frequency conflict — a bass's low-mid resonance clashing with a kick's fundamental, for instance — a sidechain-keyed dynamic EQ band is the more surgical option, ducking only that frequency range instead of the track's overall level. See `knowledge_base/mixing/eq/dynamic_eq.md` for the general case for reaching for dynamic EQ over broadband compression, and compare to how sidechain routing is set up in `knowledge_base/daw/ableton/sidechain_ducking_routing_setup_workflow.md` and `knowledge_base/daw/fl_studio/sidechain_ducking_routing_setup_workflow.md`, both of which route sidechain sources through a send/bus structure built in the mixer rather than a source dropdown inside the compressor itself.

## Common mistakes

Choosing Output when Send was actually needed (or the reverse) is the most common error — it either silences a track that should still be heard in the main mix, or leaves an intended-to-be-hidden trigger track audible. Leaving the Key Filter at its default setting while trying to trigger off transient content only is another frequent gap, producing pumping keyed off full-spectrum energy instead of just the intended transient. A third mistake is reaching for full-band sidechain compression to fix what is really a narrow frequency clash, when a sidechain-keyed dynamic EQ band would resolve the conflict without gain-reducing content in the ducked track that didn't need to move at all.
