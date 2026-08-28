# xeg\_vulkan\_rtgi.h

#### Overview

XEngine Vulkan APIs for the Ray-Traced Global Illumination feature, which provides two features: Dynamic Diffuse Global Illumination (DDGI) and Neural Network Global Illumination (NNGI). Before using the APIs in this header file, call [HMS\_XEG\_EnumerateDeviceExtensionProperties](../../../modules/xengine/document.md#hms_xeg_enumeratedeviceextensionproperties) to check whether the [XEG\_RTGI\_EXTENSION\_NAME](../../../modules/xengine/document.md#xeg_rtgi_extension_name) extension is available.

**File to include**: <xengine/xeg\_vulkan\_rtgi.h>

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

struct [XEG\_DDGIVolumeEntryParameters](../../structs/xeg-ddgivolumeentryparameters/document.md)

 | 

This structure describes the mandatory parameters of each DDGI volume.

 |
| 

struct [XEG\_DDGICreateInfo](../../structs/xeg-ddgicreateinfo/document.md)

 | 

This structure describes the information about creating an [XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi) object with the DDGI feature. If the information in the structure changes, a new [XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi) object needs to be created.

 |
| 

struct [XEG\_DDGIDescription](../../structs/xeg-ddgidescription/document.md)

 | 

This structure describes the information required for updating the DDGI probe irradiance and rendering the output GI images.

 |
| 

struct [XEG\_NNGICreateInfo](../../structs/xeg-nngicreateinfo/document.md)

 | 

This structure describes the information about creating an [XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi) object with the NNGI feature. If the information in the structure changes, a new [XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi) object needs to be created.

 |
| 

struct [XEG\_NNGIDescription](../../structs/xeg-nngidescription/document.md)

 | 

This structure describes the information required for updating the NNGI to calculate the ray-traced global illumination.

 |

#### \[h2\]Typedefs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

VK\_DEFINE\_HANDLE([XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi))

 | 

Handle to [XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi).

 |
| 

typedef enum [XEG\_RTGIQualityMode](../../../modules/xengine/document.md#xeg_rtgiqualitymode) XEG\_RTGIQualityMode

 | 

Enum for the quality modes of output images.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateRTGI](../../../modules/xengine/document.md#pfn_hms_xeg_creatertgi)) (VkDevice device, const void \*pCreateInfo, [XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi) \*pRtGI)

 | 

Defines the function pointer for creating an [XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi) object.

 |
| 

typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroyRTGI](../../../modules/xengine/document.md#pfn_hms_xeg_destroyrtgi)) ([XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi) rtGI)

 | 

Defines the function pointer for destroying an [XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi) object.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdRenderRTGI](../../../modules/xengine/document.md#pfn_hms_xeg_cmdrenderrtgi)) (VkCommandBuffer commandBuffer, [XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi) rtGI, const void \*pDescription)

 | 

Defines the function pointer for executing the rendering command.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[XEG\_RTGIQualityMode](../../../modules/xengine/document.md#xeg_rtgiqualitymode) { [XEG\_RTGI\_QUALITY\_MODE\_QUALITY](../../../modules/xengine/document.md) = 0, [XEG\_RTGI\_QUALITY\_MODE\_BALANCED](../../../modules/xengine/document.md) = 1, [XEG\_RTGI\_QUALITY\_MODE\_PERFORMANCE](../../../modules/xengine/document.md) = 2 }

 | 

Enum for the quality modes of output images.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateRTGI](../../../modules/xengine/document.md#hms_xeg_creatertgi) (VkDevice device, const void \*pCreateInfo, [XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi) \*pRtGI)

 | 

Creates an [XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi) object.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyRTGI](../../../modules/xengine/document.md#hms_xeg_destroyrtgi) ([XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi) rtGI)

 | 

Destroys an [XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi) object.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdRenderRTGI](../../../modules/xengine/document.md#hms_xeg_cmdrenderrtgi) (VkCommandBuffer commandBuffer, [XEG\_RTGI](../../../modules/xengine/document.md#xeg_rtgi) rtGI, const void \*pDescription)

 | 

Executes the rendering command.

 |
