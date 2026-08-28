# mapCommon (Map Attribute Model)

This module provides APIs for setting map component attributes.

**Start version**: 4.1.0(11)

#### Module Import

import { mapCommon } from '@kit.MapKit';

#### MapOptions

Sets initialization attributes of a map component.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

mapType

 | 

[MapType](#en-us_topic_0000001245084266_section18522846142615)

 | 

No

 | 

Yes

 | 

Map type. The default value is [MapType](#en-us_topic_0000001245084266_section18522846142615).STANDARD. An invalid value is handled as the default value.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

position

 | 

[CameraPosition](#section105031244194712)

 | 

No

 | 

No

 | 

Map camera position.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

bounds

 | 

[LatLngBounds](#section96341159111320)

 | 

No

 | 

Yes

 | 

Map display bounds. If it is set to an invalid value, the map has no bounds.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

NOTE:

The latitude of the southwest corner cannot be greater than that of the northeast corner.

 |
| 

minZoom

 | 

number

 | 

No

 | 

Yes

 | 

Minimum map zoom level. The value ranges from 2 to 20. The default value is **2**. An invalid value is handled as the default value.

If this parameter is set to a value less than 2, the value **2** will be used instead.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

maxZoom

 | 

number

 | 

No

 | 

Yes

 | 

Maximum map zoom level. The value ranges from 2 to 20. The default value is **20**. An invalid value is handled as the default value.

If this parameter is set to a value greater than 20, the value **20** will be used instead.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

rotateGesturesEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to support rotate gestures. The default value is **true**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

scrollGesturesEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to support swipe gestures. The default value is **true**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

zoomGesturesEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to support zoom gestures. The default value is **true**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

tiltGesturesEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to support tilt gestures. The default value is **true**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

zoomControlsEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to display the zoom control. The default value is **true**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

myLocationControlsEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to display the my-location icon. The default value is **false**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

compassControlsEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to display the compass control. The default value is **true**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

scaleControlsEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to display the scale. The default value is **false**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

padding

 | 

[Padding](#section144591344648)

 | 

No

 | 

Yes

 | 

Padding between the map and its edges. The default value is **{ left: 0 , top: 0 , right: 0 , bottom: 0 }**.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

styleId

 | 

string

 | 

No

 | 

Yes

 | 

Custom style ID. If the ID is invalid, the system style is used. For details, please refer to [Displaying a Custom Map](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-style).

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

dayNightMode

 | 

[DayNightMode](#section634916281725)

 | 

No

 | 

Yes

 | 

Day/Dark mode. The default value is [DayNightMode](#section634916281725).DAY (day mode).

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

alwaysShowScaleEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to always display the scale. This parameter is valid only when the scale is enabled. To enable the scale, set the **scaleControlsEnabled** attribute to **true** during map initialization or by using the [setScaleControlsEnabled](../map-map-display/mapcomponentcontroller/document.md#section1845222318187) method.

-   **true**: yes
-   **false**: no

The default value is **false**.

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

logoScale

 | 

number

 | 

No

 | 

Yes

 | 

Logo scaling ratio. The value ranges from 0.8 to 1. The default value is **1**.

**Start version**: 5.0.3(15)

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

sphereEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable the 3D globe view. The default value is **false**.

-   **true**: yes
-   **false**: no

**Start version**: 5.0.3(15)

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

indoorMapEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable the indoor map. The default value is **false**.

-   **true**: yes
-   **false**: no

**Start version**: 5.1.1(19)

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

 |
| 

scaleUnit

 | 

[ScaleUnit](#section2230143218276)

 | 

No

 | 

Yes

 | 

Map scale unit. The default value is [ScaleUnit](#section2230143218276).METRIC\_UNIT (metric unit).

**Start version**: 5.1.1(19)

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

 |
| 

language

 | 

string

 | 

No

 | 

Yes

 | 

Map language. Refer to [Languages supported by the map component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-language#section105361721671) for supported language options. The current system language is used by default.

**Start version**: 6.0.0(20)

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

 |

**Example**:

// Map initialization parameters.
let mapOptions: mapCommon.MapOptions = {
  mapType: mapCommon.MapType.STANDARD,
  position: {
    target: {
      latitude: 39.9,
      longitude: 116.4
    },
    zoom: 10
  },
  bounds: {
    northeast: {
      latitude: 41.5,
      longitude: 125.5
    },
    southwest: {
      latitude: 37.5,
      longitude: 108.5
    }
  },
  maxZoom: 20,
  minZoom: 2,
  rotateGesturesEnabled: true,
  scrollGesturesEnabled: true,
  zoomGesturesEnabled: true,
  zoomControlsEnabled: true,
  myLocationControlsEnabled: false,
  dayNightMode: mapCommon.DayNightMode.NIGHT,
  scaleControlsEnabled: true,
  alwaysShowScaleEnabled: true,
  scaleUnit: mapCommon.ScaleUnit.METRIC\_UNIT,
  language: 'zh-Hans'
};

#### LatLng

Defines a longitude-latitude object.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

latitude

 | 

number

 | 

No

 | 

No

 | 

Latitude. The value ranges from –90 to 90.

 |
| 

longitude

 | 

number

 | 

No

 | 

No

 | 

Longitude. The value ranges from –180 to 180 (excluded).

 |

**Example**:

let position: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4
};

#### CameraPosition

Defines the camera status, including the position, tilt angle, and zoom level.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

target

 | 

[LatLng](#section20691173773810)

 | 

No

 | 

No

 | 

Longitude and latitude of the map center.

 |
| 

zoom

 | 

number

 | 

No

 | 

No

 | 

Zoom level near the center of the screen. The value ranges from 2 to 20. The default value is **2**.

 |
| 

tilt

 | 

number

 | 

No

 | 

Yes

 | 

Tilt angle of the camera, that is, angle of the camera from the nadir (directly facing the Earth). The value ranges from 0 to 75. The default value is **0**.

 |
| 

bearing

 | 

number

 | 

No

 | 

Yes

 | 

Map rotation angle.

0 degrees is due north, and angles increase clockwise. The value range is \[0, 360). The default value is **0**. Values that fall outside the valid range will be adjusted to values within the range. For instance, the value **361** would be converted to **1**, and the value **\-1** would be converted to **359**.

 |

**Example**:

let cameraPosition: mapCommon.CameraPosition = {
  target: {
    latitude: 39.9,
    longitude: 116.4
  },
  zoom: 10,
  tilt: 45,
  bearing: 90
};

#### LatLngBounds

Defines a rectangular region using longitudes and latitudes.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

northeast

 | 

[LatLng](#section20691173773810)

 | 

No

 | 

No

 | 

Longitude and latitude of the northeast corner.

 |
| 

southwest

 | 

[LatLng](#section20691173773810)

 | 

No

 | 

No

 | 

Longitude and latitude of the southwest corner.

 |

**Example**:

let bounds: mapCommon.LatLngBounds = {
  northeast: {
    latitude: 41.5,
    longitude: 125.5
  },
  southwest: {
    latitude: 37.5,
    longitude: 108.5
  }
};

#### PatternItem

Defines the stroke pattern of a MapPolyline or the outline of a MapPolygon or MapCircle.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

type

 | 

[PatternItemType](#section128001052193017)

 | 

No

 | 

No

 | 

Stroke pattern.

 |
| 

length

 | 

number

 | 

No

 | 

Yes

 | 

Stroke length when the stroke pattern is DASH or GAP, in pixels. The value must be greater than or equal to 0. The default value is **1**.

 |

**Example**:

let patternItem: mapCommon.PatternItem = {
  type: mapCommon.PatternItemType.DASH,
  length: 10
};

#### MyLocationStyle

Defines the custom style of the my-location icon.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

anchorU

 | 

number

 | 

No

 | 

Yes

 | 

Horizontal offset of the anchor. The value ranges from 0 to 1. The default value is **0.5**.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

anchorV

 | 

number

 | 

No

 | 

Yes

 | 

Vertical offset of the anchor. The value ranges from 0 to 1. The default value is **0.5**.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

icon

 | 

string | [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | [Resource](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource)

 | 

No

 | 

Yes

 | 

My-location icon.

-   Images in JPG, JPEG, PNG, GIF, WEBP, and SVG formats are supported.
-   This input parameter of the string type supports the following formats:
    -   Relative resource path: The icon is stored in **resources/rawfile**. Set **icon** to the relative path of the icon file in the **rawfile** folder.
    -   toDataURL format: For example, set **icon** to **image/png;base64,<Base64-encoded byte value of the icon file>**.

NOTE:

The **icon** parameter starts to support the [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) and [Resource](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource) types since version 5.0.0(12).

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

radiusFillColor

 | 

number

 | 

No

 | 

Yes

 | 

Fill color of the my-location icon. The default value is **0x8F7570FF** (purple). The color value is in ARGB format.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

displayType

 | 

[MyLocationDisplayType](#section78428244375)

 | 

No

 | 

Yes

 | 

Display style of the my-location icon. The default value is [MyLocationDisplayType](#section78428244375).DEFAULT.

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |

**Example**:

let style: mapCommon.MyLocationStyle = {
  anchorU: 0.5,
  anchorV: 1,
  radiusFillColor: 0xffff0000,
  // The icon must be stored in the **resources/rawfile** directory.
  icon: 'test.png',
  displayType: mapCommon.MyLocationDisplayType.FOLLOW
};

#### POI

Defines a POI object on the map.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

id

 | 

string

 | 

No

 | 

No

 | 

ID of a POI.

 |
| 

name

 | 

string

 | 

No

 | 

No

 | 

Name of a POI.

 |
| 

position

 | 

[LatLng](#section20691173773810)

 | 

No

 | 

No

 | 

Longitude and latitude of a POI.

 |

**Example**:

let poi: mapCommon.Poi = {
  id: "1001",
  name: "Chengdong Barbecue Store",
  position: {
    latitude: 39.6,
    longitude: 116.4
  }
};

#### BaseOverlayOptions

Defines the basic attributes of an overlay. Classes such as [MarkerOptions](#section559041743210), [MapCircleOptions](#section5282124803117), [MapPolygonOptions](#section1615694815308), [MapPolylineOptions](#section113246334153), [MapArcParams](#section943619551002), [ImageOverlayParams](#section12537418218), and [BasePriorityOverlayParams](#section20126194774515) inherit from this base class.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

visible

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether an overlay is visible. The default value is **true**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

 |
| 

zIndex

 | 

number

 | 

No

 | 

Yes

 | 

Overlay order of an overlay. An overlay with a larger z-index covers that with a smaller z-index. Overlays with the same z-index cover each other by the order in which they are added. If the z-index is not set during overlay initialization, the default value **0** will be used. If an invalid value is passed, the default value will be used.

NOTE:

The value of **zIndex** of [BasePriorityOverlayParams](#section20126194774515) is rounded down to an integer.

 |

#### MarkerOptions

Describes the attributes of a Marker. This API inherits from [BaseOverlayOptions](#section7400647135116).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

position

 | 

[LatLng](#section20691173773810)

 | 

No

 | 

No

 | 

Position coordinates of a Marker.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

rotation

 | 

number

 | 

No

 | 

Yes

 | 

Rotation angle of a Marker.

0 degrees is due north, and angles increase clockwise. The value range is \[0, 360). The default value is **0**. Values that fall outside the valid range will be adjusted to values within the range. For instance, the value **361** would be converted to **1**, and the value **\-1** would be converted to **359**.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

icon

 | 

string | [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | [Resource](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource)

 | 

No

 | 

Yes

 | 

Icon. If this parameter is not passed, the default icon is displayed.

-   Images in JPG, JPEG, PNG, GIF, WEBP, and SVG formats are supported.
-   This input parameter of the string type supports the following formats:
    -   Relative resource path: The icon is stored in **resources/rawfile**. Set **icon** to the relative path of the icon file in the **rawfile** folder.
    -   toDataURL format: For example, set **icon** to **image/png;base64,<Base64-encoded byte value of the icon file>**.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

NOTE:

The **icon** parameter starts to support the [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) and [Resource](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource) types since version 5.0.0(12).

 |
| 

alpha

 | 

number

 | 

No

 | 

Yes

 | 

Transparency. The value ranges from 0 to 1. The value **0** indicates completely transparent, and the value **1** indicates completely opaque. The default value is **1**. An invalid value is handled as the default value.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

anchorU

 | 

number

 | 

No

 | 

Yes

 | 

Horizontal coordinate of the anchor of a Marker. The recommended value ranges from 0 to 1, expressed in a proportion of the Marker image width. The default value is **0.5**. An invalid value is handled as the default value.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

anchorV

 | 

number

 | 

No

 | 

Yes

 | 

Vertical coordinate of the anchor of a Marker. The recommended value ranges from 0 to 1, expressed in a proportion of the Marker image height. The default value is **1**. An invalid value is handled as the default value.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

clickable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether a Marker is clickable. The default value is **false**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

draggable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether a Marker can be dragged by long pressing. The default value is **false**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

flat

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether a Marker is flat on the map. The default value is **false**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

title

 | 

string

 | 

No

 | 

Yes

 | 

Title of an information window. If a title exceeds the display limit, the overflowing portion will be replaced with an ellipsis (...).

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

snippet

 | 

string

 | 

No

 | 

Yes

 | 

Subtitle of an information window. If a subtitle exceeds the display limit, the overflowing portion will be replaced with an ellipsis (...).

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

infoWindowAnchorU

 | 

number

 | 

No

 | 

Yes

 | 

Position of the anchor of an information window in the horizontal direction. The value ranges from 0 to 1. The default value is **0.5**. An invalid value is handled as the default value.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

infoWindowAnchorV

 | 

number

 | 

No

 | 

Yes

 | 

Position of the anchor of an information window in the vertical direction. The value ranges from 0 to 1. The default value is **0**. An invalid value is handled as the default value.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

altitude

 | 

number

 | 

No

 | 

Yes

 | 

Altitude, in meters. The default value is **0**.

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

collisionRule

 | 

[CollisionRule](#section230211714264)

 | 

No

 | 

Yes

 | 

Rule for handling collision between markers and map POIs. The default value is **[CollisionRule](#section230211714264).NONE**. If an invalid value is passed, the default value will be used.

NOTE:

Starting from version 5.0.3(15), **collisionRule** supports the **CollisionRule.NONE** and **CollisionRule.ALL** types.

**Start version**: 5.0.3(15)

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

annotations

 | 

[Text](#section132819018245)\[\]

 | 

No

 | 

Yes

 | 

Annotation of a Marker. The value length ranges from 1 to 3.

**Start version**: 5.0.3(15)

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

showIcon

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to display the icon of a Marker. The default value is **true**.

-   **true**: yes
-   **false**: no

**Start version**: 5.0.3(15)

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

annotationPosition

 | 

[TextPosition](#section939311423718)

 | 

No

 | 

Yes

 | 

Position of the annotation relative to the icon. The default value is **[TextPosition](#section939311423718).DEFAULT**.

**Start version**: 5.0.3(15)

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

iconBuilder

 | 

[CustomBuilder](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8)

 | 

No

 | 

Yes

 | 

Custom component used to generate a Marker icon. The priority of the custom component is higher than that of an icon attribute.

**Start version**: 6.0.0(20)

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

 |
| 

offsetX

 | 

number

 | 

No

 | 

Yes

 | 

Offset of the Marker icon along the X axis, in pixels. The positive direction of the X axis is to the right, and the origin is at the center point of the icon. If only **offsetX** is passed, **offsetY** is set to **0** by default. Invalid values will not be processed. If **offsetX** is set, the offset is determined by **offsetX**. If **offsetX** is not set, the offset is determined by **anchorU**.

**Start version**: 6.0.2(22)

**Atomic service API**: This API can be used in atomic services since API version 6.0.2(22).

 |
| 

offsetY

 | 

number

 | 

No

 | 

Yes

 | 

Offset of the Marker icon along the Y axis, in pixels. The positive direction of the Y axis is downward, and the origin is at the center point of the icon. If only **offsetY** is passed, **offsetX** is set to **0** by default. Invalid values will not be processed. If **offsetY** is set, the offset is determined by **offsetY**. If **offsetY** is not set, the offset is determined by **anchorV**.

**Start version**: 6.0.2(22)

**Atomic service API**: This API can be used in atomic services since API version 6.0.2(22).

 |

**Example**:

let markerOptions: mapCommon.MarkerOptions = {
  position: {
    latitude: 39.9,
    longitude: 116.4
  },
  rotation: 0,
  visible: true,
  zIndex: 0,
  alpha: 1,
  anchorU: 0.5,
  anchorV: 1,
  clickable: true,
  draggable: true,
  flat: false,
  // The icon must be stored in the **resources/rawfile** directory.
  icon: 'test.png',
  altitude: 100,
  collisionRule: mapCommon.CollisionRule.ALL,
  offsetX: 20,
  offsetY: 20
};

#### MapCircleOptions

Describes the attributes of a MapCircle. This API inherits from [BaseOverlayOptions](#section7400647135116).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

center

 | 

[LatLng](#section20691173773810)

 | 

No

 | 

No

 | 

Center of a MapCircle, which cannot be empty or **null**. A MapCircle can be drawn only when the latitude of its center is within the range from -85.051119 to 85.051119. If the latitude of the MapCircle center is -85.051119 or 85.051119, a MapCircle with a radius of 1 meter can be drawn exactly. Invalid parameter values are not processed.

 |
| 

radius

 | 

number

 | 

No

 | 

No

 | 

Radius of a MapCircle, in meters. The default value is **0**. An invalid value is handled as the default value.

 |
| 

clickable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether a MapCircle is clickable. The default value is **false**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

 |
| 

fillColor

 | 

number

 | 

No

 | 

Yes

 | 

Fill color of a MapCircle. The default value is **0x00000000** (black). The color value is in ARGB format. An invalid value is handled as the default value.

 |
| 

strokeColor

 | 

number

 | 

No

 | 

Yes

 | 

Stroke color of a MapCircle's outline. The default value is **0xff000000** (black). The color value is in ARGB format. An invalid value is handled as the default value.

 |
| 

patterns

 | 

Array<[PatternItem](#section917314511192)\>

 | 

No

 | 

Yes

 | 

Pattern of a MapCircle's outline, which is an empty array by default. An invalid value is handled as the default value.

 |
| 

strokeWidth

 | 

number

 | 

No

 | 

Yes

 | 

Stroke width of a MapCircle's outline, in pixels. The value must be greater than or equal to 0. The default value is **10**. An invalid value is handled as the default value.

 |

**Example**:

let mapCircleOptions: mapCommon.MapCircleOptions = {
  center: {
    latitude: 39.9,
    longitude: 116.4
  },
  radius: 5000,
  clickable: true,
  fillColor: 0XFF00FFFF,
  strokeColor: 0xFFFF0000,
  strokeWidth: 10,
  visible: true,
  zIndex: 15
};

#### MapPolygonOptions

Describes the attributes of a MapPolygon. This API inherits from [BaseOverlayOptions](#section7400647135116).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

points

 | 

Array<[LatLng](#section20691173773810)\>

 | 

No

 | 

No

 | 

Array of vertices of a MapPolygon. The value range of the vertex latitude is \[-85.2, 85.2\]. Invalid values are not processed.

 |
| 

holes

 | 

Array<Array<[LatLng](#section20691173773810)\>>

 | 

No

 | 

Yes

 | 

Array of holes in a MapPolygon, which is an empty array by default. An invalid value is handled as the default value.

NOTE:

When coordinates of a hole coincide with the outline of the MapPolygon, it can lead to rendering anomalies, such as extra hollow regions being displayed.

 |
| 

clickable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether a MapPolygon is clickable. The default value is **false**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

 |
| 

fillColor

 | 

number

 | 

No

 | 

Yes

 | 

Fill color of a MapPolygon. The default value is **0x00000000** (black). The color value is in ARGB format. An invalid value is handled as the default value.

 |
| 

geodesic

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether segments of a MapPolygon are geodesics. The default value is **false**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

 |
| 

strokeColor

 | 

number

 | 

No

 | 

Yes

 | 

Stroke color of a MapPolygon's outline. The default value is **0xff000000** (black). The color value is in ARGB format. An invalid value is handled as the default value.

 |
| 

jointType

 | 

[JointType](#section73559613164)

 | 

No

 | 

Yes

 | 

Joint type of a MapPolygon. The default value is [JointType](#section73559613164).DEFAULT. An invalid value is handled as the default value.

 |
| 

patterns

 | 

Array<[PatternItem](#section917314511192)\>

 | 

No

 | 

Yes

 | 

Pattern of a MapPolygon's outline, which is an empty array by default. An invalid value is handled as the default value.

 |
| 

strokeWidth

 | 

number

 | 

No

 | 

Yes

 | 

Stroke width of a MapPolygon's outline, in pixels. The value must be greater than or equal to 0. The default value is **10**. An invalid value is handled as the default value.

 |

**Example**:

let polygonOptions: mapCommon.MapPolygonOptions = {
  points: \[
    { latitude: 41.893478, longitude: 116.4 },
    { latitude: 41.893478, longitude: 121.4 },
    { latitude: 45.893478, longitude: 121.4 },
    { latitude: 45.893478, longitude: 116.4 }
  \],
  holes: \[\],
  clickable: true,
  fillColor: 0xff00DE00,
  geodesic: false,
  strokeColor: 0xff000000,
  jointType: mapCommon.JointType.DEFAULT,
  patterns: \[\],
  strokeWidth: 10,
  visible: true,
  zIndex: 0
};

#### MapPolylineOptions

Describes the attributes of a MapPolyline. This API inherits from [BaseOverlayOptions](#section7400647135116).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

points

 | 

Array<[LatLng](#section20691173773810)\>

 | 

No

 | 

No

 | 

Set of vertices of a MapPolyline. Invalid values are not processed.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

clickable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether a MapPolyline is clickable. The default value is **false**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

color

 | 

number

 | 

No

 | 

Yes

 | 

Color of a MapPolyline. The default value is **0xff000000** (black). The color value is in ARGB format. An invalid value is handled as the default value.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

colors

 | 

Array<number>

 | 

No

 | 

Yes

 | 

Colors for different segments of a MapPolyline, which is an empty array (indicating black) by default. The color value is in ARGB format. An invalid value is handled as the default value.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

startCap

 | 

[CapStyle](#section173028494409)

 | 

No

 | 

Yes

 | 

Style of the start vertex of a MapPolyline. The default value is [CapStyle](#section173028494409).BUTT. An invalid value is handled as the default value.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

endCap

 | 

[CapStyle](#section173028494409)

 | 

No

 | 

Yes

 | 

Style of the end vertex of a MapPolyline. The default value is [CapStyle](#section173028494409).BUTT. An invalid value is handled as the default value.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

geodesic

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether segments of a MapPolyline are geodesics. The default value is **false**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

jointType

 | 

[JointType](#section73559613164)

 | 

No

 | 

Yes

 | 

Joint type of a MapPolyline. The default value is [JointType](#section73559613164).DEFAULT. An invalid value is handled as the default value.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

patterns

 | 

Array<[PatternItem](#section917314511192)\>

 | 

No

 | 

Yes

 | 

Pattern of a MapPolyline, which is an empty array by default. An invalid value is handled as the default value.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

width

 | 

number

 | 

No

 | 

Yes

 | 

Width of a MapPolyline, in pixels. The value ranges from 0 to 512. The default value is **10**. If a value greater than 512 is passed, the value **512** will be used.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

gradient

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether a MapPolyline is gradient. The default value is **false**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

customTexture

 | 

[ResourceStr](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr) | [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

No

 | 

Yes

 | 

Texture of a MapPolyline. You are advised to use an image with a transparent background as the texture.

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

isTextureMappingUsed

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to use texture mapping to process textures. The default value is **false**.

-   **true**: yes
-   **false**: no

**Start version**: 5.0.3(15)

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

customTextures

 | 

Array<[ResourceStr](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr) | [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\>

 | 

No

 | 

Yes

 | 

Texture images.

**Start version**: 5.0.3(15)

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

NOTE:

If both **customTexture** and **customTextures** are passed, **customTexture** is used preferentially.

 |
| 

customTextureIndexes

 | 

Array<number>

 | 

No

 | 

Yes

 | 

Texture index corresponding to each coordinate.

**Start version**: 5.0.3(15)

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

NOTE:

If **customTextures** is passed in, **customTextureIndexes** must be passed. In addition, the length of the **customTextureIndexes** array must be the same as that of the **points** array, and the value of each element in the **customTextureIndexes** array must range from 0 to the length of the **customTextures** array minus 1. If the conditions are not met, error code 401 will be returned.

 |

**Example**:

let polylineOption: mapCommon.MapPolylineOptions = {
  points: \[
    { latitude: 39.693478, longitude: 116.334595 },
    { latitude: 39.593478, longitude: 116.434595 },
    { latitude: 39.593478, longitude: 116.134595}
  \],
  clickable: true,
  color: 0xff000000,
  startCap: mapCommon.CapStyle.BUTT,
  endCap: mapCommon.CapStyle.BUTT,
  geodesic: false,
  jointType: mapCommon.JointType.DEFAULT,
  patterns: \[{ type: 0, length: 100 }, { type: 0, length: 100 }, { type: 0, length: 100 }\],
  visible: true,
  width: 20,
  zIndex: 0,
  gradient: false,
  // The icon must be stored in the **resources/rawfile** directory.
  customTexture: "icon/naviline\_arrow.png",
  isTextureMappingUsed: false
};

#### BasePriorityOverlayParams

Describes the basic information about an overlay such as a Bubble or PointAnnotation. This API inherits from [BaseOverlayOptions](#section7400647135116).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

anchorU

 | 

number

 | 

No

 | 

Yes

 | 

Position of the anchor of a POI in the horizontal direction. The value ranges from 0 to 1. The default value is **0.5**. An invalid value is handled as the default value.

 |
| 

anchorV

 | 

number

 | 

No

 | 

Yes

 | 

Position of the anchor of a POI in the vertical direction. The value ranges from 0 to 1. The default value is **1**. An invalid value is handled as the default value.

 |
| 

forceVisible

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether a POI is visible after collision. The default value is **false**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

 |
| 

priority

 | 

number

 | 

No

 | 

Yes

 | 

Collision priority. A larger value indicates a lower priority. The default value is **Number.MAX\_VALUE**. An invalid value is handled as the default value.

 |
| 

minZoom

 | 

number

 | 

No

 | 

Yes

 | 

Minimum map zoom level. The default value is **2**.

Constraint: The minimum zoom level cannot be greater than the maximum zoom level and cannot be less than 2.

 |
| 

maxZoom

 | 

number

 | 

No

 | 

Yes

 | 

Maximum map zoom level. The default value is **20**.

Constraints: The maximum zoom level cannot be greater than 20 and cannot be less than the minimum zoom level.

 |

#### PointAnnotationParams

Describes the attributes of a PointAnnotation. This API inherits from [BasePriorityOverlayParams](#section20126194774515).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

position

 | 

[LatLng](#section20691173773810)

 | 

No

 | 

No

 | 

Anchor of a PointAnnotation icon. Invalid values are not processed.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

repeatable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to support deduplication when the PointAnnotation name is the same as a map POI name. The default value is **false**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

NOTE:

If the collision rule is set to [CollisionRule](#section230211714264).NONE, this parameter cannot be set.

 |
| 

collisionRule

 | 

[CollisionRule](#section230211714264)

 | 

No

 | 

Yes

 | 

Collision rule for a PointAnnotation. The default value is [CollisionRule](#section230211714264).NAME. An invalid value is handled as the default value.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

NOTE:

If this parameter is set to [CollisionRule](#section230211714264).ALL, the overlay collision priority attribute **priority** must be set.

 |
| 

titles

 | 

Array<[Text](#section132819018245)\>

 | 

No

 | 

No

 | 

Titles of a PointAnnotation. The minimum length of the array is 1 and the maximum length is 3.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

icon

 | 

string | [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | [Resource](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource)

 | 

No

 | 

Yes

 | 

Icon of a PointAnnotation. If this parameter is not passed, the default icon is used.

-   Images in JPG, JPEG, PNG, GIF, WEBP, and SVG formats are supported.
-   This input parameter of the string type supports the following formats:
    
    1\. Relative resource path: The icon is stored in **resources/rawfile**. Set **icon** to the relative path of the icon file in the **rawfile** folder.
    
    2\. toDataURL format: For example, set **icon** to **image/png;base64,<Base64-encoded byte value of the icon file>**.
    

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

NOTE:

The **icon** parameter starts to support the [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) and [Resource](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource) types since version 5.0.0(12).

 |
| 

showIcon

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to display the icon for a PointAnnotation. The default value is **true**.

-   **true**: yes
-   **false**: no

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

textPosition

 | 

[TextPosition](#section939311423718)

 | 

No

 | 

Yes

 | 

Text position of a PointAnnotation.

The default value is [TextPosition](#section939311423718).DEFAULT.

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |

**Example**:

let pointAnnotationOptions: mapCommon.PointAnnotationParams = {
  position: {
    latitude: 39.918,
    longitude: 116.397
  },
  repeatable: true,
  collisionRule: mapCommon.CollisionRule.NAME,
  titles: \[{
    content: "Title1",
    color: 0xFF000000,
    fontSize: 15,
    strokeColor: 0xFFFFFFFF,
    strokeWidth: 2,
    fontStyle: mapCommon.FontStyle.ITALIC
  }\],
  // The icon must be stored in the **resources/rawfile** directory.
  icon: "test.png",
  showIcon: true,
  anchorU: 0.5,
  anchorV: 1,
  forceVisible: false,
  priority: 3,
  minZoom: 2,
  maxZoom: 20,
  visible: true,
  zIndex: 10
};

#### BubbleParams

Describes the attributes of a Bubble. This API inherits from [BasePriorityOverlayParams](#section20126194774515).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

positions

 | 

Array<Array<[LatLng](#section20691173773810)\>>

 | 

No

 | 

No

 | 

Position of a Bubble, which is calculated by the system based on multiple position segments. Invalid values are not processed.

 |
| 

icons

 | 

Array<string | [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | [Resource](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource)\>

 | 

No

 | 

No

 | 

Bubble icon. Invalid values are not processed.

-   You must set the icons for four directions. The icons must have the same height and width.
-   Images in JPG, JPEG, PNG, GIF, WEBP, and SVG formats are supported.
-   This input parameter of the string type supports the following formats:
    -   Relative resource path: The icon is stored in **resources/rawfile**. Set **icon** to the relative path of the icon file in the **rawfile** folder.
    -   toDataURL format: For example, set **icon** to **image/png;base64,<Base64-encoded byte value of the icon file>**.

NOTE:

The **icon** parameter starts to support the [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) and [Resource](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource) types since version 5.0.0(12).

 |

**Example**:

let bubbleOptions: mapCommon.BubbleParams = {
  positions: \[\[{ latitude: 39.9, longitude: 116.4 }\]\],
  // Retrieve images in left, top, right, bottom order. The images must be stored in the **resources/rawfile** directory.
  icons: \[
    'icon1.png',
    'icon2.png',
    'icon3.png',
    'icon4.png'
  \],
  forceVisible: true,
  priority: 3,
  minZoom: 2,
  maxZoom: 20,
  visible: true,
  zIndex: 1
};

#### Text

Describes the text attributes of a PointAnnotation title.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

content

 | 

string

 | 

No

 | 

No

 | 

Title content. If the content exceeds the display limit, the overflowing portion will be replaced with an ellipsis (...).

 |
| 

color

 | 

number

 | 

No

 | 

Yes

 | 

Font color of a title. The default value is **0xFF000000** (black). The color value is in ARGB format.

 |
| 

fontSize

 | 

number

 | 

No

 | 

Yes

 | 

Font size of a title. The default value is **15**. The value ranges from 0 to 100. If a value is out of this range, the nearest boundary value is used.

 |
| 

strokeColor

 | 

number

 | 

No

 | 

Yes

 | 

Stroke color of a title. The default value is **0xFFFFFFFF** (white). The color value is in ARGB format.

 |
| 

strokeWidth

 | 

number

 | 

No

 | 

Yes

 | 

Stroke width of a title. The default value is **2**. The value ranges from 0 to 10. If a value is out of this range, the nearest boundary value is used.

 |
| 

fontStyle

 | 

[FontStyle](#section1117015922613)

 | 

No

 | 

Yes

 | 

Font style of a title. The default value is [FontStyle](#section1117015922613).REGULAR. If an invalid value is passed, the default value will be used.

 |

**Example**:

let text: mapCommon.Text = {
  content: "Nanjing Confucius Temple",
  color: 0xFF000000,
  fontSize: 15,
  strokeColor: 0xFFFFFFFF,
  strokeWidth: 2,
  fontStyle: mapCommon.FontStyle.ITALIC
};

#### Padding

Defines the padding between the map and its edges.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

left

 | 

number

 | 

No

 | 

Yes

 | 

Padding added to the left side of a map, in pixels. The default value is **0**. An invalid value is handled as the default value.

 |
| 

top

 | 

number

 | 

No

 | 

Yes

 | 

Padding added at the top of a map, in pixels. The default value is **0**. An invalid value is handled as the default value.

 |
| 

right

 | 

number

 | 

No

 | 

Yes

 | 

Padding added to the right side of a map, in pixels. The default value is **0**. An invalid value is handled as the default value.

 |
| 

bottom

 | 

number

 | 

No

 | 

Yes

 | 

Padding added at the bottom of a map, in pixels. The default value is **0**. An invalid value is handled as the default value.

 |

**Example**:

// Initialization parameters. The left padding is 0 px and the bottom padding is 50 px.
let padding: mapCommon.Padding = {
  left: 0,
  bottom: 50
};

#### VisibleRegion

Defines a VisibleRegion. A VisibleRegion contains four points that define a tetragon visible in the camera of a map. The tetragon may be a trapezoid, not necessarily a rectangle, as the camera could be tilted. If the camera is directly over the center of the visible region, the shape is rectangular. If the camera tilts, the shape will be a trapezoid whose smallest side is closest to the point of view.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

farLeft

 | 

[LatLng](#section20691173773810)

 | 

No

 | 

No

 | 

Upper left corner of the camera.

 |
| 

farRight

 | 

[LatLng](#section20691173773810)

 | 

No

 | 

No

 | 

Upper right corner of the camera.

 |
| 

bounds

 | 

[LatLngBounds](#section96341159111320)

 | 

No

 | 

No

 | 

Smallest bounding box that includes the visible region.

 |
| 

nearLeft

 | 

[LatLng](#section20691173773810)

 | 

No

 | 

No

 | 

Lower left corner of the camera.

 |
| 

nearRight

 | 

[LatLng](#section20691173773810)

 | 

No

 | 

No

 | 

Lower right corner of the camera.

 |

**Example**:

// For details about the source of **this.mapController** in the example, please refer to the sample code in [Displaying a Map](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-presenting).
let projection: map.Projection = this.mapController?.getProjection();
let visibleRegion: mapCommon.VisibleRegion = projection.getVisibleRegion();

#### MapPoint

Defines the coordinates of a point on the screen. The upper left vertex of the screen is used as the (0, 0) point. A positive value of **positionX** indicates that the visible region moves rightwards, while a negative value indicates that the visible region moves leftwards. A positive value of **positionY** indicates that the visible region moves downwards, while a negative value indicates that the visible region moves upwards.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

positionX

 | 

number

 | 

No

 | 

No

 | 

X coordinate of a point, in pixels.

 |
| 

positionY

 | 

number

 | 

No

 | 

No

 | 

Y coordinate of a point, in pixels.

 |

**Example**:

let point: mapCommon.MapPoint = {
  positionX: 100,
  positionY: 100
};

#### CustomMapStyleOptions

Defines custom style parameters.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

styleId

 | 

string

 | 

No

 | 

Yes

 | 

Custom style ID.

NOTE:

If both **styleId** and **styleContent** are passed, **styleId** takes precedence. The style ID can be created on [Petal Maps Studio](https://developer.petalmaps.com/console/studio/).

 |
| 

styleContent

 | 

string

 | 

No

 | 

Yes

 | 

Offline style content. For details about the content format, please refer to [Style Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-style#section156991344101012).

 |

**Example**:

// Replace the value of **styleId** with your own style ID. The style ID can be created on the [Petal Maps Studio](https://developer.petalmaps.com/console/studio/) platform.
let param: mapCommon.CustomMapStyleOptions = {
  styleId: "xxxxxxx"
};

#### ClusterItem

Defines a ClusterItem.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

position

 | 

[LatLng](#section20691173773810)

 | 

No

 | 

No

 | 

Coordinates of a ClusterItem to be clustered.

 |

**Example**:

let clusterItem: mapCommon.ClusterItem = {
  position: {
    latitude: 39.99,
    longitude: 116.334595
  }
};

#### ClusterOverlayParams

Defines parameters of a ClusterOverlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

clusterItems

 | 

Array<[ClusterItem](#section9436522104316)\>

 | 

No

 | 

No

 | 

Cluster item array.

 |
| 

distance

 | 

number

 | 

No

 | 

No

 | 

Clustering distance, in vp.

 |

The API provides the method described in the following table to support custom icons for ClusterItems:

| 
Return Type

 | 

Method

 |
| :-- | :-- |
| 

Promise<[image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\>

 | 

[getCustomIcon](#section252017318496)?(clusterItems: Array<[ClusterItem](#section9436522104316)\>)

This API customizes icons for ClusterItems and returns the result asynchronously through a promise.

 |

**Example**:

let clusterItem1: mapCommon.ClusterItem = {
  position: {
    latitude: 39.89,
    longitude: 116.335595
  }
};
let clusterItem2: mapCommon.ClusterItem = {
  position: {
    latitude: 39.99,
    longitude: 116.334595
  }
};
let array: Array<mapCommon.ClusterItem> = \[
  clusterItem1,
  clusterItem2
\];
let clusterOverlayParams: mapCommon.ClusterOverlayParams = { distance: 40, clusterItems: array };

#### \[h2\]getCustomIcon

getCustomIcon?(clusterItems: Array<ClusterItem>): Promise<image.PixelMap>

Customizes icons for ClusterItems. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

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

clusterItems

 | 

Array<[ClusterItem](#section9436522104316)\>

 | 

Yes

 | 

Cluster item array.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\>

 | 

Promise that returns [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md).

 |

**Example**:

// Implement the **getCustomIcon** method in **mapCommon.ClusterOverlayParams**.
import { mapCommon } from '@kit.MapKit';
import { image } from '@kit.ImageKit';

export class ClusterOverlayParamsMore implements mapCommon.ClusterOverlayParams {
  clusterItems: mapCommon.ClusterItem\[\] = new Array();
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(62, 62);
  private settings: RenderingContextSettings = new RenderingContextSettings(true);

  constructor(clusterItems: mapCommon.ClusterItem\[\], distance: number) {
    this.clusterItems = clusterItems;
    this.distance = distance;
  }

  distance: number = 0;

  // Customize a ClusterItem icon. For example, draw a circular icon with the longitude of the first ClusterItem in **clusterItems** as the text.
  async getCustomIcon(clusterItems: mapCommon.ClusterItem\[\]): Promise<image.PixelMap> {
    let offContext = this.offCanvas.getContext("2d", this.settings);

    offContext.clearRect(0, 0, 62, 62);
    // Daw a circle.
    offContext.fillStyle = 0xff990000;
    offContext.beginPath();
    offContext.arc(31, 31, 30, 0, 6.28);
    offContext.stroke();
    offContext.fill();
    offContext.save();

    // Draw text in the circle. The text is the longitude of the first item in **clusterItems**. 
    offContext.font = '20vp sans-serif';
    offContext.textAlign = 'center';
    offContext.textBaseline = 'middle';
    offContext.fillStyle = 0xffffffff;
    offContext.fillText(JSON.stringify(clusterItems\[0\].position.longitude).substring(0,3), 31, 31);
    offContext.restore();
    let iconPixelMap = offContext.getPixelMap(0, 0, 62, 62);
    return iconPixelMap;
  }
}

#### ImageOverlayParams

Defines parameters of an ImageOverlay. This API inherits from [BaseOverlayOptions](#section7400647135116).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

bounds

 | 

[LatLngBounds](#section96341159111320)

 | 

No

 | 

Yes

 | 

Position of an ImageOverlay based on the specified rectangle. Either **position** or **bounds** must be set. When both parameters are set, **bounds** has a higher priority. When **position** is used, **width** is mandatory.

 |
| 

position

 | 

[LatLng](#section20691173773810)

 | 

No

 | 

Yes

 | 

Position of an ImageOverlay. Either **position** or **bounds** must be set. When both parameters are set, **bounds** has a higher priority. When **position** is used, **width** is mandatory.

 |
| 

width

 | 

number

 | 

No

 | 

Yes

 | 

Width of an ImageOverlay, in meters. This parameter is valid only when **position** is specified. The value of this parameter must be a positive integer.

 |
| 

height

 | 

number

 | 

No

 | 

Yes

 | 

Height of an ImageOverlay, in meters. This parameter is valid only when **position** and **width** are specified. The value of this parameter must be a positive integer.

 |
| 

anchorU

 | 

number

 | 

No

 | 

Yes

 | 

Position of the anchor of an ImageOverlay in the horizontal direction. The value ranges from 0 to 1. The default value is **0.5**.

NOTE:

When **bounds** is specified, the value of **anchorU** changes the position of the anchor of the ImageOverlay in the horizontal direction, but does not change the range specified by **bounds**.

 |
| 

anchorV

 | 

number

 | 

No

 | 

Yes

 | 

Position of the anchor of an ImageOverlay in the vertical direction. The value ranges from 0 to 1. The default value is **0.5**.

NOTE:

When **bounds** is specified, the value of **anchorV** changes the position of the anchor of the ImageOverlay in the vertical direction, but does not change the range specified by **bounds**.

 |
| 

bearing

 | 

number

 | 

No

 | 

Yes

 | 

Rotation angle of an ImageOverlay.

0 degrees is due north, and angles increase clockwise. The value range is \[0, 360). The default value is **0**. Values that fall outside the valid range will be adjusted to values within the range. For instance, the value **361** would be converted to **1**, and the value **\-1** would be converted to **359**.

 |
| 

clickable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether an ImageOverlay is clickable.

-   **true**: yes
-   **false**: no

The default value is **false**.

 |
| 

image

 | 

[ResourceStr](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr) | [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

No

 | 

No

 | 

Image of an ImageOverlay.

Images in JPG, JPEG, PNG, GIF, WEBP, and SVG formats are supported.

NOTE:

[ResourceStr](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr) indicates either resource type or string type. Input parameters of the string type can be in either of the following formats:

-   Relative resource path: The image is stored in **resources/rawfile**. Set **image** to the relative path of the image file in the **rawfile** folder.
-   toDataURL format: For example, set **image** to **image/png;base64,<Base64-encoded byte value of the image file>**.

 |
| 

transparency

 | 

number

 | 

No

 | 

Yes

 | 

Transparency of an ImageOverlay.

The value ranges from 0 to 1.

The value **1** indicates completely transparent, and the value **0** indicates completely opaque.

The default value is **0**.

 |

**Example**:

let imageOverlayParams: mapCommon.ImageOverlayParams = {
  bounds: { southwest: { latitude: 32, longitude: 118 }, northeast: { latitude: 32.4, longitude: 118.4 } },
  // The icon must be stored in the **resources/rawfile** directory.
  image: 'icon/icon.png',
  transparency: 0.3,
  zIndex: 101,
  anchorU: 0.5,
  anchorV: 0.5,
  clickable: true,
  visible: true,
  bearing: 90
};

#### BuildingOverlayParams

Defines BuildingOverlay parameters.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

points

 | 

Array<[LatLng](#section20691173773810)\>

 | 

No

 | 

No

 | 

Coordinate set of a BuildingOverlay's base.

The coordinate points can be connected clockwise to form a plane. At least three coordinate points are required.

 |
| 

totalHeight

 | 

number

 | 

No

 | 

No

 | 

Height of a BuildingOverlay from the ground, in meters.

The maximum height is 30,000 meters.

 |
| 

floorBottomHeight

 | 

number

 | 

No

 | 

No

 | 

Height from the bottom of a selected floor to the ground, in meters.

 |
| 

topFaceColor

 | 

number

 | 

No

 | 

Yes

 | 

Color of a BuildingOverlay's rooftop. The value is in ARGB format.

The default value is **0xffff0000** (red).

 |
| 

sideFaceColor

 | 

number

 | 

No

 | 

Yes

 | 

Color of a BuildingOverlay's lateral surface. The value is in ARGB format.

The default value is **0xffff0000** (red).

 |
| 

floorColor

 | 

number

 | 

No

 | 

Yes

 | 

Color of the top of a selected floor. The value is in ARGB format.

The default value is **0xffff0000** (red).

 |
| 

showLevel

 | 

number

 | 

No

 | 

Yes

 | 

Floor from which a BuildingOverlay starts to be displayed. The value ranges from 2 to 20. The default value is **15**. If the value is out of the range, the default value is used.

 |
| 

animationDuration

 | 

number

 | 

No

 | 

Yes

 | 

Animation duration, in milliseconds. The value must be greater than or equal to 100. The default value is **0**. If the value is out of the range, the default value is used.

 |
| 

sideTexture

 | 

[BuildingTexture](#section16452081559)

 | 

No

 | 

Yes

 | 

Texture of a BuildingOverlay's lateral surface.

 |
| 

floorTexture

 | 

[BuildingTexture](#section16452081559)

 | 

No

 | 

Yes

 | 

Texture of a selected floor.

 |

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
  };

#### BuildingTexture

Defines the building texture.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

image

 | 

[ResourceStr](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr) | [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

No

 | 

No

 | 

Texture image.

Images in JPG, JPEG, PNG, GIF, WEBP, and SVG formats are supported.

NOTE:

[ResourceStr](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr) indicates either resource type or string type. Input parameters of the string type can be in either of the following formats:

-   Relative resource path: The image is stored in **resources/rawfile**. Set **image** to the relative path of the image file in the **rawfile** folder.
-   toDataURL format: For example, set **image** to **image/png;base64,<Base64-encoded byte value of the image file>**.

 |
| 

width

 | 

number

 | 

No

 | 

Yes

 | 

Texture width, in meters. The value must be greater than or equal to 0. The default value is **3**. An invalid value is handled as the default value.

 |
| 

height

 | 

number

 | 

No

 | 

Yes

 | 

Texture height, in meters. The value must be greater than or equal to 0. The default value is **3**. An invalid value is handled as the default value.

 |

**Example**:

let buildingTexture: mapCommon.BuildingTexture = {
  image: $r("app.media.floor\_tex"),
  height: 10,
  width: 10
};

#### TraceOverlayParams

Defines the attributes of a TraceOverlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

points

 | 

Array<[LatLng](#section20691173773810)\>

 | 

No

 | 

No

 | 

Trajectory point.

The maximum number of points is 100,000.

 |
| 

width

 | 

number

 | 

No

 | 

Yes

 | 

TraceOverlay width, in pixels.

The default value is **10**.

The value ranges from 0 to 512. If a value greater than 512 is passed, the value **512** will be used.

 |
| 

color

 | 

number

 | 

No

 | 

Yes

 | 

TraceOverlay color. The color value is in ARGB format.

The default value is **0xaaff0000**.

 |
| 

isMapMoving

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the map pans with the TraceOverlay.

-   **true**: yes
-   **false**: no

The default value is **false**.

 |
| 

animationDuration

 | 

number

 | 

No

 | 

Yes

 | 

Duration of the TraceOverlay animation, in milliseconds. The minimum value is **100**.

The default value is **5000**.

NOTE:

If this parameter is set to a value less than 100, the default value **5000** will be used.

 |
| 

animationCallback

 | 

Callback<number>

 | 

No

 | 

Yes

 | 

Listens for the TraceOverlay position. Point indexes will be returned.

 |

**Example**:

// For details about the source of **this.mapController** in the example, please refer to the sample code in [Displaying a Map](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-presenting).
// Parameters of Marker1. 
let markerOptions1: mapCommon.MarkerOptions = {
  position: {
    latitude: 31.99227173519985,
    longitude: 118.7622219990476
  },
  // The icon must be stored in the **resources/base/media** directory.
  icon: $r("app.media.track\_setting\_sport\_map\_marker\_22"),
  anchorU: 0.5,
  anchorV: 1,
  visible: true
};
// Add Marker 1. 
let markerBoy1 = await this.mapController.addMarker(markerOptions1);
let boyImages1: map.PlayImageAnimation = new map.PlayImageAnimation();
boyImages1.setDuration(1000);
let resourceArray: Array<Resource> = new Array();
resourceArray.push($r("app.media.side\_0"));
resourceArray.push($r("app.media.side\_1"));
resourceArray.push($r("app.media.side\_2"));
resourceArray.push($r("app.media.side\_3"));
resourceArray.push($r("app.media.side\_4"));
resourceArray.push($r("app.media.side\_5"));
resourceArray.push($r("app.media.side\_6"));
resourceArray.push($r("app.media.side\_7"));
resourceArray.push($r("app.media.side\_8"));
resourceArray.push($r("app.media.side\_9"));
resourceArray.push($r("app.media.side\_10"));
resourceArray.push($r("app.media.side\_11"));
resourceArray.push($r("app.media.side\_12"));
resourceArray.push($r("app.media.side\_13"));
resourceArray.push($r("app.media.side\_14"));
resourceArray.push($r("app.media.side\_15"));
resourceArray.push($r("app.media.side\_16"));
resourceArray.push($r("app.media.side\_17"));
resourceArray.push($r("app.media.side\_18"));
resourceArray.push($r("app.media.side\_19"));
resourceArray.push($r("app.media.side\_20"));
await boyImages1.addImages(resourceArray);
boyImages1.setRepeatCount(-1);

// Add an animation for Marker 1. 
markerBoy1.setAnimation(boyImages1);
markerBoy1.startAnimation();

// Parameters of Marker 2. 
let markerOptions2: mapCommon.MarkerOptions = {
  position: {
    latitude: 31.99227173519985,
    longitude: 118.7622219990476
  },
  // The icon must be stored in the **resources/base/media** directory.
  icon: $r("app.media.track\_setting\_sport\_map\_marker\_22"),
  anchorU: 0.5,
  anchorV: 1,
  visible: false
};
// Add Marker 2.
let markerBoy2 = await this.mapController.addMarker(markerOptions2);
let boyImages2: map.PlayImageAnimation = new map.PlayImageAnimation();
boyImages2.setDuration(1000);
let resourceArray2: Array<Resource> = new Array();
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_000"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_001"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_002"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_003"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_004"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_005"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_006"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_007"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_008"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_009"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_010"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_011"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_012"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_013"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_014"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_015"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_016"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_017"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_018"));
await boyImages2.addImages(resourceArray2);
boyImages2.setRepeatCount(-1);
// Add an animation for Marker 2. 
markerBoy2.setAnimation(boyImages2);
markerBoy2.startAnimation();

let points: Array<mapCommon.LatLng> = new Array();
points.push({ latitude: 31.99685233070878, longitude: 118.75846023442728 });
points.push({ latitude: 31.99671325810786, longitude: 118.75846738985165 });
points.push({ latitude: 31.99659191076709, longitude: 118.7585347621686 });
points.push({ latitude: 31.99648202537233, longitude: 118.7586266510386 });
points.push({ latitude: 31.99637707201552, longitude: 118.75872004590596 });
points.push({ latitude: 31.996278207010903, longitude: 118.75880449946251 });
points.push({ latitude: 31.996187481969695, longitude: 118.7588781960278 });
points.push({ latitude: 31.996092248919354, longitude: 118.75895330554488 });
points.push({ latitude: 31.995962740450565, longitude: 118.75904721407304 });
points.push({ latitude: 31.995792921394, longitude: 118.75916904998051 });
points.push({ latitude: 31.995601885713416, longitude: 118.7593235241019 });
points.push({ latitude: 31.995398221178277, longitude: 118.75949998588176 });
points.push({ latitude: 31.995185902197715, longitude: 118.7596871082939 });
points.push({ latitude: 31.994983473052656, longitude: 118.75987334062296 });
points.push({ latitude: 31.99482433699269, longitude: 118.76002095184032 });
points.push({ latitude: 31.994709073721708, longitude: 118.76012902920532 });
points.push({ latitude: 31.99460732100702, longitude: 118.76023892576234 });
points.push({ latitude: 31.99449284962087, longitude: 118.7603694232856 });
points.push({ latitude: 31.99435358179254, longitude: 118.76053622438056 });
points.push({ latitude: 31.99420771148339, longitude: 118.76072790126692 });
points.push({ latitude: 31.994075194901523, longitude: 118.7609100960977 });
points.push({ latitude: 31.993952686158877, longitude: 118.7610741329013 });
points.push({ latitude: 31.993840180644217, longitude: 118.7612193418965 });
points.push({ latitude: 31.993733787150244, longitude: 118.76135383115654 });
points.push({ latitude: 31.993617206525155, longitude: 118.76150529647698 });

// Input parameters of the TraceOverlay. 
let traceOptions: mapCommon.TraceOverlayParams = {
  // Trajectory points. 
  points: points,
  // TraceOverlay animation duration. 
  animationDuration: 5000,
  // Whether the camera follows the animation path.
  isMapMoving: true,
  // TraceOverlay color. 
  color: 0xAAFFAA00,
  // TraceOverlay width.
  width: 20,
  // TraceOverlay animation callback (using the trajectory point index).
  animationCallback: (pointIndex) => {
    // Change to cycling.
    if (pointIndex === 10) {
      markerBoy1.setVisible(false);
      markerBoy2.setVisible(true);
    }
  }
};
let markers: Array<map.Marker> = new Array();
markers.push(markerBoy1, markerBoy2);
// Add a trajectory point animation.
let traceOverlay = await this.mapController.addTraceOverlay(traceOptions, markers);

#### MapArcParams

Defines the attributes of a MapArc. This API inherits from [BaseOverlayOptions](#section7400647135116).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

startPoint

 | 

[LatLng](#section20691173773810)

 | 

No

 | 

No

 | 

Start point.

 |
| 

centerPoint

 | 

[LatLng](#section20691173773810)

 | 

No

 | 

No

 | 

Center point.

 |
| 

endPoint

 | 

[LatLng](#section20691173773810)

 | 

No

 | 

No

 | 

End point.

 |
| 

color

 | 

number

 | 

No

 | 

Yes

 | 

Color of a MapArc. The default value is **0xFFFFFFFF** (white). The color value is in ARGB format. An invalid value is handled as the default value.

 |
| 

width

 | 

number

 | 

No

 | 

Yes

 | 

Width of a MapArc, in pixels. The value must be greater than or equal to 0. The default value is **10**. An invalid value is handled as the default value.

 |

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

#### CoordinateLatLng

Specifies the coordinate system and coordinates.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

coordinateType

 | 

[CoordinateType](#section78948324526)

 | 

No

 | 

No

 | 

Coordinate system.

 |
| 

location

 | 

[LatLng](#section20691173773810)

 | 

No

 | 

No

 | 

Coordinates.

 |

**Example**:

let location: mapCommon.CoordinateLatLng = {
  coordinateType: mapCommon.CoordinateType.GCJ02,
  location: { latitude: 31.984410259206815, longitude: 118.76625379397866 }
};

#### TileOverlayParams

TileOverlay parameters. This API inherits from [BaseOverlayOptions](#section7400647135116).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.3(15)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

tileUrl

 | 

string

 | 

No

 | 

No

 | 

URL of a TileOverlay.

It must start with **http** or **https** and contain placeholders {x}, {y}, and {z}.

 |
| 

transparency

 | 

number

 | 

No

 | 

Yes

 | 

Transparency of a TileOverlay.

The value ranges from 0 to 1. The value **1** indicates completely transparent, and the value **0** indicates completely opaque.

The default value is **0**.

 |
| 

fadeIn

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable TileOverlay fade-in.

-   **true**: yes
-   **false**: no

The default value is **true**.

 |

**Example**:

let params: mapCommon.TileOverlayParams = {
  // Set the URL of the TileOverlay, which must start with **http** or **https** and contain placeholders {x}, {y}, and {z}.
  tileUrl: "https://xxx/xxx?x={x}&y={y}&z={z}",
  transparency: 0,
  fadeIn: false
};

#### TileOverlayOptions

TileOverlay parameters. This API inherits from [BaseOverlayOptions](#section7400647135116).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

tileUrl

 | 

string

 | 

No

 | 

Yes

 | 

URL of a TileOverlay.

It must start with **http** or **https** and contain placeholders {x}, {y}, and {z}.

 |
| 

tileProvider

 | 

[TileProvider](#section1574174915920)

 | 

No

 | 

Yes

 | 

Obtains a TileOverlay based on the coordinates.

 |
| 

transparency

 | 

number

 | 

No

 | 

Yes

 | 

Transparency of a TileOverlay.

The value ranges from 0 to 1. The value **1** indicates completely transparent, and the value **0** indicates completely opaque.

The default value is **0**.

 |
| 

fadeIn

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable TileOverlay fade-in.

-   **true**: yes
-   **false**: no

The default value is **true**.

 |
| 

diskCacheEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable disk caching.

-   **true**: yes
-   **false**: false

The default value is **false**.

 |
| 

diskCacheSize

 | 

number

 | 

No

 | 

Yes

 | 

Disk cache size, in KB. The default value is **20480**.

 |
| 

diskCachePath

 | 

string

 | 

No

 | 

Yes

 | 

Disk cache path. This parameter is mandatory if disk caching is enabled.

 |

**Example**:

let params: mapCommon.TileOverlayOptions = {
  // Set the URL of the TileOverlay, which must start with **http** or **https** and contain placeholders {x}, {y}, and {z}.
  tileUrl: "https://xxx/xxx?x={x}&y={y}&z={z}",
  diskCacheEnabled: true,
  diskCacheSize: 20480,
  diskCachePath: '/data/storage/el2/database'
};

#### HeatmapParams

Heatmap parameters.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

id

 | 

string

 | 

No

 | 

No

 | 

Heatmap ID.

 |
| 

data

 | 

[WeightedLatLng](#section14151459134817)\[\]

 | 

No

 | 

No

 | 

Heatmap data (it is recommended that the number of heatmap data records be less than 10,000).

 |
| 

color

 | 

Record<number, number>

 | 

No

 | 

Yes

 | 

Heatmap color, in ARGB format. The parameter value is in a key-value format. The key indicates the data density (value range: \[0,1\]), and the value indicates the color in ARGB format. Default values: { 0: 0x00026C39, 0.15: 0xAA138C4A, 0.3: 0xFF82CB67, 0.45: 0xFFE3F399, 0.6: 0xFFFEDE89, 0.75: 0xFFF67C4A, 0.9: 0xFFBE1827, 1: 0xFFA90426 }

If the key of a record is out of the valid range or the value is in an incorrect format, the record is removed. If no records are valid, the default value will be used.

 |
| 

intensity

 | 

number | Record<number, number>

 | 

No

 | 

Yes

 | 

Heatmap Intensity. You can configure the intensity by level. The parameter value can be in a key-value format, where the key indicates the level and the value indicates the intensity. If the **intensity** value is a number, the same intensity is used for all levels.

If a value less than or equal to 0 is passed, the default value **1** is used.

 |
| 

opacity

 | 

number | Record<number, number>

 | 

No

 | 

Yes

 | 

Heatmap opacity. The value ranges from 0 to 1. The value **1** indicates completely transparent, and the value **0** indicates completely opaque. For values less than 0, the value **0** is used; for values greater than 1, the value **1** is used. If the opacity is a number, the same opacity is used for all levels. The default value is **0**.

 |
| 

radius

 | 

number | Record<number, number>

 | 

No

 | 

Yes

 | 

Heatmap radius. You can configure the radius by level. The parameter value can be in a key-value format, where the key indicates the level and the value indicates the radius. If the **radius** value is a number, the same radius is used for all levels. The default value is **10**. The default unit is [RadiusUnit](#section117031317134216).PIXEL\_UNIT.

 |
| 

radiusUnit

 | 

[RadiusUnit](#section117031317134216)

 | 

No

 | 

Yes

 | 

Radius unit. The default value is [RadiusUnit](#section117031317134216).PIXEL\_UNIT.

 |
| 

visible

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the heatmap is visible. The default value is **true**.

-   **true**: yes
-   **false**: no

 |

#### RadiusUnit

Radius unit.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

PIXEL\_UNIT

 | 

0

 | 

Pixel.

 |
| 

METER\_UNIT

 | 

1

 | 

Meter.

 |

#### WeightedLatLng

Weighted longitude and latitude.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

point

 | 

[LatLng](#section20691173773810)

 | 

No

 | 

No

 | 

Longitude and latitude.

 |
| 

intensity

 | 

number

 | 

No

 | 

Yes

 | 

Weight of the intensity. The value range is \[0,+∞). The default value is **1**. If an invalid value is passed, the default value will be used.

 |

#### TileProvider

type TileProvider = (x: number, y: number, z: number) => Promise<ArrayBuffer>

Obtains a TileOverlay based on the coordinates.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

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

x

 | 

number

 | 

Yes

 | 

X coordinate.

 |
| 

y

 | 

number

 | 

Yes

 | 

Y-coordinate.

 |
| 

z

 | 

number

 | 

Yes

 | 

Z coordinate.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<ArrayBuffer>

 | 

Promise that returns the TileOverlay.

 |

#### MvtOverlayParams

MvtOverlay parameters. This API inherits from [BaseOverlayOptions](#section7400647135116).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core.EnhancedOverlay

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

source

 | 

[MvtSource](#section877213310341)

 | 

No

 | 

No

 | 

Source of the MvtOverlay.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

 |
| 

layers

 | 

[MvtLayer](#section14599124818)\[\]

 | 

No

 | 

No

 | 

Style array. It is recommended that the number of vector layers be less than 2000 to ensure smoothness of the MvtOverlay.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

 |
| 

blurIntensity

 | 

number | Record<number, number>

 | 

No

 | 

Yes

 | 

Blur intensity of the MvtOverlay. This parameter does not take effect for the 3D globe view.

The blur intensity ranges from 0 to 20. The decimal part is rounded down. The default value is **0**. If an invalid value is passed, the default value will be used.

If the **blurIntensity** value is a number, the same intensity is used for all zoom levels.

If the **blurIntensity** value is key-value pairs, the key indicates the zoom level and the value indicates the blur intensity. The valid level range is \[2, 20\]. For a level value outside of this range, the nearest boundary value will be used. For example, the value **{ 5: 5, 10: 8, 18: 15 }** indicates that the blur intensity is 0 (no blur) for levels 2–4, 5 for levels 5–9, 8 for levels 10–17, and 15 for levels 18–20.

**Start version**: 6.0.2(22)

**Atomic service API**: This API can be used in atomic services since API version 6.0.2(22).

 |

#### MvtSource

Source of the MvtOverlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core.EnhancedOverlay

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

tileUrl

 | 

string

 | 

No

 | 

Yes

 | 

URL for downloading MvtOverlay data. It must contain placeholders {x}, {y}, and {z}.

NOTE:

To add an MvtOverlay using an online resource (via the **tileUrl** method), you must apply for the network access permission **ohos.permission.INTERNET**.

 |
| 

tileProvider

 | 

[TileProvider](#section1574174915920)

 | 

No

 | 

Yes

 | 

Obtains a TileOverlay based on the coordinates.

 |
| 

minZoom

 | 

number

 | 

No

 | 

Yes

 | 

Minimum zoom level. The default value is **2**.

 |
| 

maxZoom

 | 

number

 | 

No

 | 

Yes

 | 

Maximum zoom level. The default value is **20**.

 |

#### MvtLayer

Style array, which is used to configure the style.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core.EnhancedOverlay

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

id

 | 

string

 | 

No

 | 

No

 | 

Unique ID, which is used to add, update, or remove an MvtOverlay.

 |
| 

type

 | 

[MvtLayerType](#section11385518298)

 | 

No

 | 

No

 | 

MvtOverlay type.

 |
| 

sourceLayer

 | 

string

 | 

No

 | 

No

 | 

MvtOverlay name.

 |
| 

paint

 | 

[MvtPaint](#section1546292610511)

 | 

No

 | 

Yes

 | 

Configures the rendering of a geometry, such as its fill and stroke.

 |

#### MvtPaint

Configures the rendering of a geometry, such as its fill and stroke.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core.EnhancedOverlay

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

fillColor

 | 

number | [Expression](#section139149121817)

 | 

No

 | 

Yes

 | 

Fill color. The default value is **0x000000**. If an invalid value is passed, the default value will be used. The value:

-   Must be in hexadecimal RGB format.
-   Can be obtained from an MvtOverlay's attributes.

 |
| 

fillOpacity

 | 

number | [Expression](#section139149121817)

 | 

No

 | 

Yes

 | 

Fill opacity. The default value is **0**. If an invalid value is passed, the default value will be used. The value:

-   Must range from 0 to 1.
-   Can be obtained from an MvtOverlay's attributes.

 |

#### MvtLayerType

MvtOverlay type.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core.EnhancedOverlay

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

FILL

 | 

'fill'

 | 

Filled polygon.

 |

#### Expression

Overlay expression of an MvtOverlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core.EnhancedOverlay

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

operator

 | 

[Operator](#section1745405383014)

 | 

No

 | 

No

 | 

Operator.

 |
| 

args

 | 

string | string\[\] | [Expression](#section139149121817)\[\]

 | 

No

 | 

No

 | 

Arguments.

NOTE:

The string\[\] and [Expression](#section139149121817)\[\] types are reserved for future use.

 |

#### Operator

Operator.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core.EnhancedOverlay

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

GET

 | 

'get'

 | 

GET operator.

 |

#### FlowFieldOverlayParams

FlowFieldOverlay parameters. This API inherits from [BaseOverlayOptions](#section7400647135116).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core.EnhancedOverlay

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

data

 | 

string

 | 

No

 | 

No

 | 

FlowFieldOverlay data. For details about the data format, please refer to [Flow Field Data Format Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-flow-field#section138174613135).

 |
| 

style

 | 

[ParticleStyle](#section1666151282917)

 | 

No

 | 

Yes

 | 

Particle style.

 |

#### ParticleStyle

Particle style.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core.EnhancedOverlay

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

count

 | 

number

 | 

No

 | 

Yes

 | 

Number of particles. The default value is **2000**. If an invalid value is passed, the default value will be used. It is recommended that the value be less than 10,000.

 |
| 

color

 | 

number

 | 

No

 | 

Yes

 | 

Particle color, in ARGB format. The default value is **0xffff69b4**. If an invalid value is passed, the default value will be used.

 |
| 

maxSpeed

 | 

number

 | 

No

 | 

Yes

 | 

Maximum speed of a particle, in m/s. The default value is **70**. It is recommended that the value be less than 255. If an invalid value is passed, the default value will be used.

 |
| 

speedFactor

 | 

number

 | 

No

 | 

Yes

 | 

Speed factor of a particle. The value ranges from 0 to 1. The default value is **0.2**. If an invalid value is passed, the default value will be used.

 |

#### MassPointItem

Mass point list.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

itemId

 | 

string

 | 

No

 | 

No

 | 

Unique ID of a mass point.

 |
| 

position

 | 

[LatLng](#section20691173773810)

 | 

No

 | 

No

 | 

Longitude-latitude coordinates of a mass point.

 |
| 

title

 | 

string

 | 

No

 | 

Yes

 | 

Title.

 |
| 

snippet

 | 

string

 | 

No

 | 

Yes

 | 

Content associated with a mass point.

 |

#### MassPointOverlayParams

MassPointOverlay parameters.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

id

 | 

string

 | 

No

 | 

No

 | 

Unique ID of a MassPointOverlay.

 |
| 

items

 | 

[MassPointItem](#section17837254174411)\[\]

 | 

No

 | 

No

 | 

Mass point list (it is recommended that the number of mass points be less than 100,000).

 |
| 

icon

 | 

[ResourceStr](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr) | [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

No

 | 

No

 | 

Mass point icon.

 |
| 

anchorU

 | 

number

 | 

No

 | 

Yes

 | 

Horizontal position of an icon anchor. The value ranges from 0 to 1. The default value is **0.5**.

 |
| 

anchorV

 | 

number

 | 

No

 | 

Yes

 | 

Vertical position of an icon anchor. The value ranges from 0 to 1. The default value is **0.5**.

 |

#### MapType

Defines the map type.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

STANDARD

 | 

0

 | 

Standard map, which displays roads, buildings, and major natural features such as rivers.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

NONE

 | 

1

 | 

Empty map without any data loaded.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

TERRAIN

 | 

2

 | 

Topographic map, which is a standard map that provides a comprehensive and detailed representation of terrain features, while still retaining other map elements such as administrative division boundaries, POIs, and buildings.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

NOTE:

-   The terrain effect is only visible at a zoom level greater than 5 and less than 14.
-   The terrain effect is not available on smart watches.

 |
| 

SATELLITE

 | 

3

 | 

Satellite map, which shows satellite imagery. It is available only in China.

**Start version**: 6.0.0(20)

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

 |
| 

HYBRID

 | 

4

 | 

Hybrid map, which displays both satellite imagery and road network information.

**Start version**: 6.0.0(20)

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

 |

#### PatternItemType

Describes the stroke pattern of a MapPolyline or the outline of a MapPolygon or MapCircle.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

DASH

 | 

0

 | 

The MapPolyline, MapPolygon, and MapCircle are displayed with a dashed line style.

 |
| 

DOT

 | 

1

 | 

The MapPolyline, MapPolygon, and MapCircle are displayed with a dotted line style.

 |
| 

GAP

 | 

2

 | 

The MapPolyline, MapPolygon, and MapCircle are displayed with a gapped line style.

 |

#### JointType

Describes the joint type of a MapPolyline or MapPolygon.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

DEFAULT

 | 

0

 | 

A miter is used to connect line segments.

 |
| 

BEVEL

 | 

1

 | 

A bevel is used to connect line segments.

 |
| 

ROUND

 | 

2

 | 

A round is used to connect line segments.

 |

#### LogoAlignment

Defines the map logo alignment mode.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

BOTTOM\_START

 | 

0

 | 

The map logo is placed in the lower left corner.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

BOTTOM\_END

 | 

1

 | 

The map logo is placed in the lower right corner.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

TOP\_START

 | 

2

 | 

The map logo is placed in the upper left corner.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

TOP\_END

 | 

3

 | 

The map logo is placed in the upper right corner.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

TOP\_CENTER

 | 

4

 | 

The map logo is placed at the top center.

**Start version**: 5.1.1(19)

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

 |
| 

BOTTOM\_CENTER

 | 

5

 | 

The map logo is placed at the bottom center.

**Start version**: 5.1.1(19)

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

 |

#### CapStyle

Customizes the start vertex and end vertex style of a MapPolyline.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

BUTT

 | 

0

 | 

The two ends of the line are parallel lines.

 |
| 

ROUND

 | 

1

 | 

The two ends of the line are extended by a half circle.

 |
| 

SQUARE

 | 

2

 | 

The two ends of the line are extended by a rectangle.

 |

#### CollisionRule

Describes the rules of collision between map POIs.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

NONE

 | 

0

 | 

Neither names nor icons are involved in the collision.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

NAME

 | 

1

 | 

Only names are involved in the collision.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

ALL

 | 

2

 | 

Both icons and names are involved in the collision.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |

#### FontStyle

Describes the font style of a PointAnnotation title.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

REGULAR

 | 

0

 | 

Regular.

 |
| 

BOLD

 | 

1

 | 

Bold.

 |
| 

ITALIC

 | 

2

 | 

Italic.

 |
| 

BOLD\_ITALIC

 | 

3

 | 

Italic and bold.

 |
| 

MEDIUM

 | 

4

 | 

Medium.

 |
| 

MEDIUM\_ITALIC

 | 

5

 | 

Medium and italic.

 |

#### CoordinateType

Defines the coordinate system type.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

WGS84

 | 

0

 | 

WGS84 coordinate system.

 |
| 

GCJ02

 | 

1

 | 

GCJ02 coordinate system.

 |

#### MyLocationDisplayType

Defines the display mode of the my-location icon.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

DEFAULT

 | 

0

 | 

Continuous location is performed. The camera does not move to my location, and the location blue dot follows the device's movement.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

LOCATE

 | 

1

 | 

A single location is performed and the camera is moved to the center of the map.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

FOLLOW

 | 

2

 | 

Continuous location is performed. The camera is moved to the center of the map, and the location blue dot follows the device's movement.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

FOLLOW\_ROTATE

 | 

3

 | 

Continuous location is performed. The camera is moved to the center of the map, and the location blue dot rotates according to the device direction and follows the device's movement.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

NOTE:

To use the value **FOLLOW\_ROTATE**, your app needs to apply for the sensor permission **ohos.permission.ACCELEROMETER**.

 |
| 

TRACK\_ROTATE

 | 

4

 | 

Continuous location is performed. The location icon follows the movement of the device and rotates according to the device direction, but will not move to the center of the map.

**Start version**: 6.0.0(20)

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

NOTE:

To use the value **FOLLOW\_ROTATE**, your app needs to apply for the sensor permission **ohos.permission.ACCELEROMETER**.

 |

#### DayNightMode

Defines the day/dark mode of a map.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

DAY

 | 

0

 | 

Day mode.

 |
| 

NIGHT

 | 

1

 | 

Dark mode.

 |
| 

AUTO

 | 

2

 | 

Automatic mode. If the system's dark mode is enabled, the dark mode is used; otherwise, the day mode is used.

 |

#### ScaleUnit

Defines the map scale unit.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

METRIC\_UNIT

 | 

0

 | 

Metric unit.

 |
| 

IMPERIAL\_UNIT

 | 

1

 | 

Imperial unit.

 |

#### TextPosition

Sets the text position of a PointAnnotation.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

DEFAULT

 | 

0

 | 

Default mode.

 |
| 

TOP

 | 

1

 | 

The text is displayed above the icon.

 |
| 

BOTTOM

 | 

2

 | 

The text is displayed below the icon.

 |
| 

LEFT

 | 

3

 | 

The text is displayed to the left of the icon.

 |
| 

RIGHT

 | 

4

 | 

The text is displayed to the right of the icon.

 |

#### MapElementType

Defines map element types.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

OVERLAY

 | 

1

 | 

Overlay, including the [MapCircle](../map-map-display/mapcircle/document.md), [MapPolygon](../map-map-display/mappolygon/document.md), [MapPolyline](../map-map-display/mappolyline/document.md), [MapArc](../map-map-display/maparc/document.md), [ImageOverlay](../map-map-display/imageoverlay/document.md), and [TraceOverlay](../map-map-display/traceoverlay/document.md).

 |
| 

POI

 | 

2

 | 

Base map [POI](#section1155919456273).

 |
| 

CUSTOM\_POI

 | 

3

 | 

Overlay that supports collision, including the [PointAnnotation](../map-map-display/pointannotation/document.md) and [Bubble](../map-map-display/bubble/document.md).

 |
| 

MARKER

 | 

4

 | 

Marker, including the [Marker](../map-map-display/marker/document.md) and [ClusterOverlay](../map-map-display/clusteroverlay/document.md).

 |
