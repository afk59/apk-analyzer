# How do I use bindContextMenu for the Image component?

The **Image** component enables the long-press drag feature by default, which conflicts with display of the context menu of **bindContextMenu**. You need to explicitly set **draggable()** to **false** to disable dragging. The sample code is as follows:

@Entry
@Component
struct Index {
  @Builder
  menuBuilder() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('Test ContextMenu1')
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
      Column() {
        Image($r('app.media.icon'))
          .draggable(false)
          .width('100vp')
      }
      .bindContextMenu(this.menuBuilder, ResponseType.LongPress)
      .onDragStart(() => {
        // Close menu when dragging
        this.getUIContext().getContextMenuController().close()
      })

    }
    .width('100%')
    .height('100%')
  }
}

**Reference**

[Menu Control](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-menu), [Image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-image)
