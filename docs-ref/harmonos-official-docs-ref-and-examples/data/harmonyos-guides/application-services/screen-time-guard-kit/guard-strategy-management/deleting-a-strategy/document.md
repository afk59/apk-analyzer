# Deleting a Strategy

#### Use Cases

When a user wants to delete a screen time guard strategy, your app can call the guard strategy deletion API. Digital Balance then deletes the strategy based on the strategy name passed to the API. Once the strategy is deleted, the user screen usage management based on this strategy is no longer performed.

#### User Experience Design

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/NYmk4c6vSf27yCBtAEKVrw/en-us_image_0000002471465328.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9461A8CB07B2FA7771026E1162E0D5904520EFA7B8881E9D8598F9B38A469F2E "Click to enlarge")

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/I0fcnqhLRXSoPoi2bDgPTQ/en-us_image_0000002504465241.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94934634D92382EDDFC8EE6047ABB1B85E994DD27247150C4FE786DA56396E8B)

The process is as follows:

1\. Your app calls the guard strategy deletion API. Then, Digital Balance is started to check whether your app has obtained the required permission and user authorization.

2\. If no, Digital Balance returns the corresponding error code. If yes, Digital Balance parses the strategy name passed in the parameter and checks whether the strategy exists.

3\. If the strategy does not exist, Digital Balance returns an error code. If the strategy exists, Digital Balance checks whether the strategy is being executed.

4\. If the strategy is in execution, Digital Balance stops its execution first and then deletes it.

#### API Description

The table below lists the key API for deleting a strategy. For details about the API, please refer to the [ArkTS APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-arkts).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[removeGuardStrategy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section116125615419)(strategyName: string): Promise<void>

 | 

Deletes a guard strategy.

 |

#### Prerequisites

To delete a guard strategy, you need to request user authorization first. For details, please refer to [Requesting User Authorization](../../user-authorization-management/requesting-user-authorization/document.md).

#### Development Procedure

1\. Import required modules.

import { guardService } from '@kit.ScreenTimeGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

2\. Call **removeGuardStrategy** to delete a guard strategy.

async function testRemoveGuardStrategy() {
  try {
    const strategyName = "TestStrategy";
    await guardService.removeGuardStrategy(strategyName);
  } catch (err) {
    const message = (err as BusinessError).message;
    const code = (err as BusinessError).code;
    hilog.error(0x0000, \`ScreenTimeGuard:removeGuardStrategy\`, \`removeGuardStrategy failed with error code: ${code}, message: ${message}\`);
  }
}
