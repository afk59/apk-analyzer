# Obtaining a Push Token

#### Use Cases

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/3JeVpdAPQq-tZXbdkXYU0w/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=935E6A8EFB1F98390168935846A56C4C31230EB37B87E9EB3EE485B9C3CA2AA7)

Push Kit will verify your relevant permissions when you obtain a push token. Before obtaining a push token, complete configurations described in [Enabling Push Kit](../enabling-push-kit/document.md).

A push token identifies each app on a user device. You can call the [getToken](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section562973524818)() API to request a push token from the Push Kit server and use the token to push messages.

Generally, the push token changes and the previous token becomes invalid only in the following scenarios:

-   A user uninstalls the app and then installs it again.
-   A user restores their device to factory settings.
-   The app calls the [deleteToken](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section1298316346493)() API in explicit mode and then calls the [getToken](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section562973524818)() API again.
-   The app calls the [deleteAAID](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-aaid-api#section18269336164311)() API in explicit mode and then calls the [getToken](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section562973524818)() API again.
-   When a wearable device leaves a country or region, the device's push token will be updated. The updated token can be returned through the callback of the [pushService.on('tokenUpdate')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section1730794845210) API.

Therefore, you are advised to call the **getToken()** API when your app is launched to check the push token. If the push token of the device changes, report the change to your app server in a timely manner to prevent message receiving failure due to the invalid push token.

#### Restrictions

The capability of obtaining a push token is supported on phones, tablets, PCs/2-in-1 devices, (since 5.1.0(18)) wearables, and (since 5.1.1(19)) TVs.

#### Precautions

-   Do not use push tokens to trace and mark users.
-   Do not let your app verify the push token length because it is variable.
-   Do not request push tokens frequently. You are advised to obtain a push token only when your app is launched.
-   Use the [getToken](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section562973524818) method to obtain a push token only after you perform operations in [Enabling Push Kit](../enabling-push-kit/document.md) in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html).

#### API Description

The APIs use either a callback or promise to return the result. The table below lists only the APIs that use a promise. The APIs that use a callback provide the same functions as their counterparts that use a promise.

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[getToken](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section562973524818)(): Promise<string>

 | 

Obtains a push token using a promise.

 |
| 

[deleteToken](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section1298316346493)(): Promise<void>

 | 

Deletes a push token using a promise.

 |

#### Obtaining a Push Token

1.  Push Kit will verify your relevant permissions when you obtain a push token. Before obtaining a push token, complete configurations described in [Enabling Push Kit](../enabling-push-kit/document.md).
2.  Import the **pushService** module and related common modules.
    
    import { pushService } from '@kit.PushKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
    
3.  You are advised to call the [getToken](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section562973524818)() API in the [onCreate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability#oncreate)() method of your **UIAbility** (for example, **EntryAbility**) to obtain the push token and report it to your app server so that your server can push messages to devices. Sample code:
    
    // File path: src/main/ets/entryability/EntryAbility.ets
    export default class EntryAbility extends UIAbility {
      // The input parameters **want** and **launchParam** are not actually used. They are defined during project initialization.
      onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        // Obtain a push token.
        pushService.getToken().then(token => {
          hilog.info(0x0000, 'testTag', 'Succeeded in getting push token');
        }).catch((err: BusinessError) => {
          hilog.error(0x0000, 'testTag', 'Failed to get push token: %{public}d %{public}s', err.code, err.message);
        })
        // Report the push token to both the Push Kit server and your server.
      }
    }
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/jO9OoJcqQWSaPjRf__6GCQ/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83EA3C1F65E218528C7BDE168F720AA37F271E06B084858E7853BECC043D1840)

If error code 1000900010 is reported (app authentication failure) when you obtain a push token, rectify the fault by referring to [ArkTS API Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-error-code#section3835124673016).

#### Deleting a Push Token

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/FKCvY3hWRImM8_7oWPdJ1Q/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60165BCD3F291F08DDB964A21B98DBCE42FD717A8F0D08C4CCFF4F10AE50A04F)

