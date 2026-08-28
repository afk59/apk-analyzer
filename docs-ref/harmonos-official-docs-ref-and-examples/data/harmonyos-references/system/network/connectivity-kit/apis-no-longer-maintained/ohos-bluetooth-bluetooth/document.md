# @ohos.bluetooth (Bluetooth)

The **Bluetooth** module provides classic Bluetooth capabilities and Bluetooth Low Energy (BLE) scan and advertising.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/P_x9Xi26QSmn25K_TaIfDA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B38609F5CA7322EDF9EFEC96D339205A37378FF4FBA85C44E7F6575B6FCF0C41)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs provided by this module are no longer maintained since API version 9. You are advised to use APIs of [@ohos.bluetooth.ble](../../arkts-apis/ohos-bluetooth-ble-bluetooth-ble-module/document.md).

#### Modules to Import

import bluetooth from '@ohos.bluetooth';

#### bluetooth.enableBluetooth(deprecated)

enableBluetooth(): boolean

Enables Bluetooth.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/prKZtckbSr-HiO6o-OmreA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=232ED38708A0266E15138F118306346F48189865ED3DDD2B50027E45C0C44DC0)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.enableBluetooth](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagerenablebluetoothdeprecated) instead.

**Required permissions**: ohos.permission.DISCOVER\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if Bluetooth is enabled; returns **false** otherwise. |

**Example**

let enable : boolean = bluetooth.enableBluetooth();

#### bluetooth.disableBluetooth(deprecated)

disableBluetooth(): boolean

Disables Bluetooth.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/HQ_kus8nSIqm_Q19RDzfmg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E5A439811BA36C9B4D99381CAB8C2F19BD2097F012FC6274C77E3F738514E8D)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.disableBluetooth](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagerdisablebluetoothdeprecated) instead.

**Required permissions**: ohos.permission.DISCOVER\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if Bluetooth is disabled; returns **false** otherwise. |

**Example**

let disable : boolean = bluetooth.disableBluetooth();

#### bluetooth.getLocalName(deprecated)

getLocalName(): string

Obtains the name of the local Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/vBobzHjiTb6G0zv6vf3tOA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=62233029AA061B8A26D0DE5384F931A0EF18CCB9737626840F1F99CE6DAC65C3)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.getLocalName](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagergetlocalnamedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Name of the local Bluetooth device obtained. |

**Example**

let localName : string = bluetooth.getLocalName();

#### bluetooth.getState(deprecated)

getState(): BluetoothState

Obtains the Bluetooth state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/3c2UkBEhTtWR9S4ZL8WApw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27BCA5666556CFD85B6B8778C26078C5045A7EC5D8CF47160D057D8F6FD1C8BA)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.getState](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagergetstatedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [BluetoothState](#bluetoothstatedeprecated) | Bluetooth state obtained. |

**Example**

let state : bluetooth.BluetoothState = bluetooth.getState();

#### bluetooth.getBtConnectionState(deprecated)

getBtConnectionState(): ProfileConnectionState

Obtains the local profile connection state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/PeF0UwScTVaLw75P7mXmNw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1ED98CB206F45D4C909B7FA12579C43E989DE68C61DCC51EAC247D6AD7FAFD4A)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.getBtConnectionState](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagergetbtconnectionstatedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [ProfileConnectionState](#profileconnectionstatedeprecated) | Profile connection state obtained. |

**Example**

let connectionState : bluetooth.ProfileConnectionState = bluetooth.getBtConnectionState();

#### bluetooth.setLocalName(deprecated)

setLocalName(name: string): boolean

Sets the name of the local Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/RYnhrNXhQX281Y87uR3oTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C25478A00D042B5767810DDDF9F3297151F2567BB6FBC870A46782433EBB153)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.setLocalName](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagersetlocalnamedeprecated) instead.

**Required permissions**: ohos.permission.DISCOVER\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Bluetooth device name to set. It cannot exceed 248 bytes. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let ret : boolean = bluetooth.setLocalName('device\_name');

#### bluetooth.pairDevice(deprecated)

pairDevice(deviceId: string): boolean

Initiates Bluetooth pairing.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/vEt6MJjcQi-a8pJtti8Dog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99AB5C6A2678633AC57D822E2B881E2B71C251436AF52F49F75C698777DD9870)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.pairDevice](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagerpairdevicedeprecated) instead.

**Required permissions**: ohos.permission.DISCOVER\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the remote device to pair, for example, XX:XX:XX:XX:XX:XX. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

// The address can be scanned.
let result : boolean = bluetooth.pairDevice("XX:XX:XX:XX:XX:XX");

#### bluetooth.getProfileConnState(deprecated)

getProfileConnState(profileId: ProfileId): ProfileConnectionState

Obtains the connection status of the specified profile.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/tQP7nONEQiey4uqtSblN6w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C61DB677C4C4BC5B1C497A10F7F978BB8C50BCFF38011A15A78E254A4EE2F0BB)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.getProfileConnectionState](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagergetprofileconnectionstatedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| profileId | ProfileId | Yes | ID of the profile to obtain, for example, **PROFILE\_A2DP\_SOURCE**. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ProfileConnectionState](#profileconnectionstatedeprecated) | Profile connection state obtained. |

**Example**

let result : bluetooth.ProfileConnectionState = bluetooth.getProfileConnState(bluetooth.ProfileId.PROFILE\_A2DP\_SOURCE);

#### bluetooth.getRemoteDeviceName(deprecated)

getRemoteDeviceName(deviceId: string): string

Obtains the name of the remote Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/huFSHaPBQiaOlOEnCOuyhg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=263EFC18ADDE5452174FCE2BF73E6CB5420245EDC1CBD6C419FFA20CCCD021CC)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.getRemoteDeviceName](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagergetremotedevicenamedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the remote device, for example, XX:XX:XX:XX:XX:XX. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Device name (a string) obtained. |

**Example**

let remoteDeviceName : string = bluetooth.getRemoteDeviceName("XX:XX:XX:XX:XX:XX");

#### bluetooth.getRemoteDeviceClass(deprecated)

getRemoteDeviceClass(deviceId: string): DeviceClass

Obtains the class of the remote Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/dJO1mM3zQ0-dxV4UpubCBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69DEF8B0F731D03C81FA2BAB3C38043A805DB8328C3171F82A616DC4D86CACAF)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.getRemoteDeviceClass](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagergetremotedeviceclassdeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the remote device, for example, XX:XX:XX:XX:XX:XX. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DeviceClass](#deviceclassdeprecated) | Class of the remote device obtained. |

**Example**

let remoteDeviceClass : bluetooth.DeviceClass = bluetooth.getRemoteDeviceClass("XX:XX:XX:XX:XX:XX");

#### bluetooth.getPairedDevices(deprecated)

getPairedDevices(): Array<string>

Obtains the paired devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/kKg6RUF6Q3eqcBKQdf_1jg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF2538EABD042985FC8610FAAA043E8B77E42F87E82189E36BE0751FD741AD9C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.getPairedDevices](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagergetpaireddevicesdeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | Addresses of the paired Bluetooth devices. |

**Example**

let devices : Array<string> = bluetooth.getPairedDevices();

#### bluetooth.setBluetoothScanMode(deprecated)

setBluetoothScanMode(mode: ScanMode, duration: number): boolean

Sets the Bluetooth scan mode so that the device can be discovered by a remote device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/FSxvdrSHQNuIBrJGK8MGyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D4AE5F50050EF374F2625E4FA79090DE06AB0E13987CBB283607DA0490FF948)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.setBluetoothScanMode](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagersetbluetoothscanmodedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [ScanMode](#scanmodedeprecated) | Yes | Bluetooth scan mode to set. |
| duration | number | Yes | Duration (in ms) in which the device can be discovered. The value **0** indicates unlimited time. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

// The device can be discovered and connected only when the discoverable and connectable mode is used.
let result : boolean = bluetooth.setBluetoothScanMode(bluetooth.ScanMode
    .SCAN\_MODE\_CONNECTABLE\_GENERAL\_DISCOVERABLE, 100);

#### bluetooth.getBluetoothScanMode(deprecated)

getBluetoothScanMode(): ScanMode

Obtains the Bluetooth scan mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/oaXRnInwRqma3uQCJoP9HQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3ABB02985B54588476ED290D0D104F533D14469B9864EB195BDB90A3DB57C47A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.getBluetoothScanMode](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagergetbluetoothscanmodedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [ScanMode](#scanmodedeprecated) | Bluetooth scan mode to set. |

**Example**

let scanMode : bluetooth.ScanMode = bluetooth.getBluetoothScanMode();

#### bluetooth.startBluetoothDiscovery(deprecated)

startBluetoothDiscovery(): boolean

Starts Bluetooth scan to discover remote devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/-Ia9MCDCQPacXyU_-jeMIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=593B5398AEE0575C653502F1CA68499402510D8A592184F94A4DA3A4049CF75D)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.startBluetoothDiscovery](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagerstartbluetoothdiscoverydeprecated) instead.

**Required permissions**: ohos.permission.DISCOVER\_BLUETOOTH and ohos.permission.LOCATION

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let deviceId : Array<string>;
function onReceiveEvent(data : Array<string>) {
    deviceId = data;
}
bluetooth.on('bluetoothDeviceFind', onReceiveEvent);
let result : boolean = bluetooth.startBluetoothDiscovery();

#### bluetooth.stopBluetoothDiscovery(deprecated)

stopBluetoothDiscovery(): boolean

Stops Bluetooth scan.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/L8sYR6nYQCGxy-WpfCq3UA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78209C4A13B7F48B47621269554616714FE660B80B9AD3E5AAC8E4A9963C65CE)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.stopBluetoothDiscovery](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagerstopbluetoothdiscoverydeprecated) instead.

**Required permissions**: ohos.permission.DISCOVER\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let result : boolean = bluetooth.stopBluetoothDiscovery();

#### bluetooth.setDevicePairingConfirmation(deprecated)

setDevicePairingConfirmation(device: string, accept: boolean): boolean

Sets the device pairing confirmation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/n5sLV1OXSXWlGk7l4Atimw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71CD2647B93601759A70214ADB78978106CD635A5ACFF84D183E354E5D4D7E86)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.setDevicePairingConfirmation](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagersetdevicepairingconfirmationdeprecated) instead.

**Required permissions**: ohos.permission.MANAGE\_BLUETOOTH (available only for system applications)

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | Address of the remote device, for example, XX:XX:XX:XX:XX:XX. |
| accept | boolean | Yes | Whether to accept the pairing request. The value **true** means to accept the pairing request, and the value **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

// Subscribe to the pinRequired event and configure the pairing confirmation after receiving a pairing request from the remote device.
function onReceivePinRequiredEvent(data : bluetooth.PinRequiredParam) { // data is the input parameter for the pairing request.
    console.info('pin required  = '+ JSON.stringify(data));
    bluetooth.setDevicePairingConfirmation(data.deviceId, true);
}
bluetooth.on("pinRequired", onReceivePinRequiredEvent);

#### bluetooth.on('bluetoothDeviceFind')(deprecated)

on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void

Subscribes to the Bluetooth device discovery events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/jwRfREC3TGiWlwAO8rmhDg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F372E7B6F2F377D833897A2B9194D95977E2EDDF5C3210432814EE988F7A5DA3)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.on('bluetoothDeviceFind')](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanageronbluetoothdevicefinddeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **bluetoothDeviceFind**, which indicates an event of discovering a Bluetooth device. |
| callback | Callback<Array<string>> | Yes | Callback used to return the discovered devices. You need to implement this callback. |

**Return value**

No value is returned.

**Example**

function onReceiveEvent(data : Array<string>) { // data is an array of Bluetooth device addresses.
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
bluetooth.on('bluetoothDeviceFind', onReceiveEvent);

#### bluetooth.off('bluetoothDeviceFind')(deprecated)

off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void

Unsubscribes from the Bluetooth device discovery events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/UfJzbbPkSki-QTBwXvLcvA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73AB81D64C0C77CD4C200E3AACCA806C1148CD06A648FE5A7595BCDE8FFE2D41)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.off('bluetoothDeviceFind')](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanageroffbluetoothdevicefinddeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **bluetoothDeviceFind**, which indicates an event of discovering a Bluetooth device. |
| callback | Callback<Array<string>> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for **type**. |

**Return value**

No value is returned.

**Example**

function onReceiveEvent(data : Array<string>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
bluetooth.on('bluetoothDeviceFind', onReceiveEvent);
bluetooth.off('bluetoothDeviceFind', onReceiveEvent);

#### bluetooth.on('pinRequired')(deprecated)

on(type: 'pinRequired', callback: Callback<PinRequiredParam>): void

Subscribes to the pairing request events of the remote Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/ceShz-AaSBSH3oqCiAk-eg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB5A471C345D6C1FFD887F43F202540D20A699D125F98A376D294AD0DED600A6)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.on('pinRequired')](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanageronpinrequireddeprecated) instead.

