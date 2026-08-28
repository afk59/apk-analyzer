# Foreground Color

Sets the foreground color of the component. The foreground color affects the coloration of component content, contrasting with the background color. It influences text color and shape fill colors in drawing components.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/bIw_YM8SSRivCRKITuXhPA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4E28A97B0C401A878D0ACE930BE99A31AE8803B95960826C66FC10126FF3CD4)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### foregroundColor

foregroundColor(value: ResourceColor | ColoringStrategy): T

Sets the foreground color of the component. Components without explicit foreground color settings inherit from their parent components by default.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | [ColoringStrategy](../../../common-definitions/enums/document.md#coloringstrategy10) | Yes | Foreground color. The value can be a specific color or a coloring strategy. The [attribute animation](../../../animation/property-animation-animation/document.md) is not supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### foregroundColor18+

foregroundColor(color: Optional<ResourceColor | ColoringStrategy>): T

Sets the foreground color of the component. Components without explicit foreground color settings inherit from their parent components by default. Compared to [foregroundColor](#foregroundcolor), the **color** parameter supports the **undefined** type.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | [ColoringStrategy](../../../common-definitions/enums/document.md#coloringstrategy10)\> | Yes | 
Foreground color. The value can be a specific color or a coloring strategy. Property animations are not supported.

If the color value is **undefined**, the previous setting or the component's default value is retained. The specific behavior may vary across components. It is recommended that you use explicit color values or [ColoringStrategy](../../../common-definitions/enums/document.md#coloringstrategy10).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Example

## Example 1: Using Foreground Color Settings

This example demonstrates how to set the foreground color using **foregroundColor**.

// xxx.ets
@Entry
@Component
struct ForegroundColorExample {
  build() {
    Column({ space: 100 }) {
      // Draw a circle with a diameter of 150. The default fill color is black.
      Circle({ width: 150, height: 200 }).margin(20)
      // Draw a circle with a diameter of 150 and set the foreground color to orange.
      Circle({ width: 150, height: 200 }).foregroundColor(Color.Orange)
    }.width('100%').backgroundColor(Color.Gray)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/9prtnYowQM6WzKLLAH0GFg/en-us_image_0000002568685147.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C30A36D2077E52FE06A9A6557EEF4441EE63BCE1052A5B6A73E57BA7E495E03)

## Example 2: Setting the Foreground Color to Background Inverse

This example demonstrates how to set the foreground color to the inverse of the background color using [ColoringStrategy](../../../common-definitions/enums/document.md#coloringstrategy10)**.INVERT**.

// xxx.ets
@Entry
@Component
struct ColoringStrategyExample {
  build() {
    Column({ space: 100 }) {
      // Draw a circle with a diameter of 150. The default fill color is black.
      Circle({ width: 150, height: 200 })
      // Draw a circle with a diameter of 150 and set its foreground color to the inverse of the component background color.
      Circle({ width: 150, height: 200 })
        .backgroundColor(Color.Black)
        .foregroundColor(ColoringStrategy.INVERT)
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/AENHAxZGTEiWhxzS5MaHdg/en-us_image_0000002568765157.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=549671C71E2228948B77363C4A42670D7D88BFF6C9DB6E63B748DE3502833C20)

## Example 3: Implementing a Foreground Color Not Inherited from the Parent Component

This example compares the effects of setting both foreground and background colors on a component versus setting only the background color.

// xxx.ets
@Entry
@Component
struct ForegroundColorInherit {
  build() {
    Column() {
      Button('Foreground Color: Set to Orange').fontSize(20).foregroundColor(Color.Orange).backgroundColor(Color.Gray)
      Divider()
      Button('Foreground Color: Inherited from Parent Component When Not Set').fontSize(20).backgroundColor(Color.Gray)
    }.foregroundColor(Color.Pink)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/ccO8z6KmQHOiibGfZn9D2Q/en-us_image_0000002537765432.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C17B7AC56C1822F39B354AC479683804A4C9EB995D15F78AB2F4083B0CA7489)
