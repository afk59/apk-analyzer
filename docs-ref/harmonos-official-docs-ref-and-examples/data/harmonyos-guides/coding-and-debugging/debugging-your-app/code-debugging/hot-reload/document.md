# Hot Reload

DevEco Studio provides the hot reload feature, which allows you to quickly see the effects of code changes of an app running or debugged on a real device or the Emulator without having to restart the app.

Hot reload supports most code modification scenarios. However, some special scenarios require restarting the app after hot reload to make the changes take effect. Therefore, DevEco Studio provides an enhanced capability based on hot reload—hot restart. [With hot restart enabled](#section1724105718289), DevEco Studio automatically switches to hot restart for scenarios that do not support hot reload.

The hot restart feature is supported since DevEco Studio 5.1.1 Beta1.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/eMVilHR-RY-AoJuOfmiydg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC524AAAC350A66BC7BED3DC69C3D9FD8EE6CC9A1BC45E837744A5647F382B22)

Hot reload supports the ArkTS projects based on the stage model, but does not support ArkTS widgets. As such, avoid widget-related operations during hot reload.

#### Differences Between Hot Reload, Hot Restart, and Full Restart

-   **Hot reload**: Does not restart the app and preserves app state. However, the entire process re-executes the logic within the entry file.
-   **Hot restart**: Restarts the app, does not preserve the app state, and supports a wider range of ArkTS code modifications to take effect quickly. Once a hot restart is performed, subsequent hot reload operations will be replaced by hot restart.
-   **Full restart**: Completely re-runs the app. This task is time-consuming because it recompiles the code and resource files in full.

#### Constraints

**Table 1** Files that can be modified during hot reload/hot restart
| 
Modified File

 | 

Hot Reload

 | 

Hot Restart

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

ets and ts code files in the Entry module

 | 

Supported

 | 

Supported

 | 

\-

 |
| 

Code files in the HAR module on which the Entry module directly or indirectly depends

 | 

Supported

 | 

Supported

 | 

No HSP exists between the HAR module and the Entry module.

 |
| 

Code files in the HSP module on which the Entry module directly or indirectly depends

 | 

Not supported

 | 

Not supported

 | 

\-

 |
| 

Code files referenced from the HAR module of other projects

 | 

Supported

 | 

Supported

 | 

No HSP exists between the HAR module and the Entry module.

 |
| 

Code files referenced from the HSP module of other projects

 | 

Not supported

 | 

Not supported

 | 

\-

 |
| 

Worker thread files

 | 

Not supported

 | 

Not supported

 | 

\-

 |
| 

Index files in the module directory

 | 

Supported

 | 

Supported

 | 

\-

 |
| 

Code files added after the app is started

 | 

Not supported

 | 

Not supported

 | 

\-

 |
| 

C++ and .so files

 | 

Not supported

 | 

Not supported

 | 

\-

 |
| 

Resource files (for example, the **string.json** file)

 | 

Not supported

 | 

Not supported

 | 

You can modify resource references, for example, the modification from **$r('app.color.greenColor')** to **$r('app.color.redColor')** takes effect quickly.

 |

**Table 2** Code element modifications supported by hot reload/hot restart
| 
Code Element

 | 

Change Type

 | 

Hot Reload

 | 

Hot Restart

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

UI code

 | 

Add, modify, and delete (for example, modifying the font size and color)

 | 

Supported

 | 

Supported

 | 

\-

 |
| 

UI response event

 | 

Add, modify, and delete (for example, adding the **onClick** event)

 | 

Supported

 | 

Supported

 | 

\-

 |
| 

import

 | 

Add

 | 

Partially supported

 | 

Partially supported

 | 

Importing modules from files not loaded at app launch is unsupported.

 |
| 

Modify and delete

 | 

Supported

 | 

Supported

 | 

\-

 |
| 

export

 | 

Add

 | 

Partially supported

 | 

Partially supported

 | 

When adding the **export default** statement, you must add the corresponding **import** statement in the calling file. Otherwise, the operation fails.

 |
| 

Modify and delete

 | 

Supported

 | 

Supported

 | 

\-

 |
| 

Decorators (such as @State and @Prop)

 | 

Add, modify, and delete

 | 

Partially supported

 | 

Partially supported

 | 

Hot reload and hot restart enable the addition, modification, and deletion of @Styles in files decorated with @Entry to take effect.

Hot restart enables the addition, modification, and deletion of @State in files decorated with @Entry to take effect.

 |
| 

**declare** variables

 | 

Add, modify, and delete

 | 

Supported

 | 

Supported

 | 

\-

 |
| 

Struct code block

 | 

Add

 | 

Partially supported

 | 

Supported

 | 

Hot reload enables the addition of Struct code blocks in files except those decorated with @Entry to take effect.

 |
| 

Modify

 | 

Partially supported

 | 

Supported

 | 

Hot reload enables the modification of member variables and member functions in files except those decorated with @Entry to take effect.

 |
| 

Delete

 | 

Supported

 | 

Supported

 | 

\-

 |
| 

Class

 | 

Add

 | 

Partially supported

 | 

Supported

 | 

Hot reload enables the addition of classes containing member functions in files except those decorated with @Entry to take effect.

 |
| 

Modify

 | 

Partially supported

 | 

Supported

 | 

Hot reload enables the modification of classes with member functions added in files except those decorated with @Entry to take effect.

 |
| 

Inherit

 | 

Partially supported

 | 

Supported

 | 

Hot reload supports class inheritance (either inheriting from other classes or being inherited by them) in files except those decorated with @Entry.

 |
| 

Delete

 | 

Supported

 | 

Supported

 | 

\-

 |
| 

APIs

 | 

Add and delete

 | 

Supported

 | 

Supported

 | 

