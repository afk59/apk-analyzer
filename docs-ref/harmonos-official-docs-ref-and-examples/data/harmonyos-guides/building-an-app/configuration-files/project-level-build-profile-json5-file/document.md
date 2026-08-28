# Project-level build-profile.json5 File

#### File Structure

The structure of the project-level **build-profile.json5** file is as follows:

app
└── signingConfigs
    └── name
    └── material
        └── storePassword
        └── certpath
        └── keyAlias
        └── keyPassword
        └── profile
        └── signAlg
        └── storeFile
    └── type
└── products
    └── name
    └── signingConfig
    └── bundleName
    └── buildOption
        └── packOptions
            └── buildAppSkipSignHap
            └── fastBuildApp
            └── enableSourceCodeCheck
            └── deduplicateHar
            └── appWithSignedPkg
        └── debuggable
        └── generateSharedTgz
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
            └── idDefinedFilePath
        └── externalNativeOptions
            └── path
            └── abiFilters
            └── arguments
            └── cppFlags
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
        └── napiLibFilterOption
            └── excludes
            └── pickFirsts
            └── pickLasts
            └── enableOverride
        └── arkOptions
            └── buildProfileFields
            └── types
            └── tscConfig
                └── targetESVersion
                └── maxFlowDepth
            └── autoLazyImport
            └── autoLazyFilter
                └── include
                └── exclude
            └── reExportCheckMode
            └── branchElimination
            └── skipOhModulesLint
            └── expandImportPath
                └── enable
                └── exclude
            └── apPath
            └── hostPGO
        └── strictMode
            └── noExternalImportByPath
            └── useNormalizedOHMUrl
            └── caseSensitiveCheck
            └── duplicateDependencyCheck
            └── harLocalDependencyCheck
            └── enableStrictCheckOHModule
            └── disableSendableCheckRules
        └── nativeCompiler
        └── removePermissions
            └── name
        └── preloadSystemSo
    └── runtimeOS
    └── arkTSVersion
    └── compileSdkVersion
    └── compatibleSdkVersion
    └── targetSdkVersion
    └── compatibleSdkVersionStage
    └── bundleType
    └── label
    └── icon
    └── versionCode
    └── versionName
    └── resource
        └── directories
    └── output
        └── artifactName
    └── vendor
└── buildModeSet
    └── name
    └── buildOption
└── multiProjects
└── capabilities
    └── bundleName
    └── config
        └── name
        └── capability
        └── subCapabilities
            └── name
            └── capability
modules
└── name
└── srcPath
└── targets
    └── name
    └── applyToProducts

#### Fields in the Configuration File

The following table lists the fields contained in the project-level **build-profile.json5** file.

**Table 1** Fields in the project-level build-profile.json5 file
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

