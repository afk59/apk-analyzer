# RotateAnimation

#### Module Import

import { map } from '@kit.MapKit';

#### RotateAnimation

Animation class for controlling rotation, which inherits from [Animation](../animation/document.md).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

#### \[h2\]constructor

constructor(fromDegree: number, toDegree: number)

Constructor, which is used to construct an animation instance for rotation control.

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

fromDegree

 | 

number

 | 

Yes

 | 

Initial angle. The value ranges from 0 to 360.

 |
| 

toDegree

 | 

number

 | 

Yes

 | 

Target angle. The value ranges from 0 to 360.

 |

**Example**:

let animation: map.RotateAnimation = new map.RotateAnimation(15, 150);
