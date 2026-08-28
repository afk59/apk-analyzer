# How do I implement automatic screen rotation for applications?

1.  Add **"orientation": "auto\_rotation"** to the **module.json5** file.
    
    Refer to the code snippet below.
    
    "abilities": \[
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ets",
        "description": "$string:EntryAbility\_desc",
        "icon": "$media:icon",
        "label": "$string:EntryAbility\_label",
        "startWindowIcon": "$media:startIcon",
        "startWindowBackground": "$color:start\_window\_background",
        "exported": true,
        "skills": \[
          // ...
        \],
        "orientation": "auto\_rotation", // Rotate with the sensor
      }
    \],
    
2.  Enable the automatic rotation feature of the phone. The procedure is as follows: Swipe down from top to access Control Panel, and disable **Orientation lock**.

**Reference**

[abilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities)
