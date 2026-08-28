# How do I implement a multi-column layout using the List component?

To implement a multi-column layout using the [List](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list) component, set its **lanes** attribute, which defines the number of columns along the cross axis. The sample code snippet is as follows:

// xxx.ets
@Entry
@Component
struct ListExample {
  @State arr: string\[\] = \['1', '2', '3', '4', '5', '6', '7', '8', '9'\];

  build() {
    Column() {
      List() {
        ForEach(this.arr, (item: string) => {
          ListItem() {
            Row() {
              Text(item)
                .fontColor(Color.Red)
                .fontSize(40)
            }
          }
          .width('100%')
          .border({
            width: 1,
            color: Color.Black,
            radius: 5
          })
        })
      }
      .lanes(3)
      .alignListItem(ListItemAlign.Center)
    }
    .padding({ top: 30 })
  }
}

The figure below shows the preview.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/BqbCv855S7uSlUpnh64pSg/en-us_image_0000002194158740.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062548Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB4D85AC850ED1E15F3074340B76A04D88477E5E274C19C6A30F5F9D5C97F18F "Click to enlarge")
