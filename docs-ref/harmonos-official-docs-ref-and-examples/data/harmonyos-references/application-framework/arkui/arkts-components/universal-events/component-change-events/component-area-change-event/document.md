# Component Area Change Event

The area change event is triggered when the component's size, position, or any other attribute that may affect its display area changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/lnKKoIpRRb2FkgnHuTXokg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C1244953D362F02990922D942FDF37FDF34A835ABF3EB4025044EC534B6EBD5)

The initial APIs of this module are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

The **onAreaChange** callback is specific to the current component only. There is no strict execution order or guarantee of constraints for the **onAreaChange** callbacks on ancestor or descendant components.

#### onAreaChange

onAreaChange(event: (oldValue: Area, newValue: Area) => void): T

Triggered when the component area changes in size or position due to layout updates.

This event is not triggered for render attribute changes caused by re-rendering, such as changes to [translate](../../../universal-attributes/visual-effects/transformation/document.md#translate), [offset](../../../universal-attributes/layout-and-borders/location/document.md#offset), [markAnchor](../../../universal-attributes/layout-and-borders/location/document.md#markanchor), [scale](../../../universal-attributes/visual-effects/transformation/document.md#scale), or [transform](../../../universal-attributes/visual-effects/transformation/document.md#transform). In addition, if the component position is altered due to drawing changes, for example, through [bindSheet](../../../universal-attributes/transition/sheet-transition/document.md#bindsheet), this event is also not triggered.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/za8L2xVJS0u4MLEGPpjeXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3483FBE98B5E5808CF878857FE344422576E84828EB862300D269D56239E5C81)

When a component is bound to both the **onAreaChange** event and the [position](../../../universal-attributes/layout-and-borders/location/document.md#position) attribute, the **onAreaChange** event responds to changes in the **position** attribute of type [Position](../../../common-definitions/basic-types/document.md#position), but does not respond to changes in the **position** attribute of type [Edges](../../../common-definitions/basic-types/document.md#edges12) or [LocalizedEdges](../../../common-definitions/basic-types/document.md#localizededges12).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (oldValue: [Area](../../../common-definitions/basic-types/document.md#area8), newValue: [Area](../../../common-definitions/basic-types/document.md#area8)) => void | Yes | Position information of the target element. **oldValue** indicates the width and height of the target element as well as its coordinates relative to the parent element and the upper left corner of the page before the change. **newValue** indicates these dimensions and coordinates after the change. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Example

This example demonstrates how to set an area change event for a **Text** component. When the layout of the **Text** component changes, the **onAreaChange** event is triggered, allowing you to obtain relevant parameters.

// xxx.ets
@Entry
@Component
struct AreaExample {
  @State value: string = 'Text'
  @State sizeValue: string = ''

  build() {
    Column() {
      Text(this.value)
        .backgroundColor(Color.Green)
        .margin(30)
        .fontSize(20)
        .onClick(() => {
          this.value = this.value + 'Text'
        })
        .onAreaChange((oldValue: Area, newValue: Area) => {
          console.info(\`Ace: on area change, oldValue is ${JSON.stringify(oldValue)} value is ${JSON.stringify(newValue)}\`)
          this.sizeValue = JSON.stringify(newValue)
        })
      Text('new area is: \\n' + this.sizeValue).margin({ right: 30, left: 30 })
    }
    .width('100%').height('100%').margin({ top: 30 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/LpLqiBJbQh-3lu9lusVElA/en-us_image_0000002537925326.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=918F6078671E936E4D535A141A8217020C211B7C78BA37B219E0C78FA39CBA24)
