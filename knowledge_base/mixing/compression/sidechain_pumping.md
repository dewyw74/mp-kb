---
technique_name: Sidechain Pumping
category: compression
problem_solved: "Bass and pads masking the kick, and the rhythmic 'breathing'/pumping feel that four-on-the-floor and 808-driven genres depend on for groove"
parameters:
  ratio: "4:1 to 10:1 (often deliberately extreme for an audible pump)"
  attack: "0-1ms (fast enough to duck instantly on the kick transient)"
  release: "80-250ms, tempo-synced to a 16th or 8th note so the duck recovers in time for the next hit"
  threshold: "set so the duck is clearly audible/felt, not subtle — the pump is usually a genre feature, not something to hide"
signal_chain_position: "Compressor on the bass/pad/synth bus, keyed from the kick (or 808), placed before any parallel or bus compression on that same channel"
genre_applicability:
  - house
  - french_house
  - tech_house
  - trance
  - uplifting_trance
  - progressive_trance
  - melodic_house
  - trap
  - drill
  - dance_pop
  - electropop
  - coldwave
related_techniques:
  - parallel_compression
  - frequency_masking
  - subtractive_eq
tags: ["sidechain", "ducking", "pumping", "four-on-the-floor", "808", "groove"]
---

# Sidechain Pumping

Sidechain compression triggered by the kick (or, in hip-hop-descended genres, the 808) is one of the most widely documented mixing techniques across this knowledge base — it appears as a defining production element in genres as different as house, trance, trap, and dance pop. The core mechanism is identical everywhere it's used: a compressor on the bass, pads, or other sustained low/mid-range elements is keyed from the kick, so every kick hit ducks those elements out of the way and lets the low end stay defined, then releases them back in before the next hit. What differs by genre is how audible and stylistically load-bearing that duck is meant to be.

## Why It Exists: Masking, Not Just Groove

The technical problem sidechain ducking solves is frequency masking — a sustained bass or pad note sitting in the same low-frequency region as the kick will mask the kick's fundamental and transient, producing a smeared, undefined low end. `house.md` documents this directly: "Sidechain compression from kick into bass and pads (the 'pumping' house groove feel)" is listed under processing, and its mixing section calls sidechain ducking "the signature rhythmic-mix technique." `trap.md` and `hip_hop.md` frame the same mechanism from the opposite direction — as damage control: "Sidechain compression from 808/kick into other low-mid elements to avoid masking" and "Sidechain compression between kick/808 and other elements to avoid low-end masking." The rhythmic "pump" that listeners associate with the technique is a side effect of solving this masking problem on every single kick hit, repeated steadily enough to become a groove element in its own right.

## When the Pump Is the Point, Not a Side Effect

In house and its close relatives, the pumping itself is treated as a genre signature independent of its masking-avoidance function. `house.md`'s production notes state it plainly: "Sidechain the kick into bass and pads for the essential 'pumping' house groove feel — it's as much a genre signature as a technical tool." `french_house.md` goes further, calling heavy sidechain ducking "both a rhythmic effect and a mix tool, carving space for bass on every beat." `dance_pop.md` borrows this same aesthetic wholesale into a pop context: "Sidechain the kick into bass and pads even at pop-level intensity — the pumping feel is what signals 'dance' rather than plain pop," with its production notes going as far as recommending "sidechain compression plugins with musical, tempo-synced curves rather than hard ducking for a smoother pump" as a specifically modern refinement.

## When the Pump Should Stay Subtle

Not every genre wants the effect to be heard as an effect. `melodic_house.md` explicitly dials back the intensity: "Moderate sidechain compression for groove cohesion (less aggressive than techno/house pumping)," prioritizing "sustain and presence without losing dynamic expression" over an audible pump. `progressive_trance.md` makes the same move even more explicitly, describing its sidechain as "present but far less pronounced/pumping than uplifting or hard trance." This is the key genre-differentiation variable for the technique: aggressive, audible pumping signals house/EDM-adjacent dance function, while a gentler, largely inaudible duck is used purely as a masking-avoidance tool in more melodically-focused or non-dance genres — `coldwave.md` frames this end of the spectrum explicitly, instructing producers to "sidechain the pads faintly to the kick to maintain rhythmic clarity without resorting to obvious pumping."

## Setting Up the Duck

Attack time needs to be fast enough (0-1ms) to catch the kick's transient instantly — a slow attack lets the transient through before the duck engages, defeating the point. Release time is the parameter that shapes the character most: a release tempo-synced to a 16th or 8th note lets the ducked element recover fully before the next kick hit, producing the tight, rhythmic pump documented across the house/trance genre family, while a slower, un-synced release produces a looser, more "breathing" duck better suited to melodic or ambient contexts. Ratio and threshold are typically pushed hard when the pump itself is the point — `house.md` and `french_house.md` both describe the technique as deliberately audible — and pulled back to a gentler setting when the goal is masking avoidance without a rhythmic signature, as in `melodic_house.md` and `progressive_trance.md`.

## Common Mistakes

**Treating the pump as optional polish rather than structural.** In house, trance, and their relatives, skipping sidechain ducking doesn't just lose a stylistic flourish — it leaves the exact masking problem the technique exists to solve unaddressed, producing the muddy, undefined low end `jungle.md`'s common-mistakes section warns about generally: "Letting mid-bass and sub-bass overlap and mask each other instead of carving distinct frequency pockets."

**Over-pumping in a context that calls for subtlety.** Applying house-style aggressive ducking to a melodic house or progressive trance track (or, per `coldwave.md`, a genre where "obvious pumping" is explicitly the thing to avoid) fights the genre's actual mixing goals — see `melodic_house.md` and `progressive_trance.md` above for the more restrained target.

**Un-synced release times.** A release that isn't locked to the track's tempo produces an inconsistent, seasick pump rather than the tight, rhythmic breathing documented throughout the house/trance family — sync the release to a musical subdivision (typically 8th or 16th note) rather than leaving it as a fixed millisecond value.

## Cross-References

- `knowledge_base/genres/edm/house.md` — sidechain pumping as core genre signature, not just a mix tool
- `knowledge_base/genres/edm/french_house.md` — sidechain ducking as simultaneously rhythmic effect and mix tool
- `knowledge_base/genres/edm/melodic_house.md` and `knowledge_base/genres/edm/progressive_trance.md` — deliberately restrained, less pumping sidechain use
- `knowledge_base/genres/hiphop/trap.md` and `knowledge_base/genres/hiphop/hip_hop.md` — sidechain framed primarily as 808/kick masking avoidance
- `knowledge_base/genres/pop/dance_pop.md` — house-style pumping borrowed into a pop context as a genre signifier
- `knowledge_base/genres/electronic/coldwave.md` — faint, deliberately inaudible sidechain use
