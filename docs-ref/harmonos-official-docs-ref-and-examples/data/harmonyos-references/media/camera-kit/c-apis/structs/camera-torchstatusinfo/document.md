# Camera\_TorchStatusInfo

typedef struct Camera\_TorchStatusInfo {...} Camera\_TorchStatusInfo

#### Overview

The struct describes the flashlight status information.

**Since**: 12

**Related module**: [OH\_Camera](../../modules/oh-camera/document.md)

**Header file**: [camera.h](../../header-files/camera-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| bool isTorchAvailable | Whether the flashlight is available. **true** if available, **false** otherwise. |
| bool isTorchActive | Whether the flashlight is activated. **true** if activated, **false** otherwise. |
| float torchLevel | Flashlight level. The value range is \[0, 1\]. A larger value indicates a greater luminance. |
