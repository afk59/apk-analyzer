# ohpm info

Queries details of a third-party library.

Since ohpm 6.21.0, you can view the attributes of metadata in a third-party library via **field**, including **keywords**, **dependencies**, **tags**, **versions**, **license**, **author**, **repository**, **dist**, and **latest**. For details, see [Field](#section1068917464119).

Since ohpm 6.0.2.636, the **log\_level** and **debug** parameters can be appended to the command to obtain the log level and specify the log level for the current command execution.

#### Command Format

ohpm info \[options\] \[<@group>/\]<pkg>\[@<version> | @tag:<tag>\] \[field\]

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/2numhBWJT4alRTnCk50mLA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F4B076326AB1A8F49F47209B7F8612C441E79388B4505EDAC395090AAB3F0C7)

-   **@group**: namespace of the third-party library. This parameter is optional.
-   **pkg**: name of the third-party library. This parameter is mandatory.
-   **version**: version number of the third-party library. This parameter is optional.
-   **tag**: tag of the third-party library, marking a specific version number. This parameter is optional.

#### Description

This command is used to display details of a specified package and output the result in standard mode by calling a cloud query API.

#### Options

## registry

-   Default value: ""
-   Value type: URL

You can configure the **\--registry <registry>** parameter at the end of the **ohpm info** command to specify a repository address. If the repository address is not specified, the repository address is obtained from the configuration by default.

## fetch\_timeout

-   Default value: 60000
-   Value type: number
-   Alias: ft

You can configure the **\--ft <number>** or **\--fetch\_timeout <number>** parameter at the end of the **ohpm info** command to set the operation timeout period. If the parameter is not specified, the default timeout period is 60000 ms.

## strict\_ssl

-   Default value: true
-   Value type: boolean

You can configure **\--strict\_ssl true** at the end of the **ohpm info** command to verify the HTTPS certificate or configure **\--strict\_ssl false** to not verify the HTTPS certificate.

## pageNum

-   Default value: 1
-   Value type: number

This parameter takes effect when **field** is set to **versions**. You can configure the **\--pageNum <number>** parameter after **field**. The value ranges from 1 to 10000. It indicates the target page number when versions are displayed as a paginated list, and can be used together with **pageSize**.

## pageSize

-   Default value: 100
-   Value type: number

This parameter takes effect when **field** is set to **versions**. You can configure the **\--pageSize <number>** parameter after **field**. The value ranges from 1 to 500. It indicates the number of versions displayed per page when versions are presented as a paginated list, and can be used together with **pageNum**.

## log\_level

-   Default value: none
-   Value type: string

You can append the **\--log\_level <string>** parameter to the **ohpm info** command to specify the log level (**info**, **debug**, **warn**, or **error**) for the execution of the current command. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## debug

-   Default value: false
-   Value type: boolean

You can append the **\--debug** parameter to the command to set the log level to **debug** for the execution of the current command. This configuration takes effect only on the current command line and does not alter the log level configured in the .ohpmrc file. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/VYrj675hTu2FSlM0KzoMJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=98A345C3B7EACEBC48A84F45CF1A97F27798DF89FB187AD5BBD9A2B91667A104)

**registry**, **fetch\_timeout**, and **strict\_ssl** configurations apply only to the current **ohpm info** command and do not alter any project-level or user-level configuration files.

#### Field

-   **keywords**: queries the keywords of the third-party library.
-   **dependencies**: queries the sub-dependency configuration of the third-party library.
-   **tags**: queries the tag list of the third-party library.
-   **versions**: queries the version list of the third-party library. Query results are sorted by release time in ascending order and presented in paginated lists. You can set the page number and number of items per page via [pageNum](#section12987141924519) and [pageSize](#section7425335114510) in **Options**. The command is configured as **versions --pageNum _<number>_ --pageSize _<number>_**.
-   **license**: queries the license of the third-party library.
-   **author**: queries the author information of the third-party library, including the **name**, **email**, and **url** fields.
-   **repository**: queries the source code address of the third-party library.
-   **dist**: queries the integrity string of the third-party library and the download address of its .har or .tgz package.
-   **latest**: queries the latest released version of the third-party library.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/OGnzdd8ISVmwbYan83TeAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA6DD48FDCFB527BC1F786313334E7EFEAAE662A890EA7FEEC4CF5298913BD47)

-   **tags**: displays all tags of the third-party library. It does not support filtering by appending a specific version or tag with @ after the dependency name. For example, running **ohpm info @ohos/lottie tags** yields the same result as running **ohpm info @ohos/lottie@latest tags** or **ohpm info @ohos/lottie@1.0.0 tags**.
-   **versions**: displays all versions of the third-party library in a paginated list. It does not support filtering by appending a specific version or tag with @ after the dependency name.

#### Examples

## Example 1

Command:

ohpm info @ohos/lottie --registry https://ohpm.openharmony.cn/ohpm

Output:

➜ ohpm info @ohos/lottie --registry https://ohpm.openharmony.cn/ohpm

@ohos/lottie@2.0.10-rc.1 | MIT | deps: none | versions: 15
lottie is an animation library for OpenHarmony, designed to work with animations exported from Adobe After Effects in JSON format through the use of Bodymovin.

keywords: OpenHarmony, HarmonyOS, Lottie

dist
.tarball: https://repo.harmonyos.com/ohpm/@ohos/lottie/-/lottie-2.0.10-rc.1.har
.integrity: sha512-fjdc1qJeEax+4/wA1eHdjvtLBOFxRGeU4J2F9Q1b+yRYjmZnzL6GCA241Ku5iyzG5j2RUZi6tyBa0rpyQnjhPg==

dist-tags:
latest: 2.0.10-rc.1

published 15 hours ago by ohos\_tpc

## Example 2

Command:

ohpm info @ohos/imageknife --registry https://ohpm.openharmony.cn/ohpm/ keywords

Output:

OpenHarmony, ImageKnife, glide, HarmonyOS

## Example 3

Command:

ohpm info @ohos/lottie --registry https://ohpm.openharmony.cn/ohpm versions --pageNum 1 --pageSize 500

Output:

current page num: 1, total pages: 88
2.0.0        2.0.1        2.0.10       2.0.10-rc.0  2.0.10-rc.1  2.0.10-rc.2  2.0.10-rc.3  2.0.10-rc.4  2.0.11       
2.0.11-rc.0  2.0.11-rc.1  2.0.11-rc.2  2.0.11-rc.3  2.0.11-rc.4  2.0.11-rc.5  2.0.11-rc.6  2.0.11-rc.7  ......
