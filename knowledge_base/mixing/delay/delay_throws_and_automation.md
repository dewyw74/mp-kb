---
technique_name: Delay Throws and Automation
category: delay
problem_solved: "A delay left at a constant send level either sits too far back to be felt on key moments or clutters the mix constantly when it should only appear as a targeted accent on specific words, hits, or transitions"
parameters:
  throw: "A brief, deliberate spike in delay send level on a single word, hit, or phrase ending, rather than a sustained send level across a whole section"
  automation_target: "Delay send level (not the delay's own time/feedback parameters) automated per-phrase or per-transition"
  live_performance_variant: "Ridden by hand at the mixing desk in real time (dub-style) rather than pre-drawn as a fixed automation curve"
signal_chain_position: "Automated on the delay aux send fader from the source track, spiking briefly at specific structural or lyrical moments"
genre_applicability:
  - glitch_hop
  - reggae
  - reggaeton
  - nu_skool_breaks
  - trip_hop
  - space_rock
  - post_punk
  - contemporary_r_and_b
  - drumstep
  - reggae_rap
related_techniques:
  - reverb_automation
  - tempo_synced_vs_free_delay
tags: ["delay-throw", "delay-automation", "send-riding", "dub-mixing"]
---

# Delay Throws and Automation

A "delay throw" — a brief, targeted spike in delay send level on a single word, hit, or transition moment, rather than a constant send level running throughout a section — is documented across the genre corpus as a distinct technique from simply having delay present in a mix. It's an automation move, and in its originating context (dub reggae), an explicitly performative one.

## The Dub Origin of the Throw

`reggae.md` names the technique as a genre-defining live-mixing practice: "Effects-send automation (reverb/delay throws) is a genre-defining live-mixing technique, especially in dub-adjacent production," and recommends "Applying effects-send automation (reverb/delay throws) as a deliberate mixing technique inherited directly from dub engineering practice." This is the origin point the corpus traces most other genres' use of the technique back to — King Tubby and Lee Perry's practice of riding effects sends live at the mixing desk as a performance, muting and unmuting channels and spiking delay/reverb sends on specific vocal phrases or drum hits in real time rather than programming a fixed curve in advance.

## Vocal-Focused Throws in R&B and Reggae-Adjacent Genres

`contemporary_r_and_b.md` documents delay throws as a precision vocal-production technique: "Extensive vocal volume riding. Delay throws automated on specific words," and its sound-design summary elaborates: vocals are treated "with immense care, utilizing techniques like parallel compression, intricate delay throws, and lush plate reverbs to create a larger-than-life, intimate presence." `reggaeton.md` pairs the technique with its reverb counterpart directly: "Vocal delay throws and reverb swells are heavily automated." `reggae_rap.md` documents the same gesture specifically at phrase endings, carrying the dub tradition into hip-hop: "dub-style echo throws on vocal phrase endings," recommending producers "Layer dub-style delay/echo throws on vocal phrase endings, a technique carried directly from reggae/dub production into the crossover's hip-hop side."

## Rhythmic and Transitional Throws in Electronic Genres

Outside vocal-specific use, several electronic genres apply the same throw technique to instrumental stabs and structural transitions. `glitch_hop.md`: "Reverb/delay throws on vocal chops for space," with its delay section adding rhythmic specificity — "Syncopated delay throws (1/8 dotted, triplet) on vocal chops and lead stabs for rhythmic interest without cluttering the main groove." `nu_skool_breaks.md` ties the throw specifically to structural transitions rather than ongoing texture: "Precision-automated reverb/delay throws for transition moments." `drumstep.md` uses the throw as a device to sell a specific structural shift: "Used mainly at transition points (pitch-bent, filtered delay throws) to sell the shift between half-time and full-tempo sections." `space_rock.md` frames the throw as part of a slower, patient build rather than a quick accent: "Automated, slowly-evolving send effects (filtered delay throws, reverb swells) programmed via DAW automation lanes to recreate the genre's patient dynamic builds." `post_punk.md` groups delay throws with other automated effects as a marker of structural change within a repetitive groove: "Effects automation (delay throws, filter sweeps, gated reverb triggers) used as a compositional device to mark structural transitions within otherwise repetitive, groove-based arrangements."

## Stereo Placement of Throws

`trip_hop.md` adds a spatial dimension to the technique, noting that delay throws are often placed wider in the stereo field than the dry source they come from: "Moderate width; drums and bass centered and mono-compatible, sampled strings/pads and delay throws panned wider for atmosphere." This suggests throws are frequently treated as an atmospheric layer distinct from the dry signal's own stereo position, rather than simply following the source's pan.

## Common Mistakes

**Setting delay send level as a constant rather than an automated spike.** Every citation above treats the throw as a *momentary* event tied to a specific word, hit, or transition — a delay send left at a fixed level throughout a section produces a different (and usually less intentional-sounding) result than a targeted throw.

**Programming throws with rigid, mechanically identical timing.** `reggae.md` and `ambient_dub.md`'s framing of the technique as a live performance gesture (see `reverb_automation.md`) is a reminder that dub-style throws are meant to feel human and slightly varied, not quantized to an identical automation shape every time.

**Ignoring stereo placement when building a throw.** As `trip_hop.md` shows, a throw panned identically to its dry source can feel like it's simply extending the source rather than opening up separate atmospheric space — placing throws wider is a deliberate spatial choice in several genre examples.

## Cross-References

- `knowledge_base/genres/world_music/reggae.md` — the dub-mixing origin of the delay/reverb throw as a live performance technique
- `knowledge_base/genres/r_and_b/contemporary_r_and_b.md` and `knowledge_base/genres/world_music/reggaeton.md` — vocal-focused delay throws automated on specific words/phrases
- `knowledge_base/genres/hiphop/reggae_rap.md` — dub-style echo throws carried from reggae into hip-hop vocal production
- `knowledge_base/genres/electronic/glitch_hop.md` and `knowledge_base/genres/edm/nu_skool_breaks.md` — syncopated and transition-focused delay throws in electronic production
- `knowledge_base/genres/edm/drumstep.md` and `knowledge_base/genres/rock/space_rock.md` — delay throws used to sell structural transitions and slow builds
- `knowledge_base/mixing/reverb/reverb_automation.md` — the parallel reverb-side technique, frequently automated alongside delay throws in the same genres
