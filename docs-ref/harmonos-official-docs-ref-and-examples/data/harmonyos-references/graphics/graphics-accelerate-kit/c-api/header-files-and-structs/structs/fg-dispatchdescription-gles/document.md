# FG\_DispatchDescription\_GLES

#### Overview

Describes the parameter information required by [HMS\_FG\_Dispatch\_GLES](../../../modules/graphicsaccelerate/document.md#gab135a0f59582d168d461ef115423cfb4). The parameter information needs to be updated for each frame. This API applies only to the OpenGL ES graphics API.

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

uint32\_t [inputColor](#a91056017b03b30a68df9018ce8e7b676)

 | 

Color buffer index of real frames. The color buffer supports the GL\_RGBA8, GL\_R11F\_G11F\_B10F, and GL\_RGBA16F formats.

Value range: \[0, 2^32 – 1\]

 |
| 

uint32\_t [inputDepthStencil](#a39d8ea5f2f685328f3d309f14e445e39)

 | 

Depth stencil buffer index of real frames. The depth stencil buffer supports the GL\_DEPTH24\_STENCIL8 and GL\_DEPTH32F\_STENCIL8 formats.

Value range: \[0, 2^32 – 1\]

 |
| 

[FG\_Mat4x4](../fg-mat4x4/document.md) [viewProj](#a46bffa3d279f60171488a6e4c0c8436d)

 | 

View projection matrix of real frames, that is, the matrix used for coordinate system conversion from the world space to the camera clip space. The matrix must be a 4x4 matrix in column-major order.

 |
| 

[FG\_Mat4x4](../fg-mat4x4/document.md) [invViewProj](#a03c61b50406beb0d0c9e7a7fa50fcf02)

 | 

Inverse view projection matrix of real frames, that is, the matrix used for coordinate system conversion from the camera clip space to the world space. The matrix must be a 4x4 matrix in column-major order.

 |
| 

uint32\_t [outputColor](#ad4c32e775aa14015a7b1e31530d7c9ab)

 | 

Predicted frame buffer index. The predicted frame buffer supports the GL\_RGBA8, GL\_R11F\_G11F\_B10F, and GL\_RGBA16F formats. This predicted frame buffer needs to be created and input by you.

Value range: \[0, 2^32 – 1\]

 |

#### Member Variable Description

#### \[h2\]inputColor

uint32\_t FG\_DispatchDescription\_GLES::inputColor

**Description**

Color buffer index of real frames. The color buffer supports the GL\_RGBA8, GL\_R11F\_G11F\_B10F, and GL\_RGBA16F formats.

#### \[h2\]inputDepthStencil

uint32\_t FG\_DispatchDescription\_GLES::inputDepthStencil

**Description**

Depth stencil buffer index of real frames. The depth stencil buffer supports the GL\_DEPTH24\_STENCIL8 and GL\_DEPTH32F\_STENCIL8 formats.

#### \[h2\]invViewProj

[FG\_Mat4x4](../fg-mat4x4/document.md) FG\_DispatchDescription\_GLES::invViewProj

**Description**

Inverse view projection matrix of real frames, that is, the matrix used for coordinate system conversion from the camera clip space to the world space. The matrix must be a 4x4 matrix in column-major order.

#### \[h2\]outputColor

uint32\_t FG\_DispatchDescription\_GLES::outputColor

**Description**

Predicted frame buffer index. The predicted frame buffer supports the GL\_RGBA8, GL\_R11F\_G11F\_B10F, and GL\_RGBA16F formats. This predicted frame buffer needs to be created and input by you.

#### \[h2\]viewProj

[FG\_Mat4x4](../fg-mat4x4/document.md) FG\_DispatchDescription\_GLES::viewProj

**Description**

View projection matrix of real frames, that is, the matrix used for coordinate system conversion from the world space to the camera clip space. The matrix must be a 4x4 matrix in column-major order.
