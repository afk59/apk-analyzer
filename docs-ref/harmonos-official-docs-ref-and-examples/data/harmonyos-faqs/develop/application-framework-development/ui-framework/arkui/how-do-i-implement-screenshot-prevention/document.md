# How do I implement screenshot prevention?

To prevent screenshots or screen recording in your application, you can enable the window privacy mode. This is suitable for scenarios that require privacy protection on sensitive pages or windows.

Method 1: Enable privacy mode when entering the page, and disable it when leaving the page.

Declare the **ohos.permission.PRIVACY\_WINDOW** permission in the **module.json5** file.

"requestPermissions": \[
  {
    "name": "ohos.permission.PRIVACY\_WINDOW"
  }
\],

Use the **onNavBarStateChange** callback to set privacy mode based on page visibility. When the user accesses the page, **isVisible** is **true**, and **setWindowPrivacyMode** is called to enable privacy mode. When the user leaves the page, **isVisible** is **false**, and **setWindowPrivacyMode** is called to disable privacy mode. Refer to the code snippet below.

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

class WindowUtils {
  static setWindowPrivacyModeInPage(context: common.UIAbilityContext, isFlag: boolean) {
    window.getLastWindow(context).then((lastWindow) => {
      lastWindow.setWindowPrivacyMode(isFlag, (err: BusinessError) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error('Failed to set the window to privacy mode. Cause:' + JSON.stringify(err));
          return;
        }
        console.info('Succeeded in setting the window to privacy mode.');
      });
    })
  }
}

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  @Provide('NavPathStack') pageStack: NavPathStack = new NavPathStack();
  context = this.getUIContext();

  @Builder
  PagesMap(name: string) {
    if (name === 'Index') {
      Index();
    } else if (name === 'PageOne') {
      PageOne();
    }
  }

  build() {
    Navigation(this.pageStack) {
      Column() {
        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageStack.pushPath({ name: 'PageOne' }) // Push the page info of specified NavDestination into the stack
          })
      }
    }
    .navDestination(this.PagesMap)
    .onNavBarStateChange((isVisible: boolean) => {
      // Callback triggered when navigation bar display state changes
      console.info('------>isVisible:' + isVisible)
      WindowUtils.setWindowPrivacyModeInPage(this.context.getHostContext() as common.UIAbilityContext, isVisible);
    })
  }
}

@Component
struct PageOne {
  @Consume('NavPathStack') pageStack: NavPathStack;

  build() {
    NavDestination() {
      Column() {
        Text('PageOne')
      }
    }
    .title('pageOne')
    .onBackPressed(() => {
      const popDestinationInfo = this.pageStack.pop(); // Pop the top element from the navigation stack
      return true;
    })
  }
}

Method 2: Set the main window to privacy mode.

Declare the **ohos.permission.PRIVACY\_WINDOW** permission in the **module.json5** file.

"requestPermissions": \[
  {
    "name": "ohos.permission.PRIVACY\_WINDOW"
  }
\],

In the **onWindowStageCreate** callback in the **EntryAbility.ets** file, set the main window to privacy mode.

import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR\_MODE\_NOT\_SET);
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    // Get the main window
    windowStage.getMainWindow((err: BusinessError, data) => {
      let errCode: number = err.code;
      if (errCode) {
        console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
        return;
      }
      let windowClass: window.Window = data;
      console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));
      // Set the window privacy mode
      let isPrivacyMode: boolean = true;
      try {
        windowClass.setWindowPrivacyMode(isPrivacyMode, (err: BusinessError) => {
          const errCode: number = err.code;
          if (errCode) {
            console.error('Failed to set the window to privacy mode. Cause:' + JSON.stringify(err));
            return;
          }
          console.info('Succeeded in setting the window to privacy mode.');
        });
      } catch (exception) {
        console.error('Failed to set the window to privacy mode. Cause:' + JSON.stringify(exception));
      }
    })
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}

**Reference**

[setWindowPrivacyMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#setwindowprivacymode9), [onNavBarStateChange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-navigation#onnavbarstatechange9)
