# Module-level build-profile.json5 File

#### File Structure

The structure of the module-level **build-profile.json5** file is as follows:

apiType
targets
└── name
└── runtimeOS
└── config
    └── distroFilter / distributionFilter
        └── apiVersion
            └── policy
            └── value
        └── screenShape
            └── policy
            └── value
        └── screenWindow
            └── policy
            └── value
        └── screenDensity
            └── policy
            └── value
        └── countryCode
            └── policy
            └── value
    └── deviceType
    └── buildOption
    └── atomicService
        └── preloads
            └── moduleName
└── source
    └── abilities
        └── name
        └── pages
        └── res
        └── icon
        └── label
        └── launchType
    └── pages
    └── sourceRoots
└── resource
    └── directories
└── output
    └── artifactName
showInServiceCenter
buildOption
buildOptionSet
└── name
└── debuggable
└── generateSharedTgz
└── copyFrom
└── resOptions
    └── compression
        └── media
            └── enable
        └── filters
            └── method
                └── type
                └── blocks
            └── files
                └── path
                └── size
                └── resolution
            └── exclude
                └── path
                └── size
                └── resolution
    └── resCompileThreads
    └── copyCodeResource
        └── enable
        └── includes
        └── excludes
    └── ignoreResourcePattern
    └── excludeHarRes
    └── includeAppScopeRes
└── externalNativeOptions
    └── path
    └── abiFilters
    └── arguments
    └── cppFlags
    └── cFlags
    └── targets
└── sourceOption
    └── workers
└── nativeLib
    └── filter
        └── excludes
        └── pickFirsts
        └── pickLasts
        └── enableOverride
        └── select
            └── package
            └── version
            └── includePattern
            └── excludePattern
            └── include
            └── exclude
    └── debugSymbol
        └── strip
        └── exclude
    └── headerPath
    └── collectAllLibs
    └── excludeFromHar
    └── excludeSoFromInterfaceHar
    └── librariesInfo
        └── name
        └── linkLibraries
└── napiLibFilterOption
    └── excludes
    └── pickFirsts
    └── pickLasts
    └── enableOverride
└── arkOptions
    └── runtimeOnly
        └── sources
        └── packages
        └── excludePackages
    └── types  
    └── obfuscation
        └── ruleOptions
            └── enable
            └── files
        └── consumerFiles
    └── buildProfileFields
    └── integratedHsp
    └── transformLib
    └── branchElimination
    └── byteCodeHar
    └── bundledDependencies
    └── packSourceMap
    └── autoLazyImport
    └── autoLazyFilter
        └── include
        └── exclude
    └── reExportCheckMode
    └── skipOhModulesLint
    └── expandImportPath
        └── enable
        └── exclude
    └── apPath
    └── hostPGO
└── packingOptions
    └── asset
        └── include
        └── exclude
    └── customizedOptions
        └── basePackage
└── removePermissions
    └── name
buildModeBinder
└── buildModeName
└── mappings
    └── targetName
    └── buildOptionName
entryModules

#### Fields in the Configuration File

The following table lists the configuration items in the module-level **build-profile.json5** file corresponding to modules of the Ability type (HAP). For modules of the Library type (HAR and HSP), the configuration items in the **build-profile.json5** file are a subnet of the items listed below.

**Table 1** Fields in the module-level build-profile.json5 file
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

apiType

 | 

String

 | 

Optional

 | 

API module type. Available options are as follows:

-   **stageMode**: stage model. This value is recommended.
-   **faMode**: FA model.

 |
| 

