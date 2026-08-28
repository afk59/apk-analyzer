# How do I implement an immersive status bar background color?

**Symptom**

To avoid the status bar color overlapping with the background, how can immersive effects adaptation be made based on the status bar and content area colors?

**Solution**

Method 1: Set the background color of the window. The sample code is as follows:

// EntryAbility.ets

onWindowStageCreate(windowStage: window.WindowStage): void {
  windowStage.loadContent('pages/Example', (err, data) => {
    if (err?.code) {
      return;
    }
    // Set the full window color to match the color of the application elements
    windowStage.getMainWindowSync().setWindowBackgroundColor('#008000');
  });
}

Method 2: Use the [expandSafeArea](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-expand-safe-area#expandsafearea) property on the top component to expand the safe area.

@Entry
@Component
struct Example {
  build() {
    Column() {
      Row() {
        Text('Top Row')
          .fontSize(40)
          .textAlign(TextAlign.Center)
          .width('100%')
      }
      .backgroundColor('#F08080')
      // Set the top drawing to extend to the status bar
      .expandSafeArea(\[SafeAreaType.SYSTEM\], \[SafeAreaEdge.TOP\])

      Row() {
        Text('ROW2')
          .fontSize(40)
      }
      .backgroundColor(Color.Orange)
      .padding(20)

      Row() {
        Text('ROW3')
          .fontSize(40)
      }
      .backgroundColor(Color.Orange)
      .padding(20)

      Row() {
        Text('ROW4')
          .fontSize(40)
      }
      .backgroundColor(Color.Orange)
      .padding(20)

      Row() {
        Text('ROW5')
          .fontSize(40)
      }
      .backgroundColor(Color.Orange)
      .padding(20)

      Row() {
        Text('Bottom Row')
          .fontSize(40)
          .textAlign(TextAlign.Center)
          .width('100%')
      }
      .backgroundColor(Color.Orange)
      // Set the bottom drawing to extend to the navigation bar
      .expandSafeArea(\[SafeAreaType.SYSTEM\], \[SafeAreaEdge.BOTTOM\])
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .backgroundColor('#008000')
    .justifyContent(FlexAlign.SpaceBetween)
  }
}

Method 3: Manually set the color of the status bar.

Procedure:

1.  Obtain and cache the window object. For details, see [Interface (Window)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window).
2.  When opening the target page, use the [setWindowSystemBarProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#setwindowsystembarproperties9) API to set the properties of the status bar.

Obtain and cache the window object.

// EntryAbility.ets

onWindowStageCreate(windowStage: window.WindowStage): void {
  // Main window is created, set main page for this ability
  hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

  windowStage.loadContent('pages/Index', (err) => {
    if (err.code) {
      hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
    let windowClass: window.Window = windowStage.getMainWindowSync(); // Get the main window of the application
    // 1. Set the window to full screen
    let isLayoutFullScreen = true;
    windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
    // 2. Cache window object
    AppStorage.setOrCreate('windowClass', windowClass);
  });
}

When opening the target page, set the properties of the status bar, selecting the desired immersive color.

import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct CommonTopBar {
  @State message: string = 'Hello World';

  aboutToAppear() {
    // Get the current application window
    let windowClass = AppStorage.get<window.Window>('windowClass') as window.Window;
    try {
      // Set the background color of the status bar and navigation bar to the same color as the application window
      windowClass.setWindowSystemBarProperties({
        // The color attribute is ARGB, set the dust cover to 0% to make it transparent
        // Navigation bar color
        navigationBarColor: '#fd121de5',
        // Status bar color
        statusBarColor: '#ff0ad9c2',
        // Status bar text color
        statusBarContentColor: '#fff1e50a'
      })
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'CommonTopBar', \`error code:${err.code},message:${err.message}\`);
    }
  }

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('PageHelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: {
            anchor: '\_\_container\_\_',
            align: VerticalAlign.Center
          },
          middle: {
            anchor: '\_\_container\_\_',
            align: HorizontalAlign.Center
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
