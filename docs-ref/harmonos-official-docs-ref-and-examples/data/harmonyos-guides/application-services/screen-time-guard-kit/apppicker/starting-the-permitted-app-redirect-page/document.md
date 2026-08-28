# Starting the Permitted App Redirect Page

#### Use Cases

Starting from version 6.0.2(22), the function of starting the permitted app redirect page is supported. To allow users to quickly access permitted apps when guard strategies are active, you can call the **startAppForm** API to start the app redirect page. This page displays the app list based on the permitted app tokens passed via the API parameter. Users can click an app icon on the page to launch the app.

#### User Experience Design

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/SvqRvwH7QXyZClRw_cm1VA/en-us_image_0000002505095767.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8D2AD68230B5433A598E0ECC89B8CA52E7A766716096631642AB7019A5D384A "Click to enlarge")

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/g8Cw9XsXQneJF2ikI60TZA/en-us_image_0000002474966400.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D310F606AB9BCCF1A97A4928977C3EF1C5F2CC66185EE7703505BE39B0CEA3D "Click to enlarge")

The process is as follows:

1\. Your app calls the API for starting the permitted app redirect page. Then, Digital Balance is started to check whether your app has obtained the required permission and user authorization.

2\. If no, Digital Balance returns the corresponding error code. If yes, your app obtains all apps based on the app token information passed, checks whether to display trusted apps, and then displays the app list form.

3\. A user clicks an app on the redirect page to launch the corresponding app.

#### API Description

The table below lists the key API for starting the permitted app redirect page. For details about the API, please refer to the [ArkTS APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-arkts).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[startAppForm](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-app-picker#section1486617762013)(context: common.Context, appSelection: [guardService.AppInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section76401996131), appSubTitle: string, displayTrustApp: boolean): Promise<void>

 | 

Starts the permitted app redirect page.

 |

#### Prerequisites

To start the permitted app redirect page, you need to request user authorization first. For details, please refer to [Requesting User Authorization](../../user-authorization-management/requesting-user-authorization/document.md).

#### Development Procedure

1\. Import required modules.

import { appPicker } from '@kit.ScreenTimeGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

2\. Call **startAppForm** to start the permitted app redirect page.

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button("TestStartAppForm")
        .onClick(async () => {
          try {
            // Call **startAppPicker** first to obtain the app tokens.
            const tokens = await appPicker.startAppPicker(this.getUIContext().getHostContext(), { appTokens: \[\] });

            await appPicker.startAppForm(this.getUIContext().getHostContext(), { appTokens: tokens }, "TestStartAppForm", false);
          } catch (err) {
            const message = (err as BusinessError).message;
            const code = (err as BusinessError).code;
            hilog.error(0x0000, \`ScreenTimeGuard:startAppForm\`, \`startAppForm failed error code: ${code}, message: ${message}\`);
          }
        })
    }
  }
}
