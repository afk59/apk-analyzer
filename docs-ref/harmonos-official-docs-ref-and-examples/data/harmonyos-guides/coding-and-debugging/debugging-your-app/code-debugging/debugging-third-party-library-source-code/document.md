# Debugging Third-Party Library Source Code

Third-party shared packages can be classified into two types: Harmony Archive (HAR) and Harmony Shared Package (HSP). The source code debugging methods for these two types of packages are different.

#### Distinguishing Between Bytecode HAR and Source Code HAR

HAR packages are categorized into bytecode HARs and source code HARs. A HAR package is a bytecode HAR if it meets both of the following conditions. Otherwise, it is a source code HAR. For more guidance on building source code HAR and bytecode HAR, see [Building HAR](../../../../building-an-app/configuring-your-build/building-a-har/document.md).

1.  The .abc file exists in the **ets** directory of the HAR package.
2.  The **oh-package.json5** file of the HAR package contains the **byteCodeHar** field and the value is **true**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/uN_9FD5kQJW-gK0vtXKcdA/en-us_image_0000002500909994.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=901A516117E56F41649A77C4A4B56516AC758A4A2911FF62E99B2DBFC6C4D1E2)
    

#### Debugging the Bytecode HAR

## Debugging C++ Code

If the HAP/HSP references a bytecode HAR package that contains C++ code, perform the following steps to debug the HAR package:

1.  Choose **Run** > **Edit Configurations** > **Debugger**, select the **Symbol Directories** tab, and click **+** to add the .so file with debugging information, which is stored in **{_ProjectPath_}/{_ModuleName_}/build/{_product_}/intermediates/libs/default/arm64-v8a**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/AisiO1sjQHif7IqmxJTSnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F66DD1B2DAE5AA34F09453BA82D17C2E9076DA26A5A5B8C91143650DE7A297F6)
    
    To generate the .so file with debugging information, add the **strip** field to the project- or module-level **build-profile.json5** file and set it to **false**. For details, see [Configuring for C++ Builds](../../../../building-an-app/configuring-your-build/configuring-for-c-builds/document.md#section2182144382320).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/SMLfdc32RUy6wzv4LOGMAg/en-us_image_0000002501069832.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27AFB0ABB08F9312214DE8896258EA33D6C5C2D96F6AA6F40CEA6397A9F9B894)
    
2.  When you debug an app, DevEco Studio loads the configured .so files preferentially. If these .so files contain debugging information, you can debug the source code. Since the source code file information embedded in the .so file refers to the file path at compile time, if it does not match the local source code file path, you need to associate the source files using either of the following methods:
    -   Method 1: Add a command in the **LLDB Startup Commands** tab to create a mapping. Example:
        
        settings set -- target.source-map {old-path} {new-path}
        
        -   **old-path**: file path at compile time.
        -   **new-path**: local source code file path.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/bsp15RN3SAmXLPnaUGFq9g/en-us_image_0000002501069846.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E463BE1E02AD0E319B9781A3429B9FA1B5F5C6EDABA4DAAE4A01F9CDEEE8EC57)
        
    -   Method 2: After the debugger steps into the assembly code, a message is displayed asking you to select the source code. Click **Select File** and select the local C++ source code.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/-Pe_hWnWRfWRQekiZeXWlQ/en-us_image_0000002500910010.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF9E8893BB162B788946EE434A65D6BF091F6ABDC14DA7039640DD5485AB69C2)
        

## Debugging ArkTS Code

If a bytecode HAR package is compiled in debug mode in Project A (HAR package project), and Project B (host project) references this bytecode HAR package with local access to the source code of the HAR package. To debug this bytecode HAR, there are two methods: debugging in the host project or debugging in the HAR package project.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/Bz_Z2eUQTaqJL92ZuOcmlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F5AE20ED5104167B7349AE361224F2D0C2472360AD30102F379625F53FFFE6CA)

The bytecode HARs compiled in release mode do not support debugging.

-   **Method 1: Debugging in the host project**
    1.  Import the module corresponding to the bytecode HAR into the host project, and ensure that the module's directory hierarchy is consistent with that of the HAR package project. For example, all HAR modules are placed in the project root directory.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/v3xvJxc7S1uygisYWbJgUw/en-us_image_0000002532669925.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=501DB784275010FABA97BC7B8912B59DBC8B978F5133608E0DEF00EC2E2EA2A2)
        
    2.  After successful import, since the bytecode HAR compiled in debug mode contains [sourceMap](../../../analyzing-logs-and-faults/fault-analysis/exception-stack-trace-analysis/document.md), the source code of the current project will be associated by default during debugging. At this point, you can directly set breakpoints in the HAR module.
