# Gesture Interaction

#### Use Cases

This section describes how to use map gestures.

Map Kit provides multiple gestures for users to interact with maps, such as zooming, scrolling, rotating, and tilting. These gestures are enabled by default. You can use APIs provided by the [MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller) class to disable some of the gestures.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/68TJZNDMSTWbFkctib6Ihg/en-us_image_0000002545966631.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2E1F2A983B4D63D2617FA357024476D1E99665577DE55953712F32ABB20E8C1 "Click to enlarge")

#### API Description

The following table lists the map gesture APIs. Gestures can be enabled or disabled in either of the following ways:

-   During map initialization, set whether to enable gestures in the initialization parameter [MapOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section816451553012). For details, please refer to [Displaying a Map](../../map-creation/displaying-a-map/document.md).
-   Call the **set** method provided by [MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller) to enable or disable related gestures.

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[setZoomGesturesEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section1151381081514)(enabled: boolean): void

 | 

Sets whether to enable zoom gestures.

The default value is **true**.

 |
| 

[setScrollGesturesEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section31711513156)(enabled: boolean): void

 | 

Sets whether to enable scroll gestures.

The default value is **true**.

 |
| 

[setRotateGesturesEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section299655171811)(enabled: boolean): void

 | 

Sets whether to enable rotation gestures.

The default value is **true**.

 |
| 

[setTiltGesturesEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section183712595910)(enabled: boolean): void

 | 

Sets whether to enable tilt gestures.

The default value is **true**.

 |
| 

[setAllGesturesEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section1965712771211)(enabled: boolean): void

 | 

Sets whether to enable zoom gestures.

The default value is **true**.

 |

#### Development Procedure

Obtain a **mapController** object during map initialization. For details about the map initialization function, please refer to [Displaying a Map](../../map-creation/displaying-a-map/document.md).

## Map Interaction Gestures

You can use a **mapController** object to enable or disable relevant map gestures.

**Zoom gestures:**

A user can pinch two fingers to zoom in or out on the map.

this.mapController.setZoomGesturesEnabled(true);

**Scroll gestures:**

A user can drag the map to move it.

this.mapController.setScrollGesturesEnabled(true);

**Rotation gesture:**

A user can rotate a map with two fingers.

this.mapController.setRotateGesturesEnabled(true);

**Tilt gestures:**

A user can tilt a map with two fingers.

this.mapController.setTiltGesturesEnabled(true);

**Enabling or disabling all gestures:**

Call the [setAllGesturesEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section1965712771211) method to enable or disable all gestures.

// Disable all gestures.
this.mapController.setAllGesturesEnabled(false);
