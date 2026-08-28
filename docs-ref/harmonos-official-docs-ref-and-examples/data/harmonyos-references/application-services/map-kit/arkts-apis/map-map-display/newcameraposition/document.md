# newCameraPosition

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### newCameraPosition

newCameraPosition(cameraPosition: mapCommon.CameraPosition): CameraUpdate

Creates a **CameraUpdate** object to update the camera position.

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

cameraPosition

 | 

[mapCommon.CameraPosition](../../mapcommon-map-attribute-model/document.md#section105031244194712)

 | 

Yes

 | 

New map camera position.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[CameraUpdate](../cameraupdate/document.md)

 | 

Description of changes to the camera position.

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
let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
