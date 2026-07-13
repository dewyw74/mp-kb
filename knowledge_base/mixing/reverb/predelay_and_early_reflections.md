---
technique_name: "Predelay and Early Reflections for Clarity-Preserving Reverb"
category: "reverb"
problem_solved: "A reverb's wash blurring a source's transient or vocal consonant clarity, even when the overall reverb size/decay time is already genre-appropriate"
parameters:
  predelay_range: "0ms (reverb onset immediately with the source) for maximum blend/glue, 20-50ms for a clearly audible gap that preserves transient definition before the reverb tail is heard, 50ms+ for a deliberately separated slap-then-wash effect"
  early_reflections: "The first, discrete echo-like reflections before the reverb's dense diffuse tail builds up; shorter/tighter early-reflection patterns read as a smaller, closer space, wider/longer patterns read as a larger room"
  vocal_specific_use: "Predelay in the 30-50ms range is a common default for lead vocal reverb sends specifically, so consonants and the start of each word stay intelligible before the reverb tail arrives"
signal_chain_position: "A parameter within the reverb send itself, adjusted alongside (not instead of) the size/decay-time choices documented in `knowledge_base/mixing/reverb/reverb_types_and_selection.md`"
genre_applicability:
  - pop
  - hip_hop
  - k_pop
  - romantic
  - opera
  - film_score
related_techniques:
  - reverb_types_and_selection
  - subtractive_eq
tags: ["predelay", "early-reflections", "reverb", "vocal-clarity", "mixing"]
---

# Predelay and Early Reflections for Clarity-Preserving Reverb

`knowledge_base/mixing/reverb/reverb_types_and_selection.md` documents reverb selection primarily along the axis of overall size and decay time matched to a genre's scale. Predelay — the gap between a dry source hitting and the reverb's tail becoming audible — is a separate, complementary parameter that solves a different problem: preserving a source's transient or consonant clarity even when a genre-appropriate reverb is already large or long enough that it would otherwise blur that detail.

## Why Predelay Exists as a Separate Control From Size/Decay

A reverb with zero predelay begins building its tail the instant the dry source hits, which means the reverb's diffuse energy starts overlapping the source's most information-dense moment — a vocal's consonant, a drum's transient — immediately. Adding even a small amount of predelay (commonly 20-50ms) creates a brief window where the dry source is heard clearly on its own before the reverb tail arrives, letting a mix use a large, long-decay reverb (matched correctly to the genre's scale per `knowledge_base/mixing/reverb/reverb_types_and_selection.md`) without that size working against intelligibility. This is why predelay and decay time are independently adjustable parameters rather than a single "reverb amount" control — they solve different problems (clarity preservation vs. spatial scale) that would otherwise trade off against each other.

## Vocal Reverb as the Clearest Use Case

Lead vocal reverb sends are the most consistent place this technique gets applied deliberately: a vocal's intelligibility depends heavily on consonant clarity at the start of each syllable, so a vocal reverb send commonly uses predelay in the 30-50ms range specifically to let each word's onset cut through clearly before the reverb's sustained tail fills in around it. This lets genres wanting a lush, spacious vocal reverb (per the hall/cathedral-scale end of `knowledge_base/mixing/reverb/reverb_types_and_selection.md`'s genre-matching guidance) still keep the vocal legible, rather than forcing a choice between spaciousness and clarity.

## Early Reflections as a Distinct Spatial Cue

Before a reverb's dense diffuse tail builds up, most reverb algorithms and real spaces produce a handful of discrete early reflections — individual, closely-spaced echoes from the nearest room boundaries. The pattern of these early reflections (how many, how closely spaced, how loud relative to the later diffuse tail) is a major contributor to a listener's sense of a space's actual size and character, somewhat independently of the reverb's total decay time — a reverb with short, tight early reflections and a long tail can still read as a relatively small or close space with a long, atmospheric decay, while dense, widely-spaced early reflections read as a larger room regardless of decay time.

## Common Mistakes

**Only adjusting reverb size/decay time and never touching predelay when a mix feels "washy" or unclear.** The genre-scale reverb selection in `knowledge_base/mixing/reverb/reverb_types_and_selection.md` may already be correct for the genre — the actual fix for a clarity problem at an otherwise-appropriate reverb size is often predelay, not a smaller/shorter reverb that would undermine the intended genre scale.

**Using zero predelay by default on every reverb send.** While appropriate for some blend-focused uses, zero predelay is the setting most likely to blur transient/consonant detail — it should be a deliberate choice for a specific blended effect, not an unconsidered default.

## Cross-References

- `knowledge_base/mixing/reverb/reverb_types_and_selection.md` — the primary genre-scale reverb selection technique this entry's predelay/early-reflection guidance complements
- `knowledge_base/mixing/eq/subtractive_eq.md` — a related clarity-preservation tool, often used alongside predelay (high-passing a reverb return) to further protect low-mid clarity
- `knowledge_base/genres/pop/k_pop.md`, `knowledge_base/genres/classical/romantic.md`, `knowledge_base/genres/classical/opera.md` — genres combining large-scale reverb with vocal/melodic clarity requirements where predelay is especially load-bearing
