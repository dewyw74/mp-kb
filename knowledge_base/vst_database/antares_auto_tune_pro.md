---
plugin_name: "Auto-Tune Pro"
developer: "Antares Audio Technologies"
category: "pitch correction"
type: "real-time pitch correction and vocal effect processor"
cpu_usage: "low"
best_genres:
  - mumble_rap
  - trap_soul
  - emo_rap
  - hyperpop
  - reggaeton
  - dancehall
  - country_pop
  - contemporary_country
  - corridos_tumbados
  - afrobeats
strengths:
  - "Auto Mode applies real-time correction fast enough for tracking and live performance, while Graph Mode exposes a full note-by-note, audio-to-MIDI-style pitch curve for detailed after-the-fact editing — one plugin covers both workflows."
  - "Retune Speed, Flex-Tune, and Humanize give granular control over how aggressively and how quickly pitch is pulled to the target note, spanning everything from an unnoticeable safety net to the fully robotic 'hard-tune' effect."
  - "Classic Mode reintroduces the original Auto-Tune 5 tracking algorithm — the specific, imperfect pitch-tracking behavior that produced the original late-1990s/2000s hard-tune sound — as a selectable mode rather than something later algorithm revisions accidentally smoothed away."
  - "Extremely low CPU cost per instance, making it practical to run on every vocal take, ad-lib, and harmony stack in a session simultaneously, which matters for genres that layer many Auto-Tuned takes at once."
weaknesses:
  - "Real-time Auto Mode tracks pitch automatically and can mistrack on fast melismatic runs, wide vibrato, or unclear pitch content, producing warbling artifacts that Graph Mode's manual note editing is usually needed to fix."
  - "Getting a natural-sounding transparent correction still requires deliberately backing Retune Speed and Flex-Tune off from their default/aggressive settings — the plugin's most famous sound (hard-tune) is also its default failure mode when transparency is the actual goal."
alternatives:
  - "Celemony Melodyne (graphical, audio-to-MIDI-style editing workflow rather than real-time knob-based correction — see `knowledge_base/vst_database/celemony_melodyne.md`)"
  - "iZotope Nectar's built-in pitch correction module (bundles Melodyne Essential alongside its own real-time correction — see `knowledge_base/vst_database/izotope_nectar.md`)"
  - "Waves Tune / Waves Tune Real-Time"
recommended_settings:
  - "Transparent pop/country-pop correction: moderate-to-fast Retune Speed (not instant), Flex-Tune engaged so already-close notes are left alone, Natural Vibrato left mostly intact — the goal is a vocal that doesn't announce the processing, per `knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md`'s transparent-use cluster (country_pop, contemporary_country)."
  - "Hard-tune/robotic 'T-Pain' effect (mumble rap, trap soul, hyperpop, reggaeton, dancehall): Retune Speed set to 0 or near-instant, Humanize off, Classic Mode engaged for the most overtly artificial tracking character, applied to whole phrases or ad-libs rather than just fixing occasional flat notes."
  - "Melismatic R&B/trap-soul vocal runs: back Retune Speed off further than the hard-tune setting and raise Flex-Tune so fast pitch movement within a phrase isn't quantized into a stepped, unnatural glide."
common_uses:
  - "Transparent, corrective-only pitch correction on a lead pop or country vocal"
  - "Deliberately audible hard-tune/robotic vocal effect as a genre-defining melodic and textural device"
  - "Real-time correction during tracking/live performance via Auto Mode, distinct from Melodyne's after-the-fact graphical editing"
tags: ["antares", "auto-tune", "pitch-correction", "vocal-processing", "hard-tune", "mixing"]
---

# Auto-Tune Pro

Auto-Tune Pro (Antares Audio Technologies) is the pitch correction plugin the effect itself is named after — "Auto-Tune" has become the generic term for audible pitch correction the way "Kleenex" has for tissue, and it is, by a wide margin, the single most-cited plugin across this knowledge base's entire genre corpus. It ships in two modes: Auto Mode, a fast, knob-driven real-time processor suited to tracking and live use, and Graph Mode, a detailed graphical pitch-curve editor for note-by-note correction after the fact. Genre files in this knowledge base cite it for two genuinely different jobs — invisible corrective polish and a deliberately audible, robotic melodic effect — and getting either one right depends on understanding which job a given genre actually wants.

## Two Opposite Uses, Both Genre-Defining

`knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md` documents this split directly, and it's worth restating in Auto-Tune Pro's own terms because the plugin's controls map almost exactly onto the two use cases. On the transparent side, `country_pop.md` states "Melodyne and Auto-Tune used flawlessly to create perfectly pitched pop vocals," and `contemporary_country.md` instructs: "Use Melodyne for precise pitch correction, followed by Auto-Tune for absolute polish" — here, Retune Speed is backed off, Flex-Tune is engaged so correctly-sung notes are left alone, and the goal is a vocal where the listener never consciously hears "Auto-Tune" as an effect. On the stylized side, `mumble_rap.md` is the most explicit genre file in the entire corpus: "Auto-Tune applied not for subtle correction but as an audible, expressive, melody-generating production tool," with its professional tips stating outright: "Treat Auto-Tune as a genuine melodic and expressive production tool, not a corrective effect." Here Retune Speed goes to (or near) zero, producing the audible, stepped "hard-tune" pitch-snap popularized by T-Pain and inherited by Future, Migos, and the broader mumble rap and trap-soul lineage documented in `trap_soul.md`'s "Auto-Tune (hard-tuned or subtly blended) as the genre's signature vocal effect."

