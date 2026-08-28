# How do I obtain the height of the status bar and navigation bar?

Call the system-provided **getWindowAvoidArea** API to obtain the system avoid area, such as the status bar and navigation bar. The **topRect.height** property in the return value is the height of the system status bar, in px. The code snippet is as follows:

// MainAbility.ets
import { common, UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

/\*\*
 \* Get the height of the system status bar and navigation bar
 \* @param context
 \* @returns
 \*/
async function getWindowAvoidArea(context: common.UIAbilityContext): Promise<window.AvoidArea | null> {
  try {
    // The default area of the system includes the status bar and navigation bar
    const mainWindow = await window.getLastWindow(context);
    const avoidAreaType = window.AvoidAreaType.TYPE\_SYSTEM;
    const avoidArea = mainWindow.getWindowAvoidArea(avoidAreaType);
    const avoidAreaTypeNavigationBar = window.AvoidAreaType.TYPE\_NAVIGATION\_INDICATOR;
    const avoidAreaNavigationBar = mainWindow.getWindowAvoidArea(avoidAreaTypeNavigationBar);
    const height = avoidArea.topRect.height;
    const heightNavigationBar = avoidAreaNavigationBar.bottomRect.height;
    return avoidArea
  } catch (e) {
    console.log('getWindowAvoidArea fail');
    return null
  }
}

export default class MainAbility extends UIAbility {
  // do something
  async onWindowStageCreate(windowStage: window.WindowStage) {
    getWindowAvoidArea(this.context);
    windowStage.loadContent('pages/index');
  }

  // do something
}

**Reference**

[getWindowAvoidArea](<https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-uiextension#getwindowavoidarea >)
