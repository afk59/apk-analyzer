# Resource Missing Error Codes

#### 00304001 AppStartup Configuration File Does Not Exist

**Error Message**

Invalid configuration in the XXX module.json5.

**Symptom**

The **module.json5** configuration of module _XXX_ is invalid.

**Possible Causes**

The AppStartup configuration file specified by the **appStartup** field in **module.json5** does not exist.

**Solution**

Ensure that the AppStartup configuration file exists.

#### 00304002 Invalid Custom Resource Path in targets

**Error Message**

Invalid Targets resource XXX configuration.

**Symptom**

The custom resource directory specified in **targets** is invalid.

**Possible Causes**

-   The custom resource directory ends with a space.
-   The custom resource directory does not exist.

**Solution**

Ensure that the custom resource directory does not end with a space and the directory exists.

#### 00304003 File Specified by the main Field in oh-package.json5 Does Not Exist

**Error Message**

Invalid main file 'XXX' defined in file: YYY.

**Symptom**

The file corresponding to the path specified by the **main** field in **oh-package.json5** does not exist.

**Possible Causes**

The **main** field is set to a non-existent file path.

**Solution**

Check the **main** field in the **oh-package.json5** file of the _XXX_ module and ensure that the corresponding file exists.

#### 00304004 hvigor-config.json5 Does Not Exist

**Error Message**

Hvigor config file XXX does not exist.

**Symptom**

The **hvigor-config.json5** configuration file does not exist.

**Possible Causes**

The **hvigor-config.json5** configuration file does not exist.

**Solution**

Ensure that the **hvigor/hvigor-config.json5** file exists in the project root directory.

#### 00304005 worker File Does Not Exist

**Error Message**

Cannot find file by 'XXX' at file: YYY.

**Symptom**

The file corresponding to the path specified by the **workers** field in **build-profile.json5** does not exist.

**Possible Causes**

The **workers** field is set to a non-existent file path.

**Solution**

1.  Ensure that the path specified by the **workers** field exists.
2.  Remove the non-existent path from **workers**.

#### 00304007 types File Does Not Exist

**Error Message**

Can not find the custom type's declaration file: 'XXX' at file: YYY.

**Symptom**

The file corresponding to the path specified by the **types** field in **build-profile.json5** does not exist.

**Possible Causes**

The **types** field is set to a non-existent file path.

**Solution**

Ensure that the file corresponding to path specified by the **types** field exists.

#### 00304008 pages File Does Not Exist

**Error Message**

Forms referenced in the config: 'XXX', was not found in the project or the libraries.

**Symptom**

In an FA project, the file corresponding to path specified by the **pages** field in the **config.json** file does not exist.

**Possible Causes**

The **pages** field is set to a non-existent file path.

**Solution**

Ensure that the file corresponding to path specified by the **pages** field exists and remove the non-existent file path _XXX_ from **pages**.

#### 00304010 apPath Not Found

**Error Message**

The file corresponding to apPath at XXX under AoT's partial mode was not found in XXX.

**Symptom**

The file configured in **apPath** cannot be found.

**Possible Causes**

The file path may not exist.

**Solution**

Configure a valid path in **apPath**.

#### 00304011 HAP Not Found

**Error Message**

No HAP found for the APP.

**Symptom**

The HAP cannot be found.

**Possible Causes**

The mapping between targets and products is not configured in **build-profile.json5** or **hvigorconfig.ts**.

**Solution**

Configure at least one target with the specified product (using the **applyToProducts** field) in the project-level **build-profile.json5** or **hvigorconfig.ts file**.

#### 00304012 File Referenced by srcEntry Is Missing

**Error Message**

Module-srcEntry not found. At file: XXX.

**Symptom**

The file referenced by **srcEntry** is missing.

**Possible Causes**

1.  The file path is incorrect.
2.  The file in the path is missing.

**Solution**

Configure a correct path in **srcEntry** that points to an existing file.

#### 00304013 File or Directory Not Found

