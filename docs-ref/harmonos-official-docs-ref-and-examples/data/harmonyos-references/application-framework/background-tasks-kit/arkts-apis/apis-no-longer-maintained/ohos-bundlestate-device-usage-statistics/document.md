# @ohos.bundleState (Device Usage Statistics)

This module provides APIs for collecting statistics on device usage.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/NM02I7oKTMynRpVmlUCt5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E396B7CB047C6B24EEDC529454EE460AADAC88B7D1CC04B9A66F4E52A4983E76)

-   The APIs of this module are deprecated since API version 9. The substitute APIs are open only to system applications.
    
-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    

#### Modules to Import

import bundleState from '@ohos.bundleState'

#### bundleState.isIdleState(deprecated)

isIdleState(bundleName: string, callback: AsyncCallback<boolean>): void

This API is supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

Checks whether the application specified by **bundleName** is in the idle state. A third-party application can only check the idle state of itself. A system application can check the idle state of other applications only when it is granted with the ohos.permission.BUNDLE\_ACTIVE\_INFO permission. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name of an application. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the specified **bundleName** is valid, the idle state of the application is returned; otherwise, **null** is returned. |

**Example**

import { BusinessError } from '@ohos.base';
// When a third-party application uses the sample code, change bundleName to its own bundle name.
bundleState.isIdleState("com.ohos.camera", (err: BusinessError, res: boolean) => {
  if (err) {
    console.error('BUNDLE\_ACTIVE isIdleState callback failed, because: ' + err.code);
  } else {
    console.info('BUNDLE\_ACTIVE isIdleState callback succeeded, result: ' + JSON.stringify(res));
  }
});

#### bundleState.isIdleState(deprecated)

isIdleState(bundleName: string): Promise<boolean>

This API is supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

Checks whether the application specified by **bundleName** is in the idle state. A third-party application can only check the idle state of itself. A system application can check the idle state of other applications only when it is granted with the ohos.permission.BUNDLE\_ACTIVE\_INFO permission. This API uses a promise to return the result.

**System capability**: SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name of an application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. If the specified **bundleName** is valid, the idle state of the application is returned; otherwise, **null** is returned. |

**Example**

import { BusinessError } from '@ohos.base';
// When a third-party application uses the sample code, change bundleName to its own bundle name.
bundleState.isIdleState("com.ohos.camera").then((res: boolean) => {
  console.info('BUNDLE\_ACTIVE isIdleState promise succeeded, result: ' + JSON.stringify(res));
}).catch((err: BusinessError) => {
  console.error('BUNDLE\_ACTIVE isIdleState promise failed, because: ' + err.code);
});
