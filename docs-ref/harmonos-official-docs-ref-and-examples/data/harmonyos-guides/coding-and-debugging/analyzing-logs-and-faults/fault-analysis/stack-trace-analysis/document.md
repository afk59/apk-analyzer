# Stack Trace Analysis

For release apps, to reduce the app size and improve runtime efficiency, the code is optimized and debug information is removed. As a result, the specific source files and line numbers cannot be directly located based on the stack information of the release app, making it difficult to quickly pinpoint and resolve issues.

To address this challenge, DevEco Studio provides a stack trace analysis feature for release apps. By leveraging the files that contain debug information (such as .so, sourceMap, and nameCache files), you can easily map obfuscated method names and file names in C++ and ArkTS stack traces back to their original, human-readable forms. For details about the build products and stack parsing principles, see [Exception Stack Trace Analysis](../exception-stack-trace-analysis/document.md).

To analyze the stack trace, perform the following steps:

1.  Choose **Code** > **Analyze Stack Trace** on the menu bar, or right-click the stack information on the **FaultLog** page and choose **Analyze Stack Trace** from the shortcut menu.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/-ufaz2HTRCC9dlokVDwsbg/en-us_image_0000002532749747.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=641094E70B476056917B2283C67D6FAEDB7580A6A9E7F69CAA57281390345C2F)
    
2.  In the dialog box that is displayed, paste the stack information of the release app.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/8tS9f5HTSYSqakK7vjLwEA/en-us_image_0000002500909888.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0253B07DABCC458BEF9834670E198DD1A9EA6A2A7E5337E4D17CABCA14D4A321)
    
3.  If the current project is the project of the app where the stack is located and there is a release build, click **Start Analyze** to parse the project.
    
    If the current project does not correspond to the app where the stack is located, select **Unscramble stack trace**, add the sourceMap, .so, and nameCache files of the app, and click **Start Analyze**.
    
    The parsed stack information is displayed in the right pane.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/STzUljbcSI6Q0GghynAOQw/en-us_image_0000002501069732.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A7BB40469E4D56AA66F50141CCEEB8E79412F0913DAB72F7014BFB2507F52809)
    
    When a release app is built, the .so file does not contain symbol table information by default. To generate a .so file that contains symbol table information, set **buildOption** in the module's [build-profile.json5](../../../../building-an-app/configuring-your-build/configuring-for-c-builds/document.md) file as follows:
    
    "buildOption": {
      "externalNativeOptions": {
        "arguments": "-DCMAKE\_BUILD\_TYPE=RelWithDebInfo"
      }
    }
    
    When analyzing an exception stack trace from native methods in a referenced release HAR module, select **Unscramble stack trace** and select the .so file with symbol information in the HAR module. The .so file in the referencing module's build product does not contain symbol information. The relative path of the .so file in the module is **build/default/intermediates/libs/default/{_CPU type_}/libxxx.so**.
