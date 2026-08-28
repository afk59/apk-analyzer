# Removing App Access Restrictions

#### Use Cases

When a user wants to remove access restrictions for specific apps, your app can call the app access restriction removal API. Based on the passed app tokens and restriction type (trustlist/blocklist), Digital Balance parses the trustlist/blocklist and removes app access restrictions accordingly.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/IjGmTQwxR6WquW9rdZ2kvQ/en-us_image_0000002471465324.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B42D85E8C3F03E50BEF5A96192350C431BA2BF0BE929553E70E2E18CA1C0C605)

The process is as follows:

1\. Your app calls the app access restriction removal API. Then, Digital Balance is started to check whether your app has obtained the required permission and user authorization.

2\. If the required permission or user authorization is not available, Digital Balance returns an error code. If the required permission and user authorization have been obtained, Digital Balance parses the restriction type and app tokens passed in the parameters.

3\. Digital Balance checks whether an app in the passed app list is being managed by any guard strategy configured by a third-party app or Digital Balance itself. If yes, access restriction removal will not be performed for this app.

4\. Digital Balance removes access restrictions for other apps in the list and returns the result.

#### API Description

The table below lists the key API for app access restriction removal. For details about the API, please refer to the [ArkTS APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-arkts).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[releaseAppsRestriction](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section0894037112812)(appInfo: [AppInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section76401996131), restrictionType: [RestrictionType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section119174813532)): Promise<void>

 | 

Removes app access restrictions based on the passed app token array and restriction type (trustlist or blocklist).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/2bQxCsJ3QSOmxwG4zq3urw/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2E410C0D04387463C9B4D3A4D4F2E865890FBF6285A3FE1825ACFF0E6AF8DE3)

**Description**

If the passed restriction type is blocklist, access restrictions for the apps in the passed list are removed.

If the passed restriction type is trustlist, access restrictions for the apps not in the passed list are removed.

**Boundary scenario**

1\. If an empty app list is passed and the restriction type is blocklist, no restriction removal is performed.

2\. If an empty app list is passed and the restriction type is trustlist, access restrictions of all apps are removed, except for system trustlist apps (such as Clock and Phone), the current app that initiates screen time guard, other authorized screen time guard apps, and Digital Balance app.

3\. To remove a restriction for an app, the restriction type specified in the restriction removal operation must match that in the restriction setting operation. For instance, if an app was restricted using blocklist, you must use the blocklist type to remove that restriction. A parameter error will be returned if the types do not match or if no prior restriction was set for the app.

4\. To remove access restrictions for apps that are restricted in blocklist mode previously, pass all the apps to the API for a complete removal.

5\. If the app list passed to the API for removing access restrictions in blocklist mode contains an app that is not in the blocklist (or a passed app token is invalid), a parameter error will be returned.

6\. If the app list passed to the API for removing access restrictions in trustlist mode contains an app that is not in the trustlist (or a passed app token is invalid), a parameter error will be returned.

#### Prerequisites

To remove app access restrictions, you need to request user authorization first. For details, please refer to [Requesting User Authorization](../../user-authorization-management/requesting-user-authorization/document.md).

#### Development Procedure

1\. Import required modules.

import { guardService, appPicker } from '@kit.ScreenTimeGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

2\. Call **releaseAppsRestriction** to remove app access restrictions.

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button("TestReleaseAppsRestriction")
        .onClick(async () => {
          try {
            // Call **startAppPicker** first to obtain the app tokens.
            const tokens = await appPicker.startAppPicker(this.getUIContext().getHostContext(), { appTokens: \[\] });

            const appInfo: guardService.AppInfo = { appTokens: tokens };
            const restrictionType: guardService.RestrictionType = guardService.RestrictionType.BLOCKLIST\_TYPE;
            await guardService.releaseAppsRestriction(appInfo, restrictionType);
          } catch (err) {
            const message = (err as BusinessError).message;
            const code = (err as BusinessError).code;
            hilog.error(0x0000, \`ScreenTimeGuard:releaseAppsRestriction\`, \`releaseAppsRestriction failed with error code: ${code}, message: ${message}\`)
          }
        })
    }
  }
}
