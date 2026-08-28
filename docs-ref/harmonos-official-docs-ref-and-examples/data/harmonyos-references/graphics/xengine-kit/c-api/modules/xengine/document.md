# XEngine

#### Overview

Provides APIs related to XEngine graphics capabilities.

**Syscap:** SystemCapability.Graphic.XEngine

**Since:** 5.0.0(12)

#### Summary

#### \[h2\]Files

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[xeg\_extension\_defs.h](../../header-files-and-structs/header-files/xeg-extension-defs-h/document.md)

 | 

Provides extension macro definitions of XEngine.

 |
| 

[xeg\_gles\_adaptive\_vrs.h](../../header-files-and-structs/header-files/xeg-gles-adaptive-vrs-h/document.md)

 | 

VRS APIs of XEngine. Before using APIs in this header file, you need to call the [HMS\_XEG\_GetString](#hms_xeg_getstring) API to xengine-kit-xengineverify that extension [XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME](#xeg_adaptive_vrs_extension_name) is available.

 |
| 

[xeg\_gles\_extension.h](../../header-files-and-structs/header-files/xeg-gles-extension-h/document.md)

 | 

(OpenGL ES) API for querying extensions of XEngine.

 |
| 

[xeg\_gles\_neural\_upscale.h](../../header-files-and-structs/header-files/xeg-gles-neural-upscale-h/document.md)

 | 

AI spatial upscaling APIs of XEngine. Before using APIs in this header file, you need to call the [HMS\_XEG\_GetString](#hms_xeg_getstring) API to verify that extension [XEG\_NEURAL\_UPSCALE\_EXTENSION\_NAME](#xeg_neural_upscale_extension_name) is available.

 |
| 

[xeg\_gles\_spatial\_upscale.h](../../header-files-and-structs/header-files/xeg-gles-spatial-upscale-h/document.md)

 | 

OpenGL ES APIs for the GPU spatial upscaling feature of XEngine. Before using APIs in this header file, you need to call the [HMS\_XEG\_GetString](#hms_xeg_getstring) API to verify that extension [XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME](#xeg_spatial_upscale_extension_name) is available.

 |
| 

[xeg\_gles\_temporal\_upscale.h](../../header-files-and-structs/header-files/xeg-gles-temporal-upscale-h/document.md)

 | 

OpenGL ES APIs for AI temporal upscaling of XEngine. The recommended upscaling factor is \[1.25, 2.0\]. Before using the APIs in this header file, you need to call [HMS\_XEG\_GetString](#hms_xeg_getstring) to query whether the [XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME](#xeg_temporal_upscale_extension_name) extension is available.

 |
| 

[xeg\_vulkan\_adaptive\_vrs.h](../../header-files-and-structs/header-files/xeg-vulkan-adaptive-vrs-h/document.md)

 | 

Vulkan APIs for the adaptive VRS of XEngine. Before using APIs in this header file, you need to call the [HMS\_XEG\_EnumerateDeviceExtensionProperties](#hms_xeg_enumeratedeviceextensionproperties) API to verify that extension [XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME](#xeg_adaptive_vrs_extension_name) is available.

 |
| 

[xeg\_vulkan\_common.h](../../header-files-and-structs/header-files/xeg-vulkan-common-h/document.md)

 | 

Contains the common type definitions related to Vulkan in XEngine.

 |
| 

[xeg\_vulkan\_extension.h](../../header-files-and-structs/header-files/xeg-vulkan-extension-h/document.md)

 | 

(Vulkan) API for querying extensions of XEngine.

 |
| 

[xeg\_vulkan\_hps.h](../../header-files-and-structs/header-files/xeg-vulkan-hps-h/document.md)

 | 

APIs for the High Performance Shaders (HPS) feature of XEngine. Before using the APIs in this header file, you need to call [HMS\_XEG\_EnumerateDeviceExtensionProperties](#hms_xeg_enumeratedeviceextensionproperties) to check whether the HPS feature extension to be used is supported.

 |
| 

[xeg\_vulkan\_rt\_reflection.h](../../header-files-and-structs/header-files/xeg-vulkan-rt-reflection-h/document.md)

 | 

APIs for the RT Reflection feature of XEngine. Before using the APIs in this header file, you need to call [HMS\_XEG\_EnumerateDeviceExtensionProperties](#hms_xeg_enumeratedeviceextensionproperties) to query whether the [XEG\_RT\_REFLECTION\_EXTENSION\_NAME](#xeg_rt_reflection_extension_name) extension is available.

 |
| 

[xeg\_vulkan\_rt\_visible\_mask.h](../../header-files-and-structs/header-files/xeg-vulkan-rt-visible-mask-h/document.md)

 | 

APIs for the RT VisibleMask feature of XEngine. Before using the APIs in this header file, you need to call [HMS\_XEG\_EnumerateDeviceExtensionProperties](#hms_xeg_enumeratedeviceextensionproperties) to check whether the [XEG\_RT\_SHADOW\_AO\_EXTENSION\_NAME](#xeg_rt_shadow_ao_extension_name) extension is available.

 |
| 

[xeg\_vulkan\_rtgi.h](../../header-files-and-structs/header-files/xeg-vulkan-rtgi-h/document.md)

 | 

XEngine Vulkan APIs for the Ray-Traced Global Illumination feature, which provides two features: Dynamic Diffuse Global Illumination (DDGI) and Neural Network Global Illumination (NNGI). Before using the APIs in this header file, call [HMS\_XEG\_EnumerateDeviceExtensionProperties](#hms_xeg_enumeratedeviceextensionproperties) to check whether the [XEG\_RTGI\_EXTENSION\_NAME](#xeg_rtgi_extension_name) extension is available.

 |
| 

[xeg\_vulkan\_spatial\_upscale.h](../../header-files-and-structs/header-files/xeg-vulkan-spatial-upscale-h/document.md)

 | 

Vulkan APIs for the GPU spatial upscaling of XEngine. Before using APIs in this header file, you need to call the [HMS\_XEG\_EnumerateDeviceExtensionProperties](#hms_xeg_enumeratedeviceextensionproperties) API to verify that extension [XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME](#xeg_spatial_upscale_extension_name) is available.

 |
| 

[xeg\_vulkan\_temporal\_upscale.h](../../header-files-and-structs/header-files/xeg-vulkan-temporal-upscale-h/document.md)

 | 

AI temporal upscaling APIs of XEngine. The recommended upscaling multiple range is \[1.25, 2.0\]. Before using APIs in this header file, you need to call the [HMS\_XEG\_EnumerateDeviceExtensionProperties](#hms_xeg_enumeratedeviceextensionproperties) API to verify that extension [XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME](#xeg_temporal_upscale_extension_name) is available.

 |

#### \[h2\]Data Structures

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [XEG\_AdaptiveVRSCreateInfo](../../header-files-and-structs/structs/xeg-adaptivevrscreateinfo/document.md)

 | 

This structure describes the parameter information for creating an [XEG\_AdaptiveVRS](#xeg_adaptivevrs) object. When the information in the structure changes, a new [XEG\_AdaptiveVRS](#xeg_adaptivevrs) object needs to be created.

 |
| 

struct [XEG\_AdaptiveVRSDescription](../../header-files-and-structs/structs/xeg-adaptivevrsdescription/document.md)

 | 

This structure describes the parameter information required for delivering the command for drawing the shading rate texture. The information needs to be updated for each frame.

 |
| 

struct [XEG\_ExtensionProperties](../../header-files-and-structs/structs/xeg-extensionproperties/document.md)

 | 

This structure describes the set of XEngine extensions queried through the [HMS\_XEG\_EnumerateDeviceExtensionProperties](#hms_xeg_enumeratedeviceextensionproperties) API.

 |
| 

struct [XEG\_HPSCreateInfo](../../header-files-and-structs/structs/xeg-hpscreateinfo/document.md)

 | 

This structure describes the information for creating an [XEG\_HPS](#xeg_hps) object.

 |
| 

struct [XEG\_HPSRadixSort](../../header-files-and-structs/structs/xeg-hpsradixsort/document.md)

 | 

This structure describes the HPS radix sort extension structure information.

 |
| 

struct [XEG\_HPSRadixSortDescription](../../header-files-and-structs/structs/xeg-hpsradixsortdescription/document.md)

 | 

This structure describes the information required for sorting using the [XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](#xeg_hps_radix_sort_extension_name) feature.

 |
| 

struct [XEG\_RTReflectionCreateInfo](../../header-files-and-structs/structs/xeg-rtreflectioncreateinfo/document.md)

 | 

This structure describes the information for creating an [XEG\_RTReflection](#xeg_rtreflection) object. When the information in the structure changes, a new [XEG\_RTReflection](#xeg_rtreflection) object needs to be created.

 |
| 

struct [XEG\_RTReflectionDescription](../../header-files-and-structs/structs/xeg-rtreflectiondescription/document.md)

 | 

This structure describes the input information for sending a ray intersection command.

 |
| 

struct [XEG\_RTShadowAOCreateInfo](../../header-files-and-structs/structs/xeg-rtshadowaocreateinfo/document.md)

 | 

This structure describes the initialization information for creating an [XEG\_RTVisibleMask](#xeg_rtvisiblemask) instance that supports the Ray-Traced Shadow and Ambient Occlusion effects. When the information in the structure changes, a new [XEG\_RTVisibleMask](#xeg_rtvisiblemask) object needs to be created.

 |
| 

struct [XEG\_RTShadowParameters](../../header-files-and-structs/structs/xeg-rtshadowparameters/document.md)

 | 

Ray-Traced Shadow algorithm parameters.

 |
| 

struct [XEG\_RTAOParameters](../../header-files-and-structs/structs/xeg-rtaoparameters/document.md)

 | 

Ray-Traced Ambient Occlusion algorithm parameters.

 |
| 

struct [XEG\_RTShadowAODenoiserParameters](../../header-files-and-structs/structs/xeg-rtshadowaodenoiserparameters/document.md)

 | 

Denoising parameter for the Ray-Traced Shadow and Ambient Occlusion algorithms.

 |
| 

struct [XEG\_RTShadowAODescription](../../header-files-and-structs/structs/xeg-rtshadowaodescription/document.md)

 | 

This structure describes the input information of the rendering command for the Ray-Traced Shadow and Ambient Occlusion algorithms.

 |
| 

struct [XEG\_DDGIVolumeEntryParameters](../../header-files-and-structs/structs/xeg-ddgivolumeentryparameters/document.md)

 | 

This structure describes the mandatory parameters of each DDGI volume.

 |
| 

struct [XEG\_DDGICreateInfo](../../header-files-and-structs/structs/xeg-ddgicreateinfo/document.md)

 | 

This structure describes the information about creating an [XEG\_RTGI](#xeg_rtgi) object with the DDGI feature. If the information in the structure changes, a new [XEG\_RTGI](#xeg_rtgi) object needs to be created.

 |
| 

struct [XEG\_DDGIDescription](../../header-files-and-structs/structs/xeg-ddgidescription/document.md)

 | 

This structure describes the information required for updating the DDGI probe irradiance and rendering the output GI images.

 |
| 

struct [XEG\_NNGICreateInfo](../../header-files-and-structs/structs/xeg-nngicreateinfo/document.md)

 | 

This structure describes the information about creating an [XEG\_RTGI](#xeg_rtgi) object with the NNGI feature. If the information in the structure changes, a new [XEG\_RTGI](#xeg_rtgi) object needs to be created.

 |
| 

struct [XEG\_NNGIDescription](../../header-files-and-structs/structs/xeg-nngidescription/document.md)

 | 

This structure describes the information required for updating the NNGI to calculate the ray-traced global illumination.

 |
| 

struct [XEG\_SpatialUpscaleCreateInfo](../../header-files-and-structs/structs/xeg-spatialupscalecreateinfo/document.md)

 | 

This structure describes the information for creating an [XEG\_SpatialUpscale](#xeg_spatialupscale) object. When the information in the structure changes, a new XEG\_SpatialUpscale object needs to be created.

 |
| 

struct [XEG\_SpatialUpscaleDescription](../../header-files-and-structs/structs/xeg-spatialupscaledescription/document.md)

 | 

This structure describes the image information required for delivering the GPU spatial upscaling rendering command.

 |
| 

struct [XEG\_TemporalUpscaleCreateInfo](../../header-files-and-structs/structs/xeg-temporalupscalecreateinfo/document.md)

 | 

This structure describes the information for creating an [XEG\_TemporalUpscale](#xeg_temporalupscale) object. When the information in the structure changes, a new [XEG\_TemporalUpscale](#xeg_temporalupscale) object needs to be created.

 |
| 

struct [XEG\_TemporalUpscaleDescription](../../header-files-and-structs/structs/xeg-temporalupscaledescription/document.md)

 | 

This structure describes the input information for delivering AI temporal upscaling rendering command.

 |

#### \[h2\]Macros

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[XEG\_spatial\_upscale](#xeg_spatial_upscale) 1

 | 

Extension macro definition of GPU spatial upscaling of XEngine.

 |
| 

[XEG\_SPATIAL\_UPSCALE\_VERSION](#xeg_spatial_upscale_version) 1

 | 

Extension version number of GPU spatial upscaling of XEngine.

 |
| 

[XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME](#xeg_spatial_upscale_extension_name) "XEG\_spatial\_upscale"

 | 

Extension name of GPU spatial upscaling of XEngine.

 |
| 

[XEG\_neural\_upscale](#xeg_neural_upscale) 1

 | 

Extension macro definition of AI spatial upscaling of XEngine.

 |
| 

[XEG\_NEURAL\_UPSCALE\_VERSION](#xeg_neural_upscale_version) 1

 | 

Extension version number of AI spatial upscaling of XEngine.

 |
| 

[XEG\_NEURAL\_UPSCALE\_EXTENSION\_NAME](#xeg_neural_upscale_extension_name) "XEG\_neural\_upscale"

 | 

Extension name of AI spatial upscaling of XEngine.

 |
| 

[XEG\_temporal\_upscale](#xeg_temporal_upscale) 1

 | 

Extension macro definition of AI temporal upscaling of XEngine.

 |
| 

[XEG\_TEMPORAL\_UPSCALE\_VERSION](#xeg_temporal_upscale_version) 1

 | 

Extension version number of AI temporal upscaling of XEngine.

 |
| 

[XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME](#xeg_temporal_upscale_extension_name) "XEG\_temporal\_upscale"

 | 

Extension name of AI temporal upscaling of XEngine.

 |
| 

[XEG\_adaptive\_vrs](#xeg_adaptive_vrs) 1

 | 

Extension macro definition of adaptive VRS of XEngine.

 |
| 

[XEG\_ADAPTIVE\_VRS\_VERSION](#xeg_adaptive_vrs_version) 1

 | 

Extension version number of adaptive VRS of XEngine.

 |
| 

[XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME](#xeg_adaptive_vrs_extension_name) "XEG\_adaptive\_vrs"

 | 

Extension name of adaptive VRS of XEngine.

 |
| 

[XEG\_RTGI\_EXTENSION\_NAME](#xeg_rtgi_extension_name) "XEG\_rtgi"

 | 

Extension name of Ray-Traced Global Illumination of XEngine.

 |
| 

[XEG\_RT\_SHADOW\_AO\_EXTENSION\_NAME](#xeg_rt_shadow_ao_extension_name) "XEG\_rt\_shadow\_ao"

 | 

Extension name of Ray-Traced Shadow and Ambient Occlusion of XEngine.

 |
| 

[XEG\_RT\_REFLECTION\_EXTENSION\_NAME](#xeg_rt_reflection_extension_name) "XEG\_rt\_reflection"

 | 

Extension name of Ray-Traced Reflections of XEngine.

 |
| 

[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](#xeg_hps_radix_sort_extension_name) "XEG\_hps\_radix\_sort"

 | 

Extension name of HPS Radix Sort of XEngine.

 |
| 

[XEG\_ADAPTIVE\_VRS\_INPUT\_SIZE](#xeg_adaptive_vrs_input_size) 0x1U

 | 

Sets the INPUT\_SIZE parameter of the [HMS\_XEG\_AdaptiveVRSParameter](#hms_xeg_adaptivevrsparameter) API, indicating the image width and height finally rendered by the rendering pipeline of the previous frame.

 |
| 

[XEG\_ADAPTIVE\_VRS\_INPUT\_REGION](#xeg_adaptive_vrs_input_region) 0x2U

 | 

Sets the INPUT\_REGION parameter of the [HMS\_XEG\_AdaptiveVRSParameter](#hms_xeg_adaptivevrsparameter) API, indicating the image region finally rendered by the rendering pipeline of the previous frame.

 |
| 

[XEG\_ADAPTIVE\_VRS\_TEXEL\_SIZE](#xeg_adaptive_vrs_texel_size) 0x3U

 | 

Sets the TEXEL\_SIZE parameter of the [HMS\_XEG\_AdaptiveVRSParameter](#hms_xeg_adaptivevrsparameter) API.

 |
| 

[XEG\_ADAPTIVE\_VRS\_ERROR\_SENSITIVITY](#xeg_adaptive_vrs_error_sensitivity) 0x4U

 | 

Sets the ERROR\_SENSITIVITY parameter of the [HMS\_XEG\_AdaptiveVRSParameter](#hms_xeg_adaptivevrsparameter) API, indicating the threshold for controlling the generation of the shading rate image. A larger value indicates a smaller average shading rate, that is, the performance is better but the image quality deteriorates. The recommended value range is \[0, 1\].

 |
| 

[XEG\_ADAPTIVE\_VRS\_FLIP](#xeg_adaptive_vrs_flip) 0x5U

 | 

Sets the FLIP parameter of the [HMS\_XEG\_AdaptiveVRSParameter](#hms_xeg_adaptivevrsparameter) API, indicating whether to flip the image vertically.

 |
| 

[XEG\_EXTENSIONS](#xeg_extensions) 0x01U

 | 

Input parameter of the [HMS\_XEG\_GetString](#hms_xeg_getstring) API, which is used to obtain OpenGL ES extensions supported by XEngine.

 |
| 

[XEG\_NEURAL\_UPSCALE\_SCISSOR](#xeg_neural_upscale_scissor) 0x1U

 | 

Sets the cropping window parameter for upscaling through the [HMS\_XEG\_NeuralUpscaleParameter](#hms_xeg_neuralupscaleparameter) API. The cropping window is used to determine the area for sampling the input image.

 |
| 

[XEG\_NEURAL\_UPSCALE\_SHARPNESS](#xeg_neural_upscale_sharpness) 0x2U

 | 

Sets the sharpness parameter for upscaling through the [HMS\_XEG\_NeuralUpscaleParameter](#hms_xeg_neuralupscaleparameter) API. The recommended value range of sharpness is \[0, 1\].

 |
| 

[XEG\_NEURAL\_UPSCALE\_INPUT\_HANDLE](#xeg_neural_upscale_input_handle) 0x4U

 | 

Sets the OH\_NativeBuffer handle associated with the upscaling input texture through the [HMS\_XEG\_NeuralUpscaleParameter](#hms_xeg_neuralupscaleparameter) API.

 |
| 

[XEG\_SPATIAL\_UPSCALE\_SCISSOR](#xeg_spatial_upscale_scissor) 0x1U

 | 

Sets the SCISSOR parameter of the [HMS\_XEG\_SpatialUpscaleParameter](#hms_xeg_spatialupscaleparameter) API.

 |
| 

[XEG\_SPATIAL\_UPSCALE\_SHARPNESS](#xeg_spatial_upscale_sharpness) 0x2U

 | 

Sets the SHARPNESS parameter of the [HMS\_XEG\_SpatialUpscaleParameter](#hms_xeg_spatialupscaleparameter) API.

 |
| 

[XEG\_TEMPORAL\_UPSCALE\_INPUT\_SIZE](#xeg_temporal_upscale_input_size) 0x1U

 | 

Sets the actual width and height of the upscaling input texture by calling [HMS\_XEG\_TemporalUpscaleParameter](#hms_xeg_temporalupscaleparameter).

 |
| 

[XEG\_TEMPORAL\_UPSCALE\_JITTER\_NUM](#xeg_temporal_upscale_jitter_num) 0x2U

 | 

Sets the number of camera jitter periods by calling [HMS\_XEG\_TemporalUpscaleParameter](#hms_xeg_temporalupscaleparameter). The value range is \[4, 16\]. The recommended value is 8.

 |
| 

[XEG\_TEMPORAL\_UPSCALE\_DEPTH\_REVERSED](#xeg_temporal_upscale_depth_reversed) 0x3U

 | 

Sets whether depth reversion exists by calling [HMS\_XEG\_TemporalUpscaleParameter](#hms_xeg_temporalupscaleparameter). The value true indicates that depth reversion exists, and the value false indicates that depth reversion does not exist.

 |
| 

[XEG\_TEMPORAL\_UPSCALE\_RESET\_HISTORY](#xeg_temporal_upscale_reset_history) 0x4U

 | 

Sets whether to reset historical frame data (true) or not (false). The value true is recommended if upscaling is not used for historical frames but is used for the current frame.

 |
| 

[XEG\_TEMPORAL\_UPSCALE\_STEADY\_LEVEL](#xeg_temporal_upscale_steady_level) 0x5U

 | 

Sets images' degree of bias towards the current frame (less ghosting but more flickering) or historical frames (more ghosting but more stable) by calling [HMS\_XEG\_TemporalUpscaleParameter](#hms_xeg_temporalupscaleparameter). The value range is \[0.0, 1.0\]. A larger value indicates a larger bias towards historical frames.

 |
| 

[XEG\_MAX\_EXTENSION\_NAME\_SIZE](#xeg_max_extension_name_size) 256

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

typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_ADAPTIVEVRSPARAMETER](#pfn_hms_xeg_adaptivevrsparameter)) (GLenum pname, GLvoid \*param)

 | 

Defines the function pointer for setting the input parameter of the adaptive variable rate shading (VRS).

 |
| 

typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_DISPATCHADAPTIVEVRS](#pfn_hms_xeg_dispatchadaptivevrs)) (GLfloat \*reprojectionMatrix, GLuint inputColorImage, GLuint inputDepthImage, GLuint shadingRateImage)

 | 

Defines the function pointer for computing the shading rate image.

 |
| 

typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_APPLYADAPTIVEVRS](#pfn_hms_xeg_applyadaptivevrs)) (GLuint shadingRateImage)

 | 

Defines the function pointer for applying the shading rate image to the render target.

 |
| 

typedef const GLubyte \*(GL\_APIENTRYP [PFN\_HMS\_XEG\_GETSTRING](#pfn_hms_xeg_getstring)) (GLenum name)

 | 

Defines the function pointer of the OpenGL ES API for querying extensions of XEngine.

 |
| 

typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_NEURALUPSCALEPARAMETER](#pfn_hms_xeg_neuralupscaleparameter)) (GLenum pname, GLvoid \*param)

 | 

Defines the function pointer for setting the AI spatial upscaling input parameter.

 |
| 

typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_RENDERNEURALUPSCALE](#pfn_hms_xeg_renderneuralupscale)) (GLuint inputTexture)

 | 

Defines the function pointer for executing the AI spatial upscaling rendering command.

 |
| 

typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_SPATIALUPSCALEPARAMETER](#pfn_hms_xeg_spatialupscaleparameter)) (GLenum pname, GLvoid \*param)

 | 

Defines the function pointer for setting the GPU spatial upscaling input parameter.

 |
| 

typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_RENDERSPATIALUPSCALE](#pfn_hms_xeg_renderspatialupscale)) (GLuint inputTexture)

 | 

Defines the function pointer for executing the GPU spatial upscaling rendering command.

 |
| 

typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_TemporalUpscaleParameter](#pfn_hms_xeg_temporalupscaleparameter)) (GLenum pname, GLvoid \*param)

 | 

Defines the function pointer for setting the input parameters for AI temporal upscaling.

 |
| 

typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_RenderTemporalUpscale](#pfn_hms_xeg_rendertemporalupscale)) (GLuint inputTexture, GLuint depthTexture, GLuint motionVectorTexture, GLuint dynamicMaskTexture, GLfloat jitterX, GLfloat jitterY)

 | 

Defines the function pointer for executing the rendering command for AI temporal upscaling.

 |
| 

1:VK\_DEFINE\_HANDLE([XEG\_AdaptiveVRS](#xeg_adaptivevrs))

 | 

[XEG\_AdaptiveVRS](#xeg_adaptivevrs) handle.

 |
| 

typedef struct [XEG\_AdaptiveVRSCreateInfo](../../header-files-and-structs/structs/xeg-adaptivevrscreateinfo/document.md) XEG\_AdaptiveVRSCreateInfo

 | 

This structure describes the parameter information for creating an [XEG\_AdaptiveVRS](#xeg_adaptivevrs) object. When the information in the structure changes, a new [XEG\_AdaptiveVRS](#xeg_adaptivevrs) object needs to be created.

 |
| 

typedef struct [XEG\_AdaptiveVRSDescription](../../header-files-and-structs/structs/xeg-adaptivevrsdescription/document.md) XEG\_AdaptiveVRSDescription

 | 

This structure describes the parameter information required for delivering the command for drawing the shading rate texture. The information needs to be updated for each frame.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateAdaptiveVRS](#pfn_hms_xeg_createadaptivevrs)) (VkDevice device, const [XEG\_AdaptiveVRSCreateInfo](../../header-files-and-structs/structs/xeg-adaptivevrscreateinfo/document.md) \*pXegAdaptiveVRSCreateInfo, [XEG\_AdaptiveVRS](#xeg_adaptivevrs) \*pXegAdaptiveVRS)

 | 

Defines the function pointer for creating an [XEG\_AdaptiveVRS](#xeg_adaptivevrs) object.

 |
| 

typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdDispatchAdaptiveVRS](#pfn_hms_xeg_cmddispatchadaptivevrs)) (VkCommandBuffer commandBuffer, [XEG\_AdaptiveVRS](#xeg_adaptivevrs) xegAdaptiveVRS, [XEG\_AdaptiveVRSDescription](../../header-files-and-structs/structs/xeg-adaptivevrsdescription/document.md) \*pXegAdaptiveVRSDescription)

 | 

Defines the function pointer for computing the adaptive VRS command.

 |
| 

typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroyAdaptiveVRS](#pfn_hms_xeg_destroyadaptivevrs)) ([XEG\_AdaptiveVRS](#xeg_adaptivevrs) xegAdaptiveVRS)

 | 

Defines the function pointer for destroying an [XEG\_AdaptiveVRS](#xeg_adaptivevrs) object.

 |
| 

typedef enum [XEG\_StructureType](#xeg_structuretype) XEG\_StructureType

 | 

Enum for the XEngine structure types.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdSetSynchronization](#pfn_hms_xeg_cmdsetsynchronization)) (VkCommandBuffer commandBuffer, const void \*xegHandle)

 | 

Defines the function pointer for setting synchronization signals and waiting for the rendering result to be written to a specified image. When the RTGI feature is used, it is the GI rendering result that needs to be waited for before being written to a specified image.

 |
| 

typedef struct [XEG\_ExtensionProperties](../../header-files-and-structs/structs/xeg-extensionproperties/document.md) XEG\_ExtensionProperties

 | 

This structure describes the set of XEngine extensions queried through the [HMS\_XEG\_EnumerateDeviceExtensionProperties](#hms_xeg_enumeratedeviceextensionproperties) API.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_EnumerateDeviceExtensionProperties](#pfn_hms_xeg_enumeratedeviceextensionproperties)) (VkPhysicalDevice physicalDevice, uint32\_t \*pPropertyCount, [XEG\_ExtensionProperties](../../header-files-and-structs/structs/xeg-extensionproperties/document.md) \*pProperties)

 | 

Defines the function pointer of the Vulkan API for querying extensions of XEngine.

 |
| 

VK\_DEFINE\_HANDLE([XEG\_HPS](#xeg_hps))

 | 

Handle to [XEG\_HPS](#xeg_hps).

 |
| 

typedef struct [XEG\_HPSCreateInfo](../../header-files-and-structs/structs/xeg-hpscreateinfo/document.md) XEG\_HPSCreateInfo

 | 

This structure describes the information for creating an [XEG\_HPS](#xeg_hps) object.

 |
| 

typedef struct [XEG\_HPSRadixSort](../../header-files-and-structs/structs/xeg-hpsradixsort/document.md) XEG\_HPSRadixSort

 | 

This structure describes the HPS radix sort extension structure information.

 |
| 

typedef struct [XEG\_HPSRadixSortDescription](../../header-files-and-structs/structs/xeg-hpsradixsortdescription/document.md) XEG\_HPSRadixSortDescription

 | 

This structure describes the information required for sorting using the [XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](#xeg_hps_radix_sort_extension_name) feature.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateHPS](#pfn_hms_xeg_createhps)) (VkDevice device, const [XEG\_HPSCreateInfo](../../header-files-and-structs/structs/xeg-hpscreateinfo/document.md) \*pCreateInfo, [XEG\_HPS](#xeg_hps) \*pHps)

 | 

Defines the function pointer for creating an [XEG\_HPS](#xeg_hps) object.

 |
| 

typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroyHPS](#pfn_hms_xeg_destroyhps)) ([XEG\_HPS](#xeg_hps) hps)

 | 

Defines the function pointer for destroying an [XEG\_HPS](#xeg_hps) object.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdRadixSortHPS](#pfn_hms_xeg_cmdradixsorthps)) (VkCommandBuffer commandBuffer, [XEG\_HPS](#xeg_hps) hps, const [XEG\_HPSRadixSortDescription](../../header-files-and-structs/structs/xeg-hpsradixsortdescription/document.md) \*pDescription)

 | 

Defines the function pointer for recording an HPS radix sort command. Before using this API, you need to call [HMS\_XEG\_EnumerateDeviceExtensionProperties](#hms_xeg_enumeratedeviceextensionproperties) to check whether the [XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](#xeg_hps_radix_sort_extension_name) extension is supported.

 |
| 

VK\_DEFINE\_HANDLE([XEG\_RTReflection](#xeg_rtreflection))

 | 

Handle to [XEG\_RTReflection](#xeg_rtreflection).

 |
| 

typedef struct [XEG\_RTReflectionCreateInfo](../../header-files-and-structs/structs/xeg-rtreflectioncreateinfo/document.md) XEG\_RTReflectionCreateInfo

 | 

This structure describes the information for creating an [XEG\_RTReflection](#xeg_rtreflection) object. When the information in the structure changes, a new [XEG\_RTReflection](#xeg_rtreflection) object needs to be created.

 |
| 

typedef struct [XEG\_RTReflectionDescription](../../header-files-and-structs/structs/xeg-rtreflectiondescription/document.md) XEG\_RTReflectionDescription

 | 

This structure describes the input information for sending a ray intersection command.

 |
| 

typedef VkResult(VKAPI\_ATTR \* [PFN\_HMS\_XEG\_CreateRTReflection](#pfn_hms_xeg_creatertreflection)) (VkDevice device, const void \*pCreateInfo, [XEG\_RTReflection](#xeg_rtreflection) \*pRtReflection)

 | 

Defines the function pointer for creating an [XEG\_RTReflection](#xeg_rtreflection) object.

 |
| 

typedef VkResult VKAPI\_ATTR \* [PFN\_HMS\_XEG\_CmdRenderRTReflection](#pfn_hms_xeg_cmdrenderrtreflection)(VkCommandBuffer commandBuffer, [XEG\_RTReflection](#xeg_rtreflection) rtReflection, const void \*pDescription)

 | 

Defines the function pointer for recording the command for calculating the RT reflection hit information.

 |
| 

typedef void VKAPI\_ATTR \* [PFN\_HMS\_XEG\_DestroyRTReflection](#pfn_hms_xeg_destroyrtreflection)([XEG\_RTReflection](#xeg_rtreflection) rtReflection)

 | 

Defines the function pointer for destroying an [XEG\_RTReflection](#xeg_rtreflection) object.

 |
| 

VK\_DEFINE\_HANDLE([XEG\_RTVisibleMask](#xeg_rtvisiblemask))

 | 

Handle to [XEG\_RTVisibleMask](#xeg_rtvisiblemask), indicating the ray-traced VisibleMask feature instance. The shadow and ambient occlusion effects are supported.

 |
| 

typedef enum [XEG\_DenoiseQualityMode](#xeg_denoisequalitymode) XEG\_DenoiseQualityMode

 | 

Enumerates denoising quality modes.

 |
| 

typedef enum [XEG\_TraversalMode](#xeg_traversalmode) XEG\_TraversalMode

 | 

Enumerates traversal modes.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateRTVisibleMask](#pfn_hms_xeg_creatertvisiblemask)) (VkDevice device, const void \*pCreateInfo, [XEG\_RTVisibleMask](#xeg_rtvisiblemask) \*pRTVisibleMask)

 | 

Defines the function pointer for creating an [XEG\_RTVisibleMask](#xeg_rtvisiblemask) object.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdRenderRTVisibleMask](#pfn_hms_xeg_cmdrenderrtvisiblemask)) (VkCommandBuffer commandBuffer, [XEG\_RTVisibleMask](#xeg_rtvisiblemask) rtVisibleMask, const void \*pDescription)

 | 

Defines the function pointer for recording the ray-traced VisibleMask rendering command.

 |
| 

typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroyRTVisibleMask](#pfn_hms_xeg_destroyrtvisiblemask)) ([XEG\_RTVisibleMask](#xeg_rtvisiblemask) rtVisibleMask)

 | 

Defines the function pointer for destroying an [XEG\_RTVisibleMask](#xeg_rtvisiblemask) object.

 |
| 

VK\_DEFINE\_HANDLE([XEG\_RTGI](#xeg_rtgi))

 | 

Handle to [XEG\_RTGI](#xeg_rtgi).

 |
| 

typedef enum [XEG\_RTGIQualityMode](#xeg_rtgiqualitymode) XEG\_RTGIQualityMode

 | 

Enum for the quality modes of output images.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateRTGI](#pfn_hms_xeg_creatertgi)) (VkDevice device, const void \*pCreateInfo, [XEG\_RTGI](#xeg_rtgi) \*pRtGI)

 | 

Defines the function pointer for creating an [XEG\_RTGI](#xeg_rtgi) object.

 |
| 

typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroyRTGI](#pfn_hms_xeg_destroyrtgi)) ([XEG\_RTGI](#xeg_rtgi) rtGI)

 | 

Defines the function pointer for destroying an [XEG\_RTGI](#xeg_rtgi) object.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdRenderRTGI](#pfn_hms_xeg_cmdrenderrtgi)) (VkCommandBuffer commandBuffer, [XEG\_RTGI](#xeg_rtgi) rtGI, const void \*pDescription)

 | 

Defines the function pointer for executing the rendering command.

 |
| 

VK\_DEFINE\_HANDLE([XEG\_SpatialUpscale](#xeg_spatialupscale))

 | 

Handle to [XEG\_SpatialUpscale](#xeg_spatialupscale).

 |
| 

typedef struct [XEG\_SpatialUpscaleCreateInfo](../../header-files-and-structs/structs/xeg-spatialupscalecreateinfo/document.md) XEG\_SpatialUpscaleCreateInfo

 | 

This structure describes the information for creating an [XEG\_SpatialUpscale](#xeg_spatialupscale) object. When the information in the structure changes, a new XEG\_SpatialUpscale object needs to be created.

 |
| 

typedef struct [XEG\_SpatialUpscaleDescription](../../header-files-and-structs/structs/xeg-spatialupscaledescription/document.md) XEG\_SpatialUpscaleDescription

 | 

This structure describes the image information required for delivering the GPU spatial upscaling rendering command.

 |
| 

typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateSpatialUpscale](#pfn_hms_xeg_createspatialupscale)) (VkDevice device, const [XEG\_SpatialUpscaleCreateInfo](../../header-files-and-structs/structs/xeg-spatialupscalecreateinfo/document.md) \*pXegSpatialUpscaleCreateInfo, [XEG\_SpatialUpscale](#xeg_spatialupscale) \*pXegSpatialUpscale)

 | 

Defines the function pointer for creating an [XEG\_SpatialUpscale](#xeg_spatialupscale) object.

 |
| 

typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdRenderSpatialUpscale](#pfn_hms_xeg_cmdrenderspatialupscale)) (VkCommandBuffer commandBuffer, [XEG\_SpatialUpscale](#xeg_spatialupscale) xegSpatialUpscale, [XEG\_SpatialUpscaleDescription](../../header-files-and-structs/structs/xeg-spatialupscaledescription/document.md) \*pXegSpatialUpscaleDescription)

 | 

Defines the function pointer for executing the GPU spatial upscaling rendering command.

 |
| 

typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroySpatialUpscale](#pfn_hms_xeg_destroyspatialupscale)) ([XEG\_SpatialUpscale](#xeg_spatialupscale) xegSpatialUpscale)

 | 

Defines the function pointer for destroying an [XEG\_SpatialUpscale](#xeg_spatialupscale) object.

 |
| 

VK\_DEFINE\_HANDLE([XEG\_TemporalUpscale](#xeg_temporalupscale))

 | 

Handle to [XEG\_TemporalUpscale](#xeg_temporalupscale).

 |
| 

typedef struct [XEG\_TemporalUpscaleCreateInfo](../../header-files-and-structs/structs/xeg-temporalupscalecreateinfo/document.md) XEG\_TemporalUpscaleCreateInfo

 | 

This structure describes the information for creating an [XEG\_TemporalUpscale](#xeg_temporalupscale) object. When the information in the structure changes, a new [XEG\_TemporalUpscale](#xeg_temporalupscale) object needs to be created.

 |
| 

typedef struct [XEG\_TemporalUpscaleDescription](../../header-files-and-structs/structs/xeg-temporalupscaledescription/document.md) XEG\_TemporalUpscaleDescription

 | 

This structure describes the input information for delivering AI temporal upscaling rendering command.

 |
| 

typedef VkResult(VKAPI\_ATTR \* [PFN\_HMS\_XEG\_CreateTemporalUpscale](#pfn_hms_xeg_createtemporalupscale)) (VkDevice device, [XEG\_TemporalUpscaleCreateInfo](../../header-files-and-structs/structs/xeg-temporalupscalecreateinfo/document.md) \*pTemporalUpscaleInfo, [XEG\_TemporalUpscale](#xeg_temporalupscale) \*pTemporalUpscale)

 | 

Defines the function pointer for creating an [XEG\_TemporalUpscale](#xeg_temporalupscale) object.

 |
| 

typedef void(VKAPI\_ATTR \* [PFN\_HMS\_XEG\_CmdRenderTemporalUpscale](#pfn_hms_xeg_cmdrendertemporalupscale)) (VkCommandBuffer commandBuffer, [XEG\_TemporalUpscale](#xeg_temporalupscale) temporalUpscale, [XEG\_TemporalUpscaleDescription](../../header-files-and-structs/structs/xeg-temporalupscaledescription/document.md) \*pDescription)

 | 

Defines the function pointer for recording the AI temporal upscaling rendering command.

 |
| 

typedef void(VKAPI\_ATTR \* [PFN\_HMS\_XEG\_DestroyTemporalUpscale](#pfn_hms_xeg_destroytemporalupscale)) ([XEG\_TemporalUpscale](#xeg_temporalupscale) temporalUpscale)

 | 

Defines the function pointer for destroying an [XEG\_TemporalUpscale](#xeg_temporalupscale) object.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[XEG\_StructureType](#xeg_structuretype) {

XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_CREATE\_INFO = 0, XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_DESCRIPTION = 1, XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_CREATE\_INFO = 2, XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_DESCRIPTION = 3,

XEG\_STRUCTURE\_TYPE\_NNGI\_CREATE\_INFO = 4, XEG\_STRUCTURE\_TYPE\_NNGI\_DESCRIPTION = 5, XEG\_STRUCTURE\_TYPE\_DDGI\_CREATE\_INFO = 6, XEG\_STRUCTURE\_TYPE\_DDGI\_DESCRIPTION = 7,

XEG\_STRUCTURE\_TYPE\_HPS\_CREATE\_INFO = 1001, XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT = 1002, XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT\_DESCRIPTION = 1003

}

 | 

Enum for the XEngine structure types.

 |
| 

[XEG\_DenoiseQualityMode](#xeg_denoisequalitymode) { XEG\_DENOISE\_QUALITY\_MODE\_NONE = 0, XEG\_DENOISE\_QUALITY\_MODE\_QUALITY = 1, XEG\_DENOISE\_QUALITY\_MODE\_BALANCED = 2, XEG\_DENOISE\_QUALITY\_MODE\_PERFORMANCES = 3 }

 | 

Enumerates denoising quality modes.

 |
| 

[XEG\_TraversalMode](#xeg_traversalmode) { XEG\_TRAVERSAL\_MODE\_DEFAULT = 0, XEG\_TRAVERSAL\_MODE\_PERFORMANCES = 1 }

 | 

Enumerates traversal modes.

 |
| 

[XEG\_RTGIQualityMode](#xeg_rtgiqualitymode) { XEG\_RTGI\_QUALITY\_MODE\_QUALITY = 0, XEG\_RTGI\_QUALITY\_MODE\_BALANCED = 1, XEG\_RTGI\_QUALITY\_MODE\_PERFORMANCE = 2 }

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

GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_AdaptiveVRSParameter](#hms_xeg_adaptivevrsparameter) (GLenum pname, GLvoid \*param)

 | 

Sets parameters of the adaptive VRS.

 |
| 

GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_DispatchAdaptiveVRS](#hms_xeg_dispatchadaptivevrs) (GLfloat \*reprojectionMatrix, GLuint inputColorImage, GLuint inputDepthImage, GLuint shadingRateImage)

 | 

Computes the shading rate image.

 |
| 

GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_ApplyAdaptiveVRS](#hms_xeg_applyadaptivevrs) (GLuint shadingRateImage)

 | 

Applies the shading rate image to the render target.

 |
| 

const GLubyte \* [HMS\_XEG\_GetString](#hms_xeg_getstring) (GLenum name)

 | 

OpenGL ES API for querying extensions of XEngine.

 |
| 

GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_NeuralUpscaleParameter](#hms_xeg_neuralupscaleparameter) (GLenum pname, GLvoid \*param)

 | 

Sets the AI spatial upscaling input parameter.

 |
| 

GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_RenderNeuralUpscale](#hms_xeg_renderneuralupscale) (GLuint inputTexture)

 | 

Executes the AI spatial upscaling rendering command.

 |
| 

GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_SpatialUpscaleParameter](#hms_xeg_spatialupscaleparameter) (GLenum pname, GLvoid \*param)

 | 

Sets the GPU spatial upscaling input parameter.

 |
| 

GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_RenderSpatialUpscale](#hms_xeg_renderspatialupscale) (GLuint inputTexture)

 | 

Executes the GPU spatial upscaling rendering command.

 |
| 

GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_TemporalUpscaleParameter](#hms_xeg_temporalupscaleparameter) (GLenum pname, const GLvoid \*param)

 | 

Sets input parameters for AI temporal upscaling.

 |
| 

GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_RenderTemporalUpscale](#hms_xeg_rendertemporalupscale) (GLuint inputTexture, GLuint depthTexture, GLuint motionVectorTexture, GLuint dynamicMaskTexture, GLfloat jitterX, GLfloat jitterY)

 | 

Executes the rendering command for AI temporal upscaling.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateAdaptiveVRS](#hms_xeg_createadaptivevrs) (VkDevice device, [XEG\_AdaptiveVRSCreateInfo](../../header-files-and-structs/structs/xeg-adaptivevrscreateinfo/document.md) \*pXegAdaptiveVRSCreateInfo, [XEG\_AdaptiveVRS](#xeg_adaptivevrs) \*pXegAdaptiveVRS)

 | 

Creates an [XEG\_AdaptiveVRS](#xeg_adaptivevrs) object.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_CmdDispatchAdaptiveVRS](#hms_xeg_cmddispatchadaptivevrs) (VkCommandBuffer commandBuffer, [XEG\_AdaptiveVRS](#xeg_adaptivevrs) xegAdaptiveVRS, [XEG\_AdaptiveVRSDescription](../../header-files-and-structs/structs/xeg-adaptivevrsdescription/document.md) \*pXegAdaptiveVRSDescription)

 | 

Executes the command for computing the adaptive VRS.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyAdaptiveVRS](#hms_xeg_destroyadaptivevrs) ([XEG\_AdaptiveVRS](#xeg_adaptivevrs) xegAdaptiveVRS)

 | 

Destroys an [XEG\_AdaptiveVRS](#xeg_adaptivevrs) object.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdSetSynchronization](#hms_xeg_cmdsetsynchronization) (VkCommandBuffer commandBuffer, const void \*xegHandle)

 | 

Sets synchronization signals and waits for the rendering result to be written to a specified image. When the RTGI feature is used, it is the GI rendering result that needs to be waited for before being written to a specified image.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_EnumerateDeviceExtensionProperties](#hms_xeg_enumeratedeviceextensionproperties) (VkPhysicalDevice physicalDevice, uint32\_t \*pPropertyCount, [XEG\_ExtensionProperties](../../header-files-and-structs/structs/xeg-extensionproperties/document.md) \*pProperties)

 | 

Vulkan API for querying extensions of XEngine.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateHPS](#hms_xeg_createhps) (VkDevice device, const [XEG\_HPSCreateInfo](../../header-files-and-structs/structs/xeg-hpscreateinfo/document.md) \*pCreateInfo, [XEG\_HPS](#xeg_hps) \*pHps)

 | 

Creates an [XEG\_HPS](#xeg_hps) object.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyHPS](#hms_xeg_destroyhps) ([XEG\_HPS](#xeg_hps) hps)

 | 

Destroys an [XEG\_HPS](#xeg_hps) object.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdRadixSortHPS](#hms_xeg_cmdradixsorthps) (VkCommandBuffer commandBuffer, [XEG\_HPS](#xeg_hps) hps, const [XEG\_HPSRadixSortDescription](../../header-files-and-structs/structs/xeg-hpsradixsortdescription/document.md) \*pDescription)

 | 

Records an HPS radix sort command. Before using this API, you need to call {[} to check whether the XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME} extension is supported.](#hms_xeg_enumeratedeviceextensionproperties)

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateRTReflection](#hms_xeg_creatertreflection) (VkDevice device, const void \*pCreateInfo, [XEG\_RTReflection](#xeg_rtreflection) \*pRtReflection)

 | 

Creates an [XEG\_RTReflection](#xeg_rtreflection) object.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdRenderRTReflection](#hms_xeg_cmdrenderrtreflection) (VkCommandBuffer commandBuffer, [XEG\_RTReflection](#xeg_rtreflection) rtReflection, const void \*pDescription)

 | 

Records the command for calculating the RT reflection hit information.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyRTReflection](#hms_xeg_destroyrtreflection) ([XEG\_RTReflection](#xeg_rtreflection) rtReflection)

 | 

Destroys an [XEG\_RTReflection](#xeg_rtreflection) object.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateRTVisibleMask](#hms_xeg_creatertvisiblemask) (VkDevice device, const void \*pCreateInfo, [XEG\_RTVisibleMask](#xeg_rtvisiblemask) \*pRTVisibleMask)

 | 

Creates an [XEG\_RTVisibleMask](#xeg_rtvisiblemask) object.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdRenderRTVisibleMask](#hms_xeg_cmdrenderrtvisiblemask) (VkCommandBuffer commandBuffer, [XEG\_RTVisibleMask](#xeg_rtvisiblemask) rtVisibleMask, const void \*pDescription)

 | 

Records the ray-traced VisibleMask rendering command.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyRTVisibleMask](#hms_xeg_destroyrtvisiblemask) ([XEG\_RTVisibleMask](#xeg_rtvisiblemask) rtVisibleMask)

 | 

Destroys an [XEG\_RTVisibleMask](#xeg_rtvisiblemask) object.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateRTGI](#hms_xeg_creatertgi) (VkDevice device, const void \*pCreateInfo, [XEG\_RTGI](#xeg_rtgi) \*pRtGI)

 | 

Creates an [XEG\_RTGI](#xeg_rtgi) object.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyRTGI](#hms_xeg_destroyrtgi) ([XEG\_RTGI](#xeg_rtgi) rtGI)

 | 

Destroys an [XEG\_RTGI](#xeg_rtgi) object.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdRenderRTGI](#hms_xeg_cmdrenderrtgi) (VkCommandBuffer commandBuffer, [XEG\_RTGI](#xeg_rtgi) rtGI, const void \*pDescription)

 | 

Executes the rendering command.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateSpatialUpscale](#hms_xeg_createspatialupscale) (VkDevice device, const [XEG\_SpatialUpscaleCreateInfo](../../header-files-and-structs/structs/xeg-spatialupscalecreateinfo/document.md) \*pXegSpatialUpscaleCreateInfo, [XEG\_SpatialUpscale](#xeg_spatialupscale) \*pXegSpatialUpscale)

 | 

Creates an [XEG\_SpatialUpscale](#xeg_spatialupscale) object.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_CmdRenderSpatialUpscale](#hms_xeg_cmdrenderspatialupscale) (VkCommandBuffer commandBuffer, [XEG\_SpatialUpscale](#xeg_spatialupscale) xegSpatialUpscale, [XEG\_SpatialUpscaleDescription](../../header-files-and-structs/structs/xeg-spatialupscaledescription/document.md) \*pXegSpatialUpscaleDescription)

 | 

Executes the GPU spatial upscaling rendering command.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroySpatialUpscale](#hms_xeg_destroyspatialupscale) ([XEG\_SpatialUpscale](#xeg_spatialupscale) xegSpatialUpscale)

 | 

Destroys an [XEG\_SpatialUpscale](#xeg_spatialupscale) object.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateTemporalUpscale](#hms_xeg_createtemporalupscale) (VkDevice device, [XEG\_TemporalUpscaleCreateInfo](../../header-files-and-structs/structs/xeg-temporalupscalecreateinfo/document.md) \*pTemporalUpscaleInfo, [XEG\_TemporalUpscale](#xeg_temporalupscale) \*pTemporalUpscale)

 | 

Creates an [XEG\_TemporalUpscale](#xeg_temporalupscale) object.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_CmdRenderTemporalUpscale](#hms_xeg_cmdrendertemporalupscale) (VkCommandBuffer commandBuffer, [XEG\_TemporalUpscale](#xeg_temporalupscale) temporalUpscale, [XEG\_TemporalUpscaleDescription](../../header-files-and-structs/structs/xeg-temporalupscaledescription/document.md) \*pDescription)

 | 

Records the AI temporal upscaling rendering command.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyTemporalUpscale](#hms_xeg_destroytemporalupscale) ([XEG\_TemporalUpscale](#xeg_temporalupscale) temporalUpscale)

 | 

Destroys an [XEG\_TemporalUpscale](#xeg_temporalupscale) object.

 |

#### Macro Definition

#### \[h2\]XEG\_adaptive\_vrs

#define XEG\_adaptive\_vrs   1

**Description**

Extension macro definition of adaptive VRS of XEngine.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_ADAPTIVE\_VRS\_ERROR\_SENSITIVITY

#define XEG\_ADAPTIVE\_VRS\_ERROR\_SENSITIVITY   0x4U

**Description**

Sets the ERROR\_SENSITIVITY parameter of the [HMS\_XEG\_AdaptiveVRSParameter](#hms_xeg_adaptivevrsparameter) API, indicating the threshold for controlling the generation of the shading rate image. A larger value indicates a smaller average shading rate, that is, the performance is better but the image quality deteriorates. The recommended value range is \[0, 1\].

When this macro is used to set the ERROR\_SENSITIVITY parameter through the [HMS\_XEG\_AdaptiveVRSParameter](#hms_xeg_adaptivevrsparameter) API, param passed to the API must be a GLfloat pointer. Otherwise, undefined behavior will occur, for example, the rendering effect is incorrect or the program crashes. This parameter is optional, and the default value is 0.5.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME

#define XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME   "XEG\_adaptive\_vrs"

**Description**

Extension name of adaptive VRS of XEngine.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_ADAPTIVE\_VRS\_FLIP

#define XEG\_ADAPTIVE\_VRS\_FLIP   0x5U

**Description**

Sets the FLIP parameter of the [HMS\_XEG\_AdaptiveVRSParameter](#hms_xeg_adaptivevrsparameter) API, indicating whether to flip the image vertically.

When this macro is used to set the FLIP parameter through the [HMS\_XEG\_AdaptiveVRSParameter](#hms_xeg_adaptivevrsparameter) API, param passed to the API must be a GLboolean pointer. Otherwise, undefined behavior will occur, for example, the rendering effect is incorrect or the program crashes. This parameter is optional, and the default value is false. The value true indicates to flip the image vertically, and the value false indicates not to flip the image vertically.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_ADAPTIVE\_VRS\_INPUT\_REGION

#define XEG\_ADAPTIVE\_VRS\_INPUT\_REGION   0x2U

**Description**

Sets the INPUT\_REGION parameter of the [HMS\_XEG\_AdaptiveVRSParameter](#hms_xeg_adaptivevrsparameter) API, indicating the image region finally rendered by the rendering pipeline of the previous frame.

When this macro is used to set the INPUT\_REGION parameter through the [HMS\_XEG\_AdaptiveVRSParameter](#hms_xeg_adaptivevrsparameter) API, param passed to the API must be a GLuint array whose length is 4, which indicates the coordinates of the lower left corner and the width and height of the rendered image area, respectively. Otherwise, undefined behavior will occur, for example, the rendering effect is incorrect or the program crashes. This parameter is optional, and the default value is \[0, 0, INPUT\_SIZE\[0\], INPUT\_SIZE\[1\]\].

**Since:** 5.0.0(12)

#### \[h2\]XEG\_ADAPTIVE\_VRS\_INPUT\_SIZE

#define XEG\_ADAPTIVE\_VRS\_INPUT\_SIZE   0x1U

**Description**

Sets the INPUT\_SIZE parameter of the [HMS\_XEG\_AdaptiveVRSParameter](#hms_xeg_adaptivevrsparameter) API, indicating the image width and height finally rendered by the rendering pipeline of the previous frame.

When this macro is used to set the INPUT\_SIZE parameter through the [HMS\_XEG\_AdaptiveVRSParameter](#hms_xeg_adaptivevrsparameter) API, param passed to the API must be a GLsizei array whose length is 2. Otherwise, undefined behavior will occur, for example, the rendering effect is incorrect or the program crashes. This parameter is mandatory and must have the same width and height as inputColorImage of [HMS\_XEG\_DispatchAdaptiveVRS](#hms_xeg_dispatchadaptivevrs).

**Since:** 5.0.0(12)

#### \[h2\]XEG\_ADAPTIVE\_VRS\_TEXEL\_SIZE

#define XEG\_ADAPTIVE\_VRS\_TEXEL\_SIZE   0x3U

**Description**

Sets the TEXEL\_SIZE parameter of the [HMS\_XEG\_AdaptiveVRSParameter](#hms_xeg_adaptivevrsparameter) API.

When this macro is used to set the TEXEL\_SIZE parameter through the [HMS\_XEG\_AdaptiveVRSParameter](#hms_xeg_adaptivevrsparameter) API, param passed to the API must be a GLsizei array whose length is 2, which indicates TEXEL\_WIDTH and TEXEL\_HEIGHT, respectively. Otherwise, undefined behavior will occur, for example, the rendering effect is incorrect or the program crashes. This parameter is optional, and the value can be \[8, 8\] or \[16, 16\]. The default value is \[8, 8\].

**Since:** 5.0.0(12)

#### \[h2\]XEG\_ADAPTIVE\_VRS\_VERSION

#define XEG\_ADAPTIVE\_VRS\_VERSION   1

**Description**

Extension version number of adaptive VRS of XEngine.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_EXTENSIONS

#define XEG\_EXTENSIONS   0x01U

**Description**

Input parameter of the [HMS\_XEG\_GetString](#hms_xeg_getstring) API, which is used to obtain OpenGL ES extensions supported by XEngine.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME

#define XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME   "XEG\_hps\_radix\_sort"

**Description**

Extension name of HPS Radix Sort of XEngine.

**Since:** 6.0.0(20)

#### \[h2\]XEG\_MAX\_EXTENSION\_NAME\_SIZE

#define XEG\_MAX\_EXTENSION\_NAME\_SIZE   256

**Description**

Maximum length of the extension name supported by XEngine.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_neural\_upscale

#define XEG\_neural\_upscale   1

**Description**

Extension macro definition of AI spatial upscaling of XEngine.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_NEURAL\_UPSCALE\_EXTENSION\_NAME

#define XEG\_NEURAL\_UPSCALE\_EXTENSION\_NAME   "XEG\_neural\_upscale"

**Description**

Extension name of AI spatial upscaling of XEngine.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_NEURAL\_UPSCALE\_INPUT\_HANDLE

#define XEG\_NEURAL\_UPSCALE\_INPUT\_HANDLE   0x4U

**Description**

Sets the OH\_NativeBuffer handle associated with the upscaling input texture through the [HMS\_XEG\_NeuralUpscaleParameter](#hms_xeg_neuralupscaleparameter) API.

When this macro is used to set the upscaling input parameter, the value of param passed to the API must be a valid OH\_NativeBuffer handle corresponding to the inputTexture parameter passed to the [HMS\_XEG\_RenderNeuralUpscale](#hms_xeg_renderneuralupscale) API. Otherwise, undefined behavior will occur, for example, the rendering effect is incorrect or the program crashes. This parameter is mandatory.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_NEURAL\_UPSCALE\_SCISSOR

#define XEG\_NEURAL\_UPSCALE\_SCISSOR   0x1U

**Description**

Sets the cropping window parameter for upscaling through the [HMS\_XEG\_NeuralUpscaleParameter](#hms_xeg_neuralupscaleparameter) API. The cropping window is used to determine the area for sampling the input image.

When this macro is used to set cropping window parameters, the value of param passed to the API must be an unsigned integer array with a length of 4. Otherwise, undefined behavior will occur, for example, the rendering effect is incorrect or the program crashes. The values in the array are x, y, width, and height in sequence, where x and y determine the lower left corner of the cropping window, and width and height respectively determine the width and height of the cropping window. This parameter is optional, and the default value (0, 0, width of the input texture, height of the input texture) will be used if cropping window parameters are not set.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_NEURAL\_UPSCALE\_SHARPNESS

#define XEG\_NEURAL\_UPSCALE\_SHARPNESS   0x2U

**Description**

Sets the sharpness parameter for upscaling through the [HMS\_XEG\_NeuralUpscaleParameter](#hms_xeg_neuralupscaleparameter) API. The recommended value range of sharpness is \[0, 1\].

When this macro is used to set the sharpness parameter of upscaling, the value of param passed to the API must be a valid pointer pointing to a float value. Otherwise, undefined behavior will occur, for example, the rendering effect is incorrect or the program crashes. This parameter is optional, and the default value 0.2 will be used if the sharpness parameter is not set.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_NEURAL\_UPSCALE\_VERSION

#define XEG\_NEURAL\_UPSCALE\_VERSION   1

**Description**

Extension version number of AI spatial upscaling of XEngine.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_RT\_REFLECTION\_EXTENSION\_NAME

#define XEG\_RT\_REFLECTION\_EXTENSION\_NAME   "XEG\_rt\_reflection"

**Description**

Extension name of Ray-Traced Reflections of XEngine.

**Since:** 6.0.0(20)

#### \[h2\]XEG\_RT\_SHADOW\_AO\_EXTENSION\_NAME

#define XEG\_RT\_SHADOW\_AO\_EXTENSION\_NAME   "XEG\_rt\_shadow\_ao"

**Description**

Extension name of Ray-Traced Shadow and Ambient Occlusion of XEngine.

**Since:** 6.0.0(20)

#### \[h2\]XEG\_RTGI\_EXTENSION\_NAME

#define XEG\_RTGI\_EXTENSION\_NAME   "XEG\_rtgi"

**Description**

Extension name of Ray-Traced Global Illumination of XEngine.

**Since:** 6.0.0(20)

#### \[h2\]XEG\_spatial\_upscale

#define XEG\_spatial\_upscale   1

**Description**

Extension macro definition of GPU spatial upscaling of XEngine.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME

#define XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME   "XEG\_spatial\_upscale"

**Description**

Extension name of GPU spatial upscaling of XEngine.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_SPATIAL\_UPSCALE\_SCISSOR

#define XEG\_SPATIAL\_UPSCALE\_SCISSOR   0x1U

**Description**

Sets the SCISSOR parameter of the [HMS\_XEG\_SpatialUpscaleParameter](#hms_xeg_spatialupscaleparameter) API.

When this macro is used to set the SCISSOR parameter through the [HMS\_XEG\_SpatialUpscaleParameter](#hms_xeg_spatialupscaleparameter) API, the value of param passed to the API must be a pointer pointing to an unsigned integer array whose length is 4. Otherwise, undefined behavior will occur, for example, the rendering effect is incorrect or the program crashes. The four values of SCISSOR are the x and y coordinates of the lower left corner and the width and height of the cropping window in sequence.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_SPATIAL\_UPSCALE\_SHARPNESS

#define XEG\_SPATIAL\_UPSCALE\_SHARPNESS   0x2U

**Description**

Sets the SHARPNESS parameter of the [HMS\_XEG\_SpatialUpscaleParameter](#hms_xeg_spatialupscaleparameter) API.

When this macro is used to set the SHARPNESS parameter through the [HMS\_XEG\_SpatialUpscaleParameter](#hms_xeg_spatialupscaleparameter) API, the value of param passed to the API must be a pointer pointing to the float type. It is recommended that the value ranges from 0 to 1. Otherwise, undefined behavior will occur, for example, the rendering effect is incorrect or the program crashes. A larger value of SHARPNESS indicates a stronger sharpening effect. The sharpness needs to be adjusted for images of different styles. Otherwise, over-sharpening will occur, for example, the image has a lot of noises.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_SPATIAL\_UPSCALE\_VERSION

#define XEG\_SPATIAL\_UPSCALE\_VERSION   1

**Description**

Extension version number of GPU spatial upscaling of XEngine.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_temporal\_upscale

#define XEG\_temporal\_upscale   1

**Description**

Extension macro definition of AI temporal upscaling of XEngine.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_TEMPORAL\_UPSCALE\_DEPTH\_REVERSED

#define XEG\_TEMPORAL\_UPSCALE\_DEPTH\_REVERSED   0x3U

**Description**

Sets whether depth reversion exists by calling [HMS\_XEG\_TemporalUpscaleParameter](#hms_xeg_temporalupscaleparameter). The value true indicates that depth reversion exists, and the value false indicates that depth reversion does not exist.

When this macro is used to define whether depth inversion exists, the param value passed to the API must be a valid pointer to a GLboolean value. Otherwise, undefined behavior may occur, for example, the rendering effect is incorrect or the program crashes. This parameter is mandatory.

**Since:** 6.0.0(20)

#### \[h2\]XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME

#define XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME   "XEG\_temporal\_upscale"

**Description**

Extension name of AI temporal upscaling of XEngine.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_TEMPORAL\_UPSCALE\_INPUT\_SIZE

#define XEG\_TEMPORAL\_UPSCALE\_INPUT\_SIZE   0x1U

**Description**

Sets the actual width and height of the upscaling input texture by calling [HMS\_XEG\_TemporalUpscaleParameter](#hms_xeg_temporalupscaleparameter).

When this macro is used to set the input width and height, the param value passed to the API must be an unsigned integer array whose length is 2. Otherwise, undefined behavior may occur, for example, the rendering effect is incorrect or the program crashes. The values in the array are width and height in sequence, which determine the width and height of the input texture, respectively. This parameter is mandatory.

**Since:** 6.0.0(20)

#### \[h2\]XEG\_TEMPORAL\_UPSCALE\_JITTER\_NUM

#define XEG\_TEMPORAL\_UPSCALE\_JITTER\_NUM   0x2U

**Description**

Sets the number of camera jitter periods by calling [HMS\_XEG\_TemporalUpscaleParameter](#hms_xeg_temporalupscaleparameter). The value range is \[4, 16\]. The recommended value is 8.

When this macro is used to set the number of camera jitter periods, the param value passed to the API must be a valid pointer to a GLuint value. Otherwise, undefined behavior may occur, for example, the rendering effect is incorrect or the program crashes. This parameter is mandatory.

**Since:** 6.0.0(20)

#### \[h2\]XEG\_TEMPORAL\_UPSCALE\_RESET\_HISTORY

#define XEG\_TEMPORAL\_UPSCALE\_RESET\_HISTORY   0x4U

**Description**

Sets whether to reset historical frame data (true) or not (false). The value true is recommended if upscaling is not used for historical frames but is used for the current frame.

When this macro is used to define whether to reset historical frame data, the param value passed to the API must be a valid pointer to a GLboolean value. Otherwise, undefined behavior may occur, for example, the rendering effect is incorrect or the program crashes. This parameter is mandatory.

**Since:** 6.0.0(20)

#### \[h2\]XEG\_TEMPORAL\_UPSCALE\_STEADY\_LEVEL

#define XEG\_TEMPORAL\_UPSCALE\_STEADY\_LEVEL   0x5U

**Description**

Sets images' degree of bias towards the current frame (less ghosting but more flickering) or historical frames (more ghosting but more stable) by calling [HMS\_XEG\_TemporalUpscaleParameter](#hms_xeg_temporalupscaleparameter). The value range is \[0.0, 1.0\]. A larger value indicates a larger bias towards historical frames.

When this macro is used to set the degree of bias, the param value passed to the API must be a valid pointer to a GLfloat value. Otherwise, undefined behavior may occur, for example, the rendering effect is incorrect or the program crashes. This parameter is optional. The default value is 0.5.

**Since:** 6.0.0(20)

#### \[h2\]XEG\_TEMPORAL\_UPSCALE\_VERSION

#define XEG\_TEMPORAL\_UPSCALE\_VERSION   1

**Description**

Extension version number of AI temporal upscaling of XEngine.

**Since:** 5.0.0(12)

#### Typedef

#### \[h2\]PFN\_HMS\_XEG\_ADAPTIVEVRSPARAMETER

typedef void(GL\_APIENTRYP PFN\_HMS\_XEG\_ADAPTIVEVRSPARAMETER) (GLenum pname, GLvoid \*param)

**Description**

Defines the function pointer for setting the input parameter of the adaptive variable rate shading (VRS).

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

pname

 | 

Enumerated name of the input parameter. The value can be [XEG\_ADAPTIVE\_VRS\_INPUT\_SIZE](#xeg_adaptive_vrs_input_size), [XEG\_ADAPTIVE\_VRS\_INPUT\_REGION](#xeg_adaptive_vrs_input_region), [XEG\_ADAPTIVE\_VRS\_TEXEL\_SIZE](#xeg_adaptive_vrs_texel_size), [XEG\_ADAPTIVE\_VRS\_ERROR\_SENSITIVITY](#xeg_adaptive_vrs_error_sensitivity), or [XEG\_ADAPTIVE\_VRS\_FLIP](#xeg_adaptive_vrs_flip).

 |
| 

param

 | 

Input parameter value. For details, see the description of the enumerated names of the input parameters.

 |

#### \[h2\]PFN\_HMS\_XEG\_APPLYADAPTIVEVRS

typedef void(GL\_APIENTRYP PFN\_HMS\_XEG\_APPLYADAPTIVEVRS) (GLuint shadingRateImage)

**Description**

Defines the function pointer for applying the shading rate image to the render target.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

shadingRateImage

 | 

Shading rate image obtained after computation and 0 means disables adaptive VRS.

 |

#### \[h2\]PFN\_HMS\_XEG\_CmdDispatchAdaptiveVRS

typedef void(VKAPI\_PTR \* PFN\_HMS\_XEG\_CmdDispatchAdaptiveVRS) (VkCommandBuffer commandBuffer, XEG\_AdaptiveVRS xegAdaptiveVRS, XEG\_AdaptiveVRSDescription \*pXegAdaptiveVRSDescription)

**Description**

Defines the function pointer for computing the adaptive VRS command.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

commandBuffer

 | 

VkCommandBuffer of the current command, which must be submitted to vkQueueSubmit before being executed.

 |
| 

xegAdaptiveVRS

 | 

The [XEG\_AdaptiveVRS](#xeg_adaptivevrs) object that has been created.

 |
| 

pXegAdaptiveVRSDescription

 | 

Pointer to the parameter structure [XEG\_AdaptiveVRSDescription](../../header-files-and-structs/structs/xeg-adaptivevrsdescription/document.md) of the delivering command. Its value cannot be null.

 |

#### \[h2\]PFN\_HMS\_XEG\_CmdRadixSortHPS

typedef VkResult(VKAPI\_PTR \* PFN\_HMS\_XEG\_CmdRadixSortHPS) (VkCommandBuffer commandBuffer, XEG\_HPS hps, const XEG\_HPSRadixSortDescription \*pDescription)

**Description**

Defines the function pointer for recording an HPS radix sort command. Before using this API, you need to call [HMS\_XEG\_EnumerateDeviceExtensionProperties](#hms_xeg_enumeratedeviceextensionproperties) to check whether the [XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](#xeg_hps_radix_sort_extension_name) extension is supported.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

commandBuffer

 | 

Vulkan command buffer object.

 |
| 

hps

 | 

Created [XEG\_HPS](#xeg_hps) object.

 |
| 

pDescription

 | 

Pointer to the input information structure [XEG\_HPSRadixSortDescription](../../header-files-and-structs/structs/xeg-hpsradixsortdescription/document.md) of the [XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](#xeg_hps_radix_sort_extension_name) feature. The value cannot be null.

 |

**Returns:**

Returns an error code of the VkResult type. VK\_SUCCESS indicates successful execution.

#### \[h2\]PFN\_HMS\_XEG\_CmdRenderRTGI

typedef VkResult(VKAPI\_PTR \* PFN\_HMS\_XEG\_CmdRenderRTGI) (VkCommandBuffer commandBuffer, XEG\_RTGI rtGI, const void \*pDescription)

**Description**

Defines the function pointer for executing the rendering command.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

commandBuffer

 | 

VkCommandBuffer of the current command, which must be submitted to vkQueueSubmit before being executed.

 |
| 

rtGI

 | 

Created [XEG\_RTGI](#xeg_rtgi) object.

 |
| 

pDescription

 | 

Pointer to the structure containing the information needed for excuting the rendering command. If DDGI rendering is used, it is the pointer to the [XEG\_DDGIDescription](../../header-files-and-structs/structs/xeg-ddgidescription/document.md) structure. If NNGI rendering is used, it is the pointer to the [XEG\_NNGIDescription](../../header-files-and-structs/structs/xeg-nngidescription/document.md) structure. The value cannot be null.

 |

**Returns:**

Returns an error code of the VkResult type. VK\_SUCCESS indicates successful execution.

#### \[h2\]PFN\_HMS\_XEG\_CmdRenderRTReflection

typedef VkResult VKAPI\_ATTR\* PFN\_HMS\_XEG\_CmdRenderRTReflection(VkCommandBuffer commandBuffer, XEG\_RTReflection rtReflection, const void \*pDescription)

**Description**

Defines the function pointer for recording the command for calculating the RT reflection hit information.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

commandBuffer

 | 

Vulkan command buffer object, which must be of the primary type.

 |
| 

rtReflection

 | 

Created **XegAdaptiveVRS** object.

 |
| 

pDescription

 | 

Pointer to the reflection rendering input information structure [XEG\_RTReflectionDescription](../../header-files-and-structs/structs/xeg-rtreflectiondescription/document.md). The value cannot be null.

 |

#### \[h2\]PFN\_HMS\_XEG\_CmdRenderRTVisibleMask

typedef VkResult(VKAPI\_PTR \* PFN\_HMS\_XEG\_CmdRenderRTVisibleMask) (VkCommandBuffer commandBuffer, XEG\_RTVisibleMask rtVisibleMask, const void \*pDescription)

**Description**

Defines the function pointer for recording the ray-traced VisibleMask rendering command.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

commandBuffer

 | 

Vulkan command buffer object.

 |
| 

rtVisibleMask

 | 

Created [XEG\_RTVisibleMask](#xeg_rtvisiblemask) object.

 |
| 

pDescription

 | 

Pointer to the input parameter structure for executing the rendering command. Only pointers of the [XEG\_RTShadowAODescription](../../header-files-and-structs/structs/xeg-rtshadowaodescription/document.md) type are supported. The value cannot be null.

 |

**Returns:**

Error code of the VkResult type. If the value is VK\_SUCCESS, the execution is successful.

#### \[h2\]PFN\_HMS\_XEG\_CmdRenderSpatialUpscale

typedef void(VKAPI\_PTR \* PFN\_HMS\_XEG\_CmdRenderSpatialUpscale) (VkCommandBuffer commandBuffer, XEG\_SpatialUpscale xegSpatialUpscale, XEG\_SpatialUpscaleDescription \*pXegSpatialUpscaleDescription)

**Description**

Defines the function pointer for executing the GPU spatial upscaling rendering command.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

commandBuffer

 | 

VkCommandBuffer of the current command, which must be submitted to vkQueueSubmit before being executed.

 |
| 

xegSpatialUpscale

 | 

The [XEG\_SpatialUpscale](#xeg_spatialupscale) object that has been created.

 |
| 

pXegSpatialUpscaleDescription

 | 

Pointer to the parameter structure [XEG\_SpatialUpscaleDescription](../../header-files-and-structs/structs/xeg-spatialupscaledescription/document.md) of the rendering command. Its value cannot be null.

 |

#### \[h2\]PFN\_HMS\_XEG\_CmdRenderTemporalUpscale

typedef void(VKAPI\_ATTR \* PFN\_HMS\_XEG\_CmdRenderTemporalUpscale) (VkCommandBuffer commandBuffer, XEG\_TemporalUpscale temporalUpscale, XEG\_TemporalUpscaleDescription \*pDescription)

**Description**

Defines the function pointer for recording the AI temporal upscaling rendering command.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

commandBuffer

 | 

Vulkan command buffer object, which must be of the primary type.

 |
| 

temporalUpscale

 | 

The [XEG\_TemporalUpscale](#xeg_temporalupscale) object that has been created.

 |
| 

pDescription

 | 

Pointer to the upscaling rendering input information structure [XEG\_TemporalUpscaleDescription](../../header-files-and-structs/structs/xeg-temporalupscaledescription/document.md). Its value cannot be null.

 |

#### \[h2\]PFN\_HMS\_XEG\_CmdSetSynchronization

typedef VkResult(VKAPI\_PTR \* PFN\_HMS\_XEG\_CmdSetSynchronization) (VkCommandBuffer commandBuffer, const void \*xegHandle)

**Description**

Defines the function pointer for setting synchronization signals and waiting for the rendering result to be written to a specified image. When the RTGI feature is used, it is the GI rendering result that needs to be waited for before being written to a specified image.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

commandBuffer

 | 

VkCommandBuffer of the current command, which must be submitted to vkQueueSubmit before being executed.

 |
| 

xegHandle

 | 

Created handle object. When the RTGI feature is used, the object is the created [XEG\_RTGI](#xeg_rtgi) object.

 |

**Returns:**

Returns an error code of the VkResult type. VK\_SUCCESS indicates successful execution.

#### \[h2\]PFN\_HMS\_XEG\_CreateAdaptiveVRS

typedef VkResult(VKAPI\_PTR \* PFN\_HMS\_XEG\_CreateAdaptiveVRS) (VkDevice device, const XEG\_AdaptiveVRSCreateInfo \*pXegAdaptiveVRSCreateInfo, XEG\_AdaptiveVRS \*pXegAdaptiveVRS)

**Description**

Defines the function pointer for creating an [XEG\_AdaptiveVRS](#xeg_adaptivevrs) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

device

 | 

Must be the VkDevice in use.

 |
| 

pXegAdaptiveVRSCreateInfo

 | 

Pointer to the structure [XEG\_AdaptiveVRSCreateInfo](../../header-files-and-structs/structs/xeg-adaptivevrscreateinfo/document.md). Its value cannot be null.

 |
| 

pXegAdaptiveVRS

 | 

Pointer to the handle. The created [XEG\_AdaptiveVRS](#xeg_adaptivevrs) is returned in this handle.

 |

**Returns:**

Returns an error code of the VkResult type. VK\_SUCCESS indicates successful execution.

#### \[h2\]PFN\_HMS\_XEG\_CreateHPS

typedef VkResult(VKAPI\_PTR \* PFN\_HMS\_XEG\_CreateHPS) (VkDevice device, const XEG\_HPSCreateInfo \*pCreateInfo, XEG\_HPS \*pHps)

**Description**

Defines the function pointer for creating an [XEG\_HPS](#xeg_hps) object.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

device

 | 

VkDevice that is currently in use.

 |
| 

pCreateInfo

 | 

Pointer to the structure containing the information needed for creating an [XEG\_HPS](#xeg_hps) instance handle. The value cannot be null.

 |
| 

pHps

 | 

Pointer to the HPS instance handle. The created [XEG\_HPS](#xeg_hps) is returned in this handle.

 |

**Returns:**

Returns an error code of the VkResult type. VK\_SUCCESS indicates successful execution.

#### \[h2\]PFN\_HMS\_XEG\_CreateRTGI

typedef VkResult(VKAPI\_PTR \* PFN\_HMS\_XEG\_CreateRTGI) (VkDevice device, const void \*pCreateInfo, XEG\_RTGI \*pRtGI)

**Description**

Defines the function pointer for creating an [XEG\_RTGI](#xeg_rtgi) object.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

device

 | 

VkDevice that is currently in use.

 |
| 

pCreateInfo

 | 

Pointer to the structure containing the information needed for creating an [XEG\_RTGI](#xeg_rtgi) object. If a DDGI handle is created, it is the pointer to the [XEG\_DDGICreateInfo](../../header-files-and-structs/structs/xeg-ddgicreateinfo/document.md) structure. If an NNGI handle is created, it is the pointer to the [XEG\_NNGICreateInfo](../../header-files-and-structs/structs/xeg-nngicreateinfo/document.md) structure. The value cannot be null.

 |
| 

pRtGI

 | 

Pointer to the handle. The created [XEG\_RTGI](#xeg_rtgi) is returned in this handle.

 |

**Returns:**

Returns an error code of the VkResult type. VK\_SUCCESS indicates successful execution.

#### \[h2\]PFN\_HMS\_XEG\_CreateRTReflection

typedef VkResult(VKAPI\_ATTR \* PFN\_HMS\_XEG\_CreateRTReflection) (VkDevice device, const void \*pCreateInfo, XEG\_RTReflection \*pRtReflection)

**Description**

Defines the function pointer for creating an [XEG\_RTReflection](#xeg_rtreflection) object.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

device

 | 

VkDevice that is currently in use.

 |
| 

pCreateInfo

 | 

Pointer to the structure containing the information needed for creating a reflection instance handle. Currently, only pointers of the [XEG\_RTReflectionCreateInfo](../../header-files-and-structs/structs/xeg-rtreflectioncreateinfo/document.md) type are supported. The value cannot be null.

 |
| 

pRtReflection

 | 

Pointer to the reflection instance handle. The created [XEG\_RTReflection](#xeg_rtreflection) is returned in this handle.

 |

**Returns:**

Returns an error code of the VkResult type. VK\_SUCCESS indicates successful execution.

#### \[h2\]PFN\_HMS\_XEG\_CreateRTVisibleMask

typedef VkResult(VKAPI\_PTR \* PFN\_HMS\_XEG\_CreateRTVisibleMask) (VkDevice device, const void \*pCreateInfo, XEG\_RTVisibleMask \*pRTVisibleMask)

**Description**

Defines the function pointer for creating an [XEG\_RTVisibleMask](#xeg_rtvisiblemask) object.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

device

 | 

VkDevice that is currently in use.

 |
| 

pCreateInfo

 | 

Pointer to the structure of the description information required for creating a VisibleMask instance handle. Currently, only pointers of the [XEG\_RTShadowAOCreateInfo](../../header-files-and-structs/structs/xeg-rtshadowaocreateinfo/document.md) type are supported. The value cannot be null.

 |
| 

pRTVisibleMask

 | 

Pointer to the VisibleMask instance handle. The created [XEG\_RTVisibleMask](#xeg_rtvisiblemask) is returned in this handle.

 |

**Returns:**

Error code of the VkResult type. If the value is VK\_SUCCESS, the creation is successful.

#### \[h2\]PFN\_HMS\_XEG\_CreateSpatialUpscale

typedef VkResult(VKAPI\_PTR \* PFN\_HMS\_XEG\_CreateSpatialUpscale) (VkDevice device, const XEG\_SpatialUpscaleCreateInfo \*pXegSpatialUpscaleCreateInfo, XEG\_SpatialUpscale \*pXegSpatialUpscale)

**Description**

Defines the function pointer for creating an [XEG\_SpatialUpscale](#xeg_spatialupscale) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

device

 | 

Must be the VkDevice in use.

 |
| 

pXegSpatialUpscaleCreateInfo

 | 

Pointer to the structure [XEG\_SpatialUpscaleCreateInfo](../../header-files-and-structs/structs/xeg-spatialupscalecreateinfo/document.md). Its value cannot be null.

 |
| 

pXegSpatialUpscale

 | 

Pointer to the handle. The created [XEG\_SpatialUpscale](#xeg_spatialupscale) is returned in this handle.

 |

**Returns:**

Returns an error code of the VkResult type. VK\_SUCCESS indicates successful execution.

#### \[h2\]PFN\_HMS\_XEG\_CreateTemporalUpscale

typedef VkResult(VKAPI\_ATTR \* PFN\_HMS\_XEG\_CreateTemporalUpscale) (VkDevice device, XEG\_TemporalUpscaleCreateInfo \*pTemporalUpscaleInfo, XEG\_TemporalUpscale \*pTemporalUpscale)

**Description**

Defines the function pointer for creating an [XEG\_TemporalUpscale](#xeg_temporalupscale) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

device

 | 

Must be the VkDevice in use.

 |
| 

pTemporalUpscaleInfo

 | 

Pointer to the upscaling creation information structure [XEG\_TemporalUpscaleCreateInfo](../../header-files-and-structs/structs/xeg-temporalupscalecreateinfo/document.md). Its value cannot be null.

 |
| 

pTemporalUpscale

 | 

Pointer to the handle. The created [XEG\_TemporalUpscale](#xeg_temporalupscale) is returned in this handle.

 |

**Returns:**

Returns an error code of the VkResult type. VK\_SUCCESS indicates successful execution.

#### \[h2\]PFN\_HMS\_XEG\_DestroyAdaptiveVRS

typedef void(VKAPI\_PTR \* PFN\_HMS\_XEG\_DestroyAdaptiveVRS) (XEG\_AdaptiveVRS xegAdaptiveVRS)

**Description**

Defines the function pointer for destroying an [XEG\_AdaptiveVRS](#xeg_adaptivevrs) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

xegAdaptiveVRS

 | 

The [XEG\_AdaptiveVRS](#xeg_adaptivevrs) object that has been created.

 |

#### \[h2\]PFN\_HMS\_XEG\_DestroyHPS

typedef void(VKAPI\_PTR \* PFN\_HMS\_XEG\_DestroyHPS) (XEG\_HPS hps)

**Description**

Defines the function pointer for destroying an [XEG\_HPS](#xeg_hps) object.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

hps

 | 

[XEG\_HPS](#xeg_hps) object to be destroyed.

 |

#### \[h2\]PFN\_HMS\_XEG\_DestroyRTGI

typedef void(VKAPI\_PTR \* PFN\_HMS\_XEG\_DestroyRTGI) (XEG\_RTGI rtGI)

**Description**

Defines the function pointer for destroying an [XEG\_RTGI](#xeg_rtgi) object.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

rtGI

 | 

Created [XEG\_RTGI](#xeg_rtgi) object.

 |

#### \[h2\]PFN\_HMS\_XEG\_DestroyRTReflection

typedef void VKAPI\_ATTR\* PFN\_HMS\_XEG\_DestroyRTReflection(XEG\_RTReflection rtReflection)

**Description**

Defines the function pointer for destroying an [XEG\_RTReflection](#xeg_rtreflection) object.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

rtReflection

 | 

[XEG\_RTReflection](#xeg_rtreflection) object to be destroyed.

 |

#### \[h2\]PFN\_HMS\_XEG\_DestroyRTVisibleMask

typedef void(VKAPI\_PTR \* PFN\_HMS\_XEG\_DestroyRTVisibleMask) (XEG\_RTVisibleMask rtVisibleMask)

**Description**

Defines the function pointer for destroying an [XEG\_RTVisibleMask](#xeg_rtvisiblemask) object.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

rtVisibleMask

 | 

[XEG\_RTVisibleMask](#xeg_rtvisiblemask) object to be destroyed.

 |

#### \[h2\]PFN\_HMS\_XEG\_DestroySpatialUpscale

typedef void(VKAPI\_PTR \* PFN\_HMS\_XEG\_DestroySpatialUpscale) (XEG\_SpatialUpscale xegSpatialUpscale)

**Description**

Defines the function pointer for destroying an [XEG\_SpatialUpscale](#xeg_spatialupscale) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

xegSpatialUpscale

 | 

The [XEG\_SpatialUpscale](#xeg_spatialupscale) object that has been created.

 |

#### \[h2\]PFN\_HMS\_XEG\_DestroyTemporalUpscale

typedef void(VKAPI\_ATTR \* PFN\_HMS\_XEG\_DestroyTemporalUpscale) (XEG\_TemporalUpscale temporalUpscale)

**Description**

Defines the function pointer for destroying an [XEG\_TemporalUpscale](#xeg_temporalupscale) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

temporalUpscale

 | 

The [XEG\_TemporalUpscale](#xeg_temporalupscale) object to destroy.

 |

#### \[h2\]PFN\_HMS\_XEG\_DISPATCHADAPTIVEVRS

typedef void(GL\_APIENTRYP PFN\_HMS\_XEG\_DISPATCHADAPTIVEVRS) (GLfloat \*reprojectionMatrix, GLuint inputColorImage, GLuint inputDepthImage, GLuint shadingRateImage)

**Description**

Defines the function pointer for computing the shading rate image.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

reprojectionMatrix

 | 

Pointer to the result matrix of the computation between the current frame and the previous frame. The computation formula is as follows: (Projection matrix of the previous frame x Observation matrix of the previous frame) x (Inverse matrix of (Projection matrix of the current frame x Observation matrix of the current frame)). The matrix must be a 4 x 4 column major-order matrix. This parameter is optional, the image quality is better when it is not empty.

 |
| 

inputColorImage

 | 

Texture ID of the color attachment containing the final rendering result of the rendering pipeline of the previous frame.

 |
| 

inputDepthImage

 | 

Texture ID of the depth attachment containing the rendering result of the rendering pipeline of the current frame.

 |
| 

shadingRateImage

 | 

Texture ID used to generate the shading rate image information, which needs to be created and entered by the user.

 |

#### \[h2\]PFN\_HMS\_XEG\_EnumerateDeviceExtensionProperties

typedef VkResult(VKAPI\_PTR \* PFN\_HMS\_XEG\_EnumerateDeviceExtensionProperties) (VkPhysicalDevice physicalDevice, uint32\_t \*pPropertyCount, XEG\_ExtensionProperties \*pProperties)

**Description**

Defines the function pointer of the Vulkan API for querying extensions of XEngine.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

physicalDevice

 | 

Current Vulkan physical device.

 |
| 

pPropertyCount

 | 

Number of queried or passed extensions. If **pProperties** is nullptr, the number of currently supported XEngine extensions is returned. If the passed **propertyCount** is greater than or equal to the number of actually supported XEngine extensions, the query information is returned through the **pProperties** API and the return result is VK\_SUCCESS. If the passed **propertyCount** is less than the number of actually supported XEngine extensions, the query information is returned through the **pProperties** API and the return result is VK\_INCOMPLETE.

 |
| 

pProperties

 | 

Queried XEngine extensions, which are returned through the [XEG\_ExtensionProperties](../../header-files-and-structs/structs/xeg-extensionproperties/document.md) pointer of the structure.

 |

**Returns:**

Result code of the VkResult type. If the query is successful, VK\_SUCCESS is returned. If **pProperties** is not nullptr and the passed **propertyCount** is less than the number of actually supported XEngine extensions, VK\_INCOMPLETE is returned, indicating that the queried features are incomplete.

#### \[h2\]PFN\_HMS\_XEG\_GETSTRING

typedef const GLubyte\*(GL\_APIENTRYP PFN\_HMS\_XEG\_GETSTRING) (GLenum name)

**Description**

Defines the function pointer of the OpenGL ES API for querying extensions of XEngine.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

name

 | 

Enumerated name of the input parameter. The value can be [XEG\_EXTENSIONS](#xeg_extensions).

 |

**Returns:**

If the parameter is [XEG\_EXTENSIONS](#xeg_extensions), a list of extensions supported by XEngine is returned. Multiple extensions are separated by spaces. Note that the extension name does not contain any space. If the query fails, null pointer is returned.

#### \[h2\]PFN\_HMS\_XEG\_NEURALUPSCALEPARAMETER

typedef void(GL\_APIENTRYP PFN\_HMS\_XEG\_NEURALUPSCALEPARAMETER) (GLenum pname, GLvoid \*param)

**Description**

Defines the function pointer for setting the AI spatial upscaling input parameter.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

pname

 | 

Enumerated name of the input parameter. The value can be [XEG\_NEURAL\_UPSCALE\_SCISSOR](#xeg_neural_upscale_scissor), [XEG\_NEURAL\_UPSCALE\_SHARPNESS](#xeg_neural_upscale_sharpness), or [XEG\_NEURAL\_UPSCALE\_INPUT\_HANDLE](#xeg_neural_upscale_input_handle).

 |
| 

param

 | 

Input parameter value. For details, see the description of the enumerated names of the input parameters.

 |

#### \[h2\]PFN\_HMS\_XEG\_RENDERNEURALUPSCALE

typedef void(GL\_APIENTRYP PFN\_HMS\_XEG\_RENDERNEURALUPSCALE) (GLuint inputTexture)

**Description**

Defines the function pointer for executing the AI spatial upscaling rendering command.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

inputTexture

 | 

The input texture. The texture type must be GL\_TEXTURE\_2D, and there is only 1 mipLevel. The valid value range of the input image width is \[448, 1728\], Otherwise, the AI inference result may be incorrect. The input texture must be created by OH\_NativeBuffer. Before calling this API, you need to set the handle corresponding to OH\_NativeBuffer as the upscaling input parameter. For details, see the [HMS\_XEG\_NeuralUpscaleParameter](#hms_xeg_neuralupscaleparameter) API.

 |

#### \[h2\]PFN\_HMS\_XEG\_RENDERSPATIALUPSCALE

typedef void(GL\_APIENTRYP PFN\_HMS\_XEG\_RENDERSPATIALUPSCALE) (GLuint inputTexture)

**Description**

Defines the function pointer for executing the GPU spatial upscaling rendering command.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

inputTexture

 | 

Input texture. The texture type must be GL\_TEXTURE\_2D, and there is only 1 mipLevel. The texture must be created before this API is called. Otherwise, the rendering will fail, for example, a black screen occurs.

 |

#### \[h2\]PFN\_HMS\_XEG\_RenderTemporalUpscale

typedef void(GL\_APIENTRYP PFN\_HMS\_XEG\_RenderTemporalUpscale) (GLuint inputTexture, GLuint depthTexture, GLuint motionVectorTexture, GLuint dynamicMaskTexture, GLfloat jitterX, GLfloat jitterY)

**Description**

Defines the function pointer for executing the rendering command for AI temporal upscaling.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

inputTexture

 | 

Upscaling input texture. The input texture is of the GL\_TEXTURE\_2D type, mipLevels is 1, and the maximum dimensions supported are 2048 x 1024.

 |
| 

depthTexture

 | 

Depth texture.

 |
| 

motionVectorTexture

 | 

Motion vector image. The motion vector is computed by subtracting the X and Y values of the NDC coordinates of the previous frame from those of the current rendered pixel.

 |
| 

dynamicMaskTexture

 | 

Dynamic mask image of an object. The format must be GL\_RED or its compatible format. The valid value of the R channel is 0.0, 0.2, or 1.0, where 0.0 indicates static objects, 0.2 indicates moving objects such as people, and 1.0 indicates special effects or translucent objects.

 |
| 

jitterX

 | 

Camera jitter in the X direction.

 |
| 

jitterX

 | 

Camera jitter in the Y direction.

 |

#### \[h2\]PFN\_HMS\_XEG\_SPATIALUPSCALEPARAMETER

typedef void(GL\_APIENTRYP PFN\_HMS\_XEG\_SPATIALUPSCALEPARAMETER) (GLenum pname, GLvoid \*param)

**Description**

Defines the function pointer for setting the GPU spatial upscaling input parameter.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

pname

 | 

Enumerated name of the input parameter. The value can be [XEG\_SPATIAL\_UPSCALE\_SCISSOR](#xeg_spatial_upscale_scissor) or [XEG\_SPATIAL\_UPSCALE\_SHARPNESS](#xeg_spatial_upscale_sharpness).

 |
| 

param

 | 

Input parameter value. For details, see the description of the enumerated names of the input parameters.

 |

#### \[h2\]PFN\_HMS\_XEG\_TemporalUpscaleParameter

typedef void(GL\_APIENTRYP PFN\_HMS\_XEG\_TemporalUpscaleParameter) (GLenum pname, GLvoid \*param)

**Description**

Defines the function pointer for setting the input parameters for AI temporal upscaling.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

pname

 | 

Enumerated names of input parameters. The values can be [XEG\_TEMPORAL\_UPSCALE\_INPUT\_SIZE](#xeg_temporal_upscale_input_size), [XEG\_TEMPORAL\_UPSCALE\_JITTER\_NUM](#xeg_temporal_upscale_jitter_num), [XEG\_TEMPORAL\_UPSCALE\_DEPTH\_REVERSED](#xeg_temporal_upscale_depth_reversed), [XEG\_TEMPORAL\_UPSCALE\_RESET\_HISTORY](#xeg_temporal_upscale_reset_history), and [XEG\_TEMPORAL\_UPSCALE\_STEADY\_LEVEL](#xeg_temporal_upscale_steady_level).

 |
| 

param

 | 

Values of input parameters. For details about the values, see the description of the enumerated names of input parameters.

 |

#### \[h2\]XEG\_AdaptiveVRS

VK\_DEFINE\_HANDL(XEG\_AdaptiveVRS)

**Description**

[XEG\_AdaptiveVRS](#xeg_adaptivevrs) handle.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_AdaptiveVRSCreateInfo

typedef struct [XEG\_AdaptiveVRSCreateInfo](../../header-files-and-structs/structs/xeg-adaptivevrscreateinfo/document.md) XEG\_AdaptiveVRSCreateInfo

**Description**

This structure describes the parameter information for creating an [XEG\_AdaptiveVRS](#xeg_adaptivevrs) object. When the information in the structure changes, a new [XEG\_AdaptiveVRS](#xeg_adaptivevrs) object needs to be created.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_AdaptiveVRSDescription

typedef struct [XEG\_AdaptiveVRSDescription](../../header-files-and-structs/structs/xeg-adaptivevrsdescription/document.md) XEG\_AdaptiveVRSDescription

**Description**

This structure describes the parameter information required for delivering the command for drawing the shading rate texture. The information needs to be updated for each frame.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_DenoiseQualityMode

typedef enum [XEG\_DenoiseQualityMode](#xeg_denoisequalitymode) XEG\_DenoiseQualityMode

**Description**

Enumerates denoising quality modes.

**Since:** 6.0.0(20)

#### \[h2\]XEG\_ExtensionProperties

typedef struct [XEG\_ExtensionProperties](../../header-files-and-structs/structs/xeg-extensionproperties/document.md) XEG\_ExtensionProperties

**Description**

This structure describes the set of XEngine extensions queried through the [HMS\_XEG\_EnumerateDeviceExtensionProperties](#hms_xeg_enumeratedeviceextensionproperties) API.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_HPS

VK\_DEFINE\_HANDLE(XEG\_HPS)

**Description**

Handle to [XEG\_HPS](#xeg_hps).

**Since:** 6.0.0(20)

#### \[h2\]XEG\_HPSCreateInfo

typedef struct [XEG\_HPSCreateInfo](../../header-files-and-structs/structs/xeg-hpscreateinfo/document.md) XEG\_HPSCreateInfo

**Description**

This structure describes the information for creating an [XEG\_HPS](#xeg_hps) object.

**Since:** 6.0.0(20)

#### \[h2\]XEG\_HPSRadixSort

typedef struct [XEG\_HPSRadixSort](../../header-files-and-structs/structs/xeg-hpsradixsort/document.md) XEG\_HPSRadixSort

**Description**

This structure describes the HPS radix sort extension structure information.

**Since:** 6.0.0(20)

#### \[h2\]XEG\_HPSRadixSortDescription

typedef struct [XEG\_HPSRadixSortDescription](../../header-files-and-structs/structs/xeg-hpsradixsortdescription/document.md) XEG\_HPSRadixSortDescription

**Description**

This structure describes the information required for sorting using the [XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](#xeg_hps_radix_sort_extension_name) feature.

**Since:** 6.0.0(20)

#### \[h2\]XEG\_RTGI

VK\_DEFINE\_HANDLE(XEG\_RTGI)

**Description**

Handle to [XEG\_RTGI](#xeg_rtgi).

**Since:** 6.0.0(20)

#### \[h2\]XEG\_RTGIQualityMode

typedef enum [XEG\_RTGIQualityMode](#xeg_rtgiqualitymode) XEG\_RTGIQualityMode

**Description**

Enum for the quality modes of output images.

**Since:** 6.0.0(20)

#### \[h2\]XEG\_RTReflection

VK\_DEFINE\_HANDLE(XEG\_RTReflection)

**Description**

Handle to [XEG\_RTReflection](#xeg_rtreflection).

**Since:** 6.0.0(20)

#### \[h2\]XEG\_RTReflectionCreateInfo

typedef struct [XEG\_RTReflectionCreateInfo](../../header-files-and-structs/structs/xeg-rtreflectioncreateinfo/document.md) XEG\_RTReflectionCreateInfo

**Description**

This structure describes the information for creating an [XEG\_RTReflection](#xeg_rtreflection) object. When the information in the structure changes, a new [XEG\_RTReflection](#xeg_rtreflection) object needs to be created.

**Since:** 6.0.0(20)

#### \[h2\]XEG\_RTReflectionDescription

typedef struct [XEG\_RTReflectionDescription](../../header-files-and-structs/structs/xeg-rtreflectiondescription/document.md) XEG\_RTReflectionDescription

**Description**

This structure describes the input information for sending a ray intersection command.

**Since:** 6.0.0(20)

#### \[h2\]XEG\_RTVisibleMask

VK\_DEFINE\_HANDLE(XEG\_RTVisibleMask)

**Description**

Handle to [XEG\_RTVisibleMask](#xeg_rtvisiblemask), indicating the ray-traced VisibleMask feature instance. The shadow and ambient occlusion effects are supported.

**Since:** 6.0.0(20)

#### \[h2\]XEG\_SpatialUpscale

VK\_DEFINE\_HANDLE(XEG\_SpatialUpscale)

**Description**

Handle to [XEG\_SpatialUpscale](#xeg_spatialupscale).

**Since:** 5.0.0(12)

#### \[h2\]XEG\_SpatialUpscaleCreateInfo

typedef struct [XEG\_SpatialUpscaleCreateInfo](../../header-files-and-structs/structs/xeg-spatialupscalecreateinfo/document.md) XEG\_SpatialUpscaleCreateInfo

**Description**

This structure describes the information for creating an [XEG\_SpatialUpscale](#xeg_spatialupscale) object. When the information in the structure changes, a new XEG\_SpatialUpscale object needs to be created.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_SpatialUpscaleDescription

typedef struct [XEG\_SpatialUpscaleDescription](../../header-files-and-structs/structs/xeg-spatialupscaledescription/document.md) XEG\_SpatialUpscaleDescription

**Description**

This structure describes the image information required for delivering the GPU spatial upscaling rendering command.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_StructureType

typedef enum [XEG\_StructureType](#xeg_structuretype) XEG\_StructureType

**Description**

Enum for the XEngine structure types.

**Since:** 6.0.0(20)

#### \[h2\]XEG\_TemporalUpscale

VK\_DEFINE\_HANDLE(XEG\_TemporalUpscale)

**Description**

Handle to [XEG\_TemporalUpscale](#xeg_temporalupscale).

**Since:** 5.0.0(12)

#### \[h2\]XEG\_TemporalUpscaleCreateInfo

typedef struct [XEG\_TemporalUpscaleCreateInfo](../../header-files-and-structs/structs/xeg-temporalupscalecreateinfo/document.md) XEG\_TemporalUpscaleCreateInfo

**Description**

This structure describes the information for creating an [XEG\_TemporalUpscale](#xeg_temporalupscale) object. When the information in the structure changes, a new [XEG\_TemporalUpscale](#xeg_temporalupscale) object needs to be created.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_TemporalUpscaleDescription

typedef struct [XEG\_TemporalUpscaleDescription](../../header-files-and-structs/structs/xeg-temporalupscaledescription/document.md) XEG\_TemporalUpscaleDescription

**Description**

This structure describes the input information for delivering AI temporal upscaling rendering command.

**Since:** 5.0.0(12)

#### \[h2\]XEG\_TraversalMode

typedef enum [XEG\_TraversalMode](#xeg_traversalmode) XEG\_TraversalMode

**Description**

Enumerates traversal modes.

**Since:** 6.0.0(20)

#### Enumeration Type

#### \[h2\]XEG\_DenoiseQualityMode

enum XEG\_DenoiseQualityMode

**Description**

Enumerates denoising quality modes.

**Since:** 6.0.0(20)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

XEG\_DENOISE\_QUALITY\_MODE\_NONE

 | 

No denoising is performed.

 |
| 

XEG\_DENOISE\_QUALITY\_MODE\_QUALITY

 | 

Generates high-quality noise-free results. The speed may be slow.

 |
| 

XEG\_DENOISE\_QUALITY\_MODE\_BALANCED

 | 

Generates high-quality noise-free results at a moderate speed.

 |
| 

XEG\_DENOISE\_QUALITY\_MODE\_PERFORMANCES

 | 

Generates noise-free results with high performance.

 |

#### \[h2\]XEG\_RTGIQualityMode

enum XEG\_RTGIQualityMode

**Description**

Enum for the quality modes of output images.

**Since:** 6.0.0(20)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

XEG\_RTGI\_QUALITY\_MODE\_QUALITY

 | 

Quality mode.

 |
| 

XEG\_RTGI\_QUALITY\_MODE\_BALANCED

 | 

Balanced mode.

 |
| 

XEG\_RTGI\_QUALITY\_MODE\_PERFORMANCE

 | 

Performance mode.

 |

#### \[h2\]XEG\_StructureType

enum XEG\_StructureType

**Description**

Enum for the XEngine structure types.

**Since:** 6.0.0(20)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_CREATE\_INFO

 | 

Type of the structure [XEG\_RTShadowAOCreateInfo](../../header-files-and-structs/structs/xeg-rtshadowaocreateinfo/document.md).

 |
| 

XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_DESCRIPTION

 | 

Type of the structure [XEG\_RTShadowAODescription](../../header-files-and-structs/structs/xeg-rtshadowaodescription/document.md).

 |
| 

XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_CREATE\_INFO

 | 

Type of the structure [XEG\_RTReflectionCreateInfo](../../header-files-and-structs/structs/xeg-rtreflectioncreateinfo/document.md).

 |
| 

XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_DESCRIPTION

 | 

Type of the structure [XEG\_RTReflectionDescription](../../header-files-and-structs/structs/xeg-rtreflectiondescription/document.md).

 |
| 

XEG\_STRUCTURE\_TYPE\_NNGI\_CREATE\_INFO

 | 

Type of the structure [XEG\_NNGICreateInfo](../../header-files-and-structs/structs/xeg-nngicreateinfo/document.md).

 |
| 

XEG\_STRUCTURE\_TYPE\_NNGI\_DESCRIPTION

 | 

Type of the structure [XEG\_NNGIDescription](../../header-files-and-structs/structs/xeg-nngidescription/document.md).

 |
| 

XEG\_STRUCTURE\_TYPE\_DDGI\_CREATE\_INFO

 | 

Type of the structure [XEG\_DDGICreateInfo](../../header-files-and-structs/structs/xeg-ddgicreateinfo/document.md).

 |
| 

XEG\_STRUCTURE\_TYPE\_DDGI\_DESCRIPTION

 | 

Type of the structure [XEG\_DDGIDescription](../../header-files-and-structs/structs/xeg-ddgidescription/document.md).

 |
| 

XEG\_STRUCTURE\_TYPE\_HPS\_CREATE\_INFO

 | 

Type of the structure [XEG\_HPSCreateInfo](../../header-files-and-structs/structs/xeg-hpscreateinfo/document.md).

 |
| 

XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT

 | 

Type of the structure [XEG\_HPSRadixSort](../../header-files-and-structs/structs/xeg-hpsradixsort/document.md).

 |
| 

XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT\_DESCRIPTION

 | 

Type of the structure [XEG\_HPSRadixSortDescription](../../header-files-and-structs/structs/xeg-hpsradixsortdescription/document.md).

 |

#### \[h2\]XEG\_TraversalMode

enum XEG\_TraversalMode

**Description**

Enumerates traversal modes.

**Since:** 6.0.0(20)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

XEG\_TRAVERSAL\_MODE\_DEFAULT

 | 

Traverses ray tracing scenarios pixel by pixel.

 |
| 

XEG\_TRAVERSAL\_MODE\_PERFORMANCES

 | 

Traverses scenarios using algorithms, which provides better performance but may have slight differences in image quality.

 |

#### Function

#### \[h2\]HMS\_XEG\_AdaptiveVRSParameter()

GL\_APICALL void GL\_APIENTRY HMS\_XEG\_AdaptiveVRSParameter (GLenum pname, GLvoid \* param)

**Description**

Sets parameters of the adaptive VRS.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

pname

 | 

Enumerated name of the input parameter. The value can be [XEG\_ADAPTIVE\_VRS\_INPUT\_SIZE](#xeg_adaptive_vrs_input_size), [XEG\_ADAPTIVE\_VRS\_INPUT\_REGION](#xeg_adaptive_vrs_input_region), [XEG\_ADAPTIVE\_VRS\_TEXEL\_SIZE](#xeg_adaptive_vrs_texel_size), [XEG\_ADAPTIVE\_VRS\_ERROR\_SENSITIVITY](#xeg_adaptive_vrs_error_sensitivity), or [XEG\_ADAPTIVE\_VRS\_FLIP](#xeg_adaptive_vrs_flip).

 |
| 

param

 | 

Input parameter value. For details, see the description of the enumerated names of the input parameters.

 |

#### \[h2\]HMS\_XEG\_ApplyAdaptiveVRS()

GL\_APICALL void GL\_APIENTRY HMS\_XEG\_ApplyAdaptiveVRS (GLuint shadingRateImage)

**Description**

Applies the shading rate image to the render target.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

shadingRateImage

 | 

Shading rate image obtained after computation and 0 means disables adaptive VRS.

 |

#### \[h2\]HMS\_XEG\_CmdDispatchAdaptiveVRS()

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_CmdDispatchAdaptiveVRS (VkCommandBuffer commandBuffer, XEG\_AdaptiveVRS xegAdaptiveVRS, XEG\_AdaptiveVRSDescription \* pXegAdaptiveVRSDescription)

**Description**

Executes the command for computing the adaptive VRS.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

commandBuffer

 | 

VkCommandBuffer of the current command, which must be submitted to vkQueueSubmit before being executed.

 |
| 

xegAdaptiveVRS

 | 

The [XEG\_AdaptiveVRS](#xeg_adaptivevrs) object that has been created.

 |
| 

pXegAdaptiveVRSDescription

 | 

Pointer to the parameter structure [XEG\_AdaptiveVRSDescription](../../header-files-and-structs/structs/xeg-adaptivevrsdescription/document.md) of the delivering command. Its value cannot be null.

 |

#### \[h2\]HMS\_XEG\_CmdRadixSortHPS()

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CmdRadixSortHPS (VkCommandBuffer commandBuffer, XEG\_HPS hps, const XEG\_HPSRadixSortDescription \* pDescription)

**Description**

Records an HPS radix sort command. Before using this API, you need to call {[} to check whether the XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME} extension is supported.](#hms_xeg_enumeratedeviceextensionproperties)

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

commandBuffer

 | 

Vulkan command buffer object.

 |
| 

hps

 | 

Created [XEG\_HPS](#xeg_hps) object.

 |
| 

pDescription

 | 

Pointer to the input information structure [XEG\_HPSRadixSortDescription](../../header-files-and-structs/structs/xeg-hpsradixsortdescription/document.md) of the [XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](#xeg_hps_radix_sort_extension_name) feature. The value cannot be null.

 |

**Returns:**

Returns an error code of the VkResult type. VK\_SUCCESS indicates successful execution.

#### \[h2\]HMS\_XEG\_CmdRenderRTGI()

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CmdRenderRTGI (VkCommandBuffer commandBuffer, XEG\_RTGI rtGI, const void \* pDescription)

**Description**

Executes the rendering command.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

commandBuffer

 | 

VkCommandBuffer of the current command, which must be submitted to vkQueueSubmit before being executed.

 |
| 

rtGI

 | 

Created [XEG\_RTGI](#xeg_rtgi) object.

 |
| 

pDescription

 | 

Pointer to the structure containing the information needed for excuting the rendering command. If DDGI rendering is used, it is the pointer to the [XEG\_DDGIDescription](../../header-files-and-structs/structs/xeg-ddgidescription/document.md) structure. If NNGI rendering is used, it is the pointer to the [XEG\_NNGIDescription](../../header-files-and-structs/structs/xeg-nngidescription/document.md) structure. The value cannot be null.

 |

**Returns:**

Returns an error code of the VkResult type. VK\_SUCCESS indicates successful execution.

#### \[h2\]HMS\_XEG\_CmdRenderRTReflection()

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CmdRenderRTReflection (VkCommandBuffer commandBuffer, XEG\_RTReflection rtReflection, const void \* pDescription)

**Description**

Records the command for calculating the RT reflection hit information.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

commandBuffer

 | 

Vulkan command buffer object, which must be of the primary type.

 |
| 

rtReflection

 | 

Created **XegAdaptiveVRS** object.

 |
| 

pDescription

 | 

Pointer to the reflection rendering input information structure [XEG\_RTReflectionDescription](../../header-files-and-structs/structs/xeg-rtreflectiondescription/document.md). The value cannot be null.

 |

#### \[h2\]HMS\_XEG\_CmdRenderRTVisibleMask()

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CmdRenderRTVisibleMask (VkCommandBuffer commandBuffer, XEG\_RTVisibleMask rtVisibleMask, const void \* pDescription)

**Description**

Records the ray-traced VisibleMask rendering command.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

commandBuffer

 | 

Vulkan command buffer object.

 |
| 

rtVisibleMask

 | 

Created [XEG\_RTVisibleMask](#xeg_rtvisiblemask) object.

 |
| 

pDescription

 | 

Pointer to the input parameter structure for executing the rendering command. Only pointers of the [XEG\_RTShadowAODescription](../../header-files-and-structs/structs/xeg-rtshadowaodescription/document.md) type are supported. The value cannot be null.

 |

**Returns:**

Error code of the VkResult type. If the value is VK\_SUCCESS, the execution is successful.

#### \[h2\]HMS\_XEG\_CmdRenderSpatialUpscale()

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_CmdRenderSpatialUpscale (VkCommandBuffer commandBuffer, XEG\_SpatialUpscale xegSpatialUpscale, XEG\_SpatialUpscaleDescription \* pXegSpatialUpscaleDescription)

**Description**

Executes the GPU spatial upscaling rendering command.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

commandBuffer

 | 

VkCommandBuffer of the current command, which must be submitted to vkQueueSubmit before being executed.

 |
| 

xegSpatialUpscale

 | 

The [XEG\_SpatialUpscale](#xeg_spatialupscale) object that has been created.

 |
| 

pXegSpatialUpscaleDescription

 | 

Pointer to the parameter structure [XEG\_SpatialUpscaleDescription](../../header-files-and-structs/structs/xeg-spatialupscaledescription/document.md) of the rendering command. Its value cannot be null.

 |

#### \[h2\]HMS\_XEG\_CmdRenderTemporalUpscale()

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_CmdRenderTemporalUpscale (VkCommandBuffer commandBuffer, XEG\_TemporalUpscale temporalUpscale, XEG\_TemporalUpscaleDescription \* pDescription)

**Description**

Records the AI temporal upscaling rendering command.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

commandBuffer

 | 

Vulkan command buffer object, which must be of the primary type.

 |
| 

temporalUpscale

 | 

The [XEG\_TemporalUpscale](#xeg_temporalupscale) object that has been created.

 |
| 

pDescription

 | 

Pointer to the upscaling rendering input information structure [XEG\_TemporalUpscaleDescription](../../header-files-and-structs/structs/xeg-temporalupscaledescription/document.md). Its value cannot be null.

 |

#### \[h2\]HMS\_XEG\_CmdSetSynchronization()

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CmdSetSynchronization (VkCommandBuffer commandBuffer, const void \* xegHandle)

**Description**

Sets synchronization signals and waits for the rendering result to be written to a specified image. When the RTGI feature is used, it is the GI rendering result that needs to be waited for before being written to a specified image.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

commandBuffer

 | 

VkCommandBuffer of the current command, which must be submitted to vkQueueSubmit before being executed.

 |
| 

xegHandle

 | 

Created handle object. When the RTGI feature is used, the object is the created [XEG\_RTGI](#xeg_rtgi) object.

 |

**Returns:**

Returns an error code of the VkResult type. VK\_SUCCESS indicates successful execution.

#### \[h2\]HMS\_XEG\_CreateAdaptiveVRS()

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateAdaptiveVRS (VkDevice device, XEG\_AdaptiveVRSCreateInfo \* pXegAdaptiveVRSCreateInfo, XEG\_AdaptiveVRS \* pXegAdaptiveVRS)

**Description**

Creates an [XEG\_AdaptiveVRS](#xeg_adaptivevrs) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

device

 | 

Must be the VkDevice in use.

 |
| 

pXegAdaptiveVRSCreateInfo

 | 

Pointer to the structure [XEG\_AdaptiveVRSCreateInfo](../../header-files-and-structs/structs/xeg-adaptivevrscreateinfo/document.md). Its value cannot be null.

 |
| 

pXegAdaptiveVRS

 | 

Pointer to the handle. The created [XEG\_AdaptiveVRS](#xeg_adaptivevrs) is returned in this handle.

 |

**Returns:**

Returns an error code of the VkResult type. VK\_SUCCESS indicates successful execution.

#### \[h2\]HMS\_XEG\_CreateHPS()

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateHPS (VkDevice device, const XEG\_HPSCreateInfo \* pCreateInfo, XEG\_HPS \* pHps)

**Description**

Creates an [XEG\_HPS](#xeg_hps) object.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

device

 | 

VkDevice that is currently in use.

 |
| 

pCreateInfo

 | 

Pointer to the structure containing the information needed for creating an [XEG\_HPS](#xeg_hps) instance handle. The value cannot be null.

 |
| 

pHps

 | 

Pointer to the HPS instance handle. The created [XEG\_HPS](#xeg_hps) is returned in this handle.

 |

**Returns:**

Returns an error code of the VkResult type. VK\_SUCCESS indicates successful execution.

#### \[h2\]HMS\_XEG\_CreateRTGI()

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateRTGI (VkDevice device, const void \* pCreateInfo, XEG\_RTGI \* pRtGI)

**Description**

Creates an [XEG\_RTGI](#xeg_rtgi) object.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

device

 | 

VkDevice that is currently in use.

 |
| 

pCreateInfo

 | 

Pointer to the structure containing the information needed for creating an [XEG\_RTGI](#xeg_rtgi) object. If a DDGI handle is created, it is the pointer to the [XEG\_DDGICreateInfo](../../header-files-and-structs/structs/xeg-ddgicreateinfo/document.md) structure. If an NNGI handle is created, it is the pointer to the [XEG\_NNGICreateInfo](../../header-files-and-structs/structs/xeg-nngicreateinfo/document.md) structure. The value cannot be null.

 |
| 

pRtGI

 | 

Pointer to the handle. The created [XEG\_RTGI](#xeg_rtgi) is returned in this handle.

 |

**Returns:**

Returns an error code of the VkResult type. VK\_SUCCESS indicates successful execution.

#### \[h2\]HMS\_XEG\_CreateRTReflection()

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateRTReflection (VkDevice device, const void \* pCreateInfo, XEG\_RTReflection \* pRtReflection)

**Description**

Creates an [XEG\_RTReflection](#xeg_rtreflection) object.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

device

 | 

VkDevice that is currently in use.

 |
| 

pCreateInfo

 | 

Pointer to the structure containing the information needed for creating a reflection instance handle. Currently, only pointers of the [XEG\_RTReflectionCreateInfo](../../header-files-and-structs/structs/xeg-rtreflectioncreateinfo/document.md) type are supported. The value cannot be null.

 |
| 

pRtReflection

 | 

Pointer to the reflection instance handle. The created [XEG\_RTReflection](#xeg_rtreflection) is returned in this handle.

 |

**Returns:**

Returns an error code of the VkResult type. VK\_SUCCESS indicates successful execution.

#### \[h2\]HMS\_XEG\_CreateRTVisibleMask()

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateRTVisibleMask (VkDevice device, const void \* pCreateInfo, XEG\_RTVisibleMask \* pRTVisibleMask)

**Description**

Creates an [XEG\_RTVisibleMask](#xeg_rtvisiblemask) object.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

device

 | 

VkDevice that is currently in use.

 |
| 

pCreateInfo

 | 

Pointer to the structure of the description information required for creating a VisibleMask instance handle. Currently, only pointers of the [XEG\_RTShadowAOCreateInfo](../../header-files-and-structs/structs/xeg-rtshadowaocreateinfo/document.md) type are supported. The value cannot be null.

 |
| 

pRTVisibleMask

 | 

Pointer to the VisibleMask instance handle. The created [XEG\_RTVisibleMask](#xeg_rtvisiblemask) is returned in this handle.

 |

**Returns:**

Error code of the VkResult type. If the value is VK\_SUCCESS, the creation is successful.

#### \[h2\]HMS\_XEG\_CreateSpatialUpscale()

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateSpatialUpscale (VkDevice device, const XEG\_SpatialUpscaleCreateInfo \* pXegSpatialUpscaleCreateInfo, XEG\_SpatialUpscale \* pXegSpatialUpscale)

**Description**

Creates an [XEG\_SpatialUpscale](#xeg_spatialupscale) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

device

 | 

Must be the VkDevice in use.

 |
| 

pXegSpatialUpscaleCreateInfo

 | 

Pointer to the structure [XEG\_SpatialUpscaleCreateInfo](../../header-files-and-structs/structs/xeg-spatialupscalecreateinfo/document.md). Its value cannot be null.

 |
| 

pXegSpatialUpscale

 | 

Pointer to the handle. The created [XEG\_SpatialUpscale](#xeg_spatialupscale) is returned in this handle.

 |

**Returns:**

Returns an error code of the VkResult type. VK\_SUCCESS indicates successful execution.

#### \[h2\]HMS\_XEG\_CreateTemporalUpscale()

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateTemporalUpscale (VkDevice device, XEG\_TemporalUpscaleCreateInfo \* pTemporalUpscaleInfo, XEG\_TemporalUpscale \* pTemporalUpscale)

**Description**

Creates an [XEG\_TemporalUpscale](#xeg_temporalupscale) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

device

 | 

Must be the VkDevice in use.

 |
| 

pTemporalUpscaleInfo

 | 

Pointer to the upscaling creation information structure [XEG\_TemporalUpscaleCreateInfo](../../header-files-and-structs/structs/xeg-temporalupscalecreateinfo/document.md). Its value cannot be null.

 |
| 

pTemporalUpscale

 | 

Pointer to the handle. The created [XEG\_TemporalUpscale](#xeg_temporalupscale) is returned in this handle.

 |

**Returns:**

Returns an error code of the VkResult type. VK\_SUCCESS indicates successful execution.

#### \[h2\]HMS\_XEG\_DestroyAdaptiveVRS()

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroyAdaptiveVRS (XEG\_AdaptiveVRS xegAdaptiveVRS)

**Description**

Destroys an [XEG\_AdaptiveVRS](#xeg_adaptivevrs) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

xegAdaptiveVRS

 | 

The [XEG\_AdaptiveVRS](#xeg_adaptivevrs) object that has been created.

 |

#### \[h2\]HMS\_XEG\_DestroyHPS()

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroyHPS (XEG\_HPS hps)

**Description**

Destroys an [XEG\_HPS](#xeg_hps) object.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

hps

 | 

[XEG\_HPS](#xeg_hps) object to be destroyed.

 |

#### \[h2\]HMS\_XEG\_DestroyRTGI()

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroyRTGI (XEG\_RTGI rtGI)

**Description**

Destroys an [XEG\_RTGI](#xeg_rtgi) object.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

rtGI

 | 

Created [XEG\_RTGI](#xeg_rtgi) object.

 |

#### \[h2\]HMS\_XEG\_DestroyRTReflection()

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroyRTReflection (XEG\_RTReflection rtReflection)

**Description**

Destroys an [XEG\_RTReflection](#xeg_rtreflection) object.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

rtReflection

 | 

[XEG\_RTReflection](#xeg_rtreflection) object to be destroyed.

 |

#### \[h2\]HMS\_XEG\_DestroyRTVisibleMask()

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroyRTVisibleMask (XEG\_RTVisibleMask rtVisibleMask)

**Description**

Destroys an [XEG\_RTVisibleMask](#xeg_rtvisiblemask) object.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

rtVisibleMask

 | 

[XEG\_RTVisibleMask](#xeg_rtvisiblemask) object to be destroyed.

 |

#### \[h2\]HMS\_XEG\_DestroySpatialUpscale()

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroySpatialUpscale (XEG\_SpatialUpscale xegSpatialUpscale)

**Description**

Destroys an [XEG\_SpatialUpscale](#xeg_spatialupscale) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

xegSpatialUpscale

 | 

The [XEG\_SpatialUpscale](#xeg_spatialupscale) object that has been created.

 |

#### \[h2\]HMS\_XEG\_DestroyTemporalUpscale()

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroyTemporalUpscale (XEG\_TemporalUpscale temporalUpscale)

**Description**

Destroys an [XEG\_TemporalUpscale](#xeg_temporalupscale) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

temporalUpscale

 | 

The [XEG\_TemporalUpscale](#xeg_temporalupscale) object to destroy.

 |

#### \[h2\]HMS\_XEG\_DispatchAdaptiveVRS()

GL\_APICALL void GL\_APIENTRY HMS\_XEG\_DispatchAdaptiveVRS (GLfloat \* reprojectionMatrix, GLuint inputColorImage, GLuint inputDepthImage, GLuint shadingRateImage)

**Description**

Computes the shading rate image.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

reprojectionMatrix

 | 

Pointer to the result matrix of the computation between the current frame and the previous frame. The computation formula is as follows: (Projection matrix of the previous frame x Observation matrix of the previous frame) x (Inverse matrix of (Projection matrix of the current frame x Observation matrix of the current frame)). The matrix must be a 4 x 4 column major-order matrix. This parameter is optional, the image quality is better when it is not empty.

 |
| 

inputColorImage

 | 

Texture ID of the color attachment containing the final rendering result of the rendering pipeline of the previous frame.

 |
| 

inputDepthImage

 | 

Texture ID of the depth attachment containing the rendering result of the rendering pipeline of the current frame.

 |
| 

shadingRateImage

 | 

Texture ID used to generate the shading rate image information, which needs to be created and entered by the user.

 |

#### \[h2\]HMS\_XEG\_EnumerateDeviceExtensionProperties()

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_EnumerateDeviceExtensionProperties (VkPhysicalDevice physicalDevice, uint32\_t \* pPropertyCount, XEG\_ExtensionProperties \* pProperties)

**Description**

Vulkan API for querying extensions of XEngine.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

physicalDevice

 | 

Current Vulkan physical device.

 |
| 

pPropertyCount

 | 

Number of queried or passed extensions. If **pProperties** is nullptr, the number of currently supported XEngine extensions is returned. If the passed **propertyCount** is greater than or equal to the number of actually supported XEngine extensions, the query information is returned through the **pProperties** API and the return result is VK\_SUCCESS. If the passed **propertyCount** is less than the number of actually supported XEngine extensions, the query information is returned through the **pProperties** API and the return result is VK\_INCOMPLETE.

 |
| 

pProperties

 | 

Queried XEngine extensions, which are returned through the [XEG\_ExtensionProperties](../../header-files-and-structs/structs/xeg-extensionproperties/document.md) pointer of the structure.

 |

**Returns:**

Result code of the VkResult type. If the query is successful, VK\_SUCCESS is returned. If **pProperties** is not nullptr and the passed **propertyCount** is less than the number of actually supported XEngine extensions, VK\_INCOMPLETE is returned, indicating that the queried features are incomplete.

#### \[h2\]HMS\_XEG\_GetString()

const GLubyte\* HMS\_XEG\_GetString (GLenum name)

**Description**

OpenGL ES API for querying extensions of XEngine.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

name

 | 

Enumerated name of the input parameter. The value can be [XEG\_EXTENSIONS](#xeg_extensions).

 |

**Returns:**

If the parameter is [XEG\_EXTENSIONS](#xeg_extensions), a list of extensions supported by XEngine is returned. Multiple extensions are separated by spaces. Note that the extension name does not contain any space. If the query fails, null pointer is returned.

#### \[h2\]HMS\_XEG\_NeuralUpscaleParameter()

GL\_APICALL void GL\_APIENTRY HMS\_XEG\_NeuralUpscaleParameter (GLenum pname, GLvoid \* param)

**Description**

Sets the AI spatial upscaling input parameter.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

pname

 | 

Enumerated name of the input parameter. The value can be [XEG\_NEURAL\_UPSCALE\_SCISSOR](#xeg_neural_upscale_scissor), [XEG\_NEURAL\_UPSCALE\_SHARPNESS](#xeg_neural_upscale_sharpness), or [XEG\_NEURAL\_UPSCALE\_INPUT\_HANDLE](#xeg_neural_upscale_input_handle).

 |
| 

param

 | 

Input parameter value. For details, see the description of the enumerated names of the input parameters.

 |

#### \[h2\]HMS\_XEG\_RenderNeuralUpscale()

GL\_APICALL void GL\_APIENTRY HMS\_XEG\_RenderNeuralUpscale (GLuint inputTexture)

**Description**

Executes the AI spatial upscaling rendering command.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

inputTexture

 | 

The input texture. The texture type must be GL\_TEXTURE\_2D, and there is only 1 mipLevel. The valid value range of the input image width is \[448, 1728\], Otherwise, the AI inference result may be incorrect. The input texture must be created by OH\_NativeBuffer. Before calling this API, you need to set the handle corresponding to OH\_NativeBuffer as the upscaling input parameter. For details, see the [HMS\_XEG\_NeuralUpscaleParameter](#hms_xeg_neuralupscaleparameter) API.

 |

#### \[h2\]HMS\_XEG\_RenderSpatialUpscale()

GL\_APICALL void GL\_APIENTRY HMS\_XEG\_RenderSpatialUpscale (GLuint inputTexture)

**Description**

Executes the GPU spatial upscaling rendering command.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

inputTexture

 | 

Input texture. The texture type must be GL\_TEXTURE\_2D, and there is only 1 mipLevel. The texture must be created before this API is called. Otherwise, the rendering will fail, for example, a black screen occurs.

 |

#### \[h2\]HMS\_XEG\_RenderTemporalUpscale()

GL\_APICALL void GL\_APIENTRY HMS\_XEG\_RenderTemporalUpscale (GLuint inputTexture, GLuint depthTexture, GLuint motionVectorTexture, GLuint dynamicMaskTexture, GLfloat jitterX, GLfloat jitterY)

**Description**

Executes the rendering command for AI temporal upscaling.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

inputTexture

 | 

Upscaling input texture. The input texture is of the GL\_TEXTURE\_2D type, mipLevels is 1, and the maximum dimensions supported are 2048 x 1024.

 |
| 

depthTexture

 | 

Depth texture.

 |
| 

motionVectorTexture

 | 

Motion vector image. The motion vector is computed by subtracting the X and Y values of the NDC coordinates of the previous frame from those of the current rendered pixel.

 |
| 

dynamicMaskTexture

 | 

Dynamic mask image of an object. The format must be GL\_RED or its compatible format. The valid value of the R channel is 0.0, 0.2, or 1.0, where 0.0 indicates static objects, 0.2 indicates moving objects such as people, and 1.0 indicates special effects or translucent objects.

 |
| 

jitterX

 | 

Camera jitter in the X direction.

 |
| 

jitterX

 | 

Camera jitter in the Y direction.

 |

#### \[h2\]HMS\_XEG\_SpatialUpscaleParameter()

GL\_APICALL void GL\_APIENTRY HMS\_XEG\_SpatialUpscaleParameter (GLenum pname, GLvoid \* param)

**Description**

Sets the GPU spatial upscaling input parameter.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

pname

 | 

Enumerated name of the input parameter. The value can be [XEG\_SPATIAL\_UPSCALE\_SCISSOR](#xeg_spatial_upscale_scissor) or [XEG\_SPATIAL\_UPSCALE\_SHARPNESS](#xeg_spatial_upscale_sharpness).

 |
| 

param

 | 

Input parameter value. For details, see the description of the enumerated names of the input parameters.

 |

#### \[h2\]HMS\_XEG\_TemporalUpscaleParameter()

GL\_APICALL void GL\_APIENTRY HMS\_XEG\_TemporalUpscaleParameter (GLenum pname, const GLvoid \* param)

**Description**

Sets input parameters for AI temporal upscaling.

**Since:** 6.0.0(20)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

pname

 | 

Enumerated names of input parameters. The values can be [XEG\_TEMPORAL\_UPSCALE\_INPUT\_SIZE](#xeg_temporal_upscale_input_size), [XEG\_TEMPORAL\_UPSCALE\_JITTER\_NUM](#xeg_temporal_upscale_jitter_num), [XEG\_TEMPORAL\_UPSCALE\_DEPTH\_REVERSED](#xeg_temporal_upscale_depth_reversed), [XEG\_TEMPORAL\_UPSCALE\_RESET\_HISTORY](#xeg_temporal_upscale_reset_history), and [XEG\_TEMPORAL\_UPSCALE\_STEADY\_LEVEL](#xeg_temporal_upscale_steady_level).

 |
| 

param

 | 

Values of input parameters. For details about the values, see the description of the enumerated names of input parameters.

 |
