# How do I set the gradient effect for both ends of the List component?

The **List** component does not support direct setting of gradient effects at both ends, but the effect can be achieved using Stack layout combined with the **LinearGradient** object. The code snippet is as follows:

@Entry
@Component
struct ListExample {
  @State arr: number\[\] = \[1, 2, 3, 4, 5, 6, 7, 8, 9\]
  private scroller: Scroller = new Scroller()

  build() {
    Stack() {
      List({ space: 10 }) {
        ForEach(this.arr, (item: string) => {
          ListItem() {
            Text("Hello World")
              .width(100)
              .height(64)
              .fontColor(Color.White)
              .backgroundColor(Color.Black)
              .textAlign(TextAlign.Center)
          }
        }, (item: string) => item)
      }
      .listDirection(Axis.Horizontal)
      .scrollBar(BarState.Off)
      .padding({ top: 20, bottom: 20 })
      .width("80%")
      .height("100%")

      Stack() {

      }
      .linearGradient({
        angle: 90,
        colors: \[\[0x000000, 0.0\], \['rgba(0,0,0,0)', 0.1\], \['rgba(0,0,0,0)', 0.9\], \[0x000000, 1.0\]\]
      })
      .width("80%")
      .height("100%")
      .hitTestBehavior(HitTestMode.None)
    }.height(100).width('100%').backgroundColor(Color.Black)
  }
}

**Reference**

[Gradient Color](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-gradient-color)
