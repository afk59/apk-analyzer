# Exception Stack Trace Analysis

#### Introduction to Build Products

## ArkTS Debug Product: sourceMaps.map

**sourceMaps.map** is a build product in release mode, stored in **{ProjectPath}/{ModuleName}/build/{product}/cache/default/default@CompileArkTS/esmodule/release/sourceMaps.map**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/o_KAA-tQR_yVjv33SIShLw/en-us_image_0000002501069952.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F95150F163B2AF39FA81F68F4CC1180953BF6D391CD0C7563BD4D8F45473460)

## C++ Debug Product: Debug .so Files

Debug .so files are .so files with debug information, stored in **{ProjectPath}/{ModuleName}/build/{product}/intermediates/libs**.

For details, see [Retaining Debug Information with .so Files in Release Builds](#section5147812132).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/tWa4G8lnTi-3e5iT4OQa7Q/en-us_image_0000002500910116.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F4FE212E19B8F20F53055FFEF2BF730FA22106316C783A5FC42332E5B1FCFB9)

## Code Obfuscation Product: nameCache.json

**nameCache.json** is an obfuscation mapping table, a build product in release mode, stored in **{ProjectPath}/{ModuleName}/build/{product}/cache/default/default@CompileArkTS/esmodule/release/obfuscation**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/JRvC6o9GS7SD4LmX_CAKCQ/en-us_image_0000002532749977.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49A61997DB4A5A17E76D680EE84D0E23A3267C158FD053DF2C2E0A6FE71F6043)

#### C++ Stack Trace Analysis Principles

## Build Option Differences

-   **Debug**: Does not perform code optimization, with debug information attached.
-   **Release**: Maximizes code optimization, without debug information attached.
-   **RelWithDebInfo**: Both optimizes code and retains debug information. Similar to the **Release** mode.

## Retaining Debug Information with .so Files in Release Builds

Typically, symbol tables and debug information are stripped from release .so files.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/L-VRGWcsTbefpI97E9z-Rg/en-us_image_0000002500910100.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C52188D9134F1AE10448823A919CFEB56C2FF43C2851841A092C50E55C2E6CAF)

To retain the symbol table and debug information in the .so file, configure the following in the **build-profile.json5** file under **buildOption/externalNativeOptions**: "arguments": "-DCMAKE\_BUILD\_TYPE=RelWithDebInfo"

{
  "apiType": "stageMode",
  "buildOption": {
    "externalNativeOptions": {
      "path": "./src/main/cpp/CMakeLists.txt",
      "arguments": "-DCMAKE\_BUILD\_TYPE=RelWithDebInfo",
      "cppFlags": "",
    }
  },
  ...
}

The compilation yields two .so outputs:

-   **libs**: .so files with debug information.
-   **stripped\_native\_libs**: .so files with debug information and other redundant data removed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/gflmYfhJQhmqj7UOwZiWUQ/en-us_image_0000002532670031.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=792863545DDEE7968B0B597C0D319E7E11B4D1F8C610F553FBCF14944F6B2C64)

## C++ Stack Trace Analysis Process

