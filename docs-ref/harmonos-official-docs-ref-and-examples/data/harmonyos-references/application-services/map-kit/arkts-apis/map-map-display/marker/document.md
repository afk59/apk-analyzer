# Marker

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### Marker

Maker, which inherits from [BaseOverlay](../baseoverlay/document.md). An instance of the Marker type will be returned when the [addMarker](../mapcomponentcontroller/document.md#section0810361284) method in the map.[MapComponentController](../mapcomponentcontroller/document.md) class is called.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Example**:

let markerOptions: mapCommon.MarkerOptions = {
  position: {
    latitude: 39.9,
    longitude: 116.4
  }
};
let marker: map.Marker = await this.mapController.addMarker(markerOptions);

#### \[h2\]getTitle

getTitle(): string

Obtains the title of an information window.

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

string

 | 

Title of an information window.

 |

**Example**:

let title: string = marker.getTitle();

#### \[h2\]getSnippet

getSnippet(): string

Obtains the subtitle of an information window.

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

string

 | 

Subtitle of an information window.

 |

**Example**:

let snippet: string = marker.getSnippet();

#### \[h2\]getAlpha

getAlpha(): number

Obtains the opacity of a Marker.

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

Opacity of a Marker. The value ranges from 0 to 1.

 |

**Example**:

let alpha: number = marker.getAlpha();

#### \[h2\]getPosition

getPosition(): mapCommon.LatLng

Obtains the position of a Marker.

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

[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

Position of a Marker.

 |

**Example**:

let position: mapCommon.LatLng = marker.getPosition();

#### \[h2\]getRotation

getRotation(): number

Obtains the rotation angle of a Marker.

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

Rotation angle of a Marker.

 |

**Example**:

let rotation: number = marker.getRotation();

#### \[h2\]isClickable

isClickable(): boolean

Checks whether a Marker is tappable.

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

Indicates whether a Marker is tappable.

-   **true**: yes
-   **false**: no

 |

**Example**:

let isClickable: boolean = marker.isClickable();

#### \[h2\]isDraggable

isDraggable(): boolean

Checks whether users can long press a Marker to drag it.

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

Indicates whether users can long press a Marker to drag it.

-   **true**: yes
-   **false**: no

 |

**Example**:

let isDraggable: boolean = marker.isDraggable();

#### \[h2\]isFlat

isFlat(): boolean

Checks whether a Marker is flatly attached to the map.

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

Indicates whether a Marker is flatly attached to the map.

-   **true**: yes
-   **false**: no

 |

**Example**:

let isFlat: boolean = marker.isFlat();

#### \[h2\]setAlpha

setAlpha(alpha: number): void

Sets the opacity of a Marker.

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

alpha

 | 

number

 | 

Yes

 | 

Opacity of a Marker. The value ranges from 0 to 1. The default value is **1**. Invalid values are not processed.

-   **0**: completely transparent
-   **1**: completely opaque

 |

**Example**:

marker.setAlpha(0.5);

#### \[h2\]setClickable

setClickable(clickable: boolean): void

Sets whether a Marker is tappable.

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

Indicates whether a Marker is tappable. The default value is **false**.

-   **true**: yes
-   **false**: no

 |

**Example**:

marker.setClickable(true);

#### \[h2\]setDraggable

setDraggable(draggable: boolean): void

Sets whether users can long press a Marker to drag it.

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

draggable

 | 

boolean

 | 

Yes

 | 

Indicates whether users can long press a Marker to drag it. The default value is **false**.

-   **true**: yes
-   **false**: no

 |

**Example**:

marker.setDraggable(true);

#### \[h2\]setFlat

setFlat(flat: boolean): void

Sets whether to flatly attach a Marker to the map. If the Marker is flatly attached to the map, it will stay on the map when the camera rotates or tilts, and remain the same size when the camera zooms in or out. If the Marker faces the camera, it will always be drawn facing the camera and rotate or tilt with the camera.

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

flat

 | 

boolean

 | 

Yes

 | 

Indicates whether to flatly attach a Marker to the map. The default value is **false**.

-   **true**: yes
-   **false**: no

 |

**Example**:

marker.setFlat(true);

#### \[h2\]setIcon

setIcon(icon: string | image.PixelMap | Resource): Promise<void>

Sets the icon of a Marker. This API returns the result asynchronously through a promise.

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

icon

 | 

string | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | [Resource](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource)

 | 

Yes

 | 

Icon of a Marker.

-   Images in JPG, JPEG, PNG, GIF, WEBP, and SVG formats are supported.
-   This input parameter of the string type supports the following formats:
    -   Relative resource path: The icon is stored in **resources/rawfile**. Set **icon** to the relative path of the icon file in the **rawfile** folder.
    -   toDataURL format: For example, set **icon** to **image/png;base64,<Base64-encoded byte value of the icon file>**.

NOTE:

The **icon** parameter starts to support the [Resource](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource) and [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) types since version 5.0.0(12).

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
await marker.setIcon('icon/test.png');

#### \[h2\]setMarkerAnchor

setMarkerAnchor(anchorU: number, anchorV: number): void

Sets the anchor position of a Marker. The anchor is used to anchor a Marker icon to the map. The coordinates (0, 0), (1, 0), (0, 1), and (1, 1) respectively indicate the top-left, top-right, bottom-left, and bottom-right corners of the Marker icon. The following figure shows a Marker's anchor X whose coordinates are (0.5, 0.3).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/c40qmnqOTpyQxz1Hn8S7ZQ/en-us_image_0000002485159994.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062511Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C8EC8ED36A64EB5464E5735E454CD35B7235B89D718E4CA7D8360A0E2768D63F "Click to enlarge")

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

anchorU

 | 

number

 | 

Yes

 | 

Horizontal coordinate of an anchor, expressed in a proportion of the image width. The value ranges from 0 to 1. Invalid values are not processed.

 |
| 

anchorV

 | 

number

 | 

Yes

 | 

Vertical coordinate of an anchor, expressed in a proportion of the image height. The value ranges from 0 to 1. Invalid values are not processed.

 |

**Example**:

marker.setMarkerAnchor(1.0, 1.0);

#### \[h2\]setPosition

setPosition(latLng: mapCommon.LatLng): void

Sets the position coordinates of a Marker.

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

latLng

 | 

[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

Yes

 | 

Position coordinates of a Marker.

 |

**Example**:

let position: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4
};
marker.setPosition(position);

#### \[h2\]setRotation

setRotation(rotation: number): void

Sets the rotation angle of a Marker, that is, the angle in which the Marker rotates around the anchor clockwise. The rotation axis is perpendicular to the Marker. By default, the Marker is north aligned, and the rotation angle is 0 degrees.

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

rotation

 | 

number

 | 

Yes

 | 

Rotation angle of a Marker.

0 degrees is due north, and angles increase clockwise. The value range is \[0, 360). The default value is **0**. Values that fall outside the valid range will be adjusted to values within the range. For instance, the value **361** would be converted to **1**, and the value **\-1** would be converted to **359**.

 |

**Example**:

marker.setRotation(30);

#### \[h2\]setTitle

setTitle(title: string): void

Sets the title of an information window.

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

title

 | 

string

 | 

Yes

 | 

Title of an information window. If the title exceeds the display limit, the overflowing portion will be replaced with an ellipsis (...).

 |

**Example**:

marker.setTitle("title");

#### \[h2\]setSnippet

setSnippet(snippet: string): void

Sets the subtitle of an information window.

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

snippet

 | 

string

 | 

Yes

 | 

Subtitle of an information window. If the subtitle exceeds the display limit, the overflowing portion will be replaced with an ellipsis (...).

 |

**Example**:

marker.setSnippet("su");

#### \[h2\]setInfoWindowAnchor

setInfoWindowAnchor(anchorU: number, anchorV: number): void

Sets the anchor position of an information window.

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

anchorU

 | 

number

 | 

Yes

 | 

Horizontal coordinate of an anchor. The value ranges from 0 to 1. Invalid values are not processed.

 |
| 

anchorV

 | 

number

 | 

Yes

 | 

Vertical coordinate of an anchor. The value ranges from 0 to 1. Invalid values are not processed.

 |

**Example**:

marker.setInfoWindowAnchor(0.5, 0.5);

#### \[h2\]setInfoWindowVisible

setInfoWindowVisible(visible: boolean): void

Sets whether an information window is visible.

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

visible

 | 

boolean

 | 

Yes

 | 

Indicates whether an information window is visible.

-   **true**: yes
-   **false**: no

 |

**Example**:

marker.setInfoWindowVisible(true);

#### \[h2\]isInfoWindowVisible

isInfoWindowVisible(): boolean

Checks whether an information window is visible.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

Indicates whether an information window is visible.

-   **true**: yes
-   **false**: no

 |

**Example**:

let visible: boolean = marker.isInfoWindowVisible();

#### \[h2\]setAnimation

setAnimation(animation: Animation): void

Sets the animation of a Marker. [FontSizeAnimation](../fontsizeanimation/document.md) is not supported.

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

animation

 | 

[Animation](../animation/document.md)

 | 

Yes

 | 

Animation.

 |

**Example**:

let animation: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
animation.setDuration(3000);
let callbackStart = () => {
  console.info("animationStart", \`callback\`);
};
let callbackEnd = () => {
  console.info("animationEnd", \`callback\`);
};
animation.on("animationStart", callbackStart);
animation.on("animationEnd", callbackEnd);
animation.setFillMode(map.AnimationFillMode.BACKWARDS);
animation.setRepeatMode(map.AnimationRepeatMode.RESTART);
animation.setRepeatCount(100);

marker.setAnimation(animation);

#### \[h2\]startAnimation

startAnimation(): void

Starts the animation of a Marker.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Example**:

let animation: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
animation.setDuration(3000);
let callbackStart = () => {
  console.info("animationStart", \`callback\`);
};
let callbackEnd = () => {
  console.info("animationEnd", \`callback\`);
};
animation.on("animationStart", callbackStart);
animation.on("animationEnd", callbackEnd);
animation.setFillMode(map.AnimationFillMode.BACKWARDS);
animation.setRepeatMode(map.AnimationRepeatMode.RESTART);
animation.setRepeatCount(100);

marker.setAnimation(animation);
marker.startAnimation();

#### \[h2\]clearAnimation

clearAnimation(): void

Clears the animation of a Marker.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Example**:

marker.clearAnimation();

#### \[h2\]getAltitude

getAltitude(): number

Obtains the altitude.

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

Altitude, in meters.

 |

**Example**:

let altitude: number = marker.getAltitude();

#### \[h2\]setAltitude

setAltitude(altitude: number): void

Sets the altitude.

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

altitude

 | 

number

 | 

Yes

 | 

Altitude, in meters.

 |

**Example**:

marker.setAltitude(500);

#### \[h2\]setAnnotationVisible

setAnnotationVisible(visible: boolean): void

Sets whether to display the annotation of a Marker.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

visible

 | 

boolean

 | 

Yes

 | 

Indicates whether to display the annotation of a Marker.

-   **true**: yes
-   **false**: no

 |

**Example**:

marker.setAnnotationVisible(true);

#### \[h2\]isAnnotationVisible

isAnnotationVisible(): boolean

Checks whether the annotation of a Marker is visible.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

Indicates whether the annotation of a Marker is visible.

-   **true**: yes
-   **false**: no

 |

**Example**:

let isVisible = marker.isAnnotationVisible();

#### \[h2\]setIconBuilder

setIconBuilder(iconBuilder: CustomBuilder): Promise<void>

Sets a custom component for generating a Marker icon. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

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

iconBuilder

 | 

[CustomBuilder](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8)

 | 

Yes

 | 

Custom component.

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

1002601005

 | 

Failed to generate the icon of the custom component.

 |

**Example**:

@Builder
renderBuilder() {
  Stack({ alignContent: Alignment.Center }) {
    Text('Test Icon Builder')
  }
  .height(50)
  .width(200)
}
// Set the custom component.
try {
  await this.marker?.setIconBuilder(() => {
    this.renderBuilder();
  })
} catch (error) {
  let err = error as BusinessError;
  console.error('Marker icon builder test error code' + err.code + 'message:' + err.message);
}

#### \[h2\]setOffset

setOffset(x: number, y: number): void

Sets the offset of the Marker icon.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.2(22).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.2(22)

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

x

 | 

number

 | 

Yes

 | 

Offset along the X axis, in pixels. The origin is the center point of the icon. Values **null**, **undefined**, and **NaN** are not processed.

 |
| 

y

 | 

number

 | 

Yes

 | 

Offset along the Y axis, in pixels. The origin is the center point of the icon. Values **null**, **undefined**, and **NaN** are not processed.

 |

**Example**:

marker.setOffset(20,20);

#### \[h2\]getOffsetX

getOffsetX(): number

Obtains the offset of the Marker icon along the X axis.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.2(22).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.2(22)

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

Offset of the Marker icon along the X axis, in pixels. The origin is the center point of the icon.

 |

**Example**:

let X: number = marker.getOffsetX();

#### \[h2\]getOffsetY

getOffsetY(): number

Obtains the offset of the Marker icon along the Y axis.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.2(22).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.2(22)

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

Offset of the Marker icon along the Y axis, in pixels. The origin is the center point of the icon.

 |

**Example**:

let Y: number = marker.getOffsetY();
