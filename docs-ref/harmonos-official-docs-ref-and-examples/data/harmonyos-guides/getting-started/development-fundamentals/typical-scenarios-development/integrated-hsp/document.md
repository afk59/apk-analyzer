# Integrated HSP

The integrated HSP is an intermediate build product of the intra-application HSP. It aims to solve the strong coupling between the bundle name and signature of the user.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/mSJ13qohQPi6mPnEVBtYOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43F9CC64E348CD25585ECE37AFAA9AF2B80699587D9890D73B75B314BA8558C1)

The HSP can be used only by projects with the same bundle name, but the integrated HSP can be used by projects with different bundle names.

When using the integrated HSP, the user needs to re-sign the integrated HSP with the signature file and install the re-signed integrated HSP first.

#### Use Scenario

If multiple applications share the same basic capability, such as a logging module, they can share a single logging module to save development costs and enable code and resource sharing. In this case, the in-application HSP can be used to provide the capabilities. Due to the limitations of the in-application HSP, each application needs to adjust its bundle name and re-sign the HSP with its own signature to build a new HSP for the current application. This means that for each additional application, the bundle name adjustment and re-signing operations must be performed, resulting in a cumbersome signature and packaging process.

With the integrated HSP, the bundle name adjustment and re-signing are automatically handled during the DevEco Studio compilation process. You do not need to concern yourself with repeated signing operations and can focus on function development.

#### Constraints

-   The integrated HSP is only available for the [stage model](../../application-package-fundamentals/application-package-structure/application-package-structure-in-stage-model/document.md).
-   The integrated HSP is supported since API version 12.
-   The integrated HSP must use the standardized OHMUrl format. You need to set the **useNormalizedOHMUrl** field under [strictMode](../../../../building-an-app/configuration-files/project-level-build-profile-json5-file/document.md#section13181758123312) to **true** in the project-level [build-profile.json5 file](../../../../building-an-app/configuration-files/project-level-build-profile-json5-file/document.md).

#### Development Instructions

## Configuring the Integrated HSP

1.  Project configuration: Set **useNormalizedOHMUrl** to **true** in the project-level **build-profile.json5** file.
    
    {
      "app": {
        "signingConfigs": \[
        \],
        "products": \[
          {
            "name": "default",
            "signingConfig": "default",
            "targetSdkVersion": "5.1.1(19)",
            "compatibleSdkVersion": "5.1.1(19)",
            "runtimeOS": "HarmonyOS",
            "buildOption": {
              "strictMode": {
                // ...
                "useNormalizedOHMUrl": true,
              }
            }
          }
        \],
        // ...
      },
      // ...
    }
    
2.  Module configuration: Set **integratedHsp** to **true** in the module-level [build-profile.json5 file](../../../../building-an-app/configuration-files/module-level-build-profile-json5-file/document.md) to specify the built HSP module as the integrated HSP.
    
    // library/build-profile.json5
    {
      "apiType": "stageMode",
      // ...
      "buildOptionSet": \[
        {
          // ...
          "arkOptions": {
            "integratedHsp": true,
            // ...
          },
        },
      \],
      // ...
    }
    
3.  Package the configuration (.tgz package).
    
    (1) Configure project signature information. For details, see [Configuring a Debug Signature](../../../../coding-and-debugging/configuring-a-debug-signature/document.md).
    
    (2) Configure the release mode.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/_25Wle7WT4-JgIq-xygVZw/en-us_image_0000002568684053.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C83ABC3D22C3B96052FB6129E5A1C6D1E9B49BA9C0EA2D49CF50F95DEB1602BE)
    
    (3) Select the **library** directory and choose **Build** > **Make Module 'library'**.
    

## Integrating the HSP

1.  Directory creation and file copying: Create a **libs** directory under the **entry** directory and copy the .tgz package to the created directory.
    
2.  Project dependency configuration: Add dependencies to the **oh-package.json5** configuration file of the main module of the user.
    
    "dependencies": {
      "library": "file:./libs/library-default.tgz"
    },
    
3.  Project configuration: Set **useNormalizedOHMUrl** to **true** in the project-level **build-profile.json5** file.
    
    {
      "app": {
        "signingConfigs": \[
        \],
        "products": \[
          {
            "name": "default",
            "signingConfig": "default",
            "targetSdkVersion": "5.1.1(19)",
            "compatibleSdkVersion": "5.1.1(19)",
            "runtimeOS": "HarmonyOS",
            "buildOption": {
              "strictMode": {
                // ...
                "useNormalizedOHMUrl": true,
              }
            }
          }
        \],
        // ...
      },
      // ...
    }
    
4.  Configure the signature.
    
    Before installing and running an application, the user must configure the project signature information. For details, see [Configuring a Debug Signature](../../../../coding-and-debugging/configuring-a-debug-signature/document.md).
    
5.  [Install and run](../../../../coding-and-debugging/running-your-app-on-a-local-real-device/document.md).
