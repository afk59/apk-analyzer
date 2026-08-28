# XEG\_SpatialUpscaleDescription

#### Overview

This structure describes the image information required for delivering the GPU spatial upscaling rendering command.

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

VkImageView [inputImage](#inputimage)

 | 

The VkImageView for upscaling must be valid. Otherwise, undefined behavior may occur, for example, rendering fails or the program crashes.

 |
| 

VkImageView [outputImage](#outputimage)

 | 

The upscaled VkImageView must be valid. Otherwise, undefined behavior may occur, for example, rendering fails or the program crashes.

 |

#### Field

#### \[h2\]inputImage

VkImageView XEG\_SpatialUpscaleDescription::inputImage

**Description**

The VkImageView for upscaling must be valid. Otherwise, undefined behavior may occur, for example, rendering fails or the program crashes.

#### \[h2\]outputImage

VkImageView XEG\_SpatialUpscaleDescription::outputImage

**Description**

The upscaled VkImageView must be valid. Otherwise, undefined behavior may occur, for example, rendering fails or the program crashes.
