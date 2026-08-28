# xeg\_vulkan\_extension.h

#### Overview

(Vulkan) API for querying extensions of XEngine.

**File to include**: <xengine/xeg\_vulkan\_extension.h>

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

struct [XEG\_ExtensionProperties](../../structs/xeg-extensionproperties/document.md)

 | 

This structure describes the set of XEngine extensions queried through the [HMS\_XEG\_EnumerateDeviceExtensionProperties](../../../modules/xengine/document.md#hms_xeg_enumeratedeviceextensionproperties) API.

 |

#### \[h2\]Macros

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[XEG\_MAX\_EXTENSION\_NAME\_SIZE](../../../modules/xengine/document.md#xeg_max_extension_name_size) 256

 | 

Maximum length of the extension name supported by XEngine.

 |

#### \[h2\]Typedefs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef struct [XEG\_ExtensionProperties](../../structs/xeg-extensionproperties/document.md) XEG\_ExtensionProperties

 | 

This structure describes the set of XEngine extensions queried through the [HMS\_XEG\_EnumerateDeviceExtensionProperties](../../../modules/xengine/document.md#hms_xeg_enumeratedeviceextensionproperties) API.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_EnumerateDeviceExtensionProperties](../../../modules/xengine/document.md#pfn_hms_xeg_enumeratedeviceextensionproperties)) (VkPhysicalDevice physicalDevice, uint32\_t \*pPropertyCount, [XEG\_ExtensionProperties](../../structs/xeg-extensionproperties/document.md) \*pProperties)

 | 

Defines the function pointer of the Vulkan API for querying extensions of XEngine.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_EnumerateDeviceExtensionProperties](../../../modules/xengine/document.md#hms_xeg_enumeratedeviceextensionproperties) (VkPhysicalDevice physicalDevice, uint32\_t \*pPropertyCount, [XEG\_ExtensionProperties](../../structs/xeg-extensionproperties/document.md) \*pProperties)

 | 

Vulkan API for querying extensions of XEngine.

 |
