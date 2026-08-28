# ohpm dist-tags

A tag can be used to identify a specific version of a third-party library. When using the **ohpm install** command, you can use a tag in place of a version number to install a package.

Since ohpm 6.0.2.636, the **log\_level** and **debug** parameters can be appended to the command to obtain the log level and specify the log level for the current command execution.

#### Command Format

ohpm dist-tags \[subcommand\] \[<@group>/\]<pkg>\[@<version>\] <tag>
alias: dist-tags

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/_6mjkrh3SsqyElzPm6PziQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE1853EC84CDBF30F7BDD0E7E36FDE309FA7EA4794E4E358C59BF11EE0892E79)

-   **subcommand**: subcommand, which can be **list**, **add**, **update**, or **remove**.
-   **@group**: namespace of the third-party library. This parameter is optional.
-   **pkg**: name of the third-party library. This parameter is mandatory.
-   **version**: version number of the third-party library. This parameter is mandatory for the **add** and **update** subcommands.
-   **tag**: tag. This parameter is mandatory for the **add**, **update**, and **remove** subcommands. A tag must start with an uppercase letter, lowercase letter, or digit and can contain a maximum of 60 characters, including uppercase letters, lowercase letters, digits, dots (.), underscores (\_), and hyphens (-).

#### Description

Operates a tag. You can view all tags of a third-party library, add a tag to a specific version, modify a tag to point to another version, and delete a tag.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/s4RVPkQnT9uXQfcrCVZ0Dg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5D4893E1B6EE7E9D3F29F7D68D8D67B5258EAA0F7E64F1859D87697FA626FB4)

The **latest** tag is a special predefined tag that cannot be modified directly using **dist-tags** commands. It automatically points to the highest official release version. If there are no official versions, it defaults to the highest beta version.

For example, for a third-party library with versions 1.0.1-beta, 1.0.1, and 2.0.1-beta, the **latest** tag automatically points to 1.0.1 because it is the highest official release version.beta version.

#### Subcommands

## list

ohpm dist-tags list \[<@group>/\]<pkg>
alias: ls

Lists all tags of the specified third-party library. In the command output, the **latest** tag is listed first, and other tags are listed in alphabetical order.

## add

ohpm dist-tags add \[<@group>/\]<pkg>\[@<version>\] <tag>

Adds a tag to point to a specific version of the specified third-party library. If a tag with the same name already exists, the addition operation will fail.

## update

ohpm dist-tags update \[<@group>/\]<pkg>\[@<version>\] <tag>
alias: up

Updates a tag to point to another version of the specified third-party library. If the specified tag does not exist, the update operation will fail.

## remove

ohpm dist-tags remove \[<@group>/\]<pkg> <tag>
alias: rm

Removes a tag of the specified third-party library. If the specified tag is not found, the deletion will fail.

#### Options

## publish\_id

-   Default value: ""
-   Value type: string

You can configure the **\--publish\_id <id>** parameter at the end of the **ohpm dist-tags** command to specify the publish code.

## key\_path

-   Default value: ""
-   Value type: string

You can configure the **\--key\_path <p>** parameter at the end of the **ohpm dist-tags** command to specify the SSH private key path.

## registry

-   Default value: none
-   Type: URL

You can configure the **\--registry <registry>** parameter at the end of the **ohpm dist-tags** command to specify a repository address. If the repository address is not specified, the repository address is obtained from the configuration by default.

## publish\_registry

-   Default value: ""
-   Type: URL

You can configure the **\--publish\_registry <r>** parameter at the end of the **ohpm dist-tags** command to specify a repository address for publishment. If this parameter is not specified, the repository address is obtained from the configuration by default.

## fetch\_timeout

-   Default value: 60000
-   Type: number
-   Alias: ft

You can configure the **\--ft <number>** or **\--fetch\_timeout <number>** parameter at the end of the **ohpm dist-tags** command to set the operation timeout period. If the parameter is not specified, the default timeout period is 60000 ms.

## strict\_ssl

-   Default value: true
-   Value type: boolean

You can configure **\--strict\_ssl true** at the end of the **ohpm dist-tags** command to enable HTTPS certificate verification or configure **\--strict\_ssl false** to disable it.

## log\_level

-   Default value: none
-   Value type: string

You can append the **\--log\_level <string>** parameter to the **ohpm dist-tags** command to specify the log level (**info**, **debug**, **warn**, or **error**) for the execution of the current command. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## debug

-   Default value: false
-   Value type: boolean

You can append the **\--debug** parameter to the command to set the log level to **debug** for the execution of the current command. This configuration takes effect only on the current command line and does not alter the log level configured in the .ohpmrc file. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

#### Example

To import the 1.0.0 version of the @ohos/axios package by using a tag in the **oh-package.json5** file, perform the following steps:

1\. Run the **add** subcommand of **ohpm dist-tags** to add the tag name **beta** to the 1.0.0 version of the @ohos/axios package.

ohpm dist-tags add @ohos/axios@1.0.0 beta

2\. In the **oh-package.json5** file, use the **beta** tag to import the 1.0.0 version of the @ohos/axios package.

{
  "dependencies": {
    // Import dependencies by tag. This example imports dependencies whose version tag is beta, corresponding to the 1.0.0 version.
    "@ohos/axios": "tag:beta"
  }
  ...
  ...
}
