# @ohos.bluetooth.baseProfile (Bluetooth baseProfile Module)

The **baseProfile** module provides the basic common methods for different Bluetooth technology protocols.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/tYGURk3mSKm7LeGnj2TrEQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=633048D351909FDEB724C706329F66685983FD87F9BE32C2F26AD6C383A8472A)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { baseProfile } from '@kit.ConnectivityKit';

#### BaseProfile

**BaseProfile** class, which provides public capabilities such as obtaining the connection status and listening for connection status changes. For example, [profiles](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#profile) such as [A2dpSourceProfile](../ohos-bluetooth-a2dp-bluetooth-a2dp-module/document.md#a2dpsourceprofile) and [HandsFreeAudioGatewayProfile](../ohos-bluetooth-hfp-bluetooth-hfp-module/document.md#handsfreeaudiogatewayprofile) are inherited from this class.

#### ProfileConnectionState

type ProfileConnectionState = constant.ProfileConnectionState

Represents the profile connection status between the local and peer Bluetooth devices.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Type | Description |
| :-- | :-- |
| [constant.ProfileConnectionState](../ohos-bluetooth-constant-bluetooth-constant-module/document.md#profileconnectionstate) | Profile connection status between the local and peer Bluetooth devices. |

#### StateChangeParam

Defines the parameters for the profile connection status change between the local and peer Bluetooth devices.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | Address of the peer device, for example, XX:XX:XX:XX:XX:XX. |
| state | [ProfileConnectionState](../ohos-bluetooth-constant-bluetooth-constant-module/document.md#profileconnectionstate) | No | No | Profile connection status. |
| cause12+ | [DisconnectCause](#disconnectcause12) | No | No | Reason of profile disconnection. |

#### DisconnectCause12+

Enumerates the reasons of profile disconnection.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| USER\_DISCONNECT | 0 | The user proactively disconnects the connection. |
| CONNECT\_FROM\_KEYBOARD | 1 | The connection request needs to be initiated from the keyboard. |
| CONNECT\_FROM\_MOUSE | 2 | The connection request needs to be initiated from the mouse. |
| CONNECT\_FROM\_CAR | 3 | The connection request needs to be initiated from the head unit. |
| TOO\_MANY\_CONNECTED\_DEVICES | 4 | The number of connections exceeds the limit. |
| CONNECT\_FAIL\_INTERNAL | 5 | Internal error. |

#### BaseProfile.getConnectedDevices

getConnectedDevices(): Array<string>

Obtains the list of peer devices that have connected to the profile of the local device.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | 
List of peer devices that have connected to the profile of the local device.

For security purposes, the device addresses obtained are virtual MAC addresses.

\- The virtual address of a paired Bluetooth device will not change.

\- If Bluetooth is disabled and then enabled again, the virtual address will change immediately.

\- If the pairing is canceled, the Bluetooth subsystem will determine when to change the address based on the actual usage of the address. If the address is being used by another application, the address will not change immediately.

\- To persistently save the address, call [access.addPersistentDeviceId](../ohos-bluetooth-access-bluetooth-access-module/document.md#accessaddpersistentdeviceid16).

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { a2dp } from '@kit.ConnectivityKit';

try {
    let a2dpSrc = a2dp.createA2dpSrcProfile(); // A2DP is used as an example.
    let retArray = a2dpSrc.getConnectedDevices();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}

#### BaseProfile.getConnectionState

getConnectionState(deviceId: string): ProfileConnectionState

Obtains the profile connection status between the local and peer devices.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the peer device, for example, XX:XX:XX:XX:XX:XX. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ProfileConnectionState](../ohos-bluetooth-constant-bluetooth-constant-module/document.md#profileconnectionstate) | Profile connection status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

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

import { BusinessError } from '@kit.BasicServicesKit';
import { a2dp } from '@kit.ConnectivityKit';

try {
    let a2dpSrc = a2dp.createA2dpSrcProfile(); // A2DP is used as an example.
    let ret = a2dpSrc.getConnectionState('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### BaseProfile.on('connectionStateChange')

on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void

Enables listening for profile connection status change events. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. The value **connectionStateChange** indicates a profile connection status change event.

This event is triggered when the profile connection status changes.

 |
| callback | Callback<[StateChangeParam](#statechangeparam)\> | Yes | Callback used to return the profile connection status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { a2dp } from '@kit.ConnectivityKit';

function onReceiveEvent(data: baseProfile.StateChangeParam) {
    console.info('a2dp state = '+ JSON.stringify(data));
}
try {
    let a2dpSrc = a2dp.createA2dpSrcProfile(); // A2DP is used as an example.
    a2dpSrc.on('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### BaseProfile.off('connectionStateChange')

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](#statechangeparam)\>): void

Disables listening for profile connection status change events.

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **connectionStateChange** indicates a profile connection status change event. |
| callback | Callback<[StateChangeParam](#statechangeparam)\> | No | 
Callback to unregister.

If this parameter is specified, it must be the same as the callback in [BaseProfile.on('connectionStateChange')](#baseprofileonconnectionstatechange). If this parameter is not specified, all callbacks corresponding to the event type are unregistered.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { a2dp } from '@kit.ConnectivityKit';

function onReceiveEvent(data: baseProfile.StateChangeParam) {
    console.info('a2dp state = '+ JSON.stringify(data));
}
try {
    let a2dpSrc = a2dp.createA2dpSrcProfile(); // A2DP is used as an example.
    a2dpSrc.on('connectionStateChange', onReceiveEvent);
    a2dpSrc.off('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
