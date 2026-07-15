---
technique_name: "PLR and Crest Factor as Practical Dynamics Metrics"
category: dynamics
problem_solved: "Genre files describe dynamic range qualitatively ('wide dynamic range preserved,' 'heavily compressed and loud') without a shared numeric metric to check a specific master against, making it hard to verify by measurement whether a master actually landed in the dynamic-range territory its genre calls for"
parameters:
  plr_definition: "Peak-to-Loudness Ratio — the difference between a track's true peak level (dBTP) and its integrated loudness (LUFS); a modern, loudness-metering-based descendant of crest factor"
  psr_definition: "Peak-to-Short-term-loudness Ratio — the same concept as PLR but measured against short-term (rather than integrated) LUFS, useful for tracking how the ratio moves section-to-section within a single track"
  practitioner_wide_range: "Widely dynamic masters commonly run PLR/crest factor in roughly the 12-20dB range and above, per general mastering-practitioner guidance (verify current sources before treating as a hard rule)"
  practitioner_moderate_range: "A commonly cited 'sweet spot' for competitive-but-not-crushed modern masters sits around 8-12dB PLR/PSR"
  practitioner_narrow_range: "Loudness-war-style masters commonly run PLR/PSR below 8dB, with values regularly cited in the roughly 4-6dB range at the most aggressively limited end"
signal_chain_position: "Measurement taken on the finished master, using a loudness/true-peak meter that reports PLR or PSR directly (most modern loudness meters include this)"
genre_applicability:
  - post_rock
  - progressive_rock
  - doom_metal
  - drone_metal
  - dub_techno
  - minimal_techno
  - techno
  - pop
  - speedcore
  - gabber
  - riddim
  - big_room_house
related_techniques:
  - lufs_targets_by_genre
  - dynamic_range_as_expressive_device
  - brickwall_limiting_artifacts
tags: ["plr", "crest-factor", "psr", "dynamics-measurement", "loudness"]
---

# PLR and Crest Factor as Practical Dynamics Metrics

Genre files across this knowledge base describe dynamic range almost entirely in qualitative language — "wide dynamic range preserved," "moderate dynamics," "minimal — brickwall limiting... treated as part of the genre's raw aesthetic." This is useful for understanding a genre's intent, but it doesn't give a mastering engineer a number to check a specific master against. Peak-to-Loudness Ratio (PLR) and its close relative crest factor fill that gap: PLR is the difference between a track's true peak (dBTP) and its integrated loudness (LUFS), giving a single measurable number that tracks the qualitative "how squashed is this" language genre files use into something a meter can report directly. This entry translates the genre corpus's qualitative dynamics spectrum into the PLR/crest-factor ranges it would practically correspond to — with the caveat, addressed directly below, that the knowledge base's genre files essentially never state PLR or crest-factor numbers themselves, so the numeric mapping here is grounded in general mastering-practitioner guidance rather than knowledge-base citation.

## Where the Numbers Come From

Practitioner sources describe PLR (and its short-term cousin PSR) as a modern, loudness-metering-based descendant of the older RMS-based crest factor, calculated as the gap between true peak and integrated (or short-term) LUFS. General mastering guidance commonly treats roughly 8-12dB PLR/PSR as a practical sweet spot for competitive-but-not-crushed modern masters, treats values regularly below 8dB (and especially in the roughly 4-6dB range) as characteristic of loudness-war-style mastering that tends to sound crushed and induces listener fatigue, and treats widely dynamic masters (classical, ambient, and similar) as commonly running considerably higher, often in the 12-20dB range or beyond. These are practitioner rules of thumb rather than fixed physical constants, and should be treated as an approximate translation layer, not as precise targets — but they're specific and checkable in a way "wide dynamic range" alone is not.

## The Wide End: Where Genre Files' Qualitative Language Implies High PLR

Genres whose files use language like "maximum dynamic range preservation is essential" are describing exactly the territory the practitioner-guidance high-PLR range covers. `post_rock.md` and `progressive_rock.md` both use close to the strongest available language in the knowledge base, and per `dynamic_range_as_expressive_device.md`, that language exists specifically because "the genre's entire expressive power depends on the contrast between near-silent openings and overwhelming climaxes." `drone_metal.md` states "the genre's impact depends on the contrast between near-silence and overwhelming volume, and heavy limiting destroys this," and `dub_techno.md`'s dynamics field goes as far as any genre file in the corpus toward naming itself the extreme case within its own family: "dub techno masters are among the least compressed/loudest in the techno family, allowing the delay/reverb decay and spacious atmosphere to breathe fully." `minimal_techno.md` makes the connection to PLR-style measurement almost explicit without using the term: "High dynamic range relative to other techno subgenres is preserved and valued — the sparse arrangement depends on audible contrast between presence and silence, which loud, compressed mastering would destroy." All of these would be expected to measure well above the 8-12dB "sweet spot," likely into the practitioner-cited 12-20dB-plus range, though none of the source genre files state a number.

## The Moderate Middle: Where the "Sweet Spot" Range Likely Sits

