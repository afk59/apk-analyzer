# Window Metadata Configuration

#### metadata

The **metadata** tag represents custom metadata of a HAP. The tag value is an array and contains three subtags: **name**, **value**, and **resource**.

**Table 1** metadata tag description

| Subtag | Description | Data Type | Optional |
| :-- | :-- | :-- | :-- |
| name | Name of the data item. The value is a string with a maximum of 255 bytes. | String | Optional, defaults to an empty array |
| value | Value of the data item. The value is a string with a maximum of 255 bytes. | String | Optional, defaults to an empty array |
| resource | Custom data, which is a resource index. The value is a string with a maximum of 255 bytes. For example, **$profile:shortcuts\_config** indicates that the data points to the **/resources/base/profile/shortcuts\_config.json** file. | String | Optional, defaults to an empty array |

Below are several use cases and examples for the **metadata** tag. You can customize the settings based on service requirements.

1.  Use the **metadata** tag to configure the default size and position (in vp) of the main window. The following **name** options are available:
    
    -   **ohos.ability.window.height**: specifies the default height of the main window. **value** indicates the height.
    -   **ohos.ability.window.width**: specifies the default width of the main window. **value** indicates the width.
    -   **ohos.ability.window.left**: specifies the default left position of the main window. **value** indicates the configuration format: alignment mode +/- offset. The alignment mode can be **center**, **left**, or **right**. The default value is **left**. It can be omitted when the offset is **0**.
    -   **ohos.ability.window.top**: specifies the default top position of the main window. **value** indicates the configuration format: alignment mode +/- offset. The alignment mode can be **center**, **top**, or **bottom**. The default value is **top**. If both the alignment mode and offset are omitted, the default stacking specifications are used.
2.  Use the **metadata** tag to configure the enabled status of the [removeStartingWindow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-windowstage#removestartingwindow14) API. Set **name** to **enable.remove.starting.window**, and set **value** to **true** to enable the API, or to **false** to disable it. The default value is **false**.
    
3.  Use the **metadata** tag to configure whether the main window is maximized upon startup. Set **name** to **ohos.ability.window.isMaximize**, and set **value** to **true** to maximize the main window upon startup, or to **false** to start in a non-maximized state. The default value is **false**. This configuration has the following restrictions:
    
    -   The configuration takes effect only on PCs/2-in-1 devices.
    -   If the **supportWindowModes** property in [startOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-startoptions) is used, the **FULL\_SCREEN** option must be configured. In this case, the **metadata** tag can be used to configure the main window to start in maximized mode; otherwise, it does not take effect.
    -   If the **supportWindowMode** property in the [module.json5](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#abilities) file is used, the **fullscreen** option must be configured. In this case, the **metadata** tag can be used to configure the main window to start in maximized mode; otherwise, it does not take effect.
    -   The priorities of the main window display settings are as follows: full-screen display > using [startOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-startoptions) to specify the size and position > using [setWindowRectAutoSave()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-windowstage#setwindowrectautosave14) to enable window size memory > using the **metadata** tag to configure maximization > using the **metadata** tag to configure the size and position. You can configure full-screen display in any of the following ways:
        1.  Set the **windowMode** property in [startOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-startoptions) to **WINDOW\_MODE\_FULLSCREEN**.
        2.  Set the **supportWindowModes** property in [startOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-startoptions) only to **FULL\_SCREEN**.
        3.  Set the **supportWindowMode** property in [module.json5](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#abilities) only to **fullscreen**.
4.  Use the **metadata** tag to configure the supported window modes in [free windows](https://developer.huawei.com/consumer/en/doc/design-guides/pad-0000001823654157#section1768267204717) mode. Set **name** to **ohos.ability.window.supportWindowModeInFreeMultiWindow**, and set **value** to **fullscreen** (full-screen mode), **split** (split-screen mode), **floating** (floating window mode), or any of their combinations (separated by commas, with no space), for example, **fullscreen,split**. This configuration takes effect only on a device that supports [freeform windows](../window-development-terminology/document.md#freeform-window) and is in the freeform window state. If the device supports freeform windows but is not in the freeform window state, or if the device does not support freeform windows, this configuration does not take effect and no error is reported.
    
    In free windows mode, the supported window modes can be configured using multiple methods. The configuration priorities are as follows: using [SetSupportedWindowModes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-windowstage#setsupportedwindowmodes15) to configure the window modes > using **StartAbility** to configure the **SupportWindowMode** property in [StartOption](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-startoptions#startoptions) > using the **metadata** tag to configure the window modes > configuring the **SupportWindowMode** property in the [abilities tag](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#abilities) of the **module.json5** file.
    
    In non-free windows mode, only the **SupportWindowMode** property in the **abilities** tag of the **module.json5** file can be used to configure the window modes. Other methods do not take effect.
    

{
  "module": {
    "abilities": \[{
      "metadata": \[{
        "name": "ability\_metadata",
        "value": "a test demo for ability",
        "resource": "$profile:config\_file"
      },
      {
        "name": "ability\_metadata\_2",
        "value": "a string test",
        "resource": "$profile:config\_file"
      },
      {
        "name": "ohos.ability.window.height",
        "value": "987"
      },
      {
        "name": "ohos.ability.window.width",
        "value": "1300"
      },
      {
        "name": "ohos.ability.window.left",
        "value": "right-50"
      },
      {
        "name": "ohos.ability.window.top",
        "value": "center+50"
      },
      {
        "name": "ohos.ability.window.isMaximize",
        "value": "true"
      },
      {
        "name": "enable.remove.starting.window",
        "value": "true"
      }
      {
        "name": "ohos.ability.window.supportWindowModeInFreeMultiWindow",
        "value": "fullscreen,split,floating",
      }\],
    }\],

    "extensionAbilities": \[{
      "metadata": \[{
        "name": "extensionAbility\_metadata",
        "value": "a test for extensionAbility",
        "resource": "$profile:config\_file"
      },
      {
        "name": "extensionAbility\_metadata\_2",
        "value": "a string test",
        "resource": "$profile:config\_file"
      }\],
    }\]
  }
}
