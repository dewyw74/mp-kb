---
plugin_name: "Ozone"
developer: "iZotope"
category: "other"
type: "mastering suite (multi-module: EQ, dynamics, imaging, loudness/limiting, tonal-balance assistant)"
cpu_usage: "high"
best_genres:
  - pop
  - hip_hop
  - house
  - trance
strengths:
  - "Bundles the full mastering-chain toolset (EQ, multiband dynamics, stereo imaging, a maximizer/limiter, and a tonal-balance reference module) into one integrated plugin rather than requiring separate tools chained manually."
  - "Includes AI-assisted 'Master Assistant' and tonal-balance-reference tooling that analyzes a mix and suggests a starting-point chain, useful as a fast first pass or a sanity check against genre-typical tonal balance."
  - "Codec/streaming-platform preview tools let a producer audition how a master will sound after common lossy-encoding and loudness-normalization processing before final export."
  - "Individual modules (the multiband dynamics processor and the maximizer in particular) are also usable standalone within the suite for more surgical, single-purpose mastering-chain steps."
weaknesses:
  - "Heavier CPU load than assembling an equivalent chain from lighter single-purpose plugins (per `knowledge_base/vst_database/fabfilter_pro_q_3.md`, `knowledge_base/vst_database/fabfilter_pro_c_2.md`), since Ozone runs multiple processing modules within one host plugin instance."
  - "The AI-assisted starting-point suggestions are a starting point, not a finished master — per `knowledge_base/mastering/dynamics/matching_master_transparency_to_source_character.md`'s broader point, a generic tonal-balance target doesn't know a track's deliberate genre-specific character (intentional harshness, vintage coloration) the way a human mastering decision does."
alternatives:
  - "A manually assembled chain of single-purpose plugins (FabFilter Pro-Q 3 + Pro-C 2 + a dedicated multiband compressor + limiter) for more surgical control over each stage"
  - "Ableton's stock EQ Eight/Compressor/Multiband Dynamics devices (see `ableton_eq_eight.md`, `ableton_compressor_and_glue_compressor.md`) for a lighter, fully in-DAW mastering chain"
recommended_settings:
  - "Full mastering pass: EQ module for broad tonal-balance correction, multiband dynamics module for frequency-specific control per `knowledge_base/mastering/dynamics/multiband_compression_and_limiter_chain_ordering.md`'s chain-ordering principle, imaging module for mono-compatibility per `knowledge_base/mixing/stereo/mid_side_processing_and_mono_compatibility.md`, and the maximizer set with true-peak-aware ceiling per `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md`."
  - "Streaming-safety check: use the codec preview tool to audition the master post-normalization before finalizing, cross-checked against `knowledge_base/mastering/streaming/platform_normalization_behavior.md`'s platform-specific behavior guidance."
common_uses:
  - "All-in-one mastering chain assembly without switching between multiple separate plugins"
  - "Tonal-balance reference checking against genre-typical targets"
  - "Pre-export codec/streaming-normalization preview"
tags: ["ozone", "izotope", "mastering-suite", "multiband", "loudness", "mastering"]
---

# Ozone

Ozone (iZotope) is a mastering suite that bundles the full conventional mastering chain — EQ, multiband dynamics, stereo imaging, and a maximizer/limiter — into a single integrated plugin, alongside a tonal-balance reference module and AI-assisted starting-point tooling. Where a mastering chain assembled from individual FabFilter- or Ableton-stock-style plugins (per `knowledge_base/vst_database/fabfilter_pro_q_3.md` and `knowledge_base/vst_database/ableton_eq_eight.md`) requires manually chaining several separate tools, Ozone consolidates that chain into one host plugin instance with modules designed to work together.

## Sound Character and Strengths

Ozone's multiband dynamics and maximizer modules directly implement the chain-ordering principle documented in `knowledge_base/mastering/dynamics/multiband_compression_and_limiter_chain_ordering.md` — broad EQ, then frequency-specific dynamics control, then a final loudness/ceiling stage — within one plugin's signal flow rather than requiring a producer to assemble and order that chain from separate tools. Its tonal-balance reference module compares a track's frequency balance against genre-typical curves, useful as a sanity check against the kind of genre-specific frequency-balance guidance documented throughout this knowledge base's mastering entries. Its codec/streaming preview tooling directly supports the platform-safety concerns in `knowledge_base/mastering/streaming/platform_normalization_behavior.md` and `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md` by letting a producer hear the post-normalization result before committing to an export.

## Weaknesses

Running several processing modules within one plugin instance carries more CPU overhead than a leaner, single-purpose-plugin-per-stage chain. More importantly, Ozone's AI-assisted suggestions and tonal-balance reference are a generic starting point — per `knowledge_base/mastering/dynamics/matching_master_transparency_to_source_character.md` and `knowledge_base/mastering/dynamics/preserving_intentional_harshness_vs_smoothing.md`, a track with deliberately unconventional tonal character (intentional harshness, vintage vinyl/tape coloration) needs a mastering decision that recognizes and preserves that intent — a generic reference-curve suggestion has no way to know a track's harshness or lo-fi coloring is deliberate rather than a mix flaw.

## Choosing Ozone Over a Manually Assembled Chain

Ozone's integrated workflow is a genuine speed advantage when a mastering pass needs the full standard chain and the producer wants one plugin's automation/preset recall rather than managing several separate instances. A manually assembled chain of dedicated single-purpose plugins remains the better choice when a specific stage needs more surgical control than Ozone's corresponding module offers, or when CPU headroom is tight enough that running several lighter single-purpose plugins beats one heavier all-in-one instance.

## Common Mistakes

**Accepting Ozone's AI-assisted master suggestion as a finished result without checking it against the track's actual intended character.** Per `knowledge_base/mastering/dynamics/preserving_intentional_harshness_vs_smoothing.md`, a generic tonal-balance-matching suggestion can't distinguish a mix flaw from a deliberate genre-defining choice — always evaluate the suggestion against what the track is actually going for, don't apply it blind.

**Running Ozone's full module chain when only one specific stage (say, just the maximizer) is actually needed.** This adds unnecessary CPU load for capability the task doesn't require.

## Cross-References

- `knowledge_base/mastering/dynamics/multiband_compression_and_limiter_chain_ordering.md` — the chain-ordering principle Ozone's module sequence implements
- `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md`, `knowledge_base/mastering/streaming/platform_normalization_behavior.md` — the true-peak and platform-safety concerns Ozone's maximizer and codec-preview tools address
- `knowledge_base/mastering/dynamics/preserving_intentional_harshness_vs_smoothing.md`, `knowledge_base/mastering/dynamics/matching_master_transparency_to_source_character.md` — why Ozone's generic tonal-balance suggestions need human judgment against a track's actual intended character
- `knowledge_base/vst_database/fabfilter_pro_q_3.md`, `knowledge_base/vst_database/fabfilter_pro_c_2.md` — single-purpose plugin alternatives for a more manually-assembled, surgical mastering chain
