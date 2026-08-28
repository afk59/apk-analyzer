# How do I disable the full-screen display of a window?

You can configure the **supportWindowMode** field under **abilities** in the **module.json5** file to specify the display mode of the window.

**fullscreen** means full-screen display, **split** means split-screen display, and **floating** means window-based display.

Refer to the code snippet below.

"abilities": \[
  {
    "name": "EntryAbility",
    "srcEntry": "./ets/entryability/EntryAbility.ets",
    "description": "$string:EntryAbility\_desc",
    "icon": "$media:icon",
    "label": "$string:EntryAbility\_label",
    "startWindowIcon": "$media:icon",
    "startWindowBackground": "$color:start\_window\_background",
    "exported": true,
    "supportWindowMode": \["split", "floating"\],
    "skills": \[
      {
        "entities": \[
          "entity.system.home"
        \],
        "actions": \[
          "ohos.want.action.home"
        \]
      }
    \]
  }
\],

**Reference**

[abilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities)
