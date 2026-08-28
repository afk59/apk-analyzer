# Using hvigorw

hvigorw is the wrapper tool for the Hvigor build tool. It facilitates the automatic installation of Hvigor and its required plugin dependencies, and enables the execution of Hvigor build commands.

Before command execution, make sure the required environments, including JDK, Node.js, and Hvigor, are configured. For details, see [Setting Up a Pipeline](../setting-up-a-pipeline/document.md).

#### Format of the hvigorw command:

The hvigorw command format is as follows:

hvigorw \[taskNames...\] <options>

**taskNames** indicates tasks to execute. Multiple tasks can be executed simultaneously. **options** is an optional parameter. For details, see [Common Commands](#section16300629103).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/NBGRxR36QSSkkXOBlHHBLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C10B91C2D36AA07675B9D974AD733D44653262FAC01C9C7EF4A25CD09B1D8E02)

Since hvigorw 5.18.4, the following commands can be executed from any directory path. However, all other hvigorw commands must be executed from the root directory of the project.

-   hvigorw -v
-   hvigorw --version
-   hvigorw version
-   hvigorw -h
-   hvigorw --help

#### Common Commands

Below are common tasks and their associated parameters. For more information about tasks, see [Task Categories](../../building-an-app/overview/build-tasks/document.md#section196919100414).

## Query

| 
**Parameter**

 | 

Description

 |
| :-- | :-- |
| 

\-h, --help

 | 

Prints help information about the hvigorw command.

 |
| 

\-v, --version, version

 | 

Displays hvigorw version information.

 |

## Compilation and Building

| 
Task

 | 

Description

 |
| :-- | :-- |
| 

clean

 | 

Cleans the build output directory.

 |
| 

collectCoverage

 | 

Generates a coverage statistics report based on the collected data.

 |
| 

assembleHap

 | 

Builds a HAP.

 |
| 

assembleApp

 | 

Builds an App Pack.

 |
| 

assembleHsp

 | 

Builds an HSP.

 |
| 

assembleHar

 | 

Builds a HAR.

 |

Common extended parameters of the compilation and building command line

| 
Parameter

 | 

Description

 |
| :-- | :-- |
| 

\-p buildMode={debug | release}

 | 

Uses the debug or release mode for builds.

By default, the debug mode is used in building HAPs, HSPs, or HARs, and the release mode is used in building App Packs.

For details about build modes, see [Setting the Build Mode](../../building-an-app/customizing-your-build/customizing-build-options/introduction/document.md#section192461528194916). For details about how to build a HAR, see [Building a HAR](../../building-an-app/configuring-your-build/building-a-har/document.md).

 |
| 

\-p debuggable=true/false

 | 

Specifies whether the product is debuggable. This configuration will override the **debuggable** setting in **buildOption** within the build mode.

For details about the priority of **debuggable** settings, see [Rules for Combining Build Options](../../building-an-app/customizing-your-build/customizing-build-options/introduction/document.md#section1727865610255).

 |
| 

\-p product={ProductName}

 | 

Specifies the target product under which the module targets are built.

Default value: **default**

 |
| 

\-p module={ModuleName}@{TargetName}

 | 

Specifies the module and target for builds. You can specify multiple modules of the same type, separated with commas (,).

Note: This option must be used together with **\--mode module**.

By default, all modules in the project are built when the AssembleHap task is executed, and **default** is used for **TargetName**.

 |
| 

\-p ohos-test-coverage={true | false}

 | 

Executes the instrumentation compilation of the test framework code coverage.

 |
| 

\-p coverage={true | false}

 |
| 

\-p parameterFile=param.json/json5

 | 

Sets the parameter configuration file in **oh-package.json5**. The value of **param** can be changed to the name of the corresponding configuration file. For details, see [parameterFile](../using-ohpm/oh-package-json5/document.md#section122411462820).

 |

Test-related command-line options:

| 
Command

 | 

Description

 |
| :-- | :-- |
| 

hvigorw onDeviceTest -p module={moduleName} -p coverage={true | false} -p scope={suiteName}#{methodName} -p ohos-debug-asan={true|false}

 | 

Runs an instrument test.

-   **module**: module on which the test is performed. By default, the test cases of all modules are performed. The HAP, HAR, and HSP modules are supported.
-   **coverage**: whether to generate a coverage report. The default value is **true**.
-   **scope**: test case, in the format of {suiteName}#{methodName}, or test suite, in the format of {suiteName} for execution. By default, all cases of the current module are executed.
-   **ohos-debug-asan**: whether to enable ASan detection. The default value is **false**. This option is supported since hvigorw 5.19.0.

Multiple values of **module** and **scope** can be specified, separated by commas (,).

-   Path to the coverage report: **<_module-path_\>/.test/default/outputs/ohosTest/reports**
-   Test result file: path\_to\_project/module\_name/.test/default/intermediates/ohosTest/coverage\_data/test\_result.txt
-   ASan log path: **<_module-path_\>/.test/default/intermediates/ohosTest/coverage\_data**

 |
| 

hvigorw test -p module={moduleName} -p coverage={true | false} -p scope={suiteName}#{methodName}

 | 

Runs a local test. The command cannot be executed on Linux.

-   **module**: module on which the test is performed. By default, the test cases of all modules are performed. The HAP, HAR, and HSP modules are supported.
-   **coverage**: whether to generate a coverage report. The default value is **true**.
-   **scope**: test case, in the format of {suiteName}#{methodName}, or test suite, in the format of {suiteName} for execution. By default, all cases of the current module are executed.

Multiple values of **module** and **scope** can be specified, separated by commas (,).

-   Coverage report file:
    
    <module-path>/.test/default/outputs/test/reports
    
-   Test result file: path\_to\_project/module\_name/.test/default/intermediates/test/coverage\_data/test\_result.txt

 |

## Logs

| 
Parameter

 | 

Description

 |
| :-- | :-- |
| 

\-e, --error

 | 

Sets the Hvigor log level to **error**.

 |
| 

\-w, --warn

 | 

Sets the Hvigor log level to **warn**.

 |
| 

\-i, --info

 | 

Sets the Hvigor log level to **info**.

 |
| 

\-d, --debug

 | 

Sets the Hvigor log level to **debug**.

 |
| 

\--stacktrace, --no-stacktrace

 | 

Enables the printing of stack information for all exceptions. This feature is disabled by default.

 |

## Visualization

| 
Parameter

 | 

Description

 |
| :-- | :-- |
| 

\--analyze=normal

 | 

Starts Build Analyzer in normal mode, so that it performs analysis based on simple logging data.

 |
| 

\--config properties.hvigor.analyzeHtml=true

 | 

Creates a visualization HTML file in the **.hvigor/report** directory of the project. The file can be opened in a browser.

 |
| 

\--analyze=false

 | 

Disables Build Analyzer.

 |
| 

\--analyze=advanced

 | 

Starts Build Analyzer in advanced mode so that it performs analysis based on detailed trace data. Select this mode if you need more details on the task consumption time.

 |
| 

\--analyze=ultrafine

 | 

Enables Build Analyzer and sets the analysis mode to **ultrafine**. Compared with the **advanced** mode, this mode records more detailed trace data during ArkTS compilation. However, enabling this mode may take a longer time for compilation and build.

This option is supported since hvigorw 6.0.0.

 |
| 

\--analyze

 | 

Same as the **\--analyze=normal** command.

This option is deprecated since hvigorw 4.3.0. Use **\--analyze=normal** instead.

 |
| 

\--no-analyze

 | 

Same as the **\--analyze=false** command.

This option is deprecated since hvigorw 4.3.0. Use **\--analyze=false** instead.

 |
| 

\--verbose-analyze

 | 

Same as the **\--analyze=advanced** command.

This option is deprecated since hvigorw 4.3.0. Use **\--analyze=advanced** instead.

 |

## daemon

| 
Parameter

 | 

Description

 |
| :-- | :-- |
| 

\--daemon

 | 

Enables usage of the [daemon process](../../building-an-app/improving-build-efficiency/using-the-daemon-process/document.md).

 |
| 

\--no-daemon

 | 

Disables usage of the daemon process for Hvigor. By default, usage of the daemon process is enabled.

This option is recommended in command line mode.

 |
| 

\--stop-daemon

 | 

Stops the daemon process of the current project.

 |
| 

\--stop-daemon-all

 | 

Stops the daemon processes of all projects.

 |
| 

\--status-daemon

 | 

Queries information about all Hvigor daemon processes in the current environment.

 |
| 

\--max-old-space-size=12345

 | 

Sets the maximum size of the old-generation memory for the daemon process to 12345 MB.

 |
| 

\--max-semi-space-size=32

 | 

Sets the maximum semi-space size of the young-generation memory for the daemon process to 32 MB.

This option is supported since hvigorw 5.18.4.

 |

## Performance/Memory

| 
Parameter

 | 

Description

 |
| :-- | :-- |
| 

\--parallel, --no-parallel

 | 

Enables or disables [parallel build](../../building-an-app/improving-build-efficiency/enabling-parallel-build/document.md) for Hvigor. By default, parallel build is enabled. To disable it, add **\--no-parallel** at the end of the command line.

 |
| 

\--incremental, --no-incremental

 | 

Enables or disables [incremental build](../../building-an-app/improving-build-efficiency/conducting-an-incremental-build/document.md) for Hvigor. By default, incremental build is enabled. To disable it, add **\--no-incremental** at the end of the command line.

 |
| 

\--optimization-strategy=performance

 | 

Sets the build mode to performance first. This mode accelerates the build speed, but occupies more memory.

This option is supported since hvigorw 5.19.2.

 |
| 

\--optimization-strategy=memory

 | 

Set the build mode to memory first. This mode reduces the compilation memory usage. The **memory** build mode is used by default.

This option is supported since hvigorw 5.19.2.

 |

## Common options

| 
Task

 | 

Description

 |
| :-- | :-- |
| 

tasks

 | 

Prints task information for each module in a project.

 |
| 

taskTree

 | 

Prints task dependency information for each module in a project.

 |
| 

prune

 | 

Clears the Hvigor cache files that are not used within 30 days and deletes the packages that are not referenced from the pnpm repository.

 |
| 

buildInfo

 | 

Prints the configuration information, such as **product**, **module**, **target**, **buildMode**, and **buildOption**, in the project-level or module-level **build-profile.json5** file to a tree structure.

This feature is supported since hvigorw 5.18.4.

 |

Extended parameters of the **buildInfo** command:

| 
Parameter

 | 

Description

 |
| :-- | :-- |
| 

\-p module={ModuleName}

 | 

Specifies the name of the module whose configuration information needs to be printed. If this parameter is not specified, the configuration information of the project is printed.

 |
| 

\-p buildOption

 | 

Specifies whether to print the **buildOption** configurations. If this parameter is not included, the **buildOption** configurations are not printed. For details about the priority of **buildOption** configurations, see [Rules for Combining Build Options](../../building-an-app/customizing-your-build/customizing-build-options/introduction/document.md#section1727865610255).

 |
| 

\-p json

 | 

Displays the output result in JSON format.

 |

## Other options

| 
Parameter

 | 

Description

 |
| :-- | :-- |
| 

\-s,--sync

 | 

Processes Hvigor project information and persistently stores it in **./hvigor/outputs/sync/output.json**.

 |
| 

\-m,--mode

 | 

Executes a task in the corresponding directory. For example, **hvigorw clean -m project** clears the **build** directory in the project (that is, the **build** folder at the project level).

 |
| 

\--enable-build-script-type-check

 | 

Enables hvigorfile.ts type check for a project. This option is deprecated. Use **\--type-check** instead.

 |
| 

\--type-check, --no-type-check

 | 

Enables **hvigorfile.ts** type check for a project. By default, **hvigorfile.ts** type check is disabled.

 |
| 

\--no-pnpm-frozen-lockfile, --pnpm-frozen-lockfile

 | 

Ignores the **pnpm-lock.yaml** file, and installs the Hvigor dependencies based on the configuration in the **hvigor-config.json5** file.

If the **pnpm-lock.yaml** file is not ignored, an error will be reported when the Hvigor dependencies are installed for Hvigor 2.0.0 or later in the CI scenario. By default, the **pnpm-lock.yaml** file is not ignored.

NOTE:

This option is deprecated since DevEco Studio 4.1 Release. The installation is automatically done in the CI scenario.

 |
| 

\--config, -c

 | 

Configures parameters in the **hvigor-config.json5** file.

Currently, only parameters in **properties** can be set. For details, see [hvigor-config.json5](../../building-an-app/configuration-files/hvigor-config-json5-file/document.md).

**\--config properties.key=value** is equivalent to **\-c properties.key=value**.

 |
| 

\--watch

 | 

Enables the watch mode, which is mainly used in preview and hot reload scenarios.

 |
| 

\--generate-build-profile, --no-generate-build-profile

 | 

Deprecated. Enables the generation of the **BuildProfile.ets** file.

 |
| 

\--node-home <string>

 | 

Specifies the Node.js path.

 |
