# How do I get and set the screen brightness?

You can get and set the screen brightness in either of the following ways:

1\. Use the **settings** module.

1.  Use the [settings.getValueSync()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-settings#settingsgetvaluesync10) method to get the screen brightness. Pass in the application context, the name of the data item (screen brightness is **settings.display.SCREEN\_BRIGHTNESS\_STATUS**), and the default value to retrieve the current screen brightness, which has a value range of 0 to 255.
    
    Button('Get screen brightness')
      .width(328)
      .margin({
        top: 16,
        bottom:16
      })
      .onClick(() => {
        // Get screen brightness through the getValueSync() method.
        this.settingsBrightness = settings.getValueSync(this.context, settings.display.SCREEN\_BRIGHTNESS\_STATUS, '10');
      })
    
2.  Use the [settings.setValue()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-settings#settingssetvalue10-1) method to set the screen brightness. Pass in the application context, the name of the data item (screen brightness is **settings.display.SCREEN\_BRIGHTNESS\_STATUS**) and the setting value to set the current screen brightness. Note that the **settings.setValue()** method is available only to system applications.

2\. Use the [window](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-window) module.

1.  In the **onWindowStageCreate** method in **EntryAbility.ets**, set AppStorage to save the window instance.
    
    onWindowStageCreate(windowStage: window.WindowStage): void {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
      let windowClass = windowStage.getMainWindowSync();
      AppStorage.setOrCreate('windowClass',windowClass);
      // ...
    }
    
2.  Use [getWindowProperties()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#getwindowproperties9) of the window instance to obtain the window properties, including the screen brightness information.
    
    Button('Get screen brightness')
      .width(328)
      .margin({
        top: 16,
        bottom:16
      })
      .onClick(() => {
        try {
          // By retrieving window properties using getWindowProperties(), the screen brightness can be obtained.
          let properties = this.windowClass?.getWindowProperties();
          this.windowBrightness = properties?.brightness ?? -1;
        } catch (exception) {
          hilog.error(0x0000, TAG,
            \`Failed to obtain the window properties. Cause code: ${exception.code}, message: ${exception.message}\`);
        }
      })
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/kN-eNSNKQaORLX3_-tOTcQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062550Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=395C6E5D3F02345D828D86C329F946540E0A41CC0CBB1BEE2D7AFCC94AC7BC75)
    
    Screen brightness. The value is a floating point number in the range \[0.0, 1.0\], and the value **1.0** means the brightest. If no value is passed, the brightness follows the system. In this case, the obtained brightness value is **\-1**.
    
3.  Use the [setWindowBrightness()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#setwindowbrightness9) method provided by the window instance to set the screen brightness.
    
    Button('Set screen brightness')
      .width(328)
      .onClick(() => {
        try {
          this.windowBrightness = Math.random() \* (1.0 - 0.0) + 0.0;
          if (this.windowBrightness < 0 || this.windowBrightness > 1) {
            hilog.error(0x0000, TAG, \`WindowBrightness is not within the valid range\`);
            return;
          }
          this.windowClass?.setWindowBrightness(this.windowBrightness, (err: BusinessError) => {
            const errCode: number = err.code;
            if (errCode) {
              hilog.error(0x0000, TAG,
                \`Failed to set the brightness. Cause code: ${err.code}, message: ${err.message}\`);
              return;
            }
            hilog.info(0x0000, TAG, 'Succeeded in setting the brightness.');
          });
        } catch (exception) {
          hilog.error(0x0000, TAG,
            \`Failed to set the brightness. Cause code: ${exception.code}, message: ${exception.message}\`);
        }
      })
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/0xaLz-eSTzqFewh9W67RXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062550Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9D885F5DFCC658DF97D848B3DFCE0BBDAB0DD22BCADF95F49C45DEDB42BECE4)
    
    The screen brightness set by this API takes effect only in the application and does not affect the screen brightness of the system.
    

**Reference**

[@ohos.settings (Data Item Settings)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-settings)
