# Trajectory-based Road Snapping

#### Use Cases

This capability captures roads based on specified coordinate points to align the user trajectory to the most likely roads that a vehicle was traveling along, and returns a set of coordinate points on the roads.

#### API Description

The following table describes APIs for route planning, which are mainly provided by methods in the [navi](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api) namespace. For more information about the APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[SnapToRoadsParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section37411438132)

 | 

Parameters for trajectory-based road snapping.

 |
| 

[snapToRoads](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section36176371320)(params: [SnapToRoadsParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section37411438132)): Promise<[SnapToRoadsResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section318832513518)\>

 | 

Performs trajectory-based road snapping.

 |
| 

[snapToRoads](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section119221856164916)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), params: [SnapToRoadsParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section37411438132)): Promise<[SnapToRoadsResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section318832513518)\>

 | 

Performs trajectory-based road snapping. The context can be passed.

 |
| 

[SnapToRoadsResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section318832513518)

 | 

Trajectory-based road snapping result.

 |

#### Development Procedure

Import required modules.

import { navi } from '@kit.MapKit';
import { BusinessError } from '@kit.BasicServicesKit';

## Trajectory-based Road Snapping

This capability captures roads based on specified coordinate points to align the user trajectory to the most likely roads that a vehicle was traveling along, and returns a set of coordinate points on the roads.

async testSnapToRoads() {
  let params: navi.SnapToRoadsParams = {
    // Road snapping points. The number of the points cannot exceed 100, and the distance between adjacent points must be less than or equal to 500 meters.
    points: \[{
      latitude: 31.984410259206815,
      longitude: 118.76625379397866
    }\]
  };
  try {
    const result = await navi.snapToRoads(params);
    console.info(\`Succeeded in snapping to roads. result is ${JSON.stringify(result)}\`);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(\`Failed in snapping to roads. Code is ${err.code}, message is ${err.message}\`);
  }
}
