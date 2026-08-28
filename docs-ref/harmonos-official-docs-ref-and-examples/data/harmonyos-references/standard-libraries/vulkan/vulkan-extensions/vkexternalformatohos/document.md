# VkExternalFormatOHOS

typedef struct VkExternalFormatOHOS {...} VkExternalFormatOHOS

#### Overview

The struct describes an externally defined format.

**Since**: 10

**Related module**: [Vulkan](../vulkan/document.md)

**Header file**: [vulkan\_ohos.h](../vulkan-ohos-h/document.md)

#### Summary

## Member Variables

| Name | Description |
| :-- | :-- |
| VkStructureType sType | Struct type. The value must be **VK\_STRUCTURE\_TYPE\_EXTERNAL\_FORMAT\_OHOS**. |
| void\* pNext | Either nullptr or a pointer to the next struct in the chain. |
| uint64\_t externalFormat | Externally defined format. |
