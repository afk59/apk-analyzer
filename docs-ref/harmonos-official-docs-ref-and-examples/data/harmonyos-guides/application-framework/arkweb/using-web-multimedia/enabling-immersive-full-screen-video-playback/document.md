# Enabling Immersive Full-Screen Video Playback

ArkWeb provides events for entering and exiting the full-screen mode. An application can listen for these events to enter and exit the immersive full-screen mode.

When a **Web** component references a video loaded by a third-party HTML5 page and the video is displayed in full screen, the video is extended to the entire **Web** component area and cannot be displayed in full screen, as shown in Figure 2. To achieve the immersive full-screen video playback (as shown in Figure 3), an application needs to listen for the full-screen events and adjust the attributes of other components on the page.

| Figure 1 Exiting the full-screen mode | Figure 2 Non-immersive full-screen mode | Figure 3 Immersive full-screen mode |
| :-- | :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/RMeR0mTdQhyctqF5jdWJrg/en-us_image_0000002568764745.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FCB635B677A19D6D935C80CCD331ACFD6E509FF8572B4D6C306463D1CACF87ED) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/rT5XGBH_TUGyQSCZePm71g/en-us_image_0000002537765020.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0737B16EF3C6685C59FAF401ACE2640161C6D3D285A4E0DDAA18F5CD710597D5) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/OC-wZFZoQJqSr83uH1U1qg/en-us_image_0000002537924960.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27A309CE1CD4D3F5151C8E72CC1B25C984C69ACCDADF9060A6A37DBDDE429FAC) |

The **Web** component can use [onFullScreenEnter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-events#onfullscreenenter9) and [onFullScreenExit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-events#onfullscreenexit9) to listen for full-screen button click events. **OnFullScreenEnter** indicates that the **Web** component enters the full-screen mode, and **onFullScreenExit** indicates that the **Web** component exits the full-screen mode. In these two events, you can adjust some global variables based on the specific service scenario, such as the display status and **margin** attribute of the component, to implement the page effect of exiting and entering the immersive full-screen mode, as shown in Figure 1 and Figure 3.

The [visibility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-visibility) attribute is a common component attribute provided by ArkUI. You can control the visibility of a component by setting its **visibility** attribute.

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct ShortWebPage {
  controller: webview.WebviewController = new webview.WebviewController();
  CONSTANT\_HEIGHT = 100;
  @State marginTop: number = this.CONSTANT\_HEIGHT;
  @State isVisible: boolean = true; // Customize the isVisible flag to determine whether to display the component.

  build() {
    Column() {
      Text('TextTextTextText')
        .width('100%')
        .height(this.CONSTANT\_HEIGHT)
        .backgroundColor('#e1dede') // When isVisible is set to true, the component is visible. Otherwise, the component is invisible, not involved in layout, and no placeholder is used for it.
        .visibility(this.isVisible ? Visibility.Visible :
          Visibility.None)
      Web({
        src: $rawfile('FullScreen.html'), // Example website.
        controller: this.controller
      })
        .onFullScreenEnter((event) => {
          console.info('onFullScreenEnter...');
          // When the full screen is displayed, the isVisible flag is false, the component is invisible, not involved in layout, and no placeholder is used for it.
          this.isVisible = false;
        })
        .onFullScreenExit(() => {
          console.info('onFullScreenExit...');
          // When the full screen is exited, the isVisible flag is true, and the component is visible.
          this.isVisible = true;
        })
        .width('100%')
        .height('100%')
        .zIndex(10)
        .zoomAccess(true)
    }.width('100%').height('100%')
  }
}
