# Adding or Deleting a Module

As a basic functional unit of apps/atomic services, a module contains source code, resource files, third-party libraries, and configuration files. You can create one or more modules in a project. Four types of modules are supported: entry, feature (supported only in app projects), har, and shared. For details, see [module.json5 Configuration File](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#tags-in-the-configuration-file).

Since DevEco Studio 6.0.1 Beta1, you can specify the C++ language standard when creating a native C++ module or library template.

#### Creating a Module

1.  Perform any of the following:
    
    -   Method 1: Right-click the top of the project directory and choose **New** > **Module** from the shortcut menu. The new module will be created in the root directory of the project.
    -   Method 2: Select any file in the project directory and choose **File** > **New** > **Module** on the menu bar. The new module will be created in the root directory of the project.
    -   Method 3: Create a directory in the root directory of the project. Right-click the directory and choose **New** > **Module** from the shortcut menu. The new module will be created in that directory.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/Z-U5dzjNQ5qlmIvyKqxH-Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C1DB17F8AC4567984181996661BFFC8F129A2FAA3B0492CEEAF0F3E61F87EBA9)
        
        Method 3 is not applicable to the following directories: **AppScope**, **hvigor**, **oh\_modules**, **build**, and directories starting with a period (such as **.hvigor** and **.idea**).
        
    
2.  On the **New Project Module** page, select a template and click **Next**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/BU4OrjL9Szyt9pHlL9gy4w/en-us_image_0000002500910194.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5477C03129640ECBB9D6293D1BB02D334F8857D3729F979820146774B62A9E69)
    
3.  Configure the module settings and click **Next**. Since DevEco Studio 6.0.1 Beta1, you can specify the C++ language standard for your project.
    
    -   **Module name**: name of the new module. It must be different from the project name or the name of another module in the project.
    -   **Module type**: module type, which can be **feature** or **entry**. This field is only available in an ability template.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/jvUJfC2HS5mKX2aLl-tGxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF46F86565E98047F9F017EDE7E978AE07AB43BD4205F66B6636C8C748100C96)
        
        -   Only one entry module can be added for a project. Yet, you can change the module type of an existing module to entry through the **config.json5** file.
        -   If a type of device already has an entry module, you must [configure distribution rules](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#distributionfilter) for a new entry module.
        
    -   **Device type**: device type of the module. If **Module type** is set to **feature**, you can only select the device type specified for the project. If **Module type** is **entry**, you can select any supported device types.
    -   **Enable native**: whether to enable native code. This field is only available in a library template. With native code enabled, you can create a shared module for invoking C++ code.
    -   **C++ Standard**: C++ standard library, which can be **Toolchain Default**, **C++11**, or **C++14**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/2aFQZLyTT8KX2QIHE8dggQ/en-us_image_0000002500910190.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA6197028BC594DDA74FAA03C875E11398CCEA7E483C8F2FE20DF52836F1D086)
    
4.  If the module is using an ability template, also set **Ability name** and **Exported** (or **Visible** in the FA model).
    
    -   When **Exported** (or **Visible**) is selected, the ability can be called by other apps/atomic services.
    -   When **Exported** (or **Visible**) is not selected, other apps/atomic services cannot call the ability.
    
5.  Click **Finish**. After the module is created, you can view and edit the new module in the project directory. You can configure settings for modules in the project through the **modules** field in the [build-profile.json5](../../../../building-an-app/configuration-files/project-level-build-profile-json5-file/document.md) file.

#### Importing or Referencing a Module

You can import a module from another project in either of the following ways:

1.  Copy the feature code of other HarmonyOS modules to the current project by using the [Import Module](#section13771399184) feature. Currently, only modules of the FA model can be imported into projects of the FA model, and only modules of the stage model can be imported into projects of the stage model.
2.  Configure the relative path under the [srcPath](#section12961144312265) field to reference a module from another project. This method only references the module information but does not copy the module code to the local project. Currently, the HAR and HSP modules from other projects can be referenced.

## Using Import Module

1.  On the menu bar, choose **File** > **New** > **Import...** > **Import Module**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/-TNRfBRBTIetOAQnlTwkiw/en-us_image_0000002501070034.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=862D01727DD4624140BDA9CDED9853E2CC5CE7BECA95225A4E2E53454B7476D5)
    
2.  Select the module to import.
    
    Select the path to the module, which can be The module to import can be a folder or a .zip file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/n2bxCeClSjqIHn2aEGbE0Q/en-us_image_0000002532670107.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88A9756998B47F816076FE2E357508BFACADB2F89A62697A18F72B76A15955DC)
    

## Using SrcPath

In the project-level **build-profile.json5** file, configure the relative path of the module outside the project under the **modules** > **srcPath** field, as shown in the following figure. The module information is referenced, but the module code is not copied to the project. Currently, the HAR and HSP modules from other projects can be referenced.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/HfjtHQ_LSs2xAG8JhSfLiA/en-us_image_0000002532670111.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=795F17A78FFB986A655080E3741A90BBBAA9970B8A852AE43352ED033150361D)

#### Deleting a Module

Right-click the module to delete in the project directory, and choose **Delete** from the shortcut menu. When prompted, click **Delete**.
