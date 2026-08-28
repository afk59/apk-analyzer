# staticMap (Static Map)

This module provides APIs for obtaining a static map.

**Start version**: 4.1.0(11)

#### Module Import

import { staticMap } from '@kit.MapKit';

#### getMapImage

getMapImage(options: StaticMapOptions): Promise<image.PixelMap>

Creates a static map based on the provided parameters. This API returns the result asynchronously through a promise.

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

options

 | 

[StaticMapOptions](#section1555293218278)

 | 

Yes

 | 

Static map parameters.

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

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

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
| 

1002600001

 | 

System internal error.

 |
| 

1002600002

 | 

Failed to connect to the Map Kit server.

 |
| 

1002600003

 | 

App authentication failed.

 |
| 

1002600004

 | 

The Map permission is not enabled.

 |
| 

1002600005

 | 

The network is unavailable.

 |
| 

1002600006

 | 

The API call times exceed the quota.

 |
| 

1002600007

 | 

The API QPS exceeds the quota.

 |
| 

1002600008

 | 

The API is in arrears.

 |
| 

1002600009

 | 

The API has not subscribed to any pay-as-you-go package.

 |
| 

1002600010

 | 

The server is busy. Please wait and try again.

 |

**Example**:

let staticMapOptions: staticMap.StaticMapOptions = {
  location: {
    latitude: 39.9,
    longitude: 116.4
  },
  zoom: 3,
  imageWidth: 10,
  imageHeight: 10
};
await staticMap.getMapImage(staticMapOptions);

#### getMapImage

getMapImage(context: common.Context, options: StaticMapOptions): Promise<image.PixelMap>

Creates a static map based on the provided parameters. The context can be passed. This API returns the result asynchronously through a promise.

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

context

 | 

[common.Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

Context.

 |
| 

options

 | 

[StaticMapOptions](#section1555293218278)

 | 

Yes

 | 

Static map parameters.

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

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

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
| 

1002600001

 | 

System internal error.

 |
| 

1002600002

 | 

Failed to connect to the Map Kit server.

 |
| 

1002600003

 | 

App authentication failed.

 |
| 

1002600004

 | 

The Map permission is not enabled.

 |
| 

1002600005

 | 

The network is unavailable.

 |
| 

1002600006

 | 

The API call times exceed the quota.

 |
| 

1002600007

 | 

The API QPS exceeds the quota.

 |
| 

1002600008

 | 

The API is in arrears.

 |
| 

1002600009

 | 

The API has not subscribed to any pay-as-you-go package.

 |
| 

1002600010

 | 

The server is busy. Please wait and try again.

 |

**Example**:

let staticMapOptions: staticMap.StaticMapOptions = {
  location: {
    latitude: 39.9,
    longitude: 116.4
  },
  zoom: 3,
  imageWidth: 10,
  imageHeight: 10
};
await staticMap.getMapImage(this.getUIContext().getHostContext(), staticMapOptions);

#### StaticMapOptions

Defines parameters for creating a static map.

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

location

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

No

 | 

Coordinates of the map center point.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

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

Map zoom level, which must be an integer ranging from 2 to 17. If this parameter is set to a decimal, the decimal will be rounded down.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

imageWidth

 | 

number

 | 

No

 | 

No

 | 

Image width.

If **scale** is set to **1**, the value range of this parameter is (0, 1024\]. If **scale** is set to **2**, the value range of this parameter is (0, 512\]. The unit is px.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

imageHeight

 | 

number

 | 

No

 | 

No

 | 

Image height.

If **scale** is set to **1**, the value range of this parameter is (0, 1024\]. If **scale** is set to **2**, the value range of this parameter is (0, 512\]. The unit is px.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

scale

 | 

number

 | 

No

 | 

Yes

 | 

Map scale, which is **1** or **2**. The default value is **1**.

This parameter can be used to obtain a map image with a high resolution. The actual size (in pixels) of the map image equals the product of **scale**, **imageWidth**, and **imageHeight**.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

logoAlignment

 | 

[mapCommon.LogoAlignment](../mapcommon-map-attribute-model/document.md#section892653673414)

 | 

No

 | 

Yes

 | 

Map logo alignment mode. The default value is **BOTTOM\_START**, indicating the lower left corner.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

markers

 | 

Array<[StaticMapMarker](#section2425142418218)\>

 | 

No

 | 

Yes

 | 

Adds Markers to the map image.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

NOTE:

Loading icon resources affects network performance. It is advised to use no more than three Markers.

 |
| 

path

 | 

[StaticMapPath](#section5891333163917)

 | 

No

 | 

Yes

 | 

Adds paths to the static map.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

dayNightMode

 | 

[mapCommon.DayNightMode](../mapcommon-map-attribute-model/document.md#section634916281725)

 | 

No

 | 

Yes

 | 

Day/Dark mode. The default value is [mapCommon.DayNightMode](../mapcommon-map-attribute-model/document.md#section634916281725).DAY.

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |

**Example**:

let staticMapOptions: staticMap.StaticMapOptions = {
  location: {
    latitude: 39.9,
    longitude: 116.4
  },
  zoom: 3,
  imageWidth: 10,
  imageHeight: 10
};

#### StaticMapMarker

Defines the position of a Marker.

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

location

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

No

 | 

Marker coordinates.

 |
| 

icon

 | 

string

 | 

No

 | 

Yes

 | 

Custom icon of a Marker. The value must start with http:// or https://. If no icon is set or the icon does not meet the requirements, the default icon will be used.

NOTE:

The icon must be in PNG format, no larger than 16 KB in size, and with dimensions no greater than 128 x 128 pixels.

 |
| 

defaultIconSize

 | 

[IconSize](#en-us_topic_0000001245084266_section18522846142615)

 | 

No

 | 

Yes

 | 

Size of the default icon. The default value is [IconSize](#en-us_topic_0000001245084266_section18522846142615).NORMAL, indicating a medium size.

 |
| 

font

 | 

string

 | 

No

 | 

Yes

 | 

Name of a Marker. If a name exceeds the display limit, the overflowing portion will be replaced with an ellipsis (...).

 |
| 

fontColor

 | 

number

 | 

No

 | 

Yes

 | 

Text color of a Marker, in ARGB format. The default value is **0xff000000** (black).

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

Rotation angle of the icon of a Marker (only a custom icon is supported).

0 degrees is due north, and angles increase clockwise. The value range is \[0, 360\]. The default value is **0**.

 |

**Example**:

let staticMapMarker: staticMap.StaticMapMarker = {
  location: {
    latitude: 50,
    longitude: 126
  },
  icon: 'https://icons.iconarchive.com/icons/papirus-team/papirus-apps/48/pingus-icon-icon.png',
  font: 'statics',
  fontColor: 0xff000000,
  rotation: 180,
  defaultIconSize: staticMap.IconSize.TINY
};

#### StaticMapPath

Defines information of paths to be added to a static map.

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

locations

 | 

Array<[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

No

 | 

No

 | 

Coordinates of a path.

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

Path color, in ARGB format. The default value is **0xff000000** (black).

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

Fill color of a path, in ARGB format. If it is set, the path forms a polygon. The default value is **0x00000000** (transparent).

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

Path width, in pixels. The value ranges from 0 (excluded) to 1024. The default value is **5**. Invalid parameter values are not processed.

 |

**Example**:

let staticMapPath: staticMap.StaticMapPath = {
  locations: \[
    { latitude: 50, longitude: 126 },
    { latitude: 50.3, longitude: 126 },
    { latitude: 50.3, longitude: 126.3 },
    { latitude: 49.7, longitude: 126 },
    { latitude: 50, longitude: 126 }
  \],
  color: 0xff00ff00,
  fillColor: 0xff0000ff,
  width: 15
};

#### IconSize

Defines the default icon size of a Marker on the static map.

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

TINY

 | 

0

 | 

Minimum icon.

 |
| 

SMALL

 | 

1

 | 

Small icon.

 |
| 

NORMAL

 | 

2

 | 

Medium-sized icon.

 |

**Example**:

let iconSize = staticMap.IconSize.TINY;
