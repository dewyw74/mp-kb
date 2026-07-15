---
plugin_name: "RX 11"
developer: "iZotope"
category: "audio repair and restoration"
type: "spectral audio repair, de-noise, and restoration suite"
cpu_usage: "high"
best_genres:
  - future_funk
  - trip_hop
  - vaporwave
strengths:
  - "Spectral Repair presents audio as a visual spectrogram that can be directly edited — unwanted sounds (clicks, dog barks, string squeaks, sirens) are lassoed and attenuated or interpolated away, a fundamentally different and often more precise approach than a purely automatic filter."
  - "Dedicated de-click, de-hum, de-noise, and de-reverb modules each target a specific, narrowly-defined noise problem, rather than one generic noise-reduction algorithm being asked to handle every kind of unwanted signal."
  - "Dialogue Isolate combines de-noise and de-reverb machine-learning processing in one real-time-capable module, purpose-built for cleaning up a vocal or dialogue take without manually chaining several separate repair steps."
  - "Machine-learning-assisted processing offers graduated intensity settings (light/medium/aggressive) per module, letting a producer choose how much repair to apply relative to how much of the source's natural character needs to survive the cleanup."
weaknesses:
  - "Heavier CPU and workflow overhead than a simple filter or gate — Spectral Repair's visual editing workflow in particular is a deliberate, manual process rather than a fast automatic fix, closer in spirit to Melodyne's graphical editing than to a real-time effect."
  - "Aggressive noise reduction settings can introduce their own audible artifacts (a thin, 'underwater,' or smeared quality) if pushed harder than the source material's actual noise floor requires — restoration tools carry the same over-processing risk documented for other corrective tools in this knowledge base, such as `knowledge_base/mixing/vocal_processing/de_essing.md`'s warning about de-essing's own potential artifacts."
alternatives:
  - "iZotope Nectar's own de-noise/de-ess capabilities for vocal-specific cleanup that doesn't need RX's broader restoration toolset (see `knowledge_base/vst_database/izotope_nectar.md`)"
  - "Manual spectral editing in a DAW's own frequency-domain tools, for producers who don't need RX's dedicated repair-module workflow"
recommended_settings:
  - "Cleaning sampled vinyl/tape source material before chopping or resampling (future_funk, trip_hop production): Spectral Repair or de-noise module set to remove vinyl surface noise and hiss from the source recording specifically before it enters the sampling/production chain, per `future_funk.md`'s documented modern-production technique: \"Spectral repair tools (iZotope RX-class) to clean vinyl noise and hiss from source material before mixing.\""
  - "Vocal/dialogue cleanup on a problematic take (mouth clicks, room hum, background noise): Dialogue Isolate or the dedicated de-click/de-hum modules at a light-to-medium intensity setting, checked by ear against the source's natural character rather than maximized by default."
  - "Deliberate lo-fi texture (the reverse use case): leave source noise/hiss intentionally unprocessed or reintroduce it after other repair, since genres like `trip_hop.md` and `french_house.md` treat vinyl noise and crackle as a deliberate emotional/textural device rather than a flaw to remove — RX's tools are not appropriate here unless the noise itself needs shaping rather than elimination."
common_uses:
  - "Removing vinyl surface noise, hiss, and crackle from sampled source material before it's used in a production"
  - "Vocal/dialogue restoration — de-clicking, de-humming, and de-noising a problematic take without re-recording"
  - "Visual, spectrogram-based removal of one-off unwanted sounds (clicks, bumps, extraneous noise) that a standard filter can't isolate"
tags: ["izotope", "rx", "restoration", "de-noise", "spectral-repair", "audio-repair"]
---

# RX 11

RX 11 (iZotope) is an audio repair and restoration suite built around spectrogram-based visual editing and a set of dedicated modules — de-click, de-hum, de-noise, de-reverb, and the combined Dialogue Isolate — each targeting a specific, narrowly defined noise or artifact problem. It occupies a distinct category from the other iZotope entries in this knowledge base: where Ozone handles full-mix mastering and Nectar handles vocal production, RX exists to fix or remove problems in a recording — noise, clicks, hum, unwanted reverb, extraneous sounds — rather than to shape or polish an otherwise clean signal.

