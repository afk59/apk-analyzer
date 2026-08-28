# FG\_ImageInfo\_VK

#### Overview

Describes the input and output image information for frame generation.

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

[FG\_Image\_VK](../../../modules/graphicsaccelerate/document.md#gabd6ee9704e997ffc2792ad3c89847019)\* [image](#af7d7acd5e8c8ea5968966fd5dae79c53)

 | 

Pointer to an [FG\_Image\_VK](../../../modules/graphicsaccelerate/document.md#gabd6ee9704e997ffc2792ad3c89847019) object. The image instance is created by [HMS\_FG\_CreateImage\_VK](../../../modules/graphicsaccelerate/document.md#ga7733f097ea5f4ae4d2aa53d11d7e60ff) and destroyed by [HMS\_FG\_DestroyImage\_VK](../../../modules/graphicsaccelerate/document.md#gac850c7cd41a1aebaf9bcf943ebff372a).

 |
| 

[FG\_ImageSync\_VK](../fg-imagesync-vk/document.md) [initialSync](#ac14678edc22ab154772896a680f65038)

 | 

Synchronization status of an image before [HMS\_FG\_Dispatch\_VK](../../../modules/graphicsaccelerate/document.md#ga21f86a194e72e99dd54fd39080385a37) is executed.

 |
| 

[FG\_ImageSync\_VK](../fg-imagesync-vk/document.md) [finalSync](#ab14f8dc283ce6e769d0d598bc3c812a8)

 | 

Synchronization status of an image after [HMS\_FG\_Dispatch\_VK](../../../modules/graphicsaccelerate/document.md#ga21f86a194e72e99dd54fd39080385a37) is executed.

 |

#### Member Variable Description

#### \[h2\]finalSync

[FG\_ImageSync\_VK](../fg-imagesync-vk/document.md) FG\_ImageInfo\_VK::finalSync

**Description**

Synchronization status of an image after [HMS\_FG\_Dispatch\_VK](../../../modules/graphicsaccelerate/document.md#ga21f86a194e72e99dd54fd39080385a37) is executed.

#### \[h2\]image

[FG\_Image\_VK](../../../modules/graphicsaccelerate/document.md#gabd6ee9704e997ffc2792ad3c89847019)\* FG\_ImageInfo\_VK::image

**Description**

Pointer to an [FG\_Image\_VK](../../../modules/graphicsaccelerate/document.md#gabd6ee9704e997ffc2792ad3c89847019) object. The image instance is created by [HMS\_FG\_CreateImage\_VK](../../../modules/graphicsaccelerate/document.md#ga7733f097ea5f4ae4d2aa53d11d7e60ff) and destroyed by [HMS\_FG\_DestroyImage\_VK](../../../modules/graphicsaccelerate/document.md#gac850c7cd41a1aebaf9bcf943ebff372a).

#### \[h2\]initialSync

[FG\_ImageSync\_VK](../fg-imagesync-vk/document.md) FG\_ImageInfo\_VK::initialSync

**Description**

Synchronization status of an image before [HMS\_FG\_Dispatch\_VK](../../../modules/graphicsaccelerate/document.md#ga21f86a194e72e99dd54fd39080385a37) is executed.
