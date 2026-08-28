# Configuration Error Codes

#### 00303002 Task Module Not Found

**Error Message**

Cannot find hvigor node in XXX with task YYY.

**Symptom**

The module _XXX_ of the task _YYY_ cannot be found.

**Possible Causes**

The module name is incorrect.

**Solution**

Correctly configure the module name in **hvigorfile.ts**.

#### 00303003 Module of a Dependent Task Not Found

**Error Message**

Cannot find dependent hvigor node XXX with task YYY.

**Symptom**

The module _XXX_ of the dependent task _YYY_ cannot be found.

**Possible Causes**

The module name is incorrect.

**Solution**

Correctly configure the module name in **hvigorfile.ts**.

#### 00303004 Dependency Task Not Found

**Error Message**

Cannot find hvigor task XXX in module YYY required by ZZZ.

**Symptom**

The task _XXX_ on which the task _ZZZ_ depends cannot be found.

**Possible Causes**

The dependent task name is incorrect.

**Solution**

Correctly configure the dependent task name in **hvigorfile.ts**.

#### 00303010 modules Field in Project-Level build-profile.json5 Must Be of the Array Type

**Error Message**

modules' property should be an array in root project build-profile.json5.

**Symptom**

The **modules** field in the project-level **build-profile.json5** file must be of the array type.

**Possible Causes**

The **modules** field is set to a non-array value in the project-level **build-profile.json5** file.

**Solution**

Set **modules** to a value of the array type.

#### 00303011 Modules Not Found

**Error Message**

No modules found.

**Symptom**

The module cannot be found.

**Possible Causes**

The modules specified in the **modules** configuration of the project-level **build-profile.json5** file are missing.

**Solution**

Correctly configure the **modules** field.

#### 00303012 Incorrect parameterFile Configuration

**Error Message**

XXX corresponding to the parameterFile is not find, Check the parameterFile is valid.

**Symptom**

The _XXX_ file corresponding to the path configured in **parameterFile** cannot be found. Check whether **parameterFile** is valid.

**Possible Causes**

**parameterFile** configured in the **oh-package.json5** file is incorrect.

**Solution**

