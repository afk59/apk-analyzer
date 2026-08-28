# @ohos.curves (Interpolation Calculation)

The **Curves** module provides APIs for interpolation calculation to create step, cubic Bezier, and spring curves.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/XOm5g1CkQu6mrW_WThJI2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F801648AE1A6F4F689B0474A6EC0008F9A0BD7AA233DC201045A96A2CFD3AD3D)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { curves } from '@kit.ArkUI';

#### curves.initCurve9+

initCurve(curve?: Curve): ICurve

Implements initialization for the interpolation curve, which is used to create an interpolation curve based on the input parameter.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| curve | [Curve](#curve) | No | 
Curve type.

Default value: **Curve.Linear**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ICurve](#icurve9) | Interpolation curve. |

#### Curve

Defines an interpolation curve. For details about the curves and animations, see [Bezier Curve](https://developer.huawei.com/consumer/en/doc/design-guides/animation-attributes-0000001797117229#section18901156102713).

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Linear | 0 | The animation speed keeps unchanged. |
| Ease | 1 | The animation starts at a low speed and then accelerates. It slows down before the animation ends. **cubic-bezier(0.25, 0.1, 0.25, 1.0)** |
| EaseIn | 2 | The animation starts at a low speed and then picks up speed until the end. The cubic-bezier curve (0.42, 0.0, 1.0, 1.0) is used. |
| EaseOut | 3 | The animation ends at a low speed. The cubic-bezier curve (0.0, 0.0, 0.58, 1.0) is used. |
| EaseInOut | 4 | The animation starts and ends at a low speed. The cubic-bezier curve (0.42, 0.0, 0.58, 1.0) is used. |
| FastOutSlowIn | 5 | The animation uses the standard cubic-bezier curve (0.4, 0.0, 0.2, 1.0). |
| LinearOutSlowIn | 6 | The animation uses the deceleration cubic-bezier curve (0.0, 0.0, 0.2, 1.0). |
| FastOutLinearIn | 7 | The animation uses the acceleration cubic-bezier curve (0.4, 0.0, 1.0, 1.0). |
| ExtremeDeceleration | 8 | The animation uses the extreme deceleration cubic-bezier curve (0.0, 0.0, 0.0, 1.0). |
| Sharp | 9 | The animation uses the sharp cubic-bezier curve (0.33, 0.0, 0.67, 1.0). |
| Rhythm | 10 | The animation uses the rhythm cubic-bezier curve (0.7, 0.0, 0.2, 1.0). |
| Smooth | 11 | The animation uses the smooth cubic-bezier curve (0.4, 0.0, 0.4, 1.0). |
| Friction | 12 | The animation uses the damping cubic-bezier curve (0.2, 0.0, 0.2, 1.0). |

**Example**

import { curves } from '@kit.ArkUI';
curves.initCurve(Curve.EaseIn) // Create a default ease-in curve, where the interpolation starts slowly and then picks up speed.

#### curves.stepsCurve9+

stepsCurve(count: number, end: boolean): ICurve

Creates a step curve.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| count | number | Yes | 
Number of steps. The value must be a positive integer.

Value range: \[1, +∞)

**NOTE**

A value less than 1 evaluates to the value **1**.

 |
| end | boolean | Yes | 

Whether the step change occurs at the start or end of each interval.

\- **true**: The step change occurs at the end of each interval.

\- **false**: The step change occurs at the start of each interval.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ICurve](#icurve9) | Interpolation curve. |

**Example**

import { curves } from '@kit.ArkUI';
curves.stepsCurve(9, true)  // Create a step curve.

#### curves.cubicBezierCurve9+

cubicBezierCurve(x1: number, y1: number, x2: number, y2: number): ICurve

Creates a cubic Bezier curve, with x-coordinates automatically normalized between 0 and 1.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x1 | number | Yes | 
X coordinate of the first point on the Bezier curve.

Value range: \[0, 1\]

**NOTE**

A value less than 0 is treated as **0**. A value greater than 1 is treated as **1**.

 |
| y1 | number | Yes | 

Y coordinate of the first point on the Bezier curve.

Value range: (-∞, +∞)

 |
| x2 | number | Yes | 

X coordinate of the second point on the Bezier curve.

Value range: \[0, 1\]

**NOTE**

A value less than 0 is treated as **0**. A value greater than 1 is treated as **1**.

 |
| y2 | number | Yes | 

Y coordinate of the second point on the Bezier curve.

Value range: (-∞, +∞)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ICurve](#icurve9) | Interpolation curve. |

**Example**

import { curves } from '@kit.ArkUI';
curves.cubicBezierCurve(0.1, 0.0, 0.1, 1.0) // Create a cubic Bézier curve.

#### curves.springCurve9+

springCurve(velocity: number, mass: number, stiffness: number, damping: number): ICurve

Creates a spring curve. The curve shape is subject to the spring parameters, and the animation duration is subject to the **duration** parameter in **animation** and **animateTo**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| velocity | number | Yes | 
Initial velocity. It is applied by external factors to the spring animation, designed to help ensure the smooth transition from the previous motion state. The velocity is the normalized velocity, and its value is equal to the actual velocity at the beginning of the animation divided by the animation attribute change value.

Value range: (-∞, +∞)

 |
| mass | number | Yes | 

Mass, which influences the inertia in the spring system. The greater the mass, the greater the amplitude of the oscillation, and the slower the speed of restoring to the equilibrium position.

Value range: (0, +∞)

**NOTE**

If this parameter is set to a value less than or equal to 0, the value **1** is used.

 |
| stiffness | number | Yes | 

Stiffness. It is the degree to which an object deforms by resisting the force applied. In an elastic system, the greater the stiffness, the stronger the ability to resist deformation, and the faster the speed of restoring to the equilibrium position.

Value range: (0, +∞)

**NOTE**

If this parameter is set to a value less than or equal to 0, the value **1** is used.

 |
| damping | number | Yes | 

Damping. It is used to describe the oscillation and attenuation of the system after being disturbed. The larger the damping, the smaller the number of oscillations of elastic motion, and the smaller the oscillation amplitude.

Value range: (0, +∞)

**NOTE**

If this parameter is set to a value less than or equal to 0, the value **1** is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ICurve](#icurve9) | Interpolation curve. |

**Example**

import { curves } from '@kit.ArkUI';
curves.springCurve(10, 1, 228, 30) // Create a spring curve.

#### curves.springMotion9+

springMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve

Creates a spring animation curve. If multiple spring animations are applied to the same attribute of an object, each animation replaces their predecessor and inherits the velocity.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| response | number | No | 
Duration of one complete oscillation.

Default value: **0.55**

Unit: second

Value range: (0, +∞)

**NOTE**

If this parameter is set to a value less than or equal to 0, the default value **0.55** is used.

 |
| dampingFraction | number | No | 

Damping coefficient.

**0**: undamped. In this case, the spring oscillates forever.

\> 0 and < 1: underdamped. In this case, the spring overshoots the equilibrium position.

**1**: critically damped.

\> 1: overdamped. In this case, the spring approaches equilibrium gradually.

Default value: **0.825**

Unit: second

Value range: \[0, +∞)

**NOTE**

A value less than 0 evaluates to the default value **0.825**.

 |
| overlapDuration | number | No | 

Duration for animations to overlap, in seconds. When animations overlap, the **response** values of these animations will transit smoothly over this duration if they are different.

Default value: **0**

Unit: second

Value range: \[0, +∞)

**NOTE**

A value less than 0 evaluates to the default value **0**.

The spring animation curve is physics-based. Its duration depends on the **springMotion** parameters and the previous velocity, rather than the **duration** parameter in [animation](../../../arkts-components/animation/property-animation-animation/document.md), [animateTo](../../../arkts-components/animation/explicit-animation-animateto/document.md), or [pageTransition](../../../arkts-components/animation/page-transition-pagetransition/document.md). The time cannot be normalized. Therefore, the interpolation cannot be obtained using the **interpolate** function of the curve.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ICurve](#icurve9) | 
Curve.

**NOTE**

The spring animation curve is physics-based. Its duration depends on the **springMotion** parameters and the previous velocity, rather than the **duration** parameter in [animation](../../../arkts-components/animation/property-animation-animation/document.md), [animateTo](../../../arkts-components/animation/explicit-animation-animateto/document.md), or [pageTransition](../../../arkts-components/animation/page-transition-pagetransition/document.md). The time cannot be normalized. Therefore, the interpolation cannot be obtained using the [interpolate](#interpolate9) function of the curve.

 |

**Example**

import { curves } from '@kit.ArkUI'
curves.springMotion() // Create a spring animation curve with default settings.
curves.springMotion(0.5) // Create a spring animation curve with the specified response value.
curves.springMotion(0.5, 0.6) // Create a spring animation curve with the specified response and dampingFraction values.
curves.springMotion(0.5, 0.6, 0) // Create a spring animation curve with the specified parameter values.

#### curves.responsiveSpringMotion9+

responsiveSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve

Creates a responsive spring animation curve. It is a special case of [springMotion](#curvesspringmotion9), with the only difference in the default values. It can be used together with **springMotion**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| response | number | No | 
See **response** in **springMotion**.

Default value: **0.15**

Unit: second

Value range: (0, +∞)

**NOTE**

If this parameter is set to a value less than or equal to 0, the default value **0.15** is used.

 |
| dampingFraction | number | No | 

See **dampingFraction** in **springMotion**.

Default value: **0.86**

Unit: second

Value range: \[0, +∞)

**NOTE**

A value less than 0 evaluates to the default value **0.86**.

 |
| overlapDuration | number | No | 

See **overlapDuration** in **springMotion**.

Default value: **0.25**

Unit: second

Value range: \[0, +∞)

**NOTE**

A value less than 0 evaluates to the default value **0.25**.

**ResponsiveSpringMotion** is a special case of **springMotion**, with the only difference in the default values. To apply custom settings for a spring animation, you are advised to use **springMotion**. When using **responsiveSpringMotion**, you are advised to retain the default settings.

The duration of the responsive spring animation depends on the **responsiveSpringMotion** parameters and the previous velocity, rather than the duration parameter in [animation](../../../arkts-components/animation/property-animation-animation/document.md), [animateTo](../../../arkts-components/animation/explicit-animation-animateto/document.md), or [pageTransition](../../../arkts-components/animation/page-transition-pagetransition/document.md). In addition, the interpolation cannot be obtained using the **interpolate** function of the curve.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ICurve](#icurve9) | 
Curve.

**NOTE**

1\. **ResponsiveSpringMotion** is a special case of **springMotion**, with the only difference in the default values. To apply custom settings for a spring animation, you are advised to use **springMotion**. When using **responsiveSpringMotion**, you are advised to retain the default settings.

2\. The duration of the responsive spring animation depends on the **responsiveSpringMotion** parameters and the previous velocity, rather than the duration parameter in [animation](../../../arkts-components/animation/property-animation-animation/document.md), [animateTo](../../../arkts-components/animation/explicit-animation-animateto/document.md), or [pageTransition](../../../arkts-components/animation/page-transition-pagetransition/document.md). In addition, the interpolation cannot be obtained using the [interpolate](#interpolate9) function of the curve.

 |

**Example**

import { curves } from '@kit.ArkUI'
curves.responsiveSpringMotion() // Create a responsive spring animation curve with default settings.

#### curves.interpolatingSpring10+

interpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number): ICurve

Creates an interpolating spring curve animated from 0 to 1. The actual animation value is calculated based on the curve. The animation duration is subject to the curve parameters, rather than the **duration** parameter in **animation** or **animateTo**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| velocity | number | Yes | 
Initial velocity. It is applied by external factors to the spring animation, designed to help ensure the smooth transition from the previous motion state. The velocity is the normalized velocity, and its value is equal to the actual velocity at the beginning of the animation divided by the animation attribute change value.

Value range: (-∞, +∞)

 |
| mass | number | Yes | 

Mass, which influences the inertia in the spring system. The greater the mass, the greater the amplitude of the oscillation, and the slower the speed of restoring to the equilibrium position.

Value range: (0, +∞)

**NOTE**

If this parameter is set to a value less than or equal to 0, the value **1** is used.

 |
| stiffness | number | Yes | 

Stiffness. It is the degree to which an object deforms by resisting the force applied. In an elastic system, the greater the stiffness, the stronger the ability to resist deformation, and the faster the speed of restoring to the equilibrium position.

Value range: (0, +∞)

**NOTE**

If this parameter is set to a value less than or equal to 0, the value **1** is used.

 |
| damping | number | Yes | 

Damping. It is used to describe the oscillation and attenuation of the system after being disturbed. The larger the damping, the smaller the number of oscillations of elastic motion, and the smaller the oscillation amplitude.

Value range: (0, +∞)

**NOTE**

If this parameter is set to a value less than or equal to 0, the value **1** is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ICurve](#icurve9) | 
Curve.

Note: The spring animation curve is physics-based. Its duration depends on the **interpolatingSpring** parameters, rather than the **duration** parameter in [animation](../../../arkts-components/animation/property-animation-animation/document.md), [animateTo](../../../arkts-components/animation/explicit-animation-animateto/document.md), or [pageTransition](../../../arkts-components/animation/page-transition-pagetransition/document.md). The time cannot be normalized. Therefore, the interpolation cannot be obtained using the [interpolate](#interpolate9) function of the curve.

 |

**Example**

import { curves } from '@kit.ArkUI'
curves.interpolatingSpring(10, 1, 228, 30) // Create an interpolating spring curve whose duration is subject to spring parameters.

#### curves.customCurve10+

customCurve(interpolate: (fraction: number) => number): ICurve

Creates a custom curve.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| interpolate | (fraction: number) => number | Yes | 
Custom interpolation callback.

**fraction**: input x value for interpolation when the animation starts. Value range: \[0, 1\].

The return value is the y value of the curve. Value range: \[0, 1\].

**NOTE**

If **fraction** is **0**, the return value **0** corresponds to the animation start point; any other return value means that the animation jumps at the start point.

If **fraction** is **1**, the return value **1** corresponds to the animation end point; any other return value means that the end value of the animation is not the value of the state variable, which will result in an effect of transition from that end value to the value of the state variable.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ICurve](#icurve9) | Interpolation curve. |

**Example**

import { curves } from '@kit.ArkUI'
let interpolate = (fraction:number):number => {
  return Math.sqrt(fraction)
}
let curve = curves.customCurve(interpolate) // Create a custom interpolation curve.

#### ICurve9+

Represents a curve object. Different types of curve objects can be created using APIs in this module, including [curves.cubicBezierCurve](#curvescubicbeziercurve9) and [curves.interpolatingSpring](#curvesinterpolatingspring10). The curve object provides interpolation functionality through its member method [interpolate](#interpolate9).

#### \[h2\]interpolate9+

interpolate(fraction: number): number

Calculates the interpolated value along the curve at the specified normalized time point.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fraction | number | Yes | 
Current normalized time.

Value range: \[0, 1\].

**NOTE**

A value less than 0 is treated as **0**. A value greater than 1 is treated as **1**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Curve interpolation corresponding to the normalized time point. |

**Example**

import { curves } from '@kit.ArkUI'
let curveValue = curves.initCurve(Curve.EaseIn) // Create an ease-in curve.
let value: number = curveValue.interpolate(0.5) // Calculate the interpolation for half of the time.

#### curves.init(deprecated)

init(curve?: Curve): string

Implements initialization for the interpolation curve, which is used to create an interpolation curve based on the input parameter.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/zgiXxnDQQlC6z3CUWOF4ww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77892909DA843A0C5BBBD0ED0FB60728E5AA2BC9CF7CDC8C3A1F1298EA8779A0)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [Curves.initCurve](#curvesinitcurve9) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| curve | [Curve](#curve) | No | 
Curve type.

Default value: **Curve.Linear**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Interpolation curve object. |

#### curves.steps(deprecated)

steps(count: number, end: boolean): string

Creates a step curve.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/c4zIHdTAQo-bMfvhbkS2oA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55EEA8EBFE21FF4723EED6CD4A15AA820CFC557A2306E6C8B0770F52E202CAF7)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [Curves.stepsCurve](#curvesstepscurve9) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| count | number | Yes | Number of steps. The value must be a positive integer. |
| end | boolean | Yes | 
Whether the step change occurs at the start or end of each interval.

\- **true**: The step change occurs at the end of each interval.

\- **false**: The step change occurs at the start of each interval.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Steps curve object. |

#### curves.cubicBezier(deprecated)

cubicBezier(x1: number, y1: number, x2: number, y2: number): string

Creates a cubic Bézier curve. The curve values must be between 0 and 1.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/Kj7BuGm3TNqcSkR1ZNnQ1A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E2AF02589AC1508F4B15A04F54A216CE869F0105D27148292980B6101370743)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [Curves.cubicBezierCurve](#curvescubicbeziercurve9) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x1 | number | Yes | X coordinate of the first point on the Bézier curve. |
| y1 | number | Yes | Y coordinate of the first point on the Bézier curve. |
| x2 | number | Yes | X coordinate of the second point on the Bézier curve. |
| y2 | number | Yes | Y coordinate of the second point on the Bézier curve. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Cubic Bézier curve object. |

#### curves.spring(deprecated)

spring(velocity: number, mass: number, stiffness: number, damping: number): string

Constructs a spring curve object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/VkxxPhkATvu30QcAY_1VqQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02FEB1B18BF87D1FAA090CD2F71DAD4EAB3EC96C74B3E7636C56752F36F033BF)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [Curves.springCurve](#curvesspringcurve9) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| velocity | number | Yes | Initial velocity. It is applied by external factors to the spring animation, designed to help ensure the smooth transition from the previous motion state. |
| mass | number | Yes | Mass, which influences the inertia in the spring system. The greater the mass, the greater the amplitude of the oscillation, and the slower the speed of restoring to the equilibrium position. |
| stiffness | number | Yes | Stiffness. It is the degree to which an object deforms by resisting the force applied. In an elastic system, the greater the stiffness, the stronger the ability to resist deformation, and the faster the speed of restoring to the equilibrium position. |
| damping | number | Yes | Damping. It is a pure number and has no real physical meaning. It is used to describe the oscillation and attenuation of the system after being disturbed. The larger the damping, the smaller the number of oscillations of elastic motion, and the smaller the oscillation amplitude. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Spring curve object. |

#### Example

// xxx.ets
import { curves } from '@kit.ArkUI';

@Entry
@Component
struct ImageComponent {
  @State widthSize: number = 200;
  @State heightSize: number = 200;

  build() {
    Column() {
      Text()
        .margin({ top: 100 })
        .width(this.widthSize)
        .height(this.heightSize)
        .backgroundColor(Color.Red)
        .onClick(() => {
          let curve = curves.cubicBezierCurve(0.25, 0.1, 0.25, 1.0);
          this.widthSize = curve.interpolate(0.5) \* this.widthSize;
          this.heightSize = curve.interpolate(0.5) \* this.heightSize;
        })
        .animation({ duration: 2000, curve: curves.stepsCurve(9, true) })
    }.width("100%").height("100%")
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/hPZaYFQ7Q6u6NwlsLlGIsg/en-us_image_0000002537925270.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2133D0C1FBE6BA8DB42FD60B2F7B30499CDD71ED20C8AAC6B147C88B016BE68E)
