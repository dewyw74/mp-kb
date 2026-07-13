---
technique_name: Diagnosing and Fixing Frequency Masking
category: eq
problem_solved: "Two or more elements occupying the same frequency range simultaneously, causing mud, lost definition, or an inaudible element, most commonly in the low end between kick and bass"
parameters:
  low_end_split: "kick fundamental typically 60-100Hz, sub-bass isolated below ~100Hz, bass fundamental 80-200Hz — kept in separate, non-overlapping pockets"
  presence_boost: "2-5kHz is the most frequently cited range for cutting a masked lead vocal or lead synth through a dense arrangement"
  highpass_strategy: "Highpass non-bass-and-kick elements aggressively to remove their unnecessary low-frequency content before it competes for the same pocket"
signal_chain_position: "EQ applied per-element before bus processing, ideally informed by soloing conflicting pairs together to identify the actual overlap rather than EQing in isolation"
genre_applicability:
  - jungle
  - house
  - trance
  - metal
  - metalcore
  - afro_house
  - glitch_hop
  - future_funk
  - classic_rock
  - blues_rock
  - k_pop
related_techniques:
  - subtractive_eq
  - sidechain_pumping
tags: ["masking", "frequency-pocket", "carving", "low-end", "mud"]
---

# Diagnosing and Fixing Frequency Masking

Frequency masking — two elements competing for the same range of the spectrum so that one or both lose definition — is the single most commonly cited mixing problem across this knowledge base's genre entries, appearing under wildly different names ("carving," "frequency pockets," "masking," "mud") but describing the identical phenomenon in every case. The fix is always structural rather than a single plugin technique: identify which elements are actually competing, then either cut one out of the shared range, move one to a different register, or use dynamic processing (sidechain compression) to separate them in time instead of frequency.

## The Low End: Where Masking Is Most Damaging

The kick-versus-bass relationship is the most frequently documented masking conflict in the knowledge base, because both elements typically want the same 60-200Hz range and both are structurally essential. `jungle.md` is explicit about the fix: "Sub-bass carved to sit below roughly 100 Hz in isolation from any mid-bass content," with its common-mistakes section naming the failure mode directly: "Letting mid-bass and sub-bass overlap and mask each other instead of carving distinct frequency pockets." `house.md` describes the desired end state as "a single dominant kick/bass frequency pocket," implying deliberate exclusivity rather than two elements sharing space. `edm_trap.md`'s hip-hop-descended relatives (`trap.md`, `hip_hop.md`) solve the same problem with a different tool — sidechain compression rather than static EQ — because the 808's pitch is melodically active and can't be permanently carved into a single fixed EQ pocket the way a static bassline can; see `sidechain_pumping.md` for that mechanism. `jump_up.md` shows a third solution to the same underlying conflict: "kick often pulled slightly higher in pitch/tuned to cut through" — separating kick and bass by pitch rather than by EQ notch or sidechain timing.

## Beyond Bass: Guitars, Vocals, and Dense Arrangements

Masking isn't only a low-end problem. `metal.md` and `metalcore.md` both describe guitar distortion as a masking risk to the kick/bass low end from above: "Guitars carved to avoid masking the kick/bass low end; vocal presence boosted to cut through dense, distorted guitar layers." `blues_rock.md` documents a masking conflict entirely in the midrange, between vocal and lead guitar, both of which want the same cutting 800Hz-2.5kHz range: "vocal and lead guitar competing for similar frequency space are arranged (not always simultaneous) to avoid masking" — note that this is an arrangement-level fix (don't play both at once) rather than a pure EQ fix, which is often the more effective solution when two elements are harmonically similar enough that EQ alone can't fully separate them. `k_pop.md` describes the same challenge at a larger scale, across an entire song's competing internal sections: "every section's competing production ideas (rap verse, sung pre-chorus, EDM chorus) are carved to remain clear despite high arrangement density."

## Sample-Based and Layered-Bass Genres

Genres that layer multiple bass sources — a sample plus a synth sub, for instance — face a compounded version of the same problem. `future_funk.md`'s common mistakes section calls this out directly: "Stacking multiple bass sources (sampled + synth) without EQ carving, producing a muddy, undefined low end," with its mixing section describing the actual fix: "EQ carving to fit multiple chopped sources together." `glitch_hop.md` documents an equivalent conflict between sub bass and rhythmic percussion detail: "Carve space for sub bass (below 100Hz) separately from glitch percussion detail (2-8kHz), since both compete for attention," and its own common-mistakes entry — "Overcrowding the low-mid with both chopped samples and wobble bass, causing masking" — makes clear this is a recurring failure mode specific to bass-heavy, sample-dense electronic production.

## The General Method

Across every genre file, the actual diagnostic method is consistent even when the specific frequencies differ: solo the two suspected conflicting elements together (not each in isolation) to hear where they actually overlap, then choose the appropriate fix for that specific conflict — a static EQ cut/highpass when one element has content it doesn't need in the contested range (the usual fix for guitar-vs-kick/bass, or secondary bass sources vs. a primary sub), a sidechain/dynamic solution when the conflicting element is melodically or rhythmically active and can't be permanently notched (the usual fix for 808-vs-kick), or an arrangement change when the two elements are harmonically similar enough that no amount of EQ fully separates them (the `blues_rock.md` vocal/guitar case).

## Common Mistakes

**EQing each element in isolation rather than while soloed together.** A cut that sounds necessary when auditioning one track alone often isn't where the actual conflict lives — the only reliable way to find a masking conflict is to solo the two competing elements together and sweep to find the overlap.

**Reaching for EQ when the real problem is rhythmic/dynamic, not static.** The 808-vs-kick conflict genres solve with sidechain compression (see `sidechain_pumping.md`) can't be fixed with a static EQ notch, because the 808's melodic content moves — a fixed cut would either do nothing at some pitches or gut the bass at others.

**Ignoring arrangement as a fix.** `blues_rock.md`'s vocal/guitar solution — not always playing both simultaneously — is often more effective than trying to carve two harmonically similar, register-overlapping sources apart with EQ alone, especially in genres with sparser overall arrangement.

## Cross-References

- `knowledge_base/genres/edm/jungle.md` — sub-bass vs. mid-bass frequency-pocket carving, named explicitly as a common mistake when skipped
- `knowledge_base/genres/edm/house.md` and `knowledge_base/genres/edm/jump_up.md` — kick/bass frequency-pocket and pitch-separation solutions
- `knowledge_base/genres/metal/metal.md` and `knowledge_base/genres/metal/metalcore.md` — guitar distortion masking the kick/bass low end
- `knowledge_base/genres/rock/blues_rock.md` — vocal-vs-guitar midrange masking solved through arrangement, not just EQ
- `knowledge_base/genres/electronic/future_funk.md` and `knowledge_base/genres/electronic/glitch_hop.md` — layered/sampled bass masking conflicts
- `knowledge_base/mixing/compression/sidechain_pumping.md` — the dynamic (non-EQ) solution to the 808/kick masking conflict
