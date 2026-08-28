# Building a HAR

In DevEco Studio, you can build a HAR in debug, release, or custom modes.

HAR products are available in three formats: source code, JavaScript intermediate code, and bytecode.

Since DevEco Studio NEXT Beta1 (5.0.3.800), the default HAR product format is bytecode for improved security.

#### Constraints

When building a HAR, avoid referencing local modules, as this may cause installation failures in other modules that depend on the HAR. If an installation failure occurs, update the [overrides](../../../command-line-tools/using-ohpm/oh-package-json5/document.md#en-us_topic_0000001792256137_overrides) settings in the **oh-package.json5** file of the project.

#### Creating a HAR

1.  Create a project of API version 10 or later in the stage model. In the created project, create a module using the **Static Library** template. For details about how to create a module, see [Adding or Deleting a Module](../../../environment-setup/creating-a-project/managing-modules/adding-or-deleting-a-module/document.md).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/nem5MNP2SNCtvW4IvxmJPQ/en-us_image_0000002532750173.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DB186E03159ADA2E75B119EC33FA0DE68DE9D192D16964B58CF61D37258F676)
    
2.  Write code.
    
      library  // HAR root directory
      ├─libs  // Native libraries referenced, generally .so files
      └─src
      │   └─main
      │     ├─cpp
      │     │  ├─types  // Native interfaces exposed
      │     │  │  └─liblibrary  
      │     │  │      ├─index.d.ts
      │     │  │      └─oh-package.json5 
      │     │  ├─CMakeLists.txt  // CMake configuration file
      │     │  └─napi\_init.cpp  // C++ source code file
      │     └─ets  // ArkTS source code
      │     │  └─components
      │     │     └─MainPage.ets
      │     ├─resources  // Resource files, such as images, multimedia files, and string files
      │     └─module.json5  // Module configuration file, including the current HAR configuration
      ├─build-profile.json5  // Configuration file for hvigor compilation and building, including build options
      ├─hvigorfile.ts  // hvigor build script file, including plug-ins and customized tasks for building the current module
      ├─Index.ets  // Entry point file of the HAR, which is generally used as an exit to define the functions and components that the HAR provides to other modules.
      **└─oh-package.json5**  // HAR description file, which defines the basic information and dependencies of the HAR.
    
3.  In the **oh-package.json5** file, define the **main** field to specify the entry of the exported files. If the **main** field is not defined, the **Index.ets** file in the current directory is used as the entry point file by default. Files are searched in the sequence of .ets > .ts > .js. In the following example, the entry point file is set to **ets/components/MainPage.ets**:
    
    {
      ...
      "main": "./src/main/ets/components/MainPage.ets",
      ...
    }
    

#### Building a Bytecode HAR

A bytecode HAR contains the .abc bytecode file, resource files, configuration file, readme, changelog, and license file. It provides higher security for publication to the ohpm repository.

Since bytecode HARs contains compiled .abc bytecode, they do not require syntax checking and recompilation during builds when used as dependencies by other app modules (HAPs or HSPs). This results in faster builds and improved code security compared to source code HARs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/i9vXqwiHT2iGqOSnD1rN-w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B8FBFC6BCC47DF283FF361549B84E50EF66A28C0951B95B15441ADF5A48E61DA)

Building bytecode HARs, which are in binary format, takes more time than building non-bytecode HARs.

## Benefits

-   Bytecode HARs protect against code leakage and make it harder for others to reverse-engineer your code.

-   Integrating bytecode HARs developed with ArkTS/TS into HAPs or HSPs speeds up syntax checking and conversion, improving overall build performance.
-   Bytecode HARs reduce the node process overhead during compilation, minimizing memory usage.
-   HARs generated in the JS language using other code generation tools can be built into bytecode HARs. When integrated into HAPs or HSPs, these bytecode HARs reduce the number of files and code processed during compilation, thereby lowering memory usage and improving build performance.

## When to Use

Technically, all source code HARs can be switched to bytecode HARs can be converted to bytecode HARs in any order. However, due to the characteristics of bytecode HAR compilation and integration, converting to bytecode HARs in recommended scenarios or sequences may yield better performance and memory benefits. Here are the recommended scenarios for converting to bytecode HARs:

