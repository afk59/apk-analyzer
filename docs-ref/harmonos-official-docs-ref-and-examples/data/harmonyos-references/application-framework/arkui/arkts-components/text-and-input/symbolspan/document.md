# SymbolSpan

As a child component of the **Text** component, the **SymbolSpan** component is used to display small icons.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/0ZV-_jvcSnGR0RNqn8Lt1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A45DE971B0FE0959FA113DB532ED8A81F32CAD0E707F4F4DC3237FB05A4F39E5)

-   This component is supported since API version 11. Updates will be marked with a superscript to indicate their earliest API version.
    
-   This component can inherit attribute settings from its parent component **Text**. This means that, if an attribute is not set in this component, it takes the value of the attribute (if set) from its parent component.
    
-   The **SymbolSpan** component is not dimmed when dragged.
    

#### Child Components

Not supported

#### APIs

SymbolSpan(value: Resource)

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | Resource of the **SymbolSpan** component, for example, **$r('sys.symbol.ohos\_wifi')**. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/G82gW-ZtQAiRdtk9iEjgKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67BA43A77170EE23999C14243B78774055A858394E51C3C3BB897F90E1E5C7BF)

The resources referenced in **$r('sys.symbol.ohos\_wifi')** are preset in the system. The **SymbolSpan** component supports only the preset symbol resources. If unsupported resources are referenced, an exception occurs.

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported. Only the following attributes are supported.

#### \[h2\]fontColor

fontColor(value: Array<ResourceColor>)

Sets the color of the symbol span.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/XAFFD0goRxWw_X8OF4n_IA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07657B54BD1E5AE3EEE06CD15E11FEADBE51763FE88BABD4C20A13F84C436F56)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Array<[ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor)\> | Yes | 
Color of the symbol span.

Default value: depending on the rendering strategy

 |

#### \[h2\]fontSize

fontSize(value: number | string | Resource)

Sets the size of the symbol span. When using the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/AaQ1HeKoRWK6ZsFq_n-0IA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB00B4207CFAA52D8665B796B698FC5EA9E056107CC34E910921C9975537F489)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Size of the symbol span.

Default value: **16fp**

Unit: [fp](../../common-definitions/pixel-units/document.md)

 |

#### \[h2\]fontWeight

fontWeight(value: number | FontWeight | string)

Sets the weight of the symbol span. For the number type, the value ranges from 100 to 900, at an interval of 100. A larger value indicates a heavier font weight. The default value is **400**. For the string type, only strings of the number type are supported, for example, **"400"**, **"bold"**, **"bolder"**, **"lighter"**, **"regular"**, and **"medium"**, which correspond to the enumerated values in **FontWeight**.

The **sys.symbol.ohos\_lungs** icon does not support font weight setting.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/4xUhWQnRRcipxXnS9Sauvw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DBCAD335D7AD031D7A3977774AB62FEE196E01E86AED8F24EEAE01EEDC77A1DA)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | [FontWeight](../../common-definitions/enums/document.md#fontweight) | string | Yes | 
Weight of the symbol span.

Default value: **FontWeight.Normal**

 |

#### \[h2\]renderingStrategy

renderingStrategy(value: SymbolRenderingStrategy)

Sets the rendering strategy of the symbol span.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/baoi7dAAQ1aKESj3lf36mg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B55A8287099908DD295EC2EF68844EE5BEB6F00899F762D429BF52FF23CEC037)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [SymbolRenderingStrategy](../symbolglyph/document.md#symbolrenderingstrategy11) | Yes | 
Rendering strategy of the symbol span.

Default value: **SymbolRenderingStrategy.SINGLE**

 |

The figure below shows the effects of different rendering strategies.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/Wz5dNlmYREKln6gbwO4IWQ/en-us_image_0000002568685409.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB669FE6C58E37EA00EF34588046A861A4AA83B0A28A546BFB74452E73EB1891)

#### \[h2\]effectStrategy

effectStrategy(value: SymbolEffectStrategy)

