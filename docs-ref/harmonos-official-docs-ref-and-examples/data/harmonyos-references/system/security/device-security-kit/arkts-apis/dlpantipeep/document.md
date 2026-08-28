# DlpAntiPeep

This module provides APIs related to the peeping status. Apps can protect user privacy based on the peeping status, for example, display a system-level overlay to mask the window, disable personalized recommendations, and hide sensitive information such as browsing records, payment records, and favorites records when the phone is being viewed by someone else besides the owner.

**Start version**: 6.0.0(20)

#### Module Import

import { dlpAntiPeep } from '@kit.DeviceSecurityKit';

#### DlpAntiPeepStatus

Enumerates the peeping status.

**System capability**: SystemCapability.Security.DlpAntiPeep

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

PASS

 | 

0

 | 

No one is peeping at the screen of the current device.

 |
| 

HIDE

 | 

1

 | 

Someone other than the owner is peeping at the screen of the device.

 |

#### isDlpAntiPeepSwitchOn

isDlpAntiPeepSwitchOn(): Promise<boolean>

Checks whether screen privacy has been enabled for the current app. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.DLP\_GET\_HIDE\_STATUS

**System capability**: SystemCapability.Security.DlpAntiPeep

**Start version**: 6.0.0(20)

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<boolean>

 | 

Promise used to return the result, indicating whether screen privacy has been enabled for the current app. The value **true** indicates that the function is enabled, and **false** indicates that the function is disabled. The default value is **false**.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/dlpantipeep/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

801

 | 

Capability not supported. Function on can not work correctly due to limited device capabilities.

 |
| 

1020600001

 | 

Internal error.

 |

**Example:**

import { dlpAntiPeep } from '@kit.DeviceSecurityKit';

