# xeg\_vulkan\_temporal\_upscale.h

#### Overview

AI temporal upscaling APIs of XEngine. The recommended upscaling multiple range is \[1.25, 2.0\]. Before using APIs in this header file, you need to call the [HMS\_XEG\_EnumerateDeviceExtensionProperties](../../../modules/xengine/document.md#hms_xeg_enumeratedeviceextensionproperties) API to verify that extension [XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME](../../../modules/xengine/document.md#xeg_temporal_upscale_extension_name) is available.

**File to include**: <xengine/xeg\_vulkan\_temporal\_upscale.h>

**Library:** libxengine.so

**Syscap:** SystemCapability.Graphic.XEngine

**Since:** 5.0.0(12)

**Related Modules:**[XEngine](../../../modules/xengine/document.md)

#### Summary

#### \[h2\]Data Structures

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [XEG\_TemporalUpscaleCreateInfo](../../structs/xeg-temporalupscalecreateinfo/document.md)

 | 

This structure describes the information for creating an [XEG\_TemporalUpscale](../../../modules/xengine/document.md#xeg_temporalupscale) object. When the information in the structure changes, a new [XEG\_TemporalUpscale](../../../modules/xengine/document.md#xeg_temporalupscale) object needs to be created.

 |
| 

struct [XEG\_TemporalUpscaleDescription](../../structs/xeg-temporalupscaledescription/document.md)

 | 

This structure describes the input information for delivering AI temporal upscaling rendering command.

 |

#### \[h2\]Typedefs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

VK\_DEFINE\_HANDLE([XEG\_TemporalUpscale](../../../modules/xengine/document.md#xeg_temporalupscale))

 | 

Handle to [XEG\_TemporalUpscale](../../../modules/xengine/document.md#xeg_temporalupscale).

 |
| 

typedef struct [XEG\_TemporalUpscaleCreateInfo](../../structs/xeg-temporalupscalecreateinfo/document.md) XEG\_TemporalUpscaleCreateInfo

 | 

This structure describes the information for creating an [XEG\_TemporalUpscale](../../../modules/xengine/document.md#xeg_temporalupscale) object. When the information in the structure changes, a new [XEG\_TemporalUpscale](../../../modules/xengine/document.md#xeg_temporalupscale) object needs to be created.

 |
| 

typedef struct [XEG\_TemporalUpscaleDescription](../../structs/xeg-temporalupscaledescription/document.md) XEG\_TemporalUpscaleDescription

 | 

This structure describes the input information for delivering AI temporal upscaling rendering command.

 |
| 

typedef VkResult(VKAPI\_ATTR \* [PFN\_HMS\_XEG\_CreateTemporalUpscale](../../../modules/xengine/document.md#pfn_hms_xeg_createtemporalupscale)) (VkDevice device, [XEG\_TemporalUpscaleCreateInfo](../../structs/xeg-temporalupscalecreateinfo/document.md) \*pTemporalUpscaleInfo, [XEG\_TemporalUpscale](../../../modules/xengine/document.md#xeg_temporalupscale) \*pTemporalUpscale)

 | 

Defines the function pointer for creating an [XEG\_TemporalUpscale](../../../modules/xengine/document.md#xeg_temporalupscale) object.

 |
| 

typedef void(VKAPI\_ATTR \* [PFN\_HMS\_XEG\_CmdRenderTemporalUpscale](../../../modules/xengine/document.md#pfn_hms_xeg_cmdrendertemporalupscale)) (VkCommandBuffer commandBuffer, [XEG\_TemporalUpscale](../../../modules/xengine/document.md#xeg_temporalupscale) temporalUpscale, [XEG\_TemporalUpscaleDescription](../../structs/xeg-temporalupscaledescription/document.md) \*pDescription)

 | 

Defines the function pointer for recording the AI temporal upscaling rendering command.

 |
| 

typedef void(VKAPI\_ATTR \* [PFN\_HMS\_XEG\_DestroyTemporalUpscale](../../../modules/xengine/document.md#pfn_hms_xeg_destroytemporalupscale)) ([XEG\_TemporalUpscale](../../../modules/xengine/document.md#xeg_temporalupscale) temporalUpscale)

 | 

Defines the function pointer for destroying an [XEG\_TemporalUpscale](../../../modules/xengine/document.md#xeg_temporalupscale) object.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateTemporalUpscale](../../../modules/xengine/document.md#hms_xeg_createtemporalupscale) (VkDevice device, [XEG\_TemporalUpscaleCreateInfo](../../structs/xeg-temporalupscalecreateinfo/document.md) \*pTemporalUpscaleInfo, [XEG\_TemporalUpscale](../../../modules/xengine/document.md#xeg_temporalupscale) \*pTemporalUpscale)

 | 

Creates an [XEG\_TemporalUpscale](../../../modules/xengine/document.md#xeg_temporalupscale) object.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_CmdRenderTemporalUpscale](../../../modules/xengine/document.md#hms_xeg_cmdrendertemporalupscale) (VkCommandBuffer commandBuffer, [XEG\_TemporalUpscale](../../../modules/xengine/document.md#xeg_temporalupscale) temporalUpscale, [XEG\_TemporalUpscaleDescription](../../structs/xeg-temporalupscaledescription/document.md) \*pDescription)

 | 

Records the AI temporal upscaling rendering command.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyTemporalUpscale](../../../modules/xengine/document.md#hms_xeg_destroytemporalupscale) ([XEG\_TemporalUpscale](../../../modules/xengine/document.md#xeg_temporalupscale) temporalUpscale)

 | 

Destroys an [XEG\_TemporalUpscale](../../../modules/xengine/document.md#xeg_temporalupscale) object.

 |
