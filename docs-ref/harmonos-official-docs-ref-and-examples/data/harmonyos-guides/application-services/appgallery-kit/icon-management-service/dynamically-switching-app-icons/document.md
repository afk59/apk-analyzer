# Dynamically Switching App Icons

AppGallery Kit enables apps to query custom icon information, switch to a custom icon, and revert to the default icon.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/k6BoXJosTNChEXpi0k83JA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062059Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11AB496D2C5FB122982DB08DD804131DFBF7940CD4579351F7AED6B733325355)

5.0.3(15) and later versions support dynamic icon switching.

#### Use Cases

-   Querying information about custom icons
    
    Query information about available custom icons in your app.
    
-   Switching to a custom icon
    
    Select an available custom icon that will be used by your app.
    
-   Reverting to the default icon
    
    Stop using the selected custom icon and revert to the default icon.
    

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/FSyGC5CgRfOFXP3Oxe9geA/en-us_image_0000002337894616.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062059Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=01F872B45C145ABD2A7EE856750603922A1939D4D142C90D50812B846B527E8F "Click to enlarge")

## Querying Information About Custom Icons

1.  A user requests to query information about available custom icons.
2.  Call the **queryDynamicIcons** API to obtain information about the custom icons.
3.  The API returns information about the custom icons to your app.
4.  Your app returns the result to the user.

## Switching to a Custom Icon

1.  A user requests to switch to a custom icon.
2.  Call the **selectDynamicIcon** API to switch to a custom icon.
3.  The API returns the selection result to your app.
4.  Your app returns the result to the user.

## Reverting to the Default Icon

1.  A user requests to revert to the default icon.
2.  Call the **disableDynamicIcon** API to disable the custom icon.
3.  The API returns the result to your app.
4.  Your app returns the result to the user.

#### Restrictions

-   The icon management service does not support the Emulator. Use a real device for debugging.
-   The icon management service is supported on phones, tablets, and PCs/2-in-1 devices. Support for wearables is available starting from 5.1.1(18), and for TVs starting from 5.1.1(19).

#### API Description

The icon management service provides the following APIs. For details about the APIs, please refer to the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/appgallery-appinfomanager).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[queryDynamicIcons](https://developer.huawei.com/consumer/en/doc/harmonyos-references/appgallery-appinfomanager#section887383520415)(): Promise<[DynamicIconInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/appgallery-appinfomanager#section1535385414136)\[\]>

 | 

Queries information about custom icons.

 |
| 

[selectDynamicIcon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/appgallery-appinfomanager#section16502191111574)(iconId: string): Promise<void>

 | 

Switches to a custom icon.

 |
| 

[disableDynamicIcon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/appgallery-appinfomanager#section984175210392)(): Promise<void>

 | 

Disables a custom icon and reverts to the default icon.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/06QrLOCGTxi7xVpBSNNNug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062059Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8EC2882697D046953829A10D0EA8B8057AB631213BA9075CDC55A42109ABE5B5)

From version 6.0.0(20), the **selectDynamicIcon(iconId: string): Promise<void>** API can return error code 1006800013.

#### Development Procedure

## Querying Information About Custom Icons

1.  Import the **appInfoManager** module and related common modules.
    
    import { appInfoManager } from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call the [queryDynamicIcons](https://developer.huawei.com/consumer/en/doc/harmonyos-references/appgallery-appinfomanager#section887383520415) method to obtain information about custom icons.
    
    try {
      appInfoManager.queryDynamicIcons()
        .then((queryResult: appInfoManager.DynamicIconInfo\[\]) => {
          hilog.info(0, 'TAG', "Succeeded in getting DynamicIconInfo size = " + queryResult.length);
          for (let i = 0; i < queryResult.length; i++) {
            hilog.info(0, 'TAG', "Succeeded in getting DynamicIconInfo iconUrl = " + queryResult\[i\]\["iconUrl"\] + ", iconId = " + queryResult\[i\]\["iconId"\] + ", enabled = "+queryResult\[i\]\["enabled"\]);
          }
        }).catch((error: BusinessError) => {
          hilog.error(0, 'TAG', "queryDynamicIcons failed, code: " + error.code + ", exception message: " + error.message);
        });
    } catch (error) {
      hilog.error(0, 'TAG', "queryDynamicIcons exception code: " + error.code + ", exception message: " + error.message);
    }
    

## Switching to a Custom Icon

1.  Import the **appInfoManager** module and related common modules.
    
    import { appInfoManager } from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call the [selectDynamicIcon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/appgallery-appinfomanager#section16502191111574) method to switch to a custom icon.
    
    try {
      let iconId: string = 'iconId';
      appInfoManager.selectDynamicIcon(iconId).then(() => {
          hilog.info(0, 'TAG', "Succeeded in selecting dynamic icon");
      }).catch((error: BusinessError) => {
        hilog.error(0, 'TAG', "selectDynamicIcon failed, code: " + error.code + ", exception message: " + error.message);
      });
    } catch (error) {
      hilog.error(0, 'TAG', "selectDynamicIcon exception code: " + error.code + ", exception message: " + error.message);
    }
    

## Reverting to the Default Icon

1.  Import the **appInfoManager** module and related common modules.
    
    import { appInfoManager } from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call the [disableDynamicIcon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/appgallery-appinfomanager#section984175210392) method to revert to the default icon.
    
    try {
      appInfoManager.disableDynamicIcon().then(() => {
          hilog.info(0, 'TAG', "Succeeded in disabling dynamic icon");
      }).catch((error: BusinessError) => {
        hilog.error(0, 'TAG', "disableDynamicIcon failed, code: " + error.code + ", exception message: " + error.message);
      });
    } catch (error) {
      hilog.error(0, 'TAG', "disableDynamicIcon exception code: " + error.code + ", exception message: " + error.message);
    }
