# Querying the Super Privacy Status

#### Use Cases

Starting from version 6.0.2(22), the function of querying the Super Privacy status on a device is supported.

The Super Privacy mode allows users to disable sensitive components with just one tap. Currently, the sensitive components managed by the Super Privacy mode include the location service, camera, and microphone, and will be adjusted with the version evolution. Apps can call the API provided by Device Security Kit to query the Super Privacy status.

#### Restrictions

This feature requires that the Super Privacy option be available on the device. To check the option, go to **Settings** > **Privacy & security** > **Super Privacy** on the device.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/Z610jj8rQRCvgvGC_JhrJg/en-us_image_0000002530018681.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062008Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F06760F8B4677603AD82C33D7A79EF00C14A1A4DD59A2141B07D85B8F9B0962A "Click to enlarge")

The process is as follows:

1.  Your HAP queries the Super Privacy status.
2.  The API of Device Security Kit returns the Super Privacy status to your HAP.
3.  Your HAP processes services based on the returned Super Privacy status.

#### API Description

The following table lists the API for querying the Super Privacy status. For more information about the API, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-superprivacymode-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[getSuperPrivacyMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-superprivacymode-api#section1339175183116)() : Promise<[SuperPrivacyMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-superprivacymode-api#section11705111513)\>

 | 

Queries the Super Privacy status.

 |

#### Development Procedure

1.  Import the SuperPrivacyMode module and related public modules.
    
    import { superPrivacyMode } from '@kit.DeviceSecurityKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Query the Super Privacy status change event.
    
    const DOMAIN = 0x0000;
    const TAG = "SuperPrivacyModeTest";
    
    let mode: superPrivacyMode.SuperPrivacyMode = superPrivacyMode.SuperPrivacyMode.OFF;
    try {
      mode = await superPrivacyMode.getSuperPrivacyMode();
      hilog.info(DOMAIN, TAG, \`Super privacy mode = ${mode}\`);
    } catch (err) {
      hilog.error(DOMAIN, TAG, \`call getSuperPrivacyMode interface failed, errCode:${err?.code}, errMessage:${err?.message}\`);
    }
