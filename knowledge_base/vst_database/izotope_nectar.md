---
plugin_name: "Nectar 4"
developer: "iZotope"
category: "vocal processing"
type: "vocal channel-strip suite (multi-module: EQ, compression, de-esser, pitch correction, harmony, reverb, delay, saturation)"
cpu_usage: "high"
best_genres:
  - pop
  - contemporary_r_and_b
  - hip_hop
strengths:
  - "Bundles a full vocal-production chain — dynamic/pitch-tracking EQ, two compressors, de-esser, gate, pitch correction, a Vocal Harmonizer, Dimension (chorus/flanger/phaser), saturation, reverb, and delay — into one plugin rather than assembling a chain from separate single-purpose tools."
  - "Includes a bundled Melodyne Essential license alongside its own real-time pitch-correction module, giving access to both graphical/corrective and real-time/creative pitch-correction workflows from a single purchase (see `knowledge_base/vst_database/celemony_melodyne.md`)."
  - "Vocal Assistant analyzes the input vocal and proposes a starting-point chain across the bundled modules, useful as a fast first pass comparable to Ozone's Master Assistant for full-mix mastering (`knowledge_base/vst_database/izotope_ozone.md`)."
  - "Vocal Harmonizer can generate stylized, deliberately robotic harmony effects in addition to subtle pitch-based harmony, covering some of the same 'obviously processed' aesthetic territory as a hard-tuned Auto-Tune vocal without requiring separately programmed harmony parts."
weaknesses:
  - "Running a dozen-plus processing modules in one plugin instance is CPU-heavy compared to instantiating only the specific single-purpose tools a given vocal actually needs (a de-esser and a compressor, for instance, without the full bundled suite)."
  - "As with Ozone's Master Assistant, the Vocal Assistant's suggested starting chain is generic — it can't know whether a genre wants transparent, corrective vocal processing or a deliberately audible, stylized character, so its recommendation still needs to be evaluated against the specific genre's documented vocal-production philosophy rather than accepted as a finished result."
alternatives:
  - "A manually assembled vocal chain from single-purpose plugins (Antares Auto-Tune Pro or Celemony Melodyne for pitch, a dedicated compressor and de-esser) for more surgical, per-stage control"
  - "iZotope Ozone (full-mix mastering suite rather than a vocal-specific channel strip — see `knowledge_base/vst_database/izotope_ozone.md`)"
  - "Waves Vocal Rider / Waves OVox for narrower, single-purpose vocal tasks"
recommended_settings:
  - "Full vocal-production pass on a pop/R&B lead vocal: EQ module for tonal shaping, compressor(s) for level control, de-esser tuned to the 4-10kHz sibilance range per `knowledge_base/mixing/vocal_processing/de_essing.md`, pitch-correction module set for transparent or stylized correction depending on genre intent, reverb/delay as the final spatial layer per `knowledge_base/mixing/vocal_processing/vocal_chain_signal_order.md`'s documented reverb-last pattern."
  - "Harmony-stack generation without recording multiple takes: Vocal Harmonizer set to follow the underlying chord/key, blended alongside (not replacing) any real doubled/stacked takes per `knowledge_base/mixing/vocal_processing/doubling_and_harmony_stacking.md`'s guidance on natural variation between stacked parts."
common_uses:
  - "All-in-one vocal-production chain assembly without switching between multiple separate plugins"
  - "Fast first-pass vocal processing via Vocal Assistant, as a starting point rather than a finished chain"
  - "Harmony generation via the Vocal Harmonizer module as an alternative or supplement to recorded doubling/stacking"
tags: ["izotope", "nectar", "vocal-processing", "channel-strip", "pitch-correction", "mixing"]
---

# Nectar 4

