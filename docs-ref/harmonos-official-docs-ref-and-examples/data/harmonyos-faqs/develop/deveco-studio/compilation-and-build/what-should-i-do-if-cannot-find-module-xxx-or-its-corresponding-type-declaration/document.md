# What should I do if "Cannot find module XXX or its corresponding type declarations" is reported during compilation?

-   **Scenario 1:**
    
    **Symptom**
    
    When the native .so file is referenced during stage model project compilation, "Cannot find module XXX or its corresponding type declarations." is reported.
    
    **Solution**
    
    For stage model projects, the compilation and build process includes syntax validation for exported symbols in native (.so) files. If a project references a native file (.so) that has no corresponding declaration file (.d.ts), the syntax validation tool reports an error, indicating that the corresponding declaration file cannot be found.
    
    To resolve this issue, try the following solutions:
    
    1.  Create the **types/libxxx** directory in the corresponding **cpp** directory, add the **index.d.ts** file to the directory to declare the type symbols in the native file, and add the **oh-package.json5** configuration file for the verification tool module querying.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/PSt5uYPaTIyHec8z2JJEoA/en-us_image_0000002229604373.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F71D4D671DA9A80E9D307E9A308ABE3D473A1ED9F3AD3F37F643A2A6B4B568EB)
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/3IxQqcPUSM-myVSPSo2iEQ/en-us_image_0000002194158980.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF8528379E91987D5131F7C2FAB79A71D74EB989BAFE7F0A978F9651FA97F44D)
        
    2.  Add the local dependency of the native file to **oh-package.json5** in the module referenced by the native file, and click **Sync Now** to synchronize the project as prompted. The following figure uses the entry module as an example to describe how to reference a native file.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/oARUmW8xQSK_H4YZw_xcTA/en-us_image_0000002194318572.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8E256ED4E188EE33A97438BE08512EAD8D744BD5F2D21BDDBD078B899D369796)
        

-   **Scenario 2:**
    
    **Symptom**
    
    During the compilation of a stage model project using API version 11, the error "Cannot find module '@kit.xxx' or its corresponding type declarations" is reported.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/ruLhrR1ARziXpMpzaoPA_w/en-us_image_0000002229758849.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65B677A351A8B6C4F0B83DF815DCB0450B21002DEF56AC3CBDA3668FE8678601)
    
    **Possible Causes**
    
    This problem occurs when DevEco Studio NEXT Developer Preview1 or a later version is used. In the newly created API 11 stage model file, the **import** mode is changed to **import xxx from '@kit.xxx'**. If the SDK uses a version earlier than HarmonyOS NEXT Developer Preview1, a compilation error is reported because the old SDK does not support this import mode.
    
    **Solution**
    
    Update the SDK or DevEco Studio.
    
    -   If the DevEco Studio between DevEco Studio NEXT Developer Preview1 and HarmonyOS NEXT Developer Beta1 (5.0.3.300) is used, choose **Tool** > **SDK Manager** on the menu bar, update the SDK to HarmonyOS NEXT Developer Preview1 or later version, and compile the project again.
    -   If DevEco Studio of HarmonyOS NEXT Developer Beta1 (5.0.3.300) or a later version is used, the SDK is installed together with the DevEco Studio software package. You can download the latest version of DevEco Studio from [Download Center](https://developer.huawei.com/consumer/en/download/).
-   **Scenario 3:**
    
    **Symptom**
    
    When a third-party package is referenced, the build fails and the error "Cannot find module 'xxx' or its corresponding type declarations" is reported.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/Otg2dYbBS3q4DWsMCV94_Q/en-us_image_0000002229758853.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C69218DE8E54F820FBE017DC1BEDD0A8654051F8A2897EE809FD8E678DB2AAA5)
    
    **Solution**
    
    Go to the module-level or project-level **oh-package.json5** file and check whether the third-party package has been installed. If not, run the **ohpm install** command to install it. If yes, check whether the **main** field is correctly configured. If not, set it to the correct entry file.
    
