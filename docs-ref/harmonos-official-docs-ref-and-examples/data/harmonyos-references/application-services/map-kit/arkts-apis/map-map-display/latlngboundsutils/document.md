# LatLngBoundsUtils

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### LatLngBoundsUtils

**LatLngBounds** utility class.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

#### \[h2\]contains

static contains(bounds: mapCommon.LatLngBounds, position: mapCommon.LatLng): boolean

Checks whether a **LatLngBounds** object contains specified location coordinates.

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

bounds

 | 

[mapCommon.LatLngBounds](../../mapcommon-map-attribute-model/document.md#section96341159111320)

 | 

Yes

 | 

**LatLngBounds** object.

 |
| 

position

 | 

[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

Yes

 | 

Location coordinates.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

**true**: The **LatLngBounds** object contains the location.

**false**: The **LatLngBounds** object does not contain the location.

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

**Example**:

let bounds: mapCommon.LatLngBounds = {
  southwest: {
    latitude: 31.98, longitude: 118.766
  },
  northeast: {
    latitude: 32.08, longitude: 118.066
  }
};
let result: boolean = map.LatLngBoundsUtils.contains(bounds, { latitude: 15, longitude: 15 });

#### \[h2\]contains

static contains(src: mapCommon.LatLngBounds, target: mapCommon.LatLngBounds): boolean

Checks whether a **LatLngBounds** object contains the target region.

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

src

 | 

[mapCommon.LatLngBounds](../../mapcommon-map-attribute-model/document.md#section96341159111320)

 | 

Yes

 | 

**LatLngBounds** object.

 |
| 

target

 | 

[mapCommon.LatLngBounds](../../mapcommon-map-attribute-model/document.md#section96341159111320)

 | 

Yes

 | 

Target region.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

**true**: The **LatLngBounds** object contains the target region.

**false**: The **LatLngBounds** object does not contain the target region.

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

**Example**:

let src: mapCommon.LatLngBounds = {
  southwest: {
    latitude: 31.98, longitude: 118
  },
  northeast: {
    latitude: 31.08, longitude: 119
  }
};
let target: mapCommon.LatLngBounds = {
  southwest: {
    latitude: 33, longitude: 120
  },
  northeast: {
    latitude: 34, longitude: 121
  }
};

let result: boolean = map.LatLngBoundsUtils.contains(src, target);

#### \[h2\]getCenter

static getCenter(bounds: mapCommon.LatLngBounds): mapCommon.LatLng

Obtains the longitude-latitude coordinates of the center of a **LatLngBounds** object.

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

bounds

 | 

[mapCommon.LatLngBounds](../../mapcommon-map-attribute-model/document.md#section96341159111320)

 | 

Yes

 | 

**LatLngBounds** object.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

Longitude-latitude coordinates of the center.

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

**Example**:

let bounds: mapCommon.LatLngBounds = {
  southwest: {
    latitude: 31, longitude: 118
  },
  northeast: {
    latitude: 33, longitude: 119
  }
};
let center: mapCommon.LatLng = map.LatLngBoundsUtils.getCenter(bounds);

#### \[h2\]include

static include(position: mapCommon.LatLng, bounds?: mapCommon.LatLngBounds): mapCommon.LatLngBounds

Obtains a **LatLngBounds** object that contains a specified location.

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

position

 | 

[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

Yes

 | 

Location coordinates.

 |
| 

bounds

 | 

[mapCommon.LatLngBounds](../../mapcommon-map-attribute-model/document.md#section96341159111320)

 | 

No

 | 

**LatLngBounds** object.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[mapCommon.LatLngBounds](../../mapcommon-map-attribute-model/document.md#section96341159111320)

 | 

**LatLngBounds** object that contains the specified location.

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

**Example**:

let resultBounds: mapCommon.LatLngBounds = map.LatLngBoundsUtils.include({ latitude: 31, longitude: 118 });
