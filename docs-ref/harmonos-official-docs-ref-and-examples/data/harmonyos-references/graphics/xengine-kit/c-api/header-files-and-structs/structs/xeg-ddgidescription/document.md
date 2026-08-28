# XEG\_DDGIDescription

#### Overview

This structure describes the information required for updating the DDGI probe irradiance and rendering the output GI images.

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

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_DDGI\_DESCRIPTION.

 |
| 

const void \* [pNext](#pnext)

 | 

Pointer to the extended structure.

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

VkImageView [inputNormalImage](#inputnormalimage)

 | 

Input Gbuffer normal image, whose width and height must be the same as those of viewSize in [XEG\_DDGICreateInfo](../xeg-ddgicreateinfo/document.md).

 |
| 

VkImageView [inputDepthImage](#inputdepthimage)

 | 

Input Gbuffer depth image, whose width and height must be the same as those of viewSize in [XEG\_DDGICreateInfo](../xeg-ddgicreateinfo/document.md).

 |
| 

VkImageView [inputBasecolorMetallicImage](#inputbasecolormetallicimage)

 | 

Input Gbuffer base color and metallic image, whose width and height must be the same as those of viewSize in [XEG\_DDGICreateInfo](../xeg-ddgicreateinfo/document.md).

 |
| 

VkImageView [inputDirectionImage](#inputdirectionimage)

 | 

Input probe rays direction image, whose width and height are the number of rays emitted by probes and the number of the input probes respectively.

 |
| 

VkImageView [inputRayRadianceDistanceImage](#inputrayradiancedistanceimage)

 | 

Input image indicating the radiance at the intersection point of the rays emitted by probes and the distance, whose width and height are the number of rays emitted by the probes and the number of the input probes respectively.

 |
| 

VkImageView [inputRayHitNormalAndMetallicImage](#inputrayhitnormalandmetallicimage)

 | 

Input image indicating the normal and metalness at the intersection point of the rays emitted by probes, whose width and height are the number of rays emitted by the probes and the number of the input probes respectively.

 |
| 

VkBuffer [inputVolumeIndexAndProbeIndex](#inputvolumeindexandprobeindex)

 | 

Index information of input probes, corresponding to the information about the rays emitted by the probes. Each data record consists of two uint values (probe index/volume index).

 |
| 

uint32\_t [inputProbeCount](#inputprobecount)

 | 

Number of input probes, corresponding to the number of valid data records in inputVolumeIndexAndProbeIndex.

 |
| 

VkBuffer [outputVolumeIndexAndProbeIndex](#outputvolumeindexandprobeindex)

 | 

Index information of output probes, indicating how the user emits rays in the next frame. Each data record consists of two uint values (probe index/volume index).

 |
| 

VkBuffer [outputProbeCount](#outputprobecount)

 | 

Number of output probes, corresponding to the number of valid data records in outputVolumeIndexAndProbeIndex.

 |
| 

VkImageView [outputGIImage](#outputgiimage)

 | 

Output GI 2D image, whose width and height must be the same as those of viewSize in [XEG\_DDGICreateInfo](../xeg-ddgicreateinfo/document.md). The VkFormat value is VK\_FORMAT\_R8G8B8A8\_UNORM.

 |
| 

uint32\_t [enableVolumeNumber](#enablevolumenumber)

 | 

Number of volumes used. The value must be less than or equal to the numberVolume value in [XEG\_DDGICreateInfo](../xeg-ddgicreateinfo/document.md).

 |
| 

const struct [XEG\_DDGIVolumeEntryParameters](../xeg-ddgivolumeentryparameters/document.md) \* [pVolumeEntryParameters](#pvolumeentryparameters)

 | 

Input volume parameter information, corresponding to [XEG\_DDGIVolumeEntryParameters](../xeg-ddgivolumeentryparameters/document.md). The size of the structure array must be equal to the enableVolumeNumber value.

 |

#### Field

#### \[h2\]enableVolumeNumber

uint32\_t XEG\_DDGIDescription::enableVolumeNumber

**Description**

Number of volumes used. The value must be less than or equal to the numberVolume value in [XEG\_DDGICreateInfo](../xeg-ddgicreateinfo/document.md).

#### \[h2\]inputBasecolorMetallicImage

VkImageView XEG\_DDGIDescription::inputBasecolorMetallicImage

**Description**

Input Gbuffer base color and metallic image, whose width and height must be the same as those of viewSize in [XEG\_DDGICreateInfo](../xeg-ddgicreateinfo/document.md).

#### \[h2\]inputDepthImage

VkImageView XEG\_DDGIDescription::inputDepthImage

**Description**

Input Gbuffer depth image, whose width and height must be the same as those of viewSize in [XEG\_DDGICreateInfo](../xeg-ddgicreateinfo/document.md).

#### \[h2\]inputDirectionImage

VkImageView XEG\_DDGIDescription::inputDirectionImage

**Description**

Input probe rays direction image, whose width and height are the number of rays emitted by probes and the number of the input probes respectively.

#### \[h2\]inputNormalImage

VkImageView XEG\_DDGIDescription::inputNormalImage

**Description**

Input Gbuffer normal image, whose width and height must be the same as those of viewSize in [XEG\_DDGICreateInfo](../xeg-ddgicreateinfo/document.md).

#### \[h2\]inputProbeCount

uint32\_t XEG\_DDGIDescription::inputProbeCount

**Description**

Number of input probes, corresponding to the number of valid data records in inputVolumeIndexAndProbeIndex.

#### \[h2\]inputRayHitNormalAndMetallicImage

VkImageView XEG\_DDGIDescription::inputRayHitNormalAndMetallicImage

**Description**

Input image indicating the normal and metalness at the intersection point of the rays emitted by probes, whose width and height are the number of rays emitted by the probes and the number of the input probes respectively.

#### \[h2\]inputRayRadianceDistanceImage

VkImageView XEG\_DDGIDescription::inputRayRadianceDistanceImage

**Description**

Input image indicating the radiance at the intersection point of the rays emitted by probes and the distance, whose width and height are the number of rays emitted by the probes and the number of the input probes respectively.

#### \[h2\]inputVolumeIndexAndProbeIndex

VkBuffer XEG\_DDGIDescription::inputVolumeIndexAndProbeIndex

**Description**

Index information of input probes, corresponding to the information about the rays emitted by the probes. Each data record consists of two uint values (probe index/volume index).

#### \[h2\]outputGIImage

VkImageView XEG\_DDGIDescription::outputGIImage

**Description**

Output GI 2D image, whose width and height must be the same as those of viewSize in [XEG\_DDGICreateInfo](../xeg-ddgicreateinfo/document.md). The VkFormat value is VK\_FORMAT\_R8G8B8A8\_UNORM.

#### \[h2\]outputProbeCount

VkBuffer XEG\_DDGIDescription::outputProbeCount

**Description**

Number of output probes, corresponding to the number of valid data records in outputVolumeIndexAndProbeIndex.

#### \[h2\]outputVolumeIndexAndProbeIndex

VkBuffer XEG\_DDGIDescription::outputVolumeIndexAndProbeIndex

**Description**

Index information of output probes, indicating how the user emits rays in the next frame. Each data record consists of two uint values (probe index/volume index).

#### \[h2\]pNext

const void\* XEG\_DDGIDescription::pNext

**Description**

Pointer to the extended structure.

#### \[h2\]projectionMatrix

float XEG\_DDGIDescription::projectionMatrix\[16\]

**Description**

Camera projection matrix, which must be a 4 x 4 matrix in column-major order.

#### \[h2\]pVolumeEntryParameters

const struct XEG\_DDGIVolumeEntryParameters\* XEG\_DDGIDescription::pVolumeEntryParameters

**Description**

Input volume parameter information, corresponding to [XEG\_DDGIVolumeEntryParameters](../xeg-ddgivolumeentryparameters/document.md). The size of the structure array must be equal to the enableVolumeNumber value.

#### \[h2\]sType

XEG\_StructureType XEG\_DDGIDescription::sType

**Description**

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_DDGI\_DESCRIPTION.

#### \[h2\]viewMatrix

float XEG\_DDGIDescription::viewMatrix\[16\]

**Description**

Camera view matrix, which must be a 4 x 4 matrix in column-major order.
