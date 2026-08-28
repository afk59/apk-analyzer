# XEG\_RTShadowAODenoiserParameters

#### Overview

Denoising parameter for the Ray-Traced Shadow and Ambient Occlusion algorithms.

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

float [temporalBlendFactor](#temporalblendfactor) = 0.075f

 | 

Weighting coefficient for mixing the current frame and historical frames during time-domain filtering. After the consistency check is passed, more information about the current frame is used if the weighting value is greater. The value of this parameter is clamped within the \[0.01, 1.0\] range. The default value is 0.075.

 |
| 

float [positionConstantDistance](#positionconstantdistance) = 1.0f

 | 

Threshold for consistency check based on the world space distance in time-domain filtering. The value must be greater than or equal to 0. If a negative value is passed, the value will be set to 0. The default value is 1.0.

 |
| 

uint32\_t [spatialDenoiseTimes](#spatialdenoisetimes) = 2

 | 

Number of times that the spatial filter is executed. A larger number reduces noise in the shadow and ambient occlusion results but may blur the output image. The value of this parameter is clamped within the \[0, 5\] range. The default value is 2.

 |
| 

float [ghostingAlpha](#ghostingalpha) = 0.0f

 | 

Ghosting issues introduced by controlling moving objects during time-domain filtering. If the value is set to 0, the ghosting issues caused by moving objects are not resolved. A larger value results in better ghosting issue resolution, but slightly weaker noise reduction effect. The value of this parameter is clamped within the \[0.0, 1.0\] range. The default value is 0.0.

 |
| 

float [spatialNormalWeight](#spatialnormalweight) = 1.0f

 | 

Normal weight used by the spatial domain filter. A larger value results in a higher normal weight and sharper image quality. The value of this parameter is clamped within the \[0.0, 1.0\] range. The default value is 1.0.

 |
| 

uint32\_t [spatialMaxKernelStep](#spatialmaxkernelstep) = 0

 | 

Sampling step of the space domain filter. A larger value results in a larger sampling range. The value of this parameter is clamped within the \[0, 4\] range. The default value is 0.

 |

#### Field

#### \[h2\]ghostingAlpha

float XEG\_RTShadowAODenoiserParameters::ghostingAlpha = 0.0f

**Description**

Ghosting issues introduced by controlling moving objects during time-domain filtering. If the value is set to 0, the ghosting issues caused by moving objects are not resolved. A larger value results in better ghosting issue resolution, but slightly weaker noise reduction effect. The value of this parameter is clamped within the \[0.0, 1.0\] range. The default value is 0.0.

#### \[h2\]positionConstantDistance

float XEG\_RTShadowAODenoiserParameters::positionConstantDistance = 1.0f

**Description**

Threshold for consistency check based on the world space distance in time-domain filtering. The value must be greater than or equal to 0. If a negative value is passed, the value will be set to 0. The default value is 1.0.

#### \[h2\]spatialDenoiseTimes

uint32\_t XEG\_RTShadowAODenoiserParameters::spatialDenoiseTimes = 2

**Description**

Number of times that the spatial filter is executed. A larger number reduces noise in the shadow and ambient occlusion results but may blur the output image. The value of this parameter is clamped within the \[0, 5\] range. The default value is 2.

#### \[h2\]spatialMaxKernelStep

uint32\_t XEG\_RTShadowAODenoiserParameters::spatialMaxKernelStep = 0

**Description**

Sampling step of the space domain filter. A larger value results in a larger sampling range. The value of this parameter is clamped within the \[0, 4\] range. The default value is 0.

#### \[h2\]spatialNormalWeight

float XEG\_RTShadowAODenoiserParameters::spatialNormalWeight = 1.0f

**Description**

Normal weight used by the spatial domain filter. A larger value results in a higher normal weight and sharper image quality. The value of this parameter is clamped within the \[0.0, 1.0\] range. The default value is 1.0.

#### \[h2\]temporalBlendFactor

float XEG\_RTShadowAODenoiserParameters::temporalBlendFactor = 0.075f

**Description**

Weighting coefficient for mixing the current frame and historical frames during time-domain filtering. After the consistency check is passed, more information about the current frame is used if the weighting value is greater. The value of this parameter is clamped within the \[0.01, 1.0\] range. The default value is 0.075.
