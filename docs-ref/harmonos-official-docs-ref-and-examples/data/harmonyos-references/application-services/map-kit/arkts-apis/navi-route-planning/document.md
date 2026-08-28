# navi (Route Planning)

This module provides the route planning function.

**Start version**: 4.1.0(11)

#### Module Import

import { navi } from '@kit.MapKit';

#### getDrivingRoutes

getDrivingRoutes(params: DrivingRouteParams): Promise<RouteResult>

Plans the driving routes between two locations. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/rapVQHvpRYOezHeUPZzNUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7D6AE16A0712DB23F1CBAF3F7EC45CE20E9D0728E646E04B9F0E29E5DAC0BAE)

-   A maximum of three routes can be returned for each API call.
-   You can specify up to 5 waypoints.

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

params

 | 

[DrivingRouteParams](#section1345541155712)

 | 

Yes

 | 

Parameters for planning driving routes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[RouteResult](#section14125152320374)\>

 | 

[RouteResult](#section14125152320374) object returned through a promise.

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
| 

1002600011

 | 

Server error.

 |
| 

1002600999

 | 

Unknown error.

 |
| 

1002602001

 | 

The start and end points do not have home countries, or a service error occurred.

 |
| 

1002602002

 | 

Cross-region route planning is not supported.

 |
| 

1002602003

 | 

The number of start points or end points exceed 100.

 |
| 

1002602004

 | 

The linear distance between the start point and end point exceeds the upper limit.

 |
| 

1002602005

 | 

The start point, end point, or waypoint does not support navigation.

 |
| 

1002602006

 | 

The request point is mapped to the same point on the road.

 |

**Example**:

let params: navi.DrivingRouteParams = {
  origins: \[{
    "latitude": 31.9821213545843,
    "longitude": 120.27745557768591
  }\],
  destination: {
    "latitude": 31.983545843,
    "longitude": 120.27745557768591
  },
  waypoints: \[
    { "latitude": 31.967236140819114, "longitude": 120.27142088866847 },
    { "latitude": 31.972868002238872, "longitude": 120.2943211817165 },
    { "latitude": 31.98469327973332, "longitude": 120.29101107384068 }
  \],
  language: "zh\_CN"
};
const result = await navi.getDrivingRoutes(params);
console.info("Succeeded in getting driving routes.");

#### getDrivingRoutes

getDrivingRoutes(context: common.Context, params: DrivingRouteParams): Promise<RouteResult>

Plans the driving routes between two locations. The context can be passed. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/cdkS-BJ8R6CBWRvMXWY7JA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DAB4B579717032089A8058E11B4FE440DD9B46C4481332ECDC578045957970A)

-   A maximum of three routes can be returned for each API call.
-   You can specify up to 5 waypoints.

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

params

 | 

[DrivingRouteParams](#section1345541155712)

 | 

Yes

 | 

Parameters for planning driving routes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[RouteResult](#section14125152320374)\>

 | 

[RouteResult](#section14125152320374) object returned through a promise.

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
| 

1002600011

 | 

Server error.

 |
| 

1002600999

 | 

Unknown error.

 |
| 

1002602001

 | 

The start and end points do not have home countries, or a service error occurred.

 |
| 

1002602002

 | 

Cross-region route planning is not supported.

 |
| 

1002602003

 | 

The number of start points or end points exceed 100.

 |
| 

1002602004

 | 

The linear distance between the start point and end point exceeds the upper limit.

 |
| 

1002602005

 | 

The start point, end point, or waypoint does not support navigation.

 |
| 

1002602006

 | 

The request point is mapped to the same point on the road.

 |

**Example**:

let params: navi.DrivingRouteParams = {
  origins: \[{
    "latitude": 31.982129213545843,
    "longitude": 120.27745557768591
  }\],
  destination: {
    "latitude": 31.9821213545843,
    "longitude": 120.277557768591
  },
  waypoints: \[
    { "latitude": 31.967236140819114, "longitude": 120.27142088866847 },
    { "latitude": 31.972868002238872, "longitude": 120.2943211817165 },
    { "latitude": 31.98469327973332, "longitude": 120.29101107384068 }
  \],
  language: "zh\_CN"
};
const result = await navi.getDrivingRoutes(this.getUIContext().getHostContext(), params);
console.info("Succeeded in getting driving routes.");

#### getWalkingRoutes

getWalkingRoutes(params: RouteParams): Promise<RouteResult>

Plans the walking routes between two locations. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/JpiIqFFJS0-RYD2M684EjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1AFFD4F43F5FCA3FFA5E9C5164BADE082BDCD2A15F7D2C9A62E172950315AC0F)

Walking route planning is limited to two locations within a straight-line distance of 150 kilometers.

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

params

 | 

[RouteParams](#section17987175793914)

 | 

Yes

 | 

Parameters for planning walking routes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[RouteResult](#section14125152320374)\>

 | 

[RouteResult](#section14125152320374) object returned through a promise.

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
| 

1002600011

 | 

Server error.

 |
| 

1002600999

 | 

Unknown error.

 |
| 

1002602001

 | 

The start and end points do not have home countries, or a service error occurred.

 |
| 

1002602002

 | 

Cross-region route planning is not supported.

 |
| 

1002602003

 | 

The number of start points or end points exceed 100.

 |
| 

1002602004

 | 

The linear distance between the start point and end point exceeds the upper limit.

 |
| 

1002602005

 | 

The start point, end point, or waypoint does not support navigation.

 |
| 

1002602006

 | 

The request point is mapped to the same point on the road.

 |

**Example**:

let params: navi.RouteParams = {
  origins: \[
    { "latitude": 39.992281, "longitude": 116.31088 },
    { "latitude": 39.996, "longitude": 116.311 }
  \],
  destination: {
    "latitude": 39.94,
    "longitude": 116.311
  },
  language: "zh\_CN"
};
const result = await navi.getWalkingRoutes(params);
console.info("Succeeded in getting walking routes.");

#### getWalkingRoutes

getWalkingRoutes(context: common.Context, params: RouteParams): Promise<RouteResult>

Plans the walking routes between two locations. The context can be passed. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/Ha1PPMV1TsSTEQhXeYS-Fg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF7881F50618209AABAEA9FDBEEA408B0A048B9B3D5FBADAB3F6F3794EC223BD)

Walking route planning is limited to locations within a straight-line distance of 150 kilometers.

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

params

 | 

[RouteParams](#section17987175793914)

 | 

Yes

 | 

Parameters for planning walking routes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[RouteResult](#section14125152320374)\>

 | 

[RouteResult](#section14125152320374) object returned through a promise.

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
| 

1002600011

 | 

Server error.

 |
| 

1002600999

 | 

Unknown error.

 |
| 

1002602001

 | 

The start and end points do not have home countries, or a service error occurred.

 |
| 

1002602002

 | 

Cross-region route planning is not supported.

 |
| 

1002602003

 | 

The number of start points or end points exceed 100.

 |
| 

1002602004

 | 

The linear distance between the start point and end point exceeds the upper limit.

 |
| 

1002602005

 | 

The start point, end point, or waypoint does not support navigation.

 |
| 

1002602006

 | 

The request point is mapped to the same point on the road.

 |

**Example**:

let params: navi.DrivingRouteParams = {
  origins: \[{
    "latitude": 31.982129213545843,
    "longitude": 120.27745557768591
  }\],
  destination: {
    "latitude": 31.9821213545843,
    "longitude": 120.277557768591
  },
  waypoints: \[
    { "latitude": 31.967236140819114, "longitude": 120.27142088866847 },
    { "latitude": 31.972868002238872, "longitude": 120.2943211817165 },
    { "latitude": 31.98469327973332, "longitude": 120.29101107384068 }
  \],
  language: "zh\_CN"
};
const result = await navi.getWalkingRoutes(this.getUIContext().getHostContext(), params);
console.info("Succeeded in getting walking routes.");

#### getCyclingRoutes

getCyclingRoutes(params: RouteParams): Promise<RouteResult>

Plans the cycling routes between two locations. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/eg3BD641SZOiZiNxtbabyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1960CF024F1C5B3E57B033F3089FBC22FF61C63022B591C9BB75824F8A82D02C)

Cycling route planning is limited to locations within a straight-line distance of 500 kilometers.

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

params

 | 

[RouteParams](#section17987175793914)

 | 

Yes

 | 

Parameters for planning cycling routes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[RouteResult](#section14125152320374)\>

 | 

[RouteResult](#section14125152320374) object returned through a promise.

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
| 

1002600011

 | 

Server error.

 |
| 

1002600999

 | 

Unknown error.

 |
| 

1002602001

 | 

The start and end points do not have home countries, or a service error occurred.

 |
| 

1002602002

 | 

Cross-region route planning is not supported.

 |
| 

1002602003

 | 

The number of start points or end points exceed 100.

 |
| 

1002602004

 | 

The linear distance between the start point and end point exceeds the upper limit.

 |
| 

1002602005

 | 

The start point, end point, or waypoint does not support navigation.

 |
| 

1002602006

 | 

The request point is mapped to the same point on the road.

 |

**Example**:

let params: navi.RouteParams = {
  origins: \[{
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  }\],
  destination: {
    latitude: 30.9844259206815,
    longitude: 119.766259397866
  },
  language: "zh\_CN"
};
const result = await navi.getCyclingRoutes(params);
console.info("Succeeded in getting cycling routes.");

#### getCyclingRoutes

getCyclingRoutes(context: common.Context, params: RouteParams): Promise<RouteResult>

Plans the cycling routes between two locations. The context can be passed. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/hQlqTjkqRj6IGlOrB0dgIg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D42E1A7B366D69AB91AF14572316B08422FDF1EB11E4632585E02F6B36B7183)

Cycling route planning is limited to locations within a straight-line distance of 500 kilometers.

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

params

 | 

[RouteParams](#section17987175793914)

 | 

Yes

 | 

Parameters for planning cycling routes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[RouteResult](#section14125152320374)\>

 | 

[RouteResult](#section14125152320374) object returned through a promise.

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
| 

1002600011

 | 

Server error.

 |
| 

1002600999

 | 

Unknown error.

 |
| 

1002602001

 | 

The start and end points do not have home countries, or a service error occurred.

 |
| 

1002602002

 | 

Cross-region route planning is not supported.

 |
| 

1002602003

 | 

The number of start points or end points exceed 100.

 |
| 

1002602004

 | 

The linear distance between the start point and end point exceeds the upper limit.

 |
| 

1002602005

 | 

The start point, end point, or waypoint does not support navigation.

 |
| 

1002602006

 | 

The request point is mapped to the same point on the road.

 |

**Example**:

let params: navi.RouteParams = {
  origins: \[{
    latitude: 31.98441059206815,
    longitude: 118.76625379397866
  }\],
  destination: {
    latitude: 30.984410259206815,
    longitude: 119.766259397866
  },
  language: "zh\_CN"
};
const result = await navi.getCyclingRoutes(this.getUIContext().getHostContext(), params);
console.info("Succeeded in getting cycling routes.");

#### getTransitRoutes

getTransitRoutes(context: common.Context, params: TransitRouteParams): Promise<TransitRouteResult>

Plans the transit routes between two locations. This API is available only in the Chinese mainland. This API supports passed context and returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/7uiF1sUMTKSTo4JsgIWDWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D15167B7E4D301D502795A14EB6465BC30E69E8019FC18A762DD568DA955714B)

The straight-line distance between the start and end points cannot exceed 100 km if they are in different cities; however, there is no distance limit if they are within the same city.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

params

 | 

[TransitRouteParams](#section54957561312)

 | 

Yes

 | 

Parameters for transit route planning.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[TransitRouteResult](#section7752185614207)\>

 | 

[TransitRouteResult](#section7752185614207) object returned through a promise.

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
| 

1002600011

 | 

Server error.

 |
| 

1002600999

 | 

Unknown error.

 |
| 

1002602001

 | 

The start and end points do not have home countries, or a service error occurred.

 |
| 

1002602002

 | 

Cross-region route planning is not supported.

 |
| 

1002602004

 | 

The linear distance between the start point and end point exceeds the upper limit.

 |
| 

1002602005

 | 

The start point, end point, or waypoint does not support navigation.

 |
| 

1002602006

 | 

The request point is mapped to the same point on the road.

 |

**Example**:

let params: navi.TransitRouteParams = {
  "origin": { "latitude": 39.921619, "longitude": 116.356587 },
  "destination": { "latitude": 39.94161, "longitude": 116.353621 },
  "departureTime": new Date().getTime() / 1000
};
const result = await navi.getTransitRoutes(this.getUIContext().getHostContext(), params);
console.info("Succeeded in getting transit routes.");

#### getDrivingMatrix

getDrivingMatrix(params: DrivingMatrixParams): Promise<MatrixResult>

Plans the driving routes between multiple locations. This API returns the result asynchronously through a promise.

This function is suitable for high-concurrency scenarios, such as ride-hailing order dispatching. In this context, the function performs a batch calculation for a single request, obtaining the route distance and journey time between multiple departure places and destinations.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/yAkMXe_jQyW-yd7iXJ3TIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16C388284B7F64524AA487AD8A92CA5D8AA6830BF1467CC8330439F900017F1E)

1\. Driving route planning is limited to locations within a straight-line distance of 2000 kilometers.

2\. The number of departure places multiplied by the number of destinations cannot exceed 100.

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

params

 | 

[DrivingMatrixParams](#section28063259547)

 | 

Yes

 | 

Parameters for batch driving route computation.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[MatrixResult](#section39821913105112)\>

 | 

[MatrixResult](#section39821913105112) object returned through a promise.

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
| 

1002600011

 | 

Server error.

 |
| 

1002600999

 | 

Unknown error.

 |
| 

1002602001

 | 

The start and end points do not have home countries, or a service error occurred.

 |
| 

1002602002

 | 

Cross-region route planning is not supported.

 |
| 

1002602003

 | 

The number of start points or end points exceed 100.

 |
| 

1002602004

 | 

The linear distance between the start point and end point exceeds the upper limit.

 |
| 

1002602005

 | 

The start point, end point, or waypoint does not support navigation.

 |
| 

1002602006

 | 

The request point is mapped to the same point on the road.

 |

**Example**:

let params: navi.DrivingMatrixParams = {
  "origins": \[
    {
      latitude: 31.9844159206815,
      longitude: 118.76625379397866
    },
    {
      latitude: 31.184410259206815,
      longitude: 118.366379397866
    }
  \],
  "destinations": \[{
    latitude: 30.98441259206815,
    longitude: 119.765379397866
  }\],
  "trafficMode": 2,
  "language": "zh\_CN"
};
const result = await navi.getDrivingMatrix(params);
console.info("Succeeded in getting driving matrix.");

#### getDrivingMatrix

getDrivingMatrix(context: common.Context, params: DrivingMatrixParams): Promise<MatrixResult>

Plans the driving routes between multiple locations. The context can be passed. This API returns the result asynchronously through a promise.

This function is suitable for high-concurrency scenarios, such as ride-hailing order dispatching. In this context, the function performs a batch calculation for a single request, obtaining the route distance and journey time between multiple departure places and destinations.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/nxnTmA2FSKKzeMbuvmpq2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64BB6C685462DBC86C0C0132B1E319AFAB31C000DA68985B1ED3C2E253019014)

1\. Driving route planning is limited to locations within a straight-line distance of 2000 kilometers.

2\. The number of departure places multiplied by the number of destinations cannot exceed 100.

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

params

 | 

[DrivingMatrixParams](#section28063259547)

 | 

Yes

 | 

Parameters for batch driving route computation.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[MatrixResult](#section39821913105112)\>

 | 

[MatrixResult](#section39821913105112) object returned through a promise.

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
| 

1002600011

 | 

Server error.

 |
| 

1002600999

 | 

Unknown error.

 |
| 

1002602001

 | 

The start and end points do not have home countries, or a service error occurred.

 |
| 

1002602002

 | 

Cross-region route planning is not supported.

 |
| 

1002602003

 | 

The number of start points or end points exceed 100.

 |
| 

1002602004

 | 

The linear distance between the start point and end point exceeds the upper limit.

 |
| 

1002602005

 | 

The start point, end point, or waypoint does not support navigation.

 |
| 

1002602006

 | 

The request point is mapped to the same point on the road.

 |

**Example**:

let params: navi.DrivingMatrixParams = {
  "origins": \[
    {
      latitude: 31.984410259206815,
      longitude: 118.76625379397866
    },
    {
      latitude: 31.904410259206815,
      longitude: 118.70625379397866
    }
  \],
  "destinations": \[{
    latitude: 30.9844109206815,
    longitude: 119.765379397866
  }\],
  "trafficMode": 2,
  "language": "zh\_CN"
};
const result = await navi.getDrivingMatrix(this.getUIContext().getHostContext(), params);
console.info("Succeeded in getting driving matrix.");

#### getWalkingMatrix

getWalkingMatrix(params: MatrixParams): Promise<MatrixResult>

Plans the walking routes between multiple locations. This API returns the result asynchronously through a promise.

This function is suitable for high-concurrency scenarios, such as package delivery. In this context, the function performs a batch calculation for a single request, obtaining the route distance and journey time between multiple departure places and destinations.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/o2DM2wweSPuy8blOsL40rg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8BE36B2F3A89C28D150E8DA7DCB4C2D9B858F44491C7F5543BA809F8ADF9AB3A)

1\. Walking route planning is limited to locations within a straight-line distance of 150 kilometers.

2\. The number of departure places multiplied by the number of destinations cannot exceed 100.

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

params

 | 

[MatrixParams](#section169321223144714)

 | 

Yes

 | 

Parameters for batch walking route computation.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[MatrixResult](#section39821913105112)\>

 | 

[MatrixResult](#section39821913105112) object returned through a promise.

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
| 

1002600011

 | 

Server error.

 |
| 

1002600999

 | 

Unknown error.

 |
| 

1002602001

 | 

The start and end points do not have home countries, or a service error occurred.

 |
| 

1002602002

 | 

Cross-region route planning is not supported.

 |
| 

1002602003

 | 

The number of start points or end points exceed 100.

 |
| 

1002602004

 | 

The linear distance between the start point and end point exceeds the upper limit.

 |
| 

1002602005

 | 

The start point, end point, or waypoint does not support navigation.

 |
| 

1002602006

 | 

The request point is mapped to the same point on the road.

 |

**Example**:

let params: navi.MatrixParams = {
  "origins": \[
    {
      latitude: 31.984410259206815,
      longitude: 118.76625379397866
    },
    {
      latitude: 31.904410259206815,
      longitude: 118.70625379397866
    }
  \],
  "destinations": \[{
    latitude: 30.9844259206815,
    longitude: 119.765379397866
  }\],
  "language": "zh\_CN"
};
const result = await navi.getWalkingMatrix(params);
console.info("Succeeded in getting walking matrix.");

#### getWalkingMatrix

getWalkingMatrix(context: common.Context, params: MatrixParams): Promise<MatrixResult>

Plans the walking routes between multiple locations. The context can be passed. This API returns the result asynchronously through a promise.

This function is suitable for high-concurrency scenarios, such as package delivery. In this context, the function performs a batch calculation for a single request, obtaining the route distance and journey time between multiple departure places and destinations.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/O2OEST5fTNays_p2RwNpoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83382AF9D79D8CFCD06CBD66FD9778303037F53A8D093B1CEDE4FF8B3A10FC0F)

1\. Walking route planning is limited to locations within a straight-line distance of 150 kilometers.

2\. The number of departure places multiplied by the number of destinations cannot exceed 100.

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

params

 | 

[MatrixParams](#section169321223144714)

 | 

Yes

 | 

Parameters for batch walking route computation.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[MatrixResult](#section39821913105112)\>

 | 

[MatrixResult](#section39821913105112) object returned through a promise.

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
| 

1002600011

 | 

Server error.

 |
| 

1002600999

 | 

Unknown error.

 |
| 

1002602001

 | 

The start and end points do not have home countries, or a service error occurred.

 |
| 

1002602002

 | 

Cross-region route planning is not supported.

 |
| 

1002602003

 | 

The number of start points or end points exceed 100.

 |
| 

1002602004

 | 

The linear distance between the start point and end point exceeds the upper limit.

 |
| 

1002602005

 | 

The start point, end point, or waypoint does not support navigation.

 |
| 

1002602006

 | 

The request point is mapped to the same point on the road.

 |

**Example**:

let params: navi.MatrixParams = {
  "origins": \[
    {
      latitude: 31.984410259206815,
      longitude: 118.76625379397866
    },
    {
      latitude: 31.904410259206815,
      longitude: 118.70625379397866
    }
  \],
  "destinations": \[{
    latitude: 30.9810259206815,
    longitude: 119.765379397866
  }\],
  "language": "zh\_CN"
};
const result = await navi.getWalkingMatrix(this.getUIContext().getHostContext(), params);
console.info("Succeeded in getting walking matrix.");

#### getCyclingMatrix

getCyclingMatrix(params: MatrixParams): Promise<MatrixResult>

Plans the cycling routes between multiple locations. This API returns the result asynchronously through a promise.

This function is suitable for high-concurrency scenarios, such as package delivery. In this context, the function performs a batch calculation for a single request, obtaining the route distance and journey time between multiple departure places and destinations.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/CssNoxxgQF63GhYG_Kdxyw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4A541DBE53B29E39C687194CDEBC0B831B002E40F5A93DE2CBB54C650053BAA)

1\. Cycling route planning is limited to locations within a straight-line distance of 500 kilometers.

2\. The number of departure places multiplied by the number of destinations cannot exceed 100.

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

params

 | 

[MatrixParams](#section169321223144714)

 | 

Yes

 | 

Parameters for batch cycling route computation.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[MatrixResult](#section39821913105112)\>

 | 

[MatrixResult](#section39821913105112) object returned through a promise.

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
| 

1002600011

 | 

Server error.

 |
| 

1002600999

 | 

Unknown error.

 |
| 

1002602001

 | 

The start and end points do not have home countries, or a service error occurred.

 |
| 

1002602002

 | 

Cross-region route planning is not supported.

 |
| 

1002602003

 | 

The number of start points or end points exceed 100.

 |
| 

1002602004

 | 

The linear distance between the start point and end point exceeds the upper limit.

 |
| 

1002602005

 | 

The start point, end point, or waypoint does not support navigation.

 |
| 

1002602006

 | 

The request point is mapped to the same point on the road.

 |

**Example**:

let params: navi.MatrixParams = {
  "origins": \[
    {
      latitude: 31.984410259206815,
      longitude: 118.76625379397866
    },
    {
      latitude: 31.904410259206815,
      longitude: 118.70625379397866
    }
  \],
  "destinations": \[{
    latitude: 30.9841259206815,
    longitude: 119.766239397866
  }\],
  "language": "zh\_CN"
};
const result = await navi.getCyclingMatrix(params);
console.info("Succeeded in getting cycling matrix.");

#### getCyclingMatrix

getCyclingMatrix(context: common.Context, params: MatrixParams): Promise<MatrixResult>

Plans the cycling routes between multiple locations. The context can be passed. This API returns the result asynchronously through a promise.

This function is suitable for high-concurrency scenarios, such as package delivery. In this context, the function performs a batch calculation for a single request, obtaining the route distance and journey time between multiple departure places and destinations.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/UXKH-8U6QBWfqBwt56DocA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44CD3E2018B5F519282E6D97C9B85046A7AFACE791934C72C318BB7DAF409CD4)

1\. Cycling route planning is limited to locations within a straight-line distance of 500 kilometers.

2\. The number of departure places multiplied by the number of destinations cannot exceed 100.

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

params

 | 

[MatrixParams](#section169321223144714)

 | 

Yes

 | 

Parameters for batch cycling route computation.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[MatrixResult](#section39821913105112)\>

 | 

[MatrixResult](#section39821913105112) object returned through a promise.

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
| 

1002600011

 | 

Server error.

 |
| 

1002600999

 | 

Unknown error.

 |
| 

1002602001

 | 

The start and end points do not have home countries, or a service error occurred.

 |
| 

1002602002

 | 

Cross-region route planning is not supported.

 |
| 

1002602003

 | 

The number of start points or end points exceed 100.

 |
| 

1002602004

 | 

The linear distance between the start point and end point exceeds the upper limit.

 |
| 

1002602005

 | 

The start point, end point, or waypoint does not support navigation.

 |
| 

1002602006

 | 

The request point is mapped to the same point on the road.

 |

**Example**:

let params: navi.MatrixParams = {
  "origins": \[
    {
      latitude: 31.984410259206815,
      longitude: 118.76625379397866
    },
    {
      latitude: 31.904410259206815,
      longitude: 118.70625379397866
    }
  \],
  "destinations": \[{
    latitude: 30.98259206815,
    longitude: 119.7679397866
  }\],
  "language": "zh\_CN"
};
const result = await navi.getCyclingMatrix(this.getUIContext().getHostContext(), params);
console.info("Succeeded in getting cycling matrix.");

#### snapToRoads

snapToRoads(params: SnapToRoadsParams): Promise<SnapToRoadsResult>

Captures roads based on specified coordinate points to align the user trajectory to the most likely roads that a vehicle was traveling along, and returns a set of coordinate points on the roads. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/r-7T-_TVSnuEffxhTAh6Wg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E494B29FB629C958A03173A8467D3132ED75C9F58532E142D7B6D47819EAD39)

The number of coordinate points cannot exceed 100, and the distance between two adjacent coordinate points cannot be greater than 500 meters.

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

params

 | 

[SnapToRoadsParams](#section37411438132)

 | 

Yes

 | 

Parameters for trajectory-based road snapping.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[SnapToRoadsResult](#section318832513518)\>

 | 

[SnapToRoadsResult](#section318832513518) object returned through a promise.

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
| 

1002600011

 | 

Server error.

 |
| 

1002600999

 | 

Unknown error.

 |
| 

1002602001

 | 

The start and end points do not have home countries, or a service error occurred.

 |
| 

1002602002

 | 

Cross-region route planning is not supported.

 |
| 

1002602003

 | 

The number of start points or end points exceed 100.

 |
| 

1002602004

 | 

The linear distance between the start point and end point exceeds the upper limit.

 |
| 

1002602005

 | 

The start point, end point, or waypoint does not support navigation.

 |
| 

1002602006

 | 

The request point is mapped to the same point on the road.

 |

**Example**:

let params: navi.SnapToRoadsParams = {
  points: \[{
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  }\]
};
const result = await navi.snapToRoads(params);
console.info("Succeeded in snapping to roads.");

#### snapToRoads

snapToRoads(context: common.Context, params: SnapToRoadsParams): Promise<SnapToRoadsResult>

Captures roads based on specified coordinate points to align the user trajectory to the most likely roads that a vehicle was traveling along, and returns a set of coordinate points on the roads. The context can be passed. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/lBIyuTNOS3K1SQ2w6u6LLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0C18AAEB1F29A6159A45E064907B9CADC61266A7F6E8B19A6053EED10E07788)

The number of coordinate points cannot exceed 100, and the distance between two adjacent coordinate points cannot be greater than 500 meters.

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

params

 | 

[SnapToRoadsParams](#section37411438132)

 | 

Yes

 | 

Parameters for trajectory-based road snapping.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[SnapToRoadsResult](#section318832513518)\>

 | 

[SnapToRoadsResult](#section318832513518) object returned through a promise.

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
| 

1002600011

 | 

Server error.

 |
| 

1002600999

 | 

Unknown error.

 |
| 

1002602001

 | 

The start and end points do not have home countries, or a service error occurred.

 |
| 

1002602002

 | 

Cross-region route planning is not supported.

 |
| 

1002602003

 | 

The number of start points or end points exceed 100.

 |
| 

1002602004

 | 

The linear distance between the start point and end point exceeds the upper limit.

 |
| 

1002602005

 | 

The start point, end point, or waypoint does not support navigation.

 |
| 

1002602006

 | 

The request point is mapped to the same point on the road.

 |

**Example**:

let params: navi.SnapToRoadsParams = {
  points: \[{
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  }\]
};
const result = await navi.snapToRoads(this.getUIContext().getHostContext(), params);
console.info("Succeeded in snapping to roads.");

#### RouteCoordinate

Defines route planning attributes.

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

matchType

 | 

number

 | 

No

 | 

Yes

 | 

Road snapping type of the departure place and destination.

The options are **0** (default), **1**, and **3**.

-   **0**: restricted snapping. Departure places are not snapped to closed roads, roads under construction, traffic restricted roads, and roads set to avoid, and destinations are not snapped to highways, ferries, and roads set to avoid.
-   **1**: unlimited snapping.
-   **3**: trajectory-based snapping. You can pass the longitude-latitude coordinates of consecutive trajectory points in the **origins** parameter for unlimited snapping. This value is supported only for the departure place.

 |
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
| 

accuracy

 | 

number

 | 

No

 | 

Yes

 | 

GPS location accuracy, in meters. It does not have a default value.

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

Altitude, in meters. It does not have a default value.

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

Deviation angle. It does not have a default value.

0 degrees is due north, and angles increase clockwise. The value range is \[0, 360). The default value is **0**. Values that fall outside the valid range will be adjusted to values within the range. For instance, the value **361** would be converted to **1**, and the value **\-1** would be converted to **359**.

 |
| 

speed

 | 

number

 | 

No

 | 

Yes

 | 

Current driving speed, in meters per second. It does not have a default value.

 |
| 

timestamp

 | 

number

 | 

No

 | 

Yes

 | 

Timestamp of the current location generation time. It does not have a default value.

 |

#### RouteParams

Defines parameters for planning walking, cycling, and driving routes.

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

origins

 | 

Array<[RouteCoordinate](#section126101118153712)\>

 | 

No

 | 

No

 | 

List of coordinates of road-snapped departure points.

The number of coordinate points cannot exceed 31, and the distance between two adjacent coordinate points must be greater than 1 meter.

 |
| 

destination

 | 

[RouteCoordinate](#section126101118153712)

 | 

No

 | 

No

 | 

Destination.

NOTE:

If waypoints are not set, the coordinates of the departure place and destination cannot be the same.

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

Language of text instructions/descriptions. Currently, only **zh\_CN** (Chinese) and **en** (English) are supported. If this parameter is not set, the local language will be used.

 |
| 

avoids

 | 

Array<number>

 | 

No

 | 

Yes

 | 

Route calculation policy. The options are as follows:

-   **0**: Fastest route.
-   **1**: Avoid toll roads.
-   **2**: Avoid highways.
-   **4**: Shortest distance.
-   **8**: Avoid ferries.
-   **16**: Avoid congested roads.
-   **32**: Prioritize major roads.
-   **64**: Smart route.
-   **128**: Prioritize highways.
-   **256**: Minimize tolls.
-   **512**: Smooth speed.

The default value is **0**.

Only two policies are supported for walking and cycling route planning: **0** and **8**.

Currently, values **16**, **32**, **128**, and **256** are supported only for route planning within the Chinese mainland, and they will be gradually supported in other countries and regions in the future.

NOTE:

Only policy **1** (Avoid toll roads) and policy **8** (Avoid ferries) can be combined for driving route planning.

 |
| 

extension

 | 

number

 | 

No

 | 

Yes

 | 

Additional information.

-   **0**: basic traffic condition
-   **1**: new traffic condition

The default value is **0**.

 |

#### RouteResult

Defines the route planning result.

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

routes

 | 

Array<[Route](#section1915119249313)\>

 | 

No

 | 

No

 | 

Planned routes from the departure place to the destination. If no routes are available, an empty array will be returned.

 |

#### DrivingRouteParams

Defines parameters for planning driving routes. This API inherits from [RouteParams](#section17987175793914).

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

waypoints

 | 

Array<[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

No

 | 

Yes

 | 

Waypoints. You can specify up to 5 waypoints.

 |
| 

isViaType

 | 

boolean

 | 

No

 | 

Yes

 | 

Waypoint type.

-   **false**: stopover (default value)
-   **true**: via
    
    NOTE:
    
    1\. The **stopover** type indicates a stopping point. The route information will be sent by segment.
    
    2\. The **via** type indicates a waypoint. The complete route information will be returned.
    

 |
| 

optimize

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to optimize a waypoint.

-   **false**: no
-   **true**: yes

The default value is **false**.

 |
| 

alternatives

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to return multiple planned routes.

-   **true**: yes
-   **false**: no (Only one planned route is returned.)

The default value is **false**.

 |
| 

departAt

 | 

number

 | 

No

 | 

Yes

 | 

Estimated departure time, in seconds since 00:00:00 on January 1, 1970 (UTC).

The value must be the current time or a future time.

NOTE:

If **departAt** is set to **0**, the current time is used.

 |
| 

trafficMode

 | 

number

 | 

No

 | 

Yes

 | 

Time estimation mode. The options are as follows:

-   **0**: Intelligent prediction.
-   **1**: Traffic conditions are worse than the historical average.
-   **2**: Traffic conditions are better than the historical average.

The default value is **0**.

 |

#### Route

Defines planned routes from the departure place to the destination.

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

steps

 | 

Array<[RouteStep](#section184864299233)\>

 | 

No

 | 

No

 | 

Route planning information.

 |
| 

overviewPolyline

 | 

Array<[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

No

 | 

Yes

 | 

Longitude and latitude of the encoded MapPolyline of a route.

 |
| 

optimizedWaypoints

 | 

Array<number>

 | 

No

 | 

Yes

 | 

Index of an optimized waypoint. This parameter is available only when **isViaType** is set to **false** and **optimize** is set to **true**.

 |
| 

bounds

 | 

Array<[CoordinateBound](#section125131653173112)\>

 | 

No

 | 

Yes

 | 

Route bounds.

 |
| 

trafficLightCount

 | 

number

 | 

No

 | 

Yes

 | 

Number of traffic lights.

 |
| 

isDestinationInRestrictedArea

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the destination is in a restricted area.

-   **true**: yes
-   **false**: no

 |
| 

isDestinationInDiffTimeZone

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the time zone of the destination is different from that of the departure place.

-   **true**: yes
-   **false**: no

 |
| 

isCrossCountry

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the route crosses a country boundary.

-   **true**: yes
-   **false**: no

 |
| 

isCrossMultiCountries

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the route crosses multiple country boundaries.

-   **true**: yes
-   **false**: no

 |
| 

hasRestrictedRoad

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the route includes private or restricted roads.

-   **true**: yes
-   **false**: no

 |
| 

hasRoughRoad

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the route includes rough roads.

-   **true**: yes
-   **false**: no

 |
| 

hasFerry

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the route includes ferry.

-   **true**: yes
-   **false**: no

 |
| 

hasTolls

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the route includes toll gates.

-   **true**: yes
-   **false**: no

 |
| 

hasStairs

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the route has stairs.

-   **true**: yes
-   **false**: no

 |

#### RouteStep

Defines road planning information.

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

roads

 | 

Array<[RouteRoad](#section61121831133213)\>

 | 

No

 | 

No

 | 

Route section information.

 |
| 

startLocation

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

No

 | 

Longitude and latitude of the departure place.

 |
| 

startAddress

 | 

string

 | 

No

 | 

Yes

 | 

Detailed address of the departure place.

 |
| 

endLocation

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

No

 | 

Longitude and latitude of the destination.

 |
| 

endAddress

 | 

string

 | 

No

 | 

Yes

 | 

Detailed address of the destination.

 |
| 

viaWaypoints

 | 

Array<[Waypoint](#section1203931103920)\>

 | 

No

 | 

Yes

 | 

Waypoint information.

 |
| 

distance

 | 

number

 | 

No

 | 

Yes

 | 

Driving/Walking/Cycling distance, in meters.

 |
| 

distanceDescription

 | 

string

 | 

No

 | 

Yes

 | 

Distance description.

 |
| 

duration

 | 

number

 | 

No

 | 

Yes

 | 

Driving/Walking/Cycling duration, in seconds.

 |
| 

durationDescription

 | 

string

 | 

No

 | 

Yes

 | 

Duration description.

 |
| 

durationInTraffic

 | 

number

 | 

No

 | 

Yes

 | 

Driving/Walking/Cycling duration calculated based on the real-time traffic condition, in seconds.

 |
| 

durationInTrafficDescription

 | 

string

 | 

No

 | 

Yes

 | 

Description of the driving/walking/cycling duration calculated based on the real-time traffic condition.

 |

#### RouteRoad

Defines route section information.

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

startLocation

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

No

 | 

Longitude and latitude of the departure place.

 |
| 

endLocation

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

No

 | 

Longitude and latitude of the destination.

 |
| 

polyline

 | 

Array<[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

No

 | 

No

 | 

A series of coordinate points on a route section (including coordinates of the departure place and destination).

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

Driving/Walking/Cycling distance, in meters.

 |
| 

distanceDescription

 | 

string

 | 

No

 | 

Yes

 | 

Distance description.

 |
| 

duration

 | 

number

 | 

No

 | 

No

 | 

Driving/Walking/Cycling duration, in seconds.

 |
| 

durationDescription

 | 

string

 | 

No

 | 

Yes

 | 

Duration description.

 |
| 

roadName

 | 

string

 | 

No

 | 

Yes

 | 

Road name.

 |
| 

action

 | 

string

 | 

No

 | 

Yes

 | 

Operation to be performed in the current step. The options are as follows:

-   **turn\_slight\_left**: Slightly turn left.
-   **turn\_sharp\_left**: Sharply turn left.
-   **turn\_left**: Turn left
-   **turn\_slight\_right**: Slightly turn right.
-   **turn\_sharp\_right**: Sharply turn right.
-   **turn\_right**: Turn right.
-   **straight**: Go straight.
-   **end**: End point.
-   **waypoint**: Waypoint.

 |
| 

orientation

 | 

number

 | 

No

 | 

Yes

 | 

Road direction. The options are as follows:

-   **0**: bidirectional
-   **1**: forward direction
-   **2**: reverse direction

 |
| 

instruction

 | 

string

 | 

No

 | 

Yes

 | 

Text instruction.

 |
| 

trafficSegments

 | 

Array<[TrafficSegment](#section15388174364413)\>

 | 

No

 | 

Yes

 | 

Traffic information.

 |

#### CoordinateBound

Defines route bounds.

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

northeast

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

No

 | 

Coordinates of the northeast corner.

 |
| 

southwest

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

No

 | 

Coordinates of the southwest corner.

 |

#### Waypoint

Defines waypoint information.

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

Longitude and latitude of a waypoint.

 |
| 

stepIndex

 | 

number

 | 

No

 | 

No

 | 

Waypoint index in the **roads** array.

 |

#### TrafficSegment

Defines traffic information.

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

distance

 | 

number

 | 

No

 | 

No

 | 

Driving/Walking/Cycling distance, in meters.

 |
| 

status

 | 

number

 | 

No

 | 

No

 | 

Traffic status. The options are as follows:

-   **0**: unknown
-   **1**: smooth
-   **2**: slow
-   **3**: congested
-   **4**: extremely congested

 |
| 

polyline

 | 

Array<[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

No

 | 

No

 | 

Road section shape coordinates.

 |

#### MatrixParams

Defines parameters for batch walking, cycling, and driving route computation.

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

origins

 | 

Array<[RouteCoordinate](#section126101118153712)\>

 | 

No

 | 

No

 | 

Longitudes and latitudes of the departure places. A maximum of 100 values are allowed.

 |
| 

destinations

 | 

Array<[RouteCoordinate](#section126101118153712)\>

 | 

No

 | 

No

 | 

Longitudes and latitudes of the destinations. A maximum of 100 values are allowed.

NOTE:

1\. Driving route planning, walking route planning, and cycling route planning are limited to locations within a straight-line distance of 2000 kilometers, 150 kilometers, and 500 kilometers, respectively.

2\. The number of departure places multiplied by the number of destinations cannot exceed 100.

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

Language of text instructions/descriptions. Currently, only **zh\_CN** (Chinese) and **en** (English) are supported. If this parameter is not set, the local language will be used.

 |
| 

avoids

 | 

Array<number>

 | 

No

 | 

Yes

 | 

Route calculation policy. The options are as follows:

-   **0**: Fastest route.
-   **1**: Avoid toll roads.
-   **2**: Avoid highways.
-   **4**: Shortest distance.
-   **8**: Avoid ferries.
-   **16**: Avoid congested roads.
-   **32**: Prioritize major roads.
-   **64**: Smart route.
-   **128**: Prioritize highways.
-   **256**: Minimize tolls.

The default value is **0**.

Only two policies are supported for walking and cycling route planning: **0** and **8**.

All values are supported for driving route planning. Currently, values **16**, **32**, **128**, and **256** are supported only for route planning within the Chinese mainland, and they will be gradually supported in other countries and regions in the future.

 |

#### TransitRouteParams

Defines parameters for transit route planning.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

origin

 | 

[RouteCoordinate](#section126101118153712)

 | 

No

 | 

No

 | 

Longitude and latitude of the departure place.

 |
| 

destination

 | 

[RouteCoordinate](#section126101118153712)

 | 

No

 | 

No

 | 

Longitude and latitude of the destination.

NOTE:

The longitude and latitude of the departure place cannot be the same as those of the destination.

 |
| 

departureTime

 | 

number

 | 

No

 | 

Yes

 | 

Estimated departure time. The value is the number of seconds counting from 1970-01-01 00:00:00 (UTC) to the estimated departure time. The value must be the current time or a future time.

 |
| 

preference

 | 

number

 | 

No

 | 

Yes

 | 

Preference setting. The options are as follows:

-   **0**: recommended (default value)
-   **1**: subway preferred
-   **2**: less walking
-   **3**: fewer transfers
-   **4**: shorter time
-   **5**: no subway

The default value is **0**.

 |

#### TransitRouteResult

Defines the transit route planning result.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

routes

 | 

[TransitRoute](#section5384133083115)\[\]

 | 

No

 | 

Yes

 | 

List of possible routes.

 |

#### TransitRoute

Defines a transit route.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

Route ID.

 |
| 

sections

 | 

[TransitRouteSection](#section82578227495)\[\]

 | 

No

 | 

No

 | 

List of transit routes and pedestrian sections.

 |
| 

busSortInfo

 | 

[BusSortInfo](#section12750123752511)

 | 

No

 | 

Yes

 | 

Route planning summary information.

 |

#### BusSortInfo

Defines the route planning summary information.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

totalCost

 | 

number

 | 

No

 | 

Yes

 | 

Total duration, in seconds.

 |
| 

walkLength

 | 

number

 | 

No

 | 

Yes

 | 

Walking distance, in meters.

 |
| 

transferNum

 | 

number

 | 

No

 | 

Yes

 | 

Number of transfers.

 |
| 

fee

 | 

number

 | 

No

 | 

Yes

 | 

Fee. This parameter is reserved and is not used currently.

 |
| 

score

 | 

number

 | 

No

 | 

Yes

 | 

Score for recommendation. The score is a weighted value calculated based on the travel time, walking distance, number of transfers, number of stops, and route type (bus-only, subway-only, or mixed). The system sorts routes by their scores and recommends the higher-scoring options. This parameter is reserved and is not used currently.

 |
| 

routeId

 | 

string

 | 

No

 | 

Yes

 | 

Route ID.

 |
| 

currency

 | 

string

 | 

No

 | 

Yes

 | 

Currency of the payment. This parameter is reserved and is not used currently.

 |
| 

arrivalTime

 | 

number

 | 

No

 | 

Yes

 | 

Earliest arrival time, in seconds.

 |
| 

routeDesc

 | 

number

 | 

No

 | 

Yes

 | 

Route label. The options are as follows:

-   **0**: normal
-   **1**: outside service hours
-   **2**: risk of missing the last service of the day

This parameter is reserved and is not used currently.

 |

#### TransitRouteSection

Defines the transit route and pedestrian section.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

type

 | 

string

 | 

No

 | 

No

 | 

Section type. The options are as follows:

-   pedestrian
-   transit

 |
| 

pedestrianSection

 | 

[PedestrianSection](#section191722569459)

 | 

No

 | 

Yes

 | 

Pedestrian section.

 |
| 

transitSection

 | 

[TransitSection](#section19721134642018)

 | 

No

 | 

Yes

 | 

Transit section.

 |

#### PedestrianSection

Defines a pedestrian section in a route.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

Unique ID of a pedestrian section.

 |
| 

type

 | 

string

 | 

No

 | 

No

 | 

Type of a pedestrian section, which is used by an app. The value is always **pedestrian**.

 |
| 

arrival

 | 

[PedestrianDepartureArrival](#section6372027173210)

 | 

No

 | 

No

 | 

Destination of a pedestrian section.

 |
| 

departure

 | 

[PedestrianDepartureArrival](#section6372027173210)

 | 

No

 | 

No

 | 

Origin of a pedestrian section.

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

Local language (if available), in BCP 47 format.

 |
| 

passthrough

 | 

[Passthrough](#section118492527531)\[\]

 | 

No

 | 

Yes

 | 

List of waypoints along a pedestrian section. Each requested waypoint is indicated in the response with **passThrough=true**. Waypoints appear on the shortest non-direct route. Waypoints are traversed in the order requested.

This parameter is reserved and is not used currently.

 |
| 

polyline

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)\[\]

 | 

No

 | 

Yes

 | 

Section shape coordinates.

 |
| 

travelSummary

 | 

[BaseSummary](#section17314179815)

 | 

No

 | 

Yes

 | 

Set of key attributes (for example, duration and length), only for the travel between the origin and destination.

 |

#### PedestrianDepartureArrival

Defines the origin and destination of a pedestrian section.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

place

 | 

[Place](#section8761419235)

 | 

No

 | 

No

 | 

Place in a pedestrian section.

 |
| 

time

 | 

number

 | 

No

 | 

Yes

 | 

Estimated departure time. The value is the number of seconds counting from 1970-01-01 00:00:00 (UTC) to the estimated departure time.

 |

#### Passthrough

Defines a place that a route passes through.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

place

 | 

[Place](#section8761419235)

 | 

No

 | 

No

 | 

Origin/destination location.

 |
| 

offset

 | 

number

 | 

No

 | 

Yes

 | 

Waypoint coordinate index.

 |

#### Place

Defines a common location related to a route.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

Location.

 |
| 

type

 | 

string

 | 

No

 | 

No

 | 

Location type. The options are as follows:

-   **accessPoint**: pedestrian access point
-   **station**: public transport station

 |
| 

name

 | 

string

 | 

No

 | 

Yes

 | 

Location name.

 |

#### BaseSummary

Defines the set of key route attributes.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

duration

 | 

number

 | 

No

 | 

No

 | 

Duration, in seconds.

 |
| 

length

 | 

number

 | 

No

 | 

No

 | 

Distance, in meters.

 |
| 

waitTime

 | 

number

 | 

No

 | 

Yes

 | 

Waiting time, in seconds.

 |

#### TransitSection

Defines a transit section. It contains the origin, destination, and route information.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

Unique ID of a transit section. This parameter is reserved and is not used currently.

 |
| 

type

 | 

string

 | 

No

 | 

No

 | 

Type of a transit section, which is used by an app. The value is always **transit**.

 |
| 

arrival

 | 

[TransitArrival](#section1822318412112)

 | 

No

 | 

No

 | 

Transit arrival information.

 |
| 

departure

 | 

[TransitDeparture](#section2991184342113)

 | 

No

 | 

No

 | 

Transit departure information.

 |
| 

intermediateStops

 | 

[TransitStop](#section218815506406)\[\]

 | 

No

 | 

Yes

 | 

Intermediate stops between the origin and destination of a transit section.

This information may be absent if unavailable or not requested.

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

Local language (if available), in BCP 47 format. This parameter is reserved and is not used currently.

 |
| 

passthrough

 | 

[Passthrough](#section118492527531)\[\]

 | 

No

 | 

Yes

 | 

List of waypoints along a transit section. Each requested waypoint is indicated in the response with **passThrough=true**. Waypoints appear on the shortest non-direct route. Waypoints are traversed in the order requested.

This parameter is reserved and is not used currently.

 |
| 

polyline

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)\[\]

 | 

No

 | 

Yes

 | 

Section shape coordinates.

 |
| 

transport

 | 

[TransitTransport](#section157057514)

 | 

No

 | 

Yes

 | 

Transit route information.

 |
| 

travelSummary

 | 

[BaseSummary](#section17314179815)

 | 

No

 | 

Yes

 | 

Set of key attributes (for example, duration and length), only for the travel between the origin and destination. Pre-operations and post-operations are not included.

 |
| 

extraTransitSection

 | 

[ExtraTransitSection](#section19216125133620)\[\]

 | 

No

 | 

Yes

 | 

Extra transit section with the same origin and destination.

 |
| 

sectionDesc

 | 

number

 | 

No

 | 

Yes

 | 

Route label. The options are as follows:

-   **0**: normal
-   **1**: outside service hours
-   **2**: risk of missing the last service of the day

This parameter is reserved and is not used currently.

 |
| 

firstVehicleHour

 | 

number

 | 

No

 | 

Yes

 | 

First bus/subway time, in seconds.

 |
| 

finalVehicleHour

 | 

number

 | 

No

 | 

Yes

 | 

Last bus/subway time, in seconds.

 |
| 

stopOffset

 | 

number

 | 

No

 | 

Yes

 | 

Time offset of the boarding stop or transfer stop from the origin station.

 |

#### TransitArrival

Defines transit arrival information.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

place

 | 

[Place](#section8761419235)

 | 

No

 | 

No

 | 

Transit arrival location.

 |
| 

delay

 | 

number

 | 

No

 | 

Yes

 | 

Cumulative delay from the planned transit arrival time, in seconds. This parameter is reserved and is not used currently.

 |
| 

time

 | 

number

 | 

No

 | 

Yes

 | 

Estimated transit arrival time. The value is the number of seconds counting from 1970-01-01 00:00:00 (UTC) to the estimated transit arrival time. The unit is second.

 |
| 

exit

 | 

[TransitEntranceExit](#section11611234133015)

 | 

No

 | 

Yes

 | 

Exit of a transfer stop.

 |

#### TransitDeparture

Defines transit departure information.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

place

 | 

[Place](#section8761419235)

 | 

No

 | 

No

 | 

Transit departure location.

 |
| 

delay

 | 

number

 | 

No

 | 

Yes

 | 

Cumulative delay from the planned transit departure time, in seconds. This parameter is reserved and is not used currently.

 |
| 

time

 | 

number

 | 

No

 | 

Yes

 | 

Estimated transit departure time. The value is the number of seconds counting from 1970-01-01 00:00:00 (UTC) to the estimated transit departure time. The unit is second.

 |
| 

entrance

 | 

[TransitEntranceExit](#section11611234133015)

 | 

No

 | 

Yes

 | 

Entrance of a transfer stop.

 |

#### TransitEntranceExit

Defines the entrance or exit of a transfer stop.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

name

 | 

string

 | 

No

 | 

No

 | 

ID of an entrance or exit.

 |
| 

location

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

No

 | 

Location.

 |

#### TransitStop

Defines a transfer stop on a route.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

departure

 | 

[TransitDeparture](#section2991184342113)

 | 

No

 | 

No

 | 

Transit departure information.

 |
| 

duration

 | 

number

 | 

No

 | 

Yes

 | 

Stop duration at a transfer stop. If it is not set, the vehicle will depart immediately once passengers are onboard.

 |

#### TransitTransport

Defines transit route information.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

mode

 | 

[TransitMode](#section6879181218313)

 | 

No

 | 

No

 | 

Transit mode.

 |
| 

category

 | 

string

 | 

No

 | 

Yes

 | 

Human-recognizable vehicle type (such as the bus, gondola, tram, and train).

 |
| 

color

 | 

string

 | 

No

 | 

Yes

 | 

Background color of a transit route.

 |
| 

headsign

 | 

string

 | 

No

 | 

Yes

 | 

Sign of a transit route.

 |
| 

name

 | 

string

 | 

No

 | 

Yes

 | 

Name of a transit route.

 |
| 

textColor

 | 

string

 | 

No

 | 

Yes

 | 

Color of a transit route name.

 |

#### ExtraTransitSection

Defines information about the extra transit section.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.1.1(19)

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

intermediateStops

 | 

[TransitStop](#section218815506406)\[\]

 | 

No

 | 

No

 | 

Intermediate stops between the origin and destination of a transit section. This information may be absent if unavailable or not requested.

 |
| 

polyline

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)\[\]

 | 

No

 | 

No

 | 

Section shape coordinates.

 |
| 

transport

 | 

[TransitTransport](#section157057514)

 | 

No

 | 

No

 | 

Transit section information.

 |
| 

travelSummary

 | 

[BaseSummary](#section17314179815)

 | 

No

 | 

No

 | 

Set of key attributes (for example, duration and length), only for the travel between the origin and destination. Pre-operations and post-operations are not included.

 |
| 

firstVehicleHour

 | 

number

 | 

No

 | 

Yes

 | 

First bus/subway time, in seconds.

 |
| 

finalVehicleHour

 | 

number

 | 

No

 | 

Yes

 | 

Last bus/subway time, in seconds.

 |
| 

stopOffset

 | 

number

 | 

No

 | 

Yes

 | 

Time offset of the boarding stop or transfer stop from the origin station.

 |

#### TransitMode

Defines the transit mode.

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

BUS

 | 

bus

 | 

Bus.

 |
| 

SUBWAY

 | 

subway

 | 

Subway.

 |

#### MatrixResult

Defines the result of batch route computation.

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

originAddresses

 | 

Array<string>

 | 

No

 | 

No

 | 

Detailed addresses of departure places.

 |
| 

destinationAddresses

 | 

Array<string>

 | 

No

 | 

No

 | 

Detailed addresses of destinations.

 |
| 

rows

 | 

Array<[MatrixRow](#section144149289579)\>

 | 

No

 | 

No

 | 

Distances and journey time of routes between departure places and destinations.

 |

#### DrivingMatrixParams

Defines parameters for batch driving route computation. This API inherits from [MatrixParams](#section169321223144714).

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

departAt

 | 

number

 | 

No

 | 

Yes

 | 

Estimated departure time, in seconds since 00:00:00 on January 1, 1970 (UTC).

The value must be the current time or a future time.

NOTE:

If **departAt** is set to **0**, the current time is used.

 |
| 

trafficMode

 | 

number

 | 

No

 | 

Yes

 | 

Time estimation mode. The options are as follows:

-   **0**: best guess (default value).
-   **1**: Traffic conditions are worse than the historical average.
-   **2**: Traffic conditions are better than the historical average.

The default value is **0**.

 |

#### MatrixRow

Defines the distances and journey time of routes between departure places and destinations.

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

cells

 | 

Array<[MatrixCell](#section941118399011)\>

 | 

No

 | 

No

 | 

Information about each element in the distance matrix.

 |

#### MatrixCell

Defines information about each element in the distance matrix.

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

distance

 | 

number

 | 

No

 | 

Yes

 | 

Driving/Walking/Cycling distance, in meters.

 |
| 

distanceDescription

 | 

string

 | 

No

 | 

Yes

 | 

Distance description.

 |
| 

duration

 | 

number

 | 

No

 | 

Yes

 | 

Driving/Walking/Cycling duration, in seconds.

 |
| 

durationDescription

 | 

string

 | 

No

 | 

Yes

 | 

Duration description.

 |

#### SnapToRoadsParams

Defines parameters for trajectory-based road snapping.

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

Array<[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

No

 | 

No

 | 

Collection of road snapping points. The number of points ranges from 1 to 100, and the distance between adjacent points must be less than or equal to 500 meters.

 |

#### SnapToRoadsResult

Defines the trajectory-based road snapping result.

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

responseTime

 | 

number

 | 

No

 | 

No

 | 

Time required, in milliseconds.

 |
| 

snappedPoints

 | 

Array<[SnappedPoint](#section174744594613)\>

 | 

No

 | 

No

 | 

Coordinate points on a road. The number of coordinate points cannot exceed 100, and the distance between two adjacent coordinate points cannot be greater than 500 meters.

 |

#### SnappedPoint

Defines road snapping points.

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

latitude

 | 

number

 | 

No

 | 

No

 | 

Latitude.

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

Longitude.

 |
| 

roadId

 | 

string

 | 

No

 | 

No

 | 

Road ID.

 |
