# hvigor-config.json5 File

#### File Structure

The structure of the **hvigor-config.json5** file is as follows:

modelVersion
dependencies
execution
└── analyze
└── daemon
└── incremental
└── parallel
└── typeCheck
└── optimizationStrategy
logging
└── level
debugging
└── stacktrace
nodeOptions
└── maxOldSpaceSize
└── maxSemiSpaceSize
└── exposeGC
javaOptions
└── Xmx
properties
└── hvigor.cacheDir
└── ohos.buildDir
└── enableSignTask
└── ohos.arkCompile.maxSize
└── hvigor.pool.cache.capacity
└── hvigor.pool.maxSize
└── ohos.pack.compressLevel
└── hvigor.analyzeHtml
└── hvigor.dependency.useNpm
└── ohos.compile.lib.entryfile
└── ohos.align.target
└── ohos.fallback.target
└── ohos.arkCompile.sourceMapDir
└── ohos.collect.debugSymbol
└── hvigor.enableMemoryCache
└── hvigor.memoryThreshold
└── ohos.nativeResolver
└── ohos.arkCompile.noEmitJs
└── ohos.arkCompile.singleFileEmit
└── ohos.sign.har
└── hvigor.keepDependency
└── ohos.arkCompile.emptyBundleName
└── ohos.uiTransform.Optimization
└── ohos.har.excludeHspDependencies
└── ohos.processLib.optimization
└── ohos.obfuscationRules.optimization
└── hvigor.incremental.optimization
└── hvigor.task.schedule.optimization
└── ohos.byteCodeHar.integratedOptimization
└── ohos.rollupCache.usePathPlaceholder
└── ohos.rollupCache.useSourceHash
└── ohos.arkCompile.writeRollupCache
└── ohos.align.deviceTypes
└── ohos.dependencies.types.enable
└── ohos.defaults.release.cmakebuildtype
└── ohos.defaults.autoLazyImport
parameterFile

#### Fields in the Configuration File

The following table lists the fields contained in the **hvigor-config.json5** file.

**Table 1** Fields in the hvigor-config.json5 file
| 
Name

 | 

Mandatory/Optional

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

modelVersion

 | 

Mandatory

 | 

String

 | 

Development-specific version number.

 |
| 

dependencies

 | 

Mandatory

 | 

Object

 | 

Dependencies for the build tasks of the project, sourced from npm.

NOTE:

After modifying **dependencies**, click **Sync Now** in the upper right corner of the editor as prompted to install the dependencies.

 |
| 

