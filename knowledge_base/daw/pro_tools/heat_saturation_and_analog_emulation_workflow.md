---
workflow_name: "Pro Tools HEAT Saturation and Analog Emulation Workflow"
daw: "pro_tools"
category: "mixing"
goal: "Use Pro Tools' HEAT (Harmonically Enhanced Algorithm Technology) as a per-track, global analog-emulation stage rather than a conventional insert plugin, applying its Drive/Tone controls and pre/post insert position deliberately instead of leaving default settings on every track."
steps:
  - "Confirm HEAT is available before planning around it: HEAT ships only with Pro Tools and Pro Tools Ultimate subscriptions, not with perpetual licenses or Pro Tools Artist, so a session built with HEAT will not translate to every collaborator's rig."
  - "Enable HEAT on a track using its own toggle at the top of the channel strip rather than inserting it from the plugin menu — HEAT is built into Pro Tools as a global, per-track-enabled stage, not a conventional insert plugin instance."
  - "Use the Pre/Post toggle on each HEAT-enabled channel strip to decide whether HEAT sits first in that track's insert chain (reacting to the raw source) or last (reacting to the signal after EQ/compression/other inserts), since this changes what content is actually driving the saturation."
  - "Turn the Drive control toward its left range for tape-style non-linear distortion, which adds odd harmonics (3rd, 5th, and beyond) as drive increases — this is the more subtle, tape-like character."
  - "Turn Drive toward its right range for a triode-tube-circuit character, which layers in even harmonics on top of the tape-style behavior for a more aggressive, tube-console-like effect."
  - "Use the Tone control to emphasize or de-emphasize high-end richness and detail independently of how much Drive is applied, rather than trying to control brightness through Drive alone."
  - "Expect HEAT's reaction to differ per track, since it responds non-linearly to each track's actual frequency content and dynamic range rather than applying a fixed, predictable amount of coloration — audition each track individually rather than assuming one Drive/Tone setting works everywhere."
  - "Reserve heavier Drive settings for individual elements that benefit from analog grit (drum bus, bass, aggressive vocal) and use lighter settings glue-wide across a mix bus or mix group where transparency still matters more than character."
  - "Compare HEAT's tape-leaning and tube-leaning character against dedicated saturation types using `knowledge_base/mixing/saturation/tape_saturation.md`, `knowledge_base/mixing/saturation/tube_saturation.md`, and `knowledge_base/mixing/saturation/even_vs_odd_harmonic_generation.md` to decide which harmonic profile actually fits the source material."
  - "Bypass HEAT per track (via its own bypass toggle) rather than removing it, so its exact settings are preserved if it's re-enabled later in the mix pass."
related_plugins:
  - "Avid HEAT"
  - "Pro Tools Channel Strip"
tags:
  - "pro-tools"
  - "heat"
  - "saturation"
  - "analog-emulation"
  - "harmonic-distortion"
  - "mixing"
  - "tone-shaping"
---

# Pro Tools HEAT Saturation and Analog Emulation Workflow

HEAT (Harmonically Enhanced Algorithm Technology) is Pro Tools' own answer to the criticism that its signal path is "too pure" compared to an analog console — but unlike a third-party saturation plugin, HEAT is built directly into the channel strip as a global, per-track-enabled stage rather than something inserted from a plugin menu. Understanding that structural difference, along with its Drive/Tone control pair and Pre/Post insert positioning, is what separates deliberate use of HEAT from leaving it on default settings across every track.

## HEAT Is Not a Conventional Insert Plugin

HEAT appears as its own toggle and control pair directly on the channel strip of every track, rather than as a plugin instance chosen from an insert slot. This is a meaningful structural difference from third-party saturation plugins, which have to be explicitly inserted and configured per track; HEAT is present as a built-in stage on every track and simply switched on where wanted. A Pre/Post toggle on each channel strip determines whether HEAT sits first in that track's signal path (reacting to the unprocessed source) or last (reacting to the signal after every other insert has shaped it) — this single toggle changes HEAT's character on a given track as much as the Drive setting does, since it changes what content is actually feeding the saturation stage.

## Drive and Tone

Drive is the core character control, and it behaves asymmetrically across its range: turning it toward the left emulates tape's non-linear distortion, adding odd harmonics (third, fifth, and beyond) as it's pushed further; turning it toward the right adds a second, more aggressive layer of even harmonics modeled on triode-based tube circuits. Tone works independently of Drive, emphasizing or de-emphasizing high-end richness and detail — it's the control to reach for when a track needs more or less top-end presence without changing how much harmonic distortion Drive is adding. For the general distinction between odd- and even-harmonic character that HEAT's Drive range is built around, see `knowledge_base/mixing/saturation/even_vs_odd_harmonic_generation.md`, and for dedicated single-character alternatives, `knowledge_base/mixing/saturation/tape_saturation.md` and `knowledge_base/mixing/saturation/tube_saturation.md`.

## Non-Linear, Per-Track Behavior

HEAT reacts to each track's actual frequency content and dynamic range rather than applying a fixed, predictable amount of coloration regardless of source — this mirrors how a real analog stage behaves, but it also means a Drive/Tone setting dialed in on one track won't necessarily translate to another. Auditioning HEAT per track, rather than copying a setting across a session, is necessary because of this non-linearity, and it's part of why HEAT reads as more "alive" than a fixed-curve saturation algorithm.

## Common mistakes

Treating HEAT like a plugin that needs to be inserted, and missing that it's already present as a channel-strip toggle on every track. Leaving every track's HEAT in the default Pre position without considering whether Post (after the track's other inserts) would actually suit that track's processing chain better. Copying one track's Drive/Tone setting onto every other track in the session and expecting the same result, when HEAT's non-linear response means the same numbers sound different on different source material. Pushing Drive hard on a mix bus or glue point where transparency was actually the goal, when a lighter setting or a dedicated saturation plugin from `knowledge_base/mixing/saturation/saturation_as_mix_glue.md` would fit the mix-bus role better.
