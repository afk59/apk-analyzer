# Querying Strategies

#### Use Cases

When a user wants to view all screen time guard strategies, your app can call the guard strategy query API. The query result will be displayed for users to browse strategy information, such as the disablement start time and end time and app usage time limit.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/pkXIHeKrRueEasklD8h2-A/en-us_image_0000002504425159.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD6FA1122C3BDCE9A3D514280B74448BE08B6364C2636C57B23B3FC7785B4DCE)

The process is as follows:

1\. Your app calls the guard strategy query API. Then, Digital Balance is started to check whether your app has obtained the required permission and user authorization.

2\. If yes, Digital Balance returns all guard strategies to your app. If no, Digital Balance returns the corresponding error code.

#### API Description

The table below lists the key API for querying strategies. For details about the API, please refer to the [ArkTS APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-arkts).

| 
API

 | 

**Description**

 |
| :-- | :-- |
| 

[queryGuardStrategies](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section1812105318579)(): Promise<[GuardStrategy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section188761911193713)\[\]>

 | 

Queries all guard strategies under your app.

 |

#### Prerequisites

To query guard strategies, you need to request user authorization first. For details, please refer to [Requesting User Authorization](../../user-authorization-management/requesting-user-authorization/document.md).

#### Development Procedure

1\. Import required modules.

import { guardService } from '@kit.ScreenTimeGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

2\. Call **queryGuardStrategy** to query all guard strategies for your app.

async function testQueryGuardStrategies() {
  try {
    let guardStrategy: guardService.GuardStrategy\[\] = await guardService.queryGuardStrategies();
    guardStrategy.forEach((element) => {
      hilog.info(0x0000, \`ScreenTimeGuard:queryGuardStrategies\`, \`${element.name}\`)
    })
  } catch (err) {
    const message = (err as BusinessError).message;
    const code = (err as BusinessError).code;
    hilog.error(0x0000, \`ScreenTimeGuard:queryGuardStrategies\`, \`queryGuardStrategies failed with error code: ${code}, message: ${message}\`);
  }
}