[targets](#section517483765814)

 | 

Object array

 | 

Optional

 | 

Targets. Multiple targets can be configured. The array length must be at least 1.

 |
| 

showInServiceCenter

 | 

Boolean

 | 

Optional

 | 

Whether to show in the service center.

-   **true**: yes
-   **false** (default): no

 |
| 

[buildOption](#section1010733210421)

 | 

Object

 | 

Optional

 | 

Build configuration of the module.

The **name**, **debuggable**, and **copyFrom** fields cannot be configured.

In the FA model, the **arkOptions** configuration only supports the **types** field.

 |
| 

buildOptionSet

 | 

Object array

 | 

Optional

 | 

Build option set. For details, see [Table 16](#table370712453588). The **name** item is mandatory. Each configuration is a common configuration option set of all available tools during compilation.

 |
| 

[buildModeBinder](#section642017215409)

 | 

Object array

 | 

Optional

 | 

Binding between the build mode (such as **debug** and **release**) and build configuration (**buildOption**). You can combine different build configurations and targets and bind them to a build mode, which must be defined in the project-level build mode list.

 |
| 

entryModules

 | 

String array

 | 

Optional

 | 

Entry module associated with a feature module. This parameter takes effect only for FA projects.

 |

#### targets

[Targets and products](../../configuring-your-build/configuring-multiple-targets-and-products/document.md) of the module. If specified, the array length must be at least 1.

**Table 2** targets
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

Target name.

 |
| 

runtimeOS

 | 

String

 | 

Optional

 | 

Environment for running the target. Available options are as follows:

-   HarmonyOS
-   OpenHarmony

 |
| 

[config](#section1967714835919)

 | 

Object

 | 

Optional

 | 

Target configuration.

 |
| 

[source](#section1838814817017)

 | 

Object

 | 

Optional

 | 

Source code of the target.

 |
| 

[resource](#table2065415762214)

 | 

Object

 | 

Optional

 | 

Resource directory contained in the target.

 |
| 

[output](#table965613111225)

 | 

Object

 | 

Optional

 | 

Configuration of the app package generated by the custom product.

 |

**Table 3** resource
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

directories

 | 

String array

 | 

Optional

 | 

Resource directories.

 |

**Table 4** output
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

artifactName

 | 

String

 | 

Mandatory

 | 

Name of the app package generated by the custom product. The name can contain only digits, letters, hyphens (-), underscores (\_), and periods (.). It can be a version number.

 |

Example configuration:

"targets": \[
  {
    "name": "default",
    "resource": {
      "directories": \["./src/main/resources"\]
    },
    "output": {
      "artifactName": "customizedTargetOutputName-1.0.0"
    }
  }
\]

#### config

Target configuration.

**Table 5** config
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

[distroFilter](#section113212281909)

 | 

Object

 | 

Optional

 | 

Distribution rule on AppGallery. It is used in the FA model.

 |
| 

[distributionFilter](#section113212281909)

 | 

Object

 | 

Optional

 | 

Distribution rule on AppGallery. It is used in the stage model.

 |
| 

deviceType

 | 

String array

 | 

Optional

 | 

Type of the device that can be used as the target. The device type must be predefined in **module.json5**.

In the FA model, the corresponding file is **config.json**.

 |
| 

[buildOption](#section1010733210421)

 | 

Object

 | 

Optional

 | 

Build configuration of the module.

The **name**, **debuggable**, and **copyFrom** fields cannot be configured.

 |
| 

[atomicService](#section106753237212)

 | 

Object

 | 

Optional

 | 

Atomic service configuration. This field is only supported for configuration in the stage model.

 |

#### source

Source code range of the target.

**Table 6** source
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

[abilities](#section1281869320)

 | 

Object array

 | 

Optional

 | 

Abilities of the custom target.

In a project of the FA model, pages in the **Ability** source code directory can be customized.

 |
| 

[pages](../../configuring-your-build/configuring-multiple-targets-and-products/introduction/document.md#section73018336472)

 | 

String array

 | 

Optional

 | 

In a project of the stage model, pages in the **pages** source code directory can be customized. The array length must be at least 1.

 |
| 

[sourceRoots](../../configuring-your-build/configuring-multiple-targets-and-products/introduction/document.md#section18668905913)

 | 

String array

 | 

Optional

 | 

Array of differentiated code spaces. This field is only supported for configuration in the stage model. The minimum array length is 1. The values in the array are subject to the following restrictions:

1.  They must be unique.
2.  They must be relative paths.
3.  They must be directories.
4.  The directories must actually exist.
5.  The directories must be at the same level as **src/main**.

When there are multiple values in the array, the addressing priority is the order of the values in the array.

 |

Example configuration:

"targets": \[
  {
    "name": "default",
    "source": {
       "pages": \[         // Stage model
        "pages/Index"
      \],
      "abilities": \[     // FA model
        {
          "name": ".MainAbility",
          "pages": \[
            "pages/index"
          \]
        }
      \],
      "sourceRoots": \[
        "./src/default"
      \]
    }
  }
\]

#### distroFilter/distributionFilter

Distribution rule on AppGallery. **distroFilter** is used in the FA model, and **distributionFilter** is used in the Stage model.

**Table 7** distroFilter/distributionFilter
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

[apiVersion](#section10176358110)

 | 

Object

 | 

Optional

 | 

Supported API version range.

 |
| 

[screenShape](#section1927031812114)

 | 

Object

 | 

Optional

 | 

Supported screen shapes.

 |
| 

[screenWindow](#section79432241314)

 | 

Object

 | 

Optional

 | 

Supported window resolutions when the app is running.

 |
| 

[screenDensity](#section99812302013)

 | 

Object

 | 

Optional

 | 

Supported pixel density of the screen.

 |
| 

[countryCode](#section04873351417)

 | 

Object

 | 

Optional

 | 

Code of the country or region to which the app is to be distributed.

 |

## apiVersion

**Table 8** apiVersion
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

policy

 | 

String

 | 

Mandatory

 | 

Available options are as follows:

-   **include**: The values specified will be included.
-   **exclude**: The values specified will be excluded.

 |
| 

value

 | 

Integer array

 | 

Mandatory

 | 

API versions. The value is an array of integers that each indicates an API version, for example, **10**.

 |

## screenShape

**Table 9** screenShape
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

policy

 | 

String

 | 

Mandatory

 | 

Available options are as follows:

-   **include**: The values specified will be included.
-   **exclude**: The values specified will be excluded.

 |
| 

value

 | 

String array

 | 

Mandatory

 | 

Available options are as follows:

-   **circle**: circle.
-   **rect**: rectangle.

 |

## screenWindow

**Table 10** screenWindow
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

policy

 | 

String

 | 

Mandatory

 | 

Only **include** is supported currently.

-   **include**: The values specified will be included.

 |
| 

value

 | 

String array

 | 

Mandatory

 | 

Supported window resolutions when the app is running. The value is an array of strings, each of which is in the format of Width × Height in pixels, for example, **454\*454**.

 |

## screenDensity

**Table 11** screenDensity
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

policy

 | 

String

 | 

Mandatory

 | 

Available options are as follows:

-   **include**: The values specified will be included.
-   **exclude**: The values specified will be excluded.

 |
| 

value

 | 

String array

 | 

Mandatory

 | 

Available options are as follows:

-   **sdpi**: screen density with small-scale dots per inch (SDPI). This value is applicable for devices with a DPI range of (0, 120\].
-   **mdpi**: screen density with medium-scale dots per inch (MDPI). This value is applicable for devices with a DPI range of (120, 160\].
-   **ldpi**: screen density with large-scale dots per inch (LDPI). This value is applicable for devices with a DPI range of (160, 240\].
-   **xldpi**: screen density with extra-large-scale dots per inch (XLDPI). This value is applicable for devices with a DPI range of (240, 320\].
-   **xxldpi**: screen density with extra-extra-large-scale dots per inch (XXLDPI). This value is applicable for devices with a DPI range of (320, 480\].
-   **xxxldpi**: screen density with extra-extra-extra-large-scale dots per inch (XXXLDPI). This value is applicable for devices with a DPI range of (480, 640\].

 |

## countryCode

**Table 12** countryCode
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

policy

 | 

String

 | 

Mandatory

 | 

Available options are as follows:

-   **include**: The values specified will be included.
-   **exclude**: The values specified will be excluded.

 |
| 

value

 | 

String array

 | 

Mandatory

 | 

Country/Region code defined in ISO-3166-1. Enumerated definitions of multiple countries and regions are supported.

 |

Example configuration:

"targets": \[
  {
    "name": "default",
    "config": {
      "distributionFilter": {
        "apiVersion": {
          "policy": "include",
          "value": \[12\]
        },
        "screenShape": {
          "policy": "include",
          "value": \[
            "circle",
            "rect"
          \]
        },
        "screenWindow": {
          "policy": "include",
          "value": \[
            "454\*454",
            "466\*466"
          \]
        },
        "screenDensity": {
          "policy": "exclude",
          "value": \[
            "ldpi",
            "xldpi"
          \]
        },
        "countryCode": {
          "policy": "include",
          "value": \[
            "CN"
          \]
        }
      }
    },
  }
\]

#### atomicService

**Table 13** atomicService
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

[preloads](../../configuring-your-build/configuring-multiple-targets-and-products/introduction/document.md#section206461457101917)

 | 

Object array

 | 

Optional

 | 

Module to be preloaded when the current module is running.

 |

**Table 14** preloads
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

moduleName

 | 

String

 | 

Optional

 | 

Name of the module to be preloaded.

 |

Example configuration:

"targets": \[
  {
    "name": "default",
    "config": {
      "atomicService": {
        "preloads": \[
          {
            "moduleName": "preloadSharedLibrary"
          }
        \]
      }
    }
  }
\]

#### abilities

Custom abilities of the target.

**Table 15** abilities
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

Name of the ability selected by the target.

 |
| 

[pages](../../configuring-your-build/configuring-multiple-targets-and-products/introduction/document.md#section73018336472)

 | 

String array

 | 

Optional

 | 

Page of the ability selected by the target in the FA model.

 |
| 

res

 | 

String array

 | 

Optional

 | 

Resource directory.

 |
| 

icon

 | 

String

 | 

Optional

 | 

Index of the ability icon file in the format "$media:ability\_icon."

 |
| 

label

 | 

String

 | 

Optional

 | 

Name of the ability visible to users. The value is a resource index to names in multiple languages.

 |
| 

launchType

 | 

String

 | 

Optional

 | 

Launch mode of the ability.

-   **multiton**: An ability instance is created each time the ability is started.

-   **standard**: Same as **multiton**. You are advised to use **multiton** instead.
-   **singleton** (default): An ability instance is created only when the ability is started for the first time.
-   **specified**: You can determine whether to create an ability instance when the app is running.

 |

Example configuration:

"targets": \[
  {
    "name": "default",
    "source": {
      "abilities": \[
        {
          "name": "EntryAbility",
          "icon": "$media:layered\_image",
          "label": "$string:EntryAbility\_label",
          "launchType": "singleton"
        }
      \]
    }
  }
\]

#### buildOption

Configuration of the module during build. **buildOptionSet**, **targets**, and the project-level **build-profile.json5** file support **buildOption**. Project-level build options are merged with module-level build options. For details about the merging rules and priorities, see [Rules for Combining Build Options](../../customizing-your-build/customizing-build-options/introduction/document.md#section1727865610255).

**Table 16** buildOption
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

Optional

 | 

Name of the build configuration.

 |
| 

debuggable

 | 

Boolean

 | 

Optional

 | 

Whether the build product can be debugged. Available options are as follows:

-   **true**: The product can be debugged.
-   **false**: The product cannot be debugged.

If this field is not configured, it defaults to **false** when the release build mode is used, and defaults to **true** when other build modes are used.

 |
| 

generateSharedTgz

 | 

Boolean

 | 

Optional

 | 

Whether to generate a .tgz package when the HSP module is compiled.

-   **true**: A .tgz package is generated.
-   **false**: No .tgz package is generated.

If this field is not set, the .tgz package is generated based on the value of **debuggable**. If **debuggable** is set to **true**, no .tgz package is generated. If **debuggable** is set to **false**, a .tgz package is generated.

This field is supported since DevEco Studio 5.1.1 Beta1.

NOTE:

This field takes effect only for the HSP module.

 |
| 

copyFrom

 | 

String

 | 

Optional

 | 

Name of a predefined build option in the same module to copy from. This enables you to replicate an existing build option in the same module.

 |
| 

[resOptions](#section754823013348)

 | 

Object

 | 

Optional

 | 

Resource build configuration information.

 |
| 

[externalNativeOptions](../../configuring-your-build/configuring-for-c-builds/document.md#section0721057575)

 | 

Object

 | 

Optional

 | 

Native build configuration information.

 |
| 

[sourceOption](#section2611239115413)

 | 

Object

 | 

Optional

 | 

Source code configuration information. Different tags are used to classify source code so that different source code can be processed differently during build.

 |
| 

[nativeLib](../../configuring-your-build/configuring-for-c-builds/document.md#section15889929155720)

 | 

Object

 | 

Optional

 | 

Native library (.so) configuration information.

 |
| 

[napiLibFilterOption](#section08781111115517)

 | 

Object

 | 

Optional

 | 

Filter option for NAPI library (.so) files. This item is marked as deprecated and is not recommended. You are advised to use [nativeLib/filter](../../configuring-your-build/configuring-for-c-builds/document.md#section15889929155720).

 |
| 

[arkOptions](#section8368152412552)

 | 

Object

 | 

Optional

 | 

ArkTS build configuration.

 |
| 

[packingOptions](#section1744183710558)

 | 

Object

 | 

Optional

 | 

Packing configuration. This setting is only applicable to HAR modules.

 |
| 

[removePermissions](#section155111918175715)

 | 

Object array

 | 

Optional

 | 

Redundant permissions to be deleted from the dependency packages during compilation. This setting is only applicable to HAP and HSP modules and does not change their own permissions.

 |

## resOptions

Resource build configuration information.

**Table 17** resOptions
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

[compression](#section2095319147103)

 | 

Object

 | 

Optional

 | 

Texture compression parameters for preset image resources in the project.

 |
| 

resCompileThreads

 | 

Integer

 | 

Optional

 | 

Number of threads for resource compilation. The value range is \[1, number of CPU cores of the host\].

This field is supported since DevEco Studio 5.1.0 Release.

 |
| 

[copyCodeResource](#table1476161719356)

 | 

Object

 | 

Optional

 | 

Configuration for copying resource files (non-source code files) located in the **src/main/ets** directory of the module.

NOTE:

This field has no effect for [non-obfuscated source code HARs](../../configuring-your-build/building-a-har/document.md#section197792874110).

 |
| 

ignoreResourcePattern

 | 

String array

 | 

Optional

 | 

Filters the names of files or folders in the **resources** directory or a custom resource directory using glob patterns. Matched files are excluded from the packaged output.

This field is supported since DevEco Studio 5.1.1 Beta1.

NOTE:

-   If the rule contains a path (for example, **./src/main/a.png**), it does not take effect.
-   If this field is not configured, the default filtering rule is used during HAP/HSP packaging: by default, .git, .svn, .scc, .ds\_store, desktop.ini, picasa.ini, cvs, thumbs.db, hidden files or directories starting with a period (.), and files ending with a tilde (~) are excluded from packaging.
-   If this field is set, the default filtering rule is overwritten. If this field is set to an empty array, no filtering rule is applied, that is, all resources are packaged.

 |
| 

excludeHarRes

 | 

String array

 | 

Optional

 | 

Names of the third-party HAR packages that do not participate in resource compilation during HAP/HSP compilation. After this field is set, the resources in the dependent HAR packages will not be packaged into the build product. Direct and indirect dependencies are supported.

This field is supported since DevEco Studio 6.0.0 Beta2.

NOTE:

This field can be set only in the HAP/HSP module.

 |
| 

includeAppScopeRes

 | 

Boolean

 | 

Optional

 | 

Whether to package the resources in the **AppScope** directory into the build product during HSP compilation.

-   **true** (default): Pack the resource files in the **AppScope** directory into the build product.
-   **false**: Do not pack the resource files in the **AppScope** directory into the build product.

This feature is supported since DevEco Studio 6.0.0 Beta2.

NOTE:

-   This field takes effect only for the HSP module.
-   If this field is set to **false**, the **icon** and **label** fields in **app.json5** do not take effect for the HSP module.

 |

**Table 18** copyCodeResource
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

enable

 | 

Boolean

 | 

Optional

 | 

Whether to pack the resource files (except .ets, .ts, and .js) in the **src/main/ets** directory into the build product.

Since DevEco Studio 6.0.0 Beta2, the **enable** field is configured with the default value **false** when you create a project or module, that is, resource files in the **ets** directory are not packed by default.

-   **true** (default): Pack the resource files in the **ets** directory into the build product.
-   **false**: Do not pack the resource files in the **ets** directory into the build product.

 |
| 

includes

 | 

String array

 | 

Optional

 | 

-   When **enable** is set to **true**, this parameter specifies the resource files to be packaged. The file paths support glob patterns and must start with **\*\*/**.
-   When **enable** is set to **false**, **includes** has no effect.

This field is supported since DevEco Studio 6.0.0 Beta2.

NOTE:

**excludes** and **includes** are mutually exclusive. Only one of them can be configured.

 |
| 

excludes

 | 

String array

 | 

Optional

 | 

-   When **enable** is set to **true**, this parameter specifies the resource files that are not packaged. The file paths support glob patterns and must start with **\*\*/**.
-   When **enable** is set to **false**, **excludes** has no effect.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/sudconDvS_y8fn4qxPL3rA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4639BBF939D91685354E0E0B9B8E8A2782497B8D04AABA66363E2E338D9F707)

-   In the **src/main/ets** directory of a module, only .ets, .ts, and .js files are processed during compilation. Other files are packaged as resource files in the build product, without obfuscation or encryption. If filtering is required, configure the **excludes** field.
-   Do not store source code files in system-hidden directories starting with a period (.). Otherwise, the filtering rule may become invalid, and all files in the **src/main/ets** directory will be packaged as resource files in the build product without obfuscation or encryption.

Example configuration:

"buildOption": {
  "resOptions": {
    "resCompileThreads": 2,
    "copyCodeResource": {
      "enable": true,
      "excludes": \['\*\*/entry/src/main/ets/component/big\_picture.png', '\*\*/\*.yml', '\*\*/subDir/\*\*'\],   // includes is configured in the same way.
    },
    "ignoreResourcePattern": \['\*.png' ,'abc.json'\],
    "excludeHarRes": \['har'\],
  }
}

## sourceOption

Source code configuration. Different tags are used to classify source code so that different source code can be processed differently during build.

**Table 19** sourceOption
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

workers

 | 

String array

 | 

Optional

 | 

JS/TS source code that uses the node.js worker. The source code is processed separately during build.

 |

Example configuration:

"buildOption": {
  "sourceOption": {
    "workers": \[
      "./src/main/ets/common/constants/CommonConstants.ets"
    \]
  }
}

## napiLibFilterOption

Filter option for NAPI library (.so) files. This field is marked as deprecated and is not recommended. You are advised to use [nativeLib/filter](../../configuring-your-build/configuring-for-c-builds/document.md#section15889929155720).

**Table 20** napiLibFilterOption
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

Excluded .so files. The listed NAPI libraries will not be packed.

 |
| 

pickFirsts

 | 

String array

 | 

Optional

 | 

.so file with the highest priority. It will be packed first.

 |
| 

pickLasts

 | 

String array

 | 

Optional

 | 

.so file with the lowest priority. It will be packed last.

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

## arkOptions

ArkTS build configuration.

**Table 21** arkOptions
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

[runtimeOnly](#table19892123422118)

 | 

Object

 | 

Optional

 | 

Name of the file to be dynamically imported and its dependencies. This field is only available for the stage model.

It is required when your project needs to import files or directories via variable-based relative paths or to incorporate third-party packages, ensuring these resources are included in the compilation process. For details, see [Dynamic Imports with Variable Expressions](../../../application-framework/arkts/arkts-runtime/arkts-modularization/dynamic-import/document.md#dynamic-imports-with-variable-expressions).

 |
| 

[types](../../../application-framework/arkts/arkts-compilation-toolchain/configuring-arkoptions-in-build-profile-json5/document.md#types)

 | 

String array

 | 

Optional

 | 

Custom types. It can be set to the bundle name or d.ts/d.ets file path.

 |
| 

[obfuscation](../../using-obfuscation-for-code-hardening/document.md)

 | 

Object

 | 

Optional

 | 

Code obfuscation configuration.

 |
| 

[buildProfileFields](../../customizing-your-build/obtaining-customized-build-parameters/document.md)

 | 

Object

 | 

Optional

 | 

Custom build parameters obtained during running. Key-value pairs are supported. The key can contain digits, letters, underscores (\_), and hyphens (-). The value type can only be string, number, or boolean.

 |
| 

integratedHsp

 | 

Boolean

 | 

Optional

 | 

Whether the HSP is an [integrated HSP](../../../getting-started/development-fundamentals/typical-scenarios-development/integrated-hsp/document.md).

-   **true**: yes
-   **false** (default): no

NOTE:

-   This field is supported since API version 12.
-   This field can be used only after **useNormalizedOHMUrl** is set to **true** in the project-level **build-profile.json5** file.
-   This field only takes effect when configured within an HSP module.

 |
| 

[transformLib](../../../application-framework/arkts/arkts-compilation-toolchain/ark-bytecode/customizing-ark-bytecode-during-compilation/document.md)

 | 

String

 | 

Optional

 | 

Bytecode instrumentation plug-in configuration, which allows you to modify the bytecode during compilation. It only supports the stage model and the format should be a relative path. The required file types for different platforms are as follows, and the file content needs to be generated on the corresponding platform, and cannot be copied and modified by changing the suffix for mixed use.

-   Windows: .dll files
-   Linux/macOS: .so files

NOTE:

-   For details about how to resolve issues with bytecode instrumentation not taking effect after adding configuration in the macOS environment, see [FAQs](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs/faqs-compiling-and-building-133).
-   For HARs, this configuration is only effective for bytecode HARs.

 |
| 

branchElimination

 | 

Boolean

 | 

Optional

 | 

Whether to enable code branch pruning to reduce the size of the build product. When this feature is enabled, code branches that are not executed in the release build mode will be pruned. For details, see the example in [branchElimination](#li71611425123512).

-   **true**: enabled (this can cause changes made with **Apply Changes** to be ignored for constants declared as **const**)
-   **false** (default): disabled

NOTE:

-   Only the projects developed using API version 11 or later based on the stage model are supported.
-   For HARs, this configuration is only effective for bytecode HARs.
-   Only the judgment expressions of boolean constants declared with **const** and string and number constants declared with **const** are supported.
-   Indirect imports are not supported. For example, if file A defines a constant A1, file B imports A1 and exports B1, and an .ets file imports B1 for judgment, pruning cannot be performed.

 |
| 

byteCodeHar

 | 

Boolean

 | 

Optional

 | 

Whether to build bytecode HARs. This field takes effect only in the HAR module. For details, see [Building a Bytecode HAR](../../configuring-your-build/building-a-har/document.md#section16598338112415).

-   **true**: supported
-   **false**: not supported

NOTE:

-   This field is supported since API version 12.
-   Since DevEco Studio NEXT Beta1 (5.0.3.800), when **useNormalizedOHMUrl** in the project-level **build-profile.json5** file is set to **true**, the default value of **byteCodeHar** is **true**; when **useNormalizedOHMUrl** is set to **false**, the default value of **byteCodeHar** is **false**.

 |
| 

bundledDependencies

 | 

Boolean

 | 

Optional

 | 

Whether to enable packing of multiple source code HARs, including both local and remote ones, into a single bytecode HAR. Note that the packing excludes bytecode HARs, HSPs, and npm files.

-   **true**: enabled
-   **false** (default): not enabled

NOTE:

-   This field is only available for [bytecode HARs](../../configuring-your-build/building-a-har/document.md#section16598338112415).
-   This field is supported since API version 12.
-   Only the stage model is supported.

 |
| 

packSourceMap

 | 

Boolean

 | 

Optional

 | 

Whether to package the **sourceMap** file into the product when compiling the [bytecode HAR](../../configuring-your-build/building-a-har/document.md#section16598338112415). This parameter can be configured only for HAR modules and takes effect only for bytecode HARs.

-   **true**: Pack the **sourceMap** file into the product.
-   **false**: Do not pack the **sourceMap** file into the product

This field is supported since DevEco Studio 5.1.0 Release.

NOTE:

-   If this parameter is not set, the default value is **true** in debug mode and **false** in release mode.
-   Packing **sourceMap** into the HAR in release mode may cause code asset leakage in the HAR.

 |
| 

autoLazyImport

 | 

Boolean

 | 

Optional

 | 

Whether to automatically add the **lazy** keyword to the import statement that complies with the lazy import syntax specifications during compilation. Note that the keyword is to be integrated directly into the source code and does not apply to the dependent bytecode HAR or HSP package. For details about lazy imports, see [Lazy Import](../../../application-framework/arkts/arkts-runtime/arkts-modularization/lazy-import/document.md).

-   **true**: Add the **lazy** keyword.
-   **false** (default): Do not add the **lazy** keyword.

NOTE:

-   When this field is set to **true**, scenario identification is skipped during the compilation process, allowing the **lazy** keyword to be added to all eligible import statements across the entire source code.
-   Only the stage model is supported.

 |
| 

[autoLazyFilter](#table1551310818378)

 | 

Object

 | 

Optional

 | 

An object that defines filtering rules to control which specific modules are automatically marked with the **lazy** keyword. This setting takes effect only when **autoLazyImport** is set to **true**.

This feature is supported since DevEco Studio 6.0.1 Beta1.

 |
| 

reExportCheckMode

 | 

String

 | 

Optional

 | 

Whether to intercept errors during compilation in the following scenario: Variables imported using lazy import are exported again in the same file.

-   **noCheck** (default): The check is not performed and no error is reported.
-   **compatible**: Compatible mode. A warning is reported.
-   **strict**: Strict mode. An error is reported.

This field is supported since DevEco Studio 5.0.5 Release.

 |
| 

skipOhModulesLint

 | 

Boolean

 | 

Optional

 | 

Whether to skip the [ArkTS rule check](../../../getting-started/learning-arkts/migration-from-typescript-to-arkts/typescript-to-arkts-cookbook/document.md) of the **oh\_modules** directory in the project. This field is supported since DevEco Studio 6.0.0 Beta1.

-   **true**: Skip the ArkTS rule check.
-   **false** (default): Do not skip the ArkTS rule check.

 |
| 

[expandImportPath](#table1921576135914)

 | 

Object

 | 

Optional

 | 

Configuration options related to import path expansion.

This feature is supported since DevEco Studio 6.0.0 Beta3.

NOTE:

The HAR modules do not support this field.

 |
| 

apPath

 | 

String

 | 

Optional

 | 

NOTE:

This item is no longer supported since API version 11. That is, its setting will no longer be effective.

Path of the app hotspot information file.

 |
| 

hostPGO

 | 

Boolean

 | 

Optional

 | 

Whether to enable profile-guided optimization (PGO). Available options are as follows:

-   **true**: enabled.
-   **false** (default): disabled

This parameter is deprecated since API version 10.

 |

-   If **branchElimination** is set to **true**, code branch pruning works as follows:
    
    \# BuildProfile file generated by the build process
    export const DEBUG = false;
    export const VERSION\_CODE = 100;
    # Custom .ets file
    import { DEBUG } from 'BuildProfile';
    import { VERSION\_CODE } from 'BuildProfile';
    if (DEBUG)
      {XXX} // This branch will be pruned during the build process.
    else
      {XXX}
    if (VERSION\_CODE){XXX} // This syntax involves type conversion and does not support code pruning.
    if (VERSION\_CODE === 100){XXX} // If code pruning is required, use this approach, explicitly specifying the condition as a boolean expression.
    

**Table 22** runtimeOnly
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

sources

 | 

String array

 | 

Optional

 | 

Relative path of the file or directory that the variable dynamically imports.

The file or directory must exist in the project, and the file name extension must be ets or ts.

 |
| 

packages

 | 

String array

 | 

Optional

 | 

Names of the dependencies that the variable dynamically imports.

They must be consistent with **dependencies** or **dynamicDependencies** configured in the project-level or module-level **oh-package.json5** file.

Since DevEco Studio 5.1.1 Beta1, third-party packages in **packages** can be configured using **dynamicDependencies**.

 |
| 

excludePackages

 | 

String array

 | 

Optional

 | 

Names of the source code HARs that do not participate in variable dynamic import during HAP/HSP compilation. Both direct and indirect dependencies are supported.

This field can be set only in the HAP/HSP module.

This field is supported since DevEco Studio 6.0.0 Beta2.

 |

**Table 23** expandImportPath
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

enable

 | 

Boolean

 | 

Optional

 | 

Whether to enable import path expansion. Enabling this feature can improve app runtime performance. For details about the principle and the side effects of this feature, see [Optimizing Performance with import Path Expansion](../../../application-framework/arkts/arkts-runtime/arkts-modularization/side-effects-and-optimization-of-module-loading/document.md#optimizing-performance-with-import-path-expansion).

-   **true**: enabled.
-   **false** (default): disabled.

NOTE:

In **import _XXX_ from '_A_'**, **_A_** must be a local HAR module. Expansion is supported only when **_A_** is a package name (not a relative path or a package name plus a path).

 |
| 

exclude

 | 

String array

 | 

Optional

 | 

Alias of dependencies for which import statements do not need to be expanded in **oh-package.json5**. Only local HAR modules are supported.

 |

**Table 24** autoLazyFilter
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

include

 | 

String array

 | 

Optional

 | 

-   When **autoLazyImport** is set to **true**, **include** specifies the names of packages (the **name** field in the **oh-package.json5** file) to be automatically marked with the **lazy** keyword. Other packages will not be marked. Regular expressions are supported.
-   When **autoLazyImport** is set to **false**, **include** does not take effect.

NOTE:

-   **include** and **exclude** are mutually exclusive. Only one of them can be configured.
-   **include** does not support empty arrays or empty strings. At least one package name must be configured, and no duplicate package names are allowed.

 |
| 

exclude

 | 

String array

 | 

Optional

 | 

-   When **autoLazyImport** is set to **true**, **exclude** specifies the names of packages not to be marked with the **lazy** keyword. Other packages will be marked. Regular expressions are supported.
-   When **autoLazyImport** is set to **false**, **exclude** does not take effect.

NOTE:

-   **include** and **exclude** are mutually exclusive. Only one of them can be configured.
-   **exclude** does not support empty arrays or empty strings. At least one package name must be configured, and no duplicate package names are allowed.

 |

Example configuration:

"buildOption": {
  "arkOptions": {
    "runtimeOnly": {
      "sources": \["./src/main/ets/utils/Calc.ets"\],
      "packages": \["myHar"\],
      "excludePackages": \["har1","har2"\],  // myHar depends on har1 and har2.
    },
    "buildProfileFields": {
      "buildOptionSetData": "BuildOptionSetDataRelease",
      "data": "DataRelease"
    },
    "transformLib": "./dll/example.dll",
    "branchElimination": true,
    "autoLazyImport": true,
    "autoLazyFilter": {
      "include": \['entry'\]
    },
    "reExportCheckMode": "compatible",
    "expandImportPath": {
      "enable": true,
      "exclude": \['localhar'\]
    },
  }
}

## packingOptions

Packing configuration. This setting is only applicable to HAR modules. This field is supported since DevEco Studio 5.1.0 Release.

**Table 25** packingOptions
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

[asset](#table14927147191119)

 | 

Object

 | 

Optional

 | 

Configuration items related to asset packing.

 |
| 

[customizedOptions](#table3942836112513)

 | 

Object

 | 

Optional

 | 

Customization options for the HAR module.

This field is supported since DevEco Studio 6.0.2 Beta1.

 |

**Table 26** asset
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

include

 | 

String array

 | 

Optional

 | 

Files to be included in the HAR product, configured via glob patterns.

NOTE:

-   The following directories are still excluded from the HAR product even when listed in the **include** field: **node\_modules**, **oh\_modules**, **.preview**, **build**, **.cxx**, and **.test**.

-   After the **include** field is configured, the **.gitignore** and **.ohpmignore** files do not take effect during source code HAR build. For details, see [Building in Debug Mode](../../configuring-your-build/building-a-har/document.md#section197792874110).

 |
| 

exclude

 | 

String array

 | 

Optional

 | 

Files to be excluded in the HAR product, configured via glob patterns.

NOTE:

-   The **oh-package.json5** files are still included in the HAR product even when listed in the **exclude** field.
-   After the **exclude** field is configured, the **.gitignore** and **.ohpmignore** files do not take effect during source code HAR build. For details, see [Building in Debug Mode](../../configuring-your-build/building-a-har/document.md#section197792874110).

 |

**Table 27** customizedOptions
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

basePackage

 | 

String

 | 

Optional

 | 

Relative path to the .abc file of the bytecode HAR that requires customization. After configuration, the compilation process can replace files in the target .abc package with identically named custom files, enabling customized modifications to the bytecode HAR.

 |

Example configuration:

"buildOption": {
  "packingOptions": {
    "asset": {
      "include": \["./src/router.json5", "router.json5"\],
      "exclude": \["./config/\*"\]
    },
    "customizedOptions": {
      "basePackage": "./basePackage/modules.abc",
    },
  }
}

## removePermissions

Redundant permissions in the dependency package to be deleted during compilation of the HAP/HSP module. The permissions of the module will not be deleted. The value is an object array.

**Table 28** removePermissions
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

Name of the permission to be deleted, which must be listed in **requestPermissions** in the **module.json** file of the dependency package.

 |

Example configuration:

"buildOption": {
  "removePermissions": \[
    {
      "name": "ohos.permission.ABILITY\_BACKGROUND\_COMMUNICATION"
    },
    {
      "name": "ohos.permission.ACCELEROMETER"
    }
  \]
}

#### compression

Texture compression parameters for preset image resources in the project.

**Table 29** compression
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

[media](#section1915545641714)

 | 

Object

 | 

Optional

 | 

Configuration for texture compression of images in the **media** folder of the resource directory.

 |
| 

[filters](#section185719543186)

 | 

Object array

 | 

Optional

 | 

File filtering configuration.

NOTE:

During compilation, image files are traversed and matched against the filter conditions. If a match is found, that image is processed. When both project-level and module-level filters are configured, the module-level conditions are matched first. If a match is successful at the module level, the project-level conditions are ignored. If no match is found at the module level, the process continues with the project-level conditions.

 |

## media

Configuration for texture compression of images in the **media** folder of the resource directory.

**Table 30** media
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

enable

 | 

Boolean

 | 

Optional

 | 

Whether to enable texture compression for images in the **media** folder.

-   **true**: enabled.
-   **false** (default): disabled

NOTE:

-   On Linux, ensure that the [libGL1 library is installed](../../../command-line-tools/setting-up-a-pipeline/document.md#section1478651816216).
-   Texture compression will change file names and contents of images, which can cause display issues with [layered icons](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#layereddrawabledescriptor) and during secondary editing. Use **filters** to exclude these files to avoid potential issues.

 |

## filters

File filtering configuration.

**Table 31** filters
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

[method](#table1568916396220)

 | 

Object

 | 

Mandatory

 | 

Method of texture compression.

 |
| 

[files](#table19762944112414)

 | 

Object

 | 

Optional

 | 

Files to be compressed. This field is used together with the **exclude** field.

 |
| 

[exclude](#table6219104952519)

 | 

Object

 | 

Optional

 | 

Files to exclude from compression in **files**.

 |

**Table 32** method
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

type

 | 

String

 | 

Mandatory

 | 

Conversion type.

-   **astc**: adaptive scalable texture compression. It is a GPU-friendly texture format that allows for faster display on devices with less memory usage.
-   **sut**: super compression for texture, which allows for faster display on devices with less memory usage. Compared with **astc**, it offers a higher compression ratio and less ROM usage.

 |
| 

blocks

 | 

String

 | 

Mandatory

 | 

Extended parameter of the **astc** or **sut** conversion type, which determines the image quality and compression ratio. Currently, only **"4x4"** is supported.

 |

**Table 33** files
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

String array

 | 

Optional

 | 

Filter condition for path matching. The value must be in glob patterns and be a relative path.

 |
| 

size

 | 

Two-dimensional array

 | 

Optional

 | 

Filter condition for size matching. The format is \[min,max\], which indicates files sized from **min** to **max**.

-   Values can be numbers, strings, or strings with units (case-insensitive), for example, **\[0, '1k'\]**.
-   Units are defined as follows: K/k = 1024, M/m = 1024 x 1024, G/g = 1024 x 1024 x 1024.
-   The maximum value in a range can be omitted, signifying infinity, for example, **\['3K'\]**.

 |
| 

resolution

 | 

Two-dimensional array

 | 

Optional

 | 

Filter condition for resolution matching. Example configuration:

resolution:\[
  \[
    { width:32, height:32 },  // Minimum width and height
    { width:64, height:64 },  // Maximum width and height
  \],  // Images with resolutions between 32 × 32 and 64 × 64
  \[
    { width:200, height:200 },  // Minimum width and height
    // The second value here is omitted, indicating the maximum width and height is infinite.
  \],  // Images with resolutions greater than 200 × 200
\]

-   **width** and **height** must be numeric values.
-   The maximum width and height can be omitted, signifying infinity.

 |

**Table 34** exclude
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

String array

 | 

Optional

 | 

Same as **files/path**.

 |
| 

size

 | 

Two-dimensional array

 | 

Optional

 | 

Same as **files/size**.

 |
| 

resolution

 | 

Two-dimensional array

 | 

Optional

 | 

Same as **files/resolution**.

 |

Example configuration:

"buildOption": {
  "resOptions": {
    "compression": {
      "media": {
                "enable": true // Set whether to enable texture compression for media images.
      },
              // File filter for texture compression, which is optional. If it is not specified, texture compression is performed on all images in the resource directory.
      "filters": \[
        {
          "method": {
                    "type": "sut", // Conversion type.
                    "blocks": "4x4" // Extended parameter of the conversion type.
          },
                  // Specify the files to be compressed. Only the files that meet all conditions and are not filtered by exclude can be compressed.
          "files": {
                    "path": \["./\*\*/\*"\], // Specify all files in the resource directory.
                    "size": \[\[0, '10k'\]\], // Specify files smaller than 10 KB.
                    // Specify images with a resolution less than 2048 x 2048.
            "resolution": \[
              \[
                        { "width": 0, "height": 0 }, // Minimum width and height.
                        { "width": 2048, "height": 2048 } // Maximum width and height.
              \]
            \]
          },
          // Exclude files that do not need to be compressed. Only files that meet all filter conditions are excluded.
          "exclude": {
                    "path": \["./\*\*/\*.jpg"\], // Filter out all .jpg files.
                    "size": \[\[0, '1k'\]\], // Filter out files smaller than 1 KB.
                    // Filter out images with a resolution less than 1024 x 1024.
            "resolution": \[
              \[
                        { "width": 0, "height": 0 }, // Minimum width and height.
                        { "width": 1024, "height": 1024 } // Maximum width and height.
              \]
            \]
          }
        }
      \]
    }
  }
}

#### buildModeBinder

Binding between the build mode (such as **debug** and **release**) and build configuration (**buildOption**). You can combine different build configurations and targets and bind them to the corresponding build mode. If **buildModeBinder** is not configured, see [Rules for Combining Build Options](../../customizing-your-build/customizing-build-options/introduction/document.md#section1727865610255) for the default binding policy.

**Table 35** buildModeBinder
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

buildModeName

 | 

String

 | 

Optional

 | 

Build mode name, which needs to be defined in the project-level **buildModeSet**.

 |
| 

[mappings](#table4672142011561)

 | 

Object array

 | 

Optional

 | 

One-to-one mapping between targets and build configurations (**buildOption**).

 |

**Table 36** mappings
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

targetName

 | 

String

 | 

Optional

 | 

Target name.

 |
| 

buildOptionName

 | 

String

 | 

Optional

 | 

Name of the build configuration (**buildOption**).

 |

Example configuration:

"buildModeBinder": \[
  {
    "buildModeName": "debug",
    "mappings": \[
      {
        "targetName": "default",
        "buildOptionName": "release"
      }
    \]
  }
\]
