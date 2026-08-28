# How do I set window rotation?

Step 1: Use [getLastWindow()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-f#windowgetlastwindow9), [createWindow()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-f#windowcreatewindow9), or [findWindow()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-f#windowfindwindow9) to obtain a **Window** instance.

Step 2: Call [setPreferredOrientation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#setpreferredorientation9) to set the window orientation. This API uses an asynchronous callback to return the result. The [Orientation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-display#orientation10) parameter indicates the window orientation type.

In the **onWindowStageCreate** method in **EntryAbility.ets**, set **windowStage** to AppStorage. The sample code is as follows:

AppStorage.setOrCreate('windowStage',windowStage);

Call **setPreferredOrientation** to set window rotation.

import { display, window } from '@kit.ArkUI';

@Component
struct ScreenRotation {
  windowStage: window.WindowStage = AppStorage.get('windowStage') as window.WindowStage;
  // Method to get the main window
  mainWin: window.Window = this.windowStage.getMainWindowSync();
  context = this.getUIContext();

  onPageShow() {
    // Method to get the top window
    window.getLastWindow(this.context.getHostContext());
    this.mainWin.setPreferredOrientation(window.Orientation.LANDSCAPE);
    // Use display interface to get current rotation direction, can be placed in listener for continuous updates
    display.getDefaultDisplaySync().rotation;
  }

  build() {
    Row() {
      Column({ space: 10 }) {
        Text('Screen rotation demo')
          .fontSize(25)
          .margin(20)
          .fontColor(0x3399FF)
      }.width('100%')
    }.height('100%').backgroundColor(Color.White)
  }
}
