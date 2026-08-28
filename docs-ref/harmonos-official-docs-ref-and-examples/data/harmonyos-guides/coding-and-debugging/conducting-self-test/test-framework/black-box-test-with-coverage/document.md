# Black-box Test with Coverage

DevEco Studio supports black-box testing with coverage, without the need to develop test cases. Simply push the instrumented HAP package to the device, simulate user operations on the app/atomic service, and generate a coverage report after the test is complete. Currently, only the stage model is supported.

#### Constraints

-   Prior to DevEco Studio 6.0.1 Beta1, code coverage testing was only supported for UIAbility.
-   Starting from DevEco Studio 6.0.1 Beta1, coverage data can be collected when the inherited ExtensionAbility contains either the **onDump** or **onDestroy** method. If neither method exists, code coverage testing cannot be performed.

#### Preparations

Connect the device to your PC and sign the app/atomic service. For details, see [Running Your App/Atomic Service on a Local Real Device](../../../running-your-app-on-a-local-real-device/document.md) and [Signing Your App/Service](../../../configuring-a-debug-signature/document.md).

#### Filtering Files for Coverage Test

If you want to test the coverage of only some files, create the **coverage-filter.json5** file in the project directory and configure the files or folders that are included or excluded in the coverage statistics in **coverage-filter.json5**. DevEco Studio filters files based on the configuration in **coverage-filter.json5** during compilation and instrumentation.

This feature is supported since DevEco Studio 5.1.0 Release.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/GwgB_s5GTjq1o3oP11G9KA/en-us_image_0000002500909960.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3996E43074F7062FBFDA0D1D404E8991C8C37B94975B128655ECFBEB98CCEA8D)

The **coverage-filter.json5** file contains the following parameters.

**Table 1**
| 
Name

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

include

 | 

No

 | 

String array

 | 

Path of the file or folder included in coverage statistics. Only the absolute path starting with the module name is supported. Wildcards are not supported. The priority of **include** is higher than that of **exclude**.

 |
| 

exclude

 | 

No

 | 

String array

 | 

Path of the file or folder excluded from coverage statistics. Only the absolute path starting with the module name is supported. Wildcards are not supported.

 |

Example:

{
  "include":\[    // Path of the file or folder included in coverage statistics. Only the absolute path starting with the module name is supported. Wildcards are not supported.
    "entry/src/main/ets/pages/aaa.ets"
  \],
  "exclude":\[    // Path of the file or folder excluded from coverage statistics. Only the absolute path starting with the module name is supported. Wildcards are not supported.
    "entry/src/main/ets/pages"
  \]
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/ljvLdnB_TqyjCLRsNs4KQQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07B3C6D749543BA5C6FEE9AE2ED533A387229B62EC6FAADD3C545CB5A91C4187)

After the configuration file is modified, incremental compilation is not triggered. You need to recompile the instrumentation and perform the test again.

#### Performing the Coverage Test

## Compilation and Installation

You can compile and install the app using DevEco Studio or the CLI by following the procedure:

-   **Method 1: using DevEco Studio, supported since DevEco Studio 6.0.2 Beta1**
    1.  Choose **Run** > **Edit Configurations** > **Diagnostics** from the menu bar, and select **Black Coverage** to enable black-box coverage testing.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/a5Sj71GAThes_8c7D7PCGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CE0037ADE57E52EEF4805AFD063F0A366446505430298E8C15E750DAC001E57)
        
        -   This configuration does not take effect in debugging scenarios, where the app runs without instrumentation.
        -   In attach debugging and wait-for-debugging scenarios, enabling this feature may result in inaccurate breakpoints. You are advised to disable it.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/FF3y_biuQnqTfiVALp2NQw/en-us_image_0000002500909958.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60F60E3907729EF37B2A0493EF174DB99BDCF6E5B13ED0404E2F6380E4278716)
        
    2.  Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/-hkh5beNRxSg-PirACBNZQ/en-us_image_0000002532749819.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=387ABF795B30506310F58025F6D6E5690C8550F394F8E744955F3E081A880B38) on the toolbar. DevEco Studio starts the instrumentation compilation process and pushes the package to the device for installation.
