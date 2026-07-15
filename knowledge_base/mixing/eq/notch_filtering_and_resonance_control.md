---
technique_name: "Notch Filtering and Resonance Control"
category: eq
problem_solved: "A narrow, specific frequency that rings, honks, or feels harsh/piercing independent of the overall tonal balance — a problem that a broad tonal EQ move would either miss or over-correct for"
parameters:
  q_width: "Narrow/high-Q for true resonance removal (isolating a specific ringing frequency); the genre corpus more often documents wider, gentler cuts for general harshness reduction than true surgical notches"
  sweep_technique: "Boost a narrow band and sweep it across the suspect range until the offending frequency jumps out, then invert to a cut at that exact point — standard practice for locating a resonance before notching it"
  harsh_midrange_zone: "1-4kHz is the most commonly cited zone for harshness/piercing content in dense vocal or ensemble material"
  surgical_vs_broad: "Genres with sparse arrangements (minimal techno, goa trance, chicago house) document deliberately less surgical, more forgiving EQ than genres with dense competing layers (symphonic black metal, djent)"
signal_chain_position: "Per-element, applied after identifying the specific offending frequency by ear (typically via boost-and-sweep), before broader tonal shaping"
genre_applicability:
  - symphonic_black_metal
  - choral_music
  - djent
  - goa_trance
  - chicago_house
  - nu_disco
  - ghetto_house
  - minimal_techno
related_techniques:
  - subtractive_eq
  - frequency_masking
  - dynamic_eq
tags: ["notch-filtering", "resonance", "surgical-eq", "harshness", "narrow-cut"]
---

# Notch Filtering and Resonance Control

Notch filtering — a narrow, targeted cut aimed at a single problem frequency rather than a broad tonal adjustment — is a less frequently named technique in this knowledge base's genre corpus than broader subtractive or additive EQ, and it's worth being upfront about that: most genre entries that discuss "surgical" EQ are describing the general precision of their carving philosophy (see `subtractive_eq.md` and `frequency_masking.md`) rather than literal narrow-Q resonance notching. The clearest genuine example of true resonance-specific cutting in the corpus is `choral_music.md`'s harshness-taming guidance; the rest of what follows documents the broader surgical-vs-forgiving spectrum genres sit on, which is the context that determines how aggressively (and how narrowly) notch-style correction gets used.

## The Clearest Documented Case: Taming Ensemble Harshness

`choral_music.md` gives the most direct description of narrow-band problem-solving in the corpus: "With 40+ voices singing simultaneously, the 1kHz-4kHz range can become overwhelmingly harsh and piercing. Gentle, wide cuts in the upper midrange are often necessary." Notably, the entry specifies *wide* cuts rather than a narrow notch — this is a deliberate distinction worth preserving: true notch filtering (high-Q, narrow) is reserved for a genuinely isolated resonant frequency (a ringing snare overtone, a specific harsh reed squeal, a boxy room mode), while a broad buildup across a wide range like 1-4kHz in a 40-voice choir calls for a gentler, wider cut instead — using a narrow notch there would leave most of the harsh content untouched while carving an audible, unnatural-sounding hole at one specific frequency.

## Surgical Precision as a Necessity in Dense Arrangements

Some genres document needing genuinely surgical (narrow, precise) EQ work specifically because two harmonically similar layers are competing for the same territory. `symphonic_black_metal.md` names this directly: "Requires careful frequency division between treble-forward black metal guitars and a dense orchestral arrangement occupying similar mid-to-high frequency territory — more surgical EQ work than either parent genre alone typically requires." `djent.md` documents a related low-end version of the same need, driven by extended-range instruments rather than orchestral layering: "careful high-pass filtering prevents mud in complex polyrhythmic passages" — precision here isn't about a resonance so much as a tightly-packed multi-layer arrangement where broad cuts would remove wanted content along with the unwanted overlap.

## Deliberately Non-Surgical Genres

