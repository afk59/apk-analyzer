# How do I obtain the height of the navigation indicator at the bottom?

Call the [getWindowAvoidArea()](<https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-uiextension#getwindowavoidarea >) method of the window to obtain the avoid area, with type set to **AvoidAreaType.TYPE\_NAVIGATION\_INDICATOR**.

import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct GetBottomNavBarHeight {
  context = this.getUIContext();

  build() {
    Column() {
      Button('Get the height of the bottom gesture bar')
        .onClick(() => {
          let type = window.AvoidAreaType.TYPE\_NAVIGATION\_INDICATOR;
          window.getLastWindow(this.context.getHostContext()).then((data) => {
            let avoidArea = data.getWindowAvoidArea(type);
            // Get the height of the navigation bar area
            let bottomRectHeight = avoidArea.bottomRect.height;
            console.info(\`window bottomRectHeight is: ${bottomRectHeight}\`);
          }).catch((err: BusinessError) => {
            console.error(\`Failed to obtain the window. Cause: ${JSON.stringify(err)}\`);
          });
        })
    }
  }
}
