---
plugin_name: "Fairchild 670"
developer: "Universal Audio"
category: "compressor"
type: "vari-mu tube compressor/limiter (hardware emulation of the Fairchild 670)"
cpu_usage: "low"
best_genres:
  - soul
  - r_and_b
  - motown_sound
  - classic_country
strengths:
  - "Vari-mu (tube variable-transconductance) gain reduction produces a soft, increasingly non-linear knee as compression increases, giving a naturally gentle, 'glue'-oriented character even at higher ratios — the specific behavior `knowledge_base/mixing/compression/compressor_topology_comparison.md` names the Fairchild 670 for directly."
  - "Two-channel (stereo) design with independent lateral/vertical stereo modes, useful for both mono-source warmth and full mix-bus stereo-image control."
  - "Universal Audio's emulation models the complete tube amplifier and transformer sections rather than just the gain-reduction curve, aiming to capture harmonic coloration a simpler circuit model would miss."
  - "Historic reference status: the original hardware (only around 150 units built) is one of the most famous mastering and mix-bus compressors in recording history, cited on classic Motown, soul, and Beatles-era masters."
weaknesses:
  - "It is an emulation of an extremely expensive, rare vintage tube unit — its value is entirely in that specific vari-mu coloration, so it is a poor fit whenever fully transparent gain reduction is the actual goal."
  - "Like other opto/vari-mu topologies, its slow, program-dependent character is not built for catching fast, sharp transients; per `compressor_topology_comparison.md`, that job belongs to FET or VCA topology instead."
  - "Deeper, more idiosyncratic control set (six time-constant settings, threshold-per-channel) than a simpler two-knob opto compressor, which can make it slower to dial in for engineers unfamiliar with the original hardware's workflow."
alternatives:
  - "Universal Audio LA-2A (see `universal_audio_la_2a.md`) — opto topology, a related but mechanically distinct 'glue and warmth' character"
  - "Universal Audio 1176 (see `universal_audio_1176.md`) — fast FET topology for transient-catching rather than gentle glue"
  - "Waves SSL G-Master Buss Compressor (see `waves_ssl_g_master_buss_compressor.md`) — VCA-topology bus glue for a punchier, more modern-sounding alternative"
recommended_settings:
  - "Vintage soul/R&B recording-chain warmth: slow attack, musical time-constant setting, light gain reduction — used for glue and harmonic warmth rather than aggressive transient shaping, per `knowledge_base/genres/r_and_b/soul.md`."
  - "Mix-bus or master-bus glue: light gain reduction (1-3dB), slower time constant, leaning on the vari-mu circuit's inherent softness rather than a fast attack/release setting."
common_uses:
  - "Vintage-character mix-bus and master-bus glue compression"
  - "Vocal and instrument warmth in classic soul, R&B, and Motown-style productions"
  - "Mastering-stage gentle dynamic control where tube coloration is a desired part of the result"
tags: ["universal-audio", "fairchild-670", "vari-mu", "compressor", "hardware-emulation", "mixing", "mastering"]
---

# Fairchild 670

The Fairchild 670 is a vari-mu (variable-mu, tube-based) stereo compressor/limiter originally built by Fairchild Recording Equipment Corporation starting in 1959 — a 65-pound unit with 14 transformers and 20 vacuum tubes that became one of the most legendary pieces of studio gear in recording history, in part because so few were made. Universal Audio's plugin emulation, modeled on producer/engineer Allen Sides' unit from Ocean Way Studios, models the complete tube amplifier and transformer sections rather than just an approximated gain-reduction curve. Its gain reduction comes from a vacuum tube's variable transconductance, which `knowledge_base/mixing/compression/compressor_topology_comparison.md` describes as producing "a soft, increasingly non-linear knee as more compression is applied" — a fundamentally gentler, more program-dependent behavior than a VCA or FET circuit.

## Sound Character and Strengths

`knowledge_base/genres/r_and_b/soul.md` names the Fairchild directly as part of classic soul's actual recording chain, alongside tape saturation and mic bleed: "the specific use of analog gear like Fairchild compressors and Pultec EQs." Its mixing-approach field is even more explicit about the sonic goal: "Slower attack, musical compression (Fairchild, LA-2A). The goal is glue and warmth, not aggressive transient shaping." `compressor_topology_comparison.md` calls this "the clearest statement in the corpus" of what vari-mu and opto topologies share and FET does not — both are reached for specifically when the point is cohesion and tonal warmth rather than catching a transient. The Fairchild's reputation as a mastering-bus tool (famously used at Abbey Road on Beatles masters, among many others) also reflects this — its gentle, musical gain reduction can sit across an entire mix without drawing attention to itself as "compression" in the way a faster topology would.

## Weaknesses

As with any hardware emulation, the Fairchild 670's entire appeal is its specific vari-mu coloration — for a mix or master that calls for genuinely transparent, uncolored dynamic control, that coloration becomes a liability rather than an asset. Its slow, program-dependent response also means it shares opto compression's fundamental limitation: it is not built to catch a sharp transient quickly, and per `compressor_topology_comparison.md`, reaching for it on material that actually needs fast transient control works against the tool's design rather than with it. Its control set is also less approachable than a simple two-knob opto compressor — six selectable time-constant settings and per-channel threshold controls reflect the original hardware's mastering-engineer-oriented workflow rather than a quick-dial-in mix tool.

## Common Mistakes

**Using the Fairchild for fast transient control instead of glue.** Per `compressor_topology_comparison.md`, vari-mu and opto topologies are both reached for specifically to avoid aggressive transient shaping — a source that actually needs its transients caught and controlled is better served by a FET (1176) or VCA-topology compressor.

**Treating "vintage tube compressor" as a single undifferentiated category.** `compressor_topology_comparison.md` warns directly against this: an LA-2A emulation and a Fairchild 670 emulation both avoid aggressive transient shaping, but they arrive at that smoothness through different circuits (electro-optical cell vs. vacuum-tube variable transconductance) with genuinely different sonic side effects, and `soul.md` cites both by name as distinct tools within the same recording chain.

## Cross-References

- `knowledge_base/mixing/compression/compressor_topology_comparison.md` — the primary reference for vari-mu vs opto vs FET vs VCA topology, naming the Fairchild 670 as the vari-mu reference unit
- `knowledge_base/genres/r_and_b/soul.md` — direct citation of Fairchild compression as part of classic soul's recording-chain character
- `knowledge_base/vst_database/universal_audio_la_2a.md` — the mechanically distinct opto alternative most often cited alongside the Fairchild
- `knowledge_base/vst_database/universal_audio_1176.md` — the fast-FET counterpart for jobs the Fairchild's vari-mu circuit is not built for
- `knowledge_base/vst_database/waves_ssl_g_master_buss_compressor.md` — a VCA-topology alternative for punchier, more modern-sounding bus glue
