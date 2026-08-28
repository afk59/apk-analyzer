# @ohos.bluetoothManager (Bluetooth)

The **Bluetooth** module provides classic Bluetooth capabilities and Bluetooth Low Energy (BLE) scan and advertising.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/HLyBdb9MRASVRaPN3E31xw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39B1A770D4AEC7A0425FD54AE74D77742DB31878319757FBCA81A1D66492A112)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs provided by this module are no longer maintained since API version 10. You are advised to use profile APIs of [@ohos.bluetooth.ble](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md).

#### Modules to Import

import { bluetoothManager } from '@kit.ConnectivityKit';

#### bluetoothManager.enableBluetooth(deprecated)

enableBluetooth(): void

Enables Bluetooth.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/x545z-XsR2WqGEImCK2kxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A62983EBFA0D090EE6E90138292BE718602D423DC22FFF6667D449360D73A775)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [access.enableBluetooth](../../arkts-apis/ohos-bluetooth-access-bluetooth-access-module/document.md#accessenablebluetooth) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    bluetoothManager.enableBluetooth();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.disableBluetooth(deprecated)

disableBluetooth(): void

Disables Bluetooth.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/RRlxl3LTQEuSVASCHZGayg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C5379BB21C7C5198C6DD2A879E0B430EB5EC3CAA4D9C409ED031E49F5577D1CD)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [access.disableBluetooth](../../arkts-apis/ohos-bluetooth-access-bluetooth-access-module/document.md#accessdisablebluetooth) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    bluetoothManager.disableBluetooth();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ", errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.getLocalName(deprecated)

getLocalName(): string

Obtains the name of the local Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/503WzKV4QkGCchCjDjj86Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0ED05D9878ADC023652950667EE1EB7C5E837DA84383E1FC0BAC4D0D53A2446E)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.getLocalName](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectiongetlocalname) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Name of the local Bluetooth device obtained. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let localName: string = bluetoothManager.getLocalName();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.getState(deprecated)

getState(): BluetoothState

Obtains the Bluetooth state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/pBRDfI9PSRG1fB0WIbRbnw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2E7872C4B120EAA8BA9998A1D1EA49F5BEA354B2DB10D40003CCF18508C526C)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [access.getState](../../arkts-apis/ohos-bluetooth-access-bluetooth-access-module/document.md#accessgetstate) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [BluetoothState](#bluetoothstatedeprecated) | Bluetooth state obtained. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let state: bluetoothManager.BluetoothState = bluetoothManager.getState();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.getBtConnectionState(deprecated)

getBtConnectionState(): ProfileConnectionState

Obtains the local profile connection status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/gGAokNqJQSiCyE__ukuyng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0371FB226ED15F79B1EF85479A0129AF9954B1AA2BB241D1805EAA1C4864DF3A)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.getProfileConnectionState](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectiongetprofileconnectionstate) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [ProfileConnectionState](#profileconnectionstatedeprecated) | Profile connection state obtained. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let connectionState: bluetoothManager.ProfileConnectionState = bluetoothManager.getBtConnectionState();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.setLocalName(deprecated)

setLocalName(name: string): void

Sets the name of the local Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/0E9fOojXSFeWKAPScebO2Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B3C7ECB1AB7A85D555C99AEA6AA54F1916A52EF834ACF46C7D09F9997936F5A)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.setLocalName](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectionsetlocalnamedeprecated) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Bluetooth device name to set. It cannot exceed 248 bytes. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    bluetoothManager.setLocalName('device\_name');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.pairDevice(deprecated)

pairDevice(deviceId: string): void

Initiates Bluetooth pairing.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/YihQ70SuQr-vam4nBD172A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43D1360C3F2AC4A92BFF49B2EF2E142415D7C0F3C7DE9D2039F92C9B3DE61343)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.pairDevice](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectionpairdevice) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the remote device to pair, for example, XX:XX:XX:XX:XX:XX. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    // The address can be scanned.
    bluetoothManager.pairDevice("XX:XX:XX:XX:XX:XX");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.getProfileConnectionState(deprecated)

getProfileConnectionState(profileId: ProfileId): ProfileConnectionState

Obtains the connection status of the specified profile.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/tvvqJ4YqRneLSkV3GamXUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6391D163B4264596934F5D4092BBFFA3D266C63F066A9D8239A7C56259188D60)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.getProfileConnectionState](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectiongetprofileconnectionstate) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| profileId | ProfileId | Yes | ID of the profile to obtain, for example, **PROFILE\_A2DP\_SOURCE**. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ProfileConnectionState](#profileconnectionstatedeprecated) | Profile connection state obtained. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let result: bluetoothManager.ProfileConnectionState = bluetoothManager.getProfileConnectionState(bluetoothManager.ProfileId.PROFILE\_A2DP\_SOURCE);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.getRemoteDeviceName(deprecated)

getRemoteDeviceName(deviceId: string): string

Obtains the name of the remote Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/HBkoCG5TRz2kOeGOgCXS3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5778E1D68BF666E89930FB0AA24EBCA75633845F2D8C6D70DD746CF5946BD30D)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.getRemoteDeviceName](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectiongetremotedevicename) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the remote device, for example, XX:XX:XX:XX:XX:XX. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Device name (a string) obtained. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let remoteDeviceName: string = bluetoothManager.getRemoteDeviceName("XX:XX:XX:XX:XX:XX");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.getRemoteDeviceClass(deprecated)

getRemoteDeviceClass(deviceId: string): DeviceClass

Obtains the class of the remote Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/5WCK4vmLS-C-aoKOClPCKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7699B6A027D30C632C93149D5AA27927385325F06ECA4A74D478573B865ED029)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.getRemoteDeviceClass](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectiongetremotedeviceclass) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the remote device, for example, XX:XX:XX:XX:XX:XX. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DeviceClass](#deviceclassdeprecated) | Class of the remote device obtained. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let remoteDeviceClass: bluetoothManager.DeviceClass  = bluetoothManager.getRemoteDeviceClass("XX:XX:XX:XX:XX:XX");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.getPairedDevices(deprecated)

getPairedDevices(): Array<string>

Obtains the paired devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/DKWMzVPFSpmzMEnAdeKWfQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=05C3E2B05DB69AA0D068B3EFA1375ED0C6C69476F6A969D079710CB17773DB0A)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.getPairedDevices](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectiongetpaireddevices) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | Addresses of the paired Bluetooth devices. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let devices: Array<string> = bluetoothManager.getPairedDevices();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.setBluetoothScanMode(deprecated)

setBluetoothScanMode(mode: ScanMode, duration: number): void

Sets the Bluetooth scan mode so that the device can be discovered by a remote device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/Pz0CCpQNSweMCOp4UWe3LA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8946C6749E60D2DE066BDFAEE3909BECFBCBB2A82DD00BFA433140A51E31D23A)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.setBluetoothScanMode](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectionsetbluetoothscanmode) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [ScanMode](#scanmodedeprecated) | Yes | Bluetooth scan mode to set. |
| duration | number | Yes | Duration (in ms) in which the device can be discovered. The value **0** indicates unlimited time. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    // The device can be discovered and connected only when the discoverable and connectable mode is used.
    bluetoothManager.setBluetoothScanMode(bluetoothManager.ScanMode.SCAN\_MODE\_CONNECTABLE\_GENERAL\_DISCOVERABLE, 100);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.getBluetoothScanMode(deprecated)

getBluetoothScanMode(): ScanMode

Obtains the Bluetooth scan mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/brkFkjRzTZKBYg9gPAwv5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FF8107BCB06F6AA0A1152EBB5244354F748B18D65E410A6B5FDE1CDA58B2031)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.getBluetoothScanMode](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectiongetbluetoothscanmode) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [ScanMode](#scanmodedeprecated) | Bluetooth scan mode to set. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let scanMode: bluetoothManager.ScanMode = bluetoothManager.getBluetoothScanMode();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.startBluetoothDiscovery(deprecated)

startBluetoothDiscovery(): void

Starts Bluetooth scan to discover remote devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/rkbtH67cTg2RWpXPTsqjEA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D130615B67A4342F59C34A1A4D0F0E0E03C6D7092D75A17A869C11465CFB3665)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.startBluetoothDiscovery](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectionstartbluetoothdiscovery) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
let deviceId: Array<string>;
function onReceiveEvent(data: Array<string>) {
    deviceId = data;
}
try {
    bluetoothManager.on('bluetoothDeviceFind', onReceiveEvent);
    bluetoothManager.startBluetoothDiscovery();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.stopBluetoothDiscovery(deprecated)

stopBluetoothDiscovery(): void

Stops Bluetooth scan.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/Qq6kW8uuSsiN8LSHGRlEvw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=523CEB59285DF849C78673DA0EA30F3FEE1EA75B1ACED27CA8EE9DD0029A40D4)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.stopBluetoothDiscovery](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectionstopbluetoothdiscovery) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    bluetoothManager.stopBluetoothDiscovery();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.setDevicePairingConfirmation(deprecated)

setDevicePairingConfirmation(device: string, accept: boolean): void

