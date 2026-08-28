# OH\_AudioBuffer

typedef struct OH\_AudioBuffer {...} OH\_AudioBuffer

#### Overview

The struct describes the configuration such as the size, type, and timestamp of audio data.

**Since**: 10

**Related module**: [AVScreenCapture](../../modules/avscreencapture/document.md)

**Header file**: [native\_avscreen\_capture\_base.h](../../header-files/native-avscreen-capture-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t\* buf | Pointer to an audio buffer. |
| int32\_t size | Size of the audio buffer. |
| int64\_t timestamp | Timestamp of the audio buffer. |
| [OH\_AudioCaptureSourceType](../../header-files/native-avscreen-capture-base-h/document.md#oh_audiocapturesourcetype) type | Type of the audio capture source. |
