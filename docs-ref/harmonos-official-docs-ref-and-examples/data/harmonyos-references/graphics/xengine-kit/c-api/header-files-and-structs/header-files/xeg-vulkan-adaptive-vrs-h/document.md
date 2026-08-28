# xeg\_vulkan\_adaptive\_vrs.h

#### Overview

Vulkan APIs for the adaptive VRS of XEngine. Before using APIs in this header file, you need to call the [HMS\_XEG\_EnumerateDeviceExtensionProperties](../../../modules/xengine/document.md#hms_xeg_enumeratedeviceextensionproperties) API to verify that extension [XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME](../../../modules/xengine/document.md#xeg_adaptive_vrs_extension_name) is available.

**File to include**: <xengine/xeg\_vulkan\_adaptive\_vrs.h>

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

struct [XEG\_AdaptiveVRSCreateInfo](../../structs/xeg-adaptivevrscreateinfo/document.md)

 | 

This structure describes the parameter information for creating an [XEG\_AdaptiveVRS](../../../modules/xengine/document.md#xeg_adaptivevrs) object. When the information in the structure changes, a new [XEG\_AdaptiveVRS](../../../modules/xengine/document.md#xeg_adaptivevrs) object needs to be created.

 |
| 

struct [XEG\_AdaptiveVRSDescription](../../structs/xeg-adaptivevrsdescription/document.md)

 | 

This structure describes the parameter information required for delivering the command for drawing the shading rate texture. The information needs to be updated for each frame.

 |

#### \[h2\]Typedefs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

VK\_DEFINE\_HANDLE([XEG\_AdaptiveVRS](../../../modules/xengine/document.md#xeg_adaptivevrs))

 | 

[XEG\_AdaptiveVRS](../../../modules/xengine/document.md#xeg_adaptivevrs) handle.

 |
| 

typedef struct [XEG\_AdaptiveVRSCreateInfo](../../structs/xeg-adaptivevrscreateinfo/document.md) XEG\_AdaptiveVRSCreateInfo

 | 

This structure describes the parameter information for creating an [XEG\_AdaptiveVRS](../../../modules/xengine/document.md#xeg_adaptivevrs) object. When the information in the structure changes, a new [XEG\_AdaptiveVRS](../../../modules/xengine/document.md#xeg_adaptivevrs) object needs to be created.

 |
| 

typedef struct [XEG\_AdaptiveVRSDescription](../../structs/xeg-adaptivevrsdescription/document.md) XEG\_AdaptiveVRSDescription

 | 

This structure describes the parameter information required for delivering the command for drawing the shading rate texture. The information needs to be updated for each frame.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateAdaptiveVRS](../../../modules/xengine/document.md#pfn_hms_xeg_createadaptivevrs)) (VkDevice device, const [XEG\_AdaptiveVRSCreateInfo](../../structs/xeg-adaptivevrscreateinfo/document.md) \*pXegAdaptiveVRSCreateInfo, [XEG\_AdaptiveVRS](../../../modules/xengine/document.md#xeg_adaptivevrs) \*pXegAdaptiveVRS)

 | 

Defines the function pointer for creating an [XEG\_AdaptiveVRS](../../../modules/xengine/document.md#xeg_adaptivevrs) object.

 |
| 

typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdDispatchAdaptiveVRS](../../../modules/xengine/document.md#pfn_hms_xeg_cmddispatchadaptivevrs)) (VkCommandBuffer commandBuffer, [XEG\_AdaptiveVRS](../../../modules/xengine/document.md#xeg_adaptivevrs) xegAdaptiveVRS, [XEG\_AdaptiveVRSDescription](../../structs/xeg-adaptivevrsdescription/document.md) \*pXegAdaptiveVRSDescription)

 | 

Defines the function pointer for computing the adaptive VRS command.

 |
| 

typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroyAdaptiveVRS](../../../modules/xengine/document.md#pfn_hms_xeg_destroyadaptivevrs)) ([XEG\_AdaptiveVRS](../../../modules/xengine/document.md#xeg_adaptivevrs) xegAdaptiveVRS)

 | 

Defines the function pointer for destroying an [XEG\_AdaptiveVRS](../../../modules/xengine/document.md#xeg_adaptivevrs) object.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateAdaptiveVRS](../../../modules/xengine/document.md#hms_xeg_createadaptivevrs) (VkDevice device, [XEG\_AdaptiveVRSCreateInfo](../../structs/xeg-adaptivevrscreateinfo/document.md) \*pXegAdaptiveVRSCreateInfo, [XEG\_AdaptiveVRS](../../../modules/xengine/document.md#xeg_adaptivevrs) \*pXegAdaptiveVRS)

 | 

Creates an [XEG\_AdaptiveVRS](../../../modules/xengine/document.md#xeg_adaptivevrs) object.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_CmdDispatchAdaptiveVRS](../../../modules/xengine/document.md#hms_xeg_cmddispatchadaptivevrs) (VkCommandBuffer cmdBuffer, [XEG\_AdaptiveVRS](../../../modules/xengine/document.md#xeg_adaptivevrs) xegAdaptiveVRS, [XEG\_AdaptiveVRSDescription](../../structs/xeg-adaptivevrsdescription/document.md) \*pXegAdaptiveVRSDescription)

 | 

Executes the command for computing the adaptive VRS.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyAdaptiveVRS](../../../modules/xengine/document.md#hms_xeg_destroyadaptivevrs) ([XEG\_AdaptiveVRS](../../../modules/xengine/document.md#xeg_adaptivevrs) xegAdaptiveVRS)

 | 

Destroys an [XEG\_AdaptiveVRS](../../../modules/xengine/document.md#xeg_adaptivevrs) object.

 |
