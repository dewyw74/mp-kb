---
plugin_name: "Serum 2"
developer: "Xfer Records"
category: "synth"
type: "wavetable synth (hybrid semi-modular architecture)"
cpu_usage: "medium-high"
best_genres:
  - dubstep
  - brostep
  - future_bass
  - trance
  - uplifting_trance
  - hardstyle
  - bass_house
  - psytrance
  - riddim
strengths:
  - "Semi-modular routing that lets modulation sources, effects, and signal paths be rearranged far more freely than Serum 1's fixed signal-chain layout."
  - "Expanded oscillator options beyond wavetable-only, including sample playback and additional synthesis modes within the same voice architecture, reducing the need to reach for a separate instrument for hybrid patches."
  - "A rebuilt, more powerful effects rack with more device slots and more flexible routing than Serum 1's fixed effects chain."
  - "Retains Serum 1's core visual wavetable-editing workflow, so the fundamental sound-design approach that made the original popular carries over rather than requiring a relearned workflow."
weaknesses:
  - "Meaningfully higher CPU cost than Serum 1 given its more complex, flexible routing architecture — large multi-instance sessions need more aggressive freezing/bouncing discipline."
  - "The added semi-modular routing options increase the decision surface for a patch — building a simple, fast sound can take longer than in Serum 1's more constrained, opinionated layout."
  - "Newer plugin means a smaller third-party preset/wavetable-pack ecosystem than Serum 1's decade-plus back catalog, though this gap is closing quickly given the shared underlying wavetable format."
alternatives:
  - "Serum 1 (Classic) — see `xfer_serum.md`; still the better choice for CPU-constrained sessions or when Serum 1's simpler, faster workflow is all a patch needs"
  - "Vital"
  - "Phase Plant"
recommended_settings:
  - "Modern growl/riddim bass: combine a wavetable oscillator with a sample-playback layer routed through the expanded modulation matrix for hybrid formant-and-wavetable movement, using the rebuilt effects rack's added routing flexibility to chain distortion into a resonant filter in a non-default order."
  - "Evolving trance/progressive pad: use the semi-modular routing to feed one oscillator's output into another's modulation input for cross-modulation textures Serum 1's fixed chain couldn't achieve in a single instance."
common_uses:
  - "Everything Serum 1 is used for (808/bass design, supersaw leads, growl bass), with more headroom for hybrid wavetable/sample patches"
  - "Cross-modulation and semi-modular sound design within a single instance, reducing the need for external routing tricks"
  - "Patches requiring more effects-chain flexibility than Serum 1's fixed slot order allowed"
tags: ["serum-2", "xfer", "wavetable-synth", "semi-modular", "edm", "bass-design", "lead-design"]
---

# Serum 2

Serum 2 (Xfer Records, released 2024) is the successor to the original Serum — see `knowledge_base/vst_database/xfer_serum.md` for that earlier version, which Xfer continues to sell and support alongside the new release. Serum 2 keeps the visual, hands-on wavetable-editing workflow that made the original the default modern-EDM sound-design tool, while rebuilding the underlying architecture to be semi-modular: modulation routing, oscillator types, and the effects chain are all more freely reconfigurable than Serum 1's more fixed, opinionated signal path.

## What Changed From Serum 1

The clearest architectural shift is routing flexibility — where Serum 1 has a largely fixed signal chain (oscillators into filter into effects rack, in a set order), Serum 2's semi-modular approach lets a producer rearrange how modulation sources, oscillators, and effects connect to each other within a single patch. This directly extends the kind of cross-modulation and hybrid oscillator/sample-layer patches that previously required either external routing workarounds or a different, more modular instrument entirely. The effects rack was also rebuilt with more slots and more flexible ordering than Serum 1's fixed effects chain.

## Sound Character and Strengths

Serum 2 inherits Serum 1's core strength — a visual wavetable editor where the waveform display doubles as an editing surface — so a producer already fluent in Serum 1's wavetable-drawing and warping workflow can transfer that skill directly. The added semi-modular routing and expanded oscillator options (including sample-based sources within the same voice architecture) make it meaningfully more capable for hybrid, evolving, or cross-modulated patches than the original, without discarding the approachable core workflow that made Serum 1 popular in the first place.

## Weaknesses

The expanded routing flexibility comes at a real CPU cost — Serum 2 instances are generally heavier than equivalent Serum 1 patches, which matters in dense, multi-instance EDM sessions (trance and hardstyle arrangements with a dozen synth layers, for instance). The added decision surface (more routing options, more oscillator types) can also slow down a producer who just needs a fast, simple patch — for straightforward sounds, Serum 1's more constrained workflow is often quicker to a finished result.

## Choosing Between Serum 1 and Serum 2

Reach for Serum 2 specifically when a patch needs cross-modulation, hybrid wavetable/sample layering, or effects-chain routing flexibility that Serum 1's fixed signal path can't provide within a single instance. For straightforward bass, lead, and pluck design — the large majority of the patch types documented across this knowledge base's EDM genre files — Serum 1 remains a fully valid, lighter-weight choice, and there's no need to treat Serum 2 as a strict replacement for every use case.

## Common Mistakes

**Assuming Serum 2 obsoletes Serum 1 and should be used by default for every patch.** Per the CPU and workflow-speed tradeoffs above, Serum 1 is still the better tool for simple patches and CPU-constrained sessions — Serum 2's added power is worth its added cost specifically for patches that need the new routing flexibility.

**Not exploring the semi-modular routing and defaulting to Serum 1-style fixed-chain patch design.** A producer who builds every Serum 2 patch exactly the way they'd build it in Serum 1 is paying the CPU and complexity cost of the new architecture without using its actual advantage.

## Cross-References

- `knowledge_base/vst_database/xfer_serum.md` — the original Serum, still actively supported and often the better choice for lighter-weight or CPU-constrained patches
- `knowledge_base/sound_design/synthesis/wavetable_synthesis.md` — general wavetable synthesis technique, shared between both Serum versions
- `knowledge_base/genres/edm/dubstep.md`, `knowledge_base/genres/edm/trance.md`, `knowledge_base/genres/edm/hardstyle.md` — genre files citing Serum as a primary sound-design tool (predates the Serum 2 release but applies to either version)
