# XEG\_RTReflectionCreateInfo

#### Overview

This structure describes the information for creating an [XEG\_RTReflection](../../../modules/xengine/document.md#xeg_rtreflection) object. When the information in the structure changes, a new [XEG\_RTReflection](../../../modules/xengine/document.md#xeg_rtreflection) object needs to be created.

**Since:** 6.0.0(20)

**Related Modules:**[XEngine](../../../modules/xengine/document.md)

**Header file**: [xeg\_vulkan\_rt\_reflection.h](../../header-files/xeg-vulkan-rt-reflection-h/document.md)

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

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_CREATE\_INFO.

 |
| 

const void \* [pNext](#pnext)

 | 

Pointer to the extended structure.

 |
| 

VkExtent2D [renderSize](#rendersize)

 | 

Size of the input image.

 |
| 

bool [enableFastTrace](#enablefasttrace)

 | 

Whether to enable the fast intersection mode. The fast intersection mode has better performance than the common intersection mode. The value true indicates that the fast intersection mode is enabled, and false indicates that the common intersection mode is used.

 |

#### Field

#### \[h2\]enableFastTrace

bool XEG\_RTReflectionCreateInfo::enableFastTrace

**Description**

Whether to enable the fast intersection mode. The fast intersection mode has better performance than the common intersection mode. The value true indicates that the fast intersection mode is enabled, and false indicates that the common intersection mode is used.

#### \[h2\]pNext

const void\* XEG\_RTReflectionCreateInfo::pNext

**Description**

Pointer to the extended structure.

#### \[h2\]renderSize

VkExtent2D XEG\_RTReflectionCreateInfo::renderSize

**Description**

Size of the input image.

#### \[h2\]sType

XEG\_StructureType XEG\_RTReflectionCreateInfo::sType

**Description**

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_CREATE\_INFO.
