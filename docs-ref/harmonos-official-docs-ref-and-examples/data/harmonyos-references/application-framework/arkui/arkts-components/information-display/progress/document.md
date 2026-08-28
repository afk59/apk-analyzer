# Progress

The **Progress** component represents a progress indicator that displays the progress of content loading or an operation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/_998EeoWTY2d516Z0Dk1ng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03B01B25DC7DA5F9D0815C9FC9AD5765B383C19AAF6076F3DD42D0844891D577)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Not supported

#### APIs

Progress(options: ProgressOptions)

Creates a progress indicator.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ProgressOptions](#progressoptions) | Yes | Options of the progress indicator, which vary by progress indicator type. |

#### ProgressOptions

Defines progress bar options.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | number | No | No | 
Current progress. Values less than 0 are adjusted to **0**, and values greater than the **total** value are capped at the **total** value.

Default value: **0**

Value range: \[0, total\]

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| total | number | No | Yes | 

Total progress. If this parameter is set to a value less than or equal to 0, the value **100** is used.

Default value: **100**

Value range: (0, 2147483647\].

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| type8+ | [ProgressType](#progresstype8) | No | Yes | 

Style of the progress indicator.

Default value: **ProgressType.Linear**

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

Note: Different types must correspond to different [style](#style8) attribute settings. For details about the mapping, see [ProgressStyleMap](#progressstylemap10).

 |
| style(deprecated) | [ProgressStyle](#progressstyle) | No | Yes | 

Style of the progress indicator.

This parameter is deprecated since API version 8. You are advised to use **type** instead.

Default value: **ProgressStyle.Linear**

 |

#### ProgressType8+

Enumerates progress indicator types.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Linear | 0 | Linear type. Since API version 9, when the height is greater than the width, the progress bar is displayed vertically. |
| Ring | 1 | Indeterminate ring type. The ring fills up as the progress increases. |
| Eclipse | 2 | Eclipse type, which visualizes the progress in a way similar to the moon waxing from new to full. |
| ScaleRing | 3 | Ring style with scales, which is similar to the clock scale style. Since API version 9, when the scale outer circle overlaps, the progress indicator automatically converts to a circular style without scale. |
| Capsule | 4 | Capsule type. At both ends, the progress indicator works in a same manner as the eclipse type. In the middle part of the capsule, the progress indicator works in a same manner as the linear type. When the height is greater than the width, the progress bar is displayed vertically. |

#### ProgressStyle

Enumerates progress indicator styles.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Linear | 0 | Linear style. |
| Ring8+ | 1 | The ring gradually displays until it is completely filled. |
| Eclipse | 2 | Eclipse style, which visualizes the progress in a way similar to the moon waxing from new to full. |
| ScaleRing8+ | 3 | Ring style with scales, which is similar to the clock scale style. |
| Capsule8+ | 4 | Capsule type. At both ends, the progress indicator works in a same manner as the eclipse type. In the middle part of the capsule, the progress indicator works in a same manner as the linear type. When the height is greater than the width, the progress bar is displayed vertically. |

#### ProgressStyleMap10+

Mapping table of progress bar types and styles.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type |
| :-- | :-- |
| ProgressType.Linear | [LinearStyleOptions10+](#linearstyleoptions10) | [ProgressStyleOptions](#progressstyleoptions8) |
| ProgressType.Ring | [RingStyleOptions10+](#ringstyleoptions10) | [ProgressStyleOptions](#progressstyleoptions8) |
| ProgressType.Eclipse | [EclipseStyleOptions10+](#eclipsestyleoptions10) | [ProgressStyleOptions](#progressstyleoptions8) |
| ProgressType.ScaleRing | [ScaleRingStyleOptions10+](#scaleringstyleoptions10) | [ProgressStyleOptions](#progressstyleoptions8) |
| ProgressType.Capsule | [CapsuleStyleOptions10+](#capsulestyleoptions10) | [ProgressStyleOptions](#progressstyleoptions8) |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/kecmcUfoRKSxMqT-3RIKCg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7756D1CCA0E42BA68790A15AAA6B1EA4A77F9E88CBD2343F76D0D53E2C0FAB8A)

This component overrides the universal attribute [backgroundColor](../../universal-attributes/basic-attributes/background/document.md#backgroundcolor). When applied directly to the **Progress** component, it sets the background color of the progress indicator itself. To set the background color for the entire **Progress** component area, apply **backgroundColor** to the outer container that wraps the **Progress** component.

#### \[h2\]value

value(value: number)

Current progress. Values less than 0 are adjusted to **0**, and values greater than the **total** value are capped at the **total** value. Invalid values do not take effect.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Current progress.

Default value: **0**

 |

#### \[h2\]color

color(value: ResourceColor | LinearGradient)

Sets the foreground color of the progress indicator.

In API version 10 and later versions, you can set gradient colors for the [LinearGradient](../datapanel/document.md#lineargradient10) style of the ring indicator. Avoid setting the opacity for the ring type. To set the opacity, you are advised to use [DataPanel](../datapanel/document.md) instead.

In API version 23 and later versions, setting gradient colors via [LinearGradient](../datapanel/document.md#lineargradient10) for the **Linear** and **Capsule** styles is supported. In API version 22 and earlier versions, setting gradient colors via **LinearGradient** for the **Linear** and **Capsule** styles will not render the custom colors; the system's default theme colors will be used instead.

**Widget capability**: This API can be used in ArkTS widgets since API version 9, except that **LinearGradient** is not supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | [LinearGradient](../datapanel/document.md#lineargradient10) | Yes | 
Foreground color of the progress indicator.

Default value:

\- Capsule:

API version 9 or earlier: **'#ff007dff'**

API version 10: **'#33006cde'**

API version 11 or later: **'#33007dff'**

\- Ring:

API version 9 or earlier: **'#ff007dff'**

API version 10 or later: start: **'#ff86c1ff'**, end: **'#ff254ff7'**

\- Other styles: **'#ff007dff'**

 |

#### \[h2\]style8+

style(value: ProgressStyleOptions | CapsuleStyleOptions | RingStyleOptions | LinearStyleOptions | ScaleRingStyleOptions | EclipseStyleOptions)

Sets the component style.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | 
[ProgressStyleOptions8+](#progressstyleoptions8) | [CapsuleStyleOptions10+](#capsulestyleoptions10) |

[RingStyleOptions10+](#ringstyleoptions10) | [LinearStyleOptions10+](#linearstyleoptions10) |

[ScaleRingStyleOptions10+](#scaleringstyleoptions10) | [EclipseStyleOptions10+](#eclipsestyleoptions10)

 | Yes | 

Component style.

\- **CapsuleStyleOptions**: capsule style.

\- **RingStyleOptions**: ring style.

\- **LinearStyleOptions**: linear style.

\- **ScaleRingStyleOptions**: determinate ring style.

\- **EclipseStyleOptions**: eclipse style.

\- **ProgressStyleOptions**: strokeWidth, scaleCount, and scaleWidth of the progress bar. This parameter is valid only for the progress bar that supports these style settings.

 |

#### \[h2\]contentModifier12+

contentModifier(modifier:ContentModifier<ProgressConfiguration>)

Creates a content modifier.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [ContentModifier<ProgressConfiguration>](#progressconfiguration12) | Yes | 
Content modifier to apply to the current component.

**modifier**: content modifier. You need a custom class to implement the **ContentModifier** API.

 |

#### \[h2\]privacySensitive12+

privacySensitive(isPrivacySensitiveMode: Optional<boolean>)

Sets whether to enable privacy-sensitive mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/KjuZUVolRsOGM3qPrCsuNw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B7D3289E9F21152B6300E2C1233C9E0E9FDF7DE8FBCE3BA63B1D3445B3EC971)

This API can be called in [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isPrivacySensitiveMode | [Optional<boolean>](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt) | Yes | 
Whether to enable privacy-sensitive mode, in which the progress indicator is cleared and text content is masked. **true**: Enable privacy-sensitive mode. **false**: Disable privacy-sensitive mode.

Default value: **false**.

**NOTE**

Setting this parameter to **null** indicates that no specific privacy sensitivity is applied.

 |

#### ProgressConfiguration12+

Provides progress indicator configuration. Inherits from [CommonConfiguration](../../universal-attributes/modifiers-and-custom-property/content-modifier/document.md#commonconfigurationt).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | number | No | No | 
Current progress. Values less than 0 are adjusted to **0**. Values greater than the value of **total** are capped at the value of **total**.

Default value: **0**

Value range: \[0, total\]

 |
| total | number | No | No | 

Total progress.

Value range: (0, 2147483647\].

**NOTE**

If the value of **total** is a negative number, it is treated as 100.

 |

#### CommonProgressStyleOptions10+

Provides common style configuration options for the progress indicator.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| enableSmoothEffect | boolean | No | Yes | 
Whether to enable the smooth effect. When this feature is enabled, the progress value transitions from the current value to the target value with a progress change animation displayed on the page. When this feature is disabled, the progress value jumps directly to the target value without any animation.

**true**: The smooth effect is enabled.

**false**: The smooth effect is disabled.

Default value: **true**.

 |

#### ScanEffectOptions10+

Defines the scan effect options.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| enableScanEffect | boolean | No | Yes | 
Whether to enable the scan effect. Only the progress bar of the [Linear, Ring, Capsule](#progresstype8) type is supported.

**true**: The scan effect is enabled.

**false**: The scan effect is disabled.

Default value: **false**

 |

#### ProgressStyleOptions8+

Defines the progress bar style options.

Inherits [CommonProgressStyleOptions](#commonprogressstyleoptions10).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| strokeWidth | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 
Stroke width of the progress indicator. Percentage values are not supported.

Default value: **4.0vp**

If the value is out of the range, the default value is used.

 |
| scaleCount | number | No | Yes | 

Number of divisions on the ring-style process indicator.

Default value: **120vp**

Value range: \[2, min(width, height)/scaleWidth/2/π\]. If the value is outside this range, the progress indicator is displayed in the indeterminate ring style. By default, the minimum width and height are 77 vp.

 |
| scaleWidth | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Width of the ring progress bar scale. The value cannot be set in percentage. If the scale width is greater than the progress bar width, the default width is used.

Default value: **2.0vp**

 |

#### CapsuleStyleOptions10+

Capsule style options.

Inherits from [ScanEffectOptions](#scaneffectoptions10) and [CommonProgressStyleOptions](#commonprogressstyleoptions10).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| borderColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 
Border color.

Default value:

API version 10: **'#33006cde'**

API version 11 or later: **'#33007dff'**

 |
| borderWidth | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Border width. It cannot be set in percentage.

Default value: **1vp**

 |
| content | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Text content, which can be customized.

The Resource type is supported since API version 20.

 |
| font | [Font](../../common-definitions/basic-types/document.md#font) | No | Yes | 

Text style.

Default value:

Font size (percentage values are not supported): **12fp**

Other text parameters are subject to the theme values of the [Text](../../text-and-input/text/document.md) component.

 |
| fontColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Font color.

Default value: **'#ff182431'**

 |
| showDefaultPercentage | boolean | No | Yes | 

Whether to display the percentage text. After this feature is enabled, the progress percentage is displayed on the progress bar. This property does not take effect when the **content** attribute is set.

**true**: The percentage text is displayed. **false**: The percentage text is not displayed.

Default value: **false**

 |
| borderRadius18+ | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | 

Corner radius. The value cannot be set in percentage.

Value range: \[0, height/2\]

Default value: height/2

If an invalid value is set, the default value is used.

 |

#### RingStyleOptions10+

Ring style option without scales.

Inherits from [ScanEffectOptions](#scaneffectoptions10) and [CommonProgressStyleOptions](#commonprogressstyleoptions10).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| strokeWidth | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 
Stroke width of the progress indicator. It cannot be set in percentage. When the width is greater than or equal to the radius, the width is changed to half of the radius by default.

Default value: **4.0vp**

 |
| shadow | boolean | No | Yes | 

Whether to enable the shadow effect.

**true**: Enable the shadow effect. **false**: Disable the shadow effect.

Default value: **false**

 |
| status | [ProgressStatus10+](#progressstatus10) | No | Yes | 

// Set the progress state. When this parameter is set to ProgressStatus.LOADING, the update check animation is enabled. In this case, the progress value setting does not take effect. When this parameter is set from ProgressStatus.LOADING to ProgressStatus.PROGRESSING, the update check animation stops at the end.

Default value: ProgressStatus.PROGRESSING

 |

#### LinearStyleOptions10+

Linear style options.

Inherits from [ScanEffectOptions](#scaneffectoptions10) and [CommonProgressStyleOptions](#commonprogressstyleoptions10).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| strokeWidth | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 
Stroke width of the progress indicator. Percentage values are not supported.

Default value: **4.0vp**

 |
| strokeRadius | [PX](../../common-definitions/basic-types/document.md#px10) | [VP](../../common-definitions/basic-types/document.md#vp10) | [LPX](../../common-definitions/basic-types/document.md#lpx10) | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 

Sets the radius of the rounded corners of the linear progress bar.

Value range: \[0, strokeWidth/2\] Default value: **strokeWidth/2**

 |

#### ScaleRingStyleOptions10+

Ring style with scale options.

Inherits [CommonProgressStyleOptions](#commonprogressstyleoptions10).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| strokeWidth | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 
Stroke width of the progress indicator. Percentage values are not supported.

Default value: **4.0vp**

 |
| scaleCount | number | No | Yes | 

Number of divisions on the ring-style process indicator.

Default value: **120vp**

Value range: \[2, min(width, height)/scaleWidth/2/π\]. If the value is outside this range, the progress indicator is displayed in the indeterminate ring style. By default, the minimum width and height are 77 vp.

 |
| scaleWidth | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Width of the ring progress bar scale. The value cannot be set in percentage. If the scale width is greater than the progress bar width, the default width is used.

Default value: **2.0vp**

 |

#### EclipseStyleOptions10+

Options of the circle style. Eclipse style, which visualizes the progress in a way similar to the moon waxing from new to full.

Inherits [CommonProgressStyleOptions](#commonprogressstyleoptions10).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### ProgressStatus10+

Current status of the progress bar.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| LOADING | 'LOADING' | Loading. |
| PROGRESSING | 'PROGRESSING' | The progress is being updated. |

#### Events

The [universal events](../../universal-events/document.md) are supported.

#### Example

## Example 1: Setting Progress Indicator Types

This example demonstrates how to set the progress indicator type using the input parameter type of [ProgressOptions](#progressoptions).

// xxx.ets
@Entry
@Component
struct ProgressExample {
  build() {
    Column({ space: 15 }) {
      Text('Linear Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')
      Progress({ value: 10, type: ProgressType.Linear }).width(200)
      Progress({ value: 20, total: 150, type: ProgressType.Linear }).color(Color.Grey).value(50).width(200)

      Text('Eclipse Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')
      Row({ space: 40 }) {
        Progress({ value: 10, type: ProgressType.Eclipse }).width(100)
        Progress({ value: 20, total: 150, type: ProgressType.Eclipse }).color(Color.Grey).value(50).width(100)
      }

      Text('ScaleRing Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')
      Row({ space: 40 }) {
        Progress({ value: 10, type: ProgressType.ScaleRing }).width(100)
        Progress({ value: 20, total: 150, type: ProgressType.ScaleRing })
          .color(Color.Grey).value(50).width(100)
          .style({ strokeWidth: 15, scaleCount: 15, scaleWidth: 5 })
      }

      // scaleCount vs. scaleWidth
      Row({ space: 40 }) {
        Progress({ value: 20, total: 150, type: ProgressType.ScaleRing })
          .color(Color.Grey).value(50).width(100)
          .style({ strokeWidth: 20, scaleCount: 20, scaleWidth: 5 })
        Progress({ value: 20, total: 150, type: ProgressType.ScaleRing })
          .color(Color.Grey).value(50).width(100)
          .style({ strokeWidth: 20, scaleCount: 30, scaleWidth: 3 })
      }

      Text('Ring Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')
      Row({ space: 40 }) {
        Progress({ value: 10, type: ProgressType.Ring }).width(100)
        Progress({ value: 20, total: 150, type: ProgressType.Ring })
          .color(Color.Grey).value(50).width(100)
          .style({ strokeWidth: 20 })
      }

      Text('Capsule Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')
      Row({ space: 40 }) {
        Progress({ value: 10, type: ProgressType.Capsule }).width(100).height(50)
        Progress({ value: 20, total: 150, type: ProgressType.Capsule })
          .color(Color.Grey)
          .value(50)
          .width(100)
          .height(50)
      }
    }.width('100%').margin({ top: 30 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/ZjYbcgQiSGqECJj-qSeDcA/en-us_image_0000002537765788.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27B6639B953BC72D6AAADD96F10832C9080BE30B985C4C33FBC61E9EF44C3E51)

## Example 2: Setting Ring Progress Indicator Attributes

This example demonstrates how to set attributes of a ring progress indicator using the **strokeWidth** and **shadow** properties in the [style](#style8) API.

// xxx.ets
@Entry
@Component
struct ProgressExample {
  private gradientColor: LinearGradient = new LinearGradient(\[{ color: Color.Yellow, offset: 0.5 },
    { color: Color.Orange, offset: 1.0 }\])

  build() {
    Column({ space: 15 }) {
      Text('Gradient Color').fontSize(9).fontColor(0xCCCCCC).width('90%')
      Progress({ value: 70, total: 100, type: ProgressType.Ring })
        .width(100).style({ strokeWidth: 20 })
        .color(this.gradientColor)

      Text('Shadow').fontSize(9).fontColor(0xCCCCCC).width('90%')
      Progress({ value: 70, total: 100, type: ProgressType.Ring })
        .width(120).color(Color.Orange)
        .style({ strokeWidth: 20, shadow: true })
    }.width('100%').padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/2g3u0SWUTLS4EXjw7ZXBLA/en-us_image_0000002537925728.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1097BE399021C46253760F9E584B54B834F04CFE6E87D3A068FA25C301946DCC)

## Example 3: Setting the Animation for the Ring Progress Indicator

This example demonstrates how to enable or disable animations for a ring progress indicator using the **status** and **enableScanEffect** properties in the [style](#style8) API.

// xxx.ets
@Entry
@Component
struct ProgressExample {
  build() {
    Column({ space: 15 }) {
      Text('Loading Effect').fontSize(9).fontColor(0xCCCCCC).width('90%')
      Progress({ value: 0, total: 100, type: ProgressType.Ring })
        .width(100).color(Color.Blue)
        .style({ strokeWidth: 20, status: ProgressStatus.LOADING })

      Text('Scan Effect').fontSize(9).fontColor(0xCCCCCC).width('90%')
      Progress({ value: 30, total: 100, type: ProgressType.Ring })
        .width(100).color(Color.Orange)
        .style({ strokeWidth: 20, enableScanEffect: true })
    }.width('100%').padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/uUeW6lbNQJqSWnbxmNy10Q/en-us_image_0000002568685505.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FBC913AFAF098DCBF908CE29ACFA2EF9DEB08EE7D4D1B238C2FBA0A94E3F124B)

## Example 4: Setting Capsule Progress Indicator Attributes

This example demonstrates how to set attributes for a capsule progress indicator using properties such as **borderColor**, **borderWidth**, **content**, **font**, **fontColor**, **enableScanEffect**, and **showDefaultPercentage** in the [style](#style8) API.

// xxx.ets
@Entry
@Component
struct ProgressExample {
  build() {
    Column({ space: 15 }) {
      Row({ space: 40 }) {
        Progress({ value: 100, total: 100, type: ProgressType.Capsule }).width(100).height(50)
          .style({
            borderColor: Color.Blue,
            borderWidth: 1,
            content: 'Installing...',
            font: { size: 13, style: FontStyle.Normal },
            fontColor: Color.Gray,
            enableScanEffect: false,
            showDefaultPercentage: false
          })
      }
    }.width('100%').padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/NFLFMKAITTOMbBBGwjVzLQ/en-us_image_0000002568765515.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9A77BF24B38FF0CDBD38FF867E8D887AA1841184EC13EFA972D87F01B686D9D)

## Example 5: Setting the Smooth Effect

This example demonstrates how to enable or disable the smooth effect for the progress animation using the **enableSmoothEffect** property in the [style](#style8) API.

// xxx.ets
@Entry
@Component
struct Index {
  @State value: number = 0;

  build() {
    Column({ space: 10 }) {
      Text('enableSmoothEffect: true')
        .fontSize(9)
        .fontColor(0xCCCCCC)
        .width('90%')
        .margin(5)
        .margin({ top: 20 })
      Progress({ value: this.value, total: 100, type: ProgressType.Linear })
        .style({ strokeWidth: 10, enableSmoothEffect: true })

      Text('enableSmoothEffect: false').fontSize(9).fontColor(0xCCCCCC).width('90%').margin(5)
      Progress({ value: this.value, total: 100, type: ProgressType.Linear })
        .style({ strokeWidth: 10, enableSmoothEffect: false })

      Button('value +10').onClick(() => {
        this.value += 10;
      })
        .width(75)
        .height(15)
        .fontSize(9)
    }
    .width('50%')
    .height('100%')
    .margin({ left: 20 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/tuvH5ta8Rz2H_rV6JTh-wQ/en-us_image_0000002537765790.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D3CF9127CD7B05B5086B950101FFB35B047DE2A943D980014092E9023FED55D6)

## Example 6: Setting the Custom Content Area

This example implements a custom progress indicator using the [contentModifier](#contentmodifier12) API. This progress indicator displays a star shape with a total progress value of **3**, and the current value can be incremented or decremented through buttons. The achieved progress is filled with a custom color.

// xxx.ets
class MyProgressModifier implements ContentModifier<ProgressConfiguration> {
  color: ResourceColor = Color.White;

  constructor(color: ResourceColor) {
    this.color = color;
  }

  applyContent(): WrappedBuilder<\[ProgressConfiguration\]> {
    return wrapBuilder(myProgress);
  }
}

@Builder
function myProgress(config: ProgressConfiguration) {

  Column({ space: 30 }) {
    Text('Current progress: ' + config.value + '/' + config.total).fontSize(20)
    Row() {
      Flex({ justifyContent: FlexAlign.SpaceBetween }) {
        Path()
          .width('30%')
          .height('30%')
          .commands('M108 0 L141 70 L218 78.3 L162 131 L175 205 L108 170 L41.2 205 L55 131 L1 78 L75 68 L108 0 Z')
          .fill(config.enabled && config.value >= 1 ? (config.contentModifier as MyProgressModifier).color :
          Color.White)
          .stroke(Color.Black)
          .strokeWidth(3)
        Path()
          .width('30%')
          .height('30%')
          .commands('M108 0 L141 70 L218 78.3 L162 131 L175 205 L108 170 L41.2 205 L55 131 L1 78 L75 68 L108 0 Z')
          .fill(config.enabled && config.value >= 2 ? (config.contentModifier as MyProgressModifier).color :
          Color.White)
          .stroke(Color.Black)
          .strokeWidth(3)
        Path()
          .width('30%')
          .height('30%')
          .commands('M108 0 L141 70 L218 78.3 L162 131 L175 205 L108 170 L41.2 205 L55 131 L1 78 L75 68 L108 0 Z')
          .fill(config.enabled && config.value >= 3 ? (config.contentModifier as MyProgressModifier).color :
          Color.White)
          .stroke(Color.Black)
          .strokeWidth(3)
      }.width('100%')
    }
  }.margin({ bottom: 100 })
}

@Entry
@Component
struct Index {
  @State currentValue: number = 0;
  modifier = new MyProgressModifier('rgb(39, 135, 217)');
  @State myModifier: (MyProgressModifier | undefined) = this.modifier;

  build() {
    Column() {
      Progress({ value: this.currentValue, total: 3, type: ProgressType.Ring }).contentModifier(this.modifier)
      Button('Progress++').onClick(() => {
        if (this.currentValue < 3) {
          this.currentValue += 1;
        }
      }).width('30%')
      Button('Progress--').onClick(() => {
        if (this.currentValue > 0) {
          this.currentValue -= 1;
        }
      }).width('30%').margin('10')
    }.width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/Sa-W8VesSCiVICpMqIN27Q/en-us_image_0000002537925730.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1B1A1BF5EF33F348AA80168FA5AB4B247473FAAAB3CB127D09595916B92537F)

## Example 7: Securing Sensitive Information

This example illustrates how to secure sensitive information using the [privacySensitive](#privacysensitive12) attribute. Note that the display requires widget framework support.

@Entry
@Component
struct ProgressExample {
  build() {
    Row() {
      Column({ space: 15 }) {
        Progress({ value: 33, total: 100, type: ProgressType.Capsule }).width(300).height(50)
          .color(Color.Blue)
          .style({
            borderWidth: 5,
            font: { size: 13, style: FontStyle.Normal },
            enableScanEffect: false,
            showDefaultPercentage: true
          })
          .privacySensitive(true)
        Progress({ value: 33, total: 100, type: ProgressType.Capsule }).width(300).height(50)
          .color(Color.Blue)
          .style({
            borderWidth: 5,
            content: 'Installing...',
            font: { size: 13, style: FontStyle.Normal },
            enableScanEffect: false,
          })
          .privacySensitive(true)
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/ILBCN7B_RbWYcgWO6S-kZQ/en-us_image_0000002568685507.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A32B2BB41A29CFA1FB9C0EA8B756A2D1C6F1AB3714B2012C4BF99372CC9260F6)

## Example 8: Setting Capsule Progress Indicator Border Radius

This example uses the input parameter **borderRadius** of [CapsuleStyleOptions](#capsulestyleoptions10) to set the rounded corner radius of the capsule progress indicator.

The **borderRadius** attribute is supported since API version 18.

import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct ProgressExample {
  build() {
    Column({ space: 15 }) {
      Text('Capsule Progress').fontSize(9).width('90%')
      Row({ space: 15 }) {
        Progress({ value: 30, total: 100, type: ProgressType.Capsule })
          .style({ content: 'Default radius', borderWidth: 5 })
          .width(100)
          .height(60)
      }

      Row({ space: 15 }) {
        Progress({ value: 30, total: 100, type: ProgressType.Capsule })
          .style({ content: 'Radius 20 vp', borderWidth: 5, borderRadius: LengthMetrics.vp(20) })
          .width(100)
          .height(60)
      }
    }
    .width('100%')
    .margin({ top: 30 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/jT11uYHsTJCPY1GKx7E9iA/en-us_image_0000002568765517.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E60EB286EBFBE3011614BC9F74FE67F62733C27CA9D7DCB661D0758E4F4C88AB)
