# Requesting User Authorization

#### Use Cases

Screen Time Guard Kit supports time management and app restriction on user devices, but you have to obtain users' explicit authorization in advance. When your app calls the API for requesting user authorization, the system displays a dialog box, informing a user of the function purpose and necessity. The functions are available after the user grants authorization. If the user rejects to grant authorization, the functions of time management and app restriction will be unavailable. During API calls for using these functions, an error code indicating user authorization not granted will be returned.

#### User Experience Design

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/wu7hXTWqTBuUEgHGLRXkMg/en-us_image_0000002504465235.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CAC8D69C83BA3ABA721BB89CB733E5A71F0501C03CECA96FADE960502AB05B3E "Click to enlarge")

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/3HpZBZamRX2CUasjpJrx7g/en-us_image_0000002471625306.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78B1847E73A5531044E14D8DE64EB0A1330EB1985E4ADB92CD438F0BE892A3CB)

The process is as follows:

1\. To request the access to Screen Time Guard Kit, your app needs to call the API for requesting user authorization. Then, Digital Balance is started to query the app's authorization status in the local database.

2\. If the status is authorized, the result is directly returned. If the status is unauthorized, the dialog box for the user to grant authorization is displayed.

3\. If the user rejects to grant authorization, the corresponding error code is returned. If the user grants authorization, the result is returned.

#### API Description

The table below lists the key APIs for requesting user authorization. For details about the APIs, please refer to the [ArkTS APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-arkts).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[requestUserAuth](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section24022538179)(context: common.UIAbilityContext): Promise<void>

 | 

Requests user authorization to access related APIs of Screen Time Guard Kit.

 |
| 

[getUserAuthStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section12377142072717)(): Promise<[AuthStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section92636497495)\>

 | 

Obtains the user authorization status.

 |

#### Development Procedure

1\. Import required modules.

import { guardService } from '@kit.ScreenTimeGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

2\. Call **requestUserAuth** to request user authorization.

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button("TestRequestUserAuth")
        .onClick(async () => {
          try {
            await guardService.requestUserAuth(this.getUIContext().getHostContext() as common.UIAbilityContext);
          } catch (err) {
            const message = (err as BusinessError).message;
            const code = (err as BusinessError).code;
            hilog.error(0x0000, \`ScreenTimeGuard:requestUserAuth\`, \`requestUserAuth failed with error code: ${code}, message: ${message}\`);
          }
        })
    }
  }
}

3\. Obtain the user authorization status.

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button("TestGetUserAuthStatus")
        .onClick(async () => {
          try {
            const status = await guardService.getUserAuthStatus();
            hilog.info(0x0000, \`ScreenTimeGuard:getUserAuthStatus\`, \`user auth status: ${status}\`);
          } catch (err) {
            const message = (err as BusinessError).message;
            const code = (err as BusinessError).code;
            hilog.error(0x0000, \`ScreenTimeGuard:getUserAuthStatus\`, \`getUserAuthStatus failed with error code: ${code}, message: ${message}\`);
          }
        })
    }
  }
}
