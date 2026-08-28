# XEG\_HPSRadixSortDescription

#### Overview

This structure describes the information required for sorting using the [XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](../../../modules/xengine/document.md#xeg_hps_radix_sort_extension_name) feature.

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

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT\_DESCRIPTION.

 |
| 

const void \* [pNext](#pnext)

 | 

Pointer to the extension structure.

 |
| 

VkBuffer [sortCount](#sortcount)

 | 

Buffer that stores the number of indexes to be sorted. The number value is read from bit 0 of the buffer.

 |
| 

VkBuffer [keyBuffer](#keybuffer)

 | 

Buffer for storing key values used for sorting. The data format is a 32-bit unsigned integer.

 |
| 

VkBuffer [indexBuffer](#indexbuffer)

 | 

Buffer for storing values to be sorted. The data format is a 32-bit unsigned integer.

 |

#### Field

#### \[h2\]indexBuffer

VkBuffer XEG\_HPSRadixSortDescription::indexBuffer

**Description**

Buffer for storing values to be sorted. The data format is a 32-bit unsigned integer.

#### \[h2\]keyBuffer

VkBuffer XEG\_HPSRadixSortDescription::keyBuffer

**Description**

Buffer for storing key values used for sorting. The data format is a 32-bit unsigned integer.

#### \[h2\]pNext

const void\* XEG\_HPSRadixSortDescription::pNext

**Description**

Pointer to the extension structure.

#### \[h2\]sortCount

VkBuffer XEG\_HPSRadixSortDescription::sortCount

**Description**

Buffer that stores the number of indexes to be sorted. The number value is read from bit 0 of the buffer.

#### \[h2\]sType

XEG\_StructureType XEG\_HPSRadixSortDescription::sType

**Description**

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT\_DESCRIPTION.
