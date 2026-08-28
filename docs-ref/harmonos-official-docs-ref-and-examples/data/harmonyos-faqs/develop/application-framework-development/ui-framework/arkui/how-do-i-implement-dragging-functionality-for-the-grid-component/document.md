# How do I implement dragging functionality for the Grid component?

1.  Set **editMode(true)** in the **Grid** component to enable edit mode, where the grid items can be dragged.
2.  In the **onItemDragStart** callback, set the image to be displayed during dragging.
3.  In the **onItemDrop** callback, obtain the initial position of the dragged item and the position to which the dragged item is dropped. In the **onItemDrop** callback, complete the array position exchange logic.

Refer to the sample code below.

@Component
export struct GridExample {
  @State numbers: string\[\] = \[\];
  scroller: Scroller = new Scroller();

  // Drag and drop process style
  @Builder
  pixelMapBuilder(text: string) {
    Column() {
      Text(text)
        .fontSize(16)
        .backgroundColor(0xF9CF93)
        .width(80)
        .height(80)
        .textAlign(TextAlign.Center)
    }
  }

  aboutToAppear() {
    for (let i = 1; i <= 15; i++) {
      this.numbers.push(i + '');
    }
  }

  // Swap array positions
  changeIndex(index1: number, index2: number) {
    let temp: string;
    temp = this.numbers\[index1\];
    this.numbers\[index1\] = this.numbers\[index2\];
    this.numbers\[index2\] = temp;
  }

  build() {
    Column({ space: 5 }) {
      Grid(this.scroller) {
        ForEach(this.numbers, (day: string) => {
          GridItem() {
            this.pixelMapBuilder(day)
          }
        })
      }
      .columnsTemplate('1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .width('90%')
      .backgroundColor(0xFAEEE0)
      .height(500)
      .editMode(true) // Set whether the Grid enters editing mode. When entering editing mode, you can drag and drop the GridItem inside the Grid component
      .onItemDragStart((event: ItemDragInfo, itemIndex: number) => { // Triggered when a grid item starts to be dragged.
        // Set the image displayed during the drag and drop process
        return this.pixelMapBuilder(this.numbers\[itemIndex\]);
      })
      .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number, isSuccess: boolean) => {
        // The component bound to this event can be used as a drag and drop release target. When the drag behavior stops within the scope of this component, a callback is triggered.
        // When isSuccess=false, it indicates that the drop is located outside the grid; When insertIndex>length, it indicates that an event of adding new elements has occurred
        if (!isSuccess || insertIndex >= this.numbers.length) {
          return;
        }
        this.changeIndex(itemIndex, insertIndex);
      })
    }
    .width('100%')
    .margin({ top: 5 })
  }
}

**Reference**

[Grid](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-grid)
