# Geocoding

#### Use Cases

The positive geocoding and reverse geocoding capabilities are provided.

-   Forward geocoding: Obtains the longitude and latitude of the location based on its address.
-   Reverse geocoding: Obtain the location information corresponding to the longitude and latitude.

#### API Description

The following table describes APIs for geocoding, which are mainly provided by methods in the [site](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site) namespace. For more information about the APIs, please refer to [site (Place Search)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[geocode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section8164175012335)(geocodeParams: [GeocodeParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section1694092873712)): Promise<[GeocodeResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section6240139114011)\>

 | 

Performs forward geocoding.

 |
| 

[geocode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section115620617362)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), geocodeParams: [GeocodeParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section1694092873712)): Promise<[GeocodeResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section6240139114011)\>

 | 

Performs forward geocoding. The context can be passed.

 |
| 

[reverseGeocode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section18528174963917)(reverseGeocodeParams: [ReverseGeocodeParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section1170341119303)): Promise<[ReverseGeocodeResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section6201636113110)\>

 | 

Performs reverse geocoding.

 |
| 

[reverseGeocode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section52110883915)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), reverseGeocodeParams: [ReverseGeocodeParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section1170341119303)): Promise<[ReverseGeocodeResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section6201636113110)\>

 | 

Performs reverse geocoding. The context can be passed.

 |
| 

[GeocodeParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section1694092873712)

 | 

Parameters for forward geocoding.

 |
| 

[GeocodeResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section6240139114011)

 | 

Forward geocoding result.

 |
| 

[ReverseGeocodeParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section1170341119303)

 | 

Parameters for reverse geocoding.

 |
| 

[ReverseGeocodeResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section6201636113110)

 | 

Reverse geocoding result.

 |

#### Development Procedure

Import required modules.

import { site } from '@kit.MapKit';
import { BusinessError } from '@kit.BasicServicesKit';

## Forward Geocoding

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/qE9ywmQoQlqdr-e6Lb27Ug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA323EC02D4436E3F5257D4672A2A1E0C510DCE6FD525909AD297EEC520E6CA9)

This capability obtains spatial coordinates (such as the longitude and latitude) of a place based on its address. A maximum of 10 records can be returned.

let params: site.GeocodeParams = {
  // Address information.
  query: 'Piazzale Dante, 41, 55049 Viareggio',
  language: 'en'
};
try {
  const result = await site.geocode(params);
  console.info(\`Succeeded in geocoding. result is ${JSON.stringify(result)}\`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`Failed in geocoding. Code is ${err.code}, message is ${err.message}\`);
}

## Reverse Geocoding

let params: site.ReverseGeocodeParams = {
  // Longitude and latitude of a place.
  location: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  },
  language: "en",
  radius: 0,
  isExtension: true,
  isNearbyAoi: true
};
try {
  const result = await site.reverseGeocode(params);
  console.info(\`Succeeded in reversing. result is ${JSON.stringify(result)}\`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`Failed in reversing. Code is ${err.code}, message is ${err.message}\`);
}