-   **Method 2: using the CLI**
    1.  Run the hvigor instrumentation compilation command. After the compilation, the **init\_coverage.json** file is generated in the **_{projectPath}_/_{moduleName}_/.test/default/intermediates/ohosTest** directory for generating a coverage report later.
        
        hvigorw --mode module -p module={moduleName@targetName} -p product={productName} -p buildMode=test -p ohos-test-coverage=true -p coverage-mode=black assembleHap --parallel --incremental --daemon
        
        -   **moduleName**: module on which the test is performed.
        -   **targetName**/**productName**: currently active target/product. To check the current target/product, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/y-gAlHqTTyWFWKsALosRXA/en-us_image_0000002500909962.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7251718F5FF45A314AF17DFB9BE9CF9DFB069555B07A28DE9DF0F1C50BB647D) in the upper-right corner of DevEco Studio.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/-hQomipyRQ20i5q4JnlMsQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=862A629EF8D621F0F27ABCA9442879633AE01D108B9895EB2DB17EC708952858)
        
        If the HAP depends on an HSP, compile the HSP separately by replacing **assembleHap** in the preceding command with **assembleHsp**.
        
    2.  Uninstall the app to be tested from the device. If the app is not installed on the device, skip this step. For details about how to use the hdc tool, see [hdc](../../../../system/debugging-tools/performance-analysis-kit/command-line-tools/hdc/document.md).
        
        hdc uninstall {bundleName}
        
        -   **bundleName**: name of the installed app package on the device.
    3.  Install the HAP generated after instrumentation and compilation on the device. If the HAP depends on an HSP, install the HSP as well.
        
        hdc install {SignedHapPath}
        
        -   **SignedHapPath**: path of the signed HAP package, which is located in the module's **build\\_{productName}_\\outputs\\_{targetName}_** directory by default.

## Performing the Test

Perform black-box testing by simulating user operations on the device. After the testing is complete, generate coverage data using either of the following methods:

-   For UIAbility (supported since DevEco Studio 5.1.0 Release) and ExtensionAbility with the **onDump** method (supported since DevEco Studio 6.0.1 Beta1), execute the following command:
    
    hdc shell aa dump -c -l
    
-   For UIAbility, exit the app to trigger the [onDestroy()](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/uiability-component/uiability-lifecycle/document.md#ondestroy) callback.
-   For ExtensionAbility with the **onDestroy** method, coverage data is generated when the ability is destroyed and its **onDestroy()** callback is triggered. This feature is supported since DevEco Studio 6.0.1 Beta1.
-   For UIAbility, use the [EventHub](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-eventhub) API to notify the UIAbility for coverage data generation. This feature is supported since DevEco Studio 6.0.2 Beta1.
    
    const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    context.eventHub.emit('coverage');
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/IPFPjgZkRGexXnE4s-K-qQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C87702D37BA7AA53FAC30E472D4252C8C4A7D3870DCF5720A58264957CF8343B)

Since API version 13, if the user closes an app by clearing all recent tasks, the **onDestroy()** callback will not be executed, which results in a failure to obtain coverage data.

## Generating the Coverage Report

1.  Run the following command to download the JSON files of coverage data. This command copies all files in the **cache** directory to the specified **_LocalPath_** directory.
    
    // For apps, LocalPath is optional. If it is not specified, files are stored in the directory where the command is executed by default.
    hdc file recv data/app/el2/100/base/{bundleName}/haps/{moduleName}/cache {LocalPath}
    // For atomic services, LocalPath is mandatory.
    hdc file recv -b {bundleName} ls ./data/storage/el2/base/haps/{moduleName}/cache {LocalPath}
    
    1.  **LocalPath**: local path for saving the downloaded files.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/MHsM45ovTqOj_E3oWagupQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB517D11E98DA26480E9C4C7B4D69D39D232A55392A15DBADE99E5D94F775E3D)
    
    In scenarios where modules interact with each other through navigation, you only need to obtain the coverage report file generated for the last module that is exited. However, in special cases where there is no navigation between modules, you must obtain the coverage report files generated for each module.
    
2.  Generate a coverage report file.
    
    hvigorw collectCoverage -p projectPath={projectPath} -p reportPath={reportPath} -p coverageFile={projectPath}/{moduleName}/.test/default/intermediates/ohosTest/init\_coverage.json#{LocalPath/bjc\_cov\_yyyyMMdd\_HHmmss\_SSS.json}
    
    1.  **projectPath**: project path.
    2.  **reportPath**: path for generating the coverage report file.
    3.  **bjc\_cov\_yyyyMMdd\_HHmmss\_SSS.json**: latest JSON file saved to the specified _**LocalPath**_ directory. The file name starts with **bjc\_cov**, and **_yyyyMMdd\_HHmmss\_SSS_** represents the timestamp (year, month, day, hour, minute, second, and millisecond) when the file is generated.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/rHNzBax5TiGmdPQtFHWaxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49A03B7857A887811447FD0DAD644A4D4A335B5429019004AAC06AAD57E99336)
    
    In scenarios where modules interact with each other through navigation, the **coverageFile** parameter is constructed by concatenating the paths to each module's **init\_coverage.json** file with the file name **_bjc\_cov\_yyyyMMdd\_HHmmss\_SSS_.json** using a number sign (#).
    
3.  Locate the report file on your local PC and open it in a web browser. For details about how coverage is calculated, see [Viewing Coverage Reports](#section10394362109).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/M6QQ9wRfSoWAy5rwZe2Hmg/en-us_image_0000002501069810.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=30A16B162B448B5E3A3C7BD06342E78E6A37B3644B24E6829B49072DE2BBA55B)
    

#### Viewing Coverage Reports

After the coverage test is complete, two reports are generated: an HTML report that provides a visual, browser-based UI for exploring coverage results, and a JSON report (**coverageReport.json**) containing the detailed coverage metrics. For details about the fields in the file, see [Interpreting the coverageReport.json File](#section175644610218).

## Interpreting the Coverage Report

The test coverage report provides insights across three key metrics:

-   Function coverage (**Functions**): checks whether every function within the codebase has been called at least once.
-   Branch coverage (**Branches**): checks whether all branches in the control flow have been traversed.

-   Line coverage (**Lines**): checks whether every line of executable code has been run.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/c6JiUGWHS0qk7R6oX_JvrQ/en-us_image_0000002532669873.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF28AF7BEBDA3F5695413EEE4B5FA0E13011ABA3CD95B97FAD3A4F0F6CAF6CCB)

The following is a breakdown of the specifics for the three metrics of coverage:

-   **Process Control**
    
    Common control flow statements include **if**, **while**, **do...while**, **switch**, **for**, and the ternary operator (**condition ? exprIfTrue : exprIfFalse**). You need to ensure that every boundary condition (that is, branch) of the control flow is executed.
    
-   **Lines of Source Code vs. Lines of Source Code**
    -   Line coverage refers to the lines of executable code, not all lines in the source file (including empty lines). Generally, each line containing a statement should be counted as an executable line.
    -   For DevEco Studio's coverage testing engine, only the statements in methods are counted. In a method:
        
        -   If a line contains executable code, it is counted as an executable line (+1).
        -   If a line consists solely of the punctuation mark **{**, it is counted as an executable line (+1).
        -   If a line contains only punctuation marks, such as **}**, **})** or **});**, it is classified as a non-executable line and is not counted (+0).
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/PmdZw-ISRfGxpUif22Fwlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F42460AB65C319286B257E8CB918662867A7634BD012267B48DAB129F9D3DB73)
        
        If an arrow function is defined inside a method, coverage is counted normally. If the arrow function is declared as a parameter, coverage for that line is not counted.
        
        Example:
        
        import { window } from '@kit.ArkUI';  // +0 (outside the method scope; not counted)
        let filePath :string;               // +0 (outside the method scope; not counted)
        const fileName = 'a.txt';          // +0 (outside the method scope; not counted)
         
        export function doTheThing ()  // +1
        {                              // +1
          let s1: string;              // +1
          const str = 'aaa';           // +1
          console.log(str);            // +1
        }                              // +0
         
        export class Person {         // +0 (outside the method scope; not counted)
          name: string = ''           // +0 (outside the method scope; not counted)
          constructor (n:string) {    // +1 (constructor)
            this.name = n;            // +1
          }                           // +0
         
          static sayHello () {        // +1 (static method of a class)
            console.log('hello');     // +1
          }                           // +0
         
          walk () {                   // +1 (instance method of a class)
            for (                     // +1              
              let i=0;                // +1
              i < 10;                 // +1
              i++)                    // +1
            {                         // +1
            }                         // +0
          }                           // +0
        }                             // +0
        
        function func ():object {    // +1
          return Object({        // +1 (statement split over multiple lines)
            a: 1,                // +1
            b: 2,                // +1
          })                     // +0
        }                        // +0
         
        func();                  // +0 (outside the method scope; not counted)
         
        function foo(n:number, m:number){}   // +1
        
        function bar():number {              // +1
          return 1;                          // +1
        }
        
        foo(1, bar());                       // +0 (outside the method scope; not counted)
        
-   Notations on the left side of coverage reports:
    -   Gray: The line is excluded from coverage statistics.
    -   Pink: The statement or function is not covered.
    -   Green: The statement or function is covered.
    -   **Nx**: The current executable line was executed N times.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/goL3PEeQRnaMCQMqwQN2hQ/en-us_image_0000002532749829.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=38BB950180432C1DF62AE57467D43E42E36AFAE993B2337275695F104A0756E3)
        
-   **Ignoring Specified Code Using Comment Syntax**
    
    There may be branches in the code that are difficult or even impossible to test. To exclude such code from being counted in the coverage, you can use the **instrument ignore** syntax.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/fIqluhWFTE6GPB9IlcTatQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2FCD3FA18CEA8E98EF33CB3D8EB3C6630EE7DDF1126A271912E9BF1B97D9528)
    
    To use this feature, first clear the cache by choosing **Build** > **Clean Project** from the menu bar.
    
    -   Ignoring an entire file: Add the comment **// instrument ignore file** or **/\* instrument ignore file \*/** in the source file. This way, the file will no longer be instrumented, and it will not appear in the coverage report.
    -   Ignoring code blocks, classes, or functions: Add **/\* instrument ignore next \*/** or **// instrument ignore next** before the code block to ignore it.
    -   Ignoring **if/else** branches: Add **// instrument ignore if** or **/\* instrument ignore if\*/** before the conditional expression to ignore the **if** branch, and **// instrument ignore else** or **/\* instrument ignore else\*/** to ignore the **else** branch.
    
    import {testA} from './Index'
    // instrument ignore file: Ignore the entire file.
    
    // instrument ignore next: Ignore the following code block.
    export function sum(a:number,b:number){
      return a+b;
    }
    sum(1,2);
     
    let a = 1;
    // instrument ignore else: Ignore the else branch.
    if (a!=1) {
      // do something
      console.log('BBB');
    }else {
      console.log('AAA');
    }
     
    // instrument ignore if: Ignore the if branch.
    if (a==1) {
      // do something
      console.log('BBB');
    }else {
      console.log('AAA');
    }
    

