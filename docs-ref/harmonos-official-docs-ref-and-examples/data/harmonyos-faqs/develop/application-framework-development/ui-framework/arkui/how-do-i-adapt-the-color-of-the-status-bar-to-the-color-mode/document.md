# How do I adapt the color of the status bar to the color mode?

**Symptom**

In dark mode, the color contrast between the status bar color and the background color is insufficient, making it difficult to read the content.

**Solution**

1.  Define the status bar background color for light mode in **base/element/color.json**.
2.  Define the status bar background color for dark mode in **dark/element/color.json**.
3.  Listen for the switching between color modes.
4.  After detecting color mode switching, set the status bar font color using [setWindowSystemBarProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#setwindowsystembarproperties9).

For details about dark mode adaptation, see [Dark Mode Adaptation](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-dark-mode-adaptation#section128661451172714).

The code snippet is as follows:

1.  Define the color resources for dark and light modes.
    
    // resources/dark/element/color.json
    {
      "color": \[
        {
          "name": "status\_bar",
          "value": "#000000"
        }
      \]
    }
    
    // resources/base/element/color.json
    {
      "color": \[
        {
          "name": "status\_bar",
          "value": "#FFFFFF"
        }
      \]
    }
    
2.  Cache the window object and the current color mode for later use with the [setWindowSystemBarProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#setwindowsystembarproperties9) API to set the status bar properties.
    
    // EntryAbility.ets
    
    
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
      hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
      // Cache the color mode of the current device
      AppStorage.setOrCreate('currentColorMode', this.context.config.colorMode);
    }
    
    
    onWindowStageCreate(windowStage: window.WindowStage): void {
      // Main window is created, set main page for this ability
      hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    
    
      windowStage.loadContent('pages/Index', (err) => {
        if (err.code) {
          hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
          return;
        }
        hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
        let windowClass: window.Window = windowStage.getMainWindowSync(); // Get the main application window
        // 1. Set the window to full screen
        let isLayoutFullScreen = true;
        windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
        // 2. Cache window object
        AppStorage.setOrCreate('windowClass', windowClass);
      });
    }
    
3.  Update the cached color mode when the color mode changes.
    
    // EntryAbility.ets
    
    // Listen for system configuration changes.
    onConfigurationUpdate(newConfig: Configuration): void {
      let newColorMode = newConfig.colorMode;
      let currentColorMode = AppStorage.get<ConfigurationConstant.ColorMode>('currentColorMode');
      if (newColorMode === currentColorMode) {
        return;
      }
      // Update the cached color mode.
      AppStorage.setOrCreate('currentColorMode', newConfig.colorMode);
    }
    
4.  Listen for color mode changes on the page and change the status bar font color if the mode changes.
    
    import { window } from '@kit.ArkUI';
    import { ConfigurationConstant } from '@kit.AbilityKit';
    
    
    @Entry
    @Component
    struct SysDarkMode {
      @State message: string = 'page layout';
      @StorageProp('currentColorMode') @Watch('onColorModeChange') currentColorMode: number =
        ConfigurationConstant.ColorMode.COLOR\_MODE\_LIGHT;
    
      aboutToAppear(): void {
        this.onColorModeChange();
      }
    
      onColorModeChange(): void {
        // Get the current application window
        let windowClass = AppStorage.get<window.Window>('windowClass') as window.Window;
    
    
        if (this.currentColorMode === ConfigurationConstant.ColorMode.COLOR\_MODE\_LIGHT) {
          // Currently in light color mode
          //Set the font to black
          windowClass.setWindowSystemBarProperties({
            // Status bar text color
            statusBarContentColor: '#000000'
          });
        } else if (this.currentColorMode === ConfigurationConstant.ColorMode.COLOR\_MODE\_DARK) {
          // Currently in dark mode
          //Set the font to white
          windowClass.setWindowSystemBarProperties({
            // Status bar text color
            statusBarContentColor: '#FFFFFF'
          });
        } else {
          console.warn("Unsupported color mode")
        }
      }
    
      build() {
        Column() {
          Row()
            .width('100%')
            .height(100)
            .backgroundColor($r('app.color.status\_bar'))
          // page layout
          Text(this.message)
            .fontSize(50)
            .fontColor(Color.Red)
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
            .layoutWeight(1)
        }
        .height('100%')
        .width('100%')
      }
    }
