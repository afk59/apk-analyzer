# XEG\_AdaptiveVRSDescription

#### Overview

This structure describes the parameter information required for delivering the command for drawing the shading rate texture. The information needs to be updated for each frame.

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

float \* [reprojectionMatrix](#reprojectionmatrix)

 | 

The parameter is optional. If the parameter is not empty, the rendering result is better. Pointer to the reprojection matrix. The computation formula is as follows: (Projection matrix of the previous frame x Observation matrix of the previous frame) x (Inverse matrix of (Projection matrix of the current frame x Observation matrix of the current frame)). The matrix must be a 4 x 4 column major-order matrix.

 |
| 

VkImageView [inputColorImage](#inputcolorimage)

 | 

VkImageView of the color attachment containing the final rendering result of the rendering pipeline of the previous frame.

 |
| 

VkImageView [inputDepthImage](#inputdepthimage)

 | 

VkImageView of the depth attachment containing the rendering result of the rendering pipeline of the current frame.

 |
| 

VkImageView [outputShadingRateImage](#outputshadingrateimage)

 | 

VkImageView for generating the shading rate image information. The VkImageView needs to be created and entered by the user.

 |

#### Field

#### \[h2\]inputColorImage

VkImageView XEG\_AdaptiveVRSDescription::inputColorImage

**Description**

VkImageView of the color attachment containing the final rendering result of the rendering pipeline of the previous frame.

#### \[h2\]inputDepthImage

VkImageView XEG\_AdaptiveVRSDescription::inputDepthImage

**Description**

VkImageView of the depth attachment containing the rendering result of the rendering pipeline of the current frame.

#### \[h2\]outputShadingRateImage

VkImageView XEG\_AdaptiveVRSDescription::outputShadingRateImage

**Description**

VkImageView for generating the shading rate image information. The VkImageView needs to be created and entered by the user.

#### \[h2\]reprojectionMatrix

float\* XEG\_AdaptiveVRSDescription::reprojectionMatrix

**Description**

The parameter is optional. If the parameter is not empty, the rendering result is better. Pointer to the reprojection matrix. The computation formula is as follows: (Projection matrix of the previous frame x Observation matrix of the previous frame) x (Inverse matrix of (Projection matrix of the current frame x Observation matrix of the current frame)). The matrix must be a 4 x 4 column major-order matrix.