## Interpreting the coverageReport.json File

The **coverageReport.json** file records detailed coverage data. The meaning of each field in the file is described below.

Before reading this section, please review [Interpreting the Coverage Report](#section1485213972114) to understand the related concepts and calculation methods for line, branch, and function coverage.

1.  The **summary** field records the overall coverage metrics for the test, including line, function, and branch coverage, as shown in the following example.
    
    {
      "summary": {
        "lines": {         // Line statistics
          "total": 43,     // Number of executable lines
          "covered": 12,   // Number of lines covered
          "pct": 27.91     // Line coverage percentage
        },
        "functions": {     // Function statistics
          "total": 17,     // Number of functions
          "covered": 4,    // Number of functions covered
          "pct": 23.53     // Function coverage percentage
        },
        "branches": {      // Branch statistics
          "total": 2,      // Number of branches
          "covered": 0,    // Number of branches covered
          "pct": 0         // Branch coverage percentage
        }
      },
    }
    
2.  **files** is an array that records the detailed coverage data for all files. Each element in the array corresponds to a file.
    
    Taking a file as an example, the meanings of its fields are as follows.
    
    {
      "files": \[
        {
          "version": "bjc v1.0.0",   // Coverage algorithm version
          "versionCode": 10000,      // Version code for the coverage algorithm
          "path": "D:/DevEcoStudioProjects/MyApplication36/application/src/main/ets/applicationability/ApplicationAbility.ets",  // File path
          "hash": "6828362e96a78934b93db4b980fa5ad83af85a111bf187e74da89ae0c0ec613a",  // File hash
          "lineCnt": 44,     // Total number of lines in the file
          "count": 0,        // Execution count
          "projectPath": "D:/DevEcoStudioProjects/MyApplication36",     // Project path
          "functions": \[\],   // [List of functions in the file](#li12117420270)
          "exeLine": {},     // [Executable line mapping](#li394306142411)
          "summary": {}      // [File-level coverage summary](#li1560041862419)
        },
        ...
      \]
    }
    

-   **functions**
    
    **functions** is an array that records the detailed coverage data for all functions in the file. Each element in the array corresponds to a function.
    
    "functions": \[
      {
        "name": "ApplicationAbility.onCreate",    // Function name (anonymous\_N for an anonymous function)
        "count": 0,         // Function execution count
        "regions": \[\],      // [Corresponding code regions](#li321242192714)
        "branches": \[\],     // [Branches](#li103591744151920)
        "ignored": 0,       // Ignored execution count
        "index": 0          // Function index within file, starting from 0
      },
      ...
    \]
    
    -   **regions**
        
        **regions** is an array of executable lines, which may contain one, two, or multiple elements.
        
        The first element is the code region corresponding to the method. If there are more than one element, the subsequent elements are executable code regions within the method. The fields in each element are described as follows:
        
        "regions": \[
          {
            "startLoc": {   // Start location of the code
              "line": 8,    // Start line number
              "col": 3      // Start column number
            },
            "endLoc": {     // End location of the code
              "line": 10,   // End line number
              "col": 4      // End column number
            },
            "count": 0,     // Execution count
            "ignored": 0    // Ignored execution count
          }
        \]
        
        -   If a method has no implementation (an empty method), the **regions** array contains only one element, which is the code region corresponding to the method, as shown in the following example.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/ciOLiHn6RPaJPPCj7oIhOA/en-us_image_0000002532749825.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=301197D8161D2B4BA71E2D1AD2618D06A7DC88A9EEBC035D4CE735C945F93024)
            
            {
              "name": "dddd",
              "count": 1,
              "regions": \[
                {
                  "startLoc": {
                    "line": 31,
                    "col": 1
                  },
                  "endLoc": {
                    "line": 33,
                    "col": 2
                  },
                  "count": 1,
                  "ignored": 0
                }
              \],
            },
            
        -   If there is only one code region within a method, the **regions** array contains two elements, as shown in the following example.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/haDyIDhmSlm5pGCRXYNutQ/en-us_image_0000002532669865.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA5C5B3C5C642F7B6DA243162C9C6A9F2CF5D6FAC923B74E27465EF2785FDF57)
            
            {
              "name": "aaaaa",
              "count": 2,
              "regions": \[
                {    // Code region corresponding to the method
                  "startLoc": {
                    "line": 2,
                    "col": 1
                  },
                  "endLoc": {
                    "line": 9,
                    "col": 2
                  },
                  "count": 2,
                  "ignored": 0
                },
                {    // Executable code region
                  "startLoc": {
                    "line": 4,
                    "col": 3
                  },
                  "endLoc": {
                    "line": 9,
                    "col": 2
                  },
                  "count": 2,
                  "ignored": 0
                }
              \],
            }
            
        -   If a method contains multiple code regions, each additional code region adds one element to the **regions** array, as shown in the following example.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/7kTtYj4RSA2NbUUCMzbmQQ/en-us_image_0000002532749827.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA33358F0A028E5DD9FA540AC4A6492811A62BB9AE7F8E86DB07D72E30946FB2)
            
            {
              "name": "bbb",
              "count": 1,
              "regions": \[
                {    // Code region corresponding to the method (lines 11 to 18)
                  "startLoc": {
                    "line": 11,
                    "col": 1
                  },
                  "endLoc": {
                    "line": 18,
                    "col": 2
                  },
                  "count": 1,
                  "ignored": 0
                },
                {    // First executable code region (lines 13 to 15)
                  "startLoc": {
                    "line": 13,
                    "col": 13
                  },
                  "endLoc": {
                    "line": 15,
                    "col": 4
                  },
                  "count": 0,    // Code not executed because flag is false
                  "ignored": 0
                },
                {    // Second executable code region (lines 15 to 17)
                  "startLoc": {
                    "line": 15,
                    "col": 10
                  },
                  "endLoc": {
                    "line": 17,
                    "col": 4
                  },
                  "count": 1,    // Code executed
                  "ignored": 0
                }
              \],
            }
            
    -   **branches**
        
        **branches** is an array that includes code blocks related to conditional statements such as **if** and **switch case**. The definitions of each field in the elements are as follows:
        
        "branches": \[
          {
            "startLoc": {      // Start location of the code
              "line": 46,      // Start line number
              "col": 10        // Start column number
            },
            "endLoc": {        // End location of the code
              "line": 46,      // End line number
              "col": 11        // End column number
            },
            "trueCount": 0,    // Number of times the true branch was taken (0 means not taken)
            "falseCount": 1,   // Number of times the false branch was taken (0 means not taken)
            "group": \[         // Grouping (not involved in if statements; involved in switch case)
              0,               // group:\[0,1\] means elements 0 and 1 in the branches array belong to the same switch case.
              1
            \],
            "ignored": 0       // Ignored execution count
          }
        \]
        
        **Example 1**: Calling **eeee(2)**
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/ePUadSyzRmejb7sDNBR-kQ/en-us_image_0000002500909964.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A030B1D4355E39F3C4774F32DA43785D8CB61856B9179F46711F978F33E8545C)
        
        {
          "name": "eeee",
          "count": 1,
          "regions": \[
            ...
          \],
          "branches": \[
            {
              "startLoc": {
                "line": 46,
                "col": 10
              },
              "endLoc": {
                "line": 46,
                "col": 11
              },
              "trueCount": 0,     // The true branch was never taken.
              "falseCount": 1,    // The false branch was taken once.
              "group": \[          // Elements 0 and 1 belong to the same switch case; elements 2 and 3 belong to another switch case.
                0,
                1
              \],
              "ignored": 0
            },
            {
              "startLoc": {
                "line": 49,
                "col": 10
              },
              "endLoc": {
                "line": 49,
                "col": 11
              },
              "trueCount": 1,
              "falseCount": 0,
              "group": \[
                0,
                1
              \],
              "ignored": 0
            },
            {
              "startLoc": {
                "line": 55,
                "col": 10
              },
              "endLoc": {
                "line": 55,
                "col": 13
              },
              "trueCount": 0,
              "falseCount": 1,
              "group": \[
                2,
                3
              \],
              "ignored": 0
            },
            {
              "startLoc": {
                "line": 58,
                "col": 10
              },
              "endLoc": {
                "line": 58,
                "col": 13
              },
              "trueCount": 1,
              "falseCount": 0,
              "group": \[
                2,
                3
              \],
              "ignored": 0
            }
          \],
        }
        
        **Example 2**: Calling **bbb** twice, with arguments **2** and **\-1** respectively
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/WHurdXs3QQu34kdGTpGOCg/en-us_image_0000002532749821.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE6BDF45D7F499D2D1F3FC20BBF56E510F80EEE22798935E0E75F88048952B6B)
        
        Element **0** in **branches** corresponds to line 12, with both **trueCount** and **falseCount** being **1**, meaning the true branch and false branch of this condition were each taken once (the condition was met once, and not met once).
        
        {
          "name": "bbb",
          "count": 2,
          "regions": \[
            ...
          \],
          "branches": \[
            {
              "startLoc": {
                "line": 12,
                "col": 7
              },
              "endLoc": {
                "line": 12,
                "col": 12
              },
              "trueCount": 1,
              "falseCount": 1,
              "group": \[\],
              "ignored": 0
            },
            {
              "startLoc": {
                "line": 14,
                "col": 14
              },
              "endLoc": {
                "line": 14,
                "col": 20
              },
              "trueCount": 0,
              "falseCount": 1,
              "group": \[\],
              "ignored": 0
            },
            {
              "startLoc": {
                "line": 22,
                "col": 7
              },
              "endLoc": {
                "line": 22,
                "col": 13
              },
              "trueCount": 1,
              "falseCount": 1,
              "group": \[\],
              "ignored": 0
            }
          \]
        }
        