`pop.md`'s "-9 to -7 LUFS integrated for streaming-competitive masters, while still preserving enough dynamic contrast between verse and chorus" and similar moderate-tier genre language documented in `lufs_targets_by_genre.md` describes exactly the territory the practitioner-cited 8-12dB PLR "sweet spot" is meant to capture — loud enough to be competitive, but not so aggressively limited that the number collapses toward the loudness-war range. `techno.md`'s framing ("Preserves enough dynamic range for club sound systems to deliver impact; techno masters are typically less brickwalled than mainstream pop/EDM masters") sits in a similar zone, likely toward the upper end of this middle band given its explicit comparison against more heavily limited EDM.

## The Narrow End: Where Genre Files Describe Loudness-War-Style Compression

`speedcore.md`'s "-6 to -4 LUFS integrated... with minimal residual dynamic range" and `gabber.md`'s "brickwall limiting and audible saturation are treated as part of the genre's raw aesthetic" both describe the practitioner-cited narrow end of the PLR range directly — a master with "minimal residual dynamic range" pushed to -4 to -6 LUFS integrated is very likely to measure in or below the roughly 4-6dB PLR range practitioner guidance associates with the most aggressive loudness-war mastering. `riddim.md` ("Very low dynamic range; the genre is mastered for maximum physical bass impact and loudness rather than dynamic nuance") and `big_room_house.md` ("Very dense and heavily limited... prioritizing maximum perceived impact... over preserved dynamic range") sit in the same narrow-PLR territory per `lufs_targets_by_genre.md`'s "loudest tier."

## A Documentation Outlier Worth Flagging: `doom_metal.md`'s Explicit Crest-Factor Number

`doom_metal.md` is the single genre file in this knowledge base's corpus that states a crest-factor number directly: "Preserve wide dynamic range (0.8–1.2 dB RMS crest factor) to retain the genre's crushing impact and atmospheric depth." Taken at face value, this number is inconsistent with the qualitative claim right next to it — a crest factor of 0.8-1.2dB is extremely narrow (well below even the loudness-war-style 4-6dB range described above), not "wide," and general practitioner guidance describes typical music crest factors as running in a roughly 10-20dB range or more. This reads as a likely documentation error in the source genre file (possibly a mismeasured or misapplied number) rather than a genuine outlier worth designing a master around, and it's flagged here specifically as a caution: don't treat every numeric claim in a genre file's frontmatter as independently verified, especially where it contradicts the same field's own qualitative language. Cross-check any specific numeric target against the surrounding prose and, where they conflict, treat the qualitative description ("wide dynamic range... crushing impact and atmospheric depth") as the more reliable signal of intent.

## Practical Use: Measuring, Not Just Reading

In practice, PLR/PSR gives a mastering engineer a way to check a finished master against its genre's intended tier without relying on ear alone — a post-rock or drone-metal master reading a PLR in the loudness-war range (regardless of what its integrated LUFS number says) is very likely over-limited relative to its genre's documented intent, and a speedcore or gabber master reading a PLR up in the wide-dynamic range has probably not achieved the "minimal residual dynamic range" character those genre files call for. This is a direct complement to `lufs_targets_by_genre.md`'s integrated-loudness targets — LUFS tells you how loud the master is on average, PLR tells you how much dynamic movement survived to get there, and a genre's documented character usually implies expectations for both numbers together, not just one.

## Common Mistakes

**Treating a genre file's stated LUFS target as sufficient information without also considering PLR.** Two masters can hit the same integrated LUFS while one preserves substantially more dynamic movement than the other — PLR is the number that distinguishes them, matching the point `dynamic_range_as_expressive_device.md` makes about judging masters by loudness number alone.

**Copying `doom_metal.md`'s stated "0.8–1.2 dB RMS crest factor" as a literal target.** As discussed above, this number appears internally inconsistent with the same field's "wide dynamic range" language and with general crest-factor practice — treat it as a likely documentation error, not a verified genre convention.

**Assuming PLR/crest-factor numbers cited here are precise, fixed industry standards.** They are practitioner rules of thumb reported via general mastering-community guidance, not values sourced from this knowledge base's genre files (which don't state PLR numbers) or from a single authoritative standard — treat the ranges in this entry as approximate orientation, not exact targets.

## Cross-References

- `knowledge_base/mastering/loudness/lufs_targets_by_genre.md` — the integrated-loudness side of the same genre spectrum this entry's PLR/crest-factor ranges are mapped onto
- `knowledge_base/mastering/dynamics/dynamic_range_as_expressive_device.md` — the qualitative dynamic-range-preservation principle this entry adds a measurable metric to
- `knowledge_base/mastering/dynamics/brickwall_limiting_artifacts.md` — the audible symptoms that tend to accompany a master pushed into the narrow-PLR range unintentionally
- `knowledge_base/genres/rock/post_rock.md`, `knowledge_base/genres/metal/drone_metal.md`, `knowledge_base/genres/edm/dub_techno.md`, `knowledge_base/genres/edm/minimal_techno.md` — wide-dynamic-range genre citations mapped to the high-PLR tier
- `knowledge_base/genres/edm/speedcore.md`, `knowledge_base/genres/edm/gabber.md`, `knowledge_base/genres/edm/riddim.md`, `knowledge_base/genres/edm/big_room_house.md` — narrow-dynamic-range genre citations mapped to the low-PLR tier
- `knowledge_base/genres/metal/doom_metal.md` — the source of the corpus's one explicit (and likely erroneous) numeric crest-factor citation