[app](#section1140014592111)

 | 

Object

 | 

Mandatory

 | 

Build configuration information.

 |
| 

[modules](#section1961794812219)

 | 

Object array

 | 

Mandatory

 | 

All modules in the project. The array length must be at least 1.

 |

#### app

Project-level compilation configuration, including the signature and product information.

**Table 2** app
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

[signingConfigs](#section153288223224)

 | 

Object array

 | 

Optional

 | 

Signature scheme information. Multiple signature schemes can be configured.

 |
| 

[products](#section45865492619)

 | 

Object array

 | 

Optional

 | 

Build product. Multiple products can be configured. For details, see [Configuring Multiple Targets and Products](../../configuring-your-build/configuring-multiple-targets-and-products/document.md).

 |
| 

[buildModeSet](#section137297344398)

 | 

Object array

 | 

Optional

 | 

Build mode set. Multiple build modes can be configured.

 |
| 

multiProjects

 | 

Boolean

 | 

Optional

 | 

Whether the current project supports multi-project build. Available options are as follows:

-   **true**: supported
-   **false** (default): not supported

 |
| 

[capabilities](#section1526318211219)

 | 

Object array

 | 

Optional

 | 

Open capabilities enabled for the app. For details, see [Signing an App Associated with a Registered App](../../../coding-and-debugging/configuring-a-debug-signature/document.md#section20943184413328).

This feature is supported since DevEco Studio 6.0.0 Beta5.

 |

#### modules

An object array that describes all modules in a project. The array length must be at least 1. The module configuration includes the name, path, and target-product configurations.

**Table 3** modules
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

Module name. The name must be the same as the value of [module.name](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#tags-in-the-configuration-file) in the **module.json5** file.

In the FA model, the corresponding file is **config.json**.

 |
| 

srcPath

 | 

String

 | 

Mandatory

 | 

Source code path of the module, which is the relative path of the module root directory relative to the project root directory. The module root directory can be outside the current project. For details, see [Importing or Referencing a Module](../../../environment-setup/creating-a-project/managing-modules/adding-or-deleting-a-module/document.md#section1295434814255).

NOTE:

Currently, the HAR and HSP modules from other projects can be referenced.

 |
| 

[targets](#table1433185416814)

 | 

Object array

 | 

Optional

 | 

Target information of a module, which is used to configure the association between the targets and products of the module during [customization of multiple targets and products](../../configuring-your-build/configuring-multiple-targets-and-products/document.md).

 |

**Table 4** targets
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

Target name, which is defined by **targets** in **build-profile.json5** of each module. Configuration is not required for HAR modules.

 |
| 

applyToProducts

 | 

String array

 | 

Optional

 | 

Products associated with the target. Configuration is not required for HAR modules.

 |

Example configuration:

{
  "modules": \[
    {
      "name": "entry",
      "srcPath": "./entry",
      "targets": \[
        {
          "name": "default",
          "applyToProducts": \[  
            "default"    // Product to which the default target of the module will be packed.
          \]
        }
      \]
    }
  \]
}

#### signingConfigs

An object array used to configure the signature scheme. Multiple signature schemes can be configured.

**Table 5** signingConfigs
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

Name of the signature scheme. The value can contain 1 to 64 characters, including only digits and letters.

 |
| 

[material](#table1269413811158)

 | 

Object

 | 

Mandatory

 | 

Materials related to the signature scheme, such as passwords and certificates.

After automatic signing is performed on **File > Project Structure... > Project > Signing Configs**, the configuration items under **material** are automatically set.

 |
| 

type

 | 

String

 | 

Optional

 | 

Signature type. Available options are as follows:

-   HarmonyOS
-   OpenHarmony

 |

**Table 6** material
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

storePassword

 | 

String

 | 

Mandatory

 | 

Keystore password, which is displayed in ciphertext.

 |
| 

certpath

 | 

String

 | 

Mandatory

 | 

Path of the debug or release certificate file. The file name extension is .cer.

 |
| 

keyAlias

 | 

String

 | 

Mandatory

 | 

Alias of the key.

 |
| 

keyPassword

 | 

String

 | 

Mandatory

 | 

Key password, which is displayed in ciphertext.

 |
| 

profile

 | 

String

 | 

Mandatory

 | 

Path of the profile file of the debug or release certificate. The file name extension is .p7b.

 |
| 

signAlg

 | 

String

 | 

Mandatory

 | 

Signing algorithm of the keystore. Currently, the value is fixed at **SHA256withECDSA**.

 |
| 

storeFile

 | 

String

 | 

Mandatory

 | 

Path of the keystore file. The file name extension is .p12.

 |

Example configuration:

{
  "app": { 
    "signingConfigs": \[
      {
        "name": "default",
        "type": "HarmonyOS",
        "material": {  
          "certpath": "D:\\\\SigningConfig\\\\debug\_hos.cer",
          "storePassword": "\*\*\*\*\*\*",
          "keyAlias": "debugKey",
          "keyPassword": "\*\*\*\*\*\*",
          "profile": "D:\\\\SigningConfig\\\\debug\_hos.p7b", 
          "signAlg": "SHA256withECDSA",
          "storeFile": "D:\\\\SigningConfig\\\\debug\_hos.p12"
        }
      }
    \]
  }
}

#### products

An object array used to configure product category information. Multiple product categories can be configured, such as the general default edition, paid edition, and free edition. For details, see [Configuring Multiple Targets and Products](../../configuring-your-build/configuring-multiple-targets-and-products/document.md).

**Table 7** products
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

Name of the product. There must be a product named **default**.

 |
| 

signingConfig

 | 

String

 | 

Optional

 | 

Signature scheme name of the current product category, which needs to be defined in [signingConfigs.name](#section153288223224). If this field is not set, the product is not signed.

 |
| 

compatibleSdkVersion

 | 

String/Number

 | 

Mandatory

 | 

Earliest SDK version compatible with the app/atomic service. The app/atomic service cannot be installed on devices running an earlier version. For details about the supported versions, see [All HarmonyOS Versions](https://developer.huawei.com/consumer/en/doc/harmonyos-releases/overview-allversion). For details about the relationship between the relevant fields and app compatibility, see [Application Compatibility](https://developer.huawei.com/consumer/en/doc/harmonyos-releases/app-compatibility).

-   If the operating environment is HarmonyOS, the value type is string, for example, **"compatibleSdkVersion": "6.0.2(22)"**.
-   If the operating environment is OpenHarmony, the value type is number, for example, **"compatibleSdkVersion": 22**.

NOTE:

When an APP Pack is built, the packing tool verifies the **compatibleSdkVersion** field of HSPs and HAPs. Only HSPs and HAPs that meet the requirements can be packaged. For details, see [Packing Tool](../../../system/debugging-tools/debugging-commands/packing-and-unpacking-tools/packing-tool/document.md).

 |
| 

targetSdkVersion

 | 

String/Number

 | 

Optional

 | 

Target SDK version of the app/atomic service. This setting provides forward compatibility when the API behavior in the new SDK version differs from earlier versions, allowing the previous API behavior to be retained.

If not specified, the value is the same as that of **compileSdkVersion**. For details about the supported versions, see [All HarmonyOS Versions](https://developer.huawei.com/consumer/en/doc/harmonyos-releases/overview-allversion). For details about the relationship between the relevant tags and app compatibility, see [Application Compatibility](https://developer.huawei.com/consumer/en/doc/harmonyos-releases/app-compatibility).

-   If the operating environment is HarmonyOS, the value type is string, for example, **"targetSdkVersion": "6.0.2(22)"**.
-   If the operating environment is OpenHarmony, the value type is number, for example, **"targetSdkVersion": 22**.

NOTE:

-   You are advised to set this field.
-   When an APP Pack is built, the packing tool verifies the **targetSdkVersion** field of HSPs and HAPs. Only HSPs and HAPs that meet the requirements can be packaged. For details, see [Packing Tool](../../../system/debugging-tools/debugging-commands/packing-and-unpacking-tools/packing-tool/document.md).

 |
| 

compileSdkVersion

 | 

String/Number

 | 

Optional

 | 

SDK version for building the app/atomic service. For details about the supported versions, see [All HarmonyOS Versions](https://developer.huawei.com/consumer/en/doc/harmonyos-releases/overview-allversion). For details about the relationship between the relevant tags and app compatibility, see [Application Compatibility](https://developer.huawei.com/consumer/en/doc/harmonyos-releases/app-compatibility).

-   If the operating environment is HarmonyOS, the value type is string, for example, **"compileSdkVersion": "6.0.2(22)"**.
-   If the operating environment is OpenHarmony, the value type is number, for example, **"compileSdkVersion": 22**.

NOTE:

-   For the HarmonyOS runtime environment, this field does not need to be explicitly configured. The SDK version built in DevEco Studio is used by default during compilation. If set, the value must match the SDK version of the current DevEco Studio.
-   This field is mandatory if the runtime environment is OpenHarmony.

 |
| 

compatibleSdkVersionStage

 | 

String

 | 

Optional

 | 

If **compatibleSdkVersion** is set to **API 12**, this field controls compatibility across different beta releases. The default value is **beta1**. Apps or atomic services cannot be installed on devices with a beta version lower than the specified value.

If **compatibleSdkVersion** is higher than API version 12, this field is ignored and does not need to be configured.

NOTE:

Configuring **beta_X_** allows you to generate an app that runs on the beta_X_ image. You will not be able to access features from later beta versions. For example, in API version 12, the sendable function and lazy import features in the beta3 version will not work if the configuration is set to **beta2** or **beta1**.

 |
| 

bundleName

 | 

String

 | 

Optional

 | 

Bundle name of the product.

 |
| 

[buildOption](#section14222051575)

 | 

Object

 | 

Optional

 | 

Build configuration of the product.

 |
| 

runtimeOS

 | 

String

 | 

Optional

 | 

Runtime environment of the product. Available options are as follows:

-   HarmonyOS
-   OpenHarmony

 |
| 

arkTSVersion

 | 

String

 | 

Optional

 | 

Version of the ArkTS syntax check tool, for example, 1.0 and 1.1.

The default value is the latest version supported by the ArkTS syntax check tool.

This item is available only in projects of API version 11 or later.

 |
| 

bundleType

 | 

String

 | 

Optional

 | 

Bundle type. Available options are as follows:

-   **app**: The bundle is used for an app.
-   **atomicService**: The bundle is used for an atomic service.
-   **shared**: The bundle is used for a shared package.

 |
| 

label

 | 

String

 | 

Optional

 | 

Name of the app/atomic service.

NOTE:

If **label**, **icon**, **versionCode**, **versionName**, and **resource** in **products** are configured, their settings will be used to replace the related configurations in **app.json5** during the build. This is usually used in scenarios where apps and atomic services are packed separately or together.

 |
| 

icon

 | 

String

 | 

Optional

 | 

App or atomic service icon

 |
| 

versionCode

 | 

Integer

 | 

Optional

 | 

Version number.

 |
| 

versionName

 | 

String

 | 

Optional

 | 

Version name.

 |
| 

[resource](#table49010413236)

 | 

Object

 | 

Optional

 | 

Directory where the resources corresponding to the name and icon are located.

 |
| 

[output](#table41925113333)

 | 

Object

 | 

Optional

 | 

Configuration of the app package generated by the custom product.

 |
| 

vendor

 | 

String

 | 

Optional

 | 

Vendor.

 |

**Table 8** resource
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

Mandatory

 | 

Resource directories.

 |

**Table 9** output
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

{
  "products": \[
    {
      "name": "default",
      "signingConfig": "default",
      "bundleName": "com.example.myapplication",
      "compatibleSdkVersion": "6.0.2(22)",
      "targetSdkVersion": "6.0.2(22)",
      "runtimeOS": "HarmonyOS",
      "arkTSVersion": "1.1",
      "bundleType": "app",
      "label": "$string:app\_name",
      "icon": "$media:app\_background",
      "versionCode": 1000000,
      "versionName": "1.0.0",
      "resource": {
        "directories": \[
          "./AppScope/resources"
        \]
      },
      "output": {
        "artifactName": "customizedTargetOutputName-1.0.0"
      },
      "vendor": "customizedProductVendorName",
    }
  \]
}

#### buildModeSet

**buildModeSet** is an object array that indicates the build mode set. Multiple build modes can be configured.

**Table 10** buildModeSet
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

Name of the build mode. By default, **debug**, **release**, and **test** modes are generated. You can customize the build mode. Although the test mode does not appear in the configuration file, it will be automatically activated when the testing framework is used to start tests.

 |
| 

[buildOption](#section14222051575)

 | 

Object

 | 

Optional

 | 

Configuration used by the build mode.

 |

#### capabilities

Open capabilities enabled for the app. For details, see [Signing an App Associated with a Registered App](../../../coding-and-debugging/configuring-a-debug-signature/document.md#section20943184413328).

**Table 11** capabilities
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

bundleName

 | 

String

 | 

Mandatory

 | 

Name of the package to which the current open capability belongs.

 |
| 

[config](#section746298142519)

 | 

Object array

 | 

Mandatory

 | 

Open capability configurations.

 |

## config

**Table 12** config
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

Name of the open capability.

 |
| 

capability

 | 

String

 | 

Optional

 | 

Unique identifier of the open capability. If **subCapabilities** does not exist, this parameter is mandatory.

 |
| 

[subCapabilities](#table98912388270)

 | 

Object array

 | 

Optional

 | 

Specific sub-open capabilities. If sub-open capabilities exist, this value is mandatory.

 |

**Table 13** subCapabilities
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

Name of the sub-open capability.

 |
| 

capability

 | 

String

 | 

Mandatory

 | 

Unique identifier of the sub-open capability.

 |

#### buildOption

Specific configuration information used for the build. **buildModeSet**, **products**, and the module-level **build-profile.json5** file support **buildOption**. Project-level build options are merged with module-level build options. For details about the merging rules and priorities, see [Rules for Combining Build Options](../../customizing-your-build/customizing-build-options/introduction/document.md#section1727865610255).

**Table 14** buildOption
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

[packOptions](#section03812484215)

 | 

Object

 | 

Optional

 | 

Configuration items related to packing.

 |
| 

debuggable

 | 

Boolean

 | 

Optional

 | 

Whether the build product can be debugged. Available options are as follows:

-   **true**: The product can be debugged. In the build product package, the **ets** directory contains **sourceMaps.map** files with source code mapping information.
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

This feature is supported since DevEco Studio 5.1.1 Beta1.

NOTE:

This field takes effect only for the HSP module.

 |
| 

[resOptions](#section5494153192911)

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

[sourceOption](#section15753419515)

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

[napiLibFilterOption](#section1488712919295)

 | 

Object

 | 

Optional

 | 

Filter option for NAPI library (.so) files. This item is marked as deprecated and is not recommended. You are advised to use [nativeLib/filter](../../configuring-your-build/configuring-for-c-builds/document.md#section15889929155720).

 |
| 

[arkOptions](#section111543473013)

 | 

Object

 | 

Optional

 | 

ArkTS build configuration.

 |
| 

[strictMode](#section13181758123312)

 | 

Object

 | 

Optional

 | 

Strict mode.

 |
| 

nativeCompiler

 | 

String

 | 

Optional

 | 

Compiler used for native compilation. Available options are as follows:

-   **Original** (default): original OpenHarmony native compiler.
-   **BiSheng**: [BiSheng compiler](../../../ndk-development/building-an-ndk-project/bisheng-compiler/document.md).

NOTE:

After DevEco Studio is upgraded to 5.1.1 Release, the BiSheng Compiler is used by default for new Native C++ projects. If you open an existing project, a dialog box is displayed, prompting you to switch to the BiSheng Compiler. Click **Try Now**.

 |
| 

[removePermissions](#section99591415322)

 | 

Object array

 | 

Optional

 | 

Redundant permissions in the dependency package to be deleted during compilation of the HAP/HSP module. The permissions of the module will not be deleted.

 |
| 

preloadSystemSo

 | 

Boolean

 | 

Optional

 | 

Whether to collect system .so files used by the app entry. The collected files will be preloaded during the app's cold start to optimize performance.

-   **true**: The system .so files are collected.
-   **false** (default): The system .so files are not collected.

This feature is supported since DevEco Studio 6.0.0 Beta3.

NOTE:

-   The app entry refers to the **srcEntry** tag configured under **module** in the **module.json5** file, or the **skills** tag with entry capability configured in **abilities** of the **module.json5** file (that is, configured with **entity.system.home** and **ohos.want.action.home**).
-   Only HAPs and bytecode HARs are supported. When a HAP is compiled, if system .so files exist in files imported by the app entry or in source code HARs, they will also be collected. When a bytecode HAR is integrated, its system .so files will be merged into the HAP.
-   Collection is not supported for dynamic variable imports.
-   This field and the **ohos.arkCompile.singleFileEmit** field in the **hvigor-config.json5** file are mutually exclusive; they cannot both be set to **true**.

 |

## packOptions

Configuration items related to packing.

**Table 15** packOptions
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

buildAppSkipSignHap

 | 

Boolean

 | 

Optional

 | 

Whether to skip the generation of a signed HAP during App Pack build. Available options are as follows:

-   **true**: Skip the generation of a signed HAP.
-   **false** (default): Do not skip the generation of a signed HAP. In this case, a signed HAP is generated.

To speed up the build process of an App Pack, set this to **true**.

 |
| 

fastBuildApp

 | 

Boolean

 | 

Optional

 | 

Whether to generate the HAP/HSP packages in the module during App Pack build.

-   **true**: Generate the App Pack directly without producing HAP/HSP packages, which can accelerate the build process.
-   **false** (default): Generate HAP/HSP and App Pack packages.

NOTE:

-   If **fastBuildApp** is set to **true**, no HAP package is generated regardless of whether **buildAppSkipSignHap** is set to **true** or **false**.
-   If **fastBuildApp** is set to **false**, the HAP package is generated according to **buildAppSkipSignHap**.

 |
| 

enableSourceCodeCheck

 | 

Boolean

 | 

Optional

 | 

Whether to check for source code files in HAP/HSP/HAR packages (excluding source code HARs with obfuscation disabled). If this feature is enabled, a warning message will be displayed during compilation when the packages contain source code files.

-   **true** (default): Enable check.
-   **false**: Disable check.

This feature is supported since DevEco Studio 6.0.0 Beta3.

NOTE:

-   Source code files are files with the following extensions: .c, .h, .cpp, .cs, .java, .rs, .py, .go, .ets, .js, and .ts.
-   Files with extensions .js, .ts, or .d.ets in [obfuscated source code HAR packages compiled in release mode](../../configuring-your-build/building-a-har/document.md#section19788284410) will not be checked.
-   The .js files in the **resources** directory will not be checked.

 |
| 

deduplicateHar

 | 

Boolean

 | 

Optional

 | 

Whether to remove duplicate HARs from the HSPs to reduce package size when multiple HAPs/HSPs depend on the same HAR (including cases where both a HAP and an HSP depend on the same HAR, or multiple HSPs depend on the same HAR) during APP/HAP/HSP build.

-   **true**: Remove duplicate HARs. The HAR will only be packaged into the HAP, and the following fields must be configured:
    -   [idDefinedFilePath](#section5494153192911) in the project-level **build-profile.json5** file.
    -   **useNormalizedOHMUrl** set to **true** in the project-level **build-profile.json5** file.
    -   **libIsolation** set to **false** in the [module.json5](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) file.
-   **false** (default): Do not remove duplicate HARs. The HAR will be packaged into each HAP/HSP.

NOTE:

-   Available since DevEco Studio 6.0.1 Beta1, this feature requires the device system to be upgraded to 6.0.1(21), and **compatibleSdkVersion** in the project-level **build-profile.json5** file to be set to **6.0.1(21)**.
-   When multiple HSPs depend on the same HAR, the HAP that depends on those HSPs must explicitly declare dependency on the HAR.
-   This feature only supports local HSP modules and does not support prebuilt HSP packages.
-   Scenarios where HAR deduplication is not supported:
    -   An app with multiple HAPs
    -   Independent running or debugging of an HSP
    -   Instrument tests and local unit tests
    -   Preview scenarios

 |
| 

appWithSignedPkg

 | 

Boolean

 | 

Optional

 | 

Whether to generate an additional app package with **all** in its name (for example, **xxx-all-unsigned.app** and **xxx-all-signed.app**) alongside the default app package during the build. The HAPs and HSPs included in such a package are all signed.

-   **true**: An additional app package with **all** in its name is generated alongside the default app package.
-   **false** (default): Only the default app package is generated, in which HAPs and HSPs are unsigned.

This feature is supported since DevEco Studio 6.0.2 Beta1.

NOTE:

To generate the **xxx-all-unsigned.app** and **xxx-all-signed.app** packages, you must set **appWithSignedPkg** to **true** and ensure that signing credentials are configured and that **enableSignTask** in **hvigor-config.json5** is not set to **false**.

 |

"buildOption": {
  "packOptions": {
    "buildAppSkipSignHap": true,
    "fastBuildApp": false,
  }
}

## resOptions

Resource build configuration information.

**Table 16** resOptions
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

[copyCodeResource](#table263894423012)

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

This field takes effect only for HAP/HSP compilation.

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
| 

idDefinedFilePath

 | 

String

 | 

Optional

 | 

Path to a user-defined .json5 file (supporting absolute/relative paths) with fixed resource IDs when HAR deduplication is enabled (that is, **deduplicateHar** is set to **true** in the project-level **build-profile.json5** file).

After duplicate HARs are removed, the HARs are only packaged into the HAP. Therefore, HSPs need to access resources in the HAP across packages via these fixed IDs.

This parameter is supported since DevEco Studio 6.0.1 Beta1.

 |

The following is an example of the .json5 file with fixed resource IDs specified by **idDefinedFilePath**:

// id-config.json5
{
  "record": \[{
    "type": "string",        // Resource type. It is recommended that all resources in the app use fixed IDs.
    "name": "app\_name",      // Resource name.
    "id": "0x01000000"       // User-defined hexadecimal resource ID, supporting IDs in the ranges \[0x01000000, 0x06FFFFFF\] and \[0x08000000, 0xFFFFFFFF\].
  }, {
    "type": "float",
    "name": "float1",
    "id": "0x01000001"
  }, {
    "type": "media",
    "name": "background",
    "id": "0x01000002"
  }, {
    "type": "profile",
    "name": "profile1",
    "id": "0x01000003"
  }\]
}

**Table 17** copyCodeResource
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

**includes** and **excludes** are mutually exclusive. Only one of them can be configured.

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/RHwTgOuvTMym0pQwpNt8wQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE193C0709BB9A39E071A49A41DABE07ED559B4D00C737530A985647E5AF6150)

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
    "idDefinedFilePath": "./id-config.json5",    // Both absolute and relative paths are supported.
  }
}

## sourceOption

Source code configuration. Different tags are used to classify source code so that different source code can be processed differently during build.

**Table 18** sourceOption
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

**Table 19** napiLibFilterOption
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

**Table 20** arkOptions
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

[buildProfileFields](../../customizing-your-build/obtaining-customized-build-parameters/document.md)

 | 

Object

 | 

Optional

 | 

Fields in the ArkTS profile file. The fields are customizable. The key can contain digits, letters, underscores (\_), and hyphens (-). The value type can only be string, number, or boolean.

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

[tscConfig](#table1714014154115)

 | 

Object

 | 

Optional

 | 

Configuration options related to TypeScript syntax compilation.

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

Object that defines filtering rules to control which modules are automatically marked with the **lazy** keyword. It takes effect only when **autoLazyImport** in **build-profile.json5** or **ohos.defaults.autoLazyImport** in **hvigor-config.json5** is set to **true**.

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

branchElimination

 | 

Boolean

 | 

Optional

 | 

Whether to enable code branch pruning to reduce the size of the build product. When this feature is enabled, code branches that are not executed in the release build mode will be pruned. For details, see the example in [branchElimination](#li12224142193612).

-   **true**: enabled (this can cause changes made with **Apply Changes** to be ignored for constants declared as **const**)
-   **false** (default): disabled

NOTE:

-   Only the projects developed using API version 11 or later based on the stage model are supported.
-   For HARs, this configuration is only effective for bytecode HARs.
-   Only the judgment expressions of boolean constants declared with **const** and string and number constants declared with **const** are supported.
-   Indirect imports are not supported. For example, if file A defines a constant A1, file B imports A1 and exports B1, and an .ets file imports B1 for judgment, pruning cannot be performed.

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

Configuration options for import path expansion.

This configuration is supported since DevEco Studio 6.0.0 Beta3.

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

This item is deprecated since API version 10. Because the partial mode may have compatibility issues, use the Target AOT capability instead of Host AOT.

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
    

**Table 21** tscConfig
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

targetESVersion

 | 

String

 | 

Optional

 | 

Target runtime ECMAScript version for the TypeScript syntax compilation products. Available options are as follows:

-   **ES2017**
-   **ES2021** (default)

 |
| 

maxFlowDepth

 | 

Integer

 | 

Optional

 | 

Maximum recursion depth of the control flow, with a range of \[2000, 65535\] and a default value of **2000**.

This field is supported since DevEco Studio 5.1.0 Release.

NOTE:

**maxFlowDepth** cannot be dynamically modified. That is, the [setBuildProfileOpt](../../expanding-build-capabilities/using-apis-for-extending-your-build/plug-in-context/document.md#section16692151412211) method cannot be used to set **maxFlowDepth** in the **hvigorfile.ts** or **hvigorconfig.ts** file.

 |

**Table 22** expandImportPath
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

-   In **import _XXX_ from '_A_'**, **_A_** must be a local HAR module. Expansion is supported only when **_A_** is a package name (not a relative path or a package name plus a path).
-   This configuration does not take effect when the HAR module is compiled independently.

 |
| 

exclude

 | 

String array

 | 

Optional

 | 

Alias of dependencies in **oh-package.json5**, used to specify dependencies for which import statements do not need to be expanded. Only local HAR modules are supported.

 |

**Table 23** autoLazyFilter
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

-   When **autoLazyImport** or **ohos.defaults.autoLazyImport** is set to **true**, **include** specifies the names of packages (the **name** field in the **oh-package.json5** file) to be automatically marked with the **lazy** keyword. Other packages will not be marked. Regular expressions are supported.
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

-   When **autoLazyImport** or **ohos.defaults.autoLazyImport** is set to **true**, **exclude** specifies the names of packages not to be marked with the **lazy** keyword. Other packages will be marked. Regular expressions are supported.
-   When **autoLazyImport** is set to **false**, **exclude** does not take effect.

NOTE:

-   **include** and **exclude** are mutually exclusive. Only one of them can be configured.
-   **exclude** does not support empty arrays or empty strings. At least one package name must be configured, and no duplicate package names are allowed.

 |

Example configuration:

"buildOption": {
  "arkOptions": {
    "buildProfileFields": {
      "targetData": "TargetData",
      "data": "DataTargetDefault"
    },
    "tscConfig": {
      "targetESVersion": "ES2021",
      "maxFlowDepth": 3000,
    },
    "autoLazyImport": true,
    "autoLazyFilter": {
      "include": \['entry'\]
    },
    "reExportCheckMode": "compatible",
    "branchElimination": true,
    "expandImportPath": {
      "enable": true,
      "exclude": \['localhar'\]
    },
  }
}

## strictMode

Defines the strict mode.

**Table 24** strictMode
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

noExternalImportByPath

 | 

Boolean

 | 

Optional

 | 

Whether to strictly check the import mode of absolute paths and cross-module import mode of relative paths.

-   **true**: yes
-   **false**: no

NOTE:

Since DevEco Studio NEXT Beta1 (5.0.3.800), when **useNormalizedOHMUrl** in the project-level **build-profile.json5** file is set to **true**, the default value of **noExternalImportByPath** is **true**; when **useNormalizedOHMUrl** is set to **false**, the default value of **noExternalImportByPath** is **false**.

 |
| 

useNormalizedOHMUrl

 | 

Boolean

 | 

Optional

 | 

Whether to use the normalized OHMUrl format (refer to the following explanation for the definition of OHMUrl). The normalized OHMUrl format unifies the format of the original OHMUrl. The integrated HSP and [bytecode HAR](../../configuring-your-build/building-a-har/document.md#section16598338112415) must use the normalized OHMUrl format.

-   **true**: Use the normalized OHMUrl format.
-   **false** (default): Do not use the normalized OHMUrl format.

NOTE:

-   This field is supported since API version 12.
-   An .ets file, after compilation, becomes part of the installation package; the bytecode corresponding to this .ets file is called a bytecode segment. OHMUrl is an identifier used to locate a bytecode segment.
-   If the project references any HAR/HSP module, make sure the **useNormalizedOHMUrl** setting in your project configuration is the same as the setting in the HAR/HSP module.
-   If **useNormalizedOHMUrl** is set to **true**, it may affect the obfuscation of local source code HARs. For details, see [Local Source Code HAR Package](../../../application-framework/arkts/arkts-compilation-toolchain/arkguard-for-source-code-obfuscation/package-specific-source-code-obfuscation-recommendations/document.md#local-source-code-har-package).
-   Since DevEco Studio NEXT Beta1 (5.0.3.800), when **useNormalizedOHMUrl** is set to **true**, files cannot be imported from external modules using relative paths or absolute paths, and the alias used by the dependent package in **oh-package.json5** must be the same as **name** configured in the **oh-package.json5** file of the package being depended upon.

 |
| 

caseSensitiveCheck

 | 

Boolean

 | 

Optional

 | 

Whether to strictly check for case sensitivity when importing files. Relative paths and symbolic links are supported.

-   **true**: Strict check is enforced.
-   **false** (default): Strict check is not enforced.

 |
| 

duplicateDependencyCheck

 | 

Boolean

 | 

Optional

 | 

Whether to check for local HSP modules that have dependencies on the same HAR. This setting is only effective for **Build App(s)**.

-   **true**: Enable the checking. In this case, if a local HSP module depends on the same HAR (regardless of location or dependency type), a compilation error is reported. (Note: If there is a remote HSP in the dependency chain, the remote HSP and its dependency chain will not be checked.)
-   **false** (default): Disable the checking.

 |
| 

harLocalDependencyCheck

 | 

Boolean

 | 

Optional

 | 

Whether to enable local dependency checking for HAR products.

-   **true**: Enable local dependency checking for HAR products. In this case, if there are local dependencies under **dependencies** or **dynamicDependencies** in the **oh-package.json5** file, a compilation error is reported.
-   **false** (default): Disable local dependency checking for HAR products.

NOTE:

Since HSP modules also generate HAR products during compilation, this setting applies to them as well.

 |
| 

enableStrictCheckOHModule

 | 

Boolean

 | 

Optional

 | 

Whether to perform strict validation on the type of parameters passed to methods in remote HAR/HSP packages.

-   **true**: Enable strict validation. If the parameter type is **undefined** or **null**, an error is reported.
-   **false** (default): Disable strict validation. If the parameter type is **undefined** or **null**, a warning is reported.

This feature is supported since DevEco Studio 6.0.1 Beta1.

 |
| 

disableSendableCheckRules

 | 

String array

 | 

Optional

 | 

Sendable rules for which validation is disabled. Currently, only **arkts-sendable-class-decorator** can be configured, indicating that custom decorators can be used on the **Sendable** class. For details about the check rules, see [Sendable Classes and Functions Cannot Use Decorators Other Than @Sendable](../../../application-framework/arkts/arkts-concurrency/inter-thread-communication/inter-thread-communication-objects/sendable-object/usage-rules-and-constraints-for-sendable/document.md#sendable-classes-and-functions-cannot-use-decorators-other-than-sendable).

This feature is supported since DevEco Studio 6.0.2 Beta1.

 |

Example configuration:

"buildOption": {
  "strictMode": {
    "useNormalizedOHMUrl": true,
    "caseSensitiveCheck": true,
    "disableSendableCheckRules": \["arkts-sendable-class-decorator"\],
  }
}

## removePermissions

Redundant permissions in the dependency package to be deleted during compilation of the HAP/HSP module. The permissions of the module will not be deleted. The value is an object array.

**Table 25** removePermissions
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

**Table 26** compression
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

**Table 27** media
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

**Table 28** filters
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

**Table 29** method
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

**Table 30** files
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
    { width:200, height:200 }, // Minimum width and height.
    // The second value here is omitted, indicating the maximum width and height is infinite.
  \],  // Images with resolutions greater than 200 × 200
\]

-   **width** and **height** must be numeric values.
-   The maximum width and height can be omitted, signifying infinity.

 |

**Table 31** exclude
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
