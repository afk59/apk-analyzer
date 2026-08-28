# Adding Dependencies

Apps/Atomic services support installation, sharing, and code distribution, and project dependency management through ohpm, a package manager. This section describes how to configure dependencies for your project, as well as the processing logic and compilation results of different configuration modes during compilation.

To specify the dependencies for your project or module, you must list them under the **dependencies** (production dependencies) or **devDependencies** (development dependencies) field in the **oh-package.json5** file of the project or module. The dependencies can be any of the following types: remote third-party package, local module, and local HAR/HSP. If an HSP needs to be loaded or executed only under certain conditions, add it under the **dynamicDependencies** field in the **oh-package.json5** file. The following uses **dependencies** as an example. For details about dependency settings, see [oh-package.json5](../../../command-line-tools/using-ohpm/oh-package-json5/document.md).

#### Configuring Dependencies

## Referencing a Remote Third-Party Package

Set the package as a dependency in the **oh-package.json5** file of the target module. The following is a configuration example:

"dependencies": {
  "@ohos/lottie": "^2.0.0"
}

## Local Module

You can set the dependency on a local module in the **oh-package.json5** file of the module in either of the following ways:

-   Setting the local folder path. Example:
    
    "dependencies": {
      "folder": "file:../folder"
    }
    
-   Setting the local module name, for example, **moduleA** (supported since DevEco Studio 6.0.0 Beta1).
    
    "dependencies": {
      "moduleA": "@module:moduleA"
    }
    

## Referencing a Local HAR or HSP

-   Referencing a HAR:
    
    "dependencies": {
      "package": "file:../package.har"
    }
    

-   Referencing an HSP (A .tgz package is generated when the HSP is built in release mode.):
    
    "dependencies": {
      "package": "file:../package.tgz"
    }
    

After the dependency is set, run the **ohpm install** command to install it to the **oh\_modules** directory of the target module.

#### Compilation Behavior Differences

You can specify dependencies in the following fields based on the current dependency configuration specifications:

-   **dependencies**, **dynamicDependencies**, and **devDependencies** in the project-level **oh-package.json5** file
-   **dependencies**, **dynamicDependencies**, and **devDependencies** in the module-level **oh-package.json5** file.

Although all the preceding fields can be used to specify dependencies, their processing logic and compilation results differ depending on the field used. For example:

1.  Create a project and a HAR module.
2.  In **dependencies** of the entry module-level **oh-package.json5** file, set the local HAR folder path as a dependency, then compile the entry module.
    
    "dependencies": {
      "har": "file:../har"
    }
    
3.  In **devDependencies** of the entry module-level **oh-package.json5** file, set the local HAR folder path as a dependency, then compile the entry module.
    
    "devDependencies": {
      "har": "file:../har"
    }
    

Compare the build logs of steps 2 and 3. You will find that step 2 prints HAR-related logs (as shown in the red box below), while step 3 does not print any HAR-related logs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/-pF2OfMSRfauufIMDbbe5A/en-us_image_0000002532750275.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0435A8EF46E86B37E8DD8B8965E19F59E06331E3F7794D3898A1E310C2EB671E)

The differences above are merely log differences. To ensure normal compilation, you are not advised to configure dependencies in the project-level **oh-package.json5** file. The specific compilation processing logic and potential abnormal results will be illustrated in the table below.

Terms are defined as follows and used only in this document:

