# DataPanel

The **DataPanel** component is used to display proportions in a chart.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/4UCT3IVKSmKENT_4wMkyfw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5231E911896A4BC9D5A5ED863F123DCDCE081B86BA3924E1AD5F1A8EE366BD90)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Not supported

#### APIs

DataPanel(options: DataPanelOptions)

Creates a data panel component.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [DataPanelOptions](#datapaneloptions) | Yes | Parameters of the data panel. |

#### DataPanelOptions

Defines data panel configuration options.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| values | number\[\] | No | No | Data value list. A maximum of nine values are supported. If more than nine values are set, only the first nine ones are used. A value less than 0 evaluates to the value **0**. |
| max | number | No | Yes | 
\- When set to a value greater than 0, this parameter indicates the maximum value in the **values** list.

\- When set to a value equal to or smaller than 0, this parameter indicates the sum of values in the **values** list, and the values are displayed proportionally based on their relative sizes.

Default value: **100**

 |
| type8+ | [DataPanelType](#datapaneltype8) | No | Yes | 

Type of the data panel (dynamic modification is not supported).

Default value: **DataPanelType.Circle**

 |

#### DataPanelType8+

Enumerates data panel types.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Line | 0 | Line data panel. |
| Circle | 4 | Circle data panel. |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]closeEffect

closeEffect(value: boolean)

Sets whether to disable the rotation and shadow effects for the component. When the [trackShadow](#trackshadow10) attribute is not configured, this attribute controls the shadow effect. If the shadow effect is enabled, the default shadow style is applied. When **trackShadow** is explicitly set, the **trackShadow** configuration takes precedence.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to disable the rotation and shadow effects for the component.

Default value: **false**. **true**: Disable the rotation and shadow effects. **false**: Enable the rotation and shadow effects.

 |

#### \[h2\]valueColors10+

valueColors(value: Array<ResourceColor | LinearGradient>)

Sets an array of data segment colors.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Array<[ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | [LinearGradient](#lineargradient10)\> | Yes | 
Array of data segment colors. A value of the **ResourceColor** type indicates a solid color, and a value of the **LinearGradient** type indicates a color gradient. The arrary defaults to gradient colors.

Default colors for the nine data segments: \[{ color: '#F7CE00', offset: 0 }, { color: '#F99B11', offset: 1 }\], \[{ color: '#F76223', offset: 0 }, { color: '#F2400A', offset: 1 }\], \[{ color: '#F772AC', offset: 0 }, { color: '#E65392', offset: 1 }\], \[{ color: '#A575EB', offset: 0 }, { color: '#A12DF7', offset: 1 }\], \[{ color: '#7B79F7', offset: 0 }, { color: '#4B48F7', offset: 1 }\], \[{ color: '#4B8AF3', offset: 0 }, { color: '#007DFF', offset: 1 }\], \[{ color: '#73C1E6', offset: 0 }, { color: '#4FB4E3', offset: 1 }\], \[{ color: '#A5D61D', offset: 0 }, { color: '#69D14F', offset: 1 }\], \[{ color: '#A2A2B0', offset: 0 }, { color: '#8E8E93', offset: 1 }\]

 |

#### \[h2\]trackBackgroundColor10+

trackBackgroundColor(value: ResourceColor)

Sets the background color.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Background color.

The value is in hexadecimal ARGB notation. The first two digits indicate opacity. Default value: **'#08182431'**

 |

#### \[h2\]strokeWidth10+

strokeWidth(value: Length)

Sets the stroke width of the border. This attribute does not take effect when the data panel type is **DataPanelType.Line**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Stroke width of the border.

Default value: **24**

Unit: vp

When string values are provided without explicit units, the default unit px will be applied. For example, '10' is equivalent to '10px'.

**NOTE**

If a value less than 0 is set, the default value is used.

If the value exceeds the radius of the ring, the thickness will automatically be adjusted to 12% of the ring's radius to prevent visual issues. Excessively large values may cause the ring to become invisible.

 |

#### \[h2\]trackShadow10+

trackShadow(value: DataPanelShadowOptions)

Sets the shadow style.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [DataPanelShadowOptions](#datapanelshadowoptions10) | Yes | 
Shadow style.

**NOTE**

If this parameter is set to **null**, the shadow effect is disabled.

 |

#### \[h2\]contentModifier12+

contentModifier(modifier: ContentModifier<DataPanelConfiguration>)

Creates a content modifier.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [ContentModifier](../../universal-attributes/modifiers-and-custom-property/content-modifier/document.md#contentmodifiert)[<DataPanelConfiguration>](#datapanelconfiguration12) | Yes | 
Content modifier to apply to the current component.

**modifier**: content modifier. You need a custom class to implement the **ContentModifier** API.

 |

#### DataPanelShadowOptions10+

Inherits from [MultiShadowOptions](../information-display-apis/document.md#multishadowoptions) and has all properties of **MultiShadowOptions**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| colors | Array<[ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | [LinearGradient](#lineargradient10)\> | No | Yes | 
Array of shadow colors for data segments.

Default value: same as the value of **valueColors**

**NOTE**

If the number of the set shadow colors is less than that of the data segments, the number of the displayed shadow colors is the same as the former.

If the number of the set shadow colors is greater than that of the data segments, the number of the displayed shadow colors is the same as the latter.

 |

#### LinearGradient10+

#### \[h2\]constructor

constructor(colorStops: ColorStop\[\])

Describes the linear gradient.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colorStops | [ColorStop](#colorstop10)\[\] | Yes | Gradient colors and color stops. |

#### ColorStop10+

Describes the gradient color stop.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| color | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | No | Color value at the gradient color stop. |
| offset | [Length](../../common-definitions/basic-types/document.md#length) | No | No | 
Gradient color stop (proportion value between 0 and 1). A value less than 0 evaluates to the value **0**. A value greater than 1 evaluates to the value **1**.

**NOTE**

If the value is a string that represents a number, it will be converted to a number.

For example, **'10vp'** is converted to 10, and **'10%'** is converted to 0.1.

 |

#### DataPanelConfiguration12+

You need a custom class to implement the **ContentModifier** API. Inherits from [CommonConfiguration](../../universal-attributes/modifiers-and-custom-property/content-modifier/document.md#commonconfigurationt).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| values | number\[\] | No | No | 
Current values of the data panel.

The length of the array should be within the range of \[0, 9\].

**NOTE**

If the array length is greater than 9, the first nine items are used.

 |
| maxValue | number | No | No | 

Maximum value displayed in the data panel.

Default value: **100**

**NOTE**

If the value is less than or equal to 0, **maxValue** is set to the sum of all items in the **values** array and displayed proportionally.

 |

#### Example

## Example 1: Setting Data Panel Types

This example shows how to set the data panel type using the **type** attribute of [DataPanelOptions](#datapaneloptions).

// xxx.ets
@Entry
@Component
struct DataPanelExample {
  public valueArr: number\[\] = \[10, 10, 10, 10, 10, 10, 10, 10, 10\]

  build() {
    Column({ space: 5 }) {
      Row() {
        Stack() {
          // Single-segment circular data panel
          DataPanel({ values: \[30\], max: 100, type: DataPanelType.Circle }).width(168).height(168)
          Column() {
            Text('30').fontSize(35).fontColor('#182431')
            Text('1.0.0').fontSize(9.33).lineHeight(12.83).fontWeight(500).opacity(0.6)
          }

          Text('%')
            .fontSize(9.33)
            .lineHeight(12.83)
            .fontWeight(500)
            .opacity(0.6)
            .position({ x: 104.42, y: 78.17 })
        }.margin({ right: 44 })

        // Multi-segment circular data panel
        Stack() {
          DataPanel({ values: \[50, 12, 8, 5\], max: 100, type: DataPanelType.Circle }).width(168).height(168)
          Column() {
            Text('75').fontSize(35).fontColor('#182431')
            Text('Used: 98 GB/128 GB').fontSize(8.17).lineHeight(11.08).fontWeight(500).opacity(0.6)
          }

          Text('%')
            .fontSize(9.33)
            .lineHeight(12.83)
            .fontWeight(500)
            .opacity(0.6)
            .position({ x: 104.42, y: 78.17 })
        }
      }.margin({ bottom: 59 })

      // Linear data panel
      DataPanel({ values: this.valueArr, max: 100, type: DataPanelType.Line }).width(300).height(20)
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/kiFlLcPqRr-Pv-bweEylaw/en-us_image_0000002537925718.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B398EA7F45213AE8F4D3655F061BC893250B0B20EF5B2BFF2F5367E7C092BE46)

## Example 2: Setting Gradient Colors and Shadows

This example demonstrates how to set gradient colors and shadows using the [valueColors](#valuecolors10) and [trackShadow](#trackshadow10) for [LinearGradient](#lineargradient10).

// xxx.ets
@Entry
@Component
struct LinearGradientDataPanelExample {
  public values1: number\[\] = \[20, 20, 20, 20\]
  public color1: LinearGradient =
    new LinearGradient(\[{ color: '#65EEC9A3', offset: 0 }, { color: '#FFEF629F', offset: 1 }\])
  public color2: LinearGradient =
    new LinearGradient(\[{ color: '#FF67F9D4', offset: 0 }, { color: '#FFFF9554', offset: 1 }\])
  public colorShadow1: LinearGradient =
    new LinearGradient(\[{ color: '#65EEC9A3', offset: 0 }, { color: '#65EF629F', offset: 1 }\])
  public colorShadow2: LinearGradient =
    new LinearGradient(\[{ color: '#65e26709', offset: 0 }, { color: '#65efbd08', offset: 1 }\])
  public colorShadow3: LinearGradient =
    new LinearGradient(\[{ color: '#6572B513', offset: 0 }, { color: '#6508efa6', offset: 1 }\])
  public colorShadow4: LinearGradient =
    new LinearGradient(\[{ color: '#65ed08f5', offset: 0 }, { color: '#65ef0849', offset: 1 }\])
  @State shadowColorArray: Array<LinearGradient | ResourceColor> =
    \[this.colorShadow1, this.colorShadow2, this.colorShadow3, this.colorShadow4\]
  @State color3: string = '#00FF00'
  @State color4: string = '#20FF0000'
  @State colorArray: Array<LinearGradient | ResourceColor> = \[this.color1, this.color2, this.color3, this.color4\]
  @State bgColor: string = '#08182431'
  @State offsetX: number = 15
  @State offsetY: number = 15
  @State radius: number = 5

  build() {
    Column({ space: 5 }) {
      Text('LinearGradient')
        .fontSize(9)
        .fontColor(0xCCCCCC)
        .textAlign(TextAlign.Start)
        .width('100%')
        .margin({ top: 20, left: 20 })
      DataPanel({ values: this.values1, max: 100, type: DataPanelType.Circle })
        .width(300)
        .height(300)
        .valueColors(this.colorArray)
        .trackShadow({
          radius: this.radius,
          colors: this.shadowColorArray,
          offsetX: this.offsetX,
          offsetY: this.offsetY
        })
        .strokeWidth(30)
        .trackBackgroundColor(this.bgColor)
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/XiOdG-U4TTK6yUBb78Dm_g/en-us_image_0000002568685495.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D88B55FE5B022885AAEBD98FBA463FEA217EF4FF5D5A7A8159DC363C67EB1FA)

## Example 3: Disabling Animations and Shadows

This example demonstrates how to disable animations and shadows using the [closeEffect](#closeeffect) attribute.

// xxx.ets
@Entry
@Component
struct LinearGradientDataPanelExample {
  public values1: number\[\] = \[20, 20, 20, 20\]
  public color1: LinearGradient =
    new LinearGradient(\[{ color: '#65EEC9A3', offset: 0 }, { color: '#FFEF629F', offset: 1 }\])
  public color2: LinearGradient =
    new LinearGradient(\[{ color: '#FF67F9D4', offset: 0 }, { color: '#FFFF9554', offset: 1 }\])
  public colorShadow1: LinearGradient =
    new LinearGradient(\[{ color: '#65EEC9A3', offset: 0 }, { color: '#65EF629F', offset: 1 }\])
  public colorShadow2: LinearGradient =
    new LinearGradient(\[{ color: '#65e26709', offset: 0 }, { color: '#65efbd08', offset: 1 }\])
  public colorShadow3: LinearGradient =
    new LinearGradient(\[{ color: '#6572B513', offset: 0 }, { color: '#6508efa6', offset: 1 }\])
  public colorShadow4: LinearGradient =
    new LinearGradient(\[{ color: '#65ed08f5', offset: 0 }, { color: '#65ef0849', offset: 1 }\])
  @State shadowColorArray: Array<LinearGradient | ResourceColor> =
    \[this.colorShadow1, this.colorShadow2, this.colorShadow3, this.colorShadow4\]
  @State color3: string = '#00FF00'
  @State color4: string = '#20FF0000'
  @State colorArray: Array<LinearGradient | ResourceColor> = \[this.color1, this.color2, this.color3, this.color4\]
  @State bgColor: string = '#08182431'
  @State offsetX: number = 15
  @State offsetY: number = 15
  @State radius: number = 5

  build() {
    Column({ space: 5 }) {
      Text('LinearGradient')
        .fontSize(9)
        .fontColor(0xCCCCCC)
        .textAlign(TextAlign.Start)
        .width('100%')
        .margin({ top: 20, left: 20 })
      DataPanel({ values: this.values1, max: 100, type: DataPanelType.Circle })
        .width(300)
        .height(300)
        .valueColors(this.colorArray)
        .strokeWidth(30)
        .closeEffect(true)
        .trackBackgroundColor(this.bgColor)
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/9kK_92CkSjy74tJ0QuUyEQ/en-us_image_0000002568765505.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FEA23A0AC6D0581738F207E41D2B68E97900B05101C2E92BCCDAC6E9538B35AF)

## Example 4: Setting the Custom Content Area

This example shows how to customize the content area of the data panel using the [contentModifier](#contentmodifier12) API.

// xxx.ets
@Builder
function buildDataPanel(config: DataPanelConfiguration) {
  Column() {
    Column() {
      ForEach(config.values, (item: number, index: number) => {
        ChildItem({ item: item, index: index, max: config.maxValue })
      }, (item: number, index: number) => item.toString())
    }.padding(10)

    Column() {
      Line().width('100%').backgroundColor('#ff373737').margin({ bottom: 5 })
    }.padding({ left: 20, right: 20 })

    Row() {
      Text('Length=' + config.values.length + '    ').margin({ left: 10 }).align(Alignment.Start)
      Text('Max=' + config.maxValue).margin({ left: 10 }).align(Alignment.Start)
    }
  }
}

class DataPanelBuilder implements ContentModifier<DataPanelConfiguration> {
  constructor() {
  }

  applyContent(): WrappedBuilder<\[DataPanelConfiguration\]> {
    return wrapBuilder(buildDataPanel)
  }
}

@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('Data panel').margin({ top: 12 });
      Row() {
        DataPanel({ values: \[12.3, 21.1, 13.4, 35.2, 26.0, 32.0\], max: 140, type: DataPanelType.Circle })
          .width(400)
          .height(260)
          .constraintSize({ maxWidth: '100%' })
          .padding({ top: 10 })
          .contentModifier(new DataPanelBuilder())
      }.margin(15).backgroundColor('#fff5f5f5')
    }
  }
}

@Component
struct ChildItem {
  @Prop item: number;
  @Prop index: number;
  @Prop max: number;
  public color1: string = '#65ff00dd'
  public color2: string = '#6500ff99'
  public color3: string = '#65ffe600'
  public color4: string = '#6595ff00'
  public color5: string = '#65000dff'
  public color6: string = '#650099ff'
  public colorArray: Array<string> = \[this.color1, this.color2, this.color3, this.color4, this.color5, this.color6\]

  build() {
    RelativeContainer() {
      Row() {
        Rect()
          .height(25)
          .width(this.item \* 600 / this.max)
          .foregroundColor((this.index < 0 || this.index >= this.colorArray.length) ? this.colorArray\[0\] :
            this.colorArray\[this.index\])
          .radius(5)
          .align(Alignment.Start)
        Text(' ' + this.item)
          .fontSize(17)
      }
    }.height(28)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/ozp8e3bFTiCftB7RRKMj7w/en-us_image_0000002537765780.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=731C1488C46BDCF98FC56D3E8866EF874BA9DA8ECF382FFF198B77932DFFEF3E)
