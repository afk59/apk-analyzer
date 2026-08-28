# Distance Calculation

#### Use Cases

This tool calculates the linear distance between the two points based on the longitude and latitude coordinates specified by the user. The unit is meter.

#### API Description

The following table describes APIs for distance calculation, which are mainly provided by the [calculateDistance](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-calculatedistance) method in the [map](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map) namespace. For more information about the APIs, please refer to [calculateDistance](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-calculatedistance).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[mapCommon.LatLng](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section20691173773810)

 | 

Longitude-latitude object.

 |
| 

[calculateDistance](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-calculatedistance)(from: [mapCommon.LatLng](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section20691173773810), to: [mapCommon.LatLng](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section20691173773810)): number

 | 

Calculates the distance between coordinate points.

 |

#### Development Procedure

1.  Import required modules.
    
    import { map, mapCommon } from '@kit.MapKit';
    
2.  Initialize the coordinates to be calculated and call the [calculateDistance](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-calculatedistance) method to calculate the distance.
    
    let fromLatLng: mapCommon.LatLng = {
      latitude: 38,
      longitude: 118
    };
    let toLatLng: mapCommon.LatLng = {
      latitude: 39,
      longitude: 119
    };
    
    let distance = map.calculateDistance(fromLatLng, toLatLng);
