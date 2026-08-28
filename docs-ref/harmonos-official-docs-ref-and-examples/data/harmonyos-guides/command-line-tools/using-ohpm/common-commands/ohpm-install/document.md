# ohpm install

Installs a third-party library.

Since ohpm 6.0.2.636, the **log\_level**, **debug**, **lockfile\_stable\_order**, **odm\_r2\_project\_root**, **enable\_cross\_process\_lock**, **resolve\_conflict\_strict**, **resolve\_conflict**, and **cache** parameters can be appended to the command.

#### Command Format

ohpm install \[options\] \[\[<@group>/\]<pkg>\[@<version> | @tag:<tag>\]\] ...
ohpm install \[options\] <folder> 
ohpm install \[options\] <har file>
alias: i

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/2vSX-cTcTe--1o4cj2u-HQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=316A1DA4E5829887BCA91CF77716F320F556F8F1589D3CA2EFD078D2759CC6EA)

-   **@group**: namespace of the third-party library. This parameter is optional.
-   **pkg**: name of the third-party library. This parameter is optional. If the name of the third-party library is not specified, full installation is performed based on the dependencies defined in **oh-package.json5** in the current directory.
-   **version**: version number of the third-party library. This parameter is optional.
-   **tag**: tag of the third-party library, marking a specific version number. This parameter is optional.

#### Description

This command is used to install a specified component or all dependencies in the **oh-package.json5** file. If the **oh-package-lock.json5** file exists, the installation depends on the version specified in the **oh-package-lock.json5** file.

-   ohpm install
    
    Installs dependencies to the local **oh\_modules** folder and writes all dependencies to the **oh-package.json5** file.
    
-   ohpm install <folder>
    
    Installs a local folder. By default, a symbolic link pointing to the folder is created.
    
    Example:
    
    ohpm install ../folder
    
-   ohpm install <har file>
    
    Installs a compressed package. Pay attention to the following requirements:
    
    1.  The file name extension must be .tar, .tar.gz, .tgz, or .har.
    2.  The compressed package contains the **package** folder.
    3.  The **package** folder must contain the **oh-package.json5** file, which must contain the **name** and **version** fields.
    
    Example:
    
    ohpm install ./package.har
    

#### Options

## install\_all

-   Default value: true
-   Value type: boolean
-   Alias: all

You can append the **\--all** or **\--install\_all** parameter to the **ohpm install** command to install all dependencies configured in the **oh-package.json5** file for all modules in your project.

## save-dynamic

-   Default value: false
-   Value type: boolean

You can configure the **\--save-dynamic** parameter at the end of the **ohpm install** command to write information about the installed third-party library to **dynamicDependencies** in the **oh-package.json5** file.

## save-dev

-   Default value: false
-   Value type: boolean

You can configure the **\--save-dev** parameter at the end of the **ohpm install** command to write information about the installed third-party library to **devDependencies** in the **oh-package.json5** file.

## save-prod

-   Default value: true
-   Value type: boolean

You can configure the **\--save-prod** parameter at the end of the **ohpm install** command to write information about the installed third-party library to **dependencies** in the **oh-package.json5** file. This is the default behavior of ohpm.

## no-save

-   Default value: false
-   Value type: boolean

You can configure the **\--no-save** parameter at the end of the **ohpm install** command to not write information about the installed third-party library to the **oh-package.json5** file.

## prefix

-   Default value: ""
-   Value type: string

You can configure the **\--prefix <string>** parameter at the end of the **ohpm install** command to specify the root directory of the package. The root directory must contain the **oh-package.json5** file.

## parameterFile

-   Default value: none
-   Value type: string
-   Alias: pf

You can configure the **\--pf <string>** or **\--parameterFile <string>** parameter at the end of the **ohpm install** command to specify the path of the parameterization configuration file. Before running this command, ensure that **parameterFile** is configured in the project-level **oh-package.json5** file.

## registry

-   Default value: ""
-   Type: URL

You can configure the **\--registry <registry>** parameter at the end of the **ohpm install** command to specify a repository address. If the repository address is not specified, the repository address is obtained from the configuration by default.

## fetch\_timeout

-   Default value: 60000
-   Type: number
-   Alias: ft

