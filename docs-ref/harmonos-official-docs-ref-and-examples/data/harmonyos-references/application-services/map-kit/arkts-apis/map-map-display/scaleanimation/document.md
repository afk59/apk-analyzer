# ScaleAnimation

#### Module Import

import { map } from '@kit.MapKit';

#### ScaleAnimation

Animation class for controlling zooming, which inherits from [Animation](../animation/document.md).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

#### \[h2\]constructor

constructor(fromX: number, toX: number, fromY: number, toY: number)

Constructor, which is used to construct an animation instance for zoom control.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/SMah0RoeTcyG859w5_02aw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062512Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E31DBE025B4CE478EF7DDBA2789FB826F48BB3D8916118C455F7E18FAAC7EA3)

The value **0** indicates that an animation zooms out until it disappears.

The value **1** indicates no zooming.

A value less than **1** indicates zoom-out.

A value greater than **1** indicates zoom-in.

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

fromX

 | 

number

 | 

Yes

 | 

Horizontal zoom level applied when the animation starts.

 |
| 

toX

 | 

number

 | 

Yes

 | 

Horizontal zoom level applied when the animation ends.

 |
| 

fromY

 | 

number

 | 

Yes

 | 

Vertical zoom level applied when the animation starts.

 |
| 

toY

 | 

number

 | 

Yes

 | 

Vertical zoom level applied when the animation ends.

 |

**Example**:

let animation: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
