# petalMaps (Starting the Map App)

This module provides the function of starting the map app.

**Start version**: 5.0.3(15)

#### Module Import

import { petalMaps } from '@kit.MapKit';

#### openMapHomePage

openMapHomePage(context: common.Context): Promise<void>

Opens the home page of Petal Maps based on the specified parameters. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 19 or earlier, this API is supported on phones and tablets but returns error code 801 on other devices. For version 20 or later, this API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.0.3(15)

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

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

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

1002600014

 | 

Failed to start the map app.

 |
| 

801

 | 

Capability not supported. Failed to call the API due to limited device capabilities.

 |

**Example**:

await petalMaps.openMapHomePage(this.getUIContext().getHostContext());

#### openMapPoiDetail

openMapPoiDetail(context: common.Context, poiDetailParams: PoiDetailParams): Promise<void>

Opens the POI details page of Petal Maps based on the specified parameters. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 19 or earlier, this API is supported on phones and tablets but returns error code 801 on other devices. For version 20 or later, this API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.0.3(15)

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

poiDetailParams

 | 

[PoiDetailParams](#section1555293218278)

 | 

Yes

 | 

Parameters for POI details.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

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

1002600014

 | 

Failed to start the map app.

 |
| 

801

 | 

Capability not supported. Failed to call the API due to limited device capabilities.

 |

**Example**:

let params: petalMaps.PoiDetailParams = {
  destinationPosition: {
    latitude: 30.983015468224288,
    longitude: 118.78058590757131
  }
};
await petalMaps.openMapPoiDetail(this.getUIContext().getHostContext(), params);

#### openMapTextSearch

openMapTextSearch(context: common.Context, textSearchParams: TextSearchParams): Promise<void>

Opens the text search page of Petal Maps based on the specified parameters. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 19 or earlier, this API is supported on phones and tablets but returns error code 801 on other devices. For version 20 or later, this API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.0.3(15)

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

textSearchParams

 | 

[TextSearchParams](#section810823717266)

 | 

Yes

 | 

Parameters for text search.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

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

1002600014

 | 

Failed to start the map app.

 |
| 

801

 | 

Capability not supported. Failed to call the API due to limited device capabilities.

 |

**Example**:

let params: petalMaps.TextSearchParams = {
  destinationName: 'Cloud Park'
};
await petalMaps.openMapTextSearch(this.getUIContext().getHostContext(), params);

#### openMapRoutePlan

openMapRoutePlan(context: common.Context, routePlanParams: RoutePlanParams): Promise<void>

Opens the route planning page of Petal Maps based on the specified parameters. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 19 or earlier, this API is supported on phones and tablets but returns error code 801 on other devices. For version 20 or later, this API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.0.3(15)

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

routePlanParams

 | 

[RoutePlanParams](#section491624219261)

 | 

Yes

 | 

Parameters for route planning.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

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

1002600014

 | 

Failed to start the map app.

 |
| 

801

 | 

Capability not supported. Failed to call the API due to limited device capabilities.

 |

**Example**:

let params: petalMaps.RoutePlanParams = {
  destinationPosition: {
    latitude: 31.983015468224288,
    longitude: 118.78058590757131
  }
};
await petalMaps.openMapRoutePlan(this.getUIContext().getHostContext(), params);

#### openMapNavi

openMapNavi(context: common.Context, naviParams: NaviParams): Promise<void>

Opens the navigation page of Petal Maps based on the specified parameters. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 19 or earlier, this API is supported on phones and tablets but returns error code 801 on other devices. For version 20 or later, this API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.0.3(15)

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

naviParams

 | 

[NaviParams](#section7249174522611)

 | 

Yes

 | 

Parameters for navigation.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

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

1002600014

 | 

Failed to start the map app.

 |
| 

801

 | 

Capability not supported. Failed to call the API due to limited device capabilities.

 |

**Example**:

let params: petalMaps.NaviParams = {
  destinationPosition: {
    latitude: 31.983015468224288,
    longitude: 118.78058590757131
  }
};
await petalMaps.openMapNavi(this.getUIContext().getHostContext(), params);

#### openMapTaxi

openMapTaxi(context: common.Context, taxiParams: TaxiParams): Promise<void>

Opens the ride hailing screen of the map app based on the specified parameters. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 21 or later, this API is supported on phones and tablets but returns error code 801 on other devices.

**Start version**: 6.0.1(21)

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

taxiParams

 | 

[TaxiParams](#section1625316256212)

 | 

Yes

 | 

Ride hailing parameters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

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

1002600014

 | 

Failed to start the map app.

 |
| 

801

 | 

Capability not supported. Failed to call the API due to limited device capabilities.

 |

**Example**:

let params: petalMaps.TaxiParams = {
  destinationPosition: {
    latitude: 31.983015468224288,
    longitude: 118.78058590757131
  }
};
await petalMaps.openMapTaxi(this.getUIContext().getHostContext(), params);

#### PoiDetailParams

Parameters for POI details.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 19 or earlier, this API is supported on phones and tablets but returns error code 801 on other devices. For version 20 or later, this API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.0.3(15)

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

destinationPosition

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

No

 | 

Coordinates of the destination.

Value range: \[-180, 180) (longitude); \[-85.2, 85.2\] (latitude). Error code 401 will be returned for any invalid value.

 |
| 

destinationName

 | 

string

 | 

No

 | 

Yes

 | 

Name of the destination. If a name exceeds the display limit, the overflowing portion will be replaced with an ellipsis (...).

 |
| 

destinationPoiId

 | 

string

 | 

No

 | 

Yes

 | 

POI ID of the destination.

When both the POI ID and coordinates are passed in, the POI ID will be used preferentially.

 |
| 

zoom

 | 

number

 | 

No

 | 

Yes

 | 

Map zoom level. The value ranges from 3 to 20. The default value is **17**. If an invalid value is passed, the default value will be used.

NOTE:

When **destinationPoiId** is set, the map zoom level cannot be customized.

**Start version**: 6.0.1(21)

 |
| 

coordinateType

 | 

[mapCommon.CoordinateType](../mapcommon-map-attribute-model/document.md#section78948324526)

 | 

No

 | 

Yes

 | 

Coordinate system of the map. The default value is [mapCommon.CoordinateType](../mapcommon-map-attribute-model/document.md#section78948324526).GCJ02. If an invalid value is passed, the default value will be used.

**Start version**: 6.0.1(21)

 |

**Example**:

let params: petalMaps.PoiDetailParams = {
  destinationPosition: {
    latitude: 30.983015468224288,
    longitude: 118.78058590757131
  }
};

#### TextSearchParams

Parameters for text search.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 19 or earlier, this API is supported on phones and tablets but returns error code 801 on other devices. For version 20 or later, this API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.0.3(15)

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

destinationName

 | 

string

 | 

No

 | 

Yes

 | 

Name of the destination. If a name exceeds the display limit, the overflowing portion will be replaced with an ellipsis (...).

 |

**Example**:

let params: petalMaps.TextSearchParams = {
  destinationName: 'Cloud Park'
};

#### RoutePlanParams

Parameters for route planning.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 19 or earlier, this API is supported on phones and tablets but returns error code 801 on other devices. For version 20 or later, this API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.0.3(15)

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

originPosition

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

Yes

 | 

Coordinates of the departure place. The default value is the user's current coordinates.

Value range: \[-180, 180) (longitude); \[-85.2, 85.2\] (latitude). Error code 401 will be returned for any invalid value.

 |
| 

originName

 | 

string

 | 

No

 | 

Yes

 | 

Name of the departure place. If a name exceeds the display limit, the overflowing portion will be replaced with an ellipsis (...).

 |
| 

originPoiId

 | 

string

 | 

No

 | 

Yes

 | 

POI ID of the departure place.

When both the POI ID and coordinates are passed in, the POI ID will be used preferentially.

 |
| 

destinationPosition

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

No

 | 

Coordinates of the destination.

Value range: \[-180, 180) (longitude); \[-85.2, 85.2\] (latitude). Error code 401 will be returned for any invalid value.

 |
| 

destinationName

 | 

string

 | 

No

 | 

Yes

 | 

Name of the destination. If a name exceeds the display limit, the overflowing portion will be replaced with an ellipsis (...).

 |
| 

destinationPoiId

 | 

string

 | 

No

 | 

Yes

 | 

POI ID of the destination.

When both the POI ID and coordinates are passed in, the POI ID will be used preferentially.

 |
| 

vehicleType

 | 

[VehicleType](#section73559613164)

 | 

No

 | 

Yes

 | 

Mode of transportation.

The default value is **[VehicleType](#section73559613164).DRIVING**. If an invalid value is passed, the default value will be used.

 |
| 

coordinateType

 | 

[mapCommon.CoordinateType](../mapcommon-map-attribute-model/document.md#section78948324526)

 | 

No

 | 

Yes

 | 

Coordinate system of the map. The default value is [mapCommon.CoordinateType](../mapcommon-map-attribute-model/document.md#section78948324526).GCJ02. If an invalid value is passed, the default value will be used.

**Start version**: 6.0.1(21)

 |

**Example**:

let params: petalMaps.RoutePlanParams = {
  destinationPosition: {
    latitude: 31.983015468224288,
    longitude: 118.78058590757131
  }
};

#### NaviParams

Parameters for navigation.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 19 or earlier, this API is supported on phones and tablets but returns error code 801 on other devices. For version 20 or later, this API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.0.3(15)

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

destinationPosition

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

No

 | 

Coordinates of the destination.

Value range: \[-180, 180) (longitude); \[-85.2, 85.2\] (latitude). Error code 401 will be returned for any invalid value.

 |
| 

destinationName

 | 

string

 | 

No

 | 

Yes

 | 

Name of the destination. If a name exceeds the display limit, the overflowing portion will be replaced with an ellipsis (...).

 |
| 

destinationPoiId

 | 

string

 | 

No

 | 

Yes

 | 

POI ID of the destination.

When both the POI ID and coordinates are passed in, the POI ID will be used preferentially.

 |
| 

vehicleType

 | 

[VehicleType](#section73559613164)

 | 

No

 | 

Yes

 | 

Mode of transportation.

The default value is **[VehicleType](#section73559613164).DRIVING**. If an invalid value is passed, the default value will be used.

 |
| 

originPosition

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

Yes

 | 

Coordinates of the departure place. The default value is the user's current coordinates.

Value range: \[-180, 180) (longitude); \[-85.2, 85.2\] (latitude). Error code 401 will be returned for any invalid value.

**Start version**: 6.0.1(21)

 |
| 

originName

 | 

string

 | 

No

 | 

Yes

 | 

Name of the departure place. If a name exceeds the display limit, the overflowing portion will be replaced with an ellipsis (...).

**Start version**: 6.0.1(21)

 |
| 

originPoiId

 | 

string

 | 

No

 | 

Yes

 | 

POI ID of the departure place.

When both the POI ID and coordinates are passed in, the POI ID will be used preferentially.

**Start version**: 6.0.1(21)

 |
| 

coordinateType

 | 

[mapCommon.CoordinateType](../mapcommon-map-attribute-model/document.md#section78948324526)

 | 

No

 | 

Yes

 | 

Coordinate system of the map. The default value is [mapCommon.CoordinateType](../mapcommon-map-attribute-model/document.md#section78948324526).GCJ02. If an invalid value is passed, the default value will be used.

**Start version**: 6.0.1(21)

 |

**Example**:

let params: petalMaps.NaviParams = {
  destinationPosition: {
    latitude: 31.983015468224288,
    longitude: 118.78058590757131
  }
};

#### VehicleType

Mode of transportation. Currently, the map app supports only driving, walking, cycling, and public transit.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 19 or earlier, this API is supported on phones and tablets but returns error code 801 on other devices. For version 20 or later, this API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.0.3(15)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

DRIVING

 | 

0

 | 

Driving.

 |
| 

WALKING

 | 

1

 | 

Walking.

 |
| 

CYCLING

 | 

2

 | 

Cycling.

 |
| 

TRANSIT

 | 

3

 | 

Public transit.

**Start version**: 6.0.1(21)

 |

#### TaxiParams

Defines parameters for ride hailing.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 21 or later, this API is supported on phones and tablets but returns error code 801 on other devices.

**Start version**: 6.0.1(21)

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

destinationPosition

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

No

 | 

Coordinates of the destination.

Value range: \[-180, 180) (longitude); \[-85.2, 85.2\] (latitude). Error code 401 will be returned for any invalid value.

 |
| 

destinationName

 | 

string

 | 

No

 | 

Yes

 | 

Name of the destination. If a name exceeds the display limit, the overflowing portion will be replaced with an ellipsis (...).

 |
| 

destinationPoiId

 | 

string

 | 

No

 | 

Yes

 | 

POI ID of the destination.

When both the POI ID and coordinates are passed in, the POI ID will be used preferentially.

 |
| 

originPosition

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

Yes

 | 

Coordinates of the departure place. The default value is the user's current coordinates.

Value range: \[-180, 180) (longitude); \[-85.2, 85.2\] (latitude). Error code 401 will be returned for any invalid value.

 |
| 

originName

 | 

string

 | 

No

 | 

Yes

 | 

Name of the departure place. If a name exceeds the display limit, the overflowing portion will be replaced with an ellipsis (...).

 |
| 

originPoiId

 | 

string

 | 

No

 | 

Yes

 | 

POI ID of the departure place.

When both the POI ID and coordinates are passed in, the POI ID will be used preferentially.

 |
| 

coordinateType

 | 

[mapCommon.CoordinateType](../mapcommon-map-attribute-model/document.md#section78948324526)

 | 

No

 | 

Yes

 | 

Coordinate system of the map. The default value is [mapCommon.CoordinateType](../mapcommon-map-attribute-model/document.md#section78948324526).GCJ02. If an invalid value is passed, the default value will be used.

 |

**Example**:

let params: petalMaps.TaxiParams = {
  destinationPosition: {
    latitude: 31.983015468224288,
    longitude: 118.78058590757131
  }
};
