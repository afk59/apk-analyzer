# oh-package.json5

ohpm supports distinguishing between project-level and module-level **oh-package.json5** files since 5.0.0. The following is a breakdown of each:

-   Project-level **oh-package.json5**: Located in the root directory of the project, this file is primarily used to describe global configurations. These may include dependency overrides (**overrides**), dependency relationship overrides (**overrideDependencyMap**), and parameterized configurations (**parameterFile**). For more details, see [Fields in the Project-level oh-package.json5 File](#section02162312018).
-   Module-level **oh-package.json5**: Located in the root directory of each module within the project, this file describes module information such as the package name, version, entry file (type declaration file), and dependencies. For details, see [Fields in the Module-level oh-package.json5 File](#en-us_topic_0000001792256137_oh-packagejson5-字段说明).

You can package each module in a standard DevEco Studio project into a HAR and publish it to the central repository of OpenHarmony third-party libraries. All packages published to the repository must include a module-level **oh-package.json5** file to describe the basic information of the current package.

#### Fields in the Project-level oh-package.json5 File

| 
Configuration Item

 | 

Name

 | 

Description

 | 

Requirement

 | 

**Type**

 | 

**Default Value**

 | 

**Remarks**

 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 

**Development-specific version**

 | 

modelVersion

 | 

Development-specific version number.

 | 

Mandatory

 | 

String

 | 

None

 | 

Set the development-specific version number.

 |
| 

**Description settings**

 | 

description

 | 

Description of the third-party library.

 | 

Optional

 | 

String

 | 

None

 | 

Project information.

 |
| 

**Dependency settings**

 | 

dependencies

 | 

Production dependencies.

 | 

Optional

 | 

Object

 | 

{}

 | 

Dependencies that participate in the compilation and runtime phases. This involves declaring third-party libraries that need to be imported in the code. (Avoid configuring production dependencies in the project-level **oh-package.json5** file.)

 |
| 

devDependencies

 | 

Development dependencies.

 | 

Optional

 | 

Object

 | 

{}

 | 

Development dependencies that are only needed during the development or testing phases of the project. Do not include in this field any dependencies that may be published with components that depend on them to a target device (such as a phone).

 |
| 

dynamicDependencies

 | 

Dynamic dependencies.

 | 

Optional

 | 

Object

 | 

{}

 | 

HSP modules on which the project dynamically depends. Avoid configuring dynamic dependencies in the project-level **oh-package.json5** file.

 |
| 

overrides

 | 

Dependency overrides.

 | 

Optional

 | 

Object

 | 

{}

 | 

Version used to replace a package in the dependency tree. For details, see [overrides](#en-us_topic_0000001792256137_overrides).

 |
| 

overrideDependencyMap

 | 

Dependency overrides.

 | 

Optional

 | 

Object

 | 

{}

 | 

Dependencies used to replace sub-dependencies of packages in the dependency tree. For details, see [overrideDependencyMap](#section106151513236).

 |
| 

exclusions

 | 

Sub-dependencies exclusion for third-party dependencies.

 | 

Optional

 | 

Object

 | 

{}

 | 

Sub-dependencies to exclude. One or more sub-dependencies of third-party dependencies (remote dependencies and local file dependencies) can be removed. For details, see [exclusions](#section18586313199).

 |
| 

**Others**

 | 

scripts

 | 

Custom script

 | 

Optional

 | 

Object

 | 

{}

 | 

This field maintains a mapping between script aliases and script content. You can run the **ohpm run <script alias >** command to execute the corresponding script.

 |
| 

hooks

 | 

Hook

 | 

Optional

 | 

Object

 | 

{}

 | 

Hook setting for installation or uninstallation, including fields **preInstall**, **postInstall**, **preUninstall**, **postUninstall**, **preVersion**, **postVersion**, **prePublish**, **postPublish**. Only hooks in the current project can be executed. Hooks in dependencies cannot be executed.

 |
| 

parameterFile

 | 

Path of the parameterization configuration file

 | 

Optional

 | 

String

 | 

None

 | 

Whether to enable parameterization. Parameterization is enabled if this field is configured and is disabled otherwise. You must also specify the path to the parameterization configuration file. For details, see [parameterFile](#section122411462820).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/-5_3JQLiT3uLouwKD8mzdA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F1470C4C2D3EF8DC3815C1811BD72612F369A090384C8FF251BBF8FA26B49B1)

Avoid configuring non-development dependencies in the project-level configuration file. In other words, module-specific dependencies and dynamic dependencies should be declared in the respective HSP or HAR modules.

#### Fields in the Module-level oh-package.json5 File

The module-level **oh-package.json5** file is located in the root directory of each module in the project. It describes information related to the current module when it is depended on by other modules, including: name, version number, entry files, and sub-dependencies.

| 
Configuration Item

 | 

Name

 | 

Description

 | 

Requirement

 | 

**Type**

 | 

**Default Value**

 | 

**Remarks**

 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 

**Description settings**

 | 

name

 | 

Name of the third-party library.

 | 

Mandatory

 | 

String

 | 

None

 | 

Unique identifier for the module when it is installed as a dependency.

Name in the format of @group/package name or package name, with a length of \[1, 128\]. The name must be globally unique in the app. It is recommended that the name contain the organization name (specified with **group**) to facilitate management and identification.

The name can contain exactly one at sign (@) and one path separator (/) only when there is an organization name (**group**).

**Organization name (group) format:**

1\. The value must start with a lowercase letter and can contain lowercase letters, digits, hyphens (-), and underscores (\_).

2\. The value cannot end with a hyphen (-) or underscore (\_).

3\. The value cannot contain keywords reserved for ArkTS.

**Package name format:**

1\. The value must start with a lowercase letter and can contain lowercase letters, digits, periods (.), hyphens (-), and underscores (\_).

2\. The value cannot end with a period (.), hyphen (-), or underscore (\_).

3\. The value cannot contain keywords reserved for ArkTS.

 |
| 

version

 | 

Version number of the third-party library.

 | 

Mandatory

 | 

String

 | 

1.0.0

 | 

Version number of the module's build product (HAR/HSP).

The value must follow the [SemVer](https://semver.org/) specification using the X.Y.Z (major.minor.patch) format, starting from 1.0.0.

 |
| 

description

 | 

Description of the third-party library.

 | 

Optional

 | 

String

 | 

None

 | 

Description of the built product (HAR/HSP), which helps make the module discoverable in searches. The value contains 0 to 512 characters.

 |
| 

keywords

 | 

Keywords.

 | 

Optional

 | 

Array

 | 

\[\]

 | 

A keyword array used for easy search, for example, \["tools", "project"\].

 |
| 

author

 | 

Author of the third-party library.

 | 

Optional

 | 

Object or string

 | 

None

 | 

An object or a string containing the **name** (mandatory), **email** (optional), and **url** (optional) fields.

The value of **name** can contain letters, digits, periods (.), hyphens (-), underscores (\_), and spaces.

-   Object format: "author": {"name": "xxx" , "email": "\*\*\*@example.com" , "url": "https://xxx.com" }
-   String format: "author": "name<\*\*\*@example.com>(https://xxx.com)"

 |
| 

homepage

 | 

Homepage link.

 | 

Optional

 | 

String

 | 

""

 | 

The value usually is a link to a Gitee project.

 |
| 

repository

 | 

Repository address of the third-party library.

 | 

Optional

 | 

String

 | 

""

 | 

Address of an open-source code repository. You can define whether the parameter is mandatory in the system settings on the private repository management page.

 |
| 

license

 | 

Open-source license used by the third-party library.

 | 

Mandatory

 | 

String

 | 

"ISC"

 | 

Open-source license of a project in compliance with specifications in [spdx license](https://spdx.org/licenses/). If the license is GPL, it is recommended that **repository** be specified.

 |
| 

**Dependency settings**

 | 

dependencies

 | 

Production dependencies.

 | 

Optional

 | 

Object

 | 

{}

 | 

Configure dependencies involved in the compilation and runtime phases. You can declare third-party libraries that need to be imported in the code.

 |
| 

devDependencies

 | 

Development dependencies.

 | 

Optional

 | 

Object

 | 

{}

 | 

Configure development dependencies that are only needed during the development or testing phases of the project. Do not include in this field any dependencies that may be published with components that depend on them to a target device (such as a phone). Dependencies introduced via **devDependencies** are not checked for circular dependencies.

 |
| 

dynamicDependencies

 | 

Dynamic dependencies.

 | 

Optional

 | 

Object

 | 

{}

 | 

Configure dynamic dependencies for HSP modules. This field is used when the HSP module needs to be dynamically loaded.

 |
| 

**File settings**

 | 

main

 | 

Main file

 | 

Mandatory

 | 

String

 | 

None

 | 

Main file to be loaded.

 |
| 

types

 | 

Type

 | 

Optional

 | 

String

 | 

""

 | 

Specified file type. If a type is defined using TypeScript for development, you need to specify a declaration file, which is a .d.ts or .d.ets file.

 |
| 

**Compatibility check configuration**

 | 

compatibleSdkVersion

 | 

SDK version.

 | 

Optional

 | 

String

 | 

None

 | 

This field sets the SDK version used by third-party library developers. It is automatically filled in by Hvigor during the build and used in SDK compatibility testing.

During execution of **prepublish** and **publish**, ohpm checks this field (for non-null and length validation) and, if any error is detected, displays a message at the log level specified through [compability\_log\_level](../ohpmrc/document.md#section96369529419) in the .ohpmrc file.

For details, see [Compatibility Field Configuration Example](#section194621247204911).

 |
| 

compatibleSdkType

 | 

SDK type.

 | 

Optional

 | 

String

 | 

None

 | 

This field sets the SDK type used by third-party library developers. It is automatically filled in by Hvigor during the build and used in SDK compatibility testing. Example values are **OpenHarmony** and **HarmonyOS**.

During execution of **prepublish** and **publish**, ohpm checks this field (for non-null and length validation) and, if any error is detected, displays a message at the log level specified through [compability\_log\_level](../ohpmrc/document.md#section96369529419) in the .ohpmrc file.

For details, see [Compatibility Field Configuration Example](#section194621247204911).

 |
| 

obfuscated

 | 

Whether to enable obfuscation.

 | 

Optional

 | 

Boolean

 | 

None

 | 

This field sets whether to enable obfuscation for third-party libraries. It is automatically filled in by Hvigor during the build and used in SDK compatibility testing.

During execution of **prepublish** and **publish**, ohpm checks this field (for non-null validation) and, if any error is detected, displays a message at the log level specified through [compability\_log\_level](../ohpmrc/document.md#section96369529419) in the .ohpmrc file.

For details, see [Compatibility Field Configuration Example](#section194621247204911).

 |
| 

nativeComponents

 | 

Native .so dependencies.

 | 

Optional

 | 

Array

 | 

None

 | 

This field sets the .so dependencies used by third-party library developers. It is automatically filled in by Hvigor during the build and used in SDK compatibility testing.

For the .so dependency (stored in the **libs** directory) that you import yourself, you need to manually maintain the array, each element of which is an object. The object can contain fields such as **name**, **compatibleSdkVersion**, and **compatibleSdkType**.

During execution of **prepublish** and **publish**, if the package contains .so files, ohpm checks this field and, if any error is detected, displays a message at the log level specified through [compability\_log\_level](../ohpmrc/document.md#section96369529419) in the .ohpmrc file. If there are no .so files in the package, this field will not be checked.

For details, see [Compatibility Field Configuration Example](#section194621247204911).

 |
| 

**Others**

 | 

artifactType

 | 

Type

 | 

Optional

 | 

String

 | 

"original"

 | 

The value is either **original** or **obfuscation**. **original** indicates that the source code is released (.ts/.ets). **obfuscation** indicates that the source code is obfuscated before being released.

 |
| 

scripts

 | 

Custom script

 | 

Optional

 | 

Object

 | 

{}

 | 

This field maintains a mapping between script aliases and script content. You can run the **ohpm run <script alias >** command to execute the corresponding script.

 |
| 

hooks

 | 

Hook

 | 

Optional

 | 

Object

 | 

{}

 | 

This field configures hook settings for installation or uninstall, including fields **preInstall**, **postInstall**, **preUninstall**, **postUninstall**, **preVersion**, **postVersion**, **prePublish**, and **postPublish**. Only hooks in the current project can be executed. Hooks in dependencies cannot be executed.

 |
| 

category

 | 

Trustlist for rule check

 | 

Optional

 | 

String

 | 

{}

 | 

The trustlist is automatically generated after being configured on the private repository management page. Each item in the trustlist must be a character string consisting of uppercase letters, lowercase letters, or underscores (\_), and multiple lists are separated by semicolons (;). Rule check is not performed for the items in the trustlist.

 |
| 

packageType

 | 

Package type

 | 

Optional

 | 

String

 | 

InterfaceHar

 | 

This field indicates whether a module is an HSP. It is automatically generated when a shared library is created and is set to **InterfaceHar** by default. If a static library does not contain this field, the module is identified as a HAR package.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/Lk7h3CtWRsKGD3TGJ8cGuA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BAE2834CA957A090DD90750336631C100224A03067A9897296E66D3E8D8B5700)

**Requirements for dependency naming:**

1\. In the **oh-package.json5** file, when local dependencies are declared under **dependencies**, **devDependencies**, or **dynamicDependencies**, the names of the dependencies configured can be inconsistent with the names of the dependent packages (that is, the names configured in the **oh-package.json5** files within the packages). However, this practice is discouraged. By default, ohpm will report warnings for such discrepancies.

To treat these warnings as errors and halt command execution, set [enforce\_dependency\_key](../ohpmrc/document.md#section920325116547) to **true** in the .ohpmrc file or **useNormalizedOHMUrl** to **true** under the **strictMode** field in the project-level [build-profile.json5](../../../building-an-app/configuration-files/project-level-build-profile-json5-file/document.md) file.

2\. When you use [parameterized configurations](#section122411462820), the dependency name must match the dependency package name (as configured in **oh-package.json5**). Any inconsistency will result in an error, causing the command execution to be interrupted.

3\. Avoid using invalid escape characters (such as **\\a**, **\\e**, and **\\o**) or Unicode codes (such as **\\uxxxx**) in the **oh-package.json5**, **overrideDependencyMap**, and **parameterFile** files.

#### Compatibility Field Configuration Example

Third-party library developers may use a different version of the SDK from the one used for compiling the project that integrates the third-party library. To address this potential inconsistency, ohpm adds compatibility field testing configurations. Here is an example of the configurations:

{
  "name": "library",
  "version": "1.0.0",
  "description": "Please describe the basic information.",
  "main": "Index.ets",
  "license": "Apache-2.0",
  "dependencies": {
    "liblibrary.so": "file:./src/main/cpp/types/liblibrary"
  },
  "**compatibleSdkVersion**": "12",
  "**compatibleSdkType**": "HarmonyOS",
  "**obfuscated**": false,
  "**nativeComponents**": \[
    {
      "name": "liblibrary.so",
      "compatibleSdkVersion": "12",
      "compatibleSdkType": "HarmonyOS"
    }
  \]
}

#### Creating an oh-package.json5 File

Perform the following operations to create an **oh-package.json5** file:

1.  Navigate to the directory of the package:
    
    cd /path/to/package
    
2.  Run the initialization command and set related parameters according to the questionnaire.
    
    -   For a module without namespaces, run the following command:
        
        ohpm init
        
    -   For a module with namespaces, run the following command:
        
        ohpm init --group group\_name
        
3.  If you skip filling in the questionnaire and create a default file, add the **\--yes** parameter to the initialization command line.
    
    ohpm init --yes
    
    The following is an example of the default **oh-package.json5** file:
    
    {
     "name": "package\_name",
     "version": "1.0.0",
     "description": "",
     "main": "index.ts",
     "author": "",
     "license": "ISC",
     "dependencies": {}
    }
    

#### Dependency Configuration Description

ohpm supports three types of dependencies: **dependencies**, **devDependencies**, and **dynamicDependencies**. Dependencies can be imported by specifying the version number, version range, tag, local .har/.tgz file path, or local source code directory, or using **@module** with the module name (example: **"module\_key": "@module:module\_name"**). If the version number of a dependent third-party library is set to **\***, the dependent package will use the latest version of that third-party library.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/pJkmuy03RAmb8PFsCz41fw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=15600760B672F9972276F26723FDCF878BCCB49C45606418DBFF7097A03FD664)

1\. Since DevEco Studio 6.0.0 Beta1, the @module configuration mode is supported. Since DevEco Studio 6.0.2 Beta1, dependencies introduced via **devDependencies** are not checked for circular dependencies.

2\. **module\_name** in the **@module** configuration must exist in the **modules** node of the **project/build-profile.json5** file or **project/.hvigor/dependencyMap/dependencyMap.json5** (generated by Hvigor) file.

3\. **module\_key** in the **@module** configuration must be the same as the name configured in the **oh-package.json5** file in the module directory specified by **@module:module\_name**.

1.  **dependencies**: These are production dependencies used in the compilation and runtime phases, defining the HAR/HSP package dependencies required for the production state and declaring third-party libraries to be imported in the code. If a component being depended on is ultimately used together with the component that depends on it on the target device (such as a phone), it must be configured in this field.
2.  **devDependencies**: These are development dependencies that participate only in the development or testing phases of the project. If a component being depended on is ultimately used together with the component that depends on it on the target device (such as a phone), it should not be configured in this field. Dependencies introduced via **devDependencies** are not checked for circular dependencies.
3.  **dynamicDependencies**: These are dynamic HSP dependencies used in conjunction with [dynamic imports](../../../application-framework/arkts/arkts-runtime/arkts-modularization/dynamic-import/document.md). Dynamic dependencies are not compiled when loaded but are conditionally imported modules or imported modules on demand, offering more efficient dependency loading speeds.
4.  Dependency configuration example:
    
    {
      "dependencies": {
        // Import dependencies by specific version number, which adheres to the semver standard.
        "specific\_version": "1.0.0",
    
        // Import dependencies by version number range. ^ means to import the latest version within the major version (for example, 1.x.x). ~ means to import the latest version within the minor version (for example, 1.0.x). Priority is given to the latest stable version that fits within the range.
        "scope\_version": "^1.0.1",
    
        // Import dependencies by tag. This example imports dependencies whose version tag is beta.
        "tag\_version": "tag:beta",
    
        // Import a local .har or .tgz file.
        "local\_file": "file:./xx.har",
    
        // Import the local source code, which can be source code from other local modules. In this example, the local module1 module is imported.
        "local\_source\_code": "file:../module1"
    
        // If the Foo module exists in the project, the modules node in the build-profile.json5 or dependencyMap.json5 file contains the Foo module, whose name in the oh-package.json5 file is foo\_test.
        "foo\_test": "@module:Foo"
      },
      "devDependencies": {
        // The dependency import type is the same as that of dependencies.
      },
      "dynamicDependencies": {
        // The dependency import type is the same as that of dependencies.
      }
    }
    
5.  Dependencies introduced via **devDependencies** are not checked for circular dependencies.
    
    As shown in the following **oh-package.json5** configuration, module **ma** depends on module **mb** via **dependencies**, while module **mb** in turn depends on module **ma** via **devDependencies**, thereby creating a circular dependency.
    
    // oh-package.json5 of module ma
    {
      "name": "ma",
      "version": "1.0.0",
      "description": "Please describe the basic information.",
      "main": "Index.ets",
      "author": "",
      "license": "Apache-2.0",
      "dependencies": {
        "mb": "../mb"
      }
    }
    
    // oh-package.json5 of module mb
    {
      "name": "mb",
      "version": "1.0.0",
      "description": "Please describe the basic information.",
      "main": "Index.ets",
      "author": "",
      "license": "Apache-2.0",
      "devDependencies": {
        "ma": "../ma"
      }
    }
    

#### overrides

The ohpm client supports the override mechanism since version 1.4.0. You can add the overrides configurations to the **oh-package.json5** file at the project level (that is, **oh-package.json5** in the root directory of the project) to replace the dependency in the dependency tree with another version. The replacement version can be specified by a version number, a version range, an existing local HAR package or source code directory, the [parameterFile](#section122411462820) configuration (for example, **"foo": "@param:dependencies.foo"**), or the **@module** with the module name to point to the module directory (for example, **"module\_key": "@module:module\_name"**).

For example, to ensure that foo 1.0.0 is always installed, add the following configuration to the project-level **oh-package.json5** file:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/IGczIYsVSgipuYyWn_ZpdQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B46FAB9814784DF92397FB23409563BC80E3BE25A1A0862C90309CDD8B94C73A)

1.  **overrides** must be configured in the project-level **oh-package.json5** file. The settings do not take effect if configured in the module-level **oh-package.json5** file.
2.  The @module configuration mode is supported since DevEco Studio 6.0.0 Beta1.
3.  **module\_name** in the **@module** configuration must exist in the **modules** node of the **project/build-profile.json5** file or **project/.hvigor/dependencyMap/dependencyMap.json5** (generated by hvigor) file. Otherwise, an error is reported.
4.  **module\_key** in the **@module** configuration must be the same as the name configured in the **oh-package.json5** file in the module directory specified by **@module:module\_name**. Otherwise, an error is reported.

{
  "overrides": {
    "foo": "1.0.0"
  }
}

If the foo source code, HAR package, or **@module** configuration exists on the local host, you can configure the following information in the project-level **oh-package.json5** file to ensure that the foo always uses your local version:

{
   "overrides": {
      // If the Foo module exists in the project, the modules node in the build-profile.json5 or dependencyMap.json5 file contains the Foo module, whose name in the oh-package.json5 file is foo\_test.
      // "foo\_test": "@module:Foo"
      // The foo source code directory exists on the local host, for example, the foo directory in the root directory of the project.
      // "foo": "file:./foo" 
      // The HAR file of foo exists on the local host, for example, foo.har in the libs directory in the root directory of the project.
      "foo": "file:./libs/foo.har"
   }
}

#### exclusions

**exclusions** is supported since ohpm 5.3.0. You can add **exclusions** configurations to the project-level **oh-package.json5** file (that is, the **oh-package.json5** file in the project root directory) to remove one or more sub-dependencies from a third-party dependency (remote dependency or local file dependency).

## Configuration Description

-   Configuration format
    
    // key:value format
    "\[@group/\]libname\[@spec\]" : \['exclude\_sub\_libname'\]
    
    -   Configure the key, which follows the format **\[@group/\]_libname_\[@spec\]**. It represents the name and version of the sub-dependency to exclude. **\[\]** indicates that the content within is optional. If the dependency does not have an organization name, **\[@group/\]** can be left empty. If there is no need for an exact match with a specific version number or local file dependency, **\[@spec\]** can be left empty. **spec** can be a specific version number or a local file path. (Both relative path and absolute path are supported, with relative paths based on the project root)
    -   Configure the value, which follows the format **\['exclude\_sub\_libname'\]**. It is a string array that contains multiple values, indicating the list of sub-dependencies to exclude.

-   Configuration example

{
  "exclusions": {
    "@ohos/lib1@1.0.0": \['@ohos/sub\_lib1'\]      // Exclude the sub-dependency @ohos/sub\_lib1 of the remote dependency @ohos/lib1.
    "@ohos/lib2@./lib2.har": \['@ohos/sub\_lib2'\] // Exclude the sub-dependency @ohos/sub\_lib2 of the local file dependency @ohos/lib2.
  }
}

-   Configuration restrictions
    -   **exclusions** must be configured in the project-level **oh-package.json5** file. The settings do not take effect if configured in the module-level **oh-package.json5** file.
    -   **exclusions** only takes effect on sub-dependencies of remote dependencies and local file dependencies, not on source code dependencies.
    -   **exclusions** only takes effect on dependencies configured in **dependencies** and **dynamicDependencies**.
    -   The key configured in **exclusions** must be different from that configured in [overrideDependencyMap](#section106151513236). Otherwise, a configuration conflict error is reported and the program is terminated.
    -   When automatic dependency version conflict resolution is enabled (**resolve\_conflict** is set to **true** in the **.ohpmrc** file), if **spec** is specified in **exclusions** but the dependency corresponding to **spec** is removed during version resolution, the **exclusions** configuration does not take effect. You are advised not to configure **spec** in such cases.

## Example

The following shows how to remove dependencies configured in **dependencies** and **dynamicDependencies** in **oh-package.json5** of a remote dependency or local file dependency. In this example, **<project>** indicates the root directory of the project.

1\. The module-level **oh-package.json5** file declares the dependencies to be installed: **@ohos/lib1** and **@ohos/lib2**.

{
  "name": "entry",
  "version": "1.0.0",
  "description": "Please describe the basic information.",  
  "dependencies": {
    "@ohos/lib1": "1.0.0" // Remote dependency
    "@ohos/lib2": "file:../lib2.har" // Local file dependency
  }
}

// oh-package.json5 configuration of @ohos/lib1
{
  "name": "@ohos/lib1",
  "version": "1.0.0",
  "description": "Please describe the basic information.",  
  "dependencies": {
    "@ohos/lib1\_sub1": "1.0.0" // Sub-dependency 1
    "@ohos/lib1\_sub2": "2.0.0" // Sub-dependency 2
  }
}

// oh-package.json5 configuration of @ohos/lib2
{
  "name": "@ohos/lib2",
  "version": "1.0.0",
  "description": "Please describe the basic information.",  
  "dependencies": {
    "@ohos/lib2\_sub1": "1.0.0" // Sub-dependency 1
    "@ohos/lib2\_sub2": "2.0.0" // Sub-dependency 2
  }
}

2\. Configure **exclusions** in the project-level **oh-package.json5** file as follows, where **lib2.har** is placed in the root directory of the project.

{
  "modelVersion": "6.0.2",
  "description": "Please describe the basic information.",
  "exclusions": {
    "@ohos/lib1@1.0.0": \['@ohos/lib1\_sub1'\],  // Exclude the sub-dependency @ohos/lib1\_sub1 of the remote dependency @ohos/lib1.
    "@ohos/lib2@./lib2.har": \['@ohos/lib2\_sub2'\] // Exclude the sub-dependency @ohos/lib2\_sub2 of the local file dependency @ohos/lib2.
  }
}

3\. Run the **ohpm install** command.

ohpm install --all

4\. After ohpm is installed, run the **ohpm list -d 10** command in the **entry** directory. The dependency structure is as follows:

entry 1.0.0 <project>\\entry
├─┬ @ohos/lib1 1.0.0
│ └── @ohos/lib1\_sub2 1.0.0 // @ohos/lib1\_sub2 is installed and @ohos/lib1\_sub1 is excluded.
├─┬ @ohos/lib2 <project>\\lib2.har
  └── @ohos/lib2\_sub1 1.0.0 // @ohos/lib2\_sub1 is installed and @ohos/lib2\_sub2 is excluded.

#### parameterFile

ohpm supports parameterization configuration. You can configure a parameterization file (in JSON5 format) in the root directory of the project for maintaining module or dependency version information. Modules are configured based on the versions in the file, allowing you to quickly switch dependency versions in different build scenarios. In addition, you can specify a parameterization file using commands to reduce the difficulty in changing module and dependency versions in pipeline scenarios.

ohpm supports parameterization configuration since version 1.6.0. You can add the **parameterFile** configuration to the project-level **oh-package.json5** file and specify the parameterization file path following the configuration rules below:

-   The file path can be a relative path and starts from the root directory of the project, for example, **"parameterFile": "./parameterFile.json5"**.
-   The configuration file content is in JSON5 format and supports JSON object nesting.
-   The characters supported by the parameterized key are the same as those in the package name. The characters are case sensitive. For details, see the requirements of the **name** field in [Fields in the Module-level oh-package.json5 File](#en-us_topic_0000001792256137_oh-packagejson5-字段说明).
-   The parameterized value can be a string or an object. If the value is of the string type, it must be a version number that complies with the [SemVer specification](https://semver.org/), a local relative path (relative to the directory where the parameterFile configuration file is located), or a local absolute path.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/ec4H6O2ZSF2B9oRIXKznjA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80E6AD513FA30F62B60C0C6EDDBF9475EFE008CAA56E63B48E3B939ADED1B3E7)

1.  **parameterFile** must be configured in the project-level **oh-package.json5** file. Otherwise, the configuration does not take effect or an error message is displayed.
2.  After the **parameterFile** field is configured, you can specify the file path for **parameterFile** using option **'-pf <string>'** or **'--parameterFile <string>'** in the **install**, **list**, and **version** commands.
3.  After the **parameterFile** field is set, you are not allowed to run the **update** or **uninstall** command, or to run an **install** command with the package name specified (for example, **'ohpm i <_pkg_\>'**).
4.  The path for **parameterFile** is case insensitive. Avoid distinguishing different configuration files by case.
5.  In **oh-package.json5**, only the following fields support parameterization: **version**, **dependencies**, **devDependencies**, **dynamicDependencies**, and **overrides**. **overrides** supports parameterization since DevEco Studio 6.0.0 Beta1.

## Basic Configuration Example

Example of a project-level **oh-package.json5** file:

{
  "modelVersion": "6.0.2",
  "description": "Please describe the project information.",
   ...
  "parameterFile": './parameterFile/parameterFile.json5', // Enable parameterization and specify the path of the parameterization configuration file.
  "overrides": {
    "libtest1": "@param:dependencies.libtest1", // All versions of dependencies named libtest1 are replaced with 1.0.1.
    "libnative": "@param:dependencies.libnative" // All versions of dependencies named libnative are replaced with the libnative source code dependency path.
  }
}

Example of a module-level **oh-package.json5** file:

{
  "name": "parameter-test",
  "version": "@param:version", // Must start with @param:.
  "description": "test desc.",
  "main": "index.ets",
  "author": "test author",
  "license": "ISC",
  "dependencies": {
    "libtest1": "@param:dependencies.libtest1"
  },
  "devDependencies": {
    "libtest2": "@param:devDependencies.libtest2"
  },
  "dynamicDependencies": {
    "libtest3": "@param:dynamicDependencies.libtest3"
  }
 }

Configuration Example of the File Specified by parameterFile

{
  "version": "1.0.0",
  "dependencies": {
    "libtest1": "1.0.1",
    "libnative": "../libnative" // Relative to the directory where the parameterFile configuration file is located.
  },
  "devDependencies": {
    "libtest2": "\*"
  },
  "dynamicDependencies": {
    "libtest3": "latest"
  }
}

## Example of Multiple Packages in One Repository

A code repository has multiple HAR/HSP modules. When publishing a package, you typically need to manually modify the version numbers of all modules before packaging and releasing. If there are many modules, this can be cumbersome and inefficient. You are advised to use parameterization configuration to address this issue.

**If the versions of all modules are different**:

As shown in the following project structure, the **version** fields in the **oh-package.json5** files of all modules are configured with parameterized versions (starting with **'@param:'**), and the versions of different modules are all different but are globally managed by the parametrization configuration file **parameter.json**. Before packaging, you only need to modify the version of the relevant module in the **parameter.json** file and then build all modules. During the packaging and building process, all parameterized versions of the modules will be replaced with the specific versions configured in **parameter.json** (for example, **@param:har1** will be replaced with **1.0.0**).

AppTest
└── har1 (module)
    └── oh-package.json5
        └── "version": "@param:har1"
└── har2 (module)
    └── oh-package.json5
        └── "version": "@param:har2"
... harn  (module)
    └── oh-package.json5
        └── "version": "@param:harn"
└── oh-package.json5 
    └── "parameterFile": "./parameter.json"    
└── parameter.json (parametrization configuration file)
    └── "har1": "1.0.0"
    └── "har2": "2.0.0"
    ...
    └── "harn": "n.0.0"

**If the versions of all modules are the same**:

As shown in the following project structure, all modules use the same parameterized version (**@param:module\_version**). Before packing, you only need to modify the value of **module\_version** in **parameter.json** and then build all modules. During the packing and building process, all parameterized versions of the modules will be replaced with the version corresponding to **module\_version** in **parameter.json** (for example, **@param:module\_version** will be replaced with **1.0.0**).

AppTest
└── har1 (module)
    └── oh-package.json5
        └── "version": "@param:module\_version"
└── har2 (module)
    └── oh-package.json5
        └── "version": "@param:module\_version"
... harn  (module)
    └── oh-package.json5
        └── "version": "@param:module\_version"
└── oh-package.json5 
    └── "parameterFile": "./parameter.json" 
└── parameter.json (parametrization configuration file)
    └── "module\_version": "1.0.0"

#### overrideDependencyMap

**overrideDependencyMap**, used to override the dependency relationships of source modules or third-party libraries, is supported in since ohpm 1.7.0. You can add an **overrideDependencyMap** configuration in the project-level **oh-package.json5** file and set it to key-value pairs, where the key indicates the dependency identifier, and the value indicates the path to the dependency relationship override file. During dependency installation, ohpm will replace all the direct child dependencies of a certain node in the dependency tree with the dependencies configured in the corresponding dependency relationship override file. The dependency types supported in the dependency relationship override file include **dependencies**, **devDependencies**, and **dynamicDependencies**. By using the **overrideDependencyMap** mechanism, you can dynamically change dependencies in different scenarios.

Additionally, you can use the **projectPackageJson** configuration item in the .ohpmrc file to override the configurations in the **oh-package.json5** file in the project's root directory. For details, see related descriptions in [ohpmrc](../ohpmrc/document.md).

**Description**

-   Configuration format
    
    "\[@group/\]libname\[@version\]" : "config\_path", where \[@group/\]libname\[@version\] is the dependency identifier (key), and config\_path is the path to the dependency relationship override file (value).
    

-   Configuration example
    
    {
      "overrideDependencyMap": {
      "@group/libname": "dep-test.json5" 
      }
    }
    

-   Configuration restrictions
    
    -   **overrideDependencyMap** must be configured in **oh-package.json5** at the project level. The configuration does not take effect in the module-level **oh-package.json5** file.
    
    -   The @version part in the key is optional. If it is not specified, all direct sub-dependencies of dependencies named **@group/libname** will be replaced. If it is specified, only those dependencies that are named **@group/libname** and have a version matching the **version** string will have their direct sub-dependencies replaced. The specified version must adhere to the SemVer specification and does not support tags or version ranges.
    
    -   The value should be the path to a JSON5 file. This file can only contain configurations for **dependencies**, **devDependencies**, and **dynamicDependencies**.
    
    -   The file path specified as the value must be an absolute path. If a relative path is used, you must set **odm\_r2\_project\_root=true** in the .ohpmrc file. With this configuration, the relative path will be resolved starting from the project root directory.

**Scenario Example for overrideDependency**

-   A dependency on remote package **libbase** is specified in the **oh-package.json5** file of the **entry** module, as shown in the following:
    
    {
      "name": "entry",
      "version": "1.0.0",
      "main": "Index.ets",
      "license": "Apache-2.0",
      "dependencies": {
        "libbase": "1.0.0"
      }
    }
    
-   The module-level **oh-package.json5** file contains a sub-dependency **lib1** in the dependency **libbase**, as shown in the following:
    
    {
      "name": "libbase",
      "version": "1.0.0",
      "description": "Please describe the basic information.",
      "main": "Index.ets",
      "author": "",
      "license": "Apache-2.0",
      "dependencies": {
        "lib1": "1.0.0" // Sub-dependency
      }
    }
    
-   The content of the **oh-package.json5** file in the project root directory is as follows:
    
    {
      "name": "overridedependencymaptest",
      "version": "1.0.0",
      "description": "Please describe the basic information.",
      "overrideDependencyMap": {      
        "libbase": "D:\\\\overrideDependencyMapTest\\\\dep-debug.json5" // overrideDependencyMap configuration. Multiple entries are allowed.
      }
    }
    
-   The dependency configuration in the **dep-debug.json5** file is as follows:
    
    {
      "dependencies": { // Dependency configuration
        "lib1": "2.0.0",
        "log4js": "2.0.0"
      },
      "devDependencies": {
      },
      "dynamicDependencies": {
      }
    }
    
-   When **ohpm i** is executed in the **entry** module, since there is a dependency on **libbase** and **libbase** has an **overrideDependencyMap** entry, the **dependencies**, **devDependencies**, and **dynamicDependencies** nodes of **libbase** are replaced with the ones defined in the **dep-debug.json5** file. As such, the **entry** module will have **libbase**, **lib1**, and **log4js** installed. This is different from the default behavior, which would only include **libbase** and its direct sub-dependency **lib1**.
-   The entry list result is as follows:
    
    entry 1.0.0 D:\\overrideDependencyMapTest\\entry
    └── libbase 1.0.0
        └── lib1 2.0.0
        └── log4js 2.0.0
    

#### ProjectPackageJson in the .ohpmrc File

Using the **projectPackageJson** configuration in the .ohpmrc file provides a way to override the project-level **oh-package.json5** configurations, including the **overrides** and **overrideDependencyMap** fields. The following are the details on how to use this configuration and its constraints:

-   Configuration format
    
    projectPackageJson:<project\_root>=<config\_path>, where projectPackageJson:<project\_root> is the key, and config\_path is the value. Set the key to the absolute path to the project's root directory, and set the value to the path to the JSON5 file that will override the configurations in the project-level **oh-package.json5** file.
    
-   Configuration example
    
    projectPackageJson:D:\\test\\TestProject=projectPackageJson.json5
    
-   Configuration restrictions
    
    -   The key must start with **projectPackageJson:**. **project\_root** indicates the absolute path to the project's root directory.
    
    -   The JSON5 file specified by the value can only contain configurations for **overrides** and **overrideDependencyMap**. It does not support **parameterFile**, which editors and compilers may not recognize.
    
    -   If there are multiple **projectPackageJson** configurations for the same **project\_root**, only the last one will take effect.
    
    -   The file path specified by the value can be either an absolute path or a relative path. If it is a relative path, it will be resolved starting from the project's root directory.

**Example**

This example demonstrates how to configure different environment settings for the same project using **projectPackageJson** in the .ohpmrc file. When these configurations take effect, they directly override the corresponding configurations in the project-level **oh-package.json5** file.

-   Add two configurations to the project-level or user-level .ohpmrc file, corresponding to the development and release environments:
    
    registry=http://localhost:8088/repos/ohpm
    log\_level=debug
    strict\_ssl=false
    projectPackageJson:D:\\overrideDependencyMapTest=oh-pkg-debug.json5 // Debug environment configuration
    projectPackageJson:D:\\overrideDependencyMapTest=oh-pkg-release.json5 // Release environment configuration; if multiple configurations exist for the same project, the last one will take effect by default.
    

-   In the **oh-pkg-release.json5** file, add an additional configuration for the **libbase** dependency:
    
    {
      "overrideDependencyMap": {
        "libbase": "D:\\\\overrideDependencyMapTest\\\\dep-release.json5"
      }
    }
    
-   Configure the **dep-release.json5** file, which is the dependency override file for **libbase** in the release environment, as follows:
    
    {
      "dependencies": {
        "lib1": "1.0.0",
        "lib2": "2.0.0",
        "lib3": "3.0.0"
      }
    }
    
-   Based on the [overrideDependencyMap scenario example](#section106151513236), execute **ohpm i** in the **entry** module. ohpm will modify the project-level **oh-package.json5** to:
    
    {
      "name": "overridedependencymaptest",
      "version": "1.0.0",
      "description": "Please describe the basic information.",
      "overrideDependencyMap": {
        "libbase": "D:\\\\overrideDependencyMapTest\\\\dep-release.json5"
      }
    }
    

-   The final installation result is as follows:
    
    entry 1.0.0 D:\\overrideDependencyMapTest\\entry
    └── libbase 1.0.0
        └── lib1 1.0.0
        └── lib2 2.0.0
        └── lib3 3.0.0
    

#### oh-package-lock.json5

The **oh-package-lock.json5** file is used to lock all dependent versions and cache metadata of the dependencies. You are not advised to manually modify the file content or use other analysis tools to directly read the file content.

Instead, commit the **oh-package-lock.json5** file to the code repository for version management. The benefits are as follows:

-   Reproduce the project build. The **oh-package-lock.json5** file records the exact dependency tree during third-party package installation, including the version of each dependency, sub-dependencies, and their versions. Committing the file to the code repository allows team members, continuous integration (CI) server users, or any other user who clones the project to obtain the same dependency version when running the **ohpm install** command, ensuring that the project can be reproduced.
-   Improve the installation speed. When installing dependencies, ohpm preferentially uses the version information locked by **oh-package-lock.json5** to avoid re-parsing dependency versions, effectively accelerating the installation process.
-   Enhance security. By locking dependency versions, **oh-package-lock.json5** prevents security vulnerabilities introduced by upstream dependency updates. If a dependency has a security problem, you can update the specific dependency version and commit the updated **oh-package-lock.json5** to the repository to ensure that all users obtain the updated version.
-   Facilitate collaboration: When team members add, update, or remove dependencies in a project, they should run **ohpm update** to update **oh-package-lock.json5**. Committing these changes to the repository enables other members to know the dependency changes and obtain the correct dependency version after pulling the latest code.
