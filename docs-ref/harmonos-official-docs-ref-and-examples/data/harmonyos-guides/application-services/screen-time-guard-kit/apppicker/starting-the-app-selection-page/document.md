# Starting the App Selection Page

#### Use Cases

In scenarios where users need to configure usage duration or access restriction strategies for specific apps, you can call the API for starting the app selection page. On the page, the users can select their target apps. The API will return the tokens of the selected apps after the users submit their selection. Then you can configure guard strategies for the apps based on the received tokens.

#### User Experience Design

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/uJ9a2LSNRqu3yLTO7SpUUQ/en-us_image_0000002505094635.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B37A5ED39B5BD63C7D0C2FA8783D8BBCAF8638978295564CF28D058096B238D0 "Click to enlarge")

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/Qc-VO2oBQVaWwW8Lm8Nt5g/en-us_image_0000002504894627.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1892D7655F1C63FD4F6EEA0DD7196E04E63AE538F2478D223E0D602F2EB3B7A1 "Click to enlarge")

The process is as follows:

1.  Your app calls the API for starting the app selection page. Then, Digital Balance is started to check whether your app has obtained the required permission and user authorization.
2.  If no, Digital Balance returns the corresponding error code. If yes, your app starts the app selection page and pre-selects apps based on the app token information passed.
3.  The app selection page converts the apps selected by the user into a token list and sends it to your app.

#### API Description

The table below lists the key API for starting the app selection page. For details about the API, please refer to the [ArkTS APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-arkts).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[startAppPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-app-picker#section11584125219191)(context: common.Context, appSelection: [guardService.AppInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section76401996131)): Promise<string\[\]>

 | 

Starts the app selection page.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/l-ddggKBQvWn5V7TtSKxxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A6165314D088B1EE7DF379915AD2291D6A09B7D09F555DE2D7EB62511CF090E4)

1.  The app list on the app selection page does not include the following system apps: Phone, Contacts, Settings, and Youth mode.
2.  The app list on the app selection page does not include the current app which initiates screen time guard, or other screen time guard apps authorized by users.

#### Prerequisites

To start the app selection page, you need to request user authorization first. For details, please refer to [Requesting User Authorization](../../user-authorization-management/requesting-user-authorization/document.md).

#### Development Procedure

1.  Import required modules.

import { appPicker } from '@kit.ScreenTimeGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

2.  Call **startAppPicker** to start the app selection page.

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button("TestStartAppPicker")
        .onClick(async () => {
          try {
            await appPicker.startAppPicker(this.getUIContext().getHostContext(), { appTokens: \[\] });
          } catch (err) {
            const message = (err as BusinessError).message;
            const code = (err as BusinessError).code;
            hilog.error(0x0000, \`ScreenTimeGuard:startAppPicker\`, \`startAppPicker failed error code: ${code}, message: ${message}\`);
          }
        })
    }
  }
}
