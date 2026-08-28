# Outline Styling

You can set outline attributes for components. Drawn outside the component, the outline does not affect the component's layout or increase its size.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/9OQwts0BS0S3OwiADjdXOw/en-us_image_0000002568685149.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8117B80488263D5CB40A860B6C1DB3999484AAC7963B78DD8F5890C1148F6D12)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/QlMJr_VbTiyYlkqzqs5zHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44F943C88FEBB1703A4AB6F1C12E7484336D3BBD86CA9A24CCA4F22A67D2A95C)

The initial APIs of this module are supported since API version 11. Updates will be marked with a superscript to indicate their earliest API version.

#### outline

outline(value: OutlineOptions): T

Sets the outline attributes in one declaration.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [OutlineOptions](../../../common-definitions/basic-types/document.md#outlineoptions11) | Yes | Outline attributes. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### outline18+

outline(options: Optional<OutlineOptions>): T

Sets the outline attributes in one declaration. Compared with [outline](#outline), this API supports the **undefined** type for the **options** parameter.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[OutlineOptions](../../../common-definitions/basic-types/document.md#outlineoptions11)\> | Yes | 
Outline attributes.

If **options** is **undefined**, the component reverts to its original style with no outline.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### OutlineStyle

Enumerates outline styles.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| SOLID | 0 | Solid border. |
| DASHED | 1 | Dashed border. |
| DOTTED | 2 | Dotted border. The radius of a dot is half of **outlineWidth**. |

#### outlineStyle

outlineStyle(value: OutlineStyle | EdgeOutlineStyles): T

Sets the outline style. If this API is not used, a solid line is displayed by default.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [OutlineStyle](#outlinestyle) | [EdgeOutlineStyles](../../../common-definitions/basic-types/document.md#edgeoutlinestyles11) | Yes | Outline style. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### outlineStyle18+

outlineStyle(style: Optional<OutlineStyle | EdgeOutlineStyles>): T

Sets the outline style. If this API is not used, a solid line is displayed by default. Compared with [outlineStyle](#outlinestyle), this API supports the **undefined** type for the **style** parameter.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[OutlineStyle](#outlinestyle) | [EdgeOutlineStyles](../../../common-definitions/basic-types/document.md#edgeoutlinestyles11)\> | Yes | 
Outline style.

If **style** is **undefined**, the component reverts to its original style with no outline.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### outlineWidth

outlineWidth(value: Dimension | EdgeOutlineWidths): T

Sets the thickness of the outline. If this API is not used, there will be no change by default.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | [EdgeOutlineWidths](../../../common-definitions/basic-types/document.md#edgeoutlinewidths11) | Yes | Outline thickness. Percentage values are not supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### outlineWidth18+

outlineWidth(width: Optional<Dimension | EdgeOutlineWidths>): T

Sets the thickness of the outline. If this API is not used, there will be no change by default. Compared with [outlineWidth](#outlinewidth), this API supports the **undefined** type for the **width** parameter.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[Dimension](../../../common-definitions/basic-types/document.md#dimension10) | [EdgeOutlineWidths](../../../common-definitions/basic-types/document.md#edgeoutlinewidths11)\> | Yes | 
Outline thickness. Percentage values are not supported.

If **width** is **undefined**, the component reverts to its original style with no outline width.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### outlineColor

outlineColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T

Sets the outline color. If this API is not used, the default color black will be applied.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | [EdgeColors](../../../common-definitions/basic-types/document.md#edgecolors9) | [LocalizedEdgeColors](../../../common-definitions/basic-types/document.md#localizededgecolors12)12+ | Yes | Outline color. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### outlineColor18+

outlineColor(color: Optional<ResourceColor | EdgeColors | LocalizedEdgeColors>): T

Sets the outline color. If this API is not used, the default color black will be applied. Compared with [outlineColor](#outlinecolor), this API supports the **undefined** type for the **color** parameter.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | [EdgeColors](../../../common-definitions/basic-types/document.md#edgecolors9) | [LocalizedEdgeColors](../../../common-definitions/basic-types/document.md#localizededgecolors12)\> | Yes | 
Outline color.

If **color** is **undefined**, the component reverts to its original style with the outline color of **Color.Black**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### outlineRadius

outlineRadius(value: Dimension | OutlineRadiuses): T

Sets the radius of the outline corners. If this API is not used, there will be no change by default.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | [OutlineRadiuses](../../../common-definitions/basic-types/document.md#outlineradiuses11) | Yes | 
Radius of the outline corners. Percentage values are not supported.

Maximum effective value: Component width/2 + outlineWidth or component height/2 + outlineWidth

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### outlineRadius18+

outlineRadius(radius: Optional<Dimension | OutlineRadiuses>): T

Sets the radius of the outline corners. If this API is not used, there will be no change by default. Compared with [outlineRadius](#outlineradius), this API supports the **undefined** type for the **radius** parameter.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| radius | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[Dimension](../../../common-definitions/basic-types/document.md#dimension10) | [OutlineRadiuses](../../../common-definitions/basic-types/document.md#outlineradiuses11)\> | Yes | 
Radius of the outline corners. Percentage values are not supported.

Maximum effective value: Component width/2 + outlineWidth or component height/2 + outlineWidth

If **radius** is **undefined**, the component reverts to its original style with the outline corner radius of 0.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Example

## Example 1: Creating Outlines

This example demonstrates how to create component outlines using [outline](#outline).

// xxx.ets
@Entry
@Component
struct OutlineExample {
  build() {
    Column() {
      Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {
        // Dashed line
        Text('DASHED')
          .backgroundColor(Color.Pink)
          .outlineStyle(OutlineStyle.DASHED).outlineWidth(5).outlineColor(0xAFEEEE).outlineRadius(10)
          .width(120).height(120).textAlign(TextAlign.Center).fontSize(16)
        // Dotted line
        Text('DOTTED')
          .backgroundColor(Color.Pink)
          .outline({ width: 5, color: 0x317AF7, radius: 10, style: OutlineStyle.DOTTED })
          .width(120).height(120).textAlign(TextAlign.Center).fontSize(16)
      }.width('100%').height(150)

      Text('.outline')
        .backgroundColor(Color.Pink)
        .fontSize(50)
        .width(300)
        .height(300)
        .outline({
          width: { left: 3, right: 6, top: 10, bottom: 15 },
          color: { left: '#e3bbbb', right: Color.Blue, top: Color.Red, bottom: Color.Green },
          radius: { topLeft: 10, topRight: 20, bottomLeft: 40, bottomRight: 80 },
          style: {
            left: OutlineStyle.DOTTED,
            right: OutlineStyle.DOTTED,
            top: OutlineStyle.SOLID,
            bottom: OutlineStyle.DASHED
          }
        }).textAlign(TextAlign.Center)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/_hODxFDSSAmU5EmJ_sZLKw/en-us_image_0000002568765159.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64F2A8A85F143418DE04033391C9B4C64AAD2E958F21A6F46E37D8DB380ABE2D)

## Example 2: Using the LocalizedEdgeColors Type

This example demonstrates how to set the **color** attribute of the [outline](#outline) attribute to the [LocalizedEdgeColors](../../../common-definitions/basic-types/document.md#localizededgecolors12) type.

// xxx.ets

@Entry
@Component
struct OutlineExample {
  build() {
    Column() {
      Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {
        // Dashed line
        Text('DASHED')
          .backgroundColor(Color.Pink)
          .outlineStyle(OutlineStyle.DASHED).outlineWidth(5).outlineColor(0xAFEEEE).outlineRadius(10)
          .width(120).height(120).textAlign(TextAlign.Center).fontSize(16)
        // Dotted line
        Text('DOTTED')
          .backgroundColor(Color.Pink)
          .outline({ width: 5, color: 0x317AF7, radius: 10, style: OutlineStyle.DOTTED })
          .width(120).height(120).textAlign(TextAlign.Center).fontSize(16)
      }.width('100%').height(150)

      Text('.outline')
        .backgroundColor(Color.Pink)
        .fontSize(50)
        .width(300)
        .height(300)
        .outline({
          width: { left: 3, right: 6, top: 10, bottom: 15 },
          color: { start: '#e3bbbb', end: Color.Blue, top: Color.Red, bottom: Color.Green },
          radius: { topLeft: 10, topRight: 20, bottomLeft: 40, bottomRight: 80 },
          style: {
            left: OutlineStyle.DOTTED,
            right: OutlineStyle.DOTTED,
            top: OutlineStyle.SOLID,
            bottom: OutlineStyle.DASHED
          }
        }).textAlign(TextAlign.Center)
    }
  }
}

The following shows how the example is represented with left-to-right scripts.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/8j-p8yXaRquDxJYx9jpAvA/en-us_image_0000002537765434.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A78D2CF12A99F772B8D7A5EC1C32A11512674B29202036F4E4D41FC3355B63B1)

The following shows how the example is represented with right-to-left scripts.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/eO8qkFxkTA-S8azNiyxnKw/en-us_image_0000002537925374.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=417F37235B8279A2425F368D96A82066CDF203F513106727784C05E3BB51241A)
