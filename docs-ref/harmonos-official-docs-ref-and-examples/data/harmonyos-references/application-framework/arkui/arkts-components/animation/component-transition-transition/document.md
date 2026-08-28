# Component Transition (transition)

You can configure the component transition animations through the **transition** attribute for when a component is inserted or removed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/53VPFLoXQ5ShGSt5PPDbYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B4F33497F7F417C74689B043C2497703FDC582C1BE79ACF3F3410C3A8BD1510)

This feature is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

There are two ways to trigger a component's transition:

1.  When a component is inserted or removed (for example, when there are changes in **if** conditions, or when components are added or removed in a **ForEach** loop), the transition effects of all newly inserted/removed components are triggered recursively.
2.  When the [visibility](../../universal-attributes/basic-attributes/visibility-control/document.md#visibility) attribute of a component changes between visible and invisible, only the transition effect of that component is triggered.

#### transition

transition(value: TransitionOptions | TransitionEffect): T

Sets the transition effects for when the component is inserted to show and removed to hide.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [TransitionOptions](#transitionoptionsdeprecated)(deprecated) | [TransitionEffect](#transitioneffect10) | Yes | 
Transition effects for when the component is inserted to show and removed to hide.

**NOTE**

For details, see [TransitionOptions](#transitionoptionsdeprecated) and [TransitionEffect](#transitioneffect10).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### transition12+

transition(effect: TransitionEffect, onFinish: Optional<TransitionFinishCallback>): T

Transition effects for when the component is inserted to show and removed to hide. Compared with [transition](#transition), this API provides the callback when the transition animation ends.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/vw0LrG8VRnC_W3Xn-1u_hw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F447517E5D39B70F067BBAA696DB2057F7125C2F0B389CF7A7E8353C980EF2E9)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| effect | [TransitionEffect](#transitioneffect10) | Yes | Transition effects for when the component is inserted to show and removed to hide. |
| onFinish | Optional<[TransitionFinishCallback](#transitionfinishcallback12)\> | Yes | Callback when the transition animation ends. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### TransitionEdge10+

Enumerates the transition edge types.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| TOP | 0 | Top edge of the window. |
| BOTTOM | 1 | Bottom edge of the window. |
| START | 2 | Start edge of the window, which is the left edge for left-to-right scripts and the right edge for right-to-left scripts. |
| END | 3 | End edge of the window, which is the right edge for left-to-right scripts and the left edge for right-to-left scripts. |

#### TransitionEffect10+

Defines the transition effect by using the provided APIs, as listed below.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

## Properties

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| IDENTITY | [TransitionEffect](#transitioneffect10)<"identity"> | Yes | No | Disables the transition effect. |
| OPACITY | [TransitionEffect](#transitioneffect10)<"opacity"> | Yes | No | Applies a transition effect with the opacity changing from 0 to 1 when the component appears and from 1 to 0 when the component disappears. This is equivalent to **TransitionEffect.opacity(0)**. |
| SLIDE | [TransitionEffect](#transitioneffect10)<"asymmetric", { appear: [TransitionEffect](#transitioneffect10)<"move", [TransitionEdge](#transitionedge10)\>; disappear: [TransitionEffect](#transitioneffect10)<"move", [TransitionEdge](#transitionedge10)\>; }> | Yes | No | This is equivalent to **TransitionEffect.asymmetric(TransitionEffect.move(TransitionEdge.START), TransitionEffect.move(TransitionEdge.END))**. Applies a transition effect of sliding in from the start edge when the component appears and sliding out from the end edge when the component disappears. This means sliding in from the left edge and sliding out from the right edge for left-to-right scripts, and sliding in from the right edge and sliding out from the left edge for right-to-left scripts. |
| SLIDE\_SWITCH | [TransitionEffect](#transitioneffect10)<"slideSwitch"> | Yes | No | Applies a transition effect of sliding in from the right with first scaling down and then scaling up when the component appears and sliding out from the left with first scaling down and then scaling up when the component disappears. This transition effect comes with its own animation parameters, which can also be overridden. The default animation duration is 600 milliseconds, with a specified animation curve of cubicBezierCurve(0.24, 0.0, 0.50, 1.0) and a minimum scale factor of 0.8. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/OwdloX-cS_-pIP23UhQ1XQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43B28E8A209FE4575171F0AF5CA7D015ED9398F403C2D49AAD42AA31409034BB)

1.  For transition effects combined through the **combine** function, animation settings can be configured through the **animation** parameter on a one-on-one basis. In addition, the animation settings of a transition effect are applicable to the one following it. For example, with **TransitionEffect.OPACITY.animation({duration: 1000}).combine(TransitionEffect.translate({x: 100}))**, the **duration** settings (1000 ms) apply to both the OPACITY and translate effects.
2.  The animation settings take effect in the following sequence: animation settings specified in the current **TransitionEffect** > animation settings specified in the previous **TransitionEffect** > animation settings specified in **animateTo** that triggers the component to appear and disappear.
3.  If **animateTo** is not used and **TransitionEffect** does not have the **animation** parameter specified, the component will appear or disappear without any transition animation.
4.  If the value of an attribute specified in **TransitionEffect** is the same as the default value, no transition animation will be applied to the attribute. For example, with **TransitionEffect.opacity(1).animation({duration:1000})**, because the default value of **opacity** is also **1**, no opacity animation will be applied, and the component appears or disappears without any transition animation.
5.  For details about the scale and rotate effects, see [Transformation](../../universal-attributes/visual-effects/transformation/document.md).
6.  If a component's attach or detach in the component tree or [visibility](../../universal-attributes/basic-attributes/visibility-control/document.md#visibility) change is triggered within the animation scope ([animateTo](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#animateto) or [animation](../property-animation-animation/document.md)), and the root component does not have a transition configured, a default opacity transition, namely **TransitionEffect.OPACITY**, will be applied to the component. The animation parameters will follow the parameters of the surrounding animation environment. If this default behavior is not desired, it can be disabled by configuring **TransitionEffect.IDENTITY**, which causes the component to appear or disappear instantly without any transition effect.
7.  To ensure that the complete disappearance transition process is visible when triggering it by deleting an entire subtree, it is necessary to guarantee that the root component of the subtree being deleted has ample time to complete its disappearance transition, as demonstrated in Example 3.

#### \[h2\]translate10+

translate(options: TranslateOptions): TransitionEffect<"translate">

Sets the translation effect for component transitions.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TranslateOptions](../../universal-attributes/visual-effects/transformation/document.md#translateoptions) | Yes | 
Translation effect for component transitions, specifying the start point of insertion and the end point of deletion.

\-**x**: distance to translate along the x-axis.

\-**y**: distance to translate along the y-axis.

\-**z**: distance to translate along the z-axis.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [TransitionEffect](#transitioneffect10)<"translate"> | Translation effect for the current animation. |

#### \[h2\]rotate10+

rotate(options: RotateOptions): TransitionEffect<"rotate">

Sets the rotation effect for component transitions.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RotateOptions](../../universal-attributes/visual-effects/transformation/document.md#rotateoptions) | Yes | 
Rotation effect for component transitions, specifying the start point of insertion and the end point of deletion.

\- **x**: X-component of the rotation vector.

\- **y**: Y-component of the rotation vector.

\- **z**: Z-component of the rotation vector.

\- **centerX** and **centerY**: rotation center point. The default values are both **"50%"**, indicating the center point of the page.

\- If the center point is (0, 0), it refers to the upper left corner of the component.

\- **centerZ**: z-axis anchor point, that is, the z-component of the 3D rotation center point. The default value is **0**.

\- **perspective**: viewing distance. It is not supported for use in transition animations.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [TransitionEffect](#transitioneffect10)<"rotate"> | Rotation effect for the current animation. |

#### \[h2\]scale10+

scale(options: ScaleOptions): TransitionEffect<"scale">

Sets the scaling effect for component transitions.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ScaleOptions](../../universal-attributes/visual-effects/transformation/document.md#scaleoptions) | Yes | 
Scaling effect for component transitions, specifying the start point of insertion and the end point of deletion. The scale value set here is multiplied by the component's **scale** attribute. For example, if the component's scale is 0.8 and the transition scale is set to 0.5, the component entry animation starts from a scale of 0.4.

\- **x**: scale factor along the x-axis.

\- **y**: scale factor along the y-axis.

\-z: currently invalid in two-dimensional display.

\- **centerX** and **centerY**: scale center point. The default values are both **"50%"**, indicating the center point of the page.

\- If the center point is (0, 0), it refers to the upper left corner of the component.

**NOTE**

If **centerX** or **centerY** is set to an invalid string (for example, **"illegalString"**), the default value **"0"** is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [TransitionEffect](#transitioneffect10)<"scale"> | Scaling effect for component transitions. |

#### \[h2\]opacity10+

opacity(alpha: number): TransitionEffect<"opacity">

Sets the opacity for component transition.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| alpha | number | Yes | 
Opacity of the component during transition, which is the value of the start point of insertion and the end point of deletion.

Value range: \[0, 1\].

**NOTE**

If the value specified is less than 0, the value **0** is used. If the value specified is greater than 1, the value **1** is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [TransitionEffect](#transitioneffect10)<"opacity"> | Opacity of component transition. |

#### \[h2\]move10+

move(edge: TransitionEdge): TransitionEffect<"move">

Sets the slide-in and slide-out effects for component transitions from the screen edges.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| edge | [TransitionEdge](#transitionedge10) | Yes | The slide-in and slide-out effects for component transitions from the screen edges. This is essentially a translation effect, specifying the start point of insertion and the end point of deletion. |

**Return value**

| Type | Description |
| :-- | :-- |
| [TransitionEffect](#transitioneffect10)<"move"> | Current animation's slide-in and slide-out effects from the screen edges. |

#### \[h2\]asymmetric10+

asymmetric(appear: TransitionEffect, disappear: TransitionEffect): TransitionEffect<"asymmetric">

Sets the asymmetric transition effect.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appear | [TransitionEffect](#transitioneffect10) | Yes | 
Transition effect for appearance.

If the **asymmetric** function is not used for **TransitionEffect**, the transition effect takes effect for both appearance and disappearance of the component.

 |
| disappear | [TransitionEffect](#transitioneffect10) | Yes | 

Transition effect for disappearance.

If the **asymmetric** function is not used for **TransitionEffect**, the transition effect takes effect for both appearance and disappearance of the component.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [TransitionEffect](#transitioneffect10)<"asymmetric"> | Asymmetric transition effect for the current animation. |

#### \[h2\]constructor10+

constructor(type: Type, effect: Effect)

Constructs a **TransitionEffect** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [Type](../../common-definitions/enums/document.md#transitiontype) | Yes | Transition type. |
| effect | [Effect](#transitioneffect10) | Yes | Transition parameter. |

#### \[h2\]combine10+

combine(transitionEffect: TransitionEffect): TransitionEffect

Combination of transition effects.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| transitionEffect | [TransitionEffect](#transitioneffect10) | Yes | Combined transition effect. |

**Return value**

| Type | Description |
| :-- | :-- |
| [TransitionEffect](#transitioneffect10) | Combined transition effect. |

#### \[h2\]animation10+

animation(value: AnimateParam): TransitionEffect

Animation settings.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [AnimateParam](../explicit-animation-animateto/document.md#animateparam) | Yes | 
Animation parameters.

The **onFinish** callback in **AnimateParam** does not work here.

If **combine** is used for combining transition effects, the animation settings of a transition effect are applicable to the one following it.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [TransitionEffect](#transitioneffect10) | Current animation effect. |

#### TransitionFinishCallback12+

type TransitionFinishCallback = (transitionIn: boolean) => void

Represents the type of callback for the end of a component's transition animation.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| transitionIn | boolean | Yes | 
Type of callback for the end of the transition animation.

The value **true** indicates that the callback is for the end of an appearance animation, and **false** indicates that the callback is for the end of a disappearance animation.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/MUym8ANmRBKCg5DpMXo9jg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B7D979CBD06B3AC2AA563BAA15167CC7A6A1FFD8C5BEF0DE3C4FA60013B31EFD)

1.  When a subtree is triggered to attach or detach, which in turn recursively triggers appearance and disappearance transitions, only the root component's disappearance animation end callback can be guaranteed to be invoked. If a child component's disappearance animation end callback is scheduled after the root component's disappearance animation end callback, it will not be invoked because the entire subtree has already been destroyed.
2.  The end callback is only invoked after the last of the same type of animation (either appearance or disappearance) for the same component has finished. That is, if appearance and disappearance animations are triggered repeatedly (for example, through changes in **Visibility**), only the end callback of the final appearance or disappearance will be executed.

#### TransitionOptions(deprecated)

Defines the transition effect by setting parameters in the struct.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/PQQAonosTFutEm_Cjx12pQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=594310EE53AD5D2B54D8D5B45CEEC8ACE91F3B75899512FE8EECE3446D83344B)

This API is supported since API version 7 and deprecated since API version 10. You are advised to use [TransitionEffect](#transitioneffect10) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [TransitionType](../../common-definitions/enums/document.md#transitiontype) | No | Yes | 
Transition type.

Default value: **TransitionType.All**

**NOTE**

If **type** is not specified, the default value **TransitionType.All** is used, which means that the transition effect works for both component addition and deletion.

 |
| opacity | number | No | Yes | 

Opacity of the component during transition, which is the value of the start point of insertion and the end point of deletion.

Value range: \[0, 1\]

**NOTE**

If the value specified is less than 0, the value **0** is used. If the value specified is greater than 1, the value **1** is used.

 |
| translate | [TranslateOptions](../../universal-attributes/visual-effects/transformation/document.md#translateoptions) | No | Yes | 

Translation of the component during transition, which is the value of the start point of insertion and the end point of deletion.

\-**x**: distance to translate along the x-axis.

\-**y**: distance to translate along the y-axis.

\-**z**: distance to translate along the z-axis.

 |
| scale | [ScaleOptions](../../universal-attributes/visual-effects/transformation/document.md#scaleoptions) | No | Yes | 

Scaling of the component during transition, which is the value of the start point of insertion and the end point of deletion.

\- **x**: scale factor along the x-axis.

\- **y**: scale factor along the y-axis.

\- **z**: scale factor along the z-axis (not effective for the current 2D graphics).

\- **centerX** and **centerY**: scale center point. The default values are both **"50%"**, indicating the center point of the page.

\- If the center point is (0, 0), it refers to the upper left corner of the component.

**NOTE**

If **centerX** or **centerY** is set to an invalid string (for example, **"illegalString"**), the default value **"0"** is used.

 |
| rotate | [RotateOptions](../../universal-attributes/visual-effects/transformation/document.md#rotateoptions) | No | Yes | 

Rotation of the component during transition, which is the value of the start point of insertion and the end point of deletion.

\- **x**: X-component of the rotation vector.

\- **y**: Y-component of the rotation vector.

\- **z**: Z-component of the rotation vector.

\- **centerX** and **centerY**: rotation center point. The default values are both **"50%"**, indicating the center point of the page.

\- If the center point is (0, 0), it refers to the upper left corner of the component.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/7UEZ0gO7QXu7kfXCLFdUZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DD162B76BEF18C2EAF4223CFBE0B8A0A8683777268095C10942F143021AA914)

1.  When set to a value of the **TransitionOptions** type, the **transition** attribute must work with [animateTo](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#animateto). The animation duration, curve, and delay follow the settings in **animateTo**.
2.  If the value of the **TransitionOptions** type has only **type** specified, the transition effect will take on the default opacity. For example, **{type: TransitionType.Insert}** produces the same effect as **{type: TransitionType.Insert, opacity: 0}**. If a specific style is specified, the transition effect will not take on the default opacity.

#### Example

## Example 1: Using the Same TransitionEffect Configuration for Image Appearance and Disappearance

This example primarily demonstrates how to use the same [TransitionEffect](#transitioneffect10) to achieve both the appearance and disappearance of an image, where the appearance and disappearance are inverse processes of each other.

// xxx.ets
@Entry
@Component
struct TransitionEffectExample1 {
  @State flag: boolean = true;
  @State show: string = 'show';

  build() {
    Column() {
      Button(this.show).width(80).height(30).margin(30)
        .onClick(() => {
          // Click the button to show or hide the image.
          if (this.flag) {
            this.show = 'hide';
          } else {
            this.show = 'show';
          }
          this.flag = !this.flag;
        })
      if (this.flag) {
        // Apply the same transition effect to the appearance and disappearance of the image.
        // When the image appears, it changes from the state where the opacity is 0 and the rotation angle is 180° around the z-axis to the state where the opacity is 1 and the rotation angle is 0°. The durations of the opacity and rotation animations are both 2000 ms.
        // When the image disappears, it changes from the state where the opacity is 1 and the rotation angle is 0° to the state where the opacity is 0 and the rotation angle is 180° around the z-axis. The durations of the opacity and rotation animations are both 2000 ms.
        // Replace $r('app.media.testImg') with the image resource file you use.
        Image($r('app.media.testImg')).width(200).height(200)
          .transition(TransitionEffect.OPACITY.animation({ duration: 2000, curve: Curve.Ease }).combine(
            TransitionEffect.rotate({ z: 1, angle: 180 })
          ))
      }
    }.width('100%')
  }
}

Below you can see the example in action.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/64LfBS0KQLWqKEnswdl_Rg/en-us_image_0000002568685615.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CAD4C3FC978AA4E4591C7320FAF7F84867A7FB4BD9FC00920B83E4537A43129)

## Example 2: Using Different TransitionEffect Configurations for Image Appearance and Disappearance

This example demonstrates how to use different [TransitionEffect](#transitioneffect10) configurations to implement the appearance and disappearance of an image.

// xxx.ets
@Entry
@Component
struct TransitionEffectExample2 {
  @State flag: boolean = true;
  @State show: string = 'show';

  build() {
    Column() {
      Button(this.show).width(80).height(30).margin(30)
        .onClick(() => {
          // Click the button to show or hide the image.
          if (this.flag) {
            this.show = 'hide';
          } else {
            this.show = 'show';
          }
          this.getUIContext().animateTo({ duration: 2000 }, () => {
            // In the first image, \*\*TransitionEffect\*\* contains \*\*animation\*\*, and therefore the animation settings are those configured in \*\*TransitionEffect\*\*.
            // In the second image, \*\*TransitionEffect\*\* does not contain \*\*animation\*\*, and therefore the animation settings are those configured in \*\*animateTo\*\*.
            this.flag = !this.flag;
          });
        })
      if (this.flag) {
        // Apply different transition effects to the appearance and disappearance of the image.
        // When the image appears, its opacity changes 0 to 1 (default value) over the duration of 1000 ms, and after 1000 ms has elapsed, its rotation angle changes from 180° around the z-axis to 0° (default value) over the duration of 1000 ms.
        // When the image disappears, after 1000 ms has elapsed, its opacity changes 1 (default value) to 0 over the duration of 1000 ms, and its rotation angle changes from 0° (default value) to 180° around the z-axis over the duration of 1000 ms.
        // Replace $r('app.media.testImg') with the image resource file you use.
        Image($r('app.media.testImg')).width(200).height(200)
          .transition(
            TransitionEffect.asymmetric(
              TransitionEffect.OPACITY.animation({ duration: 1000 }).combine(
              TransitionEffect.rotate({ z: 1, angle: 180 }).animation({ delay: 1000, duration: 1000 }))
              ,
              TransitionEffect.OPACITY.animation({ delay: 1000, duration: 1000 }).combine(
              TransitionEffect.rotate({ z: 1, angle: 180 }).animation({ duration: 1000 }))
            )
          )
        // When the image appears, the scale along the x- and y- axes is changed from 0 to 1 (default value). The animation duration is 2000 ms specified in \*\*animateTo\*\*.
        // When the image disappears, no transition effect is applied.
        // Replace $r('app.media.testImg') with the image resource file you use.
        Image($r('app.media.testImg')).width(200).height(200).margin({ top: 100 })
          .transition(
            TransitionEffect.asymmetric(
              TransitionEffect.scale({ x: 0, y: 0 }),
              TransitionEffect.IDENTITY
            )
          )
      }
    }.width('100%')
  }
}

Below you can see the example in action.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/ymc6iS2iRFaqKJ0tS-r0NA/en-us_image_0000002568765625.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0FB0A51FA52ACBE3BBF20AD64230CE7A3B3B8FC8DF8A777E15110282E690F39E)

## Example 3: Setting transition on Parent and Child Components

This example demonstrates how to configure [transition](#transition) on both parent and child components to implement the appearance and disappearance of images.

// xxx.ets
@Entry
@Component
struct TransitionEffectExample3 {
  @State flag: boolean = true;
  @State show: string = 'show';

  build() {
    Column() {
      Button(this.show).width(80).height(30).margin(30)
        .onClick(() => {
          // Click the button to show or hide the image.
          if (this.flag) {
            this.show = 'hide';
          } else {
            this.show = 'show';
          }
          this.flag = !this.flag;
        })
      if (this.flag) {
        // When the flag condition is changed, it will trigger the transition animation for elements with the IDs column1, image1, and image2.
        // The component with the ID column1 is the root node of this newly appearing/disappearing subtree.
        Column() {
          Row() {
            // Replace $r('app.media.testImg') with the image resource file you use.
            Image($r('app.media.testImg')).width(150).height(150).id("image1")
              .transition(TransitionEffect.OPACITY.animation({ duration: 1000 }))
          }

          // Replace $r('app.media.testImg') with the image resource file you use.
          Image($r('app.media.testImg'))
            .width(150)
            .height(150)
            .margin({ top: 50 })
            .id("image2")
            .transition(TransitionEffect.scale({ x: 0, y: 0 }).animation({ duration: 1000 }))
          Text("view").margin({ top: 50 })
        }
        .id("column1")
        .transition(TransitionEffect.opacity(0.99).animation({ duration: 1000 }),
          // The end callback is set on the first layer of disappearing nodes to ensure that there is a callback at the end of the disappearance.
          (transitionIn: boolean) => {
            console.info("transition finish, transitionIn:" + transitionIn);
          }
        )
      }
    }.width('100%')
  }
}

Below you can see the example in action.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/0Hxsw-UuRGW2LNzTZVYEZA/en-us_image_0000002537765900.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35EF53D1CF5C084894C763EDA44D00C521F15481B48A3FF7F0CC9119DD26942C)
