# BuildingOverlay

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### BuildingOverlay

BuildingOverlay. The BuildingOverlay effect is displayed only when the zoom level is high enough to show building details.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Example**:

let points: Array<mapCommon.LatLng> = \[
  {
    latitude: 31.984794,
    longitude: 118.765865
  },
  {
    latitude: 31.98468,
    longitude: 118.766076
  },
  {
    latitude: 31.98472,
    longitude: 118.766116
  },
  {
    latitude: 31.98463,
    longitude: 118.766292
  },
  {
    latitude: 31.984586,
    longitude: 118.766251
  },
  {
    latitude: 31.984536,
    longitude: 118.766344
  },
  {
    latitude: 31.984633,
    longitude: 118.766446
  },
  {
    latitude: 31.9848,
    longitude: 118.766285
  },
  {
    latitude: 31.984925,
    longitude: 118.766312
  },
  {
    latitude: 31.985282,
    longitude: 118.766661
  },
  {
    latitude: 31.985438,
    longitude: 118.766419
  },
  {
    latitude: 31.985801,
    longitude: 118.766755
  },
  {
    latitude: 31.985856,
    longitude: 118.766504
  },
  {
    latitude: 31.985785,
    longitude: 118.766434
  },
  {
    latitude: 31.985821,
    longitude: 118.766278
  },
  {
    latitude: 31.985897,
    longitude: 118.766311
  },
  {
    latitude: 31.985944,
    longitude: 118.766095
  },
  {
    latitude: 31.985909,
    longitude: 118.766069
  },
  {
    latitude: 31.985794,
    longitude: 118.765989
  },
  {
    latitude: 31.9857,
    longitude: 118.766029
  },
  {
    latitude: 31.985658,
    longitude: 118.766164
  },
  {
    latitude: 31.985647,
    longitude: 118.766271
  },
  {
    latitude: 31.985574,
    longitude: 118.766297
  },
  {
    latitude: 31.985458,
    longitude: 118.766285
  },
  {
    latitude: 31.985271,
    longitude: 118.766002
  },
  {
    latitude: 31.985219,
    longitude: 118.766002
  },
  {
    latitude: 31.985135,
    longitude: 118.766029
  },
  {
    latitude: 31.985093,
    longitude: 118.766083
  },
  {
    latitude: 31.985019,
    longitude: 118.766109
  },
  {
    latitude: 31.984978,
    longitude: 118.766083
  },
  {
    latitude: 31.984794,
    longitude: 118.765865
  }
\];
points.reverse();
// BuildingOverlay parameters.
let buildingOverlayOptions: mapCommon.BuildingOverlayParams =
  {
    // Range of the BuildingOverlay (the points are drawn clockwise).
    points: points,
    // Height of the BuildingOverlay.
    totalHeight: 51,
    // Height of the selected floor in the BuildingOverlay.
    floorBottomHeight: 33,
    // Color of the BuildingOverlay's rooftop.
    topFaceColor: 0xffa4b8f7,
    // Color of the BuildingOverlay's lateral surface.
    sideFaceColor: 0x44a4b8f7,
    // Color of the selected floor in the BuildingOverlay.
    floorColor: 0xff000000,
    // Floor from which the BuildingOverlay starts to be displayed.
    showLevel: 14,
    // Animation duration for the selected floor in the BuildingOverlay rising from the bottom.
    animationDuration: 5000,
    // Texture of the BuildingOverlay's lateral surface.
    sideTexture: { image: $r("app.media.side\_tex"), height: 3, width: 3 },
    // Texture of the selected floor in the BuildingOverlay.
    floorTexture: { image: $r("app.media.floor\_tex"), height: 3, width: 3 }
  }
let buildingOverlay: map.BuildingOverlay= await this.mapController?.addBuildingOverlay(buildingOverlayOptions);

#### \[h2\]getId

getId(): string

Obtains the ID of a BuildingOverlay.

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

string

 | 

Obtains the ID of a BuildingOverlay.

 |

**Example**:

let id: String = buildingOverlay.getId();

#### \[h2\]remove

remove(): void

Removes a BuildingOverlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Example**:

buildingOverlay.remove();

#### \[h2\]setSideVisible

setSideVisible(visible: boolean): void

Sets whether to display the lateral surface and rooftop of a BuildingOverlay. If you do not want to display a BuildingOverlay, call both [setSideVisible](#section162717125719) and [setFloorVisible](#section164221712205712) and pass **false**.

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

visible

 | 

boolean

 | 

Yes

 | 

Indicates whether to display the lateral surface and rooftop of a BuildingOverlay.

-   **true**: yes
-   **false**: no

 |

**Example**:

buildingOverlay.setSideVisible(true);

#### \[h2\]setFloorVisible

setFloorVisible(visible: boolean): void

Sets whether to display a selected floor of a BuildingOverlay.

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

visible

 | 

boolean

 | 

Yes

 | 

Indicates whether to display a selected floor of a BuildingOverlay.

-   **true**: yes
-   **false**: no

 |

**Example**:

buildingOverlay.setFloorVisible(true);

#### \[h2\]setFloorBottomHeight

setFloorBottomHeight(height: number): void

Sets the height from the ground to the bottom of a selected floor.

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

height

 | 

number

 | 

Yes

 | 

Height from the ground to the bottom of a selected floor, in meters. The value must be greater than or equal to 0.

 |

**Example**:

buildingOverlay.setFloorBottomHeight(80);
