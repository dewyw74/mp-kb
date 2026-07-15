---
technique_name: Reverb Automation Across a Song
category: reverb
problem_solved: "A single static reverb setting can't serve both a tight, present verse and a spacious, dramatic chorus/climax — the sense of space itself needs to change as the arrangement does"
parameters:
  send_level_automation: "Riding a reverb aux send's level up or down across sections, rather than changing the reverb's own settings, is the most common implementation"
  macro_timescale: "In slow-building genres, automation moves over many bars or minutes (filter opening + reverb send rising together) rather than per-hit"
  throws: "Short, deliberate spikes in reverb send on a single word/hit/hook rather than a section-wide level change — a different automation pattern from the gradual-build case"
signal_chain_position: "Automated on the reverb aux send's fader/level parameter (post-fader send from source tracks into the reverb bus), not on the reverb return itself"
genre_applicability:
  - screamo
  - reggaeton
  - post_rock
  - space_rock
  - gothic_rock
  - dream_pop
  - melodic_house
  - techno
  - progressive_house
  - trance
  - uplifting_trance
  - dub_techno
  - ambient_dub
  - reggae
related_techniques:
  - reverb_send_vs_insert
  - reverse_reverb
tags: ["reverb-automation", "reverb-send", "build", "dynamic-space"]
---

# Reverb Automation Across a Song

Across the knowledge base, reverb is treated less like a fixed spatial setting and more like a parameter that gets *played* over the course of a song — ridden up into choruses, opened gradually across a build, or thrown briefly onto a single word. The consistent thread is that the send level (how much of a source reaches the reverb bus), not the reverb's own internal settings, is what gets automated.

## Shifting the Sense of Space Between Sections

`screamo.md` states the goal most directly: "Careful reverb automation to shift the sense of space dramatically between quiet and loud sections within a single mix" — the reverb isn't decorating a static arrangement, it's actively marking the emotional distance between a song's quiet and loud halves. `gothic_rock.md` documents the same principle applied to a build rather than a contrast: "Reverb send and filter automation used to swell atmosphere into choruses and bridges gradually," reinforced by a layering technique — "Layering multiple long reverb sends (short room + long hall) for a more three-dimensional atmospheric depth than a single reverb plugin provides." `dream_pop.md` frames its automation as intentionally gradual rather than sharp: "Gradual, textural automation (reverb send levels, layer entrances) rather than sharp dynamic jumps; builds and releases happen slowly over many bars."

## The Macro Build: Reverb Send as a Multi-Minute Arrangement Tool

Electronic genres built around long, patient arcs treat reverb send automation as a primary structural device, often named in the same breath as filter cutoff automation. `post_rock.md` describes the technique concretely: "Automating a slow, multi-minute macro build (filter opening, reverb send increasing, additional layers fading in) across a DAW's arrangement view is a practical way to compose the genre's signature crescendo structure." `melodic_house.md`, `techno.md`, `progressive_house.md`, and `trance.md` all name near-identical versions of this pattern as their primary arrangement tool rather than an optional polish step — `progressive_house.md`: "Extensive, long-timescale automation (filter, reverb send, layer volume) is the primary arrangement tool, driving the gradual build/peak/breakdown arc that defines the genre." `uplifting_trance.md` ties it explicitly to emotional engineering: "Precise automation of unison width, filter, and reverb send across the breakdown-build-drop arc is central to engineering the genre's emotional peaks." `dub_techno.md` extends the same logic to a single sustained chord stab: "Delay feedback amount, reverb send level, and filter automation on the chord stab across extended sections are the primary arrangement tools, replacing conventional song-structure devices entirely."

## Throws: Short, Targeted Spikes Rather Than Section-Wide Builds

A distinct pattern from the gradual build is the reverb "throw" — a brief, targeted burst of send level on a single word or hit rather than a sustained rise. `reggaeton.md`: "Vocal delay throws and reverb swells are heavily automated," and `reggae.md` documents this as the genre's originating technique: "Effects-send automation (reverb/delay throws) is a genre-defining live-mixing technique, especially in dub-adjacent production," adding that this practice was "inherited directly from dub engineering practice." `ambient_dub.md` describes the same gesture as a real-time performance rather than pre-drawn automation: "Real-time, performative 'dub mixing' (channel muting, echo/reverb send riding, EQ sweeps on returns) functions as the arrangement itself, more than pre-drawn automation curves" — a reminder that reverb automation doesn't have to be programmed in advance; King Tubby and Lee Perry's dub mixing style rode these sends live at the mixing desk.

## Common Mistakes

**Automating the reverb's internal parameters (decay, size) instead of the send level.** Nearly every genre example above describes riding *send level*, which is simpler, more musical, and avoids the audible artifacts of changing a reverb's decay time mid-tail.

**Building macro automation without also automating a complementary parameter.** `post_rock.md`, `melodic_house.md`, and `progressive_house.md` all pair reverb send automation with simultaneous filter cutoff (and often layer volume) automation — reverb send rising in isolation reads as a mix error rather than an intentional build, since the ear expects the brightness/density to open up at the same time as the space does.

**Treating dub-style throws as a fixed effect rather than a live-mixing skill.** `ambient_dub.md`'s framing of effects riding as "the arrangement itself" is a reminder that throws are meant to feel performed and slightly unpredictable, not quantized to a rigid automation curve.

## Cross-References

- `knowledge_base/genres/rock/screamo.md` and `knowledge_base/genres/rock/gothic_rock.md` — reverb automation shifting the sense of space between quiet/loud or verse/chorus sections
- `knowledge_base/genres/rock/post_rock.md` and `knowledge_base/genres/rock/space_rock.md` — reverb send as part of a multi-minute macro build alongside filter automation
- `knowledge_base/genres/edm/melodic_house.md`, `knowledge_base/genres/edm/techno.md`, `knowledge_base/genres/edm/progressive_house.md`, `knowledge_base/genres/edm/trance.md`, and `knowledge_base/genres/edm/uplifting_trance.md` — reverb send automation as the primary arrangement tool across breakdown-build-drop cycles
- `knowledge_base/genres/edm/dub_techno.md` — reverb send automated on a single sustained chord stab
- `knowledge_base/genres/world_music/reggae.md` and `knowledge_base/genres/electronic/ambient_dub.md` — reverb/delay throws as a live, dub-engineering-derived mixing technique
- `knowledge_base/mixing/reverb/reverb_send_vs_insert.md` — why send routing specifically (rather than insert) is what makes this kind of automation practical
