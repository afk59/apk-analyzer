# @ohos.animator (Animator)

The **Animator** module provides APIs for applying animation effects, including defining animations, starting animations, and playing animations in reverse order.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/dWzJ9-lSQN-P_ia-xTaO4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D41CAFBA5440F03F099C0EDADC09931B604407599B97D838F1B0A6C27EA05BE0)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   This module can be used in ArkTS since API version 9.
    
-   This module cannot be used in the file declaration of the [UIAbility](../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md). In other words, the APIs of this module can be used only after a component instance is created; they cannot be called in the lifecycle of the UIAbility.
    
-   The functionality of this module depends on UI context. This means that the APIs of this module cannot be used where [the UI context is ambiguous](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). For details, see [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   A custom component usually holds an [AnimatorResult](#animatorresult) object returned by the [createAnimator](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#createanimator) API to ensure that the animation object is not destructed during the animation. The object captures the custom component object through a callback. Therefore, the animation object needs to be released in the [aboutToDisappear](../../../arkts-components/custom-components/custom-component-lifecycle/document.md#abouttodisappear) lifecycle when the custom component is destroyed to avoid memory leakage caused by cyclic dependency. For the example details, see [ArkTS-based Declarative Development Paradigm](#arkts-based-declarative-development-paradigm).
    
-   When the object of **Animator** is destructed or proactively calls [cancel](#cancel) or [finish](#finish), an additional [onFrame](#properties) API will be triggered. The return value is the end point value of the animation. Therefore, if [cancel](#cancel) or [finish](#finish) is called during the animation, the property value will jump to the end point value within a frame. To pause the animation, set **onFrame** to an empty function and then call [finish](#finish).
    
-   For an animation in an infinite loop, the animation will continue to be played even if the global animation speed is set to 0 (disabled) in the developer options.
    

#### Modules to Import

import { Animator as animator, AnimatorOptions, AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

#### Animator

Creates an **Animator** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]create(deprecated)

create(options: AnimatorOptions): AnimatorResult

Creates an **AnimatorResult** object for animations.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/vVfn5Zp9R-69MeA_uCEyQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD2BBBAC1B42542E77A49793CDDDF3FBA68D0C72E78885BF25E07D5ABE60D89F)

-   This API is supported since API version 9 and deprecated since API version 18. You are advised to use [createAnimator](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#createanimator) instead.
    
-   Since API version 10, you can use the [createAnimator](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#createanimator) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md), which ensures that the object is created in the intended UI instance.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [AnimatorOptions](#animatoroptions) | Yes | Animator options. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AnimatorResult](#animatorresult) | Animator result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

**Example**

See [ArkTS-based Declarative Development Paradigm](#arkts-based-declarative-development-paradigm).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/LNFfIun0RS6yevu-eAZzQQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07CBA146E35D1DAB55FE817A8239F423418633A2C61B1A5646AB557A6AC4D38C)

For precise UI context management, use the [createAnimator](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#createanimator) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to specify the execution context.

import { Animator as animator, AnimatorOptions } from '@kit.ArkUI';

let options: AnimatorOptions = {
  duration: 1500,
  easing: "friction",
  delay: 0,
  fill: "forwards",
  direction: "normal",
  iterations: 3,
  begin: 200.0,
  end: 400.0
};
animator.create(options); // You are advised to use UIContext.createAnimator().

#### \[h2\]create18+

create(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult

Creates an **AnimatorResult** object for animations. Compared with[create](#createdeprecated), this API accepts parameters of the [SimpleAnimatorOptions](#simpleanimatoroptions18) type.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [AnimatorOptions](#animatoroptions) | [SimpleAnimatorOptions](#simpleanimatoroptions18) | Yes | Parameters of the animation. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AnimatorResult](#animatorresult) | Animator result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

**Example**

See [ArkTS-based Declarative Development Paradigm](#arkts-based-declarative-development-paradigm).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/xJgBH7WbRN-ND_cuSabe2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87EEFFDDBC0F1798F48964C140B73A593B109290C3CBDA6A850E46D38AA0B90C)

For precise UI context management, use the [createAnimator](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#createanimator) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to specify the execution context.

import { Animator as animator, SimpleAnimatorOptions } from '@kit.ArkUI';
let options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).duration(2000);
animator.create(options);// You are advised to use UIContext.createAnimator().

#### \[h2\]createAnimator(deprecated)

createAnimator(options: AnimatorOptions): AnimatorResult

Creates an animation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/7R8go3PVS02tiBC_WNFi6g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D1EA490060E5E3661B84C01C1F946733CB609766203AA44ED596616A014D3D6)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [create](#createdeprecated) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [AnimatorOptions](#animatoroptions) | Yes | Animator options. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AnimatorResult](#animatorresult) | Animator result. |

**Example**

See [ArkTS-based Declarative Development Paradigm](#arkts-based-declarative-development-paradigm).

import { Animator as animator } from '@kit.ArkUI';

let options: AnimatorOptions = {
  // There is no need to explicitly specify the type AnimatorOptions in the xxx.js file.
  duration: 1500,
  easing: "friction",
  delay: 0,
  fill: "forwards",
  direction: "normal",
  iterations: 3,
  begin: 200.0,
  end: 400.0,
};
this.animator = animator.createAnimator(options);

#### AnimatorResult

Defines the animator result.

#### \[h2\]Properties

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| onFrame12+ | (progress: number) => void | No | No | 
Called when a frame is received.

**progress**: current value of the animation. Value range: \[begin, end\] defined in [AnimatorOptions](#animatoroptions). Default value range: \[0, 1\]

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onFinish12+ | () => void | No | No | 

Called when this animation is finished.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onCancel12+ | () => void | No | No | 

Called when this animation is canceled.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onRepeat12+ | () => void | No | No | 

Called when this animation repeats.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onframe(deprecated) | (progress: number) => void | No | No | 

Called when a frame is received.

Note: This API is supported since API version 6 and deprecated since API version 12. You are advised to use **onFrame** instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onfinish(deprecated) | () => void | No | No | 

Called when this animation is finished.

Note: This API is supported since API version 6 and deprecated since API version 12. You are advised to use **onFinish** instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| oncancel(deprecated) | () => void | No | No | 

Called when this animation is canceled.

Note: This API is supported since API version 6 and deprecated since API version 12. You are advised to use **onCancel** instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onrepeat(deprecated) | () => void | No | No | 

Called when this animation repeats.

Note: This API is supported since API version 6 and deprecated since API version 12. You are advised to use **onRepeat** instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### \[h2\]reset9+

reset(options: AnimatorOptions): void

Resets the animation parameters of this animator.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [AnimatorOptions](#animatoroptions) | Yes | Animator options. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The specified page is not found or the object property list is not obtained. |

**Example**

import { AnimatorResult } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;

  create() {
    this.animatorResult = this.getUIContext().createAnimator({
      duration: 1500,
      easing: "friction",
      delay: 0,
      fill: "forwards",
      direction: "normal",
      iterations: 3,
      begin: 200.0,
      end: 400.0
    })
    this.animatorResult.reset({
      duration: 1500,
      easing: "friction",
      delay: 0,
      fill: "forwards",
      direction: "normal",
      iterations: 5,
      begin: 200.0,
      end: 400.0
    });
  }

  build() {
    // ......
  }
}

#### \[h2\]reset18+

reset(options: AnimatorOptions | SimpleAnimatorOptions): void

Resets the animation parameters of this animator. Compared with [reset](#reset9), this API accepts parameters of the [SimpleAnimatorOptions](#simpleanimatoroptions18) type.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [AnimatorOptions](#animatoroptions) | [SimpleAnimatorOptions](#simpleanimatoroptions18) | Yes | Animator options. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The specified page is not found or the object property list is not obtained. |

**Example**

See [ArkTS-based Declarative Development Paradigm](#arkts-based-declarative-development-paradigm).

import { Animator as animator, AnimatorResult, AnimatorOptions, SimpleAnimatorOptions } from '@kit.ArkUI';

let options: AnimatorOptions = {
  duration: 1500,
  easing: "ease",
  delay: 0,
  fill: "forwards",
  direction: "normal",
  iterations: 1,
  begin: 100,
  end: 200
};
let optionsNew: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200)
  .duration(2000)
  .iterations(3)
  .delay(1000);
let animatorResult: AnimatorResult = animator.create(options);
animatorResult.reset(optionsNew);

#### \[h2\]play

play(): void

Plays this animation. The animation retains the previous playback state. For example, if the animation is set to **reverse** and paused, it will remain in **reverse** when resumed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

See [ArkTS-based Declarative Development Paradigm](#arkts-based-declarative-development-paradigm).

animator.play();

#### \[h2\]finish

finish(): void

Ends the animation, triggering the [onFinish](#properties) callback.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

See [ArkTS-based Declarative Development Paradigm](#arkts-based-declarative-development-paradigm).

animator.finish();

#### \[h2\]pause

pause(): void

Pauses this animation.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

See [ArkTS-based Declarative Development Paradigm](#arkts-based-declarative-development-paradigm).

animator.pause();

#### \[h2\]cancel

cancel(): void

Cancels the animation, triggering the [onCancel](#properties) callback. This API is functionally identical to [finish](#finish) except for the callback it triggers. It is recommended that you use the **finish** API to end animations.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

See [ArkTS-based Declarative Development Paradigm](#arkts-based-declarative-development-paradigm).

animator.cancel();

#### \[h2\]reverse

reverse(): void

Plays this animation in reverse order. This API does not take effect when the interpolating spring curve is used.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

See [ArkTS-based Declarative Development Paradigm](#arkts-based-declarative-development-paradigm).

animator.reverse();

#### \[h2\]setExpectedFrameRateRange12+

setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange): void

Sets the expected frame rate range.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rateRange | [ExpectedFrameRateRange](../../../arkts-components/animation/explicit-animation-animateto/document.md#expectedframeraterange11) | Yes | Expected frame rate range. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/gIbayLkgSliicpuS0ZZLxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=341A6F4515C913D9202B2902D2B563F547BD2E94C2EFDF7E1248588141C06207)

After a valid expected frame rate is set, the system collects the configured frame rate and divides the frequency on the rendering pipeline. The actual frame rate may be different from the expected one configured. It is limited by the system capability and screen refresh rate.

**Example**

import { AnimatorResult } from '@kit.ArkUI';

let expectedFrameRate: ExpectedFrameRateRange = {
  min: 0,
  max: 120,
  expected: 30
}

@Entry
@Component
struct AnimatorTest {
  private backAnimator: AnimatorResult | undefined = undefined

  create() {
    this.backAnimator = this.getUIContext().createAnimator({
      duration: 2000,
      easing: "ease",
      delay: 0,
      fill: "forwards",
      direction: "normal",
      iterations: 1,
      begin: 100, // Start point of the animation interpolation.
      end: 200 // End point of the animation interpolation.
    })
    this.backAnimator.setExpectedFrameRateRange(expectedFrameRate);
  }

  build() {
    // ......
  }
}

#### \[h2\]update(deprecated)

update(options: AnimatorOptions): void

Updates this animator.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/4sFUxmR1QRmN9RI9Qk2lZw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B495EC944DFF355E241A63A06CEBA66650FC4DBF06B60BDA79FC4E1280F8817)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [reset](#reset9) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [AnimatorOptions](#animatoroptions) | Yes | Animator options. |

**Example**

See [ArkTS-based Declarative Development Paradigm](#arkts-based-declarative-development-paradigm).

animator.update(options);

#### AnimatorOptions

Animator options.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

## Properties

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| duration | number | No | No | 
Duration for playing the animation, in milliseconds.

Value range: \[0, +∞).

Default value: **0**

 |
| easing | string | No | No | 

Animation interpolation curve. For details about the supported curve types, see Table 1.

If the provided string is invalid, **"ease"** is used.

 |
| delay | number | No | No | 

Animation delay duration, in milliseconds. Value **0** means that there is no delay. If the value specified is a negative number, the animation starts playing ahead of its scheduled time. If the amount of time by which the playback is advanced exceeds the total duration of the animation, the animation immediately skips to its end state.

Default value: **0**

 |
| fill | 'none' | 'forwards' | 'backwards' | 'both' | No | No | 

State of the animated target after the animation is executed.

**'none'**: No style is applied to the target before or after the animation is executed.

**'forwards'**: The target keeps the state at the end of the animation (defined in the last key frame) after the animation is executed.

**'backwards'**: During the delay period specified in [AnimatorOptions](#animatoroptions), the animation uses the value defined in the first keyframe. When **direction** in [AnimatorOptions](#animatoroptions) is **'normal'** or **'alternate'**, the animation uses the **from** keyframe value. When **direction** in [AnimatorOptions](#animatoroptions) is **'reverse'** or **'alternate-reverse'**, the animation uses the **to** keyframe value.

**'both'**: The animation follows the **'forwards'** and **'backwards'** rules.

 |
| direction | 'normal' | 'reverse' | 'alternate' | 'alternate-reverse' | No | No | 

Animation playback mode.

**'normal'**: plays the animation in forward loop mode.

**'reverse'**: plays the animation in reverse loop mode.

**'alternate'**: plays the animation in alternating loop mode. When the animation is played for an odd number of times, the playback is in forward direction. When the animation is played for an even number of times, the playback is in reverse direction.

**'alternate-reverse'**: plays the animation in reverse alternating loop mode. When the animation is played for an odd number of times, the playback is in reverse direction. When the animation is played for an even number of times, the playback is in forward direction.

Default value: **'normal'**

 |
| iterations | number | No | No | 

Number of times that the animation is played. The value **0** means the animation is not played, **\-1** means the animation is played for an unlimited number of times, and a positive integer means the animation is played that specific number of times.

Note: Any negative value other than **\-1** is treated as invalid. For invalid values, the animation is played once.

 |
| begin | number | No | No | 

Start point of the animation interpolation.

Note: This setting affects the input parameter value of the [onFrame](#properties) callback.

Default value: **0**

 |
| end | number | No | No | 

End point of animation interpolation.

Note: This setting affects the input parameter value of the [onFrame](#properties) callback.

Default value: **1**

 |

**Table 1 Supported curve types**

| Type | Description |
| :-- | :-- |
| "linear" | The animation speed keeps unchanged. |
| "ease" | The animation starts slowly, accelerates, and then slows down towards the end. The cubic-bezier curve (0.25, 0.1, 0.25, 1.0) is used. |
| "ease-in" | The animation starts at a low speed. The cubic-bezier curve (0.42, 0.0, 1.0, 1.0) is used. |
| "ease-out" | The animation ends at a low speed. The cubic-bezier curve (0.0, 0.0, 0.58, 1.0) is used. |
| "ease-in-out" | The animation starts and ends at a low speed. The cubic-bezier curve (0.42, 0.0, 0.58, 1.0) is used. |
| "fast-out-slow-in" | The animation uses the standard cubic-bezier curve (0.4, 0.0, 0.2, 1.0). |
| "linear-out-slow-in" | The animation uses the deceleration cubic-bezier curve (0.0, 0.0, 0.2, 1.0). |
| "fast-out-linear-in" | The animation uses the acceleration cubic-bezier curve (0.4, 0.0, 1.0, 1.0). |
| "friction" | The animation uses the damping cubic-bezier curve (0.2, 0.0, 0.2, 1.0). |
| "extreme-deceleration" | The animation uses the extreme deceleration cubic-bezier curve (0.0, 0.0, 0.0, 1.0). |
| "rhythm" | The animation uses the rhythm cubic-bezier curve (0.7, 0.0, 0.2, 1.0). |
| "sharp" | The animation uses the sharp cubic-bezier curve (0.33, 0.0, 0.67, 1.0). |
| "smooth" | The animation uses the smooth cubic-bezier curve (0.4, 0.0, 0.4, 1.0). |
| "cubic-bezier(x1, y1, x2, y2)" | The animation uses the cubic Bézier curve, where the values of **x1** and **x2** must be between 0 and 1. Example: **"cubic-bezier(0.42, 0.0, 0.58, 1.0)"**. |
| "steps(number, step-position)" | The animation uses the steps curve. The number must be set to a positive integer. The **step-position** parameter is optional. The value can be **start** or **end**. The default value is **end**. Example: **"steps(3, start)"**. |
| interpolating-spring(velocity, mass, stiffness, damping) | 
The animation uses the interpolating spring curve.

The **velocity**, **mass**, **stiffness**, and **damping** parameters are of the numeric type, and the values of **mass**, **stiffness**, and **damping** must be greater than 0. For details about the parameters, see [Curves.interpolatingSpring](../ohos-curves-interpolation-calculation/document.md#curvesinterpolatingspring10).

When an interpolating spring curve is used, settings for the **duration**, **fill**, **direction**, and **iterations** do not take effect. Rather, the value of **duration** is subject to the spring settings, **fill** is fixed at **forwards**, **direction** at **normal**, and **iterations** at **1**. In addition, invoking [reverse](#reverse) of **animator** is not effective. In other words, when using an interpolating spring curve, the animation can play only once in forward mode.

Supported since API version 11 and can be used only in ArkTS.

 |

#### SimpleAnimatorOptions18+

Defines a simple animation parameter object. Unlike **AnimatorOptions**, this object comes with some default values for certain animation parameters, so you do not have to set them manually.

#### \[h2\]constructor18+

constructor(begin: number, end: number)

A constructor used to create a **SimpleAnimatorOptions** instance.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| begin | number | Yes | Start point of the animation interpolation. |
| end | number | Yes | End point of animation interpolation. |

**Example**

See [ArkTS-based Declarative Development Paradigm](#arkts-based-declarative-development-paradigm).

import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200); // Animation interpolation from 100 to 200, with other animation parameters set to default values.

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}

#### \[h2\]duration18+

duration(duration: number): SimpleAnimatorOptions

Sets the animation duration.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| duration | number | Yes | 
Animation duration, in milliseconds.

Default value: **1000**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [SimpleAnimatorOptions](#simpleanimatoroptions18) | **SimpleAnimatorOptions** object for animation parameters. |

**Example**

See [ArkTS-based Declarative Development Paradigm](#arkts-based-declarative-development-paradigm).

import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).duration(500);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}

#### \[h2\]easing18+

easing(curve: string): SimpleAnimatorOptions

Sets the interpolation curve for this animation.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| curve | string | Yes | 
Interpolation curve. For details, see [AnimatorOptions](#animatoroptions).

Default value: **"ease"**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [SimpleAnimatorOptions](#simpleanimatoroptions18) | **SimpleAnimatorOptions** object for animation parameters. |

**Example**

See [ArkTS-based Declarative Development Paradigm](#arkts-based-declarative-development-paradigm).

import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).easing("ease-in");

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}

#### \[h2\]delay18+

delay(delay: number): SimpleAnimatorOptions

Sets the playback delay for this animation.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| delay | number | Yes | 
Playback delay, in milliseconds. The value **0** indicates no delay. If the value specified is a negative number, the animation starts playing ahead of its scheduled time. If the amount of time by which the playback is advanced exceeds the total duration of the animation, the animation immediately skips to its end state.

Default value: **0**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [SimpleAnimatorOptions](#simpleanimatoroptions18) | **SimpleAnimatorOptions** object for animation parameters. |

**Example**

See [ArkTS-based Declarative Development Paradigm](#arkts-based-declarative-development-paradigm).

import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).delay(500);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}

#### \[h2\]fill18+

fill(fillMode: [FillMode](../../../arkts-components/common-definitions/enums/document.md#fillmode)): SimpleAnimatorOptions

Sets the fill mode for this animation.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fillMode | [FillMode](../../../arkts-components/common-definitions/enums/document.md#fillmode) | Yes | 
Fill mode, which affects how the animation behaves during the delay period and after it ends.

Default value: **FillMode.Forwards**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [SimpleAnimatorOptions](#simpleanimatoroptions18) | **SimpleAnimatorOptions** object for animation parameters. |

**Example**

See [ArkTS-based Declarative Development Paradigm](#arkts-based-declarative-development-paradigm).

import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).fill(FillMode.Forwards);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}

#### \[h2\]direction18+

direction(direction: [PlayMode](../../../arkts-components/common-definitions/enums/document.md#playmode)): SimpleAnimatorOptions

Sets the playback direction for this animator animation.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| direction | [PlayMode](../../../arkts-components/common-definitions/enums/document.md#playmode) | Yes | 
Playback direction.

Default value: **PlayMode.Normal**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [SimpleAnimatorOptions](#simpleanimatoroptions18) | **SimpleAnimatorOptions** object for animation parameters. |

**Example**

See [ArkTS-based Declarative Development Paradigm](#arkts-based-declarative-development-paradigm).

import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).direction(PlayMode.Alternate);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}

#### \[h2\]iterations18+

iterations(iterations: number): SimpleAnimatorOptions

Sets the number of times that this animation is played.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| iterations | number | Yes | 
Number of times that the animation is played. The value **0** means the animation is not played, and **\-1** means the animation is played for an unlimited number of times.

Default value: **1**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [SimpleAnimatorOptions](#simpleanimatoroptions18) | **SimpleAnimatorOptions** object for animation parameters. |

**Example**

See [ArkTS-based Declarative Development Paradigm](#arkts-based-declarative-development-paradigm).

import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).iterations(3);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}

#### Example

## JavaScript-compatible Web-like Development Paradigm

<!-- hml -->
<div class="container">
  <div class="Animation" style="height: {{divHeight}}px; width: {{divWidth}}px; background-color: red;" onclick="Show">
  </div>
</div>

import { Animator as animator, AnimatorResult } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let DataTmp: Record<string, Animator> = {
  'divWidth': 200,
  'divHeight': 200,
  'animator': animator
}

class Tmp {
  data: animator = DataTmp
  onInit: Function = () => {
  }
  Show: Function = () => {
  }
}

class DateT {
  divWidth: number = 0
  divHeight: number = 0
  animator: AnimatorResult | null = null
}

(Fn: (v: Tmp) => void) => {
  Fn({
    data: DataTmp,
    onInit() {
      let options: AnimatorOptions = {
        duration: 1500,
        easing: "friction",
        delay: 0,
        fill: "forwards",
        direction: "normal",
        iterations: 2,
        begin: 200.0,
        end: 400.0
      };
      let DataTmp: DateT = {
        divWidth: 200,
        divHeight: 200,
        animator: null
      }
      DataTmp.animator = animator.create(options);
    },
    Show() {
      let options1: AnimatorOptions = {
        duration: 1500,
        easing: "friction",
        delay: 0,
        fill: "forwards",
        direction: "normal",
        iterations: 2,
        begin: 0,
        end: 400.0,
      };
      let DataTmp: DateT = {
        divWidth: 200,
        divHeight: 200,
        animator: null
      }
      try {
        DataTmp.animator = animator.create(options1);
        DataTmp.animator.reset(options1);
      } catch (error) {
        let message = (error as BusinessError).message
        let code = (error as BusinessError).code
        console.error(\`Animator reset failed, error code: ${code}, message: ${message}.\`);
      }
      let \_this = DataTmp;
      if (DataTmp.animator) {
        DataTmp.animator.onFrame = (value: number) => {
          \_this.divWidth = value;
          \_this.divHeight = value;
        };
        DataTmp.animator.play();
      }
    }
  })
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/dxLVnzXXTH-X5Gkp-seShw/en-us_image_0000002568765039.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF3DD906A716208DE201434729F90EAA7D80C4C7D5AC3A71C5800EDADA386C98)

## ArkTS-based Declarative Development Paradigm

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/8rODfbIPSJSbmCNwArew7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0537327D060B9C87C88AFA7361E0FB2ADEE227EF9742F301F9D1678C36A36ECD)

For precise UI context management, use the [createAnimator](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#createanimator) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to specify the execution context.

import { AnimatorResult } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private TAG: string = '\[AnimatorTest\]'
  private backAnimator: AnimatorResult | undefined = undefined
  private flag: boolean = false
  @State columnWidth: number = 100
  @State columnHeight: number = 100

  create() {
    this.backAnimator = this.getUIContext().createAnimator({
      // You are advised to use this.getUIContext().createAnimator().
      duration: 2000,
      easing: "ease",
      delay: 0,
      fill: "forwards",
      direction: "normal",
      iterations: 1,
      begin: 100, // Start point of the animation interpolation.
      end: 200 // End point of the animation interpolation.
    })
    this.backAnimator.onFinish = () => {
      this.flag = true
      console.info(this.TAG, 'backAnimator onFinish')
    }
    this.backAnimator.onRepeat = () => {
      console.info(this.TAG, 'backAnimator repeat')
    }
    this.backAnimator.onCancel = () => {
      console.info(this.TAG, 'backAnimator cancel')
    }
    this.backAnimator.onFrame = (value: number) => {
      this.columnWidth = value
      this.columnHeight = value
    }
  }

  aboutToDisappear() {
    // When the custom component disappears, call finish to end incomplete animations and prevent them from continuing.
    // backAnimator references this in onFrame, and this saves backAnimator.
    // set backAnimator stored in the custom component to undefined when the component disappears to avoid memory leak.
    this.backAnimator?.finish();
    this.backAnimator = undefined;
  }

  build() {
    Column() {
      Column() {
        Column()
          .width(this.columnWidth)
          .height(this.columnHeight)
          .backgroundColor(Color.Blue)
      }
      .width('100%')
      .height(300)

      Column() {
        Row() {
          Button('create')
            .fontSize(30)
            .fontColor(Color.Black)
            .onClick(() => {
              this.create()
            })
        }
        .padding(10)

        Row() {
          Button('play')
            .fontSize(30)
            .fontColor(Color.Black)
            .onClick(() => {
              this.flag = false
              if (this.backAnimator) {
                this.backAnimator.play()
              }
            })
        }
        .padding(10)

        Row() {
          Button('pause')
            .fontSize(30)
            .fontColor(Color.Black)
            .onClick(() => {
              if (this.backAnimator) {
                this.backAnimator.pause()
              }
            })
        }
        .padding(10)

        Row() {
          Button('finish')
            .fontSize(30)
            .fontColor(Color.Black)
            .onClick(() => {
              this.flag = true
              if (this.backAnimator) {
                this.backAnimator.finish()
              }
            })
        }
        .padding(10)

        Row() {
          Button('reverse')
            .fontSize(30)
            .fontColor(Color.Black)
            .onClick(() => {
              this.flag = false
              if (this.backAnimator) {
                this.backAnimator.reverse()
              }
            })
        }
        .padding(10)

        Row() {
          Button('cancel')
            .fontSize(30)
            .fontColor(Color.Black)
            .onClick(() => {
              if (this.backAnimator) {
                this.backAnimator.cancel()
              }
            })
        }
        .padding(10)

        Row() {
          Button('reset')
            .fontSize(30)
            .fontColor(Color.Black)
            .onClick(() => {
              if (this.flag) {
                this.flag = false
                if (this.backAnimator) {
                  this.backAnimator.reset({
                    duration: 3000,
                    easing: "ease-in",
                    delay: 0,
                    fill: "forwards",
                    direction: "alternate",
                    iterations: 3,
                    begin: 100,
                    end: 300
                  })
                }
              } else {
                console.info(this.TAG, 'Animation not ended')
              }
            })
        }
        .padding(10)
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/iznmUlibQcOfy2vcZN1bSA/en-us_image_0000002537765314.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73DC6DCDAE8DEEBB8A37C6BF8736BA716E2C6C529359AC51D9457B226571CD76)

## Example: Implementing a Translation Animation with Simple Parameters

import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private TAG: string = '\[AnimatorTest\]'
  private backAnimator: AnimatorResult | undefined = undefined
  private flag: boolean = false
  @State translate\_: number = 0

  create() {
    this.backAnimator = this.getUIContext()?.createAnimator(
      new SimpleAnimatorOptions(0, 100)
    )
    this.backAnimator.onFinish = () => {
      this.flag = true
      console.info(this.TAG, 'backAnimator onFinish')
    }
    this.backAnimator.onFrame = (value:number) => {
      this.translate\_ = value
    }
  }

  aboutToDisappear() {
    // When the custom component disappears, call finish to end incomplete animations and prevent them from continuing.
    // backAnimator references this in onFrame, and this saves backAnimator.
    // set backAnimator stored in the custom component to undefined when the component disappears to avoid memory leak.
    this.backAnimator?.finish();
    this.backAnimator = undefined;
  }

  build() {
    Column() {
      Column() {
        Column()
          .width(100)
          .height(100)
          .translate({x: this.translate\_})
          .backgroundColor(Color.Green)
      }
      .width('100%')
      .height(300)

      Column() {
        Column() {
          Button('create')
            .fontSize(30)
            .fontColor(Color.White)
            .onClick(() => {
              this.create()
            })
        }
        .padding(10)

        Column() {
          Button('play')
            .fontSize(30)
            .fontColor(Color.White)
            .onClick(() => {
              this.flag = false
              if(this.backAnimator){
                this.backAnimator.play()
              }
            })
        }
        .padding(10)

        Column() {
          Button('reset')
            .fontSize(30)
            .fontColor(Color.White)
            .onClick(() => {
              if (this.flag) {
                this.flag = false
                if(this.backAnimator){
                  this.backAnimator.reset(
                    new SimpleAnimatorOptions(0, -100)
                      .duration(2000)
                      .easing("ease-in")
                      .fill(FillMode.Forwards)
                      .direction(PlayMode.Alternate)
                      .iterations(2)
                  )
                }
              } else {
                console.info(this.TAG, 'Animation not ended')
              }
            })
        }
        .padding(10)
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Fb9PgNNAQMazCcP54cKhvQ/en-us_image_0000002537925254.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E966A0AA1EC6784B0363842EFEF75C0364E599EF876BEE149BB2E6AC6830C68E)