You can configure the **\--ft <number>** or **\--fetch\_timeout <number>** parameter at the end of the **ohpm install** command to set the operation timeout period. If the parameter is not specified, the default timeout period is 60000 ms.

## strict\_ssl

-   Default value: true
-   Value type: boolean

You can configure **\--strict\_ssl true** at the end of the **ohpm install** command to enable HTTPS certificate verification or configure **\--strict\_ssl false** to disable it.

## max\_concurrent

-   Default value: 50
-   Type: number
-   Alias: mc

You can configure the **\--mc <number>** or **\--max\_concurrent <number>** parameter at the end of the **ohpm install** command to set the maximum number of concurrent requests (the maximum number of network requests at any time during the ohpm operation). If the parameter is not specified, the default value **50** is used.

## retry\_times

-   Default value: 1
-   Type: number
-   Alias: rt

You can configure the **\--rt <number>** or **\--retry\_times <number>** parameter at the end of the **ohpm install** command to set the maximum number of retry times for an operation. If the parameter is not specified, the default value **1** is used.

## retry\_interval

-   Default value: 1000
-   Type: number
-   Alias: ri

You can configure the **\--ri <number>** or **\--retry\_interval <number>** parameter at the end of the **ohpm install** command to set the retry interval. If the parameter is not specified, the default value **1000** (in ms) is used.

## experimental-concurrently-safe

-   Default value: true
-   Value type: boolean

You can configure the **\--experimental-concurrently-safe** parameter at the end of the **ohpm install** command to install dependencies concurrently and securely. This is an experimental option.

## target\_path

-   Default value: none
-   Value type: string

