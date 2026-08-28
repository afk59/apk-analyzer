# OH\_AudioStreamInfo

typedef struct OH\_AudioStreamInfo {...} OH\_AudioStreamInfo

#### Overview

The struct describes the audio stream information, which is used to describe the basic audio format.

**Since**: 19

**Related module**: [OHAudio](../../modules/ohaudio/document.md)

**Header file**: [native\_audiostream\_base.h](../../header-files/native-audiostream-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t samplingRate | Sampling rate. |
| [OH\_AudioChannelLayout](../../../../avcodec-kit/c-apis/header-files/native-audio-channel-layout-h/document.md#oh_audiochannellayout) channelLayout | Audio channel layout. |
| [OH\_AudioStream\_EncodingType](../../header-files/native-audiostream-base-h/document.md#oh_audiostream_encodingtype) encodingType | Encoding type. |
| [OH\_AudioStream\_SampleFormat](../../header-files/native-audiostream-base-h/document.md#oh_audiostream_sampleformat) sampleFormat | Sampling format. |
