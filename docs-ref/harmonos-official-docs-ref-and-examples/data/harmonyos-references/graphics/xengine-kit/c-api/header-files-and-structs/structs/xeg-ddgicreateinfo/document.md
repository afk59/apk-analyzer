# XEG\_DDGICreateInfo

#### Overview

This structure describes the information about creating an [XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi) object with the DDGI feature. If the information in the structure changes, a new [XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi) object needs to be created.

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

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_DDGI\_CREATE\_INFO.

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

uint32\_t [numberVolume](#numbervolume)

 | 

Maximum number of volumes to be rendered at the same time. The value range is \[1, 9\].

 |
| 

VkExtent2D [scaledView](#scaledview)

 | 

Scaling ratio of the rendering width and height. The recommended value range is \[1, 4\]. The value must be greater than or equal to 1.

 |
| 

VkExtent2D [viewSize](#viewsize)

 | 

Rendering width and height of output GI images.

 |
| 

bool [enableCloud](#enablecloud)

 | 

Whether to enable the device-cloud mode (true) or not (false).

 |

#### Field

#### \[h2\]enableCloud

bool XEG\_DDGICreateInfo::enableCloud

**Description**

Whether to enable the device-cloud mode (true) or not (false).

#### \[h2\]numberVolume

uint32\_t XEG\_DDGICreateInfo::numberVolume

**Description**

Maximum number of volumes to be rendered at the same time. The value range is \[1, 9\].

#### \[h2\]pNext

const void\* XEG\_DDGICreateInfo::pNext

**Description**

Pointer to the extended structure.

#### \[h2\]qualityMode

XEG\_RTGIQualityMode XEG\_DDGICreateInfo::qualityMode

**Description**

Quality mode of output images, which must be an enum in [XEG\_RTGIQualityMode](../../../modules/xengine/document.md#xeg_rtgiqualitymode).

#### \[h2\]scaledView

VkExtent2D XEG\_DDGICreateInfo::scaledView

**Description**

Scaling ratio of the rendering width and height. The recommended value range is \[1, 4\]. The value must be greater than or equal to 1.

#### \[h2\]sType

XEG\_StructureType XEG\_DDGICreateInfo::sType

**Description**

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_DDGI\_CREATE\_INFO.

#### \[h2\]viewSize

VkExtent2D XEG\_DDGICreateInfo::viewSize

**Description**

Rendering width and height of output GI images.
