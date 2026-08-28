# Creating a Static Shortcut of the Application

With applications getting more feature-packed, it becomes tougher for users to find and use specific features. To make things smoother, you can create home screen shortcuts for popular features in your application, allowing for quick application launch and direct access to these features. Typical feature shortcuts include "Quick Photo" in camera applications, "Create Note" in note applications, and frequently used location navigation in map applications. All of these shortcuts enable users to quickly access specific feature pages, greatly improving operation efficiency and making users more reliant on the application. You can also create shortcuts to meet personalized workflow and preference needs. For details about how to configure shortcuts, see [How to Configure](#how-to-configure). For details about shortcut management, see [shortcutManager Module](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-shortcutmanager).

#### When to Use

This topic uses navigation as an example. When using a map application for navigation, users tend to search for a destination and then start navigation. To make this process more efficient and user-friendly, you can add navigation shortcuts for regular destinations like company or home for the map application. With these shortcuts, users can quickly start navigation by long pressing the application. For details, see [Home Screen Shortcuts](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-desktop-shortcuts).

#### How to Configure

The following describes how to configure a static shortcut in a project.

1.  Add the following content to the **entry/src/main/resources/base/element/string.json** file:
    
    {
      "string": \[
        {
          "name": "share",
          "value": "Share"
        },
        {
          "name": "add",
          "value": "Favorites"
        }
      \]
    }
    
2.  Configure the shortcut file.
    
    Add the [shortcut configuration file](../../application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#shortcuts), for example, **shortcuts\_config.json**, to the **/resources/base/profile/** directory of the module.
    
    {
      "shortcuts": \[
       {
          "shortcutId": "id\_test1",
          "label": "$string:add",
          "icon": "$media:add\_icon",
          "wants": \[
            {
              "bundleName": "com.ohos.hello",
              "moduleName": "entry",
              "abilityName": "EntryAbility1",
              "parameters": {
                "testKey": "testValue"
              }
            }
          \]
        },
        {
          "shortcutId": "id\_test2",
          "label": "$string:share",
          "icon": "$media:share\_icon",
          "wants": \[
            {
              "bundleName": "com.ohos.hello",
              "moduleName": "entry",
              "abilityName": "EntryAbility",
              "parameters": {
                "testKey": "testValue"
              }
            }
          \]
        }
      \]
    }
    
3.  Configure **metadata** in the **module.json5** file of the application, which points to the shortcut file.
    
    {
      "module": {
        // ...
        "abilities": \[
          {
            "name": "EntryAbility",
            "srcEntry": "./ets/entryability/EntryAbility.ets",
            "metadata": \[
              {
                "name": "ohos.ability.shortcuts",  // Configure a shortcut. The value is fixed at ohos.ability.shortcuts.
                "resource": "$profile:shortcuts\_config"  // Specify the resources of the shortcuts.
              }
            \],
            // ...
          }
        \],
        // ...
      },
    }
    

After installing the application, long press the icon on the home screen. The shortcuts (**Favorites** and **Share**) configured by you are displayed above the application icon. Tap a label to start the corresponding component. The following figure shows a static shortcut of an application displayed on the home screen.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/3vQOyrD5TJu6zXz2mDHqcg/en-us_image_0000002537764334.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FCCE3B907567C62B736F9D638A46C211E1EE738B2ED1F29E7EDF531B2618021)

#### Hiding Shortcuts

You can use the [setShortcutVisibleForSelf](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-shortcutmanager#shortcutmanagersetshortcutvisibleforself) API to hide or display shortcuts.
