# gamePerformance (Game Scene Perception)

This module provides the game scene perception capability of Game Service Kit.

**Start version**: 5.0.0(12)

#### Module Import

import { gamePerformance } from '@kit.GameServiceKit';

#### DeviceInfo

Device information class.

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

tempLevel

 | 

number

 | 

No

 | 

No

 | 

Temperature control level. A higher level indicates a higher temperature. The suggestions for different levels are as follows:

-   **1**: No action is required.
-   **2**: You are advised to lower the specifications of imperceptible services, for example, reducing the background update rate or delaying the running of game tasks.
-   **3**: You are advised to suspend imperceptible services to lower the specifications of non-core game services, for example, reducing the rate of foreground update.
-   **4**. You are advised to lower the game effects, resolution, and image quality.
-   **5**. You are advised to lower the specifications in all scenarios to further lower the resolution and image quality.
-   **6**: You are advised to lower the game specifications to a minimum.

 |
| 

gpuInfo

 | 

[GpuInfo](#section12288563197)

 | 

No

 | 

Yes

 | 

GPU performance information.

 |
| 

thermalInfo

 | 

[ThermalInfo](#section55661711201613)

 | 

No

 | 

Yes

 | 

Temperature change trend data.

**Start version**: 5.0.1(13)

 |

#### GpuInfo

GPU performance information class.

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

gpuLoadLevel

 | 

number

 | 

No

 | 

Yes

 | 

Overall GPU load level. There are 10 levels from 1 to 10. The greater the value, the higher the load level.

 |
| 

vertexLoadLevel

 | 

number

 | 

No

 | 

Yes

 | 

Vertex processing load level. There are 10 levels from 1 to 10. The greater the value, the higher the load level.

 |
| 

fragmentLoadLevel

 | 

number

 | 

No

 | 

Yes

 | 

Fragment processing load level. There are 10 levels from 1 to 10. The greater the value, the higher the load level.

 |
| 

textureLoadLevel

 | 

number

 | 

No

 | 

Yes

 | 

Texture processing load level. There are 10 levels from 1 to 10. The greater the value, the higher the load level.

 |
| 

bandwidthLoadLevel

 | 

number

 | 

No

 | 

Yes

 | 

Bandwidth load level. There are 10 levels from 1 to 10. The greater the value, the higher the load level.

 |
| 

currentFrequency

 | 

number

 | 

No

 | 

Yes

 | 

Current frequency of the GPU, in kHz.

**Start version**: 5.0.2(14)

 |

#### ThermalInfo

Temperature change trend data class.

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.0.1(13)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

thermalMargin

 | 

number

 | 

No

 | 

Yes

 | 

Time margin, that is, the time required to reach a specified temperature control level, in seconds.

NOTE:

-   If the value exceeds 60, the reliability decreases.
-   **0**: The queried temperature control level is reached.
-   **\-1**: unreachable.
-   **\-2**: The queried level is lower than the current level.

 |
| 

thermalTrend

 | 

number

 | 

No

 | 

Yes

 | 

Temperature trend. The value range is \[-100,100\]. A negative value indicates a decrease in temperature, and a larger absolute value indicates a faster rate of temperature change.

 |

#### BaseGameInfo

Basic game information class.

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

messageType

 | 

number

 | 

No

 | 

No

 | 

Information type.

-   **0**: game package body message, corresponding to [GamePackageInfo](#section3844175954711).
-   **1**: game setting message, corresponding to [GameConfigInfo](#section10841101134814).
-   **2**: game scene message, corresponding to [GameSceneInfo](#section1535311105717).
-   **3**: game network status message, corresponding to [GameNetInfo](#section138783245711).
-   **4**: game player information, corresponding to [GamePlayerInfo](#section2401441273).

 |
| 

extra

 | 

string

 | 

No

 | 

Yes

 | 

Extended parameter, which is a JSON character string and is used to transfer extended game information. The value length range is \[0, 128\].

 |

#### GamePackageInfo

Game package information class, which extends [BaseGameInfo](#section116223815415).

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

bundleName

 | 

string

 | 

No

 | 

No

 | 

Game package name. The value length range is \[1, 128\].

 |
| 

appVersion

 | 

string

 | 

No

 | 

No

 | 

Game version number. The value length range is \[1, 64\].

 |
| 

engineType

 | 

number

 | 

No

 | 

Yes

 | 

Game engine type.

-   **1**: Unity
-   **2**: Unreal4
-   **3**: Messiah
-   **4**: Cocos
-   **200**: others

 |
| 

engineVersion

 | 

string

 | 

No

 | 

Yes

 | 

Game engine version number The value length range is \[0, 64\].

 |
| 

gameType

 | 

number

 | 

No

 | 

Yes

 | 

Game type.

-   **1**: multiplayer online battle arena (MOBA)
-   **2**: role-playing game (RPG)
-   **3**: first-person shooter (FPS)
-   **4**: fight technology game (FTG)
-   **5**: racing game (RAC)
-   **200**: others

 |
| 

vulkanSupported

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether Vulkan is supported.

-   **true**: yes
-   **false**: no

The default value is **false**.

 |

#### GameConfigInfo

Game configuration information class, which extends [BaseGameInfo](#section116223815415).

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

maxPictureQualityLevel

 | 

number

 | 

No

 | 

No

 | 

Supported highest image quality level.

-   **1**: smooth
-   **2**: balancing
-   **3**: HD
-   **4**: HDR
-   **5**: UHD

 |
| 

currentPictureQualityLevel

 | 

number

 | 

No

 | 

No

 | 

Current level of the image quality.

-   **1**: smooth
-   **2**: balancing
-   **3**: HD
-   **4**: HDR
-   **5**: UHD

 |
| 

maxFrameRate

 | 

number

 | 

No

 | 

No

 | 

Supported maximum frame rate.

 |
| 

currentFrameRate

 | 

number

 | 

No

 | 

No

 | 

Current frame rate. The value range is \[1, 144\].

 |
| 

maxResolution

 | 

string

 | 

No

 | 

No

 | 

Maximum supported resolution. The value is in _AxB_ format, for example, 1260x1980. The value length range is \[1, 32\].

 |
| 

currentResolution

 | 

string

 | 

No

 | 

No

 | 

Current resolution. The value is in _AxB_ format, for example, 1260x1980. The value length range is \[1, 32\].

 |
| 

antiAliasing

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether to enable antialiasing.

-   **true**: yes
-   **false**: no

The default value is **false**.

 |
| 

shadow

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether to enable the shadow function.

-   **true**: yes
-   **false**: no

The default value is **false**.

 |
| 

multithreading

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether to enable multi-threading.

-   **true**: yes
-   **false**: no

The default value is **false**.

 |
| 

particle

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether to enable the particle effect.

-   **true**: yes
-   **false**: no

The default value is **false**.

 |
| 

hdMode

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether to enable the HD mode.

-   **true**: yes
-   **false**: no

The default value is **false**.

 |

#### GameSceneInfo

Game scene information class, which extends [BaseGameInfo](#section116223815415).

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

sceneID

 | 

number

 | 

No

 | 

No

 | 

Game scene ID.

-   **0**: After the current scene ends, the switchback scene can be sent to indicate an end.
-   **1**: game startup
-   **2**: in-game update
-   **3**: sign-in process
-   **4**: home screen
-   **5**: game loading (performed by the player)
-   **6**: game loading (loading by the player finished; waiting for loading by others)
-   **7**: gaming
-   **8**: onlooker mode

(Special game scenes are custom-coded from 100 onward.)

NOTE:

You are advised to use **subSceneID** to specify custom game scenes.

 |
| 

description

 | 

string

 | 

No

 | 

Yes

 | 

Custom game scene description. The value length range is \[0, 128\].

 |
| 

subSceneID

 | 

number

 | 

No

 | 

Yes

 | 

Custom game sub-scene ID.

 |
| 

subDescription

 | 

string

 | 

No

 | 

Yes

 | 

Custom sub-scene description. The value length range is \[0, 128\].

 |
| 

importanceLevel

 | 

number

 | 

No

 | 

No

 | 

Importance of a game scene. The value ranges from 1 to 5. The greater the value, the higher the importance.

 |
| 

sceneFrequency

 | 

number

 | 

No

 | 

Yes

 | 

Number of times a scene occurs in a round of game.

 |
| 

sceneTime

 | 

number

 | 

No

 | 

Yes

 | 

Duration of a scene, in milliseconds.

 |
| 

recommendedCpuLevel

 | 

number

 | 

No

 | 

Yes

 | 

CPU level recommended by the game in a scene.

-   **1**: low
-   **2**: middle
-   **3**: high

 |
| 

recommendedGpuLevel

 | 

number

 | 

No

 | 

Yes

 | 

GPU level recommended by the game in a scene.

-   **1**: low
-   **2**: middle
-   **3**: high

 |
| 

recommendedDdrLevel

 | 

number

 | 

No

 | 

Yes

 | 

DDR level recommended by the game in a scene.

-   **1**: low
-   **2**: middle
-   **3**: high

 |
| 

recommendedFps

 | 

number

 | 

No

 | 

Yes

 | 

Target frame rate recommended by the game in a scene.

 |
| 

maxFps

 | 

number

 | 

No

 | 

Yes

 | 

Maximum frame rate in a scene.

 |
| 

currentFps

 | 

number

 | 

No

 | 

Yes

 | 

Current frame rate in a scene.

 |
| 

keyThread

 | 

string

 | 

No

 | 

Yes

 | 

Key thread in a scene.

-   **render**: rendering thread
-   **logic**: logic thread
-   **net**: network thread

The value is in render|xxx|logic|xxx format. The value length range is \[0, 32\].

 |
| 

drawCallCount

 | 

number

 | 

No

 | 

Yes

 | 

Average number of draw calls per frame in a scene.

 |
| 

vertexCount

 | 

number

 | 

No

 | 

Yes

 | 

Average number of model vertices per frame in a scene.

 |
| 

triangleCount

 | 

number

 | 

No

 | 

Yes

 | 

Average number of model triangles per frame in a scene.

 |
| 

shaderCount

 | 

number

 | 

No

 | 

Yes

 | 

Average number of shaders per frame in a scene.

 |
| 

textureCount

 | 

number

 | 

No

 | 

Yes

 | 

Average number of textures per frame in a scene.

 |
| 

meshCount

 | 

number

 | 

No

 | 

Yes

 | 

Average number of meshes per frame in a scene.

 |
| 

channelCount

 | 

number

 | 

No

 | 

Yes

 | 

Number of render channels per frame in a scene.

 |
| 

participantCount

 | 

number

 | 

No

 | 

Yes

 | 

Number of users playing on the same screen in a scene.

 |

#### GameNetInfo

Game network information class, which extends [BaseGameInfo](#section116223815415).

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

netLatency

 | 

string

 | 

No

 | 

No

 | 

Network latency in a game scene, including the overall, uplink, downlink, and server processing time.

The unit is ms. The value length range is \[1, 128\].

NOTE:

The parameter value accepts up to four comma-separated values representing overall, uplink, downlink, and server processing time, for example, **10,20,30,40**. Partial input is allowed and interpreted in order, for example, **10**, **10,20**, or **10,20,30**.

 |
| 

netLoad

 | 

number

 | 

No

 | 

Yes

 | 

Game network load level.

-   **1**: light load
-   **2**: medium load
-   **3**: heavy load

 |

#### GamePlayerInfo

Game player information class, which extends [BaseGameInfo](#section116223815415).

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.0.0(12)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/5NajRUn7QUuOhiR1oPjz9w/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062506Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D40BED48F0FE731703355B92E041061A98B181AB21E03597B64C623DC84FA531)

**gamePlayerId**, **teamPlayerId**, and **thirdOpenId** cannot be left empty at the same time.

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

gamePlayerId

 | 

string

 | 

No

 | 

Yes

 | 

Game player ID. The value length range is \[0, 256\].

 |
| 

teamPlayerId

 | 

string

 | 

No

 | 

Yes

 | 

Team player ID. The value length range is \[0, 256\].

 |
| 

thirdOpenId

 | 

string

 | 

No

 | 

Yes

 | 

Official game account ID. The value length range is \[0, 128\].

 |

#### DeviceInfoParameter

Device status information parameter class.

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.0.1(13)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

deviceInfoType

 | 

[DeviceInfoType](#section13891254145017)

 | 

No

 | 

No

 | 

Device status information type.

NOTE:

-   If **deviceInfoType** is **DeviceInfoType.GPU**, **parameters** must be left empty.
-   If **deviceInfoType** is **DeviceInfoType.THERMAL**, **parameters** can be left empty or set to a value.

 |
| 

parameters

 | 

Record<string, string>

 | 

No

 | 

Yes

 | 

Device status information parameter.

NOTE:

This parameter can be passed when **deviceInfoType** is **DeviceInfoType.THERMAL**. The key is fixed at [DeviceInfoParameterKey](#section1346841562510).THERMAL\_TEMP\_LEVEL, and the value is a specified temperature control level. For details about the value, please refer to [DeviceInfo](#section1033653365917). If this parameter is not passed, the default temperature control level is used.

 |

#### DeviceInfoType

Enumeration object of the device status information type.

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.0.1(13)

| 
**Parameter**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

THERMAL

 | 

1

 | 

Temperature change trend data.

 |
| 

GPU

 | 

2

 | 

GPU load.

 |

#### DeviceInfoParameterKey

Enumeration object of the device status information parameter key value.

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.0.1(13)

| 
**Parameter**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

THERMAL\_TEMP\_LEVEL

 | 

tempLevel

 | 

Temperature control level.

 |

#### GameCustomTag

Enumeration object of the tags of custom game data.

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.1.0(18)

| 
**Parameter**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

CRASH

 | 

1

 | 

Crash.

 |

#### GamePerformanceErrorCode

Game Service Kit error code class.

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.0.0(12)

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Parameter**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

INTERNAL\_ERROR

 | 

1010300001

 | 

Internal system error.

 |
| 

AUTH\_FAILED

 | 

1010300002

 | 

Authentication failure.

 |
| 

INVALID\_REQUEST

 | 

1010300003

 | 

Invalid request.

 |

#### gamePerformance.init

init(gamePackageInfo: GamePackageInfo): Promise<void>

Initializes the game scene perception module when a game is launched. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

gamePackageInfo

 | 

[GamePackageInfo](#section3844175954711)

 | 

Yes

 | 

Game package information class.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

The parameter check failed.

 |
| 

1010300002

 | 

Auth failed.

 |

**Example**:

import { gamePerformance } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let gamePackageInfo: gamePerformance.GamePackageInfo = {
  messageType: 0,
    bundleName: "com.example.demo", // Replace it with the actual game package name.
  appVersion: "1.0"
}
try {
  gamePerformance.init(gamePackageInfo).then(() => {
    // The initialization is successful.
    hilog.info(0x0001, 'demo', \`Succeeded in initializing.\`);
  })
} catch (error) {
  // The initialization failed.
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', \`Failed to initialize. Code: ${err.code}, message: ${err.message}\`);
}

#### gamePerformance.updateGameInfo

updateGameInfo<T extends BaseGameInfo>(gameInfo: T): Promise<void>

Updates game information. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

gameInfo

 | 

[BaseGameInfo](#section116223815415)

 | 

Yes

 | 

Basic game information.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

The parameter check failed.

 |
| 

1010300003

 | 

Invalid request.

 |

**Example**:

// Updating game scene information is used as an example.
import { gamePerformance } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let gameSceneInfo: gamePerformance.GameSceneInfo = {
  messageType: 2,
  sceneID: 7,
  importanceLevel: 4
}
try {
  gamePerformance.updateGameInfo(gameSceneInfo).then(() => {
        // The game scene information is successfully updated.
    hilog.info(0x0001, 'demo', \`Succeeded in updating.\`);
  });
} catch (error) {
    // The game scene information failed to be updated.
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', \`Failed to update. Code: ${err.code}, message: ${err.message}\`);
}

#### gamePerformance.on('deviceStateChanged')

on(type: 'deviceStateChanged', callback: Callback<DeviceInfo>): void

Subscribes to device status changes. This API returns the result through a callback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/qVCvIQkzQ8uOQN9yMu1jkA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062506Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E753C5F76A20A7243578EFC5253EB325B5E5CB2A7FE1469029677F87DC5C303D)

Mali series GPUs do not support GPU performance information collection.

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event to be monitored. Currently, only **deviceStateChanged** event is supported.

 |
| 

callback

 | 

Callback<[DeviceInfo](#section1033653365917)\>

 | 

Yes

 | 

Callback that returns device information.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

The parameter check failed.

 |

**Example**:

import { gamePerformance } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

function onDeviceStateChange(data:gamePerformance.DeviceInfo) {
  // Device details.
  hilog.info(0x0001, 'demo', \`device state changed. tempLevel is ${data.tempLevel}\`);
}

// Subscribe to the **deviceStateChanged** event.
try {
  gamePerformance.on('deviceStateChanged', onDeviceStateChange);
} catch (error) {
  // Subscription failed.
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', \`Failed to subscribe. Code: ${err.code}, message: ${err.message}\`);
}

#### gamePerformance.on('deviceStateChanged')

on(type: 'deviceStateChanged', callback: Callback<DeviceInfo>, scope: Array<DeviceInfoType>): void

Subscribes to device status changes as required. This API returns the result through a callback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/Jd9km9ORSDSFuahd7GB9zw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062506Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D513F96CBF850600D396F2B4EDDA90FEFC38B1E900C97EF53266E116AD3947A5)

Mali series GPUs do not support GPU performance information collection.

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.0.1(13)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event to be monitored. Currently, only **deviceStateChanged** event is supported.

 |
| 

callback

 | 

Callback<[DeviceInfo](#section1033653365917)\>

 | 

Yes

 | 

Callback that returns device information.

 |
| 

scope

 | 

Array<[DeviceInfoType](#section13891254145017)\>

 | 

Yes

 | 

Type of the device status information to be subscribed to.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

The parameter check failed.

 |
| 

1010300003

 | 

Invalid request.

 |

**Example**:

import { gamePerformance } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

function onDeviceStateChange(data:gamePerformance.DeviceInfo) {
  // Device details.
  hilog.info(0x0001, 'demo', \`device state changed. tempLevel is ${data.tempLevel}\`);
}

// Subscribe to the **deviceStateChanged** event.
try {
  let types:Array<gamePerformance.DeviceInfoType> = \[gamePerformance.DeviceInfoType.GPU\];
  gamePerformance.on('deviceStateChanged', onDeviceStateChange,types);
} catch (error) {
  // Subscription failed.
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', \`Failed to subscribe. Code: ${err.code}, message: ${err.message}\`);
}

#### gamePerformance.off('deviceStateChanged')

off(type: 'deviceStateChanged', callback?: Callback<DeviceInfo>): void

Unsubscribes from device status changes. This API returns the result through a callback.

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event to be monitored. Currently, only **deviceStateChanged** event is supported.

 |
| 

callback

 | 

Callback<[DeviceInfo](#section1033653365917)\>

 | 

No

 | 

Callback that returns device information.

If this parameter is specified, the corresponding callback subscription will be canceled. If this parameter is left empty, all callback subscriptions for the **deviceStateChanged** event will be canceled.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

The parameter check failed.

 |

**Example**:

import { gamePerformance } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

function onDeviceStateChange(data:gamePerformance.DeviceInfo) {
  // Device details.
  hilog.info(0x0001, 'demo', \`device state changed. tempLevel is ${data.tempLevel}\`);
}

// Unsubscribe from the **deviceStateChanged** event.
try {
  gamePerformance.off('deviceStateChanged', onDeviceStateChange);
} catch (error) {
  // Unsubscription failed.
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', \`Failed to unsubscribe. Code: ${err.code}, message: ${err.message}\`);
}

// Cancel all callback subscriptions for the **deviceStateChanged** event.
try {
  gamePerformance.off("deviceStateChanged");
} catch (error) {
  // Unsubscription failed.
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', \`Failed to unsubscribe. Code: ${err.code}, message: ${err.message}\`);
}

#### gamePerformance.getDeviceInfoByScope

getDeviceInfoByScope(scope: Array<DeviceInfoParameter>): Promise<DeviceInfo>

Device status query. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/Nv6FbxE5TW-fHGvokHjmdA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062506Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D76CBB04ACE1F59D7EC2EF061AC574016F9C748C74BE7546B733C0C33D78638C)

Mali series GPUs do not support GPU performance information collection.

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.0.1(13)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

scope

 | 

Array<[DeviceInfoParameter](#section12485171912281)\>

 | 

Yes

 | 

Device status information parameter.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<[DeviceInfo](#section1033653365917)\>

 | 

Promise that returns the device status information.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

The parameter check failed.

 |
| 

1010300003

 | 

Invalid request.

 |

**Example**:

import { gamePerformance } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Query device status.
try {
  let gpuParam: gamePerformance.DeviceInfoParameter = {
    deviceInfoType: gamePerformance.DeviceInfoType.GPU
  }
  let thermalParam: gamePerformance.DeviceInfoParameter = {
    deviceInfoType: gamePerformance.DeviceInfoType.THERMAL     
  }
  let gameInfos: Array<gamePerformance.DeviceInfoParameter> = \[gpuParam, thermalParam\];
  gamePerformance.getDeviceInfoByScope(gameInfos).then((deviceInfo:gamePerformance.DeviceInfo) => {
    hilog.info(0x0001, 'demo', \`Succeeded in querying device info. tempLevel is ${deviceInfo.tempLevel}\`);
  });
} catch (error) {
  // Query failed.
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', \`Failed to query. Code: ${err.code}, message: ${err.message}\`);
}

#### gamePerformance.addGameCustomData

addGameCustomData(data: Record<string, string>, tag: GameCustomTag): void

Reports the game's custom data with tags.

**System capability**: SystemCapability.GameService.GamePerformance

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

data

 | 

Record<string, string>

 | 

Yes

 | 

Custom data. The value length range of the key is \[0, 128\], the value length range of the value is \[0, 1024\], and the number of records reported at a time can range from 1 to 100.

NOTE:

Data can be reported multiple times, but the total length of keys and values that have already been reported must not exceed 128,000 characters.

 |
| 

tag

 | 

[GameCustomTag](#section51091113529)

 | 

Yes

 | 

Custom tag.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: 3. Parameter verification failed.

 |
| 

1010300003

 | 

Invalid request.

 |

**Example**:

import { gamePerformance } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Report the game's custom data with the crash tag.
try {
  let data:Record<string, string> = {'custom':'gaming'};
  gamePerformance.addGameCustomData(data, gamePerformance.GameCustomTag.CRASH);
} catch (error) {
  // Failed to report custom data.
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', \`Failed to add custom data. Code: ${err.code}, message: ${err.message}\`);
}