-   **Method 2: Debugging in the HAR project by modifying the prefix configuration for attach debugging**
    
    1.  Create a demo host module of the entry type in the HAR package project. Skip this step if the host module already exists.
    2.  Configure dependencies on the bytecode HAR package in the **oh-package.json5** file of the demo host module.
        
        // oh-package.json5 of the demo host module
        "dependencies": {
          "@ohos/test\_stage\_ets\_library": "file:./lib/test\_stage\_ets\_library.har",
        }
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/TnG4X4W6RLOTXuHPBOMqSw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F08AED1EAE65ABEF3785CA7500666B76B8451FD79B5233B55E4181F3A1D0FEB5)
        
        If dependencies on the bytecode HAR module, for example, **file:../test\_stage\_ets\_library**, are configured in the **oh-package.json5** file of the demo host module, breakpoints may be invalid during debugging.
        
    3.  Call the APIs of the HAR module in the host module of the HAR package project. Ensure that the **sourceMap** file of the host module contains relevant information about the HAR module after compilation.
    4.  Build the HAR package project, open the **sourceMap** file of the host module, and search by the name specified in the HAR's **oh-package.json5** file. Record the prefix path of the **Index** file as the value of **localUrl**, for example, **demo|test\_stage\_ets\_library|1.0.0**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/HT4xkA0uSsG44d_qSipYKg/en-us_image_0000002501069840.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A4693D69D7A6AF4AD6E444CEC095C4C92A821D52FDB1E10E4E67BF21E0C3E63)
        
    5.  After the host project application runs on the device, use the attach method in the HAR package project to debug the application. In the **Debug** window, obtain the prefix when the program is loaded and record it as the value of **remoteUrl**, for example, **entry|@ohos/test\_stage\_ets\_library|1.0.0**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/h_SmMCD6R0qB6qXMrg0wTQ/en-us_image_0000002532749873.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=304ED525BF9B25EA5B3A381303D34F38895168F68BF298905FBE783CD65C9AAA)
        
    6.  Choose **Run** > **Edit Configurations** > **Debugger** > **Ets Source Pairs**, click **+**, and enter the values of **remoteUrl** and **localUrl** obtained in the previous two steps.
        
        -   **remoteUrl**: prefix path for the application to load the HAR package.
        -   **localUrl**: prefix path of the HAR in the locally generated **sourceMap**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/EqdJMGEPRH6z-g23iY5bxQ/en-us_image_0000002500909998.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0BCBB2FA8350D376CE7A323B03BC210183F2167F280ADDB1F63E2789A45AE6C5)
        
    7.  Re-debug the host project application via the attach method in the HAR package project. Breakpoints can be added to the HAR module for debugging.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/J9eYUk9DQp-CDYuIjbqgkA/en-us_image_0000002500910000.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22F924DA02EF46709AC2AC63C6B7204E453C79FC794A4D6FDE2059EDBA05C250)
        
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/FJa-545wRNuX28W-8LgSDg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A640447A3ED47B4381A7778542AE1B1F8F016D11A6F7F89E2659C2718EF80FA7)
    
    If both [Symbol Directories](#section177418333199) and **Ets Source Pairs** are configured in the HAR package project, ArkTS and C++ breakpoints can be debugged at the same time via attach.
    

#### Debugging the Source Code HAR

## Debugging C++ Code

If the HAP/HSP references a source code HAR package and the HAR package contains C++ code, perform debugging by referring to [Debugging the Bytecode HAR](#section177418333199).

## Debugging ArkTS Code

If a project references a source code HAR package, debug this HAR package. The debugging methods vary depending on whether there is local source code.

-   If there is no HAR source code on the local side, the source code in the project-level **oh\_modules** directory is referenced during the app build and packaging process. In this case, debug the source code in the **oh\_modules** directory.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/JBxMQ1O5QYK1nnW35mVVvg/en-us_image_0000002532669923.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7B42A8E058D6D64C8AC6ADF36FED9571C9D1BF0C5E37836F3F07AA6722438B28)
    
-   If there is HAR source code on the local side, associate and debug the local HAR source code in either of the following methods:
    -   Method 1: Similar to the method described in [Debugging the Bytecode HAR](#section1035165781918).
    -   Method 2: After the debugger steps into the ArkTS code in the **oh\_modules** directory, a message is displayed asking you to select the source code. Click **Choose Sources** and select the local ArkTS source code.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/T0oKNP4LTpuJp0KFMJUMoQ/en-us_image_0000002532669919.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ADDE0816A1A43F9232D3871D58929EFC362CF88D9F3BA7AC3CE58ADB73907958)
        

#### Debugging HSP Source Code

To debug the HSP source code, place the source code in the local project module and debug it by referring to [Method 1: Debugging in the host project](#li17359570194).
