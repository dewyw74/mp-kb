---
technique_name: Reverb Type and Scale Selection
category: reverb
problem_solved: "Choosing a reverb that matches a track's genre scale and character — using an oversized concert-hall reverb on an intimate genre (or a dry, tight reverb on a genre that depends on huge space) actively misrepresents the style"
parameters:
  scale_matching: "Match reverb size to the genre's actual historical/performative scale — chamber-scale for intimate acoustic genres, stadium/concert-hall scale for arena and orchestral genres"
  decay_time: "Short (room/plate, under ~1.5s) for rhythmic clarity in dense/percussive genres; long (hall/cathedral, 2s+) for atmospheric or orchestral genres where space itself is the point"
  dry_wet_by_element: "Rhythm-critical elements (drums, bass, fast riffs) typically get shorter or no reverb than melodic/atmospheric elements (pads, vocals, leads) in the same mix"
signal_chain_position: "Typically a send/return bus rather than an insert, so multiple elements can share a common sense of space rather than each getting an isolated, disconnected reverb tail"
genre_applicability:
  - house
  - trance
  - french_house
  - chamber_music
  - romantic
  - classical_period
  - baroque
  - opera
  - jungle
  - speedcore
  - dub_techno
  - afrobeat
  - flamenco
  - indian_classical
  - celtic
related_techniques:
  - delay_types_and_sync
  - stereo_widening_techniques
tags: ["reverb", "convolution", "plate", "hall", "spatial-design", "genre-scale"]
---

# Reverb Type and Scale Selection

Reverb choice across this knowledge base is treated less as a single universal "add space" tool and more as a scale-matching decision — the right reverb type and decay time is the one that represents the genre's actual (or intended) performance space, and the wrong choice actively misrepresents the style rather than merely sounding unpolished. A cathedral-scale reverb on an intimate chamber piece, or a dry, tight room reverb on a genre built around vastness, both break the illusion the genre depends on.

## Matching Reverb Scale to Historical/Performative Space

The classical-music entries in this knowledge base are the most explicit about this principle, because each era and ensemble size implies a real physical performance space. `chamber_music.md` specifies "small recital-hall or salon-scale convolution reverb, much drier and more intimate than full-orchestra reverb settings," and names the failure mode directly in its common mistakes: "Applying small recital-hall convolution reverb rather than large concert-hall or cathedral settings to preserve scale authenticity" is listed as a *technique* to use, with the inverse — using large-hall reverb on chamber-scale material — implied as the mistake to avoid. `romantic.md` goes to the opposite extreme deliberately, because the Romantic-era orchestra itself expanded dramatically: "Large concert-hall or cathedral-scale convolution reverb suited to the expanded Romantic orchestra's scale and dynamic ambition." `classical_period.md` sits explicitly between these two poles: "Mid-sized concert-hall convolution reverb suited to the era's chamber-to-small-orchestra scale, larger than Baroque chamber works but smaller than full Romantic orchestra." `opera.md` extends the same logic to vocal projection specifically: "Opera-house-scale convolution reverb, calibrated to support both vocal projection and orchestral blend" — the reverb has to support how a singer would actually project in that physical space, not just sound pleasant in isolation.

## World Music: Reverb as Venue Authenticity

The world-music genre entries apply an identical scale-matching principle to their own traditional performance contexts. `flamenco.md` specifies "natural, intimate room ambience appropriate to flamenco's traditionally small-venue (tablao) performance context," `celtic.md` calls for "natural room ambience appropriate to traditional session/performance venues (pubs, small halls)," and `indian_classical.md` matches its own tradition's typically small, intimate performance settings. `afrobeat.md` takes a more targeted approach — mostly dry, with reverb reserved for specific elements: "Natural room ambience predominates; light plate reverb on vocals and horns for polish" — reflecting a live full-band recording aesthetic rather than a constructed spatial effect.

## Dance/Club Genres: Reverb as Genre-Defining Space, Not Realism

