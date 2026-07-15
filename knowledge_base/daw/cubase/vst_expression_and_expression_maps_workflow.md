---
workflow_name: "Cubase VST Expression and Expression Maps Workflow"
daw: "cubase"
category: "midi"
goal: "Program articulation-accurate orchestral and multi-articulation sample-library MIDI in Cubase using Expression Maps and VST Expression — decoupling articulation switching from raw keyswitch notes on the timeline — and use Note Expression correctly for the separate problem of per-note polyphonic modulation."
steps:
  - "Build or import an Expression Map for the loaded instrument (Steinberg ships many for common libraries; Cubase can also import key switches directly from a VST instrument preset) rather than manually typing every articulation by hand where a starting map already exists."
  - "Define each articulation as a Sound Slot in the Expression Map, labeled by its real name (Legato, Staccato, Pizzicato, Tremolo, Sustain, Sforzando) rather than by note number, so the articulation reads correctly in the editor regardless of the library's internal keyswitch layout."
  - "Assign a remote trigger to each Sound Slot — a key switch note or a program change message, per the library's own mechanism — so Cubase knows what to actually send the instrument when that articulation is selected."
  - "Choose Attribute or Direction type per Sound Slot: Attribute affects only the single note it's attached to (for one-off accents like sforzando), while Direction stays active from its insertion point until the next articulation change (for sustained legato or staccato passages)."
  - "Enable VST Expression on the track once the map is assigned, which adds the Articulations/Dynamics controller lane to the MIDI editor — place articulation symbols directly on that lane rather than inserting audible keyswitch notes into the note lane itself."
  - "Rely on Cubase resolving the correct remote trigger at playback regardless of where the playhead starts, since VST Expression sends the articulation continuously rather than requiring the transport to physically pass over a keyswitch note first."
  - "Use Attribute Combinations where the library supports layering more than one articulation property at once (e.g. a dynamic layer plus a playing technique), instead of assuming only one Sound Slot can be active at a time."
  - "Reach for Note Expression instead of VST Expression when the task is per-note, polyphonic modulation on a VST3 instrument — pitch, timbre, or level shaping of individual notes within a chord — since VST Expression operates on articulation switching for the instrument as a whole, not independent per-note control inside a chord."
  - "Save a customized Expression Map back out once tuned for a specific library so the same map can be reused across projects instead of rebuilding sound slots and remote triggers from scratch each time."
  - "Audition articulation transitions in context against the full arrangement before finalizing, since the Attribute/Direction distinction and remote-trigger latency can behave differently once real tempo and note density are present versus an isolated test phrase."
related_plugins:
  - "Native Instruments Kontakt"
  - "Cubase VST Expression"
  - "Cubase Expression Maps"
  - "Cubase Note Expression"
  - "Cubase MIDI Editor"
tags:
  - "cubase"
  - "midi"
  - "expression-maps"
  - "vst-expression"
  - "note-expression"
  - "articulations"
  - "keyswitch"
  - "orchestral"
---

# Cubase VST Expression and Expression Maps Workflow

Expression Maps, driven by Cubase's VST Expression system, are Cubase's signature tool for articulation-switching on multi-articulation sample libraries — orchestral strings, brass, choirs, and similar patches that expose many playing techniques through internal keyswitches or program changes. Introduced with VST Expression in Cubase 5, Expression Maps are best understood as an improved, decoupled version of raw keyswitching: instead of a physical keyswitch note that the playhead must pass over during playback to trigger correctly, the articulation choice lives on its own controller lane and is sent to the instrument continuously and correctly regardless of where playback starts. This is a genuine Cubase differentiator worth using deliberately rather than falling back on manually placed keyswitch notes out of habit from other DAWs.

## Sound Slots: the building block of an Expression Map

An Expression Map is a table of Sound Slots, each representing one articulation (Legato, Staccato, Pizzicato, Tremolo, Sustain, and whatever else the loaded library exposes). Each slot carries a human-readable name and a remote trigger — either a key switch note or a program change message, matching whatever mechanism the underlying sample library actually uses internally. Steinberg ships ready-made Expression Maps for many popular libraries, and Cubase can import key switches directly out of a VST instrument preset to bootstrap a map, so building one from scratch by hand is usually only necessary for a library with no existing map.

## Attribute vs. Direction

Each Sound Slot is typed as either Attribute or Direction, and the distinction changes how long the articulation stays active. An Attribute-type slot affects only the single note it's attached to — appropriate for a one-off accent like a sforzando hit inside an otherwise legato phrase. A Direction-type slot stays active from its insertion point forward until the next articulation change is encountered — appropriate for a sustained playing technique like legato or staccato that should govern every note in a passage until explicitly changed. Getting this assignment wrong is a common source of an articulation "sticking" longer or shorter than intended.

## Why this beats raw keyswitching

With a library's native keyswitches placed directly as MIDI notes, the transport has to physically move across a keyswitch note for the articulation change to register — starting playback mid-phrase, looping a section, or scrubbing the playhead can leave the instrument on the wrong articulation. VST Expression solves this by keeping articulation choices on the dedicated Articulations/Dynamics controller lane in the MIDI editor rather than in the note lane, and resolving the correct remote trigger continuously at playback rather than only at the moment the playhead crosses a note. This is the core practical benefit of using Expression Maps over hand-placed keyswitch notes for any library that has one available.

## Attribute Combinations

Some libraries expose more than one articulation property that can be active simultaneously — for example a dynamic layer and a playing technique layered together. Expression Maps support Attribute Combinations for this case, letting more than one Sound Slot's remote trigger resolve and send together rather than forcing a single flat list of mutually exclusive articulations.

## Note Expression: a different problem entirely

Note Expression is a separate Cubase feature and should not be conflated with VST Expression. Where VST Expression switches which articulation an instrument as a whole is playing, Note Expression addresses per-note, polyphonic modulation on VST3 instruments — editing pitch, timbre, or level independently for each note inside a chord, using the VST3-specification controller type introduced for exactly this purpose. Use VST Expression for articulation switching on orchestral and multi-articulation libraries; use Note Expression when the requirement is independent per-note shaping within a polyphonic passage on a VST3 instrument that supports it (Steinberg's own HALion and Padshop are common examples).

## Common mistakes

Placing a library's raw keyswitch notes directly into the note lane out of habit instead of building an Expression Map, which reintroduces the "playhead must pass the keyswitch" problem Expression Maps exist to solve. Mistyping a Sound Slot as Attribute when it should be Direction (or vice versa), causing an articulation to affect only one note when a whole passage was intended, or to bleed into notes that should have reverted to the previous articulation. Treating VST Expression and Note Expression as interchangeable — they solve different problems and neither substitutes for the other. Building a new Expression Map by hand for a library that already ships one, or that already exposes importable key switches from its own preset.

Related reading: `knowledge_base/vst_database/native_instruments_kontakt.md` for the sample-library engine most Expression Map workflows are built around, `knowledge_base/daw/ableton/orchestral_and_strings_midi_programming_workflow.md` for the cross-DAW orchestral-programming principles (velocity layering, legato overlap, CC1/CC11 expression) that apply alongside Expression Maps in Cubase, and `knowledge_base/midi/programming/velocity_editing_and_dynamics.md` for the general velocity-programming discipline this workflow builds on.
