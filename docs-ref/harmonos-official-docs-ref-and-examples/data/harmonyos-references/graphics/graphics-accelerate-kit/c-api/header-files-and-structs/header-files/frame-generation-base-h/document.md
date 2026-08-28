# frame\_generation\_base.h

#### Overview

Declares frame generation APIs used for different graphics APIs.

**Library**: libframegeneration.so

**System capability**: SystemCapability.GraphicsGame.RenderAccelerate

**Start version**: 5.0.0(12)

**Related module**: [GraphicsAccelerate](../../../modules/graphicsaccelerate/document.md)

#### Summary

#### \[h2\]Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [FG\_Mat4x4](../../structs/fg-mat4x4/document.md)

 | 

Describes a 4x4 matrix in column-major order.

 |
| 

struct [FG\_AlgorithmModeInfo](../../structs/fg-algorithmmodeinfo/document.md)

 | 

Describes the frame generation algorithm mode information.

 |
| 

struct [FG\_Dimension2D](../../structs/fg-dimension2d/document.md)

 | 

Describes the 2D image resolution, in pixels.

 |
| 

struct [FG\_ResolutionInfo](../../structs/fg-resolutioninfo/document.md)

 | 

Describes the resolutions of input and output images for frame generation.

 |
| 

struct [FG\_Vec3D](../../structs/fg-vec3d/document.md)

 | 

Describes a frame generation 3D vector.

 |
| 

struct [FG\_PerFrameExtendedCameraInfo](../../structs/fg-perframeextendedcamerainfo/document.md)

 | 

Describes extended camera information. When the translation component of the view projection matrix is very large, more detailed camera information can be provided for more accurate frame prediction.

 |
| 

struct [FG\_IntegrationInfo](../../structs/fg-integrationinfo/document.md)

 | 

Describes the integration information about frame generation, including the display mode, whether to separately buffer depth and color textures, and whether to flip the color texture.

 |

#### \[h2\]Type Definitions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef struct [FG\_Mat4x4](../../structs/fg-mat4x4/document.md) [FG\_Mat4x4](../../../modules/graphicsaccelerate/document.md#gabbf87d3423630e0b50f19da2cbda3e90)

 | 

Describes a 4x4 matrix in column-major order.

 |
| 