## Regional and Stylistic Variation in the Hard-Tune Sound

The genre corpus makes clear that "hard-tune" isn't one fixed setting. `dancehall.md` documents its arrival as a specific historical shift within the genre: "Modern Dancehall (e.g., Popcaan) frequently uses Auto-Tune not just for pitch correction, but as a heavy, melodic, robotic texture on the vocals." `reggaeton.md` treats the vocal itself as "a modern instrument" processed with "a robotic, stylized texture." `afrobeats.md` explicitly contrasts its own lighter touch against the harder-edged version elsewhere: "Vocal production utilizes Auto-Tune, but often in a smoother, more R&B-oriented way than the robotic use found in modern Rap." `corridos_tumbados.md` sits at the gentlest end of the same spectrum, using "light Auto-Tune on vocals for contemporary polish" without fully obscuring the natural sing-song narrative delivery — closer to (but still distinct from) the transparent pop use case above. `hyperpop.md` pushes in the opposite direction, treating "obviously synthetic, robotic vocal and instrumental processing as a core aesthetic statement" — the most extreme documented endpoint of the stylized use case. `rage_rap.md` and `crunkcore.md` both document heavily, deliberately excessive Auto-Tune on screamed or chanted hooks specifically as an exaggerated, over-the-top choice rather than a subtle one.

## Sound Character and Strengths

Retune Speed is the plugin's single most consequential control: at slow-to-moderate settings it corrects pitch gradually enough that natural vibrato and expressive pitch movement survive, while at zero it forces an immediate, stepped snap to the nearest note in the target scale — the mechanical difference between "polished" and "robotic." Classic Mode is a genuinely useful historical feature rather than a nostalgia gimmick: it reinstates the original Auto-Tune 5 tracking algorithm, whose specific pitch-detection quirks are part of what made the late-1990s/2000s hard-tune sound (Cher's "Believe," T-Pain's catalog) sound the way it did — later algorithm revisions improved general-purpose tracking accuracy in ways that also subtly changed the character of the extreme setting. Flex-Tune and Humanize exist specifically to soften Auto-Tune's most mechanical tendencies for genres (trap soul, afrobeats, light corridos tumbados use) that want audible processing without the fully robotic Cher/T-Pain character.

## Weaknesses

Auto Mode's real-time pitch tracking, while fast, can mistrack on rapid melismatic runs, breathy or unclear pitch content, or wide natural vibrato, producing audible warble rather than clean correction or a clean stylized effect — Graph Mode's manual note-by-note editing is the usual fix, but that means a genuinely difficult vocal take can require abandoning the fast, knob-based workflow that's most of the plugin's appeal. The plugin also defaults toward its most recognizable, aggressive sound: getting a transparent, "flawless" pop-vocal result (per `country_pop.md`'s standard) requires deliberately dialing settings back from where a new user might first reach.

## Common Mistakes

Using default or aggressive Retune Speed settings on a genre that wants transparent correction, or the reverse — backing off Retune Speed on a genre (mumble rap, hyperpop, dancehall) whose entire vocal identity depends on the audible snap. Per `pitch_correction_philosophy.md`'s common-mistakes section, this is the single most common way Auto-Tune gets used wrong: applying it "subtly or apologetically" in a genre that wants it foregrounded, exactly as `mumble_rap.md` warns against directly.

## Cross-References

- `knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md` — the full transparent-vs-stylized framework this entry's two use cases are drawn from
- `knowledge_base/mixing/vocal_processing/vocal_chain_signal_order.md` — where pitch correction sits relative to de-essing, compression, and harmony stacking depending on whether it's corrective or stylistic
- `knowledge_base/mixing/vocal_processing/doubling_and_harmony_stacking.md` — frequently layered with hard-tuned Auto-Tune ad-libs and harmonies in trap and mumble rap production
- `knowledge_base/genres/hiphop/mumble_rap.md`, `knowledge_base/genres/hiphop/trap_soul.md`, `knowledge_base/genres/hiphop/emo_rap.md`, `knowledge_base/genres/pop/hyperpop.md` — the stylized, audible hard-tune use case
- `knowledge_base/genres/country/country_pop.md`, `knowledge_base/genres/country/contemporary_country.md` — the transparent, corrective-only use case
- `knowledge_base/genres/world_music/dancehall.md`, `knowledge_base/genres/world_music/reggaeton.md`, `knowledge_base/genres/world_music/afrobeats.md`, `knowledge_base/genres/world_music/corridos_tumbados.md` — regional variation in stylized Auto-Tune intensity and character
- `knowledge_base/vst_database/celemony_melodyne.md` — the graphical, audio-to-MIDI-style alternative workflow, often used alongside Auto-Tune rather than instead of it (per `contemporary_country.md`'s "Melodyne... followed by Auto-Tune" chain)
