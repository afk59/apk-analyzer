# Obtaining Fraudulent Apps

#### Use Cases

An app calls the API of Device Security Kit to obtain fraudulent app information for anti-fraud purposes, such as reporting fraudulent apps.

#### Restrictions

Currently, this capability is supported only on phones and tablets. It is available only to anti-fraud apps.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/bPISgDxdSauT-nOEUd3xvw/en-us_image_0000002482788470.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062008Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03A94D12111CAC4C0ECA5A451CB5E9297BDFA3EC4C3A35EF8095E6A105417A53)

The process is as follows:

1.  A user selects the function of reporting fraudulent apps in your app.
2.  Your app calls the API of Device Security Kit to start the fraudulent app picker.
3.  The user selects fraudulent apps in the fraudulent app picker.
4.  Device Security Kit calls the callback function to notify your app of the selection result. Your app then processes the service based on the fraudulent app information.

#### API Description

The following table lists the API for obtaining fraudulent apps. For more information about the API, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-antifraudpicker-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

selectFraudApp(context: common.Context, options?: AntifraudAppOptions): Promise<AntifraudAppResult>

 | 

Obtains fraudulent app information.

 |

#### Development Procedure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/bNYiah9IQv-ypKageZfCGA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062008Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CCBD9E2F3225BCB2024F9F71FC47D2B2B331552D68705FECC8131D35FDE99699)

-   When preparing for the development, you need to apply for the **ohos.permission.USE\_FRAUD\_APP\_PICKER** permission.
-   Only apps in the trustlist can apply for this permission. For details about how to apply for this permission, please refer to [Requesting Restricted Permissions](../../../application-access-control/application-permission-management/requesting-application-permissions/requesting-restricted-permissions/document.md).
-   You need to inform users about the purpose, methods, and scope of data usage.

1.  Import the Device Security Kit module and related public modules.
    
    import { securityAudit } from '@kit.DeviceSecurityKit';
    import { BusinessError} from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { common} from '@kit.AbilityKit';
    
2.  Call the **selectFraudApp** API to obtain the fraudulent app information.
    
    const TAG = "AntifraudPickerJsTest";
    
    // Request to obtain the fraudulent app information and process the service.
    let options: antifraudPicker.AntifraudAppOptions = {
      maxSelectNumber: 5
    };
    try {
      hilog.info(0x0000, TAG, 'SelectFraudApp begin.');
      let context = this.getUIContext().getHostContext();
      const result: antifraudPicker.AntifraudAppResult = await antifraudPicker.selectFraudApp(context, options);
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, TAG, 'SelectFraudApp failed: %{public}d %{public}s', e.code, e.message);
    }
