# VkMemoryGetNativeBufferInfoOHOS

typedef struct VkMemoryGetNativeBufferInfoOHOS {...} VkMemoryGetNativeBufferInfoOHOS

#### Overview

The struct is used to obtain an OH\_NativeBuffer from the Vulkan memory.

**Since**: 10

**Related module**: [Vulkan](../vulkan/document.md)

**Header file**: [vulkan\_ohos.h](../vulkan-ohos-h/document.md)

#### Summary

## Member Variables

| Name | Description |
| :-- | :-- |
| VkStructureType sType | Struct type. The value must be **VK\_STRUCTURE\_TYPE\_MEMORY\_GET\_NATIVE\_BUFFER\_INFO\_OHOS**. |
| const void\* pNext | Pointer to the next struct in the chain. The value must be nullptr. |
| VkDeviceMemory memory | VkDeviceMemory object. The value must be a valid VkDeviceMemory object. |
