# xeg\_vulkan\_rt\_reflection.h

#### Overview

APIs for the RT Reflection feature of XEngine. Before using the APIs in this header file, you need to call [HMS\_XEG\_EnumerateDeviceExtensionProperties](../../../modules/xengine/document.md#hms_xeg_enumeratedeviceextensionproperties) to query whether the [XEG\_RT\_REFLECTION\_EXTENSION\_NAME](../../../modules/xengine/document.md#xeg_rt_reflection_extension_name) extension is available.

**File to include**: <xengine/xeg\_vulkan\_rt\_reflection.h>

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

struct [XEG\_RTReflectionCreateInfo](../../structs/xeg-rtreflectioncreateinfo/document.md)

 | 

This structure describes the information for creating an [XEG\_RTReflection](../../../modules/xengine/document.md#xeg_rtreflection) object. When the information in the structure changes, a new [XEG\_RTReflection](../../../modules/xengine/document.md#xeg_rtreflection) object needs to be created.

 |
| 

struct [XEG\_RTReflectionDescription](../../structs/xeg-rtreflectiondescription/document.md)

 | 

This structure describes the input information for sending a ray intersection command.

 |

#### \[h2\]Typedefs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

VK\_DEFINE\_HANDLE([XEG\_RTReflection](../../../modules/xengine/document.md#xeg_rtreflection))

 | 

Handle to [XEG\_RTReflection](../../../modules/xengine/document.md#xeg_rtreflection).

 |
| 

typedef struct [XEG\_RTReflectionCreateInfo](../../structs/xeg-rtreflectioncreateinfo/document.md) XEG\_RTReflectionCreateInfo

 | 

This structure describes the information for creating an [XEG\_RTReflection](../../../modules/xengine/document.md#xeg_rtreflection) object. When the information in the structure changes, a new [XEG\_RTReflection](../../../modules/xengine/document.md#xeg_rtreflection) object needs to be created.

 |
| 

typedef struct [XEG\_RTReflectionDescription](../../structs/xeg-rtreflectiondescription/document.md) XEG\_RTReflectionDescription

 | 

This structure describes the input information for sending a ray intersection command.

 |
| 

typedef VkResult(VKAPI\_ATTR \* [PFN\_HMS\_XEG\_CreateRTReflection](../../../modules/xengine/document.md#pfn_hms_xeg_creatertreflection)) (VkDevice device, const void \*pCreateInfo, [XEG\_RTReflection](../../../modules/xengine/document.md#xeg_rtreflection) \*pRtReflection)

 | 

Defines the function pointer for creating an [XEG\_RTReflection](../../../modules/xengine/document.md#xeg_rtreflection) object.

 |
| 

typedef VkResult(VKAPI\_ATTR \*[PFN\_HMS\_XEG\_CmdRenderRTReflection](../../../modules/xengine/document.md#pfn_hms_xeg_cmdrenderrtreflection))(VkCommandBuffer commandBuffer, [XEG\_RTReflection](../../../modules/xengine/document.md#xeg_rtreflection) rtReflection, const void \*pDescription)

 | 

Defines the function pointer for recording the command for calculating the RT reflection hit information.

 |
| 

typedef void(VKAPI\_ATTR \*[PFN\_HMS\_XEG\_DestroyRTReflection](../../../modules/xengine/document.md#pfn_hms_xeg_destroyrtreflection))([XEG\_RTReflection](../../../modules/xengine/document.md#xeg_rtreflection) rtReflection)

 | 

Defines the function pointer for destroying an [XEG\_RTReflection](../../../modules/xengine/document.md#xeg_rtreflection) object.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateRTReflection](../../../modules/xengine/document.md#hms_xeg_creatertreflection) (VkDevice device, const void \*pCreateInfo, [XEG\_RTReflection](../../../modules/xengine/document.md#xeg_rtreflection) \*pRtReflection)

 | 

Creates an [XEG\_RTReflection](../../../modules/xengine/document.md#xeg_rtreflection) object.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdRenderRTReflection](../../../modules/xengine/document.md#hms_xeg_cmdrenderrtreflection) (VkCommandBuffer commandBuffer, [XEG\_RTReflection](../../../modules/xengine/document.md#xeg_rtreflection) rtReflection, const void \*pDescription)

 | 

Records the command for calculating the RT reflection hit information.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyRTReflection](../../../modules/xengine/document.md#hms_xeg_destroyrtreflection) ([XEG\_RTReflection](../../../modules/xengine/document.md#xeg_rtreflection) rtReflection)

 | 

Destroys an [XEG\_RTReflection](../../../modules/xengine/document.md#xeg_rtreflection) object.

 |