-   For external SDK vendors and in high-security scenarios, using bytecode HARs help reduce the risk of source code leakage.
-   In multi-repo development, publishing dependent HARs as bytecode HARs streamlines the build process (HAP) of the main project.
-   In mono-repo development, if your project includes large single code files or a significant amount of code generated by tools for second-party or third-party SDKs (HARs) written in ArkTS, TS, or JS, consider converting these HARs to bytecode HARs.
-   In memory-intensive scenarios, converting to bytecode HARs can help reduce memory usage.
-   For HARs written in ArkTS, TS, or JS that are at the lower levels of the dependency chain (leaf nodes) with minimal source code dependencies, converting these to bytecode HARs can yield significant benefits.

## Constraints

-   The dependencies used by the bytecode HAR must be configured under **dependencies** or **dynamicDependencies** in the **oh-package.json5** file of the current module. Otherwise, a runtime error may occur when the bytecode HAR is integrated. If an error occurs, you can configure **ohos.byteCodeHar.integratedOptimization** in **hvigor-config.json5** and recompile the module. For details, see [Compilation Behavior Differences](../adding-dependencies/document.md#section957371853712).
-   The dependency name specified in the **oh-package.json5** file of the bytecode HAR must match the package name specified in the **oh-package.json5** file of the corresponding dependency package.
-   If your project depends on any bytecode HAR, set [useNormalizedOHMUrl](../../configuration-files/project-level-build-profile-json5-file/document.md#section13181758123312) in the **build-profile.json5** file of the project to **true**.
-   When a HAP, an HSP, or a HAR depends on a bytecode HAR, the dependency name specified in the **oh-package.json5** file of the HAP/HSP/HAR must match the name specified in the **oh-package.json5** file of the bytecode HAR.
-   To import a bytecode HAR in HAP, HSP, or HAR code, you must make sure the dependency name (_**yyy**_) specified in the **import _xxx_ from '_yyy_'** statement must match the name specified in the **oh-package.json5** file of the current module exactly, including capitalization.
-   When a bytecode HAR is used as a dependency, its **compatibleSdkVersion** must not be higher than the project's **compatibleSdkVersion**.

## Procedure

1.  Set **useNormalizedOHMUrl** in the project-level **build-profile.json5** file to **true**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/XClouPFPTeK2jj2XJtXepg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AFCBA764D2627138BF0124B5D1608C668985FEED73D91D1E8EB4B69E20D4AE42)
    
    Since DevEco Studio NEXT Beta1 (5.0.3.800), the default value of **useNormalizedOHMUrl** and **byteCodeHar** is **true**, and therefore, you can skip steps 1 and 2.
    
    {
      "app": {
        "products": \[
          {
             "buildOption": {
               "strictMode": {
                 "useNormalizedOHMUrl": true
               }
             }
          }
        \]
      }
    }
    
2.  Set **byteCodeHar** in the **build-profile.json5** file of the HAR to **true**.
    
    {
      "buildOption": {
        "arkOptions": {
          "byteCodeHar": true
        }
      }
    }
    
3.  Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/szKM90QLSIKNF-eyppBofQ/en-us_image_0000002501070134.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE41FEBBF3638C8F8D386EF8F0706764713D8D833D6E735E73CF665EA5210926) in the upper right corner and set **Build Mode** to **<Default>**. This setting automatically switches between release mode for App Packs and debug mode for HAPs, HSPs, or HARs.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/OI3k0OYZRYeMebnFfBADoQ/en-us_image_0000002501070126.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F88CCFE8FB557DD5C5DFB3F0B0E46D579F49E0C65FA6F7229086877FC7758A3C)
    
4.  (Optional) To protect code assets in release build mode, enable obfuscation as follows: In the module-level **build-profile.json5** file, set the **enable** field under **obfuscation/ruleOptions** in the **buildOptionSet** configuration for **release** to **true**. For details about obfuscation and related rules, see [Code Obfuscation](../../using-obfuscation-for-code-hardening/document.md).
    
    {
      "apiType": "stageMode",
      "buildOption": {
      },
      "buildOptionSet": \[
        {
          "name": "release",
          "arkOptions": {
            // Obfuscation parameters
            "obfuscation": {
              "ruleOptions": {
                // true means to enable obfuscation, and false means the opposite. The default value is false since version 5.0.3.600.
                "enable": true,
                // Obfuscation rule files
                "files": \[
                  "./obfuscation-rules.txt"
                \]
              },
              // Specify the obfuscation configuration file to be used for building the library or a project that depends on the library.
              "consumerFiles": \[
                "./consumer-rules.txt"
              \]
            }
          },
        },
      \],
      "targets": \[
        {
          "name": "default"
        }
      \]
    }
    
