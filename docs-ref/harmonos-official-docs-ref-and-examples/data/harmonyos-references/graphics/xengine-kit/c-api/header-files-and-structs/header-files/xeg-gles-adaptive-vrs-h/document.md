# xeg\_gles\_adaptive\_vrs.h

#### Overview

VRS APIs of XEngine. Before using APIs in this header file, you need to call the [HMS\_XEG\_GetString](../../../modules/xengine/document.md#hms_xeg_getstring) API to verify that extension [XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME](../../../modules/xengine/document.md#xeg_adaptive_vrs_extension_name) is available.

**File to include**: <xengine/xeg\_gles\_adaptive\_vrs.h>

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

[XEG\_ADAPTIVE\_VRS\_INPUT\_SIZE](../../../modules/xengine/document.md#xeg_adaptive_vrs_input_size) 0x1U

 | 

Sets the INPUT\_SIZE parameter of the [HMS\_XEG\_AdaptiveVRSParameter](../../../modules/xengine/document.md#hms_xeg_adaptivevrsparameter) API, indicating the image width and height finally rendered by the rendering pipeline of the previous frame.

 |
| 

[XEG\_ADAPTIVE\_VRS\_INPUT\_REGION](../../../modules/xengine/document.md#xeg_adaptive_vrs_input_region) 0x2U

 | 

Sets the INPUT\_REGION parameter of the [HMS\_XEG\_AdaptiveVRSParameter](../../../modules/xengine/document.md#hms_xeg_adaptivevrsparameter) API, indicating the image region finally rendered by the rendering pipeline of the previous frame.

 |
| 

[XEG\_ADAPTIVE\_VRS\_TEXEL\_SIZE](../../../modules/xengine/document.md#xeg_adaptive_vrs_texel_size) 0x3U

 | 

Sets the TEXEL\_SIZE parameter of the [HMS\_XEG\_AdaptiveVRSParameter](../../../modules/xengine/document.md#hms_xeg_adaptivevrsparameter) API.

 |
| 

[XEG\_ADAPTIVE\_VRS\_ERROR\_SENSITIVITY](../../../modules/xengine/document.md#xeg_adaptive_vrs_error_sensitivity) 0x4U

 | 

Sets the ERROR\_SENSITIVITY parameter of the [HMS\_XEG\_AdaptiveVRSParameter](../../../modules/xengine/document.md#hms_xeg_adaptivevrsparameter) API, indicating the threshold for controlling the generation of the shading rate image. A larger value indicates a smaller average shading rate, that is, the performance is better but the image quality deteriorates. The recommended value range is \[0, 1\].

 |
| 

[XEG\_ADAPTIVE\_VRS\_FLIP](../../../modules/xengine/document.md#xeg_adaptive_vrs_flip) 0x5U

 | 

Sets the FLIP parameter of the [HMS\_XEG\_AdaptiveVRSParameter](../../../modules/xengine/document.md#hms_xeg_adaptivevrsparameter) API, indicating whether to flip the image vertically.

 |

#### \[h2\]Typedefs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_ADAPTIVEVRSPARAMETER](../../../modules/xengine/document.md#pfn_hms_xeg_adaptivevrsparameter)) (GLenum pname, GLvoid \*param)

 | 

Defines the function pointer for setting the input parameter of the adaptive variable rate shading (VRS).

 |
| 

typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_DISPATCHADAPTIVEVRS](../../../modules/xengine/document.md#pfn_hms_xeg_dispatchadaptivevrs)) (GLfloat \*reprojectionMatrix, GLuint inputColorImage, GLuint inputDepthImage, GLuint shadingRateImage)

 | 

Defines the function pointer for computing the shading rate image.

 |
| 

typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_APPLYADAPTIVEVRS](../../../modules/xengine/document.md#pfn_hms_xeg_applyadaptivevrs)) (GLuint shadingRateImage)

 | 

Defines the function pointer for applying the shading rate image to the render target.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_AdaptiveVRSParameter](../../../modules/xengine/document.md#hms_xeg_adaptivevrsparameter) (GLenum pname, GLvoid \*param)

 | 

Sets parameters of the adaptive VRS.

 |
| 

GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_DispatchAdaptiveVRS](../../../modules/xengine/document.md#hms_xeg_dispatchadaptivevrs) (GLfloat \*reprojectionMatrix, GLuint inputColorImage, GLuint inputDepthImage, GLuint shadingRateImage)

 | 

Computes the shading rate image.

 |
| 

GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_ApplyAdaptiveVRS](../../../modules/xengine/document.md#hms_xeg_applyadaptivevrs) (GLuint shadingRateImage)

 | 

Applies the shading rate image to the render target.

 |
