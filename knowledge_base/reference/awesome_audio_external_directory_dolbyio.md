---
title: "External Directory: DolbyIO/awesome-audio"
source_url: "https://github.com/DolbyIO/awesome-audio"
tags:
  - "external-resource"
  - "tool-directory"
  - "audio-apis"
  - "audio-analysis"
  - "audio-datasets"
  - "developer-tools"
  - "reference"
---

# External Directory: DolbyIO/awesome-audio

[DolbyIO/awesome-audio](https://github.com/DolbyIO/awesome-audio) is a third, differently-scoped sibling to the other two entries in this folder. Where `awesome_music_production_external_directory.md` covers end-user music-production software/hardware and `awesome_music_external_directory_noteflakes.md` leans toward audio-programming infrastructure, this list is developer/API-centric — organized around *how-to* problems (analyze, edit, playback, record, send real-time, transcribe, visualize audio) rather than around tool categories, plus Dolby.io's own commercial APIs alongside open-source alternatives. This entry is a snapshot pointer, not a mirror — the linked repo updates independently of this project, so treat the live URL as the source of truth and refetch it rather than assuming this snapshot stays current.

## When to use this

Consult this doc (or refetch the live URL) when a task needs programmatic audio processing — analysis, real-time streaming, transcription, format conversion, platform-specific recording/playback SDKs (Android/iOS/Swift) — rather than a DAW, VST, or production technique. This is the most "build a feature that touches audio" oriented of the three reference entries; the other two are more "find a tool to make music with."

## Full Category Map

- **Code** (organized by how-to problem): How-To Analyze Audio, How-To Edit Audio, How-To Playback Audio, How-To Read and Write Audio Files, How-To Record Audio, How-To Send Real-Time Audio, How-To Transcribe Audio into Text, How-To Visualize Audio
- **Community** (Social Forums)
- **Education** (Books, Courses, Journals, Tutorials & Blogs)
- **Hardware** (organized by platform: Android, Swift/iOS, and others)
- **Industry**
- **Research**

## Confirmed Highlights (by category)

The following were directly confirmed in this project's fetch of the source list. Categories not listed below (How-To Playback Audio, How-To Read and Write Audio Files, How-To Record Audio's full contents, How-To Send Real-Time Audio, How-To Transcribe Audio into Text, How-To Visualize Audio, Education's actual book/course/journal entries, Industry) were not reliably captured — refetch the live URL for those rather than trusting a guess here.

### How-To Analyze Audio

Dolby.io Media Analyze API (identifies codec, clipping, loudness, sound classification, silence, etc.), MATLAB DSP System Toolbox, Librosa (Python package for music/audio analysis), PyAudio Analysis (Python package for audio analysis and feature extraction).

### How-To Edit Audio (partial)

Dolby.io Media Enhance API (corrects noise, sibilance, EQ, tonality, loudness), Dolby.io Media Transcode API, **Dolby.io Media Music Mastering API** (professional-sounding audio masters — directly relevant to `knowledge_base/mastering/`), Avid Pro Tools, iZotope, FL Studio, Ableton Live, Nuendo (DAW with Dolby Atmos/spatial-audio support), and more (list continues past this snapshot).

### Community (Social Forums)

Music and Audio Professionals (LinkedIn group), r/audioengineering, Signal Processing StackExchange, The Audio Programmer Discord.

### Hardware (partial, by platform)

Android: AudioRecord, MediaRecorder, Oboe (C++ library wrapping OpenSL ES and AAudio for high-performance audio). Swift/iOS: AVFoundation, AVCapture, AVFAudio. Also references PyAudio (Python bindings for PortAudio) — list continues past this snapshot with more platforms.

### Research

AudioSet (large-scale annotated audio-event dataset with sound ontology), CSTR VCTK (110-speaker English speech corpus), Freesound (collaborative Creative Commons sound database), LibriSpeech (1000-hour audiobook speech corpus), Mozilla Common Voice (open-source multilingual voice dataset), Netflix Open Content (documentary/live-action/animation test titles), Spoken Wikipedia Corpora, Voice Datasets (comprehensive list of open-source voice/music datasets).

## Common Mistakes

Treating this snapshot as complete or current — several full categories (5 of 8 Code subcategories, Education's actual entries, Industry) aren't represented here at all. Refetch the live URL rather than assuming gaps have been filled in.

Citing this doc's contents as if they were vetted, KB-grounded technique recommendations — like its sibling entries, this is an external community/vendor list, not this project's own researched or genre-grounded content. Note in particular that Dolby.io's own APIs are commercial products listed by their own maintainers, not independently vetted by this project.

Confusing this developer/API-oriented list with the other two reference entries' end-user tool focus — this is the one to check for "build a feature," not "pick a production tool."

## Cross-References

- `knowledge_base/reference/awesome_music_production_external_directory.md` — the sibling entry for end-user music-production software/hardware/services
- `knowledge_base/reference/awesome_music_external_directory_noteflakes.md` — the sibling entry for audio-programming infrastructure and notation/theory-teaching resources
- `knowledge_base/mastering/` — the KB's own mastering technique documentation, relevant alongside this list's Dolby.io Media Music Mastering API mention
