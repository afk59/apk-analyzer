# Page Transition (pageTransition)

When performing route switching using the [router](../../../arkts-api/ui/ohos-router-page-routing-not-recommended/document.md), you can customize entrance and exit transition animations between pages by implementing the [pageTransition](../../custom-components/custom-component-lifecycle/document.md#pagetransition9) API. For details, see [Page Transition Animation](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-page-transition-animation).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/Etms9qTKTG2U9hSqQlEF5A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=257A2C02CD3AF669FE8AB92B89995208927C53820A1CBEAB87CB47E89E5E034F)

This feature is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

To achieve a better transition effect, you are advised to use the [Navigation](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-navigation-navigation) component and [modal transition](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-modal-transition).

#### PageTransitionEnter

PageTransitionEnter(value: PageTransitionOptions)

Sets the page entrance animation. Inherits from [CommonTransition](#commontransition).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [PageTransitionOptions](#pagetransitionoptions) | Yes | Page entrance animation. |

#### \[h2\]onEnter

onEnter(event: PageTransitionCallback): PageTransitionEnterInterface

Invoked on a per-frame basis until the entrance animation is complete, with the **progress** parameter changing from 0 to 1.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [PageTransitionCallback](#pagetransitioncallback18) | Yes | Callback invoked on a per-frame basis until the entrance animation is complete, with the **progress** parameter changing from 0 to 1. |

**Example**

  pageTransition() {
    PageTransitionEnter({ duration: 1200, curve: Curve.Linear })
      // During the transition animation, the entrance animation has a type that represents the route type, and a progress that increases from 0 to 1.
      .onEnter((type: RouteType, progress: number) => {
        // Service logic
      })
  }

#### PageTransitionExit

PageTransitionExit(value: PageTransitionOptions)

Sets the page exit animation. Inherits from [CommonTransition](#commontransition).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [PageTransitionOptions](#pagetransitionoptions) | Yes | Page exit animation. |

#### \[h2\]onExit

onExit(event: PageTransitionCallback): PageTransitionExitInterface

Invoked on a per-frame basis until the exit animation is complete, with the **progress** parameter changing from 0 to 1.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [PageTransitionCallback](#pagetransitioncallback18) | Yes | Callback invoked on a per-frame basis until the exit animation is complete, with the **progress** parameter changing from 0 to 1. |

**Example**

  pageTransition() {
    PageTransitionExit({ duration: 1200, curve: Curve.Linear })
      // During the transition animation, the exit animation has a type that represents the route type, and a progress that increases from 0 to 1.
      .onExit((type: RouteType, progress: number) => {
        // Service logic
      })
  }

#### PageTransitionOptions

**Atomic service API**: This API can be used in atomic services since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [RouteType](#routetype) | No | Yes | 
Route type for the page transition effect to take effect.

Default value: **RouteType.None**

 |
| duration | number | No | Yes | 

Animation duration.

Unit: ms

Default value: **1000**

Value range: \[0, +∞)

 |
| curve | [Curve](../../common-definitions/enums/document.md#curve) | string | [ICurve](../../../arkts-api/ui/ohos-curves-interpolation-calculation/document.md#icurve9)10+ | No | Yes | 

Animation curve.

You are advised to specify the curve using the **Curve** or **ICurve** type.

For the string type, this parameter indicates an animation interpolation curve. For available values, see the **curve** parameter in [AnimateParam](../explicit-animation-animateto/document.md#animateparam).

Default value: **Curve.Linear**

 |
| delay | number | No | Yes | 

Animation delay.

Unit: ms

Default value: **0**

**NOTE**

If no match is found, the default page transition effect is used (which may vary according to the device). To disable the default page transition effect, set **duration** to **0**.

 |

#### CommonTransition

Defines a common transition animation for page transitions.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor

constructor()

A constructor used to create a common transition animation.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]slide

slide(value: SlideEffect): T

Sets the slide-in and slide-out effects for page transitions.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [SlideEffect](#slideeffect) | Yes | Slide-in and slide-out effects for page transitions. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### \[h2\]translate

translate(value: TranslateOptions): T

Sets the translation effect for page transitions.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [TranslateOptions](../../universal-attributes/visual-effects/transformation/document.md#translateoptions) | Yes | 
Translation effect for page transitions, specifying the start value for entrance and the end value for exit. When this parameter is set together with **slide**, the latter takes effect by default.

\- **x**: translation distance along the x-axis.

\- **y**: translation distance along the y-axis.

\- **z**: translation distance along the y-axis.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### \[h2\]scale

scale(value: ScaleOptions): T

Sets the scaling effect for page transitions.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ScaleOptions](../../universal-attributes/visual-effects/transformation/document.md#scaleoptions) | Yes | 
Scaling effect for page transitions, specifying the start value for entrance and the end value for exit.

\- **x**: scale factor along the x-axis.

\- **y**: scale factor along the y-axis.

\- **z**: scale factor along the z-axis.

\- **centerX** and **centerY**: scaling center. The default values are both **"50%"**, meaning the center of the page is used as the scaling center by default.

\- If the center point is (0, 0), it refers to the upper left corner of the component.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### \[h2\]opacity

opacity(value: number): T

Sets the starting opacity value for entrance or the ending opacity value for exit.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Starting opacity value for entrance or the ending opacity value for exit.

Value range: \[0, 1\]

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### PageTransitionCallback18+

type PageTransitionCallback = (type: RouteType, progress: number) => void

Represents the callback for page transition events.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [RouteType](#routetype) | Yes | Type of page transition. |
| progress | number | Yes | Transition progress, ranging from 0 to 1. |

#### RouteType

Sets the type of page transition.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 11.

| Name | Description |
| :-- | :-- |
| Pop | Redirects to a specified page. To redirect the user from page B back to page A, set **RouteType** of **PageTransitionExit** to **None** or **Pop** for page B and set **RouteType** of **PageTransitionEnter** to **None** or **Pop** for page A. |
| Push | Redirects to the next page. To redirect the user from page A to page B, set **RouteType** of **PageTransitionExit** to **None** or **Push** for page A and set **RouteType** of **PageTransitionEnter** to **None** or **Push** for page B. |
| None | The page is not redirected. The animation specified by **PageTransitionEnter** takes effect for page entrance, and the animation specified by **PageTransitionExit** takes effect for page exit. |

#### SlideEffect

**Atomic service API**: This API can be used in atomic services since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| Left | 
When set to Enter, slides in from the left. When set to Exit, slides out to the left.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Right | 

When set to Enter, slides in from the right. When set to Exit, slides out to the right.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Top | 

When set to Enter, slides in from the top. When set to Exit, slides out to the top.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Bottom | 

When set to Enter, slides in from the bottom. When set to Exit, slides out to the bottom.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| START12+ | 

Left-to-right scripts: When set to Enter, slides in from the left; when set to Exit, slides out to the left. Right-to-left scripts: When set to Enter, slides in from the right; when set to Exit, slides out to the right.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| END12+ | 

Left-to-right scripts: When set to Enter, slides in from the right; when set to Exit, slides out to the right. Right-to-left scripts: When set to Enter, slides in from the left; when set to Exit, slides out to the left.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### Example

## Example 1: Configuring Entrance and Exit Animations

Method 1: Configure different entrance and exit animations based on different transition types.

// Index.ets
@Entry
@Component
struct Index {
  @State scale1: number = 1;
  @State opacity1: number = 1;

  build() {
    Column() {
      // Replace $r("app.media.transition\_image1") with the image resource file you use.
      Image($r("app.media.transition\_image1")).width('100%').height('100%')
    }
    .width('100%')
    .height('100%')
    .scale({ x: this.scale1 })
    .opacity(this.opacity1)
    .onClick(() => {
      this.getUIContext().getRouter().pushUrl({ url: 'pages/Page1' });
    })
  }

  pageTransition() {
    PageTransitionEnter({ duration: 1200, curve: Curve.Linear })
      .onEnter((type: RouteType, progress: number) => {
        if (type == RouteType.Push || type == RouteType.Pop) {
          this.scale1 = progress;
          this.opacity1 = progress;
        }
      })
    PageTransitionExit({ duration: 1200, curve: Curve.Ease })
      .onExit((type: RouteType, progress: number) => {
        if (type == RouteType.Push) {
          this.scale1 = 1 - progress;
          this.opacity1 = 1 - progress;
        }
      })
  }
}

// Page1.ets
@Entry
@Component
struct Page1 {
  @State scale2: number = 1;
  @State opacity2: number = 1;

  build() {
    Column() {
      // Replace $r("app.media.transition\_image2") with the image resource file you use.
      Image($r("app.media.transition\_image2")).width('100%').height('100%') // Store the image in the media folder.
    }
    .width('100%')
    .height('100%')
    .scale({ x: this.scale2 })
    .opacity(this.opacity2)
    .onClick(() => {
      this.getUIContext().getRouter().pushUrl({ url: 'pages/Index' });
    })
  }

  pageTransition() {
    PageTransitionEnter({ duration: 1200, curve: Curve.Linear })
      .onEnter((type: RouteType, progress: number) => {
        if (type == RouteType.Push || type == RouteType.Pop) {
          this.scale2 = progress;
        }
        this.opacity2 = progress;
      })
    PageTransitionExit({ duration: 1200, curve: Curve.Ease })
      .onExit((type: RouteType, progress: number) => {
        if (type == RouteType.Pop) {
          this.scale2 = 1 - progress;
          this.opacity2 = 1 - progress;
        }
      })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/69NfmRdfQyOYi1EHoJvMwA/en-us_image_0000002568685613.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EB1EBEA8214C6622ED25F242AD7B393B164CED17E0F87D6C0B3BE32845B7C214)

Customization method 2: The entrance animation of the current page is configured to slide in from the left, and the exit animation is configured to translate with opacity change.

// Index.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      // Replace $r('app.media.bg1') with the image resource file you use.
      Image($r('app.media.bg1')).width('100%').height('100%') // The image is stored in the media folder.
    }
    .onClick(() => {
      this.getUIContext().getRouter().pushUrl({ url: 'pages/Page1' });
    })
  }

  // Use the default effects provided by the system, such as translation, scaling, and opacity.
  pageTransition() {
    // Set the duration of the entrance animation to 1200 ms, in the purpose of matching the duration of the exit animation of the other page.
    PageTransitionEnter({ duration: 1200 })
      .slide(SlideEffect.Left)
    // Set the duration of the exit animation to 1000 ms, in the purpose of matching the duration of the entrance animation of the other page.
    PageTransitionExit({ duration: 1000 })
      .translate({ x: 100.0, y: 100.0 })
      .opacity(0)
  }
}

// Page1.ets
@Entry
@Component
struct Page1 {
  build() {
    Column() {
      // Replace $r('app.media.bg2') with the image resource file you use.
      Image($r('app.media.bg2')).width('100%').height('100%') // The image is stored in the media folder.
    }
    .onClick(() => {
      this.getUIContext().getRouter().pushUrl({ url: 'pages/Index' });
    })
  }

  // Use the default effects provided by the system, such as translation, scaling, and opacity.
  pageTransition() {
    // Set the duration of the entrance animation to 1000 ms, in the purpose of matching the duration of the exit animation of the other page.
    PageTransitionEnter({ duration: 1000 })
      .slide(SlideEffect.Left)
    // Set the duration of the exit animation to 1200 ms, in the purpose of matching the duration of the entrance animation of the other page.
    PageTransitionExit({ duration: 1200 })
      .translate({ x: 100.0, y: 100.0 })
      .opacity(0)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/cwD0N-ATTvabhnr4Rb6h5A/en-us_image_0000002568765623.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1BF2974369EADC37107D5BC016FA76243A84F9A47F0C55DD08453E664CB4D60)

## Example 2: Setting Translation Effects for Entrance and Exit

Customization method 1: Configure the various entrance and exit translation effects provided, with the system language layout mode set to right-to-left (RTL).

// Index.ets
@Entry
@Component
struct Index {
  @State scale1: number = 1;
  @State opacity1: number = 1;

  build() {
    Column() {
      Button("Page 1").onClick(() => {
        this.getUIContext().getRouter().pushUrl({
          url: "pages/Page1"
        })
      })
        .width(200)
        .height(60)
        .fontSize(36)
      Text("START")
        .fontSize(36)
        .textAlign(TextAlign.Center)
    }
    .scale({ x: this.scale1 })
    .opacity(this.opacity1)
    .height("100%")
    .width("100%")
    .justifyContent(FlexAlign.Center)
  }

  // Customization method 2: Use the default effects provided by the system, such as translation, scaling, and opacity.
  pageTransition() {
    // Set the entrance animation.
    PageTransitionEnter({ duration: 200 })
      .slide(SlideEffect.START)
    // Set the exit animation.
    PageTransitionExit({ delay: 100 })
      .slide(SlideEffect.START) //Left
  }
}

// Page1.ets
@Entry
@Component
struct Page1 {
  @State scale1: number = 1;
  @State opacity1: number = 1;

  build() {
    Column() {
      Button("Page 2").onClick(() => {
        this.getUIContext().getRouter().pushUrl({
          url: "pages/Index"
        });
      })
        .width(200)
        .height(60)
        .fontSize(36)
      Text("END")
        .fontSize(36)
        .textAlign(TextAlign.Center)
    }
    .scale({ x: this.scale1 })
    .opacity(this.opacity1)
    .height("100%")
    .width("100%")
    .justifyContent(FlexAlign.Center)
  }

  // Customization method 2: Use the default effects provided by the system, such as translation, scaling, and opacity.
  pageTransition() {
    PageTransitionEnter({ duration: 200 })
      .slide(SlideEffect.END) //Right
    PageTransitionExit({ delay: 100 })
      .slide(SlideEffect.END) //Right
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/_SaVOW61Tpq3ZmikhSuLKg/en-us_image_0000002537765898.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5FB01D0504A918390FBB281ADF8AA7DE3041FF1E828AF8C2B13F0F924BFACA2)

Customization method 2: Use the system's default entrance and exit effects, with the system language layout mode set to right-to-left (RTL).

// Index.ets
@Entry
@Component
struct Index {
  @State scale1: number = 1;
  @State opacity1: number = 1;

  build() {
    Column() {
      Button("Page 1").onClick(() => {
        this.getUIContext().getRouter().pushUrl({
          url: "pages/Page1"
        });
      })
        .width(200)
        .height(60)
        .fontSize(36)
    }
    .scale({ x: this.scale1 })
    .opacity(this.opacity1)
    .height("100%")
    .width("100%")
    .justifyContent(FlexAlign.Center)
  }
}

// Page1.ets
@Entry
@Component
struct Page1 {
  @State scale1: number = 1;
  @State opacity1: number = 1;

  build() {
    Column() {
      Button("Page 2").onClick(() => {
        this.getUIContext().getRouter().pushUrl({
          url: "pages/Index"
        });
      })
        .width(200)
        .height(60)
        .fontSize(36)
    }
    .scale({ x: this.scale1 })
    .opacity(this.opacity1)
    .height("100%")
    .width("100%")
    .justifyContent(FlexAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/JVqc760IRY-m2DCdijuzHA/en-us_image_0000002537925838.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD9A31D95CB992EAE782D143BCD9376F0F50AB08E8CB0FFCA4B619E045834CCD)
