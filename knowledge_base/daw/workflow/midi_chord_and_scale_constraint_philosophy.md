---
workflow_name: "MIDI Chord and Scale Constraint Tool Philosophy"
daw: "generic"
category: "midi"
goal: "Use chord-generator and scale-locking MIDI tools to accelerate finding a good harmonic idea without letting the tool's defaults quietly flatten every progression into the same generic shape, and know when to turn the constraint off so a promising idea can be developed freely."
steps:
  - "Reach for a chord-generator or scale-lock tool to explore options quickly when starting from harmonic uncertainty, not as a permanent authoring method for every part in the track."
  - "Set the scale or key deliberately based on the genre/mood decision already made, rather than accepting whatever default the tool loads with."
  - "Generate multiple chord-progression candidates in one pass and audition them against the track's existing bass or drum pattern, not in isolation, since a progression that sounds generic solo can still be the right harmonic bed under a strong melodic or rhythmic part."
  - "Treat every generated progression as a draft, not a finished part — hand-edit voicings, inversions, and voice-leading once a progression is chosen rather than keeping the tool's raw output."
  - "Watch for the specific generic-progression patterns a given tool defaults to (a stock I-V-vi-IV shape, root-position triads with no inversions, identical rhythm on every chord) and deliberately break at least one of them once a progression is selected."
  - "Turn scale-lock off as soon as a promising idea is found, rather than leaving it engaged through the entire writing and editing process, so passing tones, chromatic movement, and deliberate out-of-scale notes remain possible."
  - "Use scale-lock's real strength — preventing accidental wrong notes during fast idea capture or live performance input — rather than treating it as a harmony-writing tool in its own right."
  - "Cross-check a generated progression against the genre's actual harmonic conventions (per the relevant `knowledge_base/music_theory/` or `knowledge_base/genres/` entry) rather than assuming the tool's output is stylistically appropriate by default."
  - "Save a chord tool's output as a starting sketch in the arrangement, then continue developing the part with normal piano-roll editing rather than re-running the generator repeatedly hoping for a better result."
  - "Recognize when a generated progression is being kept only because regenerating feels like more work than editing — that's a signal to hand-edit rather than a signal the progression is actually right."
related_plugins: []
tags:
  - "midi"
  - "chord-generator"
  - "scale-lock"
  - "harmony"
  - "workflow"
  - "generic"
---

# MIDI Chord and Scale Constraint Tool Philosophy

Chord-generator and scale-locking MIDI tools solve a real problem: staring at a blank piano roll with no harmonic starting point is slow, and a tool that can propose several playable progressions in a chosen key, or prevent an accidental wrong note during fast idea capture, removes real friction from the early stages of writing. The same tools also have a real failure mode: because they work from a limited set of common chord shapes and default scale choices, leaning on them past the idea-generation stage tends to nudge every user toward the same handful of generic-sounding progressions, and treating scale-lock as a permanent constraint rather than a training-wheel removes exactly the harmonic surprise that makes a progression interesting. This entry covers the DAW-agnostic principles behind using these tools well — as accelerants for finding an idea, not as an authoring method for the finished part. See `knowledge_base/midi/patterns/chord_and_stab_pattern_programming.md` for how chords are then actually programmed once a progression is chosen.

## What These Tools Are Actually Good At

A chord generator's real strength is speed of exploration: given a key and a rough style, it can propose several harmonically valid progressions in seconds, which is useful specifically when the blocker is "I don't know where to start," not when the blocker is "I know what I want but need to refine it." Scale-lock's real strength is different — it's a live-performance and fast-idea-capture safety net, preventing an accidental wrong note from breaking the flow of playing in a new key, especially useful on a controller during quick sketching. Both tools are solving a friction problem, not a taste problem — they can hand a producer a starting point fast, but neither one has any information about what makes a progression distinctive, surprising, or right for a specific track beyond matching a key and a rough genre category.

## Why Generated Progressions Converge on the Generic

Chord generators work from a limited internal vocabulary of common, broadly-applicable chord shapes, because those are the progressions statistically likely to sound acceptable across the widest range of inputs. That's precisely why they tend to produce the same small set of familiar shapes — a I-V-vi-IV-style progression, root-position triads, one chord per bar with no rhythmic variation — regardless of how different two users' intended tracks actually are. None of that is wrong on its own; those shapes are common for a reason. The problem is scale: if every user reaching for the same tool accepts its first or most obvious suggestion, a large share of tracks built with that tool converge on a small set of interchangeable-sounding progressions, even across genres and artists that would otherwise sound distinct. The fix isn't to avoid the tool — it's to treat its output as raw material rather than a finished decision, actively listening for whether the specific progression it proposed is doing anything the track actually needs, or whether it's just the path of least resistance.

## Editing Generated Output Rather Than Keeping It As-Is

A generated progression becomes a specific, track-appropriate part through the same hand-editing any other MIDI part gets: changing voicings and inversions so the chords aren't all root-position, adjusting the rhythm so every chord doesn't hit with identical duration and timing, reharmonizing a chord or two against the melody or bass rather than accepting the generator's default choice at every position, and checking the result against how the target genre actually treats harmonic rhythm and voicing (a generator's default output rarely matches a specific genre's harmonic conventions closely enough to skip this step). This is also where a generated progression earns or fails to earn its place — a progression auditioned against the track's actual bass and drum pattern, rather than in isolation, will often reveal that it needs real editing to sit correctly, even if it sounded fine as an isolated chord loop.

## Disabling the Constraint Once an Idea Is Found

Scale-lock's value is front-loaded: it's most useful during the moment of fast idea capture, and its usefulness drops sharply once a promising idea has actually been found. Leaving it engaged through the rest of the writing and editing process blocks exactly the moves — a passing chromatic tone, a deliberate out-of-scale note for tension, a borrowed chord from a parallel mode — that often turn an acceptable progression into a distinctive one. The tool's job was to protect against wrong notes during exploration; once the idea worth developing has been identified, that protection becomes a limitation rather than a help, and turning it off is a normal, expected part of moving from sketch to finished part rather than a sign the tool failed.

## Common Mistakes

**Keeping scale-lock engaged through the entire writing process instead of just the idea-capture stage.** Its usefulness is front-loaded; past that point it mainly blocks the chromatic and out-of-scale moves that add distinctiveness.

**Accepting a generator's first suggestion without auditioning it against the track's bass and drum pattern.** A progression's fit is often only clear in context, not in isolation.

**Shipping a generated progression with no hand-editing — same voicings, same rhythm, root position throughout.** This is exactly the pattern that makes generator output sound generic and interchangeable across unrelated tracks.

**Re-running the generator repeatedly hoping for a better result instead of editing the one that's already close.** If a candidate progression is close but not quite right, hand-editing it is usually faster and more productive than regenerating from scratch.

**Assuming generated output matches the target genre's harmonic conventions by default.** Generators work from a broad, genre-agnostic vocabulary; check the result against the actual genre's harmonic tendencies rather than assuming a match.

## Cross-References

- `knowledge_base/midi/patterns/chord_and_stab_pattern_programming.md` — how a chosen chord progression is then actually programmed as stabs or sustained pad material.
- `knowledge_base/music_theory/` — genre-appropriate harmonic conventions to check a generated progression against before committing to it.
- `knowledge_base/daw/ableton/racks_macros_and_performance_controls.md` — MIDI Effect Rack context for chord/scale/arpeggiator devices as one implementation of these constraint tools.
