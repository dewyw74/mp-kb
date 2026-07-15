---
workflow_name: "Ableton Vocal Comping-Then-Tuning Pipeline Workflow"
daw: "ableton"
category: "recording"
goal: "Establish the correct order of operations for a lead vocal in Ableton — comp the best take first, then pitch-correct only the finished comp — and automate correction amount/retune speed across a phrase rather than applying one uniform correction setting to the whole vocal."
steps:
  - "Record and comp the lead vocal to a single finished take first, using Take Lanes per `knowledge_base/daw/ableton/multitrack_recording_and_take_comping_workflow.md`, before any pitch-correction plugin is inserted."
  - "Consolidate the comped take into one clean audio clip (per `knowledge_base/daw/ableton/routing_resampling_and_freezing.md`) so the pitch-correction plugin analyzes one continuous performance rather than a set of unconsolidated take-lane fragments."
  - "Decide whether the vocal needs transparent, corrective-only pitch correction or a deliberately audible, stylized effect, per `knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md`, before choosing settings for either tool."
  - "For a corrective-first approach, insert Celemony Melodyne (`knowledge_base/vst_database/celemony_melodyne.md`) on the comped clip and correct pitch note-by-note toward the nearest scale tone while preserving each note's natural vibrato and pitch drift, rather than snapping every note to dead-center pitch."
  - "For a stylized or 'polish' pass, insert Antares Auto-Tune Pro (`knowledge_base/vst_database/antares_auto_tune_pro.md`) after Melodyne in the chain, following the two-stage sequence documented in `knowledge_base/mixing/vocal_processing/vocal_chain_signal_order.md` — Melodyne for precise correction first, Auto-Tune for the audible or polish pass second — rather than running both tools independently on separate copies of the vocal."
  - "If Auto-Tune Pro alone is sufficient (no Melodyne pass needed), choose Retune Speed and Flex-Tune settings that match the intended transparent-vs-stylized goal from the philosophy decision above, rather than leaving the plugin on its default, most-aggressive setting."
  - "Automate Auto-Tune Pro's Retune Speed (or, in Melodyne, the correction amount applied per note/phrase) across the vocal's arrangement rather than leaving one fixed setting for the whole track, easing correction back on expressive, held, or emotionally important phrases and tightening it on rhythmically precise or hook-heavy phrases."
  - "Automate correction intensity down (or bypass the plugin briefly via automation) on ad-libs, breaths, or deliberately loose phrases where audible correction would flatten the performance's intended character."
  - "Re-audition the fully tuned vocal against the rest of the mix (not soloed) before finalizing correction settings, since a correction amount that sounds right in isolation can read as too mechanical or too loose once the vocal sits against the full arrangement."
  - "Only proceed to de-essing, compression, and reverb (per `knowledge_base/mixing/vocal_processing/vocal_chain_signal_order.md`) once the comped and tuned vocal is finalized, so later dynamics and spatial processing are shaped around the vocal's final pitch content rather than a pre-comp or pre-tune version of it."
related_plugins:
  - "Ableton Take Lanes"
  - "Ableton Arrangement Automation"
  - "Celemony Melodyne"
  - "Antares Auto-Tune Pro"
  - "Ableton Utility"
tags:
  - "ableton"
  - "recording"
  - "vocal-comping"
  - "pitch-correction"
  - "melodyne"
  - "auto-tune"
  - "automation"
  - "take-lanes"
---

# Ableton Vocal Comping-Then-Tuning Pipeline Workflow

A lead vocal's practical order of operations matters as much as the individual tools used on it: comping the best performance together always has to happen before pitch correction is applied, and correction settings should be automated across a phrase rather than applied at one uniform intensity for the whole take. This entry documents that pipeline end to end in Ableton — from Take Lanes through Melodyne and/or Auto-Tune Pro — building on the comping mechanics in `knowledge_base/daw/ableton/multitrack_recording_and_take_comping_workflow.md` and the tool-specific detail in `knowledge_base/vst_database/celemony_melodyne.md` and `knowledge_base/vst_database/antares_auto_tune_pro.md`.

## Why Comping Has to Happen First

