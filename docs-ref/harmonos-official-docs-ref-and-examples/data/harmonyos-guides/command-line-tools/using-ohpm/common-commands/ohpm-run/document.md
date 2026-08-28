# ohpm run

Runs a user-defined script.

Since ohpm 6.0.2.636, the **log\_level** and **debug** parameters can be appended to the command to obtain the log level and specify the log level for the current command execution.

#### Command Format

ohpm run \[options\] <script\_name> \[-- <args...>\]

#### Description

-   This command is used to run the scripts defined in the **scripts** object in the **oh-package.json5** file of the module.
    
    In the **scripts** object you can configure multiple scripts to run, each of which is in the form of "key": "value". In the following example, **scriptName1**, **scriptName2**, and **scriptName3** are script aliases, followed by a colon and the corresponding script content, such as **"echo hello"**.
    
    The following is an example of **scripts** configuration in **oh-package.json5**:
    
    {               
      "scripts": {
        "scriptName1": "echo hello",
        "scriptName2": "ohpm run scriptName1",
        // After the identifier (--), the parameter key can be specified in the form of -p or --p, and the parameter value can be connected via a space ( ) or an equals sign (=).
        "scriptName3": "node test.js -- -paramKey1 paramValue1 -paramKey2=paramValue2 --paramKey3 paramValue3"
      }
    }
    
-   In script content, you can use **ohpm run** to reference other script aliases in the same **oh-package.json5** file, for example, **scriptName2**. The **ohpm run** reference relationship is a directed acyclic graph (DAG) and does not support recursive or circular reference.
-   Executing **ohpm run** will report an error if any issue occurs during parsing of script content. For example, it will report an error if the script content references a script alias that does not exist in the same **oh-package.json5** file, or if a loop exists in the script alias reference relationship.

## Transferring Parameters

-   You can use **\--** in the **ohpm run** command to overwrite the parameters of the referenced script or pass in additional parameters to the referenced script.
    
    ohpm run scriptName3 -- -paramKey1 newValue -paramKey4 paramValue4
    
    The preceding command replaces the **paramKey1** parameter in the **scriptName3** script with **newValue** and adds the **paramKey4** parameter.
    
-   If the script content is **ohpm run _scriptName_** and **\--** is used, the script content pertaining to _scriptName_ cannot contain **"ohpm run"**, so as to avoid nested references.

## Supporting Multiple Commands

Two types of command connectors are supported: && and ||. (&& and || are not prioritized. Commands are executed from left to right. Parentheses cannot be used to change the priority of each subcommand.) For details, see [Example](#section157898418348).

## Constraints

| 
Item

 | 

Description

 |
| :-- | :-- |
| 

Constraint on scriptKey naming

 | 

A valid **scriptKey** name can contain uppercase and lowercase letters, digits, ASCII colons (:), ASCII underscores (\_), and ASCII hyphens (-), and must start with a lowercase letter.

 |
| 

Constraint on scriptContent

 | 

A valid **scriptContent** cannot reference any ohpm commands except **ohpm run**.

 |
| 

Constraint on using **ohpm run** in **scriptContent**

 | 

1\. Aliases of other scripts on which **ohpm run** depends must exist in the same **oh-package.json5** file.

2\. The reference relationship of **ohpm run** is a DAG and does not support recursive or circular reference.

 |

#### Options

## prefix

You can use **\--prefix** to specify the root directory of the package. The root directory must contain the **oh-package.json5** file. The script alias in the dependency package cannot be invoked by running the following command:

ohpm run --prefix <path> <script alias >

## log\_level

-   Default value: none
-   Value type: string

You can append the **\--log\_level <string>** parameter to the command to specify the log level (**info**, **debug**, **warn**, or **error**) for the execution of the current command. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## debug

-   Default value: false
-   Value type: boolean

You can append the **\--debug** parameter to the command to set the log level to **debug** for the execution of the current command. This configuration takes effect only on the current command line and does not alter the log level configured in the .ohpmrc file. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

#### Example

The **scripts** configurations in the sample code are all from the **oh-package.json5** file:

{
  "name": "example",
  "version": "1.0.0",
  "description": "this is an example for ohpm run.",
  "main": "./src/index.ets",
  "author": "oh",
  "license": "ISC",
  "scripts": {
    "testLogic": "ohpm run testFail || ohpm run testSuc && ohpm run testSuc",
    "testFail": "test1",
    "testSuc": "echo hello"
  }
  ...
}

## Example of Parameter Transfer

ohpm run script\_name -- -arg1=1 --arg2=2 -arg3 3 --arg4 4

Execute the **script\_name** script and set the values of **arg1**, **arg2**, **arg3**, and **arg4** to **1**, **2**, **3**, and **4**, respectively. In the preceding code, all the four forms are valid and equivalent in effect.

## Success Example

Run the following command to execute the **testSuc** script:

ohpm run testSuc

The execution result is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/Th9wZrHgTrKtarrvdhYk3Q/en-us_image_0000002532750127.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0CA942803985D7E64433020E0525C234D8494229AD27621513B745C89EED6812 "Click to enlarge")

## Failure Example

Run the following command to execute the **testFail** script:

ohpm run testFail

The execution result is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/ykh2Tl-1Qu-KcRmbo19NTQ/en-us_image_0000002501070100.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A7759993C0D4BF4574DCD1542BBD7BAC8F9BF021D0E5951B6366026749F9D803 "Click to enlarge")

## Example of Using Logical Operators (&& and ||)

Run the following command to execute the **testLogic** script:

ohpm run testLogic

The execution result is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/sn_x1KTERr2zs0UCJvjyXg/en-us_image_0000002532670179.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC2244EBEC8F1AA03AB69CD3D1B7EC97F42990E88AE5679DC37F2C5F12F1C532 "Click to enlarge")
