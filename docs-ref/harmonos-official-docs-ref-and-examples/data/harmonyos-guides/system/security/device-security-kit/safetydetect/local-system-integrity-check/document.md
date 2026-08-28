# Local System Integrity Check

#### Use Cases

When not connected to the Device Security server, an app calls the **checkSysIntegrityOnLocal** API of Device Security Kit to obtain the system integrity check result and determine whether the device environment is secure, for example, whether the device environment has been jailbroken or the device is a non-real device.

The app can evaluate how to perform service operations based on the check result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/ytIWtD0XTq2KFwh5gTNOYg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C28AF5DC1C5789418BBAD708AC6A21798126FB6DA4C4BE23F2398C1E26E7D962)

-   The system integrity check result can be used as one of the system security proofs. You should consider relevant risks caused by possibly incorrect check results and the impacts to users. You are advised not to use the check result as the only proof to determine whether the current device is secure. It's better to take extra measures to further reduce risks.
-   This function is used only in scenarios where the Device Security server cannot be accessed.

#### Restrictions

-   The local system integrity check capability is supported on phones, tablets, PCs/2-in-1 devices, and wearables.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/c7znTB9_TE6dlKPMkWHzYg/en-us_image_0000002482908422.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD349327FC37C973232BAE997119B589778C8E71DA1A64B95F90D0E8FE178699)

The process is as follows:

1.  Your app calls the **checkSysIntegrityOnLocal** API to send a local system integrity check request.
2.  When receiving the request, Device Security Kit collects the required data to perform system integrity check.
3.  Device Security Kit returns the check result to your app through the **checkSysIntegrityOnLocal** API.
4.  Your app processes the service based on the check result. If the check result is **false**, you need to check the risk type in **detail** and determine whether to notify the user based on the risk type and your app's security requirements.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/HM-dxkm7ScWrTvcMaQuc2Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08A59D50D9456F95B6B42295100AF441226A23815F50A1CF8A1BD71C027B8162)

-   The local system integrity check result can be used as one of the system security proofs. You should consider relevant risks caused by possibly incorrect check results and the impacts to users. You are advised not to use the check result as the only proof to determine whether the current device is secure. It's better to take extra measures to further reduce risks.
-   To improve user experience when notifying users within the app, consider using friendly messages like:
    
    Your device might be at risk or running in an insecure environment. Please exercise caution when using the _XXX_ feature.
    

#### API Description

The following table lists the system integrity check API, which is an ArkTS API. For more information about the API, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-safetydetectenhanced-api#section83581542173818).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

checkSysIntegrityOnLocal(): Promise<string>

 | 

Checks system integrity.

 |

#### Development Procedure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/HK3G2EQuQGSQzv3pY3RzWw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77BE785163766FB1F5C197384211BFA898D40E7FA6D397E9BECCAAB41E190B4E)

Ensure that you have [enabled SafetyDetect](../../preparations/enabling-device-security-kit/document.md) and [requested the profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-profile-0000002270709473).

1.  Import the Device Security Kit module and related public modules.
    
    import { safetyDetect } from '@kit.DeviceSecurityKit';
    import { BusinessError } from '@ohos.base';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Call the API to obtain the system integrity check result.
    
    const TAG = "SafetyDetectJsTest";
    
    // Request local system integrity check and process the result.
    try {
      hilog.info(0x0000, TAG, 'CheckSysIntegrityOnLocal begin.');
      const result: string = await safetyDetect.checkSysIntegrityOnLocal();
      hilog.info(0x0000, TAG, 'Succeeded in checkSysIntegrityOnLocal: %{public}s', result);
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, TAG, 'CheckSysIntegrityOnLocal failed: %{public}d %{public}s', e.code, e.message);
    }
    
3.  Process the service in your app based on the check result. If the check result is **false**, you can determine whether to remind the user of the risks based on your security requirements.
    
    The local system integrity check result is a JSON string. The following is an example:
    
    {
      "basicIntegrity": false,
      "detail": \[
        "attack",
        "jailbreak",
        "emulator"
      \]
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/8KtOl1EQQdO87oiaQKiGGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F0EF7979DC23CAD2DBDEA2DE21359E3206DBD87793D9EB9EDA954B006F2646D)
    
    **basicIntegrity**: system integrity check result. The value **true** indicates that the system is integral, and the value **false** indicates there are risks.
    
    **detail**: optional field. When the value of **basicIntegrity** is **false**, this field provides the cause of the risk. You can make decisions accordingly based on the risk. The options are as follows:
    
    -   **jailbreak**: indicates that the device is jailbroken.
    -   **emulator**: indicates that the device is a non-real device.
    -   **attack**: indicates that the device is attacked.
    -   **unlock**: indicates that the device is unlocked.