Pitch correction — whether Melodyne's graphical note-by-note editing or Auto-Tune's real-time tracking — analyzes and processes a continuous audio performance, so it needs a single finished take to work on, not several overlapping take-lane fragments still being auditioned and swapped. Comp the vocal to completion first, using Take Lanes to solo, audition, and drag the strongest segments from each pass into the main track lane, per `knowledge_base/daw/ableton/multitrack_recording_and_take_comping_workflow.md`. Consolidating the finished comp into a single clean clip (per `knowledge_base/daw/ableton/routing_resampling_and_freezing.md`) before inserting any pitch-correction plugin avoids the specific failure mode of tuning one take's phrase and then discovering a better-performed alternate take existed in another lane the whole time — by the time correction starts, the underlying performance decision should already be locked.

## Choosing Corrective vs. Stylized Correction

Before touching either plugin's controls, decide which side of the transparent-vs-stylized split the vocal actually needs, per `knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md` — a flawless, inaudible pop-vocal correction and a deliberately audible, robotic hard-tune effect are genuinely different production goals, not two settings of the same generic task. This decision determines both which plugin(s) to reach for and which settings to use on them, so it belongs at the start of the tuning pass rather than being decided implicitly by whatever the plugin's default happens to be.

## Plugin Chain Order: Melodyne Then Auto-Tune

Per `knowledge_base/mixing/vocal_processing/vocal_chain_signal_order.md`'s documented two-stage sequence, Melodyne's precise, graphical, note-by-note correction is the foundational first pass, with Auto-Tune Pro's faster, effect-oriented processing applied afterward for either final polish or an audible stylistic layer. In Ableton's device chain this means Melodyne sits earlier on the comped vocal clip's chain than Auto-Tune Pro, not the reverse — correcting the take's underlying pitch accuracy first with Melodyne's DNA-based editing avoids compounding pitch errors into whatever pass Auto-Tune applies afterward. A vocal that only needs one tool can skip the other entirely; the sequencing rule applies specifically when both are used together, per `knowledge_base/vst_database/celemony_melodyne.md`'s citation of this exact chain.

## Automating Correction Amount Across a Phrase

Applying one uniform Retune Speed (or one uniform Melodyne correction amount) across an entire vocal treats every phrase as equally in need of the same intensity of correction, which is rarely true. Automate Auto-Tune Pro's Retune Speed (or the equivalent per-note/phrase correction strength in Melodyne) across the Arrangement so held, expressive, or emotionally central phrases get a slower, gentler pull that preserves natural vibrato and pitch drift, while rhythmically tight or hook-heavy phrases get faster, firmer correction. Ad-libs, breaths, and deliberately loose or raw phrases are good candidates for automating correction intensity down further still, or bypassing the plugin briefly via automation, since audible correction on these moments can flatten exactly the character they were recorded to capture.

## Re-Checking Against the Full Mix

Once correction settings and their automation are in place, re-audition the vocal against the full arrangement rather than soloed, since a correction intensity that sounds right in isolation — either too robotic or too loose — often reads differently once it's sitting against the rest of the mix, per the same in-context-decision discipline documented in `knowledge_base/mixing/eq/soloed_vs_in_context_eqing.md`. Only once the comped and tuned vocal is finalized should the remaining vocal chain (de-essing, compression, reverb) be built on top of it, per `knowledge_base/mixing/vocal_processing/vocal_chain_signal_order.md`, so those later stages are shaped around the vocal's final pitch content rather than a version that will still change.

## Common mistakes

Inserting a pitch-correction plugin before the comp is finished, forcing re-tuning work to be redone (or a good tuning decision to be discarded) every time a better segment is swapped in from another take lane. Reversing the documented Melodyne-then-Auto-Tune order, which risks Auto-Tune's real-time tracking compounding pitch inaccuracies that Melodyne's precise editing would have caught first. Applying one fixed Retune Speed or correction amount to an entire vocal regardless of phrase, producing either an over-corrected, robotic performance on expressive passages or an under-corrected, loose result on rhythmically precise ones. Finalizing correction settings while the vocal is soloed, then discovering the amount reads as wrong once it's actually sitting in the mix.