At the opposite end, several genres explicitly document choosing *not* to carve surgically, treating a rawer, less-precise EQ approach as part of the intended aesthetic rather than a shortcoming. `chicago_house.md`: "Simple, direct EQ — boost the kick and bass for club weight, minimal surgical carving compared to modern productions; the rawness is part of the aesthetic." `ghetto_house.md` states the identical principle for its own lineage: "Direct, unsubtle EQ favoring a boosted kick and bass for maximum club impact; minimal surgical carving, consistent with the genre's raw, low-budget production ethos." `goa_trance.md` frames the same choice as a consequence of its analog-hardware origins: "Simpler, warmer EQ approach reflecting the genre's analog hardware roots — less surgical carving than modern psytrance, with acid lines given room via filter automation rather than aggressive EQ notching" — this is the one place in the corpus that names "notching" directly, specifically to say the genre avoids it in favor of automation instead. `nu_disco.md` documents the same restraint applied to low-end decisions specifically: "Warm low-mids are preserved rather than scooped (unlike modern EDM's often more surgical low-end approach)." `minimal_techno.md` sits at an interesting middle point — its arrangement is sparse enough that "every frequency decision is exposed," which the entry frames as demanding precision ("surgical precision") despite the genre having very few elements to carve around in the first place.

## When to Reach for a True Narrow Notch vs. a Wide Cut

Synthesizing the corpus evidence with standard practice: a genuinely narrow, high-Q notch is the right tool when a single identifiable frequency is ringing, resonating, or feels louder than the material around it — located by boosting a narrow band and sweeping it until the problem jumps out, then inverting that boost into a cut at the same point. A wider, gentler cut — like `choral_music.md`'s "gentle, wide cuts in the upper midrange" — is the right tool when the problem is a broad buildup across many overlapping sources rather than one specific resonant frequency. Reaching for a narrow notch on a broad problem leaves most of the issue unaddressed; reaching for a wide cut on a genuinely narrow resonance removes far more musical content than necessary.

## Common Mistakes

**Notching narrowly when the actual problem is broad.** `choral_music.md`'s wide-cut solution to 1-4kHz choir harshness would sound audibly holed-out if applied as a narrow notch instead — matching cut width to problem width is the core judgment call this technique requires.

**Over-applying surgical carving in genres whose aesthetic depends on rawness.** `chicago_house.md`, `ghetto_house.md`, and `goa_trance.md` all treat minimal, non-surgical EQ as a deliberate genre marker — imposing modern surgical precision on this material contradicts the intended sound rather than improving it.

**Sweeping for a resonance without first confirming one exists.** Boost-and-sweep is a diagnostic technique for locating a specific problem frequency — using it reflexively on material that doesn't have an isolated resonance (as in the dense-but-not-resonant `symphonic_black_metal.md` and `djent.md` cases) leads to chasing a notch that isn't the actual fix; those genres solve their density problems through broader frequency division, not narrow notching.

## Cross-References

- `knowledge_base/genres/classical/choral_music.md` — the clearest documented case of wide, gentle cutting to tame ensemble harshness in the 1-4kHz range
- `knowledge_base/genres/metal/symphonic_black_metal.md` and `knowledge_base/genres/metal/djent.md` — surgical precision as a necessity in dense, harmonically overlapping arrangements
- `knowledge_base/genres/edm/goa_trance.md`, `knowledge_base/genres/edm/chicago_house.md`, `knowledge_base/genres/edm/ghetto_house.md`, `knowledge_base/genres/edm/nu_disco.md` — genres that deliberately avoid surgical/notch-style carving as part of their aesthetic
- `knowledge_base/genres/edm/minimal_techno.md` — sparse arrangement exposing every frequency decision, demanding precision despite minimal element count
- `knowledge_base/mixing/eq/subtractive_eq.md` and `knowledge_base/mixing/eq/frequency_masking.md` — the broader cutting philosophies this technique's narrow-band special case sits within
