# xeg\_vulkan\_spatial\_upscale.h

#### Overview

Vulkan APIs for the GPU spatial upscaling of XEngine. Before using APIs in this header file, you need to call the [HMS\_XEG\_EnumerateDeviceExtensionProperties](../../../modules/xengine/document.md#hms_xeg_enumeratedeviceextensionproperties) API to verify that extension [XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME](../../../modules/xengine/document.md#xeg_spatial_upscale_extension_name) is available.

**File to include**: <xengine/xeg\_vulkan\_spatial\_upscale.h>

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

struct [XEG\_SpatialUpscaleCreateInfo](../../structs/xeg-spatialupscalecreateinfo/document.md)

 | 

This structure describes the information for creating an [XEG\_SpatialUpscale](../../../modules/xengine/document.md#xeg_spatialupscale) object. When the information in the structure changes, a new XEG\_SpatialUpscale object needs to be created.

 |
| 

struct [XEG\_SpatialUpscaleDescription](../../structs/xeg-spatialupscaledescription/document.md)

 | 

This structure describes the image information required for delivering the GPU spatial upscaling rendering command.

 |

#### \[h2\]Typedefs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

VK\_DEFINE\_HANDLE([XEG\_SpatialUpscale](../../../modules/xengine/document.md#xeg_spatialupscale))

 | 

Handle to [XEG\_SpatialUpscale](../../../modules/xengine/document.md#xeg_spatialupscale).

 |
| 

typedef struct [XEG\_SpatialUpscaleCreateInfo](../../structs/xeg-spatialupscalecreateinfo/document.md) XEG\_SpatialUpscaleCreateInfo

 | 

This structure describes the information for creating an [XEG\_SpatialUpscale](../../../modules/xengine/document.md#xeg_spatialupscale) object. When the information in the structure changes, a new XEG\_SpatialUpscale object needs to be created.

 |
| 

typedef struct [XEG\_SpatialUpscaleDescription](../../structs/xeg-spatialupscaledescription/document.md) XEG\_SpatialUpscaleDescription

 | 

This structure describes the image information required for delivering the GPU spatial upscaling rendering command.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateSpatialUpscale](../../../modules/xengine/document.md#pfn_hms_xeg_createspatialupscale)) (VkDevice device, const [XEG\_SpatialUpscaleCreateInfo](../../structs/xeg-spatialupscalecreateinfo/document.md) \*pXegSpatialUpscaleCreateInfo, [XEG\_SpatialUpscale](../../../modules/xengine/document.md#xeg_spatialupscale) \*pXegSpatialUpscale)

 | 

Defines the function pointer for creating an [XEG\_SpatialUpscale](../../../modules/xengine/document.md#xeg_spatialupscale) object.

 |
| 

typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdRenderSpatialUpscale](../../../modules/xengine/document.md#pfn_hms_xeg_cmdrenderspatialupscale)) (VkCommandBuffer commandBuffer, [XEG\_SpatialUpscale](../../../modules/xengine/document.md#xeg_spatialupscale) xegSpatialUpscale, [XEG\_SpatialUpscaleDescription](../../structs/xeg-spatialupscaledescription/document.md) \*pXegSpatialUpscaleDescription)

 | 

Defines the function pointer for executing the GPU spatial upscaling rendering command.

 |
| 

typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroySpatialUpscale](../../../modules/xengine/document.md#pfn_hms_xeg_destroyspatialupscale)) ([XEG\_SpatialUpscale](../../../modules/xengine/document.md#xeg_spatialupscale) xegSpatialUpscale)

 | 

Defines the function pointer for destroying an [XEG\_SpatialUpscale](../../../modules/xengine/document.md#xeg_spatialupscale) object.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateSpatialUpscale](../../../modules/xengine/document.md#hms_xeg_createspatialupscale) (VkDevice device, const [XEG\_SpatialUpscaleCreateInfo](../../structs/xeg-spatialupscalecreateinfo/document.md) \*pXegSpatialUpscaleCreateInfo, [XEG\_SpatialUpscale](../../../modules/xengine/document.md#xeg_spatialupscale) \*pXegSpatialUpscale)

 | 

Creates an [XEG\_SpatialUpscale](../../../modules/xengine/document.md#xeg_spatialupscale) object.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_CmdRenderSpatialUpscale](../../../modules/xengine/document.md#hms_xeg_cmdrenderspatialupscale) (VkCommandBuffer commandBuffer, [XEG\_SpatialUpscale](../../../modules/xengine/document.md#xeg_spatialupscale) xegSpatialUpscale, [XEG\_SpatialUpscaleDescription](../../structs/xeg-spatialupscaledescription/document.md) \*pXegSpatialUpscaleDescription)

 | 

Executes the GPU spatial upscaling rendering command.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroySpatialUpscale](../../../modules/xengine/document.md#hms_xeg_destroyspatialupscale) ([XEG\_SpatialUpscale](../../../modules/xengine/document.md#xeg_spatialupscale) xegSpatialUpscale)

 | 

Destroys an [XEG\_SpatialUpscale](../../../modules/xengine/document.md#xeg_spatialupscale) object.

 |
