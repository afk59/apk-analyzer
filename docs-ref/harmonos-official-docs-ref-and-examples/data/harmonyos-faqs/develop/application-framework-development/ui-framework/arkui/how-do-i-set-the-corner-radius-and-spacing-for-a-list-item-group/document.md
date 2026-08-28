# How do I set the corner radius and spacing for a list item group?

Use **ListItemGroupStyle** of the [ListItemGroup](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-listitemgroup) component to set the corner radius, and use [space](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list#apis) of the **List** component to set the spacing. The code snippet is as follows:

// xxx.ets
@Entry
@Component
struct ListItemGroupExample {
  private timeTable: TimeTable\[\] = \[
    { projects: \['language'\] },
    { projects: \['mathematics', 'English'\] },
    { projects: \['physics', 'chemistry', 'biology'\] },
    { projects: \['the fine arts', 'music', 'sport'\] }
  \]

  build() {
    Column() {
      List({ space: 20 }) { // Set the spacing of the grouping list
        ForEach(this.timeTable, (item: TimeTable) => {
          ListItemGroup({ style: ListItemGroupStyle.CARD }) { // Set the rounded corners of the grouping list
            ForEach(item.projects, (project: string) => {
              ListItem() {
                Text(project)
                  .width("100%")
                  .height(100)
                  .fontSize(20)
                  .textAlign(TextAlign.Center)
                  .backgroundColor(0xFFFFFF)
              }
            }, (item: string) => item)
          }
        })
      }
      .width('90%')
      .sticky(StickyStyle.Header | StickyStyle.Footer)
      .scrollBar(BarState.Off)
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5, bottom: 5 })
  }
}

interface TimeTable {
  projects: string\[\];
}
