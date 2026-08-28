# Creating a Project

Before starting to develop an app/atomic service, you must create a project. DevEco Studio will automatically create sample code and a resource template depending on the type of your project.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/_YOWH8AVQ9yRziIxwd0J6A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FC11E98BC7C92FB8C1158EF807E280FAEC9B29BC7E51FF28F08B06A2DA2EA7A)

When running a project, it is recommended that each running window have more than 2 GB available memory space.

#### Creating and Configuring a Project

When you are ready to start a new project, DevEco Studio has a variety of templates that support different devices and API versions. It would be helpful to check out the specifics of each template to find the one that fits your needs best. For details, see [Introduction to Project Templates](../introduction-to-project-templates/document.md).

Since DevEco Studio 6.0.1 Beta1, you can specify the C++ language standard for native C++ projects during creation.

## Creating a HarmonyOS Project

1.  Open the project wizard using either of the following methods:
    
    -   If no project is open, select **Create Project** on the welcome page.
    -   If a project is already open, choose **File** > **New** > **Create Project** on the menu bar.
    
2.  Following the project creation wizard, select **Application** or [Atomic Service](https://developer.huawei.com/consumer/en/doc/atomic-guides/atomic-service-create-project). Select an ability template and click **Next**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/XOe-jl_jSBeXIWGpJIjYAw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2EC63697E569A44911EC2C35DB0C637B0C57AE7F80A5756E36F63136266F5EE)
    
    -   Atomic service projects are supported since API version 11.
    -   Atomic service projects do not support development in C++.
    -   Currently, \[CloudDev\]Empty Ability is available only in the Chinese mainland.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/7UvMLYm6SdiVjfKCxlqTbA/en-us_image_0000002502714490.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C56AD05C406DF98CBA831E9784817E84CD09402988327E3358DBFE0D617C57B)
    
3.  On the project configuration page, set the basic project information.
    
    -   **Project name**: name of the project. It can be customized and must start with a letter. The value is a string of 1 to 200 characters, including uppercase letters, lowercase letters, digits, and underscores (\_).
    -   **Bundle name**: bundle name of the app/atomic service, which uniquely identifies the app/atomic service.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/Rb93UFMjQwmttkv6vaZCdg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF73E9D9DA688A2DDC6EDAB9AF1A0E69E8AD09EDAC8F3A925B2F654662913AD3)
        
        A bundle name must meet the following requirements:
        
        -   The bundle name contains at least three segments, separated by periods (.). Each segment can contain only letters, digits, and underscores (\_). Example: **com.example.myapplication**.
        -   The first segment starts with a letter, and other segments start with a digit or letter. Each segment ends with a digit or letter. Example: **com.01example.myapplication**.
        -   Consecutive periods (.) are not allowed, for example, **com.example..myapplication**.
        -   The bundle name contains 7 to 128 characters.
        
    -   **Save location**: path for storing project files. The path consists of uppercase letters, lowercase letters, digits, and underscores (\_).
    -   **Compatible SDK**: the earliest compatible API version.
    -   **Module name**: name of the module.
    -   **Device type**: device type supported by the project template. For details about device types, see [deviceTypes](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#devicetypes).
    -   **C++ Standard**: C++ standard library, which can be **Toolchain Default**, **C++11**, or **C++14**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/ey4WJ5xlR8O_DiDICgO09A/en-us_image_0000002502555148.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C1F74C5AD515DD2C3B3703D0ADD373C10741498E64A19BECB33DE756601F6B4B)
    
4.  Click **Finish**. DevEco Studio will automatically generate the sample code and resources that match your project type. Wait until the project is created.

## (Optional) Creating an OpenHarmony Project

To create an OpenHarmony project for application development, perform the following steps:

1.  After [creating a HarmonyOS project](#section11644183711342), perform the following operations in the project-level **build-profile.json5** file:
    
    1.  Add the **compileSdkVersion** field.
    2.  Set the **compatibleSdkVersion**, **compileSdkVersion**, and **targetSdkVersion** (if any) fields to numeric values.
    3.  Change the **runtimeOS** field from **HarmonyOS** to **OpenHarmony**.
    
    "products": \[
      {
        "name": "default",
        "signingConfig": "default", 
        "compileSdkVersion": 22,    // Set the SDK version for building the OpenHarmony app, for example, 22 in this case.
        "targetSdkVersion": 22,     // Set the target SDK version for running the OpenHarmony app, for example, 22 in this case.
        "compatibleSdkVersion": 22, // Set the earliest SDK version compatible with the OpenHarmony app, for example, 22 in this case.
        "runtimeOS": "OpenHarmony",
      }
    \],
    
2.  Click **Sync Now** to start synchronization. In the **Sync Check** dialog box, click **Yes** to switch the **phone** type in the **module.json5**/**config.json** file to the **default** type and delete other device types that are not applicable to OpenHarmony. The project is created once the synchronization is successful with no errors.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/E8OmjUY2RNSmS5bIfgdNVQ/en-us_image_0000002500910214.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=29FB5EA0690E18FDACD3A1F883A4E4BC366DD365000A7EDC7E018F0BB286ABCC)
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/bsSDOHMnSuyx9dEoUIr_8A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56A28E4E36037C5041DCACDC5284E77A0829E69B8B3A76F78014BC02E1B4A94C)

If you are creating an OpenHarmony project using a native C++ template, to enable your app to run on RK development boards, add **"abiFilters": "armeabi-v7a"** to **buildOption**/**externalNativeOptions** in the **build-profile.json5** file of the corresponding native module.
