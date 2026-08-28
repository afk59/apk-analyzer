# How do I determine the initiator of an application?

When you use **startAbility()** to start an application, the **parameters** attribute in the **want** parameter can carry the information about the initiator. The system provides some preset keys in **parameters**. For example, you can use **ohos.aafwk.param.callerBundleName** to obtain the bundle name of the initiator.

Refer to the sample code below.

Code for the initiator:

import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  context = this.getUIContext();

  build() {
    Row() {
      Column() {
        Button('open app')
          .onClick(() => {
            let want: Want = {
              action: 'ohos.want.action.viewData',
              entities: \['entity.system.home'\]
            }
            let context = this.context.getHostContext() as common.UIAbilityContext;
            context.startAbility(want, (err: BusinessError) => {
              if (err.code) {
                // Service logic error
                hilog.error(0x0000, 'testTag', \`startAbility failed, code is ${err.code}, message is ${err.message}\`);
                return;
              }
              // Successful outcome
              hilog.info(0x0000, 'testTag', 'startAbility succeed');
            });
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

Code for the application started:

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', \`app resource is:${want.parameters?.\['ohos.aafwk.param.callerBundleName'\]}\`);
    // ...
  }

  // ...
}

**Reference**

[Want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-want#want)
