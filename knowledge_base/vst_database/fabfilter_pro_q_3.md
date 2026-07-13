---
plugin_name: "Pro-Q 3"
developer: "FabFilter"
category: "eq"
type: "dynamic EQ"
cpu_usage: "low"
best_genres:
  - house
  - techno
  - trance
  - hip_hop
  - pop
strengths:
  - "Spectrum-analyzer-integrated interface makes it fast to identify and target problem frequencies visually rather than sweeping by ear alone."
  - "Dynamic EQ mode lets any band act as a frequency-specific compressor/expander, addressing masking and resonance issues that a static EQ curve can't solve."
  - "Very low CPU usage per instance, making it practical to run on every channel in a large session without performance concerns."
  - "Mid/side and natural-phase/linear-phase filter modes cover both fast, low-latency mixing work and transparent mastering-stage EQ."
weaknesses:
  - "Its flexibility means it's easy to over-EQ — the visual spectrum display can invite chasing every small dip or peak rather than making a few decisive moves."
  - "Linear-phase mode adds latency, which matters for live tracking or low-latency monitoring situations."
alternatives:
  - "Ableton EQ Eight (stock, similar dynamic-EQ-adjacent workflow via automation)"
  - "Waves F6"
  - "iZotope Neutron's EQ module"
recommended_settings:
  - "Frequency masking fix (bass vs. kick): dynamic EQ band at the kick's fundamental (60-100Hz) on the bass channel, threshold set so it only ducks when the kick's energy is present."
  - "De-essing/resonance control: narrow dynamic EQ band at the resonant frequency, fast attack, moderate release, gain reduction only as needed to tame the peak."
common_uses:
  - "Subtractive EQ and frequency-masking resolution across mix elements"
  - "Dynamic, program-dependent frequency control (de-essing, resonance taming) without a separate dedicated plugin"
  - "Mastering-stage tonal balance adjustment in linear-phase mode"
tags: ["fabfilter", "pro-q-3", "eq", "dynamic-eq", "mixing"]
---

# Pro-Q 3

Pro-Q 3 (FabFilter) is a dynamic EQ built around a spectrum-analyzer-integrated interface — each EQ band is placed and shaped directly on a real-time frequency display, and any band can be switched from static to dynamic (compressor/expander-like) behavior. It's one of the most widely used EQs in modern mixing precisely because it collapses "find the problem frequency" and "fix the problem frequency" into a single visual workflow.

## Sound Character and Strengths

Pro-Q 3's dynamic EQ mode is its most consequential feature for the kind of frequency-masking problems documented in `knowledge_base/mixing/eq/frequency_masking.md` — instead of a static cut that's always active, a dynamic band can duck a specific frequency range only when it's actually causing masking (e.g., only when the kick's transient is present), preserving more of the source material's natural tone the rest of the time. Its natural-phase mode keeps latency low for real-time mixing work, while linear-phase mode is available when phase-transparent processing matters more than speed, such as at the mastering stage.

## Weaknesses

Because every parameter is visible and adjustable directly on the spectrum display, Pro-Q 3 makes it unusually easy to over-EQ — chasing every visible peak or dip on the analyzer rather than making a small number of purposeful, ear-led decisions. This is a workflow risk more than a plugin flaw, but it's common enough to be worth naming directly.

## Common Mistakes

Treating the spectrum analyzer as the primary decision-making tool instead of a secondary confirmation of what's already been heard — per `knowledge_base/mixing/eq/subtractive_eq.md`'s philosophy, EQ decisions should generally be led by ear, with the visual display used to locate and confirm a problem already identified by listening, not the other way around.

## Cross-References

- `knowledge_base/mixing/eq/frequency_masking.md` — the masking-resolution use case Pro-Q 3's dynamic EQ mode directly addresses
- `knowledge_base/mixing/eq/subtractive_eq.md` — the general subtractive EQ philosophy this plugin implements
- `knowledge_base/vst_database/fabfilter_pro_c_2.md` — commonly paired with Pro-Q 3 in a mix chain (EQ before or after compression)
