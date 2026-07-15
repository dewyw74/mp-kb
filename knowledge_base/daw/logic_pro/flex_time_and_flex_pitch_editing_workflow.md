---
workflow_name: "Logic Pro Flex Time and Flex Pitch Editing Workflow"
daw: "logic_pro"
category: "editing"
goal: "Use Logic's Flex Time to correct and reshape audio timing without warp markers in the Ableton sense, and use Flex Pitch to correct or reshape individual notes directly on a monophonic audio waveform."
steps:
  - "Enable Flex on the track (Track > Flex or the Flex button in the track header) so Logic analyzes the region for transients before any editing begins."
  - "Choose a Flex Time algorithm that matches the source material: Monophonic for solo vocals or bass/melody lines, Polyphonic for chords and complex mixes, Slicing for drums and percussive material, Rhythmic for guitars/keys/Apple Loops that should loop-fill gaps, Speed or Tempophone for deliberate stretch artifacts."
  - "Drag a detected transient to a new position to create a Flex marker, which locally compresses or expands the audio around that point without moving or crossfading the whole region by hand."
  - "Add a Flex marker just before and after a section that should stay untouched, pinning it in place while timing around it is adjusted."
  - "Use Quantize on flexed audio to snap transients to the grid the same way MIDI would be quantized, now that Flex has made the audio's timing editable."
  - "Switch the track view to Flex Pitch (in the Audio Track Editor) for monophonic sources — vocals, bass, solo instruments — once Flex has segmented the recording into individual note bars."
  - "Drag a note bar vertically to correct its pitch, or use the Pitch Correction slider with a chosen Scale Quantize key to snap a whole take toward a target scale."
  - "Adjust Vibrato amount per note (reduce toward flat/robotic, increase for wider pitch variation) and adjust Gain per note directly in the pitch editor."
  - "Use Formant Shift in the Inspector when a note is transposed more than three to four semitones, shifting formants in the opposite direction of the pitch change to avoid an unnatural, chipmunked or overly deep character."
  - "Bounce or flatten only once the take is finished — Flex edits stay non-destructive and are recalculated in real time during playback until then."
related_plugins:
  - "Logic Pro Flex Time"
  - "Logic Pro Flex Pitch"
  - "Logic Pro Audio Track Editor"
  - "Celemony Melodyne"
  - "Antares Auto-Tune Pro"
tags:
  - "logic_pro"
  - "flex-time"
  - "flex-pitch"
  - "editing"
  - "vocal-tuning"
  - "time-stretching"
  - "quantize"
---

# Logic Pro Flex Time and Flex Pitch Editing Workflow

Flex Time and Flex Pitch are Logic's built-in tools for reshaping the timing and pitch of recorded audio without external plug-ins. They share a mechanism with Ableton's Warp in that both analyze audio and let the engine time-stretch it in real time, but the actual editing model differs: Logic works from Flex markers placed at (or near) detected transients rather than warp markers freely placed anywhere along a waveform, and Flex Pitch adds a genuinely distinct capability — per-note pitch and formant editing directly on the waveform — that Ableton's Warp does not include at all.

## How Flex Time actually works

Enabling Flex on a track tells Logic to analyze the audio for transients; detected transients are marked automatically. Dragging one of those transients to a new position creates a Flex marker and locally compresses or expands the audio around it, without manually trimming, moving, nudging, or crossfading regions by hand. Placing a Flex marker just before and after a passage effectively pins that passage in place while the surrounding material is stretched to fit.

Logic offers six Flex Time algorithms, and picking the right one matters more than in a generic warp-everything workflow:

- **Monophonic**: solo vocals, bass lines, single-note melodic instruments.
- **Polyphonic**: chords and complex mixes, using phase vocoding — the most CPU-intensive algorithm but the highest quality for polyphonic material.
- **Slicing**: cuts audio at transients and shifts each slice at its original speed with no stretching, best for drums and other percussive material.
- **Rhythmic**: stretches material and loops audio between slices to fill gaps, suited to rhythmic guitars, keyboard parts, and Apple Loops.
- **Speed**: a specialized stretch process for material that doesn't fit the other categories cleanly.
- **Tempophone**: a deliberately audible, tape-based-style stretch effect rather than a transparent correction tool.

Once a region is flexed, its timing becomes editable the same way MIDI timing is: transients can be quantized to the grid, nudged individually, or left as Flex markers for manual placement.

## How Flex Pitch actually works

Flex Pitch is available per track in the Audio Track Editor and works on monophonic material — vocals, bass, or any single-note source. Once enabled, Logic segments the recording into individual notes and displays them as movable bars on a pitch grid, visually similar to a piano roll but generated directly from the audio's detected pitch content.

Each note bar can be dragged vertically to correct its pitch, or the whole take can be pulled toward a target scale using the Pitch Correction slider together with a chosen Scale Quantize key. Per note, Gain can be adjusted directly in the editor, and Vibrato amount can be reduced toward a flat/robotic tone or increased for a wider natural variation. Formant Shift, available in the Inspector when a note is selected, matters most on larger pitch moves: shifting a note more than three to four semitones without compensation makes formants shift along with the pitch, producing an unnatural chipmunked or artificially deep result — shifting formants in the opposite direction of the pitch change corrects for this.

Both Flex Time and Flex Pitch are non-destructive: the original audio file is never altered, and edits are recalculated in real time on playback, so they can be disabled or adjusted at any point without losing the source take.

## Where this fits next to dedicated tuning tools

Flex Pitch covers most single-take vocal tuning and correction needs without leaving Logic, but for heavier polyphonic pitch editing or more surgical formant work, a dedicated tool like Celemony Melodyne remains the deeper option — see `knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md` for the broader philosophy of how much correction is appropriate before a performance starts sounding processed.

## Common mistakes

Using the Polyphonic algorithm on a solo vocal or bass line out of habit, which costs CPU for no quality benefit when Monophonic would track the material more accurately. Applying Flex Pitch's Scale Quantize aggressively across an entire take without per-note review, which can snap intentional blue notes or expressive pitch bends onto the nearest scale tone. Transposing a note significantly in Flex Pitch and skipping Formant Shift, leaving an audibly unnatural timbre. Forgetting that Flex edits are calculated live on playback — heavy Flex use across many tracks can add up in CPU load on a large session even though no audio has actually been rendered yet.