Sets the device pairing confirmation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/ryq0ylcMRW6SAcDua2OFDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5FF69C2F81E42A08D4D667874333E473BC4D4AFA0306898D496B68F94144A3B6)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.setDevicePairingConfirmation](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectionsetdevicepairingconfirmation) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH and ohos.permission.MANAGE\_BLUETOOTH (available only for system applications)

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | Address of the remote device, for example, XX:XX:XX:XX:XX:XX. |
| accept | boolean | Yes | Whether to accept the pairing request. The value **true** means to accept the pairing request, and the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
// Subscribe to the pinRequired event and configure the pairing confirmation after receiving a pairing request from the remote device.
function onReceivePinRequiredEvent(data: bluetoothManager.PinRequiredParam) { // data is the input parameter for the pairing request.
    console.info('pin required  = '+ JSON.stringify(data));
    bluetoothManager.setDevicePairingConfirmation(data.deviceId, true);
}
try {
    bluetoothManager.on("pinRequired", onReceivePinRequiredEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.on('bluetoothDeviceFind')(deprecated)

on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void

Subscribes to the Bluetooth device discovery events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/4y96rgusRtGULzXLw-W8yQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC7705CAAD39AC6825E85396CA66A48A85B772E5736A70201FC595B88CFC3298)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.on('bluetoothDeviceFind')](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectiononbluetoothdevicefind) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **bluetoothDeviceFind**, which indicates an event of discovering a Bluetooth device. |
| callback | Callback<Array<string>> | Yes | Callback used to return the discovered devices. You need to implement this callback. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: Array<string>) { // data is an array of Bluetooth device addresses.
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('bluetoothDeviceFind', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.off('bluetoothDeviceFind')(deprecated)

off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void

Unsubscribes from the Bluetooth device discovery events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/Z5RcO51BQy67GgGG17poPA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DAEA48B0FFC59FFD070913F7605349E6986F6B479FD1C30EE38104B7DBE914C6)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.off('bluetoothDeviceFind')](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectionoffbluetoothdevicefind) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **bluetoothDeviceFind**, which indicates an event of discovering a Bluetooth device. |
| callback | Callback<Array<string>> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for the specified **type**. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: Array<string>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('bluetoothDeviceFind', onReceiveEvent);
    bluetoothManager.off('bluetoothDeviceFind', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.on('pinRequired')(deprecated)

on(type: 'pinRequired', callback: Callback<PinRequiredParam>): void

Subscribes to the pairing request events of the remote Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/eIO8H-FURKqOAb52bv1k3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B20043BF20F98B6D0536989D436CD936EA7FB7FB93473FB43FA51ADDB211056B)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.on('pinRequired')](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectiononpinrequired) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **pinRequired**, which indicates a pairing request event. |
| callback | Callback<[PinRequiredParam](#pinrequiredparamdeprecated)\> | Yes | Callback used to return the pairing request. You need to implement this callback. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.PinRequiredParam) { // data is the pairing request parameter.
    console.info('pin required = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('pinRequired', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.off('pinRequired')(deprecated)

off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void

Unsubscribes from the pairing request events of the remote Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/n2GO18mNS1qcaA2I0NXiug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD214B7C666406B56359404083E66EE0DF36B500093392917CF719699BAA898C)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.off('pinRequired')](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectionoffpinrequired) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **pinRequired**, which indicates a pairing request event. |
| callback | Callback<[PinRequiredParam](#pinrequiredparamdeprecated)\> | No | Callback to unregister. The input parameter is the pairing request parameter. If this parameter is not set, this API unregisters all callbacks for the specified **type**. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.PinRequiredParam) {
    console.info('pin required = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('pinRequired', onReceiveEvent);
    bluetoothManager.off('pinRequired', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.on('bondStateChange')(deprecated)

on(type: 'bondStateChange', callback: Callback<BondStateParam>): void

Subscribes to the Bluetooth pairing state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/gANrWizmSruQVjn7m_UMDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A5C548337CF527BCCA57B558319120BD597C912E94F56372F15B80C95E256A6)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.on('bondStateChange')](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectiononbondstatechange) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **bondStateChange**, which indicates a Bluetooth pairing state change event. |
| callback | Callback<[BondStateParam](#bondstateparamdeprecated)\> | Yes | Callback used to return the pairing state. You need to implement this callback. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.BondStateParam) { // data, as the input parameter of the callback, indicates the pairing state.
    console.info('pair state = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('bondStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.off('bondStateChange')(deprecated)

off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void

Unsubscribes from the Bluetooth pairing state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/lVAVDXM9RHiqdF7TGIHS3A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B57F0B327AB2EA98B7C164098CA2AF2321C0E19ED4738B14275EBBA1FF2A09C)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.off('bondStateChange')](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectionoffbondstatechange) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **bondStateChange**, which indicates a Bluetooth pairing state change event. |
| callback | Callback<[BondStateParam](#bondstateparamdeprecated)\> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for the specified **type**. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.BondStateParam) {
    console.info('bond state = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('bondStateChange', onReceiveEvent);
    bluetoothManager.off('bondStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.on('stateChange')(deprecated)

on(type: 'stateChange', callback: Callback<BluetoothState>): void

Subscribes to Bluetooth state events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/KTmeyWQ7Q0GWeTFCoGl06w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD1B3703372F0C098382E8ED005AE8B1BE011DCD93A68C2F10A67251FA623EE4)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [access.on('stateChange')](../../arkts-apis/ohos-bluetooth-access-bluetooth-access-module/document.md#accessonstatechange) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **stateChange**, which indicates a Bluetooth state change event. |
| callback | Callback<[BluetoothState](#bluetoothstatedeprecated)\> | Yes | Callback used to return the Bluetooth connection state. You need to implement this callback. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.BluetoothState) {
    console.info('bluetooth state = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('stateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.off('stateChange')(deprecated)

off(type: 'stateChange', callback?: Callback<BluetoothState>): void

Unsubscribes from Bluetooth state events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/t26m4sd3SNSkNTYKr6wybA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A90CDCAB26EC74325DAB3B9977FD91BADF8923280D47D13C2F8FBDA9E5FD234)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [access.off('stateChange')](../../arkts-apis/ohos-bluetooth-access-bluetooth-access-module/document.md#accessoffstatechange) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **stateChange**, which indicates a Bluetooth state change event. |
| callback | Callback<[BluetoothState](#bluetoothstatedeprecated)\> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for the specified **type**. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.BluetoothState) {
    console.info('bluetooth state = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('stateChange', onReceiveEvent);
    bluetoothManager.off('stateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### bluetoothManager.sppListen(deprecated)

sppListen(name: string, option: SppOption, callback: AsyncCallback<number>): void

Creates a server listening socket.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/7iAx8b17RX-_cCKdYvUSkw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2A8845C46ABBA8120309F6A2D73B6DC0AC01C23F853CAC217E2850737C7188F)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [socket.sppListen](../../arkts-apis/ohos-bluetooth-socket-bluetooth-socket-module/document.md#socketspplisten) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the service. |
| option | [SppOption](#sppoptiondeprecated) | Yes | Serial port profile (SPP) listening configuration. |
| callback | AsyncCallback<number> | Yes | Callback used to return the server socket ID. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let serverNumber = -1;
function serverSocket(code: BusinessError, number: number) {
  console.info(\`bluetooth error code: ${code.code}\`);
  if (code.code == 0) {
    console.info(\`bluetooth serverSocket Number: ${number}\`);
    serverNumber = number;
  }
}

let sppOption: bluetoothManager.SppOption = {uuid: '00001810-0000-1000-8000-00805F9B34FB', secure: false, type: 0};
try {
    bluetoothManager.sppListen('server1', sppOption, serverSocket);
} catch (err) {
    console.error(\`errCode: ${err.code}, errMessage: ${err.message}\`);
}

#### bluetoothManager.sppAccept(deprecated)

sppAccept(serverSocket: number, callback: AsyncCallback<number>): void

Listens for a connection to be made to this socket from the client and accepts it.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/ZO1p8HVkR7eTUDqEUJnhkA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9BCB295BB0D5E3C12AD4C12823C3C0B5404DC9436F9A547F38E7D3C8D40CD8A)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [socket.sppAccept](../../arkts-apis/ohos-bluetooth-socket-bluetooth-socket-module/document.md#socketsppaccept) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| serverSocket | number | Yes | Server socket ID. |
| callback | AsyncCallback<number> | Yes | Callback used to return the client socket ID. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let serverNumber = -1;
function serverSocket(code: BusinessError, number: number) {
  console.info(\`bluetooth error code: ${code.code}\`);
  if (code.code == 0) {
    console.info(\`bluetooth serverSocket Number: ${number}\`);
    serverNumber = number;
  }
}
let clientNumber = -1;
function acceptClientSocket(code: BusinessError, number: number) {
  console.info(\`bluetooth error code: ${code.code}\`);
  if (code.code == 0) {
    console.info(\`bluetooth clientSocket Number: ${number}\`);
    // The obtained clientNumber is used as the socket ID for subsequent read/write operations on the server.
    clientNumber = number;
  }
}
try {
    bluetoothManager.sppAccept(serverNumber, acceptClientSocket);
} catch (err) {
    console.error(\`errCode: ${err.code}, errMessage: ${err.message}\`);
}

#### bluetoothManager.sppConnect(deprecated)

sppConnect(device: string, option: SppOption, callback: AsyncCallback<number>): void

Initiates an SPP connection to a remote device from the client.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/sfXis5mhTvyt1QKea9IXUw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95EC94DF9E930B5206445ED9552FCEE5F3B2CC30F2E675149B171735755BF3BC)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [socket.sppConnect](../../arkts-apis/ohos-bluetooth-socket-bluetooth-socket-module/document.md#socketsppconnect) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | Address of the remote device, for example, XX:XX:XX:XX:XX:XX. |
| option | [SppOption](#sppoptiondeprecated) | Yes | Configuration for connecting to the SPP client. |
| callback | AsyncCallback<number> | Yes | Callback used to return the client socket ID. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let clientNumber = -1;
function clientSocket(code: BusinessError, number: number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(\`bluetooth serverSocket Number: ${number}\`);
  // The obtained clientNumber is used as the socket ID for subsequent read/write operations on the client.
  clientNumber = number;
}
let sppOption: bluetoothManager.SppOption = {uuid: '00001810-0000-1000-8000-00805F9B34FB', secure: false, type: 0};
try {
    bluetoothManager.sppConnect('XX:XX:XX:XX:XX:XX', sppOption, clientSocket);
} catch (err) {
    console.error(\`errCode: ${err.code}, errMessage: ${err.message}\`);
}

#### bluetoothManager.sppCloseServerSocket(deprecated)

sppCloseServerSocket(socket: number): void

Closes the listening socket of the server.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/zZU_y0gSShaqbt9sxh_JQw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A220C7D684CF5600B75B917742662C61B276D5EFC723E02905F1BAF7878916AC)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [socket.sppCloseServerSocket](../../arkts-apis/ohos-bluetooth-socket-bluetooth-socket-module/document.md#socketsppcloseserversocket) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| socket | number | Yes | ID of the listening socket on the server. The ID is obtained by **sppListen**. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let serverNumber = -1;
function serverSocket(code: BusinessError, number: number) {
  console.info(\`bluetooth error code: ${code.code}\`);
  if (code.code == 0) {
    console.info(\`bluetooth serverSocket Number: ${number}\`);
    serverNumber = number;
  }
}
try {
    bluetoothManager.sppCloseServerSocket(serverNumber);
} catch (err) {
    console.error(\`errCode: ${err.code}, errMessage: ${err.message}\`);
}

#### bluetoothManager.sppCloseClientSocket(deprecated)

sppCloseClientSocket(socket: number): void

Closes the client socket.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/nlhliewATPKY_ix-dE-k5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C941CAFA1D6C80E16FC28DCBD3B876B23CC7629C113AD7321F373CBA421BBC98)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [socket.sppCloseClientSocket](../../arkts-apis/ohos-bluetooth-socket-bluetooth-socket-module/document.md#socketsppcloseclientsocket) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| socket | number | Yes | Client socket ID, which is obtained by **sppAccept** or **sppConnect**. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code: BusinessError, number: number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(\`bluetooth serverSocket Number: ${number}\`);
  // The obtained clientNumber is used as the socket ID for subsequent read/write operations on the client.
  clientNumber = number;
}
try {
    bluetoothManager.sppCloseClientSocket(clientNumber);
} catch (err) {
    console.error(\`errCode: ${err.code}, errMessage: ${err.message}\`);
}

#### bluetoothManager.sppWrite(deprecated)

sppWrite(clientSocket: number, data: ArrayBuffer): void

Writes data to the remote device through the socket.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/UFPQlsT_RaCLihT3pX2giw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7DDCFF5F98DFE0B1B82111FEC2EDF1E51B38DAC3196557A1711D32D5DFE62249)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [socket.sppWrite](../../arkts-apis/ohos-bluetooth-socket-bluetooth-socket-module/document.md#socketsppwrite) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| clientSocket | number | Yes | Client socket ID, which is obtained by **sppAccept** or **sppConnect**. |
| data | ArrayBuffer | Yes | Data to write. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2901054 | IO error. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code: BusinessError, number: number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(\`bluetooth serverSocket Number: ${number}\`);
  // The obtained clientNumber is used as the socket ID for subsequent read/write operations on the client.
  clientNumber = number;
}
let arrayBuffer = new ArrayBuffer(8);
let data = new Uint8Array(arrayBuffer);
data\[0\] = 123;
try {
    bluetoothManager.sppWrite(clientNumber, arrayBuffer);
} catch (err) {
    console.error(\`errCode: ${err.code}, errMessage: ${err.message}\`);
}

#### bluetoothManager.on('sppRead')(deprecated)

on(type: 'sppRead', clientSocket: number, callback: Callback<ArrayBuffer>): void

Subscribes to the SPP read request events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/BIMQsQU6SS29fO6a3DaHDg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=104A3BCD726E4E597D56A2F7E7E0D3C599059299B4889854775D8A80428B5187)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [socket.on('sppRead')](../../arkts-apis/ohos-bluetooth-socket-bluetooth-socket-module/document.md#socketonsppread) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **sppRead**, which indicates an SPP read request event. |
| clientSocket | number | Yes | Client socket ID, which is obtained by **sppAccept** or **sppConnect**. |
| callback | Callback<ArrayBuffer> | Yes | Callback used to return the data read. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2901054 | IO error. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code: BusinessError, number: number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(\`bluetooth serverSocket Number: ${number}\`);
  // The obtained clientNumber is used as the socket ID for subsequent read/write operations on the client.
  clientNumber = number;
}
function dataRead(dataBuffer: ArrayBuffer) {
  let data = new Uint8Array(dataBuffer);
  console.info(\`bluetooth data is: ${data\[0\]}\`);
}
try {
    bluetoothManager.on('sppRead', clientNumber, dataRead);
} catch (err) {
    console.error(\`errCode: ${err.code}, errMessage: ${err.message}\`);
}

#### bluetoothManager.off('sppRead')(deprecated)

off(type: 'sppRead', clientSocket: number, callback?: Callback<ArrayBuffer>): void

Unsubscribes from the SPP read request events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/hWFHzOYjTYazC1ycr-7WxA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5008467DA0D61BDBBB342CB620617A886D4D0CE8804E909E62E0959B10F88C5E)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [socket.off('sppRead')](../../arkts-apis/ohos-bluetooth-socket-bluetooth-socket-module/document.md#socketoffsppread) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **sppRead**, which indicates an SPP read request event. |
| clientSocket | number | Yes | Client socket ID, which is obtained by **sppAccept** or **sppConnect**. |
| callback | Callback<ArrayBuffer> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for the specified **type**. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code: BusinessError, number: number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(\`bluetooth serverSocket Number: ${number}\`);
  // The obtained clientNumber is used as the socket ID for subsequent read/write operations on the client.
  clientNumber = number;
}
try {
    bluetoothManager.off('sppRead', clientNumber);
} catch (err) {
    console.error(\`errCode: ${err.code}, errMessage: ${err.message}\`);
}

#### bluetoothManager.getProfileInstance(deprecated)

getProfileInstance(profileId: ProfileId): A2dpSourceProfile | HandsFreeAudioGatewayProfile | HidHostProfile | PanProfile

Obtains a profile instance. API version 9 is added with **HidHostProfile** and **PanProfile**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/c8cA9kdcS3u5P7s9FpSGoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D849409D1756A1959DD96512B87273A81406CCDC9A51D5B77B83B066F748BB2F)

This API is supported since API version 9 and deprecated since API version 10.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| profileId | [ProfileId](#profileiddeprecated) | Yes | ID of the profile to obtain, for example, **PROFILE\_A2DP\_SOURCE**. |

**Return value**

| Type | Description |
| :-- | :-- |
| [A2dpSourceProfile](#a2dpsourceprofile) | [HandsFreeAudioGatewayProfile](#handsfreeaudiogatewayprofiledeprecated) | [HidHostProfile](#hidhostprofiledeprecated) | [PanProfile](#panprofile) | Profile instance obtained, which can be **A2dpSourceProfile**, **HandsFreeAudioGatewayProfile**, **HidHostProfile**, or **PanProfile**. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let hidHost: bluetoothManager.HidHostProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE\_HID\_HOST);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### BLE

Provides APIs for operating and managing Bluetooth.

#### \[h2\]createGattServer(deprecated)

createGattServer(): GattServer

Creates a **GattServer** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/H3Dz4213Qb-lOgH7bmjSlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ECF43127B30C7A4F5674BC59244E4A85F89F3F522F3D5CBC546AB7C4E23A88CB)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.createGattServer](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#blecreategattserver) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [GattServer](#gattserver) | **GattServer** instance created. Before using an API of this class, you must create a **GattSever** instance. |

**Example**

let gattServer: bluetoothManager.GattServer  = bluetoothManager.BLE.createGattServer();

#### \[h2\]createGattClientDevice(deprecated)

createGattClientDevice(deviceId: string): GattClientDevice

Creates a **GattClientDevice** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/KqOrBHWxREqK2cTWXH99-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A6A9257BA39A8B84A35677C00F31ED9B685A58D8586B71291F2368BB60F1160)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.createGattClientDevice](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#blecreategattclientdevice) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the remote device, for example, XX:XX:XX:XX:XX:XX. |

**Return value**

| Type | Description |
| :-- | :-- |
| [GattClientDevice](#gattclientdevice) | **GattClientDevice** instance created. Before using an API of the client, you must create a **GattClientDevice** instance. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let device: bluetoothManager.GattClientDevice = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]getConnectedBLEDevices(deprecated)

getConnectedBLEDevices(): Array<string>

Obtains the BLE devices connected to this device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/NJUxZ0XjT6irExDgmEfF7Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77F6447496CCD6445700994E25B1AF6FFD99CB885EDCCE5D886E7E62123A3DD3)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.getConnectedBLEDevices](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#blegetconnectedbledevices) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | Addresses of the BLE devices connected to this device. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let result: Array<string>  = bluetoothManager.BLE.getConnectedBLEDevices();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]startBLEScan(deprecated)

startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void

Starts a BLE scan.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/5AaLOAGfRumO346ekZnx8g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=721ED8F9924B3DB3E8A71EBD9D4FBCF88F389E7BF4DEDED83F25576FD3099339)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.startBLEScan](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#blestartblescan) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filters | Array<[ScanFilter](#scanfilterdeprecated)\> | Yes | Criteria for filtering the scan result. Set this parameter to **null** if you do not want to filter the scan result. |
| options | [ScanOptions](#scanoptionsdeprecated) | No | Scan options. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: Array<bluetoothManager.ScanResult>) {
    console.info('BLE scan device find result = '+ JSON.stringify(data));
}
try {
    bluetoothManager.BLE.on("BLEDeviceFind", onReceiveEvent);
    let scanfilter: bluetoothManager.ScanFilter = {
        deviceId:"XX:XX:XX:XX:XX:XX",
        name:"test",
        serviceUuid:"00001888-0000-1000-8000-00805f9b34fb"
    };
    let scanoptions: bluetoothManager.ScanOptions = {
        interval: 500,
        dutyMode: bluetoothManager.ScanDuty.SCAN\_MODE\_LOW\_POWER,
        matchMode: bluetoothManager.MatchMode.MATCH\_MODE\_AGGRESSIVE,
    }
    bluetoothManager.BLE.startBLEScan(\[scanfilter\], scanoptions);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]stopBLEScan(deprecated)

stopBLEScan(): void

Stops the BLE scan.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/Y36W6fuhRuOl9xaQoeHS-w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07B7A6D5ED1834B85D898173ACD780407543F540B7FF771C56452C8688FD31DC)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.stopBLEScan](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#blestopblescan) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    bluetoothManager.BLE.stopBLEScan();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]on('BLEDeviceFind')(deprecated)

on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void

Subscribe to the BLE device discovery events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/_YN5jtAaRwChffaleP25gQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A82A40A7988DCCF8D4505592DB09FCC7EBC071A3FDE246464C5BAEFAAA489445)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.on('BLEDeviceFind')](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#bleonbledevicefind) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **BLEDeviceFind**, which indicates an event of discovering a BLE device. |
| callback | Callback<Array<[ScanResult](#scanresultdeprecated)\>> | Yes | Callback used to return the discovered devices. You need to implement this callback. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: Array<bluetoothManager.ScanResult>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    bluetoothManager.BLE.on('BLEDeviceFind', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]off('BLEDeviceFind')(deprecated)

off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void

Unsubscribes from the BLE device discovery events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/tCVIof44R7iMWkrA6XbEag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE3FE649379499E7E4107DF7B582740B3FB2909A60565D0F759E32D5C90CED54)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.off('BLEDeviceFind')](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#bleoffbledevicefind) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **BLEDeviceFind**, which indicates an event of discovering a BLE device. |
| callback | Callback<Array<[ScanResult](#scanresultdeprecated)\>> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for the specified **type**. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: Array<bluetoothManager.ScanResult>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    bluetoothManager.BLE.on('BLEDeviceFind', onReceiveEvent);
    bluetoothManager.BLE.off('BLEDeviceFind', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### BaseProfile

Provides the profile base class.

#### \[h2\]getConnectionDevices(deprecated)

getConnectionDevices(): Array<string>

Obtains the connected devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/wWmN_cAaSoK4kuT3ugbGfA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3894D6CDB2EA2C9DF0212B17746D2060CD7B0DE73A23A4EE1047AEC88814D274)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [baseProfile.getConnectedDevices](../../arkts-apis/ohos-bluetooth-baseprofile-bluetooth-baseprofile-module/document.md#baseprofilegetconnecteddevices) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | Addresses of the connected devices. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE\_A2DP\_SOURCE) as bluetoothManager.A2dpSourceProfile;
    let retArray: Array<string> = a2dpSrc.getConnectionDevices();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]getDeviceState(deprecated)

getDeviceState(device: string): ProfileConnectionState

Obtains the connection state of the profile.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/s7IDsm7ASmGjWc3ilP_26A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84D0A22E2A6AAD3E8DD4EA60E810A064CA8929FD4E858FD4D75BEFF4FFD2E51F)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [baseProfile.getConnectionState](../../arkts-apis/ohos-bluetooth-baseprofile-bluetooth-baseprofile-module/document.md#baseprofilegetconnectionstate) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | Address of the target device. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ProfileConnectionState](#profileconnectionstatedeprecated) | Profile connection state obtained. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE\_A2DP\_SOURCE) as bluetoothManager.A2dpSourceProfile;
    let ret: bluetoothManager.ProfileConnectionState = a2dpSrc.getDeviceState('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### A2dpSourceProfile

Before using an API of **A2dpSourceProfile**, you need to create an instance of this class by using **getProfile()**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/KYIh-va3TNe9PYLwE8GwSQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1B7830A5AD6E22345753665804C28F8DCD87D14303922A82A558AB4798125FF)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [a2dp.A2dpSourceProfile](../../arkts-apis/ohos-bluetooth-a2dp-bluetooth-a2dp-module/document.md#a2dpsourceprofile) instead.

#### \[h2\]connect(deprecated)

connect(device: string): void

Sets up an Advanced Audio Distribution Profile (A2DP) connection.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/GVjHymCtTXSnDMzhExB6yg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E0B88D426B122541B76AAA0F94D687C0E51811B35C1DB0DC58CEB41025D80A9)

This API is supported since API version 9 and deprecated since API version 10. The substitute API is available only for system applications.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | Address of the target device. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE\_A2DP\_SOURCE) as bluetoothManager.A2dpSourceProfile;
    a2dpSrc.connect('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]disconnect(deprecated)

disconnect(device: string): void

Disconnects an A2DP connection.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/eRef8holQYWYHLsqKoioDA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F67E0A3BC00DF76756C5EC50B1745757D6BB137B895061BAFE220E41FCAC1200)

This API is supported since API version 9 and deprecated since API version 10. The substitute API is available only for system applications.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | Address of the target device. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE\_A2DP\_SOURCE) as bluetoothManager.A2dpSourceProfile;
    a2dpSrc.disconnect('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]on('connectionStateChange')(deprecated)

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

Subscribes to the A2DP connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/giUF3BE6Q2aPDmLpOPCNcA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45D80634BE48C3ACFAE5C804634C4CFF4D27DFDD2F15E4CDB2B213327992D1B5)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [baseProfile.on('connectionStateChange')](../../arkts-apis/ohos-bluetooth-baseprofile-bluetooth-baseprofile-module/document.md#baseprofileonconnectionstatechange) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **connectionStateChange**, which indicates a connection state change event. |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | Yes | Callback used to return the A2DP connection state. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('a2dp state = '+ JSON.stringify(data));
}
try {
let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE\_A2DP\_SOURCE) as bluetoothManager.A2dpSourceProfile;
a2dpSrc.on('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]off('connectionStateChange')(deprecated)

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

Unsubscribes from the A2DP connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/k8-_minPSyG0l7bVCDqKYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32B87CCFFC4925335D3F4707FC96E443359CDD4E6D54EBC0E72D120F80F270CB)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [baseProfile.off('connectionStateChange')](../../arkts-apis/ohos-bluetooth-baseprofile-bluetooth-baseprofile-module/document.md#baseprofileoffconnectionstatechange) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **connectionStateChange**, which indicates a connection state change event. |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | No | Callback to unregister. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('a2dp state = '+ JSON.stringify(data));
}
try {
let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE\_A2DP\_SOURCE) as bluetoothManager.A2dpSourceProfile;
a2dpSrc.on('connectionStateChange', onReceiveEvent);
a2dpSrc.off('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]getPlayingState(deprecated)

getPlayingState(device: string): PlayingState

Obtains the playing state of a device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/Q-cttLVeS36kseYHmmzDoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3129CA0CDFBA3AFCF914F0B7F1DB485BD6359CCA011AD579C17E04B6DD2E8E7)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [getPlayingState](../../arkts-apis/ohos-bluetooth-a2dp-bluetooth-a2dp-module/document.md#getplayingstate) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | Address of the target device. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PlayingState](#playingstatedeprecated) | Playing state of the remote device obtained. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE\_A2DP\_SOURCE) as bluetoothManager.A2dpSourceProfile;
    let state: bluetoothManager.PlayingState  = a2dpSrc.getPlayingState('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### HandsFreeAudioGatewayProfile(deprecated)

Before using an API of **HandsFreeAudioGatewayProfile**, you need to create an instance of this class by using **getProfile()**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/Yk3TqGVwSLSF9rsblHPzzg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4300ED1635EA05EA808260E594CBC7D44862998EF199C45B7818EA797B5D3E6E)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [hfp.HandsFreeAudioGatewayProfile](../../arkts-apis/ohos-bluetooth-hfp-bluetooth-hfp-module/document.md#handsfreeaudiogatewayprofile) instead.

#### \[h2\]connect(deprecated)

connect(device: string): void

Sets up a Hands-free Profile (HFP) connection of a device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/DzjY3xd9Stu0WMJ5RSBkrQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0B77834B130A676C4F1B7550740910955D8CE2D8A4D8A3F1E47A92E05084EF1)

This API is supported since API version 9 and deprecated since API version 10. The substitute API is available only for system applications.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | Address of the target device. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let hfpAg: bluetoothManager.HandsFreeAudioGatewayProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE\_HANDS\_FREE\_AUDIO\_GATEWAY) as bluetoothManager.HandsFreeAudioGatewayProfile;
    hfpAg.connect('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]disconnect(deprecated)

disconnect(device: string): void

Disconnects the HFP connection of a device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/YSb8kRFkQiKgJmgku6zjew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=398FD10BB31E505D7B21441A4EA2C593905DE4ACA390A4F444E51E6B2FFAF331)

This API is supported since API version 9 and deprecated since API version 10. The substitute API is available only for system applications.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | Address of the target device. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let hfpAg: bluetoothManager.HandsFreeAudioGatewayProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE\_HANDS\_FREE\_AUDIO\_GATEWAY) as bluetoothManager.HandsFreeAudioGatewayProfile;
    hfpAg.disconnect('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]on('connectionStateChange')(deprecated)

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

Subscribes to the HFP connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/mBoIk-PpSFWZ4uYdfvKjyg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C046262BDC252794F29013D744B29426BC13A3D2CB7525E33C876AC82BB8812A)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [baseProfile.on('connectionStateChange')](../../arkts-apis/ohos-bluetooth-baseprofile-bluetooth-baseprofile-module/document.md#baseprofileonconnectionstatechange) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **connectionStateChange**, which indicates a connection state change event. |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | Yes | Callback used to return the HFP connection state. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('hfp state = '+ JSON.stringify(data));
}
try {
let hfpAg: bluetoothManager.HandsFreeAudioGatewayProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE\_HANDS\_FREE\_AUDIO\_GATEWAY) as
  bluetoothManager.HandsFreeAudioGatewayProfile;
hfpAg.on('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]off('connectionStateChange')(deprecated)

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

Unsubscribes from the HFP connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/mfcq73NbQxa8UMz8ls5iyg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61F72D7367A2EB2BA77D710B41FB8F4C7D6F86615ECB011C5B45FB4FAA3120DD)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [baseProfile.off('connectionStateChange')](../../arkts-apis/ohos-bluetooth-baseprofile-bluetooth-baseprofile-module/document.md#baseprofileoffconnectionstatechange) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **connectionStateChange**, which indicates a connection state change event. |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | No | Callback to unregister. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| **Example** |  |

import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('hfp state = '+ JSON.stringify(data));
}
try {
let hfpAg: bluetoothManager.HandsFreeAudioGatewayProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE\_HANDS\_FREE\_AUDIO\_GATEWAY) as
  bluetoothManager.HandsFreeAudioGatewayProfile;
hfpAg.on('connectionStateChange', onReceiveEvent);
hfpAg.off('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### HidHostProfile(deprecated)

Before using an API of **HidHostProfile**, you need to create an instance of this class by using **getProfile()**.

#### \[h2\]on('connectionStateChange')(deprecated)

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

Subscribes to the HidHost connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/V_QzX5tmQYWwjjt4veHndw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10603483635956B6757621113FE4ECD5EA02A514CE3809D855CEF0CAFB9AC3A6)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [baseProfile.on('connectionStateChange')](../../arkts-apis/ohos-bluetooth-baseprofile-bluetooth-baseprofile-module/document.md#baseprofileonconnectionstatechange) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **connectionStateChange**, which indicates a connection state change event. |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | Yes | Callback used to return the HidHost connection state. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('hidHost state = '+ JSON.stringify(data));
}
try {
let hidHost: bluetoothManager.HidHostProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE\_HID\_HOST) as bluetoothManager.HidHostProfile;
hidHost.on('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]off('connectionStateChange')(deprecated)

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

Unsubscribes from the HidHost connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/rKFdUedTTEa4Q1SJx-ZXqA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27661EFB4DB889BEF0F21567ADB116FD2519021F0591839D4298F294F7D1B657)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [baseProfile.off('connectionStateChange')](../../arkts-apis/ohos-bluetooth-baseprofile-bluetooth-baseprofile-module/document.md#baseprofileoffconnectionstatechange) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **connectionStateChange**, which indicates a connection state change event. |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | No | Callback to unregister. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('hidHost state = '+ JSON.stringify(data));
}
try {
let hidHost: bluetoothManager.HidHostProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE\_HID\_HOST) as bluetoothManager.HidHostProfile;
hidHost.on('connectionStateChange', onReceiveEvent);
hidHost.off('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### PanProfile

Before using an API of **PanProfile**, you need to create an instance of this class by using **getProfile()**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/_c4I0CC-TKGrKhWM6OCnsQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=218DDF2313E46203CAB720D47C82CE4F205B7EB78443B465407E64A072DB6C2B)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [pan.createPanProfile](../../arkts-apis/ohos-bluetooth-pan-bluetooth-pan-module/document.md#pancreatepanprofile) instead.

#### \[h2\]on('connectionStateChange')(deprecated)

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

Subscribes to the PAN connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/EFcI-lyNS5eDOCEiesFSyg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B3D3672C8309C299BD177E369A8C597837AF67B0B5862C064CAA455C59A785A)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [baseProfile.on('connectionStateChange')](../../arkts-apis/ohos-bluetooth-baseprofile-bluetooth-baseprofile-module/document.md#baseprofileonconnectionstatechange) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **connectionStateChange**, which indicates a connection state change event. |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | Yes | Callback used to return the PAN connection state. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('pan state = '+ JSON.stringify(data));
}
try {
let panProfile: bluetoothManager.PanProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE\_PAN\_NETWORK) as bluetoothManager.PanProfile;
panProfile.on('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]off('connectionStateChange')(deprecated)

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

Unsubscribes from the PAN connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/mUEMiS_uTDGylVEresuI2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB3D0A84E1600BBD8642CB7C1C5A5556C7DCA262C8D98C3B728DEC4D11E5C4D6)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [baseProfile.off('connectionStateChange')](../../arkts-apis/ohos-bluetooth-baseprofile-bluetooth-baseprofile-module/document.md#baseprofileoffconnectionstatechange) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **connectionStateChange**, which indicates a connection state change event. |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | No | Callback to unregister. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('pan state = '+ JSON.stringify(data));
}
try {
let panProfile: bluetoothManager.PanProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE\_PAN\_NETWORK) as bluetoothManager.PanProfile;
panProfile.on('connectionStateChange', onReceiveEvent);
panProfile.off('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### GattServer

Implements the Generic Attribute Profile (GATT) server. Before using an API of this class, you need to create a **GattServer** instance using **createGattServer()**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/uMndOq7vRMibjmKPqInKmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B72740B940F8B0B4D47CCA01EC52426CDB518AAA22CC86187EE1513136C45065)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattServer](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#gattserver) instead.

#### \[h2\]startAdvertising(deprecated)

startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void

Starts BLE advertising.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/yl0TaJOxTKS5EVBYauZIQQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B66D5E87D705A6ABDB1B08F0D520A3B6D7358371B917B7FAA30F36A61ABA0947)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.startAdvertising](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#blestartadvertising) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| setting | [AdvertiseSetting](#advertisesettingdeprecated) | Yes | Settings related to BLE advertising. |
| advData | [AdvertiseData](#advertisedatadeprecated) | Yes | Content of the BLE advertisement packet. |
| advResponse | [AdvertiseData](#advertisedatadeprecated) | No | Response to the BLE scan request. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
let manufactureValueBuffer = new Uint8Array(4);
manufactureValueBuffer\[0\] = 1;
manufactureValueBuffer\[1\] = 2;
manufactureValueBuffer\[2\] = 3;
manufactureValueBuffer\[3\] = 4;

let serviceValueBuffer = new Uint8Array(4);
serviceValueBuffer\[0\] = 4;
serviceValueBuffer\[1\] = 6;
serviceValueBuffer\[2\] = 7;
serviceValueBuffer\[3\] = 8;
console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
let gattServer = bluetoothManager.BLE.createGattServer();
try {
    let setting: bluetoothManager.AdvertiseSetting = {
        interval:150,
        txPower:0,
        connectable:true,
    };
    let manufactureDataUnit: bluetoothManager.ManufactureData = {
        manufactureId:4567,
        manufactureValue:manufactureValueBuffer.buffer
    };
    let serviceDataUnit: bluetoothManager.ServiceData = {
        serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
        serviceValue:serviceValueBuffer.buffer
    };
    let advData: bluetoothManager.AdvertiseData = {
        serviceUuids:\["00001888-0000-1000-8000-00805f9b34fb"\],
        manufactureData:\[manufactureDataUnit\],
        serviceData:\[serviceDataUnit\],
    };
    let advResponse: bluetoothManager.AdvertiseData = {
        serviceUuids:\["00001888-0000-1000-8000-00805f9b34fb"\],
        manufactureData:\[manufactureDataUnit\],
        serviceData:\[serviceDataUnit\],
    };
    gattServer.startAdvertising(setting, advData ,advResponse);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]stopAdvertising(deprecated)

stopAdvertising(): void

Stops BLE advertising.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/6qA2VvHsSEWhT-jqQsvSig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64FF505E1FC231E66B8C9A12F84E9531AEC8F5D8F3EBE1B1C188B657CCF506FD)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.stopAdvertising](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#blestopadvertising) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
let server = bluetoothManager.BLE.createGattServer();
try {
    server.stopAdvertising();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]addService(deprecated)

addService(service: GattService): void

Adds a service to this GATT server.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/jJomi4ioSPuaWmg0wwTq2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=89109FF69F5D366500948EC9DB1F9FD56A8A4579F4670910215F0FAF4355459B)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattServer#addService](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#addservice) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| service | [GattService](#gattservicedeprecated) | Yes | Service to add. Settings related to BLE advertising. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
// Create descriptors.
let descriptors: Array<bluetoothManager.BLEDescriptor> = \[\];
let arrayBuffer = new ArrayBuffer(8);
let descV = new Uint8Array(arrayBuffer);
descV\[0\] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
descriptors\[0\] = descriptor;

// Create characteristics.
let characteristics: Array<bluetoothManager.BLECharacteristic> = \[\];
let arrayBufferC = new ArrayBuffer(8);
let cccV = new Uint8Array(arrayBufferC);
cccV\[0\] = 1;
let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
let characteristicN: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001821-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
characteristics\[0\] = characteristic;

// Create a gattService instance.
let gattService: bluetoothManager.GattService = {serviceUuid:'00001810-0000-1000-8000-00805F9B34FB', isPrimary: true, characteristics:characteristics, includeServices:\[\]};

let gattServer  = bluetoothManager.BLE.createGattServer();
try {
    gattServer.addService(gattService);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]removeService(deprecated)

removeService(serviceUuid: string): void

Removes a service from this GATT server.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/lyJgW_DCT2W5H_oNaDMoXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82149BB121B2A39E5824D5538EE89F42F9A9E08DABDCB7B69B0C68FF543554F8)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattServer#removeService](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#removeservice) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| serviceUuid | string | Yes | Universally unique identifier (UUID) of the service to remove, for example, **00001810-0000-1000-8000-00805F9B34FB**. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
let server = bluetoothManager.BLE.createGattServer();
try {
    server.removeService('00001810-0000-1000-8000-00805F9B34FB');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]close(deprecated)

close(): void

Closes this GATT server to unregister it from the protocol stack. After this method is called, this [GattServer](#gattserver) cannot be used.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/NwDoXP49S9GtlmmFXMObIA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B538279DD06EA4B49B44B1580FFED69DDFF3513A7C91BB95A178D882B8B8250A)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattServer#close](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#close) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
let server = bluetoothManager.BLE.createGattServer();
try {
    server.close();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]notifyCharacteristicChanged(deprecated)

notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): void

Notifies the connected client device when a characteristic value changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/W_NdzMw_TzuTEShE8sKOjA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F0294DADD677852704B657EC1DAA7D7BE70A99659EAA6E815655C8BF77A66F2)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattServer#notifyCharacteristicChanged](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#notifycharacteristicchanged) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the client that receives notifications, for example, XX:XX:XX:XX:XX:XX. |
| notifyCharacteristic | [NotifyCharacteristic](#notifycharacteristicdeprecated) | Yes | New characteristic value. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
// Create descriptors.
let descriptors: Array<bluetoothManager.BLEDescriptor> = \[\];
let arrayBuffer = new ArrayBuffer(8);
let descV = new Uint8Array(arrayBuffer);
descV\[0\] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
descriptors\[0\] = descriptor;
let arrayBufferC = new ArrayBuffer(8);
let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
let notifyCharacteristic: bluetoothManager.NotifyCharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001821-0000-1000-8000-00805F9B34FB', characteristicValue: characteristic.characteristicValue, confirm: false};
let server = bluetoothManager.BLE.createGattServer();
try {
    server.notifyCharacteristicChanged('XX:XX:XX:XX:XX:XX', notifyCharacteristic);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]sendResponse(deprecated)

sendResponse(serverResponse: ServerResponse): void

Sends a response to a read or write request from the GATT client.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/BbGg9jfjTMOUlICU3itK0w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B901606227039C5C4321EAE7FDAF2B9DD440E47313131BD0975B895C63A4237)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattServer#sendResponse](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#sendresponse) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| serverResponse | [ServerResponse](#serverresponsedeprecated) | Yes | Response returned by the GATT server. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
/\* send response \*/
let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
cccValue\[0\] = 1;
let serverResponse: bluetoothManager.ServerResponse = {
    deviceId: 'XX:XX:XX:XX:XX:XX',
    transId: 0,
    status: 0,
    offset: 0,
    value: arrayBufferCCC,
};

let gattServer = bluetoothManager.BLE.createGattServer();
try {
    gattServer.sendResponse(serverResponse);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]on('characteristicRead')(deprecated)

on(type: 'characteristicRead', callback: Callback<CharacteristicReadRequest>): void

Subscribes to the characteristic read request events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/UpPn4I14SIyBHiYm7dUoSA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00533A192FEE77CCC606FE7D7D5ADD4FEDB96F4B68630814E752577F9E20AE14)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattServer#on('characteristicRead')](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#oncharacteristicread) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **characteristicRead**, which indicates a characteristic read request event. |
| callback | Callback<[CharacteristicReadRequest](#characteristicreadrequestdeprecated)\> | Yes | Callback used to return a characteristic read request event from the GATT client. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
cccValue\[0\] = 1;
function ReadCharacteristicReq(characteristicReadRequest: bluetoothManager.CharacteristicReadRequest) {
    let deviceId: string = characteristicReadRequest.deviceId;
    let transId: number = characteristicReadRequest.transId;
    let offset: number = characteristicReadRequest.offset;
    let characteristicUuid: string = characteristicReadRequest.characteristicUuid;

    let serverResponse: bluetoothManager.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferCCC};

    try {
        gattServer.sendResponse(serverResponse);
    } catch (err) {
        console.error('errCode: ' + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
    }
}

let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.on("characteristicRead", ReadCharacteristicReq);

#### \[h2\]off('characteristicRead')(deprecated)

off(type: 'characteristicRead', callback?: Callback<CharacteristicReadRequest>): void

Unsubscribes from the characteristic read request events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/T8Ov_JCiTOSl1GmcDh-QuA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90DFB6019A7491741B653FA749735819AE0B394067924BE0849A7B685097FC66)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattServer#off('characteristicRead')](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#offcharacteristicread) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **characteristicRead**, which indicates a characteristic read request event. |
| callback | Callback<[CharacteristicReadRequest](#characteristicreadrequestdeprecated)\> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for the specified **type**. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
try {
let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.off("characteristicRead");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]on('characteristicWrite')(deprecated)

on(type: 'characteristicWrite', callback: Callback<CharacteristicWriteRequest>): void

Subscribes to the characteristic write request events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/UKw35bhdT4qjgRbaPKE-Fg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B23681DCA0486BD7BB6C0862B44C2B3EAEEC1663AD552C0A407EA83FB50D5FD)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattServer#on('characteristicWrite')](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#oncharacteristicwrite) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **characteristicWrite**, which indicates a characteristic write request event. |
| callback | Callback<[CharacteristicWriteRequest](#characteristicwriterequestdeprecated)\> | Yes | Callback used to return a characteristic write request from the GATT client. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
function WriteCharacteristicReq(characteristicWriteRequest: bluetoothManager.CharacteristicWriteRequest) {
    let deviceId: string = characteristicWriteRequest.deviceId;
    let transId: number = characteristicWriteRequest.transId;
    let offset: number = characteristicWriteRequest.offset;
    let isPrep: boolean = characteristicWriteRequest.isPrep;
    let needRsp: boolean = characteristicWriteRequest.needRsp;
    let value: Uint8Array =  new Uint8Array(characteristicWriteRequest.value);
    let characteristicUuid: string = characteristicWriteRequest.characteristicUuid;

    cccValue\[0\] = value\[0\];
    let serverResponse: bluetoothManager.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferCCC};

    try {
        gattServer.sendResponse(serverResponse);
    } catch (err) {
        console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
}

let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.on("characteristicWrite", WriteCharacteristicReq);

#### \[h2\]off('characteristicWrite')(deprecated)

off(type: 'characteristicWrite', callback?: Callback<CharacteristicWriteRequest>): void

Unsubscribes from the characteristic write request events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/rvp9JnylQUm1PWDqSZ9MsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3125C34CB4875E6A94602C36D1A923C4273D69FCA0C02E9CF33D0D23F728C912)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattServer#off('characteristicWrite')](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#offcharacteristicwrite) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **characteristicWrite**, which indicates a characteristic write request event. |
| callback | Callback<[CharacteristicWriteRequest](#characteristicwriterequestdeprecated)\> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for the specified **type**. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
try {
let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.off("characteristicWrite");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]on('descriptorRead')(deprecated)

on(type: 'descriptorRead', callback: Callback<DescriptorReadRequest>): void

Subscribes to the descriptor read request events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/yzTr6NPURbaJchP2MPob7w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CF7000712D7AA335F4CDE0BAE4E29475401392EC25F5CA843F760DBED37E09F)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattServer#on('descriptorRead')](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#ondescriptorread) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **descriptorRead**, which indicates a descriptor read request event. |
| callback | Callback<[DescriptorReadRequest](#descriptorreadrequestdeprecated)\> | Yes | Callback used to return a characteristic read request event from the GATT client. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let arrayBufferDesc = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBufferDesc);
descValue\[0\] = 1;
function ReadDescriptorReq(descriptorReadRequest: bluetoothManager.DescriptorReadRequest) {
    let deviceId: string = descriptorReadRequest.deviceId;
    let transId: number = descriptorReadRequest.transId;
    let offset: number = descriptorReadRequest.offset;
    let descriptorUuid: string = descriptorReadRequest.descriptorUuid;

    let serverResponse: bluetoothManager.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferDesc};

    try {
        gattServer.sendResponse(serverResponse);
    } catch (err) {
        console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
}

let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.on("descriptorRead", ReadDescriptorReq);

#### \[h2\]off('descriptorRead')(deprecated)

off(type: 'descriptorRead', callback?: Callback<DescriptorReadRequest>): void

Unsubscribes from the descriptor read request events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/JWvCSP17SmClm_9kixsGhg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D761D226D362EC7D7E6C3307623D9AB141191E77F9E56FE7808E63A0DCE3F66C)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattServer#off('descriptorRead')](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#offdescriptorread) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **descriptorRead**, which indicates a descriptor read request event. |
| callback | Callback<[DescriptorReadRequest](#descriptorreadrequestdeprecated)\> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for the specified **type**. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
try {
let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.off("descriptorRead");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]on('descriptorWrite')(deprecated)

on(type: 'descriptorWrite', callback: Callback<DescriptorWriteRequest>): void

Subscribes to the descriptor write request events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/Qj7nb6gYRii6Zaa5oC0Q8A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=09DF9803BF36EB8C12681A1DBC7244FA479F07A217612D546926D6AC009A94C8)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattServer#on('descriptorWrite')](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#ondescriptorwrite) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **descriptorWrite**, which indicates a descriptor write request event. |
| callback | Callback<[DescriptorWriteRequest](#descriptorwriterequestdeprecated)\> | Yes | Callback used to return a characteristic write request from the GATT client. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
let arrayBufferDesc = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBufferDesc);
function WriteDescriptorReq(descriptorWriteRequest: bluetoothManager.DescriptorWriteRequest) {
    let deviceId: string = descriptorWriteRequest.deviceId;
    let transId: number = descriptorWriteRequest.transId;
    let offset: number = descriptorWriteRequest.offset;
    let isPrep: boolean = descriptorWriteRequest.isPrep;
    let needRsp: boolean = descriptorWriteRequest.needRsp;
    let value: Uint8Array = new Uint8Array(descriptorWriteRequest.value);
    let descriptorUuid: string = descriptorWriteRequest.descriptorUuid;

    descValue\[0\] = value\[0\];
    let serverResponse: bluetoothManager.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferDesc};

    try {
        gattServer.sendResponse(serverResponse);
    } catch (err) {
        console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
}

let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.on("descriptorWrite", WriteDescriptorReq);

#### \[h2\]off('descriptorWrite')(deprecated)

off(type: 'descriptorWrite', callback?: Callback<DescriptorWriteRequest>): void

Unsubscribes from the descriptor write request events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/1bWHJ97ySTifDW3c3JEPRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE5F27E1D84CDFC4EB34C1C5BF64E7CF2140F16B94383752F27676572BE47E7D)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattServer#off('descriptorWrite')](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#offdescriptorwrite) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **descriptorWrite**, which indicates a descriptor write request event. |
| callback | Callback<[DescriptorWriteRequest](#descriptorwriterequestdeprecated)\> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for the specified **type**. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
try {
let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.off("descriptorWrite");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]on('connectStateChange')(deprecated)

on(type: 'connectStateChange', callback: Callback<BLEConnectChangedState>): void

Subscribes to the BLE connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/H0lmxFn_THGZFJLxZH-XMg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D3E4D22CA5CA8A0B01ED079A5817D561F780ADF811678D983968D924EEEE4A28)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattServer#on('connectionStateChange')](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#onconnectionstatechange) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **connectStateChange**, which indicates a BLE connection state change event. |
| callback | Callback<[BLEConnectChangedState](#bleconnectchangedstatedeprecated)\> | Yes | Callback used to return the BLE connection state. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
function Connected(BLEConnectChangedState: bluetoothManager.BLEConnectChangedState) {
  let deviceId: string = BLEConnectChangedState.deviceId;
  let status: bluetoothManager.ProfileConnectionState  = BLEConnectChangedState.state;
}
try {
let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.on("connectStateChange", Connected);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]off('connectStateChange')(deprecated)

off(type: 'connectStateChange', callback?: Callback<BLEConnectChangedState>): void

Unsubscribes from the BLE connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/AERAwfA7Qr2ZL5TlskJPnQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10D3407C5067BAC034E2C40DDFDDD72793FD3A6581353A159AA9E8C722F4A956)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattServer#off('connectionStateChange')](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#offconnectionstatechange) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **connectStateChange**, which indicates a BLE connection state change event. |
| callback | Callback<[BLEConnectChangedState](#bleconnectchangedstatedeprecated)\> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for the specified **type**. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
try {
let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.off("connectStateChange");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### GattClientDevice

Implements the GATT client. Before using an API of this class, you must create a **GattClientDevice** instance using **createGattClientDevice(deviceId: string)**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/LTU3oMv2TtuFGT7ri-X7mQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F77E9CF11F35C384340B9AA8F0A8FFD57DC1F92362B62516D65F837116B781A8)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#gattclientdevice) instead.

#### \[h2\]connect(deprecated)

connect(): void

Initiates a connection to the remote BLE device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/HASyNVaNRKupGNuQtc2CHg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41FA750AB3EEDD664319448F1200C463F568A4F0CE8221D29625ED852362D12E)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#connect](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#connect) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.connect();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]disconnect(deprecated)

disconnect(): void

Disconnects from the remote BLE device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/NhpB6HIbTBOq1yRHz9p-LA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4AD202C0F006B35D8E6F7E0534DC51D3B0B916A18912940E7A2BE658537E163)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#disconnect](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#disconnect) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.disconnect();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]close(deprecated)

close(): void

Closes this GATT client to unregister it from the protocol stack. After this method is called, this [GattClientDevice](#gattclientdevice) instance cannot be used.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/hhMZTJWuR7i_LbX7dmFLEw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A0AC40CF0D399A49B78A5ECE047963EE2B91A5D9581516708824C292783C1E1)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#close](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#close) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.close();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]getServices(deprecated)

getServices(callback: AsyncCallback<Array<GattService>>): void

Obtains all services of the remote BLE device on the client.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/8iSL8Fv_RIWlGfh_I7c34A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D3674B116D393708955B0793B60611554FE9949C1D0892815C0B600883EFFB1)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#getServices](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#getservices) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[GattService](#gattservicedeprecated)\>> | Yes | Callback used to return the services obtained. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
// Callback mode.
function getServices(code: BusinessError, gattServices: Array<bluetoothManager.GattService>) {
  if (code.code == 0) {
      let services: Array<bluetoothManager.GattService> = gattServices;
      console.info(\`bluetooth code is ${code.code}\`);
      console.info(\`bluetooth services size is ${services.length}\`);

      for (let i = 0; i < services.length; i++) {
        console.info(\`bluetooth serviceUuid is ${services\[i\].serviceUuid}\`);
      }
  }
}

try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.connect();
    device.getServices(getServices);
} catch (err) {
    console.error(\`errCode: ${err.code}, errMessage: ${err.message}\`);
}

#### \[h2\]getServices(deprecated)

getServices(): Promise<Array<GattService>>

Obtains all services of the remote BLE device on the client. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/YaQSbTV3Q5CkYVogiKEkng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D672FD49C0A5E52CE0245CF840FE5E65125B66D509A7E88F8A7CB316BBB1524)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#getServices](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#getservices-1) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[GattService](#gattservicedeprecated)\>> | Promise used to return the services obtained. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
// Promise
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.connect();
    device.getServices().then(result => {
        console.info("getServices successfully:" + JSON.stringify(result));
    });
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]readCharacteristicValue(deprecated)

readCharacteristicValue(characteristic: BLECharacteristic, callback: AsyncCallback<BLECharacteristic>): void

Reads the characteristic value of the specific service of the remote BLE device. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/ND57mytqRQaj2UGk6GUdfA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F9047EC984D97199839F63CFA572974102DF0FAABB71E4AA5857A0EC6FD93CBF)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#readCharacteristicValue](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#readcharacteristicvalue) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| characteristic | [BLECharacteristic](#blecharacteristicdeprecated) | Yes | Characteristic value to read. |
| callback | AsyncCallback<[BLECharacteristic](#blecharacteristicdeprecated)\> | Yes | Callback used to return the characteristic value read. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901000 | Read forbidden. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
function readCcc(code: BusinessError, BLECharacteristic: bluetoothManager.BLECharacteristic) {
    if (code.code != 0) {
        return;
    }
    console.info(\`bluetooth characteristic uuid: ${BLECharacteristic.characteristicUuid}\`);
    let value = new Uint8Array(BLECharacteristic.characteristicValue);
    console.info(\`value length: ${value.length}\`);
}

let descriptors: Array<bluetoothManager.BLEDescriptor> = \[\];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV\[0\] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors\[0\] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV\[0\] = 1;
let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    characteristicValue: bufferCCC, descriptors:descriptors};

try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.readCharacteristicValue(characteristic, readCcc);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]readCharacteristicValue(deprecated)

readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>

Reads the characteristic value of the specific service of the remote BLE device. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/1Nr6ar1oTAeFbOS89mhBHA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4F84687AEEFC0C4B31FBB09306CE2F2F6CFBAA7D6E78AACA1D020C7A84662B7)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#readCharacteristicValue](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#readcharacteristicvalue-1) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| characteristic | [BLECharacteristic](#blecharacteristicdeprecated) | Yes | Characteristic value to read. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[BLECharacteristic](#blecharacteristicdeprecated)\> | Promise used to return the characteristic value read. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901000 | Read forbidden. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
let descriptors: Array<bluetoothManager.BLEDescriptor> = \[\];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV\[0\] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors\[0\] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV\[0\] = 1;
let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    characteristicValue: bufferCCC, descriptors:descriptors};

try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.readCharacteristicValue(characteristic);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]readDescriptorValue(deprecated)

readDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<BLEDescriptor>): void

Reads the descriptor contained in the specific characteristic of the remote BLE device on the client. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/AfykBuxqSBi14T3eHQKtRw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D03B5CF72313CE4DF27A512505B15C65706776531F86F4AD846A850FD426EF8)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#readDescriptorValue](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#readdescriptorvalue) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| descriptor | [BLEDescriptor](#bledescriptordeprecated) | Yes | Descriptor to read. |
| callback | AsyncCallback<[BLEDescriptor](#bledescriptordeprecated)\> | Yes | Callback used to return the descriptor read. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901000 | Read forbidden. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
function readDesc(code: BusinessError, BLEDescriptor: bluetoothManager.BLEDescriptor) {
    if (code.code != 0) {
        return;
    }
    console.info(\`bluetooth descriptor uuid: ${BLEDescriptor.descriptorUuid}\`);
    let value = new Uint8Array(BLEDescriptor.descriptorValue);
}

let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV\[0\] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {
    serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB',
    descriptorValue: bufferDesc
};
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.readDescriptorValue(descriptor, readDesc);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]readDescriptorValue(deprecated)

readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>

Reads the descriptor contained in the specific characteristic of the remote BLE device on the client. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/FztMXm5yStyFEw1tGV-GZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75744F575B72B22ED419A8C8C6FCC00487BD20A329B642B6F4DF35428A8D18BB)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#readDescriptorValue](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#readdescriptorvalue-1) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| descriptor | [BLEDescriptor](#bledescriptordeprecated) | Yes | Descriptor to read. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[BLEDescriptor](#bledescriptordeprecated)\> | Promise used to return the descriptor read. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901000 | Read forbidden. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV\[0\] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {
    serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB',
    descriptorValue: bufferDesc
};
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.readDescriptorValue(descriptor);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]writeCharacteristicValue(deprecated)

writeCharacteristicValue(characteristic: BLECharacteristic): void

Writes a characteristic value to the remote BLE device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/x0QzDE9sQbmE1S_z4l-IDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A2B908DC0184CBD976F2B2FDA81E3D555E588B8FF20DC03E89DD1003E098DD5)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#writeCharacteristicValue](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#writecharacteristicvalue) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| characteristic | [BLECharacteristic](#blecharacteristicdeprecated) | Yes | Binary value and other parameters of the BLE device characteristic. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901001 | Write forbidden. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
let descriptors: Array<bluetoothManager.BLEDescriptor> = \[\];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV\[0\] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors\[0\] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV\[0\] = 1;
let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    characteristicValue: bufferCCC, descriptors:descriptors};
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.writeCharacteristicValue(characteristic);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]writeDescriptorValue(deprecated)

writeDescriptorValue(descriptor: BLEDescriptor): void

Writes binary data to the specific descriptor of the remote BLE device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/hAg1jtonRPeuGpzg9sTuMA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F62652A62BAA9FFE0F83E2A74C39684B0C115BA4A1592A87AF7D65978055901)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#writeDescriptorValue](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#writedescriptorvalue) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| descriptor | [BLEDescriptor](#bledescriptordeprecated) | Yes | Binary value and other parameters of the BLE device descriptor. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901001 | Write forbidden. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV\[0\] = 22;
let descriptor: bluetoothManager.BLEDescriptor = {
    serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB',
    descriptorValue: bufferDesc
};
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.writeDescriptorValue(descriptor);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]setBLEMtuSize(deprecated)

setBLEMtuSize(mtu: number): void

Sets the maximum transmission unit (MTU) that can be transmitted between the GATT client and its remote BLE device. This API can be used only after a connection is set up by calling [connect](#connectdeprecated-1).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/ZOZU08R6RySs3X6rAgINhw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EDDC57D9FE8DE9B30D0752175AC0B6BF3EF2830E3A34B7752A1B72D8669F87D3)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#setBLEMtuSize](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#setblemtusize) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mtu | number | Yes | MTU to set, which ranges from 22 to 512 bytes. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.setBLEMtuSize(128);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]setNotifyCharacteristicChanged(deprecated)

setNotifyCharacteristicChanged(characteristic: BLECharacteristic, enable: boolean): void

Sets the function of notifying the GATT client when the characteristic value of the remote BLE device changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/rOSQKGwqS4Wye95VzTUO_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=843CB4000ADF07E0FB234488CA53AFC0855A7DDDDF138D49CA6D4D4EEC330E62)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#setCharacteristicChangeNotification](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#setcharacteristicchangenotification) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| characteristic | [BLECharacteristic](#blecharacteristicdeprecated) | Yes | BLE characteristic to listen for. |
| enable | boolean | Yes | Whether to enable the notify function. The value **true** means to enable the notify function, and the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
// Create descriptors.
let descriptors: Array<bluetoothManager.BLEDescriptor> = \[\];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV\[0\] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors\[0\] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV\[0\] = 1;
let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    characteristicValue: bufferCCC, descriptors:descriptors};
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.setNotifyCharacteristicChanged(characteristic, false);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]on('BLECharacteristicChange')(deprecated)

on(type: 'BLECharacteristicChange', callback: Callback<BLECharacteristic>): void

Subscribes to the BLE characteristic changes. The client can receive a notification from the server only after the **setNotifyCharacteristicChanged** method is called.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/mPg9q4Y-RziH-0ozLGCxzg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=780E2B280284003407EA50DADE124ACDBAC59CA108AB87AE222E2C853E6C6C2C)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#on('BLECharacteristicChange')](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#onblecharacteristicchange) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **BLECharacteristicChange**, which indicates a characteristic value change event. |
| callback | Callback<[BLECharacteristic](#blecharacteristicdeprecated)\> | Yes | Callback used to return the characteristic value changes. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
function CharacteristicChange(characteristicChangeReq: ble.BLECharacteristic) {
    let serviceUuid: string = characteristicChangeReq.serviceUuid;
    let characteristicUuid: string = characteristicChangeReq.characteristicUuid;
    let value: Uint8Array = new Uint8Array(characteristicChangeReq.characteristicValue);
}
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.on('BLECharacteristicChange', CharacteristicChange);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]off('BLECharacteristicChange')(deprecated)

off(type: 'BLECharacteristicChange', callback?: Callback<BLECharacteristic>): void

Unsubscribes from the BLE characteristic changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/wupVzyUPTpqE6TAa2oKckw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1BC2C7B3BA4C899C5EF7A6B582C58E2D77C0BF004B89BD9DF1C241940A99DE86)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#off('BLECharacteristicChange')](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#offblecharacteristicchange) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **BLECharacteristicChange**, which indicates a characteristic value change event. |
| callback | Callback<[BLECharacteristic](#blecharacteristicdeprecated)\> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for the specified **type**. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.off('BLECharacteristicChange');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]on('BLEConnectionStateChange')(deprecated)

on(type: 'BLEConnectionStateChange', callback: Callback<BLEConnectChangedState>): void

Subscribes to the BLE connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/Y7ghnNlaT2uyvvrjKsEVFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D018DFB38062076823EF267DFBE8FE7CBFF21318229D53AFDAA0AE8E026B91A0)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#on('BLEConnectionStateChange')](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#onbleconnectionstatechange) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **BLEConnectionStateChange**, which indicates a BLE connection state change event. |
| callback | Callback<[BLEConnectChangedState](#bleconnectchangedstatedeprecated)\> | Yes | Callback used to return the BLE connection state. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
function ConnectStateChanged(state: bluetoothManager.BLEConnectChangedState) {
    console.info('bluetooth connect state changed');
    let connectState: bluetoothManager.ProfileConnectionState = state.state;
}
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.on('BLEConnectionStateChange', ConnectStateChanged);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]off('BLEConnectionStateChange')(deprecated)

off(type: 'BLEConnectionStateChange', callback?: Callback<BLEConnectChangedState>): void

Unsubscribes from the BLE connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/SQBrxm6VSE-LWjC9mhysVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F1B70F8CF31F52950FF4A2548DD6199278DBCB885421F89EAB1007BDCDA69F2A)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#off('BLEConnectionStateChange')](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#offbleconnectionstatechange) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **BLEConnectionStateChange**, which indicates a BLE connection state change event. |
| callback | Callback<[BLEConnectChangedState](#bleconnectchangedstatedeprecated)\> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for the specified **type**. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@ohos.base';
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.off('BLEConnectionStateChange');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]getDeviceName(deprecated)

getDeviceName(callback: AsyncCallback<string>): void

Obtains the name of the remote BLE device on the client.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/23aLylB0QfOQ_8djKD2d1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8860401324A7A76CC7C91C33888943C5CA6BE6753C0E16E80BE82E0D52D08571)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#getDeviceName](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#getdevicename) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the remote BLE device name obtained. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
// callback
try {
    let gattClient = bluetoothManager.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
    gattClient.connect();
    let deviceName = gattClient.getDeviceName((err, data)=> {
        console.info('device name err ' + JSON.stringify(err));
        console.info('device name' + JSON.stringify(data));
    })
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]getDeviceName(deprecated)

getDeviceName(): Promise<string>

Obtains the name of the remote BLE device on the client. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/JScIDnSeRxmjxTKfAjNEOA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C1010CC642B5E55FD093E9CB17B7FA5DD0AD7BAE3B35480CDFFAC6DE0A31F28C)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#getDeviceName](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#getdevicename-1) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the remote BLE device name. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
// promise
try {
    let gattClient = bluetoothManager.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
    gattClient.connect();
    let deviceName = gattClient.getDeviceName().then((data) => {
        console.info('device name' + JSON.stringify(data));
    })
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]getRssiValue(deprecated)

getRssiValue(callback: AsyncCallback<number>): void

Obtains the received signal strength indication (RSSI) of the remote BLE device on the client. This API can be used only after a connection is set up by calling [connect](#connectdeprecated-1).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/ZNfZ9K42Siq5mwY9sreSVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9370540013E0B12F11A48685CB804EBE9487523A0C06675D949E775D5ECC78E1)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#getRssiValue](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#getrssivalue) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the RSSI, in dBm. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
// callback
try {
    let gattClient = bluetoothManager.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
    gattClient.connect();
    let rssi = gattClient.getRssiValue((err: BusinessError, data: number)=> {
        console.info('rssi err ' + JSON.stringify(err));
        console.info('rssi value' + JSON.stringify(data));
    })
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### \[h2\]getRssiValue(deprecated)

getRssiValue(): Promise<number>

Obtains the RSSI of the remote BLE device on the client. This API uses a promise to return the result. It can be used only after a connection is set up by calling [connect](#connectdeprecated-1).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/ORzLsvHGQseS9DEIsMEN2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5EED6C4EF595378E728647AB453224EFC1A6EBC9B4311E4F22825AA3B6FB43F1)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattClientDevice#getRssiValue](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#getrssivalue-1) instead.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the RSSI, in dBm. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@ohos.base';
// promise
try {
    let gattClient = bluetoothManager.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
    let rssi = gattClient.getRssiValue().then((data: number) => {
        console.info('rssi' + JSON.stringify(data));
    })
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### ScanMode(deprecated)

Enumerates the scan modes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/nDSi5NR6RRiWoX9sWClIZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=065F0D9576352016040341503AB8649DCA2F078E43C1BE21E2CE4389C7E6B2F5)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.ScanMode](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#scanmode) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SCAN\_MODE\_NONE | 0 | No scan mode. |
| SCAN\_MODE\_CONNECTABLE | 1 | Connectable mode. |
| SCAN\_MODE\_GENERAL\_DISCOVERABLE | 2 | General discoverable mode. |
| SCAN\_MODE\_LIMITED\_DISCOVERABLE | 3 | Limited discoverable mode. |
| SCAN\_MODE\_CONNECTABLE\_GENERAL\_DISCOVERABLE | 4 | General connectable and discoverable mode. |
| SCAN\_MODE\_CONNECTABLE\_LIMITED\_DISCOVERABLE | 5 | Limited connectable and discoverable mode. |

#### BondState(deprecated)

Enumerates the pairing states.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/XWHprSRYRxWpBWN9h0kHyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41413EC756528221BCF362B9AC7664EEB358C673B5410710918403953D191007)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.BondState](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#bondstate) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| BOND\_STATE\_INVALID | 0 | Invalid pairing. |
| BOND\_STATE\_BONDING | 1 | Pairing. |
| BOND\_STATE\_BONDED | 2 | Paired. |

#### SppOption(deprecated)

Defines the SPP configuration parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/XdN_EbRATBGSyVBiQivWuQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE0C7B410A8E5859FBB67801F05A029A453FF7B62CA4A98880091553B52B47DA)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [socket.SppOption](../../arkts-apis/ohos-bluetooth-socket-bluetooth-socket-module/document.md#sppoptions) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| uuid | string | No | No | UUID of the SPP. |
| secure | boolean | No | No | Whether it is a secure channel. |
| type | [SppType](#spptypedeprecated) | No | No | Type of the SPP link. |

#### SppType(deprecated)

Enumerates the SPP link types.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/JqPoXHnKSxCJ0kiGuCIKEg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D53A8A09DAC9A6FCB688961A7D00F067410C50483EEFDE319D531C19191D3BA4)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [socket.SppType](../../arkts-apis/ohos-bluetooth-socket-bluetooth-socket-module/document.md#spptype) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SPP\_RFCOMM | 0 | Radio frequency communication (RFCOMM) link type. |

#### GattService(deprecated)

Defines the GATT service API parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/v_XKrLIJQemYLJDh3upejQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=871F8F762587C431296C7A8411FE730F0C1971177386DCE48771F20122A0E9AA)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.GattService](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#gattservice) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | No | No | UUID of the service, for example, **00001888-0000-1000-8000-00805f9b34fb**. |
| isPrimary | boolean | No | No | Whether the service is a primary service. The value **true** means a primary service. |
| characteristics | Array<[BLECharacteristic](#blecharacteristicdeprecated)\> | No | No | List of characteristics of the service. |
| includeServices | Array<[GattService](#gattservicedeprecated)\> | No | Yes | Services on which the service depends. |

#### BLECharacteristic(deprecated)

Defines the characteristic API parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/tGc9wyDpQhy7V2DZWUnefQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD6A56B06063588A64527D14194A1EFF288200A21B59E96D4623CA72518ED290)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.BLECharacteristic](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#blecharacteristic) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | No | No | UUID of the service, for example, **00001888-0000-1000-8000-00805f9b34fb**. |
| characteristicUuid | string | No | No | UUID of the characteristic, for example, **00002a11-0000-1000-8000-00805f9b34fb**. |
| characteristicValue | ArrayBuffer | No | No | Binary value of the characteristic. |
| descriptors | Array<[BLEDescriptor](#bledescriptordeprecated)\> | No | No | List of descriptors of the characteristic. |

#### BLEDescriptor(deprecated)

Defines the descriptor API parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/acWrcOAHQwma4yPDIzfe3A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D96910649A4F19EF838E025C0F4B8D34526269FDAE580CAD849A021193FC56B)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.BLEDescriptor](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#bledescriptor) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | No | No | UUID of the service, for example, **00001888-0000-1000-8000-00805f9b34fb**. |
| characteristicUuid | string | No | No | UUID of the characteristic, for example, **00002a11-0000-1000-8000-00805f9b34fb**. |
| descriptorUuid | string | No | No | UUID of the descriptor, for example, **00002902-0000-1000-8000-00805f9b34fb**. |
| descriptorValue | ArrayBuffer | No | No | Binary value of the descriptor. |

#### NotifyCharacteristic(deprecated)

Defines the parameters in the notifications sent when the server characteristic value changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/iDYALfFcTyC56btmidhTiw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9549697129C6EE5B881B6416D04705053DAD7C1C5D305A6A86B3191775635C2)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.NotifyCharacteristic](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#notifycharacteristic) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | No | No | UUID of the service, for example, **00001888-0000-1000-8000-00805f9b34fb**. |
| characteristicUuid | string | No | No | UUID of the characteristic, for example, **00002a11-0000-1000-8000-00805f9b34fb**. |
| characteristicValue | ArrayBuffer | No | No | Binary value of the characteristic. |
| confirm | boolean | No | No | Whether the notification needs to be confirmed by the remote end. For a notification, set it to **true**. In this case, the remote end must confirm the receipt of the notification. For an indication, set it to **false**. In this case, the remote end does not need to confirm the receipt of the notification. |

#### CharacteristicReadRequest(deprecated)

Defines the parameters of the **CharacteristicReadReq** event received by the server.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/8DIiFZsKQ7W4rNLvuH3OLw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=38AAE080877EFBB92BBE35B37B116A335E9EDDC3FCB614FA81B0BC51E2C44BB9)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.CharacteristicReadRequest](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#characteristicreadrequest) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | Address of the remote device that sends the **CharacteristicReadReq** event, for example, XX:XX:XX:XX:XX:XX. |
| transId | number | No | No | Transmission ID of the read request. The response returned by the server must use the same transmission ID. |
| offset | number | No | No | Start position from which the characteristic value is read. For example, **k** means to read from the kth byte. The response returned by the server must use the same offset. |
| characteristicUuid | string | No | No | UUID of the characteristic, for example, **00002a11-0000-1000-8000-00805f9b34fb**. |
| serviceUuid | string | No | No | UUID of the service, for example, **00001888-0000-1000-8000-00805f9b34fb**. |

#### CharacteristicWriteRequest(deprecated)

Defines the parameters of the **CharacteristicWriteReq** event received by the server.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/OWOmsV3mTc6WBse6UW-Pnw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D4E341BDF4B274928FDDE3775A1AFCA1ACA18B275C1B4206BE3116D98E0ECC4)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.CharacteristicWriteRequest](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#characteristicwriterequest) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | Address of the remote device that sends the **CharacteristicWriteReq** event, for example, XX:XX:XX:XX:XX:XX. |
| transId | number | No | No | Transmission ID of the write request. The response returned by the server must use the same transmission ID. |
| offset | number | No | No | Start position for writing the characteristic value. For example, **k** means to write from the kth byte. The response returned by the server must use the same offset. |
| isPrep | boolean | No | No | Whether the write request is executed immediately. The value **true** means to execute the write request immediately. |
| needRsp | boolean | No | No | Whether to send a response to the GATT client. The value **true** means to send a response. |
| value | ArrayBuffer | No | No | Binary value of the descriptor to write. |
| characteristicUuid | string | No | No | UUID of the characteristic, for example, **00002a11-0000-1000-8000-00805f9b34fb**. |
| serviceUuid | string | No | No | UUID of the service, for example, **00001888-0000-1000-8000-00805f9b34fb**. |

#### DescriptorReadRequest(deprecated)

Defines the parameters of the **DescriptorReadReq** event received by the server.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/O_sI_m4bTEqSWMjcZA1jYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71B985067B043722CC1DE37AD36FE4702855BC3295092D2B84C732AF23FAA306)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.DescriptorReadRequest](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#descriptorreadrequest) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | Address of the remote device that sends the **DescriptorReadReq** event, for example, XX:XX:XX:XX:XX:XX. |
| transId | number | No | No | Transmission ID of the read request. The response returned by the server must use the same transmission ID. |
| offset | number | No | No | Start position from which the descriptor is read. For example, **k** means to read from the kth byte. The response returned by the server must use the same offset. |
| descriptorUuid | string | No | No | UUID of the descriptor, for example, **00002902-0000-1000-8000-00805f9b34fb**. |
| characteristicUuid | string | No | No | UUID of the characteristic, for example, **00002a11-0000-1000-8000-00805f9b34fb**. |
| serviceUuid | string | No | No | UUID of the service, for example, **00001888-0000-1000-8000-00805f9b34fb**. |

#### DescriptorWriteRequest(deprecated)

Defines the parameters of the **DescriptorWriteReq** event received by the server.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/TUztvoCZTZ6JWCoVFmfvhQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C83A25A5B85B27BB72A95B4E86CD533620D8EB055D80012555134B4D29F7AEFB)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.DescriptorWriteRequest](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#descriptorwriterequest) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | Address of the remote device that sends the **DescriptorWriteReq** event, for example, XX:XX:XX:XX:XX:XX. |
| transId | number | No | No | Transmission ID of the write request. The response returned by the server must use the same transmission ID. |
| offset | number | No | No | Start position for writing the descriptor. For example, **k** means to write from the kth byte. The response returned by the server must use the same offset. |
| isPrep | boolean | No | No | Whether the write request is executed immediately. |
| needRsp | boolean | No | No | Whether to send a response to the GATT client. |
| value | ArrayBuffer | No | No | Binary value of the descriptor to write. |
| descriptorUuid | string | No | No | UUID of the descriptor, for example, **00002902-0000-1000-8000-00805f9b34fb**. |
| characteristicUuid | string | No | No | UUID of the characteristic, for example, **00002a11-0000-1000-8000-00805f9b34fb**. |
| serviceUuid | string | No | No | UUID of the service, for example, **00001888-0000-1000-8000-00805f9b34fb**. |

#### ServerResponse(deprecated)

Defines the parameters of the server's response to the GATT client's read/write request.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/50FLyUudRhixYImel9M2cg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F38C1C1E78D0ECF869DA88B195B60A42EBB7A5FCD2C5542008BAAEBD5AA6A412)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.ServerResponse](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#serverresponse) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | Address of the remote device, for example, XX:XX:XX:XX:XX:XX. |
| transId | number | No | No | Transmission ID of the request. The value must be the same as the ID carried in the read/write request received. |
| status | number | No | No | Response state. Set this parameter to **0**, which indicates a normal response. |
| offset | number | No | No | Start read/write position. The value must be the same as the offset carried in the read/write request. |
| value | ArrayBuffer | No | No | Binary data in the response. |

#### BLEConnectChangedState(deprecated)

Defines the parameters of **BLEConnectChangedState**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/48w_bhd6StaLrx4S30hXyg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0CC6D02826521CF0B9CB03AB2E0886E9E45B84B67DD986677F94D67C92BC2957)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [BLEConnectionChangeState](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#bleconnectionchangestate) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | Address of the remote device, for example, XX:XX:XX:XX:XX:XX. |
| state | [ProfileConnectionState](#profileconnectionstatedeprecated) | No | No | BLE connection state. |

#### ProfileConnectionState(deprecated)

Enumerates the profile connection states.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/h3FL1XReSeOaSbBWYXWbVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=577C32E9F554A2F621E9D0A35D797154E907C74A2D94E7D4C0BCD274E873F10D)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [constant.ProfileConnectionState](../../arkts-apis/ohos-bluetooth-constant-bluetooth-constant-module/document.md#profileconnectionstate) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| STATE\_DISCONNECTED | 0 | Disconnected. |
| STATE\_CONNECTING | 1 | Connecting. |
| STATE\_CONNECTED | 2 | Connected. |
| STATE\_DISCONNECTING | 3 | Disconnecting. |

#### ScanFilter(deprecated)

Defines the scan filter parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/3Fa5k91xSYufmV848CH33g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44D4C542336D768BF4E8B92E6D082A78C6F9A6A167969D49F6D85549EE8273F2)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.ScanFilter](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#scanfilter) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | Yes | Address of the BLE device to filter, for example, XX:XX:XX:XX:XX:XX. |
| name | string | No | Yes | Name of the BLE device to filter. |
| serviceUuid | string | No | Yes | Service UUID of the device to filter, for example, **00001888-0000-1000-8000-00805f9b34fb**. |
| serviceUuidMask | string | No | Yes | Service UUID mask of the device to filter, for example, **FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF**. |
| serviceSolicitationUuid | string | No | Yes | Service solicitation UUID of the device to filter, for example, **00001888-0000-1000-8000-00805F9B34FB**. |
| serviceSolicitationUuidMask | string | No | Yes | Service solicitation UUID mask of the device to filter, for example, **FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF**. |
| serviceData | ArrayBuffer | No | Yes | Service data of the device to filter, for example, **\[0x90, 0x00, 0xF1, 0xF2\]**. |
| serviceDataMask | ArrayBuffer | No | Yes | Service data mask of the device to filter, for example, **\[0xFF,0xFF,0xFF,0xFF\]**. |
| manufactureId | number | No | Yes | Manufacturer ID of the device to filter, for example, **0x0006**. |
| manufactureData | ArrayBuffer | No | Yes | Manufacturer data of the device to filter, for example, **\[0x1F,0x2F,0x3F\]**. |
| manufactureDataMask | ArrayBuffer | No | Yes | Manufacturer data mask of the device to filter, for example, **\[0xFF, 0xFF, 0xFF\]**. |

#### ScanOptions(deprecated)

Defines the scan configuration parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/XyJi5-RtR8uIVzJstm5bVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=586F36CFE96D503E41BAF3D469A698325FFC450E947B29D0D8E4B8D4AF8A6084)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.ScanOptions](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#scanoptions) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| interval | number | No | Yes | Delay in reporting the scan result. The default value is **0**. |
| dutyMode | [ScanDuty](#scandutydeprecated) | No | Yes | Scan duty. The default value is SCAN\_MODE\_LOW\_POWER. |
| matchMode | [MatchMode](#matchmodedeprecated) | No | Yes | Hardware filtering match mode. The default value is **MATCH\_MODE\_AGGRESSIVE**. |

#### ScanDuty(deprecated)

Enumerates the scan modes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/zehwipffR82iLqfEeBs0lA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=736E0C9EE671922AA2DF395674FA8EF7310C627434EFFAE7CBC052934CB71AD2)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.ScanDuty](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#scanduty) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SCAN\_MODE\_LOW\_POWER | 0 | Low-power mode, which is the default value. |
| SCAN\_MODE\_BALANCED | 1 | Balanced mode. |
| SCAN\_MODE\_LOW\_LATENCY | 2 | Low-latency mode. |

#### MatchMode(deprecated)

Enumerates the hardware match modes of BLE scan filters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/JE81WrABShWKVBzJOAMOiw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69146F1F73BE48BB4B0F028B325E6ED0F01DCA4729D001A4A100F110CCB9158A)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.MatchMode](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#matchmode) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| MATCH\_MODE\_AGGRESSIVE | 1 | Hardware reports the scan result with a lower threshold of signal strength and few number of matches in a duration. This is the default value. |
| MATCH\_MODE\_STICKY | 2 | Hardware reports the scan result with a higher threshold of signal strength and sightings. |

#### ScanResult(deprecated)

Defines the scan result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/qUZ9BG8NTD6xo7WTIIIK-w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84F099EE9585A1EA230CD5E4D9418380ED88718AD32EA07F47132407EAE80C04)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.ScanResult](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#scanresult) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | Address of the device discovered, for example, XX:XX:XX:XX:XX:XX. |
| rssi | number | No | No | RSSI of the device. |
| data | ArrayBuffer | No | No | Advertisement packets sent by the device. |

#### BluetoothState(deprecated)

Enumerates the Bluetooth states.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/CHKDkkvbQu-wUgBSxp-oVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=253DB58C932FD7D05E012E7EB27AB4BE0273F38B4A9693723D0A8840EFE890BE)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [access.BluetoothState](../../arkts-apis/ohos-bluetooth-access-bluetooth-access-module/document.md#bluetoothstate) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| STATE\_OFF | 0 | Bluetooth is turned off. |
| STATE\_TURNING\_ON | 1 | Bluetooth is being turned on. |
| STATE\_ON | 2 | Bluetooth is turned on. |
| STATE\_TURNING\_OFF | 3 | Bluetooth is being turned off. |
| STATE\_BLE\_TURNING\_ON | 4 | The LE-only mode is being turned on for Bluetooth. |
| STATE\_BLE\_ON | 5 | Bluetooth is in LE-only mode. |
| STATE\_BLE\_TURNING\_OFF | 6 | The LE-only mode is being turned off for Bluetooth. |

#### AdvertiseSetting(deprecated)

Defines the BLE advertising parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/kFrX847YRtKwLV9P7WzaZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=419A014AE3C6720B5834C0072DCC40F159DC8D1727BD9A7581EC41E915E7855B)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.AdvertiseSetting](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#advertisesetting) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| interval | number | No | Yes | Interval for BLE advertising. The minimum value is **32** slots (20 ms). The maximum value is **16384** slots. The default value is **1600** slots (1s). |
| txPower | number | No | Yes | Transmit power, in dBm. The value range is -127 to 1. The default value is **\-7**. |
| connectable | boolean | No | Yes | Whether the advertisement is connectable. The default value is **true**. |

#### AdvertiseData(deprecated)

Defines the content of a BLE advertisement packet.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/k0D73METRWW8Ro3xTLfBZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F9E03D51078BEF0686960BE86821B82B67FFA53FE3D9B5FE30ADA8583E8D5FA2)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.AdvertiseData](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#advertisedata) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuids | Array<string> | No | No | List of service UUIDs to broadcast. |
| manufactureData | Array<[ManufactureData](#manufacturedatadeprecated)\> | No | No | List of manufacturers to broadcast. |
| serviceData | Array<[ServiceData](#servicedatadeprecated)\> | No | No | List of service data to broadcast. |

#### ManufactureData(deprecated)

Defines the content of a BLE advertisement packet.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/Cjj3J4m4QSuBgl1nCDl0xg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99CB40D76FC246C54139D71363D34B03E99558A6EE5AB12ECE24D69249A706BF)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.ManufactureData](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#manufacturedata) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| manufactureId | number | No | No | Manufacturer ID allocated by the Bluetooth SIG. |
| manufactureValue | ArrayBuffer | No | No | Manufacturer data. |

#### ServiceData(deprecated)

Defines the service data contained in an advertisement packet.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/pW_RWhk2SWOQ-hPl1M4k6g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88F3149D1B88FF2F3CAF3577FB7AA2483D8CC21F898F2D30FE7910843D2AA736)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [ble.ServiceData](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md#servicedata) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | No | No | Service UUID. |
| serviceValue | ArrayBuffer | No | No | Service data. |

#### PinRequiredParam(deprecated)

Defines the pairing request parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/yS335s1ZQhK2BaEH-OShVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=575EDB1E33533F6A376094E9C2DFD579C5A93DFF4EBF4549CD21E6A19A07AA19)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.PinRequiredParam](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#pinrequiredparam) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | ID of the device to pair. |
| pinCode | string | No | No | Key for the device pairing. |

#### BondStateParam(deprecated)

Defines the pairing state parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/1Bc9CeaYS4qunLNcBCGS7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1503262FC9D97C02B69CB1ABA1BBF1F5E81980EE67BB8BE9763CF62D3692A6D8)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.BondStateParam](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#bondstateparam) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | ID of the device to pair. |
| state | BondState | No | No | State of the device. |

#### StateChangeParam(deprecated)

Defines the profile state change parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/_klORxMJQi-lg7Iw4pGlXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B08AD969ED0C5A26C9802A7E5DC3142E17EE9FF7FCCF93D4DC1548C66FF3302D)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [baseProfile.StateChangeParam](../../arkts-apis/ohos-bluetooth-baseprofile-bluetooth-baseprofile-module/document.md#statechangeparam) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | Address of a Bluetooth device. |
| state | [ProfileConnectionState](#profileconnectionstatedeprecated) | No | No | Profile connection state of the device. |

#### DeviceClass(deprecated)

Defines the class of a Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/jRjThlE8QfaZN1CTdQo5oQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFD444FE7D72067BBBDA338E0762A996CAC7C35E53E3EC5504D2922D1C0FE1A5)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [connection.DeviceClass](../../arkts-apis/ohos-bluetooth-connection-bluetooth-connection-module/document.md#deviceclass) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| majorClass | [MajorClass](#majorclassdeprecated) | No | No | Major classes of Bluetooth devices. |
| majorMinorClass | [MajorMinorClass](#majorminorclassdeprecated) | No | No | Major and minor classes of Bluetooth devices. |
| classOfDevice | number | No | No | Class of the device. |

#### MajorClass(deprecated)

Enumerates the major classes of Bluetooth devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/LEGfyrqEQaGfnqaPkCOzHA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=09F3C5754B984BAA8B4AFD04BE99D4D0E6A584332D463124F565E64D826F7619)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [constant.MajorClass](../../arkts-apis/ohos-bluetooth-constant-bluetooth-constant-module/document.md#majorclass) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| MAJOR\_MISC | 0x0000 | Miscellaneous device. |
| MAJOR\_COMPUTER | 0x0100 | Computer. |
| MAJOR\_PHONE | 0x0200 | Mobile phone. |
| MAJOR\_NETWORKING | 0x0300 | Network device. |
| MAJOR\_AUDIO\_VIDEO | 0x0400 | Audio or video device. |
| MAJOR\_PERIPHERAL | 0x0500 | Peripheral device. |
| MAJOR\_IMAGING | 0x0600 | Imaging device. |
| MAJOR\_WEARABLE | 0x0700 | Wearable device. |
| MAJOR\_TOY | 0x0800 | Toy. |
| MAJOR\_HEALTH | 0x0900 | Health device. |
| MAJOR\_UNCATEGORIZED | 0x1F00 | Unclassified device. |

#### MajorMinorClass(deprecated)

Enumerates the major and minor classes of Bluetooth devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/dBeYrvoTRwCiLhdWoUWicQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB7961E76CC2D4B88244030FB5A1C77ACCB1C0967FE82773B59FD2C721778A3A)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [constant.MajorMinorClass](../../arkts-apis/ohos-bluetooth-constant-bluetooth-constant-module/document.md#majorminorclass) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| COMPUTER\_UNCATEGORIZED | 0x0100 | Unclassified computer. |
| COMPUTER\_DESKTOP | 0x0104 | Desktop computer. |
| COMPUTER\_SERVER | 0x0108 | Server. |
| COMPUTER\_LAPTOP | 0x010C | Laptop. |
| COMPUTER\_HANDHELD\_PC\_PDA | 0x0110 | Hand-held computer. |
| COMPUTER\_PALM\_SIZE\_PC\_PDA | 0x0114 | Palmtop computer. |
| COMPUTER\_WEARABLE | 0x0118 | Wearable computer. |
| COMPUTER\_TABLET | 0x011C | Tablet. |
| PHONE\_UNCATEGORIZED | 0x0200 | Unclassified mobile phone. |
| PHONE\_CELLULAR | 0x0204 | Portable phone. |
| PHONE\_CORDLESS | 0x0208 | Cordless phone. |
| PHONE\_SMART | 0x020C | Smartphone. |
| PHONE\_MODEM\_OR\_GATEWAY | 0x0210 | Modem or gateway phone. |
| PHONE\_ISDN | 0x0214 | ISDN phone. |
| NETWORK\_FULLY\_AVAILABLE | 0x0300 | Device with network fully available. |
| NETWORK\_1\_TO\_17\_UTILIZED | 0x0320 | Device used on network 1 to 17. |
| NETWORK\_17\_TO\_33\_UTILIZED | 0x0340 | Device used on network 17 to 33. |
| NETWORK\_33\_TO\_50\_UTILIZED | 0x0360 | Device used on network 33 to 50. |
| NETWORK\_60\_TO\_67\_UTILIZED | 0x0380 | Device used on network 60 to 67. |
| NETWORK\_67\_TO\_83\_UTILIZED | 0x03A0 | Device used on network 67 to 83. |
| NETWORK\_83\_TO\_99\_UTILIZED | 0x03C0 | Device used on network 83 to 99. |
| NETWORK\_NO\_SERVICE | 0x03E0 | Device without network service |
| AUDIO\_VIDEO\_UNCATEGORIZED | 0x0400 | Unclassified audio or video device. |
| AUDIO\_VIDEO\_WEARABLE\_HEADSET | 0x0404 | Wearable audio or video headset. |
| AUDIO\_VIDEO\_HANDSFREE | 0x0408 | Hands-free audio or video device. |
| AUDIO\_VIDEO\_MICROPHONE | 0x0410 | Audio or video microphone. |
| AUDIO\_VIDEO\_LOUDSPEAKER | 0x0414 | Audio or video loudspeaker. |
| AUDIO\_VIDEO\_HEADPHONES | 0x0418 | Audio or video headphones. |
| AUDIO\_VIDEO\_PORTABLE\_AUDIO | 0x041C | Portable audio or video device. |
| AUDIO\_VIDEO\_CAR\_AUDIO | 0x0420 | In-vehicle audio or video device. |
| AUDIO\_VIDEO\_SET\_TOP\_BOX | 0x0424 | Audio or video STB device. |
| AUDIO\_VIDEO\_HIFI\_AUDIO | 0x0428 | High-fidelity speaker device. |
| AUDIO\_VIDEO\_VCR | 0x042C | Video cassette recording (VCR) device. |
| AUDIO\_VIDEO\_VIDEO\_CAMERA | 0x0430 | Camera. |
| AUDIO\_VIDEO\_CAMCORDER | 0x0434 | Camcorder |
| AUDIO\_VIDEO\_VIDEO\_MONITOR | 0x0438 | Audio or video monitor. |
| AUDIO\_VIDEO\_VIDEO\_DISPLAY\_AND\_LOUDSPEAKER | 0x043C | Video display or loudspeaker. |
| AUDIO\_VIDEO\_VIDEO\_CONFERENCING | 0x0440 | Video conferencing device. |
| AUDIO\_VIDEO\_VIDEO\_GAMING\_TOY | 0x0448 | Audio or video gaming toy. |
| PERIPHERAL\_NON\_KEYBOARD\_NON\_POINTING | 0x0500 | Non-keyboard or non-pointing peripheral device. |
| PERIPHERAL\_KEYBOARD | 0x0540 | Keyboard device. |
| PERIPHERAL\_POINTING\_DEVICE | 0x0580 | Pointing peripheral device. |
| PERIPHERAL\_KEYBOARD\_POINTING | 0x05C0 | Keyboard pointing device. |
| PERIPHERAL\_UNCATEGORIZED | 0x0500 | Unclassified peripheral device. |
| PERIPHERAL\_JOYSTICK | 0x0504 | Peripheral joystick. |
| PERIPHERAL\_GAMEPAD | 0x0508 | Peripheral game pad |
| PERIPHERAL\_REMOTE\_CONTROL | 0x05C0 | Peripheral remote control device |
| PERIPHERAL\_SENSING\_DEVICE | 0x0510 | Peripheral sensing device. |
| PERIPHERAL\_DIGITIZER\_TABLET | 0x0514 | Peripheral digitizer tablet. |
| PERIPHERAL\_CARD\_READER | 0x0518 | Peripheral card reader. |
| PERIPHERAL\_DIGITAL\_PEN | 0x051C | Peripheral digital pen. |
| PERIPHERAL\_SCANNER\_RFID | 0x0520 | Peripheral RFID scanner. |
| PERIPHERAL\_GESTURAL\_INPUT | 0x0522 | Gesture input device. |
| IMAGING\_UNCATEGORIZED | 0x0600 | Unclassified imaging device. |
| IMAGING\_DISPLAY | 0x0610 | Imaging display device. |
| IMAGING\_CAMERA | 0x0620 | Imaging camera device. |
| IMAGING\_SCANNER | 0x0640 | Imaging scanner. |
| IMAGING\_PRINTER | 0x0680 | Imaging printer. |
| WEARABLE\_UNCATEGORIZED | 0x0700 | Unclassified wearable device. |
| WEARABLE\_WRIST\_WATCH | 0x0704 | Smart watch. |
| WEARABLE\_PAGER | 0x0708 | Wearable pager. |
| WEARABLE\_JACKET | 0x070C | Smart jacket. |
| WEARABLE\_HELMET | 0x0710 | Wearable helmet. |
| WEARABLE\_GLASSES | 0x0714 | Wearable glasses. |
| TOY\_UNCATEGORIZED | 0x0800 | Unclassified toy. |
| TOY\_ROBOT | 0x0804 | Toy robot. |
| TOY\_VEHICLE | 0x0808 | Toy vehicle. |
| TOY\_DOLL\_ACTION\_FIGURE | 0x080C | Humanoid toy doll. |
| TOY\_CONTROLLER | 0x0810 | Toy controller. |
| TOY\_GAME | 0x0814 | Toy gaming device. |
| HEALTH\_UNCATEGORIZED | 0x0900 | Unclassified health devices. |
| HEALTH\_BLOOD\_PRESSURE | 0x0904 | Blood pressure device. |
| HEALTH\_THERMOMETER | 0x0908 | Thermometer |
| HEALTH\_WEIGHING | 0x090C | Body scale. |
| HEALTH\_GLUCOSE | 0x0910 | Blood glucose monitor. |
| HEALTH\_PULSE\_OXIMETER | 0x0914 | Pulse oximeter. |
| HEALTH\_PULSE\_RATE | 0x0918 | Heart rate monitor. |
| HEALTH\_DATA\_DISPLAY | 0x091C | Health data display. |
| HEALTH\_STEP\_COUNTER | 0x0920 | Step counter. |
| HEALTH\_BODY\_COMPOSITION\_ANALYZER | 0x0924 | Body composition analyzer. |
| HEALTH\_PEAK\_FLOW\_MONITOR | 0x0928 | Hygrometer. |
| HEALTH\_MEDICATION\_MONITOR | 0x092C | Medication monitor. |
| HEALTH\_KNEE\_PROSTHESIS | 0x0930 | Prosthetic knee. |
| HEALTH\_ANKLE\_PROSTHESIS | 0x0934 | Prosthetic ankle. |
| HEALTH\_GENERIC\_HEALTH\_MANAGER | 0x0938 | Generic health management device. |
| HEALTH\_PERSONAL\_MOBILITY\_DEVICE | 0x093C | Personal mobility device. |

#### PlayingState(deprecated)

Enumerates the A2DP playing states.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/7lgIJwDfRgO9m3vf7qYYRg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F2C7685D2694B5C3EFD49B7F8CD2065C21C89976AF07CD2B1B8D1485CBD738F)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [a2dp.PlayingState](../../arkts-apis/ohos-bluetooth-a2dp-bluetooth-a2dp-module/document.md#playingstate) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| STATE\_NOT\_PLAYING | 0x0000 | Not playing. |
| STATE\_PLAYING | 0x0001 | Playing. |

#### ProfileId(deprecated)

Enumerates the Bluetooth profiles. API version 9 is added with **PROFILE\_HID\_HOST** and **PROFILE\_PAN\_NETWORK**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/NsI2H-usR-qjIa90U_sgkw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA8CF2CB13E7D39D76E6FDE9E7326B8607F93E43784F0BF9E84DAF5CFA8EE937)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [constant.ProfileId](../../arkts-apis/ohos-bluetooth-constant-bluetooth-constant-module/document.md#profileid) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| PROFILE\_A2DP\_SOURCE | 1 | A2DP profile. |
| PROFILE\_HANDS\_FREE\_AUDIO\_GATEWAY | 4 | HFP profile. |
| PROFILE\_HID\_HOST | 6 | Human Interface Device (HID) profile. |
| PROFILE\_PAN\_NETWORK | 7 | PAN profile. |
