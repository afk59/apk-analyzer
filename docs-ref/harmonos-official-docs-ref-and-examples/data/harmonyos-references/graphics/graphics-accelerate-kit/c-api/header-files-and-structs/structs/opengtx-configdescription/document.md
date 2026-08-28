# OpenGTX\_ConfigDescription

#### Overview

Describes the OpenGTX attribute settings.

**Start version**: 5.0.0(12)

**Related module**: [GraphicsAccelerate](../../../modules/graphicsaccelerate/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[OpenGTX\_LTPO\_Mode](../../../modules/graphicsaccelerate/document.md#gad531d05ca502b93f4153e4b1f749ed0c) [mode](#ac2431cda0fb7b43a7e4adbaefcbce01d)

 | 

LTPO mode, including the scene mode, touch mode, and adaptive mode.

 |
| 

int32\_t [targetFPS](#a97b1fac259c0724de14f964712c85cae)

 | 

Target frame rate of a game app. The value range is \[30, 144\].

 |
| 

char\* [packageName](#a44b999153a4f1e122d87503b323bfa3d)

 | 

Game package name. The value is a string of 1 to 256 characters.

 |
| 

char\* [appVersion](#a88573b5b4d5bf3d031adf01c4b70f09e)

 | 

Game app version. The value is a string of 1 to 256 characters.

 |
| 

[OpenGTX\_EngineType](../../../modules/graphicsaccelerate/document.md#gadd5a5e0b3b4aa3ea8b0974cba13c0389) [engineType](#a61392b5ab91e08d90223b3c0d14b5f50)

 | 

Game engine type.

 |
| 

char\* [engineVersion](#a523c7df207cd9e0ff65ce91792686b46)

 | 

Game engine version. The value is a string of 0 to 256 characters.

 |
| 

[OpenGTX\_GameType](../../../modules/graphicsaccelerate/document.md#ga34d898acfaacb3750db454a9ed2038a5) [gameType](#ae966ba7827b4c860c32696e2aff929df)

 | 

Game type.

 |
| 

[OpenGTX\_PictureQualityMaxLevel](../../../modules/graphicsaccelerate/document.md#gacd5c090213b3593e7c9ab6c93118ff8e) [pictureQualityMaxLevel](#a715706d392c4953b9593e7ff6b663602)

 | 

Image quality.

 |
| 

[OpenGTX\_ResolutionValue](../opengtx-resolutionvalue/document.md) [resolutionMaxValue](#a461418a95fa10f0b28db6e4222bea507)

 | 

Maximum resolution supported by a game app. The value ranges from 360p to 8K.

 |
| 

int32\_t [gameMainThreadId](#a2dfd147c0ebf5f2aed883f9bcdde3027)

 | 

ID of a logic thread of a game app. The value range is \[0, ∞).

 |
| 

int32\_t [gameRenderThreadId](#a77910cdc99dddd0e701e655026df85e9)

 | 

ID of a rendering thread of a game app. The value range is \[0, ∞).

 |
| 

int32\_t [gameKeyThreadIds](#af341958c7e20141209ddc2b89badc368) \[5\]

 | 

List of key thread IDs of a game app. The ID value range is \[0, ∞).

 |
| 

bool [vulkanSupport](#a59a8786658db75e046a1502f0ebaadaa)

 | 

Indicates whether Vulkan is supported.

The value is **true** or **false**.

 |

#### Member Variable Description

#### \[h2\]appVersion

char\* OpenGTX\_ConfigDescription::appVersion

**Description**

Game app version. The value is a string of 1 to 256 characters.

#### \[h2\]engineType

[OpenGTX\_EngineType](../../../modules/graphicsaccelerate/document.md#gadd5a5e0b3b4aa3ea8b0974cba13c0389) OpenGTX\_ConfigDescription::engineType

**Description**

Game engine type.

#### \[h2\]engineVersion

char\* OpenGTX\_ConfigDescription::engineVersion

**Description**

Game engine version. The value is a string of 0 to 256 characters.

#### \[h2\]gameKeyThreadIds\[5\]

int32\_t OpenGTX\_ConfigDescription::gameKeyThreadIds\[5\]

**Description**

List of key thread IDs of a game app. The ID value range is \[0, ∞).

#### \[h2\]gameMainThreadId

int32\_t OpenGTX\_ConfigDescription::gameMainThreadId

**Description**

ID of a logic thread of a game app. The value range is \[0, ∞).

#### \[h2\]gameRenderThreadId

int32\_t OpenGTX\_ConfigDescription::gameRenderThreadId

**Description**

ID of a rendering thread of a game app. The value range is \[0, ∞).

#### \[h2\]gameType

[OpenGTX\_GameType](../../../modules/graphicsaccelerate/document.md#ga34d898acfaacb3750db454a9ed2038a5) OpenGTX\_ConfigDescription::gameType

**Description**

Game type.

#### \[h2\]mode

[OpenGTX\_LTPO\_Mode](../../../modules/graphicsaccelerate/document.md#gad531d05ca502b93f4153e4b1f749ed0c) OpenGTX\_ConfigDescription::mode

**Description**

LTPO mode, including the scene mode, touch mode, and adaptive mode.

#### \[h2\]packageName

char\* OpenGTX\_ConfigDescription::packageName

**Description**

Game package name. The value is a string of 1 to 256 characters.

#### \[h2\]pictureQualityMaxLevel

[OpenGTX\_PictureQualityMaxLevel](../../../modules/graphicsaccelerate/document.md#gacd5c090213b3593e7c9ab6c93118ff8e) OpenGTX\_ConfigDescription::pictureQualityMaxLevel

**Description**

Image quality.

#### \[h2\]resolutionMaxValue

[OpenGTX\_ResolutionValue](../opengtx-resolutionvalue/document.md) OpenGTX\_ConfigDescription::resolutionMaxValue

**Description**

Maximum resolution supported by a game app. The value ranges from 360p to 8K.

#### \[h2\]targetFPS

int32\_t OpenGTX\_ConfigDescription::targetFPS

**Description**

Target frame rate of a game app. The value range is \[30, 144\].

#### \[h2\]vulkanSupport

bool OpenGTX\_ConfigDescription::vulkanSupport

**Description**

Indicates whether Vulkan is supported.
