---
workflow_name: "Logic Pro Sidechain Ducking and Filtered Side-Chain Routing Workflow"
daw: "logic_pro"
category: "routing"
goal: "Set up sidechain ducking directly from Logic's stock Compressor, without building a separate send-based routing path first, and use the Compressor's side-chain filter to make the trigger signal more surgical than a raw full-band key input."
steps:
  - "Insert Compressor on the track that should duck (the pad, bass, or bed that needs to breathe for the kick)."
  - "Open the Side Chain pop-up menu at the top of the Compressor plug-in window and choose the trigger track directly from the list of available sources — no bus or send needs to be built first."
  - "Set Threshold and Ratio to control how much gain reduction the trigger causes, and use Attack to decide how quickly the duck engages after each hit."
  - "Set Release to match the trigger's tempo and rhythmic density: short release for a tight, tempo-locked pump; longer release for a smoother, less obvious duck."
  - "Choose a Detection mode for stereo material: enable Max so either channel crossing the threshold triggers compression, or Sum so the combined level of both channels must cross it."
  - "Choose Peak or RMS detection alongside Max/Sum — Peak reacts to instantaneous transients, RMS reacts to average loudness and produces a smoother, less twitchy duck."
  - "Enable the side-chain Filter and pick a Filter Mode (LP, BP, HP, ParEQ, or HS) so the Compressor only reacts to the frequency range that actually matters in the trigger, such as isolating just the kick's low-end thump."
  - "Set the filter's Frequency and Q to isolate that trigger band, and use Gain to boost or attenuate the filtered signal before it reaches the detection circuit."
  - "Verify the duck in context against the full mix rather than soloed, since an aggressive side-chain filter setting can sound different in isolation than under the rest of the arrangement."
  - "Automate Threshold or Mix (Compressor's dry/wet knob) for sections where the ducking effect should intensify or disappear, such as easing off during a breakdown."
related_plugins:
  - "Logic Pro Compressor"
  - "Logic Pro Channel EQ"
  - "Ableton Compressor"
  - "FabFilter Pro-C 2"
  - "Xfer LFOTool"
tags:
  - "logic_pro"
  - "sidechain"
  - "ducking"
  - "compressor"
  - "routing"
  - "side-chain-filter"
  - "mixing"
---

# Logic Pro Sidechain Ducking and Filtered Side-Chain Routing Workflow

Logic's stock Compressor triggers sidechain compression from its own Side Chain pop-up menu, which lists every other track in the project directly as a selectable source. This is a meaningfully shorter path than DAWs that require an internal send or bus to be built before a compressor can key off another track's signal — in Logic, picking the trigger from the menu is the entire routing step. Logic's Compressor also carries a dedicated side-chain filter section, letting the trigger signal itself be shaped in frequency before it ever reaches the detection circuit.

## Selecting the trigger without building a bus first

Any track, whether audio or software instrument, appears in the Side Chain menu of a Compressor instance placed on a different channel strip. Choosing a track there tells that Compressor instance to key its gain reduction off the chosen source's level while continuing to compress the original channel's own audio — no aux, no send, no extra bus number to manage. This differs from a routing model built around sends creating the sidechain path, as covered from the Ableton side in `knowledge_base/daw/ableton/sidechain_ducking_routing_setup_workflow.md`; the ducking result is the same musical effect, but Logic reaches it with one menu choice instead of a routed bus.

## Detection mode: Max/Sum and Peak/RMS

For stereo trigger sources, the Max and Sum buttons control how the two channels combine before hitting the threshold: Max compresses whenever either channel individually crosses it, Sum requires the combined level of both channels together to cross it. Alongside that choice, Peak and RMS determine what kind of level is being measured — Peak responds to the trigger's instantaneous transients for a snappier, more percussive duck, while RMS tracks average loudness for a smoother, less erratic gain-reduction curve.

## Filtering the side-chain input

The Filter Mode knob (LP, BP, HP, ParEQ, HS) applies a filter to the side-chain signal only, before it reaches the detection circuit — the trigger track's own output to the mix is untouched. Isolating just the kick's fundamental thump with a bandpass filter, for example, stops a kick's cymbal bleed or a busy bassline's upper harmonics from causing false or inconsistent triggers. Frequency and Q shape which band is isolated, and Gain boosts or cuts that filtered signal's level going into the detector, independent of the trigger track's own fader.

## Common mistakes

Building an unnecessary send/bus routing structure out of habit before checking whether the target Compressor's Side Chain menu can simply select the trigger track directly. Leaving the side-chain filter off on a busy trigger source, which lets unrelated frequency content cause an inconsistent or jittery duck instead of a clean rhythmic pump. Judging the duck amount by ear only in solo, missing how the effect actually reads once the full arrangement is playing — see `knowledge_base/mixing/compression/sidechain_pumping.md` for the broader tradeoff between an audible pumping effect and transparent, arrangement-driven ducking.
