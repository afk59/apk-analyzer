# MapComponentController

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### MapComponentController

Main entrance for accessing functions of Map Kit. All map-related methods are accessed through this entrance, which also supports event listener management.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Example**:

import { MapComponent, mapCommon, map } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

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
        // Return the listening event manager of the map component.
        this.mapEventManager = this.mapController.getEventManager();
        let callback = () => {
          console.info(this.TAG, \`on-mapLoad\`);
        }
        this.mapEventManager.on("mapLoad", callback);

        // Execute a custom method.
        this.customizedMethod();
      }
    };
  }

  // Custom method.
  private customizedMethod() {
    // ...
  }

  build() {
    Stack() {
      // Call **MapComponent** to initialize the map.
      MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
        .width('100%')
        .height('100%')
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/QhmAn5RCQZWX--wgMqPKeQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062511Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6AEE6E1A7B588210291F206E9550AB7F561C05B1B9448BE506B3FDDDE9599622)

The methods in **MapComponentController** need to be executed either in the map initialization callback or in the custom method in the example above.

#### \[h2\]animateCamera

animateCamera(update: CameraUpdate, duration?: number): void

Updates the camera position in animation mode within a specified period of time.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

update

 | 

[CameraUpdate](../cameraupdate/document.md)

 | 

Yes

 | 

Camera position change.

 |
| 

duration

 | 

number

 | 

No

 | 

Animation duration, in milliseconds. The default value is **250**. The value must be greater than 0. If this parameter is set to a value less than or equal to 0, the default value will be used.

 |

**Example**:

let target: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4
};
let cameraPosition: mapCommon.CameraPosition = {
  target: target,
  zoom: 10
};
// Create a **CameraUpdate** object.
let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
// Move the camera in animation mode within 1000 ms.
this.mapController.animateCamera(cameraUpdate, 1000);

#### \[h2\]animateCameraStatus

animateCameraStatus(update: CameraUpdate, duration?: number): Promise<AnimateResult>

Updates the camera position in animation mode within a specified period of time, and returns the animation result. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

update

 | 

[CameraUpdate](../cameraupdate/document.md)

 | 

Yes

 | 

Camera position change.

 |
| 

duration

 | 

number

 | 

No

 | 

Animation duration, in milliseconds. The default value is **250**. The value must be greater than 0. If this parameter is set to a value less than or equal to 0, the default value will be used.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AnimateResult](../animateresult/document.md#section18741944605)\>

 | 

Promise that returns [AnimateResult](../animateresult/document.md#section18741944605).

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter.

 |

**Example**:

let target: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4
};
let cameraPosition: mapCommon.CameraPosition = {
  target: target,
  zoom: 10
};
// Create a **CameraUpdate** object.
let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
// Move the camera in animation mode within 1000 ms.
let animateResult = await this.mapController.animateCameraStatus(cameraUpdate, 1000);

#### \[h2\]animateCameraWithMarker

animateCameraWithMarker(update: CameraUpdate, marker: Marker, duration: number): Promise<AnimateResult>

Updates the camera position in animation mode within a specified period of time, and updates a specified Marker. This API returns the result asynchronously through a promise. The camera movement cannot be interrupted. Otherwise, the return value of the **isCanceled** parameter of [AnimateResult](../animateresult/document.md#section18741944605) will be **true**.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

update

 | 

[CameraUpdate](../cameraupdate/document.md)

 | 

Yes

 | 

Camera position change.

 |
| 

marker

 | 

[Marker](../marker/document.md)

 | 

Yes

 | 

Marker.

 |
| 

duration

 | 

number

 | 

Yes

 | 

Animation duration, in milliseconds. The default value is **250**. The value must be greater than 0. If this parameter is set to a value less than or equal to 0, the default value will be used.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AnimateResult](../animateresult/document.md#section18741944605)\>

 | 

Promise that returns [AnimateResult](../animateresult/document.md#section18741944605).

 |

**Example**:

let target: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4
};
let cameraPosition: mapCommon.CameraPosition = {
  target: target,
  zoom: 10
};
// Create a **CameraUpdate** object.
let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
// Marker initialization parameters.
let markerOptions: mapCommon.MarkerOptions = {
  position: {
    latitude: 39.9,
    longitude: 116.4
  },
  title: "XXX",
  // The icon must be stored in the **resources/rawfile** directory.
  icon: 'icon/icon.png',
  clickable: true
};
// Create a Marker.
let marker = await this.mapController?.addMarker(markerOptions);
// Move the camera in animation mode within 1000 ms and update the specified Marker.
await this.mapController.animateCameraWithMarker(cameraUpdate, marker, 1000);

#### \[h2\]animateCameraWithMarkers

animateCameraWithMarkers(update: CameraUpdate, markers: Array<Marker>, duration: number): Promise<AnimateResult>

Updates the camera position in animation mode within a specified period of time, and updates specified Markers. A group of Markers can be passed. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

update

 | 

[CameraUpdate](../cameraupdate/document.md)

 | 

Yes

 | 

Camera position change.

 |
| 

markers

 | 

Array<[Marker](../marker/document.md)\>

 | 

Yes

 | 

A group of Markers.

NOTE:

The positions of these Markers must be the same. Otherwise, error code 401 will be returned.

 |
| 

duration

 | 

number

 | 

Yes

 | 

Animation duration, in milliseconds. The default value is **250**. The value must be greater than 0. If this parameter is set to a value less than or equal to 0, the default value will be used.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AnimateResult](../animateresult/document.md#section18741944605)\>

 | 

Promise that returns [AnimateResult](../animateresult/document.md#section18741944605).

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter.

 |

**Example**:

let target: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4
};
let cameraPosition: mapCommon.CameraPosition = {
  target: target,
  zoom: 10
};
// Create a **CameraUpdate** object.
let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
// Initialization parameters of **marker1**.
let markerOptions1: mapCommon.MarkerOptions = {
  position: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  },
  title: "icon",
  // The icon must be stored in the **resources/rawfile** directory.
  icon: 'icon/icon.png',
  clickable: true
};
let markerOptions2: mapCommon.MarkerOptions = {
  position: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  },
  title: "avocado",
  // The icon must be stored in the **resources/rawfile** directory.
  icon: 'icon/avocado.png',
  clickable: true,
  anchorU: 0.5,
  anchorV: 1
};
let marker1 = await this.mapController?.addMarker(markerOptions1);
// Initialization parameters of **marker2**.
let marker2 = await this.mapController?.addMarker(markerOptions2);
// Move the camera in animation mode within 1000 ms and update the specified Markers.
await this.mapController.animateCameraWithMarkers(cameraUpdate, \[marker1, marker2\], 1000);

#### \[h2\]stopAnimation

stopAnimation(): void

Stops the current camera position change animation. When this method is called, the camera stops moving immediately and remains in that position.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Example**:

this.mapController.stopAnimation();

#### \[h2\]clear

clear(): void

Removes all MapCircles, Markers, MapPolylines, and other overlays from a map.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Example**:

this.mapController.clear();

#### \[h2\]moveCamera

moveCamera(update: CameraUpdate): void

Updates the camera position.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

update

 | 

[CameraUpdate](../cameraupdate/document.md)

 | 

Yes

 | 

Camera position change.

 |

**Example**:

let target: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4
};
let cameraPosition: mapCommon.CameraPosition = {
  target: target,
  zoom: 10
};
// Create a **CameraUpdate** object.
let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
// Move the camera.
this.mapController.moveCamera(cameraUpdate);

#### \[h2\]getCameraPosition

getCameraPosition(): mapCommon.CameraPosition

Obtains the current position of the camera.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[mapCommon.CameraPosition](../../mapcommon-map-attribute-model/document.md#section105031244194712)

 | 

Current position of the camera.

 |

**Example**:

let cameraPosition: mapCommon.CameraPosition = this.mapController.getCameraPosition();

#### \[h2\]setLatLngBounds

setLatLngBounds(bounds: mapCommon.LatLngBounds): void

Sets a [mapCommon.LatLngBounds](../../mapcommon-map-attribute-model/document.md#section96341159111320) object to constrain the camera target so that the camera target does not move outside the bounds when a user scrolls the map. Newly set bounds will overwrite the existing ones.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

bounds

 | 

[mapCommon.LatLngBounds](../../mapcommon-map-attribute-model/document.md#section96341159111320)

 | 

Yes

 | 

Bounds for constraining the camera target.

NOTE:

This parameter does not take effect if the latitude of the southwest corner is greater than that of the northeast corner.

 |

**Example**:

let bounds:mapCommon.LatLngBounds = {
  northeast: {
    latitude: 31,
    longitude: 118
  },
  southwest: {
    latitude: 30,
    longitude: 117
  }
};
this.mapController.setLatLngBounds(bounds);

#### \[h2\]setPointToCenter

setPointToCenter(point: mapCommon.MapPoint): void

Sets a pixel position on the screen as the center point of the map. After this method is called, the map centers on the given pixel position and adjusts its zoom and rotation accordingly.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

point

 | 

[mapCommon.MapPoint](../../mapcommon-map-attribute-model/document.md#section123881566186)

 | 

Yes

 | 

Coordinates of a point on the screen. Invalid values are not processed.

 |

**Example**:

let point: mapCommon.MapPoint = {
  positionX: 1000,
  positionY: 1000
};
this.mapController.setPointToCenter(point);

#### \[h2\]setMaxZoom

setMaxZoom(maxZoom: number): void

Sets the maximum zoom level of the camera.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

maxZoom

 | 

number

 | 

Yes

 | 

Maximum zoom level of the camera. The value ranges from 2 to 20. Values outside this range are automatically adjusted to the nearest boundary.

If the input value is within the allowed range but less than the current **minZoom** value, both the maximum zoom level and minimum zoom level will be set to the current input value. Invalid values are not processed.

 |

**Example**:

this.mapController.setMaxZoom(10);

#### \[h2\]setMinZoom

setMinZoom(minZoom: number): void

Sets the minimum zoom level of the camera.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

minZoom

 | 

number

 | 

Yes

 | 

Minimum zoom level of the camera. The value ranges from 2 to 20. Values outside this range are automatically adjusted to the nearest boundary.

If the input value is within the allowed range but greater than the current **maxZoom** value, both the maximum zoom level and minimum zoom level will be set to the current input value. Invalid values are not processed.

 |

**Example**:

this.mapController.setMinZoom(3); 

#### \[h2\]getMaxZoom

getMaxZoom(): number

Obtains the maximum zoom level of the camera.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Maximum zoom level of the camera.

 |

**Example**:

let maxZoom: number = this.mapController.getMaxZoom(); 

#### \[h2\]getMinZoom

getMinZoom(): number

Obtains the minimum zoom level of the camera.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Minimum zoom level of the camera.

 |

**Example**:

let minZoom: number = this.mapController.getMinZoom(); 

#### \[h2\]setTrafficEnabled

setTrafficEnabled(enabled: boolean): void

Sets whether to enable the traffic status layer.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

enabled

 | 

boolean

 | 

Yes

 | 

-   **true**: Enable the traffic status layer.
-   **false**: Disable the traffic status layer.

The default value is **false**.

 |

**Example**:

this.mapController.setTrafficEnabled(true);  

#### \[h2\]isTrafficEnabled

isTrafficEnabled(): boolean

Checks whether the traffic status layer is enabled.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

-   **true**: The traffic status layer is enabled.
-   **false**: The traffic status layer is disabled.

 |

**Example**:

let isTrafficEnabled: boolean = this.mapController.isTrafficEnabled(); 

#### \[h2\]setBuildingEnabled

setBuildingEnabled(enabled: boolean): void

Sets whether to enable the 3D building layer.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

enabled

 | 

boolean

 | 

Yes

 | 

-   **true**: Enable the 3D building layer.
-   **false**: Disable the 3D building layer.

The default value is **false**.

NOTE:

After the 3D building layer is enabled, the 3D layer effect will be rendered by zooming in or out on the map to the building visibility level.

 |

**Example**:

this.mapController.setBuildingEnabled(true);

#### \[h2\]isBuildingEnabled

isBuildingEnabled(): boolean

Checks whether the 3D building layer is enabled.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

-   **true**: The 3D building layer is enabled.
-   **false**: The 3D building layer is disabled.

 |

**Example**:

let isBuildingEnabled: boolean = this.mapController.isBuildingEnabled();  

#### \[h2\]setMyLocationEnabled

setMyLocationEnabled(myLocationEnabled: boolean): void

Sets whether to enable the **my-location** layer function. By default, the continuous location capability of the system is used to display user locations. After the function is enabled, the **my-location** icon is displayed in the lower right corner of the map by default. When the **my-location** icon is tapped, the user's current location will be displayed in the center of the screen as a blue dot.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

myLocationEnabled

 | 

boolean

 | 

Yes

 | 

-   **true**: Enable the **my-location** layer.
-   **false**: Disable the **my-location** layer.

The default value is **false**.

 |

**Example**:

this.mapController.setMyLocationEnabled(true);

#### \[h2\]setMyLocation

setMyLocation(location: geoLocationManager.Location): void

Sets the coordinates of the **my-location** icon. By default, Map Kit uses the continuous location capability of the system to display user locations. If you want to customize the display frequency or accuracy, call this API.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

location

 | 

[geoLocationManager.Location](../../../../location-kit/arkts-apis/ohos-geolocationmanager-geolocation-manager/document.md#location)

 | 

Yes

 | 

User location.

NOTE:

The value of the **location** parameter must be coordinates in the WGS84 coordinate system.

 |

**Example**:

// Import the @kit.LocationKit module.
import { geoLocationManager } from '@kit.LocationKit';

let location = await geoLocationManager.getCurrentLocation();
this.mapController.setMyLocation(location);

#### \[h2\]setMyLocationStyle

setMyLocationStyle(style: mapCommon.MyLocationStyle): Promise<void>

Sets the user location style. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

style

 | 

[mapCommon.MyLocationStyle](../../mapcommon-map-attribute-model/document.md#section3713124215275)

 | 

Yes

 | 

User location style.

NOTE:

If **displayType** is set to **FOLLOW\_ROTATE**, your app needs to apply for the sensor permission **ohos.permission.ACCELEROMETER**. For details, please refer to [Declaring Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/declare-permissions).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Example**:

let style: mapCommon.MyLocationStyle = { 
  anchorU: 0.5, 
  anchorV: 0.5, 
  radiusFillColor: 0xffff0000, 
  // Icons are custom resources stored in **resources/rawfile**. Set **icon** to what you need.
  icon: 'icon/avocado.png'   
};
await this.mapController.setMyLocationStyle(style);

#### \[h2\]isMyLocationEnabled

isMyLocationEnabled(): boolean

Checks whether the **my-location** layer is enabled.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

Indicates whether the **my-location** layer is enabled.

-   **true**: yes
-   **false**: no

 |

**Example**:

let isMyLocationEnabled: boolean = this.mapController.isMyLocationEnabled(); 

#### \[h2\]setZoomGesturesEnabled

setZoomGesturesEnabled(enabled: boolean): void

Sets whether to enable zoom gestures. By default, zoom gestures are enabled.

-   If zoom gestures are enabled, users can zoom the map camera with the following gestures:
    1.  Double-tap the map with one finger to increase the zoom level by 1 (zoom-in), or tap the map with two fingers to decrease the zoom level by 1 (zoom-out).
    2.  Stretch or pinch the map with two fingers to zoom in or out.
    3.  Double-tap with one finger and long press the map upon the second tap, and slide up to zoom out on the map or down to zoom in on the map.
-   If zoom gestures are disabled, zoom gestures will be invalid. The setting neither affects the zoom controls nor affects map camera movement and animation through APIs.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

enabled

 | 

boolean

 | 

Yes

 | 

-   **true**: Enable zoom gestures.
-   **false**: Disable zoom gestures.

The default value is **true**.

 |

**Example**:

this.mapController.setZoomGesturesEnabled(true); 

#### \[h2\]isZoomGesturesEnabled

isZoomGesturesEnabled(): boolean

Checks whether zoom gestures are enabled.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

Indicates whether zoom gestures are enabled.

-   **true**: yes
-   **false**: no

 |

**Example**:

let isZoomGesturesEnabled: boolean = this.mapController.isZoomGesturesEnabled(); 

#### \[h2\]setScrollGesturesEnabled

setScrollGesturesEnabled(enabled: boolean): void

Sets whether to enable scroll gestures. By default, scroll gestures are enabled.

-   When enabled, users can slide on the map to pan the map camera.
-   When disabled, sliding has no effect on camera movement. The setting does not affect camera movement and animation through APIs.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

enabled

 | 

boolean

 | 

Yes

 | 

-   **true**: Enable scroll gestures.
-   **false**: Disable scroll gestures.

The default value is **true**.

 |

**Example**:

this.mapController.setScrollGesturesEnabled(true); 

#### \[h2\]isScrollGesturesEnabled

isScrollGesturesEnabled(): boolean

Checks whether scroll gestures are enabled.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

Indicates whether scroll gestures are enabled.

-   **true**: yes
-   **false**: no

 |

**Example**:

let isScrollGesturesEnabled: boolean = this.mapController.isScrollGesturesEnabled();

#### \[h2\]setRotateGesturesEnabled

setRotateGesturesEnabled(enabled: boolean): void

Sets whether to enable rotation gestures. By default, rotation gestures are enabled.

-   When enabled, users can rotate the map camera with two fingers.
-   When disabled, users cannot rotate the map camera through rotation gestures. However, users can still tap the compass to change the map camera orientation. The setting does not affect camera movement and animation through APIs.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

enabled

 | 

boolean

 | 

Yes

 | 

-   **true**: Enable rotation gestures.
-   **false**: Disable rotation gestures.

The default value is **true**.

 |

**Example**:

this.mapController.setRotateGesturesEnabled(true); 

#### \[h2\]isRotateGesturesEnabled

isRotateGesturesEnabled(): boolean

Checks whether rotation gestures are enabled.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

Indicates whether rotation gestures are enabled.

-   **true**: yes
-   **false**: no

 |

**Example**:

let isRotateGesturesEnabled: boolean = this.mapController.isRotateGesturesEnabled();

#### \[h2\]setTiltGesturesEnabled

setTiltGesturesEnabled(enabled: boolean): void

Sets whether to enable tilt gestures. By default, tilt gestures are enabled.

-   When enabled, users can use two fingers to swipe up or down vertically to tilt the camera.
-   When disabled, users cannot tilt the camera through tilt gestures.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

enabled

 | 

boolean

 | 

Yes

 | 

-   **true**: Enable tilt gestures.
-   **false**: Disable tilt gestures.

The default value is **true**.

 |

**Example**:

this.mapController.setTiltGesturesEnabled(true); 

#### \[h2\]isTiltGesturesEnabled

isTiltGesturesEnabled(): boolean

Checks whether tilt gestures are enabled.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

Indicates whether tilt gestures are enabled.

-   **true**: yes
-   **false**: no

 |

**Example**:

let isTiltGesturesEnabled: boolean = this.mapController.isTiltGesturesEnabled();

#### \[h2\]setZoomControlsEnabled

setZoomControlsEnabled(enabled: boolean): void

Sets whether to enable zoom controls. By default, zoom controls are enabled.

-   When enabled, a pair of zoom controls will be displayed on the map. When a user taps the zoom controls, the map camera zoom level will increase (or decrease) by 1.
-   When disabled, the zoom controls will be hidden.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

enabled

 | 

boolean

 | 

Yes

 | 

-   **true**: Enable zoom controls.
-   **false**: Disable zoom controls.

The default value is **true**.

 |

**Example**:

this.mapController.setZoomControlsEnabled(true); 

#### \[h2\]isZoomControlsEnabled

isZoomControlsEnabled(): boolean

Checks whether zoom controls are enabled.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

Indicates whether zoom controls are enabled.

-   **true**: yes
-   **false**: no

 |

**Example**:

let isZoomControlsEnabled: boolean = this.mapController.isZoomControlsEnabled();

#### \[h2\]setMyLocationControlsEnabled

setMyLocationControlsEnabled(enabled: boolean): void

Sets whether to enable the **my-location** icon. If this icon is enabled but the **my-location** layer function is disabled, tapping this icon will not trigger any action.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

enabled

 | 

boolean

 | 

Yes

 | 

-   **true**: Enable the **my-location** icon.
-   **false**: Disable the **my-location** icon.

The default value is **false**.

 |

**Example**:

this.mapController.setMyLocationControlsEnabled(true); 

#### \[h2\]isMyLocationControlsEnabled

isMyLocationControlsEnabled(): boolean

Checks whether the **my-location** icon is enabled.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

Indicates whether the **my-location** icon is enabled.

-   **true**: yes
-   **false**: no

 |

**Example**:

let isMyLocationControlsEnabled: boolean = this.mapController.isMyLocationControlsEnabled();

#### \[h2\]setScaleControlsEnabled

setScaleControlsEnabled(enabled: boolean): void

Sets whether to enable the scale.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

enabled

 | 

boolean

 | 

Yes

 | 

-   **true**: Enable the scale.
-   **false**: Disable the scale.

The default value is **false**.

 |

**Example**:

this.mapController.setScaleControlsEnabled(true);

#### \[h2\]isScaleControlsEnabled

isScaleControlsEnabled(): boolean

Checks whether the scale is enabled.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

Indicates whether the scale is enabled.

-   **true**: yes
-   **false**: no

 |

**Example**:

let isScaleControlsEnabled: boolean = this.mapController.isScaleControlsEnabled();

#### \[h2\]setCompassControlsEnabled

setCompassControlsEnabled(enabled: boolean): void

Sets whether to enable the compass.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

enabled

 | 

boolean

 | 

Yes

 | 

-   **true**: Enable the compass.
-   **false**: Disable the compass.

The default value is **true**.

 |

**Example**:

this.mapController.setCompassControlsEnabled(true);

#### \[h2\]isCompassControlsEnabled

isCompassControlsEnabled(): boolean

Checks whether the compass is enabled.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

Indicates whether the compass is enabled.

-   **true**: yes
-   **false**: no

 |

**Example**:

let isCompassControlsEnabled: boolean = this.mapController.isCompassControlsEnabled();

#### \[h2\]setGestureScaleByMapCenter

setGestureScaleByMapCenter(enabled: boolean): void

Sets whether the map zooms based on a fixed screen center. By default, this function is disabled.

-   When this function is enabled, the map will zoom based on the passed fixed screen center. You can call the [setPointToCenter](#section159768471777) method to set the screen center coordinates.
-   When this function is disabled, the map will zoom based on the tap point on the screen.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

enabled

 | 

boolean

 | 

Yes

 | 

-   **true**: Enable the function. The map will zoom based on the passed fixed screen center.
-   **false**: Disable the function. The map will zoom based on the tap point on the screen.

The default value is **false**.

 |

**Example**:

this.mapController.setGestureScaleByMapCenter(true);

#### \[h2\]isGestureScaleByMapCenter

isGestureScaleByMapCenter(): boolean

Checks whether a fixed screen center can be passed for zooming.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

Indicates whether a fixed screen center can be passed for zooming.

-   **true**: yes
-   **false**: no

 |

**Example**:

let isGestureScaleByMapCenter: boolean = this.mapController.isGestureScaleByMapCenter();

#### \[h2\]setLogoAlignment

setLogoAlignment(alignment: mapCommon.LogoAlignment): void

Sets the map logo alignment mode.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

alignment

 | 

[mapCommon.LogoAlignment](../../mapcommon-map-attribute-model/document.md#section892653673414)

 | 

Yes

 | 

Map logo alignment mode. The default value is [LogoAlignment](../../mapcommon-map-attribute-model/document.md#section892653673414).BOTTOM\_START.

 |

**Example**:

this.mapController.setLogoAlignment(mapCommon.LogoAlignment.BOTTOM\_START);

#### \[h2\]setLogoPadding

setLogoPadding(padding: mapCommon.Padding): void

Sets the padding between the logo and map edges. The logo has a fixed size and is not affected by map zooming, always displaying in pixels.

-   The logo position remains unchanged if any padding value is out of the valid range (for example, the value is a negative number or the padding is out of the map edges).
-   The **left** and **bottom** parameters take effect if the logo is in the lower left corner.
-   The **right** and **top** parameters take effect if the logo is in the upper right corner. This rule also applies to other corners.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/nNQ7NlduR5C4Imviw5jZrg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062511Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13B448CEA647ACD80349A600CF8B824AAC184A26A6A0A30F12491277231A397C)

When setting the padding between the logo and map edges, do not hide or cover the logo.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

padding

 | 

[mapCommon.Padding](../../mapcommon-map-attribute-model/document.md#section144591344648)

 | 

Yes

 | 

Padding between map edges and the logo.

 |

**Example**:

let padding: mapCommon.Padding = {
  left: 0,
  bottom: 50
};
this.mapController.setLogoPadding(padding);

#### \[h2\]getScalePerPixel

getScalePerPixel(): number

Obtains the length corresponding to one pixel point on the map at the current zoom level. The length unit is meter.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Length corresponding to one pixel point on the map at the current zoom level, in meters.

 |

**Example**:

let scalePerPixel: number = this.mapController.getScalePerPixel();

#### \[h2\]addMarker

addMarker(options: mapCommon.MarkerOptions): Promise<Marker>

Adds a Marker to the map. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

options

 | 

[mapCommon.MarkerOptions](../../mapcommon-map-attribute-model/document.md#section559041743210)

 | 

Yes

 | 

Marker attributes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Marker](../marker/document.md)\>

 | 

Promise that returns [Marker](../marker/document.md).

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter.

 |
| 

1002601001

 | 

The object to be operated does not exist.

 |
| 

1002601005

 | 

Failed to generate the icon of the customized component.

NOTE:

This error code is available since 6.0.0 (20).

 |

**Example**:

// Marker initialization parameters.
let markerOptions: mapCommon.MarkerOptions = {
  position: {
    latitude: 39.9,
    longitude: 116.4
  },
  rotation: 0,
  visible: true,
  zIndex: 0,
  alpha: 1,
  anchorU: 0.5,
  anchorV: 1,
  clickable: true,
  draggable: true,
  flat: false,
  // The icon is stored in **resources/rawfile**.
  icon: 'test.png'
};
// Add a Marker to the map.
let marker: map.Marker = await this.mapController.addMarker(markerOptions);

#### \[h2\]addCircle

addCircle(options: mapCommon.MapCircleOptions): Promise<MapCircle>

Adds a MapCircle to the map by specifying the longitude and latitude of the center and the radius. The MapCircle is used to indicate the surrounding area of a location. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

options

 | 

[mapCommon.MapCircleOptions](../../mapcommon-map-attribute-model/document.md#section5282124803117)

 | 

Yes

 | 

MapCircle attributes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[MapCircle](../mapcircle/document.md)\>

 | 

Promise that returns [MapCircle](../mapcircle/document.md).

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter.

 |
| 

1002601001

 | 

The object to be operated does not exist.

 |

**Example**:

// MapCircle initialization parameters.
let mapCircleOptions: mapCommon.MapCircleOptions = {
  center: {
    latitude: 39.9,
    longitude: 116.4
  },
  patterns: \[{
    type: 0,
    length: 100
  }, {
    type: 1,
    length: 100
  }, {
    type: 2,
    length: 100
  }\],
  radius: 700,
  fillColor: 0XFF00FFFF,
  strokeColor: 0xFFFF0000,
  strokeWidth: 10,
  zIndex: 15
};
// Add a MapCircle to the map.
let mapCircle: map.MapCircle = await this.mapController.addCircle(mapCircleOptions);

#### \[h2\]addPolyline

addPolyline(options: mapCommon.MapPolylineOptions): Promise<MapPolyline>

Adds a MapPolyline to the map. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

options

 | 

[mapCommon.MapPolylineOptions](../../mapcommon-map-attribute-model/document.md#section113246334153)

 | 

Yes

 | 

MapPolyline attributes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[MapPolyline](../mappolyline/document.md)\>

 | 

Promise that returns [MapPolyline](../mappolyline/document.md).

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter.

 |
| 

1002601001

 | 

The object to be operated does not exist.

 |

**Example**:

// Initialization parameters.
let polylineOption: mapCommon.MapPolylineOptions = {
  // MapPolyline coordinates, which are mandatory.
  points: \[{
    latitude: 31.984410,
    longitude: 118.7662537
  }, {
    latitude: 31.084410,
    longitude: 118.0662537
  }\],
  clickable: true,
  color: 0xff000000,
  startCap: mapCommon.CapStyle.BUTT,
  endCap: mapCommon.CapStyle.BUTT,
  geodesic: false,
  jointType: mapCommon.JointType.DEFAULT,
  visible: true,
  width: 10,
  zIndex: 0,
  gradient: false
};
// Add a MapPolyline to the map.
let mapPolyline: map.MapPolyline = await this.mapController.addPolyline(polylineOption);

#### \[h2\]addPolygon

addPolygon(options: mapCommon.MapPolygonOptions): Promise<MapPolygon>

Adds a MapPolygon to the map. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

options

 | 

[mapCommon.MapPolygonOptions](../../mapcommon-map-attribute-model/document.md#section1615694815308)

 | 

Yes

 | 

MapPolygon attributes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[MapPolygon](../mappolygon/document.md)\>

 | 

Promise that returns [MapPolygon](../mappolygon/document.md).

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter.

 |
| 

1002601001

 | 

The object to be operated does not exist.

 |

**Example**:

// Initialization parameters.
let polygonOptions: mapCommon.MapPolygonOptions = {
  // MapPolygon coordinates, which are mandatory.
  points: \[{
    latitude: 31.98441,
    longitude: 118.066253
  }, {
    latitude: 31.98441,
    longitude: 118.766253
  }, {
    latitude: 32.98441,
    longitude: 118.766253
  }, {
    latitude: 32.98441,
    longitude: 118.066253
  }\],
  clickable: true,
  fillColor: 0xff00DE00,
  geodesic: false,
  strokeColor: 0xff000000,
  jointType: mapCommon.JointType.DEFAULT,
  strokeWidth: 10,
  visible: true,
  zIndex: 10
};
// Add a MapPolygon to the map.
let mapPolygon: map.MapPolygon = await this.mapController.addPolygon(polygonOptions);

#### \[h2\]addPointAnnotation

addPointAnnotation(params: mapCommon.PointAnnotationParams): Promise<PointAnnotation>

Adds a PointAnnotation to the map. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

params

 | 

[mapCommon.PointAnnotationParams](../../mapcommon-map-attribute-model/document.md#section161194598375)

 | 

Yes

 | 

PointAnnotation attributes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[PointAnnotation](../pointannotation/document.md)\>

 | 

Promise that returns [PointAnnotation](../pointannotation/document.md).

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter.

 |
| 

1002601001

 | 

The object to be operated does not exist.

 |

**Example**:

let pointAnnotationOptions: mapCommon.PointAnnotationParams = {
  // Define the anchor for the icon of a PointAnnotation.
  position: {
    latitude: 39.918,
    longitude: 116.397
  },
  // Set whether to support deduplication when the PointAnnotation name is the same as a map POI name.
  repeatable: true,
  // Set the collision rule of the PointAnnotation.
  collisionRule: mapCommon.CollisionRule.NAME,
  // Set PointAnnotation titles. The minimum length of the array is 1 and the maximum length is 3.
  titles: \[{
    // Set the title content.
    content: "Title1",
    // Set the title text color.
    color: 0xFF000000,
    // Set the title text font size.
    fontSize: 15,
    // Set the title stroke color.
    strokeColor: 0xFFFFFFFF,
    // Set the title stroke width.
    strokeWidth: 2,
    // Set the title text font style.
    fontStyle: mapCommon.FontStyle.ITALIC
  }\],
  // Set an icon for the PointAnnotation. The icon is stored in **resources/rawfile**.
  icon: "icon/avocado.png",
  // Set whether to display the icon for the PointAnnotation.
  showIcon: true,
  // Define the horizontal position of the anchor of the PointAnnotation.
  anchorU: 0.5,
  // Set the vertical position of the anchor of the PointAnnotation.
  anchorV: 1,
  // Set the display attribute of the PointAnnotation. If it is set to **true**, the PointAnnotation remains visible after collision.
  forceVisible: false,
  // Set the collision priority. A larger value indicates a lower priority.
  priority: 3,
  // Set the minimum zoom level for PointAnnotation display.
  minZoom: 2,
  // Set the maximum zoom level for PointAnnotation display.
  maxZoom: 20,
  // Define whether the PointAnnotation is visible.
  visible: true,
  // Set the stacking order attribute of the PointAnnotation.
  zIndex: 10
};
let pointAnnotation: map.PointAnnotation = await this.mapController.addPointAnnotation(pointAnnotationOptions);

#### \[h2\]addBubble

addBubble(params: mapCommon.BubbleParams): Promise<Bubble>

Adds a Bubble to the map. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

params

 | 

[mapCommon.BubbleParams](../../mapcommon-map-attribute-model/document.md#section10348735114315)

 | 

Yes

 | 

Bubble attributes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Bubble](../bubble/document.md)\>

 | 

Promise that returns [Bubble](../bubble/document.md).

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter.

 |
| 

1002601001

 | 

The object to be operated does not exist.

 |

**Example**:

let bubbleOptions: mapCommon.BubbleParams = {
  // Bubble position.
  positions: \[\[{ latitude: 31, longitude: 118 }\]\],
  // Bubble icons. Icons in four directions need to be passed. The icons are stored in **resources/rawfile**.
  icons: \[
    'icon.png',
    'icon.png',
    'icon.png',
    'icon.png'
  \],
  // Set the display attribute of the Bubble. If it is set to **true**, the Bubble remains visible after collision.
  forceVisible: true,
  // Set the Bubble collision priority. A larger value indicates a lower priority.
  priority: 3,
  // Set the minimum zoom level for Bubble display.
  minZoom: 2,
  // Set the maximum zoom level for Bubble display. 
  maxZoom: 20,
  // Set whether the Bubble is visible.
  visible: true,
  // Set the stacking order attribute of the Bubble.
  zIndex: 1
};
let bubble: map.Bubble = await this.mapController.addBubble(bubbleOptions);

#### \[h2\]setPadding

setPadding(padding?: mapCommon.Padding): void

Sets the padding between the map and its edges to define the visible region of a map. Map layer elements will adapt to the padding. For example, elements such as the zoom controls and compass will be moved to adapt to the visible region, and the camera will move in relative to the center of the visible region.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

padding

 | 

[mapCommon.Padding](../../mapcommon-map-attribute-model/document.md#section144591344648)

 | 

No

 | 

Padding between the map and its edges. The default value is **{ left: 0, right: 0, top: 0, bottom: 0 }**.

 |

**Example**:

// Initialization parameters. The left padding is 0 px and the bottom padding is 50 px.
let padding: mapCommon.Padding = {
  left: 0,
  bottom: 50
};
this.mapController.setPadding(padding);

#### \[h2\]getProjection

getProjection(): Projection

Obtains a **Projection** object that converts between the screen coordinates and the longitude-latitude coordinates.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[Projection](../projection/document.md)

 | 

[Projection](../projection/document.md) object.

 |

**Example**:

let projection: map.Projection = this.mapController.getProjection();

#### \[h2\]setCustomMapStyle

setCustomMapStyle(customMapStyleOptions: mapCommon.CustomMapStyleOptions): Promise<void>

Sets the map style to a custom style. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

customMapStyleOptions

 | 

[mapCommon.CustomMapStyleOptions](../../mapcommon-map-attribute-model/document.md#section13899143818719)

 | 

Yes

 | 

Custom style parameters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1002601002

 | 

The custom map style file does not exist.

 |
| 

1002601004

 | 

The style content format is incorrect.

 |

**Example**:

// Replace the value of **styleId** with your own style ID. The style ID can be created on the [Petal Maps Studio](https://developer.petalmaps.com/console/studio/) platform.
let param: mapCommon.CustomMapStyleOptions = {
  styleId: "xxxxxxx"
};
await this.mapController.setCustomMapStyle(param);

#### \[h2\]getDayNightMode

getDayNightMode(): mapCommon.DayNightMode

Obtains the day/dark mode of the map.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[mapCommon.DayNightMode](../../mapcommon-map-attribute-model/document.md#section634916281725)

 | 

Day/Dark mode.

 |

**Example**:

let mode = this.mapController.getDayNightMode();

#### \[h2\]setDayNightMode

setDayNightMode(mode: mapCommon.DayNightMode): void

Sets the day/dark mode of a map.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

mode

 | 

[mapCommon.DayNightMode](../../mapcommon-map-attribute-model/document.md#section634916281725)

 | 

Yes

 | 

Day/Dark mode.

 |

**Example**:

this.mapController.setDayNightMode(mapCommon.DayNightMode.AUTO);

#### \[h2\]getMapType

getMapType(): mapCommon.MapType

Obtains the map type.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[mapCommon.MapType](../../mapcommon-map-attribute-model/document.md#en-us_topic_0000001245084266_section18522846142615)

 | 

Map type.

 |

**Example**:

let mapType = this.mapController.getMapType();

#### \[h2\]setMapType

setMapType(mapType: mapCommon.MapType): void

Sets the map type.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

mapType

 | 

[mapCommon.MapType](../../mapcommon-map-attribute-model/document.md#en-us_topic_0000001245084266_section18522846142615)

 | 

Yes

 | 

Map type.

 |

**Example**:

this.mapController.setMapType(mapCommon.MapType.TERRAIN);

#### \[h2\]setScalePosition

setScalePosition(point: mapCommon.MapPoint): void

Sets the position of the scale control.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

point

 | 

[mapCommon.MapPoint](../../mapcommon-map-attribute-model/document.md#section123881566186)

 | 

Yes

 | 

Position of the scale control.

NOTE:

On wearable devices, the scale control is horizontally centered by default, and the passed **positionX** does not take effect.

 |

**Example**:

let point: mapCommon.MapPoint = {
  // Use the upper left corner of the current map component as the origin and move 1000 pixels rightwards.
  positionX: 1000,
  // Use the upper left corner of the current map component as the origin and move 1000 pixels downwards.
  positionY: 1000
};
this.mapController.setScalePosition(point);

#### \[h2\]getScaleLevel

getScaleLevel(): number

Obtains the scale at the current zoom level.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

number

 | 

Numeric value displayed on the scale, in meters.

 |

**Example**:

let level = this.mapController.getScaleLevel();

#### \[h2\]setCompassPosition

setCompassPosition(point: mapCommon.MapPoint): void

Sets the compass position.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

point

 | 

[mapCommon.MapPoint](../../mapcommon-map-attribute-model/document.md#section123881566186)

 | 

Yes

 | 

Compass position, which is the offset of the upper left corner of the compass relative to the upper left corner of the map component. The unit is px.

 |

**Example**:

let point: mapCommon.MapPoint = {
  positionX: 10,
  positionY: 10
};
this.mapController.setCompassPosition(point);

#### \[h2\]setAllGesturesEnabled

setAllGesturesEnabled(enabled: boolean): void

Sets whether to enable all gestures.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

enabled

 | 

boolean

 | 

Yes

 | 

-   **true**: Enable all gestures.
-   **false**: Disable all gestures.

The default value is **true**.

 |

**Example**:

this.mapController.setAllGesturesEnabled(true);

#### \[h2\]getScaleControlsHeight

getScaleControlsHeight(): number

Obtains the height of the scale control.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Height of the scale control, in vp.

 |

**Example**:

let height = this.mapController.getScaleControlsHeight();

#### \[h2\]getScaleControlsWidth

getScaleControlsWidth(): number

Obtains the width of the scale control.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Width of the scale control, in vp.

 |

**Example**:

let width = this.mapController.getScaleControlsWidth();

#### \[h2\]setAlwaysShowScaleEnabled

setAlwaysShowScaleEnabled(enabled: boolean): void

Sets whether to always display the scale. Before using this API, call [setScaleControlsEnabled](#section1845222318187) to enable the scale control first.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

enabled

 | 

boolean

 | 

Yes

 | 

-   **true**: Always display the scale control.
-   **false**: Not always display the scale control. The scale control will appear for 2 seconds and then disappear.

The default value is **false**.

 |

**Example**:

this.mapController.setAlwaysShowScaleEnabled(true);

#### \[h2\]isAlwaysShowScaleEnabled

isAlwaysShowScaleEnabled(): boolean

Checks whether the scale is configured to be always displayed.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

-   **true**: The scale is configured to be always displayed.
-   **false**: The scale is configured to be not always displayed.

 |

**Example**:

let scaleEnabled: boolean = this.mapController.isAlwaysShowScaleEnabled();

#### \[h2\]addClusterOverlay

addClusterOverlay(params: mapCommon.ClusterOverlayParams): Promise<ClusterOverlay>

Adds a ClusterOverlay. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

params

 | 

[mapCommon.ClusterOverlayParams](../../mapcommon-map-attribute-model/document.md#section693971514320)

 | 

Yes

 | 

ClusterOverlay parameters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ClusterOverlay](../clusteroverlay/document.md)\>

 | 

Promise that returns [ClusterOverlay](../clusteroverlay/document.md).

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter.

 |
| 

1002601001

 | 

The object to be operated does not exist.

 |

**Example**:

let clusterItem1: mapCommon.ClusterItem = {
  position: {
    latitude: 31.98,
    longitude: 118.766
  }
};
let clusterItem2: mapCommon.ClusterItem = {
  position: {
    latitude: 31.68,
    longitude: 118.366
  }
};
let array: Array<mapCommon.ClusterItem> = \[
  clusterItem1,
  clusterItem2
\];
let clusterOverlayParams: mapCommon.ClusterOverlayParams = { distance: 40, clusterItems: array };
let clusterOverlay: map.ClusterOverlay = await this.mapController.addClusterOverlay(clusterOverlayParams);

#### \[h2\]addImageOverlay

addImageOverlay(params: mapCommon.ImageOverlayParams): Promise<ImageOverlay>

Adds an ImageOverlay. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

params

 | 

[mapCommon.ImageOverlayParams](../../mapcommon-map-attribute-model/document.md#section12537418218)

 | 

Yes

 | 

ImageOverlay parameters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ImageOverlay](../imageoverlay/document.md)\>

 | 

Promise that returns [ImageOverlay](../imageoverlay/document.md).

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter.

 |
| 

1002601001

 | 

The object to be operated does not exist.

 |

**Example**:

let imageOverlayParams: mapCommon.ImageOverlayParams = {
  bounds: {
    southwest: { latitude: 32, longitude: 118 },
    northeast: { latitude: 32.4, longitude: 118.4 }
  },
  // The icon must be stored in the **resources/rawfile** directory.
  image: 'icon/icon.png',
  transparency: 0.3,
  zIndex: 101,
  anchorU: 0.5,
  anchorV: 0.5,
  clickable: true,
  visible: true,
  bearing: 0
};
let imageOverlay = await this.mapController?.addImageOverlay(imageOverlayParams);

#### \[h2\]snapshot

snapshot(): Promise<image.PixelMap>

Generates a map snapshot. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\>

 | 

Promise that returns [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md).

 |

**Example**:

import { image } from '@kit.ImageKit';

let image: image.PixelMap = await this.mapController.snapshot();

#### \[h2\]addBuildingOverlay

addBuildingOverlay(params: mapCommon.BuildingOverlayParams): Promise<BuildingOverlay>

Adds a BuildingOverlay. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

params

 | 

[mapCommon.BuildingOverlayParams](../../mapcommon-map-attribute-model/document.md#section316117228284)

 | 

Yes

 | 

BuildingOverlay attributes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[BuildingOverlay](../buildingoverlay/document.md)\>

 | 

Promise that returns [BuildingOverlay](../buildingoverlay/document.md).

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter.

 |
| 

1002601001

 | 

The object to be operated does not exist.

 |

**Example**:

let points: Array<mapCommon.LatLng> = \[
  {
    latitude: 31.984794,
    longitude: 118.765865
  },
  {
    latitude: 31.98468,
    longitude: 118.766076
  },
  {
    latitude: 31.98472,
    longitude: 118.766116
  },
  {
    latitude: 31.98463,
    longitude: 118.766292
  },
  {
    latitude: 31.984586,
    longitude: 118.766251
  },
  {
    latitude: 31.984536,
    longitude: 118.766344
  },
  {
    latitude: 31.984633,
    longitude: 118.766446
  },
  {
    latitude: 31.9848,
    longitude: 118.766285
  },
  {
    latitude: 31.984925,
    longitude: 118.766312
  },
  {
    latitude: 31.985282,
    longitude: 118.766661
  },
  {
    latitude: 31.985438,
    longitude: 118.766419
  },
  {
    latitude: 31.985801,
    longitude: 118.766755
  },
  {
    latitude: 31.985856,
    longitude: 118.766504
  },
  {
    latitude: 31.985785,
    longitude: 118.766434
  },
  {
    latitude: 31.985821,
    longitude: 118.766278
  },
  {
    latitude: 31.985897,
    longitude: 118.766311
  },
  {
    latitude: 31.985944,
    longitude: 118.766095
  },
  {
    latitude: 31.985909,
    longitude: 118.766069
  },
  {
    latitude: 31.985794,
    longitude: 118.765989
  },
  {
    latitude: 31.9857,
    longitude: 118.766029
  },
  {
    latitude: 31.985658,
    longitude: 118.766164
  },
  {
    latitude: 31.985647,
    longitude: 118.766271
  },
  {
    latitude: 31.985574,
    longitude: 118.766297
  },
  {
    latitude: 31.985458,
    longitude: 118.766285
  },
  {
    latitude: 31.985271,
    longitude: 118.766002
  },
  {
    latitude: 31.985219,
    longitude: 118.766002
  },
  {
    latitude: 31.985135,
    longitude: 118.766029
  },
  {
    latitude: 31.985093,
    longitude: 118.766083
  },
  {
    latitude: 31.985019,
    longitude: 118.766109
  },
  {
    latitude: 31.984978,
    longitude: 118.766083
  },
  {
    latitude: 31.984794,
    longitude: 118.765865
  }
\];
points.reverse();
// BuildingOverlay parameters.
let buildingOverlayOptions: mapCommon.BuildingOverlayParams =
  {
    // Range of the BuildingOverlay (the points are drawn clockwise).
    points: points,
    // Height of the BuildingOverlay.
    totalHeight: 51,
    // Height of the selected floor in the BuildingOverlay.
    floorBottomHeight: 33,
    // Color of the BuildingOverlay's rooftop.
    topFaceColor: 0xffa4b8f7,
    // Color of the BuildingOverlay's lateral surface.
    sideFaceColor: 0x44a4b8f7,
    // Color of the selected floor in the BuildingOverlay.
    floorColor: 0xff000000,
    // Floor from which the BuildingOverlay starts to be displayed.
    showLevel: 14,
    // Animation duration for the selected floor in the BuildingOverlay rising from the bottom.
    animationDuration: 5000,
    // Texture of the BuildingOverlay's lateral surface.
    sideTexture: { image: $r("app.media.side\_tex"), height: 3, width: 3 },
    // Texture of the selected floor in the BuildingOverlay.
    floorTexture: { image: $r("app.media.floor\_tex"), height: 3, width: 3 }
  };
let cameraUpdate = map.newCameraPosition({
  target: {
    latitude: 31.984794,
    longitude: 118.765865
  },
  zoom: 18,
  tilt: 70
});
// Move the map camera to focus on the BuildingOverlay area.
this.mapController?.moveCamera(cameraUpdate);
// Create a BuildingOverlay.
let buildingOverlay: map.BuildingOverlay = await this.mapController?.addBuildingOverlay(buildingOverlayOptions);

#### \[h2\]addTraceOverlay

addTraceOverlay(params: mapCommon.TraceOverlayParams, markers?: Array<Marker>): Promise<TraceOverlay>

Draws a TraceOverlay. A group of Markers can be passed. The Markers can move with the TraceOverlay. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

params

 | 

[mapCommon.TraceOverlayParams](../../mapcommon-map-attribute-model/document.md#section202444375510)

 | 

Yes

 | 

TraceOverlay parameters.

 |
| 

markers

 | 

Array<[Marker](../marker/document.md)\>

 | 

No

 | 

Image array of the TraceOverlay. Invalid values are not processed.

NOTE:

The positions of the passed Markers must be the same.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[TraceOverlay](../traceoverlay/document.md)\>

 | 

Promise that returns [TraceOverlay](../traceoverlay/document.md).

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter.

 |
| 

1002601001

 | 

The object to be operated does not exist.

 |

**Example**:

// Parameters of Marker 1.
let markerOptions1: mapCommon.MarkerOptions = {
  position: {
    latitude: 31.99227173519985,
    longitude: 118.7622219990476
  },
  // The icon must be stored in the **resources/base/media** directory.
  icon: $r("app.media.track\_setting\_sport\_map\_marker\_22"),
  anchorU: 0.5,
  anchorV: 1,
  visible: true
};
// Add Marker 1.
let markerBoy1 = await this.mapController.addMarker(markerOptions1);
let boyImages1: map.PlayImageAnimation = new map.PlayImageAnimation();
boyImages1.setDuration(1000);
let resourceArray: Array<Resource> = new Array();
resourceArray.push($r("app.media.side\_0"));
resourceArray.push($r("app.media.side\_1"));
resourceArray.push($r("app.media.side\_2"));
resourceArray.push($r("app.media.side\_3"));
resourceArray.push($r("app.media.side\_4"));
resourceArray.push($r("app.media.side\_5"));
resourceArray.push($r("app.media.side\_6"));
resourceArray.push($r("app.media.side\_7"));
resourceArray.push($r("app.media.side\_8"));
resourceArray.push($r("app.media.side\_9"));
resourceArray.push($r("app.media.side\_10"));
resourceArray.push($r("app.media.side\_11"));
resourceArray.push($r("app.media.side\_12"));
resourceArray.push($r("app.media.side\_13"));
resourceArray.push($r("app.media.side\_14"));
resourceArray.push($r("app.media.side\_15"));
resourceArray.push($r("app.media.side\_16"));
resourceArray.push($r("app.media.side\_17"));
resourceArray.push($r("app.media.side\_18"));
resourceArray.push($r("app.media.side\_19"));
resourceArray.push($r("app.media.side\_20"));
await boyImages1.addImages(resourceArray);
boyImages1.setRepeatCount(-1);

// Add an animation for Marker 1.
markerBoy1.setAnimation(boyImages1);
markerBoy1.startAnimation();

// Parameters of Marker 2.
let markerOptions2: mapCommon.MarkerOptions = {
  position: {
    latitude: 31.99227173519985,
    longitude: 118.7622219990476
  },
  // The icon must be stored in the **resources/base/media** directory.
  icon: $r("app.media.track\_setting\_sport\_map\_marker\_22"),
  anchorU: 0.5,
  anchorV: 1,
  visible: false
};
// Add Marker 2.
let markerBoy2 = await this.mapController.addMarker(markerOptions2);
let boyImages2: map.PlayImageAnimation = new map.PlayImageAnimation();
boyImages2.setDuration(1000);
let resourceArray2: Array<Resource> = new Array();
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_000"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_001"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_002"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_003"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_004"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_005"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_006"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_007"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_008"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_009"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_010"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_011"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_012"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_013"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_014"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_015"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_016"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_017"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_018"));
await boyImages2.addImages(resourceArray2);
boyImages2.setRepeatCount(-1);
// Add an animation for Marker 2.
markerBoy2.setAnimation(boyImages2);
markerBoy2.startAnimation();

let points: Array<mapCommon.LatLng> = new Array();
points.push({ latitude: 31.99685233070878, longitude: 118.75846023442728 });
points.push({ latitude: 31.99671325810786, longitude: 118.75846738985165 });
points.push({ latitude: 31.99659191076709, longitude: 118.7585347621686 });
points.push({ latitude: 31.99648202537233, longitude: 118.7586266510386 });
points.push({ latitude: 31.99637707201552, longitude: 118.75872004590596 });
points.push({ latitude: 31.996278207010903, longitude: 118.75880449946251 });
points.push({ latitude: 31.996187481969695, longitude: 118.7588781960278 });
points.push({ latitude: 31.996092248919354, longitude: 118.75895330554488 });
points.push({ latitude: 31.995962740450565, longitude: 118.75904721407304 });
points.push({ latitude: 31.995792921394, longitude: 118.75916904998051 });
points.push({ latitude: 31.995601885713416, longitude: 118.7593235241019 });
points.push({ latitude: 31.995398221178277, longitude: 118.75949998588176 });
points.push({ latitude: 31.995185902197715, longitude: 118.7596871082939 });
points.push({ latitude: 31.994983473052656, longitude: 118.75987334062296 });
points.push({ latitude: 31.99482433699269, longitude: 118.76002095184032 });
points.push({ latitude: 31.994709073721708, longitude: 118.76012902920532 });
points.push({ latitude: 31.99460732100702, longitude: 118.76023892576234 });
points.push({ latitude: 31.99449284962087, longitude: 118.7603694232856 });
points.push({ latitude: 31.99435358179254, longitude: 118.76053622438056 });
points.push({ latitude: 31.99420771148339, longitude: 118.76072790126692 });
points.push({ latitude: 31.994075194901523, longitude: 118.7609100960977 });
points.push({ latitude: 31.993952686158877, longitude: 118.7610741329013 });
points.push({ latitude: 31.993840180644217, longitude: 118.7612193418965 });
points.push({ latitude: 31.993733787150244, longitude: 118.76135383115654 });
points.push({ latitude: 31.993617206525155, longitude: 118.76150529647698 });

// Input parameters of the TraceOverlay.
let traceOptions: mapCommon.TraceOverlayParams = {
  // Trajectory points.
  points: points,
  // TraceOverlay animation duration.
  animationDuration: 5000,
  // Whether the camera follows the animation path.
  isMapMoving: true,
  // TraceOverlay color.
  color: 0xAAFFAA00,
  // TraceOverlay width.
  width: 20,
  // TraceOverlay animation callback (using the trajectory point index).
  animationCallback: (pointIndex) => {
    // Change to cycling.
    if (pointIndex === 10) {
      markerBoy1.setVisible(false);
      markerBoy2.setVisible(true);
    }
  }
};
let markers: Array<map.Marker> = new Array();
markers.push(markerBoy1, markerBoy2);
// Add a trajectory point animation.
let traceOverlay: map.TraceOverlay = await this.mapController.addTraceOverlay(traceOptions, markers);

#### \[h2\]addArc

addArc(params: mapCommon.MapArcParams): MapArc

Adds a MapArc to the map.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

params

 | 

[mapCommon.MapArcParams](../../mapcommon-map-attribute-model/document.md#section943619551002)

 | 

Yes

 | 

MapArc attributes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

MapArc

 | 

Returns [MapArc](../maparc/document.md).

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter.

 |
| 

1002601001

 | 

The object to be operated does not exist.

 |

**Example**:

// Set MapArc parameters.
let mapArcParams: mapCommon.MapArcParams = {
  // Coordinates of the MapArc start point.
  startPoint: {
    latitude: 39.913138,
    longitude: 116.415112
  },
  // Coordinates of the MapArc end point.
  endPoint: {
    latitude: 28.239473,
    longitude: 112.954094
  },
  // Coordinates of the MapArc center point.
  centerPoint: {
    latitude: 33.86970399048567,
    longitude: 112.08633528544145
  },
  width: 10,
  color: 0xffff0000,
  visible: true,
  zIndex: 100
};
// Add a MapArc.
this.mapController.addArc(mapArcParams);

#### \[h2\]show

show(): void

Switches the map to the foreground. You can call this API in **onPageShow**, which is a function in the page lifecycle.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Example**:

// This is called each time a page is displayed, for example, during page redirection or when the app is switched to the foreground. It works only for the custom components decorated by **@Entry**.
onPageShow(): void {
  // Switch the map to the foreground.
  if (this.mapController) {
    this.mapController.show();
  }
}

#### \[h2\]hide

hide(): void

Switches the map to the background. You can call this API in **onPageHide**, which is a function in the page lifecycle.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Example**:

// This is called each time a page is hidden, for example, during page redirection or when the app is switched to the background. It works only for the custom components decorated by **@Entry**.
onPageHide(): void {
  // Switch the map to the background.
  if (this.mapController) {
    this.mapController.hide();
  }
}

#### \[h2\]getEventManager

getEventManager(): MapEventManager

Obtains the map listening event manager.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[MapEventManager](../mapeventmanager/document.md)

 | 

Map event listening manager.

 |

**Example**:

let mapEventManager: map.MapEventManager = this.mapController.getEventManager();

#### \[h2\]setDisplayOrder

setDisplayOrder(types: Array<mapCommon.MapElementType>): void

Sets the overlay order of map elements from bottom to top, which means that subsequent overlays will visually stack on top of previous ones.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

types

 | 

Array<[mapCommon.MapElementType](../../mapcommon-map-attribute-model/document.md#section17215821103111)\>

 | 

Yes

 | 

Overlay order of the four types of map elements. The default order is \[1, 2, 3, 4\].

The parameter value length must be 4. Each element in the parameter value must be an enumerated value defined in [mapCommon.MapElementType](../../mapcommon-map-attribute-model/document.md#section17215821103111). Otherwise, error code 401 is returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter.

 |

**Example**:

let mapElementTypeArr: Array<mapCommon.MapElementType> = \[
  mapCommon.MapElementType.OVERLAY,
  mapCommon.MapElementType.POI,
  mapCommon.MapElementType.CUSTOM\_POI,
  mapCommon.MapElementType.MARKER\];
this.mapController.setDisplayOrder(mapElementTypeArr);

#### \[h2\]setLogoScale

setLogoScale(logoScale: number): void

Sets the logo scaling ratio.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.3(15)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

logoScale

 | 

number

 | 

Yes

 | 

Logo scaling ratio. The value ranges from 0.8 to 1. Error code 401 will be returned for any invalid value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter.

 |

**Example**:

this.mapController.setLogoScale(0.9);

#### \[h2\]getLogoScale

getLogoScale(): number

Obtains the logo scaling ratio. The scaling ratio ranges from 0.8 to 1. For any value not within the range, the default value **1** is returned.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.3(15)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Logo scaling ratio.

 |

**Example**:

let logoScale: number = this.mapController.getLogoScale();

#### \[h2\]isSphereEnabled

isSphereEnabled(): boolean

Checks whether the 3D globe view is enabled.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.3(15)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

-   **true**: The 3D globe view is enabled.
-   **false**: The 3D globe view is disabled.

 |

**Example**:

let result: boolean = this.mapController.isSphereEnabled();

#### \[h2\]setSphereEnabled

setSphereEnabled(enabled: boolean): void

Sets whether to enable the 3D globe view.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.3(15)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

enabled

 | 

boolean

 | 

Yes

 | 

Indicates whether to enable the 3D globe view. The options are as follows:

-   **true**: yes
-   **false**: no

The default value is **false**.

 |

**Example**:

this.mapController.setSphereEnabled(true);

#### \[h2\]setSphereEnabled

setSphereEnabled(enabled: boolean, animateDuration: number): void

Animates the switch between the 2D and 3D globe view.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

enabled

 | 

boolean

 | 

Yes

 | 

Animates the switch between the 2D and 3D globe view. The options are as follows:

-   **true**: switch to the 3D globe view.
-   **false**: switch to the 2D globe view.

The default value is **false**.

 |
| 

animateDuration

 | 

number

 | 

Yes

 | 

Animation duration, in ms.

 |

**Example**:

this.mapController.setSphereEnabled(true, 1000);

#### \[h2\]addHeatmap

addHeatmap(params: mapCommon.HeatmapParams): Promise<Heatmap>

Adds a heatmap. This API returns the result asynchronously through a promise. Heatmaps are well suited for visualizing data density in large-scale scenarios, such as pedestrian flow distribution and hotspot areas.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

params

 | 

[mapCommon.HeatmapParams](../../mapcommon-map-attribute-model/document.md#section273113662417)

 | 

Yes

 | 

Parameters for adding a heatmap.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Heatmap](../heatmap/document.md)\>

 | 

Promise that returns [Heatmap](../heatmap/document.md).

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1002601001

 | 

The object to be operated does not exist.

 |
| 

1002600015

 | 

The heatmap ID already exists.

 |

**Example**:

let data: mapCommon.WeightedLatLng\[\] = \[\];
for (let i = 0; i < 500; i++) {
  data.push({
    point: {
      longitude: 118.000000 + Math.random() \* 1 - 0.25,
      latitude: 31.000000 + Math.random() \* 1 - 0.25,
    },
    intensity: 1
  });
}
let heatMapOptions: mapCommon.HeatmapParams = {
  id: 'heatmap0001',
  data: data,
  radius: 20,
  intensity: {
    2: 1,
    5: 5,
    8: 10
  },
}
await this.mapController?.addHeatmap(heatMapOptions)

#### \[h2\]addMvtOverlay

addMvtOverlay(params: mapCommon.MvtOverlayParams): MvtOverlay

Adds an MvtOverlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core.EnhancedOverlay

**Start version**: 6.0.0(20)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

params

 | 

[mapCommon.MvtOverlayParams](../../mapcommon-map-attribute-model/document.md#section17301232184)

 | 

Yes

 | 

MvtOverlay parameters.

NOTE:

To add an MvtOverlay using an online resource (via the **tileUrl** method specified in the [mapCommon.MvtSource](../../mapcommon-map-attribute-model/document.md#section877213310341) parameter of [mapCommon.MvtOverlayParams](../../mapcommon-map-attribute-model/document.md#section17301232184)), you must apply for the network access permission **ohos.permission.INTERNET**.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[MvtOverlay](../mvtoverlay/document.md)

 | 

MvtOverlay object.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1022100001

 | 

The operation object does not exist.

 |

let params: mapCommon.MvtOverlayParams = {
  source: {
    // Set the URL of the MvtOverlay, which must start with **http** or **https** and contain placeholders {x}, {y}, and {z}.
    tileUrl: 'http://xxx/tiles/{z}/{x}/{y}.pbf',
    minZoom: 2,
    maxZoom: 15
  },
  layers: \[{
    id: 'layer-map',
    type: mapCommon.MvtLayerType.FILL,
    // MvtOverlay name.
    sourceLayer: 'XX',
    paint: {
      fillColor: {
        operator: mapCommon.Operator.GET,
        args: 'fill'
      },
      fillOpacity: {
        operator: mapCommon.Operator.GET,
        args: 'fill-opacity'
      }
    }
  }\]
};
let mvtOverlay = this.mapController?.addMvtOverlay(params);

#### \[h2\]setFramePerSecond

setFramePerSecond(fps: number): void

Sets the expected number of frames per second.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

fps

 | 

number

 | 

Yes

 | 

Expected number of frames per second. The value ranges from 1 to 60.

 |

**Example**:

this.mapController?.setFramePerSecond(60);

#### \[h2\]addFlowFieldOverlay

addFlowFieldOverlay(params: mapCommon.FlowFieldOverlayParams): Promise<FlowFieldOverlay>

Adds a FlowFieldOverlay, which is applicable to wind field and ocean current scenarios. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core.EnhancedOverlay

**Start version**: 6.0.0(20)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

params

 | 

[mapCommon.FlowFieldOverlayParams](../../mapcommon-map-attribute-model/document.md#section1920897172416)

 | 

Yes

 | 

FlowFieldOverlay parameters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[FlowFieldOverlay](../flowfieldoverlay/document.md)\>

 | 

Promise object that returns the FlowFieldOverlay object.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1022100001

 | 

The operation object does not exist.

 |

**Example**:

let params: mapCommon.FlowFieldOverlayParams = {
  // The value of **data** must be in JSON format that complies with the GRIB2 specification. Set **data** by referring to [Flow Field Data Format Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-flow-field#section138174613135).
  data: 'xxx'
};
let fieldOverlay = await this.mapController.addFlowFieldOverlay(params);

#### \[h2\]addMassPointOverlay

addMassPointOverlay(params: mapCommon.MassPointOverlayParams): Promise<MassPointOverlay>

Adds a MassPointOverlay. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

params

 | 

[mapCommon.MassPointOverlayParams](../../mapcommon-map-attribute-model/document.md#section1423475535919)

 | 

Yes

 | 

MassPointOverlay parameters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[MassPointOverlay](../masspointoverlay/document.md)\>

 | 

Promise that returns the MassPointOverlay object.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1002601001

 | 

The object to be operated does not exist.

 |

**Example**:

let items: mapCommon.MassPointItem\[\] = \[\];
for (let i = 0; i < 1000; i++) {
  // Save mass points to **items**.
  items.push({
    itemId: 'test' + i,
    position: {
      longitude: 118.11111 + Math.random() \* 1 - 0.5,
      latitude: 32.11111 + Math.random() \* 1 - 0.5,
    },
    snippet: 'test' + i,
    title: 'test' + i
  })
}
let params: mapCommon.MassPointOverlayParams = {
  id: 'test',
  items: items,
  // The icon is stored in **resources/rawfile**. Set **icon** to the relative path of the icon file in the **rawfile** folder.
  icon: 'icon/maps\_blue\_dot.png',
}
let massPointOverlay = await this.mapController?.addMassPointOverlay(params);

#### \[h2\]setLanguage

setLanguage(language: string): void

Sets the language of the map component.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

language

 | 

string

 | 

Yes

 | 

Map language. Refer to [Languages supported by the map component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-language#section105361721671) for supported language options.

 |

**Example**:

this.mapController?.setLanguage('ja');

#### \[h2\]getLanguage

getLanguage(): string

Obtains the language of the map component.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Map language. Refer to [Languages supported by the map component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-language#section105361721671) for supported language options.

 |

**Example**:

let language = this.mapController?.getLanguage();

#### \[h2\]changeMyLocationLayerOrder

changeMyLocationLayerOrder(isBelow: boolean): void

Changes the stacking order of the **my-location** layer relative to overlays.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.1(21)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

isBelow

 | 

boolean

 | 

Yes

 | 

Indicates whether the **my-location** layer is below overlays.

-   **true**: The **my-location** layer is below overlays.
-   **false**: The **my-location** layer is above overlays.

NOTE:

This API takes effect for the [Marker](../marker/document.md), [MapPolyline](../mappolyline/document.md), [MapPolygon](../mappolygon/document.md), [MapCircle](../mapcircle/document.md), [PointAnnotation](../pointannotation/document.md), [Bubble](../bubble/document.md), [ImageOverlay](../imageoverlay/document.md), [MapArc](../maparc/document.md), [TraceOverlay](../traceoverlay/document.md), and base map [POI](../../mapcommon-map-attribute-model/document.md#section1155919456273).

 |

**Example**:

this.mapController?.changeMyLocationLayerOrder(true);

#### \[h2\]addTileOverlay

addTileOverlay(params: mapCommon.TileOverlayParams | mapCommon.TileOverlayOptions): TileOverlay

Adds a TileOverlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.3(15)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

params

 | 

[mapCommon.TileOverlayParams](../../mapcommon-map-attribute-model/document.md#section3168172982513) | [mapCommon.TileOverlayOptions](../../mapcommon-map-attribute-model/document.md#section849136102717)

 | 

Yes

 | 

TileOverlay parameters.

NOTE:

The **params** parameter supports the [mapCommon.TileOverlayOptions](../../mapcommon-map-attribute-model/document.md#section849136102717) type since version 6.0.0(20).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[TileOverlay](../tileoverlay/document.md)

 | 

TileOverlay.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1002601001

 | 

The object to be operated does not exist.

 |

**Example**:

let params: mapCommon.TileOverlayOptions = {
  // Set the URL of the TileOverlay, which must start with **http** or **https** and contain placeholders {x}, {y}, and {z}.
  // Replace it with your own URL.
  tileUrl: "https://xxx/xxx?x={x}&y={y}&z={z}",
  // Set the transparency.
  transparency: 0.5,
  // Enable the TileOverlay fade-in effect.
  fadeIn: true,
  // Enable disk caching.
  diskCacheEnabled: true,
  // Disk cache size, in KB. The default value is **20480**.
  diskCacheSize: 20480,
  // Path of the sandbox for storing disk cache.
  diskCachePath: this.getUIContext().getHostContext()?.databaseDir
};
let tileOverlay: map.TileOverlay = this.mapController?.addTileOverlay(params);

#### \[h2\]on('cameraChange')

on(type: 'cameraChange', callback: Callback<mapCommon.LatLng>): void

Listens for map camera status change events. This API returns the result asynchronously through a callback. The callback is not triggered during animation. Instead, it is triggered when the animation ends.

You are advised to use [MapEventManager.on(type: 'cameraChange')](../mapeventmanager/document.md#section1488710318220).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'cameraChange'**: listens for map camera status change events.

 |
| 

callback

 | 

Callback<[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

Yes

 | 

Callback function, which returns [mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810). This callback is used to listen for map camera status change events. The callback is not triggered during animation. Instead, it is triggered when the animation ends.

 |

**Example**:

this.mapController.on("cameraChange", (position) => {
  console.info("cameraChange", \`on-cameraChange position = ${position.longitude}\`);
});

#### \[h2\]off('cameraChange')

off(type: 'cameraChange', callback: Callback<void>): void

Cancels listening for map camera status change events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'cameraChange')](../mapeventmanager/document.md#section1994982613283).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'cameraChange'**: listens for map camera status change events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("cameraChange", (position) => {
  console.info("cameraChange", \`off-cameraChange\`);
});

#### \[h2\]on('cameraIdle')

on(type: 'cameraIdle', callback: Callback<void>): void

Listens for camera movement end events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'cameraIdle')](../mapeventmanager/document.md#section1963201310319).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'cameraIdle'**: listens for camera movement end events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.on("cameraIdle", () => {
  console.info("cameraIdle", \`on-cameraIdle\`);
});

#### \[h2\]off('cameraIdle')

off(type: 'cameraIdle', callback: Callback<void>): void

Cancels listening for camera movement end events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'cameraIdle')](../mapeventmanager/document.md#section1763512138315).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'cameraIdle'**: listens for camera movement end events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("cameraIdle", () => {
  console.info("cameraIdle", \`off-cameraIdle\`);
});

#### \[h2\]on('cameraMoveCancel')

on(type: 'cameraMoveCancel', callback: Callback<void>): void

Listens for camera movement cancellation events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'cameraMoveCancel')](../mapeventmanager/document.md#section1322914471399).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'cameraMoveCancel'**: listens for camera movement cancellation events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.on("cameraMoveCancel", () => {
  console.info("cameraMoveCancel", \`on-cameraMoveCancel\`);
});

#### \[h2\]off('cameraMoveCancel')

off(type: 'cameraMoveCancel', callback: Callback<void>): void

Cancels listening for camera movement cancellation events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'cameraMoveCancel')](../mapeventmanager/document.md#section10232124743913).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'cameraMoveCancel'**: listens for camera movement cancellation events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("cameraMoveCancel", () => {
  console.info("cameraMoveCancel", \`off-cameraMoveCancel\`);
});

#### \[h2\]on('cameraMove')

on(type: 'cameraMove', callback: Callback<void>): void

Listens for camera movement events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'cameraMove')](../mapeventmanager/document.md#section142347477396).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'cameraMove'**: listens for camera movement events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.on("cameraMove", () => {
  console.info("cameraMove", \`on-cameraMove\`);
});

#### \[h2\]off('cameraMove')

off(type: 'cameraMove', callback: Callback<void>): void

Cancels listening for camera movement events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'cameraMove')](../mapeventmanager/document.md#section1823714753912).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'cameraMove'**: listens for camera movement events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("cameraMove", () => {
  console.info("cameraMove", \`off-cameraMove\`);
});

#### \[h2\]on('cameraMoveStart')

on(type: 'cameraMoveStart', callback: Callback<number>): void

Listens for camera movement start events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'cameraMoveStart')](../mapeventmanager/document.md#section6240147113918).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'cameraMoveStart'**: listens for camera movement start events.

 |
| 

callback

 | 

Callback<number>

 | 

Yes

 | 

Callback function, which returns **number**.

**number** indicates the reason why the camera moves.

-   **1**: A user makes a gesture on the map.
-   **2**: The default animation is triggered by user interaction.
-   **3**: You start an animation.

 |

**Example**:

this.mapController.on("cameraMoveStart", (reason) => {
  console.info("cameraMoveStart", \`on-cameraMoveStart reason = ${reason}\`);
});

#### \[h2\]off('cameraMoveStart')

off(type: 'cameraMoveStart', callback: Callback<void>): void

Cancels listening for camera movement start events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'cameraMoveStart')](../mapeventmanager/document.md#section12243647133915).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'cameraMoveStart'**: listens for camera movement start events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("cameraMoveStart", () => {
  console.info("cameraMoveStart", \`off-cameraMoveStart\`);
});

#### \[h2\]on('mapClick')

on(type: 'mapClick', callback: Callback<mapCommon.LatLng>): void

Listens for map tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'mapClick')](../mapeventmanager/document.md#section824544714394).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'mapClick'**: listens for map tap events.

 |
| 

callback

 | 

Callback<[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

Yes

 | 

Callback function that returns [mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810).

 |

**Example**:

this.mapController.on("mapClick", (position) => {
  console.info("mapClick", \`on-mapClick position = ${position.longitude}\`);
});

#### \[h2\]off('mapClick')

off(type: 'mapClick', callback: Callback<void>): void

Cancels listening for map tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'mapClick')](../mapeventmanager/document.md#section02487472392).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'mapClick'**: listens for map tap events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("mapClick", () => {
  console.info("mapClick", \`off-mapClick\`);
});

#### \[h2\]on('mapLoad')

on(type: 'mapLoad', callback: Callback<void>): void

Listens for map load events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'mapLoad')](../mapeventmanager/document.md#section19251144723913).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'mapLoad'**: listens for map load events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.on("mapLoad", () => {
  console.info("mapLoad", \`on-mapLoad\`);
});

#### \[h2\]off('mapLoad')

off(type: 'mapLoad', callback: Callback<void>): void

Cancels listening for map load events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'mapLoad')](../mapeventmanager/document.md#section132541747133918).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'mapLoad'**: listens for map load events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("mapLoad", () => {
  console.info("mapLoad", \`off-mapLoad\`);
});

#### \[h2\]on('mapLongClick')

on(type: 'mapLongClick', callback: Callback<mapCommon.LatLng>): void

Listens for map long-press events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'mapLongClick')](../mapeventmanager/document.md#section0257247133915).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'mapLongClick'**: listens for map long-press events.

 |
| 

callback

 | 

Callback<[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

Yes

 | 

Callback function that returns [mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810).

 |

**Example**:

this.mapController.on("mapLongClick", () => {
  console.info("mapLongClick", \`on-mapLongClick\`);
});

#### \[h2\]off('mapLongClick')

off(type: 'mapLongClick', callback: Callback<void>): void

Cancels listening for map long-press events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'mapLongClick')](../mapeventmanager/document.md#section2261114753919).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'mapLongClick'**: listens for map long-press events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("mapLongClick", () => {
  console.info("mapLongClick", \`off-mapLongClick\`);
});

#### \[h2\]on('myLocationButtonClick')

on(type: 'myLocationButtonClick', callback: Callback<void>): void

Listens for **my-location** icon tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'myLocationButtonClick')](../mapeventmanager/document.md#section9264124723916).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'myLocationButtonClick'**: listens for **my-location** icon tap events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.on("myLocationButtonClick", () => {
  console.info("myLocationButtonClick", \`on-myLocationButtonClick\`);
});

#### \[h2\]off('myLocationButtonClick')

off(type: 'myLocationButtonClick', callback: Callback<void>): void

Cancels listening for **my-location** icon tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'myLocationButtonClick')](../mapeventmanager/document.md#section19268134715398).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'myLocationButtonClick'**: listens for **my-location** icon tap events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("myLocationButtonClick", () => {
  console.info("myLocationButtonClick", \`off-myLocationButtonClick\`);
});

#### \[h2\]on('myLocationClick')

on(type: 'myLocationClick', callback: Callback<mapCommon.LatLng>): void

Listens for **my-location** tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'myLocationClick')](../mapeventmanager/document.md#section827144713394).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'myLocationClick'**: listens for **my-location** tap events.

 |
| 

callback

 | 

Callback<[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

Yes

 | 

Callback function that returns [mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810).

 |

**Example**:

this.mapController.on("myLocationClick", (position) => {
  console.info("myLocationClick", \`on-myLocationClick position = ${position.longitude}\`);
});

#### \[h2\]off('myLocationClick')

off(type: 'myLocationClick', callback: Callback<void>): void

Cancels listening for **my-location** tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'myLocationClick')](../mapeventmanager/document.md#section10275247193911).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'myLocationClick'**: listens for **my-location** tap events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("myLocationClick", () => {
  console.info("myLocationClick", \`off-myLocationClick\`);
});

#### \[h2\]on('poiClick')

on(type: 'poiClick', callback: Callback<mapCommon.Poi>): void

Listens for POI tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'poiClick')](../mapeventmanager/document.md#section0279247143911).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'poiClick'**: listens for POI tap events.

 |
| 

callback

 | 

Callback<[mapCommon.Poi](../../mapcommon-map-attribute-model/document.md#section1155919456273)\>

 | 

Yes

 | 

Callback function, which returns [mapCommon.Poi](../../mapcommon-map-attribute-model/document.md#section1155919456273).

 |

**Example**:

this.mapController.on("poiClick", (poi) => {
  console.info("poiClick", \`on-poiClick poi = ${poi.id}\`);
});

#### \[h2\]off('poiClick')

off(type: 'poiClick', callback: Callback<void>): void

Cancels listening for POI tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'poiClick')](../mapeventmanager/document.md#section11283174743917).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'poiClick'**: listens for POI tap events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("poiClick", () => {
 console.info("poiClick", \`off-poiClick\`);
});

#### \[h2\]on('markerClick')

on(type: 'markerClick', callback: Callback<Marker>): void

Listens for Marker tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'markerClick')](../mapeventmanager/document.md#section19286104716392).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'markerClick'**: listens for Marker tap events.

 |
| 

callback

 | 

Callback<[Marker](../marker/document.md)\>

 | 

Yes

 | 

Callback function, which returns [Marker](../marker/document.md).

 |

**Example**:

this.mapController.on("markerClick", (marker) => {
 console.info("markerClick", \`on-markerClick position = ${marker.getId()}\`);
});

#### \[h2\]off('markerClick')

off(type: 'markerClick', callback: Callback<void>): void

Cancels listening for Marker tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'markerClick')](../mapeventmanager/document.md#section929019470390).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'markerClick'**: listens for Marker tap events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("markerClick", () => {
 console.info("markerClick", \`off-markerClick\`);
});

#### \[h2\]on('markerDragStart')

on(type: 'markerDragStart', callback: Callback<Marker>): void

Listens for Marker drag start events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'markerDragStart')](../mapeventmanager/document.md#section19294747123912).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'markerDragStart'**: listens for Marker drag start events.

 |
| 

callback

 | 

Callback<[Marker](../marker/document.md)\>

 | 

Yes

 | 

Callback function, which returns [Marker](../marker/document.md).

 |

**Example**:

this.mapController.on("markerDragStart", (marker) => {
 console.info("markerDragStart", \`on-markerDragStart position = ${marker.getId()}\`);
});

#### \[h2\]off('markerDragStart')

off(type: 'markerDragStart', callback: Callback<void>): void

Cancels listening for Marker drag start events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'markerDragStart')](../mapeventmanager/document.md#section16298847183914).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'markerDragStart'**: listens for Marker drag start events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("markerDragStart", () => {
 console.info("markerDragStart", \`off-markerDragStart\`);
});

#### \[h2\]on('markerDrag')

on(type: 'markerDrag', callback: Callback<Marker>): void

Listens for Marker drag events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'markerDrag')](../mapeventmanager/document.md#section103026476395).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'markerDrag'**: listens for Marker drag events.

 |
| 

callback

 | 

Callback<[Marker](../marker/document.md)\>

 | 

Yes

 | 

Callback function, which returns [Marker](../marker/document.md).

 |

**Example**:

this.mapController.on("markerDrag", (marker) => {
 console.info("markerDrag", \`on-markerDrag position = ${marker.getId()}\`);
});

#### \[h2\]off('markerDrag')

off(type: 'markerDrag', callback: Callback<void>): void

Cancels listening for Marker drag events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'markerDrag')](../mapeventmanager/document.md#section13306124793916).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'markerDrag'**: listens for Marker drag events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("markerDrag", () => {
 console.info("markerDrag", \`off-markerDrag\`);
});

#### \[h2\]on('markerDragEnd')

on(type: 'markerDragEnd', callback: Callback<Marker>): void

Listens for Marker drag end events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'markerDragEnd')](../mapeventmanager/document.md#section13310124719393).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'markerDragEnd'**: listens for Marker drag end events.

 |
| 

callback

 | 

Callback<[Marker](../marker/document.md)\>

 | 

Yes

 | 

Callback function, which returns [Marker](../marker/document.md).

 |

**Example**:

this.mapController.on("markerDragEnd", (marker) => {
 console.info("markerDragEnd", \`on-markerDragEnd position = ${marker.getId()}\`);
});

#### \[h2\]off('markerDragEnd')

off(type: 'markerDragEnd', callback: Callback<void>): void

Cancels listening for Marker drag end events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'markerDragEnd')](../mapeventmanager/document.md#section2031414753918).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'markerDragEnd'**: listens for Marker drag end events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("markerDragEnd", () => {
 console.info("markerDragEnd", \`off-markerDragEnd\`);
});

#### \[h2\]on('circleClick')

on(type: 'circleClick', callback: Callback<MapCircle>): void

Listens for MapCircle tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'circleClick')](../mapeventmanager/document.md#section83181474399).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'circleClick'**: listens for MapCircle tap events.

 |
| 

callback

 | 

Callback<[MapCircle](../mapcircle/document.md)\>

 | 

Yes

 | 

Callback function, which returns [MapCircle](../mapcircle/document.md).

 |

**Example**:

this.mapController.on("circleClick", (position) => {
 console.info("circleClick", \`on-circleClick position = ${position.getCenter().longitude}\`);
});

#### \[h2\]off('circleClick')

off(type: 'circleClick', callback: Callback<void>): void

Cancels listening for MapCircle tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'circleClick')](../mapeventmanager/document.md#section1232294710392).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'circleClick'**: listens for MapCircle tap events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("circleClick", () => {
 console.info("circleClick", \`off-circleClick\`);
});

#### \[h2\]on('polylineClick')

on(type: 'polylineClick', callback: Callback<MapPolyline>): void

Listens for MapPolyline tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'polylineClick')](../mapeventmanager/document.md#section732614710394).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'polylineClick'**: listens for MapPolyline tap events.

 |
| 

callback

 | 

Callback<[MapPolyline](../mappolyline/document.md)\>

 | 

Yes

 | 

Callback function, which returns [MapPolyline](../mappolyline/document.md).

 |

**Example**:

this.mapController.on("polylineClick", (polyline) => {
  console.info("polylineClick", \`on-polylineClick position = ${polyline.getId()}\`);
});

#### \[h2\]off('polylineClick')

off(type: 'polylineClick', callback: Callback<void>): void

Cancels listening for MapPolyline tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'polylineClick')](../mapeventmanager/document.md#section1233024711397).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'polylineClick'**: listens for MapPolyline tap events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("polylineClick", () => {
  console.info("polylineClick", "off-polylineClick");
});

#### \[h2\]on('polygonClick')

on(type: 'polygonClick', callback: Callback<MapPolygon>): void

Listens for MapPolygon tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'polygonClick')](../mapeventmanager/document.md#section933411473395).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'polygonClick'**: listens for MapPolygon tap events.

 |
| 

callback

 | 

Callback<[MapPolygon](../mappolygon/document.md)\>

 | 

Yes

 | 

Callback function, which returns [MapPolygon](../mappolygon/document.md).

 |

**Example**:

this.mapController.on("polygonClick", (polygon) => {
  console.info("polygonClick", \`on-polygonClick position = ${polygon.getId()}\`);
});

#### \[h2\]off('polygonClick')

off(type: 'polygonClick', callback: Callback<void>): void

Cancels listening for MapPolygon tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'polygonClick')](../mapeventmanager/document.md#section133964753915).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'polygonClick'**: listens for MapPolygon tap events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("polygonClick", () => {
  console.info("polygonClick", "off-polygonClick");
});

#### \[h2\]on('infoWindowClick')

on(type: 'infoWindowClick', callback: Callback<Marker>): void

Listens for information window tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'infoWindowClick')](../mapeventmanager/document.md#section12343194753919).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'infoWindowClick'**: listens for information window tap events.

 |
| 

callback

 | 

Callback<[Marker](../marker/document.md)\>

 | 

Yes

 | 

Callback function, which returns [Marker](../marker/document.md).

 |

**Example**:

this.mapController.on("infoWindowClick", (infoWindow) => {
 console.info("infoWindowClick", \`on-infoWindowClick infoWindow = ${infoWindow.getId()}\`);
});

#### \[h2\]off('infoWindowClick')

off(type: 'infoWindowClick', callback: Callback<void>): void

Cancels listening for information window tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'infoWindowClick')](../mapeventmanager/document.md#section18348114710396).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'infoWindowClick'**: listens for information window tap events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("infoWindowClick", () => {
 console.info("infoWindowClick", \`off-infoWindowClick\`);
});

#### \[h2\]on('infoWindowClose')

on(type: 'infoWindowClose', callback: Callback<Marker>): void

Listens for information window close events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'infoWindowClose')](../mapeventmanager/document.md#section10352194713912).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'infoWindowClose'**: listens for information window close events.

 |
| 

callback

 | 

Callback<[Marker](../marker/document.md)\>

 | 

Yes

 | 

Callback function, which returns [Marker](../marker/document.md).

 |

**Example**:

this.mapController.on("infoWindowClose", (infoWindowClose) => {
 console.info("infoWindowClose", \`on-infoWindowClose infoWindowClose = ${infoWindowClose.getId()}\`);
});

#### \[h2\]off('infoWindowClose')

off(type: 'infoWindowClose', callback: Callback<void>): void

Cancels listening for information window close events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'infoWindowClose')](../mapeventmanager/document.md#section535624713394).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'infoWindowClose'**: listens for information window close events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("infoWindowClose", () => {
 console.info("infoWindowClose", \`off-infoWindowClose\`);
});

#### \[h2\]on('pointAnnotationClick')

on(type: 'pointAnnotationClick', callback: Callback<PointAnnotation>): void

Listens for PointAnnotation tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'pointAnnotationClick')](../mapeventmanager/document.md#section636111479397).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'pointAnnotationClick'**: listens for PointAnnotation tap events.

 |
| 

callback

 | 

Callback<[PointAnnotation](../pointannotation/document.md)\>

 | 

Yes

 | 

Callback function, which returns [PointAnnotation](../pointannotation/document.md).

 |

**Example**:

this.mapController.on("pointAnnotationClick", (pointAnnotation) => {
 console.info("pointAnnotationClick", \`on-PointAnnotationClick pointAnnotation = ${pointAnnotation.getId()}\`);
});

#### \[h2\]off('pointAnnotationClick')

off(type: 'pointAnnotationClick', callback: Callback<void>): void

Cancels listening for PointAnnotation tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'pointAnnotationClick')](../mapeventmanager/document.md#section5365154710393).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'pointAnnotationClick'**: listens for PointAnnotation tap events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("pointAnnotationClick", () => {
 console.info("pointAnnotationClick", \`off-PointAnnotationClick\`);
});

#### \[h2\]on('bubbleClick')

on(type: 'bubbleClick', callback: Callback<Bubble>): void

Listens for Bubble tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'bubbleClick')](../mapeventmanager/document.md#section10369124763915).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'bubbleClick'**: listens for Bubble tap events.

 |
| 

callback

 | 

Callback<[Bubble](../bubble/document.md)\>

 | 

Yes

 | 

Callback function, which returns [Bubble](../bubble/document.md).

 |

**Example**:

this.mapController.on("bubbleClick", (bubble) => {
 console.info("bubbleClick", \`on-BubbleClick bubble = ${bubble.getId()}\`);
});

#### \[h2\]off('bubbleClick')

off(type: 'bubbleClick', callback: Callback<void>): void

Cancels listening for Bubble tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'bubbleClick')](../mapeventmanager/document.md#section13374114733920).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'bubbleClick'**: listens for Bubble tap events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("bubbleClick", () => {
 console.info("bubbleClick", \`off-BubbleClick\`);
});

#### \[h2\]on('imageOverlayClick')

on(type: 'imageOverlayClick', callback: Callback<ImageOverlay>): void

Listens for ImageOverlay tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.on(type: 'imageOverlayClick')](../mapeventmanager/document.md#section2379144743910).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'imageOverlayClick'**: listens for ImageOverlay tap events.

 |
| 

callback

 | 

Callback<[ImageOverlay](../imageoverlay/document.md#section361333917368)\>

 | 

Yes

 | 

Callback function, which returns [ImageOverlay](../imageoverlay/document.md#section361333917368).

 |

**Example**:

// Callback of the listening for ImageOverlay tap events.
let imageOverlayCallback: Callback<map.ImageOverlay> = (imageOverlay:map.ImageOverlay) => {
  console.info("imageOverlay:" + imageOverlay?.getId());
};
this.mapController.on("imageOverlayClick", imageOverlayCallback)

#### \[h2\]off('imageOverlayClick')

off(type: 'imageOverlayClick', callback?: Callback<ImageOverlay>): void

Cancels listening for ImageOverlay tap events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'imageOverlayClick')](../mapeventmanager/document.md#section123841147173920).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'imageOverlayClick'**: listens for ImageOverlay tap events.

 |
| 

callback

 | 

Callback<[ImageOverlay](../imageoverlay/document.md#section361333917368)\>

 | 

No

 | 

Callback function, which returns [ImageOverlay](../imageoverlay/document.md#section361333917368). If this parameter is not passed, all listening callbacks will be cleared.

 |

**Example**:

let imageOverlayCallback: Callback<map.ImageOverlay> = (imageOverlay:map.ImageOverlay) => {
  console.info("imageOverlay:" + imageOverlay?.getId());
};
this.mapController.off("imageOverlayClick", imageOverlayCallback);

#### \[h2\]on('error')

on(type: 'error', callback: ErrorCallback): void

Listens for error events.

You are advised to use [MapEventManager.on(type: 'error')](../mapeventmanager/document.md#section19389184720396).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'error'**: listens for error events.

 |
| 

callback

 | 

[ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback)

 | 

Yes

 | 

Callback function used to listen for error events.

 |

**Example**:

this.mapController.on("error", (error) => {
  console.error("error", \`on-error: Code: ${error.code}, message: ${error.message}\`);
});

#### \[h2\]off('error')

off(type: 'error', callback: Callback<void>): void

Cancels listening for error events. This API returns the result asynchronously through a callback.

You are advised to use [MapEventManager.off(type: 'error')](../mapeventmanager/document.md#section1439524793910).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'error'**: listens for error events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

this.mapController.off("error", () => {
  console.error("error", \`off-error\`);
});

#### \[h2\]setIndoorMapEnabled

setIndoorMapEnabled(enabled: boolean): void

Sets whether to enable the indoor map. The indoor map and floor selector control are only visible at zoom level 17 and higher.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 19 or later, this API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.1.1(19)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

enabled

 | 

boolean

 | 

Yes

 | 

Indicates whether to enable the indoor map. By default, the indoor map is disabled. If an invalid value is passed, the default value will be used. The options are as follows:

-   **true**: yes
-   **false**: no

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

801

 | 

Capability not supported. Failed to call the API due to limited device capabilities.

 |

**Example**:

// Enable the indoor map.
this.mapController.setIndoorMapEnabled(true);

#### \[h2\]isIndoorMapEnabled

isIndoorMapEnabled(): boolean

Checks whether the indoor map is enabled.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 19 or later, this API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.1.1(19)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

-   **true**: The indoor map is enabled.
-   **false**: The indoor map is disabled.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

801

 | 

Capability not supported. Failed to call the API due to limited device capabilities.

 |

**Example**:

let isIndoorMapEnabled = this.mapController.isIndoorMapEnabled();

#### \[h2\]switchIndoorMapFloor

switchIndoorMapFloor(buildingId: string, floorName: string): void

Switches to a specified indoor building floor.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 19 or later, this API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.1.1(19)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

buildingId

 | 

string

 | 

Yes

 | 

Building ID. The value is obtained from the callback function of the [on('indoorMapEnter')](../mapeventmanager/document.md#section76731728143918) method.

 |
| 

floorName

 | 

string

 | 

Yes

 | 

Building floor name (example: 3F). Invalid parameter values are not processed.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

801

 | 

Capability not supported. Failed to call the API due to limited device capabilities.

 |

**Example**:

this.mapController?.switchIndoorMapFloor('822588304363886720', '3F');

#### \[h2\]setFloorControlsPosition

setFloorControlsPosition(point: mapCommon.MapPoint): void

Sets the position of the floor selector control. Before using this API, call the [setIndoorMapEnabled](#section12159164214612) method to enable the indoor map function first. The indoor map and floor selector control are only visible at zoom level 17 and higher.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 20 or later, this API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 6.0.0(20)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

point

 | 

[mapCommon.MapPoint](../../mapcommon-map-attribute-model/document.md#section123881566186)

 | 

Yes

 | 

Position of the floor selector control, in px.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

801

 | 

Capability not supported. Failed to call the API due to limited device capabilities.

 |

**Example**:

this.mapController?.setFloorControlsPosition({
  positionX: 500,
  positionY: 500
});
