# BasePriorityOverlay

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### BasePriorityOverlay

Base class of overlays with priority control, which inherits from [BaseOverlay](../baseoverlay/document.md). [PointAnnotation](../pointannotation/document.md) and [Bubble](../bubble/document.md) inherit from this base class.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

#### \[h2\]getMaxZoom

getMaxZoom(): number

Obtains the maximum zoom level of an overlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Maximum zoom level of an overlay.

 |

**Example**:

// Use a PointAnnotation as an example.
let pointAnnotationOptions: mapCommon.PointAnnotationParams = {
  position: {
    latitude: 32.120750,
    longitude: 118.788765
  },
  titles: \[{
    content: "Nanjing Confucius Temple",
  }\],
  // The icon must be stored in the **resources/rawfile** directory.
  icon: 'icon.png'
};
let pointAnnotation: map.PointAnnotation = await this.mapController.addPointAnnotation(pointAnnotationOptions);
let maxZoom: number = pointAnnotation.getMaxZoom();

#### \[h2\]getMinZoom

getMinZoom(): number

Obtains the minimum zoom level of an overlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Minimum zoom level of an overlay.

 |

**Example**:

// Use a PointAnnotation as an example.
let minZoom: number = pointAnnotation.getMinZoom();

#### \[h2\]setPriority

setPriority(priority: number): void

Sets the collision priority of an overlay. A larger value indicates a lower priority.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

priority

 | 

number

 | 

Yes

 | 

Collision priority of an overlay.

 |

**Example**:

// Use a PointAnnotation as an example.
pointAnnotation.setPriority(100);

#### \[h2\]setZoom

setZoom(minZoom: number, maxZoom: number): void

Sets the zoom levels of an overlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

minZoom

 | 

number

 | 

Yes

 | 

Minimum zoom level of an overlay. The value ranges from 2 to 20.

If the input value is greater than 20, the minimum zoom level will be 20.

If the input value is less than 2, the minimum zoom level will be 2.

NOTE:

If the value of **minZoom** is greater than that of **maxZoom**, this method will not work.

 |
| 

maxZoom

 | 

number

 | 

Yes

 | 

Maximum zoom level of an overlay. The value ranges from 2 to 20.

If the input value is greater than 20, the maximum zoom level will be 20.

If the input value is less than 2, the maximum zoom level will be 2.

 |

**Example**:

// Use a PointAnnotation as an example.
pointAnnotation.setZoom(3, 10);

#### \[h2\]setAnimation

setAnimation(animation: Animation): void

Sets the animation of an overlay. Only [AlphaAnimation](../alphaanimation/document.md), [ScaleAnimation](../scaleanimation/document.md), and [AnimationSet](../animationset/document.md) are supported.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

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

Animation.

 |

**Example**:

let animation: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
animation.setDuration(3000);
let callbackStart = () => {
  console.info("animationStart", \`callback\`);
};
let callbackEnd = () => {
  console.info("animationEnd", \`callback\`);
};
animation.on("animationStart", callbackStart);
animation.on("animationEnd", callbackEnd);
animation.setFillMode(map.AnimationFillMode.BACKWARDS);
animation.setRepeatMode(map.AnimationRepeatMode.RESTART);
animation.setRepeatCount(100);

pointAnnotation.setAnimation(animation);

#### \[h2\]startAnimation

startAnimation(): void

Starts the animation of an overlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Example**:

let animation: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
animation.setDuration(3000);
let callbackStart = () => {
  console.info("animationStart", \`callback\`);
};
let callbackEnd = () => {
  console.info("animationEnd", \`callback\`);
};
animation.on("animationStart", callbackStart);
animation.on("animationEnd", callbackEnd);
animation.setFillMode(map.AnimationFillMode.BACKWARDS);
animation.setRepeatMode(map.AnimationRepeatMode.RESTART);
animation.setRepeatCount(100);

pointAnnotation.setAnimation(animation);
pointAnnotation.startAnimation();

#### \[h2\]clearAnimation

clearAnimation(): void

Clears the animation of an overlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Example**:

pointAnnotation.clearAnimation();
