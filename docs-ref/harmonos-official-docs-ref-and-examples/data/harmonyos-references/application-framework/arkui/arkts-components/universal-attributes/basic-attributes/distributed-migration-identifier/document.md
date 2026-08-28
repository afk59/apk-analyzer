# Distributed Migration Identifier

The distributed migration identifier **restoreId** identifies a component in distributed migration scenarios. It can be used to restore the component to a specific state on a remote device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/J-Zy8Xf9RlmZbWEGbdS1AQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4A0BFFABD789B73A5BD9A287A3C46D670A42AF0E3C9D69971666C9519F261B5)

The initial APIs of this module are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### restoreId

restoreId(value: number): T

Sets the ID of the component used for device matching during hopping.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | ID of the component used for device matching during hopping. This ID must be unique within an application. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Components with Hopping Support

| Name | Initial API Version | Description |
| :-- | :-- | :-- |
| [List](../../../scroll-and-swipe/list/document.md) | 8 | The index of the top list item on the current device is migrated to the remote device. After the migration, the corresponding list item is pinned to the top on the remote device. |
| [Grid](../../../scroll-and-swipe/grid/document.md) | 9 | The index of the top grid item on the current device is migrated to the remote device. After the migration, the corresponding grid item is pinned to the top on the remote device. Note that the position of the scrollbar cannot be migrated. |
| [Scroll](../../../scroll-and-swipe/scroll/document.md) | 9 | The absolute scroll distance from the top edge is migrated. Be aware that layout differences between devices may affect hopping results. |
| [WaterFlow](../../../scroll-and-swipe/waterflow/document.md) | 11 | The index of the top **FlowItem** component on the current device is migrated to the remote device. After the migration, the corresponding **FlowItem** component is pinned to the top on the remote device. The offset (in vp) of the top water flow item relative to the **WaterFlow** component along the main axis is also migrated. |

#### Example

This example demonstrates how to use **restoreId** to set the ID of the **List** component for device matching during hopping.

// xxx.ets
@Entry
@Component
struct RestoreIdExample {
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\]
  build() {
    Column() {
      List({ space: 20 }) {
        ForEach(this.arr, (item:number) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(Color.Pink)
          }
        }, (item:number) => (item.toString()))
      }
      .restoreId(1)
    }
  }
}