-   **Scenario 4:**
    
    **Symptom**
    
    A path is directly added to the end of the referenced package path, leading to path obfuscation.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/pDVGBKlCSFK6atriUamZVA/en-us_image_0000002194158984.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C06E34423A9569119A0FAD05D70DC3B8751D6BEF6783FBD0AFF870787ACBA49)
    
    The module cannot be found if the package is referenced as follows.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/_b0W6dH8SN-iH6vCCuSjHw/en-us_image_0000002229758861.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCE3685EE2080BB9809C0A63E4DAE3DDD2D9D32012F567FC5C1D9A63C2045499)
    
    **Solution**
    
    Use the recommended reference mode as follows.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/hJsg8UqHSuuXHz45KqbVVQ/en-us_image_0000002194158972.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E9A213E8B3F2ABCE3477A5DF8A6DB49F1CD2E04ABD15FD982F95EDA855410BF)
    
-   **Scenario 5:**
    
    **Symptom**
    
    The **oh-package.json5** file of referenced module is incorrectly configured. After the **ohpm install** command is executed and the dependency is successfully installed, the module still cannot be found.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/RDekeomtSOOqOCoZi06l_g/en-us_image_0000002194158976.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B40FC5E7BA062DDAD4A8EBBBB02A4802EA415AFCA223B01805AC75A81234125)
    
    The **types** field is incorrectly configured in the **oh-package.json5** file of the referenced module.
    
    This field takes precedence over the **main** field. In other words, if the value of **types** field does not exist or is incorrectly configured, an error is reported.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/qBgaiUjMThSQuV8NWTwpbA/en-us_image_0000002229604353.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F6CB84569E0019FFC6D9BFC3502818A32518558589094435AA2D0CC89B7CF2E6)
    
    **Solution**
    
    If the package does not contain the d.ets declaration file, delete this field. If the configuration is incorrect or does not exist, an error is reported.
    
-   **Scenario 6:**
    
    **Symptom**
    
    The name of the module referenced in **dependencies** of **oh-package.json5** is different from that imported in the code.
    
    When using **import** in the code, you should use **HAR** (uppercase) instead of **har** (lowercase) configured in **dependencies**. Ensure that a consistent file name is used. Otherwise, an error is reported in the Linux system, indicating that the module cannot be found.
    
    **Solution**
    
    Ensure that the values for reference and import are the same.
    
-   **Scenario 7:**
    
    **Symptom**
    
    The value of the **main** field in **oh-package.json5** of the referenced module is inconsistent with the actual file name.
    
    **Solution**
    
    Ensure that the value of the **main** field to be in the same letter case as that of the actual file name.
    
-   **Scenario 8:**
    
    **Symptom**
    
    The stage model project fails to be built, and "Cannot find module '@bundle:rollup\_plugin\_ignore\_empty\_module\_placeholder' or its corresponding type declarations" is reported.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/Y-bSiPzTR-iwnW-jTbQXfQ/en-us_image_0000002229758841.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8983AD577E297F3281828C8153E1A491B897CB0C1CDAAAFCB360A50B505A38E0)
    
    **Solution**
    
    The project references a .d.ts file that does not have the corresponding implementation file. Do as follows:
    
    1.  Search **rollup\_plugin\_ignore\_empty\_module\_placeholder** in the **build** directory to locate fault module.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/sMZ-FNAaRGC0KA20-iXB4g/en-us_image_0000002194158956.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8296D9A8BAFC5801FE21FBFE9416971EE850D7BEB19972769D5F408B95FD553)
        
        Enter **rollup\_plugin\_ignore\_empty\_module\_placeholder** in the text box to locate the intermediate file.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/DrqJxlDOQb6mJ6KZX80l-g/en-us_image_0000002194158964.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57E8F7F42FF705DE92A466C2BCB1C796C866C2302EFDADA64952C99ECEA17719)
        
    
    2.  Add the explicit **type** symbol to the referenced type file.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/QgRWThF8SO-SDcCcWydCSA/en-us_image_0000002229758865.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C77A8FADD43D4D20D71CB949F8F745BC61AAA770B51142EF14F8B5C43823796F)
        
    
    3.  Check whether the value type symbol is referenced from the d.ts or d.ets file. Do not declare value variables in the declaration file.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/yoX08C7ER5iwZmWGtxpQ3g/en-us_image_0000002194158968.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3542527B33D29DCF72A00924100601E5965D1A9448303B5C2FE1168F2A7C93F)
