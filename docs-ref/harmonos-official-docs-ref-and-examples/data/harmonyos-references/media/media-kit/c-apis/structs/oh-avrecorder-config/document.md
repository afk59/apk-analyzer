# OH\_AVRecorder\_Config

typedef struct OH\_AVRecorder\_Config {...} OH\_AVRecorder\_Config

#### Overview

The struct describes the AVRecorder configuration.

**Since**: 18

**Related module**: [AVRecorder](../../modules/avrecorder/document.md)

**Header file**: [avrecorder\_base.h](../../header-files/avrecorder-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [OH\_AVRecorder\_AudioSourceType](../../header-files/avrecorder-base-h/document.md#oh_avrecorder_audiosourcetype) audioSourceType | Type of the audio source to record. |
| [OH\_AVRecorder\_VideoSourceType](../../header-files/avrecorder-base-h/document.md#oh_avrecorder_videosourcetype) videoSourceType | Type of the video source to record. |
| [OH\_AVRecorder\_Profile](../oh-avrecorder-profile/document.md) profile | Audio and video encoding configuration. |
| char\* url | Pointer to the URL of the recording output file, in the format of fd://xx. |
| [OH\_AVRecorder\_FileGenerationMode](../../header-files/avrecorder-base-h/document.md#oh_avrecorder_filegenerationmode) fileGenerationMode | Mode for generating the recording output file. |
| [OH\_AVRecorder\_Metadata](../oh-avrecorder-metadata/document.md) metadata | Metadata of the recorded media. |
| int32\_t maxDuration | Maximum recording duration. |
