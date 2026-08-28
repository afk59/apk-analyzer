# calculateDistance

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### calculateDistance

calculateDistance(from: mapCommon.LatLng, to: mapCommon.LatLng): number

Calculates the distance between coordinate points.

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

from

 | 

[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

Yes

 | 

Coordinates of the start point.

 |
| 

to

 | 

[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

Yes

 | 

Coordinates of the end point.

 |

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

Distance between the specified two coordinate points, in meters.

If the input parameters are undefined or null, **0** is returned.

 |

**Example**:

let fromLatLng: mapCommon.LatLng = {
  latitude: 38,
  longitude: 118
};
let toLatLng: mapCommon.LatLng = {
  latitude: 39,
  longitude: 119
};

let distance = map.calculateDistance(fromLatLng, toLatLng);
