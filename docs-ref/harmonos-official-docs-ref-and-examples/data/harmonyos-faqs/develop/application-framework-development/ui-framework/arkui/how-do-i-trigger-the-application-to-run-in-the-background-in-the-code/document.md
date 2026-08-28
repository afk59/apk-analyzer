# How do I trigger the application to run in the background in the code?

The [minimize](<https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#minimize11 >) method can serve the purpose. If called in the main window, it minimizes the window, which can then be restored from the Dock bar. If called in the subwindow, it hides the window.

The code snippet is as follows:

Save **windowStage** globally in the **onWindowStageCreate** callback in **EntryAbility.ets**.

AppStorage.setOrCreate('context',windowStage);

Obtain **windowStage** on the page and call the method to minimize the window.

import { window } from '@kit.ArkUI';

@Component
export struct BackgroundExecution {
  @State message: string = 'Run in the background';

  build() {
    Column() {
      Button(this.message)
        .width('40%')
        .onClick(() => {
          let windowStage = AppStorage.get('context') as window.WindowStage;
          if (windowStage) {
            // It can be minimized when it is the main window and hidden when it is a sub-window.
            windowStage.getMainWindowSync().minimize();
          }
        })
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }
}
