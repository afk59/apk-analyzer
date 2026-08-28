# MapCircle

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### MapCircle

Updates and queries MapCircles. This API inherits from [BaseOverlay](../baseoverlay/document.md). An instance of the MapCircle type will be returned when the [addCircle](../mapcomponentcontroller/document.md#section8212148102813) method in the map.[MapComponentController](../mapcomponentcontroller/document.md) class is called.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Example**:

let mapCircleOptions: mapCommon.MapCircleOptions = {
	center: {
	  latitude: 39.9,
	  longitude: 116.4
	},
	radius: 5000,
	fillColor: 0XFF00FFFF,
	strokeColor: 0xFFFF0000,
	strokeWidth: 10,
	zIndex: 15
};
let mapCircle = await this.mapController.addCircle(mapCircleOptions);

#### \[h2\]getCenter

getCenter(): mapCommon.LatLng

Obtains the longitude and latitude of the center of a MapCircle.

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

mapCommon.[LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

Longitude and latitude of the center of a MapCircle.

 |

**Example**:

let center: mapCommon.LatLng = mapCircle.getCenter();

#### \[h2\]getFillColor

getFillColor(): number

Obtains the fill color of a MapCircle.

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

Fill color of a MapCircle.

 |

**Example**:

let fillColor: number = mapCircle.getFillColor();

#### \[h2\]getRadius

getRadius(): number

Obtains the radius of a MapCircle.

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

Radius of a MapCircle, in meters.

 |

**Example**:

let radius: number = mapCircle.getRadius();

#### \[h2\]getStrokeColor

getStrokeColor(): number

Obtains the stroke color of a MapCircle's outline.

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

Color in ARGB format. The default value is **0xff000000** (black).

 |

**Example**:

let strokeColor: number = mapCircle.getStrokeColor();

#### \[h2\]getPatterns

getPatterns(): Array<mapCommon.PatternItem>

Obtains the pattern of a MapCircle's outline.

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

Array<[mapCommon.PatternItem](../../mapcommon-map-attribute-model/document.md#section917314511192)\>

 | 

Pattern of a MapCircle's outline.

 |

**Example**:

let patterns: Array<mapCommon.PatternItem> = mapCircle.getPatterns();

#### \[h2\]getStrokeWidth

getStrokeWidth(): number

Obtains the stroke width of a MapCircle's outline.

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

Stroke width of a MapCircle's outline.

 |

**Example**:

let strokeWidth: number = mapCircle.getStrokeWidth();

#### \[h2\]isClickable

isClickable(): boolean

Checks whether a MapCircle is tappable.

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

Indicates whether a MapCircle is tappable.

-   **true**: yes
-   **false**: no

 |

**Example**:

let clickable: boolean = mapCircle.isClickable();

#### \[h2\]setCenter

setCenter(center: mapCommon.LatLng): void

Sets the longitude and latitude of the center of a MapCircle.

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

center

 | 

[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

Yes

 | 

Longitude-latitude coordinates of the center of a MapCircle.

A MapCircle can be drawn only when the latitude of its center is within the range from -85.051119 to 85.051119. If the latitude of the MapCircle center is -85.051119 or 85.051119, a MapCircle with a radius of 1 meter can be drawn exactly.

 |

**Example**:

let center: mapCommon.LatLng = {latitude: 31.98, longitude: 116.4};
mapCircle.setCenter(center);

#### \[h2\]setClickable

setClickable(clickable: boolean): void

Sets whether a MapCircle is tappable.

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

clickable

 | 

boolean

 | 

Yes

 | 

Indicates whether a MapCircle is tappable. The default value is **false**.

-   **true**: yes
-   **false**: no

 |

**Example**:

let clickable = true;
mapCircle.setClickable(clickable);

#### \[h2\]setFillColor

setFillColor(color: number): void

Sets the fill color of a MapCircle.

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

color

 | 

number

 | 

Yes

 | 

Fill color of a MapCircle, in ARGB format. The default value is **0x00000000** (transparent).

 |

**Example**:

let fillColor = 0xFF00FFFF;
mapCircle.setFillColor(fillColor);

#### \[h2\]setRadius

setRadius(radius: number): void

Sets the radius of a MapCircle.

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

radius

 | 

number

 | 

Yes

 | 

Radius, in meters. The value must be greater than or equal to 0.

The default value is **5000**. If an invalid value is passed, the default value will be used.

 |

**Example**:

let radius = 300;
mapCircle.setRadius(radius);

#### \[h2\]setStrokeColor

setStrokeColor(color: number): void

Sets the stroke color of a MapCircle's outline.

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

color

 | 

number

 | 

Yes

 | 

Color in ARGB format. The default value is **0xff000000** (black).

 |

**Example**:

let strokeColor = 0xFFFF0000;
mapCircle.setStrokeColor(strokeColor);

#### \[h2\]setPatterns

setPatterns(patterns: Array<mapCommon.PatternItem>): void

Sets the pattern of a MapCircle's outline.

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

patterns

 | 

Array<[mapCommon.PatternItem](../../mapcommon-map-attribute-model/document.md#section917314511192)\>

 | 

Yes

 | 

Pattern of a MapCircle's outline.

 |

**Example**:

let patterns: Array<mapCommon.PatternItem> = \[
  { type: 0, length: 100 },
  { type: 1, length: 100 }, 
  { type: 2, length: 100 }\];
mapCircle.setPatterns(patterns);

#### \[h2\]setStrokeWidth

setStrokeWidth(width: number): void

Sets the stroke width of a MapCircle's outline.

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

width

 | 

number

 | 

Yes

 | 

Stroke width of a MapCircle's outline, in pixels. The value must be greater than or equal to 0.

 |

**Example**:

let width = 10;
mapCircle.setStrokeWidth(width);
