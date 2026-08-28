# ohpm version

Manages module versions.

Since ohpm 6.0.2.636, the **log\_level** and **debug** parameters can be appended to the command to obtain the log level and specify the log level for the current command execution.

#### Command Format

ohpm version \[options\] \[<newversion> | major | minor | patch\]

#### Description

Executed in the module directory, this command is used to obtain or upgrade a version number and write the data back to **oh-package.json5**.

#### Parameter Description

## None

If you run the **ohpm version** command without any parameter, the version number of the current module is displayed in the standard output.

## newversion

**newversion** is used to set the current module version to a valid semantic version, which is displayed in the standard output.

## major

When parameter **major** is used:

-   If there is no beta version number, the major version number will increase by 1 while minor and patch version numbers are 0.
-   If the beta version number exists:
    -   When both minor and patch version numbers are 0, the major version number remains unchanged and the beta version number is deleted. That is, 1.0.0-beta.1 is upgraded to 1.0.0.
    -   When either the minor or patch version is not 0, the major version number increases by 1, minor and patch version numbers are 0, and the beta version number is deleted. That is, 1.0.1-beta.1 is upgraded to 2.0.0.

## minor

When parameter **minor** is used, the major version number is fixed, and the minor and patch version numbers are changed according to the following rules:

-   If there is no beta version number, the minor version number will increase by 1 while the patch version number is 0.
-   If the beta version number exists:
    -   When the patch number is 0, the minor version number remains unchanged and the beta version number is deleted. That is, 1.1.0-beta.1 is upgraded to 1.1.0.
    -   When the patch number is not 0, the minor version number increases by 1, the patch version number is set to 0, and the beta version number is deleted. That is, 1.1.1-beta.1 is upgraded to 1.2.0.

## patch

When parameter **patch** is used, the major and minor version numbers are fixed, and the patch version number is changed according to the following rules:

-   If there is no beta version number, the patch version number increases by 1. That is, 1.0.0 is upgraded to 1.0.1.
-   If the beta version number exists, only the beta version number is deleted. That is, 1.0.0-beta.1 is upgraded to 1.0.0.

#### Options

## prefix

-   Default value: ""
-   Value type: string

You can configure the **\--prefix <string>** parameter at the end of the **ohpm version** command to specify the root directory of the package. The root directory must contain the **oh-package.json5** file.

## parameterFile

-   Default value: none
-   Value type: string
-   Alias: pf

You can configure the **\--pf <string>** or **\--parameterFile <string>** parameter at the end of the **ohpm version** command to specify the path of the parameterization configuration file. Before running this command, ensure that **parameterFile** is configured in the project-level **oh-package.json5** file.

## log\_level

-   Default value: none
-   Value type: string

You can append the **\--log\_level <string>** parameter to the **ohpm version** command to specify the log level (**info**, **debug**, **warn**, or **error**) for the execution of the current command. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## debug

-   Default value: false
-   Value type: boolean

You can append the **\--debug** parameter to the command to set the log level to **debug** for the execution of the current command. This configuration takes effect only on the current command line and does not alter the log level configured in the .ohpmrc file. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

#### Example

For the entry module, the version number is 1.0.0, run the following command in the root directory of the current module:

ohpm version

Below is an output example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/h4HbkUGHSnW_ATLThQmO5Q/en-us_image_0000002532670015.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D99EB9417A9F28A1D6F0F9A67AD36F925C0C6A2A78C182CD92617D6FEC305CE "Click to enlarge")

Run the following command:

ohpm version 1.0.1-beta.1

Below is an output example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/J6ggCnxFSeyNAX3u9Lpyhw/en-us_image_0000002532749965.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2EF60E3FD17004BCA2F5821ED3463E632A9B8A1D0134E94C8EA517F1375A604C "Click to enlarge")

Run the following command:

ohpm version major

Below is an output example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/H_WR8KRqQqOhTkzkc9nyYg/en-us_image_0000002532670017.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94C79E0AB56B030434A9781060A11332C42A4928AE17192278E1D897AC645A6C "Click to enlarge")
