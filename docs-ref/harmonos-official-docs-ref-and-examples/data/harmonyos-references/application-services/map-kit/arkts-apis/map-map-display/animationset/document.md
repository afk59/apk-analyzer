# AnimationSet

#### Module Import

import { map } from '@kit.MapKit';

#### AnimationSet

Set of animation classes, which inherit from [Animation](../animation/document.md).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

#### \[h2\]constructor

constructor(shareInterpolator: boolean)

Constructor, which is used to construct an instance of the animation class set.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/LSRGqWnPSoeM2sSy1g_EjA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062512Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D39A3410B2D1376A3CACC0CAB9AB25A8D8CDABC0B3C51B253BBDBD993D31836)

This API inherits from the [Animation](../animation/document.md) method. The interpolator is shared only when **shareInterpolator** is set to **true**. Other attributes are not shared and cannot be set.

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

shareInterpolator

 | 

boolean

 | 

Yes

 | 

Indicates whether to share the interpolator.

-   **true**: yes
-   **false**: no

 |

**Example**:

let animation1: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
let animation2: map.RotateAnimation = new map.RotateAnimation(15, 150);
let animation3: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
let animation = new map.AnimationSet(true);
animation.setInterpolator(Curve.Linear);
animation.addAnimation(animation1);
animation.addAnimation(animation2);
animation.addAnimation(animation3);
animation.clearAnimation();

#### \[h2\]addAnimation

addAnimation(animation: Animation): void

Adds an animation.

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

animation

 | 

[Animation](../animation/document.md)

 | 

Yes

 | 

Adds an animation.

 |

**Example**:

let animation1: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
let animation2: map.RotateAnimation = new map.RotateAnimation(15, 150);
let animation3: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
let animation = new map.AnimationSet(true);
animation.addAnimation(animation1);
animation.addAnimation(animation2);
animation.addAnimation(animation3);

#### \[h2\]clearAnimation

clearAnimation(): void

Deletes animations.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Example**:

let animation1: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
let animation2: map.RotateAnimation = new map.RotateAnimation(15, 150);
let animation3: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
let animation = new map.AnimationSet(true);
animation.addAnimation(animation1);
animation.addAnimation(animation2);
animation.addAnimation(animation3);
animation.clearAnimation();
