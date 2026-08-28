# Running/Debugging Configuration

#### Configuring App Debugging

Whether an app supports debugging is determined based on the **debug** field in the **app.json5** file and the **debuggable** field in the **build-profile.json5** file. The **app.json5** file takes precedence over the **build-profile.json5** file.

1.  Configure the **debug** field in the **app.json5** file.
    -   **true**: The app supports debugging.
    -   **false**: The app does not support debugging.
2.  If the **debug** field is not set, the **debuggable** field in the **build-profile.json5** file takes effect.
    -   **true**: The app supports debugging. If the [build mode](../../../building-an-app/customizing-your-build/customizing-build-options/introduction/document.md#section192461528194916) is not release, the default value of **debuggable** is **true**, indicating that the app supports debugging.
    -   **false**: The app does not support debugging. If the build mode is release, the default value of **debuggable** is **false**, indicating that debugging is not supported.

#### Setting the Debug Type

Choose **Run** > **Edit Configurations** > **Debugger**. On the left pane, choose **Application** > target module. On the right pane, set **Debug type**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/DtVqxDdqRimtp4_RPBl5zA/en-us_image_0000002507497468.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95E87D7DB204A3254AB3BA2C5092E0EF61AFFCBA2984B6272AE596DD1C407A45)

By default, the project debug type is **Detect Automatically**. The table below describes the debug types.

**Table 1** Debug types
| 
Debug Type

 | 

Code Type

 |
| :-- | :-- |
| 

**Detect Automatically**

 | 

ArkTS/JS. The debugger is selected based on the programming languages involved in the project module and its dependent modules.

 |
| 

**ArkTS/JS**

 | 

-   ArkTS
-   JS

 |
| 

**Native**

 | 

C/C++

 |
| 

**Dual (ArkTS/JS + Native)**

 | 

ArkTS/JS and C/C++ for C/C++ projects

 |

#### Setting the HAP Installation Mode

You can use either of the following modes as required:

-   Mode 1 (default): Uninstall the app/atomic service and then reinstall it. This will clear all cached app/atomic service data on the device.
    
    Since DevEco Studio 4.1 Canary2, the app/atomic service package is not pushed for installation if the code does not change. That is, only the changed modules and the modules that rely on the changed modules are pushed and installed on the device. For example, the entry module relies on the HSP module. If the code of the HSP module changes, the HSP and entry modules will be pushed and installed during debugging.
    
-   Mode 2: Install the app/atomic service in overwrite mode, which does not uninstall the existing app/atomic service. In this mode, the cached data of the app/atomic service will be retained.

To set the HAP installation mode:

Choose **Run** > **Edit Configurations**, and select or deselect **Keep Application Data** under **Installation Options**. Selecting **Keep Application Data** will install the app/atomic service in overwrite mode, which retains the app/atomic service cached data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/F82zJpMTSTqWmvURh_mQ-Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B603C62CB4245769AE3F6ECEBE5AE542F79A031093E3AA1FC303C2E3F054D8AD)

Since DevEco Studio NEXT Developer Beta1, **Keep Application Data** is selected by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/f6bWbIf6RLqMLjKgHqfUzg/en-us_image_0000002507337732.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F17BB5A73B89D17ABB0F22A2960771636A7B8A785B378A6E80E2D18DA841402)

## Setting Debugging Parameters

If you do not set debugging parameters, the app/atomic service will be installed and run based on the default configuration. You can set the parameters under **Installation Options** and **Launch Options** to match your case.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/WKhn1YGcR3W8YNAKAGlQ2g/en-us_image_0000002532670181.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB6050C3D39750510F0B7F1800B4034CC00487FE9ADD2C630B0E1BE99C8E7DA9)