\-

 |
| 

Modify

 | 

Partially supported

 | 

Supported

 | 

Hot reload enables the API object modification in files except those decorated with @Entry to take effect.

 |
| 

Enums

 | 

Add and modify

 | 

Partially supported

 | 

Supported

 | 

Hot reload enables the enum addition and key and value modification in files except those decorated with @Entry to take effect.

 |
| 

Delete

 | 

Supported

 | 

Supported

 | 

\-

 |
| 

Anonymous function

 | 

Add, modify, and delete

 | 

Supported

 | 

Supported

 | 

\-

 |
| 

Lambda functions

 | 

Add, modify, and delete

 | 

Supported

 | 

Supported

 | 

\-

 |
| 

Closure functions

 | 

Add, modify, and delete

 | 

Supported

 | 

Supported

 | 

\-

 |
| 

Closure variables

 | 

Add and delete

 | 

Partially supported

 | 

Partially supported

 | 

Hot reload enables only the addition and deletion of top-level closure variables (excluding **this** variables) to take effect.

Since DevEco Studio 6.0.0 Beta3, hot restart does not support the addition of **this** variables or the deletion of all **this** variables.

 |
| 

Modify

 | 

Partially supported

 | 

Supported

 | 

Hot reload does not support the modification of top-level closure variables.

 |
| 

Custom components

 | 

Add, modify, and delete

 | 

Partially supported

 | 

Supported

 | 

Hot reload supports only the addition and modification of custom components imported using **import** in files decorated with @Entry.

 |

**Table 3** Other scenarios
| 
Scene

 | 

Hot Reload

 | 

Hot Restart

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

When a breakpoint is hit

 | 

Not supported

 | 

Not supported

 | 

Click [Resume Program](../debug-tool-window/document.md#section638719251088) to continue the execution and then perform hot reload or hot restart.

 |
| 

When the navigation code to other ability pages is modified

 | 

Not supported

 | 

Supported

 | 

After the code is modified and hot reload is performed, restart the ability page for the modification to take effect.

 |

#### (Optional) Enabling Hot Restart

To enable hot restart, choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Build, Execution, Deployment** > **Hot Reload**, check **Enable hot restart (to hot reload and restart app)**, and click **OK**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/xsknpBNGSDKO7WYmWVAydQ/en-us_image_0000002532749867.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7B6CE26DB96C5EA5A1DA793D31164648ACEF5EFE28D672C8FE02AA683ECE9147)

#### Procedure

1.  Connect to a real device or start the Emulator.
2.  In the **entry** drop-down menu, select ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/OFKCxhymR4aw1cHEdYrowQ/en-us_image_0000002532669915.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ADD71232B25024DDA2095768CF40BE15C3A26F5398A9B5C3A209AA9DDD283FDE) (hot reload configuration).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/_izFodSMR8qr56483KLCqw/en-us_image_0000002532749857.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC2C35CD949D84E29D603EA1643E44B5D8FB3493CF575A2DF995C290B40C35FF)
    
3.  Run or debug the app. For details, see [Running Your App on a Local Real Device](../../../running-your-app-on-a-local-real-device/document.md) or [Running Your App on the Emulator](../../../running-your-app-on-the-emulator/document.md).
4.  As you modify code, you can view the effect on the device using hot reload in any of the following ways:
    
    -   Click the ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/BOWUX9uZQJOGIrBhCdLeeA/en-us_image_0000002532669911.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D649C9762985AA5DC80C024503B8CC7AB3310D356472596462C62ED59148D3E) **Hot Reload** button.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/XLmBGiZqSLaIGadVkfMblQ/en-us_image_0000002500909988.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D42EB948C22051672CF2DCFABF09B67B92AF9728C3160F64B65836B783CD0424)
        
    -   Press **Ctrl+S**. This requires you to enable the use of shortcut keys first: Choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Tools** > **Actions on Save**, select **Perform hot reload**, and click **OK**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/L03GUrfHS2eQ2JrtTYyUrg/en-us_image_0000002532669913.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C61BD9793C9467388B01A3DB45277B6AAB064C65EE9BE55FB5649D4FAE8C85F4)
        
    
    After successful execution of hot reload, the following information is displayed on the console:
    
    Performing hot reload...
    Syncing files to device xxx
    Reloaded 1 files in x s xxx ms.
    
    After successful execution of hot restart, the following information is displayed on the console:
    
    Performing hot restart...
    $ hdc shell aa force-stop com.xx.xx
    Syncing files to device xxx
    Reloaded 1 files in x s xxx ms.
    $ hdc shell aa start -a EntryAbility -b com.xxx.xxx in xxx ms
    
5.  Click the **Stop** button to stop the app running or debugging and exit the hot reload mode.

#### (Optional) Dynamically Configuring the Signature or App Version Number

In multi-developer collaboration scenarios, when using the hot reload feature, you can dynamically configure the signature or app version number in **hvigorfile.ts**, eliminating the need for each developer to make local modifications. This feature is supported since DevEco Studio 6.0.2 Beta1.

-   Signature configuration: Instead of using the automatically generated signature information in **build-profile.json5**, you can configure signature details in **hvigorfile.ts**. The hot reload feature will continue to function normally. For details, see [Modifying build-profile.json5 Configuration for Individual hvigorNode](../../../../building-an-app/customizing-your-build/dynamically-modifying-the-build-configuration/examples/document.md#section973053620286).
-   App version number configuration: Instead of using **versionCode** in **app.json5**, you can dynamically configure the app version number in **hvigorfile.ts**. The hot reload feature will continue to function normally. For details, see [Modifying app.json5 Configuration](../../../../building-an-app/customizing-your-build/dynamically-modifying-the-build-configuration/examples/document.md#section9435132933118).
