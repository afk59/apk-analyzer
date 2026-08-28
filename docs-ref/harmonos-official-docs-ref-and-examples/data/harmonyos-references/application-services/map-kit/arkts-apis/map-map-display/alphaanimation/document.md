# AlphaAnimation

#### Module Import

import { map } from '@kit.MapKit';

#### AlphaAnimation

Animation class for controlling the opacity, which inherits from [Animation](../animation/document.md).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

#### \[h2\]constructor

constructor(fromAlpha: number, toAlpha: number)

Constructor, which is used to construct an animation instance for opacity control.

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

fromAlpha

 | 

number

 | 

Yes

 | 

Initial opacity. The value ranges from 0 (completely transparent) to 1 (opaque).

 |
| 

toAlpha

 | 

number

 | 

Yes

 | 

Target opacity. The value ranges from 0 (completely transparent) to 1 (opaque).

 |

**Example**:

let animation: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
