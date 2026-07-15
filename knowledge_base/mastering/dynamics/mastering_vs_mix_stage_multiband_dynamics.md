---
technique_name: "Mastering-Stage vs. Mix-Stage Multiband Dynamics: Where the Line Sits"
category: dynamics
problem_solved: "Not distinguishing mix-stage multiband compression (fixing a frequency-specific dynamics problem within one instrument or bus, using tightly-targeted crossovers) from mastering-stage multiband compression (broad, gentle, whole-mix glue and loudness work, using wide genre-agnostic crossovers), leading to either the wrong tool being reached for at the wrong stage or mastering-stage multiband being asked to fix a problem that should have been solved during mixing"
parameters:
  mix_stage_scope: "Applied to a single instrument, sound, or sub-bus (guitar low-mids, bass sub-vs-growl split, drum bus) to solve a specific, identifiable frequency-dynamics problem within that element"
  mastering_stage_scope: "Applied to the full mix bus, generally with gentler settings and wider crossover bands, to address broad tonal-dynamics interaction across the whole finished mix rather than one instrument's problem"
  crossover_specificity: "Mix-stage multiband crossovers are typically set precisely around the problem instrument's own frequency content (e.g. a guitar's palm-mute fundamental); mastering-stage crossovers use broader, more genre-agnostic bands per `multiband_compression_and_limiter_chain_ordering.md`'s ~100-150Hz/2-5kHz starting points"
signal_chain_position: "Mix stage: on an individual channel or sub-bus, before the mix is summed to a stereo file. Mastering stage: on the master bus, after broad tonal EQ and before the final limiter"
genre_applicability:
  - thrash_metal
  - heavy_metal
  - djent
  - doom_metal
  - ambient
  - trailer_music
  - bass_house
  - electro_house
related_techniques:
  - multiband_compression_and_limiter_chain_ordering
  - dynamic_range_as_expressive_device
  - clipping_vs_limiting
tags: ["multiband-compression", "mix-vs-master", "signal-chain", "frequency-specific-dynamics"]
---

# Mastering-Stage vs. Mix-Stage Multiband Dynamics: Where the Line Sits

`knowledge_base/mastering/dynamics/multiband_compression_and_limiter_chain_ordering.md` documents mastering-stage multiband compression's role and chain position in detail and should be read first — this entry takes a different angle, using the genre corpus to establish where the line actually sits between multiband processing that belongs at the mixing stage (fixing one instrument's frequency-dynamics problem) and multiband processing that belongs at the mastering stage (broad, gentle, whole-mix work). Searching the genre files for "multiband" across both their mixing and mastering sections surfaces a clear and consistent pattern: the large majority of citations describe mix-stage, single-element use, and mastering-stage citations are comparatively rare and describe a meaningfully different kind of processing.

## Mix-Stage Multiband: Solving One Instrument's Frequency-Dynamics Problem

The most common documented use case, by a wide margin, is multiband compression applied to a specific instrument or sub-bus to solve a narrow, identifiable problem within that element. `thrash_metal.md`'s mastering prose actually describes the technique being deployed at what reads as closer to a mix/bus-processing role despite appearing in that file's mastering discussion: "Multi-band compression is essential to control the low-mid 'boom' that occurs when the guitarist aggressively palm-mutes a power chord" — the target is a specific articulation (palm-muted chords) producing a specific frequency-range problem (low-mid boom), not the whole mix's overall dynamics. `heavy_metal.md`'s modern-production-techniques guidance names the identical use case even more narrowly: "Applying heavy multiband compression to the palm-muted 'chugs' of the guitar to keep the low-mids from booming out of control." `djent.md` extends this to the genre's extended-range instruments specifically: "Applying dedicated low-end management plugins (multiband compression, dynamic EQ) to keep extended-range guitar/bass tight and defined," with its mixing prose adding that this is used "to prevent mud in complex polyrhythmic passages" — again, a specific instrument-level problem (extended-range low end getting muddy under complex rhythm) rather than a whole-mix loudness or glue function. `doom_metal.md`'s sound-design processing field lists "Multiband compression on drums" as a distinct entry from its separate mastering-stage dynamics guidance, placing it at the drum-bus level rather than the master-bus level. Outside metal, the pattern holds in bass-forward EDM: `bass_house.md` documents "Multiband processing on bass to control sub weight separately from mid/high growl content," and `electro_house.md`'s mixing compression field notes "multiband compression common for taming distorted lead/bass energy" specifically on "the drop bus" for that element's own distorted energy, not the whole mix.

## Mastering-Stage Multiband: Broader, Gentler, Whole-Mix Work

