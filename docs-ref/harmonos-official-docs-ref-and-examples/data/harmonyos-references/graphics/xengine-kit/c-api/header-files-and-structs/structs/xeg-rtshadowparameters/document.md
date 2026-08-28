# XEG\_RTShadowParameters

#### Overview

Ray-Traced Shadow algorithm parameters.

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

tMax value of the Shadow rays.

 |
| 

float [rayTMin](#raytmin)

 | 

tMin value of the Shadow rays.

 |
| 

float [sunDirection](#sundirection) \[3\]

 | 

Direction of the directional light.

 |
| 

float [raySourceAngleInDegree](#raysourceangleindegree) = 0.0f

 | 

Angle range for shadow sampling along the light source direction. A larger value results in a larger half-shadow area. The value of this parameter is clamped within the \[0.0, 90.0\] range. The default value is 0.0.

 |
| 

uint32\_t [shadowCullMask](#shadowcullmask) = 0x5FF

 | 

Configures the rayFlags and cullMask parameters in the [rayQueryInitializeEXT](https://github.com/KhronosGroup/GLSL/blob/main/extensions/ext/GLSL_EXT_ray_query.txt) function. The upper 24 bits indicate rayFlags, and the lower 8 bits indicate cullMask. The default value is 0x5FF, that is, ((gl\_RayFlagsOpaqueEXT | gl\_RayFlagsTerminateOnFirstHitEXT) << 8) | 0xFF.

 |
| 

float [shadowCullDistance](#shadowculldistance)

 | 

World space distance for shadow removal. Shadows are not calculated when the pixel distance in the scene exceeds this distance. The value must be greater than 0.

 |
| 

uint32\_t [rayPerPixel](#rayperpixel) = 1

 | 

Number of samples per pixel. Currently, only 1 SPP is supported. The default value is 1.

 |

#### Field

#### \[h2\]rayPerPixel

uint32\_t XEG\_RTShadowParameters::rayPerPixel = 1

**Description**

Number of samples per pixel. Currently, only 1 SPP is supported. The default value is 1.

#### \[h2\]raySourceAngleInDegree

float XEG\_RTShadowParameters::raySourceAngleInDegree = 0.0f

**Description**

Angle range for shadow sampling along the light source direction. A larger value results in a larger half-shadow area. The value of this parameter is clamped within the \[0.0, 90.0\] range. The default value is 0.0.

#### \[h2\]rayTMax

float XEG\_RTShadowParameters::rayTMax

**Description**

tMax value of the Shadow rays.

#### \[h2\]rayTMin

float XEG\_RTShadowParameters::rayTMin

**Description**

tMin value of the Shadow rays.

#### \[h2\]shadowCullDistance

float XEG\_RTShadowParameters::shadowCullDistance

**Description**

World space distance for shadow removal. Shadows are not calculated when the pixel distance in the scene exceeds this distance. The value must be greater than 0.

#### \[h2\]shadowCullMask

uint32\_t XEG\_RTShadowParameters::shadowCullMask = 0x5FF

**Description**

Configures the rayFlags and cullMask parameters in the [rayQueryInitializeEXT](https://github.com/KhronosGroup/GLSL/blob/main/extensions/ext/GLSL_EXT_ray_query.txt) function. The upper 24 bits indicate rayFlags, and the lower 8 bits indicate cullMask. The default value is 0x5FF, that is, ((gl\_RayFlagsOpaqueEXT | gl\_RayFlagsTerminateOnFirstHitEXT) << 8) | 0xFF.

#### \[h2\]sunDirection

float XEG\_RTShadowParameters::sunDirection\[3\]

**Description**

Direction of the directional light.