-   Third-party package dependency: Specify dependencies using [remote third-party packages](#section0999112011818) and [local HAR/HSP packages](#section636814917176).
-   Local dependency: Specify dependencies using [local folder paths](#section91117398178).
-   Bytecode HAR with **bundledDependencies** enabled: Set **bundledDependencies** under **buildOption**/**arkOptions** in the **build-profile.json5** file of the bytecode HAR to **true**.
-   Configuration of a dependency: Configure **resources**, **workers**, **runtimeOnly**, **UIAbilities**, **ExtensionAbilities**, C++ compilation products, and routing table for the dependency.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/S_gGoD9cTsuYwOechrx1Vw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D834A18D4E9AA4D31DD01A5F6A3D155B220A47742479E3B28D643FAE9B7CB32)

-   In the table below, **devDependencies** refers to **devDependencies** in both the project-level and module-level **oh-package.json5** files.
-   This table only explains scenarios that may lead to compilation abnormalities and does not cover scenarios with normal compilation (for example, configuring **dependencies** in the module-level **oh-package.json5** file).

**Table 1** Compilation behavior differences
| 
Dependency

 | 

Compiling HAPs

 | 

Compiling HSPs

 | 

Compiling Bytecode HARs with bundledDependencies Disabled

 | 

Compiling Bytecode HARs with bundledDependencies Enabled

 |
| :-- | :-- | :-- | :-- | :-- |
| 

Source code HAR

 | 

Third-party package dependency

 | 

**devDependencies**

 | 

1

 | 

1

 | 

**2**

 | 

1

 |
| 

Project-level **dependencies**

 | 

/

 | 

/

 | 

**3**

 | 

**3**

 |
| 

Local dependency

 | 

**devDependencies**

 | 

1

 | 

1

 | 

**2**

 | 

1

 |
| 

Project-level **dependencies**

 | 

/

 | 

1

 | 

**2**

 | 

1

 |
| 

Bytecode HAR

 | 

Third-party package dependency

 | 

**devDependencies**

 | 

**2**

 | 

**2**

 | 

**2**

 | 

**2**

 |
| 

Project-level **dependencies**

 | 

/

 | 

/

 | 

**3**

 | 

**3**

 |
| 

HSP

 | 

Third-party package dependency

 | 

**devDependencies**

 | 

1

 | 

1

 | 

**2**

 | 

**1**

 |
| 

Project-level **dependencies** and **dynamicDependencies**

 | 

/

 | 

/

 | 

/

 | 

/

 |
| 

Local dependency

 | 

**devDependencies**

 | 

**1**

 | 

**1**

 | 

**2**

 | 

**1**

 |
| 

Project-level **dependencies** and **dynamicDependencies**

 | 

/

 | 

1

 | 

**2**

 | 

**1**

 |

The meanings of the symbols in the table are as follows:

-   1: Only the code files (such as .ets/.ts/.js files) of the dependency are compiled; its configuration data is not collected. This may lead to compilation or runtime errors.
-   2: The dependency is not collected at all, resulting in compilation errors.
-   3: The compilation succeeds, but runtime errors may occur during later integration.
-   /: Both compilation and runtime behavior are normal.

To optimize the scenarios marked with bold symbols (**1**, **2**, or **3**) in the table, since DevEco Studio 5.1.1 Beta1, the **ohos.byteCodeHar.integratedOptimization** field has been available in the **hvigor-config.json5** file. Enabling this field optimizes the underlying dependency collection logic for these scenarios.

While this feature improves dependency collection, it does not optimize the logic for collecting the dependency configuration data. Consequently, in the scenarios marked with bold symbols, full optimization (with no compilation or runtime exceptions guaranteed) is only achievable under both of the following conditions: (1) The dependency in question is a compiled bytecode HAR. (2) The dependency is explicitly declared in the project-level **dependencies** or **dynamicDependencies** configuration. For any bold-marked scenario not meeting both of these conditions, compilation or runtime exceptions may occur.

"properties": {
  "ohos.byteCodeHar.integratedOptimization": true
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/aZD_yfqZRWCCg0DPG5aMlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5215F59C93BD08A263DFD146AF2FB6C6144CC6430D2D6FA8C301230EE7ADEF7)

This field must be configured for both the dependency package provider and integrator.

Based on the above, you are advised to:

-   Configure the dependencies used by the current module in its **oh-package.json5** file.
-   Avoid configuring any dependencies other than TypeScript type declaration packages (for example, **@types/commonmark**) for auxiliary syntax checking in **devDependencies**.
