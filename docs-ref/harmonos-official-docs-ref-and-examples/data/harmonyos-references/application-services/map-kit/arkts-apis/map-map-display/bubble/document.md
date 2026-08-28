# Bubble

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### Bubble

Bubble. This API inherits from [BasePriorityOverlay](../basepriorityoverlay/document.md). An instance of the Bubble type will be returned when the [addBubble](../mapcomponentcontroller/document.md#section1732020231338) method in the map.[MapComponentController](../mapcomponentcontroller/document.md) class is called.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Example**:

let bubbleOptions: mapCommon.BubbleParams = {
  positions: \[\[{
    latitude: 31.98, longitude: 118.766
  }\]\],
  // The icons must be stored in the **resources/rawfile** directory.
  icons: \[
    'icon.png',
    'icon.png',
    'icon.png',
    'icon.png'
  \],
  forceVisible: true,
  priority: 3,
  minZoom: 2,
  maxZoom: 20,
  visible: true,
  zIndex: 1
};
let bubble: map.Bubble = await this.mapController.addBubble(bubbleOptions);

#### \[h2\]setIcons

setIcons(icons: Array<string | image.PixelMap | Resource>): Promise<void>

Sets the icon of a Bubble. This API returns the result asynchronously through a promise.

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

icons

 | 

Array<string | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | [Resource](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource)\>

 | 

Yes

 | 

Icons of a Bubble.

-   You must set the icons for four directions. The icons must have the same height and width.
-   Images in JPG, JPEG, PNG, GIF, WEBP, and SVG formats are supported.
-   This input parameter of the string type supports the following formats:
    -   Relative resource path: The icons are stored in **resources/rawfile**. Set **icons** to the relative paths of the icon files in the **rawfile** folder.
    -   toDataURL format: For example, set **icons** to **image/png;base64,<Base64-encoded byte values of the icon files>**.

NOTE:

The **icons** parameter starts to support the [Resource](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource) and [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) types since version 5.0.0(12).

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

import { image } from '@kit.ImageKit';

// The icons must be stored in the **resources/rawfile** directory.
let icons: Array<string | image.PixelMap | Resource> = \[
  'test1.png',
  'test2.png',
  'test3.png',
  'test4.png'
\];
await bubble.setIcons(icons);

#### \[h2\]setPositions

setPositions(positions: Array<Array<mapCommon.LatLng>>): void

Sets the candidate position coordinates of a Bubble.

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

positions

 | 

Array<Array<[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)\>>

 | 

Yes

 | 

Candidate position coordinates of a Bubble.

 |

**Example**:

let positions: Array<Array<mapCommon.LatLng>> = \[\[
  { latitude: 31.9844, longitude: 118.7112 },
  { latitude: 31.9844, longitude: 118.7262 },
  { latitude: 31.9844, longitude: 118.7362 },
  { latitude: 31.9844, longitude: 118.7462 },
  { latitude: 31.9844, longitude: 118.7562 },
  { latitude: 31.9844, longitude: 118.7662 },
  { latitude: 31.9844, longitude: 118.7762 }
\]\];
bubble.setPositions(positions);
