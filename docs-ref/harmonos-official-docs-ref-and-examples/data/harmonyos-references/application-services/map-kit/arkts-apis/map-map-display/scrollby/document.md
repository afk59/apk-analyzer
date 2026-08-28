# scrollBy

#### Module Import

import { map } from '@kit.MapKit';

#### scrollBy

scrollBy(x: number, y: number): CameraUpdate

Moves the map center point by pixel.

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

x

 | 

number

 | 

Yes

 | 

Number of pixels to scroll horizontally. A positive value indicates that the visible region moves rightwards, while a negative value indicates that the visible region moves leftwards. The unit is px.

 |
| 

y

 | 

number

 | 

Yes

 | 

Number of pixels to scroll vertically. A positive value indicates that the visible region moves downwards, while a negative value indicates that the visible region moves upwards. The unit is px.

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

let cameraUpdate: map.CameraUpdate = map.scrollBy(100, 200);
