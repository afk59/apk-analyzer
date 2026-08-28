# Obtaining Fraudulent Messages

#### Use Cases

An app calls the API of Device Security Kit to obtain fraudulent message information for anti-fraud purposes, such as reporting fraudulent messages.

#### Restrictions

Currently, this capability is supported only on phones and tablets. It is available only to anti-fraud apps.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/VtbWZ1uOSwCE5bfIweTOng/en-us_image_0000002482908438.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062008Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C872348D0A7DC9E2E7A6CFA3A30A83633EB40E23885643652D1DE67929D21136)

The process is as follows:

1.  A user selects the function of reporting fraudulent messages in your app.
2.  Your app calls the API of Device Security Kit to start the fraudulent message picker.
3.  The user selects fraudulent messages in the fraudulent message picker.
4.  Device Security Kit calls the callback function to notify your app of the selection result. Your app then processes the service based on the fraudulent message information.

#### API Description

The following table lists the API for obtaining fraudulent messages. For more information about the API, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-antifraudpicker-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

selectFraudMessage(context: common.Context, options?: AntifraudMessageOptions): Promise<AntifraudMessageResult>

 | 

Obtains fraudulent message information.

 |

#### Development Procedure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/dK1jMP4FS2-Jhbfg6iV1Ww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062008Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C83C306FF31EB1AA770E8AD849BCDDAB2960A3E64B0E4529F2FE6FF5C12E653E)

-   When preparing for the development, you need to apply for the **ohos.permission.USE\_FRAUD\_MESSAGES\_PICKER** permission.
-   Only apps in the trustlist can apply for this permission. For details about how to apply for this permission, please refer to [Requesting Restricted Permissions](../../../application-access-control/application-permission-management/requesting-application-permissions/requesting-restricted-permissions/document.md).
-   You need to inform users about the purpose, methods, and scope of data usage.

1.  Import the Device Security Kit module and related public modules.
    
    import { antifraudPicker} from '@kit.DeviceSecurityKit';
    import { BusinessError} from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { common} from '@kit.AbilityKit';
    
2.  Call the **selectFraudMessage** API to obtain the fraudulent message information.
    
    const TAG = "AntifraudPickerJsTest";
    
    // Request to obtain the fraudulent message information and process the service.
    let options: antifraudPicker.AntifraudMessageOptions = {
      maxSelectNumber: 5
    };
    try {
      hilog.info(0x0000, TAG, 'SelectFraudMessage begin.');
      let context = this.getUIContext().getHostContext();
      const result: antifraudPicker.AntifraudMessageResult = await antifraudPicker.selectFraudMessage(context, options);
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, TAG, 'SelectFraudMessage failed: %{public}d %{public}s', e.code, e.message);
    }
