---
technique_name: "Mastering EQ vs. Mix EQ — Where the Role Boundary Actually Is"
category: "eq"
problem_solved: "Using mastering EQ to attempt fixes that actually require going back into the individual mix stems (frequency conflicts between specific instruments, a specific track sitting wrong in the balance) — a whole-mix EQ move cannot separate two instruments that are already summed together, so problems needing that kind of separation get worse, not better, when 'fixed' at mastering"
parameters:
  mix_eq_scope: "Applied per-track or per-bus, before summing, where individual instruments can still be isolated — carves space between competing elements (e.g. guitar vs. bass vs. kick) and shapes individual timbre"
  mastering_eq_scope: "Applied to the finished, already-summed stereo mix — shapes the overall tonal balance and genre-conformant character of the whole, without the ability to isolate any single element within it"
  diagnostic_question: "If the fix requires turning down or reshaping one specific instrument without affecting the others, it belongs at the mix stage; if it requires shifting the overall balance of the entire summed signal, it belongs at mastering"
signal_chain_position: "Mix EQ sits pre-sum, on individual tracks/buses; mastering EQ sits post-sum, on the finished two-track mix, as the first broad-strokes stage before dynamics processing"
genre_applicability:
  - death_metal
  - djent
  - garage_rock
  - shoegaze
  - avant_garde_metal
  - vocal_trance
related_techniques:
  - subtractive_mastering_eq_philosophy
  - genre_tonal_balance_targets
  - matching_mastering_eq_to_reference
tags: ["eq", "mix-vs-master", "role-boundary", "frequency-carving", "signal-chain"]
---

# Mastering EQ vs. Mix EQ — Where the Role Boundary Actually Is

The genre corpus doesn't state this boundary as an abstract rule in any single entry, but it's visible by comparing what genre files describe happening at the mix stage against what the same or related genre files describe happening at mastering — the two stages are consistently doing structurally different jobs, and several entries make that difference unusually concrete.

## Mix EQ: Separating Instruments That Are Still Individually Accessible

`death_metal.md` gives the clearest illustration of mix-stage EQ's actual job: "The guitars, bass, and kick drum are all fighting for the exact same low-end frequencies because the guitars are tuned so low. The solution is aggressive EQ: the kick drum is given a sharp, unnatural 'click' in the high frequencies, the bass guitar is distorted to provide midrange 'clank,' and the guitars are high-passed to leave room for the actual sub-bass." This is only possible because each instrument is still an individually addressable track — a mastering engineer working on the finished mix has no access to "the guitars" separately from "the bass," only to the combined signal both already occupy. `djent.md` describes the identical structural need — "careful high-pass filtering prevents mud in complex polyrhythmic passages" — again applied per-instrument, pre-sum.

## Mastering EQ: Shaping the Whole, Not Separating the Parts

By contrast, mastering-stage frequency guidance in genre files is described in terms of the summed mix's overall character, not any single element within it. `avant_garde_metal.md` makes the boundary explicit in the negative: "Deliberately inconsistent across a track by design, since each quoted genre carries its own idiomatic frequency balance; mastering must avoid over-normalizing this variety into a single homogenized tone" — the mastering engineer's job here is understood as respecting a balance that was already set at the mix stage, not reshaping it element-by-element. This is a direct statement that mastering EQ operates on a different, coarser level than mix EQ: it can nudge the whole track's tonal character, but it cannot and should not attempt to re-litigate mix-stage decisions about how individual quoted-genre sections were balanced against each other.

## The Edge Case: When Mastering Still Has to Protect One Element

`vocal_trance.md` documents a case that looks like it crosses the boundary but doesn't: "mastering engineers often ride or automate slightly to protect vocal presence across sections." This is dynamic automation of the whole-mix signal in response to what the vocal is doing, not an EQ move isolating the vocal from the rest of the mix — the mastering engineer still can't touch the vocal independently of the instrumental, they can only ride the overall balance to compensate as sections change. It illustrates that mastering-stage techniques can respond to element-level problems without actually gaining element-level access.

## Common Mistakes

**Trying to fix a specific-instrument problem with a whole-mix mastering EQ move.** `death_metal.md` and `djent.md`'s low-end frequency conflicts (guitar vs. bass vs. kick) can only be resolved by returning to the individual tracks; a broad low-end cut at mastering to "clean up the mud" removes bass and kick weight along with the guitar buildup, since a summed mix can't distinguish between them.

**Over-normalizing a deliberately uneven mix at the mastering stage.** As `avant_garde_metal.md` warns, some genres build in intentional per-section tonal variety as a compositional device; mastering EQ that "corrects" this into a single homogenized tone is undoing a mix-stage decision it isn't positioned to safely override.

**Assuming mastering has no tools for element-specific problems at all.** `vocal_trance.md` shows mastering can still respond to a specific element's needs (vocal presence) through whole-mix automation/riding, even without direct access to that element — it's a narrower tool than mix-stage EQ, not a useless one.

## Cross-References

- `knowledge_base/mastering/eq/subtractive_mastering_eq_philosophy.md` — why the mastering-stage moves that remain available tend to be broad and conservative rather than surgical
- `knowledge_base/mastering/eq/genre_tonal_balance_targets.md` — the genre-level targets mastering EQ is responsible for, as distinct from element-level mix EQ goals
- `knowledge_base/genres/metal/death_metal.md`, `knowledge_base/genres/metal/djent.md` — direct sources for mix-stage, per-instrument frequency carving that mastering cannot replicate
- `knowledge_base/genres/metal/avant_garde_metal.md` — direct source for mastering's obligation not to over-normalize mix-stage tonal variety
- `knowledge_base/genres/edm/vocal_trance.md` — direct source for the edge case of whole-mix automation protecting one element without isolating it
