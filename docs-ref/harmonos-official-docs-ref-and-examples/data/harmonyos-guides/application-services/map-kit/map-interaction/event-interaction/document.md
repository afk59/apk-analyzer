# Event Interaction

This section describes how to set listeners for map tap and long press events, camera movement events, and other events such as **my-location** icon tap events. The Huawei map's movement functionality is implemented by simulating camera movements.

#### API Description

The following table describes APIs for map event listening, which are mainly provided by [MapEventManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager). You can obtain [MapEventManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager) using the [getEventManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section154601059144812) method. For more information about the APIs, please refer to [MapEventManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section824544714394)(type: 'mapClick', callback: Callback<[mapCommon.LatLng](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section20691173773810)\>): void

 | 

Sets a listener for map tap events.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section0257247133915)(type: 'mapLongClick', callback: Callback<[mapCommon.LatLng](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section20691173773810)\>): void

 | 

Sets a listener for map long-press events.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section6240147113918)(type: 'cameraMoveStart', callback: Callback<number>): void

 | 

Sets a listener for camera movement start events.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section142347477396)(type: 'cameraMove', callback: Callback<void>): void

 | 

Sets a listener for camera movement events.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section1963201310319)(type: 'cameraIdle', callback: Callback<void>): void

 | 

Sets a listener for camera movement end events.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section19286104716392)(type: 'markerClick' , callback: Callback<[Marker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-marker)\>): void

 | 

Sets a listener for Marker tap events.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section9264124723916)(type: 'myLocationButtonClick', callback: Callback<void>): void

 | 

Sets a listener for my-location icon tap events.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section636111479397)(type: 'pointAnnotationClick', callback: Callback<[PointAnnotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-pointannotation)\>): void

 | 

Sets a listener for PointAnnotation tap events.

 |

#### Development Procedure

## Initializing the Event Management API of the Map Component

this.mapEventManager = this.mapController.getEventManager();

## Listening for Map Tap Events

let callback = (position: mapCommon.LatLng) => {
  console.info("mapClick", \`on-mapClick position = ${position.longitude}\`);
};
this.mapEventManager.on("mapClick", callback);

## Listening for Map Long-Press Events

let callback = (position: mapCommon.LatLng) => {
  console.info("mapLongClick", \`on-mapLongClick position = ${position.longitude}\`);
};
this.mapEventManager.on("mapLongClick", callback);

## Listening for Camera Movement Events

After a listener is set for camera movement events, camera movement status can be listened. The Huawei map's movement functionality is implemented by simulating camera movements.

-   When the camera starts to move, **cameraMoveStart** is called back.

let callback = (reason: number) => {
  console.info("cameraMoveStart", \`on-cameraMoveStart reason = ${reason}\`);
};
this.mapEventManager.on("cameraMoveStart", callback);

-   When the camera moves or a user interacts with the map, **cameraMove** will be called for multiple times.

let callback = () => {
  console.info("cameraMove", \`on-cameraMove\`);
};
this.mapEventManager.on("cameraMove", callback);

-   When the camera stops to move, **cameraIdle** is called back.

let callback = () => {
  console.info("cameraIdle", \`on-cameraIdle\`);
};
this.mapEventManager.on("cameraIdle", callback);

## Listening for Marker Tap Events

A Marker can be added at a specified location on the map to identify a place, store, or building. For details, please refer to [Marker](../../drawing-on-a-map/marker/document.md).

let callback = (marker: map.Marker) => {
  console.info("markerClick", \`markerClick: ${marker.getId()}\`);
};
this.mapEventManager.on("markerClick", callback);

## Listening for My-Location Tap Events

For details, please refer to [Showing My Location](../../map-creation/showing-my-location/document.md).

let callback = () => {
  console.info("myLocationButtonClick", \`myLocationButtonClick\`);
};
this.mapEventManager.on("myLocationButtonClick", callback);

## Listening for PointAnnotation Tap Events

A PointAnnotation can be added at a specified location on a map to identify locations such as stores and buildings, and the location details can be displayed in an information window. For details, please refer to [PointAnnotation](../../drawing-on-a-map/pointannotation/document.md).

let callback = (pointAnnotation: map.PointAnnotation) => {
  console.info("pointAnnotationClick", \`pointAnnotationClick: ${pointAnnotation.getId()}\`);
};
this.mapEventManager.on("pointAnnotationClick", callback);
