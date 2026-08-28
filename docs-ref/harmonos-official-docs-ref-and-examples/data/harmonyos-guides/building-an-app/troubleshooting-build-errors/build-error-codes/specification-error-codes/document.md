# Specification Error Codes

#### 00306001 File Path Exceeds Maximum Length Limit

**Error Message**

The length of path exceeds the maximum length: XXX.

**Symptom**

The file path exceeds the maximum length limit.

**Possible Causes**

The total length of the file path exceeds the limit imposed by the operating system.

**Solution**

1.  Shorten the root path of the project.
2.  Simplify the project name.
3.  Simplify the module name.
4.  Simplify the target name.

#### 00306002 Chinese Characters Not Allowed in the Project Path

**Error Message**

The Node directory and node name cannot contain Chinese characters.

**Symptom**

The project path cannot contain Chinese characters.

**Possible Causes**

The project path contains Chinese characters.

**Solution**

Remove the Chinese characters from the project path.

#### 00306003 Invalid Project Path

**Error Message**

Invalid project path. Current path does not match: XXX.

**Symptom**

The project path is invalid.

**Possible Causes**

The project path contains Chinese characters or special characters.

**Solution**

Modify the project path and ensure that the path contains only letters, digits, hyphens (-), underscores (\_), periods (.), parentheses (), spaces, or at signs (@).

#### 00306004 Unsupported API Version

**Error Message**

The compatibleSDKVersion XXX cannot be smaller than YYY declared in library ZZZ or

The project's compatibleSdkVersion: XXX cannot be lower than the minimum compatible version YYY required by the dependencies: ZZZ.

**Symptom**

The version specified by **compatibleSdkVersion** of the current project cannot be lower than the minimum compatible version declared in the third-party library.

**Possible Causes**

The version specified by **compatibleSdkVersion** of the current project is lower than the minimum compatible version (**compatibleSdkVersion**) declared when the third-party library was packaged.

**Solution**

Use either of the following methods:

-   Update **compatibleSdkVersion** of the current project to a version greater than or equal to the version declared in the third-party library.
-   Lower **compatibleSdkVersion** of the third-party library. Before packaging your app, modify **compatibleSdkVersion** in the library's own project-level **build-profile.json5** file to make the library itself compatible with an earlier SDK version.
-   Remove the third-party libraries that are incompatible with **compatibleSdkVersion** of the project, or use third-party libraries that require an earlier SDK version.

#### 00306005 Duplicate output Name

**Error Message**

Failed to build the app due to duplicate customized output names: XXX. At file: XXX.

**Symptom**

The custom **output** name is duplicate. As a result, the application fails to be built.

**Possible Causes**

The **output** name customized in the **target** configuration of the module is duplicate.

**Solution**

Check the **targets** configuration in the module-level **build-profile.json5** file, ensuring that each **output** name is unique.

#### 00306006 TargetESVersion Only Supported by API Version 12 or Later

**Error Message**

Unsupported API version. TargetESVersion is supported after API 12. At file: XXX.

**Symptom**

**TargetESVersion** is only supported by API version 12 and later. The API version of the current project is earlier than API version 12.

**Possible Causes**

The **compileSdkVersion** or **compatibleSdkVersion** of the current project is earlier than API version 12.

**Solution**

Check the **compileSdkVersion** and **compatibleSdkVersion** configurations in the project-level **build-profile.json5** file, ensuring that the versions are API version 12 or later.

#### 00306007 Only HarmonyOS Supported for runtimeOS of Insight Intent Projects

**Error Message**

The runtimeOS that supports the insightintent project can only be HarmonyOS. At file: XXX.

**Symptom**

**runtimeOS** of the insight intent project only supports **HarmonyOS**.

**Possible Causes**

**runtimeOS** of the insight intent project is not set to **HarmonyOS**.

**Solution**

Check the project-level or module-level **build-profile.json5** file and set **runtimeOS** to **HarmonyOS**.

#### 00306008 Insight Intents Not Supported by the API Version

**Error Message**

Unsupported API version. Insight intent is supported after API 11. At file: XXX.

**Symptom**

Insight intents are supported in projects of API version 11 or later.

**Possible Causes**

The **compileSdkVersion** or **compatibleSdkVersion** of the current project is earlier than API version 11.

**Solution**

Check the **compileSdkVersion** and **compatibleSdkVersion** configurations in the project-level **build-profile.json5** file, ensuring that the versions are API version 11 or later.

#### 00306009 Insight Intents Not Supported by the SDK Version

