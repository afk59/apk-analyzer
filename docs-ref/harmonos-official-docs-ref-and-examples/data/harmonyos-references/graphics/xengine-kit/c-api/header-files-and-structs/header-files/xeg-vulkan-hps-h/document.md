# xeg\_vulkan\_hps.h

#### Overview

APIs for the High Performance Shaders (HPS) feature of XEngine. Before using the APIs in this header file, you need to call [HMS\_XEG\_EnumerateDeviceExtensionProperties](../../../modules/xengine/document.md#hms_xeg_enumeratedeviceextensionproperties) to check whether the HPS feature extension to be used is supported.

**File to include**: <xengine/xeg\_vulkan\_hps.h>

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

struct [XEG\_HPSCreateInfo](../../structs/xeg-hpscreateinfo/document.md)

 | 

This structure describes the information for creating an [XEG\_HPS](../../../modules/xengine/document.md#xeg_hps) object.

 |
| 

struct [XEG\_HPSRadixSort](../../structs/xeg-hpsradixsort/document.md)

 | 

This structure describes the HPS radix sort extension structure information.

 |
| 

struct [XEG\_HPSRadixSortDescription](../../structs/xeg-hpsradixsortdescription/document.md)

 | 

This structure describes the information required for sorting using the [XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](../../../modules/xengine/document.md#xeg_hps_radix_sort_extension_name) feature.

 |

#### \[h2\]Typedefs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

VK\_DEFINE\_HANDLE([XEG\_HPS](../../../modules/xengine/document.md#xeg_hps))

 | 

Handle to [XEG\_HPS](../../../modules/xengine/document.md#xeg_hps).

 |
| 

typedef struct [XEG\_HPSCreateInfo](../../structs/xeg-hpscreateinfo/document.md) XEG\_HPSCreateInfo

 | 

This structure describes the information for creating an [XEG\_HPS](../../../modules/xengine/document.md#xeg_hps) object.

 |
| 

typedef struct [XEG\_HPSRadixSort](../../structs/xeg-hpsradixsort/document.md) XEG\_HPSRadixSort

 | 

This structure describes the HPS radix sort extension structure information.

 |
| 

typedef struct [XEG\_HPSRadixSortDescription](../../structs/xeg-hpsradixsortdescription/document.md) XEG\_HPSRadixSortDescription

 | 

This structure describes the information required for sorting using the [XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](../../../modules/xengine/document.md#xeg_hps_radix_sort_extension_name) feature.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateHPS](../../../modules/xengine/document.md#pfn_hms_xeg_createhps)) (VkDevice device, const [XEG\_HPSCreateInfo](../../structs/xeg-hpscreateinfo/document.md) \*pCreateInfo, [XEG\_HPS](../../../modules/xengine/document.md#xeg_hps) \*pHps)

 | 

Defines the function pointer for creating an [XEG\_HPS](../../../modules/xengine/document.md#xeg_hps) object.

 |
| 

typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroyHPS](../../../modules/xengine/document.md#pfn_hms_xeg_destroyhps)) ([XEG\_HPS](../../../modules/xengine/document.md#xeg_hps) hps)

 | 

Defines the function pointer for destroying an [XEG\_HPS](../../../modules/xengine/document.md#xeg_hps) object.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdRadixSortHPS](../../../modules/xengine/document.md#pfn_hms_xeg_cmdradixsorthps)) (VkCommandBuffer commandBuffer, [XEG\_HPS](../../../modules/xengine/document.md#xeg_hps) hps, const [XEG\_HPSRadixSortDescription](../../structs/xeg-hpsradixsortdescription/document.md) \*pDescription)

 | 

Defines the function pointer for recording an HPS radix sort command. Before using this API, you need to call [HMS\_XEG\_EnumerateDeviceExtensionProperties](../../../modules/xengine/document.md#hms_xeg_enumeratedeviceextensionproperties) to check whether the [XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](../../../modules/xengine/document.md#xeg_hps_radix_sort_extension_name) extension is supported.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateHPS](../../../modules/xengine/document.md#hms_xeg_createhps) (VkDevice device, const [XEG\_HPSCreateInfo](../../structs/xeg-hpscreateinfo/document.md) \*pCreateInfo, [XEG\_HPS](../../../modules/xengine/document.md#xeg_hps) \*pHps)

 | 

Creates an [XEG\_HPS](../../../modules/xengine/document.md#xeg_hps) object.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyHPS](../../../modules/xengine/document.md#hms_xeg_destroyhps) ([XEG\_HPS](../../../modules/xengine/document.md#xeg_hps) hps)

 | 

Destroys an [XEG\_HPS](../../../modules/xengine/document.md#xeg_hps) object.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdRadixSortHPS](../../../modules/xengine/document.md#hms_xeg_cmdradixsorthps) (VkCommandBuffer commandBuffer, [XEG\_HPS](../../../modules/xengine/document.md#xeg_hps) hps, const [XEG\_HPSRadixSortDescription](../../structs/xeg-hpsradixsortdescription/document.md) \*pDescription)

 | 

Records an HPS radix sort command. Before using this API, you need to call {[} to check whether the XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME} extension is supported.](../../../modules/xengine/document.md#hms_xeg_enumeratedeviceextensionproperties)

 |
