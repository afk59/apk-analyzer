# rectifyCoordinate

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### rectifyCoordinate

rectifyCoordinate(context: common.Context, locations: Array<mapCommon.CoordinateLatLng>): Promise<Array<mapCommon.CoordinateLatLng>>

Checks whether the input coordinates need to be rectified based on the input coordinates, input coordinate system, and obtained current route location. If yes, this API returns the rectified coordinate system and coordinates. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/JOstjSktRq-lLK39vEKIXA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8950B46F9244E20528F74678A135C9D588913582E7CC69D01AB452B6B64FF0FC)

-   The **rectifyCoordinate** API is solely designed to address the display offset of original coordinates on a Huawei map.
-   The **rectifyCoordinate** API supports only conversion from WGS84 coordinates to GCJ02 coordinates.

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

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

Context.

 |
| 

locations

 | 

Array<[mapCommon.CoordinateLatLng](../../mapcommon-map-attribute-model/document.md#section196281647173615)\>

 | 

Yes

 | 

Coordinate system and coordinates.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<Array<[mapCommon.CoordinateLatLng](../../mapcommon-map-attribute-model/document.md#section196281647173615)\>>

 | 

Promise that returns the rectified coordinate system and coordinates.

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
| 

1002600013

 | 

The current routing location is unknown. Try again later.

 |

**Example**:

let locations: Array<mapCommon.CoordinateLatLng> = \[
  {
    // Enter coordinates within Hong Kong (China) and the WGS84 coordinate system. If the current map site uses the GCJ02 coordinate system, the GCJ02 coordinate system and the coordinates converted from WGS84 to GCJ02 are returned. 
    coordinateType: mapCommon.CoordinateType.WGS84,
    location: { latitude: 22.280556, longitude: 114.984000 }
  }
\];
// The method containing **await** needs to use the **async** keyword.
let arr: Array<mapCommon.CoordinateLatLng> = await map.rectifyCoordinate(this.getUIContext().getHostContext(), locations);
