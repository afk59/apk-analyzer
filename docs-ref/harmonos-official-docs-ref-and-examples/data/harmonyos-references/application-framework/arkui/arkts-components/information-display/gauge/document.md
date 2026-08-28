# Gauge

The **Gauge** component represents a gauge that displays data in a circular format.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/ZL08H7A0TkGLJIuFSOk6yQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF9BD82558576301CDFD3AEE67C73DCE568D1BA3CEDD6500B6A8C7E75892C549)

This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

This component can contain only one child component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/tPzHbxFrQwGneqkx6PyQoQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A4B23391AE9C9A9506EBBA79D6524E479B7FC2EBF3B08BE78DF66A9DA514435)

-   Supported child component types: built-in and custom components, including [if/else](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-ifelse) but excluding [ForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-foreach) and [LazyForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-lazyforeach).
    
-   You are advised to use the **Text** component to build the current value and auxiliary text.
    
-   If the width and height of the child component are in percentage, the reference range is the rectangle that has the outer ring as its inscribed circle.
    

#### APIs

Gauge(options: GaugeOptions)

Creates a gauge.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [GaugeOptions](#gaugeoptions18) | Yes | Settings of the gauge. |

#### GaugeOptions18+

Provides gauge options.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value8+ | number | No | No | 
Current value of the gauge, that is, the position to which the indicator points in the gauge. It is used as the initial value of the gauge when it is created.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**NOTE**

If the value is not within the range defined by the **min** and **max** parameters, the value of **min** is used.

 |
| min8+ | number | No | Yes | 

Minimum value of the current data segment.

Default value: **0**

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| max8+ | number | No | Yes | 

Maximum value of the current data segment.

Default value: **100**

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**NOTE**

If the value of **max** is less than that of **min**, the default values **0** and **100** are used.

The values of **max** and **min** can be negative numbers.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]value

value(value: number)

Sets the value of the gauge.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Value of the gauge. It can be dynamically changed.

Default value: **0**

 |

#### \[h2\]startAngle

startAngle(angle: number)

Sets the start angle of the gauge.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| angle | number | Yes | 
Start angle of the gauge. The 0 o'clock is defined as 0 degrees. Clockwise rotation represents positive angles, and counterclockwise rotation represents negative angles. Values exceeding 360 degrees are equivalent to the remainder after division by 360 degrees.

Default value: **0**

Drawing from the start position to the end position is performed only in the clockwise direction.

 |

#### \[h2\]endAngle

endAngle(angle: number)

Sets the end angle of the gauge. Ensure an appropriate difference between the start angle and end angle. If this difference is too small, the drawn chart may be abnormal. You are advised to use a monochrome ring to set the **value** attribute of the **Gauge**. You can also use **setTimeout** to delay value loading.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| angle | number | Yes | 
End angle of the gauge. The 0 o'clock is defined as 0 degrees. Clockwise rotation represents positive angles, and counterclockwise rotation represents negative angles. Values exceeding 360 degrees are equivalent to the remainder after division by 360 degrees.

Default value: **360**

Drawing from the start position to the end position is performed only in the clockwise direction.

 |

#### \[h2\]colors

colors(colors: ResourceColor | LinearGradient | Array<\[ResourceColor | LinearGradient, number\]>)

Sets the colors of the gauge.

Since API version 11, this API follows the following rules:

If the data type is [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor), the ring is of the monochrome type.

