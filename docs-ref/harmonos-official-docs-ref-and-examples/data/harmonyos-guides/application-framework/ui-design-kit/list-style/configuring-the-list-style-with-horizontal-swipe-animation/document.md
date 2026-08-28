# Configuring the List Style with Horizontal Swipe Animation

#### Use Case

The function of configuring the list style with horizontal swipe animation is available since version 6.0.0(20) Beta1.

Your app can leverage the [HdsListItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdslistitem) component to implement the content and style of system list buttons that appear after horizontal swiping across multiple devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/CFG47zU1R-2zQXqfLBe62Q/en-us_image_0000002500304220.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8CA168BD214DEDB7B376F089636F2A98117923DF8A701A8BC8CDB7E2319DCE0C "Click to enlarge")

#### Development Procedure

1.  Import required modules.
    
    import { promptAction, SymbolGlyphModifier, TextModifier } from '@kit.ArkUI';
    import { HdsListItem } from '@kit.UIDesignKit';
    
2.  Configure the page layout simply and call the **HdsListItem** API to draw the content and style of the list buttons that appear after horizontal swiping.
    
    @Entry
    @Component
    struct HdsListItemExample {
      @State dataSource: LazyDataSource<Item> = new LazyDataSource();
      @State dataArr: Array<Item> = \[\];
      @State EndOffset: number = 0;
      private scroller: Scroller = new Scroller();
    
      build() {
        Column() {
          List({ space: 10, scroller: this.scroller }) {
            LazyForEach(this.dataSource, (item: Item) => {
              HdsListItem({
                hdsListItemCard: {
                  textItem: {
                    primaryText: {
                      text: 'Primary Text',
                      modifier: new TextModifier().fontColor(Color.Orange).fontSize(16),
                    }
                  }
                },
                swipeActionOptions: {
                  icons: \[
                    {
                      icon: new SymbolGlyphModifier($r('sys.symbol.share')).fontColor(\[Color.Red\]).fontSize(16),
                      backgroundColor: Color.Green,
                      onAction: () => {
                        promptAction.openToast({ message: 'Tap share button', duration: 100 });
                      },
                    },
                    {
                      icon: new SymbolGlyphModifier($r('sys.symbol.plus\_square\_on\_square')),
                      backgroundColor: Color.Orange,
                      onAction: () => {
                        promptAction.openToast({ message: 'Tap copy button', duration: 100 });
                      },
                    },
                    {
                      icon: new SymbolGlyphModifier($r('sys.symbol.plus\_square\_dashed\_on\_square'))
                              .symbolEffect(new BounceSymbolEffect(), true),
                      onAction: () => {
                        promptAction.openToast({ message: 'Tap paste button', duration: 100 });
                      },
                    },
                  \],
                  deleteIconOptions: {
                    backgroundColor: Color.Red, //  ---Change the background color.
                    iconColor: Color.Gray, //  ---- Change the color of the trash can.
                    onAction: () => {
                      promptAction.openToast({ message: 'Tap delete button', duration: 100 });
                    }, //   --Tap action callback.
                  },
                  fullDeleteOptions: {
                    isFullDelete: true, // --- Indicates whether to automatically trigger deletion when the swipe distance exceeds the component size. The default value is **false**.
                    onFullDeleteAction: () => {
                      promptAction.openToast({ message: 'Trigger automatic deletion', duration: 100 });
                      this.getUIContext()?.animateTo({
                        duration: 350,
                      }, () => {
                        this.dataSource.deleteItem(item)
                      });
                    }, //   -- Callback upon deletion.
                  },
                }
              })
            }, (item: Item) => item.data)
          }
          .scrollBar(BarState.Off)
          .onDidScroll((scrollOffset: number) => {
            this.EndOffset = scrollOffset
          })
          .margin(10)
          .width('100%')
          .height('100%')
        }
        .backgroundColor('#0D182431')
        .width('100%')
        .height('100%')
      }
    
      aboutToAppear() {
        for (let i = 0; i < 2; i++) {
          this.dataSource.pushItem(new Item(i + ''));
          this.dataArr.push(new Item(i + ''));
        }
      }
    }
    
    class Item {
      constructor(data: string) {
        this.data = data;
      }
    
      public data: string = '';
    }
    
    export class LazyDataSource<T> implements IDataSource {
      private elements: T\[\];
      private listeners: Set<DataChangeListener>;
    
      constructor(elements: T\[\] = \[\]) {
        this.elements = elements;
        this.listeners = new Set();
      }
    
      public totalCount(): number {
        return this.elements.length;
      }
    
      public getData(index: number): T {
        return this.elements\[index\];
      }
    
      public indexOf(item: T): number {
        return this.elements.indexOf(item);
      }
    
      public pinItem(item: T, index: number): void {
        this.elements.splice(index, 1);
        this.elements.unshift(item);
        this.listeners.forEach(listener => listener.onDataReloaded());
      }
    
      public pushItem(item: T) {
        this.elements.push(item);
        this.listeners.forEach(listener => listener.onDataAdd(this.elements.length - 1));
      }
    
      public deleteItem(item: T): void {
        const index = this.elements.indexOf(item);
        if (index < 0) {
          return;
        }
        this.elements.splice(index, 1);
        this.listeners.forEach(listener => listener.onDataDelete(index));
      }
    
      public deleteItemByIndex(index: number): void {
        this.elements.splice(index, 1);
        this.listeners.forEach(listener => listener.onDataDelete(index));
      }
    
      public registerDataChangeListener(listener: DataChangeListener): void {
        this.listeners.add(listener);
      }
    
      public unregisterDataChangeListener(listener: DataChangeListener): void {
        this.listeners.delete(listener);
      }
    }
