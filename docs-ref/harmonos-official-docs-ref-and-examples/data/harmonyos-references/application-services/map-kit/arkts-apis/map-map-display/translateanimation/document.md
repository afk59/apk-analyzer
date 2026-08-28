# TranslateAnimation

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### TranslateAnimation

Animation class for controlling movement, which inherits from [Animation](../animation/document.md).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

#### \[h2\]constructor

constructor(target: mapCommon.LatLng)

Constructor, which is used to construct an animation instance for movement control.

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

target

 | 

[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

Yes

 | 

Latitude and longitude of the movement target position.

 |

**Example**:

let target: mapCommon.LatLng = { latitude: 31, longitude: 118 };
let animation: map.TranslateAnimation = new map.TranslateAnimation(target);
