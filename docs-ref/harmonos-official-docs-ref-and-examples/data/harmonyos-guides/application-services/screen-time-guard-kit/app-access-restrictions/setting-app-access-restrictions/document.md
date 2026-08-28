# Setting App Access Restrictions

#### Use Cases

When a user wants to restrict user access to specific apps, your app can call the app access restriction setting API. Based on the app tokens and restriction type (trustlist/blocklist) passed to the API, Digital Balance either restricts user access to apps in the blocklist or allows users to access only apps in the trustlist.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/RhSe2p0zTEC38HSptzz4ag/en-us_image_0000002471465318.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4D8F7A5EE0ED046238D526D0AF1D3237C6B5ED3C520AECD50FC41F7E3580F03)

The process is as follows:

1\. Your app calls the app access restriction setting API. Then, Digital Balance is started to check whether your app has obtained the required permission and user authorization.

2\. If the required permission or user authorization is not available, Digital Balance returns an error code. If the required permission and user authorization have been obtained, Digital Balance parses the passed restriction type and app tokens, performs restrictions accordingly, and returns the result.

#### API Description

The table below lists the key API for app access restriction setting. For details about the API, please refer to the [ArkTS APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-arkts).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[setAppsRestriction](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section48957119226)(appInfo: [AppInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section76401996131), restrictionType: [RestrictionType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section119174813532)): Promise<void>

 | 

Restricts user access to apps in the blocklist or not in the trustlist based on the input app tokens and restriction type (trustlist/blocklist).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/hCeIruSoTvKQI9EjOyIEcA/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31FCE3F1AA580A4EA05C74027F2A8B37F5A7954957BDAC3F74DC70F765A61906)

**Description**

If the passed restriction type is blocklist, access to apps in the passed app list are restricted.

If the passed restriction type is trustlist, access to apps not in the passed app list are restricted.

**Boundary scenario**

1\. If an empty app list is passed and the restriction type is blocklist, no restriction is imposed on any apps. This means that no effective restrictions apply.

2\. If an empty app list is passed and the restriction type is trustlist, the access to all apps is restricted, except for system trustlist apps (such as Clock and Phone), the current app that initiates screen time guard, other authorized screen time guard apps, and the Digital Balance app.

3\. If an app's access restriction is configured repeatedly using this API, only the most recent setting will apply.

#### Prerequisites

To set app access restrictions, you need to request user authorization first. For details, please refer to [Requesting User Authorization](../../user-authorization-management/requesting-user-authorization/document.md).

#### Development Procedure

1\. Import required modules.

import { guardService, appPicker } from '@kit.ScreenTimeGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

2\. Call **setAppsRestriction** to set app access restrictions.

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button("TestSetAppsRestriction")
        .onClick(async () => {
          try {
            // Call **startAppPicker** first to obtain the app tokens.
            const tokens = await appPicker.startAppPicker(this.getUIContext().getHostContext(), { appTokens: \[\] });

            const appInfo: guardService.AppInfo = { appTokens: tokens };
            const restrictionType: guardService.RestrictionType = guardService.RestrictionType.BLOCKLIST\_TYPE;
            await guardService.setAppsRestriction(appInfo, restrictionType);
          } catch (err) {
            const message = (err as BusinessError).message;
            const code = (err as BusinessError).code;
            hilog.error(0x0000, \`ScreenTimeGuard:setAppsRestriction\`, \`setAppsRestriction failed with error code: ${code}, message: ${message}\`)
          }
        })
    }
  }
}
