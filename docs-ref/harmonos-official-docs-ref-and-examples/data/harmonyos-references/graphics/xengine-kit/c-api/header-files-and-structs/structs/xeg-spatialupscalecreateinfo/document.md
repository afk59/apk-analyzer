# XEG\_SpatialUpscaleCreateInfo

#### Overview

This structure describes the information for creating an [XEG\_SpatialUpscale](../../../modules/xengine/document.md#xeg_spatialupscale) object. When the information in the structure changes, a new XEG\_SpatialUpscale object needs to be created.

**Since:** 5.0.0(12)

**Related Modules:**[XEngine](../../../modules/xengine/document.md)

**Header file**: [xeg\_vulkan\_spatial\_upscale.h](../../header-files/xeg-vulkan-spatial-upscale-h/document.md)

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

Size of the upscaling image. The size must be the same as that of VkimageView of the image to be upscaled. Otherwise, undefined problems may occur, such as upscaling failure and program crash.

 |
| 

VkRect2D [inputRegion](#inputregion)

 | 

Sampling region of the upscaling image. The value of this parameter must be greater than 0 and less than or equal to the image size. Otherwise, the rendering fails or the rendering effect is unexpected. This parameter has two structures: VkOffset2D offset and VkExtent2D extent. offset defines the x and y coordinates of the upper left corner of the image region, and extent defines the width and height of the image region.

 |
| 

VkExtent2D [outputSize](#outputsize)

 | 

Size of the upscaled image. The size must be the same as that of VkimageView of the upscaled image. Otherwise, undefined problems may occur, such as upscaling failure and program crash.

 |
| 

VkRect2D [outputRegion](#outputregion)

 | 

Drawing region of the upscaling image. The value of this parameter must be greater than 0 and less than or equal to the image size. Otherwise, the rendering fails or the rendering effect is unexpected. This parameter has two structures: VkOffset2D offset and VkExtent2D extent. offset defines the x and y coordinates of the upper left corner of the image region, and extent defines the width and height of the image region.

 |
| 

VkFormat [format](#format)

 | 

Format of the upscaled image.

 |
| 

float [sharpness](#sharpness)

 | 

Sharpness for upscaling. The recommended value range is \[0, 1\]. The sharpness needs to be adjusted for images of different styles. Otherwise, over-sharpening will occur, for example, the image may contain excessive noise.

 |

#### Field

#### \[h2\]format

VkFormat XEG\_SpatialUpscaleCreateInfo::format

**Description**

Format of the upscaled image.

#### \[h2\]inputRegion

VkRect2D XEG\_SpatialUpscaleCreateInfo::inputRegion

**Description**

Sampling region of the upscaling image. The value of this parameter must be greater than 0 and less than or equal to the image size. Otherwise, the rendering fails or the rendering effect is unexpected. This parameter has two structures: VkOffset2D offset and VkExtent2D extent. offset defines the x and y coordinates of the upper left corner of the image region, and extent defines the width and height of the image region.

#### \[h2\]inputSize

VkExtent2D XEG\_SpatialUpscaleCreateInfo::inputSize

**Description**

Size of the upscaling image. The size must be the same as that of VkimageView of the image to be upscaled. Otherwise, undefined problems may occur, such as upscaling failure and program crash.

#### \[h2\]outputRegion

VkRect2D XEG\_SpatialUpscaleCreateInfo::outputRegion

**Description**

Drawing region of the upscaling image. The value of this parameter must be greater than 0 and less than or equal to the image size. Otherwise, the rendering fails or the rendering effect is unexpected. This parameter has two structures: VkOffset2D offset and VkExtent2D extent. offset defines the x and y coordinates of the upper left corner of the image region, and extent defines the width and height of the image region.

#### \[h2\]outputSize

VkExtent2D XEG\_SpatialUpscaleCreateInfo::outputSize

**Description**

Size of the upscaled image. The size must be the same as that of VkimageView of the upscaled image. Otherwise, undefined problems may occur, such as upscaling failure and program crash.

#### \[h2\]sharpness

float XEG\_SpatialUpscaleCreateInfo::sharpness

**Description**

Sharpness for upscaling. The recommended value range is \[0, 1\]. The sharpness needs to be adjusted for images of different styles. Otherwise, over-sharpening will occur, for example, the image may contain excessive noise.
