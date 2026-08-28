# How do I load a link with a hash (#) in the WebView?

Load the **src** of the **Web** component in the **'resource://rawfile/LoadWebLink.html#AAA'** format. For details, see the following code:

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct LoadWebLink {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    RelativeContainer() {
      Web({ src: 'resource://rawfile/LoadWebLink.html#AAA', controller: this.controller })
    }
    .height('100%')
    .width('100%')
  }
}
