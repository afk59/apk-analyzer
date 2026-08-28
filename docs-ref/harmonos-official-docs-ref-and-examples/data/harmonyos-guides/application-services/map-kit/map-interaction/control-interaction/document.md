# Control Interaction

#### Use Cases

This section describes how to use map controls.

Controls refer to a series of components floating on a map component for operating the map, such as the zoom icon ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/49xPfCOuQk-s7FDA-ZIOZg/en-us_image_0000002517280067.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7C8714FFE08CA3D7B4063473C1F5C0B264A33D774B7F67D7D5967A1CAC76923), location icon ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/vzKV9sB-T-Smu_L4sqemag/en-us_image_0000002485000160.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D69C18CE9F4C0087D5C50B7ACEB724BFC6B07C6DD6BE32D3E2DB7C394268300), and scale ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/1RcKmTR_RUuv7y9WECq3mQ/en-us_image_0000002485160130.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21823100939A41820A3C12F0D9BF8DCF346BBB4E0DF2F9268C54E99C814E31DC).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/qN3OUWuqQ6CNBoTKBimk0g/en-us_image_0000002545966443.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BBD1C132A32E68214DA9ECAFF670C7C55F1690FE9365E73E33FC060E58A45F66 "Click to enlarge")

#### API Description

The following table lists the map control APIs. Controls can be enabled or disabled in either of the following ways:

-   During map initialization, set whether to enable controls in the initialization parameter [MapOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section816451553012). For details, please refer to [Displaying a Map](../../map-creation/displaying-a-map/document.md).
-   Call the **set** method provided by [MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section816451553012) to enable or disable related controls.

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[setZoomControlsEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section4116897186)(enabled: boolean): void

 | 

Sets whether to enable the zoom control.

 |
| 

[setMyLocationEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section201759451313)(myLocationEnabled: boolean): void

 | 

Sets whether to enable the **my-location** layer.

 |
| 

[setMyLocationControlsEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section3464719101814)(enabled: boolean): void

 | 

Sets whether to enable the **my-location** icon.

 |
| 

[setScaleControlsEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section1845222318187)(enabled: boolean): void

 | 

Sets whether to enable the scale.

 |
| 

[setScalePosition](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section8413193042817)(point: [mapCommon.MapPoint](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section123881566186)): void

 | 

Sets the position of the scale control.

 |
| 

[setAlwaysShowScaleEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section3541416552)(enabled: boolean): void

 | 

Sets whether to always display the scale.

 |
| 

[setCompassControlsEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section1964925785515)(enabled: boolean): void

 | 

Sets whether to enable the compass.

 |
| 

[setLogoAlignment](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section2538830161810)(alignment: [mapCommon.LogoAlignment](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section892653673414)): void

 | 

Sets the map logo alignment mode.

 |

#### Development Procedure

Obtain a **mapController** object during map initialization. For details about the map initialization function, please refer to [Displaying a Map](../../map-creation/displaying-a-map/document.md).

## Zoom Controls

Map Kit provides built-in zoom controls, which are enabled by default.

// Enable zoom controls.
this.mapController.setZoomControlsEnabled(true);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/o83OX-uuSYCMauAWiiDDPA/en-us_image_0000002514526498.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=726425D6C65C81A145F31FB447EF00045F5710CC6714B19F4A5414A47FBDDCFA "Click to enlarge")

## Scale

Map Kit provides the built-in scale control, which is disabled by default.

// Enable the scale control.
this.mapController.setScaleControlsEnabled(true);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/6P2PpgGmSpWJakUPsxGLHA/en-us_image_0000002514366616.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB250DEF6712195B6DCA1384EED4C3DE3C876A15637A7CD9641040B2AA7EA9C2 "Click to enlarge")

**Adjust the scale position.**

Use the [setScalePosition](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section8413193042817) method to set the position of the scale control.

let point: mapCommon.MapPoint = {
  // Use the upper left corner of the current map component as the origin and pan the map 1000 pixels to the right.
  positionX: 1000,
  // Use the upper left corner of the current map component as the origin and pan the map 1000 pixels downwards.
  positionY: 1000
};
this.mapController.setScalePosition(point);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/VJGuuWmfQ-mOCcp14QspbQ/en-us_image_0000002514526564.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A151E2926115EE42CA47AF44D1FF7B8F2B921AF63F0B28A055944F865E72AC1 "Click to enlarge")

**Obtain the scale at the current level.**

Use the [getScaleLevel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section19511102142917) method to obtain the scale at the current level.

let level = this.mapController.getScaleLevel();

**Obtain the width and height of the scale control.**

Use the [getScaleControlsHeight](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section155328471187) and [getScaleControlsWidth](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section192221515111317) methods to obtain the height and width of the current scale control, respectively.

// Obtain the height of the scale control.
let height = this.mapController.getScaleControlsHeight();
// Obtain the width of the scale control.
let width = this.mapController.getScaleControlsWidth();

**Set the scale control to be always displayed.**

Use the [setAlwaysShowScaleEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section3541416552) method to set the scale control to be always displayed and use the [isAlwaysShowScaleEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section197705711554) method to check whether the scale control is always displayed.

// Set the scale control to be always displayed. 
this.mapController.setAlwaysShowScaleEnabled(true);
// Check whether the scale control is always displayed.
let scaleEnabled: boolean = this.mapController.isAlwaysShowScaleEnabled();

## Compass

Map Kit provides a built-in compass control, which is enabled by default. The control is displayed in the upper right corner of the map by default. If this control is enabled, and the map is not oriented toward due north, the compass icon will display in the upper right corner of the map. The user can touch the compass icon to rotate the map, so that it can orient toward due north. If this control is enabled and the map is oriented toward due north, the compass icon will be hidden. If this control is disabled, the compass icon will not be displayed.

// Enable the compass control.
this.mapController.setCompassControlsEnabled(true);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/_sssCUs3TWeFE_LgPH5HFA/en-us_image_0000002514526570.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C77CBC18E486F6293A18DEA31DE10D754393EDD0E5CDC1877276575DA90804DE "Click to enlarge")

**Adjust the compass position.**

Use the [setCompassPosition](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section285112882417) method to set the position of the compass control.

let point: mapCommon.MapPoint = {
  // Use the upper left corner of the current map component as the origin and pan the map 1000 pixels to the right.
  positionX: 1000,
  // Use the upper left corner of the current map component as the origin and pan the map 1000 pixels downwards.
  positionY: 1000
};
this.mapController.setCompassPosition(point);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/eE7loUb9To2LFmt27C4FwA/en-us_image_0000002545966527.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F0AD164C66ADFF29B0599E822DE6691DF3ACFD2064B6C2FC44E1B2F7763DC8F "Click to enlarge")

## Map Logo

Map Kit provides the [setLogoAlignment](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section2538830161810) method to adjust the map logo alignment mode and the [setLogoPadding](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section115618542213) method to adjust the padding between the map edges and the logo. Note that the map logo cannot be covered. You can use the [setLogoPadding](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section115618542213) method to set the padding to prevent the logo from being covered.

// Place the map logo in the lower right corner.
this.mapController.setLogoAlignment(mapCommon.LogoAlignment.BOTTOM\_END);
// Set the padding between the logo and map edges, measured in pixels.
let padding: mapCommon.Padding = {
  right: 50,
  bottom: 50
};
this.mapController.setLogoPadding(padding);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/mqb8xSZmRa2h7TyYUVD0Kw/en-us_image_0000002545966623.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AFDC2F138523956C23AADBE1B4EBF0908C166CA61393FF2837F0E08F410B8624 "Click to enlarge")
