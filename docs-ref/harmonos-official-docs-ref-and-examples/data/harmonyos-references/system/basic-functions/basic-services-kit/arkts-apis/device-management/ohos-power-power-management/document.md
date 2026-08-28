# @ohos.power (Power Management)

The **power** module provides APIs for rebooting and shutting down the system, as well as querying the screen status. You can use these APIs to obtain the device activity status, power mode, and screen on/off status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/PuZ2zXS5RLSmVQpoBYheWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC90152176915E399C95CD8031F0CD472D51DE68DFFB67F9CFEB026CED8E36E3)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import {power} from '@kit.BasicServicesKit';

#### power.isActive9+

isActive(): boolean

Checks whether the current device is active.

-   A device with a screen is active when the screen is on and inactive when the screen is off.
-   A device without a screen is active when it exits the sleep mode and inactive when it enters the sleep mode.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

**Returns**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the device is active; returns **false** otherwise. |

**Example**

let isActive = power.isActive();
console.info('power is active: ' + isActive);

#### power.rebootDevice(deprecated)

rebootDevice(reason: string): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/1R3Ks4RMTOyhI_U53iE8Bg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE5D087AE491BCCB72D1108B6ABC00DA5458B52306996ACF39A4ED15A74EE77C)

This API is supported since API version 7 and deprecated since API version 9.. The substitute API is available only for system applications.

Reboots a device.

**Required permissions**: ohos.permission.REBOOT (available only for system applications)

**System capability**: SystemCapability.PowerManager.PowerManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| reason | string | Yes | Reason for system reboot. |

**Example**

power.rebootDevice('reboot\_test');

#### power.getPowerMode9+

getPowerMode(): DevicePowerMode

Obtains the power mode of this device.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

**Returns**

| Type | Description |
| :-- | :-- |
| [DevicePowerMode](#devicepowermode9) | Power mode. |

**Example**

let mode = power.getPowerMode();
console.info('power mode: ' + mode);

#### power.isStandby10+

isStandby(): boolean

Checks whether the device is in standby mode.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

**Returns**

| Type | Description |
| :-- | :-- |
| boolean | The value **true** indicates that the device is in standby mode, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Power Manager Error Codes](../../../error-codes/power-manager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 4900101 | Failed to connect to the service. |

**Example**

try {
    let isStandby = power.isStandby();
    console.info('device is in standby: ' + isStandby);
} catch(err) {
    console.error('check isStandby failed, err: ' + err);
}

#### power.isScreenOn(deprecated)

isScreenOn(callback: AsyncCallback<boolean>): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/lmd_hbB8SwqWzJU17hiiKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EDD574C24F220C29B610FD0535883BCD3501C8BDE4C744E7877142E75949A3AA)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [power.isActive](#powerisactive9) instead.

Checks the screen status of the current device. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the screen status obtained, where the value **true** indicates on and the value **false** indicates off. Otherwise, **err** is an error object. |

**Example**

power.isScreenOn((err: Error, data: boolean) => {
    if (typeof err === 'undefined') {
        console.info('screen on status is ' + data);
    } else {
        console.error('check screen status failed, err: ' + err);
    }
})

#### power.isScreenOn(deprecated)

isScreenOn(): Promise<boolean>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/K3-NFv9sR4uzpc1Skjxiug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9ACCB2C427818BAC08D387B78CC9F3365E254EA664F0A1E592E518655FEBBD4E)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [power.isActive](#powerisactive9) instead.

Checks the screen status of the current device. This API uses a promise to return the result.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

**Returns**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the screen is on, and the value **false** indicates the opposite. |

**Example**

power.isScreenOn()
.then((data: boolean) => {
    console.info('screen on status is ' + data);
})
.catch((err: Error) => {
    console.error('check screen status failed, err: ' + err);
})

#### DevicePowerMode9+

Enumerates power modes.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| MODE\_NORMAL | 600 | Standard mode. It is the default value. |
| MODE\_POWER\_SAVE | 601 | Power saving mode. |
| MODE\_PERFORMANCE | 602 | Performance mode. |
| MODE\_EXTREME\_POWER\_SAVE | 603 | Ultra power saving mode. |
| MODE\_CUSTOM\_POWER\_SAVE20+ | 650 | Custom power saving mode. |

#### PowerKeyFilteringStrategy21+

Enumerates the power key filtering strategies.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| DISABLE\_LONG\_PRESS\_FILTERING | 0 | Disables the power key filtering strategy. This is the default value. |
| LONG\_PRESS\_FILTERING\_ONCE | 1 | Filters the long-press event of the current power key once. |