try {
  let result = await dlpAntiPeep.isDlpAntiPeepSwitchOn();
  console.info(\`isDlpAntiPeepSwitchOnsuccess.\`);
} catch (err) {
  console.error(\`isDlpAntiPeepSwitchOnfailed.\`);
}

#### on("dlpAntiPeep")

on(type: 'dlpAntiPeep', callback: Callback<DlpAntiPeepStatus>): void

Subscribes to the screen privacy notification. This API returns the result asynchronously through a callback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/7kOFgRmQTjCbV3BcI8yltQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2AEE5E0CAB9DE32F165ABE70F3E05E3E4B4279E396FA8B6E8B3589D2A24CC83C)

Call this API after the [development prerequisites](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-dlpantipeep#section128161223011) are met, ensuring that the screen privacy callback can be triggered.

**Required permission**: ohos.permission.DLP\_GET\_HIDE\_STATUS

**System capability**: SystemCapability.Security.DlpAntiPeep

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

'dlpAntiPeep'

 | 

Yes

 | 

Event to be subscribed to, which has a fixed value of **'dlpAntiPeep'**.

 |
| 

callback

 | 

Callback<[DlpAntiPeepStatus](#section11705111513)\>

 | 

Yes

 | 

Callback function used to return the result.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/dlpantipeep/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

801

 | 

Capability not supported.

 |
| 

1020600001

 | 

Internal error.

 |

**Example:**

import { dlpAntiPeep } from '@kit.DeviceSecurityKit';

try {
  dlpAntiPeep.on('dlpAntiPeep', (dlpAntiPeepStatus: dlpAntiPeep.DlpAntiPeepStatus) => {
    console.info(\`dlpAntiPeep.on success.\`);
  });
} catch (error) {
  console.error(\`dlpAntiPeep.on failed.\`);
}

#### off("dlpAntiPeep")

off(type: 'dlpAntiPeep', callback?: Callback<DlpAntiPeepStatus>): void

Unsubscribes from the screen privacy notification. This API returns the result asynchronously through a callback.

**Required permission**: ohos.permission.DLP\_GET\_HIDE\_STATUS

**System capability**: SystemCapability.Security.DlpAntiPeep

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

'dlpAntiPeep'

 | 

Yes

 | 

Event to be unsubscribed from, which has a fixed value of **'dlpAntiPeep'**.

 |
| 

callback

 | 

Callback<[DlpAntiPeepStatus](../arkts-api-error-codes/dlpantipeep/document.md)\>

 | 

No

 | 

Callback function for receiving screen privacy notifications. If a callback is passed, the subscription to this callback is canceled. If no callback is passed, subscriptions to all callbacks are canceled.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/dlpantipeep/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

801

 | 

Capability not supported.

 |
| 

1020600001

 | 

Internal error.

 |

**Example:**

import { dlpAntiPeep } from '@kit.DeviceSecurityKit';

try {
  dlpAntiPeep.off('dlpAntiPeep', (dlpAntiPeepStatus: dlpAntiPeep.DlpAntiPeepStatus) => {
    console.info(\`dlpAntiPeep.off success.\`);
  });
} catch (error) {
  console.error(\`dlpAntiPeep.off failed.\`);
}

#### getDlpAntiPeepInfo

getDlpAntiPeepInfo(): DlpAntiPeepStatus

Obtains the peeping status of the current app.

**Required permission**: ohos.permission.DLP\_GET\_HIDE\_STATUS

**System capability**: SystemCapability.Security.DlpAntiPeep

**Start version**: 6.0.0(20)

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DlpAntiPeepStatus](#section11705111513)

 | 

Peeping status.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/dlpantipeep/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

801

 | 

Capability not supported. Function getDlpHideInfo can not work correctly due to limited device capabilities.

 |
| 

1020600001

 | 

Internal error.

 |

**Example:**

import { dlpAntiPeep } from '@kit.DeviceSecurityKit';

try {
  let dlpAntiPeepStatus = dlpAntiPeep.getDlpAntiPeepInfo();
  console.info(\`getDlpHideInfo success.\`);
} catch (err) {
  console.error(\`getDlpHideInfo failed.\`);
}

#### passDlpAntiPeepInfo

passDlpAntiPeepInfo(): void

Sets the peeping status of the current app to non-peeping. Then the peeping status returned by the [on("dlpAntiPeep")](#section1794633020274) API's callback function and the peeping status obtained by the [getDlpAntiPeepInfo](#section11694411559) API are both non-peeping.

If an app no longer needs to receive the peeping status within its lifecycle, it can directly call the [off("dlpAntiPeep")](#section142181149107) API to unsubscribe from the screen privacy notification. If the app wants to receive the non-peeping state in scenarios where screen privacy protection can be bypassed, it can call the **passDlpAntiPeepInfo** API to set the peeping status to non-peeping.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/uneE2JKbRiKqpajsPvFVMA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2974CB5F333E84976164583EE3B24B2816A4B7B89838070682112931624102A3)

This API can be called only after the [development prerequisites](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-dlpantipeep#section128161223011) are met and the [on("dlpAntiPeep")](#section1794633020274) API is called. It can be used to set the peeping status to non-peeping through a callback. Then the non-peeping state remains within the app's subscription lifecycle until the app exits or the device screen is locked.

**Required permission**: ohos.permission.DLP\_GET\_HIDE\_STATUS

**System capability**: SystemCapability.Security.DlpAntiPeep

**Start version**: 6.0.0(20)

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/dlpantipeep/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

801

 | 

Capability not supported. Function passDlpHideInfo can not work correctly due to limited device capabilities.

 |
| 

1020600001

 | 

Internal error.

 |

**Example:**

import { dlpAntiPeep } from '@kit.DeviceSecurityKit';

try {
  dlpAntiPeep.passDlpAntiPeepInfo();
  console.info(\`passDlpAntiPeepInfo success.\`);
} catch (err) {
  console.error(\`passDlpAntiPeepInfo failed.\`);
}

#### setAntiPeepMaskLayer

setAntiPeepMaskLayer(windowId: number): Promise<void>

Sets a system-level overlay for a specified window. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/NtoAua-MRH-SGpemKeSnlQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=47B38712F89281FA45DF1B565FCBB3E260719276F2971B2E85FECCDC9004737E)

Once called, this API will display an overlay to mask the app window. You are advised to call this API only once when the peeking state is detected, for frequent calls may affect user experience.

**Required permission**: ohos.permission.DLP\_GET\_HIDE\_STATUS

**System capability**: SystemCapability.Security.DlpAntiPeep

**Start version**: 6.0.1(21)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

windowId

 | 

number

 | 

Yes

 | 

ID of the window to be masked for privacy protection. The value must be a positive integer.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/dlpantipeep/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

801

 | 

Capability not supported.function setAntiPeepMaskLayer can not work correctly due to limited device capabilities.

 |
| 

1020600001

 | 

Internal error.

 |
| 

1020600002

 | 

The antipeep function is not enabled.

 |
| 

1020600003

 | 

The protected application is not displayed on the screen.

 |

**Example:**

import { dlpAntiPeep } from '@kit.DeviceSecurityKit'; 
import { common } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let windowClass: window.Window;
try {
  windowClass = await window.getLastWindow(context);
} catch(err) {
  console.error('error', err.code, err.message);
  return;
}
let windowId: number;
try {
  windowId = windowClass.getWindowProperties().id;
} catch (err) {
  console.error('Failed to get window properties:', err);
  return;
}
try {
  await dlpAntiPeep.setAntiPeepMaskLayer(windowId);
} catch (err) {
  console.error(\`setAntiPeepMaskLayer failed. error code is ${JSON.stringify(err)}\`);
}
