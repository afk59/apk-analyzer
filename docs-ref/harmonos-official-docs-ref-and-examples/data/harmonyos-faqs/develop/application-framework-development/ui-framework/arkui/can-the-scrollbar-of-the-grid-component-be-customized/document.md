# Can the scrollbar of the Grid component be customized?

The default scrollbar of the **Grid** component does not support custom styles.

You can hide the default scrollbar and bind a **ScrollBar** component to implement a custom scrollbar. The sample code is as follows:

@Entry
@Component
struct Index {
  private scroller: Scroller = new Scroller()
  private arr: number\[\] = \[\];

  build() {
    Column() {
      Stack({ alignContent: Alignment.End }) {
        Grid(this.scroller) {
          ForEach(this.arr, (item: number) => {
            GridItem() {
              Text(item.toString())
                .width(100)
                .height(50)
                .backgroundColor('#3366CC')
                .borderRadius(15)
                .fontSize(16)
                .textAlign(TextAlign.Center)
            }
          })
        }
        .width('100%')
        .columnsTemplate("1fr 1fr 1fr")
        .columnsGap(5)
        .rowsGap(5)
        // Hide native scrollBar
        .scrollBar(BarState.Off)

        ScrollBar({ scroller: this.scroller, direction: ScrollBarDirection.Vertical, state: BarState.Auto }) {
          Text("A")
            .width(20)
            .height(50)
            .borderRadius(10)
            .backgroundColor('#C0C0C0')
        }
        .width(20)
        .backgroundColor('#ededed')
      }
    }
  }

  aboutToAppear() {
    for (let i = 0; i < 100; i++) {
      this.arr.push(i)
    }
  }
}

**Reference**

[Grid](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-grid), [ScrollBar](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-scrollbar)
