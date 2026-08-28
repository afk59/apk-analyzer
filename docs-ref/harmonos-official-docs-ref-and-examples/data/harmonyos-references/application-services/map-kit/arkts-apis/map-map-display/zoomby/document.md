# zoomBy

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### zoomBy

zoomBy(amount: number, focus?: mapCommon.MapPoint): CameraUpdate

Zooms in or out on the map by a specified value with the specified pixel point as the center.

The upper left vertex of the screen is used as the (0, 0) point. A positive value of **focus.positionX** indicates that the visible region moves rightwards, while a negative value indicates that the visible region moves leftwards. A positive value of **focus.positionY** indicates that the visible region moves downwards, while a negative value indicates that the visible region moves upwards.

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

amount

 | 

number

 | 

Yes

 | 

Map zoom level increment.

 |
| 

focus

 | 

[mapCommon.MapPoint](../../mapcommon-map-attribute-model/document.md#section123881566186)

 | 

No

 | 

Map center's coordinates on the screen.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[CameraUpdate](../cameraupdate/document.md)

 | 

Description of changes to the camera position.

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

let focus: mapCommon.MapPoint = {
  positionX: 100,
  positionY: 200
};
let cameraUpdate: map.CameraUpdate = map.zoomBy(10, focus);
