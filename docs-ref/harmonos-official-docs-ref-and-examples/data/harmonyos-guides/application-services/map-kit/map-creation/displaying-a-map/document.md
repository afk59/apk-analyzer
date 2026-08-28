# Displaying a Map

#### Use Cases

Starting from 5.0.3(15), the logo scaling and 3D globe view functions are supported. Starting from 5.1.1(19), the indoor map and scale unit setting functions are supported. Starting from 6.0.0(20), the map language setting function is supported.

This section describes how to use the map components [MapComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-mapcomponent#section816451553012) and [MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller) to display a map, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/LnVGE5o0T9a8BY3v8t5IUQ/en-us_image_0000002514096834.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=849594F2729DD4C199FF80B6914BF674397EBFFCBDEAB1819166C58F71E2BAB7 "Click to enlarge")

#### API Description

The map display function is mainly provided by [MapComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-mapcomponent#section816451553012). For more information about the APIs, please refer to [MapComponent (Map Component)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-mapcomponent).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[mapCommon.MapOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section816451553012)

 | 

Sets initialization attributes of a map component.

 |
| 

[MapComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-mapcomponent#section816451553012)(mapOptions: [mapCommon.MapOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section816451553012), mapCallback: AsyncCallback<[map.MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller)\>)

 | 

Map component.

 |
| 

[map.MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller)

 | 

Main entry class for map operations. It provides access for all map-related methods. It provides the following functions: switching the map type (such as standard map and empty map), changing the map status (coordinates of the map center point and zoom level), adding Markers, drawing geometric shapes (including MapPolyline, MapPolygon, and MapCircle), and listening for various events.

 |

#### Development Procedure

## Map Display

1.  Import required modules of Map Kit.
    
    import { MapComponent, mapCommon, map } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Create the map initialization parameter **mapOptions** and set the coordinates of the map center point and zoom level.
    
    Obtain a [MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller) object in callback mode to operate the map.
    
    Call the [MapComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-mapcomponent#section816451553012) component and pass the **mapOptions** and **mapCallback** parameters to initialize the map.
    
    @Entry
    @Component
    struct HuaweiMapDemo {
      private TAG = "HuaweiMapDemo";
      private mapOptions?: mapCommon.MapOptions;
      private callback?: AsyncCallback<map.MapComponentController>;
      private mapController?: map.MapComponentController;
      private mapEventManager?: map.MapEventManager;
    
      aboutToAppear(): void {
        // Map initialization parameters used to set the coordinates of the map center point and zoom level.
        this.mapOptions = {
          position: {
            target: {
              latitude: 39.9,
              longitude: 116.4
            },
            zoom: 10
          }
        };
    
        // Map initialization callback.
        this.callback = async (err, mapController) => {
          if (!err) {
            // Obtain **mapController** to operate the map.
            this.mapController = mapController;
            this.mapEventManager = this.mapController.getEventManager();
            let callback = () => {
              console.info(this.TAG, \`on-mapLoad\`);
            }
            this.mapEventManager.on("mapLoad", callback);
          } else {
            console.error(\`Failed to initialize the map. Code: ${err.code}; message: ${err.message}\`);
          }
        };
      }
    
      // This is called each time the page is displayed, for example, during page redirection or when the app is switched to the foreground. It works only for the custom components decorated using **@Entry**.
      onPageShow(): void {
        // Switch the map to the foreground.
        if (this.mapController) {
          this.mapController.show();
        }
      }
    
      // This is called each time the page is hidden, for example, during page redirection or when the app is switched to the background. It works only for the custom components decorated using **@Entry**.
      onPageHide(): void {
        // Switch the map to the background.
        if (this.mapController) {
          this.mapController.hide();
        }
      }
    
      build() {
        Stack() {
          // Call the **MapComponent** component to initialize the map.
          MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback }).width('100%').height('100%');
        }.height('100%')
      }
    }
    
3.  Run the project, and you can view the map in your app, as shown in the screenshot below.
    
    If the map fails to be loaded, see [Map Not Displayed](../../faqs/map-not-displayed/document.md).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/CI4tqANHSMiPQEmdPX_72w/en-us_image_0000002514097264.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9A5806B32964994EA90399B2D30A7EDFE2B54FCE359F86D6A123D104B0A0EA4 "Click to enlarge")
    

## Setting Map Attributes

The following table describes attributes of [MapOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section816451553012).

| 
Attribute

 | 

Description

 |
| :-- | :-- |
| 

mapType

 | 

Map type. The default value is [MapType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#en-us_topic_0000001245084266_section18522846142615).STANDARD.

 |
| 

position

 | 

Map camera position.

 |
| 

bounds

 | 

Map display box.

 |
| 

minZoom

 | 

Minimum zoom level of a map, which ranges from 2 to 20. The default value is **2**.

 |
| 

maxZoom

 | 

Maximum zoom level of a map, which ranges from 2 to 20. The default value is **20**.

 |
| 

rotateGesturesEnabled

 | 

Indicates whether to support rotate gestures. The default value is **true**.

 |
| 

scrollGesturesEnabled

 | 

Indicates whether to support scroll gestures. The default value is **true**.

 |
| 

zoomGesturesEnabled

 | 

Indicates whether to support zoom gestures. The default value is **true**.

 |
| 

tiltGesturesEnabled

 | 

Indicates whether to support tilt gestures. The default value is **true**.

 |
| 

zoomControlsEnabled

 | 

Indicates whether to display the zoom control. The default value is **true**.

 |
| 

myLocationControlsEnabled

 | 

Indicates whether to display the my-location icon. The default value is **false**.

 |
| 

compassControlsEnabled

 | 

Indicates whether to display the compass control. The default value is **true**.

 |
| 

scaleControlsEnabled

 | 

Indicates whether to display the scale control. The default value is **false**.

 |
| 

alwaysShowScaleEnabled

 | 

Indicates whether to always display the scale control. The default value is **false**.

 |
| 

padding

 | 

Padding round the edges of the map.

 |
| 

styleId

 | 

Custom style ID.

 |
| 

dayNightMode

 | 

Day/Dark mode. The default value is [DayNightMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section634916281725).DAY.

 |
| 

logoScale

 | 

Logo scaling ratio. The value range is \[0.8, 1\]. The default value is **1**.

 |
| 

sphereEnabled

 | 

Indicates whether to enable the 3D globe view. The default value is **false**.

 |
| 

indoorMapEnabled

 | 

Indicates whether to enable the indoor map. The default value is **false**.

 |
| 

scaleUnit

 | 

Map scale unit, metric or imperial. The default value is [ScaleUnit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section2230143218276).METRIC\_UNIT (metric unit).

 |

1.  Set **mapType**. For details, please refer to [Changing the Map Type](../changing-the-map-type/document.md).
2.  Set **myLocationControlsEnabled** to display the my-location icon.
    
    Set **myLocationControlsEnabled** to **true** in **mapOptions** to display the my-location icon ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/XkFt_Rm0SlKnU4jRkCF84w/en-us_image_0000002514290008.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E737FCB37BD99867468A7E46152159789855D78D90134B89062A03AB06EFC53). The following shows a configuration example.
    
    You can also call the method of the [MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller) object to display the my-location icon. For details, please refer to [Showing My Location](../showing-my-location/document.md).
    
    this.mapOptions = {
      position: {
        target: {
          latitude: 39.9,
          longitude: 116.4
        },
        zoom: 10
      },
      myLocationControlsEnabled: true
    };
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/H69B0Jv9R_Gg-db18oaS8A/en-us_image_0000002514097644.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7A26D1F49E7970B13961DCA4B70370DC375BC23C84E54751517451F7BEC0E04 "Click to enlarge")
    
3.  Display the scale.
    
    Set **scaleControlsEnabled** to **true** in **mapOptions** to display the scale. The following shows a configuration example.
    
    this.mapOptions = {
      position: {
        target: {
          latitude: 39.9,
          longitude: 116.4
        },
        zoom: 10
      },
      scaleControlsEnabled: true
    };
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/4KgQdQlqSni90L56TfkgGA/en-us_image_0000002514257672.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11649988DB8388AD9FA8A01E38EE6F69EC21A4EB7A887758B204650BDB43F7B4 "Click to enlarge")
    

## Enabling the BuildingOverlay

Call the [setBuildingEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section15905291318) method of the [MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller) object to enable the BuildingOverlay. Users can zoom in on the map to level 17 or above, and use two fingers to swipe upward on the screen to tilt the map to view the BuildingOverlay effect.

this.mapController.setBuildingEnabled(true);

The following figure illustrates the effects.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/B4pLoZwOSEqNmSZ-9SXhsw/en-us_image_0000002542400669.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A6DFE8983801F15FB0164338BA42D05DE59CF29D21A936CAD03367C33B429AC "Click to enlarge")

## Switching Between the Map Foreground and Background

You can use the [MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller) object to manage the lifecycle of a map page switching between foreground and background. When an app triggers a switchover between the foreground and background on a map page, the **show/hide** function can be called in the page lifecycle to apply for or release resources.

**Switch the map to the foreground**:

// This is called each time the page is displayed, for example, during page redirection or when the app is switched to the foreground. It works only for the custom components decorated using **@Entry**.
onPageShow(): void {
  // You are advised to call the **show** method of the map component to switch to the foreground. 
  if (this.mapController) {
    this.mapController.show();
  }
}

**Switch the map to the background**:

// This is called each time the page is hidden, for example, during page redirection or when the app is switched to the background. It works only for the custom components decorated using **@Entry**.
onPageHide(): void {
  // You are advised to call the **hide** method of the map component to switch to the background. 
  if (this.mapController) {
    this.mapController.hide();
  }
}

## Dark Mode

Map Kit provides two methods to set the dark mode of a map: during map initialization and after map creation.

Method 1: During map initialization

Set the **dayNightMode** parameter in the map initialization parameters. The options are **DAY** (day mode), **NIGHT** (dark mode), and **AUTO** (automatic mode). If **dayNightMode** is set to **AUTO**, the map's dark mode will follow the system. If the system is enabled the dark mode, the map uses the dark mode. Otherwise, the map uses the day mode.

this.mapOptions = {
  position: {
    target: {
      latitude: 39.9,
      longitude: 116.4
    },
    zoom: 10
  },
  myLocationControlsEnabled: true,
  // Set the map to the dark mode.
  dayNightMode: mapCommon.DayNightMode.NIGHT
};

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/8Fq5WTMiSvikfhua-_yDNQ/en-us_image_0000002545740639.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D7EEBD679D133DBC25D843F72A21027656D65E5727FFFED6FB829DBCE40319AC "Click to enlarge")

Method 2: After map creation

After the map is created, call the [setDayNightMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section123945545109) method of the [MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller) object to set the dark mode. Set the parameter in the following example to **AUTO**, and enable the dark color of the system. Then the map automatically changes to the dark mode.

// Set the map to the auto mode.
this.mapController.setDayNightMode(mapCommon.DayNightMode.AUTO);

## Indoor Map

The indoor map allows users to view floor plans to see the interior layout of places such as shopping malls, museums, and hospitals.

Map Kit provides two methods to enable the indoor map: during map initialization and after map creation.

Method 1: During map initialization

During map initialization, set **indoorMapEnabled** to **true** in the initialization parameter [MapOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section816451553012). The indoor map and the floor level control are only visible at map zoom level 17 and above. Users can switch between different indoor map floors using the floor level control in the lower left corner.

this.mapOptions = {
  position: {
    target: {
      latitude: 31.979227,
      longitude: 118.762245
    },
    zoom: 18
  },
  // Enable the indoor map.
  indoorMapEnabled: true
};

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/JbPw1I1gRey8ao3lY4cIVQ/en-us_image_0000002545756111.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1028D7BF360B095FD564757E5EB089DEB5F45A82348502DD3B2373619C778150 "Click to enlarge")

Method 2: After map creation

After the map is created, call the [setIndoorMapEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section12159164214612) method of the [MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller) object to enable the indoor map. In the following example, after the indoor map is enabled, the [isIndoorMapEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section820584761611) method is called to check whether the indoor map is enabled, and the [setFloorControlsPosition](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section53651918173410) method is called to set the position of the floor selector control. The [switchIndoorMapFloor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section15944125342513) method is also provided to switch to a specified indoor building and floor.

// Enable the indoor map.
this.mapController.setIndoorMapEnabled(true);
// Check whether the indoor map is enabled.
let isIndoorMapEnabled: boolean = this.mapController.isIndoorMapEnabled();
console.info('indoorMapEnabled is:' + isIndoorMapEnabled);
// Set the position of the floor selector control.
this.mapController.setFloorControlsPosition({
  positionX: 500,
  positionY: 500
});
// Switch to a specified floor. Replace the first input parameter with the required building ID and the second with the floor, for example, **1F** or **B1**.
this.mapController.switchIndoorMapFloor('822588304363886720', '3F');

You can call the [on('indoorMapEnter')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section76731728143918) method to listen for indoor map access events and the [on('indoorMapExit')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section15867173119615) method to listen for indoor map exit events.

let callbackEnter = (indoorMapInfo: map.IndoorMapInfo) => {
  console.info(this.TAG, \`on-indoorMapEnter\`);
};
let callbackExit = () => {
  console.info(this.TAG, \`on-indoorMapExit\`);
};
// Callback of listening for indoor map access events.
this.mapEventManager.on("indoorMapEnter", callbackEnter);
// Callback of listening for indoor map exit events.
this.mapEventManager.on("indoorMapExit", callbackExit);

## Setting the Logo Scaling Ratio

Map Kit provides two methods to set the logo scaling ratio of a map: during map initialization and after map creation.

Method 1: During map initialization

Set the **logoScale** parameter in the map initialization parameters. The value range is \[0.8, 1\], and the default value is **1**.

this.mapOptions = {
  position: {
    target: {
      latitude: 39.9,
      longitude: 116.4
    },
    zoom: 10
  },
  myLocationControlsEnabled: true,
  // Set the logo scaling ratio to **0.9**.
  logoScale: 0.9
};

Method 2: After map creation

1.  After the map is created, call the [setLogoScale](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section205343210177) method of the [MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section816451553012) object to set the logo scaling ratio.
    
    this.mapController.setLogoScale(0.9);
    
2.  Obtain the logo scaling ratio.
    
    Call the [getLogoScale](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section18243711173212) method of the [MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section816451553012) object to obtain the current logo scaling ratio.
    
    let logoScale: number = this.mapController.getLogoScale();
    

## Enabling the 3D Globe View

Map Kit provides two methods to enable the 3D globe view: during map initialization and after map creation.

After the 3D globe view is enabled, users can clearly view the 3D globe when the zoom level is less than 4.

Method 1: During map initialization

Set the parameter indicating whether to enable the 3D globe view to **true** in the map initialization parameters. The default value is **false**.

this.mapOptions = {
  position: {
    target: {
      latitude: 39.9,
      longitude: 116.4
    },
    zoom: 2
  },
  // Enable the 3D globe view.
  sphereEnabled: true
};

Method 2: After map creation

After the map is created, call the [setSphereEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section67801022102716) method of the [MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section816451553012) object to enable the 3D globe view. You can call the [isSphereEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section1825143352110) method of the [MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section816451553012) object to check whether the 3D globe view is enabled.

// Enable the 3D globe view.
this.mapController.setSphereEnabled(true);
// Check whether the 3D globe view is enabled.
let result: boolean = this.mapController.isSphereEnabled();

The following figure illustrates the effects.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/cc5Njp3mQsuwAeQuwOHLsA/en-us_image_0000002545881471.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ADE7A8DA48850808AC66CFCD85C5F143A160BB236E97A88B8B5328CBA7DCBC84 "Click to enlarge")
