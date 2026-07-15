---
workflow_name: "FL Studio Vocal Tuning and Comping Pipeline"
daw: "fl_studio"
category: "recording"
goal: "Sequence a lead vocal's post-recording pipeline in the correct order — comping the strongest take first, then pitch-correcting the comped take, with correction amount/retune speed automated across the phrase rather than applied uniformly — using FL Studio's native and third-party pitch-correction tools."
steps:
  - "Comp the lead vocal to a single, finished take first, per `knowledge_base/daw/fl_studio/recording_and_audio_editing_workflow.md`'s comping workflow — auditioning take lanes, cutting the strongest sections onto one comp track, and crossfading splice points — before any pitch-correction plugin touches the vocal."
  - "Render or consolidate the finished comp into a single continuous audio clip so downstream pitch correction analyzes one coherent performance rather than a stack of edited fragments with potentially mismatched pitch-detection results at each splice."
  - "Decide whether the target sound is transparent/corrective or audibly stylized before choosing a tool, per `knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md` — this decision determines both which plugin is appropriate and how aggressively its settings should be pushed."
  - "For transparent, note-accurate correction, insert Newtone on the comped vocal clip and use its graphical, note-by-note editing to nudge individual notes toward pitch while preserving natural vibrato and pitch drift, the FL Studio-native equivalent to the Melodyne workflow documented in `knowledge_base/vst_database/celemony_melodyne.md`."
  - "For a real-time or performance-style correction pass (including MIDI-controlled harmonization), insert Pitcher instead, keeping Retune Speed and correction amount moderate for a transparent result, comparable to the corrective-mode use of `knowledge_base/vst_database/antares_auto_tune_pro.md`."
  - "For a deliberately audible, stylized hard-tune effect, push Pitcher's retune speed and correction amount toward their fastest/strongest settings, or use Auto-Tune Pro's Classic Mode per `knowledge_base/vst_database/antares_auto_tune_pro.md`, matching whichever specific intensity the target genre documents rather than defaulting to maximum."
  - "Automate the correction plugin's amount/retune-speed parameter with a Playlist automation clip across the vocal's length, per `knowledge_base/daw/fl_studio/playlist_automation_clips_and_modulation_controllers.md`, easing correction back on phrases that are already in tune and pushing it forward only where pitch actually drifts, rather than leaving one uniform setting for the whole take."
  - "Sequence any de-essing, compression, or EQ after the pitch-correction pass is finalized, per the corrective-first ordering documented in `knowledge_base/mixing/vocal_processing/vocal_chain_signal_order.md`, since pitch correction changes the vocal's harmonic content in ways that affect how subsequent EQ and de-essing decisions should be made."
related_plugins:
  - "FL Studio Playlist"
  - "Edison"
  - "Newtone"
  - "Pitcher"
  - "celemony_melodyne"
  - "antares_auto_tune_pro"
tags:
  - "fl-studio"
  - "vocal-tuning"
  - "comping"
  - "pitch-correction"
  - "newtone"
  - "pitcher"
  - "recording"
  - "workflow"
---

# FL Studio Vocal Tuning and Comping Pipeline

Pitch-correcting a vocal before it's comped is a common but costly ordering mistake: correction plugins analyze pitch content per-take, and a comp built from several separately-corrected takes tends to carry small, inconsistent pitch-detection artifacts at every splice point that a comp built from one already-corrected performance doesn't. This entry documents the correct order — comp first, then correct — and the FL Studio-specific plugin chain for the correction stage itself, building directly on the comping mechanics already documented in `knowledge_base/daw/fl_studio/recording_and_audio_editing_workflow.md`.

## Comp before correcting

Follow the comping workflow in `knowledge_base/daw/fl_studio/recording_and_audio_editing_workflow.md` to completion first: audition each take lane, cut the strongest phrases and syllables from across all of them onto a single comp track, and crossfade or trim every splice point so the transitions are inaudible. Only once that comp is finished and rendered or consolidated into a single continuous audio clip should a pitch-correction plugin be inserted. Comping after correction means re-correcting (or worse, leaving uncorrected) whatever new material gets pulled into the comp on a later pass, and it means the correction plugin's pitch analysis is being run separately on however many take lanes contributed to the final comp instead of once on the finished performance.

