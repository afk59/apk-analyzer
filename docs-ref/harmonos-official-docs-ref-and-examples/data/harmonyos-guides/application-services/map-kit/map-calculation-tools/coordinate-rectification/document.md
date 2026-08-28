# Coordinate Rectification

#### Introduction to Coordinate Systems

The Huawei map involves the following coordinate systems:

-   WGS84: a geodetic coordinate system, which is also widely used in the Global Positioning System (GPS).
-   GCJ02: a coordinate system for the geographic information system developed by the State Bureau of Surveying and Mapping of China. It is an encrypted WGS84 coordinate system.

#### Coordinate Systems Used by the Huawei map

Sites in the Chinese mainland, Hong Kong (China), and Macao (China) use the GCJ02 coordinate system, and sites in Taiwan (China) and outside China use the WGS84 coordinate system.

#### Use Cases

Map Kit uses the GCJ02 coordinate system for the Chinese mainland, Hong Kong (China), and Macao (China). Directly overlaying WGS84 coordinates on a map using the GCJ02 coordinate system will result in positional offsets due to difference in coordinate values. Therefore, to properly use Map Kit services in the Chinese mainland, Hong Kong (China), and Macao (China), WGS84 coordinates must be converted to GCJ02 coordinates first.

#### API Description

The following table describes APIs for coordinate conversion, which are mainly provided by the [convertCoordinateSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-convertcoordinatesync) and [rectifyCoordinate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-rectifycoordinate) methods in the [map](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map) namespace. For more information about the APIs, please refer to [convertCoordinateSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-convertcoordinatesync).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[mapCommon.CoordinateType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section78948324526)

 | 

Coordinate system type.

 |
| 

[convertCoordinateSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-convertcoordinatesync)(fromType: [mapCommon.CoordinateType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section78948324526), toType: [mapCommon.CoordinateType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section78948324526), location: [mapCommon.LatLng](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section20691173773810)): [mapCommon.LatLng](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section20691173773810)

 | 

Converts WGS84 coordinates to GCJ02 coordinates.

 |
| 

[rectifyCoordinate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-rectifycoordinate)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), locations: Array<[mapCommon.CoordinateLatLng](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section196281647173615)\>): Promise<Array<[mapCommon.CoordinateLatLng](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section196281647173615)\>>

 | 

Performs coordinate rectification.

 |
| 

[mapCommon.LatLng](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section20691173773810)

 | 

Longitude-latitude object.

 |

#### Development Procedure

Import required modules.

import { map, mapCommon } from '@kit.MapKit';

## Coordinate Rectification

The [rectifyCoordinate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-rectifycoordinate) API checks whether rectification is required based on the input coordinates, input coordinate system, and current route location. If yes, this API returns the rectified coordinate system and coordinates.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/4c7DBs68Tt-deS9LoQDIuQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=954F9EA0989F896DBBDDCB59711B68B2A49569A969C25555228377F8B1E7F7E4)

-   This [rectifyCoordinate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-rectifycoordinate) API is solely designed to address the display offset of original coordinates on a Huawei map.
-   The [rectifyCoordinate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-rectifycoordinate) API supports only conversion from WGS84 coordinates to GCJ02 coordinates.

let locations: Array<mapCommon.CoordinateLatLng> = \[
  {
    // Enter coordinates within Hong Kong (China) and the WGS84 coordinate system. If the current map site uses the GCJ02 coordinate system, the GCJ02 coordinate system and the coordinates converted from WGS84 to GCJ02 are returned. 
    coordinateType: mapCommon.CoordinateType.WGS84,
    location: {
      latitude: 22.280556,
      longitude: 114.984000
    }
  }
\];
// The method containing **await** needs to use the **async** keyword.
let arr: Array<mapCommon.CoordinateLatLng> = await map.rectifyCoordinate(this.getUIContext().getHostContext(), locations);

## Coordinate Conversion

Initialize the coordinates to be converted and call the [convertCoordinateSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-convertcoordinatesync) method to convert the coordinates.

let wgs84Position: mapCommon.LatLng = {
  latitude: 30,
  longitude: 118
};
// Convert the longitude-latitude coordinates.
let gcj02Position: mapCommon.LatLng =
  map.convertCoordinateSync(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02, wgs84Position);
