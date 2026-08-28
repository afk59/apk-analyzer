# XEG\_RTReflectionDescription

#### Overview

This structure describes the input information for sending a ray intersection command.

**Since:** 6.0.0(20)

**Related Modules:**[XEngine](../../../modules/xengine/document.md)

**Header file**: [xeg\_vulkan\_rt\_reflection.h](../../header-files/xeg-vulkan-rt-reflection-h/document.md)

#### Summary

#### \[h2\]Data Fields

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

XEG\_StructureType [sType](#stype)

 | 

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_DESCRIPTION.

 |
| 

const void \* [pNext](#pnext)

 | 

Pointer to the extended structure.

 |
| 

VkImageView [inputRayOriginImage](#inputrayoriginimage)

 | 

Ray origin image, which cannot be empty. The format must be the float type of at least three channels. The RGB channels store the x, y, and z coordinates of the origin respectively.

 |
| 

VkImageView [inputRayDirectionImage](#inputraydirectionimage)

 | 

Ray direction image, which cannot be empty. The format must be the float type of at least three channels. The RGB channels store the x, y, and z coordinates of the direction respectively. If the format is signed float, no special processing is required. If the format is unsigned float, the direction information needs to be quantized in the following manner: direction = (direction + 1.0) / 2.0.

 |
| 

VkImageView [outputReflectionInfoImage](#outputreflectioninfoimage)

 | 

Intersection result of the output reflected rays. The format must be R32G32B32A32\_UINT. The intersection result packs the latest hit information of ray tracing into 128 bits. For parsing method, refer to the description of [outputReflectionInfoImage](#outputreflectioninfoimage) in the structure member variable explanation.

 |
| 

VkAccelerationStructureKHR [accelerationStructure](#accelerationstructure)

 | 

Ray-traced acceleration structure of the scene.

 |
| 

float [rayMin](#raymin)

 | 

Minimum distance between the start point of a light ray and the nearest possible intersection point. The value must be non-negative and less than or equal to rayMax.

 |
| 

float [rayMax](#raymax)

 | 

Maximum distance between the start point of a light ray and the farthest possible intersection point. Any intersection beyond this range will be ignored.

 |
| 

uint32\_t [reflectionCullMask](#reflectioncullmask)

 | 

Configures the rayFlags and cullMask parameters in the [rayQueryInitializeEXT](https://github.com/KhronosGroup/GLSL/blob/main/extensions/ext/GLSL_EXT_ray_query.txt) function. The upper 24 bits indicate rayFlags, and the lower 8 bits indicate cullMask.

 |

#### Field

#### \[h2\]accelerationStructure

VkAccelerationStructureKHR XEG\_RTReflectionDescription::accelerationStructure

**Description**

Ray-traced acceleration structure of the scene.

#### \[h2\]inputRayDirectionImage

VkImageView XEG\_RTReflectionDescription::inputRayDirectionImage

**Description**

Ray direction image, which cannot be empty. The format must be the float type of at least three channels. The RGB channels store the x, y, and z coordinates of the direction respectively. If the format is signed float, no special processing is required. If the format is unsigned float, the direction information needs to be quantized in the following manner: direction = (direction + 1.0) / 2.0.

#### \[h2\]inputRayOriginImage

VkImageView XEG\_RTReflectionDescription::inputRayOriginImage

**Description**

Ray origin image, which cannot be empty. The format must be the float type of at least three channels. The RGB channels store the x, y, and z coordinates of the origin respectively.

#### \[h2\]outputReflectionInfoImage

VkImageView XEG\_RTReflectionDescription::outputReflectionInfoImage

**Description**

Intersection result of the output reflected rays. The format must be R32G32B32A32\_UINT. The intersection result packs the latest hit information of ray tracing into 128 bits. The parsing method is as follows:

uint raymiss = outputReflectionInfoImage.x & 1;
uint primitiveId = (outputReflectionInfoImage.x >> 1) & (0x3ffff);
uint instanceId = outputReflectionInfoImage.x >> 19;
vec2 barycentrics = unpackHalf2x16(outputReflectionInfoImage.z);
float hitT = uintBitsToFloat(outputReflectionInfoImage.w);
uint sbtOffest = (outputReflectionInfoImage.y >> 16);
uint geomtryIndex = (outputReflectionInfoImage.y) & 0xffff;

#### \[h2\]pNext

const void\* XEG\_RTReflectionDescription::pNext

**Description**

Pointer to the extended structure.

#### \[h2\]rayMax

float XEG\_RTReflectionDescription::rayMax

**Description**

Maximum distance between the start point of a light ray and the farthest possible intersection point. Any intersection beyond this range will be ignored.

#### \[h2\]rayMin

float XEG\_RTReflectionDescription::rayMin

**Description**

Minimum distance between the start point of a light ray and the nearest possible intersection point. The value must be non-negative and less than or equal to rayMax.

#### \[h2\]reflectionCullMask

uint32\_t XEG\_RTReflectionDescription::reflectionCullMask

**Description**

Configures the rayFlags and cullMask parameters in the [rayQueryInitializeEXT](https://github.com/KhronosGroup/GLSL/blob/main/extensions/ext/GLSL_EXT_ray_query.txt) function. The upper 24 bits indicate rayFlags, and the lower 8 bits indicate cullMask.

#### \[h2\]sType

XEG\_StructureType XEG\_RTReflectionDescription::sType

**Description**

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_DESCRIPTION.
