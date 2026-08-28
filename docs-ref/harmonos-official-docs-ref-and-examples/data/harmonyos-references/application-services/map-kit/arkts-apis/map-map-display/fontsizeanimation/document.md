# FontSizeAnimation

#### Module Import

import { map } from '@kit.MapKit';

#### FontSizeAnimation

Animation class for controlling the font size, which inherits from [Animation](../animation/document.md).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

#### \[h2\]constructor

constructor(fromSize: number, toSize: number)

Constructor, which is used to construct an animation instance for font size control.

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

fromSize

 | 

number

 | 

Yes

 | 

Initial font size, in pixels. The value ranges from 0 to 100.

 |
| 

toSize

 | 

number

 | 

Yes

 | 

Target font size, in pixels. The value ranges from 0 to 100.

 |

**Example**:

let animation: map.FontSizeAnimation = new map.FontSizeAnimation(5, 25);
