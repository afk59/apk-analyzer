# How do I restore a swipe action item to its initial state?

You can use the **closeAllSwipeActions()** method provided by **ListScroller** to achieve the purpose. The sample code is as follows:

@Component
export struct SwiperActionRecover {
  @State arr: number\[\] = \[1, 2, 3, 4, 5, 6, 7, 8, 9, 10\];
  private scrollerForList: ListScroller = new ListScroller();

  @Builder
  itemEnd() {
    Row() {
      Button('Delete')
      Button('Set')
        .onClick(() => {
          this.scrollerForList.closeAllSwipeActions(); // This is the key line of code
        })
    }
    .justifyContent(FlexAlign.SpaceEvenly)
  }

  build() {
    Column() {
      List({ space: 5, scroller: this.scrollerForList }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text('item' + item)
              .width('100%')
              .height(100)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
          .transition({
            type: TransitionType.Delete,
            opacity: 0
          })
          .swipeAction({
            end: {
              builder: () => {
                this.itemEnd();
              },
              onAction: () => {
                this.getUIContext().animateTo({ duration: 1000 }, () => {
                  let index = this.arr.indexOf(item);
                  this.arr.splice(index, 1);
                });
              },
              actionAreaDistance: 56
            }
          })
        }, (item: string) => item)
      }
    }
    .padding(20)
    .backgroundColor(0xDCDCDC)
    .width('100%')
    .height('100%')
  }
}
