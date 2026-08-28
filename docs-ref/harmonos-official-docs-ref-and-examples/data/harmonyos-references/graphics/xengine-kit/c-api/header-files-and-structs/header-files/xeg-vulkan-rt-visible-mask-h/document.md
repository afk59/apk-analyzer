# xeg\_vulkan\_rt\_visible\_mask.h

#### Overview

APIs for the RT VisibleMask feature of XEngine. Before using the APIs in this header file, you need to call [HMS\_XEG\_EnumerateDeviceExtensionProperties](../../../modules/xengine/document.md#hms_xeg_enumeratedeviceextensionproperties) to check whether the [XEG\_RT\_SHADOW\_AO\_EXTENSION\_NAME](../../../modules/xengine/document.md#xeg_rt_shadow_ao_extension_name) extension is available.

**File to include**: <xengine/xeg\_vulkan\_rt\_visible\_mask.h>

**Library:** libxengine.so

**Syscap:** SystemCapability.Graphic.XEngine

**Since:** 6.0.0(20)

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

struct [XEG\_RTShadowAOCreateInfo](../../structs/xeg-rtshadowaocreateinfo/document.md)

 | 

This structure describes the initialization information for creating an [XEG\_RTVisibleMask](../../../modules/xengine/document.md#xeg_rtvisiblemask) instance that supports the Ray-Traced Shadow and Ambient Occlusion effects. When the information in the structure changes, a new [XEG\_RTVisibleMask](../../../modules/xengine/document.md#xeg_rtvisiblemask) object needs to be created.

 |
| 

struct [XEG\_RTShadowParameters](../../structs/xeg-rtshadowparameters/document.md)

 | 

Ray-Traced Shadow algorithm parameters.

 |
| 

struct [XEG\_RTAOParameters](../../structs/xeg-rtaoparameters/document.md)

 | 

Ray-Traced Ambient Occlusion algorithm parameters.

 |
| 

struct [XEG\_RTShadowAODenoiserParameters](../../structs/xeg-rtshadowaodenoiserparameters/document.md)

 | 

Denoising parameter for the Ray-Traced Shadow and Ambient Occlusion algorithms.

 |
| 

struct [XEG\_RTShadowAODescription](../../structs/xeg-rtshadowaodescription/document.md)

 | 

This structure describes the input information of the rendering command for the Ray-Traced Shadow and Ambient Occlusion algorithms.

 |

#### \[h2\]Typedefs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

VK\_DEFINE\_HANDLE([XEG\_RTVisibleMask](../../../modules/xengine/document.md#xeg_rtvisiblemask))

 | 

Handle to [XEG\_RTVisibleMask](../../../modules/xengine/document.md#xeg_rtvisiblemask), indicating the ray-traced VisibleMask feature instance. The shadow and ambient occlusion effects are supported.

 |
| 

typedef enum [XEG\_DenoiseQualityMode](../../../modules/xengine/document.md#xeg_denoisequalitymode) XEG\_DenoiseQualityMode

 | 

Enumerates denoising quality modes.

 |
| 

typedef enum [XEG\_TraversalMode](../../../modules/xengine/document.md#xeg_traversalmode) XEG\_TraversalMode

 | 

Enumerates traversal modes.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateRTVisibleMask](../../../modules/xengine/document.md#pfn_hms_xeg_creatertvisiblemask)) (VkDevice device, const void \*pCreateInfo, [XEG\_RTVisibleMask](../../../modules/xengine/document.md#xeg_rtvisiblemask) \*pRTVisibleMask)

 | 

Defines the function pointer for creating an [XEG\_RTVisibleMask](../../../modules/xengine/document.md#xeg_rtvisiblemask) object.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdRenderRTVisibleMask](../../../modules/xengine/document.md#pfn_hms_xeg_cmdrenderrtvisiblemask)) (VkCommandBuffer commandBuffer, [XEG\_RTVisibleMask](../../../modules/xengine/document.md#xeg_rtvisiblemask) rtVisibleMask, const void \*pDescription)

 | 

Defines the function pointer for recording the ray-traced VisibleMask rendering command.

 |
| 

typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroyRTVisibleMask](../../../modules/xengine/document.md#pfn_hms_xeg_destroyrtvisiblemask)) ([XEG\_RTVisibleMask](../../../modules/xengine/document.md#xeg_rtvisiblemask) rtVisibleMask)

 | 

Defines the function pointer for destroying an [XEG\_RTVisibleMask](../../../modules/xengine/document.md#xeg_rtvisiblemask) object.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[XEG\_DenoiseQualityMode](../../../modules/xengine/document.md#xeg_denoisequalitymode) { [XEG\_DENOISE\_QUALITY\_MODE\_NONE](../../../modules/xengine/document.md) = 0, [XEG\_DENOISE\_QUALITY\_MODE\_QUALITY](../../../modules/xengine/document.md) = 1, [XEG\_DENOISE\_QUALITY\_MODE\_BALANCED](../../../modules/xengine/document.md) = 2, [XEG\_DENOISE\_QUALITY\_MODE\_PERFORMANCES](../../../modules/xengine/document.md) = 3 }

 | 

Enumerates denoising quality modes.

 |
| 

[XEG\_TraversalMode](../../../modules/xengine/document.md#xeg_traversalmode) { [XEG\_TRAVERSAL\_MODE\_DEFAULT](../../../modules/xengine/document.md) = 0, [XEG\_TRAVERSAL\_MODE\_PERFORMANCES](../../../modules/xengine/document.md) = 1 }

 | 

Enumerates traversal modes.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateRTVisibleMask](../../../modules/xengine/document.md#hms_xeg_creatertvisiblemask) (VkDevice device, const void \*pCreateInfo, [XEG\_RTVisibleMask](../../../modules/xengine/document.md#xeg_rtvisiblemask) \*pRTVisibleMask)

 | 

Creates an [XEG\_RTVisibleMask](../../../modules/xengine/document.md#xeg_rtvisiblemask) object.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdRenderRTVisibleMask](../../../modules/xengine/document.md#hms_xeg_cmdrenderrtvisiblemask) (VkCommandBuffer commandBuffer, [XEG\_RTVisibleMask](../../../modules/xengine/document.md#xeg_rtvisiblemask) rtVisibleMask, const void \*pDescription)

 | 

Records the ray-traced VisibleMask rendering command.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyRTVisibleMask](../../../modules/xengine/document.md#hms_xeg_destroyrtvisiblemask) ([XEG\_RTVisibleMask](../../../modules/xengine/document.md#xeg_rtvisiblemask) rtVisibleMask)

 | 

Destroys an [XEG\_RTVisibleMask](../../../modules/xengine/document.md#xeg_rtvisiblemask) object.

 |
