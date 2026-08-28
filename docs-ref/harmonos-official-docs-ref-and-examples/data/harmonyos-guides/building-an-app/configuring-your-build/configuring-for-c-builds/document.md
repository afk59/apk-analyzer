# Configuring for C++ Builds

Hvigor integrates CMake and Ninja as the build tools for C++ code. The initial configuration should suffice in most cases. Yet, you can add your custom configuration whenever necessary.

The CPP configuration includes **externalNativeOptions** and **nativeLib**. Unless otherwise specified, the configuration is supported in the project-level and module-level **build-profile.json5** files. The project-level configuration is merged with the module-level configuration (with a higher priority). For details about the merge rules and priorities, see [Rules for Merging Build Options](../../customizing-your-build/customizing-build-options/introduction/document.md#section1727865610255).

#### externalNativeOptions

Native build configuration information.

**Table 1** externalNativeOptions field description
| 
Name

 | 

Type

 | 

Mandatory/Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

String

 | 

Optional

 | 

Path of the CMake build script, that is, the **CMakeLists.txt** file.

 |
| 

abiFilters

 | 

String array

 | 

Optional

 | 

Supported ABI build environment. Available options are as follows:

-   arm64-v8a
-   x86\_64

If this item is not set, the default value **arm64-v8a** is used.

 |
| 

arguments

 | 

String/String array

 | 

Optional

 | 

CMake build arguments.

Hvigor will pass these custom arguments to the CMake build tool. For details about the build arguments, see the official CMake documentation. These arguments will override the default ones with the same names.

 |
| 

cppFlags

 | 

String

 | 

Optional

 | 

C++ compiler parameters.

Since DevEco Studio 6.0.1 Beta1, the new **\-iclang** parameter has been added to improve compilation efficiency. For details, see [Improving C++ Incremental Compilation Efficiency via IClang](../../improving-build-efficiency/enabling-performance-optimization-experimental-features/document.md#section324586847).

 |
| 

cFlags

 | 

String

 | 

Optional

 | 

C compilation parameters. This field is only applicable to the module-level **build-profile.json5** file.

Since DevEco Studio 6.0.1 Beta1, the new **\-iclang** parameter has been added to improve compilation efficiency. For details, see [Improving C++ Incremental Compilation Efficiency via IClang](../../improving-build-efficiency/enabling-performance-optimization-experimental-features/document.md#section324586847).

 |
| 

targets

 | 

String array

 | 

Optional

 | 

Libraries and executable targets in the CMake project to build by hvigor. This field is only applicable to the module-level **build-profile.json5** file.

 |

#### nativeLib

Native library (.so) configuration information.

**Table 2** nativeLib field description
| 
Name

 | 

Type

 | 

Mandatory/Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

[filter](#section17675528161517)

 | 

Object

 | 

Optional

 | 

Filter option for the native library (.so file). The priority of this item is higher than that of [napiLibFilterOption](../../configuration-files/project-level-build-profile-json5-file/document.md#section1488712919295).

 |
| 

[debugSymbol](#section2182144382320)

 | 

Object

 | 

Optional

 | 

Symbol table and debugging information to be removed from the .so file.

 |
| 

headerPath

 | 

String/String array

 | 

Optional

 | 

Path of the header file to be exported.

CAUTION:

Do not store source code files in this path. Otherwise, the files may be packed into the product. Exercise caution when configuring this parameter.

 |
| 

collectAllLibs

 | 

Boolean

 | 

Optional

 | 

Whether to collect files with any extensions when packing the **libs** directory.

-   **true**: All files (including files without file name extensions) are collected.
-   **false** (default): Only .so files are collected.

 |
| 

excludeFromHar

 | 

Boolean

 | 

Optional

 | 

Whether to exclude the .so files within the dependency HAR module during HAR build. When excluded, these .so files will not be packaged into the build product.

-   **true** (default): excluded
-   **false**: not excluded

NOTE:

The setting is effective only for HAR modules.

 |
| 

excludeSoFromInterfaceHar

 | 

Boolean

 | 

Optional

 | 

Whether to exclude the .so files from the HAR package during [HSP module compilation](../../../environment-setup/creating-a-project/managing-modules/developing-and-publishing-shared-packages/developing-a-dynamic-shared-package/document.md#section67683213597) to minimize the .tgz package size.

-   **true**: excluded. Consequently, the HSP package contains so files, but the HAR package does not.
-   **false** (default): not excluded. In this case, both HSP and HAR packages contain .so files.

NOTE:

-   The setting is effective only for HSP modules.
-   The setting has no effect when the **headerPath** field is configured in the project-level or module-level **build-profile.json5** file of the HSP module.

 |
| 

[librariesInfo](#section969845819510)

 | 

Object array

 | 

Optional

 | 

Dependency propagation information of the .so file. This field is only applicable to the module-level **build-profile.json5** file.

 |

## filter

Filter option for the native library (.so file). The priority of this item is higher than that of [napiLibFilterOption](../../configuration-files/project-level-build-profile-json5-file/document.md#section1488712919295).

**Table 3** filter field description
| 
Name

 | 

Type

 | 

Mandatory/Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

excludes

 | 

String array

 | 

Optional

 | 

.so files to exclude, which are matched based on the regular expression. The matches will not be packaged.

 |
| 

pickFirsts

 | 

String array

 | 

Optional

 | 

.so file with the highest priority (see [Priority of .so library files](#li143214241919)). It will be packed first.

 |
| 

pickLasts

 | 

String array

 | 

Optional

 | 

.so file with the lowest priority (see [Priority of .so library files](#li143214241919)). It will be packed last.

 |
| 

enableOverride

 | 

Boolean

 | 

Optional

 | 

Whether to allow the .so file with a higher priority to overwrite the .so file with a lower priority when these files have the same name.

-   **true**: allowed
-   **false** (default): not allowed

 |
| 

[select](#li1737916541996)

 | 

Object array

 | 

Optional

 | 

Options for precise selection of native products based on package name, version, and product name, enabling the inclusion or exclusion of native products in HAP, HSP, and HAR files.

The priority of **select** is higher than **excludes**, **pickFirsts**, and other configuration items.

 |

-   **Priority of .so library files**
    
    The priority of .so library files can be set through the **pickFirsts** and **pickLasts** options. The **pickFirsts** option is used to choose higher priority library files, while **pickLasts** is for selecting lower priority ones.
    
    The priority is determined by the collection order of the module's dependencies (modules or third-party packages), which are declared in the **dependencies** field in the **oh-package.json5** file. The rules are as follows:
    
    -   Third-party packages (including remote packages and local HAR packages) always have higher priority than local module dependencies.
    -   Dependencies are collected in a breadth-first traversal manner. As shown in the figure below, the priority order is: **current** > **library0** > **library1** > **library5** > **library2** > **library3** > **library4**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/H4HhIXz5RJGILNxqSvIMKg/en-us_image_0000002511592078.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F8200DC348CA20D5360AB83C11803B5A139CA0767A5CC5058D48EDD0411A778 "Click to enlarge")
        
-   **select**
    
    **Table 4** select field description
    | 
    Name
    
     | 
    
    Type
    
     | 
    
    Mandatory/Optional
    
     | 
    
    Description
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    package
    
     | 
    
    String
    
     | 
    
    Optional
    
     | 
    
    Package name.
    
     |
    | 
    
    version
    
     | 
    
    String
    
     | 
    
    Optional
    
     | 
    
    Package version.
    
     |
    | 
    
    includePattern
    
     | 
    
    String array
    
     | 
    
    Optional
    
     | 
    
    Native products to be packaged when multiple dependent packages contain native products with the same name. Glob patterns are supported.
    
    This field is supported since DevEco Studio 6.0.0 Beta2.
    
     |
    | 
    
    excludePattern
    
     | 
    
    String array
    
     | 
    
    Optional
    
     | 
    
    Native products to exclude. Glob patterns are supported. By default, all native products are packaged. The priority of **excludePattern** is higher than that of **includePattern**.
    
    This field is supported since DevEco Studio 6.0.0 Beta2.
    
     |
    | 
    
    include
    
     | 
    
    String array
    
     | 
    
    Optional
    
     | 
    
    Native products to be packaged when multiple dependent packages contain native products with the same name.
    
    This field is marked as deprecated since DevEco Studio 6.0.0 Beta2. You are advised to use the **includePattern** field instead.
    
     |
    | 
    
    exclude
    
     | 
    
    String array
    
     | 
    
    Optional
    
     | 
    
    Native products to exclude. By default, all native products are packaged.
    
    This field is marked as deprecated since DevEco Studio 6.0.0 Beta2. You are advised to use the **excludePattern** field instead.
    
     |
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/Xb7ZWwFYQI-EGChJ5jSoLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A172C3010525FEACC8B2FC1E33B7235D044199447966D4B3B352B607939AA54)
    
    **includePattern**/**excludePattern** and **include**/**exclude** cannot be configured at the same time.
    
    **Example 1**: The entry module depends on the HAR packages **har** (**@ohos/curl**) and **har1** (**@ohos/curl1**). The .so files in these HAR packages are listed below. Since both packages contain a file named **libcurl.so**, use **includePattern** to specify the **libcurl.so** file to be packaged, while using **excludePattern** to exclude any unwanted products.
    
    // Directory structure of har (@ohos/curl)
    └── har
        └── libs
            └── x86\_64
                └── libcurl.so
                └── libcurl1.so
            └── arm64-v8a
                └── libcurl2.so
                └── libcurl3.so
                └── libcurl4.so
    // Directory structure of har1 (@ohos/curl1)
    └── har1
        └── libs
            └── x86\_64
                └── libcurl.so
    // build-profile.json5
    {
      buildOption: {
        nativeLib: {
          filter: {
            select: \[ // The priority of select is higher than excludes, pickFirsts, and other configuration items.
              {
                package: "@ohos/curl", // Package name
                version: "1.3.5", // Package version
                excludePattern: \['\*\*/arm64-v8a/\*\*'\],    // Exclude all .so files in the arm64-v8a directory of har.
               },
              {
                package: "@ohos/curl1", // Package name
                version: "1.3.5", // Package version
                includePattern: \['\*\*/x86\_64/libcurl.so'\],  // Specify the libcurl.so file in har1 for packaging (duplicate files exist).
                // include: \["libcurl.so"\]  // Specify the libcurl.so file in har1 for packaging (duplicate files exist).
               },
            \]
          }
        }
      }
    }
    // Directory structure of the HAP after packaging
    └── entry-default.hap
        └── libs
            └── x86\_64
                └── libcurl.so    // From har1
                └── libcurl1.so   // From har
    
    **Example 2**: The HAR package contains multiple .so files, and **libcurl1.so** and **libcurl2.so** need to be packaged.
    
    // Directory structure of har (@ohos/curl)
    └── libs
        └── arm64-v8a
            └── libcurl.so
            └── libcurl1.so
            └── libcurl2.so
    // build-profile.json5
    {
      buildOption: {
        nativeLib: {
          filter: {
            select: \[  // The priority of select is higher than excludes, pickFirsts, and other configuration items.
              {
                package: "@ohos/curl", // Package name
                version: "1.3.5", // Package version
                includePattern: \[\],
                excludePattern: \['\*\*/arm64-v8a/!(\*(libcurl1|libcurl2).so\*)'\], // Package the libcurl1.so and libcurl2.so files in the arm64-v8a directory.
                // include: \[\],
                // exclude: \["libcurl.so"\] // Package the libcurl1.so and libcurl2.so files in the arm64-v8a directory.
               }
            \]
          }
        }
      }
    }
    

## debugSymbol

Symbol table and debugging information to be removed from the .so file.

**Table 5** debugSymbol field description
| 
Name

 | 

Type

 | 

Mandatory/Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

strip

 | 

Boolean

 | 

Optional

 | 

Whether to remove the symbol table and debugging information from the .so file.

-   **true** (default): removed
-   **false**: not removed

NOTE:

Since DevEco Studio NEXT Developer Beta2 (5.0.3.502), the default value is changed from **false** to **true**.

 |
| 

exclude

 | 

String array

 | 

Optional

 | 

.so files to exclude. The regular expression format is supported.

-   If **strip** is set to **true**, the matched .so files are not stripped.
-   If **strip** is set to **false**, only the matched .so files are stripped.

 |

## librariesInfo

Dependency propagation information of the .so file. This field is only applicable to the module-level **build-profile.json5** file.

**Table 6**
| 
Name

 | 

Type

 | 

Mandatory/Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

name

 | 

String

 | 

Mandatory

 | 

Name of the .so library of the module.

 |
| 

linkLibraries

 | 

String array

 | 

Mandatory

 | 

Dependency information of the .so library, in the format "Dependency package name::Dependency .so name".

 |

To declare the dependency relationships between libraries, for example, if **entry** depends on **curl**, you can configure **librariesInfo** in the **build-profile.json5** file of the module:

"buildOption": {
  "nativeLib": {
    "librariesInfo": \[
      {
        "name": "libentry.so",
        "linkLibraries": \["curl::curl"\]
      }
    \]
  }
}

When other modules depend on the module that has declared dependency propagation and use **libentry.so**, **libentry.so** will add the **curl::curl** dependency to the **INTERFACE\_LINK\_LIBRARIES** parameter; you do not need to pay attention to its dependencies.

add\_library(library::library SHARED IMPORTED)
set\_target\_properties(library::library PROPERTIES
    IMPORTED\_LOCATION "/path/to/file"
    INTERFACE\_LINK\_LIBRARIES "curl::curl")

#### Configuration Example

Example of module-level **build-profile.json5**

{
  ...
  "buildOptionSet": \[
    {
      "name": "release",
      "arkOptions": {
        "obfuscation": {
          "ruleOptions": {
            "enable": true,
            "files": \[
              "./obfuscation-rules.txt"
            \]
          }
        }
      },
      "externalNativeOptions": {
        "path": "./src/main/cpp/CMakeLists.txt", // Path of the custom CMakeLists.txt file. It is a relative path starting from the root directory of the module.
        "arguments": \["-DCMAKE\_BUILD\_TYPE=Debug"\], // Custom arguments to pass to CMake. For details about the build arguments, see the official CMake documentation. These arguments will override the default ones with the same names.
        "cppFlags": "-g", // Custom C++ flag.
        "abiFilters": \["arm64-v8a"\] // Target architecture. Default: arm64-v8a.
      },
      "nativeLib": {
        "debugSymbol": { // Configuration for stripping the symbols and debugging information from .so files of C++ build products.
          "strip": true, // Perform stripping.
          "exclude": \[\] // Regular expression to use for exclusions from the strip scope.
        },
        "filter": { // Configuration for packing .so files into the app package.
          "excludes": \[ // .so files to exclude from the app package. You can use this option to reduce the package size.
            "\*\*/3.so", // Exclude all .so files whose names are 3.
            "\*\*/x86\_64/\*.so" // Exclude all .so files of the x86\_64 architecture.
          \], 
          "pickFirsts": \["\*\*/1.so"\], // Pack the .so file with the highest priority based on the priority of the .so files.
          "pickLasts": \["\*\*/2.so"\], // Pack the .so file with the lowest priority based on the priority of the .so files.
          "enableOverride": true, // Allow the .so file with a higher priority to overwrite the .so file with a lower priority when these files have the same name.
        },
        "headerPath": "./src/main/cpp/include", // File that declares the C/C++ interfaces shared by the module.
        "librariesInfo":\[
          {
             "name": "libentry.so",
             "linkLibraries": \["curl::curl"\]
          }
        \]
      },
    },
  \],
  ...
}
