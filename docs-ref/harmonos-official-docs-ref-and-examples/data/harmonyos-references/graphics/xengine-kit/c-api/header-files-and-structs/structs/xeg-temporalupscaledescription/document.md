# XEG\_TemporalUpscaleDescription

#### Overview

This structure describes the input information for delivering AI temporal upscaling rendering command.

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

VkImageView [inputImage](#inputimage)

 | 

Input image.

 |
| 

VkImageView [depthImage](#depthimage)

 | 

Depth image.

 |
| 

VkImageView [motionVectorImage](#motionvectorimage)

 | 

Motion vector image. The motion vector is computed by subtracting the X and Y values of the NDC coordinates of the previous frame from those of the current rendered pixel. The image format must be VK\_FORMAT\_R16G16\_SFLOAT or higher.

 |
| 

VkImageView [dynamicMaskImage](#dynamicmaskimage)

 | 

Dynamic mask image of an object. The format must be VK\_FORMAT\_R8\_UNORM or its compatible format. The valid value of the R channel is 0.0, 0.2 or 1.0, where 0.0 indicates static objects, 0.2 indicates moving objects such as people, and 1.0 indicates special effects or translucent objects.

 |
| 

VkImageView [outputImage](#outputimage)

 | 

Output image.

 |
| 

float [jitterX](#jitterx)

 | 

Camera jitter in the X direction.

 |
| 

float [jitterY](#jittery)

 | 

Camera jitter in the Y direction.

 |
| 

bool [resetHistory](#resethistory)

 | 

Indicates whether to reset historical frame data. true: reset; false: not reset. The value true is recommended if upscaling is not used for historical frames but is used for the current frame.

 |
| 

float [steadyLevel](#steadylevel)

 | 

Indicates whether the picture is biased towards the current frame (less ghosting but more flickering) or historical frames (more ghosting but more stable) The value range is \[0.0, 1.0\]. A larger value indicates a larger bias towards historical frames.

 |

#### Field

#### \[h2\]depthImage

VkImageView XEG\_TemporalUpscaleDescription::depthImage

**Description**

Depth image.

#### \[h2\]dynamicMaskImage

VkImageView XEG\_TemporalUpscaleDescription::dynamicMaskImage

**Description**

Dynamic mask image of an object. The format must be VK\_FORMAT\_R8\_UNORM or its compatible format. The valid value of the R channel is 0.0, 0.2 or 1.0, where 0.0 indicates static objects, 0.2 indicates moving objects such as people, and 1.0 indicates special effects or translucent objects.

#### \[h2\]inputImage

VkImageView XEG\_TemporalUpscaleDescription::inputImage

**Description**

Input image.

#### \[h2\]jitterX

float XEG\_TemporalUpscaleDescription::jitterX

**Description**

Camera jitter in the X direction.

#### \[h2\]jitterY

float XEG\_TemporalUpscaleDescription::jitterY

**Description**

Camera jitter in the Y direction.

#### \[h2\]motionVectorImage

VkImageView XEG\_TemporalUpscaleDescription::motionVectorImage

**Description**

Motion vector image. The motion vector is computed by subtracting the X and Y values of the NDC coordinates of the previous frame from those of the current rendered pixel. The image format must be VK\_FORMAT\_R16G16\_SFLOAT or higher.

#### \[h2\]outputImage

VkImageView XEG\_TemporalUpscaleDescription::outputImage

**Description**

Output image.

#### \[h2\]resetHistory

bool XEG\_TemporalUpscaleDescription::resetHistory

**Description**

Indicates whether to reset historical frame data. true: reset; false: not reset. The value true is recommended if upscaling is not used for historical frames but is used for the current frame.

#### \[h2\]steadyLevel

float XEG\_TemporalUpscaleDescription::steadyLevel

**Description**

Indicates whether the picture is biased towards the current frame (less ghosting but more flickering) or historical frames (more ghosting but more stable) The value range is \[0.0, 1.0\]. A larger value indicates a larger bias towards historical frames.
