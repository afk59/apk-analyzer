# Adapting the Dark and Light Modes

When your app needs to dynamically switch themes based on device dark/light mode changes, you can use the **onConfigurationUpdate** callback of **UIAbility** to detect mode changes and then set font and background colors accordingly.

#### API Description

This function involves one API. See the following table for detailed API information.

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[setPageConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/reader-read-core#section6297758718)(pageConfig: ReaderSetting): void

 | 

Sets or modifies page typesetting attributes.

 |

#### Preparations

Before adapting the dark and light modes, ensure that you have [built a reader](../../building-a-reader/document.md).

#### Development Procedure

1.  Listen to the **onConfigurationUpdate** callback of **UIAbility**, and save the value of **colorMode** to [AppStorage](../../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/ui-paradigm-state-management/state-management-v1/application-state-management/appstorage-storing-application-wide-ui-state/document.md) that manages the app-level variable status.
    
    import { Configuration, UIAbility } from '@kit.AbilityKit';
    
    export default class EntryAbility extends UIAbility {
    
      onConfigurationUpdate(newConfig: Configuration): void {
        AppStorage.setOrCreate('colorMode', newConfig.colorMode);
      }
    }
    
2.  Use the [@StorageLink](../../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/ui-paradigm-state-management/state-management-v1/application-state-management/appstorage-storing-application-wide-ui-state/document.md#storagelink) decorator to listen to the **colorMode** value changes. If the value changes, trigger the change of the theme color accordingly.
    
    import { ConfigurationConstant } from '@kit.AbilityKit';
    
    @StorageLink('colorMode') @Watch('colorModeChange') colorMode: ConfigurationConstant.ColorMode =
      ConfigurationConstant.ColorMode.COLOR\_MODE\_NOT\_SET;
    
    /\*\*
     \* Change the theme accordingly when the system dark mode changes.
     \*/
    colorModeChange() {
      if (this.colorMode === ConfigurationConstant.ColorMode.COLOR\_MODE\_DARK) {
        this.readerSetting.nightMode = true;
        this.readerSetting.fontColor = '#ffffff';
        this.readerSetting.themeColor = '#202224';
      } else {
        this.readerSetting.nightMode = false;
        this.readerSetting.fontColor = '#000000';
        this.readerSetting.themeColor = '#FFFFFF';
      }
      this.readerComponentController.setPageConfig(this.readerSetting);
    }
