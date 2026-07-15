---
technique_name: "Attack and Release Time Science"
category: compression
problem_solved: "A compressor doing the wrong job on a signal's envelope — crushing a transient that should have been left alone, or letting a transient through when the goal was to catch it — because attack/release were set from habit rather than from what the source's envelope and the genre actually need"
parameters:
  fast_attack: "Sub-millisecond to ~5ms; engages before the transient peak has passed, catching/controlling the initial hit — used when transient control or aggressive grab is the goal (slap bass, kick drums, peak-limiting a vocal)"
  slow_attack: "10ms and up, sometimes tens of ms; lets the transient through untouched and only clamps down on the sustain portion — used when the transient's punch needs preserving while the tail is tamed or thickened"
  fast_release: "Sub-100ms; recovers gain quickly, useful for tempo-locked rhythmic pumping but risks audible distortion or amplifying low-frequency ripple if pushed too fast on bass-heavy material"
  slow_release: "150ms and up; recovers gradually, avoiding audible pumping but risking the compressor still being in gain reduction when the next transient arrives if set too slow for the material's tempo"
signal_chain_position: "A parameter choice within any compressor insert — individual element, bus, or master — rather than a distinct chain position of its own"
genre_applicability:
  - funk
  - ambient
  - post_grunge
  - modal_jazz
  - thrash_metal
  - doom_metal
  - stoner_metal
related_techniques:
  - ratio_and_knee_selection
  - sidechain_pumping
  - transient_shaping_for_punch_and_glue
tags: ["attack-time", "release-time", "transient-control", "pumping", "compression", "envelope"]
---

# Attack and Release Time Science

Attack and release are the two settings that decide what a compressor actually reacts to — a fast attack catches a transient before it passes, a slow attack lets it through and only grabs the sustain, and release decides how quickly the compressor lets go before the next hit arrives. Genre files across this knowledge base treat these two parameters as the real creative decision in a compressor, often specifying them independently of ratio because they change what a compressor does to a signal's shape, not just how much it turns the volume down.

## Fast Attack: Controlling the Transient Itself

`funk.md` reaches for a fast attack specifically because slap bass produces sharp, aggressive transients that need active control: "VCA compression (like SSL channel strips) used for punch and 'smack' on drums and bass. Fast attack times to control the aggressive transients of slap bass." `thrash_metal.md` applies the same logic to a kick drum under extreme tempo demands: "Heavy compression on the drums to keep them punchy and consistent at extreme speeds. Fast attack/release on the kick drum." In both cases, fast attack is chosen because the transient itself is the problem being managed — too sharp, too inconsistent, or too fast for a slower-reacting compressor to keep up with.

## Slow Attack: Letting the Transient Through

The opposite choice shows up just as often, and for the opposite reason — preserving a transient's punch while the compressor works on what comes after it. `doom_metal.md`'s drum guidance states this directly: "Slow attack, medium release on drums to let transients punch." The same file applies the identical logic to guitars, in a completely different production note: "dial in a slow attack compressor on the guitar bus to sustain notes without sacrificing attack." Both citations describe the same mechanism — a slow attack means the compressor doesn't engage until after the initial transient has already passed, so the attack survives untouched while the compressor's gain reduction only affects the sustain that follows. `stoner_metal.md` documents a numeric version of the same idea on its drum bus: "Gentle bus compression on drums (2:1 ratio, 30 ms attack) to glue the kit" — 30ms is long enough to let a drum hit's initial transient through before the compressor engages.

## Release Time and the Pumping Tradeoff

Release time governs a different tradeoff: how quickly the compressor lets go before the next hit, which determines whether gain reduction is audible as "pumping" or stays inaudible. `ambient.md` treats pumping as something to actively avoid: "Light bus compression (1.5:1-2:1, slow attack/release) for glue; avoid pumping — ambient relies on sustained, unbroken tone." A slow release here keeps the compressor's recovery gradual enough that listeners don't hear the gain moving, which matters specifically because ambient's sustained tones would make any audible recovery obvious. `post_grunge.md` shows the opposite priority applied to a different element in the same track: "vocal compression with fast attack and medium release to control peaks," later specified more precisely as "a fast-attack vocal compressor (3:1) to control peaks while retaining dynamics." Here fast attack and a moderate (not slow) release are chosen because the goal is active peak control on a lead vocal, where some audible compressor movement is an acceptable cost of consistent level.

## The Same Track Can Use Opposite Settings on Different Elements

`post_grunge.md`'s mixing section is the clearest example in the corpus of attack/release being treated as a per-element decision rather than a single track-wide setting: "Compression uses a 2:1 ratio on the drum bus with medium attack to preserve transients, parallel compression on guitars for thickness, and a fast-attack vocal compressor (3:1) to control peaks while retaining dynamics." The drum bus gets a medium attack specifically to preserve transient punch across the whole kit, while the vocal — a completely different kind of source, with a different problem (peak consistency, not transient character) — gets a fast attack instead. The lesson is that attack/release settings track the specific job a compressor is doing on a specific source, not a genre-wide house style.

## Common Mistakes

**Using a single "vibe" attack/release setting across every element in a mix.** `post_grunge.md`'s drum-bus-vs-vocal split shows why this fails — a drum bus needing transient preservation and a vocal needing peak control call for genuinely different attack behavior, even within the same song.

**Setting a fast attack when the actual goal is glue, not transient control.** `doom_metal.md` and `stoner_metal.md` both specifically choose a slow attack on drums to let punch through — a fast attack in the same spot would flatten the exact transient character those genre files are protecting.

**Setting release too fast on bass-heavy or sustained material.** `ambient.md`'s "avoid pumping" instruction exists because a release fast enough to be audible on sustained tones reads as an unwanted rhythmic artifact rather than transparent glue — the slower release keeps the gain-reduction recovery below the threshold of conscious perception.

**Ignoring tempo when setting release on rhythmic material.** A release time that hasn't fully recovered by the next hit leaves the compressor perpetually in gain reduction, quietly reducing headroom and punch across an entire performance — `thrash_metal.md`'s "fast attack/release on the kick drum" exists precisely because its extreme tempo leaves no room for a release time that lingers.

## Cross-References

- `knowledge_base/genres/r_and_b/funk.md` — fast attack chosen specifically to control slap-bass transients
- `knowledge_base/genres/metal/thrash_metal.md` — fast attack/release on the kick drum to keep pace with extreme tempo
- `knowledge_base/genres/metal/doom_metal.md` — slow attack on both drums and guitar bus to preserve transient punch while shaping sustain
- `knowledge_base/genres/metal/stoner_metal.md` — a numeric 30ms attack example of a slow-enough setting to let transients through
- `knowledge_base/genres/electronic/ambient.md` — slow attack/release specifically to avoid audible pumping on sustained tone
- `knowledge_base/genres/rock/post_grunge.md` — different attack/release settings on drum bus vs vocal within the same track
- `knowledge_base/genres/jazz/modal_jazz.md` — slow-attack, very-low-ratio bus compression to glue a multi-mic ensemble without disturbing its dynamic range
- `knowledge_base/mixing/compression/sidechain_pumping.md` — a technique where fast attack and tempo-synced release are used to make gain reduction deliberately audible, the inverse goal of `ambient.md`'s approach here
