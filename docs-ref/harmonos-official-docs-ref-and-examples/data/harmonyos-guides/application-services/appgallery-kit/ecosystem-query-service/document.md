# Ecosystem Query Service

#### Use Cases

This service allows you to query operational information about your app or atomic service. Currently, it supports querying scene values and ad signature verification information. Scene values describe the paths through which users access an app and atomic service. You can use this service to query the scenario in which your app or atomic service is opened. We currently support querying scene values for atomic services, and will support the capability for apps in the future. Signature verification version queries come into play only when your app or atomic service encompasses advertising scenarios. It allows you to query the logic of processing ad signature verification parameters.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/e5lXBc_9TGiygFuewmAV-w/en-us_image_0000002371652949.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BEDBFF0F195FE05E1F1A13571758E9456FD8F99993337E678618045EC55D0B36 "Click to enlarge")

1.  You request to query the scene value of your app or atomic service, and query the ad signature verification version.
2.  Your app or atomic service calls the [getSelfSceneCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-scenemanager#section145261628122720) and [getAdsVerificationVersion](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-scenemanager#section552702811279) APIs to obtain the scene value and ad signature verification version, respectively.
3.  The APIs return the scene value and ad signature verification version to your app or atomic service.
4.  Your app or atomic service returns the result to you.

#### Restrictions

-   The ecosystem query service supports phones, tablets, and PCs/2-in-1 devices. Starting from 5.1.1(19), it also supports TVs.
-   If no scene value has been generated for your app or atomic service, [getSelfSceneCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-scenemanager#section145261628122720) will return an empty value.
-   The ecosystem query service does not support the Emulator. Use a real device for debugging.

#### API Description

The ecosystem query service provides the following APIs. For details, please refer to the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-scenemanager).

| 
API

 | 

**Description**

 |
| :-- | :-- |
| 

[getSelfSceneCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-scenemanager#section145261628122720)():string

 | 

Obtains the scene value of your app or atomic service.

 |
| 

[getAdsVerificationVersion](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-scenemanager#section552702811279)(): number

 | 

Obtains the ad signature verification version.

 |

#### Development Procedure

## Obtaining the Scene Value of Your App or Atomic Service

1.  Import the required modules.
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { sceneManager } from '@kit.AppGalleryKit';
    
2.  Call the [getSelfSceneCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-scenemanager#section145261628122720) method.
    
    try {
      const sceneCode: string = sceneManager.getSelfSceneCode();
      hilog.info(0, 'TAG', "Succeeded in getting SelfSceneCode res = " + sceneCode);
    } catch (error) {
      hilog.error(0, 'TAG', \`getSelfSceneCode failed. code is ${error.code}, message is ${error.message}\`);
    }
    

## Obtaining the Ad Signature Verification Version

1.  Import the required modules.
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { sceneManager } from '@kit.AppGalleryKit';
    
2.  Call the [getAdsVerificationVersion](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-scenemanager#section552702811279) method.
    
    try {
      const version: number = sceneManager.getAdsVerificationVersion();
      hilog.info(0, 'TAG', "Succeeded in getting AdsVerificationVersion res = " + version);
    } catch (error) {
      hilog.error(0, 'TAG', \`getAdsVerificationVersion failed. code is ${error.code}, message is ${error.message}\`);
    }
