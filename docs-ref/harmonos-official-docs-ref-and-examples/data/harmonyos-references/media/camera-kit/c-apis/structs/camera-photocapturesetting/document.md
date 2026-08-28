# Camera\_PhotoCaptureSetting

typedef struct Camera\_PhotoCaptureSetting {...} Camera\_PhotoCaptureSetting

#### Overview

The struct describes the parameters related to photo capture.

**Since**: 11

**Related module**: [OH\_Camera](../../modules/oh-camera/document.md)

**Header file**: [camera.h](../../header-files/camera-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [Camera\_QualityLevel](../../header-files/camera-h/document.md#camera_qualitylevel) quality | Quality of the photo. |
| [Camera\_ImageRotation](../../header-files/camera-h/document.md#camera_imagerotation) rotation | Rotation angle. |
| [Camera\_Location](../camera-location/document.md)\* location | Pointer to the location where the photo is taken. |
| bool mirror | 
Whether mirroring is enabled.

**true** if enabled, **false** otherwise. The default value is **false**.

 |
