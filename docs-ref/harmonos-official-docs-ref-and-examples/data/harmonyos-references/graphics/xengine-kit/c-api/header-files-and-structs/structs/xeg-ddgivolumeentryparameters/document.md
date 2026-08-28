# XEG\_DDGIVolumeEntryParameters

#### Overview

This structure describes the mandatory parameters of each DDGI volume.

**Since:** 6.0.0(20)

**Related Modules:**[XEngine](../../../modules/xengine/document.md)

**Header file**: [xeg\_vulkan\_rtgi.h](../../header-files/xeg-vulkan-rtgi-h/document.md)

#### Summary

#### \[h2\]Data Fields

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

uint32\_t [volumeIndex](#volumeindex)

 | 

The volume index range is \[0, 65535\] and is unique.

 |
| 

uint32\_t [raysPerProbe](#raysperprobe)

 | 

Number of rays emitted by probes. The recommended value is 64. The value range is \[1, 1024\].

 |
| 

float [probeMaxRayDistance](#probemaxraydistance)

 | 

Maximum intersection distance of the rays emitted by probes. The recommended value is 1000.0.

 |
| 

float [volumePosition](#volumeposition) \[3\]

 | 

Coordinates of the volume center.

 |
| 

float [probeSpacing](#probespacing) \[3\]

 | 

Probe spacing. The value must be greater than 0.

 |
| 

uint32\_t [volumeLightingChannelMask](#volumelightingchannelmask)

 | 

Volume lighting channel mask. The recommended value is 0xFFFFFFFF.

 |
| 

uint32\_t [volumeProbeGridCounts](#volumeprobegridcounts) \[3\]

 | 

Number of probes. The value must be greater than 0. The value range is \[1, 32\].

 |
| 

float [volumeProbeIrradianceEncodingGamma](#volumeprobeirradianceencodinggamma)

 | 

Gamma correction coefficient of irradiance. The recommended value is 5.0. The value cannot be 0.

 |
| 

float [probeHysteresis](#probehysteresis)

 | 

Historical weight of probe irradiance. The recommended value is 0.95. The value range is \[0, 1\].

 |
| 

float [probeChangeThreshold](#probechangethreshold)

 | 

Probe change threshold. The recommended value is 1.0.

 |
| 

float [probeBrightnessThreshold](#probebrightnessthreshold)

 | 

Probe brightness threshold. The recommended value is 1.0.

 |
| 

float [volumeNormalBias](#volumenormalbias)

 | 

Probe normal bias. The recommended value is 0.12.

 |
| 

float [volumeViewBias](#volumeviewbias)

 | 

Probe view bias. The recommended value is 0.48.

 |
| 

float [volumeBlendDistance](#volumeblenddistance)

 | 

Volume lighting blending distance. The recommended value is 1.0.

 |
| 

float [volumeBlendDistanceBlack](#volumeblenddistanceblack)

 | 

Fade-in range of the lighting at the volume edges. The recommended value is 1.0.

 |
| 

float [probeBackfaceThreshold](#probebackfacethreshold)

 | 

Backward judgment threshold of probes. The recommended value is 0.0.

 |
| 

float [probeMinFrontfaceDistance](#probeminfrontfacedistance)

 | 

Minimum forward distance of probes. The recommended value is 0.0.

 |
| 

float [volumeIrradianceScalar](#volumeirradiancescalar)

 | 

Volume irradiance scaling ratio. The recommended value is 1.0. The value must be non-negative.

 |
| 

float [emissiveMultiplier](#emissivemultiplier)

 | 

Emissive intensity multiplier. The recommended value is 1.0. The value must be non-negative.

 |
| 

float [lightingMultiplier](#lightingmultiplier)

 | 

Lighting multiplier. The recommended value is 1.0. The value must be non-negative.

 |
| 

bool [bForceUpdate](#bforceupdate)

 | 

Whether to forcibly update all probes. The value true indicates that all probes are forcibly updated, and the value false indicates that some probes are updated. The recommended value is false.

 |
| 

VkImageView [probeIrradianceSH](#probeirradiancesh)

 | 

3D image that stores the second-order spherical harmonic coefficients of probe irradiance. The width, height, and depth are volumeProbeGridCounts.y x 4 (number of second-order spherical harmonic coefficients), volumeProbeGridCounts.x, and volumeProbeGridCounts.z, respectively. The VkFormat value is VK\_FORMAT\_R32G32B32A32\_SFLOAT.

 |

#### Field

#### \[h2\]bForceUpdate

bool XEG\_DDGIVolumeEntryParameters::bForceUpdate

**Description**

Whether to forcibly update all probes. The value true indicates that all probes are forcibly updated, and the value false indicates that some probes are updated. The recommended value is false.

#### \[h2\]emissiveMultiplier

float XEG\_DDGIVolumeEntryParameters::emissiveMultiplier

**Description**

Emissive intensity multiplier. The recommended value is 1.0. The value must be non-negative.

#### \[h2\]lightingMultiplier

float XEG\_DDGIVolumeEntryParameters::lightingMultiplier

**Description**

Lighting multiplier. The recommended value is 1.0. The value must be non-negative.

#### \[h2\]probeBackfaceThreshold

float XEG\_DDGIVolumeEntryParameters::probeBackfaceThreshold

**Description**

Backward judgment threshold of probes. The recommended value is 0.0.

#### \[h2\]probeBrightnessThreshold

float XEG\_DDGIVolumeEntryParameters::probeBrightnessThreshold

**Description**

Probe brightness threshold. The recommended value is 1.0.

#### \[h2\]probeChangeThreshold

float XEG\_DDGIVolumeEntryParameters::probeChangeThreshold

**Description**

Probe change threshold. The recommended value is 1.0.

#### \[h2\]probeHysteresis

float XEG\_DDGIVolumeEntryParameters::probeHysteresis

**Description**

Historical weight of probe irradiance. The recommended value is 0.95. The value range is \[0, 1\].

#### \[h2\]probeIrradianceSH

VkImageView XEG\_DDGIVolumeEntryParameters::probeIrradianceSH

**Description**

3D image that stores the second-order spherical harmonic coefficients of probe irradiance. The width, height, and depth are volumeProbeGridCounts.y x 4 (number of second-order spherical harmonic coefficients), volumeProbeGridCounts.x, and volumeProbeGridCounts.z, respectively. The VkFormat value is VK\_FORMAT\_R32G32B32A32\_SFLOAT.

#### \[h2\]probeMaxRayDistance

float XEG\_DDGIVolumeEntryParameters::probeMaxRayDistance

**Description**

Maximum intersection distance of the rays emitted by probes. The recommended value is 1000.0.

#### \[h2\]probeMinFrontfaceDistance

float XEG\_DDGIVolumeEntryParameters::probeMinFrontfaceDistance

**Description**

Minimum forward distance of probes. The recommended value is 0.0.

#### \[h2\]probeSpacing

float XEG\_DDGIVolumeEntryParameters::probeSpacing\[3\]

**Description**

Probe spacing. The value must be greater than 0.

#### \[h2\]raysPerProbe

uint32\_t XEG\_DDGIVolumeEntryParameters::raysPerProbe

**Description**

Number of rays emitted by probes. The recommended value is 64. The value range is \[1, 1024\].

#### \[h2\]volumeBlendDistance

float XEG\_DDGIVolumeEntryParameters::volumeBlendDistance

**Description**

Volume lighting blending distance. The recommended value is 1.0.

#### \[h2\]volumeBlendDistanceBlack

float XEG\_DDGIVolumeEntryParameters::volumeBlendDistanceBlack

**Description**

Fade-in range of the lighting at the volume edges. The recommended value is 1.0.

#### \[h2\]volumeIndex

uint32\_t XEG\_DDGIVolumeEntryParameters::volumeIndex

**Description**

The volume index range is \[0, 65535\] and is unique.

#### \[h2\]volumeIrradianceScalar

float XEG\_DDGIVolumeEntryParameters::volumeIrradianceScalar

**Description**

Volume irradiance scaling ratio. The recommended value is 1.0. The value must be non-negative.

#### \[h2\]volumeLightingChannelMask

uint32\_t XEG\_DDGIVolumeEntryParameters::volumeLightingChannelMask

**Description**

Volume lighting channel mask. The recommended value is 0xFFFFFFFF.

#### \[h2\]volumeNormalBias

float XEG\_DDGIVolumeEntryParameters::volumeNormalBias

**Description**

Probe normal bias. The recommended value is 0.12.

#### \[h2\]volumePosition

float XEG\_DDGIVolumeEntryParameters::volumePosition\[3\]

**Description**

Coordinates of the volume center.

#### \[h2\]volumeProbeGridCounts

uint32\_t XEG\_DDGIVolumeEntryParameters::volumeProbeGridCounts\[3\]

**Description**

Number of probes. The value must be greater than 0. The value range is \[1, 32\].

#### \[h2\]volumeProbeIrradianceEncodingGamma

float XEG\_DDGIVolumeEntryParameters::volumeProbeIrradianceEncodingGamma

**Description**

Gamma correction coefficient of irradiance. The recommended value is 5.0. The value cannot be 0.

#### \[h2\]volumeViewBias

float XEG\_DDGIVolumeEntryParameters::volumeViewBias

**Description**

Probe view bias. The recommended value is 0.48.
