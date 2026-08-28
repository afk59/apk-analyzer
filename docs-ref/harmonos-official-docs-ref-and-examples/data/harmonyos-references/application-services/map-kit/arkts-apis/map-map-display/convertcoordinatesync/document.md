# convertCoordinateSync

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### convertCoordinateSync

convertCoordinateSync(fromType: mapCommon.CoordinateType, toType: mapCommon.CoordinateType, location: mapCommon.LatLng): mapCommon.LatLng

Converts coordinates. Currently, this API supports only conversion from WGS84 coordinates to GCJ02 coordinates.

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

fromType

 | 

[mapCommon.CoordinateType](../../mapcommon-map-attribute-model/document.md#section78948324526)

 | 

Yes

 | 

Original coordinate type. Currently, only WGS84 is supported.

 |
| 

toType

 | 

[mapCommon.CoordinateType](../../mapcommon-map-attribute-model/document.md#section78948324526)

 | 

Yes

 | 

Target coordinate type. Currently, only GCJ02 is supported.

 |
| 

location

 | 

[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

Yes

 | 

Coordinates to be converted.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

Longitude-latitude object.

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

let wgs84Position: mapCommon.LatLng = {
  latitude: 30,
  longitude: 118
};
// Convert the longitude-latitude coordinates.
let gcj02Position: mapCommon.LatLng =
  map.convertCoordinateSync(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02, wgs84Position);
