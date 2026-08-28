# Updating a Strategy

#### Use Cases

When a user wants to modify a screen time guard strategy, your app can call the guard strategy update API. Digital Balance then modifies the strategy based on the strategy name and modifications passed to the API, such as changing the app disablement start time and end time. Once the strategy is modified and recorded, the system manages user screen usage based on the updated strategy.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/byS2vqqQTvybgXQquTqmdw/en-us_image_0000002504425157.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A25F61E71C45A1D2B4A64C61F2E252A39D05CEC9596DDD6DBF6EDF3D43B5A04B)

The process is as follows:

1\. Your app calls the guard strategy update API. Then, Digital Balance is started to check whether your app has obtained the required permission and user authorization.

2\. If no, Digital Balance returns the corresponding error code. If yes, Digital Balance parses the passed strategy and then checks whether the strategy exists and whether it is valid.

3\. If the strategy exists and is valid, Digital Balance records it to the local database. Otherwise, Digital Balance returns an error code.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/TjJrBcAuReuGmV4ZYHfVhA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E53286C834AE1F3AC77456E56013330A63DC813BB817F3AD62200160B367400C)

1\. If the strategy name passed to the strategy update API does not exist, Digital Balance reports an error indicating strategy not existing.

#### API Description

The table below lists the key API for updating a strategy. For details about the API, please refer to the [ArkTS APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-arkts).

| 
API

 | 

**Description**

 |
| :-- | :-- |
| 

[updateGuardStrategy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section1863133395413)(strategyName: string, guardStrategy: [GuardStrategy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section188761911193713)): Promise<void>

 | 

Updates a screen time guard strategy.

 |

#### Prerequisites

To update a guard strategy, you need to request user authorization first. For details, please refer to [Requesting User Authorization](../../user-authorization-management/requesting-user-authorization/document.md).

#### Development Procedure

1\. Import required modules.

import { guardService, appPicker } from '@kit.ScreenTimeGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

2\. Call **updateGuardStrategy** to update a guard strategy.

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button("TestUpdateGuardStrategy")
        .onClick(async () => {
          try {
            // Call **startAppPicker** first to obtain the app tokens.
            const tokens = await appPicker.startAppPicker(this.getUIContext().getHostContext(), { appTokens: \[\] });

            const strategyName = "TestStrategy";
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
              name: strategyName,
              timeStrategy: time,
              appInfo: info,
              appRestrictionType: guardService.RestrictionType.BLOCKLIST\_TYPE
            }
            await guardService.updateGuardStrategy(strategyName, strategy);
          } catch (err) {
            const message = (err as BusinessError).message;
            const code = (err as BusinessError).code;
            hilog.error(0x0000, \`ScreenTimeGuard:updateGuardStrategy\`, \`updateGuardStrategy failed with error code: ${code}, message: ${message}\`);
          }
        })
    }
  }
}