Sets the symbol effect of the symbol span.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/83Q_X8YyTiuw0qDeHVZokg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E127E345A8B12806DD5C9DCEE7F88CF925C189AF1F661232A102AAB001A1970A)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [SymbolEffectStrategy](../symbolglyph/document.md#symboleffectstrategy11) | Yes | 
Symbol effect of the symbol span.

Default value: **SymbolEffectStrategy.NONE**

 |

#### \[h2\]attributeModifier12+

attributeModifier(modifier: AttributeModifier<SymbolSpanAttribute>)

Creates an attribute modifier.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [AttributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifiert)<SymbolSpanAttribute> | Yes | Modifier for dynamically setting attributes on the current component. |

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

## Example 1: Setting Rendering and Animation Strategies

This example demonstrates different rendering and effect strategies using [renderingStrategy](#renderingstrategy) and [effectStrategy](#effectstrategy), available since API version 11.

// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      Row() {
        Column() {
          Text("Light")
          Text() {
            SymbolSpan($r('sys.symbol.ohos\_trash'))
              .fontWeight(FontWeight.Lighter)
              .fontSize(96)
          }
        }

        Column() {
          Text("Normal")
          Text() {
            SymbolSpan($r('sys.symbol.ohos\_trash'))
              .fontWeight(FontWeight.Normal)
              .fontSize(96)
          }
        }

        Column() {
          Text("Bold")
          Text() {
            SymbolSpan($r('sys.symbol.ohos\_trash'))
              .fontWeight(FontWeight.Bold)
              .fontSize(96)
          }
        }
      }

      Row() {
        Column() {
          Text("Monochrome")
          Text() {
            SymbolSpan($r('sys.symbol.ohos\_folder\_badge\_plus'))
              .fontSize(96)
              .renderingStrategy(SymbolRenderingStrategy.SINGLE)
              .fontColor(\[Color.Black, Color.Green, Color.White\])
          }
        }

        Column() {
          Text("Multicolor")
          Text() {
            SymbolSpan($r('sys.symbol.ohos\_folder\_badge\_plus'))
              .fontSize(96)
              .renderingStrategy(SymbolRenderingStrategy.MULTIPLE\_COLOR)
              .fontColor(\[Color.Black, Color.Green, Color.White\])
          }
        }

        Column() {
          Text("Multilayer")
          Text() {
            SymbolSpan($r('sys.symbol.ohos\_folder\_badge\_plus'))
              .fontSize(96)
              .renderingStrategy(SymbolRenderingStrategy.MULTIPLE\_OPACITY)
              .fontColor(\[Color.Black, Color.Green, Color.White\])
          }
        }
      }

      Row() {
        Column() {
          Text("No effect")
          Text() {
            SymbolSpan($r('sys.symbol.ohos\_wifi'))
              .fontSize(96)
              .effectStrategy(SymbolEffectStrategy.NONE)
          }
        }

        Column() {
          Text("Overall scale effect")
          Text() {
            SymbolSpan($r('sys.symbol.ohos\_wifi'))
              .fontSize(96)
              .effectStrategy(SymbolEffectStrategy.SCALE)
          }
        }

        Column() {
          Text("Hierarchical effect")
          Text() {
            SymbolSpan($r('sys.symbol.ohos\_wifi'))
              .fontSize(96)
              .effectStrategy(SymbolEffectStrategy.HIERARCHICAL)
          }
        }
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/R-o4z06MSfufYuY_mDtzHw/en-us_image_0000002568765419.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C0F6367A9CA1DBDFB73D59DF2986986D04ABCB2AEBFB302746FEA9B949273EA)

## Example 2: Configuring Dynamic Attributes

This example demonstrates how to create icons of a specified style using the [attributeModifier](#attributemodifier12) attribute, available since API version 12.

import { SymbolSpanModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State modifier: SymbolSpanModifier =
    new SymbolSpanModifier($r("sys.symbol.ohos\_wifi")).fontColor(\[Color.Blue\]).fontSize(100);

  build() {
    Row() {
      Column() {
        Text() {
          SymbolSpan(undefined).attributeModifier(this.modifier)
        }
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/OA2X_PnrShycKayH0hCUPg/en-us_image_0000002537765694.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37705B9D29BEA237109D857B39E06C3C8AFEBBA1665BC801D692252A301DDBA4)
