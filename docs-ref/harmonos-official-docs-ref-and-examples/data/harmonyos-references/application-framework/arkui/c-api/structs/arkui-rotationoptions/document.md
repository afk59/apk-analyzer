# ArkUI\_RotationOptions

typedef struct {...} ArkUI\_RotationOptions

#### Overview

Defines the rotation effect object for a component during transition.

**Since**: 12

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Header file**: [native\_type.h](../../header-files/native-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| float x | X-component of the rotation vector. |
| float y | Y-component of the rotation vector. |
| float z | Z-component of the rotation vector. |
| float angle | Rotation angle. The value range is (-∞, +∞). A positive angle indicates a clockwise rotation, and a negative angle indicates a counterclockwise rotation. |
| float centerX | X-coordinate of the center point, in vp. |
| float centerY | Y-coordinate of the center point, in vp. |
| float centerZ | Z-component of the 3D rotation center point, in px. |
| float perspective | Viewing distance, that is, the distance from the viewpoint to the z=0 plane, in px. |
