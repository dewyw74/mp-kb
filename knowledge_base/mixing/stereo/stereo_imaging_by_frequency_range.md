---
technique_name: "Stereo Imaging by Frequency Range"
category: stereo
problem_solved: "Widening a mix's low end causes phase cancellation and inconsistent bass translation on mono/club systems, while leaving high-frequency texture and atmosphere narrow wastes an opportunity for scale and immersion that carries no equivalent mono-compatibility risk"
parameters:
  mono_threshold: "Content below roughly 100-150Hz (sub-bass, kick fundamental) is the range most consistently kept mono/centered across genre entries, regardless of how wide the rest of the mix gets"
  wide_candidates: "Pads, atmospheric textures, hi-hats/percussion, supersaw/detuned lead stacks, and reverb/delay tails are the elements most consistently widened, since their frequency content and lack of strong fundamental-pitch information carry minimal phase-cancellation risk in mono"
  genre_variance: "The width applied to the 'non-bass' portion of the spectrum varies enormously by genre — from trance's 'very wide' supersaw leads to tech house's comparatively restrained percussion spread — but the mono-bass rule itself barely varies at all"
signal_chain_position: "Set per-element at the panning/width stage, informed by each element's frequency content rather than by a single mix-wide width setting; verified again at the mix-bus stage (see mid-side processing) once all elements are combined"
genre_applicability:
  - trance
  - drum_and_bass
  - jungle
  - dubstep
  - brostep
  - dub_techno
  - melodic_techno
  - house
  - tech_house
  - halftime
  - contemporary_r_and_b
  - glitch
related_techniques:
  - panning_laws
  - mid_side_processing_and_mono_compatibility
  - stereo_widening_techniques
tags: ["stereo-imaging", "frequency-dependent-width", "mono-bass", "sub-bass", "club-translation"]
---

# Stereo Imaging by Frequency Range

One rule shows up with almost total consistency across this knowledge base's electronic genre entries, cutting across otherwise very different aesthetics: bass and sub content stays mono and centered, while everything above it is where a genre's actual stereo-width identity gets expressed. This isn't a stylistic preference so much as a translation necessity — sub-bass content that's been stereo-widened risks partial or full phase cancellation the moment a system sums to mono, which happens routinely on club soundsystems, phone speakers, and Bluetooth playback.

## The Mono-Bass Floor: Near-Universal Across Electronic Genres

`drum_and_bass.md` states the rule at its most absolute: "Sub-bass kept mono and centered across virtually all subgenres for soundsystem translation." `jungle.md` gives the mechanism explicitly: "Keep sub-bass mono and separate from mid-bass/Reese content so both translate on club soundsystems without phase cancellation." The same specification recurs almost verbatim across dance-music subgenres with otherwise very different sounds: `dubstep.md` ("Sub-bass mono and centered for soundsystem translation"), `brostep.md` ("Sub-bass kept mono/centered"), `riddim.md` ("Bass kept mostly mono/centered for maximum club impact"), `bass_house.md` ("Bass and kick centered/mono for maximum club impact"), `gabber.md` ("the low end always stays mono for club-system translation"), `jump_up.md` ("Bass and kick kept mono/centered for maximum club translation and weight"), `hard_techno.md` ("Kick and bass centered/mono for maximum club-system translation and physical impact"), and `halftime.md` ("Sub-bass mono and centered as in all drum and bass"). `liquid_dnb.md`'s common-mistakes-adjacent production notes make the tradeoff explicit: "Sub-bass kept mono and clean; broader mix retains more stereo warmth/space than harder DnB subgenres" — even in a subgenre that wants more overall width than its harder relatives, the sub-bass floor doesn't move.

Outside pure dance music, the same principle recurs: `contemporary_r_and_b.md`'s stereo-imaging notes read "Lead vocal dead center; backing vocals panned extremely wide. Bass mono. Keys and pads spread wide" — the identical mono-low/wide-everything-else split, just applied to an R&B arrangement rather than a club system.

## Where the Width Actually Lives: Above the Bass

Once the sub/bass floor is accounted for, genres diverge widely in how much width they apply above it — and that divergence is where each genre's actual stereo identity gets expressed. `trance.md` sits at the wide extreme: "Very wide — supersaw leads and pads spread hard left-right via detune and stereo widening, while kick and bass stay centered and mono below ~150Hz for club translation" — note the explicit frequency threshold. `melodic_techno.md` and `dub_techno.md` apply similar wide treatment to pads/arpeggios and delay-tail chord stabs respectively, while keeping "kick and bass kept centered/mono for club translation and low-end focus." `glitch.md` pushes furthest into "Extremely wide, often mono-incompatible — hard-panned glitch bursts and chaotic stereo movement are part of the aesthetic," while still carving out an exception: "sub bass kept mono for translation." At the more restrained end, `french_house.md` specifies "Moderate width — drums and bass centered and mono-compatible, sample loops can be widened slightly," and `tech_house.md` keeps width to "Percussion layers spread across the stereo field for groove complexity and interest; kick and bass stay centered/mono for club translation."

## The Kick/Sub Split: Two Different Centered Elements

Several entries distinguish between the kick's transient/fundamental content and true sub-bass, treating both as mono but for related reasons. `breakbeat.md`'s frequency-balance notes specify "clear separation between sub-bass and break's kick fundamental to avoid masking" — a reminder that keeping both centered doesn't just avoid phase cancellation, it also keeps two competing low-frequency sources from masking each other, a concern covered further in `panning_strategy_for_dense_arrangements.md`.

## Common Mistakes

**Widening a bass or sub synth patch directly.** This is the single most consistently flagged risk across the genre corpus — any stereo-widener or chorus effect applied to a bass patch's fundamental risks mono-incompatibility, regardless of how good it sounds in stereo headphone monitoring.

**Treating "wide mix" as a single, uniform setting rather than a frequency-dependent decision.** `trance.md`'s explicit "~150Hz" threshold and `breakbeat.md`'s sub/kick separation both show that the correct question isn't "how wide should this mix be" but "which frequency ranges should be wide, and which must stay centered."

**Assuming genres that want extreme overall width (like `glitch.md`) abandon the mono-bass rule entirely.** Even `glitch.md`, which explicitly courts "mono-incompatible" hard-panned chaos elsewhere in the spectrum, still keeps "sub bass kept mono for translation" — the mono-bass floor is close to a hard constraint, not a stylistic default that adventurous genres discard.

## Cross-References

- `knowledge_base/genres/edm/drum_and_bass.md`, `knowledge_base/genres/edm/jungle.md`, `knowledge_base/genres/edm/dubstep.md` — the mono sub-bass rule stated most explicitly, with the phase-cancellation mechanism named directly
- `knowledge_base/genres/edm/trance.md` — the widest documented "above the bass" treatment, with an explicit ~150Hz mono/wide crossover threshold
- `knowledge_base/genres/edm/tech_house.md` and `knowledge_base/genres/edm/french_house.md` — comparatively restrained width applied above a still-mono bass/kick foundation
- `knowledge_base/genres/electronic/breakbeat.md` — the kick-fundamental/sub-bass separation as a masking (not just phase) concern
- `knowledge_base/genres/r_and_b/contemporary_r_and_b.md` — the identical mono-bass/wide-texture split applied outside club/electronic contexts
- `knowledge_base/mixing/stereo/mid_side_processing_and_mono_compatibility.md` — the mid-side EQ technique used to enforce this split at the mix-bus stage
- `knowledge_base/mixing/stereo/panning_laws.md` — the pan-law behavior underlying how "centered" elements are actually placed
