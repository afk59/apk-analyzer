# VkSurfaceCreateInfoOHOS

typedef struct VkSurfaceCreateInfoOHOS {...} VkSurfaceCreateInfoOHOS

#### Overview

The struct describes the parameters required for creating a Vulkan surface.

**Since**: 10

**Related module**: [Vulkan](../vulkan/document.md)

**Header file**: [vulkan\_ohos.h](../vulkan-ohos-h/document.md)

#### Summary

## Member Variables

| Name | Description |
| :-- | :-- |
| VkStructureType sType | Struct type. The value must be **VK\_STRUCTURE\_TYPE\_SURFACE\_CREATE\_INFO\_OHOS**. |
| const void\* pNext | Pointer to the next struct in the chain. The value must be nullptr. |
| VkSurfaceCreateFlagsOHOS flags | Reserved flags. The value must be **0**. |
| [OHNativeWindow](../nativewindow/document.md)\* window | Pointer to an OHNativeWindow instance. |
