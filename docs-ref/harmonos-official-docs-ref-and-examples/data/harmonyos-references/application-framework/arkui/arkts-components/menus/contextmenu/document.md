# ContextMenu

The menu bound to a component through [bindContextMenu](../../universal-attributes/dialog-box-control/menu-control/document.md#bindcontextmenu12) on a page can be closed as needed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/00RBhk_-QuK69pVYwqPR_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=482BE04831047B588635E95D71CD38118BE9C2EFD47A1747DE171AB2F8528739)

The initial APIs of this module are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### ContextMenu.close(deprecated)

static close()

Closes the menu bound to this component through [bindContextMenu](../../universal-attributes/dialog-box-control/menu-control/document.md#bindcontextmenu12) on a page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/dmXZ0V8eTmenzQFbEr3Kdw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64EA17F00C6AA6A500C64D273CF62EC910E78189A1BDC7A39C291B4DEE7222DC)

This API is deprecated since API version 18. You are advised to use [getContextMenuController](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcontextmenucontroller12) in [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [ContextMenuController](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-contextmenucontroller/document.md) instance and then use this instance to call the [close](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-contextmenucontroller/document.md#close12) API.

Since API version 12, you can use the [getContextMenuController](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcontextmenucontroller12) API in [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to specify the UI execution context.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### Example

This example demonstrates how to call the **ContextMenu.close** API to close a context menu that is bound to a component using **bindContextMenu**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/NIr3WahnSEefOdH-lGfJDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D87F1E19F083E4BAE140F8296E4A30396CB8FDE8A390A0D2CE6AE39002D4F822)

You are advised to use the [getContextMenuController](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcontextmenucontroller12) API in [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to specify the UI execution context.

// xxx.ets
@Entry
@Component
struct Index {
  @Builder MenuBuilder() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('ContextMenu1')
      Divider().strokeWidth(2).margin(5).color(Color.Black)
      Button('ContextMenu2')
      Divider().strokeWidth(2).margin(5).color(Color.Black)
      Button('ContextMenu3')
    }
    .width(200)
    .height(160)
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Column() {
        Text('Long press to show ContextMenu')
          .fontSize(20)
          .width('100%')
          .height(500)
          .backgroundColor(0xAFEEEE)
          .textAlign(TextAlign.Center)
      }
      .bindContextMenu(this.MenuBuilder, ResponseType.LongPress)
      .onDragStart(()=>{
        // Close the menu when the component is dragged.
        ContextMenu.close() // You are advised to use this.getUIContext().getContextMenuController().close() to obtain the UI context.
      })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/v4jj5fxVSOq-ckup8xtBHA/en-us_image_0000002537925834.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9EC3B6FB89C7C71562C81B764A7108D60D2E837D201F35493185E8A5AE58CBE8)
