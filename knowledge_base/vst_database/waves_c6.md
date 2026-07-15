---
plugin_name: "C6 Multiband Compressor"
developer: "Waves"
category: "compressor"
type: "multiband compressor (6-band: 4 crossover-linked bands + 2 floating bands) with Mid/Side mode"
cpu_usage: "low"
best_genres:
  - pop
  - hip_hop
  - rock
  - house
  - trap
strengths:
  - "Paragraphic six-band layout combines 4 bands linked by adjustable crossover regions with 2 independent floating bands that sit outside the crossover matrix entirely — the floating bands are ideal for a narrow surgical fix (de-essing, a single resonance) while the 4 main bands simultaneously handle broad dynamics control."
  - "Each band can be set to compression, upward expansion, limiting, or dynamic-EQ-style static gain independently, so C6 can function as a multiband compressor, a multiband expander/gate, and a rough multiband EQ within one instance."
  - "Dedicated per-band SideChain section with internal or external triggering and adjustable filtering, so each band's dynamics can react to a different part of the spectrum than the one being processed."
  - "Mid/Side stereo mode allows the center (mono) and side (stereo-width) content to be processed independently per band, useful for taming low-end mono energy without touching stereo-width high content, or vice versa."
  - "Waves' ARC (Auto Release Control) auto-optimizes each band's release behavior for program-dependent transparency instead of requiring a single fixed release time to work across an entire performance."
  - "Low CPU cost and low native latency (64 samples at 44.1-48kHz), making it practical to run on many channels including vocal and mastering-bus duty simultaneously."
weaknesses:
  - "The 4 main bands share a linked crossover matrix, so reshaping their boundaries moves shared crossover points rather than repositioning one band independently — less flexible than FabFilter Pro-MB's freely-placed, independent bands."
  - "Six bands' worth of compression, expansion, sidechain, and gain parameters in one paragraphic window is a lot of surface area to learn relative to a purpose-built single-task tool like a dedicated de-esser."
alternatives:
  - "FabFilter Pro-MB (see `fabfilter_pro_mb.md`) — more flexible freely-placed bands and a Dynamic Phase mode, at higher CPU cost and a steeper setup workflow"
  - "Xfer OTT (see `xfer_ott.md`) — fast, characterful three-band alternative for bass/glue density rather than C6's surgical multiband correction"
  - "Waves SSL G-Master Buss Compressor (see `waves_ssl_g_master_buss_compressor.md`) or FabFilter Pro-C 2 (see `fabfilter_pro_c_2.md`) — single-band alternatives when the dynamics problem isn't frequency-specific"
recommended_settings:
  - "De-essing via a floating band: set Floating Band 1 to roughly 5-8kHz with a narrow bandwidth, compression mode with fast attack/release and a high ratio, threshold trimmed to trigger only on sibilant peaks while the 4 main bands stay free for broader dynamics — see `knowledge_base/mixing/vocal_processing/de_essing.md`."
  - "Bass/element tightening: Band 1 covering up to roughly 100-150Hz (tuned to the source's fundamental), compression ratio 3:1-4:1, ARC engaged for program-dependent release rather than a fixed value — see `knowledge_base/mixing/compression/multiband_compression_for_mix_element_control.md`."
  - "Mastering-bus glue: 4-band split near the common 100-150Hz and 2-5kHz crossover boundaries, gentle ratios with only a couple dB of gain reduction per band, Mid/Side mode engaged so low-end mono energy can be controlled independently from stereo-width high content — see `knowledge_base/mastering/dynamics/multiband_compression_and_limiter_chain_ordering.md` and `knowledge_base/mastering/stereo/mid_side_eq_at_mastering.md`."
common_uses:
  - "Vocal de-essing and de-popping using the floating bands"
  - "Mix-bus and mastering-bus frequency-specific dynamics correction"
  - "Taming harshness or boosting warmth on guitar and other instrument tracks"
  - "Mid/Side-specific low-end or high-end control at the mastering stage"
tags: ["waves", "c6", "multiband-compressor", "multiband", "de-essing", "mastering", "mid-side", "sidechain"]
---

# C6 Multiband Compressor

C6 (Waves) is a six-band multiband compressor built around a paragraphic interface: four bands linked by adjustable crossover regions handle broad, frequency-banded dynamics control, while two additional floating bands sit outside that crossover matrix entirely and can be placed anywhere in the spectrum for a narrow, surgical fix. Each of the six bands can independently run as a compressor, an upward expander, a limiter, or static dynamic-EQ-style gain, and each has its own sidechain section — which is why C6 gets used as a de-esser, a multiband compressor, and a rough corrective EQ, often within the same instance.

## Sound Character and Strengths

C6's split between four crossover-linked bands and two independent floating bands is its defining structural idea: the four main bands give the broad, evenly-divided frequency-band control that a mastering-stage multiband compressor needs, while the floating bands work like a built-in narrow-band de-esser or resonance tamer that doesn't disturb the main crossover setup. Its Mid/Side mode extends that same per-band independence into the stereo domain, letting a low band tighten mono bass energy without touching the stereo-width information sitting in the same frequency range on other bands. ARC (Auto Release Control) removes the need to hand-pick a single release time that has to work across an entire performance's dynamic range, adapting instead to the material band by band.

## Weaknesses

The four main bands' crossover points are linked together as a matrix, so adjusting one boundary affects the adjacent band rather than moving independently — a real constraint compared with FabFilter Pro-MB, where every band is placed and sized independently of the others. C6 also presents a lot of surface area at once: six bands, each with compression/expansion/limiting mode selection, sidechain filtering, and gain controls, in one paragraphic window, which is considerably more to parse than a single-purpose de-esser or a simpler three-band tool like Xfer OTT.

## Common Mistakes

**Using only the four main bands and ignoring the floating bands.** The floating bands are what let C6 do narrow, surgical work (de-essing, taming one resonant frequency) without reshaping the main crossover setup — leaving them unused means falling back on the four linked bands for jobs they're not well suited to.

**Applying Mid/Side processing without first checking whether the target problem is actually a mono/stereo-width issue.** Per `knowledge_base/mastering/stereo/mid_side_eq_at_mastering.md`, Mid/Side processing is a targeted tool for center-versus-width problems, not a default mode to engage on every band regardless of whether the problem is stereo-field-related.

## Cross-References

- `knowledge_base/mixing/vocal_processing/de_essing.md` — the floating-band de-essing use case C6 is commonly reached for
- `knowledge_base/mixing/compression/multiband_compression_for_mix_element_control.md` — the mix-stage, per-element multiband technique C6's main bands support
- `knowledge_base/mastering/dynamics/multiband_compression_and_limiter_chain_ordering.md` — the mastering-stage, whole-mix multiband technique and standard chain position
- `knowledge_base/mastering/stereo/mid_side_eq_at_mastering.md` — the Mid/Side principle C6's stereo mode implements
- `knowledge_base/vst_database/fabfilter_pro_mb.md` — the more flexible, freely-placed-band alternative
- `knowledge_base/vst_database/xfer_ott.md` — a fast, characterful alternative when surgical precision isn't the goal
