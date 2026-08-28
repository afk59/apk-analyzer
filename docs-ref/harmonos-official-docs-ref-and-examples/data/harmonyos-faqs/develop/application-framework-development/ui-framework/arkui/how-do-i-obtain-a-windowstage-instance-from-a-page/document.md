# How do I obtain a WindowStage instance from a page?

Method 1: Obtain the **WindowStage** instance in **onWindowStageCreate**. This method is applicable to the scenario where the **WindowStage** instance needs to be persisted within the lifecycle of an ability.

import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
    });
    console.info('windowStage', JSON.stringify(windowStage))
    // Store windowStage instance globally for cross-page access
    AppStorage.setAndLink('windowStage', windowStage)
  }

  // ...
}

Method 2: **UIAbilityContext** provides an API for obtaining a **WindowStage** instance. This method is applicable to page-level scenarios where **WindowStage** instances need to be dynamically obtained and do not need to be stored persistently.

// Index.ets
import common from '@ohos.app.ability.common';

@Entry
@Component
struct Index {
  @State showAbility: string = 'get windowStage'

  build() {
    Row() {
      Column() {
        Text(this.showAbility)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            console.info('Obtained WindowStage instance:',JSON.stringify(context.windowStage))
          });
      }
      .width('100%')
    }
    .height('100%')
  }
}

**Reference**

[onWindowStageCreate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#onwindowstagecreate)

[UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)
