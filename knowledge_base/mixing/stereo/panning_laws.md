---
technique_name: "Panning Laws (Equal-Power vs. Linear)"
category: stereo
problem_solved: "A signal panned to different positions across the stereo field changes in perceived loudness depending on which gain curve the pan pot uses — center-panned material can sound disproportionately loud or, with certain curves, disproportionately weak relative to hard-panned material, and the same session can translate inconsistently across DAWs with different default pan laws"
parameters:
  equal_power_law: "Center position attenuated by roughly -3dB per channel using sine/cosine (or square-root) gain curves, keeping combined acoustic power constant as a mono source sweeps from hard-left to hard-right; this is the most common DAW default"
  linear_law: "A straight-line amplitude fade between the L and R channels with no center compensation; center position sums to roughly -6dB combined relative to a hard pan, which can make center-panned elements sound comparatively weak next to hard-panned ones"
  compromise_laws: "Many consoles and DAWs offer an intermediate setting, commonly around -4.5dB attenuation at center, as a middle ground between the equal-power and linear extremes"
  hard_pan_behavior: "At full hard-left or hard-right, the choice of pan law becomes irrelevant — only one channel carries signal regardless of curve — so pan-law choice only actually matters for positions between center and the extremes"
signal_chain_position: "Set at the DAW/console's global pan-law preference or per-channel pan pot, upstream of all other processing, since it changes the fundamental L/R gain relationship before EQ, dynamics, or effects touch the signal"
genre_applicability:
  - metal
  - hard_rock
  - arena_rock
  - classic_rock
  - glam_rock
  - tech_house
  - jungle
  - trance
related_techniques:
  - haas_effect_widening
  - stereo_imaging_by_frequency_range
  - stereo_widening_techniques
tags: ["panning", "pan-law", "equal-power", "linear-pan", "stereo-imaging", "hard-panning"]
---

# Panning Laws: Equal-Power vs. Linear

A pan law is the gain curve a pan pot applies to a signal as it sweeps between hard-left and hard-right. The two dominant approaches are equal-power (roughly -3dB attenuation at center, using sine/cosine or square-root curves to keep total acoustic power constant across the pan range) and linear (a straight amplitude fade with no center compensation, which sums to roughly -6dB at center and can make centered elements sound comparatively weak). Most DAWs default to equal-power or an intermediate compromise curve around -4.5dB, precisely because an uncompensated linear pan makes centered material sound disproportionately quiet next to hard-panned material — a real, audible problem rather than a purely academic distinction (Sound on Sound, "Q. What pan-law setting should I use?"; Full Compass, "5 Things You Need to Know About Panning Laws").

This knowledge base's genre entries don't discuss pan-law curves by name — no genre file specifies "-3dB" or "equal-power" directly — so the grounding here is necessarily lighter than a technique like parallel compression or auto-tune, which the corpus documents explicitly and repeatedly. What the corpus *does* document extensively is a pattern of panning practice that pan-law behavior directly explains.

## Why Hard-Panning Is the Documented Default for Width

Across an unusually wide range of genres, the specific panning move described isn't a moderate, partial pan but a hard, full-left/full-right placement. `metal.md`'s mixing notes state it plainly: "Double-tracked rhythm guitars panned hard left/right create the genre's characteristic wide, powerful 'wall of sound.'" `hard_rock.md` matches this almost verbatim — "Rhythm guitars double-tracked and hard-panned left/right for a wide power-chord wall" — as does `classic_rock.md` ("Rhythm guitars often double-tracked and panned hard left/right for width"), `arena_rock.md` ("doubled rhythm guitars panned hard left/right"), and `glam_rock.md` ("guitar and handclaps spread for a big, glossy stereo picture").

This consistency is worth reading through the lens of pan law: at the hard-left/hard-right extremes, pan-law curve choice is moot, because only one channel is carrying signal — there's no center-compensation ambiguity to resolve. Genres that want maximum, unambiguous, translation-safe width reach for hard panning specifically because it sidesteps the pan-law question entirely, rather than relying on a partial pan position whose perceived loudness depends on which curve the DAW or console applies.

## Where Pan-Law Choice Actually Matters: Partial-Pan Elements

Pan law's practical effect shows up not at the hard extremes but in the moderate, partial-pan positions genre entries describe for texture and groove elements. `tech_house.md`'s stereo-imaging notes place "percussion layers spread across the stereo field for groove complexity and interest" while "kick and bass stay centered/mono for club translation" — this spread-but-not-hard percussion placement is exactly the pan-law-sensitive middle ground, where an uncompensated linear curve could make individual percussion hits swim in and out of perceived loudness as their pan position shifts relative to center. `jungle.md` documents a similar split: "breaks generally centered or lightly widened, with pads and horn stabs given more stereo spread" — again, moderate, non-hard positions where consistent, predictable gain behavior across the pan range is what keeps a densely layered mix's relative balance stable as individual elements are placed.

## Cross-DAW Translation

A pan-law mismatch is also a portability problem, not just a within-session mixing concern: because pan law is typically a project-level or global preference rather than something baked into the audio itself, opening the same session in a different DAW (or a collaborator's system with a different default pan law) can shift the perceived balance of any partially-panned material, even though no fader or pan pot setting actually changed (Full Compass, "5 Things You Need to Know About Panning Laws").

## Common Mistakes

**Relying on partial pan positions for critical elements without checking the project's pan-law setting.** A vocal or lead panned slightly off-center will translate differently under a linear vs. equal-power law; hard panning (as the genre corpus consistently favors for wide guitar/texture elements) avoids this ambiguity, but centered or near-centered lead elements are exactly where an unexamined pan-law default can cause an unexpected level shift.

**Assuming pan law is irrelevant because "it's just panning."** As the tech_house.md and jungle.md percussion/texture examples show, moderate stereo spread on multiple simultaneous elements is common practice — and pan law determines whether that spread reads as consistent or as an uneven, swimming balance.

**Not accounting for pan-law differences when a mix is opened in a different DAW or handed off to a collaborator.** Because pan law usually isn't printed into the audio, cross-platform translation can silently change a mix's center-vs-side balance.

## Cross-References

- `knowledge_base/genres/metal/metal.md`, `knowledge_base/genres/rock/hard_rock.md`, `knowledge_base/genres/rock/classic_rock.md`, `knowledge_base/genres/rock/arena_rock.md`, `knowledge_base/genres/rock/glam_rock.md` — hard-panned double-tracking as the consistent documented default for guitar width
- `knowledge_base/genres/edm/tech_house.md` and `knowledge_base/genres/edm/jungle.md` — moderate, partial-pan placement of percussion and texture elements, the range where pan-law curve choice has the most audible effect
- `knowledge_base/mixing/stereo/stereo_widening_techniques.md` — the broader width/mono-compatibility strategy this technique's hard-panning default supports
- `knowledge_base/mixing/stereo/haas_effect_widening.md` — a complementary, delay-based widening technique for sources that aren't simply double-tracked and panned

Sources: [Q. What pan-law setting should I use? — Sound on Sound](https://www.soundonsound.com/sound-advice/q-what-pan-law-setting-should-use), [5 Things You Need to Know About Panning Laws — Full Compass Systems](https://www.fullcompass.com/gearcast/5-things-you-need-to-know-about-panning-laws)