typedef enum [FG\_PredictionMode](../../../modules/graphicsaccelerate/document.md#gaea2169cd5ae4bf9e8a17dc58f33e8766) [FG\_PredictionMode](../../../modules/graphicsaccelerate/document.md#ga79e55783a2a38873fc6890c297885275)

 | 

Describes the frame prediction algorithm modes for frame generation.

 |
| 

typedef enum [FG\_MeMode](../../../modules/graphicsaccelerate/document.md#ga8bd44b6bea12774dd2ee6014d696e7d1) [FG\_MeMode](../../../modules/graphicsaccelerate/document.md#ga81cbe226af620e6ef19cd8ec5e9b5256)

 | 

Describes the motion estimation algorithm modes. The basic mode and enhanced mode are supported.

 |
| 

typedef struct [FG\_AlgorithmModeInfo](../../structs/fg-algorithmmodeinfo/document.md) [FG\_AlgorithmModeInfo](../../../modules/graphicsaccelerate/document.md#ga1750087784d7cbf19957243db12a7ba3)

 | 

Describes the frame generation algorithm mode information.

 |
| 

typedef enum [FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga394c554fc5d056d702180ee031ccee2c)

 | 

Describes the error codes of frame generation API calls.

 |
| 

typedef enum [FG\_CvvZSemantic](../../../modules/graphicsaccelerate/document.md#ga530448309918d6d703e28c61a848a267) [FG\_CvvZSemantic](../../../modules/graphicsaccelerate/document.md#gabac7987ddc62b712f36d95b185e47bb2)

 | 

Describes the homogeneous clip space Z/W ranges and depth functions after camera projection transformation.

 |
| 

typedef enum [FG\_PresentMode](../../../modules/graphicsaccelerate/document.md#section11881356193212) [FG\_PresentMode](../../../modules/graphicsaccelerate/document.md#section11881356193212)

 | 

Defines the predicted frame display modes. There are two modes: game display mode (the game sends predicted frames for display) and system display mode (the system sends predicted frames for display).

 |
| 

typedef struct [FG\_Dimension2D](../../structs/fg-dimension2d/document.md) [FG\_Dimension2D](../../../modules/graphicsaccelerate/document.md#ga545268ccc070666954981580f5764d20)

 | 

Describes the 2D image resolution, in pixels.

 |
| 

typedef struct [FG\_ResolutionInfo](../../structs/fg-resolutioninfo/document.md) [FG\_ResolutionInfo](../../../modules/graphicsaccelerate/document.md#gacbc0d894e11f18711fd4558d45c7cd39)

 | 

Describes the resolutions of input and output images for frame generation.

 |
| 

typedef struct [FG\_Vec3D](../../structs/fg-vec3d/document.md) [FG\_Vec3D](../../structs/fg-vec3d/document.md)

 | 

Describes a frame generation 3D vector.

 |
| 

typedef struct [FG\_PerFrameExtendedCameraInfo](../../structs/fg-perframeextendedcamerainfo/document.md) [FG\_PerFrameExtendedCameraInfo](../../structs/fg-perframeextendedcamerainfo/document.md)

 | 

Describes extended camera information. When the translation component of the view projection matrix is very large, more detailed camera information can be provided for more accurate frame prediction.

 |
| 

typedef struct [FG\_IntegrationInfo](../../structs/fg-integrationinfo/document.md)

 | 

Describes the integration information about frame generation, including the display mode, whether to separately buffer depth and color textures, and whether to flip the color texture.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[FG\_PredictionMode](../../../modules/graphicsaccelerate/document.md#gaea2169cd5ae4bf9e8a17dc58f33e8766) {

FG\_PREDICTION\_MODE\_INTERPOLATION = 0,

FG\_PREDICTION\_MODE\_EXTRAPOLATION = 1

}

 | 

Describes the frame prediction algorithm modes for frame generation.

 |
| 

[FG\_MeMode](../../../modules/graphicsaccelerate/document.md#ga8bd44b6bea12774dd2ee6014d696e7d1) {

FG\_ME\_MODE\_BASIC = 0,

FG\_ME\_MODE\_ENHANCED = 1

}

 | 

Describes the motion estimation algorithm modes. The basic mode and enhanced mode are supported.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) {

FG\_SUCCESS = 0,

FG\_INVALID\_PARAMETER = 401,

FG\_CONTEXT\_NOT\_CONFIG = 1009500001,

FG\_CONTEXT\_NOT\_ACTIVE = 1009500002,

FG\_COLLECTING\_PREVIOUS\_FRAMES = 1009500003

}

 | 

Describes the error codes of frame generation API calls.

 |
| 

[FG\_CvvZSemantic](../../../modules/graphicsaccelerate/document.md#ga530448309918d6d703e28c61a848a267) {

FG\_CVV\_Z\_SEMANTIC\_MINUS\_ONE\_TO\_ONE\_FORWARD\_Z = 0,

FG\_CVV\_Z\_SEMANTIC\_ZERO\_TO\_ONE\_REVERSE\_Z = 1,

FG\_CVV\_Z\_SEMANTIC\_MINUS\_ONE\_TO\_ONE\_REVERSE\_Z = 2,

FG\_CVV\_Z\_SEMANTIC\_ZERO\_TO\_ONE\_FORWARD\_Z = 3

}

 | 

Describes the homogeneous clip space Z/W ranges and depth functions after camera projection transformation.

 |
| 

[FG\_PresentMode](../../../modules/graphicsaccelerate/document.md#section11881356193212) {

FG\_PRESENT\_BY\_GAME = 0,

FG\_PRESENT\_BY\_SYSTEM = 1

}

 | 

Defines the predicted frame display modes. There are two modes: game display mode (the game sends predicted frames for display) and system display mode (the system sends predicted frames for display).

 |
