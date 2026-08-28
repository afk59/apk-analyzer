# Place Details Display

#### Use Cases

This section describes how to integrate the place details display control. This control provides you with a convenient implementation solution for displaying place details, eliminating the need to develop the map page yourself. This control also allows users to start navigation by tapping **Directions** or initiate a ride request by tapping the ride hailing icon next to **Directions**. Please note that this control is not supported on smart watches currently.

**Figure 1** Place details  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/rRsVNT3dRQuo0g7A2F8gxw/en-us_image_0000002514923122.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FA5FB3ED57965932C2164BAA6BAF271E8AFBBEB61E8796B12654E43C611ECAC "Click to enlarge")

#### Constraints

To use this function, the following condition must be met:

-   The device must be a mobile phone, tablet, or 2-in-1 device.

#### API Description

Functions of this control are mainly provided by the [queryLocation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap#section177377424221) method in the [sceneMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap) namespace. For more information about the APIs, please refer to [sceneMap (Scenario-based Controls)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[LocationQueryOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap#section971194972117)

 | 

Parameters for querying place details.

 |
| 

[queryLocation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap#section177377424221)(context: common.[UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext), options: [LocationQueryOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap#section971194972117)): Promise<void>

 | 

Queries place details.

 |

#### Development Procedure

1.  Import required modules.
    
    import { sceneMap } from '@kit.MapKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { common } from '@kit.AbilityKit';
    
2.  Create parameters for querying place details and call the [queryLocation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap#section177377424221) method to display the place details page.
    
    // Method 1: Pass **siteId**.
    let queryLocationOptions: sceneMap.LocationQueryOptions = { 
      siteId: "922207154068557824" 
    };
    // Display the place details page.
    sceneMap.queryLocation(this.getUIContext().getHostContext() as common.UIAbilityContext, queryLocationOptions)
      .then(() => {
        console.info("QueryLocation", "Succeeded in querying location.");
      })
      .catch((err: BusinessError) => {
        console.error("QueryLocation", \`Failed to query Location, code: ${err.code}, message: ${err.message}\`);
      });
    
    // Method 2: Pass **location** and **name**.
    let queryLocationOptions: sceneMap.LocationQueryOptions = {
      location: {
        latitude: 39.9175,
        longitude: 116.3972
      },
      name: 'The Palace Museum'
    };
    // Display the place details page.
    sceneMap.queryLocation(this.getUIContext().getHostContext() as common.UIAbilityContext, queryLocationOptions)
      .then(() => {
        console.info("QueryLocation", "Succeeded in querying location.");
      })
      .catch((err: BusinessError) => {
        console.error("QueryLocation", \`Failed to query Location, code: ${err.code}, message: ${err.message}\`);
      });
