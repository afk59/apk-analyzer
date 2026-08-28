# Travel Route Planning

#### Use Cases

Starting from 5.1.1(19), the transit route planning function is supported.

This capability plans driving, walking, cycling, and transit routes between two places. Driving route planning supports waypoints adding.

#### API Description

The following table describes APIs for route planning, which are mainly provided by methods in the [navi](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api) namespace. For more information about the APIs, please refer to [navi (Route Planning)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[getDrivingRoutes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section15371229153110)(params: [DrivingRouteParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section1345541155712)): Promise<[RouteResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section14125152320374)\>

 | 

Plans driving routes.

 |
| 

[getDrivingRoutes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section89883616310)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), params: [DrivingRouteParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section1345541155712)): Promise<[RouteResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section14125152320374)\>

 | 

Plans driving routes. The context can be passed.

 |
| 

[getWalkingRoutes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section18808624125913)(params: [RouteParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section17987175793914)): Promise<[RouteResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section14125152320374)\>

 | 

Plans walking routes.

 |
| 

[getWalkingRoutes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section20859185187)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), params: [RouteParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section17987175793914)): Promise<[RouteResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section14125152320374)\>

 | 

Plans walking routes. The context can be passed.

 |
| 

[getCyclingRoutes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section151981115506)(params: [RouteParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section17987175793914)): Promise<[RouteResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section14125152320374)\>

 | 

Plans cycling routes.

 |
| 

[getCyclingRoutes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section6187385125)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), params: [RouteParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section17987175793914)): Promise<[RouteResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section14125152320374)\>

 | 

Plans cycling routes. The context can be passed.

 |
| 

[getTransitRoutes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section5970105744912)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), params: [TransitRouteParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section54957561312)): Promise<[TransitRouteResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section7752185614207)\>

 | 

Plans transit routes. The context can be passed.

 |
| 

[DrivingRouteParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section1345541155712)

 | 

Parameters for planning driving routes.

 |
| 

[RouteParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section17987175793914)

 | 

Parameters for planning walking and cycling routes.

 |
| 

[TransitRouteParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section54957561312)

 | 

Parameters for transit route planning.

 |
| 

[RouteResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section14125152320374)

 | 

Route planning result.

 |
| 

[TransitRouteResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section7752185614207)

 | 

Transit route planning result.

 |

#### Development Procedure

Import required modules.

import { navi } from '@kit.MapKit';
import { BusinessError } from '@kit.BasicServicesKit';

## Driving Route Planning

This capability plans driving routes between the departure place and destination based on their coordinates. This capability can:

-   Return up to 3 routes for a request.
-   Support up to 5 waypoints.
-   Support planning for travel in the future.
-   Plan routes based on real-time traffic conditions.
-   Support route preferences, for example, taking the least time, avoiding toll roads, avoiding highways, and taking the shortest distance.

async testDrivingRoutes() {
  let params: navi.DrivingRouteParams = {
    // Longitude and latitude of the departure place.
    origins: \[{
      latitude: 31.982129213545843,
      longitude: 120.27745557768591
    }\],
    // Longitude and latitude of the destination.
    destination: {
      latitude: 31.986129213545843,
      longitude: 120.32745557768591
    },
    // Waypoints on the route.
    waypoints: \[{
      latitude: 31.967236140819114,
      longitude: 120.27142088866847
    }, {
      latitude: 31.972868002238872,
      longitude: 120.2943211817165
    }, {
      latitude: 31.98469327973332,
      longitude: 120.29101107384068
    }\],
    language: 'zh\_CN'
  };
  try {
    const result = await navi.getDrivingRoutes(params);
    console.info(\`Succeeded in getting driving routes. result is ${JSON.stringify(result)}\`);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(\`Failed in getting driving routes. Code is ${err.code}, message is ${err.message}\`);
  }
}

## Walking Route Planning

This capability plans walking routes between the departure place and destination based on their coordinates. This capability can:

-   Plan walking routes within a distance of 150 kilometers in a straight line.
-   Take travel policies (such as taking the least time or avoiding ferries) into consideration for route planning.

async testWalkingRoutes() {
  let params: navi.RouteParams = {
    // Longitude and latitude of the departure place.
    origins: \[{
      latitude: 39.992281,
      longitude: 116.31088
    }, { 
      latitude: 39.996,
      longitude: 116.311 
    }\],
    // Longitude and latitude of the destination.
    destination: { 
      latitude: 39.94,
      longitude: 116.311 
    },
    language: 'zh\_CN'
  };
  try {
    const result = await navi.getWalkingRoutes(params);
    console.info(\`Succeeded in getting walking routes. result is ${JSON.stringify(result)}\`);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(\`Failed in getting walking routes. Code is ${err.code}, message is ${err.message}\`);
  }
}

## Cycling Route Planning

This capability plans cycling routes between the departure place and destination based on their coordinates. This capability can:

-   Plan cycling routes within a distance of 500 kilometers in a straight line.
-   Take travel policies (such as taking the least time or avoiding ferries) into consideration for route planning.

async testCyclingRoutes() {
  let params: navi.RouteParams = {
    // Longitude and latitude of the departure place.
    origins: \[{ 
      latitude: 31.9844102,
      longitude: 118.7662537
    }\],
    // Longitude and latitude of the destination.
    destination: { 
      latitude: 31.9874102,
      longitude: 118.7362537
    },
    language: 'zh\_CN'
  };
  try {
    const result = await navi.getCyclingRoutes(params);
    console.info(\`Succeeded in getting cycling routes. result is ${JSON.stringify(result)}\`);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(\`Failed in getting cycling routes. Code is ${err.code}, message is ${err.message}\`);
  }
}

## Transit Route Planning

This capability plans transit routes based on the coordinates of the departure place and destination. This capability is available only in the Chinese mainland.

async testGetTransitRoutes() {
  let params: navi.TransitRouteParams = {
    // Longitude and latitude of the departure place.
    origin: { 
      latitude: 39.921619,
      longitude: 116.356587 
    },
    // Longitude and latitude of the destination.
    destination: {
      latitude: 39.94161,
      longitude: 116.353621 
    },
    // Estimated departure time.
    departureTime: new Date().getTime() / 1000
  };
  try {
    const result = await navi.getTransitRoutes(this.getUIContext().getHostContext(), params);
    console.info(\`Succeeded in getting transit routes. result is ${JSON.stringify(result)}\`);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(\`Failed in getting transit routes. Code is ${err.code}, message is ${err.message}\`);
  }
}
