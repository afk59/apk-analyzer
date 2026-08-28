# FG\_ImageFormat\_VK

#### Overview

Describes the input and output image format information for frame generation. This API applies only to the Vulkan graphics API.

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

VkFormat [inputColorFormat](#a09363220ef43f5006a2954d6906538f9)

 | 

Image format of the real frame color buffer.

 |
| 

VkFormat [inputDepthStencilFormat](#a1e1bfcba3b16941fd78ed5ed93af7a49)

 | 

Image format of the depth stencil buffer.

 |
| 

VkFormat [outputColorFormat](#adc87ed6f09c0fd7d07d1b85af3d715bb)

 | 

Image format of the predicted frame buffer.

 |

#### Member Variable Description

#### \[h2\]inputColorFormat

VkFormat FG\_ImageFormat\_VK::inputColorFormat

**Description**

Image format of the real frame color buffer.

#### \[h2\]inputDepthStencilFormat

VkFormat FG\_ImageFormat\_VK::inputDepthStencilFormat

**Description**

Image format of the depth stencil buffer.

#### \[h2\]outputColorFormat

VkFormat FG\_ImageFormat\_VK::outputColorFormat

**Description**

Image format of the predicted frame buffer.
