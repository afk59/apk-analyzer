# Shared Element Transition (sharedTransition)

A shared element transition is a transition animation applied to a component that is present on two pages. This component is called the shared element and can be set in the **sharedTransition** attribute. The **sharedTransition** attribute is effective only during [page routing](../../../arkts-api/ui/ohos-router-page-routing-not-recommended/document.md) transitions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/bFdmZk6zRVuHJjvB4FuGIg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFCD657D6CDD4D6D16693BF339BD887D47582AC3B4BA35CFEE82451B7CCBC1AF)

This feature is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### sharedTransition

sharedTransition(id: string, options?: sharedTransitionOptions): T

Sets the shared transition animation.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | Transition of the shared element. If the same **id** value is configured for a component on the two pages, this component is considered as a shared element of the pages. If the **id** value is an empty string, no transition will be applied to the component. |
| options | [sharedTransitionOptions](#sharedtransitionoptions) | No | Parameters of the shared element transition animation. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### sharedTransitionOptions

Parameters of the shared element transition animation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/3CgNL_w_Qsmbvd4KphPZqA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E78C68CDA1902B6700C243ADBF25093A5483B3928457F07E833DDB93BA3C257A)

**motionPath** is effective only when **type** is set to **SharedTransitionEffectType.Exchange**.

When **type** is set to **SharedTransitionEffectType.Exchange**, the effect focuses on smooth transition of the position and size of matching shared elements, which can be visually observed through the component's border. The transition, however, does not involve content properties, which will abruptly change to the target page's values at the end of the animation. For example, if a **Text** component has different **fontSize** values on two pages, the font size will snap to the target page's value once the shared transition animation completes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| duration | number | No | Yes | 
Animation duration.

Default value: **1000**

Unit: ms

Value range: \[0, +∞)

 |
| curve | [Curve](../../common-definitions/enums/document.md#curve) | string | [ICurve](../../../arkts-api/ui/ohos-curves-interpolation-calculation/document.md#icurve9) | No | Yes | 

Animation curve.

You are advised to specify the curve using the **Curve** or **ICurve** type.

For the string type, this parameter indicates an animation interpolation curve. For available values, see the **curve** parameter in [AnimateParam](../explicit-animation-animateto/document.md#animateparam).

Default value: **Curve.Linear**

 |
| delay | number | No | Yes | 

Delay of animation playback.

Default value: **0**

Unit: ms

 |
| motionPath | [MotionPathOptions](../motion-path-animation-motionpath/document.md#motionpathoptions) | No | Yes | Motion path. |
| zIndex | number | No | Yes | 

Z-axis.

Value range: (-∞, +∞)

Default value: **0**

 |
| type | [SharedTransitionEffectType](../../common-definitions/enums/document.md#sharedtransitioneffecttype) | No | Yes | 

Animation type.

Default value: **SharedTransitionEffectType.Exchange**

 |

#### Example

This example implements the custom transition of a shared image during redirection from one page to another, which is triggered by a click on the image.

// xxx.ets
@Entry
@Component
struct SharedTransitionExample {

  build() {
    Column() {
      // Replace $r('app.media.ic\_health\_heart') with the image resource file you use.
      Image($r('app.media.ic\_health\_heart')).width(50).height(50).margin({ left: 20, top: 20 })
        .sharedTransition('sharedImage', { duration: 800, curve: Curve.Linear, delay: 100 })
    }.width('100%').height('100%').alignItems(HorizontalAlign.Start)
    .onClick(() => {
      this.getUIContext().getRouter().pushUrl({ url: 'pages/PageB' })
    })
  }

  pageTransition() {
    PageTransitionEnter({ type: RouteType.None, duration: 0 })
    PageTransitionExit({ type: RouteType.None, duration: 0 })
  }
}

// PageB.ets
@Entry
@Component
struct PageBExample {
  build() {
    Stack() {
      // Replace $r('app.media.ic\_health\_heart') with the image resource file you use.
      Image($r('app.media.ic\_health\_heart')).width(150).height(150)
        .sharedTransition('sharedImage', { duration: 800, curve: Curve.Linear, delay: 100 })
    }.width('100%').height('100%')
  }

  pageTransition() {
    PageTransitionEnter({ type: RouteType.None, duration: 0 })
    PageTransitionExit({ type: RouteType.None, duration: 0 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/Re1_we9yRNGGCgfAA6FSQA/en-us_image_0000002537925840.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DE56A47D7A82DC7E16896DB2FBC0D6DD331856DE7862E95593F9C30F1CA6409)
