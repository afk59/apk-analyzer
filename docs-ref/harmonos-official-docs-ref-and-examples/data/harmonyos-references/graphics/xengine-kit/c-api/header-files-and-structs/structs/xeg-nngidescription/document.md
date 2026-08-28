# XEG\_NNGIDescription

#### Overview

This structure describes the information required for updating the NNGI to calculate the ray-traced global illumination.

**Since:** 6.0.0(20)

**Related Modules:**[XEngine](../../../modules/xengine/document.md)

**Header file**: [xeg\_vulkan\_rtgi.h](../../header-files/xeg-vulkan-rtgi-h/document.md)

#### Summary

#### \[h2\]Data Fields

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

XEG\_StructureType [sType](#stype)

 | 

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_NNGI\_DESCRIPTION.

 |
| 

const void \* [pNext](#pnext)

 | 

Pointer to the extended structure.

 |
| 

float [inferenceCameraViewMatrix](#inferencecameraviewmatrix) \[16\]

 | 

Camera view matrix of inference images, which must be a 4 x 4 matrix in column-major order.

 |
| 

float [inferenceCameraProjectionMatrix](#inferencecameraprojectionmatrix) \[16\]

 | 

Camera projection matrix of inference images, which must be a 4 x 4 matrix in column-major order.

 |
| 

VkImageView [inferenceInputDepthImage](#inferenceinputdepthimage)

 | 

Inference input depth image. The VkFormat value is VK\_FORMAT\_R16G16B16A16\_SFLOAT. The resolution is the same as that of inferenceInputSize in [XEG\_NNGICreateInfo](../xeg-nngicreateinfo/document.md).

 |
| 

VkImageView [inferenceInputNormalImage](#inferenceinputnormalimage)

 | 

Inference input normal image. The VkFormat value is VK\_FORMAT\_R16G16B16A16\_SFLOAT. The resolution is the same as that of inferenceInputSize in [XEG\_NNGICreateInfo](../xeg-nngicreateinfo/document.md).

 |
| 

VkImageView [inferenceInputBaseColorMetallicImage](#inferenceinputbasecolormetallicimage)

 | 

Inference input base color and metallic image. The VkFormat value is VK\_FORMAT\_R16G16B16A16\_SFLOAT. The resolution is the same as that of inferenceInputSize in [XEG\_NNGICreateInfo](../xeg-nngicreateinfo/document.md).

 |
| 

VkImageView [inferenceOutputGIImage](#inferenceoutputgiimage)

 | 

Inference output GI image. The VkFormat value is VK\_FORMAT\_R8G8B8A8\_SRGB. The resolution is the same as that of inferenceOutputSize in [XEG\_NNGICreateInfo](../xeg-nngicreateinfo/document.md).

 |
| 

float [trainingCameraViewMatrix](#trainingcameraviewmatrix) \[16\]

 | 

Camera view matrix of training images, which must be a 4 x 4 matrix in column-major order.

 |
| 

float [trainingCameraProjectionMatrix](#trainingcameraprojectionmatrix) \[16\]

 | 

Camera projection matrix of training images, which must be a 4 x 4 matrix in column-major order.

 |
| 

VkImageView [trainingInputPositionImage](#traininginputpositionimage)

 | 

Training input position image. The VkFormat value is VK\_FORMAT\_R16G16B16A16\_SFLOAT.

 |
| 

VkImageView [trainingInputNormalImage](#traininginputnormalimage)

 | 

Training input normal image. The VkFormat value is VK\_FORMAT\_R16G16B16A16\_SFLOAT.

 |
| 

VkImageView [trainingInputBaseColorMetallicImage](#traininginputbasecolormetallicimage)

 | 

Training input base color and metallic image. The VkFormat value is VK\_FORMAT\_R16G16B16A16\_SFLOAT.

 |
| 

VkImageView [trainingInputGIImage](#traininginputgiimage)

 | 

Training input GI image. The VkFormat value is VK\_FORMAT\_R16G16B16A16\_SFLOAT. A higher quality of the GI result of training images indicates a higher quality of the GI result output by the inference.

 |
| 

VkAabbPositionsKHR [sceneAabb](#sceneaabb)

 | 

Rendering bounding box range.

 |
| 

bool [isSceneUnbounded](#issceneunbounded) = false

 | 

Whether the rendering scene is unbounded. Currently, only false is supported.

 |
| 

float [spatialScaleFactor](#spatialscalefactor) = 0

 | 

Scene scaling factor. For bounded scenes, this parameter does not need to be set. XEngine calculates the value based on sceneAabb. For unbounded scenes, you are advised to set this parameter to the average depth.

 |

#### Field

#### \[h2\]inferenceCameraProjectionMatrix

float XEG\_NNGIDescription::inferenceCameraProjectionMatrix\[16\]

**Description**

Camera projection matrix of inference images, which must be a 4 x 4 matrix in column-major order.

#### \[h2\]inferenceCameraViewMatrix

float XEG\_NNGIDescription::inferenceCameraViewMatrix\[16\]

**Description**

Camera view matrix of inference images, which must be a 4 x 4 matrix in column-major order.

#### \[h2\]inferenceInputBaseColorMetallicImage

VkImageView XEG\_NNGIDescription::inferenceInputBaseColorMetallicImage

**Description**

Inference input base color and metallic image. The VkFormat value is VK\_FORMAT\_R16G16B16A16\_SFLOAT. The resolution is the same as that of inferenceInputSize in [XEG\_NNGICreateInfo](../xeg-nngicreateinfo/document.md).

#### \[h2\]inferenceInputDepthImage

VkImageView XEG\_NNGIDescription::inferenceInputDepthImage

**Description**

Inference input depth image. The VkFormat value is VK\_FORMAT\_R16G16B16A16\_SFLOAT. The resolution is the same as that of inferenceInputSize in [XEG\_NNGICreateInfo](../xeg-nngicreateinfo/document.md).

#### \[h2\]inferenceInputNormalImage

VkImageView XEG\_NNGIDescription::inferenceInputNormalImage

**Description**

Inference input normal image. The VkFormat value is VK\_FORMAT\_R16G16B16A16\_SFLOAT. The resolution is the same as that of inferenceInputSize in [XEG\_NNGICreateInfo](../xeg-nngicreateinfo/document.md).

#### \[h2\]inferenceOutputGIImage

VkImageView XEG\_NNGIDescription::inferenceOutputGIImage

**Description**

Inference output GI image. The VkFormat value is VK\_FORMAT\_R8G8B8A8\_SRGB. The resolution is the same as that of inferenceOutputSize in [XEG\_NNGICreateInfo](../xeg-nngicreateinfo/document.md).

#### \[h2\]isSceneUnbounded

bool XEG\_NNGIDescription::isSceneUnbounded = false

**Description**

Whether the rendering scene is unbounded. Currently, only false is supported.

#### \[h2\]pNext

const void\* XEG\_NNGIDescription::pNext

**Description**

Pointer to the extended structure.

#### \[h2\]sceneAabb

VkAabbPositionsKHR XEG\_NNGIDescription::sceneAabb

**Description**

Rendering bounding box range.

#### \[h2\]spatialScaleFactor

float XEG\_NNGIDescription::spatialScaleFactor = 0

**Description**

Scene scaling factor. For bounded scenes, this parameter does not need to be set. XEngine calculates the value based on sceneAabb. For unbounded scenes, you are advised to set this parameter to the average depth.

#### \[h2\]sType

XEG\_StructureType XEG\_NNGIDescription::sType

**Description**

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_NNGI\_DESCRIPTION.

#### \[h2\]trainingCameraProjectionMatrix

float XEG\_NNGIDescription::trainingCameraProjectionMatrix\[16\]

**Description**

Camera projection matrix of training images, which must be a 4 x 4 matrix in column-major order.

#### \[h2\]trainingCameraViewMatrix

float XEG\_NNGIDescription::trainingCameraViewMatrix\[16\]

**Description**

Camera view matrix of training images, which must be a 4 x 4 matrix in column-major order.

#### \[h2\]trainingInputBaseColorMetallicImage

VkImageView XEG\_NNGIDescription::trainingInputBaseColorMetallicImage

**Description**

Training input base color and metallic image. The VkFormat value is VK\_FORMAT\_R16G16B16A16\_SFLOAT.

#### \[h2\]trainingInputGIImage

VkImageView XEG\_NNGIDescription::trainingInputGIImage

**Description**

Training input GI image. The VkFormat value is VK\_FORMAT\_R16G16B16A16\_SFLOAT. A higher quality of the GI result of training images indicates a higher quality of the GI result output by the inference.

#### \[h2\]trainingInputNormalImage

VkImageView XEG\_NNGIDescription::trainingInputNormalImage

**Description**

Training input normal image. The VkFormat value is VK\_FORMAT\_R16G16B16A16\_SFLOAT.

## trainingInputPositionImage

VkImageView XEG\_NNGIDescription::trainingInputPositionImage

**Description**

Training input position image. The VkFormat value is VK\_FORMAT\_R16G16B16A16\_SFLOAT.
