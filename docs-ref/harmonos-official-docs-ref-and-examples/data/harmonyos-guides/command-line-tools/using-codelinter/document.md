# Using codelinter

codelinter is used to check and repair code using commands. It can be integrated into the gated check-in or continuous integration environment.

The codelinter command format is as follows:

codelinter \[options\] \[dir\] 

**options**: optional parameters. See [Table 1](#table25697717185).

**dir**: root directory of the project to be checked. This parameter is optional. If this parameter is not specified, the current context directory is used by default.

**Table 1** options configuration
| 
Option

 | 

Description

 |
| :-- | :-- |
| 

\--config/-c _<filepath>_

 | 

Specifies a rule configuration file for codelinter check. _<filepath>_ specifies the save path of the rule configuration file.

 |
| 

\--fix

 | 

Specifies whether to execute QuickFix together with codelinter check.

 |
| 

\--format/-f

 | 

Specifies an output format of the check result. Currently, the default, JSON, XML, and HTML formats are supported. If this parameter is not specified, the default format (text format) is used by default.

 |
| 

\--output/-o _<filepath>_

 | 

Specifies a path for saving the check result and prevents the check result from being displayed in the command line tool. _<filepath>_ specifies the path for saving the code check result. The value can be a relative path or an absolute path. If **\--output** is not used, the check result is displayed in the CLI by default.

 |
| 

\--version/-v

 | 

Displays the codelinter version.

 |
| 

\--product/-p _<productName>_

 | 

Specifies a product for which codelinter check takes effect. _<productName>_ indicates the name of the effective product.

 |
| 

\--incremental/-i

 | 

Checks the incremental files in the Git project (which includes newly added, modified, and renamed files).

 |
| 

\--help/-h

 | 

Displays help information about the codelinter command.

 |
| 

\--exit-on/-e <levels>

 | 

Specifies the alarm severities at which a non-zero exit code needs to be returned. The alarm severities include **error**, **warn**, and **suggestion**. To specify multiple severities, separate them with commas (,).

The exit code is calculated as follows: A 3-bit binary number is used, where the bits (from the highest to the lowest) correspond to the error, warn, and suggestion severities, respectively. If the severity is configured in the command line and the code check result contains the severity, the binary value is 1. Otherwise, the binary value is 0. The exit code is the decimal equivalent of this binary number.

Examples:

-   If the command is configured with **\--exit-on error**, and the code check results include error, warn, and suggestion alarms: The binary number for the exit code is 100, and its decimal value is 4.
-   If the command is configured with **\--exit-on error**, and the code check results include warn and suggestion alarms: The binary number for the exit code is 000, and its decimal value is 0.

 |

1.  Execute codelinter code check and repair. If your project has multiple products, run the **\--product/-p** command to specify the product for which the code check takes effect and the root directory of the project to be checked.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/AFRSqdLiQzagZQXGzlny4Q/en-us_image_0000002501070348.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B55A16B033E4015E9E287158B0B34D4E27405D014322868D4C9211C946E5AD2)
    
    -   Use the command line tool in the root directory of the project.
        1.  Run the **codelinter** command In this case, the code of the TypeScript/ArkTS file in the project is checked according to the default codelinter check rule. After the check is complete, you can view the **code-linter.json5** file in the corresponding path as prompted.
            
            codelinter // Execute codelinter check.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/KjGsm1I1RFGS9qkaqUSZ0w/en-us_image_0000002500910510.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95C95FB219E0A7211B0335B9FB0A5AA8F1EA81FBBE377B4DE795821139A45C39 "Click to enlarge")
            
        2.  Specify the **code-linter.json5** rule configuration file to be used for code check:
            
            codelinter -c _filepath_ // Specify the path to the rule configuration file.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/rFIEAEc1Q3miVyDVlJTukw/en-us_image_0000002532750373.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0DE74E72CA5EA94A07C756C943CEBC68B73B6F909C60C5551EE2E962E7196478 "Click to enlarge")
            
        3.  Perform codelinter check for a specified project based on the specified rule configuration file. Some alarms that can be cleared are automatically fixed.
            
            _codelinter -c filepath_ --fix // Fix the alarms in the project.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/rqt07X_UTRyGsBIWRScK5A/en-us_image_0000002542181027.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E763B51C08F62BB7E54DB5F4252E424EFCFA6DB511DC2FC16037FD0DA3E8CEBB)
            
    -   Use the command line tool in a non-root directory of the project.
        1.  Run the following command to specify the project directory or file path to be checked. In this case, the code of the TypeScript/ArkTS file in the project is checked according to the default check rules. After the check is complete, you can review the rules in the **code-linter.json5** file indicated in the check result.
            
            codelinter dir \[filepath\] \[dir1\] // Specify the project directory or file path to be checked. filepath indicates the file path, and dir and dir1 indicate the project directories. Multiple directories and file paths are allowed.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/XxtUTZMpQmiAH1yZ804-Fw/en-us_image_0000002500910512.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=47B074D03C2EA5F97C1220F5A1E5011E8AB2E4DF282F0B91389BAD8683599C3F "Click to enlarge")
            
        2.  Specify the codelinter rule configuration file.
            
            codelinter -c _filepath_ dir // filepath indicates the save path of the specified rule configuration file, and \[dir\] indicates the root directory of the project to be checked.
            
        3.  Perform codelinter check for the specified project based on the specified rule configuration file and fix issues that can be auto-fixed.
            
            _codelinter -c filepath dir_ --fix // Fix the alarms in the project. Multiple project paths are allowed.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/DNCCZDntRhSClC4yXUDcBw/en-us_image_0000002532750377.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD8052BF602FF45A90022C57110F3EA4AEEC448B743C70587472937D5CA4AD5F "Click to enlarge")
            
    
2.  Run the following command to specify the output format (for example, JSON) of the check result. The check result is displayed in the CLI.
    
    codelinter \[dir\] -f json // \[dir\] is the root directory of the project to be checked.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/MKRbP9JVT-KCBJEMk0r1vQ/en-us_image_0000002500910516.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40AC3BD5E853BAD452C29EFEAF41079C0426CFD6417862ABA180BC704F05BDC2)
    
3.  Run the following command to specify the code check output format and its save path. In this case, the check result is not displayed in the CLI. You can view the check result in the specified path.
    
    codelinter \[dir\] -f json -o _filepath_2     // \[dir\] indicates the root directory of the project to be checked, and filepath2 indicates the path for storing the code check result.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/sJ5GAogrRYWww59-fbLICA/en-us_image_0000002501070360.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67929AB87C00201AC6590AAEBE8D43011973C1C76785821A52F445F3BCAA49AB)
