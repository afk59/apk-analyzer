# XEG\_NNGICreateInfo

#### Overview

This structure describes the information about creating an [XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi) object with the NNGI feature. If the information in the structure changes, a new [XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi) object needs to be created.

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

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_NNGI\_CREATE\_INFO.

 |
| 

const void \* [pNext](#pnext)

 | 

Pointer to the extended structure.

 |
| 

XEG\_RTGIQualityMode [qualityMode](#qualitymode)

 | 

Quality mode of output images, which must be an enum in [XEG\_RTGIQualityMode](../../../modules/xengine/document.md#xeg_rtgiqualitymode).

 |
| 

VkExtent2D [inferenceInputSize](#inferenceinputsize)

 | 

Resolution of inference input images, which must be the same as that of the inference input images in [XEG\_NNGIDescription](../xeg-nngidescription/document.md).

 |
| 

VkExtent2D [inferenceOutputSize](#inferenceoutputsize)

 | 

Resolution of inference output images, which must be the same as that of the inference output images in [XEG\_NNGIDescription](../xeg-nngidescription/document.md). Currently, only (640, 368) is supported.

 |
| 

VkExtent2D [trainingSize](#trainingsize)

 | 

Resolution of training images, which must be the same as that of the training input and output images in [XEG\_NNGIDescription](../xeg-nngidescription/document.md). The recommended value is (64, 32).

 |

#### Field

#### \[h2\]inferenceInputSize

VkExtent2D XEG\_NNGICreateInfo::inferenceInputSize

**Description**

Resolution of inference input images, which must be the same as that of the inference input images in [XEG\_NNGIDescription](../xeg-nngidescription/document.md).

#### \[h2\]inferenceOutputSize

VkExtent2D XEG\_NNGICreateInfo::inferenceOutputSize

**Description**

Resolution of inference output images, which must be the same as that of the inference output images in [XEG\_NNGIDescription](../xeg-nngidescription/document.md). Currently, only (640, 368) is supported.

#### \[h2\]pNext

const void\* XEG\_NNGICreateInfo::pNext

**Description**

Pointer to the extended structure.

#### \[h2\]qualityMode

XEG\_RTGIQualityMode XEG\_NNGICreateInfo::qualityMode

**Description**

Quality mode of output images, which must be an enum in [XEG\_RTGIQualityMode](../../../modules/xengine/document.md#xeg_rtgiqualitymode).

#### \[h2\]sType

XEG\_StructureType XEG\_NNGICreateInfo::sType

**Description**

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_NNGI\_CREATE\_INFO.

## trainingSize

VkExtent2D XEG\_NNGICreateInfo::trainingSize

**Description**

Resolution of training images, which must be the same as that of the training input and output images in [XEG\_NNGIDescription](../xeg-nngidescription/document.md). The recommended value is (64, 32).
