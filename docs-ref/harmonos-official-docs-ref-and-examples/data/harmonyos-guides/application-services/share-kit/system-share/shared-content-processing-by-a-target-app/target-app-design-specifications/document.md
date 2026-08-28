# Target App Design Specifications

This section describes the design specifications for the target app integrated with the system sharing panel. For details, please refer to [Design - Sharing Mode Area](https://developer.huawei.com/consumer/en/doc/design-guides/share-0000001957076313#section132401520173711).

#### App Name and Icon Specifications

After implementing the [UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability) or [UIExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiextensionability) for receiving the shared content in your target app, you can register the supported shared data types in the [skills](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#skills) section of the configuration file (**src/main/module.json5**), and set **actions** to **ohos.want.action.sendData**.

If the shared content type is supported by the target app, the target app's icon will appear in the sharing mode area of the sharing panel.

You can set different names and icons for different abilities.

Example:

"abilities": \[
  {
    "name": "TestUIAbility",
    "srcEntry": "./ets/entryability/TestUIAbility.ets",
    "label": "$string:EntryAbility\_label", // Ability name.
    "icon": "$media:layered\_image", // Ability icon.
    "description": "$string:EntryAbility\_desc",
    "startWindowIcon": "$media:startIcon",
    "startWindowBackground": "$color:start\_window\_background",
    "exported": true,
    "skills": \[
      {
        "actions": \[
          "ohos.want.action.sendData"
        \],
        "uris": \[
          {
            "scheme": "file",
            "utd": "general.text",
            "maxFileSupported": 1
          }      
        \]
      }
    \]
  }
\],
"extensionAbilities": \[  
  {
    "name": "TestShareAbility",
    "srcEntry": "./ets/abilities/TestShareAbility.ts",
    "type": "share", // Support the processing of shared data.
    "exported": true,
    "label": "$string:xx\_label", // Ability name.
    "icon": "$media:icon", // Ability icon.
    "description": "$string:TestShareAbility\_desc",
    "skills": \[
      {
        "actions": \[
          "ohos.want.action.sendData"
        \],
        "uris": \[
          {
            "scheme": "file",
            "utd": "general.text",
            "maxFileSupported": 1
          }
        \]
      }
    \]
  }
\]
