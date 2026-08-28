# ImageOverlay

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### ImageOverlay

ImageOverlay. This API inherits from [BaseOverlay](../baseoverlay/document.md).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Example**:

let imageOverlayParams: mapCommon.ImageOverlayParams = {
  bounds: {
    southwest: { latitude: 32, longitude: 118 },
    northeast: { latitude: 32.4, longitude: 118.4 }
  },
  // The icon must be stored in the **resources/rawfile** directory.
  image: 'icon.png',
  transparency: 0.3,
  zIndex: 101,
  anchorU: 0.5,
  anchorV: 0.5,
  clickable: true,
  visible: true,
  bearing: 0
};
let imageOverlay = await this.mapController?.addImageOverlay(imageOverlayParams);
imageOverlay.setBearing(180);
let bearing: number = imageOverlay.getBearing();

#### \[h2\]getBearing

getBearing(): number

Obtains the rotation angle of an ImageOverlay.

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

Rotation angle of an ImageOverlay.

 |

**Example**:

let bearing: number = imageOverlay.getBearing();

#### \[h2\]getBounds

getBounds(): mapCommon.LatLngBounds

Obtains the bounds of an ImageOverlay.

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

[mapCommon.LatLngBounds](../../mapcommon-map-attribute-model/document.md#section96341159111320)

 | 

Bounds of an ImageOverlay.

 |

**Example**:

let bounds: mapCommon.LatLngBounds = imageOverlay.getBounds();

#### \[h2\]getHeight

getHeight(): number

Obtains the height of an ImageOverlay.

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

Height of an ImageOverlay, in meters.

 |

**Example**:

let height: number = imageOverlay.getHeight();

#### \[h2\]getWidth

getWidth(): number

Obtains the width of an ImageOverlay.

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

Width of an ImageOverlay, in meters.

 |

**Example**:

let width: number = imageOverlay.getWidth();

#### \[h2\]getPosition

getPosition(): mapCommon.LatLng

Obtains the position of an ImageOverlay.

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

[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

Position of an ImageOverlay.

 |

**Example**:

let position: mapCommon.LatLng = imageOverlay.getPosition();

#### \[h2\]getTransparency

getTransparency(): number

Obtains the opacity of an ImageOverlay.

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

Transparency of an ImageOverlay. The value ranges from 0 to 1. The value **1** indicates completely transparent, and the value **0** indicates completely opaque.

 |

**Example**:

let transparency: number = imageOverlay.getTransparency();

#### \[h2\]isClickable

isClickable(): boolean

Checks whether an ImageOverlay is tappable.

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

boolean

 | 

Indicates whether an ImageOverlay is tappable.

-   **true**: yes
-   **false**: no

 |

**Example**:

let click: boolean = imageOverlay.isClickable();

#### \[h2\]setBearing

setBearing(bearing: number): void

Sets the rotation angle of an ImageOverlay.

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

bearing

 | 

number

 | 

Yes

 | 

Rotation angle of an ImageOverlay.

0 degrees is due north, and angles increase clockwise. The value range is \[0, 360). The default value is **0**. Values that fall outside the valid range will be adjusted to values within the range. For instance, the value **361** would be converted to **1**, and the value **\-1** would be converted to **359**.

 |

**Example**:

imageOverlay.setBearing(180);

#### \[h2\]setClickable

setClickable(clickable: boolean): void

Sets whether an ImageOverlay is tappable.

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

clickable

 | 

boolean

 | 

Yes

 | 

Indicates whether an ImageOverlay is tappable.

-   **true**: yes
-   **false**: no

 |

**Example**:

imageOverlay.setClickable(false);

#### \[h2\]setDimensions

setDimensions(width: number, height?: number): void

Sets the width and height of an ImageOverlay.

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

Width, in meters. The value must be a positive integer.

 |
| 

height

 | 

number

 | 

No

 | 

Height, in meters. The value must be a positive integer. If the height is not set, the height will be adjusted proportionally based on the default aspect ratio of the ImageOverlay image.

 |

**Example**:

imageOverlay.setDimensions(100000, 100000);

#### \[h2\]setImage

setImage(image: ResourceStr | image.PixelMap): Promise<void>

Sets the image of an ImageOverlay. This API returns the result asynchronously through a promise.

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

image

 | 

[ResourceStr](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr) | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

Yes

 | 

Image of an ImageOverlay.

Images in JPG, JPEG, PNG, GIF, WEBP, and SVG formats are supported.

NOTE:

[ResourceStr](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr) indicates either resource type or string type. Input parameters of the string type can be in either of the following formats:

-   Relative resource path: The image is stored in **resources/rawfile**. Set **image** to the relative path of the image file in the **rawfile** folder.
-   toDataURL format: For example, set **image** to **image/png;base64,<Base64-encoded byte value of the image file>**.

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
await imageOverlay.setImage("icon.png");

#### \[h2\]setBounds

setBounds(bounds: mapCommon.LatLngBounds): void

Sets the bounds of an ImageOverlay.

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

Bounds of an ImageOverlay.

 |

**Example**:

let bounds: mapCommon.LatLngBounds = {
  southwest: { longitude: 118, latitude: 31 },
  northeast: { longitude: 119, latitude: 32 }
};
imageOverlay.setBounds(bounds);

#### \[h2\]setPosition

setPosition(position: mapCommon.LatLng): void

Sets the position of an ImageOverlay.

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

position

 | 

[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

Yes

 | 

Position of an ImageOverlay.

 |

**Example**:

let position: mapCommon.LatLng = { longitude: 118, latitude: 31 };
imageOverlay.setPosition(position);

#### \[h2\]setTransparency

setTransparency(transparency: number): void

Sets the transparency of an ImageOverlay.

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

transparency

 | 

number

 | 

Yes

 | 

Transparency of an ImageOverlay. The value ranges from 0 to 1. The value **1** indicates completely transparent, and the value **0** indicates completely opaque. Invalid values are ineffective.

 |

**Example**:

imageOverlay.setTransparency(0.1);