## The Genre-Corpus Citation: Cleaning Sampled Source Material

`future_funk.md` is this knowledge base's direct citation for RX, and it names the plugin's product class specifically rather than describing restoration in generic terms: "Spectral repair tools (iZotope RX-class) to clean vinyl noise and hiss from source material before mixing," listed alongside AI-assisted stem separation and granular resampling as one of the genre's documented modern production techniques for working with sampled disco and funk source material. This is a genuinely distinct use case from vocal or dialogue repair — future funk's sample-based production process pulls from vinyl-sourced or vinyl-emulated audio, and RX's spectral repair and de-noise tools are the documented way to clean that source material of surface noise and hiss before it's chopped, resampled, or layered into a new production, rather than leaving vinyl artifacts baked into the sample by accident.

## The Reverse Case: When Vinyl Noise Is the Point, Not the Problem

It's worth naming directly that not every genre wants what RX does. `trip_hop.md` documents the opposite aesthetic stance explicitly: "Use vinyl noise, tape hiss, and heavy low-pass filtering deliberately as emotional/textural devices, not just as nostalgia — they contribute directly to the genre's noir, melancholic atmosphere," and `french_house.md` similarly calls for "vinyl noise/crackle layered under loops for authenticity." This means RX's role in sample-based/retro-adjacent genres isn't universal cleanup — `future_funk.md` calls for cleaning noise from source material specifically so a new, controlled amount of vinyl character can be added back deliberately at the production stage, rather than leaving accidental surface noise from the original source recording in the final track. RX is the right tool when noise is unwanted or needs to be controlled; it is the wrong tool when noise and hiss are themselves the deliberate genre-defining texture.

## Sound Character and Strengths

Spectral Repair's visual, spectrogram-based editing is RX's most distinctive capability — rather than applying a blanket algorithm across the whole signal, a specific unwanted sound (a click, a mouth noise, a brief extraneous noise) can be visually selected and attenuated or interpolated away, leaving the surrounding audio untouched. This is conceptually similar to Melodyne's graphical, note-by-note editing philosophy (`knowledge_base/vst_database/celemony_melodyne.md`) but applied to noise and artifacts rather than pitch. The dedicated single-purpose modules (de-click, de-hum, de-noise, de-reverb) mean each specific problem gets an algorithm built for that problem specifically, rather than one generic "clean it up" process being asked to handle fundamentally different kinds of unwanted signal.

## Weaknesses

RX's repair workflow, especially Spectral Repair's visual editing, is a manual, deliberate process rather than a fast automatic fix — it takes real time to use well, unlike a simple gate or filter. Pushed too aggressively, its noise-reduction modules can introduce their own audible artifacts (thinness, a processed or "underwater" quality), the same over-correction risk documented elsewhere in this knowledge base for other corrective processing, such as `knowledge_base/mixing/vocal_processing/de_essing.md`'s warning against de-essing hard enough to dull adjacent, non-problem material.

## Common Mistakes

Applying RX's de-noise/spectral-repair tools to source material in a genre (trip_hop, french_house) that treats vinyl noise and hiss as a deliberate textural element — per the citations above, this removes exactly the character the genre depends on rather than fixing a flaw. Pushing any single repair module's intensity to maximum by default rather than the light-to-medium settings appropriate to how much of the source's natural character needs to survive, per RX's own graduated intensity design.

## Cross-References

- `knowledge_base/genres/electronic/future_funk.md` — the direct genre-corpus citation of RX-class spectral repair tools for cleaning sampled vinyl source material
- `knowledge_base/genres/electronic/trip_hop.md`, `knowledge_base/genres/edm/french_house.md` — genres treating vinyl noise/hiss as a deliberate textural device, the reverse use case from RX's repair function
- `knowledge_base/vst_database/celemony_melodyne.md` — a conceptually related graphical/visual editing workflow, applied to pitch rather than noise
- `knowledge_base/vst_database/izotope_nectar.md` — iZotope's vocal-specific processing suite, for de-noise/de-ess needs scoped to vocal production rather than general audio restoration
- `knowledge_base/mixing/vocal_processing/de_essing.md` — the parallel over-correction risk documented for another narrowly-targeted corrective process
