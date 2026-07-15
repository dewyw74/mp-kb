---
workflow_name: "FL Studio Sidechain Ducking Routing Setup"
daw: "fl_studio"
category: "routing"
goal: "Set up sidechain compression in FL Studio mechanically — routing a kick/trigger track into a mixer insert's sidechain input, selecting that input from a compressor plugin's own sidechain-source dropdown, and building frequency-specific sidechain ducking with Fruity Peak Controller and Fruity Parametric EQ 2 — as the 'how to route it' companion to the musical/aesthetic settings documented elsewhere."
steps:
  - "Confirm the trigger source (kick or 808) already sits on its own Mixer insert, per `knowledge_base/daw/fl_studio/mixer_routing_resampling_and_freezing.md`, since FL Studio's sidechain routing is Mixer-track-based rather than a direct plugin-to-plugin connection."
  - "On the destination insert (the bass, pad, or synth track that should duck), right-click the small triangle beneath the fader and choose 'Sidechain to this track', which assigns that insert a numbered sidechain input FL Studio can reference elsewhere."
  - "Insert a sidechain-capable compressor on the destination insert — Fruity Limiter, Fruity Compressor, or a third-party plugin such as `fabfilter_pro_c_2` — and open its own Sidechain source dropdown, which lists Mixer tracks by name once right-clicked."
  - "Select the kick/808's Mixer insert number from that dropdown so the compressor's gain reduction is driven by the trigger track's signal instead of the destination track's own input, per FL Studio's design of routing sidechain data through the Mixer rather than through the plugin interface directly."
  - "Set attack, release, ratio, and threshold on the sidechain compressor according to the musical/aesthetic target documented in `knowledge_base/mixing/compression/sidechain_pumping.md` — this entry covers only the mechanical routing, not the settings that make the duck feel right for a given genre."
  - "For frequency-specific ducking (triggering off only the kick's low-end rather than its full signal), insert Fruity Peak Controller on the kick's insert to read its volume envelope, then right-click the target EQ band's level in Fruity Parametric EQ 2 on the destination track and choose 'Link to controller' to connect it to Peak Controller's output."
  - "Set the linked band's mapping formula to Inverted so rises in the kick's peak level produce dips in the destination EQ band rather than boosts, and set Peak Controller's base level and volume knob to control how deep the frequency-specific duck reaches."
  - "Confirm the EQ band's frequency and bandwidth are set to the specific range that should duck (for example, a low-shelf or bell around 100-150Hz to clear space for a kick's fundamental) rather than affecting the destination's full spectrum, which is what distinguishes this from a standard full-band sidechain compressor."
  - "Test with the destination's other processing (its own EQ, saturation, reverb sends) active, since sidechain routing set up in isolation can behave differently once the rest of the destination's chain is engaged."
related_plugins:
  - "FL Studio Mixer"
  - "Fruity Limiter"
  - "Fruity Compressor"
  - "Fruity Peak Controller"
  - "Fruity Parametric EQ 2"
  - "fabfilter_pro_c_2"
tags:
  - "fl-studio"
  - "sidechain"
  - "routing"
  - "ducking"
  - "peak-controller"
  - "mixer"
  - "workflow"
---

# FL Studio Sidechain Ducking Routing Setup

`knowledge_base/mixing/compression/sidechain_pumping.md` documents the musical side of sidechain ducking — why genres reach for it, how audible the pump should be, and how to set ratio/attack/release for a given target. This entry is the mechanical counterpart: the literal FL Studio routing steps needed before any of those musical settings can take effect. FL Studio's sidechain system works differently from some other DAWs — sidechain data is routed through the Mixer itself, not connected plugin-to-plugin — and that single design choice is the source of most confusion for producers new to the DAW.

## Routing through the Mixer, not the plugin

Every sidechain-capable compressor in FL Studio (native or third-party) reads its trigger signal from a numbered Mixer track, not from a direct audio connection to another plugin's output. Before any compressor can be sidechained, the destination insert needs to be told which Mixer track to listen to — that assignment happens on the Mixer insert itself, via the small triangle beneath the fader, not inside the compressor plugin.

## Setting the sidechain input on the destination track

Right-click the triangle beneath the fader on the insert that should duck (the bass, pad, or synth track) and choose "Sidechain to this track." This gives that insert a sidechain input slot that any plugin loaded on it can subsequently read from. This step has to happen before the compressor's own sidechain dropdown will show a meaningful signal — skipping it is the most common reason a sidechain compressor appears configured correctly but produces no ducking at all.

## Selecting the trigger source in the compressor

With the insert sidechain-enabled, insert a compressor — Fruity Limiter and Fruity Compressor both include a native Sidechain source dropdown, and third-party compressors such as `fabfilter_pro_c_2` expose the same Mixer-track list through their own sidechain input control, since they're reading the same FL Studio-level routing rather than implementing their own separate sidechain system. Right-click the dropdown to see every available Mixer track by name, and select the kick or 808's insert number. From this point the compressor's gain reduction is driven by the trigger track's signal, and the musical settings (attack, release, ratio, threshold) from `sidechain_pumping.md` determine how that ducking actually sounds.

## Frequency-specific sidechain ducking

A standard sidechain compressor ducks the destination's full signal every time the trigger fires, which is sometimes more than needed — ducking only the specific frequency range where the trigger and destination actually clash (typically low-end masking around 60-150Hz) preserves more of the destination's other content. Build this with Fruity Peak Controller and Fruity Parametric EQ 2 rather than a compressor: insert Peak Controller on the kick's insert to track its volume envelope, then right-click the target band's gain control in Fruity Parametric EQ 2 on the destination track and link it to Peak Controller's output. Setting the mapping formula to Inverted means the EQ band's level drops as the kick's peak rises, producing a duck confined to whatever frequency and bandwidth that EQ band is set to — a low-shelf or narrow bell around the kick's fundamental, for example, rather than the compressor's full-band reduction.

## Common mistakes

Inserting a sidechain-capable compressor and setting its dropdown without first enabling "Sidechain to this track" on the destination insert, which leaves the dropdown showing no usable signal. Expecting a third-party compressor's sidechain input to work like it does in a DAW that routes sidechain plugin-to-plugin directly — FL Studio's Mixer-track-based system means the routing step happens at the Mixer level first, regardless of which specific compressor plugin is loaded. Using a full-band sidechain compressor when the actual goal is narrow, frequency-specific ducking, producing more audible pumping across the destination's full spectrum than the mix actually needs — the Peak Controller/EQ-band-link approach exists specifically for that narrower case. Setting up the routing in isolation and never testing it with the destination's other processing engaged, since reverb sends, saturation, or additional EQ downstream can mask or exaggerate a duck that looked correct in isolation.

## Cross-References

- `knowledge_base/mixing/compression/sidechain_pumping.md` — the musical/aesthetic settings (attack, release, ratio, threshold) this entry's routing steps make possible