**Error Message**

Unable to find the file or directory for XXX using the relative path XXX. At file: XXX.

**Symptom**

The specified file or directory cannot be found using the relative path.

**Possible Causes**

The **runtimeOnly** configuration in the module-level **build-profile.json5** file is incorrect.

**Solution**

Configure a correct path in the **runtimeOnly** field that points to an existing file.

#### 00304014 Specified .json File Not Found

**Error Message**

Unable to find the 'XXX.json' file or invalid resource directory configuration. At file: XXX.

**Symptom**

The specified .json file cannot be found, or the resource directory configuration is invalid.

**Possible Causes**

1.  The default resource directory **src/main/resources** does not exist or the path is incorrect.
2.  The resource directory of the current target is incorrectly configured or not configured.

**Solution**

1.  Ensure that the default resource directory **src/main/resources** exists.
2.  If the resource directory can be customized, set a correct path that points to an existing file.

#### 00304015 File Referenced by the src Field Not Found

**Error Message**

Form referenced in the config XXX was not found in the project or the libraries. At file: YYY.

**Symptom**

The file referenced by the **src** field in the specified file cannot be found in the project or library.

**Possible Causes**

The path configured in the **src** field is incorrect or the referenced file is missing.

**Solution**

Configure a correct path in the **src** field that points to an existing file.

#### 00304016 Source File Is Missing

**Error Message**

Source: XXX not exists. At file: XXX.

**Symptom**

The source file is missing.

**Possible Causes**

The source file is missing.

**Solution**

Ensure that the source file exists.

#### 00304017 Page Source File Is Missing

**Error Message**

Unable to find the page source file XXX in XXX routerMap configuration. At file: XXX.

**Symptom**

The specified page source file cannot be found in the **routerMap** configuration.

**Possible Causes**

The file referenced by **pageSourceFile** in **routerMap** of the **module.json5** file is missing.

**Solution**

Ensure that the file referenced by **pageSourceFile** in **routerMap** exists.

#### 00304018 File Referenced by pkgContextInfoPath Is Missing

**Error Message**

The pkgContextInfoPath XXX is not available. At file: XXX.

**Symptom**

The path specified in **pkgContextInfoPath** is unavailable.

**Possible Causes**

The file referenced by **pkgContextInfoPath** is an intermediate file and does not exist.

**Solution**

