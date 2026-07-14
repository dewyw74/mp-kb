---
genre_name: "Video Game Score"
parent_genre: "Cinematic"
origin:
  era: "1970s (Chiptune) to present"
  geographic_origin: "Japan, United States, Europe"
influences:
  - "Film Score"
  - "Chiptune / 8-bit Music"
  - "Electronic / Ambient"
  - "Classical and Romantic Orchestral"
related_genres:
  - "Film Score"
  - "Synthwave"
  - "Ambient"
  - "Heavy Metal (e.g., the DOOM soundtrack)"
musical_characteristics:
  tempo_range: "Variable (60-160+ BPM depending on gameplay state)"
  time_signatures: ["4/4", "Complex odd meters (5/4, 7/8) used frequently for boss battles"]
  common_keys: ["C minor", "D minor", "E minor"]
  common_scales: ["Dorian", "Phrygian", "Major", "Harmonic Minor"]
  chord_progressions:
    - "Highly dependent on the tone of the game."
    - "Often relies on vamps (repeating 2 or 4 bar loops) that can loop endlessly without causing listener fatigue."
    - "I - bVI - bVII (The 'Heroic' progression)"
  melodic_characteristics: "Melodies must be incredibly memorable (leifmotifs) but designed so they do not become annoying after hours of looping playback. They are often highly rhythmic and syncopated."
tempo_range: "Variable"
common_keys: ["C minor", "D minor", "E minor"]
arrangement:
  song_structure: ["Adaptive/Interactive loops", "Intro", "A section", "B section", "Loop point"]
  intro: "Sets the immediate atmosphere of the level."
  verse: "N/A. Instead, 'Exploration' loops provide ambient, low-tension background music."
  build: "Often handled by the game engine (middleware like Wwise/FMOD) crossfading from a quiet track to a loud, dense track when an enemy appears."
  drop_chorus: "The 'Combat' or 'Boss Battle' state. High intensity, fast tempos, and heavy orchestration."
  bridge: "Often a separate, transitional audio file triggered by crossing a threshold in the game."
  outro: "Usually absent in gameplay music (it must loop seamlessly). Dedicated 'Victory' or 'Level Clear' stings serve as the outro."
instruments:
  drums: "Ranges from orchestral percussion (Timpani, Taiko) to electronic drum machines, to heavy metal acoustic kits."
  bass: "Synthesizers, electric bass, or orchestral contrabasses depending on the aesthetic."
  synths: "Fundamental to the genre. Even massive orchestral game scores often layer modern synthesizers to provide a unique, interactive texture."
  guitars: "Acoustic guitars used for emotional themes (e.g., The Last of Us). Heavily distorted 8-string electric guitars used for aggressive combat (e.g., Mick Gordon's DOOM)."
  keys: "Pianos are frequently used for emotional, narrative-driven moments."
  orchestration: "Modern AAA games utilize massive, live symphony orchestras recorded at legendary studios (Abbey Road, AIR Lyndhurst), often augmented with esoteric world instruments or modular synthesizers."
sound_design:
  synth_types: ["All types. Chiptune (Square/Triangle waves) for retro aesthetics; modern Modular Synthesis for cutting-edge sci-fi."]
  oscillators: ["N/A"]
  filters: ["N/A"]
  modulation: ["N/A"]
  effects: ["Heavy use of digital reverbs and delays."]
  processing: ["Interactive processing. The music is often processed in real-time by the game engine (e.g., applying a low-pass filter to the music when the player goes underwater)."]
midi_programming:
  bass_patterns: "Often programmed as seamless, endlessly repeating ostinatos."
  drum_patterns: "Combat loops require driving, energetic, and highly syncopated rhythms."
  melody_patterns: "Melodies must be programmed to flow seamlessly back into themselves at the loop point."
  velocity: "Careful velocity programming is required to maintain the emotional intent over long periods of time."
  humanization: "High humanization for orchestral elements to prevent listening fatigue. Electronic/retro scores rely on strict quantization."
mixing:
  eq_approach: "The music must be mixed to leave room for Dialogue and Sound Effects (explosions, footsteps). The midrange is often gently scooped, and the master volume is kept relatively low compared to commercial music."
  compression: "Moderate. The music must be punchy but cannot completely crush the dynamic range of the overall game audio mix."
  reverb: "Often kept slightly drier than film scores to allow the game engine to apply its own environmental reverbs (e.g., if the player walks into a cave, the game engine adds cave reverb to the dry music)."
  delay: "Used creatively for spatial effects."
  stereo_imaging: "Wide, but must not interfere with the spatial positioning of important gameplay sound cues (e.g., an enemy sneaking up from the left)."
  automation: "Volume automation is often handled by the game engine via audio middleware (Wwise, FMOD), dynamically adjusting the levels based on player actions."
mastering:
  target_loudness: "-23 to -14 LUFS integrated (Depends entirely on the audio standards of the specific platform, e.g., Sony/Microsoft standards)"
  dynamics: "Highly dynamic. Mastering for games requires adhering to strict LUFS standards to ensure the music, dialogue, and sound effects sit perfectly together without blowing out the player's speakers."
  frequency_balance: "Balanced and clear. Extreme sub-bass or piercing highs can interfere with critical gameplay audio cues."
reference_artists:
  important_artists:
    - "Koji Kondo (Super Mario, Zelda)"
    - "Nobuo Uematsu (Final Fantasy)"
    - "Mick Gordon (DOOM)"
    - "Gustavo Santaolalla (The Last of Us)"
    - "Jesper Kyd (Assassin's Creed)"
  reference_tracks:
    - "Koji Kondo - 'Super Mario Bros. Theme' (The masterpiece of Chiptune melody)"
    - "Nobuo Uematsu - 'One-Winged Angel' (Epic Orchestral/Choral Boss Theme)"
    - "Mick Gordon - 'BFG Division' (Industrial Synth/Metal Fusion)"
    - "Gustavo Santaolalla - 'The Last of Us Theme' (Minimalist Acoustic)"
