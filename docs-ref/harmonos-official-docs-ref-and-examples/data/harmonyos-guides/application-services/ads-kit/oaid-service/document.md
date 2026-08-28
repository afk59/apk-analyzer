# OAID Service

#### Obtaining OAID Information

## Use Cases

An Open Anonymous Device Identifier (OAID) is a non-permanent device identifier. You can use OAIDs to provide personalized ads for users while protecting their privacy. In addition, third-party tracking platforms can provide conversion attributions for advertisers based on OAIDs.

No matter whether you are running an app, an ad platform, or a tracking platform, you can obtain OAID information from devices. The OAID information can be used to recommend personalized ads to users and attribute ad conversions.

An OAID is a 32-bit Universally Unique Identifier (UUID) generated using a Huawei algorithm. The format is xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.

To be specific, an OAID has the following features:

-   As a device-level identifier, OAIDs obtained by different apps on the same device are the same.
-   Whether an app can obtain a valid OAID is affected by the status of the **Activity tracking for this app** switch: When the switch is enabled, the app can obtain a valid OAID that is not composed of only zeros. When the switch is disabled, the app can obtain an OAID that contains only zeros.
-   An OAID is generated the first time an app on the device enables **Activity tracking for this app**.

The OAID changes in the following scenarios:

-   A user restores the device to factory settings.
-   A user resets the OAID.

## Restrictions

The OAID service supports phones, tablets, and PCs/2-in-1 devices. Starting from version 6.0.0(20), TVs are also supported.

## API Description

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[getOAID](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-oaid#identifiergetoaid)(): Promise<string>

 | 

Obtains an OAID. This API returns the result asynchronously through a promise.

 |
| 

[getOAID](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-oaid#identifiergetoaid-1)(callback: AsyncCallback<string>): void

 | 

Obtains an OAID. This API returns the result asynchronously through a callback.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/Tngf1-oBRVSjH4JX13t0-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=349B1DB88FD72FEFFDBDCD3B3EDFF31B3AA39DFDD6DF96ED53DE1C6244C30025)

To call **getOAID**, request the **ohos.permission.APP\_TRACKING\_CONSENT** permission and keep **Require consent to track** disabled. There are three situations:

1\. If the app has configured the **ohos.permission.APP\_TRACKING\_CONSENT** permission and **Activity tracking for this app** is set to **Allow**, the OAID is returned.

2\. If the app has configured the **ohos.permission.APP\_TRACKING\_CONSENT** permission and **Activity tracking for this app** is set to **Deny**, **00000000-0000-0000-0000-000000000000** is returned.

3\. If the app has not configured the **ohos.permission.APP\_TRACKING\_CONSENT** permission, **00000000-0000-0000-0000-000000000000** is returned.

## Development Procedure

1.  In the **module.json5** file of the module, request the activity tracking permission [ohos.permission.APP\_TRACKING\_CONSENT](../../../system/security/application-access-control/application-permission-management/application-permissions/open-user-grant-permissions/document.md#ohospermissionapp_tracking_consent), which is a **user\_grant** permission. For a **user\_grant** permission, **reason** and **abilities** are mandatory. For details about the configuration method, please refer to the [requestPermissions description](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md#declaring-permissions-in-the-configuration-file). The sample code is as follows:
    
    {
      "module": {
        "requestPermissions": \[
          {
            "name": "ohos.permission.APP\_TRACKING\_CONSENT",
            "reason": "$string:reason",
            "usedScene": {
              "abilities": \[
                "EntryFormAbility"
              \],
              "when": "inuse"
            }
          }
        \]
      }
    }
    
2.  To obtain OAID information, an app needs to call **requestPermissionsFromUser** to obtain the permission.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/T2tpK8TwTXeGfDdXm-Sf3Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=236707160D0D6EB8571EBF96610ABA4B859B16808E9D83BF22E5590D4B9ACD3B)
    
    For details about how to obtain the context, please click [here](../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/context-stage-model/document.md#acquisition-of-context).
    
    The sample code is as follows:
    
    import { abilityAccessCtrl, PermissionRequestResult } from '@kit.AbilityKit';
    import { identifier } from '@kit.AdsKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    async function requestOAID(context: Context): Promise<string | undefined> {
      // Request **Activity tracking for this app** from users.
      let isPermissionGranted: boolean = false;
      try {
        const atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
        const result: PermissionRequestResult =
          await atManager.requestPermissionsFromUser(context, \['ohos.permission.APP\_TRACKING\_CONSENT'\]);
        isPermissionGranted = result.authResults\[0\] === abilityAccessCtrl.GrantStatus.PERMISSION\_GRANTED;
      } catch (err) {
        hilog.error(0x0000, 'testTag', \`Failed to request permission. Code is ${err.code}, message is ${err.message}\`);
      }
      if (isPermissionGranted) {
        hilog.info(0x0000, 'testTag', 'Succeeded in requesting permission');
        try {
          const oaid = await identifier.getOAID();
          hilog.info(0x0000, 'testTag', 'Succeeded in getting OAID');
          return oaid;
        } catch (err) {
          hilog.error(0x0000, 'testTag', \`Failed to get OAID. Code is ${err.code}, message is ${err.message}\`);
        }
      } else {
        hilog.error(0x0000, 'testTag', 'Failed to request permission. User rejected');
      }
      return undefined;
    }