-   Installation Options
    -   **DebugLine Support**: Select **Enable DebugLine** to enable the system components in the build products to include the **debugline** attribute, with which you can [navigate through source code in ArkUI Inspector](../layout-analysis/document.md#section1226015494335).
    -   **Install Flags**: You can enter parameters of the **bm install** command. For details, see [install](../../../system/debugging-tools/debugging-commands/bundle-manager/document.md#install). For example, you can enter **\-w 360** to set the timeout to 360 seconds.
-   Launch Options
    -   **Launch**: Select the ability to start after the app is installed.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/VvamzftLRKGY8_CucRTzgg/en-us_image_0000002501070106.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3AC64FCF1183BE19E2C74F0CA77EDF5C1ABF624C2E639492BD79982C0DAE3DB0)
        
        -   **Nothing**: does not start any ability.
        -   **Default Ability**: starts the default EntryAbility. The default EntryAbility varies with the development model you use.
            -   Stage model: The default EntryAbility is the first ability under **skills** in the **module.json5** file. If no ability is configured under **skills**, it is the ability specified by **mainElement** (the ability must be configured in the **abilities** array). If **mainElement** is not specified, the default EntryAbility is the first ability in the **abilities** array.
                
                ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/XxQ2sznXSti9Gd58jIV0sg/en-us_image_0000002532670185.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D414A31E854C64F02C4C16DFE21B2AEDC74E202BA22FFE848E5819914F80CDA "Click to enlarge")
                
            -   FA model: The default EntryAbility is the first ability under **skills** in the **config.json** file. If no ability is configured under **skills**, it is the ability specified by **mainAbility** (the ability must be configured in the **abilities** array). If **mainAbility** is not specified, the default EntryAbility is the first ability in the **abilities** array.
        -   **Specified Ability**: starts a UIAbility or an ExtensionAbility in the project.
            
            You can add a UIAbility or an ExtensionAbility to the project. For details, see [UIAbility Component](../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/uiability-component/document.md) or [ExtensionAbility Component](../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/extensionability-component/document.md).
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/EVQ8yTFlSqCA9OggsbOeCA/en-us_image_0000002500910262.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2DC532BA3EEC2D21015FD79A98C77DB5B8184CDB9EB646330C39EC2FD4E217EB)
            
        
    -   **Launch Flags**: You can enter parameters of the **aa start** command. For details, see [start](../../../system/debugging-tools/debugging-commands/ability-assistant/document.md).

## Setting Environment Variables

By configuring environment variables under **Environment Variables**, you can configure and manage the app development environment, as well as control the app behavior.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/Pfbjk0sVQDOlJWB3hI1ePA/en-us_image_0000002532670183.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF17CDD5539869D2375B870399BD406046D3EEB43F0C2DD1C1E32CFEFC4700F9)

Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/jqtx5c2yR4m8aCoHljqfvQ/en-us_image_0000002500910272.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A56E9B87EA80F94ABC7DD1F973D9F5A9691696FC29303F1BC7CDA614251E8C5F) to add a configuration item. The following configuration items are supported:

-   **ASAN\_OPTIONS**: defines behavior of ASan at runtime. You can set the detection level, output format, and the detail level of memory error reports. For details, see [Configuring Parameters](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-stability-asan-detection#section1496994494018). If **log\_exe\_name** and **abort\_on\_error** are not configured, DevEco Studio will automatically fill them in. **ASAN\_OPTIONS** applies at the app level and is only effective when configured in entry and feature modules; it does not take effect in HAR or HSP modules.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/noYIdbZ4SJynFF2umzUhuA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=823C181C792A72ED3A10703A8514611AE00588D651AE7F374ECF137EC91D5874)

After the environment variables are configured, **Keep Application Data** does not take effect.

Select the set environment variables, and then click **Apply** for them to take effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/Z_7cqegYSTO38wnYhDaD1A/en-us_image_0000002532750133.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0DBCB06C0656C1A02AC92CC7C070E7BED06E4D35A071F6559E8ABBC62999B006)

#### Automatically Mapping the WebView Debugging Link.

If your app contains a **WebView** component page to be debugged, use DevTools of the browser. For details, see [Debugging Frontend Pages by Using DevTools](../../../application-framework/arkweb/web-debugging/debugging-frontend-pages-by-using-devtools/document.md). Debugging the **WebView** component requires complex command line operations such as port forwarding. You can select **Auto WebView Debug** in DevEco Studio, which automatically listens for the **WebView** process that can be debugged and completes port forwarding within two minutes after the app is started.

This feature is supported since DevEco Studio 5.0.5 Release.

To enable the feature:

