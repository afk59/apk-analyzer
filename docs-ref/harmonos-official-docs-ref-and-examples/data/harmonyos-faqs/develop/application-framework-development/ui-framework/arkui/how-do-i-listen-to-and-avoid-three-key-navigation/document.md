# How do I listen to and avoid three-key navigation?

**Solution**

1\. Use [settings.registerKeyObserver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-settings#settingsregisterkeyobserver11) to listen to the enabling of three-key navigation.

settings.registerKeyObserver(this.getUIContext().getHostContext(), 'float\_navigation\_info',
  settings.domainName.USER\_PROPERTY, () => {
    this.adaptLayout();
  });

2\. Use [setting.getValue](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-settings#settingsgetvalue11) to obtain the navigation information.

settings.getValue(this.getUIContext().getHostContext(), 'float\_navigation\_info',
  settings.domainName.USER\_PROPERTY).then((data: string) => {
  if (data) {
    let navigationInfo = JSON.parse(data) as NavigationButtonInfo;
    this.adaptValue = navigationInfo.getAdaptValue();
  }
})

3\. Define the three-key navigation information.

class NavigationButtonInfo {
  // Display Status: -1 Not displayed; 0 Appears in a three-key form; 1 Displayed as a floating ball
  private showType: number = -1;
  // Three-Key navigation location area: x coordinate; y coordinate; Width of the triple-key area; Triple key area height; unit: px
  private region: number\[\] = \[0, 0, 0, 0\];

  // Obtain the adaptation area and implement this function as required
  public getAdaptValue(): number {
    // If the three keys are displayed and an app is in full screen, the width of the three keys is used as the adaptation value
    // this.region\[2\] < this.region\[3\] This indicates that the three buttons are displayed at the side of the screen when the screen is in landscape mode.
    if (this.showType === 0 && this.region\[2\] < this.region\[3\]) {
      return this.region\[2\];
    } else {
      return 0;
    }
  }
}

4\. Make adaptations based on the layout information in the **region**.

.padding({ right: this.getUIContext().px2vp(this.adaptValue) })

The code snippet is as follows:

import settings from '@ohos.settings';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import window from '@ohos.window';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  @State adaptValue: number = 0;

  aboutToAppear(): void {
    this.watchNavigationButtonChange();
    window.getLastWindow(this.getUIContext().getHostContext(), ((err: BusinessError, data) => {
      data.setWindowLayoutFullScreen(true);
    }));
  }

  // Monitor the changes of three-key navigation information
  private watchNavigationButtonChange(): void {
    this.adaptLayout();

    settings.registerKeyObserver(this.getUIContext().getHostContext(), 'float\_navigation\_info',
      settings.domainName.USER\_PROPERTY, () => {
        this.adaptLayout();
      });
  }

  // Adapt the app layout based on the Three Key Navigation information
  private adaptLayout(): void {
    try {
      settings.getValue(this.getUIContext().getHostContext(), 'float\_navigation\_info',
        settings.domainName.USER\_PROPERTY).then((data: string) => {
        if (data) {
          let navigationInfo = JSON.parse(data) as NavigationButtonInfo;
          this.adaptValue = navigationInfo.getAdaptValue();
        }
      })
    } catch (e) {
      this.adaptValue = 0;
      hilog.warn(0, 'tag', 'adaptMargin err:' + e);
    }
  }

  build() {
    RelativeContainer() {
      Column() {
        Row() {
          Text(this.message)
            .id('HelloWorld')
            .fontSize($r('app.float.page\_text\_font\_size'))
            .fontWeight(FontWeight.Bold)
            .alignRules({
              center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
              middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
            })
            .onClick(() => {
              this.message = 'Welcome';
            })
        }
        .backgroundColor(Color.Red)
        .height('100%')
        .width('100%')
      }
      .backgroundColor(Color.Yellow)
      .padding({ right: this.getUIContext().px2vp(this.adaptValue) })
    }
    .height('100%')
    .width('100%')
  }
}

class NavigationButtonInfo {
  // Display Status: -1 Not displayed; 0 Appears in a three-key form; 1 Displayed as a floating ball
  private showType: number = -1;
  // Three-Key navigation location area: x coordinate; y coordinate; Width of the triple-key area; Triple key area height; unit: px
  private region: number\[\] = \[0, 0, 0, 0\];

  // Obtain the adaptation area and implement this function as required
  public getAdaptValue(): number {
    // If the three keys are displayed and an app is in full screen, the width of the three keys is used as the adaptation value
    // this.region\[2\] < this.region\[3\] This indicates that the three buttons are displayed at the side of the screen when the screen is in landscape mode.
    if (this.showType === 0 && this.region\[2\] < this.region\[3\]) {
      return this.region\[2\];
    } else {
      return 0;
    }
  }
}

For details about the immersive effect of the navigation bar, status bar, and notched area, see [Implementing the Immersive Effect](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-multi-device-window-immersive#section180431120426).
