# Border Image

You can draw an image around a component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/_AqBXMQ3TsSsbvMh_zcS5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3B9FDAF3EB36A25377F4F0D14540C828E66188C789F0AA0348708C3C99AACAD)

The APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.

#### borderImage

borderImage(value: BorderImageOption): T

Sets the border image of the component.

**Widget capability**: Since API version 9, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [BorderImageOption](#borderimageoption) | Yes | Border image or border gradient. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### BorderImageOption

**Widget capability**: Since API version 9, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| source | string | [Resource](../../../common-definitions/basic-types/document.md#resource) | [LinearGradient](#lineargradient) | No | Yes | 
Source or gradient color of the border image. When the type is string, this parameter sets the border image source. For details about how to reference image resources, see [Loading Image Resources](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-graphics-display#loading-image-resources) .

**NOTE**

The border image source applies only to container components, such as [Row](../../../rows-columns-and-stacking/row/document.md), [Column](../../../rows-columns-and-stacking/column/document.md), and [Flex](../../../rows-columns-and-stacking/flex/document.md).

 |
| slice | [Length](../../../common-definitions/basic-types/document.md#length) | [EdgeWidths](../../../common-definitions/basic-types/document.md#edgewidths9) | [LocalizedEdgeWidths](../../../common-definitions/basic-types/document.md#localizededgewidths12)12+ | No | Yes | 

Slice width and height of the upper left corner, upper right corner, lower left corner, and lower right corner of the border image.

Default value: **0**

**NOTE**

If this parameter is set to a negative value, the default value is used.

When this parameter is set to a value of the [Length](../../../common-definitions/basic-types/document.md#length) type, the value applies to the four corners in a unified manner.

When this parameter is set to a value of the [EdgeWidths](../../../common-definitions/basic-types/document.md#edgewidths9) type:

\- **Top**: slice height of the top of the image.

\- **Bottom**: slice height of the bottom of the image.

\- **Left**: slice width of the left of the image.

\- **Right**: slice width of the right of the image.

When the parameter type is [LocalizedEdgeWidths](../../../common-definitions/basic-types/document.md#localizededgewidths12)12+:

\- **Top**: slice height of the top of the image.

\- **Bottom**: slice height of the bottom of the image.

\- **Start**: slice width of the left of the image.

This parameter specifies the slice width of the right of the image for right-to-left scripts.

\- **End**: slice width of the right of the image.

This parameter specifies the slice width of the left of the image for right-to-left scripts.

 |
| width | [Length](../../../common-definitions/basic-types/document.md#length) | [EdgeWidths](../../../common-definitions/basic-types/document.md#edgewidths9) | [LocalizedEdgeWidths](../../../common-definitions/basic-types/document.md#localizededgewidths12)12+ | No | Yes | 

Width of the border image.

Default value: **0**

**NOTE**

If this parameter is set to a negative value, the value **1** is used.

When this parameter is set to a value of the [Length](../../../common-definitions/basic-types/document.md#length) type, the value applies to the four corners in a unified manner. If this parameter is set to a negative value, the default value is used.

When this parameter is set to a value of the [EdgeWidths](../../../common-definitions/basic-types/document.md#edgewidths9) type:

\- **Top**: width of the top edge of the border image.

\- **Bottom**: width of the bottom edge of the border image.

\- **Left**: width of the left edge of the border image.

\- **Right**: width of the right edge of the border image.

When the parameter type is [LocalizedEdgeWidths](../../../common-definitions/basic-types/document.md#localizededgewidths12)12+:

\- **Top**: width of the top edge of the border image.

\- **Bottom**: width of the bottom edge of the border image.

\- **Start**: width of the left edge of the border image for left-to-right scripts;

width of the right edge of the border image for right-to-left scripts.

\- **End**: width of the right edge of the border image for left-to-right scripts;

width of the left edge of the border image for right-to-left scripts.

 |
| outset | [Length](../../../common-definitions/basic-types/document.md#length) | [EdgeWidths](../../../common-definitions/basic-types/document.md#edgewidths9) | [LocalizedEdgeWidths](../../../common-definitions/basic-types/document.md#localizededgewidths12)12+ | No | Yes | 

Amount by which the border image is extended beyond the border box.

Default value: **0**

**NOTE**

If this parameter is set to a negative value, the default value is used.

When this parameter is set to a value of the [Length](../../../common-definitions/basic-types/document.md#length) type, the value applies to the four corners in a unified manner.

When this parameter is set to a value of the [EdgeWidths](../../../common-definitions/basic-types/document.md#edgewidths9) type:

\- **Top**: amount by which the top edge of the border image is extended beyond the border box.

\- **Bottom**: amount by which the bottom edge of the border image is extended beyond the border box.

\- **Left**: amount by which the left edge of the border image is extended beyond the border box.

\- **Right**: amount by which the right edge of the border image is extended beyond the border box.

When the parameter type is [LocalizedEdgeWidths](../../../common-definitions/basic-types/document.md#localizededgewidths12)12+:

\- **Top**: amount by which the top edge of the border image is extended beyond the border box.

\- **Bottom**: amount by which the bottom edge of the border image is extended beyond the border box.

\- **Start**: amount by which the left edge of the border image is extended beyond the border box for left-to-right scripts;

amount by which the right edge of the border image is extended beyond the border box for right-to-left scripts.

\- **End**: amount by which the right edge of the border image is extended beyond the border box for left-to-right scripts;

amount by which the left edge of the border image is extended beyond the border box for right-to-left scripts.

 |
| repeat | [RepeatMode](#repeatmode) | No | Yes | 

Repeat mode of the source image's slices on the border.

Default value: **RepeatMode.Stretch**

 |
| fill | boolean | No | Yes | 

Whether to fill the center of the border image. **true**: Fill the center of the border image.

**false**: Do not fill the center of the border image.

Default value: **false**

 |

#### RepeatMode

Sets the repetition mode of the cut image on the border.

**Widget capability**: Since API version 9, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Repeat | 0 | Tiles the sliced image repeatedly along the border, clipping any overflow. |
| Stretch | 1 | Stretches the sliced image to fill the entire border. |
| Round | 2 | Repeats the sliced image in integer multiples. If exact tiling does not fit the border, the image is compressed to achieve full coverage. |
| Space | 3 | Repeats the sliced image in integer multiples. If exact tiling does not fit the border, the remaining gaps are filled with space. |

#### LinearGradient

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| angle | number | string | No | Yes | 
Start angle of the linear gradient. A positive value indicates a clockwise rotation from the origin, (0, 0).

Default value: **180**.

If the angle is specified with a string, only the 'deg', 'grad', 'rad', and 'turn' types are supported.

 |
| direction | [GradientDirection](../../../common-definitions/enums/document.md#gradientdirection) | No | Yes | 

Direction of the linear gradient. It does not take effect when **angle** is set.

Default value: **GradientDirection.Bottom**.

 |
| colors | Array<\[[ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor), number\]> | No | No | Array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped. |
| repeating | boolean | No | Yes | 

Whether the gradient colors can be repeatedly rendered.

Default value: **false**

**true**: yes

**false**: no

 |

#### Example

## Example 1: Setting a Gradient Border

This example demonstrates how to set a gradient border for a component using the [borderImage](#borderimage) API.

// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Text('This is gradient color.').textAlign(TextAlign.Center).height(50).width(200)
          .borderImage({
            source: {
              angle: 90,
              direction: GradientDirection.Left,
              colors: \[\[0xAEE1E1, 0.0\], \[0xD3E0DC, 0.3\], \[0xFCD1D1, 1.0\]\],
              repeating: false
            },
            slice: { top: 10, bottom: 10, left: 10, right: 10 },
            width: { top: "10px", bottom: "10px", left: "10px", right: "10px" },
            repeat: RepeatMode.Stretch,
            fill: false
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/1vUwkLcbQ6-p1QIcgKj2Fw/en-us_image_0000002537925356.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B810A8BB5CE946EAE09F925A6CF6B4184A8D8D8D75DA3A7414698E45066C0CCE)

## Example 2: Dynamically Adjusting Property Values

This example demonstrates how to dynamically adjust the properties of the [borderImage](#borderimage) API using the [<slider>](../../../../javascript-components/javascript-compatible-web-like-development-paradigm-arkui-full/basic-components/slider/document.md) component.

// xxx.ets
@Entry
@Component
struct BorderImage {
  @State WidthValue: number = 0
  @State SliceValue: number = 0
  @State OutSetValue: number = 0
  @State RepeatValue: RepeatMode\[\] = \[RepeatMode.Repeat, RepeatMode.Stretch, RepeatMode.Round, RepeatMode.Space\]
  @State SelectIndex: number = 0
  @State SelectText: string = 'Repeat'
  @State FillValue: boolean = false

  build() {
    Row() {
      Column({ space: 20 }) {
        Row() {
          Text('This is borderImage.').textAlign(TextAlign.Center).fontSize(50)
        }
        .borderImage({
          source: $r('app.media.icon'),
          slice: this.SliceValue,
          width: this.WidthValue,
          outset: this.OutSetValue,
          repeat: this.RepeatValue\[this.SelectIndex\],
          fill: this.FillValue
        })

        Column() {
          Text(\`borderImageSlice = ${this.SliceValue}px\`)
          Slider({
            value: this.SliceValue,
            min: 0,
            max: 100,
            style: SliderStyle.OutSet
          })
            .onChange((value: number, mode: SliderChangeMode) => {
              this.SliceValue = value
            })
        }

        Column() {
          Text(\`borderImageWidth = ${this.WidthValue}px\`)
          Slider({
            value: this.WidthValue,
            min: 0,
            max: 100,
            style: SliderStyle.OutSet
          })
            .onChange((value: number, mode: SliderChangeMode) => {
              this.WidthValue = value
            })
        }

        Column() {
          Text(\`borderImageOutSet = ${this.OutSetValue}px\`)
          Slider({
            value: this.OutSetValue,
            min: 0,
            max: 100,
            style: SliderStyle.OutSet
          })
            .onChange((value: number, mode: SliderChangeMode) => {
              this.OutSetValue = value
            })
        }

        Row() {
          Text('borderImageRepeat: ')
          Select(\[{ value: 'Repeat' }, { value: 'Stretch' }, { value: 'Round' }, { value: 'Space' }\])
            .value(this.SelectText)
            .selected(this.SelectIndex)
            .onSelect((index: number, value?: string) => {
              this.SelectIndex = index
              this.SelectText = value as string
            })
        }

        Row() {
          Text(\`borderImageFill: ${this.FillValue} \`)
          Toggle({ type: ToggleType.Switch, isOn: this.FillValue })
            .onChange((isOn: boolean) => {
              this.FillValue = isOn
            })
        }

      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/NMzkqWnwRA2LVdzbrUDAlg/en-us_image_0000002568685133.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5422C2D1BFC7619CF0DE81D32887B37113CA5B4BF57B52285C4C2BED3C674A52)

## Example 3: Using LocalizedEdgeWidths Type Values

This example demonstrates how to use the [LocalizedEdgeWidths](../../../common-definitions/basic-types/document.md#localizededgewidths12) type for the **slice**, **width**, and **outset** properties in the [borderImage](#borderimage) API.

// xxx.ets
import { LengthMetrics } from '@kit.ArkUI'

@Entry
@Component
struct BorderImage {
  @State WidthStartValue: number = 0
  @State WidthEndValue: number = 0
  @State SliceStartValue: number = 0
  @State SliceEndValue: number = 0
  @State OutSetStartValue: number = 0
  @State OutSetEndValue: number = 0
  @State RepeatValue: RepeatMode\[\] = \[RepeatMode.Repeat, RepeatMode.Stretch, RepeatMode.Round, RepeatMode.Space\]
  @State SelectIndex: number = 0
  @State SelectText: string = 'Repeat'
  @State FillValue: boolean = false

  build() {
    Row() {
      Column({ space: 20 }) {
        Row() {
          Text('This is borderImage.').textAlign(TextAlign.Center).fontSize(50)
        }
        .borderImage({
          source: $r('app.media.startIcon'),
          slice: {
            top: LengthMetrics.px(10),
            bottom: LengthMetrics.px(10),
            start: LengthMetrics.px(this.SliceStartValue),
            end: LengthMetrics.px(this.SliceEndValue) },
          width: {
            top: LengthMetrics.px(10),
            bottom: LengthMetrics.px(10),
            start: LengthMetrics.px(this.WidthStartValue),
            end: LengthMetrics.px(this.WidthEndValue)
          },
          outset: {
            top: LengthMetrics.px(10),
            bottom: LengthMetrics.px(10),
            start: LengthMetrics.px(this.OutSetStartValue),
            end: LengthMetrics.px(this.OutSetEndValue)
          },
          repeat: this.RepeatValue\[this.SelectIndex\],
          fill: this.FillValue
        })

        Column() {
          Text(\`borderImageSliceStart = ${this.SliceStartValue}px\`)
          Slider({
            value: this.SliceStartValue,
            min: 0,
            max: 100,
            style: SliderStyle.OutSet
          })
            .onChange((value: number, mode: SliderChangeMode) => {
              this.SliceStartValue = value
            })
        }

        Column() {
          Text(\`borderImageEndSliceStart = ${this.SliceEndValue}px\`)
          Slider({
            value: this.SliceEndValue,
            min: 0,
            max: 100,
            style: SliderStyle.OutSet
          })
            .onChange((value: number, mode: SliderChangeMode) => {
              this.SliceEndValue = value
            })
        }

        Column() {
          Text(\`borderImageWidthStart = ${this.WidthStartValue}px\`)
          Slider({
            value: this.WidthStartValue,
            min: 0,
            max: 100,
            style: SliderStyle.OutSet
          })
            .onChange((value: number, mode: SliderChangeMode) => {
              this.WidthStartValue = value
            })
        }

        Column() {
          Text(\`borderImageWidthEnd = ${this.WidthEndValue}px\`)
          Slider({
            value: this.WidthEndValue,
            min: 0,
            max: 100,
            style: SliderStyle.OutSet
          })
            .onChange((value: number, mode: SliderChangeMode) => {
              this.WidthEndValue = value
            })
        }

        Column() {
          Text(\`borderImageOutSetStart = ${this.OutSetStartValue}px\`)
          Slider({
            value: this.OutSetStartValue,
            min: 0,
            max: 100,
            style: SliderStyle.OutSet
          })
            .onChange((value: number, mode: SliderChangeMode) => {
              this.OutSetStartValue = value
            })
        }

        Column() {
          Text(\`borderImageOutSetEnd = ${this.OutSetEndValue}px\`)
          Slider({
            value: this.OutSetEndValue,
            min: 0,
            max: 100,
            style: SliderStyle.OutSet
          })
            .onChange((value: number, mode: SliderChangeMode) => {
              this.OutSetEndValue = value
            })
        }

        Row() {
          Text('borderImageRepeat: ')
          Select(\[{ value: 'Repeat' }, { value: 'Stretch' }, { value: 'Round' }, { value: 'Space' }\])
            .value(this.SelectText)
            .selected(this.SelectIndex)
            .onSelect((index: number, value?: string) => {
              this.SelectIndex = index
              this.SelectText = value as string
            })
        }

        Row() {
          Text(\`borderImageFill: ${this.FillValue} \`)
          Toggle({ type: ToggleType.Switch, isOn: this.FillValue })
            .onChange((isOn: boolean) => {
              this.FillValue = isOn
            })
        }

      }
      .width('100%')
    }
    .height('100%')
  }
}

The following shows how the example is represented with scripts.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/bQBAyOQSSniita-_fRTXgA/en-us_image_0000002568765143.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=47460D123FC5C4E6B9902606EA0971CCB87DF1D0A0B6414C751021AB80320E94)
