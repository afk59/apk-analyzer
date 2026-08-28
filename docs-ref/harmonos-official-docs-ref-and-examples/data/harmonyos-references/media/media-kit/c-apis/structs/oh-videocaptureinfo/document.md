# OH\_VideoCaptureInfo

typedef struct OH\_VideoCaptureInfo {...} OH\_VideoCaptureInfo

#### Overview

The struct describes the video capture information. When **videoFrameWidth** and **videoFrameHeight** are both **0**, video-related parameters are ignored and screen data is not recorded.

**Since**: 10

**Related module**: [AVScreenCapture](../../modules/avscreencapture/document.md)

**Header file**: [native\_avscreen\_capture\_base.h](../../header-files/native-avscreen-capture-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint64\_t displayId | ID of the physical screen to capture. This member variable is valid when **capturemode** is set to **CAPTURE\_SPECIFIED\_SCREEN**. |
| int32\_t\* missionIDs | Mission ID list. This member variable is valid when **capturemode** is set to **CAPTURE\_SPECIFIED\_WINDOW**. |
| int32\_t missionIDsLen | Length of the mission ID list. This member variable is valid when **capturemode** is set to **CAPTURE\_SPECIFIED\_WINDOW**. |
| int32\_t videoFrameWidth | Width of the video to capture, in px. |
| int32\_t videoFrameHeight | Height of the video to capture, in px. |
| [OH\_VideoSourceType](../../header-files/native-avscreen-capture-base-h/document.md#oh_videosourcetype) videoSource | Video source type. Currently, only RGBA is supported. |
