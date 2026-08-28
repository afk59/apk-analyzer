# @ohos.bluetooth.access (Bluetooth Access Module)

The **access** module provides APIs for enabling and disabling Bluetooth and obtaining the Bluetooth status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/Z4Nw1FrmRiCwq5tgKmpCcQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B765FB3A4F7E98C1A8632E8BC211D9A43CFE3AC564C81978FDDDE51106E8D22)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { access } from '@kit.ConnectivityKit';

#### access.enableBluetooth

enableBluetooth(): void

Enables Bluetooth.

-   When this API is called, a dialog box is displayed, asking you whether to enable Bluetooth. If your application needs to detect the user's action in operating the Bluetooth switch dialog, you are advised to use [access.enableBluetoothAsync](#accessenablebluetoothasync20).
-   You can obtain the Bluetooth switch status through the [access.on('stateChange')](#accessonstatechange) callback.
-   You are advised to call this API only when the Bluetooth switch status is [STATE\_OFF](#bluetoothstate). (You can call [access.getState](#accessgetstate) to check the Bluetooth switch status.)

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    access.enableBluetooth();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### access.enableBluetoothAsync20+

enableBluetoothAsync(): Promise<void>

Enables Bluetooth. This API uses a promise to return the result.

-   When this API is called, a dialog box is displayed, asking you whether to enable Bluetooth. Allows the application to detect the user's action in operating the Bluetooth switch dialog.
-   You can obtain the Bluetooth switch status through the [access.on('stateChange')](#accessonstatechange) callback.
-   You are advised to call this API only when the Bluetooth switch status is [STATE\_OFF](#bluetoothstate). (You can call [access.getState](#accessgetstate) to check the Bluetooth switch status.)

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900013 | The user does not respond. |
| 2900014 | User refuse the action. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    access.enableBluetoothAsync().then(() => {
        console.info('enableBluetoothAsync');
    }, (error: BusinessError) => {
        console.error('enableBluetoothAsync: errCode:' + error.code + ',errMessage' + error.message);
    })
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### access.disableBluetooth

disableBluetooth(): void

Disables Bluetooth.

-   When this API is called, a dialog box is displayed, asking you whether to disable Bluetooth. If your application needs to detect the user's action in operating the Bluetooth switch dialog, you are advised to use [access.disableBluetoothAsync](#accessdisablebluetoothasync20).
-   You can obtain the Bluetooth switch status through the [access.on('stateChange')](#accessonstatechange) callback.
-   You are advised to call this API only when the Bluetooth switch status is [STATE\_ON](#bluetoothstate). (You can call [access.getState](#accessgetstate) to check the Bluetooth switch status.)

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    access.disableBluetooth();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### access.disableBluetoothAsync20+

disableBluetoothAsync(): Promise<void>

Disables Bluetooth. This API uses a promise to return the result.

-   When this API is called, a dialog box is displayed, asking you whether to disable Bluetooth. Allows the application to detect the user's action in operating the Bluetooth switch dialog.
-   You can obtain the Bluetooth switch status through the [access.on('stateChange')](#accessonstatechange) callback.
-   You are advised to call this API only when the Bluetooth switch status is [STATE\_ON](#bluetoothstate). (You can call [access.getState](#accessgetstate) to check the Bluetooth switch status.)

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900013 | The user does not respond. |
| 2900014 | User refuse the action. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    access.disableBluetoothAsync().then(() => {
        console.info('disableBluetoothAsync');
    }, (error: BusinessError) => {
        console.error('disableBluetoothAsync: errCode:' + error.code + ',errMessage' + error.message);
    })
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### access.getState

getState(): BluetoothState

Obtains the Bluetooth state.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [BluetoothState](#bluetoothstate) | Bluetooth state obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let state = access.getState();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### access.on('stateChange')

on(type: 'stateChange', callback: Callback<BluetoothState>): void

Enables listening for Bluetooth status change events of the local device. This API uses an asynchronous callback to return the result. Since API version 18, the **ohos.permission.ACCESS\_BLUETOOTH** permission is no longer verified.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. The value **stateChange** indicates a Bluetooth status change event.

For example, this event is triggered when [access.enableBluetooth](#accessenablebluetooth) or [access.disableBluetooth](#accessdisablebluetooth) is called.

 |
| callback | Callback<[BluetoothState](#bluetoothstate)\> | Yes | Callback used to return the Bluetooth switch status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function onReceiveEvent(data: access.BluetoothState) {
    console.info('bluetooth state = '+ JSON.stringify(data));
}
try {
    access.on('stateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### access.off('stateChange')

off(type: 'stateChange', callback?: Callback<BluetoothState>): void

Disables listening for Bluetooth status change events of the local device. Since API version 18, the **ohos.permission.ACCESS\_BLUETOOTH** permission is no longer verified.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **stateChange** indicates a Bluetooth status change event. |
| callback | Callback<[BluetoothState](#bluetoothstate)\> | No | 
Callback to unregister.

If this parameter is specified, it must be the same as the callback in [access.on('stateChange')](#accessonstatechange). If this parameter is not specified, all callbacks corresponding to the event type are unregistered.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function onReceiveEvent(data: access.BluetoothState) {
    console.info('bluetooth state = '+ JSON.stringify(data));
}
try {
    access.on('stateChange', onReceiveEvent);
    access.off('stateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### access.addPersistentDeviceId16+

addPersistentDeviceId(deviceId: string): Promise<void>

Stores the virtual MAC address of a Bluetooth device persistently.

-   The device address (virtual MAC address) obtained through Bluetooth APIs, such as the scan API, is different from the actual device MAC address. The Bluetooth subsystem stores the mapping between the virtual MAC address and the actual device MAC address. If the application wants to perform operations on the Bluetooth device for a long time, you are advised to use this API to store the virtual MAC address of the device persistently. The address mapping will not change.
-   The virtual MAC address to be stored persistently must be valid. You can use [access.isValidRandomDeviceId](#accessisvalidrandomdeviceid16) to check whether its validity.
-   When using this API, ensure that the real address of the peer Bluetooth device corresponding to the virtual MAC address remains unchanged. If the real address of the peer device changes, the persistently stored address will become invalid and unusable.
-   You can call [access.deletePersistentDeviceId](#accessdeletepersistentdeviceid16) to delete the persistently stored virtual MAC address.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH and ohos.permission.PERSISTENT\_BLUETOOTH\_PEERS\_MAC

**Atomic service API**: This API can be used in atomic services since API version 16.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | 
Virtual MAC address of the peer device, for example, XX:XX:XX:XX:XX:XX.

This address is typically obtained from Bluetooth scan results, which can be retrieved, for example, by calling [startScan](../ohos-bluetooth-ble-bluetooth-ble-module/document.md#startscan15) or [connection.startBluetoothDiscovery](../ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectionstartbluetoothdiscovery).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900003 | Bluetooth disabled. |
| 2900010 | The number of supported device addresses has reached the upper limit. |
| 2900099 | Add persistent device address failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let deviceId = '11:22:33:44:55:66' // The address can be obtained through BLE scanning.
try {
    access.addPersistentDeviceId(deviceId);
} catch (err) {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}

#### access.deletePersistentDeviceId16+

deletePersistentDeviceId(deviceId: string): Promise<void>

Deletes the persistently stored virtual MAC address of a Bluetooth device.

-   The virtual MAC address is persistently stored through [access.addPersistentDeviceId](#accessaddpersistentdeviceid16).

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH and ohos.permission.PERSISTENT\_BLUETOOTH\_PEERS\_MAC

**Atomic service API**: This API can be used in atomic services since API version 16.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | 
Virtual MAC address of the peer device, for example, XX:XX:XX:XX:XX:XX.

This address is typically obtained from Bluetooth scan results, which can be retrieved, for example, by calling [startScan](../ohos-bluetooth-ble-bluetooth-ble-module/document.md#startscan15) or [connection.startBluetoothDiscovery](../ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectionstartbluetoothdiscovery).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900003 | Bluetooth disabled. |
| 2900099 | delete persistent device address failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let deviceId = '11:22:33:44:55:66' // The address can be obtained through BLE scanning.
try {
    access.deletePersistentDeviceId(deviceId);
} catch (err) {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}

#### access.getPersistentDeviceIds16+

getPersistentDeviceIds(): string\[\];

Obtains the persistently stored virtual MAC address of a Bluetooth device.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH and ohos.permission.PERSISTENT\_BLUETOOTH\_PEERS\_MAC

**Atomic service API**: This API can be used in atomic services since API version 16.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string\[\] | List of persistently stored virtual MAC addresses. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Get persistent device address failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let deviceIds = access.getPersistentDeviceIds();
} catch (err) {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}

#### access.isValidRandomDeviceId16+

isValidRandomDeviceId(deviceId: string): boolean;

Checks whether the virtual MAC address of the peer device is valid.

-   Valid virtual MAC addresses are typically obtained from Bluetooth scan results, which can be retrieved, for example, by calling [startScan](../ohos-bluetooth-ble-bluetooth-ble-module/document.md#startscan15) or [connection.startBluetoothDiscovery](../ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectionstartbluetoothdiscovery).

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Atomic service API**: This API can be used in atomic services since API version 16.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Virtual MAC address of the peer device, for example, XX:XX:XX:XX:XX:XX. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the virtual MAC address of the Bluetooth device is valid. The value **true** indicates that the MAC address is valid, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Check persistent device address failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let deviceId = '11:22:33:44:55:66' // The address can be obtained through BLE scanning.
    let isValid = access.isValidRandomDeviceId(deviceId);
    console.info("isValid: " + isValid);
} catch (err) {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}

#### BluetoothState

Enumerates the Bluetooth states.

**Atomic service API**: This API can be used in atomic services since API version 11.

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
