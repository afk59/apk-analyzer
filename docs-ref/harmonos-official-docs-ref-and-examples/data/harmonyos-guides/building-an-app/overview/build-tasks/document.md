# Build Tasks

This topic gives an overview of the build tasks.

#### Build Task Flowcharts

## HAP Build Task Flowchart

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/jCBevEUMSMGuTNnk1ywpPQ/en-us_image_0000002532670115.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=087D33A882B97E428E371286B10573419DA02859C98A6BDEACF2E7D6BF822975)

## HSP Build Task Flowchart

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/Vl1xW3HQQKe3Obyg9RAO5A/en-us_image_0000002532750071.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FBE139148715F08ED077A93A21FC21A354F1CCF23733CF01913B2751909E001F)

## HAR Build Task Flowchart

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/ryWAbmhtRxOtjAWGpa7bBw/en-us_image_0000002501070042.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=234A7137CB2FB8D01ED62BFED18A9DFFE88AA4D322DEF9BF155821C783B483F4)

#### Viewing Tasks with Commands

To view available tasks, run the following command in DevEco Studio:

hvigorw taskTree

All tasks available for the project and for modules in the project are displayed, as shown below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/BKFS0A17TnuuLpMrAtaheg/en-us_image_0000002532750069.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84F13FF236DE74AF492B85AFE0127529EFC919A3BAFF86DE2F003F92705B7C0A)

As shown in the preceding figure, **assembleHap** depends on **CollectDebugSymbol**, and **CollectDebugSymbol** depends on **PackageHap**. Therefore, the order of task execution is as follows: **PackageHap** > **CollectDebugSymbol** > **assembleHap**.

#### Task Categories

There are several categories of tasks that can be executed, as listed below.

| 
Task Category

 | 

Description

 |
| :-- | :-- |
| 

Hook

 | 

Hook tasks.

 |
| 

ArkTS

 | 

Tasks related to ArkTS builds.

 |
| 

JS

 | 

Tasks related to JS builds.

 |
| 

Resources

 | 

Tasks related to resource building, processing, linking, and merging.

 |
| 

Package

 | 

Tasks related to packaging.

 |
| 

Sign

 | 

Tasks related to signing.

 |
| 

Verification

 | 

Tasks related to verifying project or dependency settings.

 |
| 

Generate

 | 

Tasks related to generating and converting prerequisite files.

 |
| 

Config

 | 

Tasks related to generating, merging, and processing configuration files.

 |
| 

Native

 | 

Tasks related to native builds.

 |
| 

Help

 | 

Tasks related to querying hvigor help information.

 |
| 

Other

 | 

Uncategorized tasks.

 |

## Hook

-   **assembleHap**: assembles a HAP.
-   **assembleHsp**: assembles an HSP.
-   **assembleHar**: assembles a HAR.
-   **assembleApp**: assembles an App Pack.
-   **assembleDevHqf**: assembles an HPF file for incremental deployment.
-   **HotReloadBuild**: runs before the **HotReloadArkTS** task.
-   **PreviewBuild**: runs before the **PreviewArkTS** task.
-   **buildHotReloadResource**: runs before hot reloading.
-   **PreviewHookCompileResource**: specifies whether to invoke RESTool to compile resources under the preview scenario.
-   **GenerateBuildProfile**: generates the **BuildProfile.ets** file.
-   **BuildUnitTestHook**: runs before resource compilation under unit testing scenarios.
-   **buildPreviewerResource**: runs before resource compilation under preview scenarios.
-   **compileNative**: runs before native resource compilation.
-   **UnitTestBuild**: runs before the **UnitTestArkTS** task.
-   **test**: executes the hook task for the local test.
-   **onDeviceTest**: executes the hook task for the instrument test.

## ArkTS

-   **CompileArkTS**/**BuildArkTS**: invokes the loader using **rollup** to compile ArkTS source code.
-   **PreviewArkTS**: invokes the loader using **rollup** to compile ArkTS source code under preview scenarios.
-   **HotReloadArkTS**: invokes the loader using **rollup** to compile ArkTS source code under hot reload scenarios.
-   **OhosTestCompileArkTS**/**OhosTestBuildArkTS**: invokes the loader using **rollup** to compile ArkTS source code under testing scenarios.
-   **HarCompileArkTS/HarBuildArkTS**: invokes the loader using **rollup** to compile ArkTS source code during a HAR build.
-   **UnitTestArkTS**: invokes the loader using **rollup** to compile ArkTS source code under unit testing scenarios.

