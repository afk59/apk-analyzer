# How do I obtain the screen information of a phone?

Refer to the following code to obtain the screen width and height. For details about all properties of a **Display** instance, see [@ohos.display (Display)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-display).

import { display } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  private screenWidth: number = 0;
  private screenHeight: number = 0;

  aboutToAppear() {
    try {
      this.screenWidth = display.getDefaultDisplaySync().width;
      this.screenHeight = display.getDefaultDisplaySync().height;
    } catch (e) {
      console.error('Fail with code: ' + JSON.stringify(e));
    }
  }

  build() {
    Row() {
      Column() {
        Text('---->width: ' + this.screenWidth)
        Text('---->height: ' + this.screenHeight)
      }
      .width('100%')
    }
    .height('100%')
  }
}
