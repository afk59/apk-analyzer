# Enabling Performance Optimization Experimental Features

To create a more agile and smooth user experience, the new version of Hvigor introduces a series of experimental features for compilation and build performance optimization. These features will significantly improve project compilation speed and reduce peak memory usage. Since some optimization solutions are still in the experimental stage, you may experience efficiency improvements with these features, but you might also encounter issues to be addressed in specific scenarios. Therefore, these features come with switches that you can toggle based on your service requirements.

#### Incremental Task Determination Optimization

**Optimization solution**:

-   Before optimization: The input and output methods of a task need to be called for multiple times when an incremental task is executed.
-   After optimization: When an incremental task is executed, the results of the input and output methods are cached. The cached results are directly read when the methods are called again, reducing the overhead of multiple calls.

**Optimization result**: Reduces the compilation time.

**How to enable**: Add the following field to **hvigor-config.json5**. This feature is supported since DevEco Studio 5.1.1 Beta1.

"properties": {
  "hvigor.incremental.optimization": true
}

**Possible impact**: If global variables are referenced in the incremental input/output determination of a custom task, the variables may change during task execution. If the variables change, the incremental determination of related tasks becomes invalid during the next build and the tasks are executed again.

#### Task Scheduling Optimization

**Optimization solution**:

-   Before optimization: Tasks in the to-be-executed queue are executed in sequence. The build duration of incremental builds is affected by the start time of the CompileArkTs task. The later the CompileArkTs task starts, the longer the build duration may be.
-   After optimization: By prioritizing the execution of CompileArkTs and its dependent tasks, the CompileArkTs compilation task can be started as early as possible, thereby reducing build duration.

**Optimization result**: Reduces the compilation time.

**How to enable**: Add the following field to **hvigor-config.json5**. This feature is supported since DevEco Studio 5.1.1 Beta1.

"properties": {
  "hvigor.task.schedule.optimization": true
}

**Possible impact**: None.

#### Writing a File to a Disk

**Optimization solution**:

-   Before optimization: During ArkTS code compilation, after an individual file is parsed, it is cached in the memory.
-   After optimization: During ArkTS code compilation, after an individual file is parsed, it is written to the disk, which can reduce the peak memory usage during compilation.

**Optimization result**: Reduces the memory usage.

**How to enable**: Add the following field to **hvigor-config.json5**.

"properties": {
  "ohos.arkCompile.singleFileEmit": true
}

**Possible impact**: The timing of writing a parsed file to the disk is advanced, which may cause custom source code instrumentation plugins to execute after the file is written to the disk and thus fail to take effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/OA05iinbRbOTnYa3kb45NQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F255CEB7FF963A0EC27CEFCDBBF55571F4C6A692C8D9E499D14939D704716B2A)

-   This field takes effect only in debug mode.
-   This field has no effect during code coverage compilation.

#### Optimization of Intermediate Compilation Product Generation

**Optimization solution**:

-   Before optimization: During ArkTS code compilation, the ArkTS/TS code is compiled into intermediate JS code.
-   After optimization: During ArkTS code compilation, no intermediate JS code is generated.

**Optimization result**: Reduces the compilation time and memory usage.

**How to enable**: Add the following field to **hvigor-config.json5**.

"properties": {
  "ohos.arkCompile.noEmitJs": true
}

**Possible impact**: None.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/14gEiS56TrqbIfmZud0jpw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21E1FEEF6748A14CDB8F12D8132D901CBE3B23D84D6379C4EF1BEDD8CADD168A)

This field is not supported in the following scenarios, and intermediate JS code will be generated regardless of the configuration:

