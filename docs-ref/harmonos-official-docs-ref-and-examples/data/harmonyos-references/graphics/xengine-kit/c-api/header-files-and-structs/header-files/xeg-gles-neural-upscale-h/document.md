# xeg\_gles\_neural\_upscale.h

#### Overview

AI spatial upscaling APIs of XEngine. Before using APIs in this header file, you need to call the [HMS\_XEG\_GetString](../../../modules/xengine/document.md#hms_xeg_getstring) API to verify that extension [XEG\_NEURAL\_UPSCALE\_EXTENSION\_NAME](../../../modules/xengine/document.md#xeg_neural_upscale_extension_name) is available.

**File to include**: <xengine/xeg\_gles\_neural\_upscale.h>

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

[XEG\_NEURAL\_UPSCALE\_SCISSOR](../../../modules/xengine/document.md#xeg_neural_upscale_scissor) 0x1U

 | 

Sets the cropping window parameter for upscaling through the [HMS\_XEG\_NeuralUpscaleParameter](../../../modules/xengine/document.md#hms_xeg_neuralupscaleparameter) API. The cropping window is used to determine the area for sampling the input image.

 |
| 

[XEG\_NEURAL\_UPSCALE\_SHARPNESS](../../../modules/xengine/document.md#xeg_neural_upscale_sharpness) 0x2U

 | 

Sets the sharpness parameter for upscaling through the [HMS\_XEG\_NeuralUpscaleParameter](../../../modules/xengine/document.md#hms_xeg_neuralupscaleparameter) API. The recommended value range of sharpness is \[0, 1\].

 |
| 

[XEG\_NEURAL\_UPSCALE\_INPUT\_HANDLE](../../../modules/xengine/document.md#xeg_neural_upscale_input_handle) 0x4U

 | 

Sets the OH\_NativeBuffer handle associated with the upscaling input texture through the [HMS\_XEG\_NeuralUpscaleParameter](../../../modules/xengine/document.md#hms_xeg_neuralupscaleparameter) API.

 |

#### \[h2\]Typedefs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_NEURALUPSCALEPARAMETER](../../../modules/xengine/document.md#pfn_hms_xeg_neuralupscaleparameter)) (GLenum pname, GLvoid \*param)

 | 

Defines the function pointer for setting the AI spatial upscaling input parameter.

 |
| 

typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_RENDERNEURALUPSCALE](../../../modules/xengine/document.md#pfn_hms_xeg_renderneuralupscale)) (GLuint inputTexture)

 | 

Defines the function pointer for executing the AI spatial upscaling rendering command.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_NeuralUpscaleParameter](../../../modules/xengine/document.md#hms_xeg_neuralupscaleparameter) (GLenum pname, GLvoid \*param)

 | 

Sets the AI spatial upscaling input parameter.

 |
| 

GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_RenderNeuralUpscale](../../../modules/xengine/document.md#hms_xeg_renderneuralupscale) (GLuint inputTexture)

 | 

Executes the AI spatial upscaling rendering command.

 |