5.  (Optional) To customize the files packed into the HAR product, open the **build-profile.json5** file of the HAR module and configure the **include** or **exclude** field using glob patterns supported.
    
    "buildOption": {
      "packingOptions": {
        "asset": {
          "include": \["./src/router.json5","router.json5"\],    // Specify the files to be included in the HAR product.
          "exclude": \["./config/\*"\]     // Specify the files to be excluded from the HAR product.
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/38ZHOO2WQnmTmDFnaQuhdg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94E18B4A2D3C1CC0E43CE544ACE75C94110C49BD91F11665C281E5325E1D3054)
    
    -   The following directories are still excluded from the HAR product even when listed in the **include** field: **node\_modules**, **oh\_modules**, **.preview**, **build**, **.cxx**, and **.test**.
    -   The **oh-package.json5** file is still included in the HAR product even when listed in the **exclude** field.
    
6.  Select the root directory of the HAR and choose **Build** > **Make Module '<_module-name_\>'** to start building.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/aGnomp_XSUyFswqqWHk-6Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=923C3B0B9DD620A03E610FD4DE592CA9A5B8A94860D9972D8D58408BE4589DE6)
    
    If the **version** field in the module-level **oh-package.json5** file of the HAR package is modified, choose **Build** > **Clean Project** in DevEco Studio and then perform a full rebuild.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/HkbLYJ2zQ5m2CYL3efM0BQ/en-us_image_0000002500910290.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A39C39AAA4299F9383A5EB679B910F72E2D084200CC637615227CF200411C898)
    
    After the build is complete, the .har file is generated in the **build** folder.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/w3HOyaveQSeE1J4RT95REw/en-us_image_0000002532670203.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B8A8BD18B6CF1A51C32CFAADB5092E882E13FF2C7754B0692F1CF0A0BC7823F)
    
    After the .har file is decompressed, its structure is as follows.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/2QJOmEjpQtWxhCr-zdFiVQ/en-us_image_0000002532750167.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCCE48002784E473C6335AA04E2FE85F4DAFFC2305A03BC34231AB5E1D191CB0)
    

#### Building a Source Code HAR

## Building in Debug Mode

In debug mode, the build product is a HAR package containing source code, resource files, and configuration files, which facilitates local debugging. The package does not contain files from **build**, **node\_modules**, **oh\_modules**, **.cxx**, **.preview**, **.hvigor**, **.gitignore**, **.ohpmignore**, files configured in **.gitignore** or **.ohpmignore**, and the **CMakeLists.txt** file from C++ projects.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/6aGmmLpgTL-Zsf6KQK3U5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0D3EF5EDD11FE55262D9D530809E61AF1FBAA57B9AEEDBB33B019FAE337B537)

-   The source code HAR package contains source code. Exercise caution when distributing the package to prevent source code leakage.
-   For a native project, the native build product in debug mode does not contain debugging information or symbol tables. For details about how to debug the product, see [Debugging Third-Party Code](../../../coding-and-debugging/debugging-your-app/code-debugging/debugging-third-party-library-source-code/document.md).
-   Since version 5.0.3.403, using relative paths to reference code files across modules is not recommended. If a historical project has such a cross-module reference, a warning will be reported. In this case, move the referenced file to the current module and rebuild.
-   Since version 5.0.3.403, HAR builds in both debug and release modes follow the same syntax validation rules. If historical projects have ArkTS syntax errors, modify the code according to the error messages to comply with ArkTS specifications.

1.  Set **byteCodeHar** in the **build-profile.json5** file of the HAR to **false**.
    
    {
      "buildOption": {
        "arkOptions": {
          "byteCodeHar": false
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/-RBoi-32SJO8NPmQk8xW7Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F73F0BB05EC1F46DFABC33A911F928471D894A98A09146D3C8BDC3835C92E6A0)
    
    In versions earlier than DevEco Studio NEXT Beta1 (5.0.3.800), where the default value of **byteCodeHar** in the module-level **build-profile.json5** file is **false**, you can skip this step.
    
2.  Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/RTIeYsa6S2qo-bkKbkYbzQ/en-us_image_0000002501070130.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=874B85E89747FE2F3C71447F384C3961B662034F91259F336BCF3B2E0A216358) in the upper right corner, and set **Build Mode** to **debug**. The default build mode is **<Default>**, which uses release mode when building App Packs and debug mode when building HAPs, HSPs, or HARs.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/dSrTU74WSdqydaFx4P5OVw/en-us_image_0000002501070136.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F11BA6AA63712E20829FCEAEFCCFC90BBF5F63C29C26FC1EA65267D9656DA9FE)
    
