# OH\_AudioCaptureInfo

typedef struct OH\_AudioCaptureInfo {...} OH\_AudioCaptureInfo

#### Overview

The struct describes the audio capture information.

When both **audioSampleRate** and **audioChannels** are **0**, the audio-related parameters are ignored and the audio data is not recorded.

**Since**: 10

**Related module**: [AVScreenCapture](../../modules/avscreencapture/document.md)

**Header file**: [native\_avscreen\_capture\_base.h](../../header-files/native-avscreen-capture-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t audioSampleRate | Audio sample rate. For details about the supported rates, see [AudioSamplingRate](../../../../audio-kit/arkts-apis/ohos-multimedia-audio-audio-management/enums/document.md#audiosamplingrate8) of Audio Kit. |
| int32\_t audioChannels | Audio channel count. |
| [OH\_AudioCaptureSourceType](../../header-files/native-avscreen-capture-base-h/document.md#oh_audiocapturesourcetype) audioSource | Audio source. |