Nectar 4 (iZotope) is a vocal-specific channel-strip suite that bundles the full standard vocal-production chain — EQ, compression, de-essing, gating, pitch correction, harmony generation, modulation, saturation, reverb, and delay — into a single plugin, alongside a bundled Melodyne Essential license and an AI-assisted Vocal Assistant that proposes a starting-point chain from an analyzed vocal take. It sits alongside iZotope's Ozone (already documented in this knowledge base) as the vocal-specific counterpart to Ozone's full-mix mastering role: where Ozone consolidates a mastering chain, Nectar consolidates a vocal-mixing chain.

This knowledge base's genre corpus does not currently name Nectar directly by product, unlike Auto-Tune and Melodyne, which are cited extensively across dozens of genre files. The entry below is grounded in Nectar's verified real feature set and in this knowledge base's general vocal-processing technique documentation (de-essing, pitch-correction philosophy, doubling/harmony), rather than in direct genre-file citations of the plugin by name — that distinction is worth stating explicitly rather than implying a level of genre-corpus grounding this entry doesn't actually have.

## Sound Character and Strengths

Nectar's module lineup maps directly onto the vocal-chain sequence documented in `knowledge_base/mixing/vocal_processing/vocal_chain_signal_order.md` — corrective EQ, compression paired with de-essing, pitch correction, then reverb/delay as the final spatial stage — but assembled within one plugin's signal flow instead of requiring separate instances chained manually. Its bundled Melodyne Essential license is a genuinely distinct capability from its own real-time pitch-correction module: the two cover the transparent/graphical and real-time/knob-based workflows documented separately in this knowledge base's `celemony_melodyne.md` and `antares_auto_tune_pro.md` entries, meaning Nectar can approximate either approach without a separate purchase. The Vocal Harmonizer's ability to generate deliberately stylized, "creative robotic" harmony effects (per its verified feature set) gives it some of the same audible-processing character documented for hard-tuned Auto-Tune vocals, without requiring a producer to record or program each harmony part by hand.

## Weaknesses

Running a dozen-plus modules within one plugin instance is heavier on CPU than instantiating only the specific tools a given vocal needs — a vocal that only needs de-essing and light compression doesn't require the full bundled suite running in the background. The Vocal Assistant's proposed starting chain, like Ozone's Master Assistant, is a generic analysis-driven suggestion rather than a genre-aware one: it has no way to know whether the vocal in question belongs to a genre documented in `knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md`'s transparent cluster (where correction should be inaudible) or its stylized cluster (where audible processing is the point), so its default suggestion still needs to be evaluated against that distinction rather than trusted as a finished result.

## Common Mistakes

Accepting the Vocal Assistant's suggested chain without checking it against the target genre's actual vocal-processing philosophy — the same failure mode documented for Ozone's Master Assistant in `knowledge_base/vst_database/izotope_ozone.md`, applied here to vocal-specific processing rather than full-mix mastering. Running the full bundled module chain by default when only one or two specific stages (say, just de-essing) are actually needed for a given vocal take.

## Cross-References

- `knowledge_base/mixing/vocal_processing/vocal_chain_signal_order.md` — the general chain-ordering logic Nectar's module sequence implements within one plugin
- `knowledge_base/mixing/vocal_processing/de_essing.md` — the sibilance-control step Nectar's de-esser module addresses
- `knowledge_base/mixing/vocal_processing/doubling_and_harmony_stacking.md` — the recorded-take-based technique the Vocal Harmonizer module offers a generated alternative to
- `knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md` — the transparent-vs-stylized distinction that should guide how Nectar's pitch-correction and harmony modules are configured
- `knowledge_base/vst_database/celemony_melodyne.md` — the bundled Melodyne Essential engine included with Nectar
- `knowledge_base/vst_database/antares_auto_tune_pro.md` — the real-time correction workflow Nectar's own pitch-correction module approximates
- `knowledge_base/vst_database/izotope_ozone.md` — iZotope's full-mix mastering-suite counterpart to Nectar's vocal-specific role, sharing the same AI-assisted-starting-point design philosophy