## JS

-   **CompileJS**/**BuildJS**: invokes the loader to compile JS source code.
-   **OhosTestCompileJS**/**OhosTestBuildJS**: invokes the loader to compile JS source code under testing scenarios.

## Resources

-   **ProcessResource**: processes and generates intermediate files for compiling resources in file mode.
-   **PreviewProcessResource**: processes and generates intermediate files for compiling resources in file mode under the preview scenario.
-   **CompileResource**: invokes RESTool to compile resources.
-   **PreviewCompileResource**: invokes RESTool to compile resources under the preview scenario.
-   **ProcessLibs**: collects the .so files in the HAP and HAR dependencies.

## Package

-   **PackageHap**: invokes the packaging tool to package a HAP.
-   **PackageHar**: invokes the packaging tool to package a HAR.
-   **PackageHsp**: invokes the packaging tool to package an HSP.
-   **PackageApp**: invokes the packaging tool to package an application program package (APP).
-   **PackageHqf**: invokes the packaging tool to package an HPF file.
-   **PackageSharedHar**: invokes the packaging tool to package a shared HAR for an HSP.
-   **PackageSharedTgz**: invokes the packaging tool to package an unsigned HAP and HAR generated by an HSP module into a .tgz package.
-   **PackageSignHar**: invokes the packaging tool to package a signed HAR. It takes effect only in daemon mode.

## Sign

-   **SignHap**: invokes the signing tool to sign a HAP.
-   **SignHsp**: invokes the signing tool to sign an HSP.
-   **SignApp**: invokes the signing tool to sign an APP.
-   **SignHqf**: invokes the signing tool to sign an HPF file.
-   **SignModuleRemoteHsp**: invokes the signing tool to sign an HSP in the module-level ohpm repository.
-   **SignProjectRemoteHsp**: invokes the signing tool to sign an HSP in the project-level ohpm repository.

## Verification

-   **PreBuild**: conducts a module-level precheck.
-   **PreBuildApp**: conducts a project-level precheck.
-   **PreCheckSyscap**: conducts a SysCap configuration precheck.

## Generate

-   **GenerateLoaderJson**: generates the **loader.json** file.
-   **GenerateMetadata**: generates the **metadata.json** file.
-   **SyscapTransform**: conducts a SysCap conversion task.
-   **MakePackInfo**: generates the module-level **pack.info** file.
-   **MakeProjectPackInfo**: generates the project-level **pack.info** file.
-   **ProcessPackageJson**: processes the **package.json** file.
-   **ProcessOHPackageJson**: processes the **oh\_package.json5** file.
-   **GeneratePackRes**: generates the **pack.res** file.
-   **CreateBuildProfile**: generates the **BuildProfile.ets** file for an HAP or HSP.
-   **CreateHarBuildProfile**: generates the **BuildProfile.ets** file for a HAR.
-   **PrepareQuickfix**: obtains the HPF file through verification and exports the file to the **quickfix.json** file.

## Config

-   **ProcessProfile**: processes the **module.json5** file.
-   **PrepareSharedHarResource**: generates **package.json** and **module.json** files for packaging the shared library.
-   **UnitTestProcessProfile**: processes and builds the intermediate product **module.json** file under the UnitTestBuild scenario.
-   **MergeProfile**: merges the **module.json5** file.
-   **PreviewUpdateAssets**: updates the **module.json** and **main\_pages.json** files generated by a pre-configuration task in the stage model before compiling the preview code.

## Native

-   **BuildNativeWithNinja**: compiles native code into .so files.
-   **BuildNativeWithCmake**: uses CMake to compile CPP source code.

## Help

-   **tasks**: displays all hvigor tasks.
-   **taskTree**: displays the task tree involved in the current project.

## Other

-   **ReplaceUnitTestIndexFile**: replaces files for unit testing.
-   **ReplacePreviewerPage**: replaces page parameters with those provided by the Previewer.
-   **OhosTestCopyMockConfigJson**: copies the **mock-config.json** file to the test package when executing mock.
-   **clean**: cleans the generated **Build** directory.
-   **collectCoverage**: generates a coverage statistics report based on the collected data.

## Sync

-   **init**: initializes a project.

## Init

This task is different from **init** under **Sync**. There is no specific task in this task, and it is responsible for preparing for invoking hvigor.
