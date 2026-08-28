# OH\_AVScreenCaptureConfig

typedef struct OH\_AVScreenCaptureConfig {...} OH\_AVScreenCaptureConfig

#### Overview

The struct describes the screen capture configuration.

**Since**: 10

**Related module**: [AVScreenCapture](../../modules/avscreencapture/document.md)

**Header file**: [native\_avscreen\_capture\_base.h](../../header-files/native-avscreen-capture-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [OH\_CaptureMode](../../header-files/native-avscreen-capture-base-h/document.md#oh_capturemode) captureMode | Screen capture mode. |
| [OH\_DataType](../../header-files/native-avscreen-capture-base-h/document.md#oh_datatype) dataType | Data type of the screen capture stream. |
| [OH\_AudioInfo](../oh-audioinfo/document.md) audioInfo | Audio capture information. |
| [OH\_VideoInfo](../oh-videoinfo/document.md) videoInfo | Video capture information. |
| [OH\_RecorderInfo](../oh-recorderinfo/document.md) recorderInfo | Recording file information. This member variable is mandatory when the data type is **OH\_CAPTURE\_FILE**. |
