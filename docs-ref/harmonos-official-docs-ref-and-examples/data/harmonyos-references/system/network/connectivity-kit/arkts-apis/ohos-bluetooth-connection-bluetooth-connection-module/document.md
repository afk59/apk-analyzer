# @ohos.bluetooth.connection (Bluetooth Connection Module)

The connection module provides capabilities for pairing with, connecting to, and querying the status of Bluetooth devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/JMNgyaydTmWbXTzs6UY1Eg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=535C1B9086E1C9119FC7833D14A899B1B3080CE9615FFD2B65D3C9C040D9AADC)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { connection } from '@kit.ConnectivityKit';

#### ProfileConnectionState

type ProfileConnectionState = constant.ProfileConnectionState

Defines the connection status of the Bluetooth profile. Supported Bluetooth profiles include Advanced Audio Distribution Profile (A2DP), Hands-Free Profile (HFP), and Human Interface Device (HID).

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Type | Description |
| :-- | :-- |
| [constant.ProfileConnectionState](../ohos-bluetooth-constant-bluetooth-constant-module/document.md#profileconnectionstate) | Connection status of the Bluetooth profile. |

#### ProfileId

type ProfileId = constant.ProfileId

Enumerates Bluetooth profiles.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Type | Description |
| :-- | :-- |
| [constant.ProfileId](../ohos-bluetooth-constant-bluetooth-constant-module/document.md#profileid) | Bluetooth profile. |

#### ProfileUuids12+

type ProfileUuids = constant.ProfileUuids

Defines the UUID of the Bluetooth profile.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Type | Description |
| :-- | :-- |
| [constant.ProfileUuids](../ohos-bluetooth-constant-bluetooth-constant-module/document.md#profileuuids12) | Defines the UUID of the Bluetooth profile. |

#### MajorClass

type MajorClass = constant.MajorClass

Defines the Bluetooth device major class. This is a standard field in the Bluetooth protocol.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Type | Description |
| :-- | :-- |
| [constant.MajorClass](../ohos-bluetooth-constant-bluetooth-constant-module/document.md#majorclass) | Bluetooth device major class. |

#### MajorMinorClass

type MajorMinorClass = constant.MajorMinorClass

Defines the Bluetooth device subclass, which is further classified based on [MajorClass](../ohos-bluetooth-constant-bluetooth-constant-module/document.md#majorclass). This is a standard field in the Bluetooth protocol.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Type | Description |
| :-- | :-- |
| [constant.MajorMinorClass](../ohos-bluetooth-constant-bluetooth-constant-module/document.md#majorminorclass) | Bluetooth device subclass. |

#### BluetoothAddress21+

type BluetoothAddress = common.BluetoothAddress

Defines the address information of a Bluetooth device, including the address and address type.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Type | Description |
| :-- | :-- |
| [common.BluetoothAddress](../ohos-bluetooth-common-bluetooth-common-module/document.md#bluetoothaddress) | Address information of the Bluetooth device. |

#### connection.pairDevice

pairDevice(deviceId: string, callback: AsyncCallback<void>): void

Initiates pairing with the peer Bluetooth device. This API uses an asynchronous callback to return the result.

-   If you do not know the [address type](../ohos-bluetooth-common-bluetooth-common-module/document.md#bluetoothaddresstype) of the target device, you are advised to call this API to initiate pairing.
-   You can obtain the Bluetooth pairing status from the callback of [on('bondStateChange')](#connectiononbondstatechange).

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the peer Bluetooth device, for example, XX:XX:XX:XX:XX:XX. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the pairing is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

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

import { BusinessError } from '@kit.BasicServicesKit';
// callback
try {
    connection.pairDevice('11:22:33:44:55:66', (err: BusinessError) => {
        console.info('pairDevice, device name err:' + JSON.stringify(err));
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.pairDevice

pairDevice(deviceId: string): Promise<void>

Initiates pairing with the peer Bluetooth device. This API uses a promise to return the result.

-   If you do not know the [address type](../ohos-bluetooth-common-bluetooth-common-module/document.md#bluetoothaddresstype) of the target device, you are advised to call this API to initiate pairing.
-   You can obtain the Bluetooth pairing status from the callback of [on('bondStateChange')](#connectiononbondstatechange).

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the peer Bluetooth device, for example, XX:XX:XX:XX:XX:XX. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

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

import { BusinessError } from '@kit.BasicServicesKit';
// promise
try {
    connection.pairDevice('11:22:33:44:55:66').then(() => {
        console.info('pairDevice');
    }, (error: BusinessError) => {
        console.error('pairDevice: errCode:' + error.code + ',errMessage' + error.message);
    })

} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.pairDevice21+

pairDevice(deviceId: BluetoothAddress): Promise<void>

Initiates pairing with the peer Bluetooth device. This API uses a promise to return the result.

-   If you know the MAC address and [address type](../ohos-bluetooth-common-bluetooth-common-module/document.md#bluetoothaddresstype) of the target device, you are advised to call this API to initiate pairing.
-   You can obtain the Bluetooth pairing status from the callback of [on('bondStateChange')](#connectiononbondstatechange).

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | [BluetoothAddress](../ohos-bluetooth-common-bluetooth-common-module/document.md#bluetoothaddress) | Yes | Address information of the peer Bluetooth device, including the address and address type. |

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
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.ConnectivityKit';
// promise
try {
    let btAddr: common.BluetoothAddress = {
        "address": '11:22:33:44:55:66', // Actual or virtual MAC address of the target device.
        "addressType": common.BluetoothAddressType.REAL, // Address type of the target device.
    }
    connection.pairDevice(btAddr).then(() => {
        console.info('pairDevice');
    }, (error: BusinessError) => {
        console.error('errCode: ' + error.code + ', errMessage' + error.message);
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.getRemoteDeviceName

getRemoteDeviceName(deviceId: string): string

Obtains the name of the peer Bluetooth device.

-   Starting from API version 21, this API can be used to obtain the device name by using the actual MAC address of the peer device.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the peer device, for example, XX:XX:XX:XX:XX:XX. |

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

import { BusinessError } from '@kit.BasicServicesKit';
try {
    let remoteDeviceName: string = connection.getRemoteDeviceName('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.getRemoteDeviceName16+

getRemoteDeviceName(deviceId: string, alias?: boolean): string

Obtains the name of the peer device. The **alias** parameter is optional.

-   Starting from API version 21, this API can be used to obtain the device name by using the actual MAC address of the peer device.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Atomic service API**: This API can be used in atomic services since API version 16.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the peer device, for example, XX:XX:XX:XX:XX:XX. |
| alias | boolean | No | 
Whether to obtain the alias of the peer device.

\- If **alias** is present, the application determines whether to obtain the alias of the peer device. The value **true** means to obtain the alias, and the value **false** means to obtain the original name .

\- If **alias** is not present, the default value is **true**, which means to obtain the alias of the peer device.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Device name (a string) obtained. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Failed to obtain the name or alias of the peer Bluetooth device. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
try {
    let remoteDeviceName: string = connection.getRemoteDeviceName('XX:XX:XX:XX:XX:XX', true);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.getRemoteDeviceClass

getRemoteDeviceClass(deviceId: string): DeviceClass

Obtains the class of the peer Bluetooth device.

-   Starting from API version 18, this API does not verify the ohos.permission.ACCESS\_BLUETOOTH permission.
-   Starting from API version 21, this API can be used to obtain the device class by using the actual MAC address of the peer device.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the peer device, for example, XX:XX:XX:XX:XX:XX. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DeviceClass](#deviceclass) | Class of the peer device. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
try {
    let remoteDeviceClass: connection.DeviceClass = connection.getRemoteDeviceClass('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.getRemoteDeviceTransport20+

getRemoteDeviceTransport(deviceId: string): BluetoothTransport

Obtains the transport type of the peer Bluetooth device.

-   Starting from API version 21, this API can be used to obtain the transport type of the peer device by using the actual MAC address of the peer device.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the peer device, for example, XX:XX:XX:XX:XX:XX. |

**Return value**

| Type | Description |
| :-- | :-- |
| [BluetoothTransport](#bluetoothtransport) | Transport type of the peer device. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Get transport failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
try {
    let transport: connection.BluetoothTransport = connection.getRemoteDeviceTransport('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.getRemoteProfileUuids12+

getRemoteProfileUuids(deviceId: string, callback: AsyncCallback<Array<ProfileUuids>>): void

Obtains the profile of the peer Bluetooth device based on the specified UUID. This API uses an asynchronous callback to return the result.

-   You are advised to use this API only for paired devices.
-   Starting from API version 21, this API can be used to obtain the profile of the peer Bluetooth device based on the actual MAC address of the peer device.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the peer device, for example, XX:XX:XX:XX:XX:XX. |
| callback | AsyncCallback<Array<[ProfileUuids](../ohos-bluetooth-constant-bluetooth-constant-module/document.md#profileuuids12)\>> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and the set of supported profiles is returned. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
try {
    connection.getRemoteProfileUuids('XX:XX:XX:XX:XX:XX', (err: BusinessError, data: Array<connection.ProfileUuids>) => {
        console.info('getRemoteProfileUuids, err: ' + JSON.stringify(err) + ', data: ' + JSON.stringify(data));
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.getRemoteProfileUuids12+

getRemoteProfileUuids(deviceId: string): Promise<Array<ProfileUuids>>

Obtains the profile of the peer Bluetooth device based on the specified UUID. This API uses a promise to return the result.

-   You are advised to use this API only for paired devices.
-   Starting from API version 21, this API can be used to obtain the profile of the peer Bluetooth device based on the actual MAC address of the peer device.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the peer device, for example, XX:XX:XX:XX:XX:XX. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[ProfileUuids](../ohos-bluetooth-constant-bluetooth-constant-module/document.md#profileuuids12)\>> | Promise used to return the set of supported profiles. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
try {
    connection.getRemoteProfileUuids('XX:XX:XX:XX:XX:XX').then(() => {
        console.info('getRemoteProfileUuids');
    }, (err: BusinessError) => {
        console.error('getRemoteProfileUuids: errCode' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.getLocalName

getLocalName(): string

Obtains the name of the local Bluetooth device.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Name of the local Bluetooth device. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
try {
    let localName: string = connection.getLocalName();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.getPairedDevices

getPairedDevices(): Array<string>

Obtains the addresses of paired Bluetooth devices.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | 
Addresses of paired Bluetooth devices.

For security purposes, the device addresses obtained are virtual MAC addresses.

\- The virtual addresses of paired Bluetooth devices will not change.

\- If Bluetooth is disabled and then enabled again, the virtual address will change immediately.

\- If the pairing is canceled, the Bluetooth subsystem will determine when to change the address based on the actual usage of the address. If the address is being used by another application, the address will not change immediately.

\- To persistently save the addresses, call [access.addPersistentDeviceId](../ohos-bluetooth-access-bluetooth-access-module/document.md#accessaddpersistentdeviceid16).

 |

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

import { BusinessError } from '@kit.BasicServicesKit';
try {
    let devices: Array<string> = connection.getPairedDevices();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.getPairState11+

getPairState(deviceId: string): BondState

Obtains the pairing status of the peer Bluetooth device.

-   Starting from API version 21, this API can be used to obtain the pairing status of the peer Bluetooth device based on the actual MAC address of the peer device.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the peer device, for example, XX:XX:XX:XX:XX:XX. |

**Return value**

| Type | Description |
| :-- | :-- |
| [BondState](#bondstate) | Bluetooth pairing state obtained. |

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

import { BusinessError } from '@kit.BasicServicesKit';
try {
    let res: connection.BondState = connection.getPairState("XX:XX:XX:XX:XX:XX");
    console.info('getPairState: ' + res);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.getProfileConnectionState

getProfileConnectionState(profileId?: ProfileId): ProfileConnectionState

Obtains the connection status of a Bluetooth profile. The **ProfileId** parameter is optional.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| profileId | [ProfileId](../ohos-bluetooth-constant-bluetooth-constant-module/document.md#profileid) | No | 
Bluetooth profile. If **ProfileId** is present, the connection status of the specified profile is returned. If **ProfileId** is not present, the connection status of all supported profiles is returned in the following order:

\- If a profile is connected, \[STATE\_CONNECTED\] (js-apis-bluetooth-constant.md#profileconnectionstate) is returned.

\- If a profile is being connected, \[STATE\_CONNECTING\] (js-apis-bluetooth-constant.md#profileconnectionstate) is returned.

\- If a profile is being disconnected, \[STATE\_DISCONNECTING\] (js-apis-bluetooth-constant.md#profileconnectionstate) is returned.

\- If none of the preceding conditions is met, \[STATE\_DISCONNECTED\] (js-apis-bluetooth-constant.md#profileconnectionstate) is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ProfileConnectionState](../ohos-bluetooth-constant-bluetooth-constant-module/document.md#profileconnectionstate) | Connection status of the profile. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { constant } from '@kit.ConnectivityKit';
try {
    let result: connection.ProfileConnectionState = connection.getProfileConnectionState(constant.ProfileId.PROFILE\_A2DP\_SOURCE);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.setDevicePairingConfirmation

setDevicePairingConfirmation(deviceId: string, accept: boolean): void

Confirms the pairing request from the peer Bluetooth device.

-   You can obtain the pairing status of the peer Bluetooth device from the callback of [on('pinRequired')](#connectiononpinrequired).

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH and ohos.permission.MANAGE\_BLUETOOTH (available only for system applications)

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the peer device, for example, XX:XX:XX:XX:XX:XX. |
| accept | boolean | Yes | Whether to accept the pairing request from the peer device. The value **true** means to accept the pairing request, and the value **false** means the opposite. |

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

import { BusinessError } from '@kit.BasicServicesKit';
// Subscribe to the pinRequired event and configure the pairing confirmation after receiving a pairing request from the peer device.
function onReceivePinRequiredEvent(data: connection.PinRequiredParam) { // data is the input parameter for the pairing request.
    console.info('pin required  = '+ JSON.stringify(data));
    connection.setDevicePairingConfirmation(data.deviceId, true);
}
try {
    connection.on('pinRequired', onReceivePinRequiredEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.setDevicePinCode

setDevicePinCode(deviceId: string, code: string, callback: AsyncCallback<void>): void

Sets the PIN used to complete Bluetooth pairing. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | MAC address of the peer device, for example, XX:XX:XX:XX:XX:XX. |
| code | string | Yes | PIN code entered by the user. The value is a string of 0 (not included) to 16 (included) characters, for example, **12345**. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

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

import { BusinessError } from '@kit.BasicServicesKit';
// callback
try {
    connection.setDevicePinCode('11:22:33:44:55:66', '12345', (err: BusinessError) => {
        console.info('setDevicePinCode,device name err: ' + JSON.stringify(err));
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.setDevicePinCode

setDevicePinCode(deviceId: string, code: string): Promise<void>

Sets the PIN used to complete Bluetooth pairing. This API uses a promise to return the result.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | MAC address of the peer device, for example, XX:XX:XX:XX:XX:XX. |
| code | string | Yes | PIN code entered by the user. The value is a string of 0 (not included) to 16 (included) characters, for example, **12345**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

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

import { BusinessError } from '@kit.BasicServicesKit';
// promise
try {
    connection.setDevicePinCode('11:22:33:44:55:66', '12345').then(() => {
        console.info('setDevicePinCode');
    }, (error: BusinessError) => {
        console.error('setDevicePinCode: errCode:' + error.code + ',errMessage' + error.message);
    })

} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.setLocalName(deprecated)

setLocalName(name: string): void

Sets the name of the local Bluetooth device. The value cannot be an empty string. If the value is an empty string, the operation will fail.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/bxWgJCkiTeOer6QDuk9Zew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=38C050A6314A991CFB1597D61715516918B59FA354DBA3BB7870CF2410F1D2AC)

This API is supported since API version 10 and deprecated since API version 12. No substitute is provided.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Bluetooth name. The value is a string of 0 (not included) to 248 (included) bytes. |

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

import { BusinessError } from '@kit.BasicServicesKit';
try {
    connection.setLocalName('device\_name');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.setBluetoothScanMode

setBluetoothScanMode(mode: ScanMode, duration: number): void

Sets the Bluetooth scan mode, which determines whether the local device can be connected or discovered.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [ScanMode](#scanmode) | Yes | Bluetooth scan mode to set. If the scan times out (**duration** is not **0**) when the scan mode is **SCAN\_MODE\_GENERAL\_DISCOVERABLE**, the scan mode will be reset to **SCAN\_MODE\_CONNECTABLE**. |
| duration | number | Yes | Duration during which the device can be discovered, in milliseconds. If the value is set to **0**, the device can be discovered permanently. |

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

import { BusinessError } from '@kit.BasicServicesKit';
try {
    // The device can be discovered and connected only when the discoverable and connectable mode is used.
    connection.setBluetoothScanMode(connection.ScanMode.SCAN\_MODE\_CONNECTABLE\_GENERAL\_DISCOVERABLE, 100);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.getBluetoothScanMode

getBluetoothScanMode(): ScanMode

Obtains the Bluetooth scan mode.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [ScanMode](#scanmode) | Bluetooth scan mode obtained. |

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

import { BusinessError } from '@kit.BasicServicesKit';
try {
    let scanMode: connection.ScanMode = connection.getBluetoothScanMode();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.startBluetoothDiscovery

startBluetoothDiscovery(): void

Starts a Bluetooth scan for device discovery.

-   This API applies to both Bluetooth Classic devices and BLE devices. The entire Bluetooth scan process takes about 12 seconds.
    
-   You can obtain the scan result from the callback of [connection.on('bluetoothDeviceFind')](#connectiononbluetoothdevicefind) (supported since API version 10) or [connection.on('discoveryResult')](#connectionondiscoveryresult18) (supported since API version 18). You are advised to use [connection.on('discoveryResult')](#connectionondiscoveryresult18), which can obtain more detailed device information.
    
-   Do not call this API repeatedly during a scan. You can use [connection.isBluetoothDiscovering](#connectionisbluetoothdiscovering11) to check whether a Bluetooth scan is in progress.
    
-   You can call [connection.stopBluetoothDiscovery](#connectionstopbluetoothdiscovery) to stop the scan. Start the next scan only after the current scan is stopped.
    

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Atomic service API**: This API can be used in atomic services since API version 12.

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

import { BusinessError } from '@kit.BasicServicesKit';
function onReceiveEvent(data: Array<string>) {
    console.info('data length' + data.length);
}
try {
    connection.on('bluetoothDeviceFind', onReceiveEvent);
    connection.startBluetoothDiscovery();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.stopBluetoothDiscovery

stopBluetoothDiscovery(): void

Stops the Bluetooth scan.

-   This API applies only to scans initiated by [connection.startBluetoothDiscovery](#connectionstartbluetoothdiscovery).
    
-   Call this API to stop the Bluetooth scan when device discovery is no longer needed.
    
-   Do not call this API repeatedly if a scan is not in progress. You can use [connection.isBluetoothDiscovering](#connectionisbluetoothdiscovering11) to check whether a Bluetooth scan is in progress.
    

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Atomic service API**: This API can be used in atomic services since API version 12.

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

import { BusinessError } from '@kit.BasicServicesKit';
try {
    connection.stopBluetoothDiscovery();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.isBluetoothDiscovering11+

isBluetoothDiscovering(): boolean

Checks whether the local Bluetooth device is in the device scanning state.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether Bluetooth discovery is in process. The value **true** indicates that Bluetooth discovery is in process, and the value **false** indicates the opposite. |

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

import { BusinessError } from '@kit.BasicServicesKit';
try {
    let res: boolean = connection.isBluetoothDiscovering();
    console.info('isBluetoothDiscovering: ' + res);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.setRemoteDeviceName12+

setRemoteDeviceName(deviceId: string, name: string): Promise<void>

Sets the name of the peer Bluetooth device. The value cannot be an empty string. If the value is an empty string, the operation will fail. This API uses a promise to return the result.

-   You are advised to use this API only for paired devices.
-   Starting from API version 21, this API can be used to set the name of the peer Bluetooth device based on the actual MAC address of the peer device.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | MAC address of the peer device, for example, XX:XX:XX:XX:XX:XX. |
| name | string | Yes | Name of the peer device. The value is a string of 0 (not included) to 64 (included) bytes. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
// promise
try {
    connection.setRemoteDeviceName('11:22:33:44:55:66', 'RemoteDeviceName').then(() => {
        console.info('setRemoteDeviceName success');
    }, (error: BusinessError) => {
        console.error('setRemoteDeviceName: errCode: ' + error.code + ',errMessage' + error.message);
    })
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.getRemoteDeviceBatteryInfo12+

getRemoteDeviceBatteryInfo(deviceId: string): Promise<BatteryInfo>

Obtains the battery level of the peer Bluetooth device. This API uses a promise to return the result.

-   You can obtain the battery level of the peer Bluetooth device from the callback of [on('batteryChange')](#connectiononbatterychange12).
-   Starting from API version 21, this API can be used to obtain the battery level of the peer Bluetooth device based on the actual MAC address of the peer device.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | MAC address of the peer Bluetooth device, for example, XX:XX:XX:XX:XX:XX. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[BatteryInfo](#batteryinfo12)\> | Promise used to return the battery level information. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
// promise
try {
    connection.getRemoteDeviceBatteryInfo('11:22:33:AA:BB:FF').then((data: connection.BatteryInfo) => {
        console.info('getRemoteDeviceBatteryInfo success, DeviceType:' + JSON.stringify(data));
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.on('batteryChange')12+

on(type: 'batteryChange', callback: Callback<BatteryInfo>): void

Subscribes to battery change events of the peer device. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **batteryChange** indicates the battery change event. This event is triggered when the battery level of the peer device changes. |
| callback | Callback<[BatteryInfo](#batteryinfo12)\> | Yes | Callback used to return the battery level information. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let onReceiveEvent: (data: connection.BatteryInfo) => void = (data: connection.BatteryInfo) => {
    console.info('BatteryInfo = '+ JSON.stringify(data));
}
try {
    connection.on('batteryChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.off('batteryChange')12+

off(type: 'batteryChange', callback?: Callback<BatteryInfo>): void

Unsubscribes from battery change events of the peer device.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **batteryChange** indicates the battery change event. |
| callback | Callback<[BatteryInfo](#batteryinfo12)\> | No | 
Callback to unregister.

If this parameter is specified, it must be the same as the callback in [connection.on('batteryChange')](#connectiononbatterychange12). If this parameter is not specified, all callbacks corresponding to the event type are unsubscribed.

 |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let onReceiveEvent: (data: connection.BatteryInfo) => void = (data: connection.BatteryInfo) => {
    console.info('BatteryInfo = '+ JSON.stringify(data));
}
try {
    connection.on('batteryChange', onReceiveEvent);
    connection.off('batteryChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.on('bluetoothDeviceFind')

on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void

Subscribes to scan result reporting events of Bluetooth devices. This API uses an asynchronous callback to return the result.

-   This API applies to both classic Bluetooth devices and BLE devices.
    
-   This API provides only the device address.
    
-   You are advised to use [connection.on('discoveryResult')](#connectionondiscoveryresult18) (supported since API version 18), which can obtain more detailed device information, including the device address, signal strength, name, and type.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **bluetoothDeviceFind** indicates a scan result reporting event. A device scan starts when [connection.startBluetoothDiscovery](#connectionstartbluetoothdiscovery) is called. This event is triggered when a device is discovered. |
| callback | Callback<Array<string>> | Yes | 
Callback used to return the set of device addresses.

For security purposes, the device addresses obtained are virtual MAC addresses.

\- The virtual addresses of paired Bluetooth devices will not change.

\- If Bluetooth is disabled and then enabled again, the virtual address will change immediately.

\- If the pairing is canceled, the Bluetooth subsystem will determine when to change the address based on the actual usage of the address. If the address is being used by another application, the address will not change immediately.

\- To persistently save the addresses, call [access.addPersistentDeviceId](../ohos-bluetooth-access-bluetooth-access-module/document.md#accessaddpersistentdeviceid16).

 |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
function onReceiveEvent(data: Array<string>) { // data is an array of Bluetooth device addresses.
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    connection.on('bluetoothDeviceFind', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.off('bluetoothDeviceFind')

off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void

Unsubscribes from Bluetooth scan result reporting events.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **bluetoothDeviceFind** indicates a scan result reporting event. |
| callback | Callback<Array<string>> | No | 
Callback to unregister.

If this parameter is specified, it must be the same as the callback in [connection.on('bluetoothDeviceFind')](#connectiononbluetoothdevicefind). If this parameter is not specified, all callbacks corresponding to the event type are unsubscribed.

 |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
function onReceiveEvent(data: Array<string>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    connection.on('bluetoothDeviceFind', onReceiveEvent);
    connection.off('bluetoothDeviceFind', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.on('bondStateChange')

on(type: 'bondStateChange', callback: Callback<BondStateParam>): void

Subscribes to Bluetooth pairing status change events. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. The value **bondStateChange** indicates a Bluetooth pairing status change event.

This event is triggered when [connection.pairDevice](#connectionpairdevice) is called to initiate pairing or the local device receives a pairing request from another device.

 |
| callback | Callback<[BondStateParam](#bondstateparam)\> | Yes | Callback used to return the pairing status. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
function onReceiveEvent(data: connection.BondStateParam) { // data, as the input parameter of the callback, indicates the pairing state.
    console.info('pair state = '+ JSON.stringify(data));
}
try {
    connection.on('bondStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.off('bondStateChange')

off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void

Unsubscribes from Bluetooth pairing status change events.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **bondStateChange** indicates a Bluetooth pairing status change event. |
| callback | Callback<[BondStateParam](#bondstateparam)\> | No | 
Callback to unregister.

If this parameter is specified, it must be the same as the callback in [connection.on('bondStateChange')](#connectiononbondstatechange). If this parameter is not specified, all callbacks corresponding to the event type are unsubscribed.

 |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
function onReceiveEvent(data: connection.BondStateParam) {
    console.info('bond state = '+ JSON.stringify(data));
}
try {
    connection.on('bondStateChange', onReceiveEvent);
    connection.off('bondStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.on('pinRequired')

on(type: 'pinRequired', callback: Callback<PinRequiredParam>): void

Subscribes to pairing request events. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. The value **pinRequired** indicates a pairing request event.

This event is triggered when [connection.pairDevice](#connectionpairdevice) is called to initiate pairing or the local device receives a pairing request from another device.

 |
| callback | Callback<[PinRequiredParam](#pinrequiredparam)\> | Yes | Callback used to return the pairing request. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
function onReceiveEvent(data: connection.PinRequiredParam) { // data is the pairing request parameter.
    console.info('pin required = '+ JSON.stringify(data));
}
try {
    connection.on('pinRequired', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.off('pinRequired')

off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void

Unsubscribes from pairing request events.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **pinRequired** indicates a pairing request event. |
| callback | Callback<[PinRequiredParam](#pinrequiredparam)\> | No | 
Callback to unregister.

If this parameter is specified, it must be the same as the callback in [connection.on('pinRequired')](#connectiononpinrequired). If this parameter is not specified, all callbacks corresponding to the event type are unsubscribed.

 |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
function onReceiveEvent(data: connection.PinRequiredParam) {
    console.info('pin required = '+ JSON.stringify(data));
}
try {
    connection.on('pinRequired', onReceiveEvent);
    connection.off('pinRequired', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.on('discoveryResult')18+

on(type: 'discoveryResult', callback: Callback<Array<DiscoveryResult>>): void

Subscribes to scan result reporting events of Bluetooth devices. This API uses an asynchronous callback to return the result.

-   This API applies to both classic Bluetooth devices and BLE devices.
    
-   The reported information includes the device address, signal strength, name, and type.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **discoveryResult** indicates a scan result reporting event. A device scan starts when [connection.startBluetoothDiscovery](#connectionstartbluetoothdiscovery) is called. This event is triggered when a device is discovered. |
| callback | Callback<Array<[DiscoveryResult](#discoveryresult18)\>> | Yes | Callback used to return the set of scan results. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let onReceiveEvent: (data: Array<connection.DiscoveryResult>) => void = (data: Array<connection.DiscoveryResult>) => { // data is an array of Bluetooth devices discovered.
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    connection.on('discoveryResult', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.off('discoveryResult')18+

off(type: 'discoveryResult', callback?: Callback<Array<DiscoveryResult>>): void

Unsubscribes from the Bluetooth device discovered.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **discoveryResult** indicates a scan result reporting event. |
| callback | Callback<Array<[DiscoveryResult](#discoveryresult18)\>> | No | 
Callback to unregister.

If this parameter is specified, it must be the same as the callback in [connection.on('discoveryResult')](#connectionondiscoveryresult18). If this parameter is not specified, all callbacks corresponding to the event type are unsubscribed.

 |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let onReceiveEvent: (data: Array<connection.DiscoveryResult>) => void = (data: Array<connection.DiscoveryResult>) => { // data is an array of Bluetooth devices discovered.
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    connection.on('discoveryResult', onReceiveEvent);
    connection.off('discoveryResult', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.getLastConnectionTime15+

getLastConnectionTime(deviceId: string): Promise<number>

Obtains the latest connection time of the peer Bluetooth device. This API uses a promise to return the result.

-   Starting from API version 21, this API can be used to obtain the latest connection time of the peer Bluetooth device based on the actual MAC address of the peer device.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | MAC address of the peer device, for example, XX:XX:XX:XX:XX:XX. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the latest connection time of the peer Bluetooth device, in the UNIX timestamp format. |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
// promise
try {
    connection.getLastConnectionTime('11:22:33:44:55:66').then((time: number) => {
        console.info(\`connectionTime: ${time}\`);
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.connectAllowedProfiles16+

connectAllowedProfiles(deviceId: string, callback: AsyncCallback<void>): void

Obtains the profiles supported by the peer device. Supported profiles include A2DP, HFP, and HID. This API uses an asynchronous callback to return the result.

-   Call [connection.pairDevice](#connectionpairdevice) to initiate pairing first. This API can be called only once within 30 seconds after each pairing is initiated.
-   Upon successful pairing, you are advised to call [getRemoteProfileUuids](#connectiongetremoteprofileuuids12) to query the profiles supported by the target device. This API is called only if the target device supports the profile required by the application.
-   Starting from API version 21, this API can be used to perform profile connection using the actual MAC address of the peer device.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the peer device, for example, XX:XX:XX:XX:XX:XX. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
try {
  connection.connectAllowedProfiles('68:13:24:79:4C:8C', (err: BusinessError) => {
    if (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
      return;
    }
    console.info('connectAllowedProfiles');
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connection.connectAllowedProfiles16+

connectAllowedProfiles(deviceId: string): Promise<void>

Obtains the profiles supported by the peer device. Supported profiles include A2DP, HFP, and HID. This API uses a promise to return the result.

-   Call [connection.pairDevice](#connectionpairdevice) to initiate pairing first. This API can be called only once within 30 seconds after each pairing is initiated.
-   Upon successful pairing, you are advised to call [getRemoteProfileUuids](#connectiongetremoteprofileuuids12) to query the profiles supported by the target device. This API is called only if the target device supports the profile required by the application.
-   Starting from API version 21, this API can be used to perform profile connection using the actual MAC address of the peer device.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the peer device, for example, XX:XX:XX:XX:XX:XX. |

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
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
try {
  connection.connectAllowedProfiles('68:13:24:79:4C:8C').then(() => {
      console.info('connectAllowedProfiles');
    }, (err: BusinessError) => {
      console.error('connectAllowedProfiles:errCode' + err.code + ', errMessage: ' + err.message);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### BondStateParam

Defines the parameters for the pairing status.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | Address of the peer device. |
| state | [BondState](#bondstate) | No | No | Pairing status. |
| cause12+ | [UnbondCause](#unbondcause12) | No | No | Reason why the pairing fails. |

#### PinRequiredParam

Defines the parameters of a pairing request.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | Address of the peer device. |
| pinCode | string | No | No | PIN used for pairing. |

#### DeviceClass

Represents the class of a Bluetooth device.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| majorClass | [MajorClass](../ohos-bluetooth-constant-bluetooth-constant-module/document.md#majorclass) | No | No | Main class. This is a standard field in the Bluetooth protocol. |
| majorMinorClass | [MajorMinorClass](../ohos-bluetooth-constant-bluetooth-constant-module/document.md#majorminorclass) | No | No | Subclass, which is further classified based on the major class. This is a standard field in the Bluetooth protocol. |
| classOfDevice | number | No | No | Class of the Bluetooth device. This is a standard field in the Bluetooth protocol. It includes the [MajorClass](../ohos-bluetooth-constant-bluetooth-constant-module/document.md#majorclass), [MajorMinorClass](../ohos-bluetooth-constant-bluetooth-constant-module/document.md#majorminorclass), and supported major services. |

#### BatteryInfo12+

Describes the battery level of a device.

Only devices that support the **Attention** (AT) command (including +XEVENT and IPHONEACCEV) defined by the Bluetooth protocol can report valid battery level information.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| batteryLevel | number | No | No | 
Battery level.

If the value is **\-1**, no battery level information is available.

 |
| leftEarBatteryLevel | number | No | No | 

Battery level of the left earbud if the device is a Bluetooth earphone.

If the value is **\-1**, no battery level information is available.

 |
| leftEarChargeState | [DeviceChargeState](#devicechargestate12) | No | No | Charging status of the left earbud if the device is a Bluetooth earbud. |
| rightEarBatteryLevel | number | No | No | 

Battery level of the right earbud if the device is a Bluetooth earphone.

If the value is **\-1**, no battery level information is available.

 |
| rightEarChargeState | [DeviceChargeState](#devicechargestate12) | No | No | Charging status of the right earbud if the device is a Bluetooth earbud. |
| boxBatteryLevel | number | No | No | 

Battery level of the earbud compartment if the device is a Bluetooth earphone.

If the value is **\-1**, no battery level information is available.

 |
| boxChargeState | [DeviceChargeState](#devicechargestate12) | No | No | Charging status of the earbud compartment if the device is a Bluetooth earbud. |

#### BluetoothTransport

Enumerates the device transmission modes.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| TRANSPORT\_BR\_EDR | 0 | Legacy Bluetooth basic rate/enhanced data rate (BR/EDR) mode. |
| TRANSPORT\_LE | 1 | BLE mode. |
| TRANSPORT\_DUAL20+ | 2 | BR/EDR and BLE modes. You can select either the BR/EDR or BLE mode for communication. |
| TRANSPORT\_UNKNOWN20+ | 3 | Unknown transport mode. |

#### ScanMode

Enumerates the scan modes. The scan mode determines whether the device is discoverable or connectable.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SCAN\_MODE\_NONE | 0 | Undiscoverable and unconnectable mode. |
| SCAN\_MODE\_CONNECTABLE | 1 | Connectable mode. |
| SCAN\_MODE\_GENERAL\_DISCOVERABLE | 2 | General discoverable mode, allowing for long-term discovery. |
| SCAN\_MODE\_LIMITED\_DISCOVERABLE | 3 | Limited discoverable mode, allowing for discovery within a specific timeframe. |
| SCAN\_MODE\_CONNECTABLE\_GENERAL\_DISCOVERABLE | 4 | Connectable and general discoverable mode. |
| SCAN\_MODE\_CONNECTABLE\_LIMITED\_DISCOVERABLE | 5 | Connectable and limited discoverable mode. |

#### BondState

Enumerates the device pairing states.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| BOND\_STATE\_INVALID | 0 | Unpaired state. |
| BOND\_STATE\_BONDING | 1 | Pairing state. |
| BOND\_STATE\_BONDED | 2 | Paired state. |

#### UnbondCause12+

Enumerates the possible causes of a pairing failure.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| USER\_REMOVED | 0 | The user proactively removes the device. If [BondState](#bondstate) is **BOND\_STATE\_BONDED**, the pairing is successful. |
| REMOTE\_DEVICE\_DOWN | 1 | The peer device is offline. For example, the Bluetooth of the peer device is disabled. |
| AUTH\_FAILURE | 2 | Authentication failed. For example, the keys of the devices at both ends do not match. |
| AUTH\_REJECTED | 3 | Authentication rejected. For example, the peer device rejects the pairing request. |
| INTERNAL\_ERROR | 4 | Internal error. For example, the device does not support pairing, or the pairing times out. |

#### DeviceChargeState12+

Enumerates the device charging states.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| DEVICE\_NORMAL\_CHARGE\_NOT\_CHARGED | 0 | A device that does not support super-fast charging is currently not charging. |
| DEVICE\_NORMAL\_CHARGE\_IN\_CHARGING | 1 | A device that does not support super-fast charging is currently charging. |
| DEVICE\_SUPER\_CHARGE\_NOT\_CHARGED | 2 | A device that supports super-fast charging is currently not charging. |
| DEVICE\_SUPER\_CHARGE\_IN\_CHARGING | 3 | A device that supports super-fast charging is currently charging. |

#### DiscoveryResult18+

Defines the device discovery result.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | 
Address of the discovered device.

For security purposes, the device addresses obtained are virtual MAC addresses.

\- The virtual addresses of paired Bluetooth devices will not change.

\- If Bluetooth is disabled and then enabled again, the virtual address will change immediately.

\- If the pairing is canceled, the Bluetooth subsystem will determine when to change the address based on the actual usage of the address. If the address is being used by another application, the address will not change immediately.

\- To persistently save the addresses, call [access.addPersistentDeviceId](../ohos-bluetooth-access-bluetooth-access-module/document.md#accessaddpersistentdeviceid16).

 |
| rssi | number | No | No | Signal strength, in dBm. |
| deviceName | string | No | No | Device name. |
| deviceClass | [DeviceClass](#deviceclass) | No | No | Device class. |
