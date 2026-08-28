# Span

As a child of the [Text](../text/document.md) and [ContainerSpan](../containerspan/document.md) components, the **Span** component is used to display inline text.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/HNQeW1O9QaWLq9NLE-bvlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7686B24E4E3B13278701BFEAD79595695280B01AE5FC8754BDABB1EAC5312EDC)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

This component is supported since API version 10. It can inherit attribute settings from its parent component **Text**. This means that, if an attribute is not set in this component, it takes the value (if any) of the attribute from its parent component. Only the following attributes can be inherited: **fontColor**, **fontSize**, **fontStyle**, **fontWeight**, **decoration**, **letterSpacing**, **textCase**, **fontFamily**, and **textShadow**.

The [universal attributes](../../universal-attributes/document.md) are not supported. To set universal attributes, use [Text](../text/document.md) for configuration or use [CustomSpan](../styled-string/document.md#customspan) in the [Styled String](../styled-string/document.md) for custom drawing.

Among [universal events](../../universal-events/document.md), only [onClick](../../universal-events/interaction-response-events/click-event/document.md#onclick) click events and [onHover](../../universal-events/interaction-response-events/hover-event/document.md#onhover) hover events are supported.

#### Child Components

Not supported

#### APIs

Span(value: string | Resource)

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | Plain text. |

#### Attributes

Inherited from [BaseSpan](#basespan).

#### \[h2\]decoration

decoration(value: DecorationStyleInterface)

Style and color of the text decorative line.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [DecorationStyleInterface12+](../styled-string/document.md#decorationstyleinterface) | Yes | 
Style of the text decorative line.

Default value:

{

type: TextDecorationType.None,

color: Color.Black,

style: TextDecorationStyle.SOLID

}

**NOTE**

The **style** parameter cannot be used in widgets.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/PmChqgMsQDukXhnNzjPeGA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DBF5413B7F9592A2A9E2ECC55D02904420290170B2BEBFC91940F22BCB127F26)

When the bottom contour of a character intersects with the decoration, underline avoidance is triggered, commonly affecting characters like "g", "j", "y", "q", and "p."

If the decoration color is set to **Color.Transparent**, it inherits the text color of the first character in each line. If the decoration color is set to **"#00FFFFFF"**, the line becomes fully transparent.

#### \[h2\]letterSpacing

letterSpacing(value: number | ResourceStr)

Sets the letter spacing. A negative value tightens the spacing; a positive value loosens the spacing, and the letters are spread farther apart with the value. For the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | 
Letter spacing.

Unit: [fp](../../common-definitions/pixel-units/document.md)

The [Resource](../../common-definitions/basic-types/document.md#resource) type is supported since API version 20.

 |

#### \[h2\]textCase

textCase(value: TextCase)

Sets the text case.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [TextCase](../../common-definitions/enums/document.md#textcase) | Yes | 
Text case.

Default value: **TextCase.Normal**

 |

#### \[h2\]fontColor

fontColor(value: ResourceColor)

Sets the font color.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Font color.

Default value: **'e6182431'**.

Default value for wearables: **'#c5ffffff'**

 |

#### \[h2\]fontSize

fontSize(value: number | string | Resource)

Sets the font size.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Font size. If **fontSize** is of the number type, the unit fp is used. The default font size is 16 fp. For the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported. Percentage values are not supported.

Default value on wearable devices: **15fp**.

 |

#### \[h2\]fontStyle

fontStyle(value: FontStyle)

Sets the font style.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [FontStyle](../../common-definitions/enums/document.md#fontstyle) | Yes | 
Font style.

Default value: **FontStyle.Normal**

 |

#### \[h2\]fontWeight

fontWeight(value: number | FontWeight | ResourceStr)

Sets the font weight. If the value is too large, the text may be clipped depending on the font.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | [FontWeight](../../common-definitions/enums/document.md#fontweight) | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | 
Font weight. For the number type, the value range is \[100, 900\], at an interval of 100. The default value is **400**. A larger value indicates a heavier font weight. For the string type, only strings of the number type are supported, for example, **400**, **"bold"**, **"bolder"**, **"lighter"**, **"regular"**, and **"medium"**, which correspond to the enumerated values in **FontWeight**.

Default value: **FontWeight.Normal**

The [Resource](../../common-definitions/basic-types/document.md#resource) type is supported since API version 20.

 |

#### \[h2\]fontFamily

fontFamily(value: string | Resource)

Sets the font family.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Font family.

Default font: **'HarmonyOS Sans'**

To specify multiple fonts, separate them with commas (,), and fonts are applied in priority order. Example: **'Arial, HarmonyOS Sans'**.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/hIiibw83S8ywxIvlASNCYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0ABC5003E2E0A8115828BCB3A8B71AC33C7C99645B9D448CE96C3B25C353331E)

You can use [loadFontSync](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#loadfontsync) to register custom fonts.

#### \[h2\]lineHeight10+

lineHeight(value: Length)

Sets the line height for the text.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Line height of the text.

If the value is of the number type, the unit is fp. When using the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported.

 |

#### \[h2\]font10+

font(value: Font)

Sets the text style, covering the font size, font width, Font family, and font style.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Font](../../common-definitions/basic-types/document.md#font) | Yes | Text style. |

#### \[h2\]textShadow11+

textShadow(value: ShadowOptions | Array<ShadowOptions>)

Text shadow. It supports input parameters in an array to implement multiple text shadows. This API does not work with the **fill** attribute or coloring strategy.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ShadowOptions](../../universal-attributes/visual-effects/image-effect/document.md#shadowoptions) | Array<[ShadowOptions](../../universal-attributes/visual-effects/image-effect/document.md#shadowoptions)\> | Yes | Text shadow. |

#### Events

Among universal events, only [onClick](../../universal-events/interaction-response-events/click-event/document.md#onclick) click events and [onHover](../../universal-events/interaction-response-events/hover-event/document.md#onhover) hover events are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/_cK1Jz6dS5y8_u9HRK2coA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AFDD9A9277360CC6E8AE4D0200B80C2AB78513C720583FF4C6FC38EE44586689)

As the **Span** component does not include size information, the **target** attribute of the **ClickEvent** object returned by the click event is invalid.

#### BaseSpan

Defines the base class **BaseSpan**, including the universal attributes of the **Span** component.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

#### \[h2\]textBackgroundStyle11+

textBackgroundStyle(style: TextBackgroundStyle): T

Background style. This attribute prioritizes the value separately set for the component. If it is not set, the component can inherit the settings from its parent [ContainerSpan](../containerspan/document.md).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [TextBackgroundStyle](#textbackgroundstyle11) | Yes | 
Sets the background style.

Default value:

{

color: Color.Transparent,

radius: 0

}

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Attributes of the span. |

#### \[h2\]baselineOffset12+

baselineOffset(value: LengthMetrics): T

Sets the offset of the baseline. This attribute coexists with the **baselineOffset** attribute of the parent component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | Yes | 
Offset of the baseline. If the value specified is a percentage, the default value is used.

A positive value moves the content upwards, while a negative value moves it downwards.

Default value: **0**

In the **ImageSpan**, when this parameter is set to a non-zero value, the [verticalAlign](../imagespan/document.md#verticalalign) is fixed to **ImageSpanAlignment.BASELINE**; when this parameter is set to **0**, [verticalAlign](../imagespan/document.md#verticalalign) must be set to **ImageSpanAlignment.BASELINE** for the baseline alignment strategy to take effect.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Attributes of the span. |

#### TextBackgroundStyle11+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| color | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | Text background color. |
| radius | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | [BorderRadiuses](../../common-definitions/basic-types/document.md#borderradiuses9) | No | Yes | Rounded corner radius of the text background. |

#### Example

## Example 1: Setting the Text Style

This example demonstrates how to apply different text styles and configure click events for the **Span** component.

// xxx.ets
@Entry
@Component
struct SpanExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
      Text('Basic Usage').fontSize(9).fontColor(0xCCCCCC)
      Text() {
        Span('In Line')
        Span(' Component')
        Span(' !')
      }

      Text() {
        Span('This is the Span component').fontSize(12).textCase(TextCase.Normal)
          .decoration({ type: TextDecorationType.None, color: Color.Red })
          .fontFamily('HarmonyOS Sans')
      }.margin({ top: 12 })

      // Add a line under the text.
      Text('Text Decoration').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('I am Underline-WAVY-span')
          .decoration({ type: TextDecorationType.Underline, color: Color.Red, style: TextDecorationStyle.WAVY })
          .fontSize(12)
      }

      Text() {
        Span('I am LineThrough-DOTTED-span')
          .decoration({ type: TextDecorationType.LineThrough, color: Color.Red, style: TextDecorationStyle.DOTTED })
          .fontSize(12)
      }

      Text() {
        Span('I am Overline-DASHED-span')
          .decoration({ type: TextDecorationType.Overline, color: Color.Red, style: TextDecorationStyle.DASHED })
          .fontSize(12)
      }

      // Set the letter spacing.
      Text('LetterSpacing').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('span letter spacing')
          .letterSpacing(0)
          .fontSize(12)
      }

      Text() {
        Span('span letter spacing')
          .letterSpacing(-2)
          .fontSize(12)
      }

      Text() {
        Span('span letter spacing')
          .letterSpacing(3)
          .fontSize(12)
      }

      // Set the text case.
      Text('Text Case').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('I am Lower-span').fontSize(12)
          .textCase(TextCase.LowerCase)
          .decoration({ type: TextDecorationType.None })
      }

      Text() {
        Span('I am Upper-span').fontSize(12)
          .textCase(TextCase.UpperCase)
          .decoration({ type: TextDecorationType.None })
      }

      // Set the text font style.
      Text('FontStyle').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('I am FontStyle-Normal').fontSize(12)
          .fontStyle(FontStyle.Normal)
      }

      Text() {
        Span('I am FontStyle-Italic').fontSize(12)
          .fontStyle(FontStyle.Italic)
      }

      // Set the text font weight.
      Text('FontWeight').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('I am FontWeight-Lighter').fontSize(12)
          .fontWeight(FontWeight.Lighter)
      }

      Text() {
        Span('I am FontWeight-Bold').fontSize(12)
          .fontWeight(FontWeight.Bold)
      }

      // Set the text line height.
      Text('LineHeight').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('I am lineHeight default\\n').fontSize(12)
          .fontWeight(FontWeight.Lighter)
        Span('I am lineHeight 30').fontSize(12)
          .lineHeight(30)
      }
      .backgroundColor(Color.Gray)

      // Set the text style.
      Text('Font').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('span font 12 Bolder Italic')
          .font({
            size: 12,
            weight: FontWeight.Bolder,
            style: FontStyle.Italic,
            family: "HarmonyOS Sans"
          })
      }

      // Set the click event.
      Text('span click event').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('Span default ').fontSize(12)
        Span('Span click')
          .onClick((event) => {
            console.info("span onClick")
          })
      }
    }.width('100%').padding({ left: 35, right: 35, top: 35 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/kIKKq45xSu2J5NRfehpnhA/en-us_image_0000002537925626.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=798FBF7FBA4B0AA91DE28A52524344763C51FDCD09EC38B9A91C593D199C0DA0)

## Example 2: Setting the Text Shadow

In API version 11 and later versions, the [textShadow](#textshadow11) attribute is used to set the text shadow.

// xxx.ets
@Entry
@Component
struct SpanExample {
  @State textShadows: ShadowOptions | Array<ShadowOptions> = \[{
    radius: 10,
    color: Color.Red,
    offsetX: 10,
    offsetY: 0
  }, {
    radius: 10,
    color: Color.Orange,
    offsetX: 20,
    offsetY: 0
  },
    {
      radius: 10,
      color: Color.Yellow,
      offsetX: 30,
      offsetY: 0
    }, {
      radius: 10,
      color: Color.Green,
      offsetX: 40,
      offsetY: 0
    },
    {
      radius: 10,
      color: Color.Blue,
      offsetX: 100,
      offsetY: 0
    }\]

  build() {
    Column({ space: 8 }) {
      Text() {
        Span('123456789').fontSize(50).textShadow(this.textShadows).fontColor(Color.Pink)
      }

      Text() {
        Span('123456789') // span can inherit text shadow & font size from outer text
      }.fontSize(50).textShadow(this.textShadows).fontColor(Color.Pink)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/NpH4Phk2TV2jWSB96M8Dzw/en-us_image_0000002568685403.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AAE87C2C6DC885BABCF722A1BB213025CB6AC5EEB1E108B76D10BD93D7DA2599)

## Example 3: Setting the Background Style

This example demonstrates how to set the background style for text using the [textBackgroundStyle](#textbackgroundstyle11) attribute, available since API version 11.

// xxx.ets
@Component
@Entry
struct SpanExample {
  build() {
    Column() {
      Text() {
        Span('   Hello World !   ')
          .fontSize('20fp')
          .textBackgroundStyle({ color: "#7F007DFF", radius: "5vp" })
          .fontColor(Color.White)
      }
    }.width('100%').margin({ bottom: '5vp' }).alignItems(HorizontalAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/2me1Q6TdS5alDBC-yqLPOQ/en-us_image_0000002568765413.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61C7BA9B3D61C3DFDB568E218466F4503A7A3792ADE7F5B41A2FAD6B369D3A73)

## Example 4: Setting the Text Baseline Offset

In API version 12 and later versions, this example demonstrates how to set different baseline offsets for text through the [baselineOffset](#baselineoffset12) attribute.

// xxx.ets
import { LengthUnit, LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct SpanExample {
  build() {
    Row() {
      Column() {
        Text() {
          Span('SpanOne')
            .fontSize(10)
            .baselineOffset(new LengthMetrics(20, LengthUnit.VP))
          Span('SpanTwo')
            .fontSize(10)
            .baselineOffset(new LengthMetrics(0, LengthUnit.VP))
          // Replace $r('app.media.sky') with the image resource file you use.
          ImageSpan($r("app.media.sky"))
            .width('80px')
            .baselineOffset(new LengthMetrics(-20, LengthUnit.VP))
        }
        .backgroundColor('#7F007DFF')
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/kRPZGe5ETka7hnURXcB4SA/en-us_image_0000002537765688.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9DEAD55C1FC5871D0CFD3B112AB8AA2AAE135FC9D63A9D484DFB68400344DAA)
