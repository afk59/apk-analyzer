# PermissionRequestResult

The **PermissionRequestResult** module defines the permission request result returned by [requestPermissionsFromUser](../../../both-models-recommended/ohos-abilityaccessctrl-application-access-control/document.md#requestpermissionsfromuser9).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/kwN0gawdS_SImmXW82jVRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062211Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD673A37865D7BADAD5FCFCC5224B1144E4D75A80C665103A4BE9C75E45AA819)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs of this module can be used only in the stage model.

#### Properties

**System capability**: SystemCapability.Security.AccessToken

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| permissions | Array<string> | No | No | 
Permissions requested.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| authResults | Array<number> | No | No | 

Result of the permission request.

\- **\-1**: The permission is not granted. If **dialogShownResults** is **true**, this is the user's initial request. If **dialogShownResults** is **false**, the permission has been set and no dialog box is displayed. The user can modify the permission in **Settings**.

\- **0**: The permission is granted.

\- **2**: The permission request is invalid. The possible causes are as follows: 1. The permission is not declared in the configuration file. 2. The permission name is invalid. 3. The conditions for requesting the permission are not met. For details, see [ohos.permission.LOCATION](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/permissions-for-all-user#ohospermissionlocation) and [ohos.permission.APPROXIMATELY\_LOCATION](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/permissions-for-all-user#ohospermissionapproximately_location).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| dialogShownResults12+ | Array<boolean> | No | Yes | 

Whether to display a dialog box.

The value **true** means to display a dialog box;

the value **false** means the opposite.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| errorReasons18+ | Array<number> | No | Yes | 

Return value.

**0**: The request is valid.

**1**: The permission name is invalid.

**2**: The permission is not declared in the configuration file.

**3**: The conditions for requesting the permission are not met. For details, see the permission description in [Permission List](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/permissions-for-all-user). Currently, only the location permissions are involved.

**4**: The user does not agree to the privacy statement.

**5**: The permission cannot be requested using the dialog box. The possible cause is that the permission cannot be requested or is forcibly controlled by system policies.

**6**: The permission authorization mode is manual\_settings, and the permission cannot be requested using the dialog box.

**12**: The service is abnormal.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### Usage

The permission request result is obtained through an **atManager** instance.

**Example**

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { abilityAccessCtrl, Context, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager = abilityAccessCtrl.createAtManager();
try {
  // Obtain the context within the component.
  let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  atManager.requestPermissionsFromUser(context, \["ohos.permission.CAMERA"\]).then((data) => {
      console.info("data permissions:" + data.permissions);
      console.info("data authResults:" + data.authResults);
      console.info("data dialogShownResults:" + data.dialogShownResults);
      console.info("data errorReasons:" + data.errorReasons);
  }).catch((err: BusinessError) => {
      console.error(\`code: ${err.code}, message: ${err.message}\`);
  })
} catch(err) {
  console.error(\`catch errcode: ${err.code}, message: ${err.message}\`);
}
