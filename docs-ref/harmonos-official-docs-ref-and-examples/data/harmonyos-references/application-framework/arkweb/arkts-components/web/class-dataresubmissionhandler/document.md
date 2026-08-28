# Class (DataResubmissionHandler)

Implements the **DataResubmissionHandler** object for resubmitting or canceling the web form data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/gH61WtfwSnukZnLAnysekQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC528F0C7415AC9C7832C47C836851CE570E05CDDC4BF67273A822ABE5DD6F66)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 9.
    
-   The sample effect is subject to the actual device.
    

#### constructor9+

constructor()

Constructs a **DataResubmissionHandler** object.

**System capability**: SystemCapability.Web.Webview.Core

#### resend9+

resend(): void

Resends the web form data.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onDataResubmitted((event) => {
          console.info('onDataResubmitted');
          event.handler.resend();
        })
    }
  }
}

#### cancel9+

cancel(): void

Cancels the resending of web form data.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onDataResubmitted((event) => {
          console.info('onDataResubmitted');
          event.handler.cancel();
        })
    }
  }
}
