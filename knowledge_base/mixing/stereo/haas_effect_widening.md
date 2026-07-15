---
technique_name: "Haas Effect (Precedence Effect) Widening"
category: stereo
problem_solved: "A mono or narrow source needs to read as wide and immersive without true stereo divergence in pitch or timbre, and without the listener consciously hearing a discrete slap-back echo"
parameters:
  delay_range: "Roughly 10-35ms between a duplicated hard-left and hard-right copy of the same source is the commonly cited sweet spot for perceived width without a discrete, audible echo"
  fusion_threshold: "The broader perceptual fusion window Helmut Haas documented in his 1949 research extends to roughly 40ms for complex program material (speech, piano, full mixes); Wallach et al.'s related 1949 precedence-effect work found fusion at 1-5ms for clicks and up to 40ms for more complex sounds — beyond that threshold the ear starts hearing a separate, discrete repeat rather than one widened source"
  source_prep: "Duplicate the mono source, pan one copy hard left and the other hard right, and delay one side within the fusion window"
  localization_behavior: "Perceived source direction follows the earlier-arriving (undelayed) signal even though both copies remain audible — this directional dominance of the first arrival is the core of the precedence effect"
signal_chain_position: "Applied per-element on a duplicated signal path (pre-bus), rather than as a mix-bus effect, since it depends on manipulating two correlated copies of the same source rather than processing a single existing stereo signal"
genre_applicability:
  - space_ambient
  - classic_rock
  - blues_rock
  - electric_blues
  - alt_country
  - ska_punk
related_techniques:
  - panning_laws
  - stereo_widening_techniques
  - delay_types_and_sync
tags: ["haas-effect", "precedence-effect", "stereo-widening", "pre-delay", "psychoacoustics"]
---

# Haas Effect (Precedence Effect) Widening

The Haas effect — named for Helmut Haas's 1949 doctoral research, and closely tied to the "precedence effect" described the same year by Wallach et al. — is the psychoacoustic phenomenon where two versions of the same sound, arriving within a short enough delay window, are perceptually fused into a single, wider-sounding source rather than heard as two distinct events. Perceived direction follows whichever copy arrives first, even though the delayed copy remains audible and contributes to the sense of width (iZotope, "What Is the Haas Effect and How to Use It"; Produce Like a Pro, "Haas Effect: What It Is and How It's Used").

The practical technique built on this: duplicate a mono source, pan one copy hard left and the other hard right, and delay one side by roughly 10-35ms. Within that window, the two copies fuse into what reads as a single, wide source rather than a doubled or echoing one; push the delay past the broader ~40ms fusion threshold Haas's and Wallach's research identified, and the ear starts perceiving a discrete second event — an audible slap-back or echo — instead of pure width (WaveInformer, "Haas Effect in Audio Production"; Wikipedia, "Precedence effect").

## A Useful Contrast: Slap-Back Delay Sits Outside the Haas Window

This knowledge base's `mixing/delay/delay_types_and_sync.md` documents a short, un-synced delay technique that is worth distinguishing carefully from Haas-window widening, because the two are easy to conflate and the genre corpus is specific about the difference in delay time. `classic_rock.md` specifies "Slap-back (80-120 ms) delay on vocals and lead guitar for classic rock 'thickness'" — a technique also documented, in near-identical form, across `blues_rock.md`, `electric_blues.md`, `alt_country.md`, and `ska_punk.md`. That 80-120ms range sits well outside the roughly 10-40ms Haas fusion window: it is long enough to be perceived as a discrete, audible repeat rather than fusing into a single wide source. Slap-back delay and Haas-effect widening solve related but distinct problems — slap-back deliberately adds a perceptible (if subtle) sense of a repeat for "thickness," while true Haas-window widening is meant to be imperceptible *as* an echo, read only as width. The genre corpus's slap-back documentation is genuine and valuable production guidance, but it describes the neighboring technique, not this one — no genre entry in this knowledge base currently specifies a delay time inside the actual Haas fusion window for pure widening purposes, which is worth stating plainly rather than stretching the slap-back citations to cover a claim they don't make.

## Practical Application

`space_ambient.md`'s processing notes give this technique's clearest direct namecheck in the genre corpus: "stereo widening via Haas delay or chorus" is listed alongside tape saturation and sidechain ducking as a core production technique for the genre's wide, immersive pad and sequencer textures — confirming both that the technique is genre-documented under its own name and that it's treated as functionally interchangeable with chorus-based widening in practice, since both decorrelate a source across the stereo field using a short time-based offset.

More broadly, the technique is best understood through the general psychoacoustic principle it rests on: because human sound localization weights the first-arriving wavefront so heavily (the precedence effect), a second, slightly delayed copy of the same signal can be added almost "for free" in terms of perceived width, provided it stays inside the fusion window. This makes it a useful alternative to true stereo-divergent widening methods — like the double-tracked, hard-panned guitar takes documented extensively across `metal.md`, `hard_rock.md`, and `classic_rock.md` (see `stereo_widening_techniques.md`) — in situations where a genuine second performance or take isn't available and only a single mono source exists to work from.

## Common Mistakes

**Setting the delay time too long and getting an unwanted slap-back instead of pure width.** As the classic-rock/blues-rock slap-back citations above illustrate, delay times in the 80-120ms range read as a discrete echo, not fused width — if the goal is Haas-effect widening rather than an audible repeat, the delay needs to stay inside the roughly 10-35ms window.

**Applying Haas widening to a mono-critical source (bass, kick).** Because one channel is delayed relative to the other, summing the result to mono reintroduces comb-filtering/phase-cancellation risk — the same mono-compatibility concern documented in `mid_side_processing_and_mono_compatibility.md` for widened low-frequency content generally.

**Confusing Haas-window widening with slap-back delay in production notes or client communication.** They use the same basic mechanism (a duplicated, delayed copy of a source) but aim for opposite perceptual outcomes — one wants to be inaudible as a discrete event, the other wants to be subtly heard.

## Cross-References

- `knowledge_base/genres/electronic/space_ambient.md` — the technique's direct, named appearance in the genre corpus ("stereo widening via Haas delay or chorus")
- `knowledge_base/mixing/delay/delay_types_and_sync.md` — the 80-120ms slap-back technique documented across `classic_rock.md`, `blues_rock.md`, `electric_blues.md`, `alt_country.md`, and `ska_punk.md`, and its important distinction from Haas-window widening
- `knowledge_base/mixing/stereo/panning_laws.md` — the hard-panning behavior this technique's L/R split depends on
- `knowledge_base/mixing/stereo/stereo_widening_techniques.md` — the double-tracking method preferred when a genuine second take/performance is available instead of a delayed duplicate
- `knowledge_base/mixing/stereo/mid_side_processing_and_mono_compatibility.md` — the mono-compatibility risk this technique introduces on low-frequency sources

Sources: [What Is the Haas Effect and How to Use It — iZotope](https://www.izotope.com/community/blog/what-is-the-haas-effect), [Haas Effect: What It Is and How It's Used — Produce Like A Pro](https://producelikeapro.com/blog/haas-effect/), [Haas Effect in Audio Production — WaveInformer](https://waveinformer.com/2024/01/31/haas-effect-in-audio-production/), [Precedence effect — Wikipedia](https://en.wikipedia.org/wiki/Precedence_effect)
