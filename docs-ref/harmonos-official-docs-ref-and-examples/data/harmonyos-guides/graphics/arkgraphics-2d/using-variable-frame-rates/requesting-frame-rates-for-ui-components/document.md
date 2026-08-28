# Requesting Frame Rates for UI Components

If you want to draw and update a UI component at an independent frame rate, you can call the APIs provided by the **DisplaySync** module. For details, see [@ohos.graphics.displaySync (Variable Frame Rate)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-graphics-displaysync).

#### How to Develop

This section describes how to use different frame rates to change the font size of the **<Text>** component. This operation simulates the effect of different frame rates on the UI components.

1.  Import the **DisplaySync** module.
    
    import { displaySync } from '@kit.ArkGraphics2D';
    
2.  Define and create a **DisplaySync** instance.
    
    @Entry
    @Component
    struct Index {
      // ...
    
      private backDisplaySyncSlow: displaySync.DisplaySync | undefined = undefined;
      private backDisplaySyncFast: displaySync.DisplaySync | undefined = undefined;
      // ...
    }
    
3.  Define two **<Text>** components.
    
    @State drawFirstSize: number = 25;
    @State drawSecondSize: number = 25;
    
    // ...
    
    @Builder
    doSomeRenderFirst() {
      Text('30')
        .fontSize(this.drawFirstSize)
    }
    
    @Builder
    doSomeRenderSecond() {
      Text('60')
        .fontSize(this.drawSecondSize)
    }
    
4.  Set the expected frame rate range and register a subscription function through the **DisplaySync** instance.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/FZNjOfh-STeIH-yCiYu4fw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1AFB354196D9F8D701F3894158733BB072BECF12795F23EA1454B9A19334A24A)
    
    The subscription function runs in the UI main thread. To avoid adverse impact on the performance, time-consuming operations related to the UI thread should not run in the subscription function.
    
    CreateDisplaySyncSlow() {
      let range: ExpectedFrameRateRange = {
        expected: 30,
        min: 0,
        max: 120
      };
    
      let draw30 = (intervalInfo: displaySync.IntervalInfo) => {
        if (this.isBigger\_30) {
          this.drawFirstSize += 1;
          if (this.drawFirstSize > 150) {
            this.isBigger\_30 = false;
          }
        } else {
          this.drawFirstSize -= 1;
          if (this.drawFirstSize < 25) {
            this.isBigger\_30 = true;
          }
        }
      };
    
      this.backDisplaySyncSlow = displaySync.create();
      this.backDisplaySyncSlow.setExpectedFrameRateRange(range);
      this.backDisplaySyncSlow.on("frame", draw30);
    }
    
5.  Start callback for each frame.
    
    Button('Start')
      .id('CustomDrawStart')
      .fontSize(14)
      .fontWeight(500)
      .margin({ bottom: 10, left: 5 })
      .fontColor(Color.White)
      .onClick((): void => {
        if (this.backDisplaySyncSlow == undefined) {
          this.CreateDisplaySyncSlow();
        }
        if (this.backDisplaySyncFast == undefined) {
          this.CreateDisplaySyncFast();
        }
        if (this.backDisplaySyncSlow) {
          this.backDisplaySyncSlow.start();
        }
        if (this.backDisplaySyncFast) {
          this.backDisplaySyncFast.start();
        }
      })
      .width('20%')
      .height(40)
      .shadow(ShadowStyle.OUTER\_DEFAULT\_LG)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/c9-ZDfrAQ4a3LGn4RX1U3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D5DE5886E999422CFCFD02EAECC6080DD106193EBE9499F6DBBA72D586B68B5)
    
    After **start()** is called, the **stop()** API must be performed and the **DisplaySync** instance must be set to null in the **aboutToDisappear** function to avoid memory leaks.
    
    aboutToDisappear() {
      if (this.backDisplaySyncSlow) {
        this.backDisplaySyncSlow.stop();
        this.backDisplaySyncSlow = undefined;
      }
      if (this.backDisplaySyncFast) {
        this.backDisplaySyncFast.stop();
        this.backDisplaySyncFast = undefined;
      }
    }
    
6.  Stop callback for each frame.
    
    Button('Stop')
      .id('CustomDrawStop')
      .fontSize(14)
      .fontWeight(500)
      .margin({ bottom: 10, left: 5 })
      .fontColor(Color.White)
      .onClick((): void => {
        if (this.backDisplaySyncSlow) {
          this.backDisplaySyncSlow.stop();
        }
        if (this.backDisplaySyncFast) {
          this.backDisplaySyncFast.stop();
        }
      })
      .width('20%')
      .height(40)
      .shadow(ShadowStyle.OUTER\_DEFAULT\_LG)
