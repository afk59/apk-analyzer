# Adding a Strategy

#### Use Cases

When a user wants to add a screen time guard strategy, your app can call the guard strategy creation API. Different strategies can be added, according to the passed parameters, such as the start time and end time specified for each app. Once the strategy is created and started, the system will perform user screen usage management based on this strategy.

#### User Experience Design

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/Vi4SVsZmS_uqQzz6g42WiA/en-us_image_0000002471465326.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=01A0F56516FE76300A0B95E86C9DB9F0E97B44AA95E896FFC22FF01CA562BC39 "Click to enlarge")

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/u8J3Dm2QQ1W3Zoj3J2wHmA/en-us_image_0000002471625312.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=017C50730E80C4E7FC2A2D7FE1C69B4A500B08FCFE593A7CCCE1740D31A7AD92)

The process is as follows:

1\. Your app calls the guard strategy creation API. Then, Digital Balance is started to check whether your app has obtained the required permission and user authorization.

2\. If no, Digital Balance returns the corresponding error code. If yes, Digital Balance parses the passed strategy and then checks whether the strategy is valid, whether the strategy is duplicate, and whether the total number of strategies is within the upper limit.

3\. If the strategy is valid and not duplicate and the total number of strategies is within the upper limit, Digital Balance records it to the local database. Otherwise, Digital Balance returns an error code.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/bBUOJjm4QOOKmRmihc_DAg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB3C6B3139DD41E27BA3F54462DE2F2AC1EA2C707CA8E7235C5E115C26275FEE)

1\. Guard strategies can be configured with a start/end time or a total duration. In both cases, the guard strategies will take effect in the specified period of time. You can also set a shared duration strategy, which allows all apps associated with the strategy to share the same duration quota. For details, please refer to [TimeStrategyType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section133401616145119).

2\. Guard strategies can be configured with a trustlist or a blocklist. If an app trustlist is configured, users can only access apps in the trustlist. If an app blocklist is configured, user access to apps in the blocklist is not allowed. For details, please refer to [RestrictionType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section119174813532).

3\. Guard strategies can be executed repeatedly within a week. A number array of digits ranging from 1 to 7 can be specified, indicating the execution days from Monday to Sunday. For details, please refer to [TimeStrategy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section7640121574612).

#### API Description

The table below lists the key API for adding a strategy. For details about the API, please refer to the [ArkTS APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-arkts).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[addGuardStrategy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section26135455267)(guardStrategy: [GuardStrategy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section188761911193713)): Promise<void>

 | 

Adds a screen time guard strategy.

 |

#### Prerequisites

To add a guard strategy, you need to request user authorization first. For details, please refer to [Requesting User Authorization](../../user-authorization-management/requesting-user-authorization/document.md).

#### Development Procedure

1\. Import required modules.

import { guardService, appPicker } from '@kit.ScreenTimeGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

2\. Call **addGuardStrategy** to add a screen time guard strategy.

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button("TestAddGuardStrategy")
        .onClick(async () => {
          try {
            // Call **startAppPicker** first to obtain the app tokens.
            const tokens = await appPicker.startAppPicker(this.getUIContext().getHostContext(), { appTokens: \[\] });

            const time: guardService.TimeStrategy = {
              type: guardService.TimeStrategyType.START\_END\_TIME\_TYPE,
              startTime: "08:00",
              endTime: "19:00",
              repeat: \[1,2,3\]
            }
            const info: guardService.AppInfo = {
              appTokens: tokens
            }
            const strategy: guardService.GuardStrategy = {
              name: "TestStrategy",
              timeStrategy: time,
              appInfo: info,
              appRestrictionType: guardService.RestrictionType.BLOCKLIST\_TYPE
            }
            await guardService.addGuardStrategy(strategy);
          } catch (err) {
            const message = (err as BusinessError).message;
            const code = (err as BusinessError).code;
            hilog.error(0x0000, \`ScreenTimeGuard:addGuardStrategy\`, \`addGuardStrategy failed with error code: ${code}, message: ${message}\`);
          }
        })
    }
  }
}
