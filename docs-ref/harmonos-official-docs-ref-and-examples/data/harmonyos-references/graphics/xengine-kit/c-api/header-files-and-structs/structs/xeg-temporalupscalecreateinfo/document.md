# XEG\_TemporalUpscaleCreateInfo

#### Overview

This structure describes the information for creating an [XEG\_TemporalUpscale](../../../modules/xengine/document.md#xeg_temporalupscale) object. When the information in the structure changes, a new [XEG\_TemporalUpscale](../../../modules/xengine/document.md#xeg_temporalupscale) object needs to be created.

**Since:** 5.0.0(12)

**Related Modules:**[XEngine](../../../modules/xengine/document.md)

**Header file**: [xeg\_vulkan\_temporal\_upscale.h](../../header-files/xeg-vulkan-temporal-upscale-h/document.md)

#### Summary

#### \[h2\]Data Fields

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

VkExtent2D [inputSize](#inputsize)

 | 

Size of the input image. The maximum size supported is 2048 \* 1024.

 |
| 

VkExtent2D [outputSize](#outputsize)

 | 

Size of the output image.

 |
| 

VkRect2D [outputRegion](#outputregion)

 | 

Output image region of upscaling.

 |
| 

VkFormat [outputFormat](#outputformat)

 | 

Format of the output image.

 |
| 

int [jitterNum](#jitternum)

 | 

Number of camera jitter cycles. The value range is \[4, 16\]. The recommended value is 8.

 |
| 

bool [isDepthReversed](#isdepthreversed)

 | 

Indicates whether depth reversion exists. If 0.0 is used to indicate the farthest depth, set this parameter to true. Otherwise, set this parameter to false.

 |

#### Field

#### \[h2\]inputSize

VkExtent2D XEG\_TemporalUpscaleCreateInfo::inputSize

**Description**

Size of the input image. The maximum size supported is 2048 \* 1024.

#### \[h2\]isDepthReversed

bool XEG\_TemporalUpscaleCreateInfo::isDepthReversed

**Description**

Indicates whether depth reversion exists. If 0.0 is used to indicate the farthest depth, set this parameter to true. Otherwise, set this parameter to false.

#### \[h2\]jitterNum

int XEG\_TemporalUpscaleCreateInfo::jitterNum

**Description**

Number of camera jitter cycles. The value range is \[4, 16\]. The recommended value is 8.

#### \[h2\]outputFormat

VkFormat XEG\_TemporalUpscaleCreateInfo::outputFormat

**Description**

Format of the output image.

#### \[h2\]outputRegion

VkRect2D XEG\_TemporalUpscaleCreateInfo::outputRegion

**Description**

Output image region of upscaling.

#### \[h2\]outputSize

VkExtent2D XEG\_TemporalUpscaleCreateInfo::outputSize

**Description**

Size of the output image.
