# FG\_ImageSync\_VK

#### Overview

Describes the synchronization status information about the input and output images for frame generation. It is used to create a memory barrier for the images.

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

VkAccessFlagBits [accessMask](#a196de1506cbe6e3d50af409137f0c2ba)

 | 

Bitmask specifying memory access types that will participate in a memory dependency.

 |
| 

VkImageLayout [layout](#a57ec08087e997e91c937dc30e0a26602)

 | 

Layout of image and image subresources.

 |
| 

VkPipelineStageFlagBits [stages](#af1041077c16e8d64f809d5fb42a615e0)

 | 

Bitmask specifying pipeline stages.

 |

#### Member Variable Description

#### \[h2\]accessMask

VkAccessFlagBits FG\_ImageSync\_VK::accessMask

**Description**

Bitmask specifying memory access types that will participate in a memory dependency.

#### \[h2\]layout

VkImageLayout FG\_ImageSync\_VK::layout

**Description**

Layout of image and image subresources.

#### \[h2\]stages

VkPipelineStageFlagBits FG\_ImageSync\_VK::stages

**Description**

Bitmask specifying pipeline stages.
