# Development Procedure (C/C++)

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/B4LYfxo8SeGZ54RCBI5yeg/en-us_image_0000002474151180.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DEB21F21E51B408DB949E87CF65E446E929C995875C4673360DEB31780BC6A7A)

1.  The game calls the [HMS\_GamePerformance\_Init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga1045d9d8f4e7972b44ff95571afca8f9) API to initialize the game scene perception module after being launched.
2.  After the initialization is successful, the game calls the [HMS\_GamePerformance\_RegisterThermalLevelChangedCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#gaa73a9464dbe4a973e7aed559835adbc6) API to register a device status change event listener and subscribe to device status change notifications.
3.  The game calls the following APIs to report relevant information to the game scene perception module:
    -   Package information: [HMS\_GamePerformance\_UpdatePackageInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga317ba7027076ce06ae73a6188bc3b129)
    -   Configuration: [HMS\_GamePerformance\_UpdateConfigInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga6fe77ea4f43939333c7c3b07e1204448)
    -   Scene information: [HMS\_GamePerformance\_UpdateSceneInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#gad9504bae5e5b570e55bdf7f84a7a05bf)
    -   Network information: [HMS\_GamePerformance\_UpdateNetInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga29ff530f9f37560359fdd0d28ba6275b)
    -   Player information: [HMS\_GamePerformance\_UpdatePlayerInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga71c7be26b9531af9bcd807e3255c4e6f)
4.  The game scene perception module broadcasts game information to the device system.
5.  The device system schedules system resources based on the game information.
6.  The device system notifies the game scene perception module of device status changes.
7.  The game scene perception module reports the device status changes to the game client.
8.  If the subscription is no longer required, the game can call the [HMS\_GamePerformance\_UnregisterThermalLevelChangedCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga306734f0bee9af7697b5fbfa19bafec0) API or [HMS\_GamePerformance\_UnregisterAllThermalLevelChangedCallbacks](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga0f2cf9152a9421d00bb0c03683b3f57d) API to cancel the device status change event listener.
9.  The game calls the following APIs to proactively query device status information from the game scene perception module:
    -   Device GPU performance information: [HMS\_GamePerformance\_QueryGpuInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga93f67c2befdb52f4b59893a7a300f292)
    -   Device CPU performance information: [HMS\_GamePerformance\_QueryCpuInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#gad59832ffd2679db7b1fa8310f586531f)
    -   Device temperature information: [HMS\_GamePerformance\_QueryThermalInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#gab7cb47e0dc3cce1169a8104827f7edb7)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/5aZf10QBQkmFcgRlpIVknQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4706858C751C510E4D8D7A84AF04F697F450BD5C988D01BFFF79609E0FBC004A)

Mali series GPUs do not support GPU performance information collection. GPU performance information cannot be obtained if you call the API for subscribing to or querying device status information.

#### API Description

For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-c).

| 
**API Name**

 | 

**Description**

 |
| :-- | :-- |
| 

[GamePerformance\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_Init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga1045d9d8f4e7972b44ff95571afca8f9) ([GamePerformance\_InitParameters](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga9ba0e813bb05d37656f9973a35fa0411) \*initParameters)

 | 

Initializes the game scene perception module.

 |
| 

[GamePerformance\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_RegisterThermalLevelChangedCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#gaa73a9464dbe4a973e7aed559835adbc6) ([GamePerformance\_DeviceInfoType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga3ebb81788405856534d8fb3cd6194ca4) \*types\[\], size\_t size, [GamePerformance\_ThermalLevelChangedCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga94e7e85a3f0ad0b495b2c525a15ebc8e) callback, void \*userData)

 | 

Registers a temperature change callback. When the trigger point is reached, this callback will be called.

 |
| 

[GamePerformance\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UpdatePackageInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga317ba7027076ce06ae73a6188bc3b129) ([GamePerformance\_PackageInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#gab57ecb4bce0af8b741ef4aa069df2d87) \*packageInfo)

 | 

Updates and reports game package information.

 |
| 

[GamePerformance\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UpdateConfigInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga6fe77ea4f43939333c7c3b07e1204448) ([GamePerformance\_ConfigInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#gab05a6dca6b3570c3b45d74a9cb8ffdc9) \*configInfo)

 | 

Updates and reports game configurations.

 |
| 

[GamePerformance\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UpdateSceneInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#gad9504bae5e5b570e55bdf7f84a7a05bf) ([GamePerformance\_SceneInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga64047fc82c0783c507e34e10c735e4d7) \*sceneInfo)

 | 

Updates and reports game scene information.

 |
| 

[GamePerformance\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UpdateNetInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga29ff530f9f37560359fdd0d28ba6275b) ([GamePerformance\_NetInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#gaba275a8588101424676258ffa7217097) \*netInfo)

 | 

Updates and reports game network information.

 |
| 

[GamePerformance\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UpdatePlayerInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga71c7be26b9531af9bcd807e3255c4e6f) ([GamePerformance\_PlayerInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga804b472fc080d73a2ce23da927ffd842) \*playerInfo)

 | 

Updates and reports game player information.

 |
| 

[GamePerformance\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UnregisterThermalLevelChangedCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga306734f0bee9af7697b5fbfa19bafec0) ([GamePerformance\_ThermalLevelChangedCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga94e7e85a3f0ad0b495b2c525a15ebc8e) callback)

 | 

Unregisters a specified temperature change callback.

 |
| 

[GamePerformance\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_UnregisterAllThermalLevelChangedCallbacks](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga0f2cf9152a9421d00bb0c03683b3f57d) (void)

 | 

Unregisters all temperature change callbacks.

 |
| 

[GamePerformance\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_QueryThermalInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#gab7cb47e0dc3cce1169a8104827f7edb7) ([GamePerformance\_ThermalInfoQueryParameters](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga0e825c8963101d40a987d4057033c788) \*parameters, [GamePerformance\_ThermalInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga6767ea8a1d76ed32db95dc0d3a265a8a) \*\*thermalInfo)

 | 

Queries temperature information.

 |
| 

[GamePerformance\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_QueryGpuInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga93f67c2befdb52f4b59893a7a300f292) ([GamePerformance\_GpuInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#gae85f740f82b3ca3f7ec9892d2f81a113) \*\*gpuInfo)

 | 

Queries GPU performance information.

 |
| 

[GamePerformance\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga615243fda2406a6f9cd3a406874b6316) [HMS\_GamePerformance\_QueryCpuInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#gad59832ffd2679db7b1fa8310f586531f) ([GamePerformance\_CpuInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga5e0fa80aa26633c1b9d765340e4a262d) \*\*cpuInfo)

 | 

Queries CPU performance information.

 |

#### Integration Procedure

## Linking the Dynamic Library in the CMake Script

target\_include\_directories(entry PUBLIC ${HMOS\_SDK\_NATIVE}/sysroot/usr/include)
target\_link\_directories(entry PUBLIC ${HMOS\_SDK\_NATIVE}/sysroot/usr/lib/aarch64-linux-ohos)
target\_link\_libraries(entry PUBLIC libgame\_performance.z.so)

## Importing Modules

Import Game Service Kit.

#include <GameServiceKit/game\_performance.h>
#include <cstdlib>

## Performing Initialization

After related modules are imported, call the [HMS\_GamePerformance\_Init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga1045d9d8f4e7972b44ff95571afca8f9) API to initialize the game scene perception module.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/Hkwb75NRQvSxEgLbuDiPqQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=522B867A3441916B0BC4B1A53C62BACF25E00B60BD134B0B498292F07210B640)

Before calling other APIs, you must first call the **HMS\_GamePerformance\_Init** API. If the initialization is not performed or fails, other APIs cannot be called.

// Create initialization parameters.
GamePerformance\_InitParameters \*initParameters = NULL; 
HMS\_GamePerformance\_CreateInitParameters(&initParameters);

// Create parameters. The second parameter of all set APIs is a placeholder. Replace it with the actual one.
GamePerformance\_ErrorCode appVersionSetCode = HMS\_GamePerformance\_InitParameters\_SetAppVersion(initParameters, "1.0");

// If a parameter of a set API is incorrect, error code **401** will be returned. To ensure the correct parameter settings, you are advised to obtain the return values and check the error code.
if (appVersionSetCode != GAME\_PERFORMANCE\_SUCCESS) {
    // Troubleshooting.
}
HMS\_GamePerformance\_InitParameters\_SetBundleName(initParameters, "com.example.demo"); 
 
// Initialization.
GamePerformance\_ErrorCode ret = HMS\_GamePerformance\_Init(initParameters);
if (ret != GAME\_PERFORMANCE\_SUCCESS) {
    // Troubleshooting.
}

// Free up memory after use.
HMS\_GamePerformance\_DestroyInitParameters(&initParameters);

## Registering a Temperature Change Callback

You can call the [HMS\_GamePerformance\_RegisterThermalLevelChangedCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#gaa73a9464dbe4a973e7aed559835adbc6) API to register a temperature change callback to obtain notifications about the device status (such as the temperature information, GPU load, and CPU load).

// Define a callback.
static void onThermalLevelChanged(GamePerformance\_DeviceInfo \*deviceInfo, void \*userData) {
    // Obtain the GPU load level. (Ensure that you have subscribed to device information **GAME\_PERFORMANCE\_DEVICEINFO\_TYPE\_GPU**.)
    (void) userData;
    GamePerformance\_GpuInfo \*gpuInfo = NULL;
    HMS\_GamePerformance\_DeviceInfo\_GetGpuInfo(deviceInfo, &gpuInfo);
    int32\_t gpuloadLevel = -1;
    int32\_t vertexLevel = -1;
    int32\_t fragmentLoadLevel = -1;
    int32\_t bandwidthLoadLevel = -1;
    int32\_t textureLoadLevel = -1;
    int32\_t currentFrequency = -1;
    HMS\_GamePerformance\_GpuInfo\_GetGpuLoadLevel(gpuInfo, &gpuloadLevel);
    HMS\_GamePerformance\_GpuInfo\_GetVertexLoadLevel(gpuInfo, &vertexLevel);
    HMS\_GamePerformance\_GpuInfo\_GetFragmentLoadLevel(gpuInfo, &fragmentLoadLevel);
    HMS\_GamePerformance\_GpuInfo\_GetBandwidthLoadLevel(gpuInfo, &bandwidthLoadLevel);
    HMS\_GamePerformance\_GpuInfo\_GetTextureLoadLevel(gpuInfo, &textureLoadLevel);
    HMS\_GamePerformance\_GpuInfo\_GetCurrentFrequency(gpuInfo, &currentFrequency);

    // Obtain temperature information. (Make sure you subscribe to the device information type **GAME\_PERFORMANCE\_DEVICEINFO\_TYPE\_THERMAL**.)
    GamePerformance\_ThermalInfo \*thermalInfo = NULL;
    HMS\_GamePerformance\_DeviceInfo\_GetThermalInfo(deviceInfo, &thermalInfo);
    int32\_t margin = INT32\_MIN;
    int32\_t trend = INT32\_MIN;
    int32\_t level = -1;
    int32\_t recommendNormalizedCurrent = 0;
    int32\_t nowNormalizedCurrent = 0;
    int32\_t recommendMaxNormalizedCurrent = 0;
    HMS\_GamePerformance\_ThermalInfo\_GetThermalMargin(thermalInfo, &margin);
    HMS\_GamePerformance\_ThermalInfo\_GetThermalTrend(thermalInfo, &trend);
    HMS\_GamePerformance\_ThermalInfo\_GetThermalLevel(thermalInfo, &level);
    HMS\_GamePerformance\_ThermalInfo\_GetRecommendNormalizedCurrent(thermalInfo, &recommendNormalizedCurrent);
    HMS\_GamePerformance\_ThermalInfo\_GetNowNormalizedCurrent(thermalInfo, &nowNormalizedCurrent);
    HMS\_GamePerformance\_ThermalInfo\_GetRecommendMaxNormalizedCurrent(thermalInfo, &recommendMaxNormalizedCurrent);

    // Obtain the CPU usage. (Ensure that you have subscribed to device information **GAME\_PERFORMANCE\_DEVICEINFO\_TYPE\_CPU**.)
    GamePerformance\_CpuInfo \*cpuInfo = NULL;
    HMS\_GamePerformance\_DeviceInfo\_GetCpuInfo(deviceInfo, &cpuInfo);
    int32\_t cpuLoadLevel = 0;
    int32\_t singleThreadLoadLevel = 0;
    HMS\_GamePerformance\_CpuInfo\_GetCpuLoadLevel(cpuInfo, &cpuLoadLevel);
    HMS\_GamePerformance\_CpuInfo\_GetSingleThreadLoadLevel(cpuInfo, &singleThreadLoadLevel);

    // Free up memory after use.
    HMS\_GamePerformance\_DestroyGpuInfo(&gpuInfo);
    HMS\_GamePerformance\_DestroyThermalInfo(&thermalInfo);
    HMS\_GamePerformance\_DestroyCpuInfo(&cpuInfo);
}

// Register the callback.
void registerCallback() {
    // Subscribe to device information types as required.
    int size = 2; // Number of subscribed device information types, that is, the length of **array** defined below.
    GamePerformance\_DeviceInfoType \*\*array = (GamePerformance\_DeviceInfoType \*\*)malloc(sizeof(GamePerformance\_DeviceInfoType \*) \* size);
    if (array == NULL) {
        // Troubleshooting.
    }
    array\[0\] = (GamePerformance\_DeviceInfoType \*)malloc(sizeof(GamePerformance\_DeviceInfoType));
    array\[1\] = (GamePerformance\_DeviceInfoType \*)malloc(sizeof(GamePerformance\_DeviceInfoType));
    if (!array\[0\] || !array\[1\]) {
        // Troubleshooting.
    }
    \*(array\[0\]) = GAME\_PERFORMANCE\_DEVICEINFO\_TYPE\_GPU;
    \*(array\[1\]) = GAME\_PERFORMANCE\_DEVICEINFO\_TYPE\_THERMAL;
    void \*userData = (void \*)"mydata"; // User-defined data of any type, which will be returned through the callback.
    GamePerformance\_ErrorCode ret =
        HMS\_GamePerformance\_RegisterThermalLevelChangedCallback(array, size, onThermalLevelChanged, userData);
    free(array);
    if (ret != GAME\_PERFORMANCE\_SUCCESS) {
        // Troubleshooting.
    }
}

## Unregistering a Specified Temperature Change Callback

You can call the [HMS\_GamePerformance\_UnregisterThermalLevelChangedCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga306734f0bee9af7697b5fbfa19bafec0) API to unregister a specified temperature change callback.

// Unregister the callback.
GamePerformance\_ErrorCode ret = HMS\_GamePerformance\_UnregisterThermalLevelChangedCallback(onThermalLevelChanged);
if (ret != GAME\_PERFORMANCE\_SUCCESS) {
    // Troubleshooting.
}

## Unregistering All Temperature Change Callbacks

You can call the [HMS\_GamePerformance\_UnregisterAllThermalLevelChangedCallbacks](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga0f2cf9152a9421d00bb0c03683b3f57d) API to unregister all temperature change callbacks.

// Unregister all callbacks.
GamePerformance\_ErrorCode ret = HMS\_GamePerformance\_UnregisterAllThermalLevelChangedCallbacks();
if (ret != GAME\_PERFORMANCE\_SUCCESS) {
    // Troubleshooting.
}

## Reporting Game Package Information

After the initialization is successful, you can call the [HMS\_GamePerformance\_UpdatePackageInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga317ba7027076ce06ae73a6188bc3b129) API to report the game package information.

GamePerformance\_PackageInfo \*packageInfo = NULL;
HMS\_GamePerformance\_CreatePackageInfo(&packageInfo);

// The second parameter of set APIs is a placeholder. Replace it with the actual one.
// Set mandatory parameters.
HMS\_GamePerformance\_PackageInfo\_SetBundleName(packageInfo, "com.example.demo");  
HMS\_GamePerformance\_PackageInfo\_SetAppVersion(packageInfo, "1.0");

// Set optional parameters based on your needs.
HMS\_GamePerformance\_PackageInfo\_SetEngineType(packageInfo, GAME\_PERFORMANCE\_ENGINE\_TYPE\_COCOS);  
HMS\_GamePerformance\_PackageInfo\_SetEngineVersion(packageInfo, "2.0");
HMS\_GamePerformance\_PackageInfo\_SetGameType(packageInfo, GAME\_PERFORMANCE\_GAME\_TYPE\_FPS);  

// Report game package information.
GamePerformance\_ErrorCode ret = HMS\_GamePerformance\_UpdatePackageInfo(packageInfo);
if (ret != GAME\_PERFORMANCE\_SUCCESS) {
    // Troubleshooting.
}

// Free up memory after use.
HMS\_GamePerformance\_DestroyPackageInfo(&packageInfo);

## Reporting Game Configurations

After the initialization is successful, you can call the [HMS\_GamePerformance\_UpdateConfigInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga6fe77ea4f43939333c7c3b07e1204448) API to report the game configurations.

GamePerformance\_ConfigInfo \*configInfo = NULL;
HMS\_GamePerformance\_CreateConfigInfo(&configInfo);

// If multiple times of reporting are required using the same instance, you only need to use set APIs to update the parameters. (The parameters set previously are retained for the same instance.)
// The second parameter of set APIs is a placeholder. Replace it with the actual one.
// Set the following optional parameters based on your needs:
HMS\_GamePerformance\_ConfigInfo\_SetMaxPictureQualityLevel(configInfo, GAME\_PERFORMANCE\_PQL\_BALANCED);
HMS\_GamePerformance\_ConfigInfo\_SetCurrentPictureQualityLevel(configInfo, GAME\_PERFORMANCE\_PQL\_HD);
HMS\_GamePerformance\_ConfigInfo\_SetMaxFrameRate(configInfo, 120);
HMS\_GamePerformance\_ConfigInfo\_SetCurrentFrameRate(configInfo, 60);
HMS\_GamePerformance\_ConfigInfo\_SetMaxResolution(configInfo, "1260\*2720");
HMS\_GamePerformance\_ConfigInfo\_SetCurrentResolution(configInfo, "1260\*2720");
HMS\_GamePerformance\_ConfigInfo\_SetAntiAliasingEnabled(configInfo, true);
HMS\_GamePerformance\_ConfigInfo\_SetShadowEnabled(configInfo, true);
HMS\_GamePerformance\_ConfigInfo\_SetMultithreadingEnabled(configInfo, true);
HMS\_GamePerformance\_ConfigInfo\_SetParticleEnabled(configInfo, true);
HMS\_GamePerformance\_ConfigInfo\_SetHdModeEnabled(configInfo, true);

// Report game configurations.
GamePerformance\_ErrorCode ret = HMS\_GamePerformance\_UpdateConfigInfo(configInfo);
if (ret != GAME\_PERFORMANCE\_SUCCESS) {
    // Troubleshooting.
}

// Free up memory after use.
HMS\_GamePerformance\_DestroyConfigInfo(&configInfo);

## Reporting Game Scene Information

After the initialization is successful, you can call the [HMS\_GamePerformance\_UpdateSceneInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#gad9504bae5e5b570e55bdf7f84a7a05bf) API to report the game scene information.

// The second parameter of set APIs is a placeholder. Replace it with the actual one.
GamePerformance\_SceneInfo \*sceneInfo = NULL;
HMS\_GamePerformance\_CreateSceneInfo(&sceneInfo);

// If multiple times of reporting are required using the same instance, you only need to use set APIs to update the parameters. (The parameters set previously are retained for the same instance.)
// Set mandatory parameters.
HMS\_GamePerformance\_SceneInfo\_SetSceneID(sceneInfo, 1);
HMS\_GamePerformance\_SceneInfo\_SetImportanceLevel(sceneInfo, GAME\_PERFORMANCE\_SIL\_LEVEL1);

// Set the following optional parameters based on your needs:
HMS\_GamePerformance\_SceneInfo\_SetDescription(sceneInfo, "this is description of scene");
HMS\_GamePerformance\_SceneInfo\_SetSubSceneID(sceneInfo, "20101020304");
HMS\_GamePerformance\_SceneInfo\_SetSubDescription(sceneInfo, "this is description of subScene");
HMS\_GamePerformance\_SceneInfo\_SetSceneFrequency(sceneInfo, 2);
HMS\_GamePerformance\_SceneInfo\_SetSceneTime(sceneInfo, 15);
HMS\_GamePerformance\_SceneInfo\_SetRecommendedCpuLevel(sceneInfo, GAME\_PERFORMANCE\_CPU\_LEVEL\_HIGH);
HMS\_GamePerformance\_SceneInfo\_SetRecommendedGpuLevel(sceneInfo, GAME\_PERFORMANCE\_GPU\_LEVEL\_HIGH);
HMS\_GamePerformance\_SceneInfo\_SetRecommendedDdrLevel(sceneInfo, GAME\_PERFORMANCE\_DDR\_LEVEL\_HIGH);
HMS\_GamePerformance\_SceneInfo\_SetKeyThread(sceneInfo, "render");
HMS\_GamePerformance\_SceneInfo\_SetDrawCallCount(sceneInfo, 100);
HMS\_GamePerformance\_SceneInfo\_SetVertexCount(sceneInfo, 100);
HMS\_GamePerformance\_SceneInfo\_SetTriangleCount(sceneInfo, 100);
HMS\_GamePerformance\_SceneInfo\_SetShaderCount(sceneInfo, 100);
HMS\_GamePerformance\_SceneInfo\_SetTextureCount(sceneInfo, 100);
HMS\_GamePerformance\_SceneInfo\_SetMeshCount(sceneInfo, 100);
HMS\_GamePerformance\_SceneInfo\_SetChannelCount(sceneInfo, 100);
HMS\_GamePerformance\_SceneInfo\_SetParticipantCount(sceneInfo, 5);

// Report game scene information.
GamePerformance\_ErrorCode ret = HMS\_GamePerformance\_UpdateSceneInfo(sceneInfo);
if (ret != GAME\_PERFORMANCE\_SUCCESS) {
    // Troubleshooting.
}

// Free up memory after use.
HMS\_GamePerformance\_DestroySceneInfo(&sceneInfo);

## Reporting Game Network Information

After the initialization is successful, you can call the [HMS\_GamePerformance\_UpdateNetInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga29ff530f9f37560359fdd0d28ba6275b) API to report the game network information.

// The second parameter of set APIs is a placeholder. Replace it with the actual one.
GamePerformance\_NetInfo \*netInfo = NULL;
HMS\_GamePerformance\_CreateNetInfo(&netInfo);

// If multiple times of reporting are required using the same instance, you only need to use set APIs to update the parameters. (The parameters set previously are retained for the same instance.)
// Set mandatory parameters.
HMS\_GamePerformance\_NetInfo\_SetTotalLatency(netInfo, 60);

// Set the following optional parameters based on your needs:
HMS\_GamePerformance\_NetInfo\_SetNetLoad(netInfo, GAME\_PERFORMANCE\_NET\_LOAD\_HEAVY);
HMS\_GamePerformance\_NetInfo\_SetUplinkLatency(netInfo, 10);
HMS\_GamePerformance\_NetInfo\_SetDownlinkLatency(netInfo, 20);
HMS\_GamePerformance\_NetInfo\_SetServerLatency(netInfo, 30);

// Report game network information.
GamePerformance\_ErrorCode ret = HMS\_GamePerformance\_UpdateNetInfo(netInfo);
if (ret != GAME\_PERFORMANCE\_SUCCESS) {
    // Troubleshooting.
}

// Free up memory after use.
HMS\_GamePerformance\_DestroyNetInfo(&netInfo);

## Reporting Game Player Information

After the initialization is successful, you can call the [HMS\_GamePerformance\_UpdatePlayerInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga71c7be26b9531af9bcd807e3255c4e6f) API to report the game player information.

// The second parameter of set APIs is a placeholder. Replace it with the actual one.
GamePerformance\_PlayerInfo \*playerInfo = NULL;
HMS\_GamePerformance\_CreatePlayerInfo(&playerInfo);

// Set at least one of the following parameters:
HMS\_GamePerformance\_PlayerInfo\_SetGamePlayerId(playerInfo, "43JIOdok74\*\*\*3980sd9453");
HMS\_GamePerformance\_PlayerInfo\_SetTeamPlayerId(playerInfo, "s2546dgs38\*\*\*374dgwa5g3");
HMS\_GamePerformance\_PlayerInfo\_SetThirdOpenId(playerInfo, "k854Cs367\*\*\*937efwhi03");

// Report game player information.
GamePerformance\_ErrorCode ret = HMS\_GamePerformance\_UpdatePlayerInfo(playerInfo);
if (ret != GAME\_PERFORMANCE\_SUCCESS) {
    // Troubleshooting.
}

// Free up memory after use.
HMS\_GamePerformance\_DestroyPlayerInfo(&playerInfo);

## Querying GPU Performance Information

In addition to subscribing to device status changes, you can also call the [HMS\_GamePerformance\_QueryGpuInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#ga93f67c2befdb52f4b59893a7a300f292) API to proactively query GPU performance information.

// Query GPU performance information.
GamePerformance\_GpuInfo \*gpuInfo = NULL;
GamePerformance\_ErrorCode ret = HMS\_GamePerformance\_QueryGpuInfo(&gpuInfo);
if (ret != GAME\_PERFORMANCE\_SUCCESS) {
    // Troubleshooting.
}

// Obtain indicator data.
int32\_t gpuloadLevel = -1;
int32\_t bandwidth = -1;
int32\_t currentFrequency = -1;
int32\_t fragmentLoadLevel = -1;
int32\_t textureLoadLevel = -1;
int32\_t vertexLoadLevel = -1;
HMS\_GamePerformance\_GpuInfo\_GetGpuLoadLevel(gpuInfo, &gpuloadLevel);
HMS\_GamePerformance\_GpuInfo\_GetBandwidthLoadLevel(gpuInfo, &bandwidth);
HMS\_GamePerformance\_GpuInfo\_GetCurrentFrequency(gpuInfo, &currentFrequency);
HMS\_GamePerformance\_GpuInfo\_GetFragmentLoadLevel(gpuInfo, &fragmentLoadLevel);
HMS\_GamePerformance\_GpuInfo\_GetTextureLoadLevel(gpuInfo, &textureLoadLevel);
HMS\_GamePerformance\_GpuInfo\_GetVertexLoadLevel(gpuInfo, &vertexLoadLevel);

// Free up memory after use.
HMS\_GamePerformance\_DestroyGpuInfo(&gpuInfo);

## Querying CPU Performance Information

In addition to subscribing to device status changes, you can also call the [HMS\_GamePerformance\_QueryCpuInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#gad59832ffd2679db7b1fa8310f586531f) API to proactively query CPU performance information.

// Query CPU performance information.
GamePerformance\_CpuInfo \*cpuInfo = NULL;
GamePerformance\_ErrorCode ret = HMS\_GamePerformance\_QueryCpuInfo(&cpuInfo);
if (ret != GAME\_PERFORMANCE\_SUCCESS) {
    // Troubleshooting.
}

int32\_t cpuLoadLevel = 0;
int32\_t singleThreadLoadLevel = 0;
HMS\_GamePerformance\_CpuInfo\_GetCpuLoadLevel(cpuInfo, &cpuLoadLevel);
HMS\_GamePerformance\_CpuInfo\_GetSingleThreadLoadLevel(cpuInfo, &singleThreadLoadLevel);

// Free up memory after use.
HMS\_GamePerformance\_DestroyCpuInfo(&cpuInfo);

## Querying Temperature Information

In addition to subscribing to device status changes, you can also call the [HMS\_GamePerformance\_QueryThermalInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#gab7cb47e0dc3cce1169a8104827f7edb7) API to proactively query the device temperature control level, temperature trend, operating current in use, recommended operating current, and recommended maximum operating current.

// Query the temperature and temperature trend information.
GamePerformance\_ThermalInfo \*thermalInfo = NULL;
GamePerformance\_ThermalInfoQueryParameters \*parameters = NULL;

// Create query parameters.
HMS\_GamePerformance\_CreateThermalInfoQueryParameters(&parameters);

// Set whether to predict the temperature trend. The value **true** indicates yes and the value **false** indicates no. The default value is **false**.
HMS\_GamePerformance\_ThermalInfoQueryParameters\_SetNeedsPrediction(parameters, true); 

// This parameter indicates the target temperature level for temperature trend prediction, and can be optionally set when **needsPrediction** is **true**. If it is set, the prediction will use this value; otherwise, the default level applies.
HMS\_GamePerformance\_ThermalInfoQueryParameters\_SetTargetThermalLevel(parameters, 4); 

// Query temperature Information.
GamePerformance\_ErrorCode ret = HMS\_GamePerformance\_QueryThermalInfo(parameters, &thermalInfo);
if (ret != GAME\_PERFORMANCE\_SUCCESS) {
    // Troubleshooting.
}
int32\_t margin = INT32\_MIN;
int32\_t trend = INT32\_MIN;
int32\_t level = -1;
int32\_t recommendNormalizedCurrent = 0;
int32\_t nowNormalizedCurrent = 0;
int32\_t recommendMaxNormalizedCurrent = 0;
HMS\_GamePerformance\_ThermalInfo\_GetThermalLevel(thermalInfo, &level);
HMS\_GamePerformance\_ThermalInfo\_GetThermalMargin(thermalInfo, &margin); // A valid value will be returned when **needsPrediction** is **true**.
HMS\_GamePerformance\_ThermalInfo\_GetThermalTrend(thermalInfo, &trend); // A valid value will be returned when **needsPrediction** is **true**.
HMS\_GamePerformance\_ThermalInfo\_GetRecommendNormalizedCurrent(thermalInfo, &recommendNormalizedCurrent);
HMS\_GamePerformance\_ThermalInfo\_GetNowNormalizedCurrent(thermalInfo, &nowNormalizedCurrent);
HMS\_GamePerformance\_ThermalInfo\_GetRecommendMaxNormalizedCurrent(thermalInfo, &recommendMaxNormalizedCurrent);

// Free up memory after use.
HMS\_GamePerformance\_DestroyThermalInfo(&thermalInfo);
HMS\_GamePerformance\_DestroyThermalInfoQueryParameters(&parameters);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/_nagdnuETRqJ0L376PfQnQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48792D1748C8498AC8BD982436FD0FFBD600DF3A7624F3CBE271BCEA65FDE9C4)

Historical data is needed as a basis for calculation when the app queries the temperature change trend. Before calling the [HMS\_GamePerformance\_QueryThermalInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice_game_performance#gab7cb47e0dc3cce1169a8104827f7edb7) API, ensure that the device has been running for at least one minute. Otherwise, error code **1010300001** will be returned.
