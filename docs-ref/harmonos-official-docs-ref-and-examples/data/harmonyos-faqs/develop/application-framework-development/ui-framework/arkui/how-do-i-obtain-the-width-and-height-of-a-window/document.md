# How do I obtain the width and height of a window?

Use **getWindowProperties** to obtain the window properties, among which **windowRect** indicates the window width and height. The sample code is as follows:

import { window } from '@kit.ArkUI';

@Entry
@Component
struct WindowProperties {
  context = this.getUIContext();

  build() {
    Text("Scroll Area")
      .width("100%")
      .height("100%")
      .backgroundColor(0X330000FF)
      .fontSize(16)
      .textAlign(TextAlign.Center)
      .onClick(() => {
        window.getLastWindow(this.context.getHostContext()).then((data) => {
          // get window attribute
          let properties = data?.getWindowProperties();
          // Get window width and height
          console.log("windowClass width: " + properties.windowRect.width);
          console.log("windowClass height: " + properties.windowRect.height);
        });
      })
  }
}

**Reference**

[WindowRect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-dialogrequest#windowrect10)
