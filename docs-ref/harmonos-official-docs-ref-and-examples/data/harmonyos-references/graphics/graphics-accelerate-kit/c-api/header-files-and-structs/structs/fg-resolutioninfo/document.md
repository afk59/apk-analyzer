# FG\_ResolutionInfo

#### Overview

Describes the resolutions of input and output images for frame generation.

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

[FG\_Dimension2D](../fg-dimension2d/document.md) [inputColorResolution](#af99a47a1f71f8c13d8f5dff8ac02d137)

 | 

Resolution of the color buffer of real frames.

 |
| 

[FG\_Dimension2D](../fg-dimension2d/document.md) [inputDepthStencilResolution](#a0938887b43f2d9353d836a95c1ce0c81)

 | 

Resolution of the depth stencil buffer of real frames. When this variable is set to **0**, the system will use the value of [inputColorResolution](#af99a47a1f71f8c13d8f5dff8ac02d137) as the resolution of the depth stencil buffer of real frames.

 |
| 

[FG\_Dimension2D](../fg-dimension2d/document.md) [outputColorResolution](#a69fd8491d75c622c2a21bc0278278965)

 | 

Resolution of the predicted frame buffer. When this variable is set to **0**, the system will use the value of [inputColorResolution](#af99a47a1f71f8c13d8f5dff8ac02d137) as the resolution of the predicted frame buffer.

 |

#### Member Variable Description

#### \[h2\]inputColorResolution

[FG\_Dimension2D](../fg-dimension2d/document.md) FG\_ResolutionInfo::inputColorResolution

**Description**

Resolution of the color buffer of real frames.

#### \[h2\]inputDepthStencilResolution

[FG\_Dimension2D](../fg-dimension2d/document.md) FG\_ResolutionInfo::inputDepthStencilResolution

**Description**

Resolution of the depth stencil buffer of real frames. When this variable is set to **0**, the system will use the value of [inputColorResolution](#af99a47a1f71f8c13d8f5dff8ac02d137) as the resolution of the depth stencil buffer of real frames.

#### \[h2\]outputColorResolution

[FG\_Dimension2D](../fg-dimension2d/document.md) FG\_ResolutionInfo::outputColorResolution

**Description**

Resolution of the predicted frame buffer. When this variable is set to **0**, the system will use the value of [inputColorResolution](#af99a47a1f71f8c13d8f5dff8ac02d137) as the resolution of the predicted frame buffer.
