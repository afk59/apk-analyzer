# Projection

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### Projection

Converts between screen coordinates and longitude-latitude coordinates. An instance of this type will be returned when the [getProjection](../mapcomponentcontroller/document.md#section8132133414720) method in the map.[MapComponentController](../mapcomponentcontroller/document.md) class is called.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Example**:

let projection: map.Projection = this.mapController?.getProjection();

#### \[h2\]fromScreenLocation

fromScreenLocation(point: mapCommon.MapPoint): mapCommon.LatLng

Converts screen coordinates to longitude-latitude coordinates. A location on the screen is specified in screen pixels (instead of display pixels) relative to the top left corner of the map (instead of the top left corner of the screen).

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

Coordinate point on the screen, in pixels.

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

Longitude-latitude coordinates.

 |

**Example**:

let point: mapCommon.MapPoint = {
  positionX: 10,
  positionY: 10
};
let latLng: mapCommon.LatLng = projection.fromScreenLocation(point);

#### \[h2\]toScreenLocation

toScreenLocation(position: mapCommon.LatLng): mapCommon.MapPoint

Converts longitude-latitude coordinates to screen coordinates. A location on the screen is specified in screen pixels (instead of display pixels) relative to the top left corner of the map (instead of the top left corner of the screen).

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

position

 | 

[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

Yes

 | 

Longitude-latitude coordinates.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[mapCommon.MapPoint](../../mapcommon-map-attribute-model/document.md#section123881566186)

 | 

Coordinate point on the screen, in pixels.

 |

**Example**:

let position: mapCommon.MapPoint = projection.toScreenLocation({ latitude: 31.984, longitude: 118.766 });

#### \[h2\]getVisibleRegion

getVisibleRegion(): mapCommon.VisibleRegion

Obtains the coordinates of the visible region.

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

[mapCommon.VisibleRegion](../../mapcommon-map-attribute-model/document.md#section88850322916)

 | 

Visible region.

 |

**Example**:

let visibleRegion: mapCommon.VisibleRegion = projection.getVisibleRegion();

#### \[h2\]getMapBounds

getMapBounds(center: mapCommon.LatLng, zoom: number): mapCommon.LatLngBounds

Obtains the target region corresponding to the map control based on the center point and the zoom level of the map.

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

center

 | 

[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

Yes

 | 

Longitude-latitude coordinates of the center point.

 |
| 

zoom

 | 

number

 | 

Yes

 | 

Zoom level. The value ranges from 2 to 20. If the passed value is greater than the maximum zoom level, the maximum zoom level is used. If the passed value is less than the minimum zoom level, the minimum zoom level is used.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[mapCommon.LatLngBounds](../../mapcommon-map-attribute-model/document.md#section96341159111320)

 | 

Target region.

 |

**Example**:

let position: mapCommon.LatLng = {
  latitude: 31.98, longitude: 118.766
};
let result: mapCommon.LatLngBounds = projection.getMapBounds(position, 10);
