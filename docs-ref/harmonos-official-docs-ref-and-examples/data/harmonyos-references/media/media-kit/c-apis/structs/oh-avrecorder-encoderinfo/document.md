# OH\_AVRecorder\_EncoderInfo

typedef struct OH\_AVRecorder\_EncoderInfo {...} OH\_AVRecorder\_EncoderInfo

#### Overview

The struct describes the encoder information.

**Since**: 18

**Related module**: [AVRecorder](../../modules/avrecorder/document.md)

**Header file**: [avrecorder\_base.h](../../header-files/avrecorder-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [OH\_AVRecorder\_CodecMimeType](../../header-files/avrecorder-base-h/document.md#oh_avrecorder_codecmimetype) mimeType | MIME type of the encoder. |
| char\* type | Pointer to the encoder type. The value **audio** means an audio encoder, and **video** means a video encoder. |
| [OH\_AVRecorder\_Range](../oh-avrecorder-range/document.md) bitRate | Bit rate range of the encoder, with the minimum and maximum bit rates specified. |
| [OH\_AVRecorder\_Range](../oh-avrecorder-range/document.md) frameRate | Video frame rate range, with the minimum and maximum frame rates specified. This parameter is available only for video encoders. |
| [OH\_AVRecorder\_Range](../oh-avrecorder-range/document.md) width | Video frame width range, with the minimum and maximum widths specified. This parameter is available only for video encoders. |
| [OH\_AVRecorder\_Range](../oh-avrecorder-range/document.md) height | Video frame height range, with the minimum and maximum heights specified. This parameter is available only for video encoders. |
| [OH\_AVRecorder\_Range](../oh-avrecorder-range/document.md) channels | Audio channel count for the audio capturer, with the minimum and maximum numbers of audio channels specified. This parameter is available only for audio encoders. |
| int32\_t\* sampleRate | Pointer to the list of audio sample rates, including all available audio sample rates. This parameter is available only for audio encoders. |
| int32\_t sampleRateLen | Length of the audio sample rate list. |
