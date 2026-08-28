# VkNativeBufferFormatPropertiesOHOS

typedef struct VkNativeBufferFormatPropertiesOHOS {...} VkNativeBufferFormatPropertiesOHOS

#### Overview

The struct describes the format properties of the NativeBuffer.

**Since**: 10

**Related module**: [Vulkan](../vulkan/document.md)

**Header file**: [vulkan\_ohos.h](../vulkan-ohos-h/document.md)

#### Summary

## Member Variables

| Name | Description |
| :-- | :-- |
| VkStructureType sType | Struct type. |
| void\* pNext | Pointer to the next-level struct. |
| VkFormat format | Format. |
| uint64\_t externalFormat | Externally defined format. |
| VkFormatFeatureFlags formatFeatures | Features of the externally defined format. |
| VkComponentMapping samplerYcbcrConversionComponents | A group of VkComponentSwizzles. |
| VkSamplerYcbcrModelConversion suggestedYcbcrModel | Color model. |
| VkSamplerYcbcrRange suggestedYcbcrRange | Color value range. |
| VkChromaLocation suggestedXChromaOffset | X chrominance offset. |
| VkChromaLocation suggestedYChromaOffset | Y chrominance offset. |
