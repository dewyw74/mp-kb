---
technique_name: "Correcting Narrow or Overly Wide Mixes at Mastering — What Mastering Can and Can't Fix"
category: "stereo"
problem_solved: "A mix arrives at mastering narrower or wider than the genre convention calls for, and the mastering engineer either over-promises what a whole-mix widening/narrowing tool can achieve, or fails to recognize which width problems are genuinely correctable at mastering versus which ones require going back to the mix"
parameters:
  narrowing_is_generally_safe: "Reducing an overly wide or phase-risky stereo image at mastering (narrowing the side channel, summing partial width toward center) is a comparatively low-risk, genuinely correctable move because it reduces phase-cancellation risk rather than introducing it"
  widening_a_narrow_mix_is_limited: "Adding real width to a mix that was recorded/mixed narrow or mono has a hard ceiling at mastering — mastering-stage widening tools can create a plausible impression of width but cannot recover genuine per-element stereo information the mix never captured"
  genre_convention_sets_the_bar: "Whether a given mix's width even counts as a 'problem' depends entirely on the target genre's documented convention — a narrow image is correct, not broken, for genres whose convention is narrow"
signal_chain_position: "Corrective stereo processing on the master bus, applied only after confirming (via the genre's documented convention) that the mix's actual width is a genuine mismatch rather than the correct target"
genre_applicability:
  - honky_tonk
  - bakersfield_sound
  - hillbilly_boogie
  - coldwave
  - glitch
  - jungle
related_techniques:
  - stereo_widening_at_mastering
  - final_mono_and_translation_check
  - genre_tonal_balance_targets
tags: ["stereo", "width-correction", "narrowing", "widening", "mastering", "phase"]
---

# Correcting Narrow or Overly Wide Mixes at Mastering

The most important thing this corpus's genre entries establish about "correcting" stereo width is that a narrow or wide image is frequently not a problem at all — it's the documented genre convention, and correcting it would be a mistake. Where genre files do describe genuine width correction, it's consistently in one direction: narrow mixes being widened modestly for a more modern release, never a mono or narrow mix being asked to become genuinely, fully wide.

## Widening a Narrow Mix Has a Real Ceiling — and Genre Files Say So

`honky_tonk.md` documents exactly this scenario and is explicit about the limited scope of the fix: "Narrow and centered, reflecting mono-era recording practice if working in a period-accurate style; modern productions can widen steel guitar and fiddle modestly for separation." The word "modestly" is doing real work here — this is a genre file acknowledging that some width can be added to a narrow mix for a more contemporary-sounding release, without claiming the result becomes a genuinely wide modern stereo image. `bakersfield_sound.md` documents the identical pattern: "Comparatively narrow and centered by modern standards, reflecting the era's mono/early-stereo studio practice; lead guitar and steel panned modestly for separation in modern productions." Both entries describe this widening as a mix-stage decision (panning elements for separation) rather than a mastering-stage fix — which is itself informative: genuine width correction on a narrow mix is described in these files as something that has to happen before mastering, not something a mastering-stage widening tool can retroactively achieve.

## When "Narrow" Isn't a Problem to Fix at All

`hillbilly_boogie.md` states the limit case plainly: "Mono in essentially all classic recordings, with instruments balanced for a tight, driving ensemble sound rather than spread wide." A period-accurate hillbilly boogie master isn't a stereo mix with a width problem — it's correctly mono, and applying any width-correction tool to "fix" it would misrepresent the genre entirely. `coldwave.md` documents a modern (not historical-technology-limited) genre that still targets a narrow image as an aesthetic choice: "fairly narrow and mono-centric by 1980s production standards" — again, not a defect, but the documented target.

## When Width Genuinely Needs to Be Reduced

The corrective direction genre files most directly support is narrowing, specifically around phase-cancellation risk in the low end. `jungle.md`'s instruction to "keep sub-bass mono and separate from mid-bass/Reese content so both translate on club soundsystems without phase cancellation" describes exactly the kind of problem mastering-stage narrowing (or a mono-summing filter on the low end specifically) is well suited to fixing — reducing an overly wide, phase-risky low end is a safe, genuinely correctable move because it removes cancellation risk rather than trying to manufacture stereo information that isn't there. `glitch.md`'s "extremely wide, often mono-incompatible" stereo image, discussed at length in `stereo_widening_at_mastering.md`, is the corpus's clearest example of a mix that's wide by design — here, narrowing at mastering would be actively wrong, since the mono incompatibility is understood as part of the genre's aesthetic rather than a defect, with only the sub-bass carved out as needing to stay mono.

## Common Mistakes

**Trying to make a narrow or mono mix "genuinely wide" at mastering.** `honky_tonk.md` and `bakersfield_sound.md`'s own "modestly" wording shows genre-literate engineers already know this has a ceiling — pushing a mastering-stage widener hard on a mix like `hillbilly_boogie.md`'s period-mono recordings won't recover real stereo information, it will just add artificial-sounding artifacts.

**Treating a genre's documented narrow convention as an unfixed problem rather than the target.** `coldwave.md` and `hillbilly_boogie.md` both show narrow/mono imaging as the correct, intentional choice — narrowing or widening either one to match a generic "modern wide" standard actively works against genre identity.

**Widening broadband instead of narrowing specifically the problematic content.** `jungle.md`'s low-end phase-cancellation risk is best solved by controlling width specifically in the low end (see `low_end_and_sub_bass_control_at_mastering.md`), not by a whole-mix narrowing move that also dulls whatever wide high-frequency content the mix correctly has.

## Cross-References

- `knowledge_base/mastering/stereo/stereo_widening_at_mastering.md` — the related technique of widening at mastering, including why it has a narrower toolkit and higher translation risk than mix-stage widening
- `knowledge_base/mastering/stereo/final_mono_and_translation_check.md` — the verification step that confirms whether a width correction actually resolved a phase problem
- `knowledge_base/mastering/eq/low_end_and_sub_bass_control_at_mastering.md` — the frequency-specific companion to the low-end narrowing case described here
- `knowledge_base/genres/country/honky_tonk.md`, `knowledge_base/genres/country/bakersfield_sound.md` — direct sources for the "modestly widen a narrow mix" correction pattern
- `knowledge_base/genres/country/hillbilly_boogie.md`, `knowledge_base/genres/electronic/coldwave.md` — direct sources for narrow/mono as correct genre convention rather than a problem
- `knowledge_base/genres/edm/jungle.md`, `knowledge_base/genres/electronic/glitch.md` — direct sources for legitimate low-end narrowing versus intentional wide/mono-incompatible design
