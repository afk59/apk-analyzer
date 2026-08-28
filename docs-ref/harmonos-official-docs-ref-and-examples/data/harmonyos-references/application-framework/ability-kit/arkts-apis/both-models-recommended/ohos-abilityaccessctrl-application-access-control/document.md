# @ohos.abilityAccessCtrl (Application Access Control)

This module provides permission verification and management capabilities for applications.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/GV2LiEgtQaaqiFpRUTBeKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=470F11EE528A4280FD4DDCF25B48ADC3EC841E7CCC4B56EAC72541D421172412)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { abilityAccessCtrl } from '@kit.AbilityKit';

#### abilityAccessCtrl.createAtManager

createAtManager(): AtManager

Access control: Creates an object for application access control.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Security.AccessToken

**Return value**

| Type | Description |
| :-- | :-- |
| [AtManager](#atmanager) | **AtManager** instance obtained. |

**Example**

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();

#### AtManager

Provides APIs for application access control.

#### \[h2\]checkAccessToken9+

checkAccessToken(tokenID: number, permissionName: Permissions): Promise<GrantStatus>

Checks whether the user has granted the permission. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Security.AccessToken

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tokenID | number | Yes | Identifier of the target application, which is the value of **accessTokenId** contained in [ApplicationInfo](../../dependent-elements-and-definitions/bundlemanager/applicationinfo/document.md). |
| permissionName | [Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions) | Yes | Permission to verify. For details about the permission, see [Application Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[GrantStatus](#grantstatus)\> | Promise used to return the authorization result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Access Control Error Codes](../../../error-codes/access-control-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12100001 | Invalid parameter. The tokenID is 0, or the permissionName exceeds 256 characters. |

**Example**

import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // Use bundleManager.getApplicationInfo() to obtain the token ID for a system application, and use bundleManager.getBundleInfoForSelf() to obtain the token ID for a third-party application.
atManager.checkAccessToken(tokenID, 'ohos.permission.GRANT\_SENSITIVE\_PERMISSIONS').then((data: abilityAccessCtrl.GrantStatus) => {
  console.info(\`checkAccessToken success, result: ${data}\`);
}).catch((err: BusinessError) => {
  console.error(\`checkAccessToken fail, code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]checkAccessTokenSync10+

checkAccessTokenSync(tokenID: number, permissionName: Permissions): GrantStatus

Verifies whether a permission is granted to an application. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Security.AccessToken

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tokenID | number | Yes | Identifier of the target application, which is the value of **accessTokenId** contained in [ApplicationInfo](../../dependent-elements-and-definitions/bundlemanager/applicationinfo/document.md). |
| permissionName | [Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions) | Yes | Permission to verify. For details about the permission, see [Application Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions). |

**Return value**

| Type | Description |
| :-- | :-- |
| [GrantStatus](#grantstatus) | Permission grant state. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Access Control Error Codes](../../../error-codes/access-control-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12100001 | Invalid parameter. The tokenID is 0, or the permissionName exceeds 256 characters. |

**Example**

import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // Use bundleManager.getApplicationInfo() to obtain the token ID for a system application, and use bundleManager.getBundleInfoForSelf() to obtain the token ID for a third-party application.
let permissionName: Permissions = 'ohos.permission.GRANT\_SENSITIVE\_PERMISSIONS';
let data: abilityAccessCtrl.GrantStatus = atManager.checkAccessTokenSync(tokenID, permissionName);
console.info(\`Result: ${data}\`);

#### \[h2\]on18+

on(type: 'selfPermissionStateChange', permissionList: Array<Permissions>, callback: Callback<PermissionStateChangeInfo>): void

Subscribes to the permission state change events of the specified permission list of the current application. Such event triggers a corresponding callback. This API uses an asynchronous callback to return the result.

-   When this subscription API is called for multiple times, if the subscribed permission lists are the same but the callbacks are different, the subscription is successful.
    
-   When this subscription API is called for multiple times, if the subscribed permission lists contain the same subset and the callbacks are the same, the subscription fails.
    

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Security.AccessToken

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'selfPermissionStateChange'**, which indicates the changes in the permission states specific to this application alone. |
| permissionList | Array<[Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions)\> | Yes | List of target permissions. If this parameter is not specified, this API will subscribe to state changes of all permissions. For details about the permissions, see [Application Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions). |
| callback | Callback<[PermissionStateChangeInfo](#permissionstatechangeinfo18)\> | Yes | Callback used to return the result of subscribing to state changes of the specified permission. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Access Control Error Codes](../../../error-codes/access-control-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12100001 | Invalid parameter. Possible causes: 1. The permissionList exceeds the size limit; 2. The permissionNames in the list are all invalid. |
| 12100004 | The API is used repeatedly with the same input. |
| 12100005 | The registration time has exceeded the limit. |
| 12100007 | The service is abnormal. |

**Example**

import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let permissionList: Array<Permissions> = \['ohos.permission.APPROXIMATELY\_LOCATION'\];
try {
    atManager.on('selfPermissionStateChange', permissionList, (data: abilityAccessCtrl.PermissionStateChangeInfo) => {
        console.info(\`receive permission state change, result: ${data}\`);
    });
} catch(err) {
    console.error(\`Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]off18+

off(type: 'selfPermissionStateChange', permissionList: Array<Permissions>, callback?: Callback<PermissionStateChangeInfo>): void

Unsubscribes from changes in the state of the specified permissions for this application. This API uses an asynchronous callback to return the result.

If **callback** is not specified, this API will unregister all callbacks for **permissionList**.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Security.AccessToken

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'selfPermissionStateChange'**, which indicates the changes in the permission states specific to this application alone. |
| permissionList | Array<[Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions)\> | Yes | List of target permissions. The value must be the same as that in **on()**. If this parameter is not specified, this API will unsubscribe from state changes for all permissions. For details about the permissions, see [Application Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions). |
| callback | Callback<[PermissionStateChangeInfo](#permissionstatechangeinfo18)\> | No | Callback used to return the result of canceling the subscription to state changes of the specified token ID and permission. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Access Control Error Codes](../../../error-codes/access-control-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12100001 | Invalid parameter. The permissionNames in the list are all invalid. |
| 12100004 | The API is not used in pair with 'on'. |
| 12100007 | The service is abnormal. |

**Example**

import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let permissionList: Array<Permissions> = \['ohos.permission.APPROXIMATELY\_LOCATION'\];
try {
    atManager.off('selfPermissionStateChange', permissionList);
} catch(err) {
    console.error(\`Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]requestPermissionsFromUser9+

requestPermissionsFromUser(context: Context, permissionList: Array<Permissions>, requestCallback: AsyncCallback<PermissionRequestResult>): void

Starts a dialog box for [Requesting User Authorization](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/request-user-authorization) for UIAbility/UIExtensionAbility. This API uses an asynchronous callback to return the result.

If the user rejects to grant permissions, the dialog box cannot be displayed again. If permission granting is required, the user can manually grant permissions on the **Settings** page or call [requestPermissionOnSetting](#requestpermissiononsetting12) to display the permission settings dialog box for the user to grant permissions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/yKzVRkb8QNi7vK6CinIKUw/en-us_image_0000002568685027.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40A75AF7FF5EA20BCB8139613C5D3844047F9607C262879DF3F7B70481845D3A)

**Atomic service API**: This API can be used in atomic services since API version 12.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Security.AccessToken

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | Context of the UIAbility/UIExtensionAbility that requests the permission. |
| permissionList | Array<[Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions)\> | Yes | Permissions to request. For details about the permissions, see [Application Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions). |
| requestCallback | AsyncCallback<[PermissionRequestResult](../../dependent-elements-and-definitions/security/permissionrequestresult/document.md)\> | Yes | Callback used to return the result. If the dialog box for requesting permissions is displayed successfully, **err** is **undefined**, and **data** is the obtained **PermissionRequestResult**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Access Control Error Codes](../../../error-codes/access-control-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12100001 | Invalid parameter. The context is invalid when it does not belong to the application itself. |

**Example**

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

For details about the process and example of applying for user authorization, see [Requesting User Authorization](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/request-user-authorization).

import { abilityAccessCtrl, Context, PermissionRequestResult, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
// Obtain the context within the component.
let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
atManager.requestPermissionsFromUser(context, \['ohos.permission.CAMERA'\], (err: BusinessError, data: PermissionRequestResult) => {
  if (err) {
    console.error(\`requestPermissionsFromUser fail, code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info(\`requestPermissionsFromUser success, result: ${data}\`);
    console.info('requestPermissionsFromUser data permissions:' + data.permissions);
    console.info('requestPermissionsFromUser data authResults:' + data.authResults);
    console.info('requestPermissionsFromUser data dialogShownResults:' + data.dialogShownResults);
    console.info('requestPermissionsFromUser data errorReasons:' + data.errorReasons);
  }
});

#### \[h2\]requestPermissionsFromUser9+

requestPermissionsFromUser(context: Context, permissionList: Array<Permissions>): Promise<PermissionRequestResult>

Starts a dialog box for [Requesting User Authorization](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/request-user-authorization) for UIAbility/UIExtensionAbility. This API uses a promise to return the result.

If the user rejects to grant permissions, the dialog box cannot be displayed again. If permission granting is required, the user can manually grant permissions on the **Settings** page or call [requestPermissionOnSetting](#requestpermissiononsetting12) to display the permission settings dialog box for the user to grant permissions.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Security.AccessToken

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | Context of the UIAbility/UIExtensionAbility that requests the permission. |
| permissionList | Array<[Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions)\> | Yes | Permissions to request. For details about the permissions, see [Application Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PermissionRequestResult](../../dependent-elements-and-definitions/security/permissionrequestresult/document.md)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Access Control Error Codes](../../../error-codes/access-control-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12100001 | Invalid parameter. The context is invalid when it does not belong to the application itself. |

**Example**

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

For details about the process and example of applying for user authorization, see [Requesting User Authorization](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/request-user-authorization).

import { abilityAccessCtrl, Context, PermissionRequestResult, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
// Obtain the context within the component.
let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
atManager.requestPermissionsFromUser(context, \['ohos.permission.CAMERA'\]).then((data: PermissionRequestResult) => {
  console.info(\`requestPermissionsFromUser success, result: ${data}\`);
  console.info('requestPermissionsFromUser data permissions:' + data.permissions);
  console.info('requestPermissionsFromUser data authResults:' + data.authResults);
  console.info('requestPermissionsFromUser data dialogShownResults:' + data.dialogShownResults);
  console.info('requestPermissionsFromUser data errorReasons:' + data.errorReasons);
}).catch((err: BusinessError) => {
  console.error(\`requestPermissionsFromUser fail, code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]requestPermissionOnSetting12+

requestPermissionOnSetting(context: Context, permissionList: Array<Permissions>): Promise<Array<GrantStatus>>

Starts a permission setting dialog box again for [UIAbility](../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md#uiability) or [UIExtensionAbility](../../stage-model/ohos-app-ability-uiextensionability-extensionability-with-ui/document.md#uiextensionability). This API uses a promise to return the result.

Before calling this API, the application must have called [requestPermissionsFromUser](#requestpermissionsfromuser9). If the user grants the permissions required when the authorization dialog box is displayed the first time, calling this API will not display the permission settings dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/0b9gnx5eSlu_DqLvflO3Xg/en-us_image_0000002568765037.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F07F177B3D1222F350AA03581528A1AFAD3C6B187516B467CF972AF3041F310)

**Atomic service API**: This API can be used in atomic services since API version 12.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Security.AccessToken

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | Context of the UIAbility/UIExtensionAbility that requests the permissions. |
| permissionList | Array<[Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions)\> | Yes | Permissions to request. For details about the permissions, see [Application Permission Groups](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permission-group-list). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[GrantStatus](#grantstatus)\>> | Promise used to return the authorization result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Access Control Error Codes](../../../error-codes/access-control-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12100001 | 
Invalid parameter. Possible causes:

1\. The context is invalid because it does not belong to the application itself;

2\. The permission list contains the permission that is not declared in the module.json file;

3\. The permission list is invalid because the permissions in it do not belong to the same permission group.

 |
| 12100011 | All permissions in the permission list have been granted. |
| 12100012 | The permission list contains the permission that has not been revoked by the user. |
| 12100014 | Unexpected permission. You cannot request this type of permission from users via a pop-up window. |

**Example**

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { abilityAccessCtrl, Context, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
// Obtain the context within the component.
let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
atManager.requestPermissionOnSetting(context, \['ohos.permission.CAMERA'\]).then((data: Array<abilityAccessCtrl.GrantStatus>) => {
  console.info(\`requestPermissionOnSetting success, result: ${data}\`);
}).catch((err: BusinessError) => {
  console.error(\`requestPermissionOnSetting fail, code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]requestGlobalSwitch12+

requestGlobalSwitch(context: Context, type: SwitchType): Promise<boolean>

Displays a dialog box for setting a global switch for UIAbility or UIExtensionAbility. This API uses a promise to return the result.

When the features such as recording and photographing are disabled, the application can display the dialog box, asking the user to enable the related features. If the global switch is turned on, no dialog box will be displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/s8lNHd1hRrejjNYemzpcKw/en-us_image_0000002537765312.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5EA2B0FAD02A4472E0B807AA7461ECC7491F5D9297D9A511366B22C185B0363B)

**Atomic service API**: This API can be used in atomic services since API version 12.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Security.AccessToken

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | Context of the UIAbility/UIExtensionAbility that requests the permissions. |
| type | [SwitchType](#switchtype12) | Yes | Type of the global switch. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. Returns **true** if the global switch is enabled. Returns **false** if the global switch is disabled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Access Control Error Codes](../../../error-codes/access-control-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12100001 | Invalid parameter. Possible causes: 1. The context is invalid because it does not belong to the application itself; 2. The type of global switch is not support. |
| 12100010 | The request already exists. |
| 12100013 | The specific global switch is already open. |

**Example**

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { abilityAccessCtrl, Context, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
// Obtain the context within the component.
let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
atManager.requestGlobalSwitch(context, abilityAccessCtrl.SwitchType.CAMERA).then((data: Boolean) => {
  console.info(\`requestGlobalSwitch success, result: ${data}\`);
}).catch((err: BusinessError) => {
  console.error(\`requestGlobalSwitch fail, code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]getSelfPermissionStatus20+

getSelfPermissionStatus(permissionName: Permissions): PermissionStatus

Queries the permission status of an application. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Security.AccessToken

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| permissionName | [Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions) | Yes | Permission to verify. For details about the permission, see [Application Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions). |

**Return value**

| Type | Description |
| :-- | :-- |
| [PermissionStatus](#permissionstatus20) | Permission status. |

**Error codes**

For details about the error codes, see [Access Control Error Codes](../../../error-codes/access-control-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12100001 | Invalid parameter. The permissionName is empty or exceeds 256 characters. |
| 12100007 | The service is abnormal. |

**Example**

import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
try {
  let data: abilityAccessCtrl.PermissionStatus = atManager.getSelfPermissionStatus('ohos.permission.CAMERA');
  console.info(\`getSelfPermissionStatus success, result: ${data}\`);
} catch(err) {
  console.error(\`getSelfPermissionStatus fail, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]openPermissionOnSetting22+

openPermissionOnSetting(context: Context, permission: Permissions): Promise<SelectedResult>

Starts the dialog box for redirection to the settings page for [UIAbility](../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md#uiability) or [UIExtensionAbility](../../stage-model/ohos-app-ability-uiextensionability-extensionability-with-ui/document.md#uiextensionability). This API uses a promise to return the result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Security.AccessToken

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | Context of the UIAbility/UIExtensionAbility that requests the permissions. |
| permission | [Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions) | Yes | Permission name. Only permissions whose authorization mode is [manual\_settings](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permission-mgmt-overview#manual_settings-manual-authorization) are supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SelectedResult](#selectedresult22)\> | Promise used to return the result of redirection to the settings page. |

**Error codes**

For details about the error codes, see [Access Control Error Codes](../../../error-codes/access-control-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12100001 | 
Invalid parameter. Possible causes:

1\. The context is invalid because it does not belong to the application itself;

2\. The permission is invalid or not declared in the module.json file.

 |
| 12100009 | Common inner error. An error occurs when creating the pop-up window or obtaining user operation result. |
| 12100014 | Unexpected permission. The permission is not a manual\_settings permission. |

**Example**

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { abilityAccessCtrl, Context, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
// Obtain the context within the component.
let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
atManager.openPermissionOnSetting(context, 'ohos.permission.HOOK\_KEY\_EVENT').then((data: abilityAccessCtrl.SelectedResult) => {
  console.info(\`openPermissionOnSetting success, result: ${data}\`);
}).catch((err: BusinessError) => {
  console.error(\`openPermissionOnSetting fail, code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]verifyAccessTokenSync9+

verifyAccessTokenSync(tokenID: number, permissionName: Permissions): GrantStatus

Verifies whether a permission is granted to an application. This API returns the result synchronously.

**System capability**: SystemCapability.Security.AccessToken

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tokenID | number | Yes | Identifier of the target application, which is the value of **accessTokenId** contained in [ApplicationInfo](../../dependent-elements-and-definitions/bundlemanager/applicationinfo/document.md). |
| permissionName | [Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions) | Yes | Permission to verify. For details about the permission, see [Application Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions). |

**Return value**

| Type | Description |
| :-- | :-- |
| [GrantStatus](#grantstatus) | Permission grant state. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Access Control Error Codes](../../../error-codes/access-control-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12100001 | Invalid parameter. The tokenID is 0, or the permissionName exceeds 256 characters. |

**Example**

import { abilityAccessCtrl } from '@kit.AbilityKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // Use bundleManager.getApplicationInfo() to obtain the token ID for a system application, and use bundleManager.getBundleInfoForSelf() to obtain the token ID for a third-party application.
try {
  let data: abilityAccessCtrl.GrantStatus = atManager.verifyAccessTokenSync(tokenID, 'ohos.permission.GRANT\_SENSITIVE\_PERMISSIONS');
  console.info(\`verifyAccessTokenSync success, result: ${data}\`);
} catch(err) {
  console.error(\`verifyAccessTokenSync fail, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]verifyAccessToken9+

verifyAccessToken(tokenID: number, permissionName: Permissions): Promise<GrantStatus>

Checks whether the user has granted the permission. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/WzfzJ4qLTRChdSGbjAIq3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1BD351E8220BE256D680AFDB09DFE9FDAC640903D53042223B308EA300BB555C)

You are advised to use [checkAccessToken](#checkaccesstoken9).

**System capability**: SystemCapability.Security.AccessToken

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tokenID | number | Yes | Identifier of the target application, which is the value of **accessTokenId** contained in [ApplicationInfo](../../dependent-elements-and-definitions/bundlemanager/applicationinfo/document.md). |
| permissionName | [Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions) | Yes | Permission to verify. For details about the permission, see [Application Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[GrantStatus](#grantstatus)\> | Promise used to return the authorization result. |

**Example**

import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // Use bundleManager.getApplicationInfo() to obtain the token ID for a system application, and use bundleManager.getBundleInfoForSelf() to obtain the token ID for a third-party application.
let permissionName: Permissions = 'ohos.permission.GRANT\_SENSITIVE\_PERMISSIONS';
atManager.verifyAccessToken(tokenID, permissionName).then((data: abilityAccessCtrl.GrantStatus) => {
  console.info(\`verifyAccessToken success, result: ${data}\`);
}).catch((err: BusinessError) => {
  console.error(\`verifyAccessToken fail, code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]verifyAccessToken(deprecated)

verifyAccessToken(tokenID: number, permissionName: string): Promise<GrantStatus>

Checks whether the user has granted the permission. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/6c2UYFlgS-6b-yXrRaCQTg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F49317CB6C00A14C95EB193464D00091309F111ABCECE8570ACA0B077279C921)

This API is supported since API version 8 and deprecated since API version 9. Use [checkAccessToken](#checkaccesstoken9) instead.

**System capability**: SystemCapability.Security.AccessToken

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tokenID | number | Yes | Identifier of the target application, which is the value of **accessTokenId** contained in [ApplicationInfo](../../dependent-elements-and-definitions/bundlemanager/applicationinfo/document.md). |
| permissionName | string | Yes | Permission to verify. For details about the permission, see [Application Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[GrantStatus](#grantstatus)\> | Promise used to return the authorization result. |

**Example**

import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // Use bundleManager.getApplicationInfo() to obtain the token ID for a system application, and use bundleManager.getBundleInfoForSelf() to obtain the token ID for a third-party application.
atManager.verifyAccessToken(tokenID, 'ohos.permission.GRANT\_SENSITIVE\_PERMISSIONS').then((data: abilityAccessCtrl.GrantStatus) => {
  console.info(\`verifyAccessToken success, result: ${data}\`);
}).catch((err: BusinessError) => {
  console.error(\`verifyAccessToken fail, code: ${err.code}, message: ${err.message}\`);
});

#### GrantStatus

Enumerates the permission grant states.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Security.AccessToken

| Name | Value | Description |
| :-- | :-- | :-- |
| PERMISSION\_DENIED | \-1 | The permission is not granted. |
| PERMISSION\_GRANTED | 0 | The permission is granted. |

#### SwitchType12+

Enumerates the global switch types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.AccessToken

| Name | Value | Description |
| :-- | :-- | :-- |
| CAMERA | 0 | Global switch of the camera. |
| MICROPHONE | 1 | Global switch of the microphone. |
| LOCATION | 2 | Global switch of the location service. |

#### PermissionStateChangeType18+

Enumerates the operations that trigger permission state changes.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Security.AccessToken

| Name | Value | Description |
| :-- | :-- | :-- |
| PERMISSION\_REVOKED\_OPER | 0 | Operation to revoke a permission. |
| PERMISSION\_GRANTED\_OPER | 1 | Operation to grant a permission. |

#### PermissionStateChangeInfo18+

Represents the permission state change details.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Security.AccessToken

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| change | [PermissionStateChangeType](#permissionstatechangetype18) | No | No | Operation that triggers the permission state change. |
| tokenID | number | No | No | Identifier of the target application, which is the value of **accessTokenId** contained in [ApplicationInfo](../../dependent-elements-and-definitions/bundlemanager/applicationinfo/document.md). |
| permissionName | [Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions) | No | No | Permissions whose authorization state changes. For details about the permissions, see [Application Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions). |

#### PermissionRequestResult10+

type PermissionRequestResult = \_PermissionRequestResult

Represents the permission request result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Security.AccessToken

| Type | Description |
| :-- | :-- |
| [\_PermissionRequestResult](../../dependent-elements-and-definitions/security/permissionrequestresult/document.md) | Permission request result object. |

#### Context10+

type Context = \_Context

Represents the context for the ability or application. It allows access to application-specific resources.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Security.AccessToken

| Type | Description |
| :-- | :-- |
| [\_Context](../../dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Context for an ability or application to access to application-specific resources. |

#### PermissionStatus20+

Enumerates the permission states.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Security.AccessToken

| Name | Value | Description |
| :-- | :-- | :-- |
| DENIED | \-1 | The permission is not granted. |
| GRANTED | 0 | The permission is granted. |
| NOT\_DETERMINED | 1 | The permission state is not determined. This value is returned when the application declares [user\_grant permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/permissions-for-all-user) and does not call [requestPermissionsFromUser](#requestpermissionsfromuser9) to request user authorization, or when the user changes the permission state to **Ask each time** in **Settings**. |
| INVALID | 2 | The permission is invalid. The application does not [declare permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/declare-permissions) or cannot process the request. For example, if the status of the approximate location permission is **NOT\_DETERMINED**, this value will be returned when the status of the precise location permission is queried. |
| RESTRICTED | 3 | The permission is restricted. The user does not agree to the privacy statement (only system apps return this status). |

#### SelectedResult22+

Enumerates the results of the dialog box for redirection to the settings page.

**System capability**: SystemCapability.Security.AccessToken

| Name | Value | Description |
| :-- | :-- | :-- |
| REJECTED | \-1 | The user chooses not to go to the settings. |
| OPENED | 0 | The user chooses to go to the settings. |
| GRANTED | 1 | The permission has been granted and no dialog box is displayed. |
