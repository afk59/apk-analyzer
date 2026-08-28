# @system.battery (Battery Information)

The **battery** module allows you to query the charging status and remaining power of a device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/sGsEa0xhQPKFarbYihifYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75052C1362F97ACD12285592EE7B7D73F7D052BBD346C41FAB4C7AB294E81B53)

-   The APIs of this module are no longer maintained since API version 6. You are advised to use [@ohos.batteryInfo](../../device-management/ohos-batteryinfo-battery-information/document.md) instead.
-   The initial APIs of this module are supported since API version 3. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import {Battery, BatteryResponse } from '@kit.BasicServicesKit';

#### Battery.getStatus(deprecated)

getStatus(options?: GetStatusOptions): void;

Obtains the current charging state and battery level.

**System capability**: SystemCapability.PowerManager.BatteryManager.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [GetStatusOptions](#getstatusoptionsdeprecated) | No | Object that contains the API calling result. This parameter is optional and is left blank by default. |

**Example**

Battery.getStatus({
    success: (data: BatteryResponse) => {
        console.info('success get battery level:' + data.level);
    },
    fail: (data: string, code: number) => {
        console.error('fail to get battery level code:' + code + ', data: ' + data);
    }
});

#### GetStatusOptions(deprecated)

Object that contains the API calling result.

**System capability**: SystemCapability.PowerManager.BatteryManager.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| success | (data: [BatteryResponse](#batteryresponsedeprecated)) => void | No | Called when an API call is successful. **data** is a return value of the [BatteryResponse](#batteryresponsedeprecated) type. |
| fail | (data: string, code: number) => void | No | Called when an API call has failed. **data** indicates the error information, and **code** indicates the error code. |
| complete | () => void | No | Called when an API call is complete. |

#### BatteryResponse(deprecated)

Defines a response that returns the charging status and remaining power of the device.

**System capability**: SystemCapability.PowerManager.BatteryManager.Lite

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| charging | boolean | No | No | 
Whether the battery is being charged. The value **true** indicates that the battery is being changed; **false** indicates the opposite. The default value is **false**.

Note: This API is no longer maintained since API version 6 except for lite wearables. You are advised to use [batteryInfo.chargingStatus](../../device-management/ohos-batteryinfo-battery-information/document.md#constants) instead.

 |
| level | number | No | No | 

Current battery level, which ranges from **0.00** to **1.00**.

Note: This API is no longer maintained since API version 6 except for lite wearables. You are advised to use [batteryInfo.batterySOC](../../device-management/ohos-batteryinfo-battery-information/document.md#constants) instead.

 |