If the data type is [LinearGradient](../datapanel/document.md#lineargradient10), the ring is of the gradient type.

If the data type is Array, the ring is of the gradient type. The first parameter indicates the color value. If it is set to a non-color value, the color of 0xFFE84026 is used. The second parameter indicates the color weight. If it is set to a negative number or a non-numeric value, the color weight is 0.

A ring of the gradient type contains a maximum of nine color segments. If there are more than nine segments, the excess is not displayed.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colors | [ResourceColor11+](../../common-definitions/basic-types/document.md#resourcecolor) | [LinearGradient11+](../datapanel/document.md#lineargradient10) | Array<\[[ResourceColor10+](../../common-definitions/basic-types/document.md#resourcecolor) | [LinearGradient11+](../datapanel/document.md#lineargradient10) , number\]> | Yes | 
Colors of the gauge. You can set colors for individual segments.

Default value in API version 9: **Color.Black**

Default value in API version 11:

If no color is provided or the array is empty, the ring color will be a gradient consisting of the following colors: 0xFF64BB5C, 0xFFF7CE00, and 0xFFE84026.

If a color value is provided but invalid, the ring will be in the color of 0xFFE84026.

Colors with a weight of 0 are not displayed in the ring. If all weights are 0, the ring is not displayed.

 |

#### \[h2\]strokeWidth

strokeWidth(length: Length)

Sets the stroke width of the gauge.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Stroke width of the gauge.

Default value: **4**

Unit: vp

**NOTE**

A value less than or equal to 0 is handled as the default value.

If the value exceeds the maximum value, the radius of the gauge, the maximum value is used.

The value cannot be in percentage.

 |

#### \[h2\]description11+

description(value: CustomBuilder)

Sets the description of the gauge.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | Yes | 
Description.

**NOTE**

You need to customize the content – text or imagery recommended – in @Builder.

If the width and height of the custom content are in percentage, the reference range is a rectangle that is 44.4% of the diameter of the ring horizontally and 25.4% vertically (for images, it is 28.6% both horizontally and vertically), positioned 0 vp away from the bottom of the ring and centered horizontally.

If this parameter is set to null, no description is displayed.

If this parameter is not set, what's displayed is subject to the maximum and minimum value settings.

If either or both of the maximum and minimum values are set, they are displayed.

If neither maximum nor minimum values are set, no description is displayed.

The maximum and minimum values are displayed at the bottom of the ring and cannot be relocated. They may be blocked by the ring if the ring's start and end angles are not set properly.

 |

#### \[h2\]trackShadow11+

trackShadow(value: GaugeShadowOptions)

Sets the shadow style of the gauge.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [GaugeShadowOptions](#gaugeshadowoptions11) | Yes | 
Shadow effect. You can specify the blur radius, and the offset along the X and Y axes.

**NOTE**

The shadow color is the same as the ring color.

If this attribute is set to **null**, the shadow effect is disabled.

 |

#### \[h2\]indicator11+

indicator(value: GaugeIndicatorOptions)

Sets the indicator style of the gauge.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [GaugeIndicatorOptions](#gaugeindicatoroptions11) | Yes | 
Indicator style.

**NOTE**

If this attribute is set to **null**, no indicator is displayed.

 |

#### \[h2\]privacySensitive12+

privacySensitive(isPrivacySensitiveMode: Optional<boolean>)

Sets whether to enable privacy mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/S2W6d666SX6yAM4gv5keeg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=773C0CAD49F38BC4BCF3EDE8633C85682C780D64D29F340AC88D0F649369B196)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isPrivacySensitiveMode | Optional<boolean> | Yes | 
Whether to enable privacy mode. In privacy mode, the gauge indicator points to **0**, the maximum and minimum values are masked, and the scale range is displayed in gray or the background color. The value **true** means to enable privacy mode, and **false** means the opposite.

**NOTE**

If this parameter is set to **null**, privacy mode is disabled.

 |

#### \[h2\]contentModifier12+

contentModifier(modifier: ContentModifier<GaugeConfiguration>)

Creates a content modifier.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [ContentModifier<GaugeConfiguration>](#gaugeconfiguration12) | Yes | 
Content modifier to apply to the current component.

**modifier**: content modifier. You need a custom class to implement the **ContentModifier** API.

 |

#### GaugeShadowOptions11+

Inherits from [MultiShadowOptions](../information-display-apis/document.md#multishadowoptions) and has all attributes of **MultiShadowOptions**.

**Atomic service API**: This API can be used in atomic services since API version 12.

#### GaugeIndicatorOptions11+

Provides gauge indicator options.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| icon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 
Image path of the icon.

**NOTE**

If this parameter is not set, the default style is used, which is a triangle pointer.

Only icons in SVG format are supported. If icons in other formats are used, the default triangle style indicator is used.

 |
| space | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Distance between the indicator and the outer edge of the ring. The value cannot be in percentage.

Default value: **8**

Unit: vp

**NOTE**

For the default triangle style indicator, the distance is the amount of space between the triangle and the outer edge of the ring.

If this parameter is set to a value less than 0, the default value will be used.

If this parameter is set to a value greater than the ring radius, the default value will be used.

 |

#### GaugeConfiguration12+

You need a custom class to implement the **ContentModifier** API. Inherits from [CommonConfiguration](../../universal-attributes/modifiers-and-custom-property/content-modifier/document.md#commonconfigurationt).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | number | No | No | Current value. |
| min | number | No | No | Minimum value of the current data segment. |
| max | number | No | No | Maximum value of the current data segment. |

#### Example

## Example 1: Implementing a Multi-color Gauge

This example demonstrates how to implement a multi-color gauge using the [colors](#colors) attribute.

@Entry
@Component
struct Gauge1 {
  @Builder
  descriptionBuilder() {
    Text('Description')
      .maxFontSize('30sp')
      .minFontSize('10.0vp')
      .fontColor('#fffa2a2d')
      .fontWeight(FontWeight.Medium)
      .width('100%')
      .height('100%')
      .textAlign(TextAlign.Center)
  }

  build() {
    Column() {
      Gauge({ value: 50, min: 1, max: 100 }) {
        Column() {
          Text('50')
            .fontWeight(FontWeight.Medium)
            .width('62%')
            .fontColor('#ff182431')
            .maxFontSize('60.0vp')
            .minFontSize('30.0vp')
            .textAlign(TextAlign.Center)
            .margin({ top: '35%' })
            .textOverflow({ overflow: TextOverflow.Ellipsis })
            .maxLines(1)
          Text('Auxiliary text')
            .maxFontSize('16.0fp')
            .minFontSize('10.0vp')
            .fontColor($r('sys.color.ohos\_id\_color\_text\_secondary'))
            .fontWeight(FontWeight.Regular)
            .width('67.4%')
            .height('9.5%')
            .textAlign(TextAlign.Center)
        }.width('100%').height('100%')
      }
      .value(50)
      .startAngle(210)
      .endAngle(150)
      .colors(\[\[new LinearGradient(\[{ color: '#deb6fb', offset: 0 }, { color: '#ac49f5', offset: 1 }\]), 9\],
        \[new LinearGradient(\[{ color: '#bbb7fc', offset: 0 }, { color: '#564af7', offset: 1 }\]), 8\],
        \[new LinearGradient(\[{ color: '#f5b5c2', offset: 0 }, { color: '#e64566', offset: 1 }\]), 7\],
        \[new LinearGradient(\[{ color: '#f8c5a6', offset: 0 }, { color: '#ed6f21', offset: 1 }\]), 6\],
        \[new LinearGradient(\[{ color: '#fceb99', offset: 0 }, { color: '#f7ce00', offset: 1 }\]), 5\],
        \[new LinearGradient(\[{ color: '#dbefa5', offset: 0 }, { color: '#a5d61d', offset: 1 }\]), 4\],
        \[new LinearGradient(\[{ color: '#c1e4be', offset: 0 }, { color: '#64bb5c', offset: 1 }\]), 3\],
        \[new LinearGradient(\[{ color: '#c0ece5', offset: 0 }, { color: '#61cfbe', offset: 1 }\]), 2\],
        \[new LinearGradient(\[{ color: '#b5e0f4', offset: 0 }, { color: '#46b1e3', offset: 1 }\]), 1\]\])
      .width('80%')
      .height('80%')
      .strokeWidth(18)
      .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })
      .description(this.descriptionBuilder)
      .padding(18)
    }.margin({ top: 40 }).width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/3YXWXgPZQOSf39fQbg9kYg/en-us_image_0000002537925720.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7EB7B2CA1B1E18D018F9814145EC2102BB6D9865F76C973A8E5BDAAB55F4851D)

## Example 2: Implementing a Single-Color Gauge

This example demonstrates how to implement a single-color gauge using the [colors](#colors) attribute.

@Entry
@Component
struct Gauge2 {
  @Builder
  descriptionBuilderImage() {
    Image($r('sys.media.ohos\_ic\_public\_clock')).width(72).height(72)
  }

  build() {
    Column() {
      Gauge({ value: 50, min: 1, max: 100 }) {
        Column() {
          Text('50')
            .fontWeight(FontWeight.Medium)
            .width('62%')
            .fontColor('#ff182431')
            .maxFontSize('60.0vp')
            .minFontSize('30.0vp')
            .textAlign(TextAlign.Center)
            .margin({ top: '35%' })
            .textOverflow({ overflow: TextOverflow.Ellipsis })
            .maxLines(1)
        }.width('100%').height('100%')
      }
      .startAngle(210)
      .endAngle(150)
      .colors('#cca5d61d')
      .width('80%')
      .height('80%')
      .strokeWidth(18)
      .description(this.descriptionBuilderImage)
      .padding(18)
    }.margin({ top: 40 }).width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/XqCxe3exQq-26JI_ScMOxg/en-us_image_0000002568685497.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FCFA861AD4ECEC1C2E3CC16355EFEF8A45EF03F3616F96608F3A86657C91163D)

## Example 3: Configuring a Custom Description Area

This example illustrates how to configure a custom description area using the [description](#description11) attribute.

  @Entry
  @Component
  struct Gauge3 {
    @Builder
    descriptionBuilder() {
      Text('Description')
        .maxFontSize('30sp')
        .minFontSize('10.0vp')
        .fontColor('#fffa2a2d')
        .fontWeight(FontWeight.Medium)
        .width('100%')
        .height('100%')
        .textAlign(TextAlign.Center)
    }
  
    build() {
      Column() {
        Column() {
          Gauge({ value: 50, min: 1, max: 100 }) {
            Column() {
              Text('50')
                .fontWeight(FontWeight.Medium)
                .width('62%')
                .fontColor('#ff182431')
                .maxFontSize('60.0vp')
                .minFontSize('30.0vp')
                .textAlign(TextAlign.Center)
                .margin({ top: '35%' })
                .textOverflow({ overflow: TextOverflow.Ellipsis })
                .maxLines(1)
            }.width('100%').height('100%')
          }
          .startAngle(210)
          .endAngle(150)
          .colors(\[\[new LinearGradient(\[{ color: '#deb6fb', offset: 0 }, { color: '#ac49f5', offset: 1 }\]), 9\],
            \[new LinearGradient(\[{ color: '#bbb7fc', offset: 0 }, { color: '#564af7', offset: 1 }\]), 8\],
            \[new LinearGradient(\[{ color: '#f5b5c2', offset: 0 }, { color: '#e64566', offset: 1 }\]), 7\],
            \[new LinearGradient(\[{ color: '#f8c5a6', offset: 0 }, { color: '#ed6f21', offset: 1 }\]), 6\],
            \[new LinearGradient(\[{ color: '#fceb99', offset: 0 }, { color: '#f7ce00', offset: 1 }\]), 5\],
            \[new LinearGradient(\[{ color: '#dbefa5', offset: 0 }, { color: '#a5d61d', offset: 1 }\]), 4\],
            \[new LinearGradient(\[{ color: '#c1e4be', offset: 0 }, { color: '#64bb5c', offset: 1 }\]), 3\],
            \[new LinearGradient(\[{ color: '#c0ece5', offset: 0 }, { color: '#61cfbe', offset: 1 }\]), 2\],
            \[new LinearGradient(\[{ color: '#b5e0f4', offset: 0 }, { color: '#46b1e3', offset: 1 }\]), 1\]\])
          .width('80%')
          .height('80%')
          .strokeWidth(18)
          .description(this.descriptionBuilder)
          .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })
          .padding(18)
        }.margin({ top: 40 }).width('100%').height('100%')
      }
    }
  }

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/FMmsb8zgTx67cZ3HE61pIg/en-us_image_0000002568765507.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6085838CD54C13DFB221BEA9DB894EFF02083BA919FA76F334CB7C11C928B053)

## Example 4: Configuring the Auxiliary Area

This example demonstrates how to configure the auxiliary area by setting child components.

@Entry
@Component
struct Gauge4 {
  build() {
    Column() {
      Gauge({ value: 50, min: 1, max: 100 }) {
        Column() {
          Text('50')
            .maxFontSize('72.0vp')
            .minFontSize('10.0vp')
            .fontColor('#ff182431')
            .width('40%')
            .textAlign(TextAlign.Center)
            .margin({ top: '35%' })
            .textOverflow({ overflow: TextOverflow.Ellipsis })
            .maxLines(1)
          Text('Auxiliary text')
            .maxFontSize('30.0vp')
            .minFontSize('18.0vp')
            .fontWeight(FontWeight.Medium)
            .fontColor($r('sys.color.ohos\_id\_color\_text\_secondary'))
            .width('62%')
            .height('15.9%')
            .textAlign(TextAlign.Center)
        }.width('100%').height('100%')
      }
      .startAngle(210)
      .endAngle(150)
      .colors(\[\[new LinearGradient(\[{ color: '#deb6fb', offset: 0 }, { color: '#ac49f5', offset: 1 }\]), 9\],
        \[new LinearGradient(\[{ color: '#bbb7fc', offset: 0 }, { color: '#564af7', offset: 1 }\]), 8\],
        \[new LinearGradient(\[{ color: '#f5b5c2', offset: 0 }, { color: '#e64566', offset: 1 }\]), 7\],
        \[new LinearGradient(\[{ color: '#f8c5a6', offset: 0 }, { color: '#ed6f21', offset: 1 }\]), 6\],
        \[new LinearGradient(\[{ color: '#fceb99', offset: 0 }, { color: '#f7ce00', offset: 1 }\]), 5\],
        \[new LinearGradient(\[{ color: '#dbefa5', offset: 0 }, { color: '#a5d61d', offset: 1 }\]), 4\],
        \[new LinearGradient(\[{ color: '#c1e4be', offset: 0 }, { color: '#64bb5c', offset: 1 }\]), 3\],
        \[new LinearGradient(\[{ color: '#c0ece5', offset: 0 }, { color: '#61cfbe', offset: 1 }\]), 2\],
        \[new LinearGradient(\[{ color: '#b5e0f4', offset: 0 }, { color: '#46b1e3', offset: 1 }\]), 1\]\])
      .width('80%')
      .height('80%')
      .strokeWidth(18)
      .description(null)
      .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })
      .padding(18)
    }.margin({ top: 40 }).width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/TBh61w_TRxaCdF8jEuTX9Q/en-us_image_0000002537765782.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6AEA87BBFA779270F50327CB9EA095BF6A817680C4476B01BF646BE5638C7714)

## Example 5: Setting the Minimum and Maximum Values

This example shows how to set the minimum and maximum values of the gauge by configuring **min** and **max** in [GaugeOptions](#gaugeoptions18).

@Entry
@Component
struct Gauge5 {
  build() {
    Column() {
      Gauge({ value: 50, min: 1, max: 100 }) {
        Column() {
          Text('50')
            .maxFontSize('80sp')
            .minFontSize('60.0vp')
            .fontWeight(FontWeight.Medium)
            .fontColor('#ff182431')
            .width('40%')
            .height('30%')
            .textAlign(TextAlign.Center)
            .margin({ top: '22.2%' })
            .textOverflow({ overflow: TextOverflow.Ellipsis })
            .maxLines(1)
        }.width('100%').height('100%')
      }
      .startAngle(225)
      .endAngle(135)
      .colors(new LinearGradient(\[{ color: '#e84026', offset: 0 },
        { color: '#f7ce00', offset: 0.6 },
        { color: '#64bb5c', offset: 1 }\]))
      .width('80%')
      .height('80%')
      .strokeWidth(18)
      .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })
      .padding(18)
    }.margin({ top: 40 }).width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/Y0rR2pjdQhWEr2vI9yXupA/en-us_image_0000002537925722.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60483550AF1AAE0F571E4628725A2681C0AEF3F37B8D6AF4BC30C6984CCBCCA4)

## Example 6: Setting the Indicator

This example illustrates how to set the indicator of the gauge using the [indicator](#indicator11) attribute.

@Entry
@Component
struct Gauge6 {
  build() {
    Column() {
      Gauge({ value: 50, min: 1, max: 100 }) {
        Column() {
          Text('50')
            .maxFontSize('60sp')
            .minFontSize('30.0vp')
            .fontWeight(FontWeight.Medium)
            .fontColor('#ff182431')
            .width('62%')
            .textAlign(TextAlign.Center)
            .margin({ top: '35%' })
            .textOverflow({ overflow: TextOverflow.Ellipsis })
            .maxLines(1)
          Text('Auxiliary text')
            .maxFontSize('16sp')
            .minFontSize('10.0vp')
            .fontColor($r('sys.color.ohos\_id\_color\_text\_secondary'))
            .fontWeight(FontWeight.Regular)
            .width('67.4%')
            .height('9.5%')
            .textAlign(TextAlign.Center)
        }.width('100%').height('100%')
      }
      .startAngle(225)
      .endAngle(135)
      .colors(Color.Red)
      .width('80%')
      .height('80%')
      .indicator(null)
      .strokeWidth(18)
      .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })
      .padding(18)
    }.margin({ top: 40 }).width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/Xfc6wfKuTHuGl4ijcwChMQ/en-us_image_0000002568685499.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0A3A29D4F202A5A0B1138C15D242D1CCE3411214A4088677FDB39C6297ED4E8)

## Example 7: Setting the Start and End Angles

This example demonstrates how to set the start and end angles of the gauge using the [startAngle](#startangle) and [endAngle](#endangle) attributes.

@Entry
@Component
struct Gauge7 {
  build() {
    Column() {
      Gauge({ value: 50, min: 1, max: 100 }) {
        Column() {
          Text('50')
            .maxFontSize('60sp')
            .minFontSize('30.0vp')
            .fontWeight(FontWeight.Medium)
            .fontColor('#ff182431')
            .width('62%')
            .textAlign(TextAlign.Center)
            .margin({ top: '35%' })
            .textOverflow({ overflow: TextOverflow.Ellipsis })
            .maxLines(1)
        }.width('100%').height('100%')
      }
      .startAngle(225)
      .endAngle(135)
      .colors(Color.Red)
      .width('80%')
      .height('80%')
      .indicator(null)
      .strokeWidth(18)
      .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })
      .padding(18)
    }.margin({ top: 40 }).width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/mwJ47_x3SuSFTCYtXa278g/en-us_image_0000002568765509.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CA4A6E5972E9C75783365E3E9DFBBAF49601922C13BC1D31B3D8FF7BADE21A04)

## Example 8: Setting the Custom Content Area

This example shows how to customize the content area of the gauge using the [contentModifier](#contentmodifier12) attribute.

// xxx.ets
// The example implements the customization of the gauge's content area using a Builder, utilizing a circular chart, buttons, and text boxes. When the increase button is clicked, the indicator will shift to the right; conversely, when the decrease button is clicked, the indicator will shift to the left.
@Builder
function buildGauge(config: GaugeConfiguration) {
  Column({ space: 30 }) {
    Row() {
      Text('\[ContentModifier\] value: ' + JSON.stringify((config.contentModifier as MyGaugeStyle).value) +
        ' min:' + JSON.stringify((config.contentModifier as MyGaugeStyle).min) +
        ' max:' + JSON.stringify((config.contentModifier as MyGaugeStyle).max))
        .fontSize(12)
    }

    Text('\[Config\] value: ' + config.value + ' min: ' + config.min + ' max: ' + config.max).fontSize(12)
    Gauge({
      value: config.value,
      min: config.min,
      max: config.max
    }).width('50%')
  }
  .width('100%')
  .padding(20)
  .margin({ top: 5 })
  .alignItems(HorizontalAlign.Center)
}

class MyGaugeStyle implements ContentModifier<GaugeConfiguration> {
  value: number = 0
  min: number = 0
  max: number = 0

  constructor(value: number, min: number, max: number) {
    this.value = value
    this.min = min
    this.max = max
  }

  applyContent(): WrappedBuilder<\[GaugeConfiguration\]> {
    return wrapBuilder(buildGauge)
  }
}

@Entry
@Component
struct refreshExample {
  @State gaugeValue: number = 20
  @State gaugeMin: number = 0
  @State gaugeMax: number = 100

  build() {
    Column({ space: 20 }) {
      Gauge({
        value: this.gaugeValue,
        min: this.gaugeMin,
        max: this.gaugeMax
      })
        .contentModifier(new MyGaugeStyle(30, 10, 100))

      Column({ space: 20 }) {
        Row({ space: 20 }) {
          Button('Increase').onClick(() => {
            if (this.gaugeValue < this.gaugeMax) {
              this.gaugeValue += 1
            }
          })
          Button('Decrease').onClick(() => {
            if (this.gaugeValue > this.gaugeMin) {
              this.gaugeValue -= 1
            }
          })
        }
      }.width('100%')
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/1B2pE8n5TTKOK4PI3Lf4nQ/en-us_image_0000002537765784.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=023DCFCB096074910DE9733BD82112DEFFB5D1173669905D540808763A1BE5B2)

## Example 9: Securing Sensitive Information

This example illustrates how to secure sensitive information using the [privacySensitive](#privacysensitive12) attribute. Note that the display requires widget framework support.

@Entry
@Component
struct GaugeExample {
  build() {
    Scroll() {
      Column({ space: 15 }) {
        Row() {
          Gauge({ value: 60, min: 20, max: 100 })
            .startAngle(225)
            .endAngle(135)
            .colors(Color.Red)
            .width('80%')
            .height('80%')
            .strokeWidth(18)
            .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })
            .padding(18)
            .privacySensitive(true)
        }
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/jAYRh3baS2qh7e5DzkhGFQ/en-us_image_0000002537925724.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26458EC2438BEF2FAB2227EAB4156A295E0DA5AC66257D5B4DAB23F5A9D0A1E0)

## Example 10: Implementing a Custom Indicator

This example demonstrates how to implement a custom indicator using [indicator](#indicator11). You can import an SVG image to replace the default indicator.

@Entry
@Component
struct Gauge2 {
  build() {
    Column() {
      Gauge({ value: 50, min: 1, max: 100 })
        // Replace $r('app.media.indicator') with the image resource file you use.
        .indicator({ space: 10, icon: $r('app.media.indicator') })
        .startAngle(210)
        .endAngle(150)
        .colors('#cca5d61d')
        .width('80%')
        .height('80%')
        .strokeWidth(18)
        .padding(18)
    }.margin({ top: 40 }).width('100%').height('100%')
  }
}

<svg width='200px' height='200px'>
    <path d='M 10,30 A 20,20 0,0,1 50,30 A 20,20 0,0,1 90,30 Q 90,60 50,90 Q 10,60 10,30 z'
          stroke='black' stroke-width='3' fill='white'>
    </path>
</svg>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/51MtExW_SBy_xmZLxDSAjQ/en-us_image_0000002568685501.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8E139FCF607433120AF3B6C129F0DA465F7FA9DA5A8B1D7EF514ACDCDD1A4CB4)
