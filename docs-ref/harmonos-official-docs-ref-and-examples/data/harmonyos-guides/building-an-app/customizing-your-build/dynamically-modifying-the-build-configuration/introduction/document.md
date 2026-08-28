# Introduction

Hvigor supports the reception of some build configurations in the **hvigorfile.ts** file to achieve dynamic configuration of the build process and to enable it into the build process and results.

There are two methods to implement this capability:

-   Based on the hvigor hook capability, dynamically configure settings through the plug-in context. (Recommended)
-   Export dynamic configurations in **hvigorfile.ts** using the **overrides** keyword. (Not recommended)

#### Using Hooks and Plug-in Context to Implement Dynamic Configuration

Hvigor lets you operate the following configurations read from the disk within the Hvigor hook in the stage model:

-   **build-profile.json5** file for each **hvigorNode**
-   **module.json5** file
-   **app.json5** file
-   **dependency**, **devDependency**, **dynamicDependency**, and **version** settings in the module-level **oh-package.json5** files

Currently, you can directly access and modify configurations through the context provided by the **hvigor** object to achieve dynamic setting of build configurations and to enable them in the build process and results.

In **hvigorfile.ts** or **hvigorconfig.ts** files, you can use the APIs provided by Hvigor to implement this capability.

Compared to the **overrides** capability mentioned below, dynamically modifying signatures and build configurations through hooks and plugin context is more flexible, easier to understand, and more comprehensive in functionality. This method is recommended. For details, see [(Recommended) Using Hooks and Plug-in Context to Implement Dynamic Configuration](../examples/document.md#section67131365449).

#### Exporting Dynamic Configurations in hvigorfile.ts Using the overrides Keyword

In **hvigorfile.ts**, receive build configurations in the **config.ohos** property of the exported object:

export default {  
    system: hapTasks,  
    config: {  
        ohos: {
            ...
        }    
    }
}

Currently, the **config.ohos** property in the project-level **hvigorfile.ts** file provides the following fields:

-   **overrides**: defines the fields that will override the corresponding existing configurations during the build process.
    -   **signingConfig**: indicates signing configuration and corresponds to [signingConfigs](../../../configuration-files/project-level-build-profile-json5-file/document.md#section153288223224) in **build-profile.json5**.
        -   type
        -   material
            -   certpath
            -   storePassword
            -   keyAlias
            -   keyPassword
            -   profile
            -   signAlg
            -   storeFile
    -   **appOpt**: corresponds to the configuration field in [app.json5](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/app-json5-configuration-file/document.md).
        -   bundleName
        -   bundleType
        -   icon
        -   label
        -   vendor
        -   versionCode
        -   versionName

Currently, the **config.ohos** property in the module-level **hvigorfile.ts** file provides the following fields:

-   **overrides**: defines the fields that will override the corresponding existing configurations during the build process.
    -   **buildOption**: corresponds to [buildOption](../../../configuration-files/module-level-build-profile-json5-file/document.md#section1010733210421) in **build-profile.json5**.
        -   arkOptions
        -   externalNativeOptions
        -   napiLibFilterOption
        -   nativeLib
        -   resOptions
        -   sourceOption

Parameters configured in **overrides** are given a higher priority than the corresponding parameters in other configuration items.
