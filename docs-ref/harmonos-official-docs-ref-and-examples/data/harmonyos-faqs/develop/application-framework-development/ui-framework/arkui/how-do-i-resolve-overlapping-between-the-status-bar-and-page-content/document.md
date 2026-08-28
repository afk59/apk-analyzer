# How do I resolve overlapping between the status bar and page content?

**Symptom**

There are two scenarios for the overlap issue between the status bar and page content:

1.  The status bar is not hidden as expected, such as in image preview scenarios.
2.  The UI layout does not make way for the status bar.

**Solution for Scenario 1**

1.  Call **setWindowLayoutFullScreen()** to set the window to full screen mode.
2.  Obtain and cache the window object. For details, see [Interface (Window)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window).
3.  When the image preview page is displayed, use the window object to call [setSpecificSystemBarEnabled()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#setspecificsystembarenabled11) to set the status bar to hidden.
4.  When the mask is clicked to exit image preview, use the window object to call [setSpecificSystemBarEnabled()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#setspecificsystembarenabled11) to set the status bar to visible.

Refer to the code snippet below.

Set the window to full screen mode and cache the window object.

// EntryAbility.ets

onWindowStageCreate(windowStage: window.WindowStage): void {
  // Main window is created, set main page for this ability
  hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

  windowStage.loadContent('pages/ImagePreview', (err) => {
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

import { window } from '@kit.ArkUI';

@Entry
@Component
struct ImagePreviewExample {
  windowClass: window.Window = AppStorage.get<window.Window>('windowClass') as window.Window;
  @State visible: Visibility = Visibility.None;
  @State scaleValue: number = 1;
  @State pinchValue: number = 1;
  @State pinchX: number = 0;
  @State pinchY: number = 0;
  @State count: number = 0;
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State positionX: number = 0;
  @State positionY: number = 0;

  build() {
    Stack() {
      Row() {
        Column() {
          Image($r('app.media.startIcon'))
            .width(100)
            .height(100)
            .onClick(() => {
              if (this.visible === Visibility.Visible) {
                this.visible = Visibility.None;
              } else {
                this.visible = Visibility.Visible;
                this.windowClass.setSpecificSystemBarEnabled('status', false);
              }
            })
        }
        .width('100%')
        .justifyContent(FlexAlign.Center)
        .alignItems(HorizontalAlign.Center)
      }
      .height('100%')

      Text('')
        .onClick(() => {
          if (this.visible === Visibility.Visible) {
            this.windowClass.setSpecificSystemBarEnabled('status', true);
            this.visible = Visibility.None;
          } else {
            this.visible = Visibility.Visible;
          }
        })
        .width('100%')
        .height('100%')
        .opacity(0.16)// transparency
        .backgroundColor(Color.Black)
        .visibility(this.visible)

      Column() {
        Image($r('app.media.startIcon'))
          .width(300)
          .height(300)
          .draggable(false)
          .visibility(this.visible)
          .scale({
            x: this.scaleValue,
            y: this.scaleValue,
            z: 1
          })
          .translate({
            x: this.offsetX,
            y: this.offsetY,
            z: 0
          })
          .gesture(
            GestureGroup(GestureMode.Parallel,
              PinchGesture({ fingers: 2 })
                .onActionUpdate((event?: GestureEvent) => {
                  if (event) {
                    this.scaleValue = this.pinchValue \* event.scale;
                    this.pinchX = event.pinchCenterX;
                    this.pinchY = event.pinchCenterY;
                  }
                })
                .onActionEnd(() => {
                  this.pinchValue = this.scaleValue;
                }),
              PanGesture()
                .onActionUpdate((event?: GestureEvent) => {
                  if (event) {
                    this.offsetX = this.positionX + event.offsetX;
                    this.offsetY = this.positionY + event.offsetY;
                  }
                })
                .onActionEnd(() => {
                  this.positionX = this.offsetX;
                  this.positionY = this.offsetY;
                })
            )
          )
      }
    }
    .backgroundColor(Color.White)
    .height('100%')
    .width('100%')
  }
}

**Solution for Scenario 2**

1.  Call [setWindowLayoutFullScreen()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#setwindowlayoutfullscreen9) to set the window to full screen mode.
2.  Call [getWindowAvoidArea()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-uiextension#getwindowavoidarea) to obtain the avoid area, where the window cannot be displayed (such as the status bar and navigation bar).
3.  In the layout, make accommodations for specific component layouts to avoid obstruction, such as adding corresponding height to the top component or setting margins or padding.

Refer to the code snippet below.

// EntryAbility.ets

onWindowStageCreate(windowStage: window.WindowStage): void {
  // Main window is created, set main page for this ability
  hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

  windowStage.loadContent('pages/AvoidStatusBar', (err) => {
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

    // 3. Obtain layout to avoid obstructed areas
    let type = window.AvoidAreaType.TYPE\_SYSTEM;
    let avoidArea = windowClass.getWindowAvoidArea(type);
    let statusBar =windowClass.getUIContext().px2vp( avoidArea.topRect.height); // Get the height of the status bar
    AppStorage.setOrCreate('statusBar', statusBar);
  });
}

@Entry
@Component
struct AvoidStatusBar {
  statusBar: number = AppStorage.get<number>('statusBar') as number;

  build() {

    Column() {
      Row() {
        Text('ROW1')
          .fontSize(40)
      }
      .backgroundColor(Color.Orange)
      .padding(20)

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
        Text('ROW6')
          .fontSize(40)
      }
      .backgroundColor(Color.Orange)
      .padding(20)
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.SpaceBetween)
    .padding({ top: this.statusBar }) // The specific value of the margin or padding here should be consistent with the height of the status bar area in practice
    .backgroundColor('#008000')
  }
}
