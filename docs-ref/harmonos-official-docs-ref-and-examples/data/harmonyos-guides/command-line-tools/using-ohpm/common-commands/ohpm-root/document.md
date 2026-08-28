# ohpm root

Prints valid path information of the **oh\_modules** directory in the standard output.

Since ohpm 6.0.2.636, the **log\_level** and **debug** parameters can be appended to the command to obtain the log level and specify the log level for the current command execution.

#### Command Format

ohpm root

#### Description

Executed in any subdirectory of the module, this command is used to print the valid **oh\_modules** directory path information of the package in the working path of the command.

#### Options

## prefix

-   Default value: ""
-   Value type: string

You can configure the **\--prefix <string>** parameter at the end of the **ohpm root** command to specify the root directory of the package. The root directory must contain the **oh-package.json5** file. The valid **oh\_modules** directory path information in the root directory will be printed.

## log\_level

-   Default value: none
-   Value type: string

You can append the **\--log\_level <string>** parameter to the **ohpm root** command to specify the log level (**info**, **debug**, **warn**, or **error**) for the execution of the current command. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## debug

-   Default value: false
-   Value type: boolean

You can append the **\--debug** parameter to the command to set the log level to **debug** for the execution of the current command. This configuration takes effect only on the current command line and does not alter the log level configured in the .ohpmrc file. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

#### Example

Below is the directory structure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/0txmZXSTRhuxVoTcWQdzhA/en-us_image_0000002532669797.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FA48DFCE7A52269EDDDAC67F26E8A6091D91E8553613499346087E35D25AB3A)

Run the following command in the **src** directory of **entry**:

ohpm root

Below is an output example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/ff4V5iDuQJuoKqojnM0vrQ/en-us_image_0000002501069734.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00F6723CC58A0D7F6DFEED66F6C40FB5B50168643978B5E2AC428A4D593F6263)
