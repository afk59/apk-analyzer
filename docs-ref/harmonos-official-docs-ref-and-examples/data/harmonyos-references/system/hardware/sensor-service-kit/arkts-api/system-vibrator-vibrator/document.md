# @system.vibrator (Vibrator)

The **Vibrator** module provides APIs for controlling LED lights and vibrators. You can use the APIs to query the LED light list, vibrator list, and vibration effect, and turn on or off the LED light and the vibrator.

Misc devices refer to LED lights and vibrators on devices. LED lights are mainly used for indication (for example, indicating the charging state) and blinking (such as tri-colored lights). Vibrators are mainly used in scenarios such as the alarm clock, power-on/off, and incoming call vibration.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/-FmlqSswQQawSIrKPBkshA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3ECF0011C9EC966E391EE41B3A8C1266F1E2E7D641D37B550C01BABAE7562F1D)

-   Module maintenance policy:
    -   For lite wearables, this module is constantly maintained and available.
    -   For other device types, this module is no longer maintained since API version 8, and you are advised to use the new [@ohos.vibrator](../ohos-vibrator-vibrator/document.md) module.
-   The initial APIs of this module are supported since API version 3. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   This module requires hardware support and can only be debugged on real devices.

#### Modules to Import

import { Vibrator } from '@kit.SensorServiceKit';

#### Vibrator.vibrate

vibrate(options?: VibrateOptions): void

Triggers device vibration.

Except for lite wearables, you are advised to use [vibrator.startVibration()](../ohos-vibrator-vibrator/document.md#vibratorstartvibration9) since API version 8.

**Required permissions**: ohos.permission.VIBRATE

**System capability**: SystemCapability.Sensors.MiscDevice.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [VibrateOptions](#vibrateoptions) | No | Vibration options. |

**Example**

import { Vibrator, VibrateOptions } from '@kit.SensorServiceKit';

let vibrateOptions: VibrateOptions = {
  mode: 'short',
  success: () => {
    console.info('Succeed in vibrating');
  },
  fail: (data: string, code: number) => {
    console.error(\`Failed to vibrate. Data: ${data}, code: ${code}\`);
  },
  complete: () => {
    console.info('completed in vibrating');
  }
};
Vibrator.vibrate(vibrateOptions);

#### VibrateOptions

Defines the vibration options.

**Required permissions**: ohos.permission.VIBRATE

**System capability**: SystemCapability.Sensors.MiscDevice.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | string | No | Vibration mode. The value **long** indicates long vibration, and **short** indicates short vibration. The default value is **long**. |
| success | Function | No | Called when the vibrator data changes. |
| fail | Function | No | Called when the API call fails. |
| complete | Function | No | Called when the API call is complete. |
