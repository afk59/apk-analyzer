# OH\_AVRecorder\_Profile

typedef struct OH\_AVRecorder\_Profile {...} OH\_AVRecorder\_Profile

#### Overview

The struct describes the parameters used for audio and video recording.

You can choose to record only audio or only video by setting the parameters.

1.  When **audioBitrate** or **audioChannels** is set to **0**, audio recording is disabled.
2.  When **videoFrameWidth** or **videoFrameHeight** is set to **0**, video recording is disabled.

For details about the value range of each parameter, see [AVRecorderProfile](../../../arkts-apis/ohos-multimedia-media-media/interfaces-others/document.md#avrecorderprofile9).

**Since**: 18

**Related module**: [AVRecorder](../../modules/avrecorder/document.md)

**Header file**: [avrecorder\_base.h](../../header-files/avrecorder-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t audioBitrate | Audio bit rate. |
| int32\_t audioChannels | Number of channels. |
| [OH\_AVRecorder\_CodecMimeType](../../header-files/avrecorder-base-h/document.md#oh_avrecorder_codecmimetype) audioCodec | Audio encoding format. |
| int32\_t audioSampleRate | Audio sample rate. |
| [OH\_AVRecorder\_ContainerFormatType](../../header-files/avrecorder-base-h/document.md#oh_avrecorder_containerformattype) fileFormat | Output file format. |
| int32\_t videoBitrate | Video bit rate. |
| [OH\_AVRecorder\_CodecMimeType](../../header-files/avrecorder-base-h/document.md#oh_avrecorder_codecmimetype) videoCodec | Video encoding format. |
| int32\_t videoFrameWidth | Video width. |
| int32\_t videoFrameHeight | Video height. |
| int32\_t videoFrameRate | Video frame rate. |
| bool isHdr | 
Whether HDR videos are recorded.

**true** if recorded, **false** otherwise.

The default value is **false**.

 |
| bool enableTemporalScale | 

Whether temporal scalable encoding is enabled.

When this parameter is set to **true**, some frames in the encoded output stream can be skipped to optimize encoding efficiency. When it is set to **false**, all frames in the encoded output stream must be encoded without skipping. For details, see [Temporally Scalable Video Coding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-encoding-temporal-scalability)

The default value is **false**.

 |
