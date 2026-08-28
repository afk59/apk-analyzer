# How do I align the TabBar of the Tabs component to the left?

The system-provided **Tabs** component only supports center alignment for the **TabBar**. To achieve left alignment, you can implement a custom TabBar: Combine **Scroll** and **Row** components to create a tab, and in the **onClick** event, change the index value and link it to the **Tabs** component's index to achieve the switching effect. In addition, set **barHeight** of the **Tabs** component to **0**. The code snippet is as follows:

// xxx.ets
@Entry
@Component
struct TabsExample {
  @State tabArray: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\];
  @State focusIndex: number = 0;
  private controller: TabsController = new TabsController();

  build() {
    Column() {
      // Use custom tab components
      Scroll() {
        Row() {
          ForEach(this.tabArray, (item: number, index: number) => {
            Row({ space: 20 }) {
              Text('tab' + item)
                .fontWeight(index === this.focusIndex ? FontWeight.Bold : FontWeight.Normal)
            }
            .padding({ left: 10, right: 10 })
            .onClick(() => {
              this.controller.changeIndex(index);
              this.focusIndex = index;
            })
          })
        }
      }
      .align(Alignment.Start)
      .scrollable(ScrollDirection.Horizontal)
      .scrollBar(BarState.Off)
      .width('100%')

      //The tabs component hides the tab bar
      Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
        ForEach(this.tabArray, (item: number, index: number) => {
          TabContent() {
            Text('I am the page ' + item + " the content")
              .fontSize(30)
          }
        })
      }.barHeight(0)
    }
    .height('100%')
    .width('100%')
  }
}
