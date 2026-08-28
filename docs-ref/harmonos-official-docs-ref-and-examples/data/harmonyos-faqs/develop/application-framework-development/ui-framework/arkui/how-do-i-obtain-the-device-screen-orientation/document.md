# How do I obtain the device screen orientation?

Method 1: Use the media query API.

import { mediaquery, UIContext } from '@kit.ArkUI';

// Store context in EntryAbility
const context = AppStorage.get("context") as UIContext;
let listener = context.getMediaQuery().matchMediaSync('(orientation: landscape)'); // Listen to landscape events
function onPortrait(mediaQueryResult: mediaquery.MediaQueryResult) {
  console.info('mediaQueryResult.matches:' + mediaQueryResult.matches)
  if (mediaQueryResult.matches) {
    // do something here
  } else {
    // do something here
  }
}
listener.on('change', onPortrait) // Register callback
listener.off('change', onPortrait) // Unregister callback

@Entry
@Component
struct Index {
  build() {
    Column() {
      Column() {
        Text('test')
      }
      .width('100%')
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.End)
  }
}

Method 2:

You can obtain a [Display](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-display#display) instance by calling the [display.getDefaultDisplaySync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-display#displaygetdefaultdisplaysync9) method, and then obtain its **rotation** property to determine the screen orientation (portrait or landscape).

import { display, window } from '@kit.ArkUI';

@Entry
@Component
struct WindowRotation {
  build() {
    Text("Scroll Area")
      .width("100%")
      .height("100%")
      .backgroundColor(0X330000FF)
      .fontSize(16)
      .textAlign(TextAlign.Center)
      .onClick(() => {
        window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
          let cutOutInfo = win.getWindowAvoidArea(window.AvoidAreaType.TYPE\_SYSTEM\_GESTURE)
          console.log(JSON.stringify(cutOutInfo))
          if (window.Orientation.AUTO\_ROTATION) {
            let rotation: number = display.getDefaultDisplaySync().orientation // Get current screen orientation enum value
            console.log('' + rotation);
            if (rotation == 0) {
              console.log("CutOutInfo Portrait data: " + JSON.stringify(cutOutInfo));
            } else if (rotation == 1) {
              console.log("CutOutInfo Landscape data: " + JSON.stringify(cutOutInfo));
            } else if (rotation == 2) {
              console.log("CutOutInfo Reverse portrait data: " + JSON.stringify(cutOutInfo));
            } else {
              console.log("CutOutInfo Reverse landscape data: " + JSON.stringify(cutOutInfo));
            }
          }
        })
      })
  }
}
