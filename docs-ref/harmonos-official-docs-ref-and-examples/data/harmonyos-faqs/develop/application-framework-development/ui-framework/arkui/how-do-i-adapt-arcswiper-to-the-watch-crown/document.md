# How do I adapt ArcSwiper to the watch crown?

Slidable components need to be adapted to the rotating watch crown. Components that support crown interactions by default can respond to crown events when focused.

1.  You only need to add the **.focusable(true)**, **.focusOnTouch(true)**, and **.defaultFocus(true)** attributes to them.
    
    Components that support crown interactions by default: **Slider**, **DatePicker**, **TextPicker**, **TimePicker**, **Scroll**, **List**, **Grid**, **WaterFlow**, **ArcList**, **Refresh**, and **Swiper**.
    
    The sample code is as follows:
    
    @Entry
    @Component
    struct Index {
      private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\];
    
      build() {
        Column() {
          List({ space: 20, initialIndex: 0 }) {
            ForEach(this.arr, (item: number) => {
              ListItem() {
                Button('' + item)
                  .width('100%')
                  .height(100)
                  .fontSize(16)
              }
              .onClick(() => {
              })
            }, (item: string) => item)
          }
          .focusable(true)
          .defaultFocus(true)
          .focusOnTouch(true) // After the list component is focused, it can respond to the sliding control of the rotating crown
          .width('90%')
          .height('100%')
        }
        .width('100%')
        .height('100%')
        .backgroundColor(0xDCDCDC)
        .padding({ top: 5 })
      }
    }
    
2.  Other components can listen to crown events through **onDigitalCrown**.
    
    The sample code is as follows:
    
    @Entry
    @Component
    struct CityList {
      @State message: string = 'onDigitalCrown';
    
      build() {
        Column() {
          Row() {
            Stack() {
              Text(this.message)
                .fontSize(20)
                .fontColor(Color.White)
                .backgroundColor('#262626')
                .textAlign(TextAlign.Center)
                .focusable(true)
                .focusOnTouch(true)
                .defaultFocus(true)
                .borderWidth(2)
                .width(223)
                .height(223)
                .borderRadius(110)
                .onDigitalCrown((event: CrownEvent) => {
                  event.stopPropagation();
                  this.message = 'CrownEvent\\n\\n' + JSON.stringify(event);
                  console.debug('action:%d, angularVelocity:%f,degree:%f,timestamp:%f', event.action, event.angularVelocity,
                    event.degree, event.timestamp);
                })
            }
          }
        }
      }
    }
    
3.  The **List** component cannot automatically obtain focus in the else scenario of the if/else statement, and the rotating crown does not take effect. Call **requestFocus** in the **onAppear** method of the **List** component to manually obtain focus. The sample code is as follows:
    
    @Entry
    @Component
    struct Index {
      private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\];
      @State isLoading: boolean = true;
    
      onPageShow(): void {
        setTimeout(() => {
          this.isLoading = false;
        }, 3000)
      }
    
      build() {
        Column() {
          if (this.isLoading) {
            Text('Loading data...')
          } else {
            List({ space: 20, initialIndex: 0 }) {
              ForEach(this.arr, (item: number) => {
                ListItem() {
                  Button('' + item)
                    .width('100%')
                    .height(100)
                    .fontSize(16)
                }
                .onClick(() => {
                })
              }, (item: string) => item)
            }
            .onAppear(() => {
              try {
                this.getUIContext().getFocusController().requestFocus('test');
              } catch (error) {
                console.error('requestFocus failed code is ' + error.code + 'message is ' + error.message);
              }
            })
            .id('test')
            .focusable(true)
            .defaultFocus(true)
            .focusOnTouch(true) // After the list component is focused, it can respond to the sliding control of the rotating crown
            .width('90%')
            .height('100%')
          }
        }
        .width('100%')
        .height('100%')
        .backgroundColor(0xDCDCDC)
        .padding({ top: 5 })
      }
    }
    

**Reference**

[Crown Event](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-events-crown)

[Focus Control](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-focus)

[ArcSwiper Example](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-arcswiper#example)