**Required permissions**: ohos.permission.DISCOVER\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **pinRequired**, which indicates a pairing request event. |
| callback | Callback<[PinRequiredParam](#pinrequiredparamdeprecated)\> | Yes | Callback used to return the pairing request. You need to implement this callback. |

**Return value**

No value is returned.

**Example**

function onReceiveEvent(data : bluetooth.PinRequiredParam) { // data is the pairing request parameter.
    console.info('pin required = '+ JSON.stringify(data));
}
bluetooth.on('pinRequired', onReceiveEvent);

#### bluetooth.off('pinRequired')(deprecated)

off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void

Unsubscribes from the pairing request events of the remote Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/CRy1OCxXRMOT9Vpa8t7X9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ECDB801192CE12E0DE39AF9F8D1518C1DE111BC2BE0133D14A3D82CC42CBBDEF)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.off('pinRequired')](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanageroffpinrequireddeprecated) instead.

**Required permissions**: ohos.permission.DISCOVER\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **pinRequired**, which indicates a pairing request event. |
| callback | Callback<[PinRequiredParam](#pinrequiredparamdeprecated)\> | No | Callback to unregister. The input parameter is the pairing request parameter. If this parameter is not set, this API unregisters all callbacks for **type**. |

**Return value**

No value is returned.

**Example**

function onReceiveEvent(data : bluetooth.PinRequiredParam) {
    console.info('pin required = '+ JSON.stringify(data));
}
bluetooth.on('pinRequired', onReceiveEvent);
bluetooth.off('pinRequired', onReceiveEvent);

#### bluetooth.on('bondStateChange')(deprecated)

on(type: 'bondStateChange', callback: Callback<BondStateParam>): void

Subscribes to the Bluetooth pairing state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/1xYmMg_tQm-1eT27IclkkA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F630DE517CD3CE91941E3EF22F8501611403580E348A182F854D3564146C890)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.on('bondStateChange')](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanageronbondstatechangedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **bondStateChange**, which indicates a Bluetooth pairing state change event. |
| callback | Callback<[BondStateParam](#bondstateparamdeprecated)\> | Yes | Callback used to return the pairing state. You need to implement this callback. |

**Return value**

No value is returned.

**Example**

function onReceiveEvent(data : bluetooth.BondStateParam) { // data, as the input parameter of the callback, indicates the pairing state.
    console.info('pair state = '+ JSON.stringify(data));
}
bluetooth.on('bondStateChange', onReceiveEvent);

#### bluetooth.off('bondStateChange')(deprecated)

off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void

Unsubscribes from the Bluetooth pairing state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/p2TpJ1w5Rpy7tXc6G6XXLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99EB9EFF404B12549BDDF9A36AABE0A6CC33C15DA628AD1311F4BFD49A843567)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.off('bondStateChange')](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanageroffbondstatechangedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **bondStateChange**, which indicates a Bluetooth pairing state change event. |
| callback | Callback<[BondStateParam](#bondstateparamdeprecated)\> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for **type**. |

**Return value**

No value is returned.

**Example**

function onReceiveEvent(data : bluetooth.BondStateParam) {
    console.info('bond state = '+ JSON.stringify(data));
}
bluetooth.on('bondStateChange', onReceiveEvent);
bluetooth.off('bondStateChange', onReceiveEvent);

#### bluetooth.on('stateChange')(deprecated)

on(type: 'stateChange', callback: Callback<BluetoothState>): void

Subscribes to the Bluetooth connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/ITbB9XfpSwSFSRNqKatgdQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF438A62E242A31BDC6968404DF7F54AA5CFFB622852661EAFB9D87E66C82223)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.on('stateChange')](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanageronstatechangedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **stateChange**, which indicates a Bluetooth connection state change event. |
| callback | Callback<[BluetoothState](#bluetoothstatedeprecated)\> | Yes | Callback used to return the Bluetooth connection state. You need to implement this callback. |

**Return value**

No value is returned.

**Example**

function onReceiveEvent(data : bluetooth.BluetoothState) {
    console.info('bluetooth state = '+ JSON.stringify(data));
}
bluetooth.on('stateChange', onReceiveEvent);

#### bluetooth.off('stateChange')(deprecated)

off(type: 'stateChange', callback?: Callback<BluetoothState>): void

Unsubscribes from the Bluetooth connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/aDzb3VLtT4-pDWE0jSP2jQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4C1E684329E952D03E1F8DC3D9A9CA69E9161E2B66EC9871E02D819FEE656B08)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.off('stateChange')](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanageroffstatechangedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **stateChange**, which indicates a Bluetooth connection state change event. |
| callback | Callback<[BluetoothState](#bluetoothstatedeprecated)\> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for **type**. |

**Return value**

No value is returned.

**Example**

function onReceiveEvent(data : bluetooth.BluetoothState) {
    console.info('bluetooth state = '+ JSON.stringify(data));
}
bluetooth.on('stateChange', onReceiveEvent);
bluetooth.off('stateChange', onReceiveEvent);

#### bluetooth.sppListen(deprecated)

sppListen(name: string, option: SppOption, callback: AsyncCallback<number>): void

Creates a server listening socket.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/qefnJHosRoGKvSd27tloCg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=403FAA9DA70BC91E1F17743F026A4B956DCF1F2D5C205E4C75F5F34E9E1FC6E2)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.sppListen](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagerspplistendeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the service. |
| option | [SppOption](#sppoptiondeprecated) | Yes | Serial port profile (SPP) listening configuration. |
| callback | AsyncCallback<number> | Yes | Callback used to return the server socket ID. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let serverNumber = -1;
function serverSocket(code : BusinessError, number : number) {
  console.info(\`bluetooth error code: ${code.code}\`);
  if (code.code == 0) {
    console.info(\`bluetooth serverSocket Number: ${number}\`);
    serverNumber = number;
  }
}

let sppOption : bluetooth.SppOption = {uuid: '00001810-0000-1000-8000-00805F9B34FB', secure: false, type: 0};
bluetooth.sppListen('server1', sppOption, serverSocket);

#### bluetooth.sppAccept(deprecated)

sppAccept(serverSocket: number, callback: AsyncCallback<number>): void

Listens for a connection to be made to this socket from the client and accepts it.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/3-rzFAzlQRWpmjKctGb5YA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8BDD919DA49CE7C20D27C5F2B9981003CD6B548CCD4A48DD252C44501C6A502E)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.sppAccept](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagersppacceptdeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| serverSocket | number | Yes | Server socket ID. |
| callback | AsyncCallback<number> | Yes | Callback used to return the client socket ID. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let serverNumber = -1;
function serverSocket(code : BusinessError, number : number) {
  console.info(\`bluetooth error code: ${code.code}\`);
  if (code.code == 0) {
    console.info(\`bluetooth serverSocket Number: ${number}\`);
    serverNumber = number;
  }
}
let clientNumber = -1;
function acceptClientSocket(code : BusinessError, number : number) {
  console.info(\`bluetooth error code: ${code.code}\`);
  if (code.code == 0) {
    console.info(\`bluetooth clientSocket Number: ${number}\`);
    // The obtained clientNumber is used as the socket ID for subsequent read/write operations on the server.
    clientNumber = number;
  }
}
bluetooth.sppAccept(serverNumber, acceptClientSocket);

#### bluetooth.sppConnect(deprecated)

sppConnect(device: string, option: SppOption, callback: AsyncCallback<number>): void

Initiates an SPP connection to a remote device from the client.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/GhfbQwRcQKmiOHZL4VyAvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0BF16E5D8716EF713C9953057C8876BB95B119FA9FF17CDE23AED229C3EE9208)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.sppConnect](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagersppconnectdeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | Address of the remote device, for example, XX:XX:XX:XX:XX:XX. |
| option | [SppOption](#sppoptiondeprecated) | Yes | Configuration for connecting to the SPP client. |
| callback | AsyncCallback<number> | Yes | Callback used to return the client socket ID. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code : BusinessError, number : number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(\`bluetooth serverSocket Number: ${number}\`);
  // The obtained clientNumber is used as the socket ID for subsequent read/write operations on the client.
  clientNumber = number;
}
let sppOption : bluetooth.SppOption = {uuid: '00001810-0000-1000-8000-00805F9B34FB', secure: false, type: 0};
bluetooth.sppConnect('XX:XX:XX:XX:XX:XX', sppOption, clientSocket);

#### bluetooth.sppCloseServerSocket(deprecated)

sppCloseServerSocket(socket: number): void

Closes the listening socket of the server.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/4gH6fttHSX2I8rWvH_1vMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E2F88D0F164F3A083A33F967CEF12A0EDD87DA826318AA09D4CD0B67E19C5CB)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.sppCloseServerSocket](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagersppcloseserversocketdeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| socket | number | Yes | ID of the listening socket on the server. The ID is obtained by **sppListen**. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let serverNumber = -1;
function serverSocket(code : BusinessError, number : number) {
  console.info(\`bluetooth error code: ${code.code}\`);
  if (code.code == 0) {
    console.info(\`bluetooth serverSocket Number: ${number}\`);
    serverNumber = number;
  }
}
bluetooth.sppCloseServerSocket(serverNumber);

#### bluetooth.sppCloseClientSocket(deprecated)

sppCloseClientSocket(socket: number): void

Closes the client socket.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/xt2XCfT3SFOX3KnEBgSRtA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71F08E44744B2B9DF2F2F8C24F4353C1817EB8868FDE65CB54A416A1CF96E8B5)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.sppCloseClientSocket](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagersppcloseclientsocketdeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| socket | number | Yes | Client socket ID, which is obtained by **sppAccept** or **sppConnect**. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code : BusinessError, number : number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(\`bluetooth serverSocket Number: ${number}\`);
  // The obtained clientNumber is used as the socket ID for subsequent read/write operations on the client.
  clientNumber = number;
}
bluetooth.sppCloseClientSocket(clientNumber);

#### bluetooth.sppWrite(deprecated)

sppWrite(clientSocket: number, data: ArrayBuffer): boolean

Writes data to the remote device through the socket.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/kkrM_1OmTE2xqq8urH17nw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A6A49ACE5BBEB23A05CC2593B14DBC907DCB942D260CFB8C3DD4F97EBE3C9B29)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.sppWrite](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagersppwritedeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| clientSocket | number | Yes | Client socket ID, which is obtained by **sppAccept** or **sppConnect**. |
| data | ArrayBuffer | Yes | Data to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code : BusinessError, number : number) {
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
let ret : boolean = bluetooth.sppWrite(clientNumber, arrayBuffer);
if (ret) {
  console.info('spp write successfully');
} else {
  console.error('spp write failed');
}

#### bluetooth.on('sppRead')(deprecated)

on(type: 'sppRead', clientSocket: number, callback: Callback<ArrayBuffer>): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/hC6cCOS-SSmRY138oBVbQw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=469FD13E7FE0A3CC09FA8EF7B80874E0A0EC2B15C9B472CADCF3AF9CC4D2B6CF)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.on('sppRead')](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanageronsppreaddeprecated) instead.

Subscribes to the SPP read request events.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **sppRead**, which indicates an SPP read request event. |
| clientSocket | number | Yes | Client socket ID, which is obtained by **sppAccept** or **sppConnect**. |
| callback | Callback<ArrayBuffer> | Yes | Callback used to return the data read. |

**Return value**

No value is returned.

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code : BusinessError, number : number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(\`bluetooth serverSocket Number: ${number}\`);
  // The obtained clientNumber is used as the socket ID for subsequent read/write operations on the client.
  clientNumber = number;
}
function dataRead(dataBuffer : ArrayBuffer) {
  let data = new Uint8Array(dataBuffer);
}
bluetooth.on('sppRead', clientNumber, dataRead);

#### bluetooth.off('sppRead')(deprecated)

off(type: 'sppRead', clientSocket: number, callback?: Callback<ArrayBuffer>): void

Unsubscribes from the SPP read request events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/eddViOEvTM2LsW8MGc7RxA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68DA644240002C5C2CB8284E9393A90F0EC85F0078FF3FE08C4628CE4EE8DA6B)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.off('sppRead')](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanageroffsppreaddeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **sppRead**, which indicates an SPP read request event. |
| clientSocket | number | Yes | Client socket ID, which is obtained by **sppAccept** or **sppConnect**. |
| callback | Callback<ArrayBuffer> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for **type**. |

**Return value**

No value is returned.

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code : BusinessError, number : number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(\`bluetooth serverSocket Number: ${number}\`);
  // The obtained clientNumber is used as the socket ID for subsequent read/write operations on the client.
  clientNumber = number;
}
bluetooth.off('sppRead', clientNumber);

#### bluetooth.getProfile(deprecated)

getProfile(profileId: ProfileId): A2dpSourceProfile | HandsFreeAudioGatewayProfile

Obtains a profile object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/PNsDLYFKQTSRn5BK-Q18ZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=677240A91B8504E55CBECCB126B603D9AC50EC0DBEC7B30668DDBCA1B56D1E0A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.getProfileInstance](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothmanagergetprofileinstancedeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| profileId | [ProfileId](#profileiddeprecated) | Yes | ID of the profile to obtain, for example, **PROFILE\_A2DP\_SOURCE**. |

**Return value**

| Type | Description |
| :-- | :-- |
| [A2dpSourceProfile](#a2dpsourceprofile) | [HandsFreeAudioGatewayProfile](#handsfreeaudiogatewayprofile) | Profile object obtained. Only **A2dpSourceProfile** and **HandsFreeAudioGatewayProfile** are supported. |

**Example**

let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE\_A2DP\_SOURCE) as bluetooth.A2dpSourceProfile;

#### BLE

#### \[h2\]createGattServer(deprecated)

createGattServer(): GattServer

Creates a **GattServer** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/37XhrCrBRs2mSJDtrl1W3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B72E7637A4A8FD3AA39CDA5DA2B31BB8739AA798041DD642C72EC366360F56F6)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.BLE.createGattServer](../ohos-bluetoothmanager-bluetooth/document.md#creategattserverdeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [GattServer](#gattserver) | **GattServer** instance created. Before using a method of the server, you must create a **GattSever** instance. |

**Example**

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();

#### \[h2\]createGattClientDevice(deprecated)

createGattClientDevice(deviceId: string): GattClientDevice

Creates a **GattClientDevice** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/J6nzpJqRT62hDwKIeHNotQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF802F0A8F73E1271D63FB101CBFFCEA2722F81F4FCE597DFC1B5A393A3DEC37)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.BLE.createGattClientDevice](../ohos-bluetoothmanager-bluetooth/document.md#creategattclientdevicedeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the remote device, for example, XX:XX:XX:XX:XX:XX. |

**Return value**

| Type | Description |
| :-- | :-- |
| [GattClientDevice](#gattclientdevice) | **GattClientDevice** instance created. Before using a method of the client, you must create a **GattClientDevice** instance. |

**Example**

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');

#### \[h2\]getConnectedBLEDevices(deprecated)

getConnectedBLEDevices(): Array<string>

Obtains the BLE devices connected to this device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/GjJpttEYQ7i4EZ_Ks2Vw_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61FF40A4861592F498747A4804044F58AAFBDF0CD75D033F09A9565369892D7A)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.BLE.getConnectedBLEDevices](../ohos-bluetoothmanager-bluetooth/document.md#getconnectedbledevicesdeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | Addresses of the BLE devices connected to this device. |

**Example**

let result : Array<string> = bluetooth.BLE.getConnectedBLEDevices();

#### \[h2\]startBLEScan(deprecated)

startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void

Starts a BLE scan.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/dhwcxwI7TLa9236DfPdPdA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7E999F79F074A295EF21A8AF068978C0FC1AE03471C56CF69D8B4BD1FF10D32)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.BLE.startBLEScan](../ohos-bluetoothmanager-bluetooth/document.md#startblescandeprecated) instead.

**Required permissions**: ohos.permission.DISCOVER\_BLUETOOTH, ohos.permission.MANAGE\_BLUETOOTH (available only for system applications), and ohos.permission.LOCATION

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filters | Array<[ScanFilter](#scanfilterdeprecated)\> | Yes | Criteria for filtering the scan result. Set this parameter to **null** if you do not want to filter the scan result. |
| options | [ScanOptions](#scanoptionsdeprecated) | No | Scan options. |

**Return value**

No value is returned.

**Example**

function onReceiveEvent(data : Array<bluetooth.ScanResult>) {
    console.info('BLE scan device find result = '+ JSON.stringify(data));
}
bluetooth.BLE.on("BLEDeviceFind", onReceiveEvent);
let scanOptions : bluetooth.ScanOptions = {
    interval: 500,
    dutyMode: bluetooth.ScanDuty.SCAN\_MODE\_LOW\_POWER,
    matchMode: bluetooth.MatchMode.MATCH\_MODE\_AGGRESSIVE,
}

let scanFilter : bluetooth.ScanFilter = {
    deviceId:"XX:XX:XX:XX:XX:XX",
    name:"test",
    serviceUuid:"00001888-0000-1000-8000-00805f9b34fb"
}
bluetooth.BLE.startBLEScan(
    \[scanFilter\], scanOptions
);

#### \[h2\]stopBLEScan(deprecated)

stopBLEScan(): void

Stops the BLE scan.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/93L4uQDZSbqYqJkcynTvZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2749DBA3342B10BDC0B823C12CE0CE45F173E15D0CD33847A111B3BB9603FAFE)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.BLE.stopBLEScan](../ohos-bluetoothmanager-bluetooth/document.md#stopblescandeprecated) instead.

**Required permissions**: ohos.permission.DISCOVER\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

No value is returned.

**Example**

bluetooth.BLE.stopBLEScan();

#### \[h2\]on('BLEDeviceFind')(deprecated)

on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void

Subscribe to the BLE device discovery events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/9Ryu48m4RdibZ45pKludtA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16E9514FB363D95BB47AEF00533EA84BEEFD6D8121E24833C081F629A04FB649)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.BLE.on('BLEDeviceFind')](../ohos-bluetoothmanager-bluetooth/document.md#onbledevicefinddeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **BLEDeviceFind**, which indicates an event of discovering a BLE device. |
| callback | Callback<Array<[ScanResult](#scanresultdeprecated)\>> | Yes | Callback used to return the discovered devices. You need to implement this callback. |

**Return value**

No value is returned.

**Example**

function onReceiveEvent(data : Array<bluetooth.ScanResult>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
bluetooth.BLE.on('BLEDeviceFind', onReceiveEvent);

#### \[h2\]off('BLEDeviceFind')(deprecated)

off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void

Unsubscribes from the BLE device discovery events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/AjD-wikbR0ypF7nLOl1T-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F294827E209D8A9E0BB9CD155DE24EA74E3D001553D082B9ADE9E309FD70DA7)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.BLE.off('BLEDeviceFind')](../ohos-bluetoothmanager-bluetooth/document.md#offbledevicefinddeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **BLEDeviceFind**, which indicates an event of discovering a BLE device. |
| callback | Callback<Array<[ScanResult](#scanresultdeprecated)\>> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for **type**. |

**Return value**

No value is returned.

**Example**

function onReceiveEvent(data : Array<bluetooth.ScanResult>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
bluetooth.BLE.on('BLEDeviceFind', onReceiveEvent);
bluetooth.BLE.off('BLEDeviceFind', onReceiveEvent);

#### BaseProfile

Provides the profile base class.

#### \[h2\]getConnectionDevices(deprecated)

getConnectionDevices(): Array<string>

Obtains the connected devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/6p5TPZ_AQhq4NpH3ZtSYzg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=125683DD66E106D168C6244D0CB43ACF1EFB41D5695A2B0C1BD844C56493BBD8)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.BaseProfile.getConnectionDevices](../ohos-bluetoothmanager-bluetooth/document.md#getconnectiondevicesdeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | Addresses of the connected devices. |

**Example**

let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE\_A2DP\_SOURCE) as bluetooth.A2dpSourceProfile;
let retArray : Array<string> = a2dpSrc.getConnectionDevices();

#### \[h2\]getDeviceState(deprecated)

getDeviceState(device: string): ProfileConnectionState

Obtains the connection state of the profile.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/8SSUX1jbSeCkLRg38dHN_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE42B344AF2DC0B1F6EF269C9CD1B1EF3C5304609A5BB178AEE052DD758D6D51)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.BaseProfile.getDeviceState](../ohos-bluetoothmanager-bluetooth/document.md#getdevicestatedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | Address of the target device. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ProfileConnectionState](#profileconnectionstatedeprecated) | Profile connection state obtained. |

**Example**

let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE\_A2DP\_SOURCE) as bluetooth.A2dpSourceProfile;
let ret : bluetooth.ProfileConnectionState = a2dpSrc.getDeviceState('XX:XX:XX:XX:XX:XX');

#### A2dpSourceProfile

Before using a method of **A2dpSourceProfile**, you need to create an instance of this class by using the **getProfile()** method.

#### \[h2\]connect(deprecated)

connect(device: string): boolean

Sets up an Advanced Audio Distribution Profile (A2DP) connection.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/57ay6bAiQy6QP7JnJZd82g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0575801BD3282A702C7F6B5921E564914C2D462C664ED3483B80B35587A2B28D)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.A2dpSourceProfile.connect](../ohos-bluetoothmanager-bluetooth/document.md#connectdeprecated) instead.

**Required permissions**: ohos.permission.DISCOVER\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | Address of the target device. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE\_A2DP\_SOURCE) as bluetooth.A2dpSourceProfile;
let ret : boolean = a2dpSrc.connect('XX:XX:XX:XX:XX:XX');

#### \[h2\]disconnect(deprecated)

disconnect(device: string): boolean

Disconnects an A2DP connection.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/xFAyXeyLR8ee8AY5P3PJ2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=575F1DC3BFDC0A0245FC467F3683E505CAD1A167A70DBDF042B282BCCA23C31F)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.A2dpSourceProfile.disconnect](../ohos-bluetoothmanager-bluetooth/document.md#disconnectdeprecated) instead.

**Required permissions**: ohos.permission.DISCOVER\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | Address of the target device. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE\_A2DP\_SOURCE) as bluetooth.A2dpSourceProfile;
let ret : boolean = a2dpSrc.disconnect('XX:XX:XX:XX:XX:XX');

#### \[h2\]on('connectionStateChange')(deprecated)

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

Subscribes to the A2DP connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/kkSk-_a3Rs6wRZJ0aLvcFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5573E31F15ADC9AA53CACF9E01A7C3B03E7870A1F38EC12BE9835C2C0168880)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.A2dpSourceProfile.on('connectionStateChange')](../ohos-bluetoothmanager-bluetooth/document.md#onconnectionstatechangedeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **connectionStateChange**, which indicates a connection state change event. |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | Yes | Callback used to return the A2DP connection state. |

**Return value**

No value is returned.

**Example**

function onReceiveEvent(data : bluetooth.StateChangeParam) {
    console.info('a2dp state = '+ JSON.stringify(data));
}
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE\_A2DP\_SOURCE) as bluetooth.A2dpSourceProfile;
a2dpSrc.on('connectionStateChange', onReceiveEvent);

#### \[h2\]off('connectionStateChange')(deprecated)

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

Unsubscribes from the A2DP connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/mEID8mT8SAKECnQ6Gj_rmQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8605938AC14E8B6C35737664D7E1666B719BAB9BA49F7B66719EEFA69EC1B3D)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.A2dpSourceProfile.off('connectionStateChange')](../ohos-bluetoothmanager-bluetooth/document.md#offconnectionstatechangedeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **connectionStateChange**, which indicates a connection state change event. |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | No | Callback to unregister. |

**Return value**

No value is returned.

**Example**

function onReceiveEvent(data : bluetooth.StateChangeParam) {
    console.info('a2dp state = '+ JSON.stringify(data));
}
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE\_A2DP\_SOURCE) as bluetooth.A2dpSourceProfile;
a2dpSrc.on('connectionStateChange', onReceiveEvent);
a2dpSrc.off('connectionStateChange', onReceiveEvent);

#### \[h2\]getPlayingState(deprecated)

getPlayingState(device: string): PlayingState

Obtains the playing state of a device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/Z9_WZCh7R2WU4tk8Y_xZcg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2AE5B19C06A62D9175CD5623C4A39C1060C0E766F62794D60AF787039E7E13C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.A2dpSourceProfile.getPlayingState](../ohos-bluetoothmanager-bluetooth/document.md#getplayingstatedeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | Address of the target device. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PlayingState](#playingstatedeprecated) | Playing state of the remote device obtained. |

**Example**

let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE\_A2DP\_SOURCE) as bluetooth.A2dpSourceProfile;
let state : bluetooth.PlayingState = a2dpSrc.getPlayingState('XX:XX:XX:XX:XX:XX');

#### HandsFreeAudioGatewayProfile

Before using a method of **HandsFreeAudioGatewayProfile**, you need to create an instance of this class by using the **getProfile()** method.

#### \[h2\]connect(deprecated)

connect(device: string): boolean

Sets up a Hands-free Profile (HFP) connection of a device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/2jU1_WdlSo2TMoyq5hWi3Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F6636FBB3FBE57DFCFF2626242FB2D00ECD725BDEA3B0047F9E4C252D59BF153)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.HandsFreeAudioGatewayProfile.connect](../ohos-bluetoothmanager-bluetooth/document.md#connectdeprecated-1) instead.

**Required permissions**: ohos.permission.DISCOVER\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | Address of the target device. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let hfpAg : bluetooth.HandsFreeAudioGatewayProfile= bluetooth.getProfile(bluetooth.ProfileId
    .PROFILE\_HANDS\_FREE\_AUDIO\_GATEWAY);
let ret : boolean = hfpAg.connect('XX:XX:XX:XX:XX:XX');

#### \[h2\]disconnect(deprecated)

disconnect(device: string): boolean

Disconnects the HFP connection of a device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/LrEKpUGxRJOI3vJU0NGNYw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02F1DF42A7537D0E55F1664F6CB5FBE092E073465AA968F5CBE2195156274BAE)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.HandsFreeAudioGatewayProfile.disconnect](../ohos-bluetoothmanager-bluetooth/document.md#disconnectdeprecated-1) instead.

**Required permissions**: ohos.permission.DISCOVER\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | Address of the target device. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let hfpAg : bluetooth.HandsFreeAudioGatewayProfile = bluetooth.getProfile(bluetooth.ProfileId
    .PROFILE\_HANDS\_FREE\_AUDIO\_GATEWAY);
let ret : boolean = hfpAg.disconnect('XX:XX:XX:XX:XX:XX');

#### \[h2\]on('connectionStateChange')(deprecated)

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

Subscribes to the HFP connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/JsxmE1gqQhiEXwYkDXUyPQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D418F18271F6192B7C60D3A063AD1C4EABE3A4CC6850B50BE59AA4F3EDB8BDC)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.HandsFreeAudioGatewayProfile.on('connectionStateChange')](../ohos-bluetoothmanager-bluetooth/document.md#onconnectionstatechangedeprecated-1) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **connectionStateChange**, which indicates a connection state change event. |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | Yes | Callback used to return the HFP connection state. |

**Return value**

No value is returned.

**Example**

function onReceiveEvent(data : bluetooth.StateChangeParam) {
    console.info('hfp state = '+ JSON.stringify(data));
}
let hfpAg : bluetooth.HandsFreeAudioGatewayProfile= bluetooth.getProfile(bluetooth.ProfileId
    .PROFILE\_HANDS\_FREE\_AUDIO\_GATEWAY);
hfpAg.on('connectionStateChange', onReceiveEvent);

#### \[h2\]off('connectionStateChange')(deprecated)

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

Unsubscribes from the HFP connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/m-w1obxgSzyLWG_dTF78og/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8E34004EBE917E095B3BA8E11F2AFDE967ED2C751ADC485DB73F1A486358617C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.HandsFreeAudioGatewayProfile.off('connectionStateChange')](../ohos-bluetoothmanager-bluetooth/document.md#offconnectionstatechangedeprecated-1) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **connectionStateChange**, which indicates a connection state change event. |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | No | Callback to unregister. |

**Return value**

No value is returned.

**Example**

function onReceiveEvent(data : bluetooth.StateChangeParam) {
    console.info('hfp state = '+ JSON.stringify(data));
}
let hfpAg : bluetooth.HandsFreeAudioGatewayProfile= bluetooth.getProfile(bluetooth.ProfileId
    .PROFILE\_HANDS\_FREE\_AUDIO\_GATEWAY);
hfpAg.on('connectionStateChange', onReceiveEvent);
hfpAg.off('connectionStateChange', onReceiveEvent);

#### GattServer

Implements the Generic Attribute Profile (GATT) server. Before using a method of this class, you need to create a **GattServer** instance using the **createGattServer()** method.

#### \[h2\]startAdvertising(deprecated)

startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void

Starts BLE advertising.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/QQN0j4SSREqRJ9h0PDlufw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=476C054CEDC2A13F8370EA879F30AC30720090DD4BEFEF713EA5264CC25C1FA3)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattServer.startAdvertising](../ohos-bluetoothmanager-bluetooth/document.md#startadvertisingdeprecated) instead.

**Required permissions**: ohos.permission.DISCOVER\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| setting | [AdvertiseSetting](#advertisesettingdeprecated) | Yes | Settings related to BLE advertising. |
| advData | [AdvertiseData](#advertisedatadeprecated) | Yes | Content of the BLE advertisement packet. |
| advResponse | [AdvertiseData](#advertisedatadeprecated) | No | Response to the BLE scan request. |

**Return value**

No value is returned.

**Example**

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
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
let setting : bluetooth.AdvertiseSetting = {
    interval:150,
    txPower:60,
    connectable:true,
}

let manufactureData : bluetooth.ManufactureData = {
    manufactureId:4567,
    manufactureValue:manufactureValueBuffer.buffer
}

let serviceData : bluetooth.ServiceData = {
    serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
    serviceValue:serviceValueBuffer.buffer
}

let advData : bluetooth.AdvertiseData = {
    serviceUuids:\["00001889-0000-1000-8000-00805f9b34fb"\],
    manufactureData:\[manufactureData\],
    serviceData:\[serviceData\],
}

let advResponse : bluetooth.AdvertiseData = {
    serviceUuids:\["00001889-0000-1000-8000-00805f9b34fb"\],
    manufactureData:\[manufactureData\],
    serviceData:\[serviceData\],
}
gattServer.startAdvertising(setting, advData, advResponse);

#### \[h2\]stopAdvertising(deprecated)

stopAdvertising(): void

Stops BLE advertising.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/qf4U3r8oSByT0BzC8snqow/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66064C8DE478C7EC040A2F5AB8009A5FFD2988AD90F6700F5FF12882250F0845)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattServer.stopAdvertising](../ohos-bluetoothmanager-bluetooth/document.md#stopadvertisingdeprecated) instead.

**Required permissions**: ohos.permission.DISCOVER\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

No value is returned.

**Example**

let server : bluetooth.GattServer = bluetooth.BLE.createGattServer();
server.stopAdvertising();

#### \[h2\]addService(deprecated)

addService(service: GattService): boolean

Adds a service to this GATT server.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/l8Fk7im0RF-EueLo7eHRSA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02C9C0ECFB16250D10B3D354F9FF3F255D9A1D02028B35985902519A245D1C3C)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattServer.addService](../ohos-bluetoothmanager-bluetooth/document.md#addservicedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| service | [GattService](#gattservicedeprecated) | Yes | Service to add. Settings related to BLE advertising. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

// Create descriptors.
let descriptors : Array<bluetooth.BLEDescriptor> = \[\];
let arrayBuffer = new ArrayBuffer(8);
let descV = new Uint8Array(arrayBuffer);
descV\[0\] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
descriptors\[0\] = descriptor;

// Create characteristics.
let characteristics : Array<bluetooth.BLECharacteristic> = \[\];
let arrayBufferC = new ArrayBuffer(8);
let cccV = new Uint8Array(arrayBufferC);
cccV\[0\] = 1;
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
let characteristicN : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001821-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
characteristics\[0\] = characteristic;

// Create a gattService instance.
let gattService : bluetooth.GattService = {serviceUuid:'00001810-0000-1000-8000-00805F9B34FB', isPrimary: true, characteristics:characteristics, includeServices:\[\]};

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
let ret : boolean = gattServer.addService(gattService);
if (ret) {
   console.info("add service successfully");
} else {
   console.error("add service failed");
}

#### \[h2\]removeService(deprecated)

removeService(serviceUuid: string): boolean

Removes a service from this GATT server.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/OVAnuKa3TS6ltbgq9joSOg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C66B4D5CAD451AA097E9AF8F72FDD84D94A2A96B9A71CBDF4DB95ED274E2E699)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattServer.removeService](../ohos-bluetoothmanager-bluetooth/document.md#removeservicedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| serviceUuid | string | Yes | Universally unique identifier (UUID) of the service to remove, for example, **00001810-0000-1000-8000-00805F9B34FB**. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let server : bluetooth.GattServer = bluetooth.BLE.createGattServer();
server.removeService('00001810-0000-1000-8000-00805F9B34FB');

#### \[h2\]close(deprecated)

close(): void

Closes this GATT server to unregister it from the protocol stack. After this method is called, this [GattServer](#gattserver) cannot be used.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/GX4R6Q70QLWQg8DmZl2Lhw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=859006A92B3E87C52039D13E8D0CE72E041219203C0BCEE829D0F322EF46305D)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattServer.close](../ohos-bluetoothmanager-bluetooth/document.md#closedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Example**

let server : bluetooth.GattServer = bluetooth.BLE.createGattServer();
server.close();

#### \[h2\]notifyCharacteristicChanged(deprecated)

notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): boolean

Notifies the connected client device when a characteristic value changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/kUhlx3IGRLqJH9GL4EadYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=374BE83E4EBCFBBE26F1DC57FF2427CAF969497027D05A1C42C95E5E34F40067)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattServer.notifyCharacteristicChanged](../ohos-bluetoothmanager-bluetooth/document.md#notifycharacteristicchangeddeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Address of the client that receives notifications, for example, XX:XX:XX:XX:XX:XX. |
| notifyCharacteristic | [NotifyCharacteristic](#notifycharacteristicdeprecated) | Yes | New characteristic value. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

// Create descriptors.
let descriptors : Array<bluetooth.BLEDescriptor> = \[\];
let arrayBuffer = new ArrayBuffer(8);
let descV = new Uint8Array(arrayBuffer);
descV\[0\] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
descriptors\[0\] = descriptor;
let arrayBufferC = new ArrayBuffer(8);
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
let notifyCharacteristic : bluetooth.NotifyCharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001821-0000-1000-8000-00805F9B34FB', characteristicValue: characteristic.characteristicValue, confirm: false};
let server : bluetooth.GattServer = bluetooth.BLE.createGattServer();
server.notifyCharacteristicChanged('XX:XX:XX:XX:XX:XX', notifyCharacteristic);

#### \[h2\]sendResponse(deprecated)

sendResponse(serverResponse: ServerResponse): boolean

Sends a response to a read or write request from the GATT client.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/Fpur1jXbQm23z4Hfca_12w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C759DF8FC77BD1ABA48E44D2C80D57E2A63B9FC8332ED961467D4E9973BD5B79)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattServer.sendResponse](../ohos-bluetoothmanager-bluetooth/document.md#sendresponsedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| serverResponse | [ServerResponse](#serverresponsedeprecated) | Yes | Response returned by the GATT server. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

/\* send response \*/
let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
cccValue\[0\] = 1;
let serverResponse : bluetooth.ServerResponse = {
    "deviceId": "XX:XX:XX:XX:XX:XX",
    "transId": 0,
    "status": 0,
    "offset": 0,
    "value": arrayBufferCCC,
};

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
let ret : boolean = gattServer.sendResponse(serverResponse);
if (ret) {
  console.info('bluetooth sendResponse successfully');
} else {
  console.error('bluetooth sendResponse failed');
}

#### \[h2\]on('characteristicRead')(deprecated)

on(type: 'characteristicRead', callback: Callback<CharacteristicReadReq>): void

Subscribes to the characteristic read request events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/kFXZZKX4S5CtNZ6uqnO3sg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C668B763ECD864A72318E5E13A6BE24D70E185B010AAB46450D155B4268CBC4D)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattServer.on('characteristicRead')](../ohos-bluetoothmanager-bluetooth/document.md#oncharacteristicreaddeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **characteristicRead**, which indicates a characteristic read request event. |
| callback | Callback<[CharacteristicReadReq](#characteristicreadreqdeprecated)\> | Yes | Callback used to return a characteristic read request event from the GATT client. |

**Return value**

No value is returned.

**Example**

let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
cccValue\[0\] = 1;
function ReadCharacteristicReq(CharacteristicReadReq : bluetooth.CharacteristicReadReq) {
  let deviceId : string = CharacteristicReadReq.deviceId;
  let transId : number = CharacteristicReadReq.transId;
  let offset : number = CharacteristicReadReq.offset;
  let characteristicUuid : string = CharacteristicReadReq.characteristicUuid;

  let serverResponse : bluetooth.ServerResponse = {deviceId: deviceId, transId: transId, status: 0,
  offset: offset, value:arrayBufferCCC};

  let ret : boolean = gattServer.sendResponse(serverResponse);
  if (ret) {
    console.info('bluetooth sendResponse successfully');
  } else {
    console.error('bluetooth sendResponse failed');
  }
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("characteristicRead", ReadCharacteristicReq);

#### \[h2\]off('characteristicRead')(deprecated)

off(type: 'characteristicRead', callback?: Callback<CharacteristicReadReq>): void

Unsubscribes from the characteristic read request events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/ytf3b68YQuKsULuUDmJp1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73F58213341ED79BA66D1651C1B712A78CDBCBD1E4753590003B44CBD0B5FA2E)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattServer.off('characteristicRead')](../ohos-bluetoothmanager-bluetooth/document.md#offcharacteristicreaddeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **characteristicRead**, which indicates a characteristic read request event. |
| callback | Callback<[CharacteristicReadReq](#characteristicreadreqdeprecated)\> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for **type**. |

**Return value**

No value is returned.

**Example**

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("characteristicRead");

#### \[h2\]on('characteristicWrite')(deprecated)

on(type: 'characteristicWrite', callback: Callback<CharacteristicWriteReq>): void

Subscribes to the characteristic write request events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/uSX-SH3BQjatgnxM6UiqPw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=38823FEAA873181F440221B113A6885D14E1AB65D664CCA065F7E4FB5F164C41)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattServer.on('characteristicWrite')](../ohos-bluetoothmanager-bluetooth/document.md#oncharacteristicwritedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **characteristicWrite**, which indicates a characteristic write request event. |
| callback | Callback<[CharacteristicWriteReq](#characteristicwritereqdeprecated)\> | Yes | Callback used to return a characteristic write request from the GATT client. |

**Return value**

No value is returned.

**Example**

let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
function WriteCharacteristicReq(CharacteristicWriteReq : bluetooth.CharacteristicWriteReq) {
  let deviceId : string = CharacteristicWriteReq.deviceId;
  let transId : number = CharacteristicWriteReq.transId;
  let offset : number = CharacteristicWriteReq.offset;
  let isPrep : boolean = CharacteristicWriteReq.isPrep;
  let needRsp : boolean = CharacteristicWriteReq.needRsp;
  let value =  new Uint8Array(arrayBufferCCC);
  let characteristicUuid : string = CharacteristicWriteReq.characteristicUuid;

  cccValue.set(new Uint8Array(value));
  let serverResponse : bluetooth.ServerResponse = {deviceId: deviceId, transId: transId, status: 0,
  offset: offset, value:arrayBufferCCC};

  let ret : boolean = gattServer.sendResponse(serverResponse);
  if (ret) {
    console.info('bluetooth sendResponse successfully');
  } else {
    console.error('bluetooth sendResponse failed');
  }
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("characteristicWrite", WriteCharacteristicReq);

#### \[h2\]off('characteristicWrite')(deprecated)

off(type: 'characteristicWrite', callback?: Callback<CharacteristicWriteReq>): void

Unsubscribes from the characteristic write request events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/pXNLc7CJQqKTyw8c5melKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD82998F0E9B34C9FDEC7A53A7B16D6DEF74E38B72F5877D32B75A934FF4CF6E)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattServer.off('characteristicWrite')](../ohos-bluetoothmanager-bluetooth/document.md#offcharacteristicwritedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **characteristicWrite**, which indicates a characteristic write request event. |
| callback | Callback<[CharacteristicWriteReq](#characteristicwritereqdeprecated)\> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for **type**. |

**Return value**

No value is returned.

**Example**

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("characteristicWrite");

#### \[h2\]on('descriptorRead')(deprecated)

on(type: 'descriptorRead', callback: Callback<DescriptorReadReq>): void

Subscribes to the descriptor read request events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/MKOO3YSOR5-T1rfofERRCg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=89280AC6DFC44414EEAD4224D594BCD163D32E1754D6F9919D8948178CD555B5)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattServer.on('descriptorRead')](../ohos-bluetoothmanager-bluetooth/document.md#ondescriptorreaddeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **descriptorRead**, which indicates a descriptor read request event. |
| callback | Callback<[DescriptorReadReq](#descriptorreadreqdeprecated)\> | Yes | Callback used to return a characteristic read request event from the GATT client. |

**Return value**

No value is returned.

**Example**

let arrayBufferDesc = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBufferDesc);
descValue\[0\] = 1;
function ReadDescriptorReq(DescriptorReadReq : bluetooth.DescriptorReadReq) {
  let deviceId : string = DescriptorReadReq.deviceId;
  let transId : number = DescriptorReadReq.transId;
  let offset : number = DescriptorReadReq.offset;
  let descriptorUuid : string = DescriptorReadReq.descriptorUuid;

  let serverResponse : bluetooth.ServerResponse = {deviceId: deviceId, transId: transId, status: 0,
  offset: offset, value:arrayBufferDesc};

  let ret : boolean = gattServer.sendResponse(serverResponse);
  if (ret) {
    console.info('bluetooth sendResponse successfully');
  } else {
    console.error('bluetooth sendResponse failed');
  }
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("descriptorRead", ReadDescriptorReq);

#### \[h2\]off('descriptorRead')(deprecated)

off(type: 'descriptorRead', callback?: Callback<DescriptorReadReq>): void

Unsubscribes from the descriptor read request events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/LtOewEa7Tf-p_UVsGQlGww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D14D0D224AB4FBCEE372D9D8BCAFBA861DB54751F4A60E804C58A25F2226CE57)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattServer.off('descriptorRead')](../ohos-bluetoothmanager-bluetooth/document.md#offdescriptorreaddeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **descriptorRead**, which indicates a descriptor read request event. |
| callback | Callback<[DescriptorReadReq](#descriptorreadreqdeprecated)\> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for **type**. |

**Return value**

No value is returned.

**Example**

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("descriptorRead");

#### \[h2\]on('descriptorWrite')(deprecated)

on(type: 'descriptorWrite', callback: Callback<DescriptorWriteReq>): void

Subscribes to the descriptor write request events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/juOcMCn4TEemOxGGUjC8Qg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53A3D2EAA0310A3CEB4793E4D6ED569BCF6475C00D8F2B644F0FE69A5BBC6C8C)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattServer.on('descriptorWrite')](../ohos-bluetoothmanager-bluetooth/document.md#ondescriptorwritedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **descriptorWrite**, which indicates a descriptor write request event. |
| callback | Callback<[DescriptorWriteReq](#descriptorwritereqdeprecated)\> | Yes | Callback used to return a characteristic write request from the GATT client. |

**Return value**

No value is returned.

**Example**

let arrayBufferDesc = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBufferDesc);
function WriteDescriptorReq(DescriptorWriteReq : bluetooth.DescriptorWriteReq) {
  let deviceId : string = DescriptorWriteReq.deviceId;
  let transId : number = DescriptorWriteReq.transId;
  let offset : number = DescriptorWriteReq.offset;
  let isPrep : boolean = DescriptorWriteReq.isPrep;
  let needRsp : boolean = DescriptorWriteReq.needRsp;
  let value = new Uint8Array(arrayBufferDesc);
  let descriptorUuid : string = DescriptorWriteReq.descriptorUuid;

  descValue.set(new Uint8Array(value));
  let serverResponse : bluetooth.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferDesc};

  let ret : boolean = gattServer.sendResponse(serverResponse);
  if (ret) {
    console.info('bluetooth sendResponse successfully');
  } else {
    console.error('bluetooth sendResponse failed');
  }
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("descriptorWrite", WriteDescriptorReq);

#### \[h2\]off('descriptorWrite')(deprecated)

off(type: 'descriptorWrite', callback?: Callback<DescriptorWriteReq>): void

Unsubscribes from the descriptor write request events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/YOnaQHOVQRS3NDPuuhlmxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E75302A25C6BAA04D71B1B7392F30BA9EA3A70B8FB6A1A8200999C984A9D5C65)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattServer.off('descriptorWrite')](../ohos-bluetoothmanager-bluetooth/document.md#offdescriptorwritedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **descriptorWrite**, which indicates a descriptor write request event. |
| callback | Callback<[DescriptorWriteReq](#descriptorwritereqdeprecated)\> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for **type**. |

**Return value**

No value is returned.

**Example**

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("descriptorWrite");

#### \[h2\]on('connectStateChange')(deprecated)

on(type: 'connectStateChange', callback: Callback<BLEConnectChangedState>): void

Subscribes to the BLE connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/HmzdCUe2TLCy4AcQPD7R6A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=93EE49E424B12F6AE99EC2BD68C6099484CD08FAC85A9B98AA2DC00F0FB3E2FE)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattServer.on('connectStateChange')](../ohos-bluetoothmanager-bluetooth/document.md#onconnectstatechangedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **connectStateChange**, which indicates a BLE connection state change event. |
| callback | Callback<[BLEConnectChangedState](#bleconnectchangedstatedeprecated)\> | Yes | Callback used to return the BLE connection state. |

**Return value**

No value is returned.

**Example**

function Connected(BLEConnectChangedState : bluetooth.BLEConnectChangedState) {
  let deviceId : string = BLEConnectChangedState.deviceId;
  let status : bluetooth.ProfileConnectionState = BLEConnectChangedState.state;
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("connectStateChange", Connected);

#### \[h2\]off('connectStateChange')(deprecated)

off(type: 'connectStateChange', callback?: Callback<BLEConnectChangedState>): void

Unsubscribes from the BLE connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/0vWD2HshQhKh7Iuho8Lz8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=276F3B2C3341E46DDEAA449539EE7A28100BDEF73346436A96F01FF74391E41F)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattServer.off('connectStateChange')](../ohos-bluetoothmanager-bluetooth/document.md#offconnectstatechangedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **connectStateChange**, which indicates a BLE connection state change event. |
| callback | Callback<[BLEConnectChangedState](#bleconnectchangedstatedeprecated)\> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for **type**. |

**Return value**

No value is returned.

**Example**

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("connectStateChange");

#### GattClientDevice

Implements the GATT client. Before using a method of this class, you must create a **GattClientDevice** instance using the **createGattClientDevice(deviceId: string)** method.

#### \[h2\]connect(deprecated)

connect(): boolean

Initiates a connection to the remote BLE device on the client.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/iW1G4OesSaqs2ECLVW4bsQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64176941CCDB491D4AE3A5851C308B4799FB365082EE15099A66B940249C865E)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.connect](../ohos-bluetoothmanager-bluetooth/document.md#connectdeprecated-1) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the connection is successful; returns **false** otherwise. |

**Example**

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let ret : boolean = device.connect();

#### \[h2\]disconnect(deprecated)

disconnect(): boolean

Disconnects from the remote BLE device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/lYiW6l4zSmOK3JI5-M189A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE4775FBBC17601007A38B8E6AA90366BD12A93E209A474B591B420D8905B92B)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.disconnect](../ohos-bluetoothmanager-bluetooth/document.md#disconnectdeprecated-2) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let ret : boolean = device.disconnect();

#### \[h2\]close(deprecated)

close(): boolean

Closes this GATT client to unregister it from the protocol stack. After this method is called, this [GattClientDevice](#gattclientdevice) instance cannot be used.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/9mV_XEtxS_S-riClrTKKqg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=12D15533497567286FC4B7AA2795AC9467ABA1C77EB9EFF02D8E0712A99119D4)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.close](../ohos-bluetoothmanager-bluetooth/document.md#closedeprecated-1) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let ret : boolean = device.close();

#### \[h2\]getServices(deprecated)

getServices(callback: AsyncCallback<Array<GattService>>): void

Obtains all services of the remote BLE device. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/obAh7-4VT4e6lEuKpv6xRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B74D9A476AFACD186B15EDF4240BFB22795092A4655C440645E7432E7CED6267)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.getServices](../ohos-bluetoothmanager-bluetooth/document.md#getservicesdeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[GattService](#gattservicedeprecated)\>> | Yes | Callback used to return the services obtained. |

**Return value**

No value is returned.

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
// Callback mode.
function getServices(code : BusinessError, gattServices : Array<bluetooth.GattService>) {
  if (code.code == 0) {
      console.info(\`bluetooth code is ${code.code}\`);
      console.info(\`bluetooth services size is ${gattServices.length}\`);

      for (let i = 0; i < gattServices.length; i++) {
        console.info(\`bluetooth serviceUuid is ${gattServices\[i\].serviceUuid}\`);
      }
  }
}

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.connect();
device.getServices(getServices);

#### \[h2\]getServices(deprecated)

getServices(): Promise<Array<GattService>>

Obtains all services of the remote BLE device. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/gYCtxPtLR9OBeS51A2yPVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CD84C48FA4A7198FB6C68E5C28C614A14676EE137910E426C26EB3545AA4C9D)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.getServices](../ohos-bluetoothmanager-bluetooth/document.md#getservicesdeprecated-1) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[GattService](#gattservicedeprecated)\>> | Promise used to return the services obtained. |

**Example**

// Promise
let device : bluetooth.GattClientDevice= bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.connect();
device.getServices().then((result : Array<bluetooth.GattService>) => {
    console.info("getServices successfully:" + JSON.stringify(result));
});

#### \[h2\]readCharacteristicValue(deprecated)

readCharacteristicValue(characteristic: BLECharacteristic, callback: AsyncCallback<BLECharacteristic>): void

Reads the characteristic value of the specific service of the remote BLE device on the client.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/iCqxI9BESJWSwW6ign1X7w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B93AAF6A16A16B48C3579965E40A0DBF7FB1A0CD9F64D1D6644A94EF311069EE)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.readCharacteristicValue](../ohos-bluetoothmanager-bluetooth/document.md#readcharacteristicvaluedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| characteristic | [BLECharacteristic](#blecharacteristicdeprecated) | Yes | Characteristic value to read. |
| callback | AsyncCallback<[BLECharacteristic](#blecharacteristicdeprecated)\> | Yes | Callback used to return the characteristic value read. |

**Return value**

No value is returned.

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
function readCcc(code : BusinessError, BLECharacteristic : bluetooth.BLECharacteristic) {
  if (code.code != 0) {
      return;
  }
  console.info(\`bluetooth characteristic uuid: ${BLECharacteristic.characteristicUuid}\`);
  let value = new Uint8Array(BLECharacteristic.characteristicValue);
}

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let descriptors : Array<bluetooth.BLEDescriptor> = \[\];
let bufferDesc : ArrayBuffer = new ArrayBuffer(8);
let descV : Uint8Array = new Uint8Array(bufferDesc);
descV\[0\] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors\[0\] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV\[0\] = 1;
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
characteristicValue: bufferCCC, descriptors:descriptors};

device.readCharacteristicValue(characteristic, readCcc);

#### \[h2\]readCharacteristicValue(deprecated)

readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>

Reads the characteristic value of the specific service of the remote BLE device on the client. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/xnYWmpFdTAu_BLdS1ryliw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=946EFF608669ECFAD2D17AECB36275C06907660BC63E06E133241734CAE33F0B)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.readCharacteristicValue](../ohos-bluetoothmanager-bluetooth/document.md#readcharacteristicvaluedeprecated-1) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| characteristic | [BLECharacteristic](#blecharacteristicdeprecated) | Yes | Characteristic value to read. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[BLECharacteristic](#blecharacteristicdeprecated)\> | Promise used to return the characteristic value read. |

**Example**

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let descriptors : Array<bluetooth.BLEDescriptor> = \[\];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV\[0\] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors\[0\] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV\[0\] = 1;
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
characteristicValue: bufferCCC, descriptors:descriptors};

device.readCharacteristicValue(characteristic);

#### \[h2\]readDescriptorValue(deprecated)

readDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<BLEDescriptor>): void

Reads the descriptor contained in the specific characteristic of the remote BLE device on the client.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/V5ou1BZHQVa0Vtc9lgpOTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70B099AA4E1BBD06254781703369FCC03789915EE09CAE2BA695F823CD2DBA29)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.readDescriptorValue](../ohos-bluetoothmanager-bluetooth/document.md#readdescriptorvaluedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| descriptor | [BLEDescriptor](#bledescriptordeprecated) | Yes | Descriptor to read. |
| callback | AsyncCallback<[BLEDescriptor](#bledescriptordeprecated)\> | Yes | Callback used to return the descriptor read. |

**Return value**

No value is returned.

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
function readDesc(code : BusinessError, BLEDescriptor : bluetooth.BLEDescriptor) {
  if (code.code != 0) {
      return;
  }
  console.info(\`bluetooth descriptor uuid: ${BLEDescriptor.descriptorUuid}\`);
  let value = new Uint8Array(BLEDescriptor.descriptorValue);
}

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV\[0\] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
device.readDescriptorValue(descriptor, readDesc);

#### \[h2\]readDescriptorValue(deprecated)

readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>

Reads the descriptor contained in the specific characteristic of the remote BLE device on the client. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/omO2rk-JRj-Z05QUo4p0cg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A5F6067140FBBB403A93C1E5F88529690949540E48098D09BAB1EA4E5E491CED)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.readDescriptorValue](../ohos-bluetoothmanager-bluetooth/document.md#readdescriptorvaluedeprecated-1) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| descriptor | [BLEDescriptor](#bledescriptordeprecated) | Yes | Descriptor to read. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[BLEDescriptor](#bledescriptordeprecated)\> | Promise used to return the descriptor read. |

**Example**

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV\[0\] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
device.readDescriptorValue(descriptor);

#### \[h2\]writeCharacteristicValue(deprecated)

writeCharacteristicValue(characteristic: BLECharacteristic): boolean

Writes a characteristic value to the remote BLE device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/EbJKHKzZQQCPRHN3r-_ySg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4AEB8A381D818C7DFACFB64BDE6A70E2977D25AF5B54699DCB19123AC92CFD1)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.writeCharacteristicValue](../ohos-bluetoothmanager-bluetooth/document.md#writecharacteristicvaluedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| characteristic | [BLECharacteristic](#blecharacteristicdeprecated) | Yes | Binary value and other parameters of the BLE device characteristic. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let descriptors : Array<bluetooth.BLEDescriptor> = \[\];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV\[0\] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors\[0\] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV\[0\] = 1;
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  characteristicValue: bufferCCC, descriptors:descriptors};
let retWriteCcc : boolean = device.writeCharacteristicValue(characteristic);
if (retWriteCcc) {
  console.info('write characteristic successfully');
} else {
  console.error('write characteristic failed');
}

#### \[h2\]writeDescriptorValue(deprecated)

writeDescriptorValue(descriptor: BLEDescriptor): boolean

Writes binary data to the specific descriptor of the remote BLE device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/ovYsbVS5QXCG0ccVBIfX8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5136E8E956E755C868FBF2045838C35EFE8C9E0C1ED263487B134C2717272167)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.writeDescriptorValue](../ohos-bluetoothmanager-bluetooth/document.md#writedescriptorvaluedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| descriptor | [BLEDescriptor](#bledescriptordeprecated) | Yes | Binary value and other parameters of the BLE device descriptor. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV\[0\] = 22;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
let retWriteDesc : boolean = device.writeDescriptorValue(descriptor);
if (retWriteDesc) {
  console.info('bluetooth write descriptor successfully');
} else {
  console.error('bluetooth write descriptor failed');
}

#### \[h2\]setBLEMtuSize(deprecated)

setBLEMtuSize(mtu: number): boolean

Sets the maximum transmission unit (MTU) that can be transmitted between the GATT client and its remote BLE device. This API can be used only after a connection is set up by calling [connect](#connectdeprecated).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/vysjzLURSVKxHtiSG70dFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9BFE04D8BE260CA2463CF1C3BC4844BCD38F98F4BECB352A1A73E4E1A772FB46)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.setBLEMtuSize](../ohos-bluetoothmanager-bluetooth/document.md#setblemtusizedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mtu | number | Yes | MTU to set, which ranges from 22 to 512 bytes. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.setBLEMtuSize(128);

#### \[h2\]setNotifyCharacteristicChanged(deprecated)

setNotifyCharacteristicChanged(characteristic: BLECharacteristic, enable: boolean): boolean

Sets the function of notifying the GATT client when the characteristic value of the remote BLE device changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/ceClS-UZSc2cafOJAE9blQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C23EABACBF17CF41A2F8563C6D2A3DC05AC7ACC3E730B7ACB242949FA8C9A4B)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.setNotifyCharacteristicChanged](../ohos-bluetoothmanager-bluetooth/document.md#setnotifycharacteristicchangeddeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| characteristic | [BLECharacteristic](#blecharacteristicdeprecated) | Yes | BLE characteristic to listen for. |
| enable | boolean | Yes | Whether to enable the notify function. The value **true** means to enable the notify function, and the value **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

// Create descriptors.
let descriptors : Array<bluetooth.BLEDescriptor> = \[\];
let arrayBuffer = new ArrayBuffer(8);
let descV = new Uint8Array(arrayBuffer);
descV\[0\] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
descriptors\[0\] = descriptor;
let arrayBufferC = new ArrayBuffer(8);
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.setNotifyCharacteristicChanged(characteristic, false);

#### \[h2\]on('BLECharacteristicChange')(deprecated)

on(type: 'BLECharacteristicChange', callback: Callback<BLECharacteristic>): void

Subscribes to the BLE characteristic changes. The client can receive a notification from the server only after the **setNotifyCharacteristicChanged** method is called.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/7u9OEPk2TfWVV72MymqmTA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53A5FD37F9C07BE03695E7C681D93CDD1C420DA447156E095203EC339A89A8A7)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.on('BLECharacteristicChange')](../ohos-bluetoothmanager-bluetooth/document.md#onblecharacteristicchangedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **BLECharacteristicChange**, which indicates a characteristic value change event. |
| callback | Callback<[BLECharacteristic](#blecharacteristicdeprecated)\> | Yes | Callback used to return the characteristic value changes. |

**Return value**

No value is returned.

**Example**

function CharacteristicChange(CharacteristicChangeReq : bluetooth.BLECharacteristic) {
  let serviceUuid : string = CharacteristicChangeReq.serviceUuid;
  let characteristicUuid : string = CharacteristicChangeReq.characteristicUuid;
  let value = new Uint8Array(CharacteristicChangeReq.characteristicValue);
}
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.on('BLECharacteristicChange', CharacteristicChange);

#### \[h2\]off('BLECharacteristicChange')(deprecated)

off(type: 'BLECharacteristicChange', callback?: Callback<BLECharacteristic>): void

Unsubscribes from the BLE characteristic changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/C1VIFi6NS-aA2bMEZgLH-w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C29C5D747A761800F3983A8C5CEC296B7D3D55325BCCDE29BDC3865DE57ABED6)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.off('BLECharacteristicChange')](../ohos-bluetoothmanager-bluetooth/document.md#offblecharacteristicchangedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **BLECharacteristicChange**, which indicates a characteristic value change event. |
| callback | Callback<[BLECharacteristic](#blecharacteristicdeprecated)\> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for **type**. |

**Return value**

No value is returned.

**Example**

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.off('BLECharacteristicChange');

#### \[h2\]on('BLEConnectionStateChange')(deprecated)

on(type: 'BLEConnectionStateChange', callback: Callback<BLEConnectChangedState>): void

Subscribes to the BLE connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/SgZilZG7RNGoJFjDOewZAg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DC1617DE0C9CEAB24D04D590B2FED33606903DD325BA38E436707FE59F8A1A7)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.on('BLEConnectionStateChange')](../ohos-bluetoothmanager-bluetooth/document.md#onbleconnectionstatechangedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **BLEConnectionStateChange**, which indicates a BLE connection state change event. |
| callback | Callback<[BLEConnectChangedState](#bleconnectchangedstatedeprecated)\> | Yes | Callback used to return the BLE connection state. |

**Return value**

No value is returned.

**Example**

function ConnectStateChanged(state : bluetooth.BLEConnectChangedState) {
  console.info('bluetooth connect state changed');
  let connectState : bluetooth.ProfileConnectionState = state.state;
}
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.on('BLEConnectionStateChange', ConnectStateChanged);

#### \[h2\]off('BLEConnectionStateChange')(deprecated)

off(type: 'BLEConnectionStateChange', callback?: Callback<BLEConnectChangedState>): void

Unsubscribes from the BLE connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/Z_9iX3U-Qjq4w4lSTsMcGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB025D47DE44ED7B4656D2E6112EA38BF9CB53C549F841B2EC664C4B879BC3D5)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.off('BLEConnectionStateChange')](../ohos-bluetoothmanager-bluetooth/document.md#offbleconnectionstatechangedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **BLEConnectionStateChange**, which indicates a BLE connection state change event. |
| callback | Callback<[BLEConnectChangedState](#bleconnectchangedstatedeprecated)\> | No | Callback to unregister. If this parameter is not set, this API unregisters all callbacks for **type**. |

**Return value**

No value is returned.

**Example**

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.off('BLEConnectionStateChange');

#### \[h2\]getDeviceName(deprecated)

getDeviceName(callback: AsyncCallback<string>): void

Obtains the name of the remote BLE device on the client.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/DhNxDVMFTYiW1d4U2tWrug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB4F2283DE10ED1447167C0BD453038051BD3B38F9BA55EEF8B4B7EA29515EF2)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.getDeviceName](../ohos-bluetoothmanager-bluetooth/document.md#getdevicenamedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the remote BLE device name obtained. |

**Return value**

No value is returned.

**Example**

import { BusinessError } from '@ohos.base';
// callback
let gattClient : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
let deviceName : void = gattClient.getDeviceName((err : BusinessError, data : string)=> {
    console.info('device name err ' + JSON.stringify(err));
    console.info('device name' + JSON.stringify(data));
})

#### \[h2\]getDeviceName(deprecated)

getDeviceName(): Promise<string>

Obtains the name of the remote BLE device on the client. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/bPsCRPQQTl22CMytp-2aPA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F54B8E64E427CE4A3C61CE7C533C2FBAEC11B763765A40D3C3FE0434532AF91F)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.getDeviceName](../ohos-bluetoothmanager-bluetooth/document.md#getdevicenamedeprecated-1) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the remote BLE device name. |

**Example**

// promise
let gattClient : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
gattClient.getDeviceName().then((data) => {
    console.info('device name' + JSON.stringify(data));
})

#### \[h2\]getRssiValue(deprecated)

getRssiValue(callback: AsyncCallback<number>): void

Obtains the received signal strength indication (RSSI) of the remote BLE device on the client. This API can be used only after a connection is set up by calling [connect](#connectdeprecated).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/opJegiDOSD60YbvH-wuZrg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A17EB4A3852F60517A9A2D2C28984B9E70F0097C8102CBEFFD5855FD637C70A4)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.getRssiValue](../ohos-bluetoothmanager-bluetooth/document.md#getrssivaluedeprecated) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the RSSI, in dBm. |

**Return value**

No value is returned.

**Example**

import { BusinessError } from '@ohos.base';
// callback
let gattClient : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
let ret : boolean = gattClient.connect();
gattClient.getRssiValue((err : BusinessError, data : number)=> {
    console.info('rssi err ' + JSON.stringify(err));
    console.info('rssi value' + JSON.stringify(data));
})

#### \[h2\]getRssiValue(deprecated)

getRssiValue(): Promise<number>

Obtains the RSSI of the remote BLE device on the client. This API uses a promise to return the result. It can be used only after a connection is set up by calling [connect](#connectdeprecated).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/nJSrEpnPSbKwSeMrb8XDFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC3547C4E714A22841A2740338BE11402B2E5310EB87119AD90FAB79ADDB57F6)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattClientDevice.getRssiValue](../ohos-bluetoothmanager-bluetooth/document.md#getrssivaluedeprecated-1) instead.

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the RSSI, in dBm. |

**Example**

// promise
let gattClient : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
gattClient.getRssiValue().then((data : number) => {
    console.info('rssi' + JSON.stringify(data));
})

#### ScanMode(deprecated)

Enumerates the scan modes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/jofJ4tD1SayJ4RWDu1q4Sw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6456D03F503E9E661F49718A237973E9CC4C74E9350FB32A130BE6C892E9360C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.ScanMode](../ohos-bluetoothmanager-bluetooth/document.md#scanmodedeprecated) instead.

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/JAlhvZmMQrKaqBAmBGYoPw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ABB3B3E6206E9F6ED5EA5ECC96625A98C53E3CEA6859E89FDAA88746C781384C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.BondState](../ohos-bluetoothmanager-bluetooth/document.md#bondstatedeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| BOND\_STATE\_INVALID | 0 | Invalid pairing. |
| BOND\_STATE\_BONDING | 1 | Pairing. |
| BOND\_STATE\_BONDED | 2 | Paired. |

#### SppOption(deprecated)

Defines the SPP configuration parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/JE7ab2-XSjKRTT_AUtq0Vg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=735357963A52995AC51B1392C6960E327E2465CBC29CAC2AD6408E7498E4C152)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.SppOption](../ohos-bluetoothmanager-bluetooth/document.md#sppoptiondeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| uuid | string | No | No | UUID of the SPP. |
| secure | boolean | No | No | Whether it is a secure channel. |
| type | [SppType](#spptypedeprecated) | No | No | Type of the SPP link. |

#### SppType(deprecated)

Enumerates the SPP link types.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/xz553pAfRdGgQEPYVfPwpA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D911146B1131D84B7F16A7504BE3393A2DBF684E0ED20C8E41BEF862DA9B138D)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.SppType](../ohos-bluetoothmanager-bluetooth/document.md#spptypedeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SPP\_RFCOMM | 0 | Radio frequency communication (RFCOMM) link type. |

#### GattService(deprecated)

Defines the GATT service API parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/mB8yhHR0SGOBxUoVjPmxsQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD352C43C6511410ABFDD54111D88CF8A2BA4574EC277F7AFEB6EB756EB04DA9)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.GattService](../ohos-bluetoothmanager-bluetooth/document.md#gattservicedeprecated).

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | No | No | UUID of the service, for example, **00001888-0000-1000-8000-00805f9b34fb**. |
| isPrimary | boolean | No | No | Whether the service is a primary service. The value **true** means a primary service. |
| characteristics | Array<[BLECharacteristic](#blecharacteristicdeprecated)\> | No | No | List of characteristics of the service. |
| includeServices | Array<[GattService](#gattservicedeprecated)\> | No | Yes | Services on which the service depends. |

#### BLECharacteristic(deprecated)

Defines the characteristic API parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/bwEjDuJvQ--vDjXRb2bKWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6DF7FCF0091AE31D3C9212A52E9835EB1F92E15C040B51785E541B607A5536C8)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.BLECharacteristic](../ohos-bluetoothmanager-bluetooth/document.md#blecharacteristicdeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | No | No | UUID of the service, for example, **00001888-0000-1000-8000-00805f9b34fb**. |
| characteristicUuid | string | No | No | UUID of the characteristic, for example, **00002a11-0000-1000-8000-00805f9b34fb**. |
| characteristicValue | ArrayBuffer | No | No | Binary value of the characteristic. |
| descriptors | Array<[BLEDescriptor](#bledescriptordeprecated)\> | No | No | List of descriptors of the characteristic. |

#### BLEDescriptor(deprecated)

Defines the descriptor API parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/G9SWcuE8TVOwH2qxJPkB1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=189C4EF08906D772B4293B279963D7270CDB31374BFB6343CE1A42C5116E879B)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.BLEDescriptor](../ohos-bluetoothmanager-bluetooth/document.md#bledescriptordeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | No | No | UUID of the service, for example, **00001888-0000-1000-8000-00805f9b34fb**. |
| characteristicUuid | string | No | No | UUID of the characteristic, for example, **00002a11-0000-1000-8000-00805f9b34fb**. |
| descriptorUuid | string | No | No | UUID of the descriptor, for example, **00002902-0000-1000-8000-00805f9b34fb**. |
| descriptorValue | ArrayBuffer | No | No | Binary value of the descriptor. |

#### NotifyCharacteristic(deprecated)

Defines the parameters in the notifications sent when the server characteristic value changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/QXIUE_cfRc-Pbhox0YYweA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9C8B068F6F75A53E41B0DBC1A3B1E3262C3AACBE786330EB3D688FA6156CA07)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.NotifyCharacteristic](../ohos-bluetoothmanager-bluetooth/document.md#notifycharacteristicdeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | No | No | UUID of the service, for example, **00001888-0000-1000-8000-00805f9b34fb**. |
| characteristicUuid | string | No | No | UUID of the characteristic, for example, **00002a11-0000-1000-8000-00805f9b34fb**. |
| characteristicValue | ArrayBuffer | No | No | Binary value of the characteristic. |
| confirm | boolean | No | No | Whether the notification needs to be confirmed by the remote end. For a notification, set it to **true**. In this case, the remote end must confirm the receipt of the notification. For an indication, set it to **false**. In this case, the remote end does not need to confirm the receipt of the notification. |

#### CharacteristicReadReq(deprecated)

Defines the parameters of the **CharacteristicReadReq** event received by the server.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/t1iFBhNFT9iuICRBL-fR2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E550EAF8B09122792B6E0287760DAF25C77772BF11F67527A7D88AC1A7AED57B)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.CharacteristicReadRequest](../ohos-bluetoothmanager-bluetooth/document.md#characteristicreadrequestdeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | Address of the remote device that sends the **CharacteristicReadReq** event, for example, XX:XX:XX:XX:XX:XX. |
| transId | number | No | No | Transmission ID of the read request. The response returned by the server must use the same transmission ID. |
| offset | number | No | No | Start position from which the characteristic value is read. For example, **k** means to read from the kth byte. The response returned by the server must use the same offset. |
| characteristicUuid | string | No | No | UUID of the characteristic, for example, **00002a11-0000-1000-8000-00805f9b34fb**. |
| serviceUuid | string | No | No | UUID of the service, for example, **00001888-0000-1000-8000-00805f9b34fb**. |

#### CharacteristicWriteReq(deprecated)

Defines the parameters of the **CharacteristicWriteReq** event received by the server.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/g5RbyEL0QD24C2DxC2DPOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=89D0290C3CCDDFA511661FF826D3D09E36C54C58AE855C06094AF7EBD8EEDB6E)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.CharacteristicWriteRequest](../ohos-bluetoothmanager-bluetooth/document.md#characteristicwriterequestdeprecated) instead.

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

#### DescriptorReadReq(deprecated)

Defines the parameters of the **DescriptorReadReq** event received by the server.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/JKv1R3dIQ4-gdXSg17J-5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8FA51377C81F653AC6AB314A54B03315E5EC3AA1F46992269A18FDBA254258D)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.DescriptorReadRequest](../ohos-bluetoothmanager-bluetooth/document.md#descriptorreadrequestdeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | Address of the remote device that sends the **DescriptorReadReq** event, for example, XX:XX:XX:XX:XX:XX. |
| transId | number | No | No | Transmission ID of the read request. The response returned by the server must use the same transmission ID. |
| offset | number | No | No | Start position from which the descriptor is read. For example, **k** means to read from the kth byte. The response returned by the server must use the same offset. |
| descriptorUuid | string | No | No | UUID of the descriptor, for example, **00002902-0000-1000-8000-00805f9b34fb**. |
| characteristicUuid | string | No | No | UUID of the characteristic, for example, **00002a11-0000-1000-8000-00805f9b34fb**. |
| serviceUuid | string | No | No | UUID of the service, for example, **00001888-0000-1000-8000-00805f9b34fb**. |

#### DescriptorWriteReq(deprecated)

Defines the parameters of the **DescriptorWriteReq** event received by the server.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/e8MSRfDNRBuQEuq4vrRF4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8CBFEF20936A03B33013CB3981924984A97F8E1A4D77EFDB73038E5175C44092)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.DescriptorWriteRequest](../ohos-bluetoothmanager-bluetooth/document.md#descriptorwriterequestdeprecated) instead.

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/QyMlQphnR1-B22O044VomA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=93CFEEC47291F02BC1E2BBF961F725387365F6D5174422332C55C2E9AA4DA09B)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.ServerResponse](../ohos-bluetoothmanager-bluetooth/document.md#serverresponsedeprecated) instead.

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/i31-f-0DStCkrMOvwkbNGA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0339997524A488AD91F7E2585B41CF2199055ADC61826B8FD3FB145DEB3B033D)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.BLEConnectChangedState](../ohos-bluetoothmanager-bluetooth/document.md#bleconnectchangedstatedeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | Address of the remote device, for example, XX:XX:XX:XX:XX:XX. |
| state | [ProfileConnectionState](#profileconnectionstatedeprecated) | No | No | BLE connection state. |

#### ProfileConnectionState(deprecated)

Enumerates the profile connection states.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/6qeJSyScRJmXg4mIrRHU7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A32C4AC90DB858E07AAA3EFDDEEA0B01D5DCB700EA0647C869CD28CD22881FAC)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.ProfileConnectionState](../ohos-bluetoothmanager-bluetooth/document.md#profileconnectionstatedeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| STATE\_DISCONNECTED | 0 | Disconnected. |
| STATE\_CONNECTING | 1 | Connecting. |
| STATE\_CONNECTED | 2 | Connected. |
| STATE\_DISCONNECTING | 3 | Disconnecting. |

#### ScanFilter(deprecated)

Defines the scan filter parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/ZuCjoBTwRFWz6O9gpx_18Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3FF657EA202C1540D65B4E33ABBA38E695E9FB684A921B7EBAEAB6E7C1101E3A)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.ScanFilter](../ohos-bluetoothmanager-bluetooth/document.md#scanfilterdeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | Yes | Address of the BLE device to filter, for example, XX:XX:XX:XX:XX:XX. |
| name | string | No | Yes | Name of the BLE device to filter. |
| serviceUuid | string | No | Yes | Service UUID of the device to filter, for example, **00001888-0000-1000-8000-00805f9b34fb**. |

#### ScanOptions(deprecated)

Defines the scan configuration parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/Vl0v8tAYTJKp1s-_tsKolg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CEAA5BEA8B1B6C1699F3414F7AB528C0032681047D818E1A559A37F1440EE2E6)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.ScanOptions](../ohos-bluetoothmanager-bluetooth/document.md#scanoptionsdeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| interval | number | No | Yes | Delay in reporting the scan result. The default value is **0**. |
| dutyMode | [ScanDuty](#scandutydeprecated) | No | Yes | Scan duty. The default value is SCAN\_MODE\_LOW\_POWER. |
| matchMode | [MatchMode](#matchmodedeprecated) | No | Yes | Hardware filtering match mode. The default value is **MATCH\_MODE\_AGGRESSIVE**. |

#### ScanDuty(deprecated)

Enumerates the scan modes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/fLhmLchBQ-m87AEBpzIi-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CBA83E511AB1E8C6FC028832840A926808D980293AA8E0437114B18350A96877)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.ScanDuty](../ohos-bluetoothmanager-bluetooth/document.md#scandutydeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SCAN\_MODE\_LOW\_POWER | 0 | Low-power mode, which is the default value. |
| SCAN\_MODE\_BALANCED | 1 | Balanced mode. |
| SCAN\_MODE\_LOW\_LATENCY | 2 | Low-latency mode. |

#### MatchMode(deprecated)

Enumerates the hardware match modes of BLE scan filters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/aSAACesKRGGbx1UwVu0xFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=967883B2A0019011CEEEFC4C953440E19A4AF47E88DBA6321F757FC711FA6600)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.MatchMode](../ohos-bluetoothmanager-bluetooth/document.md#matchmodedeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| MATCH\_MODE\_AGGRESSIVE | 1 | Hardware reports the scan result with a lower threshold of signal strength and few number of matches in a duration. This is the default value. |
| MATCH\_MODE\_STICKY | 2 | Hardware reports the scan result with a higher threshold of signal strength and sightings. |

#### ScanResult(deprecated)

Defines the scan result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/zgus_4QcR8Wa4jk203XUew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02BA5590EFACAB737456F8D85E5EA360E989B297DA905C43C2679EEA3E74D5E9)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.ScanResult](../ohos-bluetoothmanager-bluetooth/document.md#scanresultdeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | Address of the device discovered, for example, XX:XX:XX:XX:XX:XX. |
| rssi | number | No | No | RSSI of the device. |
| data | ArrayBuffer | No | No | Advertisement packets sent by the device. |

#### BluetoothState(deprecated)

Enumerates the Bluetooth states.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/EZtfzrH8QSuV70TfcuSrVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3DF4795E11072F8359AEF9D5A4FC3F6B6E9E55DB8F0EF1D8F6407A8B2F88EB45)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.BluetoothState](../ohos-bluetoothmanager-bluetooth/document.md#bluetoothstatedeprecated) instead.

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/b13czRwlQ1-CEq0yirzHHg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A49C503D5425428FB209545B5D6EB1FBA448E7AEF67FF21BB196C026F91138E2)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.AdvertiseSetting](../ohos-bluetoothmanager-bluetooth/document.md#advertisesettingdeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| interval | number | No | Yes | Interval for BLE advertising. The minimum value is **32** slots (20 ms). The maximum value is **16384** slots. The default value is **1600** slots (1s). |
| txPower | number | No | Yes | Transmit power, in dBm. The value range is -127 to 1. The default value is **\-7**. |
| connectable | boolean | No | Yes | Whether the advertisement is connectable. The default value is **true**. |

#### AdvertiseData(deprecated)

Defines the content of a BLE advertisement packet.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/Ipz5xaUASfiusQJE4pPDeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D34CBAFDAAB28664C5371CDD18C4196139C0FF84088ECDD12C9FEFAEDFCFB10E)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.AdvertiseData](../ohos-bluetoothmanager-bluetooth/document.md#advertisedatadeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuids | Array<string> | No | No | List of service UUIDs to broadcast. |
| manufactureData | Array<[ManufactureData](#manufacturedatadeprecated)\> | No | No | List of manufacturers to broadcast. |
| serviceData | Array<[ServiceData](#servicedatadeprecated)\> | No | No | List of service data to broadcast. |

#### ManufactureData(deprecated)

Defines the content of a BLE advertisement packet.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/KJr6F_2-QUStoyq_jKwbog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF2C0325A703E3228A7BFDD9D3167B39E8D833AE0845AD1C67BC15EBF3936C15)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.ManufactureData](../ohos-bluetoothmanager-bluetooth/document.md#manufacturedatadeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| manufactureId | number | No | No | Manufacturer ID allocated by the Bluetooth SIG. |
| manufactureValue | ArrayBuffer | No | No | Manufacturer data. |

#### ServiceData(deprecated)

Defines the service data contained in an advertisement packet.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/oaXuZ1xpQnGofwPbCW5lbg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4EC12178E5087F12FEF5250B82543374A1D3A98464EAB9D540CE2D6B3EDCCCF6)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [bluetoothManager.ServiceData](../ohos-bluetoothmanager-bluetooth/document.md#servicedatadeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | No | No | Service UUID. |
| serviceValue | ArrayBuffer | No | No | Service data. |

#### PinRequiredParam(deprecated)

Defines the pairing request parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/3c-1hxbVR8uIYnaD-PVzRg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=970E96D2D373640385EE47430A32B90A59E9C8F3363CE6AEF669CC59C7A327CD)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.PinRequiredParam](../ohos-bluetoothmanager-bluetooth/document.md#pinrequiredparamdeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | ID of the device to pair. |
| pinCode | string | No | No | Key for the device pairing. |

#### BondStateParam(deprecated)

Defines the pairing state parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/Y_tWSOFxQbGx4Hhty9HU5A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=187D89526F2AED4BF8B05EBE4FB669746FDF401E68D2116CCCD1669A0D07218D)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.BondStateParam](../ohos-bluetoothmanager-bluetooth/document.md#bondstateparamdeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | ID of the device to pair. |
| state | BondState | No | No | State of the device. |

#### StateChangeParam(deprecated)

Defines the profile state change parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/j586TCV5R7-HTxMnzcbmtg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84459419945D3DDC0976E9810B355090F42F0BCA1FF7E28D56CF7EB7C48E929A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.StateChangeParam](../ohos-bluetoothmanager-bluetooth/document.md#statechangeparamdeprecated).

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | Address of a Bluetooth device. |
| state | [ProfileConnectionState](#profileconnectionstatedeprecated) | No | No | Profile connection state of the device. |

#### DeviceClass(deprecated)

Defines the class of a Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/haqP5i-wR-OifBXQuh-x7w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E1D691B68B80310CE20A09CF712FFEB6495D39DB593F30A565333EF7D31E8D0)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.DeviceClass](../ohos-bluetoothmanager-bluetooth/document.md#deviceclassdeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| majorClass | [MajorClass](#majorclassdeprecated) | No | No | Major classes of Bluetooth devices. |
| majorMinorClass | [MajorMinorClass](#majorminorclassdeprecated) | No | No | Major and minor classes of Bluetooth devices. |
| classOfDevice | number | No | No | Class of the device. |

#### MajorClass(deprecated)

Enumerates the major classes of Bluetooth devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/qEmaxMfdTc2tGSZbjSQb9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E13192C3AC78896D1D5079CF1F493473A7FB512348D7D40B3B35EF84716E644)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.MajorClass](../ohos-bluetoothmanager-bluetooth/document.md#majorclassdeprecated) instead.

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/IUabsxqgRguQyBNPVk6GMA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F479A2D3D0BFDEA8A169574892EEA359559762445781B5C0EFE8B3E7975F05AE)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.MajorMinorClass](../ohos-bluetoothmanager-bluetooth/document.md#majorminorclassdeprecated) instead.

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
| HEALTH\_PEAK\_FLOW\_MOITOR | 0x0928 | Hygrometer. |
| HEALTH\_MEDICATION\_MONITOR | 0x092C | Medication monitor. |
| HEALTH\_KNEE\_PROSTHESIS | 0x0930 | Prosthetic knee. |
| HEALTH\_ANKLE\_PROSTHESIS | 0x0934 | Prosthetic ankle. |
| HEALTH\_GENERIC\_HEALTH\_MANAGER | 0x0938 | Generic health management device. |
| HEALTH\_PERSONAL\_MOBILITY\_DEVICE | 0x093C | Personal mobility device. |

#### PlayingState(deprecated)

Enumerates the A2DP playing states.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/8LxTs9XkSx6Uj4M836asjg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7CACAB95A8A8B6FEAB01E8BB6C7E0A5F7B7D6AB6EF156EFBDC710F38491893EC)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.PlayingState](../ohos-bluetoothmanager-bluetooth/document.md#playingstatedeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| STATE\_NOT\_PLAYING | 0x0000 | Not playing. |
| STATE\_PLAYING | 0x0001 | Playing. |

#### ProfileId(deprecated)

Enumerates the Bluetooth profiles. API version 9 is added with **PROFILE\_HID\_HOST** and **PROFILE\_PAN\_NETWORK**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/ofkJ0lNPTiWMM4zzl7PvIA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE795068E422862D36A4478E2336D57F822CC440F98709E5E91AD9D68E5889E4)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [bluetoothManager.ProfileId](../ohos-bluetoothmanager-bluetooth/document.md#profileiddeprecated) instead.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| PROFILE\_A2DP\_SOURCE | 1 | A2DP profile. |
| PROFILE\_HANDS\_FREE\_AUDIO\_GATEWAY | 4 | HFP profile. |
