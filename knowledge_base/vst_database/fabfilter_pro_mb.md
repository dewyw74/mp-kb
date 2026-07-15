---
plugin_name: "Pro-MB"
developer: "FabFilter"
category: "compressor"
type: "multiband compressor/expander (up to 6 freely placed bands)"
cpu_usage: "medium"
best_genres:
  - pop
  - hip_hop
  - house
  - trap
  - djent
strengths:
  - "Bands are created freely at whatever frequency range needs work, rather than being locked to a fixed crossover ladder — the interactive display shows exactly which part of the spectrum stays untouched, and bands can be snapped together to recreate a traditional crossover setup when that's what's actually needed."
  - "Three selectable processing modes — Dynamic Phase (zero latency, no static phase shift, no pre-ringing), Linear Phase (no audible artifacts when crossover frequencies are moved), and Minimum Phase (traditional, lowest CPU) — let the plugin match the transparency/CPU tradeoff to the task."
  - "Each band exposes threshold, range, attack, release, output gain, ratio, variable knee, lookahead (up to 20ms), variable stereo linking, mid- or side-only processing, and an external sidechain input that can trigger off a different, freely configurable frequency range than the band being processed."
  - "Adjustable crossover slope steepness (6-48dB/oct per crossover) gives control over how much bands bleed into each other, from soft and blended to steep and surgically isolated."
  - "Handles the full range of dynamics behavior per band — transparent compression, limiting, gating, and upward or downward expansion — rather than being compression-only, so one instance can both tighten a bass band and gate noise out of a high band."
weaknesses:
  - "Linear Phase mode, while eliminating crossover-adjustment artifacts, adds noticeably more latency and CPU load than Dynamic Phase mode — not a free upgrade, and unnecessary for tracking or performance contexts where latency matters."
  - "The freely-placed band workflow (versus a fixed set of crossover-linked bands) has a steeper learning curve than more constrained multiband tools like Waves C6's paragraphic layout or Xfer OTT's minimal three-knob approach."
  - "With many bands active, each carrying a full parameter set including per-band sidechain and lookahead, CPU cost climbs quickly relative to a single-band compressor like Pro-C 2."
alternatives:
  - "Waves C6 (see `waves_c6.md`) — fixed 4-band-plus-2-floating-band paragraphic layout with dedicated Mid/Side mode, a more constrained but faster-to-grasp alternative"
  - "Xfer OTT (see `xfer_ott.md`) — fast, characterful upward/downward multiband glue when Pro-MB's precision and per-band control aren't needed"
  - "FabFilter Pro-C 2 (see `fabfilter_pro_c_2.md`) — single-band alternative when the dynamics problem isn't frequency-specific"
recommended_settings:
  - "De-essing band: create a narrow band around 5-9kHz, fast attack (under 1ms) and fast release, high ratio, threshold trimmed so only sibilant peaks trigger gain reduction — see `knowledge_base/mixing/vocal_processing/de_essing.md`."
  - "Bass/element tightening band: low band up to roughly 100-150Hz (set to the specific source's fundamental range), ratio 3:1-4:1, moderate attack to preserve initial pluck/pick transient, lookahead engaged for consistent leveling — see `knowledge_base/mixing/compression/multiband_compression_for_mix_element_control.md`."
  - "Mastering glue: 3-band split around 100-150Hz and 2-5kHz crossover points, Linear Phase mode to avoid artifacts if crossovers get nudged later, gentle ratio (1.5:1-2:1) with only 1-2dB gain reduction per band, EQ before and a limiter after in the chain — see `knowledge_base/mastering/dynamics/multiband_compression_and_limiter_chain_ordering.md`."
common_uses:
  - "Frequency-specific corrective compression on individual mix elements (bass note-to-note evenness, de-essing, harsh resonance taming)"
  - "Mastering-stage multiband dynamics control on a finished stereo mix"
  - "Creative upward compression/expansion effects isolated to a specific frequency band"
tags: ["fabfilter", "pro-mb", "multiband-compressor", "multiband", "mastering", "mixing", "de-essing", "dynamics"]
---

# Pro-MB

Pro-MB (FabFilter) is a multiband compressor/expander offering up to six fully customizable bands that are created freely at any frequency range rather than being locked into a fixed crossover ladder. Where a conventional multiband compressor asks a user to first divide the spectrum into a fixed number of adjacent bands and then set parameters within each one, Pro-MB instead lets a band be drawn directly on the specific frequency range that has a problem, with the interactive display continuously showing which parts of the spectrum are being left alone. Combined with three selectable processing modes (Dynamic Phase, Linear Phase, and Minimum Phase) and a full per-band parameter set including sidechain and mid/side control, it functions as both a surgical corrective tool and a full mastering-chain multiband processor.

## Sound Character and Strengths

Pro-MB's defining feature is its band-creation workflow: instead of committing to a fixed number of crossover-linked bands up front, a band is placed exactly where the problem frequency range sits, and multiple bands can be layered or snapped together into a traditional crossover arrangement only when that's genuinely what the task calls for. This makes it equally suited to a narrow, surgical fix (a single band carved out for de-essing) and a broad mastering-stage 3-4 band split. Dynamic Phase mode is the plugin's other standout feature — it delivers essentially the same frequency response as traditional multiband processing without the latency or pre-ringing artifacts that linear-phase filtering introduces, only shifting phase when gain reduction is actually happening, which makes it usable in tracking and low-latency contexts where a fully linear-phase multiband compressor would not be.

## Weaknesses

The flexibility that makes Pro-MB precise also makes it slower to set up than a fixed-band tool — deciding where to place bands and how wide to make each one is a real design decision, not a matter of filling in a preset crossover template the way Waves C6's four-band-plus-floating-band layout works. Linear Phase mode, while eliminating audible artifacts when crossover points are adjusted mid-session, costs meaningfully more CPU and adds latency compared with Dynamic Phase mode, so it isn't a mode to leave on by default without reason. And with several bands active, each carrying its own attack/release/ratio/lookahead/sidechain parameter set, overall CPU load adds up faster than with a single-band compressor.

## Common Mistakes

**Defaulting to Linear Phase mode for everything.** Dynamic Phase mode covers the vast majority of use cases with far lower CPU cost and no added latency; Linear Phase is worth its cost specifically when crossover frequencies are still being actively adjusted and phase-artifact-free adjustment matters, or in a final mastering pass where CPU and latency are non-issues.

**Setting up a wide, generic 3-4 band split out of habit for a problem that's actually confined to one narrow frequency range.** Pro-MB's whole advantage over a fixed-crossover multiband compressor is the ability to place a single tightly-scoped band exactly on the problem — using it like a traditional multiband compressor for every job wastes that advantage.

## Cross-References

- `knowledge_base/mixing/compression/multiband_compression_for_mix_element_control.md` — the mix-stage, per-element multiband technique Pro-MB's freely-placed bands directly support
- `knowledge_base/mastering/dynamics/multiband_compression_and_limiter_chain_ordering.md` — the mastering-stage, whole-mix multiband technique and standard chain position (after EQ, before the limiter)
- `knowledge_base/mixing/vocal_processing/de_essing.md` — a narrow single-band Pro-MB use case
- `knowledge_base/vst_database/waves_c6.md` — the fixed-band-plus-floating-band alternative with a faster, more constrained workflow
- `knowledge_base/vst_database/xfer_ott.md` — a fast, characterful multiband alternative when precision isn't the goal
- `knowledge_base/vst_database/fabfilter_pro_c_2.md` — the single-band FabFilter compressor for non-frequency-specific dynamics problems
