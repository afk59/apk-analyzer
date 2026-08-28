# POI Search

#### Use Cases

The following POI information search capabilities are provided:

-   Keyword search: Returns a list of places based on keywords entered by the user.
-   Nearby place search: Searches for nearby places based on the current location of the user's device.
-   Autocomplete: Returns an autocomplete place and a list of suggested places based on the entered keyword.
-   Place details search: Searches for details about a place.

#### API Description

The following table describes APIs for POI search, which are mainly provided by methods in the [site](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site) namespace. For more information about the APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[searchByText](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section1117619561413)(searchByTextParams: [SearchByTextParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section186305710274)): Promise<[SearchByTextResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section55651334123013)\>

 | 

Performs keyword search.

 |
| 

[searchByText](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section142981754612)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), searchByTextParams: [SearchByTextParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section186305710274)): Promise<[SearchByTextResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section55651334123013)\>

 | 

Performs keyword search. The context can be passed.

 |
| 

[nearbySearch](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section6315894393)(nearbySearchParams: [NearbySearchParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section1963813341280)): Promise<[NearbySearchResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section15617144513016)\>

 | 

Performs nearby place search.

 |
| 

[nearbySearch](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section4478173620711)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), nearbySearchParams: [NearbySearchParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section1963813341280)): Promise<[NearbySearchResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section15617144513016)\>

 | 

Performs nearby place search. The context can be passed.

 |
| 

[queryAutoComplete](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section20324320183912)(queryAutoCompleteParams: [QueryAutoCompleteParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section18371146292)): Promise<[QueryAutoCompleteResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section81901456163020)\>

 | 

Performs autocomplete.

 |
| 

[queryAutoComplete](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section1095410462267)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), queryAutoCompleteParams: [QueryAutoCompleteParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section18371146292)): Promise<[QueryAutoCompleteResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section81901456163020)\>

 | 

Performs autocomplete. The context can be passed.

 |
| 

[searchById](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section17490031173910)(searchByIdParams: [SearchByIdParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section756019297292)): Promise<[SearchByIdResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section9671461314)\>

 | 

Searches for place details.

 |
| 

[searchById](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section192881428123313)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), searchByIdParams: [SearchByIdParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section756019297292)): Promise<[SearchByIdResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-site#section9671461314)\>

 | 

Searches for place details. The context can be passed.

 |

#### Development Procedure

Import required modules.

import { site } from '@kit.MapKit';
import { BusinessError } from '@kit.BasicServicesKit';

## Keyword Search

This capability allows a user to search for a place, such as a scenic spot, enterprise, or school, based on the user's input keyword and coordinate bounds. Coordinate bounds are optional.

let params: site.SearchByTextParams = {
  // Set a search keyword, for example, "The Palace Museum" or "Confucius Temple".
  query: "Piazzale Dante, 41, 55049 Viareggio, Tuscany, Italy",
  // Longitude-latitude coordinates.
  location: {
    latitude: 31.984,
    longitude: 118.76625
  },
 // Specify the radius of a geographical location.
  radius: 10000,
  // Language of the search result.
  language: "en"
};
// Return the keyword search result.
try {
  const result = await site.searchByText(params);
  console.info(\`Succeeded in searching by text. result is ${JSON.stringify(result)}\`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`Failed in searching by text. Code is ${err.code}, message is ${err.message}\`);
}

## Nearby Place Search

This capability searches for nearby places based on the user device location. You can optimize the search result by providing keywords or specifying the type of the places to search.

let params: site.NearbySearchParams = {
  location: {
    latitude:51.50811219132287,
    longitude:-0.07594896472392065
  },
  poiTypes: \[
    "Watch\_Store",
    "SUBWAY",
    "PRIMARY\_SCHOOL",
    "GENERAL\_AUTO\_REPAIR\_SERVICE\_CENTER"
  \]
}
// Return the nearby place search result. 
try {
  const result = await site.nearbySearch(params);
  console.info(\`Succeeded in searching nearby. result is ${JSON.stringify(result)}\`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`Failed in searching nearby. Code is ${err.code}, message is ${err.message}\`);
}

## Autocomplete

This capability presents the most possible search terms to users based on their input keywords to reduce the amount of information they need to enter and improve their experience. For example, if a user enters Beijing, this capability suggests Beijing, Beijing Railway Station, and Beijing West Railway Station.

let params: site.QueryAutoCompleteParams = {
  // Custom keyword.
  query: "hotel",
  // Longitude-latitude coordinates.
  location: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  },
  language: "en",
  // Return child nodes. 
  isChildren: true
};
// Return the autocomplete result.
try {
  const result = await site.queryAutoComplete(params);
  console.info(\`Succeeded in querying. result is ${JSON.stringify(result)}\`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`Failed in querying. Code is ${err.code}, message is ${err.message}\`);
}

## Place Details Search

This capability obtains details about a place based on its unique site ID (**siteId**) which serves as the primary key. The details include the name, address, and longitude and latitude of the place. The value of **siteId** can be obtained from the return result of APIs of other capabilities including keyword search, nearby place search, place details search, autocomplete, and forward geocoding.

let params: site.SearchByIdParams = {
  // Specify the primary key site ID.
  siteId: "144129739873977856",
  language: "en",
  // Return child nodes. 
  isChildren: true
};
// Return the place details search result.
try {
  const result = await site.searchById(params);
  console.info(\`Succeeded in searching. result is ${JSON.stringify(result)}\`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`Failed in searching. Code is ${err.code}, message is ${err.message}\`);
}
