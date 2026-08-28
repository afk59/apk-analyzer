# ohpm init

Creates an **oh-package.json5** file.

Since ohpm 6.0.2.636, the **log\_level** and **debug** parameters can be appended to the command to obtain the log level and specify the log level for the current command execution.

#### Command Format

ohpm init \[options\]

#### Description

This command is used to create an **oh-package.json5** file and initialize a package in the working directory.

During the command execution, an interaction interface is displayed for you to input basic information about the third-party library, such as the library name and version. ohpm creates an **oh-package.json5** file in the working directory based on existing fields, dependencies, and selected options. The set fields and values will all be retained.

#### Options

## yes

-   Default value: null
-   Type: null or Boolean
-   Alias: y

Besides creating the default **oh-package.json5** file, you can configure the **\-y** or **\--yes** parameter at the end of the **ohpm init** command to skip the interaction interface.

The default content is as follows:

{
    "name": "work\_dir",
    "version": "1.0.0",
    "description": "",
    "main": "Index.ets",
    "author": "",
    "license": "ISC",
    "dependencies": {}
  }

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/aJE91cfpQd-gx3eLBZbVow/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BDD56DE3FCF728ECA05578D77ADF38D4B9F607995DFEBA057E0909BA474D78C)

If there is no existing **oh-package.json5** file in the current working directory, the **name** field in the new file is the name of the current working directory by default. If there is already an **oh-package.json5** file, the new file overwrites the existing one, with the **name** field set to the same value as that in the existing file.

## group

-   Default value: namespace of the current project or ""
-   Value type: string
-   Alias: g

You can append the **\-g <group\_name>** or **\--group <group\_name>** parameter to the **ohpm init** command to create an **oh-package.json5** file. The namespace of the **name** field is **@group\_name**.

## log\_level

-   Default value: none
-   Value type: string

You can append the **\--log\_level <string>** parameter to the **ohpm init** command to specify the log level (**info**, **debug**, **warn**, or **error**) for the execution of the current command. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## debug

-   Default value: false
-   Value type: boolean

You can append the **\--debug** parameter to the command to set the log level to **debug** for the execution of the current command. This configuration takes effect only on the current command line and does not alter the log level configured in the .ohpmrc file. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

#### Example

-   The **oh-package.json5** file does not exist in the current working directory.
    
    In **D:\\demo**, run the following command:
    
    ohpm init -y
    
    The command output is as follows:
    
    Wrote to D:\\demo\\oh-package.json5:
    
    {
        "name": "demo",
        "version": "1.0.0",
        "description": "",
        "main": "Index.ets",
        "author": "",
        "license": "ISC",
        "dependencies": {}
    }
    
-   The **oh-package.json5** file with the **name** field set to **demo\_name** already exists in the current working directory.
    
    In **D:\\demo**, run the following command:
    
    ohpm init -y
    
    The command output is as follows:
    
    Wrote to D:\\demo\\oh-package.json5:
    
    {
        "name": "demo\_name",
        "version": "1.0.0",
        "description": "",
        "main": "Index.ets",
        "author": "",
        "license": "ISC",
        "dependencies": {}
    }
    
-   Create an **oh-package.json5** file in which the **name** field is set to **@group\_name/demo** instead of **demo**.
    
    ohpm init -g group\_name
    
    The command output is as follows. The **name** field in the example is automatically displayed as **@group\_name/demo**.
    
    package name: (@group\_name/demo)
