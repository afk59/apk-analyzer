# newLatLng

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### newLatLng

newLatLng(latLng: mapCommon.LatLng, zoom?: number): CameraUpdate

Sets the map center and zoom level.

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

latLng

 | 

[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

Yes

 | 

Longitude and latitude.

 |
| 

zoom

 | 

number

 | 

No

 | 

Zoom level. The value ranges from 2 to 20. If a value is out of this range, the nearest boundary value is used.

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

let latLng: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4
};
let cameraUpdate: map.CameraUpdate = map.newLatLng(latLng);
