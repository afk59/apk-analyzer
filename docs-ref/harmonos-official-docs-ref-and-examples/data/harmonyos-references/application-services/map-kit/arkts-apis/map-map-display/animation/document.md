# Animation

#### Module Import

import { map } from '@kit.MapKit';

#### Animation

Animation abstract class.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Example**:

let animation = new map.RotateAnimation(0, 270);
// Animation execution duration.
animation.setDuration(2000);

// Post-animation state.
animation.setFillMode(map.AnimationFillMode.BACKWARDS);

// Animation replay mode.
animation.setRepeatMode(map.AnimationRepeatMode.REVERSE);

// Number of times that the animation is replayed.
animation.setRepeatCount(100);

// Set the animation listener based on the development requirements.
let callbackStart = () => {
  console.info("animationStart", \`callback\`);
};
let callbackEnd = () => {
  console.info("animationEnd", \`callback\`);
};
animation.on("animationStart", callbackStart);
animation.on("animationEnd", callbackEnd);

#### \[h2\]setDuration

setDuration(duration: number): void

Sets the animation duration.

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

duration

 | 

number

 | 

Yes

 | 

Animation duration, in milliseconds. The default value is **250**. The value must be greater than or equal to 0.

 |

**Example**:

animation.setDuration(3000);

#### \[h2\]setFillMode

setFillMode(fillMode: AnimationFillMode): void

Sets the post-animation state.

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

fillMode

 | 

[AnimationFillMode](../animationfillmode/document.md)

 | 

Yes

 | 

Post-animation state. The default value is [AnimationFillMode](../animationfillmode/document.md).FORWARDS.

 |

**Example**:

animation.setFillMode(map.AnimationFillMode.BACKWARDS);

#### \[h2\]setInterpolator

setInterpolator(curve: Curves.Curve): void

Sets an animation interpolator.

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

curve

 | 

[Curves.Curve](../../../../../application-framework/arkui/arkts-api/ui/ohos-curves-interpolation-calculation/document.md#curve)

 | 

Yes

 | 

Animation interpolator. The default value is [Curve](../../../../../application-framework/arkui/arkts-api/ui/ohos-curves-interpolation-calculation/document.md#curve).Linear.

 |

**Example**:

animation.setInterpolator(Curve.Linear);

#### \[h2\]setRepeatCount

setRepeatCount(repeatCount: number): void

Sets the number of times that an animation is replayed.

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

repeatCount

 | 

number

 | 

Yes

 | 

Number of times that an animation is replayed. The default value is **0**.

-   Positive number: The animation is executed repeatedly based on the value of this parameter.
-   **0**: The animation is not replayed.
-   **\-1**: The animation is replayed an unlimited number of times.
-   Value less than -1: The default value **0** is used.
-   Invalid value: The default value **0** is used.

 |

**Example**:

animation.setRepeatCount(100);

#### \[h2\]setRepeatMode

setRepeatMode(repeatMode: AnimationRepeatMode): void

Sets the animation replay mode. By default, the animation is replayed from the start.

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

repeatMode

 | 

[AnimationRepeatMode](../animationrepeatmode/document.md)

 | 

Yes

 | 

Animation replay mode. The default value is [AnimationRepeatMode](../animationrepeatmode/document.md).RESTART.

 |

**Example**:

animation.setRepeatMode(map.AnimationRepeatMode.RESTART);

#### \[h2\]on('start')

on(type: 'start', callback: Callback<void>): void

Listens for animation start events. This API returns the result asynchronously through a callback.

You are advised to use [animation.on(type: 'animationStart')](#section1282619121137).

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

type

 | 

string

 | 

Yes

 | 

**'start'**: Animation start events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

animation.on("start", () => {
  console.info(\`start alphaAnimation\`);
});

#### \[h2\]off('start')

off(type: 'start', callback: Callback<void>): void

Cancels listening for animation start events. This API returns the result asynchronously through a callback.

You are advised to use [animation.off(type: 'animationStart')](#section983316121834).

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

type

 | 

string

 | 

Yes

 | 

**'start'**: Animation start events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

animation.off("start", () => {
  console.info(\`start alphaAnimation\`);
});

#### \[h2\]on('end')

on(type: 'end', callback: Callback<void>): void

Listens for animation end events. This API returns the result asynchronously through a callback.

You are advised to use [animation.on(type: 'animationEnd')](#section1184051219311).

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

type

 | 

string

 | 

Yes

 | 

**'end'**: Animation end events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

animation.on("end", () => {
  console.info(\`end alphaAnimation\`);
});

#### \[h2\]off('end')

off(type: 'end', callback: Callback<void>): void

Cancels listening for animation end events. This API returns the result asynchronously through a callback.

You are advised to use [animation.off(type: 'animationEnd')](#section984616121137).

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

type

 | 

string

 | 

Yes

 | 

**'end'**: Animation end events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

**Example**:

animation.off("end", () => {
  console.info(\`end alphaAnimation\`);
});

#### \[h2\]on('animationStart')

on(type: 'animationStart', callback: Callback<void>): void

Listens for animation start events. This API can use multiple asynchronous callbacks to return the result.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

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

type

 | 

string

 | 

Yes

 | 

**'animationStart'**: Listens for animation start events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value. This callback is used to listen for animation start events.

 |

**Example**:

let callback1 = () => {
  console.info("animationStart", \`callback1\`);
};
let callback2 = () => {
  console.info("animationStart", \`callback2\`);
};
let callback3 = () => {
  console.info("animationStart", \`callback3\`);
};
animation.on("animationStart", callback1);
animation.on("animationStart", callback2);
animation.on("animationStart", callback3);

#### \[h2\]off('animationStart')

off(type: 'animationStart', callback?: Callback<void>): void

Cancels listening for animation start events. This API can use multiple asynchronous callbacks to return the result.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

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

type

 | 

string

 | 

Yes

 | 

**'animationStart'**: Listens for animation start events.

 |
| 

callback

 | 

Callback<void>

 | 

No

 | 

Callback function that returns no value. Cancels listening for animation start events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = () => {
  console.info("animationStart", \`callback1\`);
};
let callback2 = () => {
  console.info("animationStart", \`callback2\`);
};
let callback3 = () => {
  console.info("animationStart", \`callback3\`);
};
animation.on("animationStart", callback1);
animation.on("animationStart", callback2);
animation.on("animationStart", callback3);

// Cancel only the event response of the **callback1** object. When a **animationStart** event occurs, **callback2** and **callback3** will be called.
animation.off('animationStart', callback1);
// Cancel all **animationStart** event responses.
animation.off('animationStart');

#### \[h2\]on('animationEnd')

on(type: 'animationEnd', callback: Callback<void>): void

Listens for animation end events. This API can use multiple asynchronous callbacks to return the result.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

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

type

 | 

string

 | 

Yes

 | 

**'animationEnd'**: Animation end events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value. This callback is used to listen for animation end events.

 |

**Example**:

let callback1 = () => {
  console.info("animationEnd", \`callback1\`);
};
let callback2 = () => {
  console.info("animationEnd", \`callback2\`);
};
let callback3 = () => {
  console.info("animationEnd", \`callback3\`);
};
animation.on("animationEnd", callback1);
animation.on("animationEnd", callback2);
animation.on("animationEnd", callback3);

#### \[h2\]off('animationEnd')

off(type: 'animationEnd', callback?: Callback<void>): void

Cancels listening for animation end events. This API can use multiple asynchronous callbacks to return the result.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

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

type

 | 

string

 | 

Yes

 | 

**'animationEnd'**: Listens for animation end events.

 |
| 

callback

 | 

Callback<void>

 | 

No

 | 

Callback function that returns no value. This callback is used to cancel listening for animation end events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = () => {
  console.info("animationEnd", \`callback1\`);
};
let callback2 = () => {
  console.info("animationEnd", \`callback2\`);
};
let callback3 = () => {
  console.info("animationEnd", \`callback3\`);
};
animation.on("animationEnd", callback1);
animation.on("animationEnd", callback2);
animation.on("animationEnd", callback3);

// Cancel only the event response of the **callback1** object. When a **animationEnd** event occurs, **callback2** and **callback3** will be called. 
animation.off('animationEnd', callback1);
// Cancel all **animationEnd** event responses.
animation.off('animationEnd');