Choose **Run** > **Edit Configurations**. On the **General** tab page, select **Auto WebView Debug**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/n7E9X85NRnWdxXT7O2GYZA/en-us_image_0000002539177811.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20FB33D6575AB6AECD8F561382CA46781DC109BE1F528F426CA5DC935113E82A)

After this feature is enabled, when a **WebView** component process that can be debugged is detected on the device, the port that is successfully forwarded is displayed on the Run panel. You can connect to the port for debugging using DevTools of the browser.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/SK0WTaNcSfifnoid9qj8og/en-us_image_0000002532750147.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A38FA10C06366B58D523151B37EC743E713821E4F2B9325E2EE4606CBC1EBA7)

#### Debugging Multiple Modules

## Installing Multiple Modules

If a device in a project has multiple modules (for example, a device has **entry** and **feature** modules) and the modules are invoked by each other, you need to install the HAPs of the modules on the device in the debugging phase. In this case, you need to specify the modules on the **Deploy Multi Hap/Hsp** tab page. When you start debugging, DevEco Studio will install the specified modules on the device.

To install multiple modules for debugging:

Choose **Run** > **Edit Configurations**. On the **Deploy Multi Hap/Hsp** tab page, select **Deploy Multi Hap/Hsp Packages** and specify the modules.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/hp0hzkr2TnKfxfvGUHDHJQ/en-us_image_0000002532670177.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=075303F9F482FC45DA0A57E069F5774A81C5E6587D5DF4290A69651961FF8C6E)

## Installing Dependencies Automatically

If a module has direct and indirect dependency modules (for example, the **entry** module depends on the **HAR** module, which in turn depends on the **HSP** module), you need to install HAPs of all these modules in the debugging phase. In this case, you can select **Auto Dependencies**. When you start debugging, DevEco Studio will install all dependency modules on the device.

To deploy dependencies:

Choose **Run** > **Edit Configurations**. On the **General** tab page, select **Auto Dependencies**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/575mADVGQh2xYhTDAMtsfQ/en-us_image_0000002539180951.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0681A471CCA7BF0CEB9AA679EC020F5E3085C3ECFAFF9E91AE535F688CB5B817)

In the **Before launch** pane, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/JgaTHVjbTfOfpgI9qv3gsA/en-us_image_0000002500910276.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB5A5DCFD483BEBA344F7036CC8DBF585F3AF69D9348966B9B4189720C76928B) to add a task before the app is started.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/6h2pFn7gSCS0qXmdsrrheQ/en-us_image_0000002500910266.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9EC9F187EF21EB738E1714A7CB2DCD0563002812377EDDD1F09D1CC85269CBBC)

To remove a task, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/3OuiDuVFSTqs2c-pfyUp_Q/en-us_image_0000002532750139.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D40BF6946CC9CDF1ED79EFC3992A3E7104D95D092B75026907BBCD01B03B6F9).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/cgIRVdVzRTGXzXcDFh7FPA/en-us_image_0000002500910258.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9E9FBD18500515EFDA7FB70E1E009D9ABA9DB3F6487E128215BC13B7E46ABC9)

After selecting **Auto Dependencies**, you can also select **Deploy Multi Hap/Hsp Packages** to push all packages.

#### Running on Multiple Devices

DevEco Studio 6.0.2 Beta1 and later versions allow your app to run on multiple devices, including real devices and launched emulators.

1.  In the device selection box, click **Select Multiple Devices…** to open the multi-device selection dialog.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/WtS0jccLSYq3VMR75GyKoA/en-us_image_0000002500910260.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9E477B776926B99DC4F23D91F0B42C5146E62763863983BC74F61C94F03603C)
    
2.  Select the target devices where you want to run your app.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/yvfKvrCNQL2iRSIGVXzxeQ/en-us_image_0000002532750143.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A69FF10DF8154B42E2B804BAC5882343FA496E44AF4B06F4CDE83044D42D5D4)
    
3.  The device bar will show **Multiple Devices(N)**, indicating that _N_ devices are selected. Click the run button to launch and run the app on all selected devices at once.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/n3pLZ0wlRl6sf7faEw9chQ/en-us_image_0000002532750137.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F791EAF38EC29043EDF16678FD2BDDA1384CF15CEFC38313AA15B892A21A3F62)
