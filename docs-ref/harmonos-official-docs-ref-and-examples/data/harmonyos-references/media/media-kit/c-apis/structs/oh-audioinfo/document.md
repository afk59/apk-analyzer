# OH\_AudioInfo

typedef struct OH\_AudioInfo {...} OH\_AudioInfo

#### Overview

The struct describes the audio information.

To perform both external capture (using microphones) and internal capture, **audioSampleRate** and **audioChannels** must be the same for both audio channels.

**Since**: 10

**Related module**: [AVScreenCapture](../../modules/avscreencapture/document.md)

**Header file**: [native\_avscreen\_capture\_base.h](../../header-files/native-avscreen-capture-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [OH\_AudioCaptureInfo](../oh-audiocaptureinfo/document.md) micCapInfo | External audio capture information. |
| [OH\_AudioCaptureInfo](../oh-audiocaptureinfo/document.md) innerCapInfo | Internal audio capture information. |
| [OH\_AudioEncInfo](../oh-audioencinfo/document.md) audioEncInfo | Audio encoding information, which is not required for raw streams. |
