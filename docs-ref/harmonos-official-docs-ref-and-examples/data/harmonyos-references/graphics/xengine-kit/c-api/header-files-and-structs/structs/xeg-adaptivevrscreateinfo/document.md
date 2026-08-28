# XEG\_AdaptiveVRSCreateInfo

#### Overview

This structure describes the parameter information for creating an [XEG\_AdaptiveVRS](../../../modules/xengine/document.md#xeg_adaptivevrs) object. When the information in the structure changes, a new [XEG\_AdaptiveVRS](../../../modules/xengine/document.md#xeg_adaptivevrs) object needs to be created.

**Since:** 5.0.0(12)

**Related Modules:**[XEngine](../../../modules/xengine/document.md)

**Header file**: [xeg\_vulkan\_adaptive\_vrs.h](../../header-files/xeg-vulkan-adaptive-vrs-h/document.md)

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

Image size finally rendered by the rendering pipeline of the previous frame.

 |
| 

VkRect2D [inputRegion](#inputregion)

 | 

Image region finally rendered by the rendering pipeline of the previous frame. This parameter has two structures: VkOffset2D offset and VkExtent2D extent. offset defines the x and y coordinates of the upper left corner of the rendered image region, and extent defines the width and height of the rendered image region.

 |
| 

int32\_t [adaptiveTileSize](#adaptivetilesize)

 | 

Tile size for adaptive VRS rendering. A larger tile size indicates better performance but deteriorated image quality. Currently, XEngine Adaptive VRS supports only two TileSize specifications: 16 and 8.

 |
| 

float [errorSensitivity](#errorsensitivity)

 | 

Threshold for generating the final shading rate texture result. A larger value indicates a smaller average shading rate, that is, the performance is better but the image quality deteriorates. The recommended value range is \[0, 1\].

 |
| 

bool [flip](#flip)

 | 

Indicates whether to flip an image. true: flip; false: not flip.

 |

#### Field

#### \[h2\]adaptiveTileSize

int32\_t XEG\_AdaptiveVRSCreateInfo::adaptiveTileSize

**Description**

Tile size for adaptive VRS rendering. A larger tile size indicates better performance but deteriorated image quality. Currently, XEngine Adaptive VRS supports only two TileSize specifications: 16 and 8.

#### \[h2\]errorSensitivity

float XEG\_AdaptiveVRSCreateInfo::errorSensitivity

**Description**

Threshold for generating the final shading rate texture result. A larger value indicates a smaller average shading rate, that is, the performance is better but the image quality deteriorates. The recommended value range is \[0, 1\].

#### \[h2\]flip

bool XEG\_AdaptiveVRSCreateInfo::flip

**Description**

Indicates whether to flip an image. true: flip; false: not flip.

#### \[h2\]inputRegion

VkRect2D XEG\_AdaptiveVRSCreateInfo::inputRegion

**Description**

Image region finally rendered by the rendering pipeline of the previous frame. This parameter has two structures: VkOffset2D offset and VkExtent2D extent. offset defines the x and y coordinates of the upper left corner of the rendered image region, and extent defines the width and height of the rendered image region.

#### \[h2\]inputSize

VkExtent2D XEG\_AdaptiveVRSCreateInfo::inputSize

**Description**

Image size finally rendered by the rendering pipeline of the previous frame.
