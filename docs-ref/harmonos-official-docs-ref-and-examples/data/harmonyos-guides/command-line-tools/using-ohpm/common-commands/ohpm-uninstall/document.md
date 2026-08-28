# ohpm uninstall

Uninstalls a third-party library.

Since ohpm 6.0.2.636, the **log\_level**, **debug**, **lockfile\_stable\_order**, **odm\_r2\_project\_root**, **resolve\_conflict\_strict**, **resolve\_conflict**, and **cache** parameters can be appended to the command.

#### Command Format

ohpm uninstall \[options\] \[<@group>/\]<pkg> ...
alias: un

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/y5b4PISTT1e15xzE3j_7jg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EBE65A68F0AB4B0BF5682F73677DDED0060132A89684A412965759F508DB88E3)

-   **@group**: namespace of the third-party library. This parameter is optional.
-   **pkg**: name of the third-party library. This parameter is mandatory.

#### Description

This command is used to uninstall a specified third-party library and remove information about the third-party library specified in **dependencies** and **devDependencies** from the **oh-package.json5** file. If no third-party library is specified, no action is performed.

If you do not need to remove the information specified in **dependencies** or **devDependencies** from the **oh-package.json5** file, configure the **\--no-save** parameter.

#### Options

## install\_all

-   Default value: false
-   Value type: boolean
-   Alias: all

You can append the **\--all** or **\--install\_all** parameter to the **ohpm uninstall** command. This ensures that after the specified dependencies of the current module are successfully uninstalled, the dependencies of all modules in the current project are installed.

## no-save

-   Default value: false
-   Value type: boolean

To prevent information of uninstalled third-party libraries from being removed from the **oh-package.json5** file, you can configure the **\--no-save** parameter at the end of the **ohpm uninstall** command.

## prefix

-   Default value: ""
-   Value type: string

You can configure the **\--prefix <string>** parameter at the end of the **ohpm uninstall** command to specify the root directory of the package. The root directory must contain the **oh-package.json5** file.

## registry

-   Default value: ""
-   Type: URL

You can configure the **\--registry <registry>** parameter at the end of the **ohpm uninstall** command to specify a repository address. If the **oh-package.json5** file contains a third-party package that hasn't been installed, this package will be automatically obtained from the repository indicated by **registry** and installed following the execution of the uninstall command. If no repository address is specified, the repository address is obtained from the configuration by default.

## fetch\_timeout

-   Default value: 60000
-   Type: number
-   Alias: ft

You can configure the **\--ft <number>** or **\--fetch\_timeout <number>** parameter at the end of the **ohpm uninstall** command to set the operation timeout period. If the parameter is not specified, the default timeout period is 60000 ms.

## strict\_ssl

-   Default value: true
-   Value type: boolean

You can configure **\--strict\_ssl true** at the end of the **ohpm uninstall** command to enable HTTPS certificate verification or configure **\--strict\_ssl false** to disable it.

## experimental-concurrently-safe

-   Default value: true
-   Value type: boolean

You can configure the **\--experimental-concurrently-safe** parameter at the end of the **ohpm install** command to install dependencies concurrently and securely. This is an experimental parameter.

## log\_level

-   Default value: none
-   Value type: string

You can append the **\--log\_level <string>** parameter to the **ohpm uninstall** command to specify the log level (**info**, **debug**, **warn**, or **error**) for the execution of the current command. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## debug

-   Default value: false
-   Value type: boolean

You can append the **\--debug** parameter to the command to set the log level to **debug** for the execution of the current command. This configuration takes effect only on the current command line and does not alter the log level configured in the .ohpmrc file. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## lockfile\_stable\_order

-   Default value: false
-   Value type: boolean

You can append the **\--lockfile\_stable\_order** parameter to the **ohpm uninstall** command. This ensures that if the **oh-package.json5** file is not changed, the fields in the generated **oh-package-lock.json5** file remain unchanged.

## odm\_r2\_project\_root

-   Default value: false
-   Value type: boolean

You can append the **\--odm\_r2\_project\_root** parameter to the **ohpm uninstall** command. This ensures that if the **overrideDependencyMap** configuration exists and the target configuration file contains dependencies configured with relative paths, ohpm will resolve and locate these relative paths based on the project root path. For details, see [odm\_r2\_project\_root](../../ohpmrc/document.md#section136621053184912).

## resolve\_conflict\_strict

-   Default value: false
-   Value type: boolean

You can append the **\--resolve\_conflict\_strict** parameter to the **ohpm uninstall** command to enable the strict mode for handling dependency version conflicts. For details, see [resolve\_conflict\_strict](../../ohpmrc/document.md#section1942983310492).

## resolve\_conflict

-   Default value: false
-   Value type: boolean

You can append the **\--resolve\_conflict** parameter to the **ohpm uninstall** command to have ohpm automatically resolve dependency version conflicts. For details, see [resolve\_conflict](../../ohpmrc/document.md#section368717475562).

## cache

-   Default value: none
-   Value type: string

You can append the **\--cache <string>** parameter to the **ohpm uninstall** command to specify the cache path.

#### Example

Uninstall the package of a direct dependency from the current project.

Run the following command:

ohpm uninstall lottie

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/mwjpMgmjSmqt32aZC5WK6A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E01498ED960A2A3EED4AB0F3860BF78FCA347E8128FCA2178B40D3C2E7F38E22)

-   ohpm 1.0.0 to ohpm 1.3.0
    -   If the JSON file is the package of a direct dependency, the **lottie** folder in the **oh\_modules** directory of the current project is deleted, the indirect dependencies of the JSON file may also be deleted (if the indirect dependency package is not referenced by other third-party packages).
    -   The corresponding line (for example, "lottie": "2.0.7") is deleted from **dependencies** in the **oh-package.json5** file.
-   ohpm 1.4.x and later
    -   Running the **ohpm uninstall** command will not delete the **lottie** folder in the project-level **oh\_modules** directory, but it deletes the **lottie** folder in the module-level **oh\_modules** directory.
    -   The corresponding line (for example, "lottie": "2.0.7") is deleted from **dependencies** in the **oh-package.json5** file.
