# MapPolygon

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### MapPolygon

MapPolygon, which inherits from [BaseOverlay](../baseoverlay/document.md). A MapPolygon can be convex or concave. It can span the 180th meridian and have holes that are not filled in. An instance of the MapPolygon type will be returned when the [addPolygon](../mapcomponentcontroller/document.md#section1825517119280) method in the map.[MapComponentController](../mapcomponentcontroller/document.md) class is called.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Example**:

let polygonOptions: mapCommon.MapPolygonOptions = {
  points: \[
    { latitude: 31.9844102, longitude: 118.7662 },
    { latitude: 31.9844102, longitude: 123.7662 },
    { latitude: 36.9844102, longitude: 123.7662 },
    { latitude: 36.9844102, longitude: 118.7662 }
  \]
};
let mapPolygon = await this.mapController.addPolygon(polygonOptions);

#### \[h2\]getFillColor

getFillColor(): number

Obtains the fill color of a MapPolygon, which is in ARGB format.

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

Color in ARGB format.

 |

**Example**:

let fillColor: number = mapPolygon.getFillColor();

#### \[h2\]getHoles

getHoles(): Array<Array<mapCommon.LatLng>>

Obtains holes in a MapPolygon.

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

Array<Array<[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)\>>

 | 

Array of holes in a MapPolygon, which is a [LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810) array.

 |

**Example**:

let holes: Array<Array<mapCommon.LatLng>> = mapPolygon.getHoles();

#### \[h2\]getPoints

getPoints(): Array<mapCommon.LatLng>

Obtains vertex coordinates of a MapPolygon.

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

Array<[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

Vertex coordinates of a MapPolygon.

 |

**Example**:

let points: Array<mapCommon.LatLng> = mapPolygon.getPoints();

#### \[h2\]getStrokeColor

getStrokeColor(): number

Obtains the stroke color of a MapPolygon's outline.

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

let strokeColor: number = mapPolygon.getStrokeColor();

#### \[h2\]getJointType

getJointType(): mapCommon.JointType

Obtains the vertex style of a MapPolygon.

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

[mapCommon.JointType](../../mapcommon-map-attribute-model/document.md#section73559613164)

 | 

Vertex style of a MapPolygon.

 |

**Example**:

let jointType: mapCommon.JointType = mapPolygon.getJointType();

#### \[h2\]getPatterns

getPatterns(): Array<mapCommon.PatternItem>

Obtains the pattern of a MapPolygon's outline.

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

Pattern of a MapPolygon's outline.

 |

**Example**:

let patterns: Array<mapCommon.PatternItem> = mapPolygon.getPatterns();

#### \[h2\]getStrokeWidth

getStrokeWidth(): number

Obtains the stroke width of a MapPolygon's outline.

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

Stroke width of a MapPolygon's outline, in pixels.

 |

**Example**:

let strokeWidth: number = mapPolygon.getStrokeWidth();

#### \[h2\]isClickable

isClickable(): boolean

Checks whether a MapPolygon is tappable.

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

Indicates whether a MapPolygon is tappable.

-   **true**: yes
-   **false**: no

 |

**Example**:

let clickable: boolean = mapPolygon.isClickable();

#### \[h2\]isGeodesic

isGeodesic(): boolean

Checks whether each segment of a MapPolygon is geodesic.

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

Indicates whether each segment of a MapPolygon is geodesic.

-   **true**: yes
-   **false**: no

 |

**Example**:

let geodesic: boolean = mapPolygon.isGeodesic();

#### \[h2\]setClickable

setClickable(clickable: boolean): void

Sets whether a MapPolygon is tappable.

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

Indicates whether a MapPolygon is tappable. The default value is **false**.

-   **true**: yes
-   **false**: no

 |

**Example**:

mapPolygon.setClickable(true);

#### \[h2\]setFillColor

setFillColor(color: number): void

Sets the fill color of a MapPolygon.

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

Color in ARGB format. The default value is **0x00000000** (transparent).

 |

**Example**:

mapPolygon.setFillColor(0xff000FFF);

#### \[h2\]setGeodesic

setGeodesic(geodesic: boolean): void

Sets whether to draw each segment of a MapPolygon as a geodesic.

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

geodesic

 | 

boolean

 | 

Yes

 | 

Indicates whether to draw each segment of a MapPolygon as a geodesic. The default value is **false**.

-   **true**: yes
-   **false**: no

 |

**Example**:

mapPolygon.setGeodesic(true);

#### \[h2\]setHoles

setHoles(holes: Array<Array<mapCommon.LatLng>>): void

Sets holes in a MapPolygon.

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

holes

 | 

Array<Array<[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)\>>

 | 

Yes

 | 

Array of holes in a MapPolygon, which is a [LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810) array.

 |

**Example**:

let holes: Array<Array<mapCommon.LatLng>> = \[
  \[
    {
      latitude: 31.98,
      longitude: 115.76
    },
    {
      latitude: 31.98,
      longitude: 118.76
    },
    {
      latitude: 35.98,
      longitude: 118.76
    },
    {
      latitude: 35.98,
      longitude: 118.76
    }
  \]
\];
mapPolygon.setHoles(holes);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/ob5Q7fP6QKSMKF5PJKMM-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062511Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6AA33BF33C1B6F420F1D89A695DB3CB81F54A2E00B44B91D4173BDB098100811)

When coordinates of a hole coincide with the outline of the MapPolygon, it can lead to rendering anomalies, such as extra hollow regions being displayed.

#### \[h2\]setPoints

setPoints(points: Array<mapCommon.LatLng>): void

Sets the vertex coordinates of a MapPolygon.

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

points

 | 

Array<[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

Yes

 | 

Array of vertex coordinates of a MapPolygon.

 |

**Example**:

let points: Array<mapCommon.LatLng> = \[
  { 
    latitude: 31.98,
    longitude: 115.76
  },
  { 
    latitude: 31.98,
    longitude: 118.76
  },
  { 
    latitude: 35.98,
    longitude: 118.76
  },
  { 
    latitude: 35.98,
    longitude: 118.76
  }
\];
mapPolygon.setPoints(points);

#### \[h2\]setStrokeColor

setStrokeColor(color: number): void

Sets the stroke color of a MapPolygon's outline.

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

mapPolygon.setStrokeColor(0xff00DB93);

#### \[h2\]setJointType

setJointType(jointType: mapCommon.JointType): void

Sets the vertex style of a MapPolygon.

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

jointType

 | 

[mapCommon.JointType](../../mapcommon-map-attribute-model/document.md#section73559613164)

 | 

Yes

 | 

Vertex style. The default value is [JointType](../../mapcommon-map-attribute-model/document.md#section73559613164).DEFAULT.

 |

**Example**:

mapPolygon.setJointType(mapCommon.JointType.ROUND);

#### \[h2\]setPatterns

setPatterns(patterns: Array<mapCommon.PatternItem>): void

Sets the pattern of a MapPolygon's outline.

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

Array of [PatternItem](../../mapcommon-map-attribute-model/document.md#section917314511192) objects. The default outline pattern is solid.

 |

**Example**:

let linePatterns: Array<mapCommon.PatternItem> = \[
  { 
    type: mapCommon.PatternItemType.DASH,
    length: 100
  },
  { 
    type: mapCommon.PatternItemType.DOT,
    length: 100
  },
  { 
    type: mapCommon.PatternItemType.GAP,
    length: 100 
  }
\];
mapPolygon.setPatterns(linePatterns);

#### \[h2\]setStrokeWidth

setStrokeWidth(width: number): void

Sets the stroke width of a MapPolygon's outline.

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

Stroke width, in pixels. The default value is **10**. The value must be greater than or equal to 0. Invalid values are not processed.

 |

**Example**:

mapPolygon.setStrokeWidth(30);