3.  (Optional) To exclude certain source files or folders from the HAR product, create an .ohpmignore file in the module directory and list the files or folders to be excluded, or add them to the existing .gitignore file in the module directory. The .ohpmignore file supports regular expressions, and the .gitignore file supports glob patterns. DevEco Studio will then skip the specified files and folders during the build process.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/hrfrVQbZSLSohp_aSgD4mw/en-us_image_0000002500910304.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B541236C37B6C88A78EAF99A3B66A1DC4A4F0DEA17F465875C061ECEF08201FF)
    
4.  (Optional) To customize the files packed into the HAR product, open the **build-profile.json5** file of the HAR module and configure the **include** or **exclude** field using glob patterns supported. After the **include** or **exclude** field is configured, the **.gitignore** and **.ohpmignore** files do not take effect.
    
    "buildOption": {
      "packingOptions": {
        "asset": {
          "include": \["./src/router.json5","router.json5"\],    // Specify the files to be included in the HAR product.
          "exclude": \["./config/\*"\]     // Specify the files to be excluded from the HAR product.
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/4Xjgo_-GQECAppuxP-rlhA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A085476E67E808A1E32AB47C5D256122B7AD94C0FA80888B49B8454385361BE)
    
    -   The following directories are still excluded from the HAR product even when listed in the **include** field: **node\_modules**, **oh\_modules**, **.preview**, **build**, **.cxx**, and **.test**.
    -   The **oh-package.json5** file is still included in the HAR product even when listed in the **exclude** field.
    
5.  Select the root directory of the HAR and choose **Build** > **Make Module '<_module-name_\>'** to start building.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/WEpbuzoNQjm97b1JtNCrZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6FD64A67A11F9A44B706B72346A9AEAFA42302F16FFCE170A088711503DA693)
    
    If the **version** field in the module-level **oh-package.json5** file of the HAR package is modified, choose **Build** > **Clean Project** in DevEco Studio and then perform a full rebuild.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/dxU_qANuR1KMBZ0W4jcmvw/en-us_image_0000002532750171.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F38EB8C63D54213DF3F6933F8821427121B1E21B1E3F4F1424AFC2210DCBB135)
    
    After the build is complete, the .har file is generated in the **build** folder.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/TdOLKIw2RtO6wFil4YZGiw/en-us_image_0000002532750157.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51A2F91D6D2BBD00B433093A3EC4DD07D1CB2D321673ED8165DA27CEEF98E712)
    
    After the .har file is decompressed, its structure is as follows.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/xLVm4bzTREGNzGW5c977ZQ/en-us_image_0000002532750169.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCB0D160DC39879810E3AA2914BBDD8EF4EE36065926059435D06785640F48D4)
    

## Building in Release Mode

