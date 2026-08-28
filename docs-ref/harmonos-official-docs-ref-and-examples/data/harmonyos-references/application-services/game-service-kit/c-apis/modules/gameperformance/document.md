# GamePerformance

#### Overview

This section provides the definition on the C APIs of the game scene perception module.

**System capability:** SystemCapability.GameService.GamePerformance

**Start version**: 5.0.2(14)

#### Summary

#### \[h2\]File

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[game\_performance.h](../../header-files-and-structs/header-files/game-performance-h/document.md)

 | 

Declares the basic concepts of the game scene perception module.

 |

#### \[h2\]Type Definitions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef struct [GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80) [GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80)

 | 

Defines device performance information.

 |
| 

typedef struct [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113)

 | 

Defines GPU performance information.

 |
| 

typedef struct [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d)

 | 

Defines CPU performance information.

 |
| 

typedef struct [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a)

 | 

Defines temperature information.

 |
| 

typedef struct [GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) [GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788)

 | 

Defines the parameters for querying temperature information.

 |
| 

typedef struct [GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) [GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411)

 | 

Defines initialization parameters.

 |
| 

typedef struct [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87)

 | 

Defines game package information.

 |
| 

typedef struct [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9)

 | 

Defines game configuration information.

 |
| 

typedef struct [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7)

 | 

Defines game scene information.

 |
| 

typedef struct [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097)

 | 

Defines game network information.

 |
| 

typedef struct [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842)

 | 

Defines game player information.

 |
| 

