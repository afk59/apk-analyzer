# OH\_AudioFormat

typedef struct {...} OH\_AudioFormat

#### Overview

The struct describes the audio stream information, which is used to describe the basic audio format, required for audio creation.

**Since**: 22

**Related module**: [OHAudioSuite](../../modules/ohaudiosuite/document.md)

**Header file**: [native\_audio\_suite\_base.h](../../header-files/native-audio-suite-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [OH\_Audio\_SampleRate](../../header-files/native-audio-suite-base-h/document.md#oh_audio_samplerate) samplingRate | Sample rate of the audio stream. |
| OH\_AudioChannelLayout channelLayout | Channel layout of the audio stream. Currently, only **CH\_LAYOUT\_MONO** and **CH\_LAYOUT\_STEREO** are supported. |
| uint32\_t channelCount | Number of audio channels in the audio stream. Currently, only single-channel (1) and dual-channel (2) configurations are supported. |
| [OH\_Audio\_EncodingType](../../header-files/native-audio-suite-base-h/document.md#oh_audio_encodingtype) encodingType | Encoding type used for the audio stream. |
| [OH\_Audio\_SampleFormat](../../header-files/native-audio-suite-base-h/document.md#oh_audio_sampleformat) sampleFormat | Sample format of the audio stream. |
