# Configuring an Application Icon and Label

This topic describes how to configure the application icon and label. Application icons are classified into single-layer icons and layered icons. A single-layer icon contains only one image, and a layered icon contains a foreground image and a background image. For details about icon specifications, see [Icon Deliverables](https://developer.huawei.com/consumer/en/doc/design-guides/application-icon-0000001953444009#section634668113212). For details about the restrictions on icon and label configuration, see [Configuring the Application Icon and Label](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/application-or-component-level-configuration-stage-model/document.md#configuring-the-application-icon-and-label).

#### Use Scenarios

-   Used to display an application on the home screen, for example, applications displayed on the home screen or in recent tasks.
-   Used to display an application on an application screen, for example, application list in Settings.
-   Used to display an application that sends a notification in the notification panel.

The display effects are as follows.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/_Gqq7BVaR9uLjEcmnhzkUg/en-us_image_0000002537924276.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF1A1BB05030C0BB8C1F758284AB7B0DF2350EF88703BC4E1D66F368C79D7B01)

#### Configuration Priority and Build Policy

-   For the HAP file containing UIAbility configuration, the following scenarios are possible:
    
    -   If the **icon** and **label** fields under **abilities** of the [module.json5 file](../../application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) are configured, and under **skills** of the corresponding ability, **entities** contains **entity.system.home** and **actions** contains **ohos.want.action.home**, the system returns the **icon** and **label** configured in the **module.json5** file. If there are multiple abilities that meet the requirements, the system returns the icon and label specified for the ability corresponding to **mainElement** in **module.json5**.
        
    -   If the **icon** and **label** fields under **abilities** of the **module.json5** file are not configured, the system returns the **icon** and **label** configured in [app.json5](../../application-configuration-files-in-stage-model/app-json5-configuration-file/document.md).
        
-   For the HAP file that does not contain UIAbility configuration, the system returns the **icon** and **label** configured in **app.json5**.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/oYulKvyjRR-gzQFws9wThw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31ADE88B616CEA146BEB04B95623EAA96C0892F263775AB3FD94BB6AE6F80676)

The resource files in the **AppScope** directory are merged into the **resources** directory of the module. If files with the same name exist in these two directories, the ones in the **AppScope** directory will overwrite those in the module after build and packaging.

For example, if the labels of the layered icon files configured in **app.json5** and **module.json5** are the same but the icons are different, the resource files in the **AppScope** directory overwrite those in the module. Finally, the icon configured in **app.json5** is used.

If no entry UIAbility is set in the application configuration, the application details page is displayed after you tap the application icon on the home screen. Alternatively, go to **Settings** > **Apps & services**, and tap any application to access the application details page. In other cases, the application main page is displayed after you tap the application icon on the home screen. An application does not have an entry UIAbility in either of the following scenarios:

1.  The application does not have any UIAbility.
2.  Under the **skills** tag in all **UIAbility** configurations, **entities** is not set or does not contain **entity.system.home**, and **actions** is not set or does not contain **ohos.want.action.home**.

#### Configuring a Single-Layer Icon and Label

-   **Method 1: Configuring app.json5**
    
    This configuration takes effect only when the **module.json5** configuration file does not contain any UIAbility or **icon** and **label** under the **abilities** tag of the UIAbility are not set. (You can manually delete the icon and label configurations).
    
    {
      "app": {
        // ...
        "icon": "$media:app\_icon",
        "label": "$string:app\_name" // Configure the resource whose name is app\_name in AppScope/resources/base/element/string.json. If the resource already exists, skip this step.
      }
    }
    
-   **Method 2: Configuring module.json5**
    
    In addition to configuring the **icon** and **label** fields, you also need to add **entity.system.home** to **entities** and **ohos.want.action.home** to **actions** under the **skills** tag.
    
    {
      "module": {
        // ...
        "abilities": \[
          {
            // ...
            "icon": "$media:icon",
            // Configure the resource whose name is EntryAbility\_label in entry/src/main/resources/base/element/string.json. If the resource already exists, skip this step.
            "label": "$string:EntryAbility\_label",
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
        // ...
      }
    }
    

#### Configuring a Layered Icon and Label

-   **Method 1: Configuring app.json5**
    
    This configuration takes effect only when the **module.json5** configuration file does not contain any UIAbility or **icon** and **label** under the **abilities** tag of the UIAbility are not set. (You can manually delete the icon and label configurations).
    
    1.  Place the foreground and background resource files in **AppScope\\resources\\base\\media**.
        
        In this example, the file names of the foreground and background resource files are **foreground.png** and **background.png**, respectively.
        
    2.  In the **app\_layered\_image.json** file under the **AppScope\\resources\\base\\media** directory, configure the foreground and background resources of the layered icon.
        
        {
          "layered-image":
          {
            "background" : "$media:background",
            "foreground" : "$media:foreground"
          }
        }
        
    3.  Reference the layered icon resource file in the [app.json5](../../application-configuration-files-in-stage-model/app-json5-configuration-file/document.md) file. Example:
        
        {
          "app": {
            // ...
            "icon": "$media:layered\_image",
            "label": "$string:app\_name" // Configure the resource whose name is app\_name in AppScope/resources/base/element/string.json. If the resource already exists, skip this step.
          }
        }
        
-   **Method 2: Configuring module.json5**
    
    1.  Place the foreground and background resource files in **entry\\src\\main\\resources\\base\\media**.
        
        In this example, the file names of the foreground and background resource files are **foreground.png** and **background.png**, respectively.
        
    2.  In the **layered\_image.json** file under the **entry\\src\\main\\resources\\base\\media** directory, configure the foreground and background resources of the layered icon.
        
        {
          "layered-image":
          {
            "background" : "$media:background",
            "foreground" : "$media:foreground"
          }
        }
        
    3.  If you need to display a **UIAbility** icon on the home screen, in addition to configuring the **icon** and **label** fields, you also need to add **entity.system.home** to **entities** and **ohos.want.action.home** to **actions** under the **skills** tag.
        
        {
          "module": {
            // ...
            "abilities": \[
              {
                // ...
                // Set icon to the index of the layered icon resource file.
                "icon": "$media:layered\_image",
                // Configure the resource whose name is EntryAbility\_label in entry/src/main/resources/base/element/string.json. If the resource already exists, skip this step.
                "label": "$string:EntryAbility\_label",
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
            // ...
          }
        }
        

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/QSxntAPkR2y-VMlRSJhNwg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B61D2A0D48A894B92B91FA8D6D0B9FD1BC638BD73FE8FFAA183615907C261FEE)

Since DevEco Studio 5.0.3.814, the default template contains the layered icon resource file when an application is created. The name of the resource file generated in different versions may be different. The file name can be manually modified. If the layered icon resource file does not exist, you have to manually create it. The file name must comply with the resource naming rules and can contain only digits, letters, periods (.), and underscores (\_).
