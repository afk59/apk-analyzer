# Can I set variables for the universal attribute width?

Yes. The following is an example:

@Entry
@Component
struct Page1 {
  @State message: string = 'Hello';
  @State widthNum: number = 300;

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .width(this.widthNum)
          .backgroundColor(Color.Blue)
      }
      .width('100%')
    }
    .height('100%')
  }
}

The following animation shows the display effects.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/vga8W8xfQySv2wPKY5RfiQ/en-us_image_0000002194158632.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062552Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7390A7913235995D288EE9F15884FA5AFD103CFA1C48CF6E211884414F85FB19 "Click to enlarge")
