# How do I obtain the frame rate and rendering time during application running?

No API is provided for obtaining the real-time frame rate. However, an API is provided to obtain the arrival time of a single frame. You can calculate the rendering time based on the arrival time of two adjacent frames.

Refer to the code snippet below.

import { displaySync } from '@kit.ArkGraphics2D';

@Entry
@Component
struct Index {
  @State backDisplaySync: displaySync.DisplaySync = displaySync.create();
  private passframeInfo: Array<displaySync.IntervalInfo> = \[\]
  @State fps: number = 0

  aboutToAppear(): void {
    let callback = (frameInfo: displaySync.IntervalInfo) => {
      this.passframeInfo.push(frameInfo);
      if (this.passframeInfo.length >= 2) {
        let tmp = this.passframeInfo\[1\].timestamp - this.passframeInfo\[0\].timestamp;
        let result = 1000000000 / Number.parseInt(tmp.toString());
        this.fps = result;
        this.passframeInfo.shift();
      }
    };
    // Register subscription function
    this.backDisplaySync?.on("frame", callback);
  }

  build() {
    Column() {
      Row() {
        Text('Start')
          .fontSize(50)
          .onClick(() => \[
            this.backDisplaySync?.start()
          \])
      }

      Row() {
        Text(this.fps.toString())
          .fontSize(50)
      }

      Row() {
        Text('End')
          .fontSize(50)
          .onClick(() => \[
            this.backDisplaySync?.stop()
          \])
      }
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}

**Reference**

[@ohos.graphics.displaySync (Variable Frame Rate)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-graphics-displaysync)
