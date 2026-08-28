# FG\_DispatchDescription\_VK

#### Overview

Describes the parameter information required by [HMS\_FG\_Dispatch\_VK](../../../modules/graphicsaccelerate/document.md#ga21f86a194e72e99dd54fd39080385a37). The parameter information needs to be updated for each frame. This API applies only to the Vulkan graphics API.

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

[FG\_ImageInfo\_VK](../fg-imageinfo-vk/document.md) [inputColorInfo](#a7578dc22d86211692bc10f03d3e6bd80)

 | 

Image instance of the real frame color buffer. It is created by [HMS\_FG\_CreateImage\_VK](../../../modules/graphicsaccelerate/document.md#ga7733f097ea5f4ae4d2aa53d11d7e60ff) and destroyed by [HMS\_FG\_DestroyImage\_VK](../../../modules/graphicsaccelerate/document.md#gac850c7cd41a1aebaf9bcf943ebff372a).

 |
| 

[FG\_ImageInfo\_VK](../fg-imageinfo-vk/document.md) [inputDepthStencilInfo](#a8d769ac5e41a27c668d32e0819895de5)

 | 

Image instance of the real frame depth stencil buffer. It is created by [HMS\_FG\_CreateImage\_VK](../../../modules/graphicsaccelerate/document.md#ga7733f097ea5f4ae4d2aa53d11d7e60ff) and destroyed by [HMS\_FG\_DestroyImage\_VK](../../../modules/graphicsaccelerate/document.md#gac850c7cd41a1aebaf9bcf943ebff372a).

 |
| 

[FG\_ImageInfo\_VK](../fg-imageinfo-vk/document.md) [outputColorInfo](#a50597ac7da9fc3292f0ebc1a9e36157c)

 | 

Image instance of the predicted frame buffer. It is created by [HMS\_FG\_CreateImage\_VK](../../../modules/graphicsaccelerate/document.md#ga7733f097ea5f4ae4d2aa53d11d7e60ff) and destroyed by [HMS\_FG\_DestroyImage\_VK](../../../modules/graphicsaccelerate/document.md#gac850c7cd41a1aebaf9bcf943ebff372a).

 |
| 

[FG\_Mat4x4](../fg-mat4x4/document.md) [viewProj](#abfad453e18fe901b2e7539b96e45a02a)

 | 

View projection matrix of real frames, that is, the matrix used for coordinate system conversion from the world space to the camera clip space. The matrix must be a 4x4 matrix in column-major order.

 |
| 

[FG\_Mat4x4](../fg-mat4x4/document.md) [invViewProj](#a2edcff364646e5bd4506e96a6e6fd863)

 | 

Inverse view projection matrix of real frames, that is, the matrix used for coordinate system conversion from the camera clip space to the world space. The matrix must be a 4x4 matrix in column-major order.

 |
| 

VkCommandBuffer [vkCommandBuffer](#a4c42121e915c5293c142f0737ff242d3)

 | 

Command buffer used to record frame drawing commands.

 |
| 

uint8\_t [frameIdx](#acffef3d1baef878cd923ec2e1709c80b)

 | 

Sequence number of the current frame. The sequence number starts from 0. The value must be less than that of **framesInFlight** in [FG\_ContextDescription\_VK](../fg-contextdescription-vk/document.md).

 |

#### Member Variable Description

#### \[h2\]frameIdx

uint8\_t FG\_DispatchDescription\_VK::frameIdx

**Description**

Sequence number of the current frame. The sequence number starts from 0. The value must be less than that of **framesInFlight** in [FG\_ContextDescription\_VK](../fg-contextdescription-vk/document.md).

#### \[h2\]inputColorInfo

[FG\_ImageInfo\_VK](../fg-imageinfo-vk/document.md) FG\_DispatchDescription\_VK::inputColorInfo

**Description**

Image instance of the real frame color buffer. It is created by [HMS\_FG\_CreateImage\_VK](../../../modules/graphicsaccelerate/document.md#ga7733f097ea5f4ae4d2aa53d11d7e60ff) and destroyed by [HMS\_FG\_DestroyImage\_VK](../../../modules/graphicsaccelerate/document.md#gac850c7cd41a1aebaf9bcf943ebff372a).

#### \[h2\]inputDepthStencilInfo

[FG\_ImageInfo\_VK](../fg-imageinfo-vk/document.md) FG\_DispatchDescription\_VK::inputDepthStencilInfo

**Description**

Image instance of the real frame depth stencil buffer. It is created by [HMS\_FG\_CreateImage\_VK](../../../modules/graphicsaccelerate/document.md#ga7733f097ea5f4ae4d2aa53d11d7e60ff) and destroyed by [HMS\_FG\_DestroyImage\_VK](../../../modules/graphicsaccelerate/document.md#gac850c7cd41a1aebaf9bcf943ebff372a).

#### \[h2\]invViewProj

[FG\_Mat4x4](../fg-mat4x4/document.md) FG\_DispatchDescription\_VK::invViewProj

**Description**

Inverse view projection matrix of real frames, that is, the matrix used for coordinate system conversion from the camera clip space to the world space. The matrix must be a 4x4 matrix in column-major order.

#### \[h2\]outputColorInfo

[FG\_ImageInfo\_VK](../fg-imageinfo-vk/document.md) FG\_DispatchDescription\_VK::outputColorInfo

**Description**

Image instance of the predicted frame buffer. It is created by [HMS\_FG\_CreateImage\_VK](../../../modules/graphicsaccelerate/document.md#ga7733f097ea5f4ae4d2aa53d11d7e60ff) and destroyed by [HMS\_FG\_DestroyImage\_VK](../../../modules/graphicsaccelerate/document.md#gac850c7cd41a1aebaf9bcf943ebff372a).

#### \[h2\]viewProj

[FG\_Mat4x4](../fg-mat4x4/document.md) FG\_DispatchDescription\_VK::viewProj

**Description**

View projection matrix of real frames, that is, the matrix used for coordinate system conversion from the world space to the camera clip space. The matrix must be a 4x4 matrix in column-major order.

#### \[h2\]vkCommandBuffer

VkCommandBuffer FG\_DispatchDescription\_VK::vkCommandBuffer

**Description**

Command buffer used to record frame drawing commands.
