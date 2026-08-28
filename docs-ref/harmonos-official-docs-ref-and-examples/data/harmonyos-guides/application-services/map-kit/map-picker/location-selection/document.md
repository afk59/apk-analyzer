# Location Selection

#### Use Cases

This section describes how to integrate the location selection control. You can use this control to quickly implement location selection on a map without developing a map page. This control does not apply to smart watches.

<table style="border-style: none;"><tbody><tr><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><div class="fignone"><span class="figcap"><b>Figure 1 </b>Location selection screen</span></div><p><span><img height="680.63814" originheight="2688" originwidth="1216" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/4CF9HhSER0yQdZcIf6XOHQ/en-us_image_0000002514763792.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062113Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=9A26E32EE85C3F474B22B0B1DA09BFEF3C68B4D6691BE1765DE68822DD30B4A4" title="Click to enlarge" width="307.887286"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><div class="fignone"><span class="figcap"><b>Figure 2 </b>Location selection</span></div><p><span><img height="679.1957550000001" originheight="2688" originwidth="1216" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Zl8Ff1rPQ5qNLUOk4Jf7Xw/en-us_image_0000002515286050.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062113Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=3270E2E42C5E7634BEB64A260781743860593852F5B8B4C43E582C4F94702FDC" title="Click to enlarge" width="307.23"></span></p></td></tr></tbody></table>

#### Constraints

To use this function, the following condition must be met:

-   The device must be a mobile phone, tablet, or 2-in-1 device.

#### API Description

Functions of this control are mainly provided by the [chooseLocation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap#section927375116348) method in the [sceneMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap) namespace. For more information about the APIs, please refer to [sceneMap (Scenario-based Controls)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[LocationChoosingOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap#section1313113517227)

 | 

Parameters for selecting a location on the map.

 |
| 

[chooseLocation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap#section927375116348)(context: common.[UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext), options: [LocationChoosingOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap#section1313113517227)): Promise<[LocationChoosingResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap#section0471517192216)\>

 | 

Selects a location.

 |
| 

[LocationChoosingResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap#section0471517192216)

 | 

Location selection result.

 |

#### Development Procedure

1.  Import required modules.
    
    import { sceneMap } from '@kit.MapKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { common } from '@kit.AbilityKit';
    
2.  Create location selection parameters and call the [chooseLocation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-scenemap#section927375116348) method to display the location selection page.
    
    let locationChoosingOptions: sceneMap.LocationChoosingOptions = {
      // Coordinates of the map center point.
      location: { 
        latitude: 39.91804051376904,
        longitude: 116.3970536796932
      },
      // Display the search control.
      searchEnabled: true,
      // Display nearby POIs. 
      showNearbyPoi: true
    };
    // Display the location selection page.
    sceneMap.chooseLocation(this.getUIContext().getHostContext() as common.UIAbilityContext,
      locationChoosingOptions).then((data) => {
      console.info("ChooseLocation", "Succeeded in choosing location.");
    }).catch((err: BusinessError) => {
      console.error("ChooseLocation", \`Failed to choose location, code: ${err.code}, message: ${err.message}\`);
    });