[execution](#section6901191119219)

 | 

Optional

 | 

Object

 | 

Build execution settings, effective only in the CLI scenario.

 |
| 

[logging](#section85176471028)

 | 

Optional

 | 

Object

 | 

Log settings.

 |
| 

[debugging](#section76575554217)

 | 

Optional

 | 

Object

 | 

Debugging settings.

 |
| 

[nodeOptions](#section74431812314)

 | 

Optional

 | 

Object

 | 

Node.js related settings.

 |
| 

[javaOptions](#section7929682318)

 | 

Optional

 | 

Object

 | 

Java related settings.

 |
| 

[properties](#section260315160319)

 | 

Optional

 | 

Object

 | 

Additional configuration properties.

 |
| 

[parameterFile](#section24539147532)

 | 

Optional

 | 

String

 | 

Path of the custom parameterization configuration file.

This field is supported since DevEco Studio 6.0.2 Beta1.

 |

#### execution

**execution** indicates the build execution settings. Except the **optimizationStrategy** field, other fields take effect only in the CLI scenario. To configure build execution settings for builds using DevEco Studio, choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Build, Execution, Deployment** > **Build Tools** > **Hvigor**.

**Table 2** execution field description
| 
Name

 | 

Mandatory/Optional

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

analyze

 | 

Optional

 | 

String/Boolean

 | 

Build analysis mode.

-   **normal** (default): In this mode, analysis is performed using simple tracking data. The original **default** mode is deprecated.
-   **advanced**: In this mode, analysis is performed using more detailed tracking data. Select this mode if you need more details on the task consumption time. The original **verbose** mode is deprecated.
-   **ultrafine**: ultra-fine mode. Compared with the **advanced** mode, this mode records more detailed trace data during ArkTS compilation. However, enabling this mode may take a longer time for compilation and build. This mode is supported since DevEco Studio 6.0.0 Beta1.
-   **false**: Build analysis is disabled.

 |
| 

daemon

 | 

Optional

 | 

Boolean

 | 

Whether to enable the daemon process build.

-   **true** (default): enabled
-   **false**: disabled

 |
| 

incremental

 | 

Optional

 | 

Boolean

 | 

Whether to enable incremental build.

-   **true** (default): enabled
-   **false**: disabled

 |
| 

parallel

 | 

Optional

 | 

Boolean

 | 

Whether to enable parallel build.

-   **true** (default): enabled
-   **false**: disabled

 |
| 

typeCheck

 | 

Optional

 | 

Boolean

 | 

Whether to enable the type check of the build script **hvigorfile.ts**. After the type check is enabled, the build efficiency may decrease.

-   **true**: enabled
-   **false** (default): disabled

 |
| 

optimizationStrategy

 | 

Optional

 | 

String

 | 

Build mode. This field is supported since DevEco Studio 5.1.1 Release.

-   **performance**: performance first mode. This mode can accelerate the build speed, but occupies more memory.
-   **memory** (default): memory first mode. This mode can reduce the compilation memory usage.

NOTE:

A full compilation is performed for the first compilation after the mode change.

 |

Example configuration:

{
  "execution": {
    "analyze": "normal",
    "daemon": true,
    "incremental": true,
    "parallel": true,
    "typeCheck": false,
    "optimizationStrategy": "performance",
  }
}

#### logging

Log settings.

**Table 3** logging field description
| 
Name

 | 

Mandatory/Optional

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

level

 | 

Optional

 | 

String

 | 

Level of logs to be printed during the build process.

-   **debug**: debug log.
-   **info** (default): basic information log.
-   **warn**: warning log.
-   **error**: error log.

 |

Example configuration:

{
  "logging": {
    "level": "debug"
  }
}

#### debugging

Debugging settings.

**Table 4** debugging field description
| 
Name

 | 

Mandatory/Optional

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

stacktrace

 | 

Optional

 | 

Boolean

 | 

Whether to enable stack trace.

-   **true**: enabled
-   **false** (default): disabled

 |

Example configuration:

{
  "debugging": {
    "stacktrace": true
  }
}

#### nodeOptions

Node.js related settings.

**Table 5** nodeOptions field description
| 
Name

 | 

Mandatory/Optional

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

maxOldSpaceSize

 | 

Optional

 | 

Integer

 | 

Maximum old-generation memory size (in MB) of the daemon process when it is enabled for the build. The default value is **8192**. If JavaScript memory overflow occurs due to a large amount of project code, you can adjust this parameter value to solve the issue.

 |
| 

maxSemiSpaceSize

 | 

Optional

 | 

Integer

 | 

Maximum semi-space size, in MB, of the young-generation memory for the daemon process when it is enabled for the build. The default value is **16**. Increasing this value can improve the Node.js throughput, but may lead to higher memory usage.

This field is supported since DevEco Studio 5.1.0 Release.

 |
| 

exposeGC

 | 

Optional

 | 

Boolean

 | 

Whether to enable Garbage Collection (GC) to optimize peak memory during the compilation process.

-   **true** (default): enabled
-   **false**: disabled

 |

Example configuration:

{
  "nodeOptions": {
    "maxOldSpaceSize": 8192,
    "maxSemiSpaceSize": 16,
    "exposeGC": true,
  }
}

#### javaOptions

Java related settings.

**Table 6** javaOptions field description
| 
Name

 | 

Mandatory/Optional

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

Xmx

 | 

Optional

 | 

Integer

 | 

Maximum JVM heap size, in MB. The default value is **512**.

 |

Example configuration:

{
  "javaOptions": {
    "Xmx": 512
  }
}

#### properties

Additional configuration properties. In addition to configuring **properties** in **hvigor-config.json5**, you can also specify **properties** using the command-line argument **\-c** or **\--config**. Command-line configurations take precedence over those in **hvigor-config.json5**. For details, see [Other options](../../../command-line-tools/using-hvigorw/document.md#section92386011817).

**Table 7** properties field description
| 
Name

 | 

Mandatory/Optional

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

hvigor.cacheDir

 | 

Optional

 | 

String

 | 

Storage location of the .hvigor cache folder in the project's root directory.

NOTE:

Different projects with the same name cannot be stored in the same location.

 |
| 

ohos.buildDir

 | 

Optional

 | 

String

 | 

Storage location of the project's build output directory (**build** directory).

NOTE:

Different projects with the same name cannot be stored in the same location.

 |
| 

enableSignTask

 | 

Optional

 | 

Boolean

 | 

Whether to enable HAP or HSP signature tasks.

-   **true** (default): enabled
-   **false**: disabled

 |
| 

ohos.arkCompile.maxSize

 | 

Optional

 | 

Integer

 | 

Number of ArkTS compilation threads. The default value is **5**.

 |
| 

hvigor.pool.cache.capacity

 | 

Optional

 | 

Integer

 | 

Cache size in the memory. The default value is **4**. A smaller value indicates less cached data in the memory. The value **0** means that memory caching is disabled.

 |
| 

hvigor.pool.maxSize

 | 

Optional

 | 

Integer

 | 

Number of threads during the compilation process, including signature and packing tasks that are not included in **ohos.arkCompile.maxSize**. The default value is number of project modules or the number of virtual cores minus 1, whichever is smaller.

 |
| 

ohos.pack.compressLevel

 | 

Optional

 | 

String

 | 

Compression level for packing the HAP (compressing .so files) or App Pack (compressing HAPs). Higher compression levels result in slower compression speeds.

-   **fast** (default): lowest compression level, which offers the fastest compression speed.
-   **standard**: moderate compression level, with a balanced compression speed.
-   **ultimate**: highest compression level, which results in the slowest compression speed.

 |
| 

hvigor.analyzeHtml

 | 

Optional

 | 

Boolean

 | 

Whether to generate a build visualization HTML file.

-   **true**: Generate a build visualization HTML file. The generated HTML file is stored in the project's **.hvigor/report** directory and can be opened directly in a browser.
-   **false** (default): Do not generate a build visualization HTML file.

 |
| 

hvigor.dependency.useNpm

 | 

Optional

 | 

Boolean

 | 

Whether to use npm to download hvigor dependencies.

If this parameter is not set, and the Node.js version is 16 or later, pnpm is used by default to download dependencies. In certain scenarios, you can set this parameter to specify the use of npm for downloading dependencies.

-   **true**: Use npm to download dependencies regardless of the Node.js version.
-   **false** (default): Use pnpm to download dependencies if the Node.js version is 16 or later; use npm if the Node.js version is earlier than 16.

 |
| 

ohos.compile.lib.entryfile

 | 

Optional

 | 

Boolean

 | 

Whether to start compiling from the entry point file.

-   **true**: Compile from the module's entry point file. The entry point file and referenced files are compiled, but unreferenced files are not.
-   **false** (default): Perform a full compilation of .ets and .ts files under **src/main/ets**. Specifically, the .ets and .ts files under the **src/main/ets** directory are compiled into the product in the following scenarios:
    1.  HSP build
    2.  HAR obfuscation or bytecode HAR creation in release mode
    3.  Dynamically dependent HAR during an HAP or HSP build

 |
| 

ohos.align.target

 | 

Optional

 | 

String

 | 

Target for all modules and their dependencies involved in the current build task. For details, see [Understanding Multi-Product Build Targets](../../configuring-your-build/configuring-multiple-targets-and-products/introduction/document.md#section7121513141619).

 |
| 

ohos.fallback.target

 | 

Optional

 | 

String array

 | 

Fallback target for all modules and their dependencies involved in the current build task. The priority order of targets is as follows: align target > CLI-specified module target > dependent parent module target > fallback target > default target. For details, see [Understanding Multi-Product Build Targets](../../configuring-your-build/configuring-multiple-targets-and-products/introduction/document.md#section7121513141619).

 |
| 

ohos.arkCompile.sourceMapDir

 | 

Optional

 | 

String

 | 

Path for generating **sourceMap** files to facilitate stack backtrace and error location. Currently, only the Stage model is supported. If no path is specified, the files are generated in **build/{productName}/outputs/{targetName}/mapping** by default.

NOTE:

This parameter is supported since API version 12.

 |
| 

ohos.collect.debugSymbol

 | 

Optional

 | 

Boolean

 | 

Whether to archive the [sourceMap](../../../coding-and-debugging/analyzing-logs-and-faults/fault-analysis/exception-stack-trace-analysis/document.md#section666114451518), [nameCache](../../../coding-and-debugging/analyzing-logs-and-faults/fault-analysis/exception-stack-trace-analysis/document.md#section19215122372720), and .so files with debugging information to the product path. The destination path differs based on the build mode and the type of build: For HAPs, HSPs, and HARs, these files are stored in either the **release** or **debug** folder under **build/{_productName_}/outputs/{_targetName_}/symbol** in the module directory; for App Packs, the files are placed in either the **release** or **debug** folder under **build/outputs/{_productName_}/symbol** in the project directory.

-   **true**: Enable archiving.
-   **false**: Disable archiving.

NOTE:

-   If this parameter is not set, the default value is **true** in release mode and **false** in debug mode.
-   Only the stage model is supported.
-   The nameCache file is generated only in release mode when obfuscation is enabled.

 |
| 

hvigor.enableMemoryCache

 | 

Optional

 | 

Boolean

 | 

Whether to enable caching. Enabling caching speeds up incremental compilation, while disabling it saves memory but increases incremental compilation time.

-   **true** (default): enabled
-   **false**: disabled

 |
| 

hvigor.memoryThreshold

 | 

Optional

 | 

Integer

 | 

Memory usage threshold, in MB. When the build process exceeds this threshold, new build tasks do not start until the ongoing tasks are completed, potentially extending build times.

NOTE:

-   After this parameter is set, caching is not performed even if **hvigor.enableMemoryCache** is set to **true**.
-   Setting the parameter to a very small value will cause build tasks to execute sequentially, equivalent to setting **ohos.arkCompile.maxSize: 1**. Setting it to a large value makes no difference compared to not setting it at all.

 |
| 

ohos.nativeResolver

 | 

Optional

 | 

Boolean

 | 

Whether to use a high-performance plug-in for dependency addressing during ArkTS compilation, which can reduce the peak memory usage during compilation and accelerate the compilation.

-   **true** (default): The high-performance plug-in is used.
-   **false**: The high-performance plug-in is not used.

 |
| 

ohos.arkCompile.noEmitJs

 | 

Optional

 | 

Boolean

 | 

Whether to generate JS intermediate products during ArkTS compilation. For details about the solution and impact, see [Optimizing the Generation of Compilation Intermediate Products](../../improving-build-efficiency/enabling-performance-optimization-experimental-features/document.md#section11117155101617).

-   **true**: Disable generation.
-   **false** (default): Enable generation.

 |
| 

ohos.arkCompile.singleFileEmit

 | 

Optional

 | 

Boolean

 | 

Whether to write the parsed single file to the disk. For details about the solution and impact, see [Writing a File to a Disk](../../improving-build-efficiency/enabling-performance-optimization-experimental-features/document.md#section1131619813214).

-   **true**: enabled.
-   **false** (default): disabled.

 |
| 

ohos.sign.har

 | 

Optional

 | 

Boolean

 | 

Whether to enable HAR signature tasks. For details, see [Building a Signed HAR](../../configuring-your-build/building-a-har/document.md#section116791730173713).

-   **true**: enabled
-   **false** (default): disabled

 |
| 

hvigor.keepDependency

 | 

Optional

 | 

Boolean

 | 

Whether to retain all dependencies in the HSP.

-   **true** (default): Retain all dependencies in the HSP.
-   **false**: Do not retain all dependencies in the HSP. In this case, only HSP-related dependencies in the HSP are retained.

 |
| 

ohos.arkCompile.emptyBundleName

 | 

Optional

 | 

Boolean

 | 

Whether to set the **bundleName** field to an empty value in the product generated after ArkTS compilation and conversion.

-   **true**: The **bundleName** field is empty.
-   **false** (default): The **bundleName** field is set to the actual app bundle name.

NOTE:

-   This field can be set to **true** only when **loadContentByName** is used to load the home page in EntryAbility and the **Navigation** component is used for page redirection. Otherwise, the application will crash.
-   This field cannot be configured during preview. The default value is **false**.

 |
| 

ohos.uiTransform.Optimization

 | 

Optional

 | 

Boolean

 | 

Whether to enable optimization for the **bundleName** field in the product generated after ArkTS compilation and conversion.

-   **true**: Optimization is enabled. The value of **bundleName** is converted into a variable.
-   **false** (default): Optimization is disabled. The value of **bundleName** remains at the actual app bundle name.

This field is supported since DevEco Studio 5.0.5 Beta1.

NOTE:

-   This field does not take effect for bytecode HARs, for which the value of **bundleName** is a variable by default.
-   This field cannot be configured during preview. The default value is **false**.

 |
| 

ohos.har.excludeHspDependencies

 | 

Optional

 | 

Boolean

 | 

Whether to exclude the HSP on which the project depends from the **module.json** file during the build of the HAR. After the exclusion, the **module.json** file does not contain the **dependencies** field.

-   **true**: Exclude the HSP on which the project depends from the **module.json** file.
-   **false** (default): Do not exclude the HSP on which the project depends from the **module.json** file.

This field is supported since DevEco Studio 5.1.0 Release.

 |
| 

ohos.processLib.optimization

 | 

Optional

 | 

Boolean

 | 

Whether to enable performance optimization for the [ProcessLibs task](../../overview/build-tasks/document.md#li671313965913), which can reduce the time required to determine .so file increments during the task.

-   **true**: enabled.
-   **false** (default): disabled.

 |
| 

ohos.obfuscationRules.optimization

 | 

Optional

 | 

Boolean

 | 

Whether to optimize the collection of obfuscation configuration files from third-party dependencies when obfuscation is enabled in release mode. The optimization can reduce the collection time and speed up the compilation.

-   **true**: Enable optimization.
-   **false** (default): Disable optimization.

This field is supported since DevEco Studio 5.1.0 Release.

 |
| 

hvigor.incremental.optimization

 | 

Optional

 | 

Boolean

 | 

Whether to enable incremental task determination optimization. For details about the optimization solution and impact, see [Incremental Task Determination Optimization](../../improving-build-efficiency/enabling-performance-optimization-experimental-features/document.md#section95571022144613).

-   **true**: enabled.
-   **false** (default): disabled.

 |
| 

hvigor.task.schedule.optimization

 | 

Optional

 | 

Boolean

 | 

Whether to enable task scheduling optimization. For details about the optimization solution and impact, see [Task Scheduling Optimization](../../improving-build-efficiency/enabling-performance-optimization-experimental-features/document.md#section09371546164610).

-   **true**: enabled.
-   **false** (default): disabled.

 |
| 

ohos.byteCodeHar.integratedOptimization

 | 

Optional

 | 

Boolean

 | 

Whether to enable bytecode HAR integration optimization. After this feature is enabled, dependencies used by the bytecode HAR can be configured in **dependencies** or **dynamicDependencies** in the project-level **oh-package.json5** file. This optimization also enhances dependency collection behaviors. For details, see [Compilation Behavior Differences](../../configuring-your-build/adding-dependencies/document.md#section957371853712).

-   **true**: enabled.
-   **false** (default): disabled.

This feature is supported since DevEco Studio 5.1.1 Beta1.

 |
| 

ohos.rollupCache.usePathPlaceholder

 | 

Optional

 | 

Boolean

 | 

Whether to replace the absolute path in the rollup cache in the **build** directory with a placeholder. This is a trial feature. Enabling it will degrade the read/write cache performance.

-   **true**: enabled, that is, the placeholder is used.
-   **false** (default): disabled, that is, the absolute path is used.

This feature is supported since DevEco Studio 6.0.0 Beta1.

 |
| 

ohos.rollupCache.useSourceHash

 | 

Optional

 | 

Boolean

 | 

Whether to replace the source code in the rollup cache in the **build** directory with the corresponding hash values to reduce the cache size. This is a trial feature that can improve the cache comparison and read/write performance.

-   **true**: enabled, that is, the hash value of source code is cached.
-   **false** (default): disabled, that is, the source code content is cached.

This feature is supported since DevEco Studio 6.0.0 Beta1.

 |
| 

ohos.arkCompile.writeRollupCache

 | 

Optional

 | 

Boolean

 | 

Whether to write the rollup cache to the **build** directory.

-   **true** (default): enabled.
-   **false**: disabled.

This feature is supported since DevEco Studio 6.0.0 Beta2.

 |
| 

ohos.align.deviceTypes

 | 

Optional

 | 

String array

 | 

Unified device types. During app build, the HAP/HSP module will be packaged into the APP Pack only when the device types defined in **module.json5** of the module are a superset of **ohos.align.deviceTypes**. The device type in the packaged product is set to the value of **ohos.align.deviceTypes**.

This feature is supported since DevEco Studio 6.0.0 Beta2.

NOTE:

Only the stage model is supported.

 |
| 

ohos.dependencies.types.enable

 | 

Optional

 | 

Boolean

 | 

Whether to collect the [type declaration files](../../../application-framework/arkts/arkts-compilation-toolchain/configuring-arkoptions-in-build-profile-json5/document.md#types) of dependent HAR modules or [source code HAR packages](../../configuring-your-build/building-a-har/document.md#section197792874110) for syntax check during compilation. If the type declaration file is configured in the HAR, you are advised to enable this feature.

-   **true**: The type declaration files are collected.
-   **false** (default): The type declaration files are not collected.

This feature is supported since DevEco Studio 6.0.0 Beta3.

 |
| 

ohos.defaults.release.cmakebuildtype

 | 

Optional

 | 

String

 | 

CMake build type in release mode. This field takes effect for all modules.

-   **Debug**: Does not perform code optimization, with debug information attached.
-   **Release**: (Default) Maximizes code optimization, without debug information attached.
-   **RelWithDebInfo**: Optimizes code while retaining debug information. Similar to the **Release** mode.

This field is supported since DevEco Studio 6.0.1 Beta1.

NOTE:

-   You can also specify the CMake build type through the [arguments](../../../coding-and-debugging/analyzing-logs-and-faults/fault-analysis/exception-stack-trace-analysis/document.md#section147714466283) field in the module-level **build-profile.json5** file, for example, **"arguments": "-DCMAKE\_BUILD\_TYPE=RelWithDebInfo"**. The **arguments** field takes precedence over **ohos.defaults.release.cmakebuildtype**.
-   This field is invalid in debug mode. The **Debug** build type is used by default.

 |
| 

ohos.defaults.autoLazyImport

 | 

Optional

 | 

Boolean

 | 

Whether to automatically add the **lazy** keyword to the import statement that complies with the lazy import syntax specifications during compilation. Note that the keyword is to be integrated directly into the source code and does not apply to the dependent bytecode HAR or HSP package. For details about lazy imports, see [Lazy Import](../../../application-framework/arkts/arkts-runtime/arkts-modularization/lazy-import/document.md).

-   **true**: Add the **lazy** keyword.
-   **false** (default): Do not add the **lazy** keyword.

This field is supported since DevEco Studio 6.0.2 Beta1.

NOTE:

-   When this field is set to **true**, scenario identification is skipped during the compilation process, allowing the **lazy** keyword to be added to all eligible import statements across the entire source code.
-   Only the stage model is supported.
-   This feature can also be enabled via the **autoLazyImport** field in the **build-profile.json5** file. Configurations in **autoLazyImport** take precedence over those in **ohos.defaults.autoLazyImport**.

 |

Example configuration:

{
  "properties": {
    "hvigor.cacheDir": "D://tmp",
    "ohos.buildDir": "D://tmp",
    "enableSignTask": true,
    "ohos.arkCompile.maxSize": 6,
    "hvigor.pool.cache.capacity": 2,
    "hvigor.pool.maxSize": 8,
    "ohos.pack.compressLevel": "standard",
    "hvigor.analyzeHtml": true,
    "hvigor.dependency.useNpm": false,
    "ohos.compile.lib.entryfile": true,
    "ohos.align.target": "target1",
    "ohos.fallback.target": \["target1", "target2"\],
    "ohos.arkCompile.sourceMapDir": "D://MyProject",
    "ohos.collect.debugSymbol": false,
    "hvigor.enableMemoryCache": true,
    "hvigor.memoryThreshold": 1000,
    "ohos.nativeResolver": true,
    "ohos.arkCompile.noEmitJs": true,
    "ohos.arkCompile.singleFileEmit": true,
    "ohos.sign.har": true,
    "hvigor.keepDependency": false,
    "ohos.arkCompile.emptyBundleName": true,
    "ohos.align.deviceTypes": \["phone", "tablet"\],
    "ohos.defaults.release.cmakebuildtype": "RelWithDebInfo",
  }
}

#### parameterFile

Since DevEco Studio 6.0.2 Beta1, the parameterization configuration feature has been added to the build process. You can add a parameterization file (a JSON5 file) to maintain values for certain fields in the build configuration file **build-profile.json5**. The project-level or module-specific **build-profile.json5** files will be configured based on the key-value pairs in this file, meeting the need to quickly switch build configurations across different build scenarios.

## Configuration Description

Add the **parameterFile** configuration in the **hvigor-config.json5** file and specify the path to the parameterization file following the configuration rules below:

-   The value of **parameterFile** must be a relative path, with the project-level **hvigor-config.json5** file as its base path, for example, **"parameterFile": "./parameterFile.json5"**.
-   The content of the parameterization file is in JSON5 format and supports multi-level JSON object nesting.
-   The parameter keys in the parameterization file are user-defined. The type and configuration requirements of the parameter values must match the fields they intend to replace. For details, refer to the corresponding fields in the **build-profile.json5** file.
-   Fields in **build-profile.json5** that support parameterization only include **source.sourceRoots**, **resource.directories**, and **buildProfileFields**.
-   In **build-profile.json5**, reference the corresponding custom field from **parameterFile** using the format "@param:key", as shown in the example below.
-   Parameterization configuration is not supported in **hvigorfile.ts** scripts.

## Example

Example of the **parameterFile** field in **hvigor-config.json5**:

{
  "nodeOptions": {
    ...
  },
  "parameterFile": "./parameterFile.json5"
}

Configuration example of the file specified by **parameterFile**

{
  "source": {
    "customizedSourceRoot1": "./src/default1",
    "customizedSourceRoot2": "./src/default2"
  }
}

Example of module-level **build-profile.json5** (with multiple HAR modules):

// build-profile.json5 of the module har1
"targets": \[
  {
    "name": "default",
    "source": {
      "sourceRoots": \["@param:source.customizedSourceRoot1"\]   // sourceRoots must start with '@param:' (replaced with './src/default1' during the build).
    }
  }
\]
// build-profile.json5 of the module har2
"targets": \[
  {
    "name": "default",
    "source": {
      "sourceRoots": \["@param:source.customizedSourceRoot2"\]
    }
  }
\]
