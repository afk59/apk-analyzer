# ohpm prepublish

Prepublishes a third-party library.

Since ohpm 6.0.2.636, the **log\_level** and **debug** parameters can be appended to the command to obtain the log level and specify the log level for the current command execution.

#### Command Format

ohpm prepublish \[options\] <har\_or\_tgz\_file>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/2ImHGCPdQm2-vd_aUjc_-Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=97983D41D51120588D34E88D82F23108BF54C0A1F7C62E4379AAB687A7C2E332)

-   **har\_or\_tgz\_file**: path of the compressed package. The package can be a .har package or a .tgz package packed by the hsp module. This parameter is mandatory.
-   ohpm support the **prepublish** command since v1.8.0.

#### Description

-   The **prepublish** command is subject to all the rules that are applied to the **publish** command, ensuring a thorough check of the content to be published.
-   Only the content of the third-party libraries to be published is checked. **publish\_registry**, **publish\_id**, and **key\_path** are not checked.
-   For details about the format, structure, and verification rules of the package, see [ohpm publish](../ohpm-publish/document.md).

#### Options

None.

## log\_level

-   Default value: none
-   Value type: string

You can append the **\--log\_level <string>** parameter to the **ohpm prepublish** command to specify the log level (**info**, **debug**, **warn**, or **error**) for the execution of the current command. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## debug

-   Default value: false
-   Value type: boolean

You can append the **\--debug** parameter to the command to set the log level to **debug** for the execution of the current command. This configuration takes effect only on the current command line and does not alter the log level configured in the .ohpmrc file. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

#### Example

Run the following command to prepublish a third-party library in the working directory:

ohpm prepublish publish\_test.har

Below is an output example:

C:\\Program Files\\Huawei\\DevEco Studio\\tools\\ohpm\\bin> ohpm prepublish D:\\publish\_test.har
prepublish publish\_test 1.0.0 succeed.