Check whether the file referenced by **pkgContextInfoPath** exists. If not, [download DevEco Studio](https://developer.huawei.com/consumer/en/download/deveco-studio) again.

#### 00304019 Package Name Does Not Exist

**Error Message**

The pkgName XXX does not exist. At file: XXX.

**Symptom**

The specified package name does not exist.

**Possible Causes**

**pkgName** is not defined in the project, or defined in an invalid location.

**Solution**

Set the **PageSourceFile** field under **routerMap** in the **module.json5** file to a valid relative path starting with **src/**.

#### 00304020 Source Path Not Found

**Error Message**

Module-Abilities-srcPath XXX file YYY not found. At file: ZZZ.

**Symptom**

The file referenced by **srcPath** cannot be found in the specified file.

**Possible Causes**

The file referenced by **srcPath** is missing.

**Solution**

Ensure that the referenced file exists.

#### 00304021 JS Page File of the Module Not Found

**Error Message**

Module-js-page XXX file YYY not found. At file: ZZZ.

**Symptom**

The JS page file referenced by **page** cannot be found in the specified file.

**Possible Causes**

The JS page file referenced by **page** is missing.

**Solution**

Ensure that the referenced file exists.

#### 00304022 Module Page Not Found

**Error Message**

Module page XXX not found. At file: XXX.

**Symptom**

The specified module page file cannot be found.

**Possible Causes**

1.  The specified page .json file is missing.
2.  An incorrect resource path is configured. As a result, the corresponding module page cannot be found.

**Solution**

Ensure that the **/resources/base/profile/_XXX_.json** file exists and the path is correct.

#### 00304024 File Not Found or Not Executable

**Error Message**

Not an internal or external command, operable program, or batch file. At file: XXX.

**Symptom**

The file name is not recognized as an internal command, an external command, an operable program, or a batch file.

**Possible Causes**

1.  The file does not exist.
2.  The file exists but is not executable.

**Solution**

1.  Verify that the file exists at the specified path.
2.  Verify that the file is executable.

#### 00304025 oh-package.json5 File Is Missing

**Error Message**

The XXX file does not exist. At file: XXX.

**Symptom**

The **oh-package.json5** file is missing.

**Possible Causes**

The **oh-package.json5** file is missing.

**Solution**

Ensure that the **oh-package.json5** file exists.

#### 00304026 File Referenced by headerPath Is Missing

**Error Message**

The property of headerPath specifies directory XXX which doesn't exist. At file: YYY.

**Symptom**

The file referenced by **headerPath** is missing.

**Possible Causes**

The file referenced by **headerPath** is missing.

**Solution**

Ensure that the file referenced by **headerPath** in the specified file exists.

#### 00304027 Value of headerPath Is Not a Directory

**Error Message**

The property of headerPath specifies directory XXX is not directory. At file: YYY.

**Symptom**

The value of **headerPath** is not a directory.

**Possible Causes**

The value of **headerPath** is not a directory.

**Solution**

Ensure **headerPath** in the specified file points to an existing directory.

#### 00304028 Duplicate File Name

**Error Message**

The following path contains a file with the same name: XXX. At file: YYY and ZZZ.

**Symptom**

Files with the same name exist in the _YYY_ and _ZZZ_ directories.

**Possible Causes**

The **headerPath** field in the **build-profile.json5** file points to two files with the same name.

**Solution**

Ensure that the file names in the path specified by **headerPath** are unique.

#### 00304029 File Referenced by path in externalNativeOptions Is Missing

**Error Message**

The configured cmake script in externalNativeOptions/path does not exist. At file: XXX.

**Symptom**

The file referenced by **path** in **externalNativeOptions** is missing.

**Possible Causes**

The file referenced by **path** in **externalNativeOptions** is missing.

**Solution**

Ensure that the file referenced by **path** in **externalNativeOptions** in the specified file exists.

#### 00304030 Incorrect CMake Script Name

**Error Message**

Error cmake script name XXX, should be CMakeLists.txt. At file: XXX.

**Symptom**

The name of the CMake script is incorrect, which must be **CMakeLists.txt**.

**Possible Causes**

The name of the CMake script is incorrect, which must be **CMakeLists.txt**.

**Solution**

Name the CMake script to **CMakeLists.txt**.

#### 00304031 Signing Material Is Not a Directory

**Error Message**

Signing materials XXX is not a directory. At file: YYY.

**Symptom**

The signing material is not a directory.

**Possible Causes**

The signing material is not a directory.

**Solution**

Remove the **signingConfigs** field from the _YYY_ file and choose **File** > **Project Structure** > **Project** > **Signing Configs** to reconfigure signing.

#### 00304032 Signing Material Is an Empty Directory

**Error Message**

Signing materials XXX is an empty directory. At file: YYY.

**Symptom**

The signing material is an empty directory.

**Possible Causes**

The signing material is an empty directory.

**Solution**

Remove the **signingConfigs** field from the _YYY_ file and choose **File** > **Project Structure** > **Project** > **Signing Configs** to reconfigure signing.

#### 00304033 Signing Material Is Missing

**Error Message**

Can not find signing material XXX. At file: YYY.

**Symptom**

The signing material is missing.

**Possible Causes**

The signing material does not exist.

**Solution**

Remove the **signingConfigs** field from the _YYY_ file and choose **File** > **Project Structure** > **Project** > **Signing Configs** to reconfigure signing.

#### 00304035 Project-level build-profile.json5 File Is Missing

**Error Message**

Cannot find project build file.

**Symptom**

The project-level **build-profile.json5** file is missing.

**Possible Causes**

The **build-profile.json5** file is renamed or deleted by mistake.

**Solution**

Ensure that the project directory contains the **build-profile.json5** file.

#### 00304036 Obfuscation Rule File Not Found

**Error Message**

The obfuscation rule file XXX cannot be found in YYY.

**Symptom**

The specified obfuscation rule file is missing.

**Possible Causes**

The obfuscation rule file does not exist at the expected path.

**Solution**

1.  Ensure that the specified obfuscation rule file exists.
2.  Ensure that the rule file configured in the **files** field under **ruleOptions** in the module-level **build-profile.json5** file exists.

#### 00304037 HSP Module Not Found.

**Error Message**

Unable to find module XXX.

**Symptom**

The module cannot be found.

**Possible Causes**

The module name or module path is incorrect.

**Solution**

Ensure that the target module exists.

#### 00304047 Failed to Package the .tgz File

**Error Message**

XXX is not exist, Failed to pack the tgz package.

**Symptom**

The specified file or directory cannot be found, and the .tgz file cannot be packaged.

**Possible Causes**

The specified file or directory cannot be found, and the .tgz file cannot be packaged.

**Solution**

Check whether the file path is correct.

#### 00304048 File Referenced by transformLib Is Missing

**Error Message**

Invalid transformLib value, XXX is not exist.

**Symptom**

**transformLib** is set to an invalid value. The referenced file does not exist.

**Possible Causes**

**transformLib** is set to an invalid value.

**Solution**

Ensure the file path is correct and accessible.

#### 00304049 schema File Is Missing

**Error Message**

The schema file cannot be found.

**Symptom**

The schema file is missing.

**Possible Causes**

The SDK does not contain the schema file.

**Solution**

Check whether the file in the error message exists. If not, download [DevEco Studio](https://developer.huawei.com/consumer/en/download/deveco-studio) again.

#### 00304050 Invalid Module Configuration

**Error Message**

Invalid module model.

**Symptom**

The module configuration is invalid.

**Possible Causes**

An unknown error occurs when the FA model project loads the module.

**Solution**

Check whether the configured module name exists.

#### 00304051 Failed to Find the Node By Node Name

**Error Message**

node not found by node name: XXX.

**Symptom**

No node that matches the specified node name is found.

**Possible Causes**

The specified node name is not listed under the **modules** field in the project-level **build-profile.json5** file.

**Solution**

Ensure that the specified node name is listed under **modules** in the project-level **build-profile.json5** file.

#### 00304054 Schema for app.json5 Is Not Initialized

**Error Message**

app.json5 schemaPath not initialized.

**Symptom**

The schema of **app.json5** is not initialized.

**Possible Causes**

The build process was triggered before schema initialization for **app.json5**.

**Solution**

Choose **File** > **Sync and Refresh Project** to synchronize the project.

#### 00304055 Failed to Execute onDeviceTest

**Error Message**

The path XXX does not exist. Failed to execute the command 'onDeviceTest'.

**Symptom**

The **onDeviceTest** command fails to execute because a required file is missing.

**Possible Causes**

The required file does not exist in the module directory.

**Solution**

Ensure that the required file exists in the module directory.

#### 00304056 build-profile.json5 File Is Missing

**Error Message**

Can not find build config file build-profile.json5 at 'XXX'.

**Symptom**

The **build-profile.json5** file does not exist in the specified directory. As a result, the build fails.

**Possible Causes**

The module-level **build-profile.json5** file is missing.

**Solution**

Ensure that the **build-profile.json5** file exists.

#### 00304057 File Referenced by parameterFile Is Missing

**Error Message**

The parameterFile file 'XXX' configured at the project level does not exist. Check at file: YYY.

**Symptom**

The file referenced by **parameterFile** in the project-level **oh-package.json5** file is missing.

**Possible Causes**

**parameterFile** in the project-level **oh-package.json5** file is set to an incorrect path.

**Solution**

Check and correct the **parameterFile** configuration in the project-level **oh-package.json5** file and ensure that the referenced file exists in the specified directory.

#### 00304058 Invalid File referenced by parameterFile

**Error Message**

The parameterFile file 'XXX' is not a file. Check at file: YYY.

**Symptom**

The file referenced by **parameterFile** is invalid, causing parsing failure.

**Possible Causes**

The configured path points to a directory or a file in an invalid format.

**Solution**

Ensure that **parameterFile** is correctly configured in the **oh-package.json5** file, pointing to a readable file instead of a directory or a file in an invalid format.

#### 00304060 ohosTest Directory or Configuration File Not Found

**Error Message**

The ./XXX/src/main/ohosTest directory cannot be found, or the ./XXX/src/main/ohosTest/YYY file is missing.

**Symptom**

The **ohosTest** directory or the configuration file _YYY_ is missing.

**Possible Causes**

1.  The **ohosTest** directory was not created or the path is incorrect.
2.  The _YYY_ file is missing, resulting in incomplete **ohosTest** configuration.

**Solution**

Ensure that the specified module directory contains the **./_XXX_/src/main/ohosTest** folder, and that the _YYY_ file exists.

#### 00304061 ohosTest Path Not Found

**Error Message**

The path XXX does not exist, Failed to execute the command YYY.

**Symptom**

The specified path does not exist during ohos test coverage report generation, causing the command to fail.

**Possible Causes**

The target path was not created or is incorrectly configured.

**Solution**

Ensure that the target path exists.

#### 00304062 module.json5 File in the ohosTest Directory Is Missing

**Error Message**

The file XXX does not exist.

**Symptom**

The **module.json5** file is missing during ohos test coverage report generation.

**Possible Causes**

The **module.json5** file is missing from the **ohosTest** directory or has an incorrect path.

**Solution**

Ensure that the **module.json5** file exists at the specified path within the **ohosTest** directory.

#### 00304063 Local Dependency Configured in parameterFile Not Found

**Error Message**

Local dependency in parameterFile does not exist.

**Symptom**

The local dependency configured in **parameterFile** does not exist.

**Possible Causes**

The local dependency is incorrectly configured.

**Solution**

Verify the following:

1.  The local dependency path exists.
2.  File and directory names in the path comply with case sensitivity requirements.

#### 00304064 module.json5 File Not Found

**Error Message**

module.json5 file not found.

**Symptom**

The **module.json5** file is missing from the module directory.

**Possible Causes**

The module directory does not contain the **module.json5** file.

**Solution**

For a project developed in the stage model, make sure that the module directory contains the **module.json5** file.

#### 00304065 Profile File Not Found or Invalid Resource Directory Configuration

**Error Message**

Profile XXX not found or invalid resource directory configuration.

**Symptom**

The profile file cannot be found, or the resource directory configuration is invalid.

**Possible Causes**

1.  The profile file in the default resource directory **src/main/resources** does not exist.
2.  The profile file in the resource directory configured in **target** does not exist.

**Solution**

1.  Ensure that the profile file in the resource directory **src/main/resources** exists.
2.  If the resource directory is customized in **targets** in the module-level **build-profile.json5** file, ensure that the profile file in the directory exists.

#### 00304066 C++ Product File Does Not Exist

**Error Message**

Non-existent file XXX.

**Symptom**

The C++ product file does not exist.

**Possible Causes**

The target file pointed to by the C++ product's symbolic link is missing.

**Solution**

1.  Choose **Build** > **Clean Project** to delete the cache and rebuild the project. Check whether the file is generated.
2.  If the file cannot be generated, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 00304067 app.json5 File Not Found

**Error Message**

app.json5 file not found. At file: XXX.

**Symptom**

The **app.json5** file cannot be found.

**Possible Causes**

The **app.json5** file is missing.

**Solution**

Ensure that the **app.json5** file exists.
