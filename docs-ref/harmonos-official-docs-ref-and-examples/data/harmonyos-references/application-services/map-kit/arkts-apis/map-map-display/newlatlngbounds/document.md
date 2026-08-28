# newLatLngBounds

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### newLatLngBounds

newLatLngBounds(bounds: mapCommon.LatLngBounds, padding?: number): CameraUpdate

Sets the map's longitude and latitude extent as well as the padding between the map region and map edges.

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

bounds

 | 

[mapCommon.LatLngBounds](../../mapcommon-map-attribute-model/document.md#section96341159111320)

 | 

Yes

 | 

Longitude and latitude extent for displaying the map.

 |
| 

padding

 | 

number

 | 

No

 | 

Padding between the map region and map edges, in pixels. The default value is **0**.

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

let bounds: mapCommon.LatLngBounds = {
  northeast: {
    latitude: 33,
    longitude: 118
  },
  southwest: {
    latitude: 32,
    longitude: 119
  }
};
let cameraUpdate: map.CameraUpdate = map.newLatLngBounds(bounds, 5);

#### newLatLngBounds

newLatLngBounds(bounds: mapCommon.LatLngBounds, width: number, height: number, padding: number): CameraUpdate

Sets the map's longitude and latitude extent, the height and width of the latitude-longitude bounding box, and the padding between the map region and map edges.

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

bounds

 | 

[mapCommon.LatLngBounds](../../mapcommon-map-attribute-model/document.md#section96341159111320)

 | 

Yes

 | 

Longitude and latitude extent for displaying the map.

 |
| 

width

 | 

number

 | 

Yes

 | 

Screen width of the latitude-longitude bounding box, in pixels. The value must be greater than or equal to 0.

 |
| 

height

 | 

number

 | 

Yes

 | 

Screen height of the latitude-longitude bounding box, in pixels. The value must be greater than or equal to 0.

 |
| 

padding

 | 

number

 | 

Yes

 | 

Padding between the map region and map edges, in pixels. The default value is **0**.

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

let bounds: mapCommon.LatLngBounds = {
  northeast: {
    latitude: 31,
    longitude: 118
  },
  southwest: {
    latitude: 30.5,
    longitude: 123
  }
};
// Set the map's longitude and latitude extent. Set both the width and height of the latitude-longitude bounding box to 1000 pixels, and set the padding between the map region and edges to 100 pixels.
let cameraUpdate: map.CameraUpdate = map.newLatLngBounds(bounds, 1000, 1000, 100);

#### newLatLngBounds

newLatLngBounds(bounds: mapCommon.LatLngBounds, padding: mapCommon.Padding): CameraUpdate

Sets the map's longitude and latitude extent as well as the padding between the map region and the four map edges.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.1(13).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.1(13)

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

bounds

 | 

[mapCommon.LatLngBounds](../../mapcommon-map-attribute-model/document.md#section96341159111320)

 | 

Yes

 | 

Longitude and latitude extent for displaying the map.

 |
| 

padding

 | 

[mapCommon.Padding](../../mapcommon-map-attribute-model/document.md#section144591344648)

 | 

Yes

 | 

Padding between the map region and map edges, in pixels. The default value is **0**.

NOTE:

-   The height of the map component, after subtracting the top and bottom padding values, must be at least 100 px.
-   The width of the map component, after subtracting the left and right padding values, must be at least 100 px.

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

let bounds: mapCommon.LatLngBounds = {
  northeast: {
    latitude: 31,
    longitude: 118
  },
  southwest: {
    latitude: 30.5,
    longitude: 123
  }
};
// Initialization parameters. The left padding is 0 px and the bottom padding is 50 px.
let padding: mapCommon.Padding = {
  left: 0,
  bottom: 50
};
let cameraUpdate: map.CameraUpdate = map.newLatLngBounds(bounds, padding);
