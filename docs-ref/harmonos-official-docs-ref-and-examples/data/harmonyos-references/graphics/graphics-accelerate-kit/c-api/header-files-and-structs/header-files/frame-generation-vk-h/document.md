# frame\_generation\_vk.h

#### Overview

Declares frame generation APIs used for the Vulkan graphics API.

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

struct [FG\_ContextDescription\_VK](../../structs/fg-contextdescription-vk/document.md)

 | 

Describes the attribute information required for creating a frame generation context instance [FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7).

 |
| 

struct [FG\_ImageFormat\_VK](../../structs/fg-imageformat-vk/document.md)

 | 

Describes the input and output image format information for frame generation. This API applies only to the Vulkan graphics API.

 |
| 

struct [FG\_ImageSync\_VK](../../structs/fg-imagesync-vk/document.md)

 | 

Describes the synchronization status information about the input and output images for frame generation. It is used to create a memory barrier for the images.

 |
| 

struct [FG\_ImageInfo\_VK](../../structs/fg-imageinfo-vk/document.md)

 | 

Describes the input and output image information for frame generation.

 |
| 

struct [FG\_DispatchDescription\_VK](../../structs/fg-dispatchdescription-vk/document.md)

 | 

Describes the parameter information required by [HMS\_FG\_Dispatch\_VK](../../../modules/graphicsaccelerate/document.md#ga21f86a194e72e99dd54fd39080385a37). The parameter information needs to be updated for each frame. This API applies only to the Vulkan graphics API.

 |

#### \[h2\]Type Definitions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef struct [FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7) [FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7)

 | 

Describes the frame generation context. This API applies only to the Vulkan graphics API.

 |
| 

typedef struct [FG\_Image\_VK](../../../modules/graphicsaccelerate/document.md#gabd6ee9704e997ffc2792ad3c89847019) [FG\_Image\_VK](../../../modules/graphicsaccelerate/document.md#gabd6ee9704e997ffc2792ad3c89847019)

 | 

Describes the input and output images for frame generation. This API applies only to the Vulkan graphics API.

 |
| 

typedef struct [FG\_ContextDescription\_VK](../../structs/fg-contextdescription-vk/document.md) [FG\_ContextDescription\_VK](../../../modules/graphicsaccelerate/document.md#ga6d3f20ae7b60a4a38baf696031d609c0)

 | 

Describes the attribute information required for creating a frame generation context instance [FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7).

 |
| 

typedef struct [FG\_ImageFormat\_VK](../../structs/fg-imageformat-vk/document.md) [FG\_ImageFormat\_VK](../../../modules/graphicsaccelerate/document.md#ga2ef395664c0fd54102510c62a84ebc3a)

 | 

Describes the input and output image format information for frame generation. This API applies only to the Vulkan graphics API.

 |
| 

typedef struct [FG\_ImageSync\_VK](../../structs/fg-imagesync-vk/document.md) [FG\_ImageSync\_VK](../../../modules/graphicsaccelerate/document.md#ga847779a17b04d183b31397007b11735f)

 | 

Describes the synchronization status information about the input and output images for frame generation. It is used to create a memory barrier for the images.

 |
| 

typedef struct [FG\_ImageInfo\_VK](../../structs/fg-imageinfo-vk/document.md) [FG\_ImageInfo\_VK](../../../modules/graphicsaccelerate/document.md#gabf275c34e4b1335ddcda4b576009d6c7)

 | 

Describes the input and output image information for frame generation.

 |
| 

typedef struct [FG\_DispatchDescription\_VK](../../structs/fg-dispatchdescription-vk/document.md) [FG\_DispatchDescription\_VK](../../../modules/graphicsaccelerate/document.md#gabdf63f9fb31687516fee81d83b609302)

 | 

Describes the parameter information required by [HMS\_FG\_Dispatch\_VK](../../../modules/graphicsaccelerate/document.md#ga21f86a194e72e99dd54fd39080385a37). The parameter information needs to be updated for each frame. This API applies only to the Vulkan graphics API.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7)\* [HMS\_FG\_CreateContext\_VK](../../../modules/graphicsaccelerate/document.md#gac39606d03c25d898c656ab6973bb54f3)(const [FG\_ContextDescription\_VK](../../structs/fg-contextdescription-vk/document.md)\* contextDescription)

 | 

Creates a frame generation context instance. If the call is successful, a pointer to the [FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7) object will be returned. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetAlgorithmMode\_VK](../../../modules/graphicsaccelerate/document.md#ga9262d0cde377603a6ccc1239095be917)([FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7)\* context, const [FG\_AlgorithmModeInfo](../../structs/fg-algorithmmodeinfo/document.md)\* predictionModeInfo)

 | 

Sets the frame generation algorithm mode, including the prediction algorithm mode and motion estimation mode. This API is mandatory. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetResolution\_VK](../../../modules/graphicsaccelerate/document.md#ga2295f5bde5b0186e0f89f7d49e3338bf)([FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7)\* context, const [FG\_ResolutionInfo](../../structs/fg-resolutioninfo/document.md)\* resolutionInfo)

 | 

Sets the resolutions of input and output images for frame generation. This API is mandatory. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetCvvZSemantic\_VK](../../../modules/graphicsaccelerate/document.md#ga7a71df6640e6e95d5d6f67b2e24448fd)([FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7)\* context, [FG\_CvvZSemantic](../../../modules/graphicsaccelerate/document.md#ga530448309918d6d703e28c61a848a267) semantic)

 | 

Sets the homogeneous clip space Z/W range and depth function. This API is optional. If it is not called, the default value **FG\_CVV\_Z\_SEMANTIC\_ZERO\_TO\_ONE\_FORWARD\_Z** will be used. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetImageFormat\_VK](../../../modules/graphicsaccelerate/document.md#gabcb428cb2187ce986cf8ac0f1c76a3ca)([FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7)\* context, const [FG\_ImageFormat\_VK](../../structs/fg-imageformat-vk/document.md)\* format)

 | 

Sets the input and output image formats for frame generation. This API is optional. If it is not called, the default value **VK\_FORMAT\_R8G8B8A8\_UNORM** will be used for the real frame color buffer and predicted frame buffer, and **VK\_FORMAT\_D24\_UNORM\_S8\_UINT** will be used for the depth stencil buffer. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetDepthStencilYDirectionInverted\_VK](../../../modules/graphicsaccelerate/document.md#ga5148977465964658f817de45e28ab80a)([FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7)\* context, bool inverted)

 | 

Sets the flag bit for flipping the color buffer around the Y axis relative to the depth stencil buffer. This API is optional. If it is not called, no flipping is performed by default. This API applies only to the Vulkan graphics API. If flipping occurs but **inverted** is not set to **true**, the predicted frame effect may be abnormal.

 |
| 

[FG\_Image\_VK](../../../modules/graphicsaccelerate/document.md#gabd6ee9704e997ffc2792ad3c89847019)\* [HMS\_FG\_CreateImage\_VK](../../../modules/graphicsaccelerate/document.md#ga7733f097ea5f4ae4d2aa53d11d7e60ff)([FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7)\* context, VkImage image, VkImageView view)

 | 

Creates input and output image instances for frame generation. An image instance must be created through this API for the real frame color buffer, depth stencil buffer, and predicted frame buffer, respectively. Then, the created image instances are passed to the [HMS\_FG\_Dispatch\_VK](../../../modules/graphicsaccelerate/document.md#ga21f86a194e72e99dd54fd39080385a37) API to generate a predicted frame. This API is used to associate the image resources in a game app with the frame generation algorithm implementation.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_DestroyImage\_VK](../../../modules/graphicsaccelerate/document.md#gac850c7cd41a1aebaf9bcf943ebff372a)([FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7)\* context, [FG\_Image\_VK](../../../modules/graphicsaccelerate/document.md#gabd6ee9704e997ffc2792ad3c89847019)\* image)

 | 

Destroys input and output image instances for frame generation and cancels the corresponding association.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_Activate\_VK](../../../modules/graphicsaccelerate/document.md#ga6871faa08ebf19d380301cf400c086a8)([FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7)\* context)

 | 

Activates a frame generation context instance. Before the activation, the instance attributes must be set. For an activated frame generation context instance, the [HMS\_FG\_Dispatch\_VK](../../../modules/graphicsaccelerate/document.md#ga21f86a194e72e99dd54fd39080385a37) API can be called to generate a predicted frame. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_Deactivate\_VK](../../../modules/graphicsaccelerate/document.md#gad52fbbb8dcfd929300224cb91ce96380)([FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7)\* context)

 | 

Deactivates a frame generation context instance. To activate the instance again, call the [HMS\_FG\_Activate\_VK](../../../modules/graphicsaccelerate/document.md#ga6871faa08ebf19d380301cf400c086a8) API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_IsActive\_VK](../../../modules/graphicsaccelerate/document.md#ga2b8aea406b51b42083c740fbe44b3ad1)([FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7)\* context, bool\* isActive)

 | 

Queries whether a frame generation context instance is activated. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_Dispatch\_VK](../../../modules/graphicsaccelerate/document.md#ga21f86a194e72e99dd54fd39080385a37)([FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7)\* context, const [FG\_DispatchDescription\_VK](../../structs/fg-dispatchdescription-vk/document.md)\* desc)

 | 

Sets the parameter information required for frame prediction to generate a predicted frame. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_DestroyContext\_VK](../../../modules/graphicsaccelerate/document.md#ga6be707669124e0bb6e5d61c2e24043be)([FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7)\*\* context)

 | 

Destroys a frame generation context instance and releases memory resources. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga394c554fc5d056d702180ee031ccee2c) [HMS\_FG\_SetIntegrationMode\_VK](../../../modules/graphicsaccelerate/document.md#section1557174711191)([FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7)\* context, const [FG\_IntegrationInfo](../../structs/fg-integrationinfo/document.md)\* integrationInfo)

 | 

Sets the integration information for frame generation. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga394c554fc5d056d702180ee031ccee2c) [HMS\_FG\_SetUiPredictionEnabled\_VK](../../../modules/graphicsaccelerate/document.md#section9619114861914)([FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7)\* context, bool isEnabled)

 | 

Sets whether to enable the UI prediction function. This function can be enabled only in system display mode. It is invalid in game display mode. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga394c554fc5d056d702180ee031ccee2c) [HMS\_FG\_SetTargetFps\_VK](../../../modules/graphicsaccelerate/document.md#section655214195204)([FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7)\* context, int targetFps)

 | 

Sets the target frame rate for frame generation. The setting takes effect only for the system display mode and is invalid for the game display mode. This API takes effect after the game is released for the first time and applies only to the Vulkan graphics API.

 |
