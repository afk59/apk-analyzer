# How do I change the font color for the status bar?

You can use the [setWindowSystemBarProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#setwindowsystembarproperties9) method, which sets the properties of the navigation bar and status bar in the window, including the background color and font color of the status bar.

In **EntryAbility.ets**, modify the **onWindowStageCreate** callback. The code snippet is as follows:

AppStorage.setOrCreate('windowStage',windowStage);

Call **setWindowSystemBarProperties** to set the properties of the status bar.

import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Component
struct ChangeStatusBar {
  windowStage: window.WindowStage = AppStorage.get("windowStage") as window.WindowStage;
  // How to get the main window
  mainWin: window.Window = this.windowStage.getMainWindowSync();

  aboutToAppear(): void {
    let sysBarProps: window.SystemBarProperties = {
      statusBarColor: '#000000',
      statusBarContentColor: '#ffffff'
    };
    this.mainWin.setWindowSystemBarProperties(sysBarProps).then(() => {
      console.info('\[StaticUtils\] Succeeded in setting the system bar properties.');
    }).catch((err: BusinessError) => {
      console.error(\`setting system bar properties failed, code is ${err.code}, message is ${err.message}\`);
    });
  }

  build() {
    Row() {
      Column({ space: 10 }) {
        Text('Demo of modifying the status bar')
          .fontSize(25)
          .margin(20)
          .fontColor(0x3399FF)
      }.width('100%')
    }.height('100%').backgroundColor(Color.White)
  }
}
