# ohpm cache clean

Cleans the ohpm cache.

Since ohpm 6.0.2.636, the **log\_level** and **debug** parameters can be appended to the command to obtain the log level and specify the log level for the current command execution.

#### Command Format

ohpm cache clean \[options\]

#### Description

This command is used to clean the ohpm cache.

#### Options

## log\_level

-   Default value: none
-   Value type: string

You can append the **\--log\_level <string>** parameter to the command to specify the log level (**info**, **debug**, **warn**, or **error**) for the execution of the current command. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## debug

-   Default value: false
-   Value type: boolean

You can append the **\--debug** parameter to the command to set the log level to **debug** for the execution of the current command. This configuration takes effect only on the current command line and does not alter the log level configured in the .ohpmrc file. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

#### Example

Run the following command to clean the ohpm cache:

ohpm cache clean

Below is an output example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/sWIWE-UPTvWcKcKZ6dgNIw/en-us_image_0000002500910284.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22505E3C6CAD908B85A59D3A8CF399339B9EEFB7A28A37868A0155A59E3F20E3)

## Description of Cache Design

The ohpm stores the cache data in the **content-v1** folder of the configured cache directory. The folder stores all the HAR package data obtained through HTTP requests. The package path is constructed by splitting the package's SHA-512 hash into three segments: the first two characters form the level-1 directory, the next two characters form the level-2 directory, and all remaining characters (from the fifth character to the end) are used as the file name. Hash values are used to evenly distribute files in each directory. The three-layer directory structure prevents a directory from containing too many files and improves file indexing efficiency.

## Configuration

For details about how to configure the cache, see [ohpmrc](../../ohpmrc/document.md).
