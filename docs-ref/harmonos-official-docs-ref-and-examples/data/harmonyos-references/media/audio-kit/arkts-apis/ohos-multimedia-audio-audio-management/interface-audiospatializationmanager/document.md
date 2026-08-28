# Interface (AudioSpatializationManager)

This interface implements spatial audio management.

Before calling any API in AudioSpatializationManager, you must use [getSpatializationManager](../interface-audiomanager/document.md#getspatializationmanager18) to obtain an AudioSpatializationManager instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/5iaazbFQQVWhmeG5vjQTGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B7624C99C7DD7612BBB42BB870D56658E42EB1D0BB972CC5B36E9AB0B838503)

-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 18.

#### Modules to Import

import { audio } from '@kit.AudioKit';

#### isSpatializationEnabledForCurrentDevice18+

isSpatializationEnabledForCurrentDevice(): boolean

Checks whether spatial audio rendering is enabled for the current device. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Spatialization

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether spatial audio rendering is enabled. **true** if enabled, **false** otherwise. |

**Example**

import { audio } from '@kit.AudioKit';

let isSpatializationEnabledForCurrentDevice: boolean = audioSpatializationManager.isSpatializationEnabledForCurrentDevice();
console.info(\`AudioSpatializationManager isSpatializationEnabledForCurrentDevice: ${isSpatializationEnabledForCurrentDevice}\`);

#### on('spatializationEnabledChangeForCurrentDevice')18+

on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void

Subscribes to the spatial audio rendering status change event of the current device. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Spatialization

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'spatializationEnabledChangeForCurrentDevice'** is triggered when the spatial audio rendering status is changed. |
| callback | Callback<boolean> | Yes | Callback used to return the result, indicating whether spatial audio rendering is enabled. **true** if enabled, **false** otherwise. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

import { audio } from '@kit.AudioKit';

audioSpatializationManager.on('spatializationEnabledChangeForCurrentDevice', (isSpatializationEnabledForCurrentDevice: boolean) => {
  console.info(\`isSpatializationEnabledForCurrentDevice: ${isSpatializationEnabledForCurrentDevice}\`);
});

#### off('spatializationEnabledChangeForCurrentDevice')18+

off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void

Unsubscribes from the spatial audio rendering status change event of the current device. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Spatialization

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'spatializationEnabledChangeForCurrentDevice'** is triggered when the spatial audio rendering status is changed. |
| callback | Callback<boolean> | No | Callback used to return the result, indicating whether spatial audio rendering is enabled. **true** if enabled, **false** otherwise. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

import { audio } from '@kit.AudioKit';
audioSpatializationManager.off('spatializationEnabledChangeForCurrentDevice');