llvm-addr2line ([obtain the llvm-addr2line tool](#li11164144153)) is a tool that translates function addresses into file names or line numbers.

Given an address in an executable file or an offset address in a relocatable object, the tool uses debug information to find the associated file name and line number.

The table below lists common parameters.

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

\-a

 | 

Displays the address in hexadecimal notation.

 |
| 

\-C

 | 

Decodes symbolic names to user-level names.

 |
| 

\-e

 | 

Sets the name of the executable file whose address needs to be converted.

 |
| 

\-f

 | 

Displays the file name, line number, and function name.

 |
| 

\-F

 | 

Displays the function name and file line number.

 |
| 

\-j

 | 

Reads the offset of the specified part instead of the absolute address.

 |
| 

\-p

 | 

Configures each address information to appear on a separate line.

 |

Examples:

View the file name, line number, and function name.

llvm-addr2line -f -e File.so

Find the code location corresponding to a specific address.

llvm-addr2line 0x00000000004005e7 -e test -f -C -s

Sample code:

llvm-addr2line -e libapplication.so 00003714 -f -C

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/e0W7S76nS56KfWwUTEoQbw/en-us_image_0000002500910118.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD93FC8F3276C0E529A95654AF8378133D00B9BFD3DC18D711124DA1A8A651A2)

ASan stack trace analysis

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/bLq2ompJSS-OOgWGhyA08g/en-us_image_0000002532670029.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC8752DB3948A688E2B46E9158B8C9FB999B21477C90709BC72F3265CCD30698)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/Mfy9rXiqSzWFCwvTbKcXMw/en-us_image_0000002532749975.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=211B41E238626E5DB3E7827331D7B79BF91BDD9F685A97A47E3F8AC317336E38)

## FAQs

-   What is UUID?
    
    Each executable is uniquely identified by a build UUID. Crash logs contain the build UUID of the app that crashed and the build UUIDs of all library files loaded by the app at the time of the crash.
    
-   How do I obtain the llvm-addr2line tool?
    
    You can find **llvm-addr2line.exe** in the **/deveco-studio/sdk/default/openharmony/native/llvm/bin** directory within the DevEco Studio installation path.
    

#### ArkTS Stack Trace Analysis Principles

## sourceMap Format

**Figure 1** Source code  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/oauFPhGlS5eZlcVzlmazzw/en-us_image_0000002500910102.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2394CD5C4AC16610860ADEB5DBD21A38E4FD7D3DF25591BC829591B367BE7787)

**Figure 2** Build product  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/Ek4PKysDQIOJfccJFLe-jA/en-us_image_0000002501069950.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE6E1D5497A134354679F17B4ED27EC6DF08B8972F2DDA8DA0FC8C727E2B541A "Click to enlarge")

**Actual code line mapping:**

70->29

71->30

72->31

73->32

**sourceMap structure**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/Jq-UZ1L8RUmydtPvmSbaYg/en-us_image_0000002532670019.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5F83814DBB5303FE232D68E1CBA69684789D273F3E1BAAE93DD2808C4527371)

The **sourceMaps.map** file, as an individual module build product, is a merged file that contains the mapping relationships of all the files in that module. Each JSON has a key that serves as the primary key for the unique path of the build product. The running program's .abc file retains the corresponding key information. When an exception occurs during runtime and the code is attributed to this file, the output information is the key in the file. **sources** is the actual source code file information used for stack trace decompression; **mappings** is an encoded line and column number mapping table, with each file having an independent mapping relationship.

