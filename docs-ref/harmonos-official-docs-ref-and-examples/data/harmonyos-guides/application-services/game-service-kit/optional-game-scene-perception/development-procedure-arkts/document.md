# Development Procedure (ArkTS)

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/J8v2_13bQHOoFrGuwRr_zw/en-us_image_0000002474151168.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=361B2B8292E3D8FFFFB3B4B2519F78C56F875DE0D3B795C3414F014F983EA4F3)

1.  After the game is launched, it calls the [gamePerformance.init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameperformance#section131971556806) API to initialize the game scene perception module.
2.  After the initialization is successful, the game calls the [gamePerformance.on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameperformance#section17453143012584) API to register a device status change event listener and subscribe to device status change notifications.
3.  The game calls the [gamePerformance.updateGameInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameperformance#section225333655719) API to report game information (including the package, configuration, scene, and network) to the game scene perception module.
4.  The game scene perception module broadcasts game information to the device system.
5.  The device system schedules system resources based on the game information.
6.  The device system notifies the game scene perception module of device status changes.
7.  The game scene perception module reports the device status changes to the game client.
8.  If the subscription is no longer required, the game can call the [gamePerformance.off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameperformance#section3614173614593) API to cancel the device status change event listener.
9.  The game calls the [gamePerformance.getDeviceInfoByScope](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameperformance#section106164517195) API to proactively query device status information from the game scene perception module.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/QHh164jGQiqqcBBFWT-5IQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B0621957F0A01F3A3BDEAC89A8002B6494C976BB3B966083231EC01FB00EE76)

Mali series GPUs do not support GPU performance information collection. GPU performance information cannot be obtained if you call the API for subscribing to or querying device status information.

#### API Description

For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameperformance).

| 
**API Name**

 | 

**Description**

 |
| :-- | :-- |
| 

[init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameperformance#section131971556806)(gamePackageInfo: GamePackageInfo): Promise<void>

 | 

Initializes the game scene perception module. This API returns the result through a promise.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameperformance#section17453143012584)(type: 'deviceStateChanged', callback: Callback<DeviceInfo>): void

 | 

Subscribes to device status changes. This API is used to listen to **deviceStateChanged** events.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameperformance#section060864914495)(type: 'deviceStateChanged', callback: Callback<DeviceInfo>, scope: Array<DeviceInfoType>): void

 | 

Subscribes to device status changes as required. This API is used to listen to **deviceStateChanged** events. The input parameter can specify the type of device status information to be subscribed.

 |
| 

[updateGameInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameperformance#section225333655719)<T extends BaseGameInfo>(gameInfo: T): Promise<void>

 | 

Updates game information (including the package, configuration, scene, and network). This API returns the result through a promise.

 |
| 

[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameperformance#section3614173614593)(type: 'deviceStateChanged', callback?: Callback<DeviceInfo>): void

 | 

Unsubscribes from device status changes. This API is used to unsubscribe from **deviceStateChanged** events.

 |
| 

[getDeviceInfoByScope](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameperformance#section106164517195)(scope: Array<DeviceInfoParameter>): Promise<DeviceInfo>

 | 

Queries device status information.

 |

#### Integration Procedure

## Importing Modules

Import Game Service Kit and common modules.

import { gamePerformance } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

## Performing Initialization

After related modules are imported, call the [init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameperformance#section131971556806) API to initialize the game scene perception module.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/6L42JbfBTmKZu8asXJB3pA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB1D1FFBB4911C2D95343085B9272B2522092F3702C0FA00BC9E70623E941B25)

Before calling other APIs, you must first call the **init** API. If the initialization is not performed or fails, other APIs cannot be called.

let gamePackageInfo: gamePerformance.GamePackageInfo = {
  messageType: 0,
    bundleName: "com.example.demo", // Example. Replace it with the actual game package name.
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

## Subscribing to Device Status Changes

You can call the [on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameperformance#section17453143012584) API to subscribe to device status change events and obtain device status change notifications (for example, device temperature control level).

function onDeviceStateChange(data:gamePerformance.DeviceInfo) {
  // Device details.
  hilog.info(0x0001, 'demo', \`device state changed. tempLevel is ${data.tempLevel}\`);
}

// Subscribe to **deviceStateChanged** events.
try {
  gamePerformance.on('deviceStateChanged', onDeviceStateChange);
} catch (error) {
  // Subscription failed.
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', \`Failed to subscribe. Code: ${err.code}, message: ${err.message}\`);
}

Currently, two types of device status data can be subscribed to: GPU and temperature change trend. You can also call the [on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameperformance#section060864914495) API to subscribe to the data as required. For example, you can subscribe to only GPU data.

function onDeviceStateChange(data:gamePerformance.DeviceInfo) {
// The data contains only **gpuInfo**.
  hilog.info(0x0001, 'demo', \`device state changed. tempLevel is ${data.tempLevel}\`);
}

// Subscribe to **deviceStateChanged** events.
try {
  let types:Array<gamePerformance.DeviceInfoType> = \[gamePerformance.DeviceInfoType.GPU\];
  gamePerformance.on('deviceStateChanged', onDeviceStateChange, types);
} catch (error) {
  // Subscription failed.
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', \`Failed to subscribe. Code: ${err.code}, message: ${err.message}\`);
}

## Reporting Game Information

After the initialization is successful, the [updateGameInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameperformance#section225333655719) API can be called to report game information (including the package, configuration, scene, and network). Call the [addGameCustomData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameperformance#section72524718166) API to report custom data.

// Updating game scene information is used as an example.
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
    // Failed to update the game scene information.
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', \`Failed to update. Code: ${err.code}, message: ${err.message}\`);
}

## Unsubscribing from Device Status Changes

If the subscription is no longer required, call the [off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameperformance#section3614173614593) API to unsubscribe from device status changes.

function onDeviceStateChange(data:gamePerformance.DeviceInfo) {
  // Device details.
  hilog.info(0x0001, 'demo', \`device state changed. tempLevel is ${data.tempLevel}\`);
}

// Unsubscribe from **deviceStateChanged** events.
try {
  gamePerformance.off('deviceStateChanged', onDeviceStateChange);
} catch (error) {
  // Unsubscription failed.
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', \`Failed to unsubscribe. Code: ${err.code}, message: ${err.message}\`);
}

// Unsubscribe from all **deviceStateChanged** events.
try {
  gamePerformance.off("deviceStateChanged");
} catch (error) {
  // Unsubscription failed.
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', \`Failed to unsubscribe. Code: ${err.code}, message: ${err.message}\`);
}

## Querying Device Status Information

In addition to subscribing to device status changes, you can also call the [getDeviceInfoByScope](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameperformance#section106164517195) API to actively query device status.

// Query device status
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

The active query API also supports on-demand query, such as querying only temperature change trend data.

// Query only the device temperature data.
try {
  let thermalParam: gamePerformance.DeviceInfoParameter = {
    deviceInfoType: gamePerformance.DeviceInfoType.THERMAL     
  }
  let gameInfos: Array<gamePerformance.DeviceInfoParameter> = \[thermalParam\];
  gamePerformance.getDeviceInfoByScope(gameInfos).then((deviceInfo:gamePerformance.DeviceInfo) => {
    // The query result does not contain **gpuInfo**.
    hilog.info(0x0001, 'demo', \`Succeeded in querying device info. tempLevel is ${deviceInfo.tempLevel}\`);
  });
} catch (error) {
  // Query failed.
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', \`Failed to query. Code: ${err.code}, message: ${err.message}\`);
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/QTiB19VUQRi9QCwQFl018A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53CEEB877ACBC7C2F696BB6408E774F0560486A0F67CF84E7C6C38A945366624)

Historical data is needed as a basis for calculation when the app queries the temperature change trend. Before calling this API, ensure that the device was started at least 1 minute before. Otherwise, error code **1010300003** will be returned.
