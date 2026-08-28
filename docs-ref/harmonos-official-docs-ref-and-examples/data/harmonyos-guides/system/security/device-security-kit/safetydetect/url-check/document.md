# URL Check

#### Use Cases

An app calls the **checkUrlThreat** API of Device Security Kit to check whether a URL is malicious, and notifies the user or blocks the URL based on the check result.

Typical scenario: When a user visits a URL, this API checks whether the URL is malicious. If so, you can either warn the user of the risk or block the URL.

#### Restrictions

-   The URL check capability is supported on phones, tablets, and PCs/2-in-1 devices. Starting from version 5.1.0(18), it's also supported on wearables.
-   Each app can call the API for up to 10,000 times per day on each device. A maximum of five concurrent calls are supported on each device.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/hOXZc6DbT--4ObJB41huFQ/en-us_image_0000002514988413.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6E7432A5DD560D48088AB4A6C90C42A34415964134F2DAFE642DBFA973B83BE9 "Click to enlarge")

The process is as follows:

1.  Your app calls the **checkUrlThreat** API to pass the URL to be checked and obtain the URL check result.
    
    Device Security Kit sends the request to the Huawei server to check for URL threats and returns the check result (**NORMAL**, **PHISHING**, **MALWARE**, or **OTHERS**) to your app.
    
2.  Your app determines the service processing policy based on the check result.

#### API Description

The following table lists the URL check API, which is an ArkTS API. For more information about the API, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-arktsapi).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

checkUrlThreat(req: UrlCheckRequest): Promise<UrlCheckResponse>

 | 

Checks for URL threats.

 |

#### Development Procedure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/yeFTgvlOR_STZtm5x-HNmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3191F32E9CC5A23C9D7A9504899FD7D7D448F6A5088D6B5442D9281E78EDBAB2)

Ensure that you have [enabled SafetyDetect](../../preparations/enabling-device-security-kit/document.md) and [requested the profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-profile-0000002270709473).

1.  Import the Device Security Kit module and related public modules.
    
    import { safetyDetect } from '@kit.DeviceSecurityKit';
    import { BusinessError} from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Call the API to obtain the URL check result.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/J2-ImtfTT1e5h-l4wFQxBA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8B2E0B1D0130E26FCFD6529E4B236BA1BC3C84E9F8E00E420C4081D518B9DAF)
    
    This API involves device-cloud synergy and time-consuming operations such as network connection. Therefore, do not execute this API in the UI thread, in order to avoid UI thread blocking.
    
    const TAG = "SafetyDetectJsTest";
    
    // Request URL check and process the result.
    let req : safetyDetect.UrlCheckRequest = {
      urls : \['https://test1.com'\]
    };
    try {
      hilog.info(0x0000, TAG, 'CheckUrlThreat begin.');
      const data: safetyDetect.UrlCheckResponse = await safetyDetect.checkUrlThreat(req);
      hilog.info(0x0000, TAG, 'Succeeded in checkUrlThreat: %{public}s %{public}d', data.results\[0\].url, data.results\[0\].threat);
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, TAG, 'CheckUrlThreat failed: %{public}d %{public}s', e.code, e.message);
    }