Trance and house diverge from the "match a real space" logic entirely — their reverb choices construct an artificial, idealized sense of scale that has no real-world venue equivalent. `trance.md` names this directly: "Long plate/hall reverbs create the genre's signature 'huge' sense of space," describing the goal elsewhere as a "big room in the sky." This is reverb used for emotional/atmospheric maximalism rather than spatial realism — the "space" being represented isn't any actual room, it's a feeling. `french_house.md` sits at the opposite pole within the same broader EDM family, favoring almost no reverb at all: "short room/plate on drums only; the genre favors a dry, upfront, in-your-face groove over spacious reverb tails" — because that genre's identity depends on a tight, sample-forward directness that a wash of reverb would dilute.

## Rhythm-Critical Genres: Reverb as the Enemy of Clarity

Several fast, transient-dense genres treat reverb primarily as a threat to manage rather than a tool to reach for. `speedcore.md` is unambiguous: "Minimal — used only for brief atmosphere in intros/breakdowns, never on the kick or main stab elements, since reverb tails would blur together at extreme tempo." `jungle.md` makes an almost identical case: "Used sparingly and mostly on vocal/horn stabs — jungle generally favors a dry, forward drum mix over spacious drum reverb." At high tempo or high rhythmic density, reverb tails from one hit don't have time to decay before the next hit arrives, so they stack up into an undifferentiated wash — the fix in both genres is the same: keep reverb off the elements carrying rhythmic information and reserve it, if used at all, for secondary/atmospheric elements that aren't competing for rhythmic clarity.

## The Notable Exception: Dub Techno's Reverb-as-Instrument

`dub_techno.md` treats reverb (paired with delay) not as a spatial finishing touch but as the genre's actual compositional and harmonic content — the reverb/delay tail on a chord stab is the sustained harmonic material the whole track is built around, not an effect applied after the fact. This is worth flagging specifically because it inverts the usual signal-chain assumption that reverb comes late in the chain as polish; in dub techno, the wet signal often *is* the arrangement.

## Common Mistakes

**Using a single default reverb setting across every genre.** A "safe" mid-length hall reverb applied indiscriminately will feel too big for jungle or speedcore, too small for trance, and too artificial for flamenco or celtic — reverb selection has to start from the genre's actual scale logic (real venue for world music/classical, constructed atmosphere for trance, near-absence for high-tempo/dense-rhythm genres), not a one-size-fits-all default.

**Reverb on rhythm-critical elements in high-tempo genres.** As `speedcore.md` and `jungle.md` both document, reverb tails on kick or lead rhythmic stabs at high tempo don't resolve before the next hit, producing a smeared, undefined groove rather than added space.

**Ignoring physical/vocal-projection logic in classical and vocal-forward genres.** `opera.md`'s point about reverb needing to support actual vocal projection (not just sound spacious) is a reminder that reverb choice in acoustically-grounded genres should be informed by how the real instrument/voice would behave in that space, not chosen purely by ear against a reference track.

## Cross-References

- `knowledge_base/genres/classical/chamber_music.md`, `knowledge_base/genres/classical/classical_period.md`, `knowledge_base/genres/classical/romantic.md` — reverb scale matched precisely to each era's actual ensemble/venue size
- `knowledge_base/genres/classical/opera.md` — reverb calibrated for vocal projection, not just ambience
- `knowledge_base/genres/edm/trance.md` and `knowledge_base/genres/edm/french_house.md` — opposite poles of constructed (non-realistic) reverb use within EDM
- `knowledge_base/genres/edm/speedcore.md` and `knowledge_base/genres/edm/jungle.md` — reverb minimized to protect rhythmic clarity at high tempo/density
- `knowledge_base/genres/edm/dub_techno.md` — reverb/delay as compositional content rather than a spatial finishing touch
- `knowledge_base/genres/world_music/flamenco.md`, `knowledge_base/genres/world_music/celtic.md`, `knowledge_base/genres/world_music/indian_classical.md`, `knowledge_base/genres/world_music/afrobeat.md` — reverb as traditional-venue authenticity
