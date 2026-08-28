# How do I implement the eye comfort mode?

**Solution**

Currently, the eye comfort mode can be implemented in the following ways:

Solution 1: Adapt to the dark mode. For details about how to develop the dark mode, please refer to [Dark Mode Adaption](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-dark-mode-adaptation).

Solution 2: Enable the eye comfort mode globally in the system settings. Guide users to manually enable the eye comfort mode on the settings page.

import { common } from "@kit.AbilityKit";
import { BusinessError } from "@kit.BasicServicesKit";

@Entry
@Component
export struct ImplementEyeProtectionMode {
  build() {
    Row() {
      Button('Go to the settings page')
        .onClick(() => {
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          context.startAbility({
            bundleName: 'com.huawei.hmos.settings',
            abilityName: 'com.huawei.hmos.settings.MainAbility',
            uri: 'display\_settings'
          }).catch((err: BusinessError) => {
            console.error(\`startAbility failed, code is ${err.code}, message is ${err.message}\`);
          })
        })
    }
    .width('100%')
    .height('100%')
    .alignItems(VerticalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}
