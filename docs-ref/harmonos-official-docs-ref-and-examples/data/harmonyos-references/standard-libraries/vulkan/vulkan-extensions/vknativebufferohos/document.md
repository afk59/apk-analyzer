# VkNativeBufferOHOS

typedef struct VkNativeBufferOHOS {...} VkNativeBufferOHOS

#### Overview

Contains parameters for the native device memory.

**Since**: 10

**Related module**: [Vulkan](../vulkan/document.md)

**Header file**: [vulkan\_ohos.h](../vulkan-ohos-h/document.md)

#### Summary

## Member Variables

| Name | Description |
| :-- | :-- |
| VkStructureType sType | Struct type. |
| const void\* pNext | Pointer to the next-level struct; pNext is either null or a pointer to the next-level struct. |
| struct [OHBufferHandle\*](../ohbufferhandle/document.md) handle | Device memory handle. |
