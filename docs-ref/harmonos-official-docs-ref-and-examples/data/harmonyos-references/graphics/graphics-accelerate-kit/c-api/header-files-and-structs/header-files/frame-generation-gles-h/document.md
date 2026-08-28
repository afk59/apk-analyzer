# frame\_generation\_gles.h

#### Overview

Declares frame generation APIs used for the OpenGL ES graphics API.

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

struct [FG\_DispatchDescription\_GLES](../../structs/fg-dispatchdescription-gles/document.md)

 | 

Describes the parameter information required by [HMS\_FG\_Dispatch\_GLES](../../../modules/graphicsaccelerate/document.md#gab135a0f59582d168d461ef115423cfb4). The parameter information needs to be updated for each frame. This API applies only to the OpenGL ES graphics API.

 |

#### \[h2\]Type Definitions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef struct [FG\_Context\_GLES](../../../modules/graphicsaccelerate/document.md#ga62e666292d67fd19fd35ad07463e21cc) [FG\_Context\_GLES](../../../modules/graphicsaccelerate/document.md#ga62e666292d67fd19fd35ad07463e21cc)

 | 

Describes the frame generation context. This API applies only to the OpenGL ES graphics API.

 |
| 

typedef struct [FG\_DispatchDescription\_GLES](../../structs/fg-dispatchdescription-gles/document.md) [FG\_DispatchDescription\_GLES](../../../modules/graphicsaccelerate/document.md#ga3f4c6e065ff13670d8c64cb9cc3796a7)

 | 

Describes the parameter information required by [HMS\_FG\_Dispatch\_GLES](../../../modules/graphicsaccelerate/document.md#gab135a0f59582d168d461ef115423cfb4). The parameter information needs to be updated for each frame. This API applies only to the OpenGL ES graphics API.

 |
| 

typedef enum [FG\_ImageFormat\_GLES](../../../modules/graphicsaccelerate/document.md#ga3bec27405891e089234bf50d0589c3cd) [FG\_ImageFormat\_GLES](../../../modules/graphicsaccelerate/document.md#ga5fbce7432ad1a2e3d9a37554bce2352a)

 | 

Describes the image formats of the real frame color buffer and the predicted frame buffer. This API applies only to the OpenGL ES graphics API.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[FG\_ImageFormat\_GLES](../../../modules/graphicsaccelerate/document.md#ga3bec27405891e089234bf50d0589c3cd) {

FG\_FORMAT\_R8G8B8A8\_UNORM = 0,

FG\_FORMAT\_R11G11B10\_SFLOAT = 1,

FG\_FORMAT\_R16G16B16A16\_SFLOAT = 2

}

 | 

Describes the image formats of the real frame color buffer and the predicted frame buffer. This API applies only to the OpenGL ES graphics API.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[FG\_Context\_GLES](../../../modules/graphicsaccelerate/document.md#ga62e666292d67fd19fd35ad07463e21cc)\* [HMS\_FG\_CreateContext\_GLES](../../../modules/graphicsaccelerate/document.md#ga58e6b601cc4a7e8f0208d4f10f16c7e5)(void)

 | 

Creates a frame generation context instance. If the call is successful, a pointer to the [FG\_Context\_GLES](../../../modules/graphicsaccelerate/document.md#ga62e666292d67fd19fd35ad07463e21cc) object will be returned. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetAlgorithmMode\_GLES](../../../modules/graphicsaccelerate/document.md#ga79cc36ec768553a6560d1c553ef83c3b)([FG\_Context\_GLES](../../../modules/graphicsaccelerate/document.md#ga62e666292d67fd19fd35ad07463e21cc)\* context, const [FG\_AlgorithmModeInfo](../../structs/fg-algorithmmodeinfo/document.md)\* predictionModeInfo)

 | 

Sets the frame prediction algorithm mode and motion estimation mode for frame generation. This API is mandatory. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetResolution\_GLES](../../../modules/graphicsaccelerate/document.md#gae46fcee6c715a6fda24df727465d42b1)([FG\_Context\_GLES](../../../modules/graphicsaccelerate/document.md#ga62e666292d67fd19fd35ad07463e21cc)\* context, const [FG\_ResolutionInfo](../../structs/fg-resolutioninfo/document.md)\* resolutionInfo)

 | 

Sets the resolutions of input and output images for frame generation. This API is mandatory. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetCvvZSemantic\_GLES](../../../modules/graphicsaccelerate/document.md#ga6247264302a139024a92cf89da565b52)([FG\_Context\_GLES](../../../modules/graphicsaccelerate/document.md#ga62e666292d67fd19fd35ad07463e21cc)\* context, [FG\_CvvZSemantic](../../../modules/graphicsaccelerate/document.md#ga530448309918d6d703e28c61a848a267) semantic)

 | 

Sets the homogeneous clip space Z/W range and depth function. This API is optional. If it is not called, the default value **FG\_CVV\_Z\_SEMANTIC\_MINUS\_ONE\_TO\_ONE\_FORWARD\_Z** will be used. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetImageFormat\_GLES](../../../modules/graphicsaccelerate/document.md#gaafa490d4377cc5babbc0ac0f4f7b78a7)([FG\_Context\_GLES](../../../modules/graphicsaccelerate/document.md#ga62e666292d67fd19fd35ad07463e21cc)\* context, [FG\_ImageFormat\_GLES](../../../modules/graphicsaccelerate/document.md#ga3bec27405891e089234bf50d0589c3cd) format)

 | 

Sets the image format of the real frame color buffer and the predicted frame buffer. This API is optional. If it is not called, the default value **FG\_FORMAT\_R8G8B8A8\_UNORM** will be used. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetDepthStencilYDirectionInverted\_GLES](../../../modules/graphicsaccelerate/document.md#gaa6e340d0b1f1bc4dcd6abf378aa933df)([FG\_Context\_GLES](../../../modules/graphicsaccelerate/document.md#ga62e666292d67fd19fd35ad07463e21cc)\* context, bool inverted)

 | 

Sets the flag bit for flipping the color buffer around the Y axis relative to the depth stencil buffer. This API is optional. If it is not called, no flipping is performed by default. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_Activate\_GLES](../../../modules/graphicsaccelerate/document.md#gaa5f1d5b98694100aa3e3dbb4c99ac23a)([FG\_Context\_GLES](../../../modules/graphicsaccelerate/document.md#ga62e666292d67fd19fd35ad07463e21cc)\* context)

 | 

Activates a frame generation context instance. Before the activation, the instance attributes must be set. For an activated frame generation context instance, the [HMS\_FG\_Dispatch\_GLES](../../../modules/graphicsaccelerate/document.md#gab135a0f59582d168d461ef115423cfb4) API can be called to generate a predicted frame. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_Deactivate\_GLES](../../../modules/graphicsaccelerate/document.md#gad08ff75c271a0c7c99ae3ebc596928b9)([FG\_Context\_GLES](../../../modules/graphicsaccelerate/document.md#ga62e666292d67fd19fd35ad07463e21cc)\* context)

 | 

Deactivates a frame generation context instance. To activate the instance again, call the [HMS\_FG\_Activate\_GLES](../../../modules/graphicsaccelerate/document.md#gaa5f1d5b98694100aa3e3dbb4c99ac23a) API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_IsActive\_GLES](../../../modules/graphicsaccelerate/document.md#gaaa592e60d1cda40068b51c36d436b8eb)([FG\_Context\_GLES](../../../modules/graphicsaccelerate/document.md#ga62e666292d67fd19fd35ad07463e21cc)\* context, bool\* isActive)

 | 

Checks whether a frame generation context instance is activated. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_Dispatch\_GLES](../../../modules/graphicsaccelerate/document.md#gab135a0f59582d168d461ef115423cfb4)([FG\_Context\_GLES](../../../modules/graphicsaccelerate/document.md#ga62e666292d67fd19fd35ad07463e21cc)\* context, const [FG\_DispatchDescription\_GLES](../../structs/fg-dispatchdescription-gles/document.md)\* desc)

 | 

Sets the parameter information required for frame prediction to generate a predicted frame. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetExtendedCameraInfo\_GLES](../../../modules/graphicsaccelerate/document.md#section1450921818712)([FG\_Context\_GLES](../../../modules/graphicsaccelerate/document.md#ga62e666292d67fd19fd35ad07463e21cc)\* context, const [FG\_PerFrameExtendedCameraInfo](../../structs/fg-perframeextendedcamerainfo/document.md)\* info)

 | 

Sets the extended camera attribute information. When the translation component of the view projection matrix is very large, this information is provided for more accurate frame generation. This API is optional. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_DestroyContext\_GLES](../../../modules/graphicsaccelerate/document.md#ga8c61d12e9e4c8f7e95bed76006ee3335)([FG\_Context\_GLES](../../../modules/graphicsaccelerate/document.md#ga62e666292d67fd19fd35ad07463e21cc)\*\* context)

 | 

Destroys a frame generation context instance and releases memory resources. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga394c554fc5d056d702180ee031ccee2c) [HMS\_FG\_SetIntegrationMode\_GLES](../../../modules/graphicsaccelerate/document.md#section291123211916)([FG\_Context\_GLES](../../../modules/graphicsaccelerate/document.md#ga62e666292d67fd19fd35ad07463e21cc)\* context, const [FG\_IntegrationInfo](../../structs/fg-integrationinfo/document.md)\* integrationInfo)

 | 

Sets the integration information for frame generation. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga394c554fc5d056d702180ee031ccee2c) [HMS\_FG\_SetUiPredictionEnabled\_GLES](../../../modules/graphicsaccelerate/document.md#section41231648141914)([FG\_Context\_GLES](../../../modules/graphicsaccelerate/document.md#ga62e666292d67fd19fd35ad07463e21cc)\* context, bool isEnabled)

 | 

Sets whether to enable the UI prediction function. This function can be enabled only in system display mode. It is invalid in game display mode. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga394c554fc5d056d702180ee031ccee2c) [HMS\_FG\_SetTargetFps\_GLES](../../../modules/graphicsaccelerate/document.md#section19112185207)([FG\_Context\_GLES](../../../modules/graphicsaccelerate/document.md#ga62e666292d67fd19fd35ad07463e21cc)\* context, int targetFps)

 | 

Sets the target frame rate for frame generation. The setting takes effect only for the system display mode and is invalid for the game display mode. This API takes effect after the game is released for the first time and applies only to the OpenGL ES graphics API.

 |
