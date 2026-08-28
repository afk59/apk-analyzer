# ohpm unpublish

Unpublishes a third-party library.

Since ohpm 6.0.2.636, the **log\_level** and **debug** parameters can be appended to the command to obtain the log level and specify the log level for the current command execution.

#### Command Format

ohpm unpublish \[options\] \[<@group>\]<pkg>\[@<version>\]

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/KdiAGh-tSM-bjGqEHB4iRw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D86E84CD33FF12B41669D5303959DFA294184EE41CC5AFA02D82CF513B658B6C)

-   **@group**: namespace of the third-party library. This parameter is optional.
-   **pkg**: name of the third-party library. This parameter is mandatory.
-   **version**: version number of the third-party library. This parameter is optional.

#### Description

-   This command is used to unpublish an approved third-party library from the central repository for OpenHarmony third-party libraries.
-   If no version is specified, all versions of the specified third-party library are unpublished by default, on the prerequisites that the **\-f** parameter is added. After all versions are removed, a third-party library with the same name cannot be published within 24 hours.
-   If a specific version has been removed, this version number cannot be used again. A new version number is required for subsequent publishment.
-   If the third-party library is depended on by other third-party libraries, do not delete it, but label it with **deprecated**. If the third-party library is not depended on, just delete it.

#### Options

## force

-   Default value: false
-   Value type: boolean
-   Alias: f

This parameter is used to forcibly unpublish a third-party library.

## publish\_registry

-   Default value: ""
-   Type: URL

You can configure the **\--publish\_registry <r>** parameter at the end of the **ohpm unpublish** command to specify a repository address for unpublishment. If this parameter is not specified, the repository address is obtained from the configuration by default.

## publish\_id

-   Default value: ""
-   Value type: string

This parameter is used to specify the publish code.

## key\_path

-   Default value: ""
-   Value type: string

You can configure the **\--key\_path <p>** parameter at the end of the **ohpm unpublish** command to specify the SSH private key path.

## fetch\_timeout

-   Default value: 60000
-   Type: number
-   Alias: ft

You can configure the **\--ft** or **\--fetch\_timeout <number>** parameter at the end of the **ohpm unpublish** command to set the operation timeout period. If the parameter is not specified, the default timeout period is 60000 ms.

## strict\_ssl

-   Default value: true
-   Value type: boolean

You can configure **\--strict\_ssl true** at the end of the **ohpm unpublish** command to enable HTTPS certificate verification or configure **\--strict\_ssl false** to disable it.

## log\_level

-   Default value: none
-   Value type: string

You can append the **\--log\_level <string>** parameter to the **ohpm unpublish** command to specify the log level (**info**, **debug**, **warn**, or **error**) for the execution of the current command. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## debug

-   Default value: false
-   Value type: boolean

You can append the **\--debug** parameter to the command to set the log level to **debug** for the execution of the current command. This configuration takes effect only on the current command line and does not alter the log level configured in the .ohpmrc file. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

#### Example

Run the following command to unpublish a third-party library:

ohpm unpublish demo@1.0.0 -f

Below is an output example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/TMH9JoYUS8WXWnLF_uX3eQ/en-us_image_0000002532750587.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B80D45614E7AD82E33124358B1FAF2B907F044DCF359E62773F0BAA5A7D9F750 "Click to enlarge")
