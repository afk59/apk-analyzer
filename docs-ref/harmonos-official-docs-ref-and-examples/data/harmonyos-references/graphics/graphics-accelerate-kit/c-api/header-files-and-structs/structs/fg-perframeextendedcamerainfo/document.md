# FG\_PerFrameExtendedCameraInfo

#### Overview

Describes extended camera information. When the translation component of the view projection matrix is very large, more detailed camera information can be provided for more accurate frame prediction.

**Start version**: 5.0.0(12)

**Related module**: [GraphicsAccelerate](../../../modules/graphicsaccelerate/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[FG\_Mat4x4](../fg-mat4x4/document.md) proj

 | 

Camera projection matrix, that is, the matrix used for coordinate system conversion from the view space to the clip space.

 |
| 

[FG\_Mat4x4](../fg-mat4x4/document.md) translatedInvViewProj

 | 

Translated inverse view projection matrix, that is, the matrix used for coordinate system conversion from the clip space to the camera-centric world space.

 |
| 

[FG\_Mat4x4](../fg-mat4x4/document.md) translatedView

 | 

Translated view matrix, that is, the matrix used for coordinate system conversion from the camera-centric world space to the view space.

 |
| 

[FG\_Mat4x4](../fg-mat4x4/document.md) translatedViewProj

 | 

Translated view projection matrix, that is, the matrix used for coordinate system conversion from the camera-centric world space to the clip space.

 |
| 

[FG\_Vec3D](../fg-vec3d/document.md) worldPosition

 | 

Camera coordinates in the world space.

 |

#### Member Variable Description

#### \[h2\]proj

[FG\_Mat4x4](../fg-mat4x4/document.md) FG\_PerFrameExtendedCameraInfo::proj

**Description**

Camera projection matrix, that is, the matrix used for coordinate system conversion from the view space to the clip space.

#### \[h2\]translatedInvViewProj

[FG\_Mat4x4](../fg-mat4x4/document.md) FG\_PerFrameExtendedCameraInfo::translatedInvViewProj

**Description**

Translated inverse view projection matrix, that is, the matrix used for coordinate system conversion from the clip space to the camera-centric world space.

#### \[h2\]translatedView

[FG\_Mat4x4](../fg-mat4x4/document.md) FG\_PerFrameExtendedCameraInfo::translatedView

**Description**

Translated view matrix, that is, the matrix used for coordinate system conversion from the camera-centric world space to the view space.

#### \[h2\]translatedViewProj

[FG\_Mat4x4](../fg-mat4x4/document.md) FG\_PerFrameExtendedCameraInfo::translatedViewProj

**Description**

Translated view projection matrix, that is, the matrix used for coordinate system conversion from the camera-centric world space to the clip space.

#### \[h2\]worldPosition

[FG\_Vec3D](../fg-vec3d/document.md) FG\_PerFrameExtendedCameraInfo::worldPosition

**Description**

Camera coordinates in the world space.
