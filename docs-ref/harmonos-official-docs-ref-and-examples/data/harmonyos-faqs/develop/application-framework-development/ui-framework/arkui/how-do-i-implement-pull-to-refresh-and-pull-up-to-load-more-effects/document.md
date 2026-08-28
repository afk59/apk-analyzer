# How do I implement pull-to-refresh and pull-up-to-load-more effects?

Use the [onTouch](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-events-touch#ontouch) event to determine whether the touch conditions meet the criteria for pull-to-refresh and pull-up-to-load-more within the **putDownPullUpRefresh** method. In addition, use conditional rendering to decide whether to display the refresh and load-more layouts.

The code snippet is as follows:

@Entry
@Component
struct PageToRefresh {
  private currentOffsetY: number = 0;
  @State refreshStatus: boolean = false;
  @State refreshText: string = 'Refreshing';
  @State pullUpText: string = 'loading';
  private timer: number = 0;
  @State isRefreshing: boolean = false;
  @State isCanLoadMore: boolean = false;
  @State ArrData: string\[\] = \['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'\];
  @State newArr: string \[\] = \['10', '11'\]

  putDownPullUpRefresh(event?: TouchEvent): void {
    if (event === undefined) {
      return;
    }
    switch (event.type) {
      case TouchType.Down:
        this.currentOffsetY = event.touches\[0\].y;
        break;
      case TouchType.Move:
        let isDownPull = event.touches\[0\].y - this.currentOffsetY > 50;
        if (isDownPull && this.isCanLoadMore === false) {
          this.refreshStatus = true;
        }

        if (this.ArrData.length <= 11) {
          this.isCanLoadMore = true;
        }
        break;
      case TouchType.Cancel:
        break;
      case TouchType.Up:
        if (this.refreshStatus) {
          this.timer = setTimeout(() => {
            this.refreshStatus = false;
            this.ArrData = \['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'\];
          }, 1500)
        }

        if (this.isCanLoadMore) {
          this.timer = setTimeout(() => {
            this.isCanLoadMore = false;
            this.newArr.forEach((item) => {
              this.ArrData.push(item)
            })
          }, 1000)
        }

        break;
      default:
        break;
    }
  }

  @Builder
  putDown() {
    Row() {
      Image($r('app.media.refreshing'))
        .width(40)
        .height(20)
      Text(this.refreshText).fontSize(16)
    }
    .justifyContent(FlexAlign.Center)
    .width('94%')
    .height('10%')
  }

  @Builder
  PullUp() {
    Row() {
      Image($r('app.media.refreshing'))
        .width(40)
        .height(40)
      Text(this.pullUpText).fontSize(16)
    }
    .justifyContent(FlexAlign.Center)
    .width('94%')
    .height('5%')
  }

  build() {
    Column() {
      Scroll() {
        Column() {
          Text('goods')
          if (this.refreshStatus) {
            this.putDown()
          }
          ForEach(this.ArrData, (item: string) => {
            ListItem() {
              Text(item)
                .height(100)
            }
          }, (item: string) => JSON.stringify(item))
          if (this.isCanLoadMore) {
            this.PullUp()
          }
          if (!this.isCanLoadMore) {
            Text('No more data available at the moment')
          }
        }
      }
      .width('100%')
      .onTouch((event?: TouchEvent) => {
        this.putDownPullUpRefresh(event);
      })
    }
  }
}
