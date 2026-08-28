# XEG\_RTAOParameters

#### Overview

Ray-Traced Ambient Occlusion algorithm parameters.

**Since:** 6.0.0(20)

**Related Modules:**[XEngine](../../../modules/xengine/document.md)

**Header file**: [xeg\_vulkan\_rt\_visible\_mask.h](../../header-files/xeg-vulkan-rt-visible-mask-h/document.md)

#### Summary

#### \[h2\]Data Fields

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

float [rayTMax](#raytmax)

 | 

tMax value of the AO rays.

 |
| 

float [rayTMin](#raytmin)

 | 

tMin value of the AO rays.

 |
| 

float [aoIntensity](#aointensity) = 1.0f

 | 

AO strength. A larger value results in a stronger AO effect. The value of this parameter is clamped within the \[0.5, 1.0\] range. The default value is 1.0.

 |
| 

float [aoNormalBias](#aonormalbias) = 1.0f

 | 

Bias distance from the shading point along the normal direction. This parameter is used to solve the self-occlusion error caused by precision issues when the depth value is converted to the world coordinate. The default value is 1.0.

 |
| 

uint32\_t [aoCullMask](#aocullmask) = 0x5FF

 | 

Configures the rayFlags and cullMask parameters in the [rayQueryInitializeEXT](https://github.com/KhronosGroup/GLSL/blob/main/extensions/ext/GLSL_EXT_ray_query.txt) function. The upper 24 bits indicate rayFlags, and the lower 8 bits indicate cullMask. The default value is 0x5FF, that is, ((gl\_RayFlagsOpaqueEXT | gl\_RayFlagsTerminateOnFirstHitEXT) << 8) | 0xFF.

 |
| 

float [aoCullDistance](#aoculldistance)

 | 

World space distance for ambient occlusion removal. Ambient occlusion is not calculated when the pixel distance in the scene exceeds this distance. The value must be greater than 0.

 |
| 

uint32\_t [rayPerPixel](#rayperpixel) = 1

 | 

Number of samples per pixel. Currently, only 1 SPP is supported. The default value is 1.

 |

#### Field

#### \[h2\]aoCullDistance

float XEG\_RTAOParameters::aoCullDistance

**Description**

World space distance for ambient occlusion removal. Ambient occlusion is not calculated when the pixel distance in the scene exceeds this distance. The value must be greater than 0.

#### \[h2\]aoCullMask

uint32\_t XEG\_RTAOParameters::aoCullMask = 0x5FF

**Description**

Configures the rayFlags and cullMask parameters in the [rayQueryInitializeEXT](https://github.com/KhronosGroup/GLSL/blob/main/extensions/ext/GLSL_EXT_ray_query.txt) function. The upper 24 bits indicate rayFlags, and the lower 8 bits indicate cullMask. The default value is 0x5FF, that is, ((gl\_RayFlagsOpaqueEXT | gl\_RayFlagsTerminateOnFirstHitEXT) << 8) | 0xFF.

#### \[h2\]aoIntensity

float XEG\_RTAOParameters::aoIntensity = 1.0f

**Description**

AO strength. A larger value results in a stronger AO effect. The value of this parameter is clamped within the \[0.5, 1.0\] range. The default value is 1.0.

#### \[h2\]aoNormalBias

float XEG\_RTAOParameters::aoNormalBias = 1.0f

**Description**

Bias distance from the shading point along the normal direction. This parameter is used to solve the self-occlusion error caused by precision issues when the depth value is converted to the world coordinate. The value of this parameter is clamped within the \[0.0, 1.0\] range. The default value is 1.0.

#### \[h2\]rayPerPixel

uint32\_t XEG\_RTAOParameters::rayPerPixel = 1

**Description**

Number of samples per pixel. Currently, only 1 SPP is supported. The default value is 1.

#### \[h2\]rayTMax

float XEG\_RTAOParameters::rayTMax

**Description**

tMax value of the AO rays.

#### \[h2\]rayTMin

float XEG\_RTAOParameters::rayTMin

**Description**

tMin value of the AO rays.