typedef enum [GamePerformance\_EngineType](#gab7f3d09e6dd4af1692872b6b5815af45) [GamePerformance\_EngineType](#ga449d5fa8c8ee0fbea9188fd345401462)

 | 

Defines game engine types.

 |
| 

typedef enum [GamePerformance\_GameType](#ga9c1b6f00c4769f13c510a7a871c7afd3) [GamePerformance\_GameType](#ga1e1370020b763cb4cce215d955ebb78d)

 | 

Defines game types.

 |
| 

typedef enum [GamePerformance\_PictureQualityLevel](#ga64fd3d566be9f8240d0f474d52c292dd) [GamePerformance\_PictureQualityLevel](#gab726f445d701d96ff647efa723ef993d)

 | 

Defines image quality levels.

 |
| 

typedef enum [GamePerformance\_SceneImportanceLevel](#gaf6bbf14a7010d4e99e6c758a718a08a6) [GamePerformance\_SceneImportanceLevel](#ga59c720e67f9586ae4f24223be1ae3dc5)

 | 

Defines importance levels of game scenes.

 |
| 

typedef enum [GamePerformance\_CpuLevel](#ga11ac456fd1b33d0b1f6220af5e5cd1ce) [GamePerformance\_CpuLevel](#ga4d30bee20aca3ea7082302ae7164a196)

 | 

Defines CPU levels.

 |
| 

typedef enum [GamePerformance\_GpuLevel](#ga48d14f66a8d484b497157458dd13a473) [GamePerformance\_GpuLevel](#ga12e1ee7ac06fc6bd25a87cce66d2a632)

 | 

Defines GPU levels.

 |
| 

typedef enum [GamePerformance\_DdrLevel](#gaec1b60b592a13ea85774a4d2ec8581bb) [GamePerformance\_DdrLevel](#ga57b549a68edbc9c84843040beb886389)

 | 

Defines DDR levels.

 |
| 

typedef enum [GamePerformance\_NetLoad](#ga517e25164876d3727c407c887943aee2) [GamePerformance\_NetLoad](#ga638c2b6f6d0dda3138e34869635b2dd4)

 | 

Defines game network load levels.

 |
| 

typedef enum [GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [GamePerformance\_ErrorCode](#gad952c8a450a72955d4dc24c43df7eee6)

 | 

Defines error codes.

 |
| 

typedef enum [GamePerformance\_DeviceInfoType](#ga3ebb81788405856534d8fb3cd6194ca4) [GamePerformance\_DeviceInfoType](#gac1d8c407b85cedf00dc6f6cf1f3ac202)

 | 

Defines device performance information types.

 |
| 

typedef void(\*[GamePerformance\_ThermalLevelChangedCallback](#ga94e7e85a3f0ad0b495b2c525a15ebc8e)) ([GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80) \*deviceInfo, void \*userData)

 | 

Callback used in [HMS\_GamePerformance\_RegisterThermalLevelChangedCallback](#gaa73a9464dbe4a973e7aed559835adbc6). This callback will be triggered once when the temperature level changes to a level below 3, and will be triggered every 10 seconds when the temperature level changes to level 3 or higher.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[GamePerformance\_EngineType](#gab7f3d09e6dd4af1692872b6b5815af45) {

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

[GamePerformance\_GameType](#ga9c1b6f00c4769f13c510a7a871c7afd3) {

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

[GamePerformance\_PictureQualityLevel](#ga64fd3d566be9f8240d0f474d52c292dd) {

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

[GamePerformance\_SceneImportanceLevel](#gaf6bbf14a7010d4e99e6c758a718a08a6) {

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

[GamePerformance\_CpuLevel](#ga11ac456fd1b33d0b1f6220af5e5cd1ce) {

GAME\_PERFORMANCE\_CPU\_LEVEL\_LOW = 1,

GAME\_PERFORMANCE\_CPU\_LEVEL\_MIDDLE = 2,

GAME\_PERFORMANCE\_CPU\_LEVEL\_HIGH = 3

}

 | 

Describes CPU levels.

 |
| 

[GamePerformance\_GpuLevel](#ga48d14f66a8d484b497157458dd13a473) {

GAME\_PERFORMANCE\_GPU\_LEVEL\_LOW = 1,

GAME\_PERFORMANCE\_GPU\_LEVEL\_MIDDLE = 2,

GAME\_PERFORMANCE\_GPU\_LEVEL\_HIGH = 3

}

 | 

Describes GPU levels.

 |
| 

[GamePerformance\_DdrLevel](#gaec1b60b592a13ea85774a4d2ec8581bb) {

GAME\_PERFORMANCE\_DDR\_LEVEL\_LOW = 1,

GAME\_PERFORMANCE\_DDR\_LEVEL\_MIDDLE = 2,

GAME\_PERFORMANCE\_DDR\_LEVEL\_HIGH = 3

}

 | 

Describes DDR levels.

 |
| 

[GamePerformance\_NetLoad](#ga517e25164876d3727c407c887943aee2) {

GAME\_PERFORMANCE\_NET\_LOAD\_LIGHT = 1,

GAME\_PERFORMANCE\_NET\_LOAD\_MODERATE = 2,

GAME\_PERFORMANCE\_NET\_LOAD\_HEAVY = 3

}

 | 

Describes network load levels.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) {

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

[GamePerformance\_DeviceInfoType](#ga3ebb81788405856534d8fb3cd6194ca4) {

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

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_CreateInitParameters](#ga82a96cb32e0980c6650b262b268158a2) ([GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) \*\*initParameters)

 | 

Creates a [GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) instance, which will be used in the [HMS\_GamePerformance\_Init](#ga1045d9d8f4e7972b44ff95571afca8f9) method.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyInitParameters](#gaef8a6ecaefc0f7ca4b8e2c88a84f5db0) ([GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) \*\*initParameters)

 | 

Destroys a [GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) instance when it is no longer used.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_InitParameters\_SetBundleName](#ga35962b201b42b841202d0986e7e80250) ([GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) \*initParameters, const char \*bundleName)

 | 

Sets the package name for the [GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_InitParameters\_SetAppVersion](#gab19d551d38ea087012ba205f975ec5ed) ([GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) \*initParameters, const char \*appVersion)

 | 

Sets the version number for the [GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_Init](#ga1045d9d8f4e7972b44ff95571afca8f9) ([GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) \*initParameters)

 | 

Initializes the game scene perception module.

 |
| 

**Functions related to game package information (PackageInfo)**

Before calling **HMS\_GamePerformance\_UpdatePackageInfo**, ensure that **bundleName** and **appVersion** have been set.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_CreatePackageInfo](#ga6b54d67769794ce6833cbecf7a0fb9ab) ([GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) \*\*packageInfo)

 | 

Creates a [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance, which will be used in the [HMS\_GamePerformance\_UpdatePackageInfo](#ga317ba7027076ce06ae73a6188bc3b129) method.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyPackageInfo](#ga2019dcc34f428ae80868c0af612237c3) ([GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) \*\*packageInfo)

 | 

Destroys a [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance when it is no longer used.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_PackageInfo\_SetBundleName](#ga623a88c7ea2c5eb022dd8a784e8b6661) ([GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo, const char \*bundleName)

 | 

Sets the package name for the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_PackageInfo\_SetAppVersion](#ga0afa327f6afed7acfc998c3f79bfeb76) ([GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo, const char \*appVersion)

 | 

Sets the version number for the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_PackageInfo\_SetEngineType](#ga1436072d310ec40ddc2a85d6bafd0ee2) ([GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo, const [GamePerformance\_EngineType](#gab7f3d09e6dd4af1692872b6b5815af45) engineType)

 | 

Sets the engine type for the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_PackageInfo\_SetEngineVersion](#ga73b762ef177488deecf97f04395f70d5) ([GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo, const char \*engineVersion)

 | 

Sets the engine version number for the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_PackageInfo\_SetGameType](#gac5f6695702063b61b4f7cc885129dfe2) ([GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo, const [GamePerformance\_GameType](#ga9c1b6f00c4769f13c510a7a871c7afd3) gameType)

 | 

Sets the game type for the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_PackageInfo\_SetVulkanSupported](#gadfbc32fbe65b9763d2cb393af8485dbb) ([GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo, const bool vulkanSupported)

 | 

Sets whether the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance supports Vulkan.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UpdatePackageInfo](#ga317ba7027076ce06ae73a6188bc3b129) ([GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo)

 | 

Updates game package information.

 |
| 

**Functions related to game configuration information (ConfigInfo)**

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_CreateConfigInfo](#ga2124abdf7dfed3b2c37242228a442128) ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*\*configInfo)

 | 

Creates a [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance, which will be used in the [HMS\_GamePerformance\_UpdateConfigInfo](#ga6fe77ea4f43939333c7c3b07e1204448) method.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyConfigInfo](#ga8328d927012e4b868175ad3c192a947b) ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*\*configInfo)

 | 

Destroys a [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance when it is no longer used.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetMaxPictureQualityLevel](#ga5f85d32e8f74f4ab008abd49f1109c46) ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const [GamePerformance\_PictureQualityLevel](#ga64fd3d566be9f8240d0f474d52c292dd) maxPictureQualityLevel)

 | 

Sets the maximum image quality level for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetCurrentPictureQualityLevel](#gad44e9925a145ab621f4d8ff348de4034) ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const [GamePerformance\_PictureQualityLevel](#ga64fd3d566be9f8240d0f474d52c292dd) currentPictureQualityLevel)

 | 

Sets the current image quality level for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetMaxFrameRate](#ga6665850e826d430bba7525351ef2df70) ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const int64\_t maxFrameRate)

 | 

Sets the maximum frame rate for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetCurrentFrameRate](#ga89845a005ea8f0a5069ef2563f55936e) ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const int64\_t currentFrameRate)

 | 

Sets the current frame rate for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetMaxResolution](#gad34b019dfa3a973512c7157dcba92ad1) ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const char \*maxResolution)

 | 

Sets the maximum resolution for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetCurrentResolution](#ga9bee7c2052d81a0dd6c6f93ce57ddc1f) ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const char \*currentResolution)

 | 

Sets the current resolution for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetAntiAliasingEnabled](#ga5657a6e00ba9e08803a201a8d0c1cecd) ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const bool antiAliasingEnabled)

 | 

Sets whether to enable anti-aliasing for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetShadowEnabled](#ga1beebb2eabcea33e37de8015ac29ef9c) ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const bool shadowEnabled)

 | 

Sets whether to enable the shadow effect for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetMultithreadingEnabled](#gab69ed9d7e95fe067d618514a6472c2b3) ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const bool multithreadingEnabled)

 | 

Enables multi-threading for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetParticleEnabled](#ga808ed7b13bc8ed4fd97267a65c8f4469) ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const bool particleEnabled)

 | 

Sets the particle effect for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ConfigInfo\_SetHdModeEnabled](#ga5ef09e013a67def087e5f6b5442ff0b0) ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const bool hdModeEnabled)

 | 

Enables the HD mode for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UpdateConfigInfo](#ga6fe77ea4f43939333c7c3b07e1204448) ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo)

 | 

Updates game configuration information.

 |
| 

**Functions related to game scene information (SceneInfo)**

Before calling **HMS\_GamePerformance\_UpdateSceneInfo**, ensure that **sceneID** and **importanceLevel** have been set.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_CreateSceneInfo](#ga20ba3d28237372a1f44652f50d0850c4) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*\*sceneInfo)

 | 

Creates a [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance, which will be used in the [HMS\_GamePerformance\_UpdateSceneInfo](#gad9504bae5e5b570e55bdf7f84a7a05bf) method.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroySceneInfo](#gadc5f2c4b6b7258830736fb194d06bdd8) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*\*sceneInfo)

 | 

Destroys a [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance when it is no longer used.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetSceneID](#gaaf792159ff58c372c80106a3e050e7bc) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t sceneID)

 | 

Sets the scene ID for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetDescription](#ga32193247c7f59a29920b5ec084a89a6c) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const char \*description)

 | 

Sets the scene description for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetSubSceneID](#gaf66ab2b453b1f9e5df8173f839490540) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const char \*subSceneID)

 | 

Sets the sub-scene ID for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetSubDescription](#ga1d6ed7ffa24f5002ffbd799877467056) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const char \*subDescription)

 | 

Sets the sub-scene description for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetImportanceLevel](#ga5a7748133e83c9aebaa439e0d97fe742) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const [GamePerformance\_SceneImportanceLevel](#gaf6bbf14a7010d4e99e6c758a718a08a6) importanceLevel)

 | 

Sets the scene importance level for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetSceneFrequency](#ga3743a3ad2a364d6b039b2dbc1213f04a) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t sceneFrequency)

 | 

Sets the number of times a scene appears in a round of the game for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetSceneTime](#gaa7d8eab6076c00e220da385a51016847) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t sceneTime)

 | 

Sets the scene duration for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetRecommendedCpuLevel](#ga423176ac542a8058fd4bdc31e19e49fb) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const [GamePerformance\_CpuLevel](#ga11ac456fd1b33d0b1f6220af5e5cd1ce) recommendedCpuLevel)

 | 

Sets the recommended CPU level for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetRecommendedGpuLevel](#gaf7bb4de842d1045434417997abb12365) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const [GamePerformance\_GpuLevel](#ga48d14f66a8d484b497157458dd13a473) recommendedGpuLevel)

 | 

Sets the recommended GPU level for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetRecommendedDdrLevel](#ga919d39c5eaa6e8e0a1f88c42f4d55264) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const [GamePerformance\_DdrLevel](#gaec1b60b592a13ea85774a4d2ec8581bb) recommendedDdrLevel)

 | 

Sets the recommended DDR level for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetMaxFrameRate](#gad672cb46e420b0cee29da39d4009a7c9) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t maxFrameRate)

 | 

Sets the maximum frame rate of a scene for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetCurrentFrameRate](#ga70f297a098b963e0216cf1fc0b2d3075) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t currentFrameRate)

 | 

Sets the frame rate of the current scene for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetKeyThread](#gaa41913e398bd82a136497889c4c40435) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const char \*keyThread)

 | 

Sets the key thread for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetDrawCallCount](#ga8504590e1f52eba1ab01f9e29d5344e3) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t drawCallCount)

 | 

Sets the average number of draw calls per frame for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetVertexCount](#ga5a10d96f46fbc5353d4c077970b5b3b7) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t vertexCount)

 | 

Sets the average number of model vertices per frame for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetTriangleCount](#ga98ba98ee175a97bc9b40dfb4576194ea) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t triangleCount)

 | 

Sets the average number of model triangles per frame for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetShaderCount](#gacc04bf99a463910cfdf3e96e0d1f7168) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t shaderCount)

 | 

Sets the average number of shaders per frame for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetTextureCount](#gac374255a0c99f721ff7227e2c9a599d3) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t textureCount)

 | 

Sets the average number of textures per frame for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetMeshCount](#ga00ab8ad16a928499daf8359fed8343b8) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t meshCount)

 | 

Sets the average number of meshes per frame for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetChannelCount](#ga4d6f34ef3b653c79c110c0fd35a5cca6) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t channelCount)

 | 

Sets the number of channels rendered per frame for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_SceneInfo\_SetParticipantCount](#ga3a3eaf50d555e6539c0f61543bc7898e) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t participantCount)

 | 

Sets the number of players on the same screen in a scene for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UpdateSceneInfo](#gad9504bae5e5b570e55bdf7f84a7a05bf) ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo)

 | 

Updates game scene information.

 |
| 

**Functions related to game network information (NetInfo)**

Before calling **HMS\_GamePerformance\_UpdateNetInfo**, ensure that **totalLatency** has been set.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_CreateNetInfo](#ga7c2084205b1c6402f6c7697aa93ea08e) ([GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) \*\*netInfo)

 | 

Creates a [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance, which will be used in the [HMS\_GamePerformance\_UpdateNetInfo](#ga29ff530f9f37560359fdd0d28ba6275b) method.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyNetInfo](#ga7e97470d2e305c3777438ba7cc524cac) ([GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) \*\*netInfo)

 | 

Destroys a [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance when it is no longer used.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_NetInfo\_SetTotalLatency](#gaf2b2757c599992d8eb90767513abef59) ([GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) \*netInfo, const int64\_t total)

 | 

Sets the total network latency for the [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_NetInfo\_SetUplinkLatency](#gaa0876f5a71061d68f084d40d2b1039e2) ([GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) \*netInfo, const int64\_t up)

 | 

Sets the uplink network latency for the [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_NetInfo\_SetDownlinkLatency](#ga1edfa8aa64d9773b3b768e1653690479) ([GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) \*netInfo, const int64\_t down)

 | 

Sets the downlink network latency for the [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_NetInfo\_SetServerLatency](#ga5920ded727e6ca21760b82d5586064b9) ([GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) \*netInfo, const int64\_t server)

 | 

Sets the server network latency for the [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_NetInfo\_SetNetLoad](#ga74aab7c053e2bf62aacef57ea223aa28) ([GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) \*netInfo, const [GamePerformance\_NetLoad](#ga517e25164876d3727c407c887943aee2) netLoad)

 | 

Sets the network load for the [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UpdateNetInfo](#ga29ff530f9f37560359fdd0d28ba6275b) ([GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) \*netInfo)

 | 

Updates game network information.

 |
| 

**Functions related to game player information (PlayerInfo)**

**gamePlayerId**, **teamPlayerId**, and **thirdOpenId** cannot be left empty at the same time.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_CreatePlayerInfo](#ga97925740bdc7df3aefbd482304294208) ([GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) \*\*playerInfo)

 | 

Creates a [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) instance, which will be used in the [HMS\_GamePerformance\_UpdatePlayerInfo](#ga71c7be26b9531af9bcd807e3255c4e6f) method.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyPlayerInfo](#ga42254ab6d5c9a8ec61f512d1e2903256) ([GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) \*\*playerInfo)

 | 

Destroys a [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) instance when it is no longer used.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_PlayerInfo\_SetGamePlayerId](#gaccabd2811fc0e84e95a50219b34f1814) ([GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) \*playerInfo, const char \*gamePlayerId)

 | 

Sets the player ID for the [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_PlayerInfo\_SetTeamPlayerId](#gaa5068c2f80ffc184cbebb03f22ece595) ([GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) \*playerInfo, const char \*teamPlayerId)

 | 

Sets the team player ID for the [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_PlayerInfo\_SetThirdOpenId](#ga875a2f1dad9091927ada365f6e9b6d5d) ([GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) \*playerInfo, const char \*thirdOpenId)

 | 

Sets the official game account for the [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UpdatePlayerInfo](#ga71c7be26b9531af9bcd807e3255c4e6f) ([GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) \*playerInfo)

 | 

Updates game player information.

 |
| 

**Functions related to subscription**

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_RegisterThermalLevelChangedCallback](#gaa73a9464dbe4a973e7aed559835adbc6) ([GamePerformance\_DeviceInfoType](#ga3ebb81788405856534d8fb3cd6194ca4) \*types\[\], size\_t size, [GamePerformance\_ThermalLevelChangedCallback](#ga94e7e85a3f0ad0b495b2c525a15ebc8e) callback, void \*userData)

 | 

Subscribes to temperature changes by registering the callback for temperature changes. When the trigger point is reached, this callback will be called.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UnregisterThermalLevelChangedCallback](#ga306734f0bee9af7697b5fbfa19bafec0) ([GamePerformance\_ThermalLevelChangedCallback](#ga94e7e85a3f0ad0b495b2c525a15ebc8e) callback)

 | 

Deregisters specified callbacks for temperature changes.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UnregisterAllThermalLevelChangedCallbacks](#ga0f2cf9152a9421d00bb0c03683b3f57d) (void)

 | 

Deregisters all callbacks for temperature changes.

 |
| 

**Functions for querying temperature information**

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_CreateThermalInfoQueryParameters](#gad3e60ec2d47a5068206bc3e1f217acc2) ([GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) \*\*parameters)

 | 

Creates a [GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) instance, which will be used in the [HMS\_GamePerformance\_QueryThermalInfo](#gab7cb47e0dc3cce1169a8104827f7edb7) method.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyThermalInfoQueryParameters](#ga6b9314f647ed520b11b9dfa4fbc40351) ([GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) \*\*parameters)

 | 

Destroys a [GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) instance when it is no longer used.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ThermalInfoQueryParameters\_SetNeedsPrediction](#ga7ce2e82b511a0158d93d2ee147536ee7) ([GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) \*parameters, const bool needsPrediction)

 | 

Sets whether predicting temperature trend is required for the [GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ThermalInfoQueryParameters\_SetTargetThermalLevel](#ga5cb94581ca23d465933e9316fdb0605d) ([GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) \*parameters, const int32\_t targetThermalLevel)

 | 

Sets the target temperature level for predicting the temperature trend for the [GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) instance.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_QueryThermalInfo](#gab7cb47e0dc3cce1169a8104827f7edb7) ([GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) \*parameters, [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*\*thermalInfo)

 | 

Queries temperature information.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyThermalInfo](#gacc640a4e15fe9cab1f8bccb652d77e59) ([GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*\*thermalInfo)

 | 

Destroys a [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) instance when it is no longer used.

 |
| 

**Functions for querying GPU performance information**

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_QueryGpuInfo](#ga93f67c2befdb52f4b59893a7a300f292) ([GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) \*\*gpuInfo)

 | 

Queries GPU performance information.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyGpuInfo](#ga249433eea6a463cb2401e7bbbbcd19dd) ([GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) \*\*gpuInfo)

 | 

Destroys a [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) instance when it is no longer used.

 |
| 

**Functions for querying CPU performance information**

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_QueryCpuInfo](#gad59832ffd2679db7b1fa8310f586531f) ([GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) \*\*cpuInfo)

 | 

Queries CPU performance information.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyCpuInfo](#ga6e76026d1a4c34c4bf983136e0a21734) ([GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) \*\*cpuInfo)

 | 

Destroys a [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) instance when it is no longer used.

 |
| 

**Functions for parsing temperature information**

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DeviceInfo\_GetThermalInfo](#ga233f517841cc5ab435a1e4fa8cd1d2de) ([GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80) \*deviceInfo, [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*\*thermalInfo)

 | 

Obtains the temperature information [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) from the device performance information [GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80).

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ThermalInfo\_GetThermalMargin](#gaf64ba82ad7342aeef688f5f515e86765) ([GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*thermalInfo, int32\_t \*thermalMargin)

 | 

Obtains the temperature time margin from the temperature information [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a).

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ThermalInfo\_GetThermalTrend](#ga4e0b7380232ea2120f017cf717d66f5f) ([GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*thermalInfo, int32\_t \*thermalTrend)

 | 

Obtains the temperature trend from [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a).

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ThermalInfo\_GetThermalLevel](#ga36713ebcb8a94fd99772965437c18b7f) ([GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*thermalInfo, int32\_t \*thermalLevel)

 | 

Obtains the temperature level from [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a).

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ThermalInfo\_GetRecommendNormalizedCurrent](#gaf0a4a9c0d97ecdc55f44bdbe4560b10b) ([GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*thermalInfo, int32\_t \*recommendCurrent)

 | 

Obtains the recommended operating current from [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a). If the current operating current is higher than the recommended value, the temperature trend **thermalTrend** will be greater than 0, indicating a risk of device overheating.

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ThermalInfo\_GetNowNormalizedCurrent](#gaa8968228efdefebe9ceb1aeb47ca2005) ([GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*thermalInfo, int32\_t \*nowCurrent)

 | 

Obtains the current operating current from [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a).

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_ThermalInfo\_GetRecommendMaxNormalizedCurrent](#ga273f8d969801ef92a8b201b48b66d5dd) ([GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*thermalInfo, int32\_t \*recommendMaxCurrent)

 | 

Obtains the recommended maximum operating current from [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a). If the current operating current is higher than this value, the device will immediately heat up.

 |
| 

**Functions for parsing GPU performance information**

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DeviceInfo\_GetGpuInfo](#ga028805183830f3638fb9b122a934d30a) ([GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80) \*deviceInfo, [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) \*\*gpuInfo)

 | 

Obtains the GPU performance information [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) from the device performance information [GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80).

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_GpuInfo\_GetGpuLoadLevel](#ga2542ab4c2a7a8ea411f5ca78236f3057) ([GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) \*gpuInfo, int32\_t \*gpuLoadLevel)

 | 

Obtains the GPU load information from [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113).

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_GpuInfo\_GetVertexLoadLevel](#gab2c0f4d08ce347fc2ce57cd4f75a207d) ([GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) \*gpuInfo, int32\_t \*vertexLoadLevel)

 | 

Obtains the GPU vertex processing load level from [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113).

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_GpuInfo\_GetFragmentLoadLevel](#ga9ed72dbe4214471b0c62888e220c535b) ([GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) \*gpuInfo, int32\_t \*fragmentLoadLevel)

 | 

Obtains the GPU fragment processing load level from [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113).

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_GpuInfo\_GetTextureLoadLevel](#ga0b690f0f661dcc5b552e1c3b0a6c48b0) ([GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) \*gpuInfo, int32\_t \*textureLoadLevel)

 | 

Obtains the GPU texture processing load level from [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113).

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_GpuInfo\_GetBandwidthLoadLevel](#ga798a410d53057a8735c342c41066e286) ([GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) \*gpuInfo, int32\_t \*bandwidthLoadLevel)

 | 

Obtains the GPU bandwidth load level from [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113).

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_GpuInfo\_GetCurrentFrequency](#ga54d57643697d513fb1d2f94fa5d01633) ([GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) \*gpuInfo, int32\_t \*currentFrequency)

 | 

Obtains the GPU frequency information from [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113).

 |
| 

**Functions for parsing CPU performance information**

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DeviceInfo\_GetCpuInfo](#ga2526a18580b2c5ad497017bf05adc4da) ([GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80) \*deviceInfo, [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) \*\*cpuInfo)

 | 

Obtains the CPU performance information [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) from the device performance information [GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80).

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_CpuInfo\_GetCpuLoadLevel](#ga2f7d2cbc801dc60873bca2664f521ccb) ([GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) \*cpuInfo, int32\_t \*cpuLoadLevel)

 | 

Obtains the overall CPU load level from [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d).

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_CpuInfo\_GetSingleThreadLoadLevel](#gac323aa2708efd9224133e61fb157a27f) ([GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) \*cpuInfo, int32\_t \*singleThreadLoadLevel)

 | 

Obtains the overall load level of the heaviest thread in the game from [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d).

 |
| 

**Functions related to device performance information (DeviceInfo)**

 |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_DestroyDeviceInfo](#gaf8031fd101ee970aa0339aed14d4507e) ([GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80) \*\*deviceInfo)

 | 

Destroys a [GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80) instance when it is no longer used.

 |

#### Type Definition Description

#### \[h2\]GamePerformance\_ConfigInfo

typedef struct [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9)

**Description**:

Defines game configuration information.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_CpuInfo

typedef struct [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d)

**Description**:

Defines CPU performance information.

**Start version**: 6.0.2(22)

#### \[h2\]GamePerformance\_CpuLevel

typedef enum [GamePerformance\_CpuLevel](#ga11ac456fd1b33d0b1f6220af5e5cd1ce) [GamePerformance\_CpuLevel](#ga11ac456fd1b33d0b1f6220af5e5cd1ce)

**Description**:

Defines CPU levels.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_DdrLevel

typedef enum [GamePerformance\_DdrLevel](#gaec1b60b592a13ea85774a4d2ec8581bb) [GamePerformance\_DdrLevel](#gaec1b60b592a13ea85774a4d2ec8581bb)

**Description**:

Defines DDR levels.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_DeviceInfo

typedef struct [GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80) [GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80)

**Description**:

Defines device performance information.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_DeviceInfoType

typedef enum [GamePerformance\_DeviceInfoType](#ga3ebb81788405856534d8fb3cd6194ca4) [GamePerformance\_DeviceInfoType](#ga3ebb81788405856534d8fb3cd6194ca4)

**Description**:

Defines device performance information types.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_EngineType

typedef enum [GamePerformance\_EngineType](#gab7f3d09e6dd4af1692872b6b5815af45) [GamePerformance\_EngineType](#gab7f3d09e6dd4af1692872b6b5815af45)

**Description**:

Defines game engine types.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_ErrorCode

typedef enum [GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) [GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

**Description**:

Defines error codes.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_GameType

typedef enum [GamePerformance\_GameType](#ga9c1b6f00c4769f13c510a7a871c7afd3) [GamePerformance\_GameType](#ga9c1b6f00c4769f13c510a7a871c7afd3)

**Description**:

Defines game types.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_GpuInfo

typedef struct [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113)

**Description**:

Defines GPU performance information.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_GpuLevel

typedef enum [GamePerformance\_GpuLevel](#ga48d14f66a8d484b497157458dd13a473) [GamePerformance\_GpuLevel](#ga48d14f66a8d484b497157458dd13a473)

**Description**:

Defines GPU levels.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_InitParameters

typedef struct [GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) [GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411)

**Description**:

Defines initialization parameters.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_NetInfo

typedef struct [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097)

**Description**:

Defines game network information.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_NetLoad

typedef enum [GamePerformance\_NetLoad](#ga517e25164876d3727c407c887943aee2) [GamePerformance\_NetLoad](#ga517e25164876d3727c407c887943aee2)

**Description**:

Defines game network load levels.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_PackageInfo

typedef struct [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87)

**Description**:

Defines package information.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_PictureQualityLevel

typedef enum [GamePerformance\_PictureQualityLevel](#ga64fd3d566be9f8240d0f474d52c292dd) [GamePerformance\_PictureQualityLevel](#ga64fd3d566be9f8240d0f474d52c292dd)

**Description**:

Defines image quality levels.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_PlayerInfo

typedef struct [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842)

**Description**:

Defines game player information.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_SceneImportanceLevel

typedef enum [GamePerformance\_SceneImportanceLevel](#gaf6bbf14a7010d4e99e6c758a718a08a6) [GamePerformance\_SceneImportanceLevel](#gaf6bbf14a7010d4e99e6c758a718a08a6)

**Description**:

Defines importance levels of game scenes.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_SceneInfo

typedef struct [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7)

**Description**:

Defines game scene information.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_ThermalInfo

typedef struct [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a)

**Description**:

Defines temperature information.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_ThermalInfoQueryParameters

typedef struct [GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) [GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788)

**Description**:

Defines the parameters for querying temperature information.

**Start version**: 5.0.2(14)

#### \[h2\]GamePerformance\_ThermalLevelChangedCallback

typedef void(\*GamePerformance\_ThermalLevelChangedCallback) ([GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80) \*deviceInfo, void \*userData)

**Description**:

Callback used in [HMS\_GamePerformance\_RegisterThermalLevelChangedCallback](#gaa73a9464dbe4a973e7aed559835adbc6). This callback will be triggered once when the temperature level changes to a level below 3, and will be triggered every 10 seconds when the temperature level changes to level 3 or higher.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

deviceInfo

 | 

Device details [GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80).

 |
| 

userData

 | 

User-specified data.

 |

#### Enumeration Description

#### \[h2\]GamePerformance\_CpuLevel

enum [GamePerformance\_CpuLevel](#ga11ac456fd1b33d0b1f6220af5e5cd1ce)

**Description**:

Defines CPU levels.

**Start version**: 5.0.2(14)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

GAME\_PERFORMANCE\_CPU\_LEVEL\_LOW

 | 

Low.

 |
| 

GAME\_PERFORMANCE\_CPU\_LEVEL\_MIDDLE

 | 

Medium.

 |
| 

GAME\_PERFORMANCE\_CPU\_LEVEL\_HIGH

 | 

High.

 |

#### \[h2\]GamePerformance\_DdrLevel

enum [GamePerformance\_DdrLevel](#gaec1b60b592a13ea85774a4d2ec8581bb)

**Description**:

Defines DDR levels.

**Start version**: 5.0.2(14)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

GAME\_PERFORMANCE\_DDR\_LEVEL\_LOW

 | 

Low.

 |
| 

GAME\_PERFORMANCE\_DDR\_LEVEL\_MIDDLE

 | 

Medium.

 |
| 

GAME\_PERFORMANCE\_DDR\_LEVEL\_HIGH

 | 

High.

 |

#### \[h2\]GamePerformance\_DeviceInfoType

enum [GamePerformance\_DeviceInfoType](#ga3ebb81788405856534d8fb3cd6194ca4)

**Description**:

Defines the device performance information types returned by callbacks.

**Start version**: 5.0.2(14)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

GAME\_PERFORMANCE\_DEVICEINFO\_TYPE\_THERMAL

 | 

Temperature information.

 |
| 

GAME\_PERFORMANCE\_DEVICEINFO\_TYPE\_GPU

 | 

GPU performance information.

 |
| 

GAME\_PERFORMANCE\_DEVICEINFO\_TYPE\_CPU

 | 

CPU performance information.

**Start version**: 6.0.2(22)

 |

#### \[h2\]GamePerformance\_EngineType

enum [GamePerformance\_EngineType](#gab7f3d09e6dd4af1692872b6b5815af45)

**Description**:

Defines game engine types.

**Start version**: 5.0.2(14)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

GAME\_PERFORMANCE\_ENGINE\_TYPE\_UNITY

 | 

UNITY.

 |
| 

GAME\_PERFORMANCE\_ENGINE\_TYPE\_UNREAL

 | 

UNREAL.

 |
| 

GAME\_PERFORMANCE\_ENGINE\_TYPE\_MESSIAH

 | 

MESSIAH.

 |
| 

GAME\_PERFORMANCE\_ENGINE\_TYPE\_COCOS

 | 

COCOS.

 |
| 

GAME\_PERFORMANCE\_ENGINE\_TYPE\_OTHERS

 | 

Other engine types.

 |

#### \[h2\]GamePerformance\_ErrorCode

enum [GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

**Description**:

Defines error codes.

**Start version**: 5.0.2(14)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

GAME\_PERFORMANCE\_SUCCESS

 | 

Success.

 |
| 

GAME\_PERFORMANCE\_PARAM\_INVALID

 | 

Invalid parameter.

 |
| 

GAME\_PERFORMANCE\_INTERNAL\_ERROR

 | 

Internal system error.

 |
| 

GAME\_PERFORMANCE\_AUTH\_FAILED

 | 

Authentication failure.

 |
| 

GAME\_PERFORMANCE\_INVALID\_REQUEST

 | 

Invalid request.

 |
| 

GAME\_PERFORMANCE\_PARAM\_ERROR

 | 

Invalid parameter.

**Start version**: 6.0.2(22)

 |

#### \[h2\]GamePerformance\_GameType

enum [GamePerformance\_GameType](#ga9c1b6f00c4769f13c510a7a871c7afd3)

**Description**:

Defines game types.

**Start version**: 5.0.2(14)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

GAME\_PERFORMANCE\_GAME\_TYPE\_MOBA

 | 

Multiplayer online battle arena (MOBA).

 |
| 

GAME\_PERFORMANCE\_GAME\_TYPE\_RPG

 | 

Role-playing game (RPG).

 |
| 

GAME\_PERFORMANCE\_GAME\_TYPE\_FPS

 | 

First-person shooter (FPS).

 |
| 

GAME\_PERFORMANCE\_GAME\_TYPE\_FTG

 | 

Fight technology game (FTG).

 |
| 

GAME\_PERFORMANCE\_GAME\_TYPE\_RAC

 | 

Racing game (RAC).

 |
| 

GAME\_PERFORMANCE\_GAME\_TYPE\_OTHERS

 | 

Other game types.

 |

#### \[h2\]GamePerformance\_GpuLevel

enum [GamePerformance\_GpuLevel](#ga48d14f66a8d484b497157458dd13a473)

**Description**:

Defines GPU levels.

**Start version**: 5.0.2(14)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

GAME\_PERFORMANCE\_GPU\_LEVEL\_LOW

 | 

Low.

 |
| 

GAME\_PERFORMANCE\_GPU\_LEVEL\_MIDDLE

 | 

Medium.

 |
| 

GAME\_PERFORMANCE\_GPU\_LEVEL\_HIGH

 | 

High.

 |

#### \[h2\]GamePerformance\_NetLoad

enum [GamePerformance\_NetLoad](#ga517e25164876d3727c407c887943aee2)

**Description**:

Defines game network load levels.

**Start version**: 5.0.2(14)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

GAME\_PERFORMANCE\_NET\_LOAD\_LIGHT

 | 

Light load.

 |
| 

GAME\_PERFORMANCE\_NET\_LOAD\_MODERATE

 | 

Medium load.

 |
| 

GAME\_PERFORMANCE\_NET\_LOAD\_HEAVY

 | 

Heavy load.

 |

#### \[h2\]GamePerformance\_PictureQualityLevel

enum [GamePerformance\_PictureQualityLevel](#ga64fd3d566be9f8240d0f474d52c292dd)

**Description**:

Defines image quality levels.

**Start version**: 5.0.2(14)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

GAME\_PERFORMANCE\_PQL\_SMOOTH

 | 

Smooth.

 |
| 

GAME\_PERFORMANCE\_PQL\_BALANCED

 | 

Balanced.

 |
| 

GAME\_PERFORMANCE\_PQL\_HD

 | 

HD.

 |
| 

GAME\_PERFORMANCE\_PQL\_HDR

 | 

HDR.

 |
| 

GAME\_PERFORMANCE\_PQL\_UHD

 | 

UHD.

 |

#### \[h2\]GamePerformance\_SceneImportanceLevel

enum [GamePerformance\_SceneImportanceLevel](#gaf6bbf14a7010d4e99e6c758a718a08a6)

**Description**:

Defines the importance level of a game scene. The value ranges from 1 to 5. A larger value indicates a higher level of importance.

**Start version**: 5.0.2(14)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

GAME\_PERFORMANCE\_SIL\_LEVEL1

 | 

Level 1.

 |
| 

GAME\_PERFORMANCE\_SIL\_LEVEL2

 | 

Level 2.

 |
| 

GAME\_PERFORMANCE\_SIL\_LEVEL3

 | 

Level 3.

 |
| 

GAME\_PERFORMANCE\_SIL\_LEVEL4

 | 

Level 4.

 |
| 

GAME\_PERFORMANCE\_SIL\_LEVEL5

 | 

Level 5.

 |

#### Function Description

#### \[h2\]HMS\_GamePerformance\_ConfigInfo\_SetAntiAliasingEnabled()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_ConfigInfo\_SetAntiAliasingEnabled ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const bool antiAliasingEnabled)

**Description**:

Sets whether to enable anti-aliasing for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

configInfo

 | 

Pointer to the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

antiAliasingEnabled

 | 

Indicates whether to enable anti-aliasing.

-   **true**: yes
-   **false**: no

The default value is **false**.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_ConfigInfo\_SetCurrentFrameRate()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_ConfigInfo\_SetCurrentFrameRate ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const int64\_t currentFrameRate)

**Description**:

Sets the current frame rate for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

configInfo

 | 

Pointer to the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

currentFrameRate

 | 

Current frame rate. The value ranges from 1 to 144.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_ConfigInfo\_SetCurrentPictureQualityLevel()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_ConfigInfo\_SetCurrentPictureQualityLevel ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const [GamePerformance\_PictureQualityLevel](#ga64fd3d566be9f8240d0f474d52c292dd) currentPictureQualityLevel)

**Description**:

Sets the current image quality level for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

configInfo

 | 

Pointer to the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

currentPictureQualityLevel

 | 

Current image quality level. For details, please refer to [GamePerformance\_PictureQualityLevel](#ga64fd3d566be9f8240d0f474d52c292dd).

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_ConfigInfo\_SetCurrentResolution()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_ConfigInfo\_SetCurrentResolution ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const char \*currentResolution)

**Description**:

Sets the current resolution for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

configInfo

 | 

Pointer to the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

currentResolution

 | 

Current resolution, which is in _AxB_ format, for example, **1260x1980**. The value length range is \[1, 32\].

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_ConfigInfo\_SetHdModeEnabled()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_ConfigInfo\_SetHdModeEnabled ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const bool hdModeEnabled)

**Description**:

Enables the HD mode for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

configInfo

 | 

Pointer to the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

hdModeEnabled

 | 

Indicates whether to enable the HD mode.

-   **true**: yes
-   **false**: no

The default value is **false**.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_ConfigInfo\_SetMaxFrameRate()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_ConfigInfo\_SetMaxFrameRate ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const int64\_t maxFrameRate)

**Description**:

Sets the maximum frame rate for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

configInfo

 | 

Pointer to the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

maxFrameRate

 | 

Maximum frame rate.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_ConfigInfo\_SetMaxPictureQualityLevel()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_ConfigInfo\_SetMaxPictureQualityLevel ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const [GamePerformance\_PictureQualityLevel](#ga64fd3d566be9f8240d0f474d52c292dd) maxPictureQualityLevel)

**Description**:

Sets the maximum image quality level for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

configInfo

 | 

Pointer to the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

maxPictureQualityLevel

 | 

Supported highest image quality level. For details, please refer to [GamePerformance\_PictureQualityLevel](#ga64fd3d566be9f8240d0f474d52c292dd).

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_ConfigInfo\_SetMaxResolution()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_ConfigInfo\_SetMaxResolution ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const char \*maxResolution)

**Description**:

Sets the maximum resolution for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

configInfo

 | 

Pointer to the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

maxResolution

 | 

Maximum resolution, which is in _AxB_ format, for example, **1260x1980**. The value length range is \[1, 32\].

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_ConfigInfo\_SetMultithreadingEnabled()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_ConfigInfo\_SetMultithreadingEnabled ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const bool multithreadingEnabled)

**Description**:

Enables multi-threading for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

configInfo

 | 

Pointer to the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

multithreadingEnabled

 | 

Indicates whether to enable multi-threading.

-   **true**: yes
-   **false**: no

The default value is **false**.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_ConfigInfo\_SetParticleEnabled()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_ConfigInfo\_SetParticleEnabled ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const bool particleEnabled)

**Description**:

Sets the particle effect for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

configInfo

 | 

Pointer to the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

particleEnabled

 | 

Indicates whether to enable the particle effect.

-   **true**: yes
-   **false**: no

The default value is **false**.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_ConfigInfo\_SetShadowEnabled()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_ConfigInfo\_SetShadowEnabled ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo, const bool shadowEnabled)

**Description**:

Sets whether to enable the shadow effect for the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

configInfo

 | 

Pointer to the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

shadowEnabled

 | 

Indicates whether to enable the shadow effect.

-   **true**: yes
-   **false**: no

The default value is **false**.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_CpuInfo\_GetCpuLoadLevel()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_CpuInfo\_GetCpuLoadLevel ([GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) \*cpuInfo, int32\_t \*cpuLoadLevel)

**Description**:

Obtains the overall CPU load level from [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d).

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

cpuInfo

 | 

Pointer to a [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) instance. The value cannot be null. Otherwise, error code 1010300004 will be returned.

 |
| 

cpuLoadLevel

 | 

Overall CPU load level. The value is an integer ranging from 1 to 10. A larger value indicates a heavier load.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_ERROR**: invalid parameter. The parameter cannot be a null pointer.

 |

#### \[h2\]HMS\_GamePerformance\_CpuInfo\_GetSingleThreadLoadLevel()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_CpuInfo\_GetSingleThreadLoadLevel ([GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) \*cpuInfo, int32\_t \*singleThreadLoadLevel)

**Description**:

Obtains the overall load level of the heaviest thread in the game from [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d).

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

cpuInfo

 | 

Pointer to a [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) instance. The value cannot be null. Otherwise, error code 1010300004 will be returned.

 |
| 

singleThreadLoadLevel

 | 

Overall load level of the heaviest thread in the game. The value is an integer ranging from 1 to 10. A larger value indicates a heavier load.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_ERROR**: invalid parameter. The parameter cannot be a null pointer.

 |

#### \[h2\]HMS\_GamePerformance\_CreateConfigInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_CreateConfigInfo ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*\*configInfo)

**Description**:

Creates a [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance, which will be used in the [HMS\_GamePerformance\_UpdateConfigInfo](#ga6fe77ea4f43939333c7c3b07e1204448) method.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

configInfo

 | 

Double pointer to the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

 |

#### \[h2\]HMS\_GamePerformance\_CreateInitParameters()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_CreateInitParameters ([GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) \*\*initParameters)

**Description**:

Creates a [GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) instance, which will be used in the [HMS\_GamePerformance\_Init](#ga1045d9d8f4e7972b44ff95571afca8f9) method.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

initParameters

 | 

Double pointer to the initialization parameter instance [GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411).

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

 |

#### \[h2\]HMS\_GamePerformance\_CreateNetInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_CreateNetInfo ([GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) \*\*netInfo)

**Description**:

Creates a [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance, which will be used in the [HMS\_GamePerformance\_UpdateNetInfo](#ga29ff530f9f37560359fdd0d28ba6275b) method.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

netInfo

 | 

Double pointer to the [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

 |

#### \[h2\]HMS\_GamePerformance\_CreatePackageInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_CreatePackageInfo ([GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) \*\*packageInfo)

**Description**:

Creates a [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance, which will be used in the [HMS\_GamePerformance\_UpdatePackageInfo](#ga317ba7027076ce06ae73a6188bc3b129) method.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

packageInfo

 | 

Double pointer to the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

 |

#### \[h2\]HMS\_GamePerformance\_CreatePlayerInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_CreatePlayerInfo ([GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) \*\*playerInfo)

**Description**:

Creates a [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) instance, which will be used in the [HMS\_GamePerformance\_UpdatePlayerInfo](#ga71c7be26b9531af9bcd807e3255c4e6f) method.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

playerInfo

 | 

Double pointer to the [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) instance.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

 |

#### \[h2\]HMS\_GamePerformance\_CreateSceneInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_CreateSceneInfo ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*\*sceneInfo)

**Description**:

Creates a [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance, which will be used in the [HMS\_GamePerformance\_UpdateSceneInfo](#gad9504bae5e5b570e55bdf7f84a7a05bf) method.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Double pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

 |

#### \[h2\]HMS\_GamePerformance\_CreateThermalInfoQueryParameters()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_CreateThermalInfoQueryParameters ([GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) \*\*parameters)

**Description**:

Creates a [GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) instance, which will be used in the [HMS\_GamePerformance\_QueryThermalInfo](#gab7cb47e0dc3cce1169a8104827f7edb7) method.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

parameters

 | 

Double pointer to the [GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) instance.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

 |

#### \[h2\]HMS\_GamePerformance\_DestroyConfigInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_DestroyConfigInfo ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*\*configInfo)

**Description**:

Destroys a [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance when it is no longer used.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

configInfo

 | 

Double pointer to the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_DestroyCpuInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_DestroyCpuInfo ([GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) \*\*cpuInfo)

**Description**:

Destroys a [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) instance when it is no longer used.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

cpuInfo

 | 

Double pointer to a [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) instance. The value cannot be null. Otherwise, error code 1010300004 will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_ERROR**: invalid parameter. The parameter cannot be a null pointer.

 |

#### \[h2\]HMS\_GamePerformance\_DestroyDeviceInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_DestroyDeviceInfo ([GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80) \*\*deviceInfo)

**Description**:

Destroys a [GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80) instance when it is no longer used.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

deviceInfo

 | 

Double pointer to the [GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_DestroyGpuInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_DestroyGpuInfo ([GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) \*\*gpuInfo)

**Description**:

Destroys a [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) instance when it is no longer used.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

gpuInfo

 | 

Double pointer to the [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_DestroyInitParameters()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_DestroyInitParameters ([GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) \*\*initParameters)

**Description**:

Destroys a [GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) instance when it is no longer used.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

initParameters

 | 

Double pointer to the [GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_DestroyNetInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_DestroyNetInfo ([GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) \*\*netInfo)

**Description**:

Destroys a [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance when it is no longer used.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

netInfo

 | 

Double pointer to the [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_DestroyPackageInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_DestroyPackageInfo ([GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) \*\*packageInfo)

**Description**:

Destroys a [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance when it is no longer used.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

packageInfo

 | 

Double pointer to the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_DestroyPlayerInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_DestroyPlayerInfo ([GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) \*\*playerInfo)

**Description**:

Destroys a [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) instance when it is no longer used.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

playerInfo

 | 

Double pointer to the [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_DestroySceneInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_DestroySceneInfo ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*\*sceneInfo)

**Description**:

Destroys a [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance when it is no longer used.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Double pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_DestroyThermalInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_DestroyThermalInfo ([GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*\*thermalInfo)

**Description**:

Destroys a [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) instance when it is no longer used.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

thermalInfo

 | 

Double pointer to the [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_DestroyThermalInfoQueryParameters()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_DestroyThermalInfoQueryParameters ([GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) \*\*parameters)

**Description**:

Destroys a [GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) instance when it is no longer used.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

parameters

 | 

Double pointer to the [GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_DeviceInfo\_GetCpuInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_DeviceInfo\_GetCpuInfo ([GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80) \*deviceInfo, [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) \*\*cpuInfo)

**Description**:

Obtains the CPU performance information [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) from the device performance information [GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80). When a [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) instance is no longer needed, you must call [HMS\_GamePerformance\_DestroyCpuInfo](#ga6e76026d1a4c34c4bf983136e0a21734) to destroy it.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

deviceInfo

 | 

Pointer to the [GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80) instance. The value cannot be null. Otherwise, error code 1010300004 will be returned.

 |
| 

cpuInfo

 | 

Double pointer to a [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) instance.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_ERROR**: invalid parameter. The parameter cannot be a null pointer.

 |

#### \[h2\]HMS\_GamePerformance\_DeviceInfo\_GetGpuInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_DeviceInfo\_GetGpuInfo ([GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80) \*deviceInfo, [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) \*\*gpuInfo)

**Description**:

Obtains the GPU performance information [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) from the device performance information [GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80). When a [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) instance is no longer needed, you must call [HMS\_GamePerformance\_DestroyGpuInfo](#ga249433eea6a463cb2401e7bbbbcd19dd) to destroy it.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

deviceInfo

 | 

Pointer to the [GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

gpuInfo

 | 

Double pointer to the [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) instance.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_DeviceInfo\_GetThermalInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_DeviceInfo\_GetThermalInfo ([GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80) \*deviceInfo, [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*\*thermalInfo)

**Description**:

Obtains the temperature information [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) from the device performance information [GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80). When a [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) instance is no longer needed, you must call [HMS\_GamePerformance\_DestroyThermalInfo](#gacc640a4e15fe9cab1f8bccb652d77e59) to destroy it.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

deviceInfo

 | 

Pointer to the [GamePerformance\_DeviceInfo](#ga530e1cf28aa5c4d0b355dc053ce27e80) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

thermalInfo

 | 

Double pointer to the [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) instance.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_GpuInfo\_GetBandwidthLoadLevel()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_GpuInfo\_GetBandwidthLoadLevel ([GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) \*gpuInfo, int32\_t \*bandwidthLoadLevel)

**Description**:

Obtains the GPU bandwidth load level from [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113).

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

gpuInfo

 | 

Pointer to the [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

bandwidthLoadLevel

 | 

GPU bandwidth load level. The value is an integer ranging from 1 to 10. A larger value indicates a heavier load.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_GpuInfo\_GetCurrentFrequency()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_GpuInfo\_GetCurrentFrequency ([GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) \*gpuInfo, int32\_t \*currentFrequency)

**Description**:

Obtains the GPU frequency information from [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113).

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

gpuInfo

 | 

Pointer to the [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

currentFrequency

 | 

GPU frequency information, in KHz.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_GpuInfo\_GetFragmentLoadLevel()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_GpuInfo\_GetFragmentLoadLevel ([GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) \*gpuInfo, int32\_t \*fragmentLoadLevel)

**Description**:

Obtains the GPU fragment processing load level from [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113).

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

gpuInfo

 | 

Pointer to the [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

fragmentLoadLevel

 | 

GPU fragment processing load level. The value is an integer ranging from 1 to 10. A larger value indicates a heavier load.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_GpuInfo\_GetGpuLoadLevel()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_GpuInfo\_GetGpuLoadLevel ([GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) \*gpuInfo, int32\_t \*gpuLoadLevel)

**Description**:

Obtains the GPU load information from [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113).

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

gpuInfo

 | 

Pointer to the [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

gpuLoadLevel

 | 

GPU load information. The value is an integer ranging from 1 to 10. A larger value indicates a heavier load.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_GpuInfo\_GetTextureLoadLevel()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_GpuInfo\_GetTextureLoadLevel ([GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) \*gpuInfo, int32\_t \*textureLoadLevel)

**Description**:

Obtains the GPU texture processing load level from [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113).

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

gpuInfo

 | 

Pointer to the [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

textureLoadLevel

 | 

GPU texture processing load level. The value is an integer ranging from 1 to 10. A larger value indicates a heavier load.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_GpuInfo\_GetVertexLoadLevel()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_GpuInfo\_GetVertexLoadLevel ([GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) \*gpuInfo, int32\_t \*vertexLoadLevel)

**Description**:

Obtains the GPU vertex processing load level from [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113).

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

gpuInfo

 | 

Pointer to the [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

vertexLoadLevel

 | 

GPU vertex processing load level. The value is an integer ranging from 1 to 10. A larger value indicates a heavier load.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_Init()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_Init ([GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) \*initParameters)

**Description**:

Initializes the game scene perception module.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

initParameters

 | 

Pointer to the [GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

**GAME\_PERFORMANCE\_INTERNAL\_ERROR**: internal system error.

**GAME\_PERFORMANCE\_AUTH\_FAILED**: authentication failure.

 |

#### \[h2\]HMS\_GamePerformance\_InitParameters\_SetAppVersion()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_InitParameters\_SetAppVersion ([GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) \*initParameters,const char \*appVersion)

**Description**:

Sets the version number for the [GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

initParameters

 | 

Pointer to the [GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

appVersion

 | 

Game version number. The value length range is \[1, 64\].

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_InitParameters\_SetBundleName()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_InitParameters\_SetBundleName ([GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) \*initParameters, const char \*bundleName)

**Description**:

Sets the package name for the [GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

initParameters

 | 

Pointer to the [GamePerformance\_InitParameters](#ga9ba0e813bb05d37656f9973a35fa0411) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

bundleName

 | 

Game package name. The value length range is \[1, 128\].

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_NetInfo\_SetDownlinkLatency()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_NetInfo\_SetDownlinkLatency ([GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) \*netInfo, const int64\_t down)

**Description**:

Sets the downlink network latency for the [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

netInfo

 | 

Pointer to the [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

down

 | 

Downlink network latency, in ms.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_NetInfo\_SetNetLoad()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_NetInfo\_SetNetLoad ([GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) \*netInfo, const [GamePerformance\_NetLoad](#ga517e25164876d3727c407c887943aee2) netLoad)

**Description**:

Sets the network load for the [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

netInfo

 | 

Pointer to the [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

netLoad

 | 

Network load [GamePerformance\_NetLoad](#ga638c2b6f6d0dda3138e34869635b2dd4).

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_NetInfo\_SetServerLatency()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_NetInfo\_SetServerLatency ([GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) \*netInfo, const int64\_t server)

**Description**:

Sets the server network latency for the [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

netInfo

 | 

Pointer to the [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

server

 | 

Server network latency, in ms.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_NetInfo\_SetTotalLatency()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_NetInfo\_SetTotalLatency ([GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) \*netInfo, const int64\_t total)

**Description**:

Sets the total network latency for the [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

netInfo

 | 

Pointer to the [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

total

 | 

Total network latency, in ms.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_NetInfo\_SetUplinkLatency()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_NetInfo\_SetUplinkLatency ([GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) \*netInfo, const int64\_t up)

**Description**:

Sets the uplink network latency for the [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

netInfo

 | 

Pointer to the [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

up

 | 

Uplink network latency, in ms.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_PackageInfo\_SetAppVersion()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_PackageInfo\_SetAppVersion ([GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo, const char \*appVersion)

**Description**:

Sets the game version number for the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

packageInfo

 | 

Pointer to the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

appVersion

 | 

Game version number. The value length range is \[1, 64\].

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_PackageInfo\_SetBundleName()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_PackageInfo\_SetBundleName ([GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo, const char \*bundleName)

**Description**:

Sets the package name for the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

packageInfo

 | 

Pointer to the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

bundleName

 | 

Game package name. The value length range is \[1, 128\].

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_PackageInfo\_SetEngineType()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_PackageInfo\_SetEngineType ([GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo, const [GamePerformance\_EngineType](#gab7f3d09e6dd4af1692872b6b5815af45) engineType)

**Description**:

Sets the engine type for the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

packageInfo

 | 

Pointer to the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

engineType

 | 

Engine type [GamePerformance\_EngineType](#ga449d5fa8c8ee0fbea9188fd345401462).

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_PackageInfo\_SetEngineVersion()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_PackageInfo\_SetEngineVersion ([GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo, const char \*engineVersion)

**Description**:

Sets the engine version number for the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

packageInfo

 | 

Pointer to the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

engineVersion

 | 

Game engine version number. The value length range is \[0, 64\].

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_PackageInfo\_SetGameType()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_PackageInfo\_SetGameType ([GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo, const [GamePerformance\_GameType](#ga9c1b6f00c4769f13c510a7a871c7afd3) gameType)

**Description**:

Sets the game type for the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

packageInfo

 | 

Pointer to the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

gameType

 | 

Game type [GamePerformance\_GameType](#ga1e1370020b763cb4cce215d955ebb78d).

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_PackageInfo\_SetVulkanSupported()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_PackageInfo\_SetVulkanSupported ([GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo, const bool vulkanSupported)

**Description**:

Sets whether the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance supports Vulkan.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

packageInfo

 | 

Pointer to the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

vulkanSupported

 | 

Indicates whether Vulkan is supported.

-   **true**: yes
-   **false**: no

The default value is **false**.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_PlayerInfo\_SetGamePlayerId()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_PlayerInfo\_SetGamePlayerId ([GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) \*playerInfo, const char \*gamePlayerId)

**Description**:

Sets the player ID for the [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

playerInfo

 | 

Pointer to the [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

gamePlayerId

 | 

Game player ID. The value length range is \[0, 256\].

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_PlayerInfo\_SetTeamPlayerId()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_PlayerInfo\_SetTeamPlayerId ([GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) \*playerInfo, const char \*teamPlayerId)

**Description**:

Sets the team player ID for the [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

playerInfo

 | 

Pointer to the [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

teamPlayerId

 | 

Team player ID. The value length range is \[0, 256\].

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_PlayerInfo\_SetThirdOpenId()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_PlayerInfo\_SetThirdOpenId ([GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) \*playerInfo, const char \*thirdOpenId)

**Description**:

Sets the official game account for the [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

playerInfo

 | 

Pointer to the [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

thirdOpenId

 | 

Official game account. The value length range is \[0, 128\].

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_QueryCpuInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_QueryCpuInfo ([GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) \*\*cpuInfo)

**Description**:

Queries CPU performance information. When a [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) instance is no longer needed, you must call [HMS\_GamePerformance\_DestroyCpuInfo](#ga6e76026d1a4c34c4bf983136e0a21734) to destroy it.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

cpuInfo

 | 

Double pointer to a [GamePerformance\_CpuInfo](#ga5e0fa80aa26633c1b9d765340e4a262d) instance.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_INTERNAL\_ERROR**: internal system error. [Submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354579010004&amp;keyWord=Game Service Kit>) for assistance.

**GAME\_PERFORMANCE\_INVALID\_REQUEST**: invalid request. Call the [HMS\_GamePerformance\_Init](#ga1045d9d8f4e7972b44ff95571afca8f9) API first.

**GAME\_PERFORMANCE\_PARAM\_ERROR**: invalid parameter. The parameter cannot be a null pointer.

 |

#### \[h2\]HMS\_GamePerformance\_QueryGpuInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_QueryGpuInfo ([GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) \*\*gpuInfo)

**Description**:

Queries GPU performance information. When a [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) instance is no longer needed, you must call [HMS\_GamePerformance\_DestroyGpuInfo](#ga249433eea6a463cb2401e7bbbbcd19dd) to destroy it.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/_PT0rsveSrO_NWvli6aHWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062506Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F645FC809D7B54BD646B0DF48BF54B74744677712E14EE0C22FA8F186A1B042)

Mali series GPUs do not support GPU performance information collection.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

gpuInfo

 | 

Double pointer to the [GamePerformance\_GpuInfo](#gae85f740f82b3ca3f7ec9892d2f81a113) instance.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

**GAME\_PERFORMANCE\_INTERNAL\_ERROR**: internal system error.

**GAME\_PERFORMANCE\_INVALID\_REQUEST**: invalid request.

 |

#### \[h2\]HMS\_GamePerformance\_QueryThermalInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_QueryThermalInfo ([GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) \*parameters, [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*\*thermalInfo)

**Description**:

Queries temperature information. When a [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) instance is no longer needed, you must call [HMS\_GamePerformance\_DestroyThermalInfo](#gacc640a4e15fe9cab1f8bccb652d77e59) to destroy it.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

parameters

 | 

Pointer to the [GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

thermalInfo

 | 

Double pointer to the [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) instance.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

**GAME\_PERFORMANCE\_INTERNAL\_ERROR**: internal system error.

**GAME\_PERFORMANCE\_INVALID\_REQUEST**: invalid request.

 |

#### \[h2\]HMS\_GamePerformance\_RegisterThermalLevelChangedCallback()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_RegisterThermalLevelChangedCallback ([GamePerformance\_DeviceInfoType](#ga3ebb81788405856534d8fb3cd6194ca4) \*types\[\], size\_t size, [GamePerformance\_ThermalLevelChangedCallback](#ga94e7e85a3f0ad0b495b2c525a15ebc8e) callback, void \*userData)

**Description**:

Subscribes to temperature changes by registering the callback for temperature changes. When the trigger point is reached, this callback will be called.

This callback will be triggered once when the temperature level changes to a level below 3, and will be triggered every 10 seconds when the temperature level changes to level 3 or higher.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/0o94WF-4SM6Dw_aTY1F4UQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062506Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=005214B8129AC3407DCEC2DF8F9A5F2FF3FECE768A441BCC30F737F9B7A3267F)

Mali series GPUs do not support GPU performance information collection.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

types\[\]

 | 

Type of the device performance information. For details, please refer to [GamePerformance\_DeviceInfoType](#ga3ebb81788405856534d8fb3cd6194ca4).

 |
| 

size

 | 

Length of the **types** array.

 |
| 

callback

 | 

Callback [GamePerformance\_ThermalLevelChangedCallback](#ga94e7e85a3f0ad0b495b2c525a15ebc8e).

 |
| 

userData

 | 

User-specified data. The value is defined by a user and then passed through a callback.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

**GAME\_PERFORMANCE\_INTERNAL\_ERROR**: internal system error.

**GAME\_PERFORMANCE\_INVALID\_REQUEST**: invalid request.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetChannelCount()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetChannelCount ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t channelCount)

**Description**:

Sets the number of channels rendered per frame for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

channelCount

 | 

Number of channels rendered per frame.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetCurrentFrameRate()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetCurrentFrameRate ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t currentFrameRate)

**Description**:

Sets the frame rate of the current scene for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

currentFrameRate

 | 

Frame rate of the current scene.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetDescription()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetDescription ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const char \*description)

**Description**:

Sets the scene description for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

description

 | 

Custom game scene description. The value length range is \[0, 128\].

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetDrawCallCount()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetDrawCallCount ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t drawCallCount)

**Description**:

Sets the average number of draw calls per frame for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

drawCallCount

 | 

Average number of draw calls per frame.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetImportanceLevel()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetImportanceLevel ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const [GamePerformance\_SceneImportanceLevel](#gaf6bbf14a7010d4e99e6c758a718a08a6) importanceLevel)

**Description**:

Sets the scene importance level for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

importanceLevel

 | 

Importance level of a scene [GamePerformance\_SceneImportanceLevel](#ga59c720e67f9586ae4f24223be1ae3dc5).

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetKeyThread()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetKeyThread ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const char \*keyThread)

**Description**:

Sets the key thread for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

keyThread

 | 

Key thread of a scene.

-   **render**: render thread
-   **logic**: logic thread
-   **net**: network thread

The value is in _render|xxx|logic|xxx_ format. The value length range is \[0, 32\].

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetMaxFrameRate()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetMaxFrameRate ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t maxFrameRate)

**Description**:

Sets the maximum frame rate of a scene for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

maxFrameRate

 | 

Maximum frame rate of a scene.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetMeshCount()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetMeshCount ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t meshCount)

**Description**:

Sets the average number of meshes per frame for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

meshCount

 | 

Average number of meshes per frame.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetParticipantCount()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetParticipantCount ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t participantCount)

**Description**:

Sets the number of players on the same screen in a scene for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

participantCount

 | 

Number of players on the same screen in a scene.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetRecommendedCpuLevel()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetRecommendedCpuLevel ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const [GamePerformance\_CpuLevel](#ga11ac456fd1b33d0b1f6220af5e5cd1ce) recommendedCpuLevel)

**Description**:

Sets the recommended CPU level for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

recommendedCpuLevel

 | 

Recommended CPU level [GamePerformance\_CpuLevel](#ga4d30bee20aca3ea7082302ae7164a196).

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetRecommendedDdrLevel()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetRecommendedDdrLevel ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const [GamePerformance\_DdrLevel](#gaec1b60b592a13ea85774a4d2ec8581bb) recommendedDdrLevel)

**Description**:

Sets the recommended DDR level for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

recommendedDdrLevel

 | 

Recommended DDR level [GamePerformance\_DdrLevel](#ga57b549a68edbc9c84843040beb886389).

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetRecommendedGpuLevel()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetRecommendedGpuLevel ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const [GamePerformance\_GpuLevel](#ga48d14f66a8d484b497157458dd13a473) recommendedGpuLevel)

**Description**:

Sets the recommended GPU level for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

recommendedGpuLevel

 | 

Recommended GPU level [GamePerformance\_GpuLevel](#ga12e1ee7ac06fc6bd25a87cce66d2a632).

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetSceneFrequency()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetSceneFrequency ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t sceneFrequency)

**Description**:

Sets the number of times a scene appears in a round of the game for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

sceneFrequency

 | 

Number of times a scene appears in a round of game.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetSceneID()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetSceneID ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t sceneID)

**Description**:

Sets the scene ID for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

sceneID

 | 

Scene ID.

-   **0**: scene switchback, indicating the end of the current scene
-   **1**: game startup
-   **2**: in-game update
-   **3**: sign-in
-   **4**: home screen
-   **5**: loading a game session by the player
-   **6**: having finished loading a game session and waiting for other players to load theirs
-   **7**: gaming
-   **8**: onlooker mode

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetSceneTime()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetSceneTime ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t sceneTime)

**Description**:

Sets the scene duration for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

sceneTime

 | 

Duration of a scene, in ms.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetShaderCount()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetShaderCount ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t shaderCount)

**Description**:

Sets the average number of shaders per frame for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

shaderCount

 | 

Average number of shaders per frame.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetSubDescription()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetSubDescription ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const char \*subDescription)

**Description**:

Sets the sub-scene description for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

subDescription

 | 

Custom game sub-scene description. The value length range is \[0, 128\].

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetSubSceneID()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetSubSceneID ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const char \*subSceneID)

**Description**:

Sets the sub-scene ID for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

subSceneID

 | 

Game sub-scene ID. The value length range is \[0, 128\].

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetTextureCount()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetTextureCount ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t textureCount)

**Description**:

Sets the average number of textures per frame for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

textureCount

 | 

Average number of textures per frame.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetTriangleCount()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetTriangleCount ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t triangleCount)

**Description**:

Sets the average number of model triangles per frame for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

triangleCount

 | 

Average number of model triangles per frame.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_SceneInfo\_SetVertexCount()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_SceneInfo\_SetVertexCount ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo, const int64\_t vertexCount)

**Description**:

Sets the average number of model vertices per frame for the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

vertexCount

 | 

Average number of model vertices per frame.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_ThermalInfo\_GetNowNormalizedCurrent()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_ThermalInfo\_GetNowNormalizedCurrent ([GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*thermalInfo, int32\_t \*nowCurrent)

**Description**:

Obtains the current operating current from [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a).

**Start version**: 6.0.2(22)

**Device behavior differences**: This API is supported on phones, but returns no value on other devices.

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

thermalInfo

 | 

Pointer to the [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) instance. The value cannot be null. Otherwise, error code 1010300004 will be returned.

 |
| 

nowCurrent

 | 

Current operating current, in mA.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_ERROR**: invalid parameter. The parameter cannot be a null pointer.

 |

#### \[h2\]HMS\_GamePerformance\_ThermalInfo\_GetRecommendMaxNormalizedCurrent()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_ThermalInfo\_GetRecommendMaxNormalizedCurrent ([GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*thermalInfo, int32\_t \*recommendMaxCurrent)

**Description**:

Obtains the recommended maximum operating current from [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a).

**Start version**: 6.0.2(22)

**Device behavior differences**: This API is supported on phones, but returns no value on other devices.

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

thermalInfo

 | 

Pointer to the [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) instance. The value cannot be null. Otherwise, error code 1010300004 will be returned.

 |
| 

recommendMaxCurrent

 | 

Recommended maximum operating current, in mA.

If the current operating current is higher than this value, the device will immediately heat up.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_ERROR**: invalid parameter. The parameter cannot be a null pointer.

 |

#### \[h2\]HMS\_GamePerformance\_ThermalInfo\_GetRecommendNormalizedCurrent()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_ThermalInfo\_GetRecommendNormalizedCurrent ([GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*thermalInfo, int32\_t \*recommendCurrent)

**Description**:

Obtains the recommended operating current from [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a).

**Start version**: 6.0.2(22)

**Device behavior differences**: This API is supported on phones, but returns no value on other devices.

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

thermalInfo

 | 

Pointer to the [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) instance. The value cannot be null. Otherwise, error code 1010300004 will be returned.

 |
| 

recommendCurrent

 | 

Recommended operating current, in mA.

If the current operating current is higher than the recommended value, the temperature trend **thermalTrend** will be greater than 0, indicating a risk of device overheating.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_ERROR**: invalid parameter. The parameter cannot be a null pointer.

 |

#### \[h2\]HMS\_GamePerformance\_ThermalInfo\_GetThermalLevel()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_ThermalInfo\_GetThermalLevel ([GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*thermalInfo, int32\_t \*thermalLevel)

**Description**:

Obtains the temperature level from [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a).

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

thermalInfo

 | 

Pointer to the [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

thermalLevel

 | 

Temperature level, or temperature control level. A higher level indicates a higher temperature. The suggestions for different levels are as follows:

-   **1**: No action is required.
-   **2**: You are advised to lower the specifications of imperceptible services, for example, reducing the background update rate or delaying the running of game tasks.
-   **3**: You are advised to suspend imperceptible services to lower the specifications of non-core game services, for example, reducing the rate of foreground update.
-   **4**. You are advised to lower the game effects, resolution, and image quality.
-   **5**. You are advised to lower the specifications in all scenes to further lower the resolution and image quality.
-   **6**: You are advised to lower the game specifications to the minimum level.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_ThermalInfo\_GetThermalMargin()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_ThermalInfo\_GetThermalMargin ([GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*thermalInfo, int32\_t \*thermalMargin)

**Description**:

Obtains the temperature time margin from the temperature information [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a).

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

thermalInfo

 | 

Pointer to the [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

thermalMargin

 | 

Time margin, that is, the time needed for the temperature to reach the specified level. A negative value indicates that the time margin cannot be predicted. Unit: second

NOTE:

-   If the value exceeds 60, the reliability decreases.
-   **0**: The queried temperature control level is reached.
-   **\-1**: The queried level cannot be reached.
-   **\-2**: The queried level is lower than the current level.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_ThermalInfo\_GetThermalTrend()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_ThermalInfo\_GetThermalTrend ([GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*thermalInfo, int32\_t \*thermalTrend)

**Description**:

Obtains the temperature trend from the temperature information [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a).

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

thermalInfo

 | 

Pointer to the [GamePerformance\_ThermalInfo](#ga6767ea8a1d76ed32db95dc0d3a265a8a) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

thermalTrend

 | 

Temperature trend. The value range is \[-100, 100\]. A negative value represents a temperature drop, and a larger absolute value indicates a faster rate of temperature change.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_ThermalInfoQueryParameters\_SetNeedsPrediction()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_ThermalInfoQueryParameters\_SetNeedsPrediction ([GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) \*parameters, const bool needsPrediction)

**Description**:

Sets whether predicting temperature trend is required for the [GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

parameters

 | 

Pointer to the [GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

needsPrediction

 | 

Indicates whether predicting temperature trend is required. If predicting temperature trend is required, the temperature time margin and temperature trend will be returned.

-   **true**: yes
-   **false**: no

The default value is **false**.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_ThermalInfoQueryParameters\_SetTargetThermalLevel()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_ThermalInfoQueryParameters\_SetTargetThermalLevel ([GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) \*parameters, const int32\_t targetThermalLevel)

**Description**:

Sets the target temperature level for predicting the temperature trend for the [GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) instance.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

parameters

 | 

Pointer to the [GamePerformance\_ThermalInfoQueryParameters](#ga0e825c8963101d40a987d4057033c788) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |
| 

targetThermalLevel

 | 

Target temperature level for predicting the temperature trend. If predicting temperature trend is required, the temperature time margin and temperature trend are calculated based on the target temperature level. For details about the parameter values, please refer to [HMS\_GamePerformance\_ThermalInfo\_GetThermalLevel()](#ga36713ebcb8a94fd99772965437c18b7f).

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

 |

#### \[h2\]HMS\_GamePerformance\_UnregisterAllThermalLevelChangedCallbacks()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_UnregisterAllThermalLevelChangedCallbacks (void)

**Description**:

Deregisters all callbacks for temperature changes.

**Start version**: 5.0.2(14)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_INTERNAL\_ERROR**: internal system error.

**GAME\_PERFORMANCE\_INVALID\_REQUEST**: invalid request.

 |

#### \[h2\]HMS\_GamePerformance\_UnregisterThermalLevelChangedCallback()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_UnregisterThermalLevelChangedCallback ([GamePerformance\_ThermalLevelChangedCallback](#ga94e7e85a3f0ad0b495b2c525a15ebc8e) callback)

**Description**:

Deregisters specified callbacks for temperature changes.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

callback

 | 

Callback [GamePerformance\_ThermalLevelChangedCallback](#ga94e7e85a3f0ad0b495b2c525a15ebc8e).

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

**GAME\_PERFORMANCE\_INTERNAL\_ERROR**: internal system error.

**GAME\_PERFORMANCE\_INVALID\_REQUEST**: invalid request.

 |

#### \[h2\]HMS\_GamePerformance\_UpdateConfigInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_UpdateConfigInfo ([GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo)

**Description**:

Updates game configuration information.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

configInfo

 | 

Pointer to the [GamePerformance\_ConfigInfo](#gab05a6dca6b3570c3b45d74a9cb8ffdc9) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

**GAME\_PERFORMANCE\_INTERNAL\_ERROR**: internal system error.

**GAME\_PERFORMANCE\_INVALID\_REQUEST**: invalid request.

 |

#### \[h2\]HMS\_GamePerformance\_UpdateNetInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_UpdateNetInfo ([GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) \*netInfo)

**Description**:

Updates game network information.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

netInfo

 | 

Pointer to the [GamePerformance\_NetInfo](#gaba275a8588101424676258ffa7217097) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

**GAME\_PERFORMANCE\_INTERNAL\_ERROR**: internal system error.

**GAME\_PERFORMANCE\_INVALID\_REQUEST**: invalid request.

 |

#### \[h2\]HMS\_GamePerformance\_UpdatePackageInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_UpdatePackageInfo ([GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo)

**Description**:

Updates game package information.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

packageInfo

 | 

Pointer to the [GamePerformance\_PackageInfo](#gab57ecb4bce0af8b741ef4aa069df2d87) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

**GAME\_PERFORMANCE\_INTERNAL\_ERROR**: internal system error.

**GAME\_PERFORMANCE\_INVALID\_REQUEST**: invalid request.

 |

#### \[h2\]HMS\_GamePerformance\_UpdatePlayerInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_UpdatePlayerInfo ([GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) \*playerInfo)

**Description**:

Updates game player information.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

playerInfo

 | 

Pointer to the [GamePerformance\_PlayerInfo](#ga804b472fc080d73a2ce23da927ffd842) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

**GAME\_PERFORMANCE\_INTERNAL\_ERROR**: internal system error.

**GAME\_PERFORMANCE\_INVALID\_REQUEST**: invalid request.

 |

#### \[h2\]HMS\_GamePerformance\_UpdateSceneInfo()

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316) HMS\_GamePerformance\_UpdateSceneInfo ([GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo)

**Description**:

Updates game scene information.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneInfo

 | 

Pointer to the [GamePerformance\_SceneInfo](#ga64047fc82c0783c507e34e10c735e4d7) instance. The value cannot be null. Otherwise, error code 401 will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](#ga615243fda2406a6f9cd3a406874b6316)

 | 

**GAME\_PERFORMANCE\_SUCCESS**: success.

**GAME\_PERFORMANCE\_PARAM\_INVALID**: invalid parameter.

**GAME\_PERFORMANCE\_INTERNAL\_ERROR**: internal system error.

**GAME\_PERFORMANCE\_INVALID\_REQUEST**: invalid request.

 |
