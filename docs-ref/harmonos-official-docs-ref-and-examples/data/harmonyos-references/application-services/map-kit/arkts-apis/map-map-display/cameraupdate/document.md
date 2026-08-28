# CameraUpdate

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### CameraUpdate

Defines camera movement parameters. For details about how to create a **CameraUpdate** object, please refer to [newCameraPosition](../newcameraposition/document.md).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

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
