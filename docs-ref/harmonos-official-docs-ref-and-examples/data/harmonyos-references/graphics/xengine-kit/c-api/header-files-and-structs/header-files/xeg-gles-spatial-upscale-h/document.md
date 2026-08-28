# xeg\_gles\_spatial\_upscale.h

#### Overview

OpenGL ES APIs for the GPU spatial upscaling feature of XEngine. Before using APIs in this header file, you need to call the [HMS\_XEG\_GetString](../../../modules/xengine/document.md#hms_xeg_getstring) API to verify that extension [XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME](../../../modules/xengine/document.md#xeg_spatial_upscale_extension_name) is available.

**File to include**: <xengine/xeg\_gles\_spatial\_upscale.h>

**Library:** libxengine.so

**Syscap:** SystemCapability.Graphic.XEngine

**Since:** 5.0.0(12)

**Related Modules:**[XEngine](../../../modules/xengine/document.md)

#### Summary

#### \[h2\]Macros

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[XEG\_SPATIAL\_UPSCALE\_SCISSOR](../../../modules/xengine/document.md#xeg_spatial_upscale_scissor) 0x1U

 | 

Sets the SCISSOR parameter of the [HMS\_XEG\_SpatialUpscaleParameter](../../../modules/xengine/document.md#hms_xeg_spatialupscaleparameter) API.

 |
| 

[XEG\_SPATIAL\_UPSCALE\_SHARPNESS](../../../modules/xengine/document.md#xeg_spatial_upscale_sharpness) 0x2U

 | 

Sets the SHARPNESS parameter of the [HMS\_XEG\_SpatialUpscaleParameter](../../../modules/xengine/document.md#hms_xeg_spatialupscaleparameter) API.

 |

#### \[h2\]Typedefs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_SPATIALUPSCALEPARAMETER](../../../modules/xengine/document.md#pfn_hms_xeg_spatialupscaleparameter)) (GLenum pname, GLvoid \*param)

 | 

Defines the function pointer for setting the GPU spatial upscaling input parameter.

 |
| 

typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_RENDERSPATIALUPSCALE](../../../modules/xengine/document.md#pfn_hms_xeg_renderspatialupscale)) (GLuint inputTexture)

 | 

Defines the function pointer for executing the GPU spatial upscaling rendering command.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_SpatialUpscaleParameter](../../../modules/xengine/document.md#hms_xeg_spatialupscaleparameter) (GLenum pname, GLvoid \*param)

 | 

Sets the GPU spatial upscaling input parameter.

 |
| 

GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_RenderSpatialUpscale](../../../modules/xengine/document.md#hms_xeg_renderspatialupscale) (GLuint inputTexture)

 | 

Executes the GPU spatial upscaling rendering command.

 |