**Error Message**

Unsupported SDK version. Insight intent is supported after API 11. At file: XXX.

**Symptom**

Insight intents are supported in projects of API version 11 or later.

**Possible Causes**

The SDK version is earlier than API version 11.

**Solution**

Download the latest [DevEco Studio](https://developer.huawei.com/consumer/en/download/deveco-studio) from the official website.

#### 00306010 ArkData Not Supported by the SDK Version

**Error Message**

The current SDK version does not support ArkData. At file: XXX.

**Symptom**

The current SDK version does not support ArkData.

**Possible Causes**

The current SDK version does not support ArkData.

**Solution**

Download the latest [DevEco Studio](https://developer.huawei.com/consumer/en/download/deveco-studio) from the official website.

#### 00306011 UI Syntax Not Supported by the SDK Version

**Error Message**

The current SDK version does not support uiSyntax. At file: XXX.

**Symptom**

The current SDK version does not support the UI syntax.

**Possible Causes**

The current SDK version does not support the UI syntax.

**Solution**

Download the latest [DevEco Studio](https://developer.huawei.com/consumer/en/download/deveco-studio) from the official website.

#### 00306012 Unsupported Dynamic Imports

**Error Message**

Invalid configuration of runtimeOnly in XXX. At file: XXX.

**Symptom**

The **runtimeOnly** configuration is invalid. Dynamic import is not supported.

**Possible Causes**

**runtimeOnly** can be configured only for Stage model projects of API version 11 or later.

**Solution**

1.  Set **compatibleSdkVersion** in the project-level **build-profile.json5** file to **11** or larger.
2.  Set **apiType** in the module-level **build-profile.json5** file to **stageMode**.

#### 00306013 Atomic Service Development Not Supported for OpenHarmony Projects in Stage Model

**Error Message**

Atomic service development is not supported for OpenHarmony stage model. At file: XXX

**Symptom**

Atomic service development is not supported for OpenHarmony projects in Stage model.

**Possible Causes**

**runtimeOS** of the atomic service project is set to **OpenHarmony**.

**Solution**

If you need to develop an atomic service, change **runtimeOS** in the project-level **build-profile.json5** file to **HarmonyOS**.

#### 00306014 Atomic Service Development Not Supported by the API Version

**Error Message**

Atomic service development is not supported for compileSdkVersion/compatibleSdkVersion less than api 11. At file: XXX.

**Symptom**

**compileSdkVersion** or **compatibleSdkVersion** is earlier than API version 11, which does not support the development of atomic services.

**Possible Causes**

**compileSdkVersion** or **compatibleSdkVersion** of the project is earlier than API version 11, which does not support the development of atomic services.

**Solution**

Check the **compileSdkVersion** and **compatibleSdkVersion** configurations in the project-level **build-profile.json5** file, ensuring that the versions are API version 11 or later.

#### 00306015 Native Code Development Not Supported in Atomic Services

**Error Message**

Atomic service development does not support Native development. At file: XXX.

**Symptom**

Native code development is not supported in the atomic service.

**Possible Causes**

The current project file _XXX_ contains **externalNativeOptions**, which is related to native code development.

**Solution**

Remove **externalNativeOptions** from the atomic service project.

#### 00306016 Only ArkTS Supported for Atomic Service Development

**Error Message**

Atomic service development only supported arkTS widget. At file: XXX.

**Symptom**

Only ArkTS components can be used for atomic service development.

**Possible Causes**

JS components are used in the project.

**Solution**

Remove the code and configuration related to the JS components from the project.

#### 00306017 Integrated HSP Not Supported by the API Version

**Error Message**

The integratedHsp can only be used in API 12 and later. At file: XXX.

**Symptom**

The integrated HSP is supported only by API version 12 and later.

**Possible Causes**

The **compileSdkVersion** or **compatibleSdkVersion** of the current project is earlier than API version 12.

**Solution**

Check the **compileSdkVersion** and **compatibleSdkVersion** configurations in the project-level **build-profile.json5** file, ensuring that the versions are API version 12 or later.

#### 00306018 useNormalizedOHMUrl Must Be Set to true When the Integrated HSP Is Used

**Error Message**

The integratedHsp is available only when useNormalizedOHMUrl is set to true. At file: XXX.

**Symptom**

**useNormalizedOHMUrl** must be set to **true** when the integrated HSP is used.

**Possible Causes**

**useNormalizedOHMUrl** is set to **false**.

**Solution**

Set **useNormalizedOHMUrl** in the project-level **build-profile.json5** file to **true**.

#### 00306019 bundledDependencies Only Supported in the Bytecode HAR

**Error Message**

Only the byte code har supports to configure the bundledDependencies. At file: XXX.

**Symptom**

**bundledDependencies** can only be configured in the bytecode HAR.

**Possible Causes**

1.  The **useNormalizedOHMUrl** attribute is not configured in **buildOption.strictMode** of the project-level **build-profile.json5** file, or this attribute is set to **false**.
2.  **buildOption.arkOptions.byteCodeHar** is set to **false** in the module-level **build-profile.json5** file.

**Solution**

1.  Include **useNormalizedOHMUrl** in **buildOption.strictMode** of the project-level **build-profile.json5** file and set it to **true**.
2.  Set **buildOption.arkOptions.byteCodeHar** to **true** in the module-level **build-profile.json5** file.

#### 00306026 Only JS Development Supported for Lite Wearable Projects

**Error Message**

Lite wearable only support JS.

**Symptom**

Lite wearable projects support only JS development.

**Possible Causes**

A TS file exists in the lite wearable project.

**Solution**

Exclude all non-JS files from the project.

#### 00306027 Device Type Not Supported by the Dependency Module

**Error Message**

The XXX module YYY that the current module depends on does not support the device type: ZZZ, which may cause runtime exception on the device.

**Symptom**

The _YYY_ module that the current module depends on does not support the device type _ZZZ_. As a result, a runtime exception may occur.

**Possible Causes**

The **module.json** file of the dependency module does not contain the current device type.

**Solution**

Select the module that supports the device type as the dependency.

#### 00306030 transformLib Must Be Set to a Relative Path

**Error Message**

Invalid transformLib, its value should be a relative path.

**Symptom**

**transformLib** is invalid. The value must be a relative path.

**Possible Causes**

**transformLib** is not set to a relative path.

**Solution**

Set **transformLib** to a relative path.

#### 00306034 Invalid buildRoot

**Error Message**

Invalid buildRoot value XXX.

**Symptom**

The **buildRoot** parameter is invalid.

**Possible Causes**

The **buildRoot** parameter specified during the execution of the **hvigorw** command starts with **..**.

**Solution**

Ensure that the directory specified by the **buildRoot** parameter is under the current module. That is, paths starting with **..** are not allowed.

#### 00306035 Unknown abiFilter

**Error Message**

Unknown abiFilter XXX.

**Symptom**

Unknown **abiFilter** configuration _XXX_.

**Possible Causes**

The configured **abiFilter** is not in the supported list or is misspelled.

**Solution**

Check the project-level or module-level **build-profile.json5** file, ensuring that **abiFilters** contains only **arm64-v8a** and **x86\_64**.

#### 00306036 ohosTest Cannot Be Used As the Target During HSP/HAR Build

**Error Message**

Hvigor task 'XXX' not supported for building an 'ohosTest' target 'YYY'.

**Symptom**

**ohosTest** cannot be selected as the target when the HSP/HAR is built.

**Possible Causes**

**ohosTest** is selected as the target when the HSP/HAR is built using the CLI.

**Solution**

-   Select another target to build the HAR/HSP.
-   You can select **ohosTest** as the target when building the HAP module.

#### 00306038 Stage Model Modules Cannot Depend on the FA Model Modules

**Error Message**

Stage model module XXX does not allow Harmony library packages or modules in FA model. Build tasks will not be executed, and resources will not be packed.

**Symptom**

The stage model module _XXX_ cannot depend on the Harmony library or module of the FA model. Otherwise, the build task cannot be executed and resources cannot be packaged.

**Possible Causes**

The module in the stage model depends on the library or module in the FA model.

**Solution**

Check the dependencies of _XXX_ and remove the referenced Harmony libraries or modules of the FA model.

#### 00306039 HSP Cannot Depend on Itself

**Error Message**

Shared Library cannot depend on shared module self in module XXX at file: YYY.

**Symptom**

In the _XXX_ module, the HSP (shared library) cannot depend on itself.

**Possible Causes**

The HSP module has a dependency on itself.

**Solution**

Remove the dependency of the HSP on itself.

#### 00306040 FA Model Modules Cannot Depend on Non-Source-Code OpenHarmony npm Packages

**Error Message**

FA module XXX does not allow OpenHarmony npm packages, which artifactType is not original. Check at file: YYY.

**Symptom**

The FA model module cannot depend on non-source-code OpenHarmony npm packages.

**Possible Causes**

The OpenHarmony npm package on which the _XXX_ module depends is bytecode or obfuscated source code.

**Solution**

Remove the _XXX_ module's dependencies on the non-source-code OpenHarmony npm packages.

#### 00306041 FA Model Modules Cannot Depend on the Stage Model Modules

**Error Message**

FA model module XXX does not allow Harmony library packages or modules in Stage model. Build tasks will not be executed, and resources will not be packed. Check at file: YYY.

**Symptom**

The FA model module _XXX_ cannot depend on the Harmony library or module of the stage model. Otherwise, the build task cannot be executed and resources cannot be packaged.

**Possible Causes**

The module in the FA model depends on the library or module in the stage model.

**Solution**

Check the dependencies of _XXX_ and remove the referenced Harmony libraries or modules of the stage model.

#### 00306042 Incorrect API Version Format

**Error Message**

In HarmonyOS configuration mode, the value of compileSdkVersion/compatibleSdkVersion/targetSdkVersion must be M.S.F when API level is 10 or later, Example: '4.0.0(10)'; In OpenHarmony configuration mode, the value of compileSdkVersion/compatibleSdkVersion/targetSdkVersion must be a number when API level is 10 or later, Example: 10.

**Symptom**

For API version 10 or later, the format of **compileSdkVersion**, **compatibleSdkVersion**, and **targetSdkVersion** must meet the following requirements:

-   In HarmonyOS configuration mode, the value must be in the M.S.F format, for example, **4.0.0(10)**.
-   In OpenHarmony configuration mode, the value must be in the numeric format, for example, **10**.

**Possible Causes**

The format of **compileSdkVersion**, **compatibleSdkVersion**, or **targetSdkVersion** is incorrect.

**Solution**

Check the project-level **build-profile.json5** file and configure the preceding fields to the correct formats.

#### 00306043 JS Modules Cannot Depend on the ArkTS Library

**Error Message**

JS module XXX does not allow ArkTS dependency YYY. Check at file: ZZZ.

**Symptom**

The JS module _XXX_ cannot depend on ArkTS _YYY_.

**Possible Causes**

The JS module depends on ArkTS _YYY_.

**Solution**

Check the dependencies of the **oh-package.json5** file of the _XXX_ module and remove the dependency of ArkTS _YYY_.

#### 00306044 Insufficient JS Heap Memory

**Error Message**

Worker terminated due to reaching memory limit: JS heap out of memory.

**Symptom**

The task is terminated due to insufficient JS heap memory.

**Possible Causes**

The heap memory is insufficient during task execution.

**Solution**

1.  Modify thread-related configurations (**hvigor.pool.maxSize**, **ohos.arkCompile.maxSize**, and **hvigor.enableMemoryCache**) in [hvigor-config.json5](../../../configuration-files/hvigor-config-json5-file/document.md).
2.  Disable the [parallel mode](../../../improving-build-efficiency/enabling-parallel-build/document.md) during task execution.

#### 00306045 useNormalizedOHMUrl Can Be Set to true Only When compatibleSdkVersion Is Set to 5.0.0(12) or Later

**Error Message**

UseNormalizedOHMUrl can be true only when Compatible SDK Version is 5.0.0 (12) or later.

**Symptom**

**useNormalizedOHMUrl** can be set to **true** only when **compatibleSdkVersion** is set to **5.0.0(12)** or later.

**Possible Causes**

**compatibleSdkVersion** is set to **4.1.0(11)** or earlier, and **useNormalizedOHMUrl** is set to **true** in the project-level **build-profile.json5**.

**Solution**

Set **useNormalizedOHMUrl** to **false** if **compatibleSdkVersion** is **4.1.0(11)** or earlier.

#### 00306046 Bytecode HAR Not Supported If useNormalizedOHMUrl Is Set to false

**Error Message**

Bytecode HARs: XXX not supported when useNormalizedOHMUrl is not true.

**Symptom**

If **useNormalizedOHMUrl** is set to **false**, the bytecode HAR is not supported.

**Possible Causes**

The **useNormalizedOHMUrl** field in the project-level **build-profile.json5** file is set to **false**, and the dependency chain of the current module contains the bytecode HAR.

**Solution**

If the dependency chain of the current compilation module contains the bytecode HAR, set **useNormalizedOHMUrl** in the project-level **build-profile.json5** file to **true**.

#### 00306047 Multiple HSP Modules Depend on the Same HAR

**Error Message**

Found HSPs that have the same HAR.

**Symptom**

Multiple HSP modules depend on the same HAR.

**Possible Causes**

Multiple HSP modules depend on the same HAR.

**Solution**

For details, see [Modular Design](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-modular-design).

#### 00306048 autoLazyImport Not Supported in the Current API Version

**Error Message**

autoLazyImport cannot be configured for the current API version. autoLazyImport can be used in the beta3 version of API 12 or higher versions.

**Symptom**

**autoLazyImport** is not supported in the current API version. It is supported in API version 12 beta3 and later.

**Possible Causes**

**autoLazyImport** is set to **true** in a version earlier than API version 12 beta3.

**Solution**

Use either of the following methods:

-   Check the **compatibleSdkVersion** and **compatibleSdkVersionStage** fields in the project-level **build-profile.json5** file. If **compatibleSdkVersion** is set to API version 12, set **compatibleSdkVersionStage** to **beta3**.
-   Set **autoLazyImport** to **false**.

#### 00306049 Duplicate Files in the Module

**Error Message**

Duplicated files found in module XXX. This may cause unexpected errors at runtime.

**Symptom**

Duplicate files exist in module _XXX_, which may cause runtime errors.

**Possible Causes**

The .so files with the same name exist in the module.

**Solution**

Use either of the following methods:

-   Assign a unique name to every .so file.

-   Set the priority of .so files using the [pickFirsts, pickLasts, or select field](../../../configuring-your-build/configuring-for-c-builds/document.md#section17675528161517).

#### 00306050 Projects in the FA Model Cannot Depend on External Project Modules

**Error Message**

This project is in the FA model and does not allow for external dependencies.

**Symptom**

The project in the FA model depends on an external project module.

**Possible Causes**

In the **build-profile.json5** file of the project developed in the FA model, the value of the **srcPath** field contains a reference to an external project module.

**Solution**

In the project-level **build-profile.json5** file, identify and remove any references to external project modules from the **srcPath** field.

#### 00306051 Projects in the Stage Model Cannot Depend on FA Model Modules

**Error Message**

This project is in the stage model and does not allow for dependencies of modules in the FA model.

**Symptom**

The project in the stage model cannot depend on an FA model module.

**Possible Causes**

In the project-level **build-profile.json5** file in the stage model, the value of the **srcPath** field contains a reference to a project module developed in the FA model.

**Solution**

In the project-level **build-profile.json5** file, identify and remove any references to project modules developed in the FA model.

#### 00306052 Reference to External HAP Modules Not Allowed

**Error Message**

Cannot depend on HAP modules outside of this project.

**Symptom**

The HAP module outside the project cannot be depended on.

**Possible Causes**

In the project-level **build-profile.json5** file, the value of the **srcPath** field contains a reference to a HAP module outside of the current project.

**Solution**

Replace any references to HAP modules outside of the current project with references to HSP or HAR modules.

#### 00306053 Failed to Install the ohpm Dependency

**Error Message**

ohpm install failed.

**Symptom**

An ohpm dependency failed to be installed.

**Possible Causes**

There is an error with the Internet connection, or the [ohpm repository address](../../../../command-line-tools/using-ohpm/ohpmrc/document.md#en-us_topic_0000001792216397_%E9%BB%98%E8%AE%A4%E9%85%8D%E7%BD%AE%E9%A1%B9) or the dependency name or version number specified in the **oh-package.json5** file is incorrect.

**Solution**

Verify the Internet connectivity. Make sure the ohpm repository address and the dependency name or version number specified in the **oh-package.json5** file are correct.

#### 00306054 Invalid Build Task Command

**Error Message**

Task XXX was not found in the project XXX. Invalid command to execute the build task, please verify the parameters in the command and try again.

**Symptom**

The task cannot be found in the project. The build task command is invalid. Check the parameters in the command and try again.

**Possible Causes**

The parameters in the build command are incorrectly set.

**Solution**

1.  Run the **hvigorw --help** command to learn more about the hvigor command.
2.  Run the **hvigorw tasks** command to view the available task list.
3.  Add the **\--info** or **\--debug** option when running the command to obtain more log output.

#### 00306055 External Modules Not Configured

**Error Message**

Missing module configuration for external module outside the current project.

**Symptom**

The external modules used by the project are not configured.

**Possible Causes**

The external modules used by the project are not configured in the project-level **build-profile.json5** file.

**Solution**

Check the project-level **build-profile.json5** file and ensure that all the modules used by the project are configured in the **modules** field.
