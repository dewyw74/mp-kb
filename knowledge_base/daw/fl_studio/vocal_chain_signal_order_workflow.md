---
workflow_name: "FL Studio Lead Vocal Mixing Chain Signal Order"
daw: "fl_studio"
category: "mixer"
goal: "Build a lead vocal's full mixing chain in FL Studio's Mixer in a deliberate order — gain staging, subtractive EQ, de-essing, two-stage compression (level then tone), corrective/tonal EQ, saturation, and reverb/delay sends — picking up immediately after tuning and comping is already finished."
steps:
  - "Confirm the vocal has already been comped and pitch-corrected per `knowledge_base/daw/fl_studio/vocal_tuning_and_comping_pipeline_workflow.md` before adding any mixing processing — this chain starts from that finished, tuned comp, not a raw take."
  - "Set gain staging first using Fruity Balance or the insert's trim control so the vocal's peaks sit with headroom before any EQ or compression sees the signal, per `knowledge_base/daw/fl_studio/mixing_bus_routing_and_gain_staging_workflow.md`'s trim-before-fader discipline."
  - "Apply subtractive EQ first with Fruity Parametric EQ 2 or `fabfilter_pro_q_3` — high-pass unneeded low-end rumble, cut resonant honk or boxiness — before any dynamics processing, per the corrective-EQ-first ordering documented in `knowledge_base/mixing/vocal_processing/vocal_chain_signal_order.md`."
  - "De-ess next, using Maximus's de-esser preset (narrow-band dynamic compression at the sibilance range) or a dynamic band in Fruity Parametric EQ 2, targeting roughly 4-10kHz per `knowledge_base/mixing/vocal_processing/de_essing.md`, since this pass happens before compression re-emphasizes whatever sibilance remains."
  - "Apply a first compression stage for level control — `fabfilter_pro_c_2` in Vocal or Clean style, or Fruity Compressor, moderate ratio and medium attack — to even out the vocal's overall dynamic range before any tone-shaping compression is added on top."
  - "Apply a second compression stage for tone and character — a slower, more colored compressor such as `universal_audio_la_2a` or `universal_audio_1176`-style plugin, or a second `fabfilter_pro_c_2` instance in Opto or Punch style — layered after the first stage rather than replacing it, per the serial multi-stage approach documented in `knowledge_base/mixing/compression/serial_multi_stage_compression.md`."
  - "Re-check for reintroduced sibilance after both compression stages, since raising the vocal's average level can push previously-controlled sibilance back into audibility, per `knowledge_base/mixing/vocal_processing/de_essing.md`'s documented compression/de-essing interaction."
  - "Apply corrective and tonal EQ as a second EQ pass — `fabfilter_pro_q_3` again or a fresh Fruity Parametric EQ 2 instance — for final presence/air shaping now that dynamics are settled, distinct from the first pass's purely corrective cuts."
  - "Add saturation for warmth and density using `soundtoys_decapitator` at a low drive amount or Fruity Blood Overdrive, placed after EQ and compression so it's coloring an already-controlled signal rather than an unpredictable raw one."
  - "Set reverb and delay send levels last, sending to dedicated Mixer send tracks carrying `valhalla_vintageverb` or Fruity Reeverb 2 and `valhalla_delay` or Fruity Delay 3, per the reverb-last pattern documented in `knowledge_base/mixing/vocal_processing/vocal_chain_signal_order.md` and the send-routing discipline in `knowledge_base/mixing/reverb/reverb_send_vs_insert.md`."
related_plugins:
  - "Fruity Balance"
  - "Fruity Parametric EQ 2"
  - "Maximus"
  - "Fruity Compressor"
  - "Fruity Blood Overdrive"
  - "Fruity Reeverb 2"
  - "Fruity Delay 3"
  - "fabfilter_pro_q_3"
  - "fabfilter_pro_c_2"
  - "universal_audio_la_2a"
  - "universal_audio_1176"
  - "soundtoys_decapitator"
  - "valhalla_vintageverb"
  - "valhalla_delay"
  - "izotope_nectar"
tags:
  - "fl-studio"
  - "vocal-chain"
  - "mixing"
  - "signal-order"
  - "compression"
  - "de-essing"
  - "mixer"
  - "workflow"
---

# FL Studio Lead Vocal Mixing Chain Signal Order

