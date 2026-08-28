# Hover Effect

The hover effect is applied to a component in hover state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/V0H928IxQrC4SscFw0BEMQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06C49E1A656477B0C3696B849D9210AA422BDA6A9F0BC617511A2DFFB1C19A46)

The initial APIs of this module are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### hoverEffect

hoverEffect(value: HoverEffect): T

Sets the hover effect for the component. When no hover effect is specified, the component uses the default **HoverEffect.Auto** effect. For components with hover effects applied, the hover effect is hidden when the mouse hovers and presses down on the component, and restored when the mouse button is released.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [HoverEffect](../../../common-definitions/enums/document.md#hovereffect8) | Yes | Hover effect of the component. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Example

This example demonstrates how to set the hover effect for components using **hoverEffect**.

// xxx.ets
@Entry
@Component
struct HoverExample {
  @State isHoverVal: boolean = false

  build() {
    Column({ space: 5 }) {
      Column({ space: 5 }) {
        Text('Scale').fontSize(20).fontColor(Color.Gray).width('90%').position({ x: 0, y: 80 })
        Column()
          .width('80%')
          .height(200)
          .backgroundColor(Color.Gray)
          .position({ x: 40, y: 120 })
          .hoverEffect(HoverEffect.Scale)
          .onHover((isHover?: boolean) => {
            console.info(\`Scale isHover: ${isHover}\`)
            this.isHoverVal = isHover as boolean
          })

        Text('Board').fontSize(20).fontColor(Color.Gray).width('90%').position({ x: 0, y: 380 })
        Column()
          .width('80%')
          .height(200)
          .backgroundColor(Color.Yellow)
          .hoverEffect(HoverEffect.Highlight)
          .position({ x: 40, y: 420 })
          .onHover((isHover?: boolean) => {
            console.info(\`Highlight isHover: ${isHover}\`)
            this.isHoverVal = isHover as boolean
          })
      }
      .hoverEffect(HoverEffect.None)
      .width('100%')
      .height('100%')
      .border({ width: 1 })
      .onHover((isHover?: boolean) => {
        console.info('HoverEffect.None')
        this.isHoverVal = isHover as boolean
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/t8B-5-2lSnSlFmw5klz9SA/en-us_image_0000002568765179.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F3BAD95DE2CFAD881F1ACE265C87AC27B653BF041F443C37F49E0B875216F54)
