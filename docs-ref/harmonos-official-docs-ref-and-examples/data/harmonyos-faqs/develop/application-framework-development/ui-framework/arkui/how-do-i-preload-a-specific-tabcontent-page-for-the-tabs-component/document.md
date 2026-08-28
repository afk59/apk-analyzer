# How do I preload a specific TabContent page for the Tabs component?

Solution 1: Whether using **ForEach** or **LazyForEach** for repeated rendering, the content in **TabContent** is rendered once. Therefore, repeated rendering cannot be used.

Since the **Tabs** component has a swiping transition animation, the current page is swiped to the target page when the **TabBar** is clicked. As a result, the intermediate page between the current page and the target page is also loaded. You can use a custom transition animation to avoid the problem that multiple **TabContent** pages are loaded. For details, see the **customContentTransition** usage description.

Refer to the code snippet below.

@Entry
@Component
struct TabsDemo {
  @State currentIndex: number = 0;
  private tabsController: TabsController = new TabsController();
  // Set up page switching animations instead of sliding to jump to page animations
  private customContentTransition: (from: number, to: number) => TabContentAnimatedTransition =
    (from: number, to: number) => {
      let tabContentAnimatedTransition = {
        timeout: 1000,
        transition: (proxy: TabContentTransitionProxy) => {
          this.getUIContext().animateTo({
            duration: 0,
            onFinish: () => {
              proxy.finishTransition();
            }
          }, () => {
          })
        }
      } as TabContentAnimatedTransition
      return tabContentAnimatedTransition;
    }

  build() {
    Column() {
      Tabs({ index: this.currentIndex, controller: this.tabsController }) {
        TabContent() {
          MyComponent({ color: '#00CB87' })
        }.tabBar(SubTabBarStyle.of('green'))

        TabContent() {
          MyComponent({ color: '#007DFF' })
        }.tabBar(SubTabBarStyle.of('green'))

        TabContent() {
          MyComponent({ color: '#FFBF00' })
        }.tabBar(SubTabBarStyle.of('green'))

        TabContent() {
          MyComponent({ color: '#E67C92' })
        }.tabBar(SubTabBarStyle.of('green'))
      }
      .customContentTransition(this.customContentTransition)
      .width('100%')
      .height(296)
      .barBackgroundColor('#F1F3F5')
      .onChange((index: number) => {
        this.currentIndex = index;
      })
    }
  }
}

@Component
struct MyComponent {
  private color: string = '';

  aboutToAppear(): void {
    // It can be observed by printing the log that no intermediate page has been loaded
    console.info('aboutToAppear backgroundColor:' + this.color);
  }

  aboutToDisappear(): void {
    console.info('aboutToDisappear backgroundColor:' + this.color);
  }

  build() {
    Column()
      .width('100%')
      .height('100%')
      .backgroundColor(this.color)
  }
}

Solution 2: If you want to avoid loading intermediate pages and retain the swiping gesture for page switching, you can use **Swiper** to customize the **Tabs** component. You can call the **changeIndex** method of **SwiperController** to go to the specified page. If **useAnimation** is set to **false**, no animation is displayed.

Refer to the code snippet below.

class MyDataSource implements IDataSource {
  private list: number\[\] = \[\];

  constructor(list: number\[\]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list\[index\];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
  }
}

@Entry
@Component
struct SwiperExample {
  private swiperController: SwiperController = new SwiperController();
  private data: MyDataSource = new MyDataSource(\[\]);

  aboutToAppear(): void {
    let list: number\[\] = \[\];
    for (let i = 0; i <= 10; i++) {
      list.push(i);
    }
    this.data = new MyDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        LazyForEach(this.data, (item: string) => {
          Text(item.toString())
            .width('90%')
            .height(160)
            .backgroundColor(0XAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .cachedCount(2)
      .index(1)
      .autoPlay(true)
      .interval(4000)
      .loop(true)
      .duration(1000)
      .itemSpace(0)
      .indicator(false)

      Row({ space: 12 }) {
        Button('change to index:4')
          .onClick(() => {
            this.swiperController.changeIndex(3, false);
          })
        Button('change to index:7')
          .onClick(() => {
            this.swiperController.changeIndex(6, false);
          })
      }
      .margin(5)
    }
    .width('100%')
    .margin({ top: 5 })
  }
}
