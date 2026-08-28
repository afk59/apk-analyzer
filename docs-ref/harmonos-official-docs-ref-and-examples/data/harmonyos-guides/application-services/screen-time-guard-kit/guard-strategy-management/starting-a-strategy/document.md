# Starting a Strategy

#### Use Cases

When a user wants to start a guard strategy, your app can call the guard strategy start API with the strategy name passed. Digital Balance then starts it. Once the strategy is created and started, the system will perform user screen usage management based on this strategy.

#### User Experience Design

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/N60cyoHFQkiZDCBrJUNhaA/en-us_image_0000002504425165.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=50FDA9FDB66DC6DF07FB9027745457306FE67428ADDDFAAD9EAEEF7B0A09EDBD "Click to enlarge")

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/qNWGphORSHKNzfwp_LjAjw/en-us_image_0000002471625318.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73633F90DFCD6980120CD9CBFDABB53DB5480EC02052CA6FA2751700BFC70ABD)

The process is as follows:

1\. (Optional) Your app inherits from **TimeGuardExtensionAbility** to implement the **onStart** method.

2\. Your app calls the guard strategy start API. Then, Digital Balance is started to check whether your app has obtained the required permission and user authorization.

3\. If no, Digital Balance returns the corresponding error code. If yes, Digital Balance parses the strategy name passed in the parameter and checks whether the strategy exists.

4\. If the strategy does not exist, Digital Balance returns an error code. If the strategy exists, Digital Balance checks whether the strategy is being executed.

5\. If the strategy is not in execution, Digital Balance starts it and records its startup status. If the strategy is in execution, Digital Balance returns an error code indicating strategy in execution.

6\. After the strategy is started, the system time cannot be changed and the app that initiates the guard strategy cannot be uninstalled.

7\. The strategy takes effect at its scheduled activation time. The **extension** process is started to execute the **onStart** callback of **TimeGuardExtensionAbility**.

#### API Description

The table below lists the key APIs for starting a strategy. For details about the APIs, please refer to the [ArkTS APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-arkts).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[startGuardStrategy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section18918313999)(strategyName: string): Promise<void>

 | 

Starts a guard strategy based on the strategy name.

 |
| 

[onStart](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-timeguardextensionability#section7699846154419)(strategyName: string): Promise<void>

 | 

Executes specific logic when a guard strategy starts.

 |

#### Prerequisites

To start a guard strategy, you need to request user authorization first. For details, please refer to [Requesting User Authorization](../../user-authorization-management/requesting-user-authorization/document.md).

#### Development Procedure

1\. Import required modules.

import { guardService, TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

2\. Inherit from **TimeGuardExtensionAbility** and override the **onStart** callback.

export default class EntryAbility extends TimeGuardExtensionAbility {
  async onStart(strategyName: string): Promise<void> {
    hilog.info(0x0000, 'test --- onStart', strategyName);
  }
}

3\. Call **startGuardStrategy** to start a guard strategy.

async function testStartGuardStrategy() {
  try {
    const strategyName = "TestStrategy";
    await guardService.startGuardStrategy(strategyName);
  } catch (err) {
    const message = (err as BusinessError).message;
    const code = (err as BusinessError).code;
    hilog.error(0x0000, \`ScreenTimeGuard:startGuardStrategy\`, \`startGuardStrategy failed with error code: ${code}, message: ${message}\`);
  }
}
