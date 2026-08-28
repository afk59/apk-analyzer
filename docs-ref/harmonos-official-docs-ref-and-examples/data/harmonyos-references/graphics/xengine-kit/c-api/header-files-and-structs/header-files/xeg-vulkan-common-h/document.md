# xeg\_vulkan\_common.h

#### Overview

Contains the common type definitions related to Vulkan in XEngine.

**File to include**: <xengine/xeg\_vulkan\_common.h>

**Library:** libxengine.so

**Syscap:** SystemCapability.Graphic.XEngine

**Since:** 6.0.0(20)

**Related Modules:**[XEngine](../../../modules/xengine/document.md)

#### Summary

#### \[h2\]Typedefs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef enum [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) XEG\_StructureType

 | 

Enum for the XEngine structure types.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdSetSynchronization](../../../modules/xengine/document.md#pfn_hms_xeg_cmdsetsynchronization)) (VkCommandBuffer commandBuffer, const void \*xegHandle)

 | 

Defines the function pointer for setting synchronization signals and waiting for the rendering result to be written to a specified image. When the RTGI feature is used, it is the GI rendering result that needs to be waited for before being written to a specified image.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) {

[XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_CREATE\_INFO](../../../modules/xengine/document.md) = 0, [XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_DESCRIPTION](../../../modules/xengine/document.md) = 1, [XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_CREATE\_INFO](../../../modules/xengine/document.md) = 2, [XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_DESCRIPTION](../../../modules/xengine/document.md) = 3,

[XEG\_STRUCTURE\_TYPE\_NNGI\_CREATE\_INFO](../../../modules/xengine/document.md) = 4, [XEG\_STRUCTURE\_TYPE\_NNGI\_DESCRIPTION](../../../modules/xengine/document.md) = 5, [XEG\_STRUCTURE\_TYPE\_DDGI\_CREATE\_INFO](../../../modules/xengine/document.md) = 6, [XEG\_STRUCTURE\_TYPE\_DDGI\_DESCRIPTION](../../../modules/xengine/document.md) = 7,

[XEG\_STRUCTURE\_TYPE\_HPS\_CREATE\_INFO](../../../modules/xengine/document.md) = 1001, [XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT](../../../modules/xengine/document.md) = 1002, [XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT\_DESCRIPTION](../../../modules/xengine/document.md) = 1003

}

 | 

Enum for the XEngine structure types.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdSetSynchronization](../../../modules/xengine/document.md#hms_xeg_cmdsetsynchronization) (VkCommandBuffer commandBuffer, const void \*xegHandle)

 | 

Sets synchronization signals and waits for the rendering result to be written to a specified image. When the RTGI feature is used, it is the GI rendering result that needs to be waited for before being written to a specified image.

 |
