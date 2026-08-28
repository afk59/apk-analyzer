# Heatmap

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### Heatmap

Heatmap object. An instance of the Heatmap type will be returned when the [addHeatmap](../mapcomponentcontroller/document.md#section849314585910) method in the map.[MapComponentController](../mapcomponentcontroller/document.md) class is called.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

**Example**:

let data: mapCommon.WeightedLatLng\[\] = \[\];
for (let i = 0; i < 500; i++) {
  data.push({
    point: {
      longitude: 118.000000 + Math.random() \* 1 - 0.25,
      latitude: 31.000000 + Math.random() \* 1 - 0.25,
    },
    intensity: 1
  });
}
let heatMapOptions: mapCommon.HeatmapParams = {
  id: 'heatmap0001',
  data: data,
  radius: 20,
  intensity: {
    2: 1,
    5: 5,
    8: 10
  },
}
let heatMap = await this.mapController.addHeatmap(heatMapOptions)

#### \[h2\]setData

setData(data: mapCommon.WeightedLatLng\[\]): void

Sets the heatmap data.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

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

data

 | 

[mapCommon.WeightedLatLng](../../mapcommon-map-attribute-model/document.md#section14151459134817)\[\]

 | 

Yes

 | 

Heatmap data (it is recommended that the number of heatmap data records be less than 10,000).

 |

**Example**:

let data: mapCommon.WeightedLatLng\[\] = \[
  {
    point: {
      longitude: -151.5129,
      latitude: 63.1016
    },
    intensity: 2.3
  }
\];
heatMap.setData(data);

#### \[h2\]getData

getData(): mapCommon.WeightedLatLng\[\]

Obtains the heatmap data.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[mapCommon.WeightedLatLng](../../mapcommon-map-attribute-model/document.md#section14151459134817)\[\]

 | 

Heatmap data.

 |

**Example**:

let data: mapCommon.WeightedLatLng\[\] = heatMap.getData();

#### \[h2\]setColor

setColor(color: Record<number, number>): void

Sets the heatmap color.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

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

Record<number, number>

 | 

Yes

 | 

Heatmap color.

-   key: data density. The value range is \[0, 1\].
-   value: gradient color, in ARGB format.

If the input parameter value is invalid, no processing will be performed.

 |

**Example**:

let record: Record<number, number> = {
  0: 0x26C3999,    // Dark blue.
  0.15: 0xFF4D4DFF, // Blue-violet.
  0.3: 0xFF9999FF,  // Light blue-violet.
  0.45: 0xFFE6E6FF, // Pale blue-violet.
  0.6: 0xFFFFCCFF, // Light purple.
  0.75: 0xFFFF99FF, // Purple.
  0.9: 0xFFFF66FF, // Dark purple.
  1: 0xFFFF00FF    // Deep dark purple.
};
heatMap.setColor(record);

#### \[h2\]getColor

getColor(): Record<number, number>

Obtains the heatmap color.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Record<number, number>

 | 

Heatmap color.

-   key: data density. The value range is \[0, 1\].
-   value: gradient color, in ARGB format.

If the heatmap color is not set, the default value is returned.

 |

**Example**:

let record: Record<number, number> = heatMap.getColor();

#### \[h2\]setIntensity

setIntensity(intensity: number | Record<number, number>): void

Sets the heatmap intensity.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

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

intensity

 | 

number | Record<number, number>

 | 

Yes

 | 

Heatmap intensity. If the intensity is a number, the same intensity is used for all levels.

-   key: level. The value range is \[2, 20\].
-   value: heatmap intensity. The value range is (0, +∞).

If the input parameter value is invalid, no processing will be performed.

 |

**Example**:

let intensity: Record<number, number> | number = {
  2:0.1,
  3:0.1,
  4:0.1
};
heatMap.setIntensity(intensity);

#### \[h2\]getIntensity

getIntensity(): number | Record<number, number>

Obtains the heatmap intensity.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number | Record<number, number>

 | 

Heatmap intensity. If the intensity is a number, the same intensity is used for all levels.

-   key: level. The value range is \[2, 20\].
-   value: heatmap intensity. The value range is (0, +∞).

If the heatmap intensity is not set, the default value is returned.

 |

**Example**:

let intensity: Record<number, number> | number = heatMap.getIntensity();

#### \[h2\]setOpacity

setOpacity(opacity: number | Record<number, number>): void

Sets the heatmap opacity.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

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

opacity

 | 

number | Record<number, number>

 | 

Yes

 | 

Heatmap opacity. If the opacity is a number, the same opacity is used for all levels.

-   key: level. The value range is \[2, 20\].
-   value: heatmap opacity. The value range is \[0, 1\]. The value **0** indicates completely opaque, and the value **1** indicates completely transparent.

If the input parameter value is invalid, no processing will be performed.

 |

**Example**:

let opacity: Record<number, number> | number = {
  2:0.1,
  3:0.1,
  4:0.1
}
heatMap.setOpacity(opacity);

#### \[h2\]getOpacity

getOpacity(): number | Record<number, number>

Obtains the heatmap opacity.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number | Record<number, number>

 | 

Heatmap opacity. If the opacity is a number, the same opacity is used for all levels.

-   key: heatmap color gradient level. The value range is \[2, 20\].
-   value: heatmap opacity. The value range is \[0, 1\]. The value **0** indicates completely opaque, and the value **1** indicates completely transparent.

If the heatmap opacity is not set, the default value is returned.

 |

**Example**:

let opacity: Record<number, number> | number = heatMap.getOpacity();

#### \[h2\]setRadius

setRadius(radius: number | Record<number, number>): void

Sets the heatmap radius.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

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

number | Record<number, number>

 | 

Yes

 | 

Heatmap radius. If the radius is a number, the same radius is used for all levels.

-   key: level. The value range is \[2, 20\].
-   value: heatmap radius. The value range is \[1, +∞).

If the input parameter value is invalid, no processing will be performed.

 |

**Example**:

heatMap.setRadius(3000);

#### \[h2\]getRadius

getRadius(): number | Record<number, number>

Obtains the heatmap radius.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number | Record<number, number>

 | 

Heatmap radius. If the radius is a number, the same radius is used for all levels.

-   key: level. The value range is \[2, 20\].
-   value: heatmap radius. The value range is \[1, +∞).

If the heatmap radius is not set, the default value is returned.

 |

**Example**:

let radius: number | Record<number, number> = heatMap.getRadius();

#### \[h2\]setRadiusUnit

setRadiusUnit(radiusUnit: mapCommon.RadiusUnit): void

Sets the heatmap radius unit.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

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

radiusUnit

 | 

[mapCommon.RadiusUnit](../../mapcommon-map-attribute-model/document.md#section117031317134216)

 | 

Yes

 | 

Heatmap radius unit. If the input parameter value is invalid, no processing will be performed.

 |

**Example**:

heatMap.setRadiusUnit(mapCommon.RadiusUnit.PIXEL\_UNIT);

#### \[h2\]getRadiusUnit

getRadiusUnit(): mapCommon.RadiusUnit

Obtains the heatmap radius unit.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[mapCommon.RadiusUnit](../../mapcommon-map-attribute-model/document.md#section117031317134216)

 | 

Heatmap radius unit. If the heatmap radius unit is not set, the default value is returned.

 |

**Example**:

let radiusUnit: mapCommon.RadiusUnit = heatMap.getRadiusUnit();

#### \[h2\]setVisible

setVisible(visible: boolean): void

Sets the visibility of the heatmap.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

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

visible

 | 

boolean

 | 

Yes

 | 

Indicates whether the heatmap is visible.

-   **true**: yes
-   **false**: no

If the input parameter value is invalid, no processing will be performed.

 |

**Example**:

heatMap.setVisible(false);

#### \[h2\]isVisible

isVisible(): boolean

Checks whether the heatmap is visible.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

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

Indicates whether the heatmap is visible.

-   **true**: yes
-   **false**: no

If the heatmap visibility is not set, the default value is returned.

 |

**Example**:

let isVisible: boolean = heatMap.isVisible();

#### \[h2\]remove

remove(): void

Deletes a heatmap.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

**Example**:

heatMap.remove();
