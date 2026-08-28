# XEG\_RTShadowAOCreateInfo

#### Overview

This structure describes the initialization information for creating an [XEG\_RTVisibleMask](../../../modules/xengine/document.md#xeg_rtvisiblemask) instance that supports the Ray-Traced Shadow and Ambient Occlusion effects. When the information in the structure changes, a new [XEG\_RTVisibleMask](../../../modules/xengine/document.md#xeg_rtvisiblemask) object needs to be created.

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

XEG\_StructureType [sType](#stype)

 | 

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_CREATE\_INFO.

 |
| 

const void \* [pNext](#pnext)

 | 

Pointer to the extended structure.

 |
| 

VkExtent2D [rtInputGbufferSize](#rtinputgbuffersize)

 | 

Dimensions of the input GBuffer depth and normal images. The dimensions of the depth and normal images must be the same.

 |
| 

VkExtent2D [rtShadowAOSize](#rtshadowaosize)

 | 

Dimensions of the output shadow and ambient occlusion images, which must be in the same proportion as rtInputGbufferSize.

 |
| 

bool [enableRTShadow](#enablertshadow)

 | 

Whether to enable the Ray-Traced Shadow effect (true) or not (false). At least one of the shadow and ambient occlusion effects must be enabled.

 |
| 

bool [enableRTAO](#enablertao)

 | 

Whether to enable the Ray-Traced Ambient Occlusion effect (true) or not (false). At least one of the shadow and ambient occlusion effects must be enabled.

 |
| 

XEG\_TraversalMode [traversalMode](#traversalmode)

 | 

Traversal mode. Ray-Traced Shadow and Ambient Occlusion use the same traversal mode.

 |
| 

XEG\_DenoiseQualityMode [denoiseMode](#denoisemode)

 | 

Denoising quality mode. Ray-Traced Shadow and Ambient Occlusion use the same quality mode.

 |
| 

bool [aoOnlyInShadow](#aoonlyinshadow)

 | 

This parameter takes effect only when the Ray-Traced Shadow effect is enabled. If this parameter is set to true, only the ambient occlusion value of pixels in the shadow area is calculated. If this parameter is set to false, the ambient occlusion value of all pixels is calculated.

 |
| 

bool [reverseZ](#reversez)

 | 

Whether depth flipping is enabled. If depth flipping is enabled, the depth at the far plane is 0. Depth flipping can help obtain a higher-precision depth value. It is recommended that it be enabled. The value true indicates that it is enabled, and the value false indicates that it is disabled.

 |

#### Field

#### \[h2\]aoOnlyInShadow

bool XEG\_RTShadowAOCreateInfo::aoOnlyInShadow

**Description**

This parameter takes effect only when the Ray-Traced Shadow effect is enabled. If this parameter is set to true, only the ambient occlusion value of pixels in the shadow area is calculated. If this parameter is set to false, the ambient occlusion value of all pixels is calculated.

#### \[h2\]denoiseMode

XEG\_DenoiseQualityMode XEG\_RTShadowAOCreateInfo::denoiseMode

**Description**

Denoising quality mode. Ray-Traced Shadow and Ambient Occlusion use the same quality mode.

#### \[h2\]enableRTAO

bool XEG\_RTShadowAOCreateInfo::enableRTAO

**Description**

Whether to enable the Ray-Traced Ambient Occlusion effect (true) or not (false). At least one of the shadow and ambient occlusion effects must be enabled.

#### \[h2\]enableRTShadow

bool XEG\_RTShadowAOCreateInfo::enableRTShadow

**Description**

Whether to enable the Ray-Traced Shadow effect (true) or not (false). At least one of the shadow and ambient occlusion effects must be enabled.

#### \[h2\]pNext

const void\* XEG\_RTShadowAOCreateInfo::pNext

**Description**

Pointer to the extended structure.

#### \[h2\]reverseZ

bool XEG\_RTShadowAOCreateInfo::reverseZ

**Description**

Whether depth flipping is enabled. If depth flipping is enabled, the depth at the far plane is 0. Depth flipping can help obtain a higher-precision depth value. It is recommended that it be enabled. The value true indicates that it is enabled, and the value false indicates that it is disabled.

#### \[h2\]rtInputGbufferSize

VkExtent2D XEG\_RTShadowAOCreateInfo::rtInputGbufferSize

**Description**

Dimensions of the input GBuffer depth and normal images. The dimensions of the depth and normal images must be the same.

#### \[h2\]rtShadowAOSize

VkExtent2D XEG\_RTShadowAOCreateInfo::rtShadowAOSize

**Description**

Dimensions of the output shadow and ambient occlusion images, which must be in the same proportion as rtInputGbufferSize.

#### \[h2\]sType

XEG\_StructureType XEG\_RTShadowAOCreateInfo::sType

**Description**

Identifies the [XEG\_StructureType](../../../modules/xengine/document.md#xeg_structuretype) value of this structure, which must be XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_CREATE\_INFO.

#### \[h2\]traversalMode

XEG\_TraversalMode XEG\_RTShadowAOCreateInfo::traversalMode

**Description**

Traversal mode. Ray-Traced Shadow and Ambient Occlusion use the same traversal mode.
