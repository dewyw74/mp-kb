---
title: "Foley for Cinematic and Game Sound Design"
technique: "Object-recording and adaptive-audio foley practices specific to picture and interactive media"
tags:
  - "foley"
  - "sound-design"
  - "video-game-audio"
  - "cinematic"
  - "interactive-audio"
  - "sampling"
---

# Foley for Cinematic and Game Sound Design

`knowledge_base/sound_design/sampling/field_recording_and_foley_integration.md` covers field recording and foley as a general music-production texture and percussion source across genres (industrial techno, dark ambient, post-rock). This entry covers a narrower, deeper application specific to scoring for picture and interactive media: recording objects specifically to become designed instruments for a fictional world's identity, and the production constraints (mixing against dialogue/SFX, building adaptive/interactive audio) unique to that context. Genre files consulted for grounding: `knowledge_base/genres/cinematic/video_game_score.md`, `sci_fi_score.md`, `horror_score.md`.

## Recording Real Objects to Build a World's Instrument Palette

`video_game_score.md` documents the clearest example of foley functioning as sound-design *composition* rather than atmosphere: "Sound design and music composition are deeply intertwined in game audio. Composers often create unique, custom sound palettes (like recording the sound of striking a rusted oil barrel and pitching it down into a massive percussion instrument) to give a specific game world a unique sonic identity." This differs in kind from the general music-production foley technique documented in `field_recording_and_foley_integration.md`: the goal isn't adding one textural or percussive element to an otherwise-conventional arrangement, it's building a game or film's entire signature percussion voice from one deliberately chosen, heavily processed object recording, so that the resulting instrument itself becomes part of the world's identifiable sonic branding.

## Sound Design Serving a Malfunction/Technological Narrative

`sci_fi_score.md` documents foley-adjacent sound design used for a specific narrative function distinct from `video_game_score.md`'s world-identity instrument-building: "Glitch, bitcrush, and granular processing for technological/malfunction sound design," deployed alongside the genre's hybrid orchestral-electronic scoring specifically to signal "alien" or "technological" narrative content as distinct from "human" orchestral content. Here, processed sound-design material (which can include foley-sourced or synthesized origins) is doing a specific storytelling job — marking a scene or object as non-human or malfunctioning — rather than establishing a persistent instrumental identity the way the oil-barrel percussion example does.

## Infrasound and Processed Field Recording for Physical Effect

`horror_score.md` documents a third distinct cinematic application: physically-targeted, rather than melodically or texturally targeted, sound design — "layer processed field recordings and infrasound (very low, near-inaudible frequency content) with orchestral drones for a physically unsettling low-end presence." This use case aims at the audience's physical/visceral response (a felt, barely-heard low-end pressure) rather than at building a recognizable instrument or signaling a narrative event, distinguishing it from both of the above cinematic/game foley applications.

## Mixing Foley/Sound Design Against Dialogue and SFX

Both cinematic and game contexts impose a mixing constraint that general music production doesn't share: sound-design and score material must leave room for dialogue and other sound effects rather than filling the entire frequency and dynamic range themselves.

- `video_game_score.md` states this directly: "A game score cannot be mixed in a vacuum. It must be mixed to leave room for the game's Sound Effects (SFX) and Dialogue (VO). The midrange is often carefully managed to ensure the characters' voices remain intelligible. Reverb is often kept relatively tight, allowing the game engine's environmental audio system to apply spatial reverb dynamically." The same file's EQ notes add that "the midrange is often gently scooped, and the master volume is kept relatively low compared to commercial music" specifically so foley-derived and musical elements alike don't fight the game's other audio layers.
- This is a structurally different mixing goal from the general music-production foley/field-recording use documented in `field_recording_and_foley_integration.md`, where the recorded material is typically a lead or co-lead element in the mix rather than one layer among score, dialogue, and SFX competing for the same space.

## Interactive/Adaptive Audio as a Structural Constraint on Foley Use

`video_game_score.md` documents a production requirement with no equivalent in film or general music production: "Interactive processing. The music is often processed in real-time by the game engine (e.g., applying a low-pass filter to the music when the player goes underwater)," built from "Stems (separate tracks for percussion, bass, harmony, and melody) so the game engine can manipulate them individually." Foley-derived percussion instruments (like the pitched oil-barrel hit) built for a game score need to be delivered and organized as manipulable stems specifically because the game engine — not a fixed mix — determines final playback processing and layer balance in real time, using middleware such as FMOD or Wwise per the file's production notes.

## Common Mistakes

**Treating game/film foley sound design as identical to general music-production field recording.** The mixing constraints (leaving headroom for dialogue/SFX) and delivery requirements (stems for interactive processing) documented above are specific to picture and interactive media and don't apply to a standalone track's field-recording use.

**Building a foley-derived instrument without considering its narrative or world-identity function.** `video_game_score.md`'s oil-barrel example works because the resulting sound becomes a recognizable, reused element of the game's sonic identity — a one-off foley hit used once carries much less of this world-building value.

**Mastering game or film score material as if it were a standalone commercial release.** `video_game_score.md` explicitly warns that mastering game music too loud "will completely drown out the dialogue and sound effects," naming -14 or -23 LUFS as typical game-specific targets rather than a pop-release loudness target.

## Cross-References

- `knowledge_base/sound_design/sampling/field_recording_and_foley_integration.md` — the general music-production application of field recording and foley this entry's cinematic/game-specific practices build on and diverge from.
- `knowledge_base/genres/cinematic/video_game_score.md` — custom object-recording sound design, stem-based interactive audio delivery, and SFX/dialogue-aware mixing.
- `knowledge_base/genres/cinematic/sci_fi_score.md` — glitch/bitcrush/granular sound design for technological/malfunction narrative signaling.
- `knowledge_base/genres/cinematic/horror_score.md` — infrasound and processed field recordings for physically unsettling effect.
- `knowledge_base/mastering/loudness/lufs_targets_by_genre.md` — general loudness/LUFS mastering context, distinct from the game-specific LUFS targets `video_game_score.md` documents.
