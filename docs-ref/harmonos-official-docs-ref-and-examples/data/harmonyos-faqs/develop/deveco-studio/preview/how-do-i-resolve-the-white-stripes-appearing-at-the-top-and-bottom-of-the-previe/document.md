# How do I resolve the white stripes appearing at the top and bottom of the preview window?

**Symptom**

How do I resolve the white stripes appearing at the top and bottom of the preview window?

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/6pSQgxhyRkO8iRaAprMgKg/en-us_image_0000002229603709.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF0C6CD5375D25F9F925EB48C137F24437FA1700E98FA5108A3190690E0B71FF)

**Solution**

White stripes appear because the application is set to immersive mode, where the status bar and navigation bar are located in the avoid area, and the components you develop are located in the safe area (beyond the avoid area). If you want to set the page layout to the full screen mode, use either of the following methods:

-   Method 1: In the preview scenario, use [expandSafeArea()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-expand-safe-area#expandsafearea) to extend the safe area.
    
    //Index.ets
    @Entry
    @Component
    struct Index {
      @State message: string = 'Hello World';
    
    
      build() {
        RelativeContainer() {
          Text(this.message)
            .id('HelloWorld')
            .fontSize(50)
            .fontWeight(FontWeight.Bold)
            .alignRules({
              center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
              middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
            })
        }
        .height('100%')
        .width('100%')
        .backgroundColor('#008000')
        .expandSafeArea(\[SafeAreaType.SYSTEM\])
      }
    }
    

-   Method 2: During preview debugging, call [setWindowLayoutFullScreen()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#setwindowlayoutfullscreen9) to set the window to full screen mode.
    
    // EntryAbility.ets
    onWindowStageCreate(windowStage: window.WindowStage): void {
      // Main window is created, set main page for this ability
      hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
      windowStage.loadContent('pages/Index', (err) => {
        // ...
      });
      windowStage.getMainWindow((err, data) => {
        if (!err.code) {
          data.setWindowLayoutFullScreen(true)
        }
      });
    }
    

**Reference**

[Immersive Effect Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-develop-apply-immersive-effects)