After a push token is deleted, all historical Push Kit data of the app will also be deleted. Call the [deleteToken](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section1298316346493)() API only when necessary.

1.  Import the pushService module.
    
    import { pushService } from '@kit.PushKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { UIAbility } from '@kit.AbilityKit';
    
2.  Call the **PushService.[deleteToken](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section1298316346493)()** API to delete the push token. Sample code:
    
    // File path: src/main/ets/entryability/EntryAbility.ets
    export default class EntryAbility extends UIAbility {
      async myDeletePushToken() {
        try {
          await pushService.deleteToken();
          hilog.info(0x0000, 'testTag', 'Succeeded in deleting push token');
        } catch (err) {
          let e: BusinessError = err as BusinessError;
          hilog.error(0x0000, 'testTag', 'Failed to delete push token: %{public}d %{public}s', e.code, e.message);
        }
      }
    }
    

#### Implementing Push Token Update Callback

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/7rjArvQ1RCmnwFKfQOdVMA/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4DFED4F8BA8FE6FFC2A53AECF45F54E1591656975CDD391DFF64A490F75668F)

This API can be used only on wearables currently.

When a device leaves a country or region, the push token may be automatically updated. If your app needs to detect the push token update event, call the **on()** method to register the callback. To deregister the callback so your app can stop receiving push token update events, call the **off()** method.

1.  Import the pushService module.
    
    import { pushService } from '@kit.PushKit';
    
2.  Import the **push** module to the ability (for example, **PushMessageAbility**) in your project and call the **on()** method to receive token update messages. Note that you can only use **UIAbility** to receive token update messages. Sample code:
    
    // File path: src/main/ets/abilities/PushMessageAbility.ets
    import { UIAbility } from '@kit.AbilityKit';
    import { pushService } from '@kit.PushKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    // You do not need to add a UIAbility. You can call the API in the **onCreate** method of the original UIAbility. Here, **PushMessageAbility** is used as an example.
    export default class PushMessageAbility extends UIAbility {
      onCreate(): void {
        const callBack = (data: string) => {
          try {
            hilog.info(0x0000, 'testTag', 'update token: %{public}s', data);
          } catch (e) {
            let err: BusinessError = e as BusinessError;
            hilog.error(0x0000, 'testTag', 'Failed to update data: %{public}d %{public}s', err.code, err.message);
          }
        }
    
        try {
          // Register a token update callback.
          pushService.on('tokenUpdate', this, callBack);
          hilog.info(0x0000, 'testTag', 'Register on success');
        } catch (e) {
          let err: BusinessError = e as BusinessError;
          hilog.error(0x0000, 'testTag', 'Register on error: %{public}d %{public}s', err.code, err.message);
        }
      }
    
      onDestroy(): void {
        try {
          // Callback for token update event deregistration.
          pushService.off('tokenUpdate');
          hilog.info(0x0000, 'testTag', 'Register off success');
        } catch (e) {
          let err: BusinessError = e as BusinessError;
          hilog.error(0x0000, 'testTag', 'Register off error: %{public}d %{public}s', err.code, err.message);
        }
      }
    }
    
3.  Set **actions** to **action.ohos.push.listener** in **skills** in the **abilities** section of the **src/main/module.json5** file at the project level. (This action can be defined for only one ability. **If the uris parameter also exists, it should be left empty.**)
    
    "abilities": \[
      {
        "name": "PushMessageAbility",
        "srcEntry": "./ets/abilities/PushMessageAbility.ets",
        "launchType": "singleton",
        "startWindowIcon": "$media:startIcon",
        "startWindowBackground": "$color:start\_window\_background",
        "exported": false,
        "skills": \[
          {
            "actions": \[
              "action.ohos.push.listener"
            \]
          }
        \]
      }
    \]
