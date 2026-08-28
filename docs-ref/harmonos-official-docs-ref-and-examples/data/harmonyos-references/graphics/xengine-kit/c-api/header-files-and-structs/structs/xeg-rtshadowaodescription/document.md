# XEG\_RTShadowAODescription

#### Overview

This structure describes the input information of the rendering command for the Ray-Traced Shadow and Ambient Occlusion algorithms.

**Since:** 6.0.0(20)

**Related Modules:**[XEngine](../../../modules/xengine/document.md)

**Header file**: [xeg\_vulkan\_rt\_visible\_mask.h](../../header-files/xeg-vulkan-rt-visible-mask-h/document.md)

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

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_DESCRIPTION.

 |
| 

const void \* [pNext](#pnext)

 | 

Pointer to the extended structure.

 |
| 

VkImageView [inputDepthImage](#inputdepthimage)

 | 

Depth image, which cannot be null.

 |
| 

VkImageView [inputNormalImage](#inputnormalimage)

 | 

Normal image, which cannot be null. The value must be in unsigned floating-point format and contain more than three channels, for example, VK\_FORMAT\_R8G8B8\_UNORM. XEngine parses the normal vector using the formula: Normal=textureLod(inputNormalImage).xyz\*2.0–1.0.

 |
| 

VkImageView [inputMotionVectorImage](#inputmotionvectorimage)

 | 

Motion vector image, which can be null. The motion vector is computed by subtracting the X and Y values of the NDC coordinates of the previous frame from those of the current rendered pixel. The image format must be VK\_FORMAT\_R16G16\_SFLOAT or higher.

 |
| 

VkImageView [outputShadowAOImage](#outputshadowaoimage)

 | 

Output shadow and ambient occlusion image, which cannot be null. The format must be VK\_FORMAT\_R8G8\_UNORM. The shadow value is written to the R channel, and the ambient occlusion value is written to the G channel.

 |
| 

VkAccelerationStructureKHR [accelerationStructure](#accelerationstructure)

 | 

Top-level Acceleration Structure of the scene.

 |
| 

bool [isAsInTranslatedSpace](#section12304204164113)

 | 

Indicates whether the ray tracing acceleration structure is built in the translated world space. The value true indicates it is built in the translated world space, and false indicates it is built in the absolute world space. The default value is false.

 |
| 

float [translatedViewMatrix](#section37620432414)

 | 

Camera translated view matrix, which must be a 4 x 4 matrix in column-major order. It can be left unassigned when the value of isAsInTranslatedSpace is false.

 |
| 

float [viewMatrix](#viewmatrix) \[16\]

 | 

Camera view matrix, which must be a 4 x 4 matrix in column-major order.

 |
| 

float [projectionMatrix](#projectionmatrix) \[16\]

 | 

Camera projection matrix, which must be a 4 x 4 matrix in column-major order.

 |
| 

float [worldCameraOrigin](#worldcameraorigin) \[3\]

 | 

Position coordinates of the camera in the world space.

 |
| 

bool [ndcFilpY](#section145279466411)

 | 

Indicates whether there is a Y-axis flip relationship between the NDC space and the world space. The value true indicates a flip, and false indicates no flip. The default value is false.

 |
| 

const [XEG\_RTShadowParameters](../xeg-rtshadowparameters/document.md) \* [pRtShadowParameters](#prtshadowparameters)

 | 

Ray-Traced Shadow algorithm parameter, which cannot be null when the [XEG\_RTShadowAOCreateInfo::enableRTShadow](../xeg-rtshadowaocreateinfo/document.md#enablertshadow) value is true.

 |
| 

const [XEG\_RTAOParameters](../xeg-rtaoparameters/document.md) \* [pRtAOParameters](#prtaoparameters)

 | 

Ray-Traced Ambient Occlusion algorithm parameter, which cannot be null when the [XEG\_RTShadowAOCreateInfo::enableRTAO](../xeg-rtshadowaocreateinfo/document.md#enablertao) value is true.

 |
| 

const [XEG\_RTShadowAODenoiserParameters](../xeg-rtshadowaodenoiserparameters/document.md) \* [pRtShadowAODenoiserParameters](#prtshadowaodenoiserparameters)

 | 

Denoising parameter, which cannot be null. Ray-Traced Shadow and Ambient Occlusion use the same denoising parameter.

 |

#### Field

#### \[h2\]accelerationStructure

VkAccelerationStructureKHR XEG\_RTShadowAODescription::accelerationStructure

**Description**

Top-level Acceleration Structure of the scene.

#### \[h2\]inputDepthImage

VkImageView XEG\_RTShadowAODescription::inputDepthImage

**Description**

Depth image, which cannot be null.

#### \[h2\]inputMotionVectorImage

VkImageView XEG\_RTShadowAODescription::inputMotionVectorImage

**Description**

Motion vector image, which can be null. The motion vector is computed by subtracting the X and Y values of the NDC coordinates of the previous frame from those of the current rendered pixel. The image format must be VK\_FORMAT\_R16G16\_SFLOAT or higher.

#### \[h2\]inputNormalImage

VkImageView XEG\_RTShadowAODescription::inputNormalImage

**Description**

Normal image, which cannot be null. The value must be in unsigned floating-point format and contain more than three channels, for example, VK\_FORMAT\_R8G8B8\_UNORM. XEngine parses the normal vector using the formula: Normal=textureLod(inputNormalImage).xyz\*2.0–1.0.

#### \[h2\]outputShadowAOImage

VkImageView XEG\_RTShadowAODescription::outputShadowAOImage

**Description**

Output shadow and ambient occlusion image, which cannot be null. The format must be VK\_FORMAT\_R8G8\_UNORM. The shadow value is written to the R channel, and the ambient occlusion value is written to the G channel.

#### \[h2\]pNext

const void\* XEG\_RTShadowAODescription::pNext

**Description**

Pointer to the extended structure.

#### \[h2\]projectionMatrix

float XEG\_RTShadowAODescription::projectionMatrix\[16\]

**Description**

Camera projection matrix, which must be a 4 x 4 matrix in column-major order.

#### \[h2\]pRtAOParameters

const XEG\_RTAOParameters\* XEG\_RTShadowAODescription::pRtAOParameters

**Description**

Ray-Traced Ambient Occlusion algorithm parameter, which cannot be null when the [XEG\_RTShadowAOCreateInfo::enableRTAO](../xeg-rtshadowaocreateinfo/document.md#enablertao) value is true.

#### \[h2\]pRtShadowAODenoiserParameters

const XEG\_RTShadowAODenoiserParameters\* XEG\_RTShadowAODescription::pRtShadowAODenoiserParameters

**Description**

Denoising parameter, which cannot be null. Ray-Traced Shadow and Ambient Occlusion use the same denoising parameter.

#### \[h2\]pRtShadowParameters

const XEG\_RTShadowParameters\* XEG\_RTShadowAODescription::pRtShadowParameters

**Description**

Ray-Traced Shadow algorithm parameter, which cannot be null when the [XEG\_RTShadowAOCreateInfo::enableRTShadow](../xeg-rtshadowaocreateinfo/document.md#enablertshadow) value is true.

#### \[h2\]sType

XEG\_StructureType XEG\_RTShadowAODescription::sType

**Description**

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_DESCRIPTION.

#### \[h2\]viewMatrix

float XEG\_RTShadowAODescription::viewMatrix\[16\]

**Description**

Camera view matrix, which must be a 4 x 4 matrix in column-major order.

#### \[h2\]worldCameraOrigin

float XEG\_RTShadowAODescription::worldCameraOrigin\[3\]

**Description**

Position coordinates of the camera in the world space.

#### \[h2\]isAsInTranslatedSpace

float XEG\_RTShadowAODescription::isAsInTranslatedSpace

**Description**

Indicates whether the ray tracing acceleration structure is built in the translated world space. The value true indicates it is built in the translated world space, and false indicates it is built in the absolute world space. The default value is false.

#### \[h2\]translatedViewMatrix

float XEG\_RTShadowAODescription::translatedViewMatrix\[16\]

**Description**

Camera translated view matrix, which must be a 4 x 4 matrix in column-major order. It can be left unassigned when the value of isAsInTranslatedSpace is false.

#### \[h2\]ndcFilpY

float XEG\_RTShadowAODescription::ndcFilpY

**Description**

Indicates whether there is a Y-axis flip relationship between the NDC space and the world space. The value true indicates a flip, and false indicates no flip. The default value is false.
