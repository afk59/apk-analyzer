# @ohos.multimodalAwareness.deviceStatus (Device Status Awareness)

The **deviceStatus** module provides the device status awareness functionality.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/XHH_aVubT06cCW9ojpwPmg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062410Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0B3621574D55548C1E1AD4412CCDB35A52A8703E9EF4D873F8007D498C96920)

The initial APIs of this module are supported since API version 18. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { deviceStatus } from '@kit.MultimodalAwarenessKit';

#### SteadyStandingStatus

Defines the steady standing state (that is, stand mode).

A device enters stand mode when it is stationary, and its screen is at an angle between 45 and 135 degrees relative to the horizontal plane. For foldable smartphones, the device must be in a folded state or fully unfolded state.

**System capability**: SystemCapability.MultimodalAwareness.DeviceStatus

| Name | Value | Description |
| :-- | :-- | :-- |
| STATUS\_EXIT | 0 | Exit of the stand mode. |
| STATUS\_ENTER | 1 | Entry to the stand mode. |

#### deviceStatus.on('steadyStandingDetect')

on(type: 'steadyStandingDetect', callback: Callback<SteadyStandingStatus>): void

Subscribes to steady standing state events.

**System capability**: SystemCapability.MultimodalAwareness.DeviceStatus

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. This field has a fixed value of **steadyStandingDetect**. |
| callback | Callback<[SteadyStandingStatus](#steadystandingstatus)\> | Yes | Callback used to return the steady standing state of the device. |

**Error codes**

For details about the error codes, see [Device Status Awareness Error Codes](../../error-codes/device-status-awareness-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Function can not work correctly due to limited device capabilities. |
| 32500001 | Service exception. |
| 32500002 | Subscription failed. |

**Example**

try {
   deviceStatus.on('steadyStandingDetect', (data:deviceStatus.SteadyStandingStatus) => {
      console.info('succeed to get status, now status = ' + data);
   });
} catch (err) {
   console.error('on failed, err = ' + err);
}

#### deviceStatus.off('steadyStandingDetect')

off(type: 'steadyStandingDetect', callback?: Callback<SteadyStandingStatus>): void

Unsubscribes from steady standing state events.

**System capability**: SystemCapability.MultimodalAwareness.DeviceStatus

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. This field has a fixed value of **steadyStandingDetect**. |
| callback | Callback<[SteadyStandingStatus](#steadystandingstatus)\> | No | Callback used to return the steady standing state of the device. |

**Error codes**

For details about the error codes, see [Device Status Awareness Error Codes](../../error-codes/device-status-awareness-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Function can not work correctly due to limited device capabilities. |
| 32500001 | Service exception. |
| 32500003 | Unsubscription failed. |

**Example**

Example 1: Unsubscribe from all callbacks of steady standing state change events.

try {
   deviceStatus.off('steadyStandingDetect');
} catch (err) {
   console.error('off failed, err = ' + err);
}

Example 2: Unsubscribe from a specific callback of steady standing state change events.

// Define the callback variable.
let callback : Callback<deviceStatus.SteadyStandingStatus> = (data : deviceStatus. SteadyStandingStatus) => {
   console.info('succeed to get status, now status = ' + data);
};
// Subscribe to a specific callback of steady standing state change events.
try {
   deviceStatus.on('steadyStandingDetect', callback);
} catch (err) {
   console.error('on failed, err = ' + err);
}
// Unsubscribe from the specific callback of steady standing state change events.
try {
   deviceStatus.off('steadyStandingDetect', callback);
} catch (err) {
   console.error('off failed, err = ' + err);
}