## Choosing transparent or stylized correction

Before reaching for a specific plugin, decide which of the two fundamentally different goals `knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md` documents actually applies: a transparent, "flawless" correction that shouldn't announce itself as processing, or a deliberately audible, stylized hard-tune effect used as a melodic and textural device in its own right. This decision, not a fixed default setting, is what should drive every subsequent choice in the chain.

## FL Studio's native pitch-correction tools

FL Studio ships two distinct native pitch-correction plugins built for different workflows, and confusing them is the most common mistake in this pipeline. Newtone is a graphical, analysis-then-edit pitch and time manipulation editor — it displays detected notes as editable blocks with a Center control (global correction toward the nearest pitch) and a Variation control (governing how much natural vibrato and pitch drift survive the correction), making it FL Studio's equivalent to the Melodyne workflow documented in `knowledge_base/vst_database/celemony_melodyne.md`: precise, note-by-note, after-the-fact editing rather than a real-time effect. Pitcher, by contrast, is a real-time pitch-correction, manipulation, and harmonization plugin that can be driven under MIDI control from a keyboard or the Piano roll — it's built for tracking-time or performance-style correction and harmony generation, the same real-time role `knowledge_base/vst_database/antares_auto_tune_pro.md`'s Auto Mode plays. For projects that already license Melodyne or Auto-Tune Pro directly, those plugins slot into the same two roles (Melodyne matching Newtone's graphical editing approach, Auto-Tune Pro matching Pitcher's real-time correction) rather than requiring a different pipeline.

## Setting the correction intensity

For a transparent result, keep Newtone's Center amount moderate rather than pushed to 100%, preserving enough of each note's natural pitch drift that the correction doesn't read as processed, and keep Pitcher's retune speed backed off from its fastest setting for the same reason. For a stylized, audible hard-tune effect, push retune speed and correction amount toward their fastest and strongest settings — in Auto-Tune Pro specifically, Classic Mode reproduces the original hard-tune character some genres document as a specific, named sonic signature rather than simply "more correction." Match the target genre's documented intensity rather than defaulting to either extreme; `knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md` documents this as a real spectrum, not a binary on/off choice.

## Automating correction amount across the phrase

A single uniform correction setting for an entire vocal take is rarely correct even within one genre's chosen philosophy, since real performances drift in and out of tune unevenly across a phrase. Automate the correction plugin's amount or retune-speed parameter with a Playlist automation clip, per `knowledge_base/daw/fl_studio/playlist_automation_clips_and_modulation_controllers.md`: ease the correction back (or bypass it entirely) on phrases that are already accurately sung, and bring it up only where pitch genuinely drifts or where the stylized effect is specifically wanted (an ad-lib, a hook line). This keeps correction from flattening the expressive pitch movement in a performer's best-sung phrases while still fixing the phrases that actually need it.

## Sequencing correction relative to the rest of the vocal chain

Once pitch correction is finalized, move on to de-essing, compression, and EQ, per the corrective-first ordering `knowledge_base/mixing/vocal_processing/vocal_chain_signal_order.md` documents for genres that treat pitch correction as an early, foundational step: correcting the lead vocal's pitch before any harmony stacking or doubling avoids compounding pitch errors across every stacked take built from it, and finalizing pitch content before EQ/de-essing means those later decisions are being made against the vocal's actual final harmonic content rather than content that's about to shift under correction.

## Common mistakes

Pitch-correcting individual take lanes before comping, which produces a comp with small, inconsistent correction artifacts at every splice rather than one coherent, evenly-corrected performance. Confusing Newtone's graphical, after-the-fact editing role with Pitcher's real-time performance role and reaching for the wrong one — Newtone for precise note-by-note work, Pitcher for MIDI-controlled real-time correction and harmonization. Applying one uniform correction amount across an entire vocal take instead of automating it phrase by phrase, which either over-processes already-accurate phrases or under-corrects the ones that actually drift. Running EQ and de-essing before pitch correction is finalized, then having to redo those decisions once the corrected vocal's harmonic content changes.
