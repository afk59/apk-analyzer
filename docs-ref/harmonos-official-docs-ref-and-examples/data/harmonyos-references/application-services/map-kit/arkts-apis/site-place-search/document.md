# site (Place Search)

This module provides the place search service.

**Start version**: 4.1.0(11)

#### Module Import

import { site } from '@kit.MapKit';

#### searchByText

searchByText(searchByTextParams: SearchByTextParams): Promise<SearchByTextResult>

Searches for a place, such as a scenic spot, enterprise, or school, based on a user's input keyword and coordinate bounds. Coordinate bounds are optional. This API returns the result asynchronously through a promise.

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

searchByTextParams

 | 

[SearchByTextParams](#section186305710274)

 | 

Yes

 | 

Parameters for keyword search.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[SearchByTextResult](#section55651334123013)\>

 | 

[SearchByTextResult](#section55651334123013) object returned through a promise.

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

1002603001

 | 

Zero result.

 |

**Example**:

let params: site.SearchByTextParams = {
  query: "Piazzale Dante, 41, 55049 Viareggio, Tuscany, Italy",
  location: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  },
  radius: 10000,
  language: "en"
};
const result = await site.searchByText(params);
console.info("Succeeded in searching by text.");

#### searchByText

searchByText(context: common.Context, searchByTextParams: SearchByTextParams): Promise<SearchByTextResult>

Searches for a place, such as a scenic spot, enterprise, or school, based on a user's input keyword and coordinate bounds. Coordinate bounds are optional. The context can be passed. This API returns the result asynchronously through a promise.

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

searchByTextParams

 | 

[SearchByTextParams](#section186305710274)

 | 

Yes

 | 

Parameters for keyword search.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[SearchByTextResult](#section55651334123013)\>

 | 

[SearchByTextResult](#section55651334123013) object returned through a promise.

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

1002603001

 | 

Zero result.

 |

**Example**:

let params: site.SearchByTextParams = {
  query: "Piazzale Dante, 41, 55049 Viareggio, Tuscany, Italy",
  location: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  },
  radius: 10000,
  language: "en"
};
const result = await site.searchByText(this.getUIContext().getHostContext(), params);
console.info("Succeeded in searching by text.");

#### nearbySearch

nearbySearch(nearbySearchParams: NearbySearchParams): Promise<NearbySearchResult>

Searches for nearby places based on the user device location. You can optimize the search result by providing keywords or specifying the type of the places to search. This API returns the result asynchronously through a promise.

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

nearbySearchParams

 | 

[NearbySearchParams](#section1963813341280)

 | 

Yes

 | 

Parameters for nearby place search.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[NearbySearchResult](#section15617144513016)\>

 | 

[NearbySearchResult](#section15617144513016) object returned through a promise.

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

1002603001

 | 

Zero result.

 |

**Example**:

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
const result = await site.nearbySearch(params);
console.info(\`Succeeded in searching nearby. result is ${result}\`);

#### nearbySearch

nearbySearch(context: common.Context, nearbySearchParams: NearbySearchParams): Promise<NearbySearchResult>

Searches for nearby places based on the user device location. The context can be passed. You can optimize the search result by providing keywords or specifying the type of the places to search. This API returns the result asynchronously through a promise.

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

nearbySearchParams

 | 

[NearbySearchParams](#section1963813341280)

 | 

Yes

 | 

Parameters for nearby place search.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[NearbySearchResult](#section15617144513016)\>

 | 

[NearbySearchResult](#section15617144513016) object returned through a promise.

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

1002603001

 | 

Zero result.

 |

**Example**:

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
const result = await site.nearbySearch(this.getUIContext().getHostContext(), params);
console.info(\`Succeeded in searching nearby. result is ${result}\`);

#### queryAutoComplete

queryAutoComplete(queryAutoCompleteParams: QueryAutoCompleteParams): Promise<QueryAutoCompleteResult>

Returns an autocomplete place and a list of suggested places based on the input keyword. This API returns the result asynchronously through a promise.

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

queryAutoCompleteParams

 | 

[QueryAutoCompleteParams](#section18371146292)

 | 

Yes

 | 

Parameters for autocomplete.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[QueryAutoCompleteResult](#section81901456163020)\>

 | 

[QueryAutoCompleteResult](#section81901456163020) object returned through a promise.

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

1002603001

 | 

Zero result.

 |

**Example**:

let params: site.QueryAutoCompleteParams = {
  query: "hotel",
  location: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  },
  language: "en",
  isChildren: true
};
const result = await site.queryAutoComplete(params);
console.info("Succeeded in querying.");

#### queryAutoComplete

queryAutoComplete(context: common.Context, queryAutoCompleteParams: QueryAutoCompleteParams): Promise<QueryAutoCompleteResult>

Returns an autocomplete place and a list of suggested places based on the input keyword. The context can be passed. This API returns the result asynchronously through a promise.

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

queryAutoCompleteParams

 | 

[QueryAutoCompleteParams](#section18371146292)

 | 

Yes

 | 

Parameters for autocomplete.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[QueryAutoCompleteResult](#section81901456163020)\>

 | 

[QueryAutoCompleteResult](#section81901456163020) object returned through a promise.

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

1002603001

 | 

Zero result.

 |

**Example**:

let params: site.QueryAutoCompleteParams = {
  query: "hotel",
  location: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  },
  language: "en",
  isChildren: true
};
const result = await site.queryAutoComplete(this.getUIContext().getHostContext(), params);
console.info("Succeeded in querying.");

#### searchById

searchById(searchByIdParams: SearchByIdParams): Promise<SearchByIdResult>

Obtains details about a place based on its unique ID which serves as the primary key. The details include the name, address, and longitude and latitude of the place. This API returns the result asynchronously through a promise.

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

searchByIdParams

 | 

[SearchByIdParams](#section756019297292)

 | 

Yes

 | 

Parameters for place details search.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[SearchByIdResult](#section9671461314)\>

 | 

[SearchByIdResult](#section9671461314) object returned through a promise.

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

1002603001

 | 

Zero result.

 |

**Example**:

let params: site.SearchByIdParams = {
  siteId: "144129739873977856",
  language: "en",
  isChildren: true
};
const result = await site.searchById(params);
console.info("Succeeded in searching by id.");

#### searchById

searchById(context: common.Context, searchByIdParams: SearchByIdParams): Promise<SearchByIdResult>

Obtains details about a place based on its unique ID which serves as the primary key. The details include the name, address, and longitude and latitude of the place. The context can be passed in to this API. This API returns the result asynchronously through a promise.

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

searchByIdParams

 | 

[SearchByIdParams](#section756019297292)

 | 

Yes

 | 

Parameters for place details search.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[SearchByIdResult](#section9671461314)\>

 | 

[SearchByIdResult](#section9671461314) object returned through a promise.

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

1002603001

 | 

Zero result.

 |

**Example**:

let params: site.SearchByIdParams = {
  siteId: "144129739873977856",
  language: "en",
  isChildren: true
};
const result = await site.searchById(this.getUIContext().getHostContext(), params);
console.info("Succeeded in searching by id.");

#### geocode

geocode(geocodeParams: GeocodeParams): Promise<GeocodeResult>

Obtains the longitude and latitude of a place based on its structured address. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/-7oYZOX3RVWgsErYnZAwlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D25C0CA2CA756BD2CAE684437B875CD5D90CA281E327497EB23886DB12EB1C6E)

This API obtains spatial coordinates (such as the longitude and latitude) of a place based on its address. A maximum of 10 records can be returned.

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

geocodeParams

 | 

[GeocodeParams](#section1694092873712)

 | 

Yes

 | 

Parameters for forward geocoding.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[GeocodeResult](#section6240139114011)\>

 | 

[GeocodeResult](#section6240139114011) object returned through a promise.

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

1002603001

 | 

Zero result.

 |

**Example**:

let params: site.GeocodeParams = {
  "query": "Piazzale Dante, 41, 55049 Viareggio",
  "language": "en"
};
const result = await site.geocode(params);
console.info("Succeeded in geocoding.");

#### geocode

geocode(context: common.Context, geocodeParams: GeocodeParams): Promise<GeocodeResult>

Obtains the longitude and latitude of a place based on its structured address. The context can be passed. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/0RGiIqx1TyuHaKEU4ETfMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3215A767382E3B5138081DB5C2BEC42D335652036A1E3539EA22ADE5EB09D53E)

This API obtains spatial coordinates (such as the longitude and latitude) of a place based on its address. A maximum of 10 records can be returned.

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

geocodeParams

 | 

[GeocodeParams](#section1694092873712)

 | 

Yes

 | 

Parameters for forward geocoding.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[GeocodeResult](#section6240139114011)\>

 | 

[GeocodeResult](#section6240139114011) object returned through a promise.

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

1002603001

 | 

Zero result.

 |

**Example**:

let params: site.GeocodeParams = {
  "query": "Piazzale Dante, 41, 55049 Viareggio",
  "language": "en"
};
const result = await site.geocode(this.getUIContext().getHostContext(), params);
console.info("Succeeded in geocoding.");

#### reverseGeocode

reverseGeocode(reverseGeocodeParams: ReverseGeocodeParams): Promise<ReverseGeocodeResult>

Returns address information based on the longitude and latitude. The address information includes the location description, structured administrative division information, and nearby POIs. This API returns the result asynchronously through a promise.

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

reverseGeocodeParams

 | 

[ReverseGeocodeParams](#section1170341119303)

 | 

Yes

 | 

Parameters for reverse geocoding.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ReverseGeocodeResult](#section6201636113110)\>

 | 

[ReverseGeocodeResult](#section6201636113110) object returned through a promise.

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

1002603001

 | 

Zero result.

 |

**Example**:

let params: site.ReverseGeocodeParams = {
  location: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  },
  language: "en",
  radius: 200
};
const result = await site.reverseGeocode(params);
console.info("Succeeded in reversing geocode.");

#### reverseGeocode

reverseGeocode(context: common.Context, reverseGeocodeParams: ReverseGeocodeParams): Promise<ReverseGeocodeResult>

Returns address information based on the longitude and latitude. The address information includes the location description, structured administrative division information, and nearby POIs. The context can be passed in to this API. This API returns the result asynchronously through a promise.

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

reverseGeocodeParams

 | 

[ReverseGeocodeParams](#section1170341119303)

 | 

Yes

 | 

Parameters for reverse geocoding.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ReverseGeocodeResult](#section6201636113110)\>

 | 

[ReverseGeocodeResult](#section6201636113110) object returned through a promise.

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

1002603001

 | 

Zero result.

 |

**Example**:

let params: site.ReverseGeocodeParams = {
  location: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  },
  language: "en",
  radius: 200
};
const result = await site.reverseGeocode(this.getUIContext().getHostContext(), params);
console.info("Succeeded in reversing geocode.");

#### SortRule

Defines the result sorting rule.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

COMPOSITE

 | 

0

 | 

Comprehensive sorting.

 |
| 

DISTANCE

 | 

1

 | 

Sorting by distance.

 |

#### SearchByTextParams

Defines parameters for keyword search.

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

query

 | 

string

 | 

No

 | 

No

 | 

Search keyword, for example, "Forbidden City". The length of the parameter value ranges from 1 to 512.

 |
| 

location

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

Yes

 | 

Longitude and latitude of the search result.

 |
| 

radius

 | 

number

 | 

No

 | 

Yes

 | 

Search radius, in meters. The value ranges from 1 to 50000. The default value is **50000**. The digits after the decimal point are ignored. Error code 401 will be returned for any invalid value.

 |
| 

poiTypes

 | 

Array<string>

 | 

No

 | 

Yes

 | 

Huawei POI type of a place to search. The value range is the same as that of [HwLocationType](../appendixes/poi-types/document.md#section1662744719618).

 |
| 

countryCodes

 | 

Array<string>

 | 

No

 | 

Yes

 | 

Country/Region code, which complies with ISO 3166-1 alpha-2. This parameter is used to specify the country/region where places are searched.

A maximum of five country/region codes can be passed.

 |
| 

cityId

 | 

string

 | 

No

 | 

Yes

 | 

City ID. This parameter is used to specify the city where places are searched. The length of the parameter value ranges from 1 to 32.

NOTE:

-   Chinese names of Hong Kong (China), and Macao (China), and cities in the Chinese mainland are supported.
-   For Hong Kong, Macao, and cities in the Chinese mainland, the value can be the city code with 3-4 digits or the administrative division code with 6 digits. For details, please refer to [City Codes and Administrative Division Codes](../appendixes/city-codes-and-administrative-division-codes/document.md).
-   The value can also be a city ID with 16-18 digits.

 |
| 

isCityLimit

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the search result must be in the specified city. This parameter needs to be used with **cityId**. The default value is **false**.

-   **true**: yes
-   **false**: no

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

Language of the returned result. The length of the parameter value ranges from 1 to 16. Refer to [Languages Supported by Place Search](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-language#section1629711151663) for supported language options.

If this parameter is not passed, the local language will be used by default. If an invalid value is passed, the local language will be used.

 |
| 

pageSize

 | 

number

 | 

No

 | 

Yes

 | 

Number of records on each page. The value ranges from 1 to 20. The default value is **20**.

 |
| 

pageIndex

 | 

number

 | 

No

 | 

Yes

 | 

Number of the current page. The value ranges from 1 to 500. The default value is **1**.

NOTE:

pageIndex \* pageSize <= 500

 |
| 

isChildren

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to return information about child nodes. The default value is **false**.

-   **true**: yes (Full information about child nodes will be returned.)
-   **false**: no

 |

#### NearbySearchParams

Defines parameters for nearby place search.

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

Current location of a user.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

radius

 | 

number

 | 

No

 | 

Yes

 | 

Radius of a circle area where places are searched, in meters. The value ranges from 1 to 50000. The default value is **1000**. The digits after the decimal point are ignored. Error code 401 will be returned for any invalid value.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

query

 | 

string

 | 

No

 | 

Yes

 | 

Search keyword. The length of the parameter value ranges from 1 to 512.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

poiTypes

 | 

Array<string>

 | 

No

 | 

Yes

 | 

Huawei POI type of a place to search. The value range is the same as that of [HwLocationType](../appendixes/poi-types/document.md#section1662744719618).

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

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

Input language. The length of the parameter value ranges from 1 to 16. Refer to [Languages Supported by Place Search](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-language#section1629711151663) for supported language options.

If this parameter is not passed, the local language will be used by default. If an invalid value is passed, the local language will be used.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

pageSize

 | 

number

 | 

No

 | 

Yes

 | 

Number of records on each page. The value ranges from 1 to 20. The default value is **20**.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

pageIndex

 | 

number

 | 

No

 | 

Yes

 | 

Number of the current page. The value ranges from 1 to 500. The default value is **1**.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

NOTE:

pageIndex \* pageSize <= 500

 |
| 

sortRule

 | 

[SortRule](#section73559613164)

 | 

No

 | 

Yes

 | 

Sorting rule. The default value is [SortRule](#section73559613164).COMPOSITE.

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |

#### QueryAutoCompleteParams

Defines parameters for autocomplete.

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

query

 | 

string

 | 

No

 | 

No

 | 

Search keyword. The length of the parameter value ranges from 1 to 512.

 |
| 

location

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

Yes

 | 

Longitude and latitude of the search result.

 |
| 

radius

 | 

number

 | 

No

 | 

Yes

 | 

Search radius, in meters. The value ranges from 1 to 50000. The default value is **50000**. The digits after the decimal point are ignored. Error code 401 will be returned for any invalid value.

 |
| 

poiTypes

 | 

Array<string>

 | 

No

 | 

Yes

 | 

Huawei POI type of a place to search. The value range is the same as that of [HwLocationType](../appendixes/poi-types/document.md#section1662744719618).

 |
| 

cityId

 | 

string

 | 

No

 | 

Yes

 | 

City ID. This parameter is used to specify the city where places are searched. The length of the parameter value ranges from 1 to 32.

NOTE:

-   Chinese names of Hong Kong (China), and Macao (China), and cities in the Chinese mainland are supported.
-   For Hong Kong, Macao, and cities in the Chinese mainland, the value can be the city code with 3-4 digits or the administrative division code with 6 digits. For details, please refer to [City Codes and Administrative Division Codes](../appendixes/city-codes-and-administrative-division-codes/document.md).
-   The value can also be a city ID with 16-18 digits.

 |
| 

isCityLimit

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the search result must be in the specified city. This parameter needs to be used with **cityId**. The default value is **false**.

-   **true**: yes
-   **false**: no

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

Input language. The length of the parameter value ranges from 1 to 16. Refer to [Languages Supported by Place Search](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-language#section1629711151663) for supported language options.

If this parameter is not passed, the local language will be used by default. If an invalid value is passed, the local language will be used.

 |
| 

isChildren

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to return information about child nodes. The default value is **false**.

-   **true**: yes (Full information about child nodes will be returned.)
-   **false**: no

 |

#### SearchByIdParams

Defines parameters for place details search.

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

siteId

 | 

string

 | 

No

 | 

No

 | 

Address ID. The length of the parameter value ranges from 1 to 256.

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

Input language. The length of the parameter value ranges from 1 to 16. Refer to [Languages Supported by Place Search](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-language#section1629711151663) for supported language options.

If this parameter is not passed, the local language will be used by default. If an invalid value is passed, the local language will be used.

 |
| 

isChildren

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to return information about child nodes. The default value is **false**.

-   **true**: yes (Full information about child nodes will be returned.)
-   **false**: no

 |

#### ReverseGeocodeParams

Defines parameters for reverse geocoding.

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

Longitude and latitude for reverse geocoding.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

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

Input language. The length of the parameter value ranges from 1 to 16. Refer to [Languages Supported by Place Search](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-language#section1629711151663) for supported language options.

If this parameter is not passed, the local language will be used by default. If an invalid value is passed, the local language will be used.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

radius

 | 

number

 | 

No

 | 

Yes

 | 

Search radius, in meters. The value ranges from 0 to 1000. The default value is **1000**. The digits after the decimal point are ignored. Error code 401 will be returned for any invalid value.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

isExtension

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to return extended information such as POIs, AOIs, roads, and crosspoints. You are advised to set it to **true**. The default value is **false**.

-   **true**: yes
-   **false**: no. Only the division information is returned.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

NOTE:

In the extended information returned, there are a maximum of 30 POIs, 10 AOIs, 3 roads, and 1 crosspoint.

 |
| 

poiTypes

 | 

Array<string>

 | 

No

 | 

Yes

 | 

Huawei POI type of a place to search. The value range is the same as that of [HwLocationType](../appendixes/poi-types/document.md#section1662744719618).

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

isNearbyAoi

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to return nearby AOIs.

This parameter is valid only when **isExtension** is set to **true**.

You are advised to set this parameter to **true**. The default value is **false**.

-   **true**: returns nearby AOIs.
-   **false**: returns only AOIs specified by the passed longitude and latitude.

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

sortRule

 | 

[SortRule](#section73559613164)

 | 

No

 | 

Yes

 | 

POI sorting rule.

The default value is [SortRule](#section73559613164).DISTANCE, which indicates sorting by distance.

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |

#### GeocodeParams

Defines parameters for forward geocoding.

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

query

 | 

string

 | 

No

 | 

No

 | 

Address information. The length of the parameter value ranges from 1 to 512.

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

Input language. The length of the parameter value ranges from 1 to 16. Refer to [Languages Supported by Place Search](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-language#section1629711151663) for supported language options.

If this parameter is not passed, the local language will be used by default. If an invalid value is passed, the local language will be used.

 |
| 

bounds

 | 

[mapCommon.LatLngBounds](../mapcommon-map-attribute-model/document.md#section96341159111320)

 | 

No

 | 

Yes

 | 

Coordinate bounds of the search result.

 |

#### SearchByTextResult

Defines the keyword search result.

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

totalCount

 | 

number

 | 

No

 | 

No

 | 

Total number of records that meet the search criteria when the search is successful.

 |
| 

sites

 | 

Array<[Site](#section75488253219)\>

 | 

No

 | 

Yes

 | 

Search result returned upon a successful search.

 |

#### NearbySearchResult

Defines the nearby place search result.

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

totalCount

 | 

number

 | 

No

 | 

No

 | 

Total number of records that meet the search criteria when the search is successful.

 |
| 

sites

 | 

Array<[Site](#section75488253219)\>

 | 

No

 | 

Yes

 | 

Search result returned upon a successful search.

 |

#### QueryAutoCompleteResult

Defines the autocomplete result.

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

sites

 | 

Array<[Site](#section75488253219)\>

 | 

No

 | 

Yes

 | 

Autocomplete result.

 |

#### SearchByIdResult

Defines the place details search result.

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

site

 | 

[Site](#section75488253219)

 | 

No

 | 

Yes

 | 

Place details returned upon a successful search.

 |

#### ReverseGeocodeResult

Defines the reverse geocoding result.

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

addressComponent

 | 

[AddressComponent](#section1652881563212)

 | 

No

 | 

No

 | 

Address details.

 |
| 

addressDescription

 | 

string

 | 

No

 | 

No

 | 

Unstructured address text.

 |
| 

aois

 | 

Array<[Aoi](#section049863583319)\>

 | 

No

 | 

Yes

 | 

AOI information.

 |
| 

pois

 | 

Array<[ReverseGeocodePoi](#section862815423335)\>

 | 

No

 | 

Yes

 | 

POI information.

 |
| 

roads

 | 

Array<[Road](#section131351553173312)\>

 | 

No

 | 

Yes

 | 

Road information.

 |
| 

intersections

 | 

Array<[Intersection](#section114801402343)\>

 | 

No

 | 

Yes

 | 

Crosspoint information.

 |

#### GeocodeResult

Defines the forward geocoding result.

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

sites

 | 

Array<[Site](#section75488253219)\>

 | 

No

 | 

Yes

 | 

Search result returned upon a successful search.

 |

#### Site

Defines place details.

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

siteId

 | 

string

 | 

No

 | 

No

 | 

Unique ID of a place.

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

Name of a place.

 |
| 

formatAddress

 | 

string

 | 

No

 | 

Yes

 | 

Formatted detailed address of a place.

 |
| 

addressComponent

 | 

[AddressComponent](#section1652881563212)

 | 

No

 | 

No

 | 

Address details.

 |
| 

location

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

Yes

 | 

Longitude and latitude of a place.

 |
| 

viewport

 | 

[mapCommon.LatLngBounds](../mapcommon-map-attribute-model/document.md#section96341159111320)

 | 

No

 | 

Yes

 | 

Viewport of a place.

NOTE:

The [queryAutoComplete](#section20324320183912) API does not support returning this parameter.

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

Linear distance between a place and the location specified by the input parameter **location**, in meters.

NOTE:

Currently, this parameter is supported only for keyword search and nearby place search.

 |
| 

poi

 | 

[Poi](#section36139487328)

 | 

No

 | 

Yes

 | 

POI information about a place if the place is a POI.

 |
| 

utcOffset

 | 

number

 | 

No

 | 

Yes

 | 

Difference between the time zone of a place and the UTC time zone, in minutes.

NOTE:

This parameter is not supported for the autocomplete function.

 |

#### AddressComponent

Defines address details.

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

countryCode

 | 

string

 | 

No

 | 

Yes

 | 

Country/Region code.

 |
| 

countryName

 | 

string

 | 

No

 | 

Yes

 | 

Country name.

 |
| 

adminLevel1

 | 

string

 | 

No

 | 

Yes

 | 

Level-1 administrative division.

 |
| 

adminLevel2

 | 

string

 | 

No

 | 

Yes

 | 

Level-2 administrative division.

 |
| 

adminLevel3

 | 

string

 | 

No

 | 

Yes

 | 

Level-3 administrative division.

 |
| 

adminLevel4

 | 

string

 | 

No

 | 

Yes

 | 

Level-4 administrative division.

 |
| 

adminLevel5

 | 

string

 | 

No

 | 

Yes

 | 

Level-5 administrative division.

 |
| 

locality

 | 

string

 | 

No

 | 

Yes

 | 

locality.

 |
| 

subLocality1

 | 

string

 | 

No

 | 

Yes

 | 

Level-1 locality.

 |
| 

subLocality2

 | 

string

 | 

No

 | 

Yes

 | 

Level-2 locality.

 |
| 

neighborhoods

 | 

Array<string>

 | 

No

 | 

Yes

 | 

Neighborhood.

 |
| 

adminCode

 | 

string

 | 

No

 | 

Yes

 | 

[Administrative division code.](../appendixes/city-codes-and-administrative-division-codes/document.md)

NOTE:

The administrative division codes returned by the API cover all provinces, cities, districts/counties, and towns/streets in the Chinese mainland, Hong Kong (China), and Macao (China). The appendix provides only a sample of city administrative division codes.

 |
| 

postalCode

 | 

string

 | 

No

 | 

Yes

 | 

Postal code.

 |
| 

city

 | 

[City](#section12960326133219)

 | 

No

 | 

Yes

 | 

City information.

 |
| 

streetNumber

 | 

[StreetNumber](#section1710437103212)

 | 

No

 | 

Yes

 | 

Street number.

 |

#### City

Defines city information.

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

cityCode

 | 

string

 | 

No

 | 

Yes

 | 

City code.

 |
| 

cityId

 | 

string

 | 

No

 | 

Yes

 | 

City ID.

 |
| 

cityName

 | 

string

 | 

No

 | 

Yes

 | 

City name.

 |

#### StreetNumber

Defines a street number.

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

direction

 | 

string

 | 

No

 | 

Yes

 | 

Direction of an input point along a street.

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

Linear distance between a place and the location specified by the input parameter **location**, in meters.

 |
| 

location

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

Yes

 | 

Longitude and latitude of a street.

 |
| 

streetNumber

 | 

string

 | 

No

 | 

Yes

 | 

Street number.

 |
| 

streetName

 | 

string

 | 

No

 | 

Yes

 | 

Street name.

 |
| 

formatAddress

 | 

string

 | 

No

 | 

Yes

 | 

Formatted street address.

 |

#### Poi

Defines the POI information.

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

poiTypes

 | 

Array<string>

 | 

No

 | 

Yes

 | 

Huawei POI type. The value range is the same as that of [HwLocationType](../appendixes/poi-types/document.md#section1662744719618).

 |
| 

poiTypeIds

 | 

Array<string>

 | 

No

 | 

Yes

 | 

Huawei POI type ID. This parameter is reserved and is not used currently.

 |
| 

phone

 | 

string

 | 

No

 | 

Yes

 | 

Phone number.

 |
| 

internationalPhone

 | 

string

 | 

No

 | 

Yes

 | 

International phone number.

 |
| 

rating

 | 

number

 | 

No

 | 

Yes

 | 

Rating.

 |
| 

websiteUrl

 | 

string

 | 

No

 | 

Yes

 | 

Website URL.

 |
| 

openingHours

 | 

[OpeningHours](#section118078574321)

 | 

No

 | 

Yes

 | 

Business hours.

 |
| 

businessStatus

 | 

string

 | 

No

 | 

Yes

 | 

Business status.

-   **OPEN\_NOW**: open
-   **CLOSE\_NOW**: closed
-   **CLOSED\_TEMPORARILY**: temporarily closed
-   **CLOSED\_PERMANENTLY**: permanently closed
-   **STATUS\_UNKNOWN**: unknown

NOTE:

This parameter is returned only by the place details search API.

 |
| 

brand

 | 

string

 | 

No

 | 

Yes

 | 

Brand name.

 |
| 

email

 | 

string

 | 

No

 | 

Yes

 | 

Email address.

 |
| 

starRating

 | 

number

 | 

No

 | 

Yes

 | 

Star rating.

 |
| 

childNodes

 | 

Array<[ChildNode](#section13552162093312)\>

 | 

No

 | 

Yes

 | 

Child nodes of a POI.

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

POI icon URL.

 |
| 

description

 | 

string

 | 

No

 | 

Yes

 | 

Description.

 |
| 

abstractText

 | 

string

 | 

No

 | 

Yes

 | 

Abstract information.

 |
| 

comment

 | 

[Comment](#section123615297334)

 | 

No

 | 

Yes

 | 

Comment information about a POI.

 |

#### OpeningHours

Defines the business hours.

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

texts

 | 

Array<string>

 | 

No

 | 

Yes

 | 

Description of weekly opening hours of a place.

 |
| 

periods

 | 

Array<[Period](#section42941963337)\>

 | 

No

 | 

Yes

 | 

Opening hours of a place.

 |

#### Period

Defines the opening hours of a place.

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

open

 | 

[TimeOfWeek](#section46711483319)

 | 

No

 | 

Yes

 | 

Open time.

 |
| 

close

 | 

[TimeOfWeek](#section46711483319)

 | 

No

 | 

Yes

 | 

Close time.

 |

#### TimeOfWeek

Defines the time model.

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

week

 | 

number

 | 

No

 | 

Yes

 | 

**0**: Sunday

**1**: Monday

**2**: Tuesday

**3**: Wednesday

**4**: Thursday

**5**: Friday

**6**: Saturday

 |
| 

time

 | 

string

 | 

No

 | 

Yes

 | 

24-hour time in _hhmm_ format.

 |

#### ChildNode

Defines information about child nodes of a POI.

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

siteId

 | 

string

 | 

No

 | 

Yes

 | 

Location ID.

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

Name of a place.

 |
| 

formatAddress

 | 

string

 | 

No

 | 

Yes

 | 

Formatted detailed address of a place.

 |
| 

location

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

Yes

 | 

Longitude and latitude of a place.

 |
| 

poiTypes

 | 

Array<string>

 | 

No

 | 

Yes

 | 

Huawei POI type. The value range is the same as that of [HwLocationType](../appendixes/poi-types/document.md#section1662744719618).

 |

#### Comment

Defines comment information about a POI.

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

averageRating

 | 

number

 | 

No

 | 

Yes

 | 

Average rating.

 |
| 

total

 | 

number

 | 

No

 | 

Yes

 | 

Total number of comments.

 |

#### Aoi

Defines AOI information.

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

area

 | 

number

 | 

No

 | 

Yes

 | 

AOI area.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

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

Linear distance between a place and the location specified by the input parameter **location**, in meters.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

siteId

 | 

string

 | 

No

 | 

Yes

 | 

AOI ID.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

location

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

Yes

 | 

Longitude and latitude of a place.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

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

Name of a place.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

poiType

 | 

string

 | 

No

 | 

Yes

 | 

Huawei POI type. The value range is the same as that of [HwLocationType](../appendixes/poi-types/document.md#section1662744719618).

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

direction

 | 

string

 | 

No

 | 

Yes

 | 

Direction of the AOI at the input point.

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |

#### ReverseGeocodePoi

Defines the POI information of the reverse geocoding result.

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

address

 | 

string

 | 

No

 | 

Yes

 | 

Address.

 |
| 

direction

 | 

string

 | 

No

 | 

Yes

 | 

Direction of an input point towards the POI.

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

Linear distance between a place and the location specified by the input parameter **location**, in meters.

 |
| 

siteId

 | 

string

 | 

No

 | 

Yes

 | 

ID of a place.

 |
| 

location

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

Yes

 | 

Longitude and latitude of a place.

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

Name of a place.

 |
| 

poiType

 | 

string

 | 

No

 | 

Yes

 | 

Huawei POI type. The value range is the same as that of [HwLocationType](../appendixes/poi-types/document.md#section1662744719618).

 |

#### Road

Defines road information.

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

direction

 | 

string

 | 

No

 | 

Yes

 | 

Direction of an input point along a road.

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

Linear distance between a road and the location specified by the input parameter **location**, in meters.

 |
| 

siteId

 | 

string

 | 

No

 | 

Yes

 | 

Road ID.

 |
| 

location

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

Yes

 | 

Longitude and latitude of a road.

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

Road name.

 |

#### Intersection

Defines crosspoint information.

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

direction

 | 

string

 | 

No

 | 

Yes

 | 

Direction of an input point towards a crosspoint.

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

Linear distance between a crosspoint and the location specified by the input parameter **location**, in meters.

 |
| 

siteId

 | 

string

 | 

No

 | 

Yes

 | 

Crosspoint ID.

 |
| 

location

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

Yes

 | 

Longitude and latitude of a crosspoint.

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

Crosspoint name.

 |