-   **exeLine**
    
    **exeLine** records the line numbers of all executable lines, as shown in the following example:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/cBFGSl5VSsqsHjYUGg7XWA/en-us_image_0000002500909952.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=562504DFA7CF8EE2CE915B2A3B11C21FD91F82D07ECA441181B264A3FB34C203)
    
    The generated **exeLine** is as follows:
    
    "exeLine": {
      "0": 2,
      "1": 3,
      "2": 4,
      "3": 6,
      "4": 7,
      "5": 8,
    }
    
-   **summary**
    
    **summary** records the detailed coverage data of a single file.
    
    "summary": {
      "lines": {           // Line statistics
        "total": 10,       // Number of executable lines
        "covered": 5,      // Number of lines covered
        "pct": 50,         // Line coverage percentage
        "executedLineCount": \[     // Number of code line executions (-1: not counted; 0: not executed; 1-N: executed 1-N times)
          -1,
          -1,
          -1,
          0,
          -1,
          1,
          0,
          2,
          2,
          -1,
          1,
          1,
          0,
          0,
          0,
          -1
        \]
      },
      "functions": {    // Function statistics
        "total": 6,     // Number of functions
        "covered": 5,   // Number of functions covered
        "pct": 83.33    // Function coverage percentage
      },
      "branches": {     // Branch statistics
        "total": 2,     // Number of branches
        "covered": 1,   // Number of branches covered
        "pct": 50       // Branch coverage percentage
      }
    }
