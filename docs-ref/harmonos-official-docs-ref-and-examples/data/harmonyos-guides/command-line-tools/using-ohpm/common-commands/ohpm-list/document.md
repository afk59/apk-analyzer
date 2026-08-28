# ohpm list

Lists the installed third-party libraries.

Since ohpm 6.0.2.636, the **log\_level** and **debug** parameters can be appended to the command to obtain the log level and specify the log level for the current command execution.

#### Command Format

ohpm list \[options\] \[\[<@group>/\]<pkg>\[@<version>\]\]
alias: ls

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/yyoNG-h2Qpuofk_g3C7rIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=958408D1482390229A523E23B3B086AE0FD2447403741E60B719CEF1C171B7C2)

-   **@group**: namespace of the third-party library. This parameter is optional.
-   **pkg**: name of the third-party library. This parameter is optional.
-   **version**: version number of the third-party library. This parameter is optional.

#### Description

This command is used to list information about all installed third-party libraries of the current project and their dependencies in a tree structure.

If the name of a third-party library is specified, its parent dependencies are all listed. If no name is specified, only direct dependencies are listed by default. You can add the **depth** option to specify the depth of dependencies to print.

#### Options

## depth

-   Default value: 0
-   Type: number
-   Alias: d

You can configure the **\-d <number>** or **\--depth <number>** parameter at the end of the **ohpm list** command to set the maximum depth of the output tree structure. If the depth exceeds the maximum, no data is output. If this parameter is not configured, the default value 0 is used, that is, only direct dependencies are displayed.

Since the DevEco Studio console only displays up to 5000 lines by default, for large projects, use the **ohpm list -d <number> > fileName.txt** command to redirect the output to a specified file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/v1ZCD2TMTl-Uau1J0LAW_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E6D485C8D8C254F2894C5151570AB74EDADAF56BA988A60628925A4279A7454)

If garbled characters appear in the output, run the **powershell -Command "(Get-Content 'fileName.txt') -replace (\[char\]27 + '\\\[\[0-9;\]\*m'), ''" > result.txt** command to export the content to the **result.txt** file.

## json

-   Default value: none
-   Alias: j

You can configure the **\-j** or **\--json** parameter at the end of the **ohpm list** command to output information about all third-party libraries installed in the current project and their dependencies in JSON format.

## prefix

-   Default value: ""
-   Value type: string

You can configure the **\--prefix <string>** parameter at the end of the **ohpm list** command to specify the root directory of the package. The root directory must contain the **oh-package.json5** file.

## parameterFile

-   Default value: none
-   Value type: string
-   Alias: pf

You can configure the **\--pf <string>** or **\--parameterFile <string>** parameter at the end of the **ohpm list** command to specify the path of the parameterization configuration file. Before running this command, ensure that **parameterFile** is configured in the project-level **oh-package.json5** file.

## recursive

-   Default value: none
-   Alias: r

Since OHPM 5.2.0, you can configure the **\-r** or **\--recursive** parameter at the end of the **ohpm list** command to print information about third-party libraries installed in all project modules, as well as their dependencies.

## target\_path

-   Default value: none
-   Value type: string

You can configure the **\--target\_path <string>** parameter at the end of the **ohpm list** command to specify the path of the dependency configuration file (**oh-package.json5**) of each module in the context of a specific target product. When you run the **ohpm list** command, ohpm installs the dependency in the **<_target\_path_\>/<_moduleName_\>/oh-package.json5** file first. For details, see [target\_path](../ohpm-install/document.md#section79331822125611).

## log\_level

-   Default value: none
-   Value type: string

You can append the **\--log\_level <string>** parameter to the **ohpm list** command to specify the log level (**info**, **debug**, **warn**, or **error**) for the execution of the current command. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## debug

-   Default value: false
-   Value type: boolean

You can append the **\--debug** parameter to the command to set the log level to **debug** for the execution of the current command. This configuration takes effect only on the current command line and does not alter the log level configured in the .ohpmrc file. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

#### Example

-   View all third-party libraries installed in the current project and their dependencies.
    
    Run the following command:
    
    ohpm list
    
    Below is an output example:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/wvGvqFXdQf2cjKntSuSq_Q/en-us_image_0000002501070284.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A01F4AE52BB677BE9B45C4136F5700DDEDDA8446D1DAC954DFFDEE10B123C32E "Click to enlarge")
    
-   View the dependencies of a third-party library installed in the current project.
    
    Run the following command:
    
    ohpm list universalify
    
    Below is an output example:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/EKLob6mnSZ-7FC40YcU1Zg/en-us_image_0000002501070286.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4642DF97E6ABCC3A32C5855701C2C1F3A7B1D5028DB4464E0808CD7F5B172479)
    
-   View all third-party libraries installed in the project modules and their dependencies.
    
    Run the following command:
    
    ohpm list -r
    
    Below is an output example:
    
    . D:\\xxx\\ProjectName
    └── @ohos/hypium 1.0.6
    
    module1 D:\\xxx\\ProjectName\\module1
    ├─┬ lib1 1.0.0
    │ ├── lib1\_sub1 1.0.0
    │ └── lib1\_sub2 1.0.0
    └─┬ lib2 1.0.0
      ├── lib2\_sub1 1.0.0
      └── lib2\_sub2 1.0.0
    
    module2 D:\\xxx\\ProjectName\\module2
    └── @ohos/lib3 1.0.0
    

-   When **target\_path** is specified, view all third-party libraries installed in the project modules and their dependencies.
    
    If the module **dynamic** is added to the **target\_path** directory and **module1** has a new dependency **lib3**, run the following command:
    
    ohpm list -r --target\_path xxx/.hvigor/dependencyMap
    
    Below is an output example:
    
    . D:\\xxx\\ProjectName
    └── @ohos/hypium 1.0.6
    
    dynamic D:\\xxx\\ProjectName1\\dynamic // Import the module using target\_path.
    └── @ohos/lib4 1.0.0
    
    module1 D:\\xxx\\ProjectName\\module1
    ├─┬ lib1 1.0.0
    │ ├── lib1\_sub1 1.0.0
    │ └── lib1\_sub2 1.0.0
    └─┬ lib2 1.0.0
      ├── lib2\_sub1 1.0.0
      └── lib2\_sub2 1.0.0
    └── lib3 1.0.0 // New dependency of target\_path.
    
    module2 D:\\xxx\\ProjectName\\module2
    └── @ohos/lib3 1.0.0
