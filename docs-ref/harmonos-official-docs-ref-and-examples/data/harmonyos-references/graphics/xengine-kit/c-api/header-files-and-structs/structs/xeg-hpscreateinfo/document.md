# XEG\_HPSCreateInfo

#### Overview

This structure describes the information for creating an [XEG\_HPS](../../../modules/xengine/document.md#xeg_hps) object.

**Since:** 6.0.0(20)

**Related Modules:**[XEngine](../../../modules/xengine/document.md)

**Header file**: [xeg\_vulkan\_hps.h](../../header-files/xeg-vulkan-hps-h/document.md)

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

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_HPS\_CREATE\_INFO.

 |
| 

const void \* [pNext](#pnext)

 | 

Pointer to the extension structure. The value cannot be null. It indicates the enabled XEngine HPS extension feature. For example, when the [XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](../../../modules/xengine/document.md#xeg_hps_radix_sort_extension_name) feature is used, the value must be specified as [XEG\_HPSRadixSort](../xeg-hpsradixsort/document.md).

 |

#### Field

#### \[h2\]pNext

const void\* XEG\_HPSCreateInfo::pNext

**Description**

Pointer to the extension structure. The value cannot be null. It indicates the enabled XEngine HPS extension feature. For example, when the [XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](../../../modules/xengine/document.md#xeg_hps_radix_sort_extension_name) feature is used, the value must be specified as [XEG\_HPSRadixSort](../xeg-hpsradixsort/document.md).

#### \[h2\]sType

XEG\_StructureType XEG\_HPSCreateInfo::sType

**Description**

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_HPS\_CREATE\_INFO.
