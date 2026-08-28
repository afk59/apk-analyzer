# MapArc

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### MapArc

MapArc. This API inherits from [BaseOverlay](../baseoverlay/document.md). An instance of the MapArc type will be returned when the [addArc](../mapcomponentcontroller/document.md#section123390488448) method in the map.[MapComponentController](../mapcomponentcontroller/document.md) class is called.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Example**:

// Set MapArc parameters.
let mapArcParams: mapCommon.MapArcParams = {
  // Coordinates of the MapArc start point.
  startPoint: {
    latitude: 39.913138,
    longitude: 116.415112
  },
  // Coordinates of the MapArc end point.
  endPoint: {
    latitude: 28.239473,
    longitude: 112.954094
  },
  // Coordinates of the MapArc center point.
  centerPoint: {
    latitude: 33.86970399048567,
    longitude: 112.08633528544145
  },
  width: 10,
  color: 0xffff0000,
  visible: true,
  zIndex: 100
};
// Add a MapArc.
let mapArc: map.MapArc = this.mapController.addArc(mapArcParams);

#### \[h2\]getColor

getColor(): number

Obtains the color of a MapArc.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

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

let color: number = mapArc.getColor();

#### \[h2\]getWidth

getWidth(): number

Obtains the width of a MapArc.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

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

Width of a MapArc. The unit is px.

 |

**Example**:

let width: number = mapArc.getWidth();

#### \[h2\]setColor

setColor(color: number): void

Sets the color of a MapArc.

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

color

 | 

number

 | 

Yes

 | 

Color in ARGB format. The default value is **0xff000000** (black).

 |

**Example**:

mapArc.setColor(0xffff00ff);

#### \[h2\]setWidth

setWidth(width: number): void

Sets the width of a MapArc.

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

width

 | 

number

 | 

Yes

 | 

Width of a MapArc, in pixels. The value must be greater than or equal to 0.

 |

**Example**:

mapArc.setWidth(20);