1\. Correctly configure the [parameterFile](../../../../command-line-tools/using-ohpm/oh-package-json5/document.md#section122411462820) field in the project-level **oh-package.json5** file.

2\. Check the corresponding file of **parameterFile** to ensure that the file exists and is correctly named.

#### 00303013 Hvigor Only Available for API Version 8 and Later

**Error Message**

Hvigor only works with API version 8 and later versions.

**Symptom**

Hvigor is only available for API version 8 and later.

**Possible Causes**

The value of **compatibleSdkVersion** in the **oh-package.json5** file is less than 8.

**Solution**

Select an SDK of API version 8 or later to create a project.

#### 00303015 SDK Version Compatibility Rule Violation

**Error Message**

Configure the API version according to the rule of compatibleSdkVersion <= targetSdkVersion <= compileSdkVersion.

**Symptom**

The API version must be configured according to the rule "compatibleSdkVersion <= targetSdkVersion <= compileSdkVersion."

**Possible Causes**

The API version does not comply with the preceding rules.

**Solution**

Correctly configure the **compileSdkVersion**, **compatibleSdkVersion**, and **targetSdkVersion** fields in the project-level **build-profile.json5** file to ensure that the values comply with the preceding rules.

#### 00303017 Value of srcEntry or configEntry Must Be a Relative Path

**Error Message**

Invalid app startup configuration XXX in the module YYY: the value of 'srcEntry' or 'configEntry' should be a relative path. At file: ZZZ.

**Symptom**

The AppStartup configuration _XXX_ in module _YYY_ is incorrect. The value of **srcEntry** or **configEntry** must be a relative path.

**Possible Causes**

The value of **configEntry** in the _ZZZ_ file or the value of **srcEntry** under **startupTasks** is an absolute path.

**Solution**

Set **srcEntry** or **configEntry** to a relative path.

#### 00303018 Files Configured in srcEntry/configEntry Must Have .ets, .ts or .js Extensions

**Error Message**

Invalid app startup configuration XXX in the module YYY: the suffix of the code file specified by the field 'srcEntry' under 'startupTasks' and 'configEntry' should be ets,ts or js. At file: ZZZ.

**Symptom**

The AppStartup configuration _XXX_ in module _YYY_ is incorrect. The file name extensions of the code files configured in **srcEntry** and **configEntry** under **startupTasks** must be .ets, .ts, or .js.

**Possible Causes**

The files configured in the **srcEntry** or **configEntry** field under **startupTasks** of the _ZZZ_ file are not .ets, .ts, or .js files.

**Solution**

Configure **srcEntry** or **configEntry** correctly, ensuring that the corresponding files are .ets, .ts, or .js files.

#### 00303019 Files Specified by srcEntry or configEntry Must Be in the Current Module Directory

**Error Message**

Invalid app startup configuration XXX in the module YYY: the file of 'srcEntry' or 'configEntry' in startupTasks should be the module file where it is configuration. At file: ZZZ.

**Symptom**

The AppStartup configuration _XXX_ in module _YYY_ is incorrect. The files configured in **srcEntry** or **configEntry** must be in the current module directory.

**Possible Causes**

The files specified by the **configEntry** field in the _ZZZ_ file or the **srcEntry** field under **startupTasks** are not in the current module directory.

**Solution**

Configure **srcEntry** or **configEntry** correctly, ensuring that the files specified are in the current module directory.

#### 00303020 Files Configured in srcEntry/configEntry Must Exist

**Error Message**

Invalid app startup configuration XXX in the module YYY: the code file specified by the field 'srcEntry' or 'configEntry' in startupTasks must exist. At file: ZZZ.

**Symptom**

The AppStartup configuration _XXX_ in module _YYY_ is incorrect. The file configured in **srcEntry** or **configEntry** must exist.

**Possible Causes**

The files specified by the **configEntry** field in the _ZZZ_ file or the **srcEntry** field under **startupTasks** do not exist.

**Solution**

Configure **srcEntry** or **configEntry** correctly, ensuring that the specified files exist.

#### 00303021 Files Configured in srcEntry Under appPreloadHintStartupTasks Must Be .so Files

**Error Message**

Invalid app startup configuration XXX in the module YYY: the suffix of the code file specified by the field 'srcEntry' in appPreloadHintStartupTasks should be so. At file: ZZZ.

**Symptom**

The AppStartup configuration _XXX_ in module _YYY_ is incorrect. The file name extension of the files configured in **srcEntry** under **appPreloadHintStartupTasks** must be .so.

**Possible Causes**

The files configured in the **srcEntry** field under **appPreloadHintStartupTasks** of the _ZZZ_ file are not .so files.

**Solution**

Configure **srcEntry** correctly, ensuring that the corresponding files are .so files.

#### 00303022 name Must Be Unique

**Error Message**

Duplicate name 'XXX' exists in the 'YYY' attribute in the startup configuration file of the 'ZZZ' module.

**Symptom**

AppStartup configuration conflict: the elements under the _YYY_ attribute in module _ZZZ_ and its dependent modules have duplicate name _XXX_.

**Possible Causes**

The elements under **startupTasks** or **appPreloadHintStartupTasks** in the AppStartup configuration files of module _ZZZ_ and its dependent modules have duplicate name.

**Solution**

Configure unique **name** attribute values for elements under **startupTasks** or **appPreloadHintStartupTasks** in the AppStartup configuration files of module _ZZZ_ and its dependent modules.

#### 00303023 .so File Must Exist and Be Correctly Configured in the Dependency

**Error Message**

Invalid app startup configuration XXX in the module YYY: the .so file must exist and be correctly configured in the dependency. At file: ZZZ.

**Symptom**

The AppStartup configuration _XXX_ in module _YYY_ is incorrect. The .so file must exist and be correctly configured in the dependency.

**Possible Causes**

The .so file specified by **srcEntry** under **appPreloadHintStartupTasks** in the _ZZZ_ file does not exist or is not correctly configured in the dependency.

**Solution**

Correctly configure **srcEntry**, ensuring that the specified file exists and the dependency is correctly configured in the **oh-package.json5** file of the _YYY_ module.

#### 00303024 Project Structure and Configuration Need to Be Upgraded

**Error Message**

The project structure and configuration need to be upgraded before use.

**Symptom**

The project structure and configuration need to be upgraded.

**Possible Causes**

You have opened a historical project using DevEco Studio.

**Solution**

Migrate the historical project by referring to [Integrated Project Migration](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V14/ide-integrated-project-migration-V14).

#### 00303025 Incompatible modelVersion Type of Hvigor

**Error Message**

Incompatible types of hvigor modelVersion.

**Symptom**

The **modelVersion** type of Hvigor is incompatible.

**Possible Causes**

The value of **modelVersion** in **hvigor-config.json5** is not of the string type.

**Solution**

Change the value of **modelVersion** in **hvigor-config.json5** to a string.

#### 00303026 Incompatible modelVersion Type in oh-package.json5

**Error Message**

Incompatible types of oh-package.json5 modelVersion.

**Symptom**

The **modelVersion** type in **oh-package.json5** is incompatible.

**Possible Causes**

The value of **modelVersion** in **oh-package.json5** is not of the string type.

**Solution**

Change the value of **modelVersion** in **oh-package.json5** to a string.

#### 00303027 Inconsistent modelVersion Configurations in hvigor-config.json5 and oh-package.json5

**Error Message**

The modelVersion in hvigor-config.json5 is XXX,and the modelVersion in oh-package.json5 is YYY.

**Symptom**

**modelVersion** is set to _XXX_ in **hvigor-config.json5** and **modelVersion** is set to _YYY_ in **oh-package.json5**.

**Possible Causes**

The **modelVersion** values in the **hvigor-config.json5** and **oh-package.json5** files are inconsistent.

**Solution**

Set **modelVersion** in the **hvigor-config.json5** and project-level **oh-package.json5** files to the same value.

#### 00303028 Unsupported modelVersion Values Used for Hvigor

**Error Message**

Unsupported modelVersion of Hvigor XXX.

**Symptom**

**modelVersion** is set to an unsupported value.

**Possible Causes**

**modelVersion** is set to an unsupported value in **hvigor-config.json5**.

**Solution**

Set **modelVersion** to a supported value based on the error message.

#### 00303029 Unsupported modelVersion Values Used in oh-package.json5

**Error Message**

Unsupported modelVersion of oh-package.json5 XXX.

**Symptom**

**modelVersion** is set to an unsupported value.

**Possible Causes**

**modelVersion** is set to an unsupported value in **oh-package.json5**.

**Solution**

Set **modelVersion** to a supported value based on the error message.

#### 00303030 compileSdkVersion Unconfigured in product for an OpenHarmony Project

**Error Message**

For the OpenHarmony project, you need to configure the compileSdkVersion in the product, at file: %s.

**Symptom**

**compileSdkVersion** must be configured in **product** of an OpenHarmony project.

**Possible Causes**

**compileSdkVersion** is not configured in the project-level **build-profile.json5** file of an OpenHarmony project.

**Solution**

Configure **compileSdkVersion** in the project-level **build-profile.json5** file.

#### 00303031 Unsupported compileSdkVersion Values Used

**Error Message**

Unsupported compileSdkVersion XXX.

**Symptom**

The version set in **compileSdkVersion** is not supported.

**Possible Causes**

The version set in **compileSdkVersion** is not supported.

**Solution**

Set **compileSdkVersion** to a supported value based on the error message.

#### 00303032 Unsupported compatibleSdkVersion Values Used

**Error Message**

Unsupported compatibleSdkVersion XXX.

**Symptom**

The version set in **compatibleSdkVersion** is not supported.

**Possible Causes**

The version set in **compatibleSdkVersion** is not supported.

**Solution**

Set **compatibleSdkVersion** to a supported value based on the error message.

#### 00303033 compatibleSdkVersion Left Unconfigured

**Error Message**

Please configure compatibleSdkVersion in the product.

**Symptom**

**compatibleSdkVersion** is not configured in **product**.

**Possible Causes**

**compatibleSdkVersion** is not configured.

**Solution**

Configure the **compileSdkVersion** field in the project-level **build-profile.json5** file based on the error message.

#### 00303034 compileSdkVersion Left Unconfigured

**Error Message**

Please configure compileSdkVersion in the product.

**Symptom**

**compileSdkVersion** is not configured in **product**.

**Possible Causes**

**compileSdkVersion** is not configured when the runtime OS is OpenHarmony.

**Solution**

Configure the **compileSdkVersion** field in the project-level **build-profile.json5** file based on the error message.

#### 00303035 FA Model Projects Only Available for API Version 8 and Later

**Error Message**

According to the compatibility specifications, fa-model project can only support the development of API version 8 or later.

**Symptom**

According to the compatibility specifications, FA model projects support only API version 8 and later.

**Possible Causes**

**compatibleSdkVersion** in the FA model project is less than 8.

**Solution**

Set **compatibleSdkVersion** in project-level **build-profile.json5** to **8** or larger.

#### 00303036 Stage Model Projects Only Available for API Version 9 and Later

**Error Message**

According to the compatibility specifications,stage-model project can only support the development of API version 9 or later.

**Symptom**

According to the compatibility specifications, Stage model projects support only API version 9 and later.

**Possible Causes**

**compatibleSdkVersion** in the Stage model project is less than 9.

**Solution**

Set **compatibleSdkVersion** in project-level **build-profile.json5** to **9** or larger.

#### 00303037 API Version Incompatible with Device Version

**Error Message**

According to the compatibility specifications, apps of API version XXX or stage mode can only run on devices of API version XXX or later.

**Symptom**

According to the compatibility specifications, applications targeting API version _XXX_ or using the Stage model can only run on devices with API version _XXX_ or later.

**Possible Causes**

**compatibleSdkVersion** configured in project-level **build-profile.json5** is later than the device API version.

**Solution**

Upgrade the device API version to the same or a later version as **compatibleSdkVersion**, or set **compatibleSdkVersion** to the same version as the device API.

#### 00303038 Schema Verification Failed

**Error Message**

Schema validate failed.

**Symptom**

Schema verification failed.

**Possible Causes**

The **schema** configuration in the configuration file is incorrect.

**Solution**

Modify the **schema** configuration based on the error message in different scenarios.

#### 00303039 Duplicate Values of Name-related Fields

**Error Message**

Duplicated XXX: YYY.

**Symptom**

The name-related fields are assigned duplicate values.

**Possible Causes**

The name-related fields (such as **moduleName** and **targetName**) are assigned duplicate values.

**Solution**

Modify the name-related fields in the corresponding file based on the error message, ensuring that each name is unique.

#### 00303040 Product Named default Not Found

**Error Message**

Unable to find or load the default product.

**Symptom**

The product named **default** cannot be found or loaded.

**Possible Causes**

The product named **default** does not exist in the project.

**Solution**

Add the product named **default** to the corresponding file based on the error message.

#### 00303041 Standard- and Mini-System Devices Cannot Coexist

**Error Message**

It's not allowed to configure mini-system device when standard-system device exists.

**Symptom**

Mini-system devices cannot be configured when standard-system devices exist.

**Possible Causes**

Both standard-system devices and mini-system devices are configured.

**Solution**

Check whether abnormal device types exist based on the error message file.

#### 00303042 T Multiple Mini-System Devices Included

**Error Message**

The device types cannot include multiple mini-system devices.

**Symptom**

The device type cannot contain multiple mini-system devices.

**Possible Causes**

The device type contains multiple mini-system devices.

**Solution**

Configure only one mini-system device for device type based on the reported error message.

#### 00303043 Unsupported Mini-System Devices Configured for FA Model Projects

**Error Message**

Mini-system devices cannot be configured in an FA project.

**Symptom**

The FA model project does not support the configuration of mini-system devices.

**Possible Causes**

The mini-system device has been configured in the FA model project.

**Solution**

Remove mini-system devices from the configuration based on the reported error message.

#### 00303044 Only One Default Card Allowed in form\_config.json

**Error Message**

Only one default card can be configured in the form\_config.json file.

**Symptom**

Only one default card can be configured in the **form\_config.json** file.

**Possible Causes**

The **form\_config.json** file contains multiple cards with **isDefault** set to **true**.

**Solution**

Configure only one card with **isDefault** set to **true** in the **form\_config.json** file.

#### 00303045 updateDuration and scheduleUpdateTime Cannot Be Both Empty

**Error Message**

In the form\_config.json file, if the value of the updateEnabled field is true,the updateDuration and scheduleUpdateTime fields cannot be both empty.

**Symptom**

In the **form\_config.json** file, if **updateEnabled** is set to **true**, the **updateDuration** and **scheduleUpdateTime** fields cannot be empty at the same time.

**Possible Causes**

**updateEnabled** is set to **true** in the **form\_config.json** file, but **updateDuration** and **scheduleUpdateTime** are unconfigured.

**Solution**

If **updateEnabled** is set to **true**, configure the **updateDuration** or **scheduleUpdateTime** field.

#### 00303046 Invalid Key in parameterFile

**Error Message**

Invalid key: XXX in parameterFile.at YYY.

**Symptom**

The key _XXX_ in **parameterFile** in the _YYY_ directory is invalid.

**Possible Causes**

The corresponding key value does not exist in **parameterFile**.

**Solution**

Modify **@param:key** to ensure that the key value can be found in the corresponding **parameterFile**.

#### 00303047 key Configured in parameterFile Does Not Comply with the Verification Rule

**Error Message**

The key: XXX in parameterFile is invalid, only support at(@), slashe(/), letters, digits, dots(.), hyphens(-), and underscores(\_). For details, see the package name verification rules.

**Symptom**

The key _XXX_ in **parameterFile** is invalid. Only @, slash (/), letters, digits, periods (.), hyphens (-), and underscores (\_) are supported. For details, see the package name verification rules.

**Possible Causes**

**key** configured in **parameterFile** does not meet the verification rules.

**Solution**

Modify **key** in **parameterFile** based on the error message to ensure that the key complies with the verification rules.

#### 00303048 Version Configured in parameterFile Does Not Comply with the SemVer specification

**Error Message**

Invalid version: XXX in parameterFile, the version must comply with the semver specifications.

**Symptom**

The version _XXX_ configured in **parameterFile** is invalid. The version must comply with the [SemVer](https://semver.org/) specification.

**Possible Causes**

The version configured in **parameterFile** does not comply with the SemVer specification.

**Solution**

Correctly configure the version in **parameterFile** to make sure it complies with the SemVer specification.

#### 00303050 Invalid File Type for the main Field (.ets/.ts/.js Required)

**Error Message**

The value of 'main' must be a .ets, .ts, or .js file.

**Symptom**

The value of the **main** field must be a file with .ets, .ts, or .js extension.

**Possible Causes**

The **main** field is configured with a file whose file name extension is not .ets, .ts, or .js.

**Solution**

Check the **oh-package.json5** file of the module and correctly configure the **main** field.

#### 00303051 Invalid File Type for the workers Field (.ets/.ts/.js Required)

**Error Message**

Field 'workers' only accepts path ends with '.js', '.ts' or '.ets' but get: XXX.

**Symptom**

The value of the **workers** field must be a file with .ets, .ts, or .js extension.

**Possible Causes**

The **workers** field is configured with a file whose file name extension is not .ets, .ts, or .js.

**Solution**

Remove _XXX_ from **workers**.

#### 00303052 Lite Wearable Projects of API Version 9 or Later Support Only JS

**Error Message**

Lite-wearable devices with API version 9 or later support only JS.

**Symptom**

Lite wearable projects of API version 9 or later support only JS.

**Possible Causes**

The **ets** directory exists in **src/main** of the module.

**Solution**

Remove the **ets** directory from **src/main** of the module.

#### 00303053 Inconsistent Module Names Configured in build-profile.json5/hvigorconfig.ts and module.json5

**Error Message**

The module name XXX in build-profile.json5 or hvigorconfig.ts must be same as moduleName in module.json5.

**Symptom**

The module name in **build-profile.json5**/**hvigorconfig.ts** must be the same as that in **module.json5**.

**Possible Causes**

The value of **name** in **modules** of **build-profile.json5**/**hvigorconfig.ts** is inconsistent with that of **module.name** in **module.json5**.

**Solution**

Assign the same value to **name** in **modules** of **build-profile.json5**/**hvigorconfig.ts** and **module.name** in **module.json5**.

#### 00303054 The types Field Supported Only in ArkTS Projects

**Error Message**

Only ArkTS project supports custom types.

**Symptom**

The **types** field can be configured only in ArkTS projects.

**Possible Causes**

The **types** configuration is added to the JS module.

**Solution**

Switch to the ArkTS module.

#### 00303055 Files in the types Field Must Omit .d.ets or .d.ts Extensions

**Error Message**

The custom type's declaration file XXX does not require the suffix YYY.

**Symptom**

The file _XXX_ specified by the **types** field does not need the _YYY_ extension.

**Possible Causes**

The file specified by the **types** field has the .d.ets or .d.ts name extension.

**Solution**

Remove the extension .d.ets or .d.ts from the file specified by **types** field.

#### 00303056 Invalid File Extension of the types Field

**Error Message**

The suffix of custom type's declaration file 'XXX' is not valid.

**Symptom**

The file name extension _XXX_ of the **types** field is invalid.

**Possible Causes**

The **types** field is configured with a file whose file name extension is not .d.ets or .d.ts.

**Solution**

Configure the .d.ets or .d.ts files for the **types** field.

#### 00303057 dynamicDependencies Unsupported in FA Model Projects

**Error Message**

Current module XXX do not support dynamicDependencies.

**Symptom**

The _XX_ module does not support **dynamicDependencies**.

**Possible Causes**

The current project is an FA project, and **dynamicDependencies** is configured in **oh-package.json5**.

**Solution**

Migrate dependencies from **dynamicDependencies** to **dependencies** in the configuration file.

#### 00303058 Invalid Value of defaultDimension

**Error Message**

Invalid default dimension settings in these widgets: XXX.

**Symptom**

The value of **defaultDimension** is invalid.

**Possible Causes**

The value of **defaultDimension** is not within the range of **supportDimensions**.

**Solution**

Set **defaultDimension** to a value present in **supportDimensions**.

#### 00303059 Duplicate Permission Name

**Error Message**

Duplicate permission names detected under "XXX": "YYY".

**Symptom**

Duplicate permission name _YYY_ is detected in _XXX_.

**Possible Causes**

Multiple permissions with the same name are configured in _XXX_.

**Solution**

Remove duplicate permissions.

#### 00303060 Empty Intersection of SystemCapability Configurations for Multiple Devices

**Error Message**

The intersection of the system capability sets configured for multiple devices is empty.

**Symptom**

The intersection of SystemCapability sets configured for multiple devices is empty.

**Possible Causes**

This error occurs when the SystemCapabilities configured for device types under the **custom** and **general** fields in **syscap.json** have no common capabilities (that is, their intersection is empty).

**Solution**

Ensure that the intersection of SystemCapabilities defined for device types in both **custom** and **general** configurations of **syscap.json** is not empty.

#### 00303061 Invalid Custom SystemCapability

**Error Message**

The device type defined in the module.json5 of the module 'XXX' is empty, and the general and custom fields in the syscap.json file are not specified or their values are empty.

**Symptom**

The **deviceTypes** field in the **module.json5** file of the _XXX_ module is empty, and the **general** and **custom** fields in the **syscap.json** file are also empty.

**Possible Causes**

The **deviceTypes** field in the **module.json5** file of the _XXX_ module is empty, and the **general** and **custom** fields in the **syscap.json** file are also empty.

**Solution**

1.  Set **deviceTypes** in **module.json5**.
2.  Set **general** in **syscap.json**. The value must be the same as that of **deviceTypes**.

#### 00303062 Invalid deviceType of the Target

**Error Message**

Invalid target deviceType.

**Symptom**

**deviceType** of the target is invalid.

**Possible Causes**

The value of **deviceType** in **targets** of the **build-profile.json5** file is not defined in **deviceTypes** of the **module.json5** file.

**Solution**

Ensure that the value of **deviceType** in **targets** of the **build-profile.json5** file is defined in **deviceTypes** of the **module.json5** file.

#### 00303065 Inconsistent runtimeOS Configured in the Target and Product

**Error Message**

The runtimeOS configuration of the target XXX:YYY does not match the product ZZZ.

**Symptom**

**runtimeOS** of the target is different from that of the product.

**Possible Causes**

**runtimeOS** configured in the module-level **build-profile.json5** file is inconsistent with that in the project-level **build-profile.json5** file.

**Solution**

Ensure that **runtimeOS** in the project-level **build-profile.json5** file is the same as that in the module-level **build-profile.json5** file.

#### 00303071 Product Specified for a Target Does Not Exist

**Error Message**

Invalid product for target XXX.

**Symptom**

The product specified for the target does not exist.

**Possible Causes**

The **applyToProducts** field for a specific target in the project-level **build-profile.json5** file is configured with a non-existent product.

**Solution**

Correctly configure the **applyToProducts** field for the target in the project-level **build-profile.json5** file.

#### 00303072 Invalid Association of the ohosTest Target with a Product

**Error Message**

The 'ohosTest' target does not need to be packaged into the application. 'ohosTest' target cannot be applied to product.

**Symptom**

The **ohosTest** target is excluded from the app bundle and thus cannot be associated with a product.

**Possible Causes**

The project-level **build-profile.json5** file defines a target named **ohosTest** with **applyToProduct** set to **true**.

**Solution**

Remove the **ohosTest** target configuration from the project-level **build-profile.json5** file.

#### 00303073 Unknown Target

**Error Message**

Unknown target XXX.

**Symptom**

An undefined target is referenced.

**Possible Causes**

The target is not defined in the **build-profile.json5** file.

**Solution**

Define the target under the **targets** field in the module-level **build-profile.json5** file.

#### 00303074 Mismatched bundleName Between Project Configuration and Signing Material

**Error Message**

BundleName in the project configuration does not match that in the SigningConfigs.

**Symptom**

The **bundleName** configured in the project does not match that in the signing material.

**Possible Causes**

The **bundleName** used during signing material generation differs from that specified in the **app.json5** file or the project-level **build-profile.json5** file.

**Solution**

1.  If **bundleName** is configured in the project-level **build-profile.json5** file, ensure it matches **bundleName** in the signing material.
2.  If **bundleName** is not configured in the project-level **build-profile.json5** file, ensure **bundleName** in **app.json5** matches that in the signing material.

#### 00303075 version Field Must Be a String

**Error Message**

The version number of the module must be a string, but received a XXX.

**Symptom**

The **version** field must be a string, but is set to a value of the other type.

**Possible Causes**

The **version** field in **oh-package.json5** is not formatted as a string.

**Solution**

Set **version** to a value of the string type.

#### 00303076 name Field Must Be a String

**Error Message**

The name of the module must be a string, but received a XXX.

**Symptom**

The **name** field must be a string, but is set to a value of the other type.

**Possible Causes**

The **name** field in **oh-package.json5** is not formatted as a string.

**Solution**

Set **name** to a value of the string type.

#### 00303077 No Overlap in deviceType Configuration Between the Current Module and entryModules

**Error Message**

The deviceType values XXX of XXX in the XXX don't overlap that XXX of XXX in the associated XXX module.

**Symptom**

The **deviceType** configuration of the current module has no intersection with that of **entryModules**.

**Possible Causes**

In projects developed using the FA model, the **deviceType** configuration of the current module has no intersection with that of **entryModules**.

**Solution**

Modify the **deviceType** configuration of the current module to ensure at least one overlapping device type with the entry modules.

#### 00303078 Duplicate name Values in js and abilities of config.json

**Error Message**

Forms referenced in the config. In the configuration item named 'XXX', the type field does not match between 'module.abilities' and 'module.js'.

**Symptom**

Duplicate **name** values are not allowed between **abilities** and **js** configurations in the **config.json** file.

**Possible Causes**

In projects developed using the FA model, the **config.json** file contains identical **name** values in both **abilities** and **js**.

**Solution**

Ensure the **name** values in **abilities** and **js** are unique.

#### 00303082 Required SDK Not Found

**Error Message**

Unable to find the XXX in SDK Manager.

**Symptom**

The SDK corresponding to **compatibleSdkVersion**/**compileSdkVersion**/**targetSdkVersion** cannot be found.

**Possible Causes**

The Hvigor version does not match the SDK version.

**Solution**

1.  Since NEXT Developer Beta1, DevEco Studio offers an out-of-the-box development experience by packing the SDK, Node.js, Hvigor, ohpm, and other tools together, simplifying the installation and configuration process of DevEco Studio. It also provides capabilities for migrating historical projects, helping you quickly complete project conversion.
2.  [Download DevEco Studio tools](https://developer.huawei.com/consumer/en/download/).

#### 00303083 Incorrect SDK Version

**Error Message**

The platform version XXX and API version YYY of ZZZ in build-profile.json5 do not match.

**Symptom**

The value of **compatibleSdkVersion**, **compileSdkVersion**, or **targetSdkVersion** in **build-profile.json5** does not match the API version.

**Possible Causes**

The value of **compatibleSdkVersion**, **compileSdkVersion**, or **targetSdkVersion** in **build-profile.json5** does not match the API version.

**Solution**

During project creation, view all supported SDK versions by clicking the drop-down list box of **Compatible SDK** on the project configuration page.

#### 00303087 External Module Dynamic Import Not Allowed

**Error Message**

Invalid dynamic import configuration XXX in current module XXX.

**Symptom**

The dynamic import configuration in the current module is invalid.

**Possible Causes**

The dynamically imported file is not within the current module or other modules of the project.

**Solution**

Ensure the dynamically imported file path is within the current module or other project modules.

#### 00303088 Invalid File Extension for Dynamic Import

**Error Message**

Invalid file XXX found in the module XXX dynamic import files.

**Symptom**

The dynamically imported file must have the .ts or .ets extension.

**Possible Causes**

The extension of the dynamically imported file is not .ts or .ets.

**Solution**

Check the dynamically imported file and ensure that the extension is .ts or .ets.

#### 00303089 Cross-Module Dynamic Import Not Allowed

**Error Message**

Invalid dynamic import configuration XXX in module XXX.

**Symptom**

The dynamic import configuration in the module is invalid.

**Possible Causes**

When **noExternalImportByPath** is set to **true** in the project-level **build-profile.json5** file, **runtimeOnly** does not allow cross-module dynamic import.

**Solution**

1.  Ensure that the dynamically imported files are within the current module.
2.  If the cross-module import is required, adjust the **noExternalImportByPath** configuration.

#### 00303090 Invalid Dynamic Import Configuration

**Error Message**

Invalid dynamic import configurations in current module XXX.

**Symptom**

The dynamic import configuration in the current module is invalid.

**Possible Causes**

The dynamically imported file path is not defined in **dependencies** of **oh-package.json5**. The path of a file in a third-party package cannot be configured.

**Solution**

Ensure that all dynamically imported files or relative paths are defined in **dependencies** of **oh-package.json5**.

#### 00303091 Incorrect srcEntry Format

**Error Message**

Invalid configuration of XXX field.

**Symptom**

The **srcEntry** field is invalid.

**Possible Causes**

The **srcEntry** field in **module.json5** is not set to a relative path.

**Solution**

Ensure that the **srcEntry** field uses a relative path (for example, **./\*\***).

#### 00303092 Missing src Field in Card Configuration

**Error Message**

The required field form.src is missing.

**Symptom**

The required field **src** is missing.

**Possible Causes**

The card configuration file lacks the **src** field.

**Solution**

Ensure the card configuration file includes the **src** field.

#### 00303093 Invalid Path for form.src

**Error Message**

The value of form.src: XXX, is not under module YYY.

**Symptom**

The value of **form.src** is not within module _YYY_.

**Possible Causes**

The value of the **src** field in the card configuration file is not within module _YYY_.

**Solution**

Ensure that the value of the **src** field is within module _YYY_.

#### 00303094 mainElement Field Not Found

**Error Message**

The 'mainElement' field was not found in the module.json5 file.

**Symptom**

The **mainElement** field cannot be found in the **module.json5** file.

**Possible Causes**

The **module.json5** file of an atomic service project does not contain the **mainElement** field.

**Solution**

Ensure that the **module.json5** file of the atomic service project contains the **mainElement** field.

#### 00303096 Invalid Path in mock-config.json5

**Error Message**

XXX is a invalid path. At file: YYY.

**Symptom**

The path configured in the **mock-config.json5** file is invalid or does not exist.

**Possible Causes**

The path configured in the **mock-config.json5** file is invalid or does not exist.

**Solution**

Ensure all paths configured in **mock-config.json5** are correct and exist.

#### 00303098 Invalid configuration Field in app.json5

**Error Message**

Invalid configuration in the app.json5.

**Symptom**

The **configuration** field in the **app.json5** file is invalid.

**Possible Causes**

The path corresponding to the **configuration** field in **app.json5** does not exist.

**Solution**

Ensure that the file path corresponding to the **configuration** field exists.

#### 00303099 Path Does Not Exist

**Error Message**

Invalid configuration. The path of XXX does not exist. At file: YYY.

**Symptom**

The path corresponding to the _XXX_ field does not exist.

**Possible Causes**

The path corresponding to the _XXX_ field does not exist.

**Solution**

Ensure that the path corresponding to the _XXX_ field exists.

#### 00303100 Error in the general Field

**Error Message**

The value of general in the syscap.json file must be the same as that of XXX in the YYY file.

**Symptom**

The value of **general** in the **syscap.json** file must be the same as that of _XXX_ in the _YYY_ file.

**Possible Causes**

The field values in the two files do not match.

**Solution**

Ensure that the field values in the two files are consistent.

#### 00303101 Inconsistent Device Types Configured in the general Field

**Error Message**

Unable to find the general field or its value is invalid. At file: XXX.

**Symptom**

The **general** field is not configured, or the configured device types are inconsistent with those in **deviceTypes** of the module.

**Possible Causes**

The **general** field is not configured, or the configured device types are inconsistent with those in **deviceTypes** of the module.

**Solution**

Ensure that the field exists and the field value is consistent with the value of **deviceTypes**.

#### 00303104 Invalid Format of the pageSourceFile Field in routerMap

**Error Message**

Invalid pageSourceFile format in the XXX routerMap configuration. At file: XXX.

**Symptom**

The format of the **pageSourceFile** field in the **routerMap** configuration is invalid.

**Possible Causes**

The **pageSourceFile** field is not set to a path starting with **src/**.

**Solution**

Ensure that the **pageSourceFile** field is set to a relative path starting with **src/**.

#### 00303105 srcLanguage Field Not Defined

**Error Message**

Module-Abilities-srcLanguage in XXX is not defined. At file: YYY.

**Symptom**

The **Module-Abilities-srcLanguage** field is not defined.

**Possible Causes**

The **srcLanguage** tag is missing.

**Solution**

Ensure that the **Module-Abilities-srcLanguage** field in the _YYY_ file is defined.

#### 00303106 Signing Material Not Found in signingConfigs

**Error Message**

The material has not been configured in signingConfigs. At file: XXX.

**Symptom**

No signing material is found in **signingConfigs**.

**Possible Causes**

**material** is not configured in **signingConfigs** in the **build-profile.json5** file.

**Solution**

Ensure that **material** in the project-level **build-profile.json5** file has been configured.

#### 00303107 Invalid Signing Material

**Error Message**

Invalid XXX value. Make sure it is not null or empty. The file must be included in YYY.

**Symptom**

The value of _XXX_ in the signing material is an invalid file or folder.

**Possible Causes**

The _XXX_ field is not configured or the configured value is invalid.

**Solution**

Ensure that the _XXX_ field in the project-level **build-profile.json5** file has been configured. If the value of this field is a file path, ensure that the file path exists.

#### 00303108 Mismatch Between the type Field in signingConfigs and runtimeOS

**Error Message**

Signing configuration XXX does not apply to YYY.

**Symptom**

The signing configuration _XXX_ cannot be used in a project of the _YYY_ type.

**Possible Causes**

The **type** field in **signingConfigs** does not match **runtimeOS**.

**Solution**

Ensure that the **runtimeOS** field under **products** in **build-profile.json5** matches the **type** field under **signingConfigs**.

#### 00303110 pages Field Not Found

**Error Message**

Unable to replace pages. Cannot find moduleJsonObj.module.pages in module XXX.

**Symptom**

Failed to replace pages. The **pages** field does not exist in target module.

**Possible Causes**

The **pages** field is missing in the **module.json5** file of the module.

**Solution**

Ensure that the **module.json5** file contains the **pages** field.

#### 00303111 Invalid Value Type for buildProfileFields

**Error Message**

buildProfileFields only support number/string/boolean,not support XXX, the value YYY does not meet the requirements.

**Symptom**

The value of **buildProfileFields** can only be of the number, string, or Boolean type. The configured value does not meet the requirement.

**Possible Causes**

The value of **buildProfileFields** is not a number, string, or Boolean.

**Solution**

Ensure that the value of **buildProfileFields** meets the requirement.

#### 00303112 Bytecode HAR Not Supported When useNormalizedOHMUrl Is Not Set to true

**Error Message**

byteCodeHar not supported when useNormalizedOHMUrl is not true.

**Symptom**

When **useNormalizedOHMUrl** is not set to **true**, the bytecode HAR is not supported.

**Possible Causes**

When **useNormalizedOHMUrl** is not set to **true**, the bytecode HAR is not supported.

**Solution**

Check the **useNormalizedOHMUrl** field in the project-level **build-profile.json5** file.

#### 00303113 Empty path Field in externalNativeOptions

**Error Message**

The configured cmake script in externalNativeOptions/path cannot be empty. At file: XXX.

**Symptom**

The **path** field under **externalNativeOptions** cannot be empty.

**Possible Causes**

The **path** field under **externalNativeOptions** is empty.

**Solution**

Ensure that the value of **path** under **externalNativeOptions** in the module-level or project-level **build-profile.json5** file is valid.

#### 00303114 Unsupported armeabi-v7a in HarmonyOS Projects

**Error Message**

"armeabi-v7a" not supported for HarmonyOS. At file: XXX.

**Symptom**

HarmonyOS projects do not support **armeabi-v7a**.

**Possible Causes**

The **abiFilters** field is set to **armeabi-v7a** in the HarmonyOS project.

**Solution**

Ensure that [abiFilters](../../../configuring-your-build/configuring-for-c-builds/document.md#section0721057575) is set to a valid value.

#### 00303115 Only armeabi-v7a Configured for abiFilters in OpenHarmony Projects

**Error Message**

"armeabi-v7a" not supported for OpenHarmony as the only option. At file: XXX.

**Symptom**

**armeabi-v7a** cannot be the sole ABI configuration in an OpenHarmony project.

**Possible Causes**

In an OpenHarmony project, only **armeabi-v7a** is configured for the **abiFilters** field.

**Solution**

Add **arm64-v8a** or **x86\_64** to the **abiFilters** field.

#### 00303116 Invalid storePassword/keyPassword Length in Signing Material

**Error Message**

The length of the storePassword or keyPassword field in the signature configuration is less than 32. At file: XXX.

**Symptom**

The length of the **storePassword** or **keyPassword** field in the signing material cannot be less than 32.

**Possible Causes**

The length of the **storePassword** or **keyPassword** field in the signing material cannot be less than 32.

**Solution**

Remove the **signingConfigs** field from the _XXX_ file and choose **File** > **Project Structure** > **Project** > **Signing Configs** to reconfigure signing.

#### 00303117 Even Value Length of storePassword/keyPassword in Signing Material

**Error Message**

The length of the storePassword or keyPassword field in the signature configuration is an even number. At file: XXX.

**Symptom**

The value length of the **storePassword** or **keyPassword** field in the signing material is an even number.

**Possible Causes**

The value length of the **storePassword** or **keyPassword** field in the signing material is an even number.

**Solution**

Remove the **signingConfigs** field from the _XXX_ file and choose **File** > **Project Structure** > **Project** > **Signing Configs** to reconfigure signing.

#### 00303118 Signing Material Data Error

**Error Message**

Signing failed: Signing material data error!. At file: XXX.

**Symptom**

The signing material data is incorrect.

**Possible Causes**

The signing material is damaged.

**Solution**

Remove the **signingConfigs** field from the _XXX_ file and choose **File** > **Project Structure** > **Project** > **Signing Configs** to reconfigure signing.

#### 00303119 Invalid Signing Material

**Error Message**

Signing failed: Signing materials XXX is illegal!.At file: YYY.

**Symptom**

The signing material _XXX_ is invalid.

**Possible Causes**

The signing material is damaged.

**Solution**

Remove the **signingConfigs** field from the _YYY_ file and choose **File** > **Project Structure** > **Project** > **Signing Configs** to reconfigure signing.

#### 00303120 Signing Failed: The Signature Material Is Empty or Not a Folder

**Error Message**

Signing failed: signing material XXX is empty or not a directory.At file: YYY.

**Symptom**

The signing material _XXX_ is empty or not a folder.

**Possible Causes**

The signing material is empty or not a folder.

**Solution**

Remove the **signingConfigs** field from the _YYY_ file and choose **File** > **Project Structure** > **Project** > **Signing Configs** to reconfigure signing.

#### 00303121 Signing Material Error

**Error Message**

Signing failed: Signing material error. At file: XXX.

**Symptom**

The signing material is incorrect.

**Possible Causes**

The signing material is damaged.

**Solution**

Remove the **signingConfigs** field from the _XXX_ file and choose **File** > **Project Structure** > **Project** > **Signing Configs** to reconfigure signing.

#### 00303127 Invalid apPath Suffix

**Error Message**

The suffix of apPath at XXX is invalid.

**Symptom**

The path configured in **apPath** has an invalid suffix.

**Possible Causes**

The suffix of the path configured in **apPath** is not .ap.

**Solution**

Ensure that the suffix of the path configured in **apPath** is .ap.

#### 00303128 Unconfigured minAPIVersion Field

**Error Message**

The minAPIVersion was not configured. At file: XXX.

**Symptom**

The **minAPIVersion** field is not configured.

**Possible Causes**

The **minAPIVersion** field is missing.

**Solution**

Ensure that the **minAPIVersion** field exists in the _XXX_ file.

#### 00303130 Product Not Found

**Error Message**

Unable to find the product XXX for module YYY. At file: ZZZ.

**Symptom**

The product _XXX_ required by module _YYY_ cannot be found in the specified file.

**Possible Causes**

The **product** configuration is missing or incorrect in the project-level **build-profile.json5** file.

**Solution**

Check the project-level **build-profile.json5** file and ensure that **product** is correctly configured.

#### 00303136 Duplicate Plugin ID

**Error Message**

Plugin with ID XXX has been registered. Please check.

**Symptom**

The plugin ID is duplicated and already in use.

**Possible Causes**

The configured ID of the plugin is the same as that of another plugin.

**Solution**

Check the **hvigorfile.ts** file and ensure that the plugin IDs are unique.

#### 00303137 .npmrc File Missing in the User Directory

**Error Message**

The hvigor depends on the npmrc file. No npmrc file is matched in the current user folder. Configure the npmrc file first.

**Symptom**

The .npmrc file on which hvigor depends does not exist in the current user directory.

**Possible Causes**

The .npmrc file does not exist in the user directory.

**Solution**

Create the .npmrc file in the user directory and configure the following information:

registry=https://repo.huaweicloud.com/repository/npm/
@ohos:registry=https://repo.harmonyos.com/npm/

#### 00303138 Empty Module Name Not Allowed

**Error Message**

Error module name, can not be empty string!

**Symptom**

The module name cannot be an empty string.

**Possible Causes**

The module name in **hvigorfile.ts** is an empty string.

**Solution**

Check the **hvigorfile.ts** file and ensure that the module name is a non-empty string.

#### 00303139 hook Not Set to beforeNodeEvaluate or afterNodeEvaluate

**Error Message**

node Hook must be beforeNodeEvaluate or afterNodeEvaluate.

**Symptom**

**hook** is not set to **beforeNodeEvaluate** or **afterNodeEvaluate**.

**Possible Causes**

**hook** is not set to **beforeNodeEvaluate** or **afterNodeEvaluate**.

**Solution**

Set **hook** to either **beforeNodeEvaluate** or **afterNodeEvaluate**.

#### 00303140 Node Not Found

**Error Message**

Cannot find Node, at file:XXX.

**Symptom**

The node cannot be found by node name.

**Possible Causes**

The module name is incorrect.

**Solution**

Correctly configure the module name in the _XXX_ file.

#### 00303143 Task Not Found

**Error Message**

Can not find task XXX.At file:YYY.

**Symptom**

The task cannot be found by task name.

**Possible Causes**

The task name is misconfigured.

**Solution**

Correctly configure the module name in the _YYY_ file.

#### 00303144 Invalid Task Node Key

**Error Message**

XXX is not a valid task node key. The values of moduleName and taskName cannot contain ':'.

**Symptom**

_XXX_ is not a valid task node key. The values of **moduleName** and **taskName** cannot contain **':'**.

**Possible Causes**

The values of **moduleName** and **taskName** in **hvigorfile.ts** contain **':'**.

**Solution**

Ensure that the values of **moduleName** and **taskName** in **hvigorfile.ts** do not contain **':'**.

#### 00303145 Duplicate Task Name

**Error Message**

Duplicate task: XXX. Rename the task. At file: YYY.

**Symptom**

This task name already exists.

**Possible Causes**

The custom task name is the same as an existing task name.

**Solution**

Ensure that the custom task name is unique.

#### 00303146 Invalid version Format in oh-package.json5

**Error Message**

XXX file version format is not compliant, please check.

**Symptom**

The format of the **version** field in the _XXX_ file does not meet the requirements.

**Possible Causes**

The **version** field in the module-level **oh-package.json5** file violates the [SemVer](https://semver.org/) specification.

**Solution**

Correctly configure the **version** field according to the SemVer specification.

#### 00303147 Module Type Must Be shared When bundleType Is shared

**Error Message**

module type must be shared when bundleType is shared.module name : XXX.

**Symptom**

When **bundleType** is set to **shared**, the module type must be **shared**.

**Possible Causes**

**bundleType** is set to **shared** in **app.json5**, but **type** in **module.json5** of the _XXX_ module is not.

**Solution**

Use either of the following methods:

-   Set **type** in **module.json5** of the _XXX_ module to **shared**.
-   Set **bundleType** in **app.json5** to a value other than **shared**.

#### 00303148 hvigorfile.ts Not Found

**Error Message**

Hvigorfile not found: XXX.

**Symptom**

The **hvigorfile.ts** file cannot be found.

**Possible Causes**

The **hvigorfile.ts** file name is changed or the file is deleted.

**Solution**

Ensure that there is a **hvigorfile.ts** file under both the project and module directories.

#### 00303149 File Not Found by Path

**Error Message**

Path not found: XXX.

**Symptom**

The file cannot be found using the file path.

**Possible Causes**

The configured file path is incorrect.

**Solution**

Check the file path based on the error message.

#### 00303153 .json5 File Path Does Not Exist

**Error Message**

XXX is not exist.

**Symptom**

The .json5 file path does not exist.

**Possible Causes**

The file path is misspelled.

**Solution**

Configure a correct file path.

#### 00303155 Path Is Not a File Path

**Error Message**

the path: XXX is not a file path.

**Symptom**

The path _XXX_ is not a file path.

**Possible Causes**

_XXX_ is a folder.

**Solution**

Ensure that the file path is correct and exists.

#### 00303157 Duplicate Ability Name in config.json

**Error Message**

Check the ability name in the config.json file and make sure it is unique.

**Symptom**

Ensure all ability names in **config.json** are unique.

**Possible Causes**

The ability name is duplicated in the **config.json** file.

**Solution**

Ensure all ability names in **config.json** are unique.

#### 00303158 Duplicate Form Name in config.json

**Error Message**

Check the form name in the config.json file and make sure it is unique.

**Symptom**

The form name in **config.json** is not unique.

**Possible Causes**

The form name is duplicated in the **config.json** file.

**Solution**

Ensure the form name in **config.json** is unique.

#### 00303159 XXX File Modification Not Supported in Projects Developed Using the FA Model

**Error Message**

FA mode does not support modifying the XXX.

**Symptom**

The _XXX_ file of the FA model project cannot be modified.

**Possible Causes**

The _XXX_ file of the FA model project is modified.

**Solution**

Use the stage model instead.

#### 00303160 Only Relative Paths Allowed for Plugin Configuration

**Error Message**

Only relative path is allowed.

**Symptom**

Only relative paths are allowed.

**Possible Causes**

An absolute path is used for the plugin configuration in **hvigorfile.ts**.

**Solution**

Use a relative path for the plugin configuration in **hvigorfile.ts**.

#### 00303161 Plugin Path Does Not Exist

**Error Message**

plugin path XXX not exists.

**Symptom**

The configured plugin path does not exist.

**Possible Causes**

The path is misspelled.

**Solution**

Configure a correct plugin path.

#### 00303164 Invalid Extension of the Plugin File

**Error Message**

plugin file XXX must end with .ts.

**Symptom**

The plugin file name must end with .ts.

**Possible Causes**

The plugin file name does not end with .ts.

**Solution**

Ensure that the plugin file extension is .ts.

#### 00303166 Cyclic Dependency Exists in copyFrom

**Error Message**

buildOptionSet config buildOption: XXX copyFrom has circle.

**Symptom**

The path configured for **copyFrom** of the _XXX_ configuration under **buildOptionSet** has a cyclic dependency.

**Possible Causes**

The path configured for **copyFrom** of the _XXX_ configuration under **buildOptionSet** has a cyclic dependency.

**Solution**

Ensure that no cyclic dependency exists in the path configured for **copyFrom**.

#### 00303168 SDK Component Missing

**Error Message**

SDK component missing. Please verify the integrity of your SDK.

**Symptom**

The SDK component is missing.

**Possible Causes**

An incorrect SDK is configured.

**Solution**

-   Configure a correct SDK path: **$_DevEco Studio installation directory_****/sdk/default**.
-   [Download DevEco Studio](https://developer.huawei.com/consumer/en/download/) again.

#### 00303169 Target Not Found in the HAR Module

**Error Message**

Unable to find target 'XXX' in module 'YYY'. Make sure module 'YYY' has the same target as module 'ZZZ'.

**Symptom**

The target _XXX_ cannot be found in the _YYY_ module. Ensure that the _YYY_ module and _ZZZ_ module have the same target.

**Possible Causes**

The _ZZZ_ module depends on the _YYY_ module. When _ZZZ_ is compiled using commands, the target _XXX_ is specified for both _YYY_ and _ZZZ_. However, the target _XXX_ cannot be found in the _YYY_ module.

**Solution**

Ensure that the _YYY_ and _ZZZ_ modules have the same target _XXX_.

#### 00303170 Target Not Found in the HSP Module

**Error Message**

Unable to find target 'XXX' in module 'YYY'. Make sure module 'YYY' has the same target as module 'ZZZ'.

**Symptom**

The target _XXX_ cannot be found in the _YYY_ module. Ensure that the _YYY_ module and _ZZZ_ module have the same target.

**Possible Causes**

The _ZZZ_ module depends on the _YYY_ module. When _ZZZ_ is compiled using commands, the target _XXX_ is specified for both _YYY_ and _ZZZ_. However, the target _XXX_ cannot be found in the _YYY_ module.

**Solution**

Ensure that the _YYY_ and _ZZZ_ modules have the same target _XXX_.

#### 00303172 Value of transformLib Not Pointing to a File

**Error Message**

Invalid transformLib value XXX is not File.

**Symptom**

The value of **transformLib** is invalid since it does not point to an existing file.

**Possible Causes**

The file path configured for **transformLib** is incorrect.

**Solution**

Configure a correct file path for **transformLib**.

#### 00303173 Value of transformLib on Windows Not Pointing to a .dll File

**Error Message**

Invalid transformLib value, it requires a .dll file in Windows.

**Symptom**

The value of **transformLib** is invalid on Windows since it does not point to a .dll file.

**Possible Causes**

On Windows, the value of **transformLib** does not point to a .dll file.

**Solution**

Configure a file path that points to a .dll file for **transformLib**.

#### 00303179 Invalid metadata.resource Value Type

**Error Message**

metadata.resource must be string in file: XXX.

**Symptom**

The value of **metadata.resource** must be a string.

**Possible Causes**

**metadata.resource** is set to a value of another data type.

**Solution**

Configure a value of the string type for **metadata.resource**.

#### 00303181 Unresolvable Symbol Detected in metadata.resource

**Error Message**

Cannot resolve symbol metadata.resource. At file XXX.

**Symptom**

**metadata.resource** contains unresolved symbols.

**Possible Causes**

The file path configured for **metadata.resource** is incorrect.

**Solution**

Configure a correct and valid file path.

#### 00303183 Version Number Not of the String Type

**Error Message**

Invalid dependency: Version XXX is not a string.

**Symptom**

The provided version number is invalid.

**Possible Causes**

The version number in the **hvigorfile.ts** file is not a string.

**Solution**

Make sure the parameter passed to the **setVersion** API in the **hvigorfile.ts** file is a string.

#### 00303184 Dependency Value Not of the String Type

**Error Message**

Invalid dependency: DependencyVersion XXX is not a string.

**Symptom**

The provided dependency value is invalid.

**Possible Causes**

The dependency value in the **hvigorfile.ts** file is not a string.

**Solution**

Check the **hvigorfile.ts** file and ensure that the dependency value a string.

#### 00303185 Dynamic Addition or Deletion of products Not Allowed

**Error Message**

Cannot add or delete products, at file:XXX.

**Symptom**

The configured values in the **products** field cannot be added or deleted.

**Possible Causes**

The configured values in the **products** field are added to or deleted from the project-level **build-profile.json5** file using the **setBuildProfileOpt** API of the **hvigorfile.ts** plugin.

**Solution**

Check the **hvigorfile.ts** file and ensure that **products** is not added or deleted.

#### 00303186 Modification of name or runtimeOS under products Is Prohibited

**Error Message**

Cannot rename products or runtimeOS. Keep the name or runtimeOS XXX unchanged.

**Symptom**

**name** or **runtimeOS** under **products** cannot be modified.

**Possible Causes**

The **name** and **runtimeOS** fields under **products** in the project-level **build-profile.json5** file are modified using the **setBuildProfileOpt** API of the **hvigorfile.ts** plugin.

**Solution**

Check the **hvigorfile.ts** file and ensure that the **name** and **runtimeOS** fields under **products** are not modified.

#### 00303188 Invalid moduleType Configuration

**Error Message**

moduleType: XXX is an invalid value.

**Symptom**

**moduleType** is set to an invalid value.

**Possible Causes**

The **moduleType** field is misconfigured or misspelled.

**Solution**

Verify the value of the **type** field under **module** in the **module.json5** or **config.json** file. The valid values include **entry**, **feature**, **har**, and **shared**.

#### 00303189 Invalid runtimeOS Configuration

**Error Message**

runtimeOS: XXX is an invalid value. Please check it.

**Symptom**

**runtimeOS** is set to an invalid value.

**Possible Causes**

The **runtimeOS** field is misconfigured or misspelled.

**Solution**

Set **runtimeOS** to **OpenHarmony** or **HarmonyOS** in the **build-profile.json5** file.

#### 00303190 JS Component Missing for Page Ability

**Error Message**

A Page ability requires a JS component with the same name at XXX.

**Symptom**

A Page ability requires a JS component with the same name.

**Possible Causes**

The corresponding JS component is not defined in the **config.json** file, or the JS component name does not match the Page ability or contains a spelling error.

**Solution**

Ensure the **config.json** file includes a JS component with the same name as the Page ability.

#### 00303191 FA Model Ability Name Not Found

**Error Message**

Ability name XXX does not exist in config.json.

**Symptom**

Only abilities defined in the **config.json** file are allowed.

**Possible Causes**

The specified ability name is not defined in the **config.json** file or misspelled.

**Solution**

Ensure that the specified ability has been defined in the **config.json** file.

#### 00303192 entryModules Configuration Required for the Feature Module in FA Model Projects

**Error Message**

entryModules must be configured for a feature module in FA project.

**Symptom**

**entryModules** must be configured for the feature module of an FA model project.

**Possible Causes**

**entryModules** is not configured in the module-level **build-profile.json5** file.

**Solution**

Configure **entryModules** in the module-level **build-profile.json5** file.

#### 00303193 deviceType Configuration Required for Modules in FA Model Projects

**Error Message**

Unable to obtain the module deviceType.

**Symptom**

The **deviceType** configuration of the module cannot be obtained.

**Possible Causes**

The **config.json** file does not contain the **deviceType** field.

**Solution**

Ensure that the **config.json** file exists and is correctly formatted, with the **deviceType** field properly configured.

#### 00303194 deviceTypes Configuration Required for Modules in Stage Model Projects

**Error Message**

Unable to obtain the module deviceTypes.

**Symptom**

The **deviceTypes** configuration of the module cannot be obtained.

**Possible Causes**

The **module.json5** file does not contain the **deviceTypes** field.

**Solution**

Ensure that the **module.json5** file exists and is correctly formatted, with the **deviceTypes** field properly configured.

#### 00303195 Failed to Obtain the Module Information

**Error Message**

Unable to obtain the module information at file: XXX.

**Symptom**

The module information cannot be obtained from the **module.json5** file.

**Possible Causes**

The **module.json5** file does not contain the **module** field.

**Solution**

Correctly configure the **module** field in the **module.json5** file.

#### 00303196 Failed to Obtain the Module Type

**Error Message**

Unable to obtain the module type at file: XXX.

**Symptom**

The module type cannot be obtained.

**Possible Causes**

The **module.json5** file does not contain the **type** field.

**Solution**

Correctly configure the **module.type** field in the **module.json5** file.

#### 00303197 Missing or Invalid parameterFile Configuration

**Error Message**

Missing or invalid config of parameterFile in the project-level oh-package.json5 file. Check at file: XXX.

**Symptom**

The project-level **oh-package.json5** file does not contain a correctly configured **parameterFile** field.

**Possible Causes**

The **parameterFile** field is missing from the project-level **oh-package.json5** file or not correctly configured.

**Solution**

Add the [parameterFile](../../../../command-line-tools/using-ohpm/oh-package-json5/document.md#section122411462820) field to the project-level **oh-package.json5** file and ensure that the configuration is correct.

#### 00303198 build-profile.json5 File Violates the Schema Specification

**Error Message**

The project-level build-profile.json5 file does not comply with the schema.

**Symptom**

The project-level **build-profile.json5** file does not comply with the schema specification.

**Possible Causes**

1.  The **build-profile.json5** file is copied from another module, causing incompatible formats or fields.
2.  The **system** field in the module-level **hvigorfile.ts** file is incorrectly configured, for example, **appTasks**.

**Solution**

1.  Check the project-level **build-profile.json5** file and remove the fields that were directly copied from other modules, ensuring that all fields meet the schema specification.
2.  In the module-level **hvigorfile.ts** file, set the **system** field to **hapTasks**, **hspTasks**, or **harTasks** based on the module type.

#### 00303199 products Configuration Not Found in build-profile.json5

**Error Message**

No products found in the build-profile.json5 file. At file: XXX.

**Symptom**

The **products** configuration cannot be found in the **build-profile.json5** file.

**Possible Causes**

The **products** field is not defined in the **build-profile.json5** file.

**Solution**

Configure **products** in the project-level **build-profile.json5** file.

#### 00303200 Invalid Module Name

**Error Message**

Invalid module name settings in these modules: 'XXX'. Check whether the module is valid.

**Symptom**

The module name _XXX_ is invalid.

**Possible Causes**

The module names specified in the **modules** parameter of the **arkui-x-config.json5** file in the ArkUI-X project are incorrect.

**Solution**

Ensure that the module names specified in the **modules** parameter are correct.

#### 00303201 target Does Not Exist in the Module

**Error Message**

The module target XXX is not found in the YYY.

**Symptom**

The required target cannot be found in the specified module.

**Possible Causes**

The required target is not defined in the specified module.

**Solution**

Ensure **target** in the command line or in the **build-profile.json5** file of the module is correct.

#### 00303202 Entry Module Missing

**Error Message**

No available entry module found.

**Symptom**

No available entry module is found.

**Possible Causes**

1.  The module-level **build-profile.json5** file does not contain the **entryModules** configuration.
2.  The associated entry module is not correctly defined or is misspelled.

**Solution**

Ensure that **entryModules** exists and is correctly configured in the **build-profile.json5** file of the feature module.

#### 00303203 Build Mode in the Command Line Not Defined in buildModeSet

**Error Message**

Build mode XXX used in command line is not declared in buildModeSet in file: YYY.

**Symptom**

The build mode used in the command line is not defined in the **buildModeSet** field of the specified file.

**Possible Causes**

The build mode used is not defined in the project-level **build-profile.json5**.

**Solution**

Add the build mode used to the **buildModeSet** field in the project-level **build-profile.json5**.

#### 00303204 Build Mode in buildModeBinder Not Defined in buildModeSet

**Error Message**

Build mode XXX used in buildModeBinder is not declared in buildModeSet in file: YYY.

**Symptom**

The build mode used in **buildModeBinder** is not defined in the **buildModeSet** field of the specified file.

**Possible Causes**

The build mode used is not defined in the specified file.

**Solution**

Add the build mode used to the **buildModeSet** field in the specified file.

#### 00303205 target in buildModeBinder Not Defined

**Error Message**

Target XXX used in buildModeBinder is not declared in file: YYY.

**Symptom**

The target used in the **buildModeBinder** is not defined in the specified file.

**Possible Causes**

The target used is not defined in the specified file.

**Solution**

Add the target used to the **targets** field in the specified file.

#### 00303206 Build Options in buildModeBinder Not Defined

**Error Message**

Build option XXX used in buildModeBinder is not declared in file: YYY.

**Symptom**

The build option used in **buildModeBinder** is not defined in the **buildOptionSet** field of the specified file.

**Possible Causes**

The build option used is not defined in the specified file.

**Solution**

Add the build option used to the **buildOptionSet** field in the specified file.

#### 00303207 ArkUI-X SDK Directory Not Found

**Error Message**

Unable to find XXX in local.properties or YYY in the system environment path. Check at file: ZZZ.

**Symptom**

The path to the ArkUI-X SDK is not properly configured in **local.properties** or the system environment variables, preventing the SDK from being located.

**Possible Causes**

1.  The ArkUI-X SDK has not been downloaded.
2.  The SDK path is not configured or is configured incorrectly in the **local.properties** file.
3.  The environment variable _YYY_ is not set or points to an incorrect SDK path in the local system.

**Solution**

1.  Choose **File** > **Settings** > **ArkUI-X** (**DevEco Studio** > **Preferences/Settings** > **ArkUI-X** on macOS) to download the SDK.
2.  Configure the SDK path correctly in either **local.properties** or local system environment variables, ensuring the configured path matches the actual installation location of the SDK.

#### 00303208 SDK Directory Not Found

**Error Message**

Unable to find XXX in local.properties or YYY in the system environment path. Check at file: ZZZ.

**Symptom**

The system fails to find _XXX_, causing SDK configuration errors.

**Possible Causes**

1.  The _XXX_ configuration option is missing in the **local.properties** file.
2.  The environment variable _YYY_ is incorrectly set or has an invalid path.

**Solution**

1.  Ensure that the SDK path is correctly configured in **local.properties**. Run **hvigorw--stop-daemon** to stop the daemon process and try again.
2.  Add _YYY_ to the system environment variable path.

#### 00303209 Target Missing in the Entry Module of the FA Model

**Error Message**

Unable to find target 'YYY' in module 'XXX'.

**Symptom**

The required target is missing in the specified module.

**Possible Causes**

The required target is not correctly configured or is missing in the specified module.

**Solution**

Ensure that the entry module associated with the feature module of the FA model includes the corresponding target.

#### 00303210 Duplicate Arkdata JSON File Names

**Error Message**

The XXX file in the YYY module has the same name as the ZZZ file in the AAA module.

**Symptom**

The name of the _XXX_ file in the _YYY_ module is the same as that of the _ZZZ_ file in the _AAA_ module.

**Possible Causes**

An Arkdata JSON file with the same name exists in both the two modules.

**Solution**

Rename one of the files to avoid naming conflicts.

#### 00303211 ohosTest target Missing in the Module

**Error Message**

The module XXX does not exist ohosTest target, Failed to execute the command YYY.

**Symptom**

The **ohosTest target** is not defined for the specified module during ohos test coverage report generation, causing the **ohosTest** command to fail.

**Possible Causes**

**ohosTest target** is not configured in the module-level **build-profile.json5** file.

**Solution**

Check the **build-profile.json5** file of the specified module and ensure that the target named **ohosTest** exists.

#### 00303214 Target Device Type Mismatch

**Error Message**

The type of target device does not match the device type configured by module: XXX.Required device type:XXX, current module device type:XXX.

**Symptom**

The target device type specified in the command does not match the device type configured in the module.

**Possible Causes**

The device type specified in the **hvigorw** command is not defined in the **module.json5** or module-level **build-profile.json5** file, or the device type is incorrectly modified.

**Solution**

1.  Ensure that **deviceTypes** in **module.json5** of the module contains the required device type.
2.  If **deviceType** has been defined in the **targets** field in the module-level **build-profile.json5** file, ensure that **deviceType** contains the required device type.
3.  Ensure that the device type is not modified in the **hvigorfile.ts** or **hvigorconfig.ts** file.

#### 00303215 Dependency Name Mismatch with Package Name

**Error Message**

There are some dependency names that are inconsistent with the actual package names.

**Symptom**

Dependency names do not match their corresponding package names.

**Possible Causes**

The dependency names in configuration files do not match the actual package names.

**Solution**

Verify that the dependency names match the **name** field in **oh-package.json5** of the dependencies.

#### 00303216 Unidentifiable Format of the File Referenced by parameterFile

**Error Message**

Unrecognized archive format in parameterFile.

**Symptom**

The file referenced by **parameterFile** cannot be identified.

**Possible Causes**

The value of **parameterFile** references neither a directory nor a valid .har/.tgz file.

**Solution**

Ensure that the dependency configuration points to a directory or a .har/.tgz file.

#### 00303217 Invalid Environment Path

**Error Message**

Invalid value of 'XXX' in the system environment path.

**Symptom**

The specified value in the system environment variable is invalid.

**Possible Causes**

The specified value in the system environment path is incorrect.

**Solution**

Modify the specified value in the environment path, run the **hvigorw --stop-daemon** command, and try again.

#### 00303218 Required Attributes Unconfigured for user\_grant Permissions

**Error Message**

The reason and usedScene attributes are mandatory for user\_grant permissions.

**Symptom**

For user\_grant permissions, the **reason** and **usedScene** attributes are mandatory.

**Possible Causes**

The **reason** or **usedScene** field is not configured as expected for permissions of the user\_grant type in the **module.json5** file.

**Solution**

1.  For HAP modules, make sure both the **reason** and **usedScene** fields are configured under **requestPermissions** in the **module.json5** file.
2.  For HAR and HSP modules, make sure the **reason** field is configured under **requestPermissions** in the **module.json5** file.

#### 00303219 Duplicate routerMap Object Names

**Error Message**

Duplicate 'routerMap' object names detected.

**Symptom**

Duplicate **routerMap** object names exist.

**Possible Causes**

The **router\_map.json** file of the current module contains duplicate **routerMap** object names, either within the current module or between the current module and its dependent modules.

**Solution**

Make sure all **routerMap** objects in the **router\_map.json** file have unique names.

#### 00303220 Failed to Obtain the Module Type

**Error Message**

Failed to obtain the module type.

**Symptom**

Failed to obtain the module type.

**Possible Causes**

1.  The **config.json** file does not exist for projects developed using the FA model.
2.  In projects developed using the FA model, the **module/distro/moduleType** field in the **config.json** file is either missing or incorrectly configured.

**Solution**

1.  Ensure that the **config.json** file exists.
2.  Make sure the **config.json** file contains a correctly configured **module/distro/moduleType** field.

#### 00303221 Undefined Permission

**Error Message**

The XXX permission under requestPermissions must be a value that is predefined within the SDK or a custom one that you have included under definePermissions.

**Symptom**

The specified permission in **requestPermissions** is not predefined in the SDK or not declared in **definePermissions**.

**Possible Causes**

The permission name configured in **requestPermissions** in the **module.json5** file is invalid.

**Solution**

In the **module.json5** file, update the value of the **name** field under **requestPermissions** to a valid permission name, either predefined in the SDK or custom-defined under **definePermissions**.

#### 00303222 reason Attribute Unconfigured for user\_grant Permissions

**Error Message**

The reason attribute are mandatory for user\_grant permissions.

**Symptom**

For user\_grant permissions, the **reason** attribute is mandatory.

**Possible Causes**

The **reason** field is not configured as expected for permissions of the user\_grant type in the **module.json5** file.

**Solution**

1.  For HAP modules, make sure both the **reason** and **usedScene** fields are configured under **requestPermissions** in the **module.json5** file.
2.  For HAR and HSP modules, make sure the **reason** field is configured under **requestPermissions** in the **module.json5** file.

#### 00303223 metadata in FormExtensionAbility Left Empty or Set to an Empty Array

**Error Message**

The metadata field in FormExtensionAbility cannot be left blank or as an empty array.

**Symptom**

The **metadata** field in the FormExtensionAbility cannot be empty or an empty array.

**Possible Causes**

The **metadata** field in the ExtensionAbility of the form type in the **module.json5** file is either empty or set to an empty array.

**Solution**

Configure the [metadata](../../../../application-framework/form-kit/arkts-widget-development-recommended/configuring-arkts-widget-configuration-files/document.md) field in the ExtensionAbility of the form type in the **module.json5** file.

#### 00303224 ohos.extension.form Missing in metadata of the FormExtensionAbility

**Error Message**

In FormExtensionAbility, metadata must contain an object with its name set to 'ohos.extension.form' and resource set to a second-level resource reference.

**Symptom**

In the FormExtensionAbility, **metadata** must contain an object named **ohos.extension.form** with **resource** set to a second-level resource reference.

**Possible Causes**

The **metadata** field in the ExtensionAbility of the form type in the **module.json5** file either does not contain an object named **ohos.extension.form** or does not contain the **resource** field.

**Solution**

For the ExtensionAbility objects of the form type in the **module.json5** file, make sure the **metadata** field contains an object named **ohos.extension.form** with a valid **resource** field. For details about the configuration instructions, see [Configuring ArkTS Widget Configuration Files](../../../../application-framework/form-kit/arkts-widget-development-recommended/configuring-arkts-widget-configuration-files/document.md).

#### 00303225 Duplicate Module-Abilities Object Names

**Error Message**

Duplicate 'Module-Abilities' object names detected.

**Symptom**

The names of the Module-Abilities objects are duplicate.

**Possible Causes**

The **name** values of abilities or extensionAbilities objects conflict between the current module's **module.json5** file and the dependent HAR modules' **module.json5** file.

**Solution**

Ensure the uniqueness of **name** values of abilities and extensionAbilities objects in the current module's and dependent HAR modules' **module.json5** files.

#### 00303226 Invalid Form Name

**Error Message**

Invalid form name 'XXX'.

**Symptom**

The form name is invalid.

**Possible Causes**

The form name is not defined in the **form\_config.json** file.

**Solution**

Configure the form name in the **form\_config.json** file.

#### 00303227 string Property Missing

**Error Message**

File 'string.json' is missing the required property 'string'.

**Symptom**

The **string.json** file does not contain the required **string** property.

**Possible Causes**

The **string.json** file does not contain the required **string** property.

**Solution**

Make sure the **string.json** file contains the required **string** property.

#### 00303228 Tags Not Allowed in the version Field

**Error Message**

The 'tag' keyword is not allowed for 'version' at XXX.

**Symptom**

A tag is used in the **version** field of the **oh-package.json5** file.

**Possible Causes**

When the **version** field in the **oh-package.json5** file is configured via **parameterFile**, the **version** field must not contain a tag.

**Solution**

Locate the parameter in **parameterFile** that is referenced by the **version** field in **oh-package.json5** and ensure it contains no tag.

#### 00303229 name Attribute Missing

**Error Message**

The required attribute: module-name is missing.

**Symptom**

The required attribute **module-name** is missing.

**Possible Causes**

1.  The **name** field under **modules** is missing from the project-level **build-profile.json5** file.
2.  The **name** field is not set when the module is dynamically added to the **hvigorconfig.ts** file.

**Solution**

1.  Open the **build-profile.json5** file in the root directory of the project and ensure that the **name** field exists under **modules** and is not empty.
2.  Open the [hvigorconfig.ts](../../../overview/build-system-lifecycle/document.md#section810245135914) file in the root directory of the project and ensure that the **name** parameter of **includeNode** exists and is not empty.

#### 00303230 srcPath Attribute Missing

**Error Message**

The required attribute module-srcPath is missing.

**Symptom**

The required attribute **module-srcPath** is missing.

**Possible Causes**

1.  The **srcPath** field under **modules** is missing from the project-level **build-profile.json5** file.
2.  The **srcPath** field is not set when the module is dynamically added to the **hvigorconfig.ts** file.

**Solution**

1.  Open the **build-profile.json5** file in the root directory of the project and ensure that the **srcPath** field exists under **modules** and is not empty.
2.  Open the [hvigorconfig.ts](../../../overview/build-system-lifecycle/document.md#section810245135914) file in the root directory of the project and ensure that the **srcPath** parameter of **includeNode** exists and is not empty.

#### 00303231 srcPath Not a Relative Path

**Error Message**

The srcPath is not a relative path: XXX.

**Symptom**

The value of **srcPath** is not a relative path.

**Possible Causes**

The value of **srcPath** is not a relative path when the module is dynamically added to the **hvigorconfig.ts** file.

**Solution**

Open the [hvigorconfig.ts](../../../overview/build-system-lifecycle/document.md#section810245135914) file in the root directory of the project and ensure that the **srcPath** parameter of **includeNode** is a relative path.

#### 00303232 Module Not Found in the Task Dependency

**Error Message**

Failed to find the XXX node while setting the task dependencies in the YYY module's task: ZZZ.

**Symptom**

The module cannot be found in the task dependency.

**Possible Causes**

The module name configured in the task dependency is incorrect.

**Solution**

Check the **hvigorfile.ts** file and ensure that the module name in the task dependency is correctly configured.

#### 00303234 Path Not Found

**Error Message**

Path not found. At path: XXX.

**Symptom**

The specified path does not exist.

**Possible Causes**

An invalid or a misspelled path is configured.

**Solution**

Correct the path configuration according to the error message.

#### 00303236 Syntax Error Detected in hvigor-config.json5

**Error Message**

The error message is subject to the actual syntax error.

**Symptom**

The **hvigor-config.json5** file contains a syntax error.

**Possible Causes**

The **hvigor-config.json5** file contains a syntax error. For details, see the error message.

**Solution**

Rectify the syntax error in the **hvigor-config.json5** file based on the error message.

#### 00303237 Invalid Value Type of ohos.align.target in hvigor-config.json5

**Error Message**

The value of 'ohos.align.target' in hvigor-config.json5 must be a string.

**Symptom**

The value of **ohos.align.target** in the **hvigor-config.json5** file must be a string.

**Possible Causes**

The value of **ohos.align.target** in the **hvigor-config.json5** file is not a string.

**Solution**

Ensure that the value of **ohos.align.target** is a string.

#### 00303238 Invalid Ability Name

**Error Message**

Invalid ability name XXX. At file: YYY.

**Symptom**

The ability name is invalid.

**Possible Causes**

The **ability** configuration for the uiAbility object under the **insightIntents** field in the InsightIntent configuration file **insight\_intent.json** is invalid.

**Solution**

Ensure that the ability with a specific name is configured in the **abilities** field of the **module.json5** file.

#### 00303242 Signing Material Verification Failed

**Error Message**

Signature material verification failed, as: XXX.

**Symptom**

The signing material verification failed.

**Possible Causes**

The signing material is damaged.

**Solution**

Choose **File** > **Project Structure** > **Project** > **Signing Configs** to re-sign the project.

#### 00303243 Invalid Ability Name

**Error Message**

Invalid ability name XXX. At file: YYY.

**Symptom**

The ability name is invalid.

**Possible Causes**

The **ability** configuration for the serviceExtension object under the **insightIntents** field in the InsightIntent configuration file **insight\_intent.json** is invalid.

**Solution**

Ensure that the extension ability of the service type with a specific name exists under the **extensionAbilities** field in the **module.json5** file.

#### 00303244 Invalid Ability Name

**Error Message**

Invalid ability name XXX. At file: YYY.

**Symptom**

The ability name is invalid.

**Possible Causes**

The **ability** configuration for the form object under the **insightIntents** field in the InsightIntent configuration file **insight\_intent.json** is invalid.

**Solution**

Ensure that the extension ability of the form type with a specific name exists under the **extensionAbilities** field in the **module.json5** file.

#### 00303245 Invalid Ability Name

**Error Message**

Invalid ability name XXX. At file: YYY.

**Symptom**

The ability name is invalid.

**Possible Causes**

The **ability** configuration for the uiExtension object under the **insightIntents** field in the InsightIntent configuration file **insight\_intent.json** is invalid.

**Solution**

Ensure that the ability with a specific name is configured in the **abilities** or **extensionAbilities** field of the **module.json5** file.

#### 00303249 Circular Dependency Between Tasks

**Error Message**

Circular dependency between the following tasks.

**Symptom**

There is a circular dependency between tasks.

**Possible Causes**

The user configured dependencies for custom tasks, resulting in circular dependencies between tasks.

**Solution**

Remove the tasks that cause the circular dependency as prompted.

#### 00303250 preloadSystemSo Unsupported in FA Model Projects

**Error Message**

FA mode does not support 'preloadSystemSo'.

**Symptom**

The FA model project does not support **preloadSystemSo**.

**Possible Causes**

**preloadSystemSo** is set to **true** under **buildOption** in the project-level **build-profile.json5** file.

**Solution**

Remove **preloadSystemSo** or set **preloadSystemSo** to **false**.

#### 00303251 preloadSystemSo and ohos.arkCompile.singleFileEmit Enabled Simultaneously

**Error Message**

'ohos.arkCompile.singleFileEmit' does not support when 'preloadSystemSo' is set to true.

**Symptom**

**preloadSystemSo** and **ohos.arkCompile.singleFileEmit** cannot be enabled simultaneously.

**Possible Causes**

The **preloadSystemSo** in **build-profile.json5** is set to **true**, and the **ohos.arkCompile.singleFileEmit** in **hvigor-config.json5** is set to **true**.

**Solution**

-   Remove **ohos.arkCompile.singleFileEmit** or set **ohos.arkCompile.singleFileEmit** to **false**.
-   Remove **preloadSystemSo** or set **preloadSystemSo** to **false**.

#### 00303252 Module Not Found

**Error Message**

Referenced module XXX not found.

**Symptom**

The configured module cannot be found in the project.

**Possible Causes**

The module referenced via **formExtensionModule** or **formWidgetModule** does not exist.

**Solution**

Ensure that the module exists in the project.

#### 00303253 Incorrect Type of Module Referenced via formExtensionModule

**Error Message**

formExtensionModule can only reference entry or feature modules, but XXX is of type YYY.

**Symptom**

**formExtensionModule** must point to a feature module or an entry module, but the referenced module is of a different type.

**Possible Causes**

The module referenced via **formExtensionModule** is not a feature or an entry module.

**Solution**

Ensure that **formExtensionModule** points to an entry or a feature module.

#### 00303254 Incorrect Module Associated with the Standalone Widget Package

**Error Message**

Referenced module XXX must have formWidgetModule/formExtensionModule pointing back to YYY to establish a bidirectional reference.

**Symptom**

The **formWidgetModule**/**formExtensionModule** field of module _XXX_ must point to module _YYY_ to ensure bidirectional association between the two modules.

**Possible Causes**

The **formWidgetModule**/**formExtensionModule** field does not point to module _XXX_ or _YYY_.

**Solution**

1.  Ensure that the **formWidgetModule**/**formExtensionModule** field of module _XXX_ points to module _YYY_.
2.  Ensure that the **formWidgetModule**/**formExtensionModule** field of module _YYY_ points to module _XXX_.

#### 00303255 Embedded Widgets and Standalone Widget Packages Cannot Coexist

**Error Message**

Embedded widgets and standalone widgets must not be used together.

**Symptom**

Embedded widgets and standalone widget packages cannot coexist.

**Possible Causes**

When the standalone widget package is used, the **form\_config.json** file exists in both the entry module of the app package and the library module of the widget package.

**Solution**

Remove the standalone widget package or the embedded widget.

#### 00303256 Library Module of the Standalone Widget Package Can Only Depend on HAR Modules

**Error Message**

When a module is a standalone widget, all of its dependencies must be HAR modules.

**Symptom**

The library module of the standalone widget package can only depend on HAR modules.

**Possible Causes**

The library module of the standalone widget package is configured to depend on an HSP module in the **oh-package.json5** file.

**Solution**

Remove the HSP dependency of the library module of the standalone widget package from the **oh-package.json5** file.

#### 00303257 Incorrect deliveryWithInstall Configuration

**Error Message**

Field deliveryWithInstall was not set to true.

**Symptom**

**deliveryWithInstall** is not set to **true**.

**Possible Causes**

**deliveryWithInstall** is not set to **true**.

**Solution**

Set the **deliveryWithInstall** field to **true** in the **module.json5** file of both the main application module (entry) and the widget-providing library module within the standalone widget package.

#### 00303258 Standalone Widget Packages Unsupported in Projects with API Version Lower Than 20

**Error Message**

Standalone widgets are not supported on API versions earlier than 20. Set compatibleSdkVersion to 6.0.0(20) or higher in the project-level build-profile.json5 file.

**Symptom**

Standalone widget packages cannot be used in projects with API version lower than 20.

**Possible Causes**

**compatibleSdkVersion** of the project using the standalone widget package is lower than 6.0.0(20).

**Solution**

Set **compatibleSdkVersion** in the project-level **build-profile.json5** file to **6.0.0(20)** or later.

#### 00303259 Incorrect Type of Module Referenced via formWidgetModule

**Error Message**

formWidgetModule can only reference a hsp module, but XXX is of type YYY.

**Symptom**

**formWidgetModule** must point to an HSP module, but the referenced module is of a different type.

**Possible Causes**

The module referenced via **formWidgetModule** is not an HSP module.

**Solution**

Ensure that **formWidgetModule** points to an HSP module.

#### 00303260 Duplicate URIs in Merged Shared Configuration Files

**Error Message**

Duplicate 'crossAppSharedConfig' object uris detected.

**Symptom**

There are duplicate URIs in the **crossAppSharedConfig** object of the merged shared configuration files from different modules.

**Possible Causes**

Duplicate URIs exist in the shared configuration files of the current module and its dependent modules.

**Solution**

Modify the URI to ensure its uniqueness.

#### 00303261 Duplicate URIs in the Merged Shared Configuration File of the Current Module

**Error Message**

Duplicate uri exists in the crossAppSharedConfig configuration file of the current module.

**Symptom**

There are duplicate URIs in the **crossAppSharedConfig** object of the shared configuration file of the current module.

**Possible Causes**

Duplicate URIs exist in the **crossAppSharedConfig** object of the shared configuration file.

**Solution**

Modify the URI to ensure its uniqueness.

#### 00303262 expandImportPath Unsupported in FA Model Projects

**Error Message**

FA mode does not support 'expandImportPath'.

**Symptom**

The FA model project does not support **expandImportPath**.

**Possible Causes**

**expandImportPath** is configured in the **build-profile.json5** file.

**Solution**

Remove **expandImportPath**.

#### 00303263 Invalid expandImportPath.exclude Configuration

**Error Message**

Dependency names: '\[XXX\]' configured in 'expandImportPath.exclude' are prohibited in current module.

**Symptom**

Configuring dependency XXX in **expandImportPath.exclude** is not allowed.

**Possible Causes**

The dependency referenced by the alias configured in **expandImportPath.exclude** of **build-profile.json5** is not a local HAR module.

**Solution**

Remove the dependency alias _XXX_ from **expandImportPath.exclude**.

#### 00303265 Invalid sourceRoots File Path

**Error Message**

Invalid value 'XXX' in module 'YYY'. At file: 'ZZZ'.

**Symptom**

The **sourceRoots** configuration of module _YYY_ is invalid.

**Possible Causes**

**sourceRoots** is set to an invalid value in **build-profile.json5** of module _YYY_.

**Solution**

Ensure that all paths configured in the **sourceRoots** field meet the following requirements:

1.  All paths exist and are unique.
2.  All paths are relative paths.
3.  All paths are under the module and are directories.

#### 00303267 Product Not Found

**Error Message**

Can not find product XXX. At File: YYY.

**Symptom**

The specified product cannot be found.

**Possible Causes**

The product specified in the compilation command is not found in the project-level **build-profile.json5** file.

**Solution**

Modify the compilation parameters and use the correct product.

#### 00303268 HAR Package That hspA and hspB Depend on Missing from HAP Dependencies

**Error Message**

${har}: the common dependency of ${hspA} and ${hspB} must be declared in dependencies of ${hap}.

**Symptom**

The HAR package that both hspA and hspB depend on is not added to the HAP's dependencies.

**Possible Causes**

The HAR package is missing from the HAP's dependencies.

**Solution**

Add the HAR package to the HAP's dependencies.

#### 00303269 Unsupported deduplicateHar for FA Model Projects

**Error Message**

The FA model does not support the 'deduplicateHar' field. At file: XXX.

**Symptom**

The FA model project does not support the **deduplicateHar** configuration.

**Possible Causes**

The current project uses the FA model.

**Solution**

Remove the **deduplicateHar** field or set it to **false**.

#### 00303270 Incompatible SDK Version for deduplicateHar

**Error Message**

'deduplicateHar' can be enabled only when 'compatibleSdkVersion' is greater than or equal to 21. At file: XXX.

**Symptom**

Enabling **deduplicateHar** requires **compatibleSdkVersion** to be at least 21.

**Possible Causes**

The value of **compatibleSdkVersion** in the project-level **build-profile.json5** file is less than 21.

**Solution**

Set **compatibleSdkVersion** to a value greater than or equal to 21, or set **deduplicateHar** to **false**.

#### 00303271 Invalid idDefinedFilePath Configuration

**Error Message**

'idDefinedFilePath': XXX must be an existing json5 file. At file: YYY.

**Symptom**

The specified **idDefinedFilePath** does not point to a valid .json5 file.

**Possible Causes**

The configured path does not exist or the referenced file is not in JSON5 format.

**Solution**

Ensure that the path configured in **idDefinedFilePath** points to an existing .json5 file.

#### 00303272 Missing idDefinedFilePath for deduplicateHar

**Error Message**

When 'deduplicateHar' is enabled, the 'idDefinedFilePath' field must be configured. At file: XXX.

**Symptom**

**idDefinedFilePath** is mandatory when **deduplicateHar** is set to **true**.

**Possible Causes**

The **idDefinedFilePath** field is missing from the configuration.

**Solution**

Add the **idDefinedFilePath** field under **buildOption** or **resOptions**.

#### 00303273 Multiple HAPs Not Supported for One Project with deduplicateHar

**Error Message**

The 'deduplicateHar' field supports only one HAP per product. Now there are XXX haps: YYY in product ZZZ

**Symptom**

The **deduplicateHar** feature cannot be used in products containing multiple HAPs.

**Possible Causes**

The product contains multiple HAPs.

**Solution**

Ensure that each product contains only one HAP.

#### 00303274 Conflict Between deduplicateHar and libIsolation

**Error Message**

When 'deduplicateHar' is enabled, the 'libIsolation' field cannot be set to true. At file: XXX.

**Symptom**

When **deduplicateHar** is set to **true**, **libIsolation** cannot be set to **true**.

**Possible Causes**

Both **deduplicateHar** and **libIsolation** are set to **true**.

**Solution**

Set **libIsolation** to **false**.

#### 00303275 Missing useNormalizedOHMUrl Configuration for deduplicateHar

**Error Message**

When 'deduplicateHar' is enabled, the 'useNormalizedOHMUrl' field must be set to true. At file: XXX.

**Symptom**

When **deduplicateHar** is set to **true**, **useNormalizedOHMUrl** must be set to **true**.

**Possible Causes**

**useNormalizedOHMUrl** is not set to **true**.

**Solution**

Set **useNormalizedOHMUrl** to **true**.

#### 00303276 Current Module Must Be a Bytecode HAR During Customized HAR Builds

**Error Message**

The har module must be set to byte code har when building customized har. At file: XXX.

**Symptom**

The current HAR module is not configured as a bytecode HAR, which is required for building a customized HAR.

**Possible Causes**

The customized HAR build is enabled in the HAR module's configuration (**buildOption** > **packingOptions.customizedOptions.basePackage**), but the current module is not set to the bytecode HAR type.

**Solution**

Configure the current HAR module as a [bytecode HAR](../../../configuring-your-build/building-a-har/document.md#section16598338112415).

#### 00303277 ohos.compile.lib.entryfile Cannot Be Set to true During Customized HAR Builds

**Error Message**

ohos.compile.lib.entryfile must not set to true when building customized har. At file: XXX.

**Symptom**

**ohos.compile.lib.entryfile** is set to **true**, which is not allowed for customized HAR builds.

**Possible Causes**

The customized HAR build is enabled in the HAR module's configuration (**packingOptions.customizedOptions.basePackage**), but **ohos.compile.lib.entryfile** in **hvigor-config.json5** is set to **true**.

**Solution**

Set **ohos.compile.lib.entryfile** to **false** or delete the configuration item.

#### 00303278 Unable to Obtain the Plugin from hvigorfile.ts of the Module

**Error Message**

Unable to get plugin in hvigorfile.ts of module 'XXX'. At file: YYY.

**Symptom**

The plugin cannot be obtained from the module's **hvigorfile.ts** file.

**Possible Causes**

1.  The **hvigorfile.ts** file uses undefined properties or methods.
2.  The **system** field value of the **default** object exported from the **hvigorfile.ts** file of the module does not match the **type** field value configured in the **module.json5** file of the module.

**Solution**

1.  Check and correct any use of undefined properties or methods in the **hvigorfile.ts** file of the module.
2.  Ensure that the **system** field value of the **default** object exported from the **hvigorfile.ts** file matches the **type** field value configured in the **module.json5** file. The following table shows the matching rules.
    
    | 
    type
    
     | 
    
    system
    
     |
    | :-- | :-- |
    | 
    
    entry
    
     | 
    
    hapTasks
    
     |
    | 
    
    feature
    
     | 
    
    hapTasks
    
     |
    | 
    
    shared
    
     | 
    
    hspTasks
    
     |
    | 
    
    har
    
     | 
    
    harTasks
    
     |