Genuine mastering-stage (full-mix-bus) multiband citations are noticeably rarer in the genre corpus, and where they appear, the character of the processing described is different in kind, not just in degree. `ambient.md`'s mastering frequency-balance field is the clearest full-mix-bus citation in the corpus: "avoid excessive de-essing artifacts on field recordings by using gentle multiband processing" — explicitly gentle, explicitly full-mix (field recordings summed into the finished ambient piece), and explicitly corrective of a broad, whole-signal artifact rather than one instrument's problem. This matches `multiband_compression_and_limiter_chain_ordering.md`'s framing of mastering-stage multiband as addressing "frequency-specific dynamic problems... that survive from the mix" once "there's no going back to adjust an individual channel's compression."

## An Ambiguous Middle Case Worth Naming Honestly

Two genre files use language that sits genuinely on the boundary and are worth citing precisely rather than forced into one category. `trailer_music.md`'s compression field (filed under that genre's `mixing:` block, not its `mastering:` block) states: "Multiband compression is used to control the massive low end, while heavy limiting on the master bus ensures the track competes with modern EDM and Rock" — the multiband compression and the limiting are described together, with the limiting explicitly placed "on the master bus" while the multiband compression's exact bus placement is left less explicit despite sitting in the same sentence. `country_pop.md`'s sound-design processing field similarly names "Aggressive multi-band compression on the master bus" without being filed under that genre's `mastering:` block at all. Read together, these two citations suggest that genre files don't always cleanly separate mix-stage and master-stage multiband use the way the schema's `mixing:`/`mastering:` block division implies — some genre authors describe master-bus multiband processing within a "mixing" or "sound design" field, which is a documentation looseness worth being aware of rather than over-interpreting as a technical claim about where the processing "really" belongs.

## The Practical Distinction to Apply

Reading the corpus as a whole, the operative distinction isn't really "which stage of the session is this happening in" so much as "what problem is this solving." Mix-stage multiband compression, per the thrash_metal/heavy_metal/djent/doom_metal/bass_house/electro_house citations above, is reached for when one specific instrument or sub-bus has a frequency-dependent dynamics problem that a full-range compressor on that same element would over-correct (turning down the guitar's high end along with its boomy low-mids, for instance). Mastering-stage multiband compression, per `ambient.md` and `multiband_compression_and_limiter_chain_ordering.md`, is reached for once everything is already summed into one stereo file and a broad, gentle, whole-signal frequency-dynamics issue needs correcting without the option of going back to isolate the original problem instrument. The `trailer_music.md`/`country_pop.md` ambiguous cases are a useful reminder that in practice, "aggressive... on the master bus" processing does exist and gets documented — it just tends to appear in genres already committed to a dense, maximal, chart/trailer-competitive aesthetic where more corrective transparency isn't the goal in the first place.

## Common Mistakes

**Reaching for mastering-stage multiband compression to fix a single instrument's frequency-dynamics problem that should have been solved at the mix.** Per `multiband_compression_and_limiter_chain_ordering.md`'s own common-mistakes guidance, this is "more effective (and less likely to introduce audible artifacts) to fix a severely unbalanced element during mixing than to rely entirely on mastering-stage multiband compression to compensate" — the thrash_metal/djent/doom_metal citations above show exactly the kind of narrow, instrument-specific problem this principle is meant to be solved at.

**Assuming every genre-file "multiband" citation describes the same kind of processing.** As shown above, "multiband compression on the palm-muted guitar chugs" and "gentle multiband processing" on a full ambient mix bus are different tools solving different problems at different stages, even though both are described with the same word.

**Over-reading the `trailer_music.md`/`country_pop.md` ambiguous citations as proof that mastering-stage multiband is common or standard across genres.** These are two files where documentation structure (which schema field the technique was described under) doesn't map cleanly onto stage — genuinely broad, transparent, whole-mix-bus multiband citations (like `ambient.md`'s) are comparatively rare in this corpus relative to the many narrow, instrument-specific mix-stage citations.

## Cross-References

- `knowledge_base/mastering/dynamics/multiband_compression_and_limiter_chain_ordering.md` — the primary reference on mastering-stage multiband compression's role, crossover conventions, and chain position
- `knowledge_base/genres/metal/thrash_metal.md`, `knowledge_base/genres/metal/heavy_metal.md`, `knowledge_base/genres/metal/djent.md` — mix-stage multiband compression solving a specific guitar/bass low-mid problem
- `knowledge_base/genres/metal/doom_metal.md` — mix-stage multiband compression applied to the drum bus specifically
- `knowledge_base/genres/edm/bass_house.md` and `knowledge_base/genres/edm/electro_house.md` — mix-stage multiband compression solving bass/lead-bus frequency-dynamics problems
- `knowledge_base/genres/electronic/ambient.md` — the clearest genuinely full-mix-bus, mastering-stage multiband citation in the corpus
- `knowledge_base/genres/cinematic/trailer_music.md` and `knowledge_base/genres/country/country_pop.md` — ambiguous cases naming master-bus multiband processing outside a `mastering:` frontmatter block, cited here as an honest documentation-boundary caveat rather than a clean example
