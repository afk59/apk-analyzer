# MapPolyline

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### MapPolyline

MapPolyline, which inherits from [BaseOverlay](../baseoverlay/document.md). An instance of the MapPolyline type will be returned when the [addPolyline](../mapcomponentcontroller/document.md#section6818109112812) method in the map.[MapComponentController](../mapcomponentcontroller/document.md) class is called.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Example**:

import { image } from '@kit.ImageKit';

// Store images in an array.
let customTextures: Array<ResourceStr | image.PixelMap> = new Array();
// The icons are stored in the **resources/rawfile** directory.
customTextures.push('icon/img.png');
customTextures.push('icon/img\_1.png');
let cusIndexNumber: Array<number> = new Array();
// The length of the **cusIndexNumber** array must be the same as the number of MapPolyline points. The array element content corresponds to the subscripts of **customTextures**. Images are stored from the second element in the array.
cusIndexNumber.push(0, 0, 1);
let polylineOption: mapCommon.MapPolylineOptions = {
  points: \[
    { latitude: 31.68, longitude: 118.166 },
    { latitude: 31.48, longitude: 118.366 },
    { latitude: 31.28, longitude: 118.766 }
  \],
  customTextures: customTextures,
  customTextureIndexes: cusIndexNumber
};
let mapPolyline = await this.mapController.addPolyline(polylineOption);

#### \[h2\]getColor

getColor(): number

Obtains the color of a MapPolyline.

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

let color: number = mapPolyline.getColor();

#### \[h2\]getColors

getColors(): Array<number>

Obtains colors of a MapPolyline's segments.

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

Array<number>

 | 

Array of colors of a MapPolyline's segments.

 |

**Example**:

let colors: Array<number> = mapPolyline.getColors();

#### \[h2\]getEndCap

getEndCap(): mapCommon.CapStyle

Obtains the end vertex style of a MapPolyline.

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

[mapCommon.CapStyle](../../mapcommon-map-attribute-model/document.md#section173028494409)

 | 

End vertex style of a MapPolyline.

 |

**Example**:

let endCap: mapCommon.CapStyle = mapPolyline.getEndCap();

#### \[h2\]getJointType

getJointType(): mapCommon.JointType

Obtains the joint type of all vertices of a MapPolyline, except the start and end vertices.

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

Joint type of all vertices of a MapPolyline, except the start and end vertices.

 |

**Example**:

let jointType: mapCommon.JointType = mapPolyline.getJointType();

#### \[h2\]getPatterns

getPatterns(): Array<mapCommon.PatternItem>

Obtains the pattern of a MapPolyline.

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

Pattern of a MapPolyline.

 |

**Example**:

let patterns: Array<mapCommon.PatternItem> = mapPolyline.getPatterns();

#### \[h2\]getPoints

getPoints(): Array<mapCommon.LatLng>

Obtains the vertex coordinates of a MapPolyline.

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

Vertex coordinates of a MapPolyline.

 |

**Example**:

let points: Array<mapCommon.LatLng> = mapPolyline.getPoints();

#### \[h2\]getStartCap

getStartCap(): mapCommon.CapStyle

Obtains the start vertex style of a MapPolyline.

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

[mapCommon.CapStyle](../../mapcommon-map-attribute-model/document.md#section173028494409)

 | 

Start vertex style of a MapPolyline.

 |

**Example**:

let startCap: mapCommon.CapStyle = mapPolyline.getStartCap();

#### \[h2\]getWidth

getWidth(): number

Obtains the width of a MapPolyline.

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

Width of a MapPolyline, in pixels.

 |

**Example**:

let width: number = mapPolyline.getWidth();

#### \[h2\]isClickable

isClickable(): boolean

Checks whether a MapPolyline is tappable.

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

Indicates whether a MapPolyline is tappable.

-   **true**: yes
-   **false**: no

 |

**Example**:

let isClickable: boolean = mapPolyline.isClickable();

#### \[h2\]isGeodesic

isGeodesic(): boolean

Checks whether a MapPolyline is geodesic.

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

Indicates whether a MapPolyline is geodesic.

-   **true**: yes
-   **false**: no

 |

**Example**:

let isGeodesic: boolean = mapPolyline.isGeodesic();

#### \[h2\]isGradient

isGradient(): boolean

Checks whether a MapPolyline is gradient.

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

Indicates whether a MapPolyline is gradient.

-   **true**: yes
-   **false**: no

 |

**Example**:

let isGradient: boolean = mapPolyline.isGradient();

#### \[h2\]setClickable

setClickable(clickable: boolean): void

Sets whether a MapPolyline is tappable.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

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

Indicates whether a MapPolyline is tappable. The default value is **false**.

-   **true**: yes
-   **false**: no

 |

**Example**:

mapPolyline.setClickable(true);

#### \[h2\]setColor

setColor(color: number): void

Sets the color of a MapPolyline.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

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

mapPolyline.setColor(0xff000000);

#### \[h2\]setColors

setColors(colors: Array<number>): void

Sets colors for segments of a MapPolyline.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

colors

 | 

Array<number>

 | 

Yes

 | 

Array of colors of a MapPolyline's segments, in ARGB format.

 |

**Example**:

mapPolyline.setColors(\[0xffffff00, 0xff000000\]);

#### \[h2\]setEndCap

setEndCap(endCap: mapCommon.CapStyle): void

Sets the end vertex style of a MapPolyline.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

endCap

 | 

[mapCommon.CapStyle](../../mapcommon-map-attribute-model/document.md#section173028494409)

 | 

Yes

 | 

End vertex style of a MapPolyline.

 |

**Example**:

mapPolyline.setEndCap(mapCommon.CapStyle.BUTT);

#### \[h2\]setGeodesic

setGeodesic(geodesic: boolean): void

Sets whether to draw each segment of a MapPolyline as a geodesic.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

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

Indicates whether to draw each segment of a MapPolyline as a geodesic. The default value is **false**.

-   **true**: yes
-   **false**: no

 |

**Example**:

mapPolyline.setGeodesic(true);

#### \[h2\]setGradient

setGradient(gradient: boolean): void

Sets whether a MapPolyline is gradient. This API takes effect only when the MapPolyline color is specified.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

gradient

 | 

boolean

 | 

Yes

 | 

Indicates whether a MapPolyline is gradient. The default value is **false**.

-   **true**: yes
-   **false**: no

 |

**Example**:

mapPolyline.setGradient(true);

#### \[h2\]setJointType

setJointType(jointType: mapCommon.JointType): void

Sets the joint type of all vertices of a MapPolyline, except the start and end vertices.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

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

Joint type.

 |

**Example**:

mapPolyline.setJointType(mapCommon.JointType.DEFAULT);

#### \[h2\]setPatterns

setPatterns(patterns: Array<mapCommon.PatternItem>): void

Sets patterns of a MapPolyline.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

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

Array of [PatternItem](../../mapcommon-map-attribute-model/document.md#section917314511192) objects.

 |

**Example**:

let linePattern: Array<mapCommon.PatternItem> = \[
  { type: mapCommon.PatternItemType.DASH, length: 100 },
  { type: mapCommon.PatternItemType.DOT, length: 100 },
  { type: mapCommon.PatternItemType.GAP, length: 100 }
\];
mapPolyline.setPatterns(linePattern);

#### \[h2\]setPoints

setPoints(points: Array<mapCommon.LatLng>): void

Sets the vertex coordinates of a MapPolyline.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

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

Array of vertices of a MapPolyline. A MapPolyline is open by default. To form a closed MapPolyline, its start and end vertices must coincide.

 |

**Example**:

let points: Array<mapCommon.LatLng> = \[
  { latitude: 31.18, longitude: 118.766 },
  { latitude: 31.38, longitude: 118.366 },
  { latitude: 31.68, longitude: 118.566 },
  { latitude: 31.98, longitude: 118.266 },
  { latitude: 31.88, longitude: 118.866 }
\];
mapPolyline.setPoints(points);

#### \[h2\]setStartCap

setStartCap(startCap: mapCommon.CapStyle): void

Sets the start vertex style of a MapPolyline.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

startCap

 | 

[mapCommon.CapStyle](../../mapcommon-map-attribute-model/document.md#section173028494409)

 | 

Yes

 | 

Start vertex style of a MapPolyline.

 |

**Example**:

mapPolyline.setStartCap(mapCommon.CapStyle.BUTT);

#### \[h2\]setWidth

setWidth(width: number): void

Sets the width of a MapPolyline.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

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

Width of a MapPolyline, in pixels. The value must be greater than or equal to 0.

The default value is **10**. If an invalid value is passed, the default value will be used.

 |

**Example**:

mapPolyline.setWidth(20);

#### \[h2\]setCustomTexture

setCustomTexture(customTexture: ResourceStr | image.PixelMap): Promise<void>

Sets the texture of a MapPolyline. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

customTexture

 | 

[ResourceStr](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr) | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

Yes

 | 

Texture of a MapPolyline. You are advised to use an image with a transparent background as the texture.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Example**:

// The icon is stored in the **resources/rawfile** directory.
await mapPolyline.setCustomTexture("icon/naviline\_arrow.png");

#### \[h2\]setCustomTexture

setCustomTexture(customTexture: ResourceStr | image.PixelMap, isTextureMappingUsed: boolean): Promise<void>

Sets the texture of a MapPolyline. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.3(15)

**Parameters**:

| 
Name

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

customTexture

 | 

[ResourceStr](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr) | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

Yes

 | 

Texture of a MapPolyline. You are advised to use an image with a transparent background as the texture.

 |
| 

isTextureMappingUsed

 | 

boolean

 | 

Yes

 | 

Indicates whether to use texture mapping for texture drawing. The default value is **false**. If it is set to **false**, it is recommended that the texture background be transparent.

-   **true**: yes
-   **false**: no

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Example**:

// The icon must be stored in the **resources/rawfile** directory.
await mapPolyline.setCustomTexture("icon/naviline\_arrow.png", true);

#### \[h2\]setCustomTextureIndexes

setCustomTextureIndexes(customTextureIndexes: number\[\]): Promise<void>

Dynamically sets the indexes of custom textures. After textures are configured for a MapPolyline, this API can be used to apply the textures to each segment of the MapPolyline. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.3(15)

**Parameters**:

| 
Name

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

customTextureIndexes

 | 

number\[\]

 | 

Yes

 | 

Texture index corresponding to each coordinate. The array length must be the same as the number of points.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

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

await mapPolyline.setCustomTextureIndexes(\[0,1,0\]);
