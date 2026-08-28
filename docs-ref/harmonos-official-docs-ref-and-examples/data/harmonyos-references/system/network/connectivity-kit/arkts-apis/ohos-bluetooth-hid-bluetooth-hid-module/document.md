# @ohos.bluetooth.hid (Bluetooth HID Module)

The **hid** module provides Bluetooth capabilities based on Bluetooth Classic's [Human Interface Device Profile (HID)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#hid), such as obtaining the Bluetooth connection status. All the APIs in this module are also accessible to devices using Bluetooth Low Energy (BLE)'s [HID over GATT Profile (HOGP)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#hogp).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/NbS736_cSW-HsP03enKCcQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0382C6B4457531ECE5F726299019496E806D4D9F57913B49AC1C5424BD2A77B3)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { hid } from '@kit.ConnectivityKit';

#### BaseProfile

type BaseProfile = baseProfile.BaseProfile

**BaseProfile** class, which provides public capabilities such as obtaining the connection status and listening for connection status changes.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Type | Description |
| :-- | :-- |
| [baseProfile.BaseProfile](../ohos-bluetooth-baseprofile-bluetooth-baseprofile-module/document.md#baseprofile) | **BaseProfile** API definition. |

#### hid.createHidHostProfile

createHidHostProfile(): HidHostProfile

Creates a Bluetooth [HID host](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#hid-host) instance. Through this instance, you can use the local device as the HID host and implement functions such as obtaining the Bluetooth HID connection status.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| HidHostProfile | 
HID host instance.

\- The **HidHostProfile** class is inherited from [BaseProfile](#baseprofile). Therefore, you can use the APIs in its parent class.

\- The counterpart of the HID host role is the [HID device](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#hid-device) role.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let hidHostProfile = hid.createHidHostProfile();
    console.info('hidHost success');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
