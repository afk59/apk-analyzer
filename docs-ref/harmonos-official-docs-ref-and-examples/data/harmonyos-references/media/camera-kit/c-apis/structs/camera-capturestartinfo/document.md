# Camera\_CaptureStartInfo

typedef struct Camera\_CaptureStartInfo {...} Camera\_CaptureStartInfo

#### Overview

The struct describes the capture start information.

**Since**: 12

**Related module**: [OH\_Camera](../../modules/oh-camera/document.md)

**Header file**: [camera.h](../../header-files/camera-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t captureId | Capture ID. |
| int64\_t time | Estimated duration when the sensor captures frames at the bottom layer in a single capture. If **–1** is reported, there is no estimated duration. |
