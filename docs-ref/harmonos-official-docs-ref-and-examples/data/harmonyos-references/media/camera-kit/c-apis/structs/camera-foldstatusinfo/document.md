# Camera\_FoldStatusInfo

typedef struct Camera\_FoldStatusInfo {...} Camera\_FoldStatusInfo

#### Overview

The struct describes the fold status information of the camera.

**Since**: 13

**Related module**: [OH\_Camera](../../modules/oh-camera/document.md)

**Header file**: [camera.h](../../header-files/camera-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [Camera\_Device](../camera-device/document.md)\*\* supportedCameras | Double pointer to the camera list. |
| uint32\_t cameraSize | Number of cameras in the list. |
| [Camera\_FoldStatus](../../header-files/camera-h/document.md#camera_foldstatus) foldStatus | Current fold status. |
