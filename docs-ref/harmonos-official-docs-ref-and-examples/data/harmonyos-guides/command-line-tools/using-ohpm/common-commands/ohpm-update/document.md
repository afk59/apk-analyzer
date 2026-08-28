# ohpm update

Updates a third-party library.

Since ohpm 6.0.2.636, the **log\_level**, **debug**, **lockfile\_stable\_order**, **odm\_r2\_project\_root**, **resolve\_conflict\_strict**, **resolve\_conflict**, and **cache** parameters can be appended to the command.

#### Command Format

ohpm update \[options\] \[\[<@group>/\]<pkg>\] ...
alias: up

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/SB0I_giaSPmbYvNn0Aq_zA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5FE75FA8D02A74F4A26D135A9C8B42E1129986D1C8E131C5DC952E06825D5E26)

-   **@group**: namespace of the third-party library. This parameter is optional.
-   **pkg**: name of the third-party library. This parameter is optional.

#### Description

This command is used to update a locally installed third-party library to its latest version based on the [semver](https://semver.org/) specifications and dependency version. If **pkg** is not specified, the dependencies of the current project will be fully updated and the missing third-party libraries will be installed together.

#### Options

## install\_all

-   Default value: **false**
-   Type: Boolean
-   Alias: all

You can append the **\--all** or **\--install\_all** parameter to the **ohpm update** command. This ensures that after the specified dependencies of the current module are successfully updated, the dependencies of all modules in the current project are installed.

## prefix

-   Default value: ""
-   Value type: string

You can configure the **\--prefix <string>** parameter at the end of the **ohpm update** command to specify the root directory of the package. The root directory must contain the **oh-package.json5** file.

## fetch\_timeout

-   Default value: 60000
-   Type: number
-   Alias: ft

You can configure the **\--ft <number>** or **\--fetch\_timeout <number>** parameter at the end of the **ohpm update** command to set the operation timeout period. If the parameter is not specified, the default timeout period is 60000 ms.

## max\_concurrent

-   Default value: 50
-   Type: number
-   Alias: mc

You can configure the **\--mc <number>** or **\--max\_concurrent <number>** parameter at the end of the **ohpm update** command to set the maximum number of concurrent requests (that is, the maximum number of network requests at any time during the ohpm operation). If the parameter is not specified, the maximum number of concurrent requests is 50 by default.

## retry\_times

-   Default value: 1
-   Type: number
-   Alias: rt

You can configure the **\--rt <number>** or **\--retry\_times <number>** parameter at the end of the **ohpm update** command to set the maximum number of retries before an operation fails. If the parameter is not specified, the maximum number of retries is **1** by default.

## retry\_interval

-   Default value: 1000
-   Type: number
-   Alias: ri

You can configure the **\--ri <number>** or **\--retry\_interval <number>** parameter at the end of the **ohpm update** command to set the retry interval. If the parameter is not specified, the default retry interval is 1000 ms.

## strict\_ssl

-   Default value: true
-   Value type: boolean

You can configure **\--strict\_ssl true** at the end of the **ohpm update** command to enable HTTPS certificate verification or configure **\--strict\_ssl false** to disable it.

## registry

-   Default value: ""
-   Type: URL

You can configure the **\--registry <registry>** parameter at the end of the **ohpm update** command to specify a repository address. If the parameter is not specified, the repository address is obtained from the configuration by default.

## all-modules

-   Default value: ""
-   Type: Boolean

You can configure the **\--all-modules** parameter at the end of the **ohpm update** command to update the dependencies of all modules.

## tag-filter

-   Default value: none
-   Type: Regex

You can configure the **\--tag-filter <regex>** parameter at the end of the **ohpm update** command to update only the dependencies whose tags match the specified regular expression. Use the **\--tag-filter** parameter to update the dependencies of all modules by default.

## experimental-concurrently-safe

-   Default value: true
-   Value type: boolean

You can configure the **\--experimental-concurrently-safe** parameter at the end of the **ohpm update** command to update dependencies concurrently and securely. This is an experimental parameter.

## log\_level

-   Default value: none
-   Value type: string

You can append the **\--log\_level <string>** parameter to the **ohpm update** command to specify the log level (**info**, **debug**, **warn**, or **error**) for the execution of the current command. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## debug

-   Default value: false
-   Value type: boolean

You can append the **\--debug** parameter to the command to set the log level to **debug** for the execution of the current command. This configuration takes effect only on the current command line and does not alter the log level configured in the .ohpmrc file. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## lockfile\_stable\_order

-   Default value: false
-   Value type: boolean

You can append the **\--lockfile\_stable\_order** parameter to the **ohpm update** command. This ensures that if the **oh-package.json5** file is not changed, the fields in the generated **oh-package-lock.json5** file remain unchanged.

## odm\_r2\_project\_root

-   Default value: false
-   Value type: boolean

You can append the **\--odm\_r2\_project\_root** parameter to the **ohpm update** command. This ensures that if the **overrideDependencyMap** configuration exists and the target configuration file contains dependencies configured with relative paths, ohpm will resolve and locate these relative paths based on the project root path. For details, see [odm\_r2\_project\_root](../../ohpmrc/document.md#section136621053184912).

## resolve\_conflict\_strict

-   Default value: false
-   Value type: boolean

You can append the **\--resolve\_conflict\_strict** parameter to the **ohpm update** command to enable the strict mode for handling dependency version conflicts. For details, see [resolve\_conflict\_strict](../../ohpmrc/document.md#section1942983310492).

## resolve\_conflict

-   Default value: false
-   Value type: boolean

You can append the **\--resolve\_conflict** parameter to the **ohpm update** command to have ohpm automatically resolve dependency version conflicts. For details, see [resolve\_conflict](../../ohpmrc/document.md#section368717475562).

## cache

-   Default value: none
-   Value type: string

You can append the **\--cache <string>** parameter to the **ohpm update** command to specify the cache path.

#### Example

If the current third-party library is an app and its dependency is dep1 ( dep2,...), the released versions of dep1 are as follows:

{
  "dist-tags": { "latest": "1.2.2", "release": "1.2.0" },
  "versions": \[
    "1.2.2",
    "1.2.1",
    "1.2.0",
    "1.1.2",
    "1.1.1",
    "1.0.0",
    "0.4.1",
    "0.4.0",
    "0.2.0"
  \]
}

## ^ Dependency

Using the ^ symbol will update **y** and **z** in version x.y.z to their latest versions. Assume that the version number of **dep1** in the **oh-package.json5** file of the app is as follows:

"dependencies": {
  "dep1": "^1.1.1"
}

As the latest version is **1.2.2**, running the **ohpm update** command will update the version to **dep1@1.2.2**.

## ~ Dependency

Using the ~ symbol will update **z** in version x.y.z to its latest version. Assume that the version number of **dep1** in the **oh-package.json5** file of the app is as follows:

"dependencies": {
  "dep1": "~1.1.1"
}

Although the latest version is **1.2.2**, running the **ohpm update** command will update the version to **dep1@1.1.2** due to the use of the ~ symbol.

## Tag Dependencies

If a tag is used, dependencies will be updated to the version corresponding to the tag. Assume that the version number of **dep1** in the **oh-package.json5** file of the app is as follows:

"dependencies": {
  "dep1": "tag:release"
}

If the release tag is updated to point to version 1.2.2, running **ohpm update --tag-filter ^r** will update dep1 from 1.2.0 to 1.2.2. As dep1 is imported through the release tag, and the release tag matches the ^r regex pattern specified by **\--tag-filter**, ohpm will obtain dep1 at 1.2.2.

## ^ Dependency with Version Earlier than 1.0.0

-   Assume that the version number of **dep1** of the app is earlier than 1.0.0 and contains the ^ symbol as follows:
    
    "dependencies": {
      "dep1": "^0.2.0"
    }
    
    Running the **ohpm update** command will install dep1@0.2.0 because no other version meets ^0.2.0 requirements.
    
-   If the version number of **dep1** is **^0.4.0**:
    
    "dependencies": {
      "dep1": "^0.4.0"
    }
    
    Running the **ohpm update** command will install dep1@0.4.1 because it is the highest version after sorting and meets ^0.4.0 requirements (0.4.0 ≤ version < 0.5.0).
