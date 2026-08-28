# Subscribing to Status Change Events

#### Use Cases

Starting from version 6.0.2(22), the function of subscribing to Super Privacy status change events is supported.

The Super Privacy mode allows users to disable sensitive components with just one tap. Currently, the sensitive components managed by the Super Privacy mode include the location service, camera, and microphone, and will be adjusted with the version evolution. Apps can call the API provided by Device Security Kit to listen for the Super Privacy status.

#### Restrictions

This feature requires that the Super Privacy option be available on the device. To check the option, go to **Settings** > **Privacy & security** > **Super Privacy** on the device.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/xFh-OXfBSKOnIppxqBEhGQ/en-us_image_0000002498258716.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062008Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2AFB5846BE1F55120C3514CC4297697CAE6E6BA5A403580E5F347FD5B72DA527 "Click to enlarge")

The process is as follows:

1.  Your HAP subscribes to Super Privacy status change events.
2.  Device Security Kit calls the callback function to notify your HAP of the status change.
3.  Your HAP processes services based on the current Super Privacy status.
4.  Your HAP unsubscribes from Super Privacy status change events when the Super Privacy status is no longer needed.

#### API Description

The following table lists the APIs for subscribing to and unsubscribing from Super Privacy status change events. For details, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-superprivacymode-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

on(type: 'superPrivacyModeChange', callback: Callback<[SuperPrivacyMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-superprivacymode-api#section11705111513)\>): void

 | 

Subscribes to Super Privacy status change events.

 |
| 

off(type: 'superPrivacyModeChange', callback?: Callback<[SuperPrivacyMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-superprivacymode-api#section11705111513)\>): void

 | 

Unsubscribes from Super Privacy status change events.

 |

#### Development Procedure

1.  Import the SuperPrivacyMode module and related public modules.
    
    import { superPrivacyMode } from '@kit.DeviceSecurityKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Subscribe to Super Privacy status change events.
    
    const DOMAIN = 0x0000;
    const TAG = "SuperPrivacyModeTest";
    
    const superPrivacyChangedCallback = (superPrivacyMode: superPrivacyMode.SuperPrivacyMode): void => {
      hilog.info(DOMAIN, TAG, \`super privacy mode changed, mode = ${superPrivacyMode}\`);
    }
    hilog.info(DOMAIN, TAG, 'start register super privacy mode changed listener');
    try {
      superPrivacyMode.on('superPrivacyModeChange', superPrivacyChangedCallback);
      hilog.info(DOMAIN, TAG, 'register super privacy mode change listener success');
    } catch (err) {
      hilog.error(DOMAIN, TAG, \`register super privacy changed listener failed, ${JSON.stringify(err)}\`);
    }
    
3.  Unsubscribe from Super Privacy status change events.
    
    hilog.info(DOMAIN, TAG, 'start unregister super privacy mode changed listener');
    try {
      superPrivacyMode.off('superPrivacyModeChange', superPrivacyChangedCallback);
    } catch (err) {
      hilog.error(DOMAIN, TAG, \`unregister super privacy changed listener failed, ${JSON.stringify(err)}\`);
    }
