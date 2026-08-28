# @ohos.screenLock (Screen Lock)

The **screenlock** module is a system module in HarmonyOS. It provides APIs for screen lock applications to subscribe to screen lock status changes as well as callbacks for them to receive the results. It also provides APIs for third-party applications to unlock the screen, obtain the screen locked status, and check whether a lock screen password has been set.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/7_s0EPAsSDy64V6ldzE0vw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=194CD5EA1899FBF1DCFD6409140CE0EEF64520E0F05DC9F3C0ED5E36EF38F4CD)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import screenLock from '@ohos.screenLock';

#### screenLock.isScreenLocked(deprecated)

isScreenLocked(callback: AsyncCallback<boolean>): void

Checks whether the screen is locked. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/CrqJB_lZSFeSblN9GI6T7w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2DCC14F5D958A3A0C4B5411E461970040E6697D0C17888718DD494ACF364AB51)

This API is supported since API version 7 and deprecated since API version 9. The substitute API is available only for system applications.

**System capability**: SystemCapability.MiscServices.ScreenLock

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means that the screen is locked, and **false** means the opposite. |

**Example**

import { BusinessError } from '@ohos.base';

screenLock.isScreenLocked((err: BusinessError, data: Boolean)=>{
  if (err) {
    console.error(\`Failed to obtain whether the screen is locked, Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in Obtaining whether the screen is locked. result: ${data}\`);
});

#### screenLock.isScreenLocked(deprecated)

isScreenLocked(): Promise<boolean>

Checks whether the screen is locked. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/I9NC23QXQJ-W7Vx-EWSfGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D0457670B498169EF54DAAD68C0BE5535552BBB090F1361211CD191ABD84446)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.ScreenLock

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the screen is locked, and **false** means the opposite. |

**Example**

import { BusinessError } from '@ohos.base';

screenLock.isScreenLocked().then((data: Boolean) => {
  console.info(\`Succeeded in Obtaining whether the screen is locked. result: ${data}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to obtain whether the screen is locked, Code: ${err.code}, message: ${err.message}\`);
});

#### screenLock.isSecureMode(deprecated)

isSecureMode(callback: AsyncCallback<boolean>): void

Checks whether the device is in secure mode. When the device is in secure mode, its screen requires a password, unlock pattern, or other user credentials to unlock. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/CLM1R7o3SwizbKMHO5CLbA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C5EDF4627C6996E7F67A9BBBBA2653D1B55E703A2227E8C60E3C08DCAB33A5BE)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.ScreenLock

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means that the device is in secure mode, and **false** means the opposite. |

**Example**

import { BusinessError } from '@ohos.base';

screenLock.isSecureMode((err: BusinessError, data: Boolean)=>{
  if (err) {
    console.error(\`Failed to obtain whether the device is in secure mode, Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in Obtaining whether the device is in secure mode. result: ${data}\`);
});

#### screenLock.isSecureMode(deprecated)

isSecureMode(): Promise<boolean>

Checks whether the device is in secure mode. When the device is in secure mode, its screen requires a password, unlock pattern, or other user credentials to unlock. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/CpsLLdFgQEGccGLE4KgBNw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A9CC9E4DC5550B321D03BDB1159E16D3AF4F08D4D39C68F77B21A933553F289)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.ScreenLock

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the device is in secure mode, and **false** means the opposite. |

**Example**

import { BusinessError } from '@ohos.base';

screenLock.isSecureMode().then((data: Boolean) => {
  console.info(\`Succeeded in Obtaining whether the device is in secure mode. result: ${data}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to obtain whether the device is in secure mode, Code: ${err.code}, message: ${err.message}\`);
});

#### screenLock.unlockScreen(deprecated)

unlockScreen(callback: AsyncCallback<void>): void

Unlocks the screen. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/BpDd1J6TTfCebKnyaep0xg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8EDF9DE67E8EB1BFFAE182DFD4FB699FB50ED9F4967A44DA9A2AC57457E53E78)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.ScreenLock

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the screen is unlocked successfully, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@ohos.base';

screenLock.unlockScreen((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to unlock the screen, Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded unlocking the screen.\`);
});

#### screenLock.unlockScreen(deprecated)

unlockScreen(): Promise<void>

Unlocks the screen. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/7UM1RHViTy2rs1Kz6Glf5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D061D685A50925488897B6503C7AB68D0A37E5C46250D1B84C785C0B6C659F15)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.ScreenLock

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';

screenLock.unlockScreen().then(() => {
  console.info('Succeeded unlocking the screen.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to unlock the screen, Code: ${err.code}, message: ${err.message}\`);
});