Since DevEco Studio NEXT Developer Beta3 (5.0.3.600), obfuscation is disabled by default, in which case the build product in release mode is the same as [in debug mode](#section197792874110).

To protect code assets, code obfuscation is recommended. When this feature is enabled, the build product is a JavaScript intermediate code HAR, which contains the obfuscated JavaScript intermediate code file, resource files, configuration file, readme, changelog, and license file. The type of HAR can be published to the ohpm repository.

1.  Set **byteCodeHar** in the **build-profile.json5** file of the HAR to **false**.
    
    {
      "buildOption": {
        "arkOptions": {
          "byteCodeHar": false
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/3J2IbMUjTGO6Ivr0D5lGhg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D3D001F31812D08F71313F6ACF135FE40D26E54A573DE13DBA119652D1A98A0D)
    
    In versions earlier than DevEco Studio NEXT Beta1 (5.0.3.800), where the default value of **byteCodeHar** in the module-level **build-profile.json5** file is **false**, you can skip this step.
    
2.  Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/zXILJPZaQWafGHo-hD3N8w/en-us_image_0000002532750175.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9D30E9FF4543992F10A3144A587A51792D42B38DE8B920204B1C1D6BAE8BC5D) in the upper right corner, and set **Build Mode** to **release**. The default build mode is **<Default>**, which automatically switches between release mode for App Packs and debug mode for HAPs, HSPs, or HARs.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/_1yQUA-ERJGJlyumlLc-zg/en-us_image_0000002501070138.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7EF620BD4AB7FE6A6A15DD6AEC76311E61E647E43126EBC8413F3F4DA4041D2A)
    
3.  To protect code assets, enable obfuscation as follows: In the module-level **build-profile.json5** file, set the **enable** field under **obfuscation/ruleOptions** in the **buildOptionSet** configuration for **release** ([build mode](../../customizing-your-build/customizing-build-options/introduction/document.md#section192461528194916)) to **true**. For details about obfuscation and related rules, see [Code Obfuscation](../../using-obfuscation-for-code-hardening/document.md).
    
    {
      "apiType": "stageMode",
      "buildOption": {
      },
      "buildOptionSet": \[
        {
          "name": "release",
          "arkOptions": {
            // Obfuscation parameters
            "obfuscation": {
              "ruleOptions": {
                // true means to enable obfuscation, and false means the opposite. The default value is false since version 5.0.3.600.
                "enable": true,
                // Obfuscation rule files
                "files": \[
                  "./obfuscation-rules.txt"
                \]
              },
              // Specify the obfuscation configuration file to be used for building the library or a project that depends on the library.
              "consumerFiles": \[
                "./consumer-rules.txt"
              \]
            }
          },
        },
      \],
      "targets": \[
        {
          "name": "default"
        }
      \]
    }
    
4.  (Optional) To customize the files packed into the HAR product, open the **build-profile.json5** file of the HAR module and configure the **include** or **exclude** field using glob patterns supported.
    
    "buildOption": {
      "packingOptions": {
        "asset": {
          "include": \["./src/router.json5","router.json5"\],    // Specify the files to be included in the HAR product.
          "exclude": \["./config/\*"\]     // Specify the files to be excluded from the HAR product.
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/hHl-B2Q1TUaK202Lhn4QCA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FBDA0C3ED1805FB6FBF972B03438CAA0BF0380B28272615F3520818435AA1B8A)
    
    -   The following directories are still excluded from the HAR product even when listed in the **include** field: **node\_modules**, **oh\_modules**, **.preview**, **build**, **.cxx**, and **.test**.
    -   The **oh-package.json5** file is still included in the HAR product even when listed in the **exclude** field.
    
5.  Select the root directory of the HAR and choose **Build** > **Make Module '<_module-name_\>'** to start building.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/_2PlofYdQ8SQ-zNfYFKEyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80F08DC800050F25D82CB2EF5DB40DF6C0C7A268872A6445F79479B058FF9D73)
    
    If the **version** field in the module-level **oh-package.json5** file of the HAR package is modified, choose **Build** > **Clean Project** in DevEco Studio and then perform a full rebuild.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/WVCr5pxFTdiGcmc1I12h1g/en-us_image_0000002501070128.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F48DC549237128B58D84768E0E6F67A505D6F02E228D1745EBB3B29CB345741)
    
    After the build is complete, the .har file is generated in the **build** folder.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/2gqDAZGYQkCgm_X8vz6dzA/en-us_image_0000002500910302.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D3F80E6A009DECA5DD01D7D45C225ED6E93F886084A59D1FB53CD98A5CB08AC)
    
    After the .har file is decompressed, its structure is as follows.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/eiteP4qrQ8Cg62AdR6dGEg/en-us_image_0000002500910308.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4C9A286B56A001F97417F1A2B599428E58685E51B3C0C8DBAEB30899E2E62E15)
    

#### Signing a HAR

You can sign a HAR during the build process,

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/_im7txZASdyqJZTouSkQMA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B44A09283BF5AFD9D00CE66C7B09F5FFAEEEF096B6692799886AD47C585FC22)

1\. This feature is supported only when **compatibleSdkVersion** is **5.0.0(12)** or higher.

2\. To use this feature, ensure that the daemon is enabled for the current project: Choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Build, Execution, Deployment** > **Build Tools** > **Hvigor** and select **Enable the Daemon for tasks**.

1.  In **hvigor-config.json5**, enable the feature for building a signed HAR:
    
    {
      "properties": {
        "ohos.sign.har": true
      }
    }
    
2.  Configure the project's signature information. For details, see [Configuring Signature Information](../../../app-release/release/document.md#section793484619307).
3.  Select the root directory of the HAR and choose **Build** > **Make Module '<_module-name_\>'** to start building.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/eWkn77UeS9SDzkL4vVTm8w/en-us_image_0000002532750165.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19724F0C4C6AE45D548EC27C54E052EEA99778D30DDE41A3E6916F77A33D4854)
    
    After the build is complete, the signed .har file is generated in the **build** folder.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/iC6g63cERXyi95dIQM8aEg/en-us_image_0000002532670209.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F806DFA099AE83770D81F6FDF6497E761AC643BB053C93F06A02BE388592499C)
