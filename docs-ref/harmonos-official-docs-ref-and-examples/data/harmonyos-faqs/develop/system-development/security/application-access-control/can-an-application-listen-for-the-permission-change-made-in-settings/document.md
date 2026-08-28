# Can an application listen for the permission change made in Settings?

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-abilityaccessctrl#on18) can be used to listen for the permission change of an application. The following sample code listens for the permission change of **ohos.permission.APPROXIMATELY\_LOCATION**. You need to declare the permission in **module.json5**. The sample code is as follows:

import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    let permissionList: Array<Permissions> = \['ohos.permission.APPROXIMATELY\_LOCATION'\];
    try {
      atManager.on('selfPermissionStateChange', permissionList, (data: abilityAccessCtrl.PermissionStateChangeInfo) => {
        console.info('receive permission state change, data:' + JSON.stringify(data));
      });
    } catch (err) {
      console.error(\`catch err->${JSON.stringify(err)}\`);
    }
  }

  build() {
    // ...
  }
}
