# Batch Route Computation

#### Use Cases

This capability quickly calculates distances and travel times between multiple departure places and destinations across different transportation modes, including driving, walking, and cycling, in batches.

#### API Description

The following table describes APIs for route planning, which are mainly provided by methods in the [navi](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api) namespace. For more information about the APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[getDrivingMatrix](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section13344132412116)(params: [DrivingMatrixParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section28063259547)): Promise<[MatrixResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section39821913105112)\>

 | 

Performs batch route computation for driving.

 |
| 

[getDrivingMatrix](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section51124206433)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), params: [DrivingMatrixParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section28063259547)): Promise<[MatrixResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section39821913105112)\>

 | 

Performs batch route computation for driving. The context can be passed.

 |
| 

[getWalkingMatrix](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section99212131124)(params: [MatrixParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section169321223144714)): Promise<[MatrixResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section39821913105112)\>

 | 

Performs batch route computation for walking.

 |
| 

[getWalkingMatrix](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section2073332519489)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), params: [MatrixParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section169321223144714)): Promise<[MatrixResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section39821913105112)\>

 | 

Performs batch route computation for walking. The context can be passed.

 |
| 

[getCyclingMatrix](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section20522154810218)(params: [MatrixParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section169321223144714)): Promise<[MatrixResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section39821913105112)\>

 | 

Performs batch route computation for cycling.

 |
| 

[getCyclingMatrix](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section20175113834919)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), params: [MatrixParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section169321223144714)): Promise<[MatrixResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section39821913105112)\>

 | 

Performs batch route computation for cycling. The context can be passed.

 |
| 

[DrivingMatrixParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section28063259547)

 | 

Parameters for batch driving route computation.

 |
| 

[MatrixParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section169321223144714)

 | 

Parameters for batch walking and cycling route computation.

 |
| 

[MatrixResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-navi-api#section39821913105112)

 | 

Result of batch route computation.

 |

#### Development Procedure

Import required modules.

import { navi } from '@kit.MapKit';
import { BusinessError } from '@kit.BasicServicesKit';

## Batch Route Computation for Driving

This capability plans driving routes between multiple departure places and destinations based on their coordinates. This capability can:

-   Support planning for travel in the future.
-   Plan routes based on real-time traffic conditions.
-   Support route preferences, for example, taking the least time, avoiding toll roads, avoiding highways, and taking the shortest distance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/uditakHIRbOA-bWLPedMlQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A04EFF4DFE1E315D59D067346987CECC42A8A67336BDF2F9E8ACC814613EFF0)

Restriction: The number of departure places multiplying the number of destinations must be less than 100.

async testDrivingMatrix() {
  let params: navi.DrivingMatrixParams = {
    // Longitude and latitude of the departure place.
    origins: \[{
      latitude: 31.9844,
      longitude: 118.766253
    }, {
      latitude: 31.9644,
      longitude: 118.746253
    }\],
    // Longitude and latitude of the destination.
    destinations: \[{
      latitude: 31.9344,
      longitude: 118.706253
    }\],
    // Time estimation mode.
    trafficMode: 2,
    language: 'zh\_CN'
  };
  try {
    const result = await navi.getDrivingMatrix(params);
    console.info(\`Succeeded in getting driving matrix. result is ${JSON.stringify(result)}\`);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(\`Failed in getting driving matrix. Code is ${err.code}, message is ${err.message}\`);
  }
}

## Batch Route Computation for Walking

This capability plans walking routes between multiple departure places and destinations based on their coordinates. This capability can:

-   Plan walking routes within a distance of 150 kilometers.
-   Take travel policies (such as taking the least time or avoiding ferries) into consideration for route planning.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/Rkr66A74SsG2OQP1FKp-5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3AEC97600039EB0107977DC9AF066AA907E15A0D4896E21F2525703FE4FF0C50)

Restriction: The number of departure places multiplying the number of destinations must be less than 100.

async testWalkingMatrix() {
  let params: navi.MatrixParams = {
    // Longitude and latitude of the departure place.
    origins: \[
      { 
        latitude: 31.9844,
        longitude: 118.766253 
      }, { 
      latitude: 31.9644,
      longitude: 118.746253 
    }\],
    // Longitude and latitude of the destination.
    destinations: \[{ 
      latitude: 31.9344,
      longitude: 118.706253 
    }\],
    language: 'zh\_CN'
  };
  try {
    const result = await navi.getWalkingMatrix(params);
    console.info(\`Succeeded in getting walking matrix. result is ${JSON.stringify(result)}\`);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(\`Failed in getting walking matrix. Code is ${err.code}, message is ${err.message}\`);
  }
}

## Batch Route Computation for Cycling

This capability plans cycling routes between multiple departure places and destinations based on their coordinates. This capability can:

-   Plan cycling routes within a distance of 500 kilometers.
-   Take travel policies (such as taking the least time or avoiding ferries) into consideration for route planning.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/Z2xXGk8RRQi2GdujOZiolQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B6B8350C06240BBCCEBA853F355F7B8BD8344CB95C9EF5808AC251E804893FE7)

Restriction: The number of departure places multiplying the number of destinations must be less than 100.

async testCyclingMatrix() {
  let params: navi.MatrixParams = {
    // Longitude and latitude of the departure place.
    origins: \[{ 
      latitude: 31.9844,
      longitude: 118.766253
    }, { 
      latitude: 31.9644,
      longitude: 118.746253
    }\],
    // Longitude and latitude of the destination.
    destinations: \[{ 
      latitude: 31.9344,
      longitude: 118.706253
    }\],
    language: 'zh\_CN'
  };
  try {
    const result = await navi.getCyclingMatrix(params);
    console.info(\`Succeeded in getting cycling matrix. result is ${JSON.stringify(result)}\`);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(\`Failed in getting cycling matrix. Code is ${err.code}, message is ${err.message}\`);
  }
}
