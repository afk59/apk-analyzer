# Class (ContextMenuController)

Provides the capability to control the closing of context menus.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/8zk0Fk91SJSt6AYPRmPu8Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062227Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CD5CC1386AF9289C10CA6727233AEB185414C922DBACCCAA544C2723F010342)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 12.
    
-   In the following API examples, you must first use [getContextMenuController()](../class-uicontext/document.md#getcontextmenucontroller12) in **UIContext** to obtain a **ContextMenuController** instance, and then call the APIs using the obtained instance.
    

#### close12+

close(): void

Closes this context menu.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

This example demonstrates how to trigger the **close()** API of **ContextMenuController** via a timer to close the menu automatically after a specified delay.

import { ContextMenuController } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  menu: ContextMenuController = this.getUIContext().getContextMenuController();

  @Builder MenuBuilder() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('Test ContextMenu1 Close')
      Divider().strokeWidth(2).margin(5).color(Color.Black)
      Button('Test ContextMenu2')
      Divider().strokeWidth(2).margin(5).color(Color.Black)
      Button('Test ContextMenu3')
    }
    .width(200)
    .height(160)
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button("Start Timer").onClick(()=>
      {
        setTimeout(() => {
          this.menu.close();
        }, 10000);
      })

      Column() {
        Text("Test ContextMenu close")
          .fontSize(20)
          .width('100%')
          .height(500)
          .backgroundColor(0xAFEEEE)
          .textAlign(TextAlign.Center)
      }
      .bindContextMenu(this.MenuBuilder, ResponseType.LongPress)
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/SZbQDYLKSaWJR-kH3yZEpw/en-us_image_0000002537765322.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062227Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C1314B9AD608D6ADC58E06D6A2F2A537E9E0EA40407492A9A3795EBCE5E221EF)