production_notes:
  professional_tips:
    - "The Golden Rule of Game Audio: The music must loop perfectly. Ensure your reverb tails and delay lines at the end of the track carry over seamlessly to the beginning of the track."
    - "Write in 'Stems'. A modern combat track is not a single audio file; it is usually 4 or 5 stems (Percussion, Bass, Strings, Brass) that the game engine fades in and out dynamically based on how many enemies are attacking."
    - "Melody is incredibly important in gaming. A great video game theme (like Zelda or Halo) becomes deeply embedded in the player's memory because they hear it for dozens of hours. Make your themes singable."
  common_mistakes:
    - "Writing music that is too dense or distracting. If your 'Exploration' music has a massive, distracting brass melody, it will annoy the player after 10 minutes. Save the massive melodies for the boss fights."
    - "Failing to account for the loop point. A noticeable 'click' or a sudden drop in reverb when the music loops will instantly break the player's immersion."
    - "Over-mastering. If you master your game music to -8 LUFS (like a pop track), it will completely drown out the dialogue and sound effects. Master to the game's specific audio standard (often -14 or -23 LUFS)."
  modern_production_techniques:
    - "Using audio middleware (FMOD, Wwise) to create complex, interactive music systems where the tempo, key, and instrumentation change dynamically based on the player's health, location, or actions."
    - "Generative music: Using algorithms or modular synthesizers to create ambient music that never repeats the exact same way twice, preventing listener fatigue during 100+ hour open-world games."
tags: ["cinematic", "video-game", "interactive", "looping", "orchestral", "chiptune"]
---

## History

Video Game music has evolved more drastically than any other genre over the last 40 years. It began in the 1970s and 80s as "Chiptune" (e.g., Koji Kondo's *Super Mario*), constrained by the extreme physical limitations of early computer chips that could only play 3 or 4 simple waveforms (square, triangle, noise) simultaneously. In the 90s, CD-ROMs allowed for pre-recorded audio, bringing lush synthesizers and early orchestral samples to games like *Final Fantasy*. Today, AAA video game scores (like *God of War* or *The Last of Us*) feature massive live orchestras, complex modular synthesis, and production budgets rivaling Hollywood blockbusters.

## Music Theory

The theory behind game music varies wildly depending on the aesthetic. However, a unifying principle is the mastery of the "Vamp"—a short, repeating chord progression that maintains a specific emotional state (tension, wonder, fear) without ever fully resolving, allowing the music to loop endlessly while the player explores. Modes (Dorian, Lydian) are heavily used to create specific atmospheres.

## Arrangement

Video Game arrangement is fundamentally different from linear music. It is "Interactive." Composers do not just write a 3-minute song; they write a musical "system." A track might consist of an "Ambient" loop (just quiet strings), a "Suspense" loop (adding ticking percussion), and a "Combat" loop (adding massive brass and heavy drums). The game engine seamlessly crossfades between these loops based on the player's actions.

## Instruments

The instrumentation is limitless. It ranges from pure 8-bit sine waves, to solo acoustic guitars, to 100-piece symphony orchestras, to heavily distorted 8-string electric guitars (as popularized by Mick Gordon's groundbreaking *DOOM* soundtrack). The genre frequently blends all of these elements together.

## Sound Design

Sound design and music composition are deeply intertwined in game audio. Composers often create unique, custom sound palettes (like recording the sound of striking a rusted oil barrel and pitching it down into a massive percussion instrument) to give a specific game world a unique sonic identity. 

## MIDI Programming

Programming is the core of game music production. Even when utilizing live orchestras, the interactive nature of the music requires composers to program complex, tempo-synced mockups in their DAWs. MIDI must be meticulously organized into "Stems" (separate tracks for percussion, bass, harmony, and melody) so the game engine can manipulate them individually.

## Mixing

A game score cannot be mixed in a vacuum. It must be mixed to leave room for the game's Sound Effects (SFX) and Dialogue (VO). The midrange is often carefully managed to ensure the characters' voices remain intelligible. Reverb is often kept relatively tight, allowing the game engine's environmental audio system to apply spatial reverb dynamically.

## Mastering

Mastering for video games requires adhering to strict loudness standards (often measured in LUFS). Unlike commercial music, which is often crushed with limiters to sound as loud as possible, game music is mastered to a specific, lower target (e.g., -14 LUFS for mobile, -23 LUFS for console) to ensure a balanced, highly dynamic mix where explosions are significantly louder than the background music.

## Reference Artists

Koji Kondo (Nintendo) is the godfather of the genre, proving that unforgettable melodies could be written with only 3 square waves. Nobuo Uematsu (*Final Fantasy*) brought epic, progressive rock and Romantic orchestral sensibilities to gaming. Modern composers like Mick Gordon (*DOOM*), Jesper Kyd (*Assassin's Creed*), and Gustavo Santaolalla (*The Last of Us*) have pushed the medium into cutting-edge electronic, historical, and minimalist acoustic territories.

## Production Notes

The most important technical skill for a game composer is mastering the perfect loop. Your music will be heard by a player for hours at a time. It must loop without any audible clicks or pops, and the reverb tail from the end of the track must seamlessly carry over to the beginning. Emotionally, your music must set the perfect tone without becoming distracting. A great game score is an invisible emotional engine that drives the gameplay experience.
