# SpatialRelationUtil

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### SpatialRelationUtil

Utility class for calculating point-surface relationships.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

#### \[h2\]isPointContainedInPolygon

static isPointContainedInPolygon(points: Array<mapCommon.LatLng>, point: mapCommon.LatLng): boolean

Checks whether a point is within a polygon.

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

points

 | 

Array<[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

Yes

 | 

Coordinates of a polygon.

 |
| 

point

 | 

[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

Yes

 | 

Coordinates of the point to be checked.

 |

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

Indicates whether a point is within a polygon.

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

401

 | 

Invalid input parameter.

 |

**Example**:

let points: Array<mapCommon.LatLng> = \[
  { latitude: 31.693478, longitude: 118.434595 },
  { latitude: 31.693478, longitude: 118.534595 },
  { latitude: 32.993478, longitude: 118.734595 },
  { latitude: 32.993478, longitude: 118.934595 }
\];
let point: mapCommon.LatLng = { latitude: 31.984, longitude: 118.766 };
let result: boolean = map.SpatialRelationUtil.isPointContainedInPolygon(points, point);
