# Stopping a Strategy

#### Use Cases

When a user wants to stop a guard strategy, your app can call the guard strategy stop API with the strategy name passed. Digital Balance then stops it. Once the strategy is stopped, the user screen usage management based on this strategy is no longer performed.

#### User Experience Design

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/b2J7s1A_SqGN23momzkjUg/en-us_image_0000002471625322.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C73919461B849D2A9194F37451314CE60828E66B77C19335A278F1ADF245348B "Click to enlarge")

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/oDNYtJAPSWGmaaoVqu-ZdA/en-us_image_0000002471465334.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9746DBA064D88FCD40C53ABF98F94F41348E5A6D875C6BFCC01A5568AF7CBD77)

The process is as follows:

1\. (Optional) Your app inherits from **TimeGuardExtensionAbility** to implement the **onStop** method.

2\. Your app calls the guard strategy stop API. Then, Digital Balance is started to check whether your app has obtained the required permission and user authorization.

3\. If no, Digital Balance returns the corresponding error code. If yes, Digital Balance parses the strategy name passed in the parameter and checks whether the strategy exists.

4\. If the strategy does not exist, Digital Balance returns an error code. If the strategy exists, Digital Balance checks whether the strategy is being executed.

5\. If the strategy is in execution, Digital Balance stops it and the strategy is properly stopped. Then, Digital Balance records its stopped status. If the strategy is not in execution, Digital Balance returns an error code indicating that the strategy is not currently executing.

6\. If a strategy is stopped during its effective period, the **extension** process is started to execute the **onStop** callback of **TimeGuardExtensionAbility**. If a strategy is stopped when it is not effective, the **onStop** callback is not executed.

7\. After the strategy is stopped, if the app has no started strategies, the app can be uninstalled.

8\. After the strategy is stopped, if the device has no started strategies, the system time can be manually changed.

#### API Description

The table below lists the key APIs for stopping a strategy. For details about the APIs, please refer to the [ArkTS APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-arkts).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[stopGuardStrategy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section10788197141416)(strategyName: string): Promise<void>

 | 

Stops a guard strategy based on the strategy name.

 |
| 

[onStop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-timeguardextensionability#section62391222174814)(strategyName: string): Promise<void>

 | 

Executes specific logic when a guard strategy stops.

 |

#### Prerequisites

To stop a guard strategy, you need to request user authorization first. For details, please refer to [Requesting User Authorization](../../user-authorization-management/requesting-user-authorization/document.md).

#### Development Procedure

1\. Import required modules.

import { guardService, TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

2\. Inherit from **TimeGuardExtensionAbility** and override the **onStop** callback.

export default class EntryAbility extends TimeGuardExtensionAbility {
  async onStop(strategyName: string): Promise<void> {
    hilog.info(0x0000, 'test --- onStop', strategyName);
  }
}

3\. Call **stopGuardStrategy** to stop a guard strategy.

async function testStopGuardStrategy() {
  try {
    const strategyName = "TestStrategy";
    await guardService.stopGuardStrategy(strategyName);
  } catch (err) {
    const message = (err as BusinessError).message;
    const code = (err as BusinessError).code;
    hilog.error(0x0000, \`ScreenTimeGuard:stopGuardStrategy\`, \`stopGuardStrategy failed with error code: ${code}, message: ${message}\`);
  }
}
