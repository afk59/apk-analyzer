# How do I use ErrorManager to capture exceptions?

The ErrorManager module provides APIs for registering and deregistering error observers.

The capabilities of the **ErrorObserver** API are as follows:

| 
API

 | 

Description

 |
| :-- | :-- |
| 

onUnhandledException(errMsg: string): void

 | 

Called when an uncaught exception is reported after the application is registered.

 |
| 

onException?(errObject: Error): void

 | 

Called when an application exception is reported to the JavaScript layer after the application is registered.

 |

Refer to the sample code below for exception capture.

In **Index.ets**:

@Entry
@Component
struct ErrorManagerPage {
  @State message: string = 'Capture exceptions';

  build() {
    Row() {
      Column() {
        Button(this.message)
          .onClick(() => {
            let tempList = \['0', '1'\];
            tempList\[5\].toString();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

In **EntryAbility.ets**:

import { AbilityConstant, errorManager, UIAbility, Want } from '@kit.AbilityKit';
import { ConfigurationConstant } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

let callback: errorManager.ErrorObserver = {
  onUnhandledException: (errMsg) => {
    console.log('Callback when an uncaught exception occurs,onUnhandledException:', errMsg);
  },
  onException: (errorObj) => {
    console.log('The callback when an exception is reported to the JS layer,onException');
    console.log('onException, name: ', errorObj.name);
    console.log('onException, message: ', errorObj.message);
    if (typeof (errorObj.stack) === 'string') {
      console.log('onException, stack: ', errorObj.stack);
    }
  }
}

let abilityWant: Want;
let registerId = -1;
const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR\_MODE\_NOT\_SET);
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
      console.log('\[Demo\] EntryAbility onCreate');
      registerId = errorManager.on('error', callback);
      abilityWant = want;
      console.log('registerId:', registerId);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', \`setColorMode failed, code is ${err.code}, message is ${err.message}\`);
    }
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
    console.log('\[Demo\] EntryAbility onDestroy');
    errorManager.off('error', registerId, (result) => {
      console.log(\`\[Demo\] result:${result}\`);
    });
  }

  // ...
}

**Reference**

[@ohos.app.ability.errorManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-errormanager)