-   **key**: For details, see [sourceMap Parsing Process](#section983741193211).
    
-   **version**: sourcemap standard version. Currently, it is **3**.
-   **file**: name of the generated file.
-   **sources**: list of source file URLs.
-   **names**: all variable and property names before conversion.
-   **mappings**: string that records location information.
-   **sourceRoot**: directory address of the source file, which can be used to reposition the source files on the server.
-   **entry-package-info:"entry|1.0.0"**: name and version from the module's **oh-package.json** file, used to associate with the resources of the de-obfuscation **nameCache**\-specified version.
-   **package-info: "har1|1.0.0"**: name and version of any other module specified in the **dependencies** field of the **oh-package.json** file. This information is useful for secondary parsing of sourceMap for third-party libraries.

## sourceMap Parsing Process

The following figure illustrates the structured parsing process for each key in the source map. Taking **entry|har1|1.0.0|src/main/ets/pages/w.ts** as an example, the fields are separated by the "|" delimiter and have the following meanings:

**entry** is the name of the module defined in the **oh-package.json5** file, **har1|1.0.0** is the name and version of the dependent HAR package defined in the **oh-package.json5** file (or the module's own name and version if there is no dependent package), and **src/main/ets/pages/w.ts** is the path to the referenced source file.

**Figure 3** Structured key processing in the sourceMap  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/6r9rMEsiQTy8K-XqdDW1Lw/en-us_image_0000002532749973.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6F57EB899885DAFA21DBEC2D6ACF1CC4E4A0663B79EFA21BF826663756D187D "Click to enlarge")

#### De-obfuscation Analysis Principles

For details about code obfuscation configuration, see [Code Obfuscation](../../../../building-an-app/using-obfuscation-for-code-hardening/document.md).

## Introduction to the Code Obfuscation Product

The code obfuscation product is in effect an obfuscation mapping table: **$ProjectPath\\$ModuleName\\build\\$product\\cache\\default\\default@CompileArkTS\\esmodule\\release\\obfuscation\\nameCache.json**.

{
  "home/src/main/ets/homeability/HomeAbility.ets": {
    "IdentifierCache": {
      "#AbilityConstant": "AbilityConstant",
      "#hilog": "hilog",
      "#UIAbility": "UIAbility",
      "#Want": "Want",
      "#window": "window",
      "HomeAbility#onWindowStageCreate#\_\_function": "i"
    },
    "MemberMethodCache": {
      "onCreate:10:16": "onCreate",
      "onDestroy:18:20": "onDestroy",
      "onWindowStageCreate:22:33": "onWindowStageCreate",
      "onWindowStageDestroy:35:38": "onWindowStageDestroy",
      "onForeground:40:43": "onForeground",
      "onBackground:45:48": "onBackground"
    },
    "obfName": "home/src/main/ets/homeability/HomeAbility.ets"
  },
  "compileSdkVersion": "5.0.0.25",
  "entryPackageInfo": "home|1.0.0",
  "PropertyCache": {
    "integratedHsp": "i",
    "asanClick": "j",
    "Index\_Params": "m",
    "testNapi": "o",
    "Index": "t",
    "testObfuscation": "g2"
  }
}

-   **originalfieldname**: This field represents the original file path and name of each file, such as **home/src/main/ets/homeability/HomeAbility.ets** in the preceding example.

-   **ObfName**: This field's key is fixed, and its value is the obfuscated name of each file, which is paired with the original field name.
    
    "obfName": "home/src/main/ets/pages/a.ts"
    
-   **IdentifierCache**: The value of this field corresponds to the mapping relationship between the variable names before and after obfuscation in the file.
    
    Variables are classified as common variables and class method variables.
    
    The format of the mapping relationship for common variables is as follows:
    
    originalvariablename :  obfuscatedvariablename
    
    -   **originalvariablename**: original variable name.
    
    -   **obfuscatedvariablename**: obfuscated variable name.
    
    The format of the mapping relationship for class method variables is as follows:
    
    /\*--------------------------key----------------------------------  :  -----------value----------\*/
    originalmethodname: originalmethodstartline: originalmethodendline :  obfuscatedmethodname
    
    -   **originalmethodname**: original method name.
    -   **\[: originalmethodstartline: originalmethodendline\]**: start line number and end line number of the original method. The left and right ends are both closed intervals.
    -   **obfuscatedmethodname**: obfuscated method name.
-   **MemberMethodCache**: The value of this field corresponds to the mapping relationship between the member method names before and after obfuscation in the file.
    
    When property obfuscation is enabled, the format of the member method mapping relationship is as follows:
    
    /\*--------------------------key---------------------------------  :  -----------value----------\*/
    originalmethodname:originalmethodstartline:originalmethodendline  :  obfuscatedmethodname
    
    When property obfuscation is not enabled, the format of the member method mapping relationship is as follows:
    
    /\*--------------------------key-------------------------------------  :  -----------value----------\*/
    originalmethodname : originalmethodstartline : originalmethodendline  :  originalmethodname
    
    -   **originalmethodname**: original member method name.
    -   **\[: originalmethodstartline: originalmethodendline\]**: start line number and end line number of the original member method. The left and right ends are both closed intervals.
    -   **obfuscatedmethodname**: obfuscated member method name.
-   **PropertyCache**: The value of this field is the mapping relationship between all global property names before and after obfuscation. This field has a value only when property obfuscation is enabled.
    
    The format of the property name mapping relationship is as follows:
    
    /\*--------key-------  :  -----------value----------\*/ 
    originalpropertyname  :  obfuscatedmethodname
    
    -   **originalpropertyname**: original property name.
    -   **obfuscatedmethodname**: obfuscated property name.

## Code Obfuscation Analysis Process

The exception stack is as follows:

Pid:58348
Uid:20020156
Reason:RangeError
Error name:RangeError
Error message:The number cannot be converted to a BigInt because it is not an integer
Stacktrace:
Cannot get SourceMap info, dump raw stack:
    at g2 (home|home|1.0.0|src/main/ets/pages/a.ts:6:6)
    at getVersion (home|home|1.0.0|src/main/ets/pages/a.ts:2:2)
    at anonymous (home|home|1.0.0|src/main/ets/pages/Index.ts:61:61)

1.  After transcoding via source map mapping, the stack trace is as follows:
    
    at g2 (home/src/main/ets/pages/tool.ts:7:27)
    at getVersion (home/src/main/ets/pages/tool.ts:2:30)
    at anonymous (home/src/main/ets/pages/Index.ets:23:40)
    
    **a.ts** is restored to **tool.ts** through the source map.
    
    "home|home|1.0.0|src/main/ets/pages/a.ts": {
        "version": 3,
        "file": "tool.ts",
        "sources": \[
          "home/src/main/ets/pages/tool.ts"
        \],
        "names": \[\],
        "mappings": "AAAA,MAAM,CAAC,OAAO,UAAU,UAAU,IAAI,MAAM;IAC1C,IAAI,KAAM,IAAiB,CAAA;IAC3B,UAAW;AACb,CAAC;AAED,eAA2B,MAAM;IAC/B,IAAI,GAAG,GAAG,MAAM,CAAC,MAAM,CAAC,CAAA;IACxB,OAAO,GAAG,CAAC;AACb,CAAC",
        "sourceRoot": "",
        "entry-package-info": "home|1.0.0"
      }
    
2.  Conduct function-level file name mapping.
    
    Check the obfuscation mapping table **$ProjectPath\\$ModuleName\\build\\$product\\cache\\default\\default@CompileArkTS\\esmodule\\release\\obfuscation\\nameCache.json**.
    
    "home/src/main/ets/pages/tool.ts": {
        "IdentifierCache": {
          "getVersion#res": "h2",
          "#testObfuscation:6:9": "g2"
        },
        "MemberMethodCache": {},
        "obfName": "home/src/main/ets/pages/a.ts"
      }
    
    The **IdentifierCache** and **MemberMethodCache** fields save the mapping relationship between the method names before and after obfuscation, in the following format: "source code method name:start line:end line":"obfuscated method name".
    
    The "source code method name" in the source code represents the parent-child relationship. Therefore, you can use the number sign (#) to retain the last name after mapping.
    
    The first stack has the obfuscated method name **g2**. If there are multiple **g2** entries, you need to filter them by line number range. Therefore, use the above fields to restore this method name:
    
    1.  Find the mapping table based on **key(home/src/main/ets/pages/tool.ts)**.
    2.  Find all entries in the above field where the obfuscated method name is **g2**. The entry found is:
        
        "#testObfuscation:6:9": "g2"
        
    3.  Find the entry whose line number range includes the line number restored in step 1. The line number obtained in step 1 is **7**, which is included in 6–9. Therefore, the corresponding source code method name is **#testObfuscation**, and the result after string processing is **testObfuscation**.
        
        at testObfuscation (home/src/main/ets/pages/tool.ts:7:27)
        at getVersion (home/src/main/ets/pages/tool.ts:2:30)
        at anonymous (home/src/main/ets/pages/Index.ets:23:40)
