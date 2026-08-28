# hdsEffect

This module extends visual effects for components, encompassing point-light effects, press illumination effects, and animation control.

**Start version**: 6.0.0(20)

#### Modules to Import

import { hdsEffect } from '@kit.UIDesignKit';

#### HdsEffectBuilder

Adds the visual effect parameters to the **VisualEffect** object and constructs the object.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

#### \[h2\]constructor

constructor()

Constructor for **HdsEffectBuilder**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

#### \[h2\]pointLight

pointLight(value: PointLightEffect): HdsEffectBuilder

Creates a point-light effect for a component. A component can be illuminated by a maximum of 12 light sources at the same time. The following components support the point-light effect: Button, Toggle, Row, Column, Image, Flex, Stack, Select, Menu, and MenuItem.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[PointLightEffect](#section19211215155213)

 | 

Yes

 | 

Point-light effect parameters. You can apply a point-light effect by setting the point light emission and illuminated types to achieve a UI effect where a point-light source illuminates surrounding components.

NOTE:

The light source position is initially at the center of the component but does not move with the component. Therefore, you are not advised to use this effect for scrollable components.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HdsEffectBuilder](#section10585433123716)

 | 

**HdsEffectBuilder** object.

 |

**Example**:

import { hdsEffect } from '@kit.UIDesignKit';

@Entry
@Component
struct Index {
  @State lightSourceType: hdsEffect.PointLightSourceType = hdsEffect.PointLightSourceType.NONE;
  build() {
    Column({ space: 10 }) {
      Row({ space: 10 }) {
        Column() {
          Text('illuminated').padding(10).fontColor(Color.White)
          Text('illuminated').padding(10).fontColor(Color.White)
          Text('illuminated').padding(10).fontColor(Color.White)
        }
        .visualEffect(new hdsEffect.HdsEffectBuilder()
          .pointLight({
            illuminatedType: hdsEffect.PointLightIlluminatedType.BORDER
          })
          .buildEffect())
      }
      Row({ space: 10 }) {
        Button('lightSource')
          .visualEffect(new hdsEffect.HdsEffectBuilder()
            .pointLight({
              sourceType: this.lightSourceType,
              illuminatedType: hdsEffect.PointLightIlluminatedType.BORDER
            })
            .buildEffect())
          .onTouch((event: TouchEvent) => {
            if (event.type === TouchType.Down) {
              this.lightSourceType = hdsEffect.PointLightSourceType.BRIGHT;
            } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
              this.lightSourceType = hdsEffect.PointLightSourceType.NONE;
            }
          })
      }
      Row({ space: 10 }) {
        Column() {
          Text('illuminated').padding(10).fontColor(Color.White)
          Text('illuminated').padding(10).fontColor(Color.White)
          Text('illuminated').padding(10).fontColor(Color.White)
        }
        .visualEffect(new hdsEffect.HdsEffectBuilder()
          .pointLight({
            illuminatedType: hdsEffect.PointLightIlluminatedType.BORDER
          })
          .buildEffect())
      }
    }
    .backgroundColor(Color.Black)
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/xDcYD2Q-Q0y0m0q8T7ZtBw/en-us_image_0000002500424064.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CAA38540B91DAFEAEFF2AFD44C1C5998A0CA28876D6DE6903598AC1F1006C617 "Click to enlarge")

#### \[h2\]pressShadow

pressShadow(type: PressShadowType): HdsEffectBuilder

Sets the shadow effect upon a press for the current component, which usually applies to background color changes after the component is pressed. This API is available only for button components.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

[PressShadowType](#section83024319529)

 | 

Yes

 | 

Shadow effect after a component is pressed.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HdsEffectBuilder](#section10585433123716)

 | 

**HdsEffectBuilder** object.

 |

**Example**:

import { hdsEffect } from '@kit.UIDesignKit';

@Entry
@Component
struct PressShadowExample {
  @State button\_blend\_state: hdsEffect.PressShadowType = hdsEffect.PressShadowType.NONE;
  @State button\_gradient\_state: hdsEffect.PressShadowType = hdsEffect.PressShadowType.NONE;

  build() {
    NavDestination() {
      Column({ space: 50 }) {
        Button("BLEND\_WHITE", { buttonStyle: ButtonStyleMode.EMPHASIZED, role: ButtonRole.ERROR, stateEffect: false })
          .visualEffect(new hdsEffect.HdsEffectBuilder()
            .pressShadow(this.button\_blend\_state)
            .buildEffect())
          .onTouch((event: TouchEvent) => {
            if (event.type === TouchType.Down) {
              this.button\_blend\_state =  hdsEffect.PressShadowType.BLEND\_WHITE;
            } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
              this.button\_blend\_state =  hdsEffect.PressShadowType.NONE;
            }
          })

        Button("GRADIENT", { buttonStyle: ButtonStyleMode.NORMAL, stateEffect: false })
          .visualEffect(new hdsEffect.HdsEffectBuilder()
            .pressShadow(this.button\_gradient\_state)
            .buildEffect())
          .onTouch((event: TouchEvent) => {
            if (event.type === TouchType.Down) {
              this.button\_gradient\_state =  hdsEffect.PressShadowType.BLEND\_GRADIENT;
            } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
              this.button\_gradient\_state =  hdsEffect.PressShadowType.NONE;
            }
          })
      }
      .height('70%')
      .justifyContent(FlexAlign.Center)
    }
    .width('100%')
    .height('100%')
    .title('Button example')
    .backgroundColor('#040404')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/V6LcldmPSo6YeWdwo5DJ0g/en-us_image_0000002532304097.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02D57275269DAF127B8DD5F3A7126722EEA8C8EF6C4E7DCA3D492C652CA7EDF1)

#### \[h2\]shaderEffect

shaderEffect(params: ShaderEffectParams): HdsEffectBuilder

Creates a shader visual effect.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

params

 | 

[ShaderEffectParams](#section67731724154216)

 | 

Yes

 | 

Shader visual effect parameters.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HdsEffectBuilder](#section10585433123716)

 | 

**HdsEffectBuilder** object.

 |

**Example**:

import { hdsEffect } from '@kit.UIDesignKit';

@Entry
@Component
struct Index {
  @State controller: hdsEffect.ShaderEffectController = new hdsEffect.ShaderEffectController();

  build() {
    Column() {
      Stack() {
      }
      .visualEffect(new hdsEffect.HdsEffectBuilder()
        .shaderEffect({
          effectType: hdsEffect.EffectType.DUAL\_EDGE\_FLOW\_LIGHT,
          animation: {
            duration: 4000,
            iterations: -1,
            autoPlay: true,
            onFinish: () => {
              console.info('Succeeded in finishing');
            }
          },
          controller: this.controller,
          params: {
            firstEdgeFlowLight: {
              startPos: 0,
              endPos: 1.0,
              color: '#1AD0F1',
            },
            secondEdgeFlowLight: {
              startPos: 0.5,
              endPos: 1.5,
              color: '#FFA4E5',
            }
          }
        })
        .buildEffect())
      .width(200)
      .borderRadius('50%')
      .clip(true)
      .height(200)
      .backgroundColor('#383838')
    }
    .justifyContent(FlexAlign.Center)
    .backgroundColor(Color.Black)
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/IPJRwAWQSQy5Ps8MC_60Ew/en-us_image_0000002500424058.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=031509F61C26174725090485BA7F578FB9E0071BA280CA9B441C9739A29D984E)

#### \[h2\]buildEffect

buildEffect(): VisualEffect

Adds all visual effects configured above to the **VisualEffect** object.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[VisualEffect](../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-uieffect-cascading-effect/document.md#visualeffect)

 | 

**VisualEffect** object that contains various visual effects.

 |

#### ShaderEffectParams

Defines visual effect settings for **shaderEffect**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

**Optional**

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

effectType

 | 

[EffectType](#section139655943218)

 | 

No

 | 

No

 | 

Visual effect type.

 |
| 

animation

 | 

[AnimationParams](#section17826183003616)

 | 

No

 | 

Yes

 | 

Visual effect animation parameters.

 |
| 

params

 | 

[EffectParams](#section2246122705112)

 | 

No

 | 

Yes

 | 

Shader parameters.

 |
| 

controller

 | 

[ShaderEffectController](#section03476195383)

 | 

No

 | 

Yes

 | 

Visual effect controller.

 |

#### EffectType

Defines visual effect types.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

DUAL\_EDGE\_FLOW\_LIGHT

 | 

0

 | 

Dual-edge flowing light effect.

NOTE:

This effect does not apply for TVs.

 |
| 

UV\_BACKGROUND\_FLOW\_LIGHT

 | 

1

 | 

UV background flowing light effect.

NOTE:

This effect does not apply for TVs.

 |

#### AnimationParams

Defines visual effect animation parameters.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

**Optional**

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

duration

 | 

number

 | 

No

 | 

Yes

 | 

Time for playing the visual effect animation once, in milliseconds.

The default value is **1000**.

**Note**:

\- A value less than 0 evaluates to the value **0**.

\- Floating-point values will be rounded down to integers. For example, if the value set is 1.2, **1** will be used.

 |
| 

iterations

 | 

number

 | 

No

 | 

Yes

 | 

Number of playbacks. The value **\-1** indicates continuous looping.

Value range: \[-1,+∞)

The default value is **1**.

**Note**:

\- If the value is out of the range, the default value is used.

\- Floating-point values will be rounded down to integers. For example, if the value set is 1.2, **1** will be used.

 |
| 

curve

 | 

[Curve](../../../arkui/arkts-components/common-definitions/enums/document.md#curve)

 | 

No

 | 

Yes

 | 

Animation curve.

 |
| 

delay

 | 

number

 | 

No

 | 

Yes

 | 

Delay for playing the visual effect animation, in milliseconds.

The default value is **0**.

Value range: (-∞, +∞)

**Note**:

\- A value greater than or equal to 0 means to start the animation after the specified amount of time has elapsed, and a value less than 0 means to start the animation in advance. When the value is less than 0: If the absolute value of **delay** is less than the actual animation duration, the animation starts its first frame from the progress state at the absolute value; if the absolute value of **delay** is greater than or equal to the actual animation duration, the animation directly ends. The actual animation duration is equal to the duration of a single animation multiplied by the number of animation playback times.

\- Floating-point values will be rounded down to integers. For example, if the value set is 1.2, **1** will be used.

 |
| 

autoPlay

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the animation starts automatically. The options are **true** (yes) and **false** (no).

The default value is **true**.

 |
| 

onFinish

 | 

[OnFinishCallback](#section11120115316396)

 | 

No

 | 

Yes

 | 

Callback function triggered when animation playback ends.

 |
| 

expectedFrameRateRange

 | 

[ExpectedFrameRateRange](#section19809172171211)

 | 

No

 | 

Yes

 | 

Expected frame rate range.

 |

#### OnFinishCallback

type OnFinishCallback = () => void

Defines the callback triggered upon animation ending.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

#### ExpectedFrameRateRange

Defines the visual effect frame rate range settings.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

expected

 | 

[FrameRateType](#section17378113301412)

 | 

No

 | 

No

 | 

Expected frame rate.

 |
| 

min

 | 

[FrameRateType](#section17378113301412)

 | 

No

 | 

No

 | 

Minimum frame rate.

 |
| 

max

 | 

[FrameRateType](#section17378113301412)

 | 

No

 | 

No

 | 

Maximum frame rate.

 |

#### FrameRateType

Defines the visual effect frame rate options.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

FRAME\_RATE\_15

 | 

15

 | 

15 fps frame rate.

 |
| 

FRAME\_RATE\_30

 | 

30

 | 

30 fps frame rate.

 |
| 

FRAME\_RATE\_60

 | 

60

 | 

60 fps frame rate.

 |

#### EffectParams

type EffectParams = DualEdgeFlowLightParam | UVFlowLightColorParam

Defines visual effect parameters.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DualEdgeFlowLightParam](#section15132153911546)

 | 

Dual-edge flowing light effect parameters.

 |
| 

[UVFlowLightColorParam](#section219214925411)

 | 

UV flowing light effect parameters.

 |

#### DualEdgeFlowLightParam

Defines dual-edge flowing light effect parameters.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

firstEdgeFlowLight

 | 

[EdgeFlowLightParam](#section63471415181915)

 | 

No

 | 

No

 | 

Parameters of the first flowing light edge.

 |
| 

secondEdgeFlowLight

 | 

[EdgeFlowLightParam](#section63471415181915)

 | 

No

 | 

No

 | 

Parameters of the second flowing light edge.

 |

#### UVFlowLightColorParam

Defines UV flowing light effect parameters.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

**Optional**

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

colorSource

 | 

Array<[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)\>

 | 

No

 | 

No

 | 

Array of background colors before the gradient color change.

 |
| 

colorTarget

 | 

Array<[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)\>

 | 

No

 | 

Yes

 | 

Array of background colors after the gradient color change. The color of the flowing light does not change by default.

 |

#### EdgeFlowLightParam

Defines edge flowing light effect parameters.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

**Optional**

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

startPos

 | 

number

 | 

No

 | 

No

 | 

Flowing light starting point. The starting point is represented by the ratio of the distance between the midpoint of the visual effect container's top edge and the starting point along the container's edge in a specified direction, relative to the container's total perimeter. Moving counter-clockwise along the container's edge is the positive direction and is represented using a positive value of this parameter; while moving clockwise is the negative direction and is represented using a negative value of this parameter.

 |
| 

endPos

 | 

number

 | 

No

 | 

No

 | 

Flowing light ending point. The starting point is represented by the ratio of the distance between the midpoint of the visual effect container's top edge and the starting point along the container's edge in a specified direction, relative to the container's total perimeter. Moving counter-clockwise along the container's edge is the positive direction and is represented using a positive value of this parameter; while moving clockwise is the negative direction and is represented using a negative value of this parameter.

 |
| 

color

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

No

 | 

Color of the flowing light on the current edge.

 |

#### ShaderEffectController

Defines the visual effect controller.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

#### \[h2\]constructor

constructor()

Constructor for **ShaderEffectController**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

#### \[h2\]play

play(): void

Starts playing a visual effect animation.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

#### \[h2\]pause

pause(): void

Pauses a visual effect animation.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

#### \[h2\]resume

resume(): void

Resumes a visual effect animation.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

#### \[h2\]reverse

reverse(): void

Reverses a visual effect animation.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

#### \[h2\]stop

stop(): void

Stops playing a visual effect animation.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

#### \[h2\]setEffectParams

setEffectParams(params: EffectParams): void

Sets visual effect shader parameters.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

params

 | 

[EffectParams](#section2246122705112)

 | 

Yes

 | 

Shader visual effect parameters.

 |

#### PointLightEffect

Defines point-light effect parameters.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

sourceType

 | 

[PointLightSourceType](#section86635247262)

 | 

No

 | 

Yes

 | 

Light emission type of a component. The light emission affects the surrounding components that are marked as illuminable and creates light effects on those components.

The default value is **NONE**, indicating that the component does not emit light.

 |
| 

illuminatedType

 | 

[PointLightIlluminatedType](#section2083334203018)

 | 

No

 | 

Yes

 | 

Illumination type of a component, which defines whether this component can be illuminated by a light source and the illuminated type.

The default value is **NONE**, indicating that the component will not be illuminated.

NOTE:

If the border color and width are set for an illuminated component, these settings take priority and the point-light illumination effect on the border will not take effect.

 |
| 

options

 | 

[PointLightOptions](#section102501857172520)

 | 

No

 | 

Yes

 | 

Custom point-light effect options of a component.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/ViQ80cpHRxqo38Oxiwbl1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E803D6E33EFBC4328B7DB5C57435A468238696520AC9F58CAF4B259D8A100D40)

**sourceType** takes precedence over **options**. That is, if both **sourceType** and **options** are set, the setting of **options** does not take effect.

#### PointLightSourceType

Defines light emission types of a component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Value**

 | 

Description

 |
| :-- | :-- | :-- |
| 

NONE

 | 

0

 | 

The point-light effect does not take effect and the component does not emit light.

 |
| 

SOFT

 | 

1

 | 

A soft point-light effect is applied, with weak light intensity and a smaller surrounding illumination range.

 |
| 

BRIGHT

 | 

2

 | 

A bright point-light effect is applied, with strong light intensity and a larger surrounding illumination range.

 |

#### PointLightIlluminatedType

Defines illuminated types of a component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Value**

 | 

Description

 |
| :-- | :-- | :-- |
| 

NONE

 | 

0

 | 

The component is not illuminated.

 |
| 

BORDER

 | 

1

 | 

Only the edges of the component are illuminated.

 |
| 

CONTENT

 | 

2

 | 

Only the content of the component is illuminated.

 |
| 

BORDER\_CONTENT

 | 

3

 | 

Both the edges and content of the component are illuminated.

 |
| 

DEFAULT\_FEATHERING\_BORDER

 | 

20

 | 

Only the edges of the component are illuminated, with a feathered effect.

 |

#### PointLightOptions

Defines the custom point-light effect options of a component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

color

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Light source color.

The default value is **Color.White**.

 |
| 

intensity

 | 

number

 | 

No

 | 

Yes

 | 

Intensity of the light source. The recommended value range is 0–1. A larger numeric value indicates stronger light intensity. When the light source intensity is 0, the light source does not emit light.

The default value is **0**.

 |
| 

height

 | 

[Dimension](../../../arkui/arkts-components/common-definitions/basic-types/document.md#dimension10)

 | 

No

 | 

Yes

 | 

Height of the light source. The higher the light source, the broader the light illumination.

The default value is **0**.

 |
| 

bloom

 | 

number

 | 

No

 | 

Yes

 | 

Bloom effect intensity of the component. The recommended value range is 0–1. A larger numeric value indicates a larger bloom range.

The default value is **0**.

 |

#### PressShadowType

Defines the shadow effect types after a component is pressed.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

NONE

 | 

0

 | 

No shadow effect is applied upon a press.

 |
| 

BLEND\_GRADIENT

 | 

1

 | 

The shadow is an elliptical radial gradient of white, with the center being 85% transparent white and the edges being opaque white. It is overlaid on the background color of the component.

 |
| 

BLEND\_WHITE

 | 

2

 | 

The shadow is 15% transparent white, and is overlaid on the background color of the component.

 |
