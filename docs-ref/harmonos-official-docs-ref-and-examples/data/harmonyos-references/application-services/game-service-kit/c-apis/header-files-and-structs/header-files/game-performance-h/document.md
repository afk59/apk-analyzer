# game\_performance.h

#### Overview

This section declares the types of game scene perception and related APIs.

**File to include**: <GameServiceKit/game\_performance.h>

**Library**: libgame\_performance.z.so

**System capability:** SystemCapability.GameService.GamePerformance

**Start version**: 5.0.2(14)

**Related module**: [GamePerformance](../../../modules/gameperformance/document.md)

#### Summary

#### \[h2\]Type Definitions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef struct [GamePerformance\_DeviceInfo](../../../modules/gameperformance/document.md#ga530e1cf28aa5c4d0b355dc053ce27e80) [GamePerformance\_DeviceInfo](../../../modules/gameperformance/document.md#ga530e1cf28aa5c4d0b355dc053ce27e80)

 | 

Defines device performance information.

 |
| 

typedef struct [GamePerformance\_GpuInfo](../../../modules/gameperformance/document.md#gae85f740f82b3ca3f7ec9892d2f81a113) [GamePerformance\_GpuInfo](../../../modules/gameperformance/document.md#gae85f740f82b3ca3f7ec9892d2f81a113)

 | 

Defines GPU performance information.

 |
| 

typedef struct [GamePerformance\_CpuInfo](../../../modules/gameperformance/document.md#ga5e0fa80aa26633c1b9d765340e4a262d) [GamePerformance\_CpuInfo](../../../modules/gameperformance/document.md#ga5e0fa80aa26633c1b9d765340e4a262d)

 | 

Defines CPU performance information.

 |
| 

typedef struct [GamePerformance\_ThermalInfo](../../../modules/gameperformance/document.md#ga6767ea8a1d76ed32db95dc0d3a265a8a) [GamePerformance\_ThermalInfo](../../../modules/gameperformance/document.md#ga6767ea8a1d76ed32db95dc0d3a265a8a)

 | 

Defines temperature information.

 |
| 

typedef struct [GamePerformance\_ThermalInfoQueryParameters](../../../modules/gameperformance/document.md#ga0e825c8963101d40a987d4057033c788) [GamePerformance\_ThermalInfoQueryParameters](../../../modules/gameperformance/document.md#ga0e825c8963101d40a987d4057033c788)

 | 

Defines the parameters for querying temperature information.

 |
| 

typedef struct [GamePerformance\_InitParameters](../../../modules/gameperformance/document.md#ga9ba0e813bb05d37656f9973a35fa0411) [GamePerformance\_InitParameters](../../../modules/gameperformance/document.md#ga9ba0e813bb05d37656f9973a35fa0411)

 | 

Defines initialization parameters.

 |
| 

typedef struct [GamePerformance\_PackageInfo](../../../modules/gameperformance/document.md#gab57ecb4bce0af8b741ef4aa069df2d87) [GamePerformance\_PackageInfo](../../../modules/gameperformance/document.md#gab57ecb4bce0af8b741ef4aa069df2d87)

 | 

Defines game package information.

 |
| 

typedef struct [GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) [GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9)

 | 

Defines game configuration information.

 |
| 

typedef struct [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7)

 | 

Defines game scene information.

 |
| 

typedef struct [GamePerformance\_NetInfo](../../../modules/gameperformance/document.md#gaba275a8588101424676258ffa7217097) [GamePerformance\_NetInfo](../../../modules/gameperformance/document.md#gaba275a8588101424676258ffa7217097)

 | 

Defines game network information.

 |
| 

typedef struct [GamePerformance\_PlayerInfo](../../../modules/gameperformance/document.md#ga804b472fc080d73a2ce23da927ffd842) [GamePerformance\_PlayerInfo](../../../modules/gameperformance/document.md#ga804b472fc080d73a2ce23da927ffd842)

 | 

Defines game player information.

 |
| 

typedef enum [GamePerformance\_EngineType](../../../modules/gameperformance/document.md#gab7f3d09e6dd4af1692872b6b5815af45) [GamePerformance\_EngineType](../../../modules/gameperformance/document.md#ga449d5fa8c8ee0fbea9188fd345401462)

 | 

Defines game engine types.

 |
| 

typedef enum [GamePerformance\_GameType](../../../modules/gameperformance/document.md#ga9c1b6f00c4769f13c510a7a871c7afd3) [GamePerformance\_GameType](../../../modules/gameperformance/document.md#ga1e1370020b763cb4cce215d955ebb78d)

 | 

Defines game types.

 |
| 

typedef enum [GamePerformance\_PictureQualityLevel](../../../modules/gameperformance/document.md#ga64fd3d566be9f8240d0f474d52c292dd) [GamePerformance\_PictureQualityLevel](../../../modules/gameperformance/document.md#gab726f445d701d96ff647efa723ef993d)

 | 

Defines image quality levels.

 |
| 

typedef enum [GamePerformance\_SceneImportanceLevel](../../../modules/gameperformance/document.md#gaf6bbf14a7010d4e99e6c758a718a08a6) [GamePerformance\_SceneImportanceLevel](../../../modules/gameperformance/document.md#ga59c720e67f9586ae4f24223be1ae3dc5)

 | 

Defines importance levels of game scenes.

 |
| 

typedef enum [GamePerformance\_CpuLevel](../../../modules/gameperformance/document.md#ga11ac456fd1b33d0b1f6220af5e5cd1ce) [GamePerformance\_CpuLevel](../../../modules/gameperformance/document.md#ga4d30bee20aca3ea7082302ae7164a196)

 | 

Defines CPU levels.

 |
| 

typedef enum [GamePerformance\_GpuLevel](../../../modules/gameperformance/document.md#ga48d14f66a8d484b497157458dd13a473) [GamePerformance\_GpuLevel](../../../modules/gameperformance/document.md#ga12e1ee7ac06fc6bd25a87cce66d2a632)

 | 

Defines GPU levels.

 |
| 

typedef enum [GamePerformance\_DdrLevel](../../../modules/gameperformance/document.md#gaec1b60b592a13ea85774a4d2ec8581bb) [GamePerformance\_DdrLevel](../../../modules/gameperformance/document.md#ga57b549a68edbc9c84843040beb886389)

 | 

Defines DDR levels.

 |
| 

typedef enum [GamePerformance\_NetLoad](../../../modules/gameperformance/document.md#ga517e25164876d3727c407c887943aee2) [GamePerformance\_NetLoad](../../../modules/gameperformance/document.md#ga638c2b6f6d0dda3138e34869635b2dd4)

 | 

Defines game network load levels.

 |
| 

typedef enum [GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#gad952c8a450a72955d4dc24c43df7eee6)

 | 

Defines error codes.

 |
| 

typedef enum [GamePerformance\_DeviceInfoType](../../../modules/gameperformance/document.md#ga3ebb81788405856534d8fb3cd6194ca4) [GamePerformance\_DeviceInfoType](../../../modules/gameperformance/document.md#gac1d8c407b85cedf00dc6f6cf1f3ac202)

 | 

Defines device performance information types.

 |
| 

typedef void(\*[GamePerformance\_ThermalLevelChangedCallback](../../../modules/gameperformance/document.md#ga94e7e85a3f0ad0b495b2c525a15ebc8e)) ([GamePerformance\_DeviceInfo](../../../modules/gameperformance/document.md#ga530e1cf28aa5c4d0b355dc053ce27e80) \*deviceInfo, void \*userData)

 | 

Callback used in [HMS\_GamePerformance\_RegisterThermalLevelChangedCallback](../../../modules/gameperformance/document.md#gaa73a9464dbe4a973e7aed559835adbc6). This callback will be triggered once when the temperature level changes to a level below 3, and will be triggered every 10 seconds when the temperature level changes to level 3 or higher.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[GamePerformance\_EngineType](../../../modules/gameperformance/document.md#gab7f3d09e6dd4af1692872b6b5815af45) {

GAME\_PERFORMANCE\_ENGINE\_TYPE\_UNITY = 1,

GAME\_PERFORMANCE\_ENGINE\_TYPE\_UNREAL = 2,

GAME\_PERFORMANCE\_ENGINE\_TYPE\_MESSIAH = 3,

GAME\_PERFORMANCE\_ENGINE\_TYPE\_COCOS = 4,

GAME\_PERFORMANCE\_ENGINE\_TYPE\_OTHERS = 200

}

 | 

Describes engine types.

 |
| 

[GamePerformance\_GameType](../../../modules/gameperformance/document.md#ga9c1b6f00c4769f13c510a7a871c7afd3) {

GAME\_PERFORMANCE\_GAME\_TYPE\_MOBA = 1,

GAME\_PERFORMANCE\_GAME\_TYPE\_RPG = 2,

GAME\_PERFORMANCE\_GAME\_TYPE\_FPS = 3,

GAME\_PERFORMANCE\_GAME\_TYPE\_FTG = 4,

GAME\_PERFORMANCE\_GAME\_TYPE\_RAC = 5,

GAME\_PERFORMANCE\_GAME\_TYPE\_OTHERS = 200

}

 | 

Describes game types.

 |
| 

[GamePerformance\_PictureQualityLevel](../../../modules/gameperformance/document.md#ga64fd3d566be9f8240d0f474d52c292dd) {

GAME\_PERFORMANCE\_PQL\_SMOOTH = 1,

GAME\_PERFORMANCE\_PQL\_BALANCED = 2,

GAME\_PERFORMANCE\_PQL\_HD = 3,

GAME\_PERFORMANCE\_PQL\_HDR = 4,

GAME\_PERFORMANCE\_PQL\_UHD = 5

}

 | 

Describes image quality levels.

 |
| 

[GamePerformance\_SceneImportanceLevel](../../../modules/gameperformance/document.md#gaf6bbf14a7010d4e99e6c758a718a08a6) {

GAME\_PERFORMANCE\_SIL\_LEVEL1 = 1,

GAME\_PERFORMANCE\_SIL\_LEVEL2 = 2,

GAME\_PERFORMANCE\_SIL\_LEVEL3 = 3,

GAME\_PERFORMANCE\_SIL\_LEVEL4 = 4,

GAME\_PERFORMANCE\_SIL\_LEVEL5 = 5

}

 | 

Describes importance levels of game scenes.

 |
| 

[GamePerformance\_CpuLevel](../../../modules/gameperformance/document.md#ga11ac456fd1b33d0b1f6220af5e5cd1ce) {

GAME\_PERFORMANCE\_CPU\_LEVEL\_LOW = 1,

GAME\_PERFORMANCE\_CPU\_LEVEL\_MIDDLE = 2,

GAME\_PERFORMANCE\_CPU\_LEVEL\_HIGH = 3

}

 | 

Describes CPU levels.

 |
| 

[GamePerformance\_GpuLevel](../../../modules/gameperformance/document.md#ga48d14f66a8d484b497157458dd13a473) {

GAME\_PERFORMANCE\_GPU\_LEVEL\_LOW = 1,

GAME\_PERFORMANCE\_GPU\_LEVEL\_MIDDLE = 2,

GAME\_PERFORMANCE\_GPU\_LEVEL\_HIGH = 3

}

 | 

Describes GPU levels.

 |
| 

[GamePerformance\_DdrLevel](../../../modules/gameperformance/document.md#gaec1b60b592a13ea85774a4d2ec8581bb) {

GAME\_PERFORMANCE\_DDR\_LEVEL\_LOW = 1,

GAME\_PERFORMANCE\_DDR\_LEVEL\_MIDDLE = 2,

GAME\_PERFORMANCE\_DDR\_LEVEL\_HIGH = 3

}

 | 

Describes DDR levels.

 |
| 

[GamePerformance\_NetLoad](../../../modules/gameperformance/document.md#ga517e25164876d3727c407c887943aee2) {

GAME\_PERFORMANCE\_NET\_LOAD\_LIGHT = 1,

GAME\_PERFORMANCE\_NET\_LOAD\_MODERATE = 2,

GAME\_PERFORMANCE\_NET\_LOAD\_HEAVY = 3

}

 | 

Describes network load levels.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) {

GAME\_PERFORMANCE\_SUCCESS = 0,

GAME\_PERFORMANCE\_PARAM\_INVALID = 401,

GAME\_PERFORMANCE\_INTERNAL\_ERROR = 1010300001,

GAME\_PERFORMANCE\_AUTH\_FAILED = 1010300002,

GAME\_PERFORMANCE\_INVALID\_REQUEST = 1010300003,

GAME\_PERFORMANCE\_PARAM\_ERROR = 1010300004

}

 | 

Describes error codes.

**GAME\_PERFORMANCE\_PARAM\_ERROR** is supported since 6.0.2(22).

 |
| 

[GamePerformance\_DeviceInfoType](../../../modules/gameperformance/document.md#ga3ebb81788405856534d8fb3cd6194ca4) {

GAME\_PERFORMANCE\_DEVICEINFO\_TYPE\_THERMAL = 0,

GAME\_PERFORMANCE\_DEVICEINFO\_TYPE\_GPU = 1,

GAME\_PERFORMANCE\_DEVICEINFO\_TYPE\_CPU = 2

}

 | 

Describes device performance information types.

**GAME\_PERFORMANCE\_DEVICEINFO\_TYPE\_CPU** is supported since 6.0.2(22).

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

**Functions related to initialization (init)**

Before calling **HMS\_GamePerformance\_Init**, ensure that **bundleName** and **appVersion** have been set.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_CreateInitParameters](../../../modules/gameperformance/document.md#ga82a96cb32e0980c6650b262b268158a2) ([GamePerformance\_InitParameters](../../../modules/gameperformance/document.md#ga9ba0e813bb05d37656f9973a35fa0411) \*\*initParameters)

 | 

Creates a [GamePerformance\_InitParameters](../../../modules/gameperformance/document.md#ga9ba0e813bb05d37656f9973a35fa0411) instance, which will be used in the [HMS\_GamePerformance\_Init](../../../modules/gameperformance/document.md#ga1045d9d8f4e7972b44ff95571afca8f9) method.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyInitParameters](../../../modules/gameperformance/document.md#gaef8a6ecaefc0f7ca4b8e2c88a84f5db0) ([GamePerformance\_InitParameters](../../../modules/gameperformance/document.md#ga9ba0e813bb05d37656f9973a35fa0411) \*\*initParameters)

 | 

Destroys a [GamePerformance\_InitParameters](../../../modules/gameperformance/document.md#ga9ba0e813bb05d37656f9973a35fa0411) instance when it is no longer used.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_InitParameters\_SetBundleName](../../../modules/gameperformance/document.md#ga35962b201b42b841202d0986e7e80250) ([GamePerformance\_InitParameters](../../../modules/gameperformance/document.md#ga9ba0e813bb05d37656f9973a35fa0411) \*initParameters, const char \*bundleName)

 | 

Sets the package name for the [GamePerformance\_InitParameters](../../../modules/gameperformance/document.md#ga9ba0e813bb05d37656f9973a35fa0411) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_InitParameters\_SetAppVersion](../../../modules/gameperformance/document.md#gab19d551d38ea087012ba205f975ec5ed) ([GamePerformance\_InitParameters](../../../modules/gameperformance/document.md#ga9ba0e813bb05d37656f9973a35fa0411) \*initParameters, const char \*appVersion)

 | 

Sets the version number for the [GamePerformance\_InitParameters](../../../modules/gameperformance/document.md#ga9ba0e813bb05d37656f9973a35fa0411) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_Init](../../../modules/gameperformance/document.md#ga1045d9d8f4e7972b44ff95571afca8f9) ([GamePerformance\_InitParameters](../../../modules/gameperformance/document.md#ga9ba0e813bb05d37656f9973a35fa0411) \*initParameters)

 | 

Initializes the game scene perception module.

 |
| 

**Functions related to game package information (PackageInfo)**

Before calling **HMS\_GamePerformance\_UpdatePackageInfo**, ensure that **bundleName** and **appVersion** have been set.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_CreatePackageInfo](../../../modules/gameperformance/document.md#ga6b54d67769794ce6833cbecf7a0fb9ab) ([GamePerformance\_PackageInfo](../../../modules/gameperformance/document.md#gab57ecb4bce0af8b741ef4aa069df2d87) \*\*packageInfo)

 | 

Creates a [GamePerformance\_PackageInfo](../../../modules/gameperformance/document.md#gab57ecb4bce0af8b741ef4aa069df2d87) instance, which will be used in the [HMS\_GamePerformance\_UpdatePackageInfo](../../../modules/gameperformance/document.md#ga317ba7027076ce06ae73a6188bc3b129) method.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyPackageInfo](../../../modules/gameperformance/document.md#ga2019dcc34f428ae80868c0af612237c3) ([GamePerformance\_PackageInfo](../../../modules/gameperformance/document.md#gab57ecb4bce0af8b741ef4aa069df2d87) \*\*packageInfo)

 | 

Destroys a [GamePerformance\_PackageInfo](../../../modules/gameperformance/document.md#gab57ecb4bce0af8b741ef4aa069df2d87) instance when it is no longer used.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_PackageInfo\_SetBundleName](../../../modules/gameperformance/document.md#ga623a88c7ea2c5eb022dd8a784e8b6661) ([GamePerformance\_PackageInfo](../../../modules/gameperformance/document.md#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo, const char \*bundleName)

 | 

Sets the package name for the [GamePerformance\_PackageInfo](../../../modules/gameperformance/document.md#gab57ecb4bce0af8b741ef4aa069df2d87) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_PackageInfo\_SetAppVersion](../../../modules/gameperformance/document.md#ga0afa327f6afed7acfc998c3f79bfeb76) ([GamePerformance\_PackageInfo](../../../modules/gameperformance/document.md#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo, const char \*appVersion)

 | 

Sets the version number for the [GamePerformance\_PackageInfo](../../../modules/gameperformance/document.md#gab57ecb4bce0af8b741ef4aa069df2d87) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_PackageInfo\_SetEngineType](../../../modules/gameperformance/document.md#ga1436072d310ec40ddc2a85d6bafd0ee2) ([GamePerformance\_PackageInfo](../../../modules/gameperformance/document.md#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo, const [GamePerformance\_EngineType](../../../modules/gameperformance/document.md#gab7f3d09e6dd4af1692872b6b5815af45) engineType)

 | 

Sets the engine type for the [GamePerformance\_PackageInfo](../../../modules/gameperformance/document.md#gab57ecb4bce0af8b741ef4aa069df2d87) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_PackageInfo\_SetEngineVersion](../../../modules/gameperformance/document.md#ga73b762ef177488deecf97f04395f70d5) ([GamePerformance\_PackageInfo](../../../modules/gameperformance/document.md#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo, const char \*engineVersion)

 | 

Sets the engine version number for the [GamePerformance\_PackageInfo](../../../modules/gameperformance/document.md#gab57ecb4bce0af8b741ef4aa069df2d87) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_PackageInfo\_SetGameType](../../../modules/gameperformance/document.md#gac5f6695702063b61b4f7cc885129dfe2) ([GamePerformance\_PackageInfo](../../../modules/gameperformance/document.md#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo, const [GamePerformance\_GameType](../../../modules/gameperformance/document.md#ga9c1b6f00c4769f13c510a7a871c7afd3) gameType)

 | 

Sets the game type for the [GamePerformance\_PackageInfo](../../../modules/gameperformance/document.md#gab57ecb4bce0af8b741ef4aa069df2d87) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_PackageInfo\_SetVulkanSupported](../../../modules/gameperformance/document.md#gadfbc32fbe65b9763d2cb393af8485dbb) ([GamePerformance\_PackageInfo](../../../modules/gameperformance/document.md#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo, const bool vulkanSupported)

 | 

Sets whether the [GamePerformance\_PackageInfo](../../../modules/gameperformance/document.md#gab57ecb4bce0af8b741ef4aa069df2d87) instance supports Vulkan.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UpdatePackageInfo](../../../modules/gameperformance/document.md#ga317ba7027076ce06ae73a6188bc3b129) ([GamePerformance\_PackageInfo](../../../modules/gameperformance/document.md#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo)

 | 

Updates game package information.

 |
| 

**Functions related to game configuration information (ConfigInfo)**

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_CreateConfigInfo](../../../modules/gameperformance/document.md#ga2124abdf7dfed3b2c37242228a442128) ([GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*\*configInfo)

 | 

Creates a [GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance, which will be used in the [HMS\_GamePerformance\_UpdateConfigInfo](../../../modules/gameperformance/document.md#ga6fe77ea4f43939333c7c3b07e1204448) method.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyConfigInfo](../../../modules/gameperformance/document.md#ga8328d927012e4b868175ad3c192a947b) ([GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*\*configInfo)

 | 

Destroys a [GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance when it is no longer used.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetMaxPictureQualityLevel](../../../modules/gameperformance/document.md#ga5f85d32e8f74f4ab008abd49f1109c46) ([GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const [GamePerformance\_PictureQualityLevel](../../../modules/gameperformance/document.md#ga64fd3d566be9f8240d0f474d52c292dd) maxPictureQualityLevel)

 | 

Sets the maximum image quality level for the [GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetCurrentPictureQualityLevel](../../../modules/gameperformance/document.md#gad44e9925a145ab621f4d8ff348de4034) ([GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const [GamePerformance\_PictureQualityLevel](../../../modules/gameperformance/document.md#ga64fd3d566be9f8240d0f474d52c292dd) currentPictureQualityLevel)

 | 

Sets the current image quality level for the [GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetMaxFrameRate](../../../modules/gameperformance/document.md#ga6665850e826d430bba7525351ef2df70) ([GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const int64\_t maxFrameRate)

 | 

Sets the maximum frame rate for the [GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetCurrentFrameRate](../../../modules/gameperformance/document.md#ga89845a005ea8f0a5069ef2563f55936e) ([GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const int64\_t currentFrameRate)

 | 

Sets the current frame rate for the [GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetMaxResolution](../../../modules/gameperformance/document.md#gad34b019dfa3a973512c7157dcba92ad1) ([GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const char \*maxResolution)

 | 

Sets the maximum resolution for the [GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetCurrentResolution](../../../modules/gameperformance/document.md#ga9bee7c2052d81a0dd6c6f93ce57ddc1f) ([GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const char \*currentResolution)

 | 

Sets the current resolution for the [GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetAntiAliasingEnabled](../../../modules/gameperformance/document.md#ga5657a6e00ba9e08803a201a8d0c1cecd) ([GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const bool antiAliasingEnabled)

 | 

Sets whether to enable anti-aliasing for the [GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetShadowEnabled](../../../modules/gameperformance/document.md#ga1beebb2eabcea33e37de8015ac29ef9c) ([GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const bool shadowEnabled)

 | 

Sets whether to enable the shadow effect for the [GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetMultithreadingEnabled](../../../modules/gameperformance/document.md#gab69ed9d7e95fe067d618514a6472c2b3) ([GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const bool multithreadingEnabled)

 | 

Enables multi-threading for the [GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetParticleEnabled](../../../modules/gameperformance/document.md#ga808ed7b13bc8ed4fd97267a65c8f4469) ([GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const bool particleEnabled)

 | 

Sets the particle effect for the [GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetHdModeEnabled](../../../modules/gameperformance/document.md#ga5ef09e013a67def087e5f6b5442ff0b0) ([GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const bool hdModeEnabled)

 | 

Enables the HD mode for the [GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UpdateConfigInfo](../../../modules/gameperformance/document.md#ga6fe77ea4f43939333c7c3b07e1204448) ([GamePerformance\_ConfigInfo](../../../modules/gameperformance/document.md#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo)

 | 

Updates game configuration information.

 |
| 

**Functions related to game scene information (SceneInfo)**

Before calling **HMS\_GamePerformance\_UpdateSceneInfo**, ensure that **sceneID** and **importanceLevel** have been set.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_CreateSceneInfo](../../../modules/gameperformance/document.md#ga20ba3d28237372a1f44652f50d0850c4) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*\*sceneInfo)

 | 

Creates a [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance, which will be used in the [HMS\_GamePerformance\_UpdateSceneInfo](../../../modules/gameperformance/document.md#gad9504bae5e5b570e55bdf7f84a7a05bf) method.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroySceneInfo](../../../modules/gameperformance/document.md#gadc5f2c4b6b7258830736fb194d06bdd8) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*\*sceneInfo)

 | 

Destroys a [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance when it is no longer used.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetSceneID](../../../modules/gameperformance/document.md#gaaf792159ff58c372c80106a3e050e7bc) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t sceneID)

 | 

Sets the scene ID for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetDescription](../../../modules/gameperformance/document.md#ga32193247c7f59a29920b5ec084a89a6c) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const char \*description)

 | 

Sets the scene description for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetSubSceneID](../../../modules/gameperformance/document.md#gaf66ab2b453b1f9e5df8173f839490540) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const char \*subSceneID)

 | 

Sets the sub-scene ID for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetSubDescription](../../../modules/gameperformance/document.md#ga1d6ed7ffa24f5002ffbd799877467056) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const char \*subDescription)

 | 

Sets the sub-scene description for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetImportanceLevel](../../../modules/gameperformance/document.md#ga5a7748133e83c9aebaa439e0d97fe742) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const [GamePerformance\_SceneImportanceLevel](../../../modules/gameperformance/document.md#gaf6bbf14a7010d4e99e6c758a718a08a6) importanceLevel)

 | 

Sets the scene importance level for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetSceneFrequency](../../../modules/gameperformance/document.md#ga3743a3ad2a364d6b039b2dbc1213f04a) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t sceneFrequency)

 | 

Sets the number of times a scene appears in a round of the game for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetSceneTime](../../../modules/gameperformance/document.md#gaa7d8eab6076c00e220da385a51016847) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t sceneTime)

 | 

Sets the scene duration for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetRecommendedCpuLevel](../../../modules/gameperformance/document.md#ga423176ac542a8058fd4bdc31e19e49fb) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const [GamePerformance\_CpuLevel](../../../modules/gameperformance/document.md#ga11ac456fd1b33d0b1f6220af5e5cd1ce) recommendedCpuLevel)

 | 

Sets the recommended CPU level for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetRecommendedGpuLevel](../../../modules/gameperformance/document.md#gaf7bb4de842d1045434417997abb12365) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const [GamePerformance\_GpuLevel](../../../modules/gameperformance/document.md#ga48d14f66a8d484b497157458dd13a473) recommendedGpuLevel)

 | 

Sets the recommended GPU level for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetRecommendedDdrLevel](../../../modules/gameperformance/document.md#ga919d39c5eaa6e8e0a1f88c42f4d55264) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const [GamePerformance\_DdrLevel](../../../modules/gameperformance/document.md#gaec1b60b592a13ea85774a4d2ec8581bb) recommendedDdrLevel)

 | 

Sets the recommended DDR level for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetMaxFrameRate](../../../modules/gameperformance/document.md#gad672cb46e420b0cee29da39d4009a7c9) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t maxFrameRate)

 | 

Sets the maximum frame rate of a scene for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetCurrentFrameRate](../../../modules/gameperformance/document.md#ga70f297a098b963e0216cf1fc0b2d3075) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t currentFrameRate)

 | 

Sets the frame rate of the current scene for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetKeyThread](../../../modules/gameperformance/document.md#gaa41913e398bd82a136497889c4c40435) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const char \*keyThread)

 | 

Sets the key thread for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetDrawCallCount](../../../modules/gameperformance/document.md#ga8504590e1f52eba1ab01f9e29d5344e3) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t drawCallCount)

 | 

Sets the average number of draw calls per frame for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetVertexCount](../../../modules/gameperformance/document.md#ga5a10d96f46fbc5353d4c077970b5b3b7) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t vertexCount)

 | 

Sets the average number of model vertices per frame for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetTriangleCount](../../../modules/gameperformance/document.md#ga98ba98ee175a97bc9b40dfb4576194ea) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t triangleCount)

 | 

Sets the average number of model triangles per frame for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetShaderCount](../../../modules/gameperformance/document.md#gacc04bf99a463910cfdf3e96e0d1f7168) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t shaderCount)

 | 

Sets the average number of shaders per frame for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetTextureCount](../../../modules/gameperformance/document.md#gac374255a0c99f721ff7227e2c9a599d3) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t textureCount)

 | 

Sets the average number of textures per frame for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetMeshCount](../../../modules/gameperformance/document.md#ga00ab8ad16a928499daf8359fed8343b8) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t meshCount)

 | 

Sets the average number of meshes per frame for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetChannelCount](../../../modules/gameperformance/document.md#ga4d6f34ef3b653c79c110c0fd35a5cca6) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t channelCount)

 | 

Sets the number of channels rendered per frame for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetParticipantCount](../../../modules/gameperformance/document.md#ga3a3eaf50d555e6539c0f61543bc7898e) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t participantCount)

 | 

Sets the number of players on the same screen in a scene for the [GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UpdateSceneInfo](../../../modules/gameperformance/document.md#gad9504bae5e5b570e55bdf7f84a7a05bf) ([GamePerformance\_SceneInfo](../../../modules/gameperformance/document.md#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo)

 | 

Updates game scene information.

 |
| 

**Functions related to game network information (NetInfo)**

Before calling **HMS\_GamePerformance\_UpdateNetInfo**, ensure that **totalLatency** has been set.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_CreateNetInfo](../../../modules/gameperformance/document.md#ga7c2084205b1c6402f6c7697aa93ea08e) ([GamePerformance\_NetInfo](../../../modules/gameperformance/document.md#gaba275a8588101424676258ffa7217097) \*\*netInfo)

 | 

Creates a [GamePerformance\_NetInfo](../../../modules/gameperformance/document.md#gaba275a8588101424676258ffa7217097) instance, which will be used in the [HMS\_GamePerformance\_UpdateNetInfo](../../../modules/gameperformance/document.md#ga29ff530f9f37560359fdd0d28ba6275b) method.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyNetInfo](../../../modules/gameperformance/document.md#ga7e97470d2e305c3777438ba7cc524cac) ([GamePerformance\_NetInfo](../../../modules/gameperformance/document.md#gaba275a8588101424676258ffa7217097) \*\*netInfo)

 | 

Destroys a [GamePerformance\_NetInfo](../../../modules/gameperformance/document.md#gaba275a8588101424676258ffa7217097) instance when it is no longer used.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_NetInfo\_SetTotalLatency](../../../modules/gameperformance/document.md#gaf2b2757c599992d8eb90767513abef59) ([GamePerformance\_NetInfo](../../../modules/gameperformance/document.md#gaba275a8588101424676258ffa7217097) \*netInfo, const int64\_t total)

 | 

Sets the total network latency for the [GamePerformance\_NetInfo](../../../modules/gameperformance/document.md#gaba275a8588101424676258ffa7217097) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_NetInfo\_SetUplinkLatency](../../../modules/gameperformance/document.md#gaa0876f5a71061d68f084d40d2b1039e2) ([GamePerformance\_NetInfo](../../../modules/gameperformance/document.md#gaba275a8588101424676258ffa7217097) \*netInfo, const int64\_t up)

 | 

Sets the uplink network latency for the [GamePerformance\_NetInfo](../../../modules/gameperformance/document.md#gaba275a8588101424676258ffa7217097) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_NetInfo\_SetDownlinkLatency](../../../modules/gameperformance/document.md#ga1edfa8aa64d9773b3b768e1653690479) ([GamePerformance\_NetInfo](../../../modules/gameperformance/document.md#gaba275a8588101424676258ffa7217097) \*netInfo, const int64\_t down)

 | 

Sets the downlink network latency for the [GamePerformance\_NetInfo](../../../modules/gameperformance/document.md#gaba275a8588101424676258ffa7217097) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_NetInfo\_SetServerLatency](../../../modules/gameperformance/document.md#ga5920ded727e6ca21760b82d5586064b9) ([GamePerformance\_NetInfo](../../../modules/gameperformance/document.md#gaba275a8588101424676258ffa7217097) \*netInfo, const int64\_t server)

 | 

Sets the server network latency for the [GamePerformance\_NetInfo](../../../modules/gameperformance/document.md#gaba275a8588101424676258ffa7217097) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_NetInfo\_SetNetLoad](../../../modules/gameperformance/document.md#ga74aab7c053e2bf62aacef57ea223aa28) ([GamePerformance\_NetInfo](../../../modules/gameperformance/document.md#gaba275a8588101424676258ffa7217097) \*netInfo, const [GamePerformance\_NetLoad](../../../modules/gameperformance/document.md#ga517e25164876d3727c407c887943aee2) netLoad)

 | 

Sets the network load for the [GamePerformance\_NetInfo](../../../modules/gameperformance/document.md#gaba275a8588101424676258ffa7217097) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UpdateNetInfo](../../../modules/gameperformance/document.md#ga29ff530f9f37560359fdd0d28ba6275b) ([GamePerformance\_NetInfo](../../../modules/gameperformance/document.md#gaba275a8588101424676258ffa7217097) \*netInfo)

 | 

Updates game network information.

 |
| 

**Functions related to game player information (PlayerInfo)**

**gamePlayerId**, **teamPlayerId**, and **thirdOpenId** cannot be left empty at the same time.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_CreatePlayerInfo](../../../modules/gameperformance/document.md#ga97925740bdc7df3aefbd482304294208) ([GamePerformance\_PlayerInfo](../../../modules/gameperformance/document.md#ga804b472fc080d73a2ce23da927ffd842) \*\*playerInfo)

 | 

Creates a [GamePerformance\_PlayerInfo](../../../modules/gameperformance/document.md#ga804b472fc080d73a2ce23da927ffd842) instance, which will be used in the [HMS\_GamePerformance\_UpdatePlayerInfo](../../../modules/gameperformance/document.md#ga71c7be26b9531af9bcd807e3255c4e6f) method.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyPlayerInfo](../../../modules/gameperformance/document.md#ga42254ab6d5c9a8ec61f512d1e2903256) ([GamePerformance\_PlayerInfo](../../../modules/gameperformance/document.md#ga804b472fc080d73a2ce23da927ffd842) \*\*playerInfo)

 | 

Destroys a [GamePerformance\_PlayerInfo](../../../modules/gameperformance/document.md#ga804b472fc080d73a2ce23da927ffd842) instance when it is no longer used.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_PlayerInfo\_SetGamePlayerId](../../../modules/gameperformance/document.md#gaccabd2811fc0e84e95a50219b34f1814) ([GamePerformance\_PlayerInfo](../../../modules/gameperformance/document.md#ga804b472fc080d73a2ce23da927ffd842) \*playerInfo, const char \*gamePlayerId)

 | 

Sets the player ID for the [GamePerformance\_PlayerInfo](../../../modules/gameperformance/document.md#ga804b472fc080d73a2ce23da927ffd842) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_PlayerInfo\_SetTeamPlayerId](../../../modules/gameperformance/document.md#gaa5068c2f80ffc184cbebb03f22ece595) ([GamePerformance\_PlayerInfo](../../../modules/gameperformance/document.md#ga804b472fc080d73a2ce23da927ffd842) \*playerInfo, const char \*teamPlayerId)

 | 

Sets the team player ID for the [GamePerformance\_PlayerInfo](../../../modules/gameperformance/document.md#ga804b472fc080d73a2ce23da927ffd842) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_PlayerInfo\_SetThirdOpenId](../../../modules/gameperformance/document.md#ga875a2f1dad9091927ada365f6e9b6d5d) ([GamePerformance\_PlayerInfo](../../../modules/gameperformance/document.md#ga804b472fc080d73a2ce23da927ffd842) \*playerInfo, const char \*thirdOpenId)

 | 

Sets the official game account for the [GamePerformance\_PlayerInfo](../../../modules/gameperformance/document.md#ga804b472fc080d73a2ce23da927ffd842) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UpdatePlayerInfo](../../../modules/gameperformance/document.md#ga71c7be26b9531af9bcd807e3255c4e6f) ([GamePerformance\_PlayerInfo](../../../modules/gameperformance/document.md#ga804b472fc080d73a2ce23da927ffd842) \*playerInfo)

 | 

Updates game player information.

 |
| 

**Functions related to subscription**

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_RegisterThermalLevelChangedCallback](../../../modules/gameperformance/document.md#gaa73a9464dbe4a973e7aed559835adbc6) ([GamePerformance\_DeviceInfoType](../../../modules/gameperformance/document.md#ga3ebb81788405856534d8fb3cd6194ca4) \*types\[\], size\_t size, [GamePerformance\_ThermalLevelChangedCallback](../../../modules/gameperformance/document.md#ga94e7e85a3f0ad0b495b2c525a15ebc8e) callback, void \*userData)

 | 

Subscribes to temperature changes by registering the callback for temperature changes. When the trigger point is reached, this callback will be called.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UnregisterThermalLevelChangedCallback](../../../modules/gameperformance/document.md#ga306734f0bee9af7697b5fbfa19bafec0) ([GamePerformance\_ThermalLevelChangedCallback](../../../modules/gameperformance/document.md#ga94e7e85a3f0ad0b495b2c525a15ebc8e) callback)

 | 

Deregisters specified callbacks for temperature changes.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UnregisterAllThermalLevelChangedCallbacks](../../../modules/gameperformance/document.md#ga0f2cf9152a9421d00bb0c03683b3f57d) (void)

 | 

Deregisters all callbacks for temperature changes.

 |
| 

**Functions for querying temperature information**

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_CreateThermalInfoQueryParameters](../../../modules/gameperformance/document.md#gad3e60ec2d47a5068206bc3e1f217acc2) ([GamePerformance\_ThermalInfoQueryParameters](../../../modules/gameperformance/document.md#ga0e825c8963101d40a987d4057033c788) \*\*parameters)

 | 

Creates a [GamePerformance\_ThermalInfoQueryParameters](../../../modules/gameperformance/document.md#ga0e825c8963101d40a987d4057033c788) instance, which will be used in the [HMS\_GamePerformance\_QueryThermalInfo](../../../modules/gameperformance/document.md#gab7cb47e0dc3cce1169a8104827f7edb7) method.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyThermalInfoQueryParameters](../../../modules/gameperformance/document.md#ga6b9314f647ed520b11b9dfa4fbc40351) ([GamePerformance\_ThermalInfoQueryParameters](../../../modules/gameperformance/document.md#ga0e825c8963101d40a987d4057033c788) \*\*parameters)

 | 

Destroys a [GamePerformance\_ThermalInfoQueryParameters](../../../modules/gameperformance/document.md#ga0e825c8963101d40a987d4057033c788) instance when it is no longer used.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ThermalInfoQueryParameters\_SetNeedsPrediction](../../../modules/gameperformance/document.md#ga7ce2e82b511a0158d93d2ee147536ee7) ([GamePerformance\_ThermalInfoQueryParameters](../../../modules/gameperformance/document.md#ga0e825c8963101d40a987d4057033c788) \*parameters, const bool needsPrediction)

 | 

Sets whether predicting temperature trend is required for the [GamePerformance\_ThermalInfoQueryParameters](../../../modules/gameperformance/document.md#ga0e825c8963101d40a987d4057033c788) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ThermalInfoQueryParameters\_SetTargetThermalLevel](../../../modules/gameperformance/document.md#ga5cb94581ca23d465933e9316fdb0605d) ([GamePerformance\_ThermalInfoQueryParameters](../../../modules/gameperformance/document.md#ga0e825c8963101d40a987d4057033c788) \*parameters, const int32\_t targetThermalLevel)

 | 

Sets the target temperature level for predicting the temperature trend for the [GamePerformance\_ThermalInfoQueryParameters](../../../modules/gameperformance/document.md#ga0e825c8963101d40a987d4057033c788) instance.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_QueryThermalInfo](../../../modules/gameperformance/document.md#gab7cb47e0dc3cce1169a8104827f7edb7) ([GamePerformance\_ThermalInfoQueryParameters](../../../modules/gameperformance/document.md#ga0e825c8963101d40a987d4057033c788) \*parameters, [GamePerformance\_ThermalInfo](../../../modules/gameperformance/document.md#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*\*thermalInfo)

 | 

Queries temperature information.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyThermalInfo](../../../modules/gameperformance/document.md#gacc640a4e15fe9cab1f8bccb652d77e59) ([GamePerformance\_ThermalInfo](../../../modules/gameperformance/document.md#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*\*thermalInfo)

 | 

Destroys a [GamePerformance\_ThermalInfo](../../../modules/gameperformance/document.md#ga6767ea8a1d76ed32db95dc0d3a265a8a) instance when it is no longer used.

 |
| 

**Functions for querying GPU performance information**

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_QueryGpuInfo](../../../modules/gameperformance/document.md#ga93f67c2befdb52f4b59893a7a300f292) ([GamePerformance\_GpuInfo](../../../modules/gameperformance/document.md#gae85f740f82b3ca3f7ec9892d2f81a113) \*\*gpuInfo)

 | 

Queries GPU performance information.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyGpuInfo](../../../modules/gameperformance/document.md#ga249433eea6a463cb2401e7bbbbcd19dd) ([GamePerformance\_GpuInfo](../../../modules/gameperformance/document.md#gae85f740f82b3ca3f7ec9892d2f81a113) \*\*gpuInfo)

 | 

Destroys a [GamePerformance\_GpuInfo](../../../modules/gameperformance/document.md#gae85f740f82b3ca3f7ec9892d2f81a113) instance when it is no longer used.

 |
| 

**Functions for querying CPU performance information**

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_QueryCpuInfo](../../../modules/gameperformance/document.md#gad59832ffd2679db7b1fa8310f586531f) ([GamePerformance\_CpuInfo](../../../modules/gameperformance/document.md#ga5e0fa80aa26633c1b9d765340e4a262d) \*\*cpuInfo)

 | 

Queries CPU performance information.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyCpuInfo](../../../modules/gameperformance/document.md#ga6e76026d1a4c34c4bf983136e0a21734) ([GamePerformance\_CpuInfo](../../../modules/gameperformance/document.md#ga5e0fa80aa26633c1b9d765340e4a262d) \*\*cpuInfo)

 | 

Destroys a [GamePerformance\_CpuInfo](../../../modules/gameperformance/document.md#ga5e0fa80aa26633c1b9d765340e4a262d) instance when it is no longer used.

 |
| 

**Functions for parsing temperature information**

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DeviceInfo\_GetThermalInfo](../../../modules/gameperformance/document.md#ga233f517841cc5ab435a1e4fa8cd1d2de) ([GamePerformance\_DeviceInfo](../../../modules/gameperformance/document.md#ga530e1cf28aa5c4d0b355dc053ce27e80) \*deviceInfo, [GamePerformance\_ThermalInfo](../../../modules/gameperformance/document.md#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*\*thermalInfo)

 | 

Obtains the temperature information [GamePerformance\_ThermalInfo](../../../modules/gameperformance/document.md#ga6767ea8a1d76ed32db95dc0d3a265a8a) from the device performance information [GamePerformance\_DeviceInfo](../../../modules/gameperformance/document.md#ga530e1cf28aa5c4d0b355dc053ce27e80).

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ThermalInfo\_GetThermalMargin](../../../modules/gameperformance/document.md#gaf64ba82ad7342aeef688f5f515e86765) ([GamePerformance\_ThermalInfo](../../../modules/gameperformance/document.md#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*thermalInfo, int32\_t \*thermalMargin)

 | 

Obtains the temperature time margin from the temperature information [GamePerformance\_ThermalInfo](../../../modules/gameperformance/document.md#ga6767ea8a1d76ed32db95dc0d3a265a8a).

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ThermalInfo\_GetThermalTrend](../../../modules/gameperformance/document.md#ga4e0b7380232ea2120f017cf717d66f5f) ([GamePerformance\_ThermalInfo](../../../modules/gameperformance/document.md#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*thermalInfo, int32\_t \*thermalTrend)

 | 

Obtains the temperature trend from [GamePerformance\_ThermalInfo](../../../modules/gameperformance/document.md#ga6767ea8a1d76ed32db95dc0d3a265a8a).

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ThermalInfo\_GetThermalLevel](../../../modules/gameperformance/document.md#ga36713ebcb8a94fd99772965437c18b7f) ([GamePerformance\_ThermalInfo](../../../modules/gameperformance/document.md#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*thermalInfo, int32\_t \*thermalLevel)

 | 

Obtains the temperature level from [GamePerformance\_ThermalInfo](../../../modules/gameperformance/document.md#ga6767ea8a1d76ed32db95dc0d3a265a8a).

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ThermalInfo\_GetRecommendNormalizedCurrent](../../../modules/gameperformance/document.md#gaf0a4a9c0d97ecdc55f44bdbe4560b10b) ([GamePerformance\_ThermalInfo](../../../modules/gameperformance/document.md#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*thermalInfo, int32\_t \*recommendCurrent)

 | 

Obtains the recommended operating current from [GamePerformance\_ThermalInfo](../../../modules/gameperformance/document.md#ga6767ea8a1d76ed32db95dc0d3a265a8a). If the current operating current is higher than the recommended value, the temperature trend **thermalTrend** will be greater than 0, indicating a risk of device overheating.

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ThermalInfo\_GetNowNormalizedCurrent](../../../modules/gameperformance/document.md#gaa8968228efdefebe9ceb1aeb47ca2005) ([GamePerformance\_ThermalInfo](../../../modules/gameperformance/document.md#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*thermalInfo, int32\_t \*nowCurrent)

 | 

Obtains the current operating current from [GamePerformance\_ThermalInfo](../../../modules/gameperformance/document.md#ga6767ea8a1d76ed32db95dc0d3a265a8a).

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ThermalInfo\_GetRecommendMaxNormalizedCurrent](../../../modules/gameperformance/document.md#ga273f8d969801ef92a8b201b48b66d5dd) ([GamePerformance\_ThermalInfo](../../../modules/gameperformance/document.md#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*thermalInfo, int32\_t \*recommendMaxCurrent)

 | 

Obtains the recommended maximum operating current from [GamePerformance\_ThermalInfo](../../../modules/gameperformance/document.md#ga6767ea8a1d76ed32db95dc0d3a265a8a). If the current operating current is higher than this value, the device will immediately heat up.

 |
| 

**Functions for parsing GPU performance information**

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DeviceInfo\_GetGpuInfo](../../../modules/gameperformance/document.md#ga028805183830f3638fb9b122a934d30a) ([GamePerformance\_DeviceInfo](../../../modules/gameperformance/document.md#ga530e1cf28aa5c4d0b355dc053ce27e80) \*deviceInfo, [GamePerformance\_GpuInfo](../../../modules/gameperformance/document.md#gae85f740f82b3ca3f7ec9892d2f81a113) \*\*gpuInfo)

 | 

Obtains the GPU performance information [GamePerformance\_GpuInfo](../../../modules/gameperformance/document.md#gae85f740f82b3ca3f7ec9892d2f81a113) from the device performance information [GamePerformance\_DeviceInfo](../../../modules/gameperformance/document.md#ga530e1cf28aa5c4d0b355dc053ce27e80).

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_GpuInfo\_GetGpuLoadLevel](../../../modules/gameperformance/document.md#ga2542ab4c2a7a8ea411f5ca78236f3057) ([GamePerformance\_GpuInfo](../../../modules/gameperformance/document.md#gae85f740f82b3ca3f7ec9892d2f81a113) \*gpuInfo, int32\_t \*gpuLoadLevel)

 | 

Obtains the GPU load information from [GamePerformance\_GpuInfo](../../../modules/gameperformance/document.md#gae85f740f82b3ca3f7ec9892d2f81a113).

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_GpuInfo\_GetVertexLoadLevel](../../../modules/gameperformance/document.md#gab2c0f4d08ce347fc2ce57cd4f75a207d) ([GamePerformance\_GpuInfo](../../../modules/gameperformance/document.md#gae85f740f82b3ca3f7ec9892d2f81a113) \*gpuInfo, int32\_t \*vertexLoadLevel)

 | 

Obtains the GPU vertex processing load level from [GamePerformance\_GpuInfo](../../../modules/gameperformance/document.md#gae85f740f82b3ca3f7ec9892d2f81a113).

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_GpuInfo\_GetFragmentLoadLevel](../../../modules/gameperformance/document.md#ga9ed72dbe4214471b0c62888e220c535b) ([GamePerformance\_GpuInfo](../../../modules/gameperformance/document.md#gae85f740f82b3ca3f7ec9892d2f81a113) \*gpuInfo, int32\_t \*fragmentLoadLevel)

 | 

Obtains the GPU fragment processing load level from [GamePerformance\_GpuInfo](../../../modules/gameperformance/document.md#gae85f740f82b3ca3f7ec9892d2f81a113).

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_GpuInfo\_GetTextureLoadLevel](../../../modules/gameperformance/document.md#ga0b690f0f661dcc5b552e1c3b0a6c48b0) ([GamePerformance\_GpuInfo](../../../modules/gameperformance/document.md#gae85f740f82b3ca3f7ec9892d2f81a113) \*gpuInfo, int32\_t \*textureLoadLevel)

 | 

Obtains the GPU texture processing load level from [GamePerformance\_GpuInfo](../../../modules/gameperformance/document.md#gae85f740f82b3ca3f7ec9892d2f81a113).

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_GpuInfo\_GetBandwidthLoadLevel](../../../modules/gameperformance/document.md#ga798a410d53057a8735c342c41066e286) ([GamePerformance\_GpuInfo](../../../modules/gameperformance/document.md#gae85f740f82b3ca3f7ec9892d2f81a113) \*gpuInfo, int32\_t \*bandwidthLoadLevel)

 | 

Obtains the GPU bandwidth load level from [GamePerformance\_GpuInfo](../../../modules/gameperformance/document.md#gae85f740f82b3ca3f7ec9892d2f81a113).

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_GpuInfo\_GetCurrentFrequency](../../../modules/gameperformance/document.md#ga54d57643697d513fb1d2f94fa5d01633) ([GamePerformance\_GpuInfo](../../../modules/gameperformance/document.md#gae85f740f82b3ca3f7ec9892d2f81a113) \*gpuInfo, int32\_t \*currentFrequency)

 | 

Obtains the GPU frequency information from [GamePerformance\_GpuInfo](../../../modules/gameperformance/document.md#gae85f740f82b3ca3f7ec9892d2f81a113).

 |
| 

**Functions for parsing CPU performance information**

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DeviceInfo\_GetCpuInfo](../../../modules/gameperformance/document.md#ga2526a18580b2c5ad497017bf05adc4da) ([GamePerformance\_DeviceInfo](../../../modules/gameperformance/document.md#ga530e1cf28aa5c4d0b355dc053ce27e80) \*deviceInfo, [GamePerformance\_CpuInfo](../../../modules/gameperformance/document.md#ga5e0fa80aa26633c1b9d765340e4a262d) \*\*cpuInfo)

 | 

Obtains the CPU performance information [GamePerformance\_CpuInfo](../../../modules/gameperformance/document.md#ga5e0fa80aa26633c1b9d765340e4a262d) from the device performance information [GamePerformance\_DeviceInfo](../../../modules/gameperformance/document.md#ga530e1cf28aa5c4d0b355dc053ce27e80).

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_CpuInfo\_GetCpuLoadLevel](../../../modules/gameperformance/document.md#ga2f7d2cbc801dc60873bca2664f521ccb) ([GamePerformance\_CpuInfo](../../../modules/gameperformance/document.md#ga5e0fa80aa26633c1b9d765340e4a262d) \*cpuInfo, int32\_t \*cpuLoadLevel)

 | 

Obtains the overall CPU load level from [GamePerformance\_CpuInfo](../../../modules/gameperformance/document.md#ga5e0fa80aa26633c1b9d765340e4a262d).

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_CpuInfo\_GetSingleThreadLoadLevel](../../../modules/gameperformance/document.md#gac323aa2708efd9224133e61fb157a27f) ([GamePerformance\_CpuInfo](../../../modules/gameperformance/document.md#ga5e0fa80aa26633c1b9d765340e4a262d) \*cpuInfo, int32\_t \*singleThreadLoadLevel)

 | 

Obtains the overall load level of the heaviest thread in the game from [GamePerformance\_CpuInfo](../../../modules/gameperformance/document.md#ga5e0fa80aa26633c1b9d765340e4a262d).

 |
| 

**Functions related to device performance information (DeviceInfo)**

 |
| 

[GamePerformance\_ErrorCode](../../../modules/gameperformance/document.md#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyDeviceInfo](../../../modules/gameperformance/document.md#gaf8031fd101ee970aa0339aed14d4507e) ([GamePerformance\_DeviceInfo](../../../modules/gameperformance/document.md#ga530e1cf28aa5c4d0b355dc053ce27e80) \*\*deviceInfo)

 | 

Destroys a [GamePerformance\_DeviceInfo](../../../modules/gameperformance/document.md#ga530e1cf28aa5c4d0b355dc053ce27e80) instance when it is no longer used.

 |
