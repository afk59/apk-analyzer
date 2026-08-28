# Gestures Freeze or Do Not Work

**Symptom**

Gestures freeze or do not work on the map.

**Possible causes**

1.  Gesture masking or gesture conflict occurs.
    -   Gesture masking: The upper-layer map components do not support gesture passthrough.
    -   Gesture conflict: The gestures of another component, for example, the Swiper component, conflict with those of the map component.
2.  The main thread is blocked.
    
    If the app's main thread is blocked due to processing of a large number of logical operations, map gesture operations will experience a significant slowdown or even failure.
    

**Solution**

1.  For gesture masking or gesture conflict:
    -   Gesture masking: Refer to [Hit Test Control](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-hit-test-behavior) to enable gesture passthrough.
    -   Gesture conflict: Solve the problem by referring to the following code, which provides a solution to the gesture conflict between the Swiper component and map component.
        
        import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
        import { map, mapCommon, MapComponent } from '@kit.MapKit';
        
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
          private mapOptions?: mapCommon.MapOptions;
          private callback?: AsyncCallback<map.MapComponentController>;
          private mapController?: map.MapComponentController;
          private mapEventManager?: map.MapEventManager;
          @State mapPositionX: number = 0;
          @State mapPositionY: number = 0;
          @State mapHeight: number = 0;
          @State mapWidth: number = 0;
          @State index: number = 0;
        
          // Check whether the coordinates are within the map rectangle.
          isMap(event: TouchEvent) {
            if (event.changedTouches\[0\].displayX > this.mapPositionX
              && event.changedTouches\[0\].displayX < this.mapPositionX + this.mapWidth
              && event.changedTouches\[0\].displayY > this.mapPositionY
              && event.changedTouches\[0\].displayY < this.mapPositionY + this.mapHeight) {
              return true;
            }
            return false;
          }
        
          aboutToAppear(): void {
            let list: number\[\] = \[\];
            for (let i = 1; i <= 10; i++) {
              list.push(i);
            }
            this.data = new MyDataSource(list);
        
            this.mapOptions = {
              position: {
                target: {
                  latitude: 31.98441025,
                  longitude: 118.766253
                },
                zoom: 10,
                tilt: 10,
                bearing: 90
              },
              scaleControlsEnabled: true
            }
        
            this.callback = async (err, mapController) => {
              if (!err) {
                this.mapController = mapController;
                this.mapEventManager = this.mapController.getEventManager();
                let callback = () => {
                  console.info(\`on-mapLoad\`);
                };
                this.mapEventManager.on("mapLoad", callback);
              } else {
                console.error(\`Failed to initialize the map. Code: ${err.code}; message: ${err.message}\`);
              }
            }
          }
        
          build() {
            Column({ space: 5 }) {
              Swiper(this.swiperController) {
                LazyForEach(this.data, (item: string) => {
                  if (item == "3") {
                    Column() {
                      Text(item.toString())
                        .width('90%')
                        .height(160)
                        .backgroundColor(0xAFEEEE)
                        .textAlign(TextAlign.Center)
                        .fontSize(30)
                      MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
                        // Obtain the position, width, and height of the MapComponent.
                        .width('100%')
                        .height('65%')
                        .onAreaChange((\_oldValue: Area, newValue: Area) => {
                          try {
                            if (newValue.globalPosition.x !== undefined && newValue.globalPosition.y !== undefined) {
                              this.mapPositionX = Number(newValue.globalPosition.x);
                              this.mapPositionY = Number(newValue.globalPosition.y);
                              this.mapHeight = Number(newValue.height);
                              this.mapWidth = Number(newValue.width);
                            }
                          } catch (error) {
                            let e: BusinessError = error as BusinessError;
                            console.error("onAreaChange error code:" + e.code + "message:" + e.message);
                          }
                        })
                    }.height("100%")
                  } else {
                    Text(item.toString())
                      .width('90%')
                      .height(160)
                      .backgroundColor(0xAFEEEE)
                      .textAlign(TextAlign.Center)
                      .fontSize(30)
                  }
                }, (item: string) => item)
              }
              // Gesture judgment. When the index indicates that the map page exists and the tap is in the map rectangle, the value is **HitTestMode.None** (indicating that gestures of the subcomponent will be responded to instead of swiper gestures).
              .onTouchIntercept((event: TouchEvent) => {
                if (this.index === 2 && this.isMap(event)) {
                  return HitTestMode.None;
                }
                return HitTestMode.Transparent;
              })
              .cachedCount(2)
              .index(1)
              .loop(true)
              .itemSpace(0)
              // Set the style of the navigation dots.
              .indicator(
                new DotIndicator()
                  .itemWidth(15)
                  .itemHeight(15)
                  .selectedItemWidth(15)
                  .selectedItemHeight(15)
                  .color(Color.Gray)
                  .selectedColor(Color.Blue))
              .displayArrow({
                // Set the style of the navigation arrows.
                showBackground: true,
                isSidebarMiddle: true,
                backgroundSize: 24,
                backgroundColor: Color.White,
                arrowSize: 18,
                arrowColor: Color.Blue
              }, false)
              .curve(Curve.Linear)
              .onChange((index: number) => {
                this.index = index;
              })
              .onGestureSwipe((index: number, extraInfo: SwiperAnimationEvent) => {
                console.info("index: " + index);
                console.info("current offset: " + extraInfo.currentOffset);
              })
        
              Row({ space: 12 }) {
                Button('showNext')
                  .onClick(() => {
                    this.swiperController.showNext();
                  })
                Button('showPrevious')
                  .onClick(() => {
                    this.swiperController.showPrevious();
                  })
              }.margin(5)
            }.width('100%')
            .margin({ top: 5 })
          }
        }
        
2.  For the main thread blocking:
    
    Analyze the service logic of the app and offload complex logic to a subthread.