-   FA model
-   Code coverage testing
-   [HAR built in release mode with obfuscation enabled](../../configuring-your-build/building-a-har/document.md#section19788284410)
-   Projects corresponding to lite wearable devices

#### Module-level Skip of Incremental Judgment

**Use Case**

Since DevEco Studio 6.0.0 Beta3, if there is a need to frequently modify code for incremental builds, you can enable this feature to speed up incremental compilation.

**Constraints**

-   Before enabling this feature, a full build is required to ensure that the build product directory (**build**) exists.
-   After enabling this feature, only modifications to content under the **src** directory of the module are supported; modifying content outside the **src** directory may cause modifications to not take effect or result in compilation issues.
-   Preview and Local Test are not supported.

**Optimization solution**:

-   Before optimization: All tasks of each module require incremental judgment.
-   After optimization: With this feature enabled, during building with modifications to content under the module's **src** directory, unmodified modules will not undergo incremental judgment.

**Optimization result**: Reduces the compilation time of incremental builds.

**How to enable**: Choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Build, Execution, Deployment** > **Build Tools** > **Hvigor** and select **Enable module level incremental skip for incremental build**.

**Possible impact**: If the constraints are not met, the feature setting may become invalid or compilation errors may occur.

#### Executing ohpm install Using Hvigor

Since DevEco Studio 6.0.0 Beta3, a new toggle labeled **Enable ohpm execution via hvigor** has been added to the **Settings**. This option is applicable in the following two use cases.

**How to enable**: Choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Build, Execution, Deployment** > **Build Tools** > **Hvigor** and select **Enable ohpm execution by hvigor**.

**Use Case 1**

With this feature enabled, you can use the [excludeNodeByName](../../expanding-build-capabilities/using-apis-for-extending-your-build/basic-build-capability/document.md#section14183309272) method to exclude a module that does not exist.

1.  Follow the preceding steps to enable the **Enable ohpm execution by hvigor** toggle.
2.  Add a module that does not exist in the project, for example, **testModule**, to the **module** field in the project-level **build-profile.json5** file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/NjTZziIHSIWZgdL4041IJQ/en-us_image_0000002500910124.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FCEFEF4C000D4996B5DA43A6564A297377A8C3411D4EFF9FA8A15D96EFE23B53)
    
3.  Call the **excludeNodeByName** method to exclude the inexistent module **testModule**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/l2PBdn8xR5KGwWoHruQqQA/en-us_image_0000002501069964.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A80247C76CBBC5EFA191D141F7A5DD5C90103782FD9578FADA1B1D845DFD59D)
    
4.  Execute the build and verify its successful completion.

**Use Case 2**

After the [setDependenciesOpt](../../expanding-build-capabilities/using-apis-for-extending-your-build/plug-in-context/document.md#section18789410129) and [setOverrides](../../expanding-build-capabilities/using-apis-for-extending-your-build/plug-in-context/document.md#section469812496459) methods are called to dynamically modify the dependency configuration in the **oh-package.json5** file, DevEco Studio executes **ohpm install** twice when operations such as **sync** or **build** are performed. If this feature is enabled, Hvigor executes **ohpm install** only once, improving build efficiency.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/oe6P0l9TSLmgoAgbnAC6Jw/en-us_image_0000002532749999.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A624C03B92A40D62BFD8B17604AEF46EAF6DF40658C3A49CD3257D3BF80A2254)

#### Improving C++ Incremental Compilation Efficiency via IClang

**Use Case**

For DevEco Studio 6.0.1 Beta1 and later versions, if you need to frequently modify a specific C++ source file, you can enable the IClang feature to improve C++ incremental compilation efficiency. IClang is a function-level incremental compilation optimization technology for C++. For details, see [BiSheng Compiler](../../../ndk-development/building-an-ndk-project/bisheng-compiler/document.md#section8221174018112).

**Constraints**

-   IClang is supported only in debug build mode.
-   The BiSheng Compiler is required for compilation, that is, **nativeCompiler** in the project-level **build-profile.json5** file must be set to **BiSheng**.
-   During the first modification of a C++ file, IClang identifies it as a frequently modified target and generates a cache. The efficiency gains kick in from the second incremental build onward.
-   Any changes to header files, including content modifications, adjustments to import statements (order, blank lines, or formatting), will invalidate the cache and disable compilation efficiency improvements.

**How to Enable**

-   Method 1: Choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Build, Execution, Deployment** > **Build Tools** > **Hvigor**, and select **Enable C++ function level incremental compilation**.
-   Method 2: Add the **\-iclang** parameter to **cppFlags** and **cFlags** in the module-level **build-profile.json5** file.
    
    "buildOption": {
      "externalNativeOptions": {
        "cppFlags": "-iclang",
        "cFlags": "-iclang",
      }
    }
    

**Possible impact**: The **build-profile.json5** file is part of version control. Adding the **\-iclang** parameter will automatically enable this experimental feature for all other project developers. Please ensure thorough validation of functionality before committing the configuration changes to the code repository.