`knowledge_base/daw/fl_studio/vocal_tuning_and_comping_pipeline_workflow.md` covers comping and pitch-correcting a lead vocal, ending once "correction is finalized" and pointing forward to "de-essing, compression, and EQ." This entry picks up exactly there: the full mixing chain applied to an already comped and tuned vocal, built in FL Studio's Mixer insert chain, in the order `knowledge_base/mixing/vocal_processing/vocal_chain_signal_order.md` synthesizes from across the genre corpus — corrective EQ first, then compression and de-essing (paired and order-sensitive), then tonal EQ, saturation, and reverb/delay as the final spatial layer.

## Starting point: a finished, tuned comp

Nothing in this chain should touch the vocal until `vocal_tuning_and_comping_pipeline_workflow.md`'s pipeline is complete — a single, comped, pitch-corrected audio clip. Mixing processing applied to an unfinished comp or an uncorrected take means redoing EQ and compression decisions once the upstream work changes the vocal's actual content, exactly the ordering mistake that workflow's common-mistakes section warns against.

## Gain staging and the first EQ pass

Set trim with Fruity Balance before anything else touches the signal, per `knowledge_base/daw/fl_studio/mixing_bus_routing_and_gain_staging_workflow.md` — a vocal recorded hot or quiet distorts every downstream decision if the fader is doing the gain-staging work instead of the trim. With levels set, apply a first, purely subtractive EQ pass: high-pass filtering below the vocal's useful range and broad cuts at resonant or boxy frequencies, using `fabfilter_pro_q_3`'s spectrum display or Fruity Parametric EQ 2 by ear. This mirrors the EQ-before-de-essing order `vocal_chain_signal_order.md` documents for broad tonal problems — remove general harshness before targeting sibilance specifically.

## De-essing before the first compression stage

De-ess next, targeting the roughly 4-10kHz range where sibilant energy concentrates, per `knowledge_base/mixing/vocal_processing/de_essing.md`. Maximus's de-esser preset isolates a narrow band and compresses only that range, leaving the vocal's body untouched; a dynamic band in Fruity Parametric EQ 2 works identically in principle. This step happens before compression specifically because compression tends to raise sibilance along with everything else — de-essing an already-compressed signal means fighting a problem the compressor itself partly created.

## Two-stage compression: level, then tone

Split compression into two distinct jobs rather than one aggressive pass. The first stage controls overall level consistency — a moderate ratio, medium attack setting in `fabfilter_pro_c_2`'s Clean or Vocal style — evening out the performance's natural dynamic range. The second stage is about character rather than level control: a slower, more colored compressor (an 1176-style fast/aggressive setting via `universal_audio_1176`, or LA-2A-style smooth leveling via `universal_audio_la_2a`) layered on top per `knowledge_base/mixing/compression/serial_multi_stage_compression.md`'s serial multi-stage approach, adding the analog-style density a single clean compressor stage doesn't provide on its own.

## Re-checking sibilance, then tonal EQ

Because both compression stages raise average level, listen again for sibilance that's crept back in after de-essing — a second, lighter de-esser pass or a small EQ trim at the sibilance frequency is common at this point rather than a flaw in the earlier work. With dynamics settled, apply a second EQ pass focused on tone rather than correction: presence boosts, air shelving, or further resonance control now that the signal's dynamic behavior is finalized and won't shift the EQ decisions again.

## Saturation and spatial sends

Add `soundtoys_decapitator` at a low drive setting or Fruity Blood Overdrive for harmonic density and warmth, placed after EQ and compression so it's shaping an already-controlled signal. Finish with reverb and delay as sends, not inserts — route to dedicated Mixer send tracks carrying `valhalla_vintageverb` (or Fruity Reeverb 2) and `valhalla_delay` (or Fruity Delay 3), per `knowledge_base/mixing/reverb/reverb_send_vs_insert.md`'s send-routing discipline, and set send levels last so the wet/dry balance is judged against the vocal's final, fully-processed tone rather than an intermediate one. `izotope_nectar` can substitute for several of these individual stages within one plugin instance for producers who prefer an all-in-one channel strip, following the same signal-order logic internally.

## Common mistakes

Starting this chain on a vocal that hasn't finished comping or pitch correction, forcing every EQ and compression decision to be redone once the upstream take changes. De-essing only once before compression and never re-checking afterward, missing sibilance the compression stages themselves reintroduce. Collapsing both compression stages into one aggressive setting instead of splitting level-control and tone-shaping into two lighter, sequential stages, which tends to either over-flatten the performance or fail to add the intended character. Setting reverb/delay send levels early, before EQ and saturation are finalized, which means judging spatial balance against a vocal tone that's about to change.
