# How do I apply for the precise location permission?

**Question**

A user applies for the fuzzy and precise location permissions \['ohos.permission.APPROXIMATELY\_LOCATION','ohos.permission.LOCATION'\]. When a dialog box is displayed for the fuzzy location request, if the user taps **Agree** and applies for the precise location permission, **grantStatus** returns a value of **2**. What does it mean?

**Answer**

If **2** is returned for **grantStatus**, the permission is not granted, and the request is invalid. The possible causes are as follows: The target permission is not declared in the setting file. The permission name is invalid. Some permissions require special application conditions. The specified conditions are not met when the corresponding permissions are applied for. For details about the error codes returned for other permissions, see [PermissionRequestResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-permissionrequestresult).

import { abilityAccessCtrl, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct ApplyPrecisePositioning {
  permissions: Array<Permissions> = \['ohos.permission.APPROXIMATELY\_LOCATION', 'ohos.permission.LOCATION'\];

  aboutToAppear(): void {
    this.reqPermissionsFromUser(this.permissions);
  }

  reqPermissionsFromUser(permissions: Array<Permissions>): void {
    let context: Context = getContext(this) as common.UIAbilityContext;
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    // RequestPermissionsFromUser will determine whether to trigger a pop-up window based on the authorization status of the permission
    atManager.requestPermissionsFromUser(context, permissions).then((data: PermissionRequestResult) => {
      let grantStatus: Array<number> = data.authResults;
      let length: number = grantStatus.length;
      for (let i = 0; i < length; i++) {
        if (grantStatus\[i\] === 0) {
          // User authorization allows continued access to the target operation
        } else {
          // The user refuses authorization, prompting the user that authorization is required to access the functionality of the current page, and guiding the user to open the corresponding permissions in the system settings
          this.getUIContext().getPromptAction().showToast({ message: 'User refuses authorization' });
          return;
        }
      }
      // Authorization successful
    }).catch((err: BusinessError) => {
      console.error(\`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}\`);
    })
  }

  build() {
  }
}
