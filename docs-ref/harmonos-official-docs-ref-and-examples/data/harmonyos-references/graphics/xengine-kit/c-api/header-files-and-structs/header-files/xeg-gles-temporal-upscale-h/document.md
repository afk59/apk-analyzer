# xeg\_gles\_temporal\_upscale.h

#### Overview

OpenGL ES APIs for AI temporal upscaling of XEngine. The recommended upscaling factor is \[1.25, 2.0\]. Before using the APIs in this header file, you need to call [HMS\_XEG\_GetString](../../../modules/xengine/document.md#hms_xeg_getstring) to query whether the [XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME](../../../modules/xengine/document.md#xeg_temporal_upscale_extension_name) extension is available.

**File to include**: <xengine/xeg\_gles\_temporal\_upscale.h>

**Library:** libxengine.so

**Syscap:** SystemCapability.Graphic.XEngine

**Since:** 6.0.0(20)

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

[XEG\_TEMPORAL\_UPSCALE\_INPUT\_SIZE](../../../modules/xengine/document.md#xeg_temporal_upscale_input_size) 0x1U

 | 

Sets the actual width and height of the upscaling input texture by calling [HMS\_XEG\_TemporalUpscaleParameter](../../../modules/xengine/document.md#hms_xeg_temporalupscaleparameter).

 |
| 

[XEG\_TEMPORAL\_UPSCALE\_JITTER\_NUM](../../../modules/xengine/document.md#xeg_temporal_upscale_jitter_num) 0x2U

 | 

Sets the number of camera jitter periods by calling [HMS\_XEG\_TemporalUpscaleParameter](../../../modules/xengine/document.md#hms_xeg_temporalupscaleparameter). The value range is \[4, 16\]. The recommended value is 8.

 |
| 

[XEG\_TEMPORAL\_UPSCALE\_DEPTH\_REVERSED](../../../modules/xengine/document.md#xeg_temporal_upscale_depth_reversed) 0x3U

 | 

Sets whether depth reversion exists by calling [HMS\_XEG\_TemporalUpscaleParameter](../../../modules/xengine/document.md#hms_xeg_temporalupscaleparameter). The value true indicates that depth reversion exists, and the value false indicates that depth reversion does not exist.

 |
| 

[XEG\_TEMPORAL\_UPSCALE\_RESET\_HISTORY](../../../modules/xengine/document.md#xeg_temporal_upscale_reset_history) 0x4U

 | 

Sets whether to reset historical frame data (true) or not (false). The value true is recommended if upscaling is not used for historical frames but is used for the current frame.

 |
| 

[XEG\_TEMPORAL\_UPSCALE\_STEADY\_LEVEL](../../../modules/xengine/document.md#xeg_temporal_upscale_steady_level) 0x5U

 | 

Sets images' degree of bias towards the current frame (less ghosting but more flickering) or historical frames (more ghosting but more stable) by calling [HMS\_XEG\_TemporalUpscaleParameter](../../../modules/xengine/document.md#hms_xeg_temporalupscaleparameter). The value range is \[0.0, 1.0\]. A larger value indicates a larger bias towards historical frames.

 |

#### \[h2\]Typedefs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_TemporalUpscaleParameter](../../../modules/xengine/document.md#pfn_hms_xeg_temporalupscaleparameter)) (GLenum pname, GLvoid \*param)

 | 

Defines the function pointer for setting the input parameters for AI temporal upscaling.

 |
| 

typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_RenderTemporalUpscale](../../../modules/xengine/document.md#pfn_hms_xeg_rendertemporalupscale)) (GLuint inputTexture, GLuint depthTexture, GLuint motionVectorTexture, GLuint dynamicMaskTexture, GLfloat jitterX, GLfloat jitterY)

 | 

Defines the function pointer for executing the rendering command for AI temporal upscaling.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_TemporalUpscaleParameter](../../../modules/xengine/document.md#hms_xeg_temporalupscaleparameter) (GLenum pname, const GLvoid \*param)

 | 

Sets input parameters for AI temporal upscaling.

 |
| 

GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_RenderTemporalUpscale](../../../modules/xengine/document.md#hms_xeg_rendertemporalupscale) (GLuint inputTexture, GLuint depthTexture, GLuint motionVectorTexture, GLuint dynamicMaskTexture, GLfloat jitterX, GLfloat jitterY)

 | 

Executes the rendering command for AI temporal upscaling.

 |
