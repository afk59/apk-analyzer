# Obtaining Fraudulent Call Logs

#### Use Cases

An app calls the API of Device Security Kit to obtain fraudulent call logs for anti-fraud purposes, such as reporting fraudulent call logs.

#### Restrictions

Currently, this capability is supported only on phones and tablets. It is available only to anti-fraud apps.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/789oux3VTLSB9pwPUrFPMA/en-us_image_0000002482788460.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062008Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8EE370494442E358011687627020CFEBF747369ACEAB50986952810B13E78AD6)

The process is as follows:

1.  A user selects the function of reporting fraudulent call logs in your app.
2.  Your app calls the API of Device Security Kit to start the fraudulent call log picker.
3.  The user selects fraudulent call logs in the fraudulent call log picker.
4.  Device Security Kit calls the callback function to notify your app of the selection result. Your app then processes the service based on the fraudulent call log information.

#### API Description

The following table lists the API for obtaining fraudulent call logs. For more information about the API, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-antifraudpicker-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

selectFraudCallLog(context: common.Context, options?: AntifraudCallLogOptions): Promise<AntifraudCallLogResult>

 | 

Obtains fraudulent call logs.

 |

#### Development Procedure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/NsYGbiFNQGKrTZSJ4CGC_Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062008Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=230C850F01E40D0FDF6880CF76EA8508474BEADF41A14D70E00EBF188578F2A7)

-   When preparing for the development, you need to apply for the **ohos.permission.USE\_FRAUD\_CALL\_LOG\_PICKER** permission.
-   Only apps in the trustlist can apply for this permission. For details about how to apply for this permission, please refer to [Requesting Restricted Permissions](../../../application-access-control/application-permission-management/requesting-application-permissions/requesting-restricted-permissions/document.md).
-   You need to inform users about the purpose, methods, and scope of data usage.

1.  Import the Device Security Kit module and related public modules.
    
    import { securityAudit } from '@kit.DeviceSecurityKit';
    import { BusinessError} from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { common} from '@kit.AbilityKit';
    
2.  Call the **selectFraudCallLog** API to obtain the fraudulent call log information.
    
    const TAG = "AntifraudPickerJsTest";
    
    // Request to obtain the fraudulent call log information and process the service.
    let options: antifraudPicker.AntifraudCallLogOptions = {
      maxSelectNumber: 5
    };
    try {
      hilog.info(0x0000, TAG, 'SelectFraudCallLog begin.');
      let context = this.getUIContext().getHostContext();
      const result: antifraudPicker.AntifraudCallLogResult = await antifraudPicker.selectFraudCallLog(context, options);
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, TAG, 'SelectFraudCallLog failed: %{public}d %{public}s', e.code, e.message);
    }
