# Context (Context Base Class of the FA Model)

The Context module provides context for ability components or applications. It allows access to application-specific resources, as well as permission requests and verification.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/mmtxQY9NT1uQiRXTeLgruw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79EA30B68103C7F5A84305E9AADD4524A8A7A496590292D3272FB28D2AE4D99B)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the FA model.

#### Modules to Import

import featureAbility from '@ohos.ability.featureAbility';

#### Usage

The Context object is created in a featureAbility and returned through its [getContext](../../ohos-ability-featureability-featureability-module/document.md#featureabilitygetcontext) API. Therefore, you must import the @ohos.ability.featureAbility package before using the Context module. An example is as follows:

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getOrCreateLocalDir().then((data) => {
    console.info(\`getOrCreateLocalDir data: ${JSON.stringify(data)}\`);
});

#### Context.getOrCreateLocalDir7+

getOrCreateLocalDir(callback: AsyncCallback<string>): void

Obtains the local root directory of the application. This API uses an asynchronous callback to return the result.

If this API is called for the first time, a root directory will be created.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the local root directory. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getOrCreateLocalDir((error, data)=>{
    if (error && error.code !== 0) {
        console.error(\`getOrCreateLocalDir fail, error: ${JSON.stringify(error)}\`);
    } else {
        console.info(\`getOrCreateLocalDir success, data: ${JSON.stringify(data)}\`);
    }
});

#### Context.getOrCreateLocalDir7+

getOrCreateLocalDir(): Promise<string>

Obtains the local root directory of the application. This API uses a promise to return the result.

If this API is called for the first time, a root directory will be created.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the local root directory. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getOrCreateLocalDir().then((data) => {
    console.info(\`getOrCreateLocalDir data: ${JSON.stringify(data)}\`);
});

#### Context.verifyPermission7+

verifyPermission(permission: string, options: PermissionOptions, callback: AsyncCallback<number>): void

Verifies whether a PID and UID have the given permission. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| permission | string | Yes | Name of the permission to verify. |
| options | [PermissionOptions](#permissionoptions7) | Yes | Permission options. |
| callback | AsyncCallback<number> | Yes | Callback used to return the permission verification result. The value **0** means that the PID and UID have the given permission, and the value **\-1** means the opposite. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';
import bundle from '@ohos.bundle.bundleManager';
import { BusinessError } from '@ohos.base';

let context: featureAbility.Context = featureAbility.getContext();
bundle.getBundleInfo('com.context.test', 1, (err: BusinessError, datainfo: bundle.BundleInfo) =>{
    context.verifyPermission('com.example.permission', {uid:datainfo.appInfo.uid}, (error, data) =>{
        if (error && error.code !== 0) {
            console.error(\`verifyPermission fail, error: ${JSON.stringify(error)}\`);
        } else {
            console.info(\`verifyPermission success, data: ${JSON.stringify(data)}\`);
        }
    });
});

For details about **getBundleInfo** in the sample code, see [bundleManager](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md).

#### Context.verifyPermission7+

verifyPermission(permission: string, callback: AsyncCallback<number>): void

Verifies whether the current PID and UID have the given permission. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| permission | string | Yes | Name of the permission to verify. |
| callback | AsyncCallback<number> | Yes | Callback used to return the permission verification result. The value **0** means that the PID and UID have the given permission, and the value **\-1** means the opposite. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.verifyPermission('com.example.permission', (error, data) =>{
    if (error && error.code !== 0) {
        console.error(\`verifyPermission fail, error: ${JSON.stringify(error)}\`);
    } else {
        console.info(\`verifyPermission success, data: ${JSON.stringify(data)}\`);
    }
});

#### Context.verifyPermission7+

verifyPermission(permission: string, options?: PermissionOptions): Promise<number>

Verifies whether a PID and UID have the given permission. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| permission | string | Yes | Name of the permission to verify. |
| options | [PermissionOptions](#permissionoptions7) | No | Permission options. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the permission verification result. The value **0** means that the PID and UID have the given permission, and the value **\-1** means the opposite. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.verifyPermission('com.context.permission', {pid:1}).then((data) => {
    console.info(\`verifyPermission data: ${JSON.stringify(data)}\`);
});

#### Context.requestPermissionsFromUser7+

requestPermissionsFromUser(permissions: Array<string>, requestCode: number, resultCallback: AsyncCallback<PermissionRequestResult>): void

Requests certain permissions from the system. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| permissions | Array<string> | Yes | Permissions to request. This parameter cannot be **null**. |
| requestCode | number | Yes | Request code to be passed to [PermissionRequestResult](#permissionrequestresult7). |
| resultCallback | AsyncCallback<[PermissionRequestResult](#permissionrequestresult7)\> | Yes | Callback used to return the permission request result. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.requestPermissionsFromUser(
    \['com.example.permission1',
     'com.example.permission2',
     'com.example.permission3',
     'com.example.permission4',
     'com.example.permission5'\],
    1,
    (error, data) => {
        if (error && error.code !== 0) {
            console.error(\`requestPermissionsFromUser fail, error: ${JSON.stringify(error)}\`);
        } else {
            console.info(\`requestPermissionsFromUser success, data: ${JSON.stringify(data)}\`);
        }
    }
);

#### Context.requestPermissionsFromUser7+

requestPermissionsFromUser(permissions: Array<string>, requestCode: number): Promise<PermissionRequestResult>

Requests certain permissions from the system. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| permissions | Array<string> | Yes | Permissions to request. This parameter cannot be **null**. |
| requestCode | number | Yes | Request code to be passed to [PermissionRequestResult](#permissionrequestresult7). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PermissionRequestResult](#permissionrequestresult7)\> | Promise used to return the permission request result. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.requestPermissionsFromUser(
    \['com.example.permission1',
     'com.example.permission2',
     'com.example.permission3',
     'com.example.permission4',
     'com.example.permission5'\],
    1).then((data)=>{
        console.info(\`requestPermissionsFromUser data: ${JSON.stringify(data)}\`);
    }
);

#### Context.getApplicationInfo7+

getApplicationInfo(callback: AsyncCallback<ApplicationInfo>): void

Obtains information about the application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[ApplicationInfo](../../../dependent-elements-and-definitions/bundlemanager/applicationinfo/document.md)\> | Yes | Callback used to return the application information. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getApplicationInfo((error, data) => {
    if (error && error.code !== 0) {
        console.error(\`getApplicationInfo fail, error: ${JSON.stringify(error)}\`);
    } else {
        console.info(\`getApplicationInfo success, data: ${JSON.stringify(data)}\`);
    }
});

#### Context.getApplicationInfo7+

getApplicationInfo(): Promise<ApplicationInfo>

Obtains information about the application. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ApplicationInfo](../../../apis-no-longer-maintained/bundle/applicationinfo/document.md)\> | Promise used to return the application information. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getApplicationInfo().then((data) => {
    console.info(\`getApplicationInfo data: ${JSON.stringify(data)}\`);
});

#### Context.getBundleName7+

getBundleName(callback: AsyncCallback<string>): void

Obtains the bundle name of this ability. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the bundle name. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getBundleName((error, data) => {
    if (error && error.code !== 0) {
        console.error(\`getBundleName fail, error: ${JSON.stringify(error)}\`);
    } else {
        console.info(\`getBundleName success, data: ${JSON.stringify(data)}\`);
    }
});

#### Context.getBundleName7+

getBundleName(): Promise<string>

Obtains the bundle name of this ability. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the bundle name. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getBundleName().then((data) => {
    console.info(\`getBundleName data: ${JSON.stringify(data)}\`);
});

#### Context.getDisplayOrientation7+

getDisplayOrientation(callback: AsyncCallback<bundle.DisplayOrientation>): void

Obtains the display orientation of this ability. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[bundle.DisplayOrientation](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#displayorientation)\> | Yes | Callback used to return the display orientation. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getDisplayOrientation((error, data) => {
    if (error && error.code !== 0) {
        console.error(\`getDisplayOrientation fail, error: ${JSON.stringify(error)}\`);
    } else {
        console.info(\`getDisplayOrientation success, data: ${JSON.stringify(data)}\`);
    }
});

#### Context.getDisplayOrientation7+

getDisplayOrientation(): Promise<bundle.DisplayOrientation>

Obtains the display orientation of this ability. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[bundle.DisplayOrientation](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#displayorientation)\> | Promise used to return the display orientation. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getDisplayOrientation().then((data) => {
    console.info(\`getDisplayOrientation data: ${JSON.stringify(data)}\`);
});

#### Context.getExternalCacheDir(deprecated)

getExternalCacheDir(callback: AsyncCallback<string>): void

Obtains the external cache directory of the application. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/TLIHLHf4TEyBGoQUl3cjTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A22E145A77213B38F357B235997CECA6DD266DB2D08F3CC9C5C0CFB5A66C3B7)

This API is deprecated since API version 7.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the absolute path of the cache directory. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getExternalCacheDir((error, data) => {
    if (error && error.code !== 0) {
        console.error(\`getExternalCacheDir fail, error: ${JSON.stringify(error)}\`);
    } else {
        console.info(\`getExternalCacheDir success, data: ${JSON.stringify(data)}\`);
    }
});

#### Context.getExternalCacheDir(deprecated)

getExternalCacheDir(): Promise<string>

Obtains the external cache directory of the application. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/gkzesJ2JSM-G1MFfzh-9FQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCDDD87C51A264325E1C229647DF67F118DA13F21345E21B4A40FA8888C129DC)

This API is deprecated since API version 7.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the absolute path of the cache directory. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getExternalCacheDir().then((data) => {
    console.info(\`getExternalCacheDir data: ${JSON.stringify(data)}\`);
});

#### Context.setDisplayOrientation7+

setDisplayOrientation(orientation: bundle.DisplayOrientation, callback: AsyncCallback<void>): void

Sets the display orientation for this ability. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| orientation | [bundle.DisplayOrientation](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#displayorientation) | Yes | Display orientation to set. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the setting is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';
import bundleManager from '@ohos.bundle';

let context: featureAbility.Context = featureAbility.getContext();
let orientation = bundleManager.DisplayOrientation.LANDSCAPE;
context.setDisplayOrientation(orientation, (error) => {
    console.error(\`setDisplayOrientation fail, error: ${JSON.stringify(error)}\`);
});

#### Context.setDisplayOrientation7+

setDisplayOrientation(orientation: bundle.DisplayOrientation): Promise<void>

Sets the display orientation for this ability. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| orientation | [bundle.DisplayOrientation](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#displayorientation) | Yes | Callback used to return the display orientation. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';
import bundleManager from '@ohos.bundle';

let context: featureAbility.Context = featureAbility.getContext();
let orientation = bundleManager.DisplayOrientation.UNSPECIFIED;
context.setDisplayOrientation(orientation).then((data) => {
    console.info(\`setDisplayOrientation data: ${JSON.stringify(data)}\`);
});

#### Context.setShowOnLockScreen(deprecated)

setShowOnLockScreen(show: boolean, callback: AsyncCallback<void>): void

Sets whether to show this feature at the top of the lock screen so that the feature remains activated. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/l-dCpC9DR-K7XHYYGMtOvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31AA750BE6EC30EA76193E9D46E8616B77AB53C3D6A3F405ACAC95DFA5BA6352)

This API is valid only for system applications.

This API is supported since API version 7 and deprecated since API version 9. You are advised to use **window.setShowOnLockScreen**, which is a system API.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| show | boolean | Yes | Whether to show this feature at the top of the lock screen. **true** to show, **false** otherwise. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the setting is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
let show = true;
context.setShowOnLockScreen(show, (error) => {
    console.error(\`setShowOnLockScreen fail, error: ${JSON.stringify(error)}\`);
});

#### Context.setShowOnLockScreen(deprecated)

setShowOnLockScreen(show: boolean): Promise<void>

Sets whether to show this feature at the top of the lock screen so that the feature remains activated. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/YerXprszRXyfMnDlLotCvw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F154529BAEA91654A22318FAFC84D4CB0AC95540C100CBCC89272B4288405BCF)

This API is valid only for system applications.

This API is supported since API version 7 and deprecated since API version 9. You are advised to use **window.setShowOnLockScreen**, which is a system API.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| show | boolean | Yes | Whether to show this feature at the top of the lock screen. **true** to show, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
let show = true;
context.setShowOnLockScreen(show).then((data) => {
    console.info(\`setShowOnLockScreen data: ${JSON.stringify(data)}\`);
});

#### Context.setWakeUpScreen(deprecated)

setWakeUpScreen(wakeUp: boolean, callback: AsyncCallback<void>): void

Sets whether to wake up the screen when this feature is restored. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/8pZLvO4qSreX4HebcwRmIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=114EEF539C75D24B19EC144958109C1B33123B8ACBE9FEBA68CF84C4EA9B974F)

This API is valid only for system applications.

This API is supported since API version 7 and deprecated since API version 12. You can use **window.setWakeUpScreen** instead, which is a system API.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| wakeUp | boolean | Yes | Whether to wake up the screen. **true** to wake up, **false** otherwise. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the setting is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
let wakeUp = true;
context.setWakeUpScreen(wakeUp, (error) => {
    console.error(\`setWakeUpScreen fail, error: ${JSON.stringify(error)}\`);
});

#### Context.setWakeUpScreen(deprecated)

setWakeUpScreen(wakeUp: boolean): Promise<void>

Sets whether to wake up the screen when this feature is restored. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/G5ej51MeSeqIpLFAED_-cA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43083E0B9C8481498928F34476EC86734CB63A74A9BE72D72B77DE383765D00A)

This API is valid only for system applications.

This API is supported since API version 7 and deprecated since API version 12. You can use **window.setWakeUpScreen** instead, which is a system API.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| wakeUp | boolean | Yes | Whether to wake up the screen. **true** to wake up, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
let wakeUp = true;
context.setWakeUpScreen(wakeUp).then((data) => {
    console.info(\`setWakeUpScreen data: ${JSON.stringify(data)}\`);
});

#### Context.getProcessInfo7+

getProcessInfo(callback: AsyncCallback<ProcessInfo>): void

Obtains information about the current process, including the PID and process name. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[ProcessInfo](../processinfo/document.md)\> | Yes | Callback used to return the process information. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getProcessInfo((error, data) => {
    if (error && error.code !== 0) {
        console.error(\`getProcessInfo fail, error: ${JSON.stringify(error)}\`);
    } else {
        console.info(\`getProcessInfo success, data: ${JSON.stringify(data)}\`);
    }
});

#### Context.getProcessInfo7+

getProcessInfo(): Promise<ProcessInfo>

Obtains information about the current process, including the PID and process name. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ProcessInfo](../processinfo/document.md)\> | Promise used to return the process information. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getProcessInfo().then((data) => {
    console.info(\`getProcessInfo data: ${JSON.stringify(data)}\`);
});

#### Context.getElementName7+

getElementName(callback: AsyncCallback<ElementName>): void

Obtains the element name of this ability. This API uses an asynchronous callback to return the result.

This API is available only to Page ability components.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[ElementName](../../../dependent-elements-and-definitions/bundlemanager/elementname/document.md)\> | Yes | Callback used to return the element name, which is an ohos.bundleManager.ElementName object. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getElementName((error, data) => {
    if (error && error.code !== 0) {
        console.error(\`getElementName fail, error: ${JSON.stringify(error)}\`);
    } else {
        console.info(\`getElementName success, data: ${JSON.stringify(data)}\`);
    }
});

#### Context.getElementName7+

getElementName(): Promise<ElementName>

Obtains the element name of this ability. This API uses a promise to return the result.

This API is available only to Page ability components.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ElementName](../../../dependent-elements-and-definitions/bundlemanager/elementname/document.md)\> | Promise used to return the element name, which is an ohos.bundleManager.ElementName object. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getElementName().then((data) => {
    console.info(\`getElementName data: ${JSON.stringify(data)}\`);
});

#### Context.getProcessName7+

getProcessName(callback: AsyncCallback<string>): void

Obtains the name of the current process. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the process name. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getProcessName((error, data) => {
    if (error && error.code !== 0) {
        console.error(\`getProcessName fail, error: ${JSON.stringify(error)}\`);
    } else {
        console.info(\`getProcessName success, data: ${JSON.stringify(data)}\`);
    }
});

#### Context.getProcessName7+

getProcessName(): Promise<string>

Obtains the name of the current process. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the process name. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getProcessName().then((data) => {
    console.info(\`getProcessName data: ${JSON.stringify(data)}\`);
});

#### Context.getCallingBundle7+

getCallingBundle(callback: AsyncCallback<string>): void

Obtains the bundle name of the caller ability. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the bundle name. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getCallingBundle((error, data) => {
    if (error && error.code !== 0) {
        console.error(\`getCallingBundle fail, error: ${JSON.stringify(error)}\`);
    } else {
        console.info(\`getCallingBundle success, data: ${JSON.stringify(data)}\`);
    }
});

#### Context.getCallingBundle7+

getCallingBundle(): Promise<string>

Obtains the bundle name of the caller ability. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the bundle name. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getCallingBundle().then((data) => {
    console.info(\`getCallingBundle data: ${JSON.stringify(data)}\`);
});

#### Context.getCacheDir

getCacheDir(callback: AsyncCallback<string>): void

Obtains the cache directory of the application in the internal storage. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the cache directory. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getCacheDir((error, data) => {
    if (error && error.code !== 0) {
        console.error(\`getCacheDir fail, error: ${JSON.stringify(error)}\`);
    } else {
        console.info(\`getCacheDir success, data: ${JSON.stringify(data)}\`);
    }
});

#### Context.getCacheDir

getCacheDir(): Promise<string>

Obtains the cache directory of the application in the internal storage. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the cache directory. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getCacheDir().then((data) => {
    console.info(\`getCacheDir data: ${JSON.stringify(data)}\`);
});

#### Context.getFilesDir

getFilesDir(callback: AsyncCallback<string>): void

Obtains the file directory of the application in the internal storage. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the file directory. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getFilesDir((error, data) => {
    if (error && error.code !== 0) {
        console.error(\`getFilesDir fail, error: ${JSON.stringify(error)}\`);
    } else {
        console.info(\`getFilesDir success, data: ${JSON.stringify(data)}\`);
    }
});

#### Context.getFilesDir

getFilesDir(): Promise<string>

Obtains the file directory of the application in the internal storage. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the file directory. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getFilesDir().then((data) => {
    console.info(\`getFilesDir data: ${JSON.stringify(data)}\`);
});

#### Context.getOrCreateDistributedDir7+

getOrCreateDistributedDir(callback: AsyncCallback<string>): void

Obtains the distributed file path for storing ability or application data files. This API uses an asynchronous callback to return the result.

If the distributed file path does not exist, the system will create a path and return the created path.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | 
Callback used to return the distributed file path.

If the path does not exist, the system will create one and return the created path.

 |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getOrCreateDistributedDir((error, data) => {
    if (error && error.code !== 0) {
        console.error(\`getOrCreateDistributedDir fail, error: ${JSON.stringify(error)}\`);
    } else {
        console.info(\`getOrCreateDistributedDir success, data: ${JSON.stringify(data)}\`);
    }
});

#### Context.getOrCreateDistributedDir7+

getOrCreateDistributedDir(): Promise<string>

Obtains the distributed file path for storing ability or application data files. This API uses a promise to return the result.

If the distributed file path does not exist, the system will create a path and return the created path.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the distributed file path. If this API is called for the first time, a path will be created. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getOrCreateDistributedDir().then((data) => {
    console.info(\`getOrCreateDistributedDir data: ${JSON.stringify(data)}\`);
});

#### Context.getAppType7+

getAppType(callback: AsyncCallback<string>): void

Obtains the application type. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the application type. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getAppType((error, data) => {
    if (error && error.code !== 0) {
        console.error(\`getAppType fail, error: ${JSON.stringify(error)}\`);
    } else {
        console.info(\`getAppType success, data: ${JSON.stringify(data)}\`);
    }
});

#### Context.getAppType7+

getAppType(): Promise<string>

Obtains the application type. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the application type. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getAppType().then((data) => {
    console.info(\`getAppType data: ${JSON.stringify(data)}\`);
});

#### Context.getHapModuleInfo7+

getHapModuleInfo(callback: AsyncCallback<HapModuleInfo>): void

Obtains the module information of the application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[HapModuleInfo](../../../dependent-elements-and-definitions/bundlemanager/hapmoduleinfo/document.md)\> | Yes | Callback used to return the module information, which is a HapModuleInfo object. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getHapModuleInfo((error, data) => {
    if (error && error.code !== 0) {
        console.error(\`getHapModuleInfo fail, error: ${JSON.stringify(error)}\`);
    } else {
        console.info(\`getHapModuleInfo success, data: ${JSON.stringify(data)}\`);
    }
});

#### Context.getHapModuleInfo7+

getHapModuleInfo(): Promise<HapModuleInfo>

Obtains the module information of the application. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[HapModuleInfo](../../../dependent-elements-and-definitions/bundlemanager/hapmoduleinfo/document.md)\> | Promise used to return the module information, which is a HapModuleInfo object. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getHapModuleInfo().then((data) => {
    console.info(\`getHapModuleInfo data: ${JSON.stringify(data)}\`);
});

#### Context.getAppVersionInfo7+

getAppVersionInfo(callback: AsyncCallback<AppVersionInfo>): void

Obtains the version information of the application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AppVersionInfo](../appversioninfo/document.md)\> | Yes | Callback used to return the version information. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getAppVersionInfo((error, data) => {
    if (error && error.code !== 0) {
        console.error(\`getAppVersionInfo fail, error: ${JSON.stringify(error)}\`);
    } else {
        console.info(\`getAppVersionInfo success, data: ${JSON.stringify(data)}\`);
    }
});

#### Context.getAppVersionInfo7+

getAppVersionInfo(): Promise<AppVersionInfo>

Obtains the version information of the application. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AppVersionInfo](../appversioninfo/document.md)\> | Promise used to return the version information. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getAppVersionInfo().then((data) => {
    console.info(\`getAppVersionInfo data: ${JSON.stringify(data)}\`);
});

#### Context.getAbilityInfo7+

getAbilityInfo(callback: AsyncCallback<AbilityInfo>): void

Obtains information about this ability. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AbilityInfo](../../../dependent-elements-and-definitions/bundlemanager/abilityinfo/document.md)\> | Yes | Callback used to return the ability information. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getAbilityInfo((error, data) => {
    if (error && error.code !== 0) {
        console.error(\`getAbilityInfo fail, error: ${JSON.stringify(error)}\`);
    } else {
        console.info(\`getAbilityInfo success, data: ${JSON.stringify(data)}\`);
    }
});

#### Context.getAbilityInfo7+

getAbilityInfo(): Promise<AbilityInfo>

Obtains information about this ability. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AbilityInfo](../../../dependent-elements-and-definitions/bundlemanager/abilityinfo/document.md)\> | Promise used to return the ability information. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getAbilityInfo().then((data) => {
    console.info(\`getAbilityInfo data: ${JSON.stringify(data)}\`);
});

#### Context.getApplicationContext7+

getApplicationContext(): Context

Obtains the context of the application.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Context | Application context. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext().getApplicationContext();

#### Context.isUpdatingConfigurations7+

isUpdatingConfigurations(callback: AsyncCallback<boolean>): void

Checks whether the configuration of this ability is being updated. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. **true** if the configuration of the ability is being updated, **false** otherwise. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.isUpdatingConfigurations((error, data) => {
    if (error && error.code !== 0) {
        console.error(\`isUpdatingConfigurations fail, error: ${JSON.stringify(error)}\`);
    } else {
        console.info(\`isUpdatingConfigurations success, data: ${JSON.stringify(data)}\`);
    }
});

#### Context.isUpdatingConfigurations7+

isUpdatingConfigurations(): Promise<boolean>

Checks whether the configuration of this ability is being updated. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. **true** if the configuration of the ability is being updated, **false** otherwise. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.isUpdatingConfigurations().then((data) => {
    console.info(\`isUpdatingConfigurations data: ${JSON.stringify(data)}\`);
});

#### Context.printDrawnCompleted7+

printDrawnCompleted(callback: AsyncCallback<void>): void

Notifies the system of the time required to draw this page function. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the notification is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.printDrawnCompleted((err) => {
    console.error(\`printDrawnCompleted err: ${JSON.stringify(err)}\`);
});

#### Context.printDrawnCompleted7+

printDrawnCompleted(): Promise<void>

Notifies the system of the time required to draw this page function. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.printDrawnCompleted().then((data) => {
    console.info(\`printDrawnCompleted data: ${JSON.stringify(data)}\`);
});

#### PermissionOptions7+

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pid | number | No | Yes | Process ID. |
| uid | number | No | Yes | User ID. |

#### PermissionRequestResult7+

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| requestCode | number | No | No | Request code passed. |
| permissions | Array<string> | No | No | Permissions requested. |
| authResults | Array<number> | No | No | Permission request result. |
