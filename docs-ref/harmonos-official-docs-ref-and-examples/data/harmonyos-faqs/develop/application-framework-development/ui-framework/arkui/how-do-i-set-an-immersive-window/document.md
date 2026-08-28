# How do I set an immersive window?

In the **onWindowStageCreate** method of **EntryAbility**, obtain the window through **windowStage** and call the **setWindowLayoutFullScreen** and **setWindowSystemBarEnable** methods. The code snippet is as follows:

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // 1.Get the main window of the application.
    let windowClass: window.Window | null = null;
    windowStage.getMainWindow((err: BusinessError, data) => {
      let errCode: number = err.code;
      if (errCode) {
        console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
        return;
      }
      windowClass = data;
      console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));

      // 2.Realize immersive effects. Method 1: Set the navigation bar and status bar to not display.
      let names: Array<'status' | 'navigation'> = \[\];
      windowClass.setWindowSystemBarEnable(names).then(() => {
        console.info('Succeeded in setting the system bar to be visible.');
      });
      // 2.Realize immersive effects. Method 2: Set the window to a full screen layout, and coordinate with the transparency, background/text color, and highlighted icons of the navigation bar and status bar to maintain consistency with the main window display.
      let isLayoutFullScreen = true;
      windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
        console.info('Succeeded in setting the window layout to full-screen mode.');
      });
      let sysBarProps: window.SystemBarProperties = {
        statusBarColor: '#ff00ff',
        navigationBarColor: '#00ff00',
        statusBarContentColor: '#ffffff',
        navigationBarContentColor: '#ffffff'
      };
      windowClass.setWindowSystemBarProperties(sysBarProps).then(() => {
        console.info('Succeeded in setting the system bar properties.');
      });
    })
    // 3.Load the corresponding target page for the immersive window.
    windowStage.loadContent("pages/page2", (err: BusinessError) => {
      let errCode: number = err.code;
      if (errCode) {
        console.error('Failed to load the content. Cause:' + JSON.stringify(err));
        return;
      }
      console.info('Succeeded in loading the content.');
    });
  }
};

**Reference**

[Experiencing the Immersive Window Feature](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-window-stage#experiencing-the-immersive-window-feature)
