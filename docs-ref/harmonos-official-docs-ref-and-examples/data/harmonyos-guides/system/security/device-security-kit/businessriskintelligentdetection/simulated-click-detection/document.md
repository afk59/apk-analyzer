# Simulated Click Detection

#### Use Cases

Starting from version 6.0.0(20), simulated click detection is supported.

An app calls the **detectSimulatedClickRisk** API of Device Security Kit to obtain the simulated click detection result for detecting cheating behaviors like automated clicks and device farming.

The app can evaluate how to perform service operations based on the detection result.

#### Restrictions

Each app can call the API for up to 10 times every 30 seconds and up to 20 times per day on each device.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/2gmpdL8fSzqjIBFE_B2dsg/en-us_image_0000002482788464.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062008Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7BEA1582153A2C33DBA688B3719FF666B7110374B6390B4C52BC0A3F83C8D5A6)

The process is as follows:

1.  Your app calls the **detectSimulatedClickRisk** API to initiate a simulated click detection request.
    
    After receiving the request, Device Security Kit collects the simulated click clue data of the current device, sends the clue data to the Device Security server for detection, and passes the detection result to your app through the return value of the **detectSimulatedClickRisk** API.
    
2.  Your app obtains the detection result and performs corresponding operations based on the result.

#### API Description

The following table lists the simulated click detection API. For more information about the API, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-brid-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[detectSimulatedClickRisk](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-brid-api#section8901423132412)(params: [SimulatedClickDetectionRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-brid-api#section157731058201714)): Promise<string>

 | 

Detects simulated clicks.

 |

#### Development Procedure

1.  Import the Device Security Kit module and related public modules.
    
    import { businessRiskIntelligentDetection } from '@kit.DeviceSecurityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Call the **detectSimulatedClickRisk** API to obtain the simulated click detection result.
    
    const TAG = "BusinessRiskIntelligentDetectionJsTest";
    
    let params = {
        version: 1
    } as businessRiskIntelligentDetection.SimulatedClickDetectionRequest;
    try {
        hilog.info(0x0000, TAG, 'Detect simulated click risk begin.');
        businessRiskIntelligentDetection.detectSimulatedClickRisk(params).then((result: string) => {
            hilog.info(0x0000, TAG, 'Detect simulated click risk success: %{public}s', result);
        }).catch((error: Error) => {
            let e: BusinessError = error as BusinessError;
            hilog.error(0x0000, TAG, 'Detect simulated click risk failed: %{public}d %{public}s', e.code, e.message);
        });
    } catch (error) {
        let e: BusinessError = error as BusinessError;
        hilog.error(0x0000, TAG, 'Detect simulated click risk failed: %{public}d %{public}s', e.code, e.message);
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/rYpEWGrmQsiwXLpNujvQgQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062008Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E7DD20C914AF00B9B8DF7FCBABDBA4A4525F8F17C6EF65B67832A6CBDDA8384)
    
    For details about the parameters, please refer to the parameter description of [detectSimulatedClickRisk](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-brid-api#section8901423132412).
