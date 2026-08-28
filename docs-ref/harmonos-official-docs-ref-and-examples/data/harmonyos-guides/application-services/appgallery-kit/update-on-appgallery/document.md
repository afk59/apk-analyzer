# Update on AppGallery

This function provides version detection and in-app update reminders for apps that have been released, so that you can notify users of the latest version.

#### Use Cases

When your app is launched or a user proactively checks for a new version, you can use this service to determine if an update is available. If there is a new version, this service can display update reminders to users.

<table style="border-style: none;"><tbody><tr><td class="nocellnorowborder" style="border: none;" valign="top" width="37.21%"><div class="fignone"><span class="figcap"><b>Figure 1 </b>Version detection and update reminder</span></div></td><td class="cell-norowborder" style="border: none;" valign="top" width="62.79%"><div class="fignone"><span class="figcap"><b>Figure 2 </b>Version update page</span></div></td></tr><tr><td class="cellrowborder" style="border: none;" valign="top" width="37.21%"><p><span><img height="630.0639590000001" originheight="2848" originwidth="1276" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/jaLfz5FuSZ6z7Owxntr5rg/en-us_image_0000002371732717.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062058Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=95F0A6C690E5A2176E1AE6467D17FCD21288905FA5FFA7154ED23667323414FC" title="Click to enlarge" width="282.2925"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="62.79%"><p><span><img height="636.741091" originheight="2848" originwidth="1276" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/sC_Lg0seRqa8wXND7Nmwbw/en-us_image_0000002337894508.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062058Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=4BF2C36A6E01B971FE9C36E9E301DA6B2620C2F68F83E800A1CF6F1FC19DE732" title="Click to enlarge" width="285.285"></span></p></td></tr></tbody></table>

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/4tWw0t57SG2q6V2wwGRw9A/en-us_image_0000002337734732.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07D0FCBC18AE5FA4BAD77EC26382949ED802DB14FEDAA8AFD44A5AAC2584103B "Click to enlarge")

1.  The app calls the API for checking for updates.
2.  The API returns the result about whether a new version is available.
3.  Call the API for displaying an update pop-up.
4.  The display result is returned to the app.

#### Restrictions

-   The Update on AppGallery function supports phones, tablets, and PCs/2-in-1 devices. Starting from 5.1.1(19), it also supports TVs, and starting 6.0.0(20), it also supports wearables.
-   The Update on AppGallery function does not support the Emulator. Use a real device for debugging. If you use this service in the Emulator, the message "Unable to load content. Tap the screen to retry." will be displayed.
-   The app must have been released on AppGallery.

#### API Description

The update service provides the following APIs. For details, please refer to the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-updatemanager).

| 
API

 | 

**Description**

 |
| :-- | :-- |
| 

[checkAppUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-updatemanager#section10984155711373)(context: [common.UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)): Promise<[CheckUpdateResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-updatemanager#section1535385414136)\>

 | 

Detects whether a new version is available.

 |
| 

[showUpdateDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-updatemanager#section16502191111574)(context:[common.UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)): Promise<[ShowUpdateResultCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-updatemanager#section194882568246)\>

 | 

Displays an update pop-up.

 |

#### Development Procedure

## Detecting Whether a New App Version Is Available

1.  Import the **updateManager** module and related common modules.
    
    import { updateManager } from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import type { common } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Construct an input parameter, which is a context of the [common.UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) type.
    
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    
3.  Call the [checkAppUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-updatemanager#section10984155711373) method to check whether a new app version is available.
    
    try {
      updateManager.checkAppUpdate(context)
        .then((checkResult: updateManager.CheckUpdateResult) => {
          hilog.info(0, 'TAG', "Succeeded in checking Result updateAvailable:" + checkResult.updateAvailable);
        }).catch((error: BusinessError) => {
        hilog.error(0, 'TAG', \`checkAppUpdate onError.code is ${error.code}, message is ${error.message}\`);
      });
    } catch (error) {
      hilog.error(0, 'TAG', \`checkAppUpdate onError.code is ${error.code}, message is ${error.message}\`);
    }
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/E3nAte3iQSedrMHMaAWeIw/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C606191C13A76291C56472F72B6F0EFBA4BCD9B5DFC73A7B28E7C80086A1F296)

-   An update can be detected only if the locally installed version is lower than the version released on AppGallery.
-   The signature of the locally installed version must be the same as that of the version released on AppGallery.
-   Currently, closed testing and open testing are not supported.

## Displaying an Update Pop-up

1.  Import the **updateManager** module and related common modules.
    
    import { updateManager } from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import type { common } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Construct an input parameter, which is a context of the [common.UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) type.
    
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    
3.  Call the [showUpdateDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-updatemanager#section16502191111574) method to display the update pop-up.
    
    try {
      updateManager.showUpdateDialog(context)
        .then((resultCode: updateManager.ShowUpdateResultCode) => {
          hilog.info(0, 'TAG', "Succeeded in showing UpdateDialog resultCode:" + resultCode);
        })
        .catch((error: BusinessError) => {
          hilog.error(0, 'TAG', \`showUpdateDialog onError.code is ${error.code}, message is ${error.message}\`);
        });
    } catch (error) {
      hilog.error(0, 'TAG', \`showUpdateDialog onError.code is ${error.code}, message is ${error.message}\`);
    }