You can configure the **\--target\_path <string>** parameter at the end of the **ohpm install** command to specify the path of the dependency configuration file (**oh-package.json5**) of each module in the context of a specific target product. When you run the **ohpm install** command, ohpm installs the dependency in the **<_target\_path_\>/<_moduleName_\>/oh-package.json5** file first. For details, see [target\_path](#section79331822125611).

## log\_level

-   Default value: none
-   Value type: string

You can append the **\--log\_level <string>** parameter to the **ohpm install** command to specify the log level (**info**, **debug**, **warn**, or **error**) for the execution of the current command. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## debug

-   Default value: false
-   Value type: boolean

You can append the **\--debug** parameter to the command to set the log level to **debug** for the execution of the current command. This configuration takes effect only on the current command line and does not alter the log level configured in the .ohpmrc file. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## lockfile\_stable\_order

-   Default value: false
-   Value type: boolean

You can append the **\--lockfile\_stable\_order** parameter to the **ohpm install** command. This ensures that if the **oh-package.json5** file is not changed, the fields in the generated **oh-package-lock.json5** file remain unchanged.

## odm\_r2\_project\_root

-   Default value: false
-   Value type: boolean

You can append the **\--odm\_r2\_project\_root** parameter to the **ohpm install** command. If the **overrideDependencyMap** configuration exists and the target configuration file contains dependencies configured with relative paths, ohpm will resolve and locate these relative paths based on the project root path. For details, see [odm\_r2\_project\_root](../../ohpmrc/document.md#section136621053184912).

## enable\_cross\_process\_lock

-   Default value: false
-   Value type: boolean

You can append the **\--enable\_cross\_process\_lock** parameter to the **ohpm install** command. Due to the restrictions of the **oh\_modules** directory structure, ohpm does not support the parallel execution of multiple **ohpm install**, **ohpm update**, or **ohpm uninstall** commands within the same project. To execute these commands in parallel for a project, set this parameter to **true** to have them run sequentially.

## resolve\_conflict\_strict

-   Default value: false
-   Value type: boolean

You can append the **\--resolve\_conflict\_strict** parameter to the **ohpm install** command to enable the strict mode for handling dependency version conflicts. For details, see [resolve\_conflict\_strict](../../ohpmrc/document.md#section1942983310492).

## resolve\_conflict

-   Default value: false
-   Value type: boolean

You can append the **\--resolve\_conflict** parameter to the **ohpm install** command to have ohpm automatically resolve dependency version conflicts. For details, see [resolve\_conflict](../../ohpmrc/document.md#section368717475562).

## cache

-   Default value: none
-   Value type: string

You can append the **\--cache <string>** parameter to the **ohpm install** command to specify the cache path.

#### Example

Run the following command to install Lottie:

ohpm install @ohos/lottie

Below is an output example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/eDolQ2-bR6WCpLZ39zavNQ/en-us_image_0000002532750529.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=491E12AE396050EC7AB0194BC48B9BE0F9A0894AC335C310F88D78240075B30A "Click to enlarge")

#### oh\_modules

## ohpm 1.0.0 to ohpm 1.3.0

During the execution of **ohpm install**, the dependencies of each module in the project are all installed in **oh\_modules** in the module-specific root directory. All direct and indirect dependencies of the module are stored in tile mode in **.ohpm** in the **oh\_modules** directory, and direct dependencies are added to the root directory of **oh\_modules** as a symbolic link. Therefore, the same dependency is installed only once, reducing disk space usage and accelerating installation.

## ohpm 1.4.x and later

From ohpm client 1.4.0, the dependencies of every module in the project are all installed in **oh\_modules** in the root directory of the project. In addition, symbolic links of the direct dependencies of a module are generated in **oh\_modules** in the module-specific root directory. These symbolic links point to the actual storage directories in **.ohpm** of **oh\_modules** in the root directory of the project.

#### target\_path

To support customized dependencies for different build targets during the build process, Hvigor automatically generates tailored dependency configuration files (**oh-package.json5**) for each module based on the target build product. You can use the **target\_path** option with the **ohpm install** command to specify the path for the dependency configuration files (**oh-package.json5**) of each module within the context of a specific target product.

ohpm gives precedence to the dependencies specified in **<target\_path>/moduleName/oh-package.json5**. It generates a lock file named **oh-package-<targetName>-lock.json5** in the **<project\_root>/moduleName/** directory. When **target\_path** is specified, the automatic handling of dependency version conflicts is enabled by default. After the dependencies are installed, ohpm will create new **oh-package.json5** files in the **<_target\_path_\>/resolve-conflict/_moduleName_/** directory.

The following is an example of the **target\_path** directory structure:

+---default                   // <targetName> defaults to default.
|   |   dependencyMap.json5   // Path of the dependency configuration file of each module in a specific target context.
|   +---module1               // Directory for storing the dependency configuration file of a module in a specific target context. The directory name is the same as the root directory of the original module.
|   |       oh-package.json5  // Configuration file on which a module depends in a specific target context.
|   +---module2
|   |       oh-package.json5
|   |   oh-package.json5      // Project-level dependency configuration file generated in a specific target context.

The following is an example of the **dependencyMap.json5** file:

{
  targetName: "default",
  rootDependency: "./oh-package.json5",
  dependencyMap: {
       "module1": "./module1/oh-package.json5",
       "module2": "./module2/oh-package.json5"
  }
}

When the **ohpm install** command is used with a specified **target\_path**, the priority of dependency configurations is determined by a specific hierarchy, as follows:

1\. The **oh-package.json5** configured in **rootDependency** under **<target\_path>/dependencyMap.json5** takes precedence over the **oh-package.json5** at the project root, that is, **<project\_root>/oh-package.json5**.

2\. The configurations specified in the project-level configuration file pointed to by **projectPackageJson** in the .ohpmrc file, particularly the **overrides** and **overrideDependencyMap**, have a higher priority than: (1) the corresponding configurations in the **oh-package.json5** as configured by **rootDependency** in **<target\_path>/dependencyMap.json5**; (2) the corresponding configurations in **<project\_root>/oh-package.json5**.

3\. **<target\_path>/moduleName/oh-package.json5** has a higher priority than the dependency configuration files specified in **overrideDependencyMap**.

4\. The dependency versions specified in **overrides** have the higher priority than the dependency versions specified in **<target\_path>/moduleName/oh-package.json5**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/tMhd2gvGQKSVdU4a6PxWiA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36DAA772CCD8CFB6617392F7828147430D17DD23A259CC2DCE4E5A19E04343F8)

If **targetName** in **<target\_path>/dependencyMap.json5** is non-empty and not **"default"**, the naming of the lock file in the **<project\_root>/moduleName directory** is adjusted to **oh-package-<targetName>-lock.json5**.
