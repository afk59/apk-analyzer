# Script Error Codes

#### 00302001 Unit Tests Not Supported in the FA Model

**Error Message**

FA mode does not support unit test.

**Symptom**

The FA model does not support unit tests.

**Possible Causes**

Unit tests are executed using commands in the FA model project.

**Solution**

Do not perform unit tests on FA model projects.

#### 00302002 Failed to Find the Plug-in During Module Initialization

**Error Message**

The XXX plugin was not found when initializing the YYY module

**Symptom**

The _XXX_ plug-in cannot be found during module initialization.

**Possible Causes**

The **module.type** field in the **module.json5** file is inconsistent with the system plug-in exported from the **hvigorfile.ts** file.

**Solution**

Ensure that the value of **module.type** in the **module.json5** file of the module is the same as the system plug-in exported from the **hvigorfile.ts** file.

#### 00302013 Root Node Not Ready for Build

**Error Message**

The root node is not yet available for build.

**Symptom**

The root node is not ready for build.

**Possible Causes**

The API is called in **hvigorconfig.ts**. The execution time of this file is earlier than that of **nodesInitialized**. As a result, the API fails to be called.

**Solution**

When calling the API in **hvigorfile.ts**, make sure that the execution sequence complies with [Hvigor lifecycle execution sequence](../../../overview/build-system-lifecycle/document.md#section746253616316).

#### 00302014 hvigorConfig Not Ready for Build

**Error Message**

The hvigorConfig is not yet available for build.

**Symptom**

**hvigorConfig** is not ready for build.

**Possible Causes**

Unknown.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei technical support will get back to you as soon as possible.

#### 00302015 An Exception Occurs When the Internal hook Function Is Called.

**Error Message**

XXX in hvigorfile at XXX.

**Symptom**

An exception occurs when the internal **hook** function is called.

**Possible Causes**

An exception occurs when the **hook** function in the node is executed.

**Solution**

Call the API correctly by referring to the [extended API document](../../../expanding-build-capabilities/using-apis-for-extending-your-build/document.md).

#### 00302016 Lack of System Plugins in hvigorfile.ts of the Stage Model Project

**Error Message**

Invalid exports, no system plugins were found in hvigorfile: XXX.

**Symptom**

Export failed. No system plug-ins are found in **hvigorfile**.

**Possible Causes**

1.  The **system** field is missing in **hvigorfile.ts**.
2.  **appTasks**, **hapTasks**, **hspTasks**, or **harTasks** used in **hvigorfile.ts** does not exist.
3.  The **hvigorfile.ts** file does not use **export default** for its export.

**Solution**

1.  Ensure that the **system** field exists in **hvigorfile.ts**.
2.  Verify that the project-level **hvigorfile.ts** uses **appTasks**, and the module-level **hvigorfile.ts** uses **hapTasks**, **hspTasks**, or **harTasks**.
3.  Ensure that **hvigorfile.ts** uses **export default** for its export.

Example:

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

#### 00302017 Unknown Module Name in the Command Line

**Error Message**

Unknown module XXX in the command line.

**Symptom**

The CLI contains an unknown module _XXX_.

**Possible Causes**

The module name in the command is dynamically deleted from the **hvigorconfig.ts** file.

**Solution**

Ensure that the module is not deleted from the **hvigorconfig.ts** file.

#### 00302018 Unknown Module Name in the Command Line

**Error Message**

Unknown module XXX in the command line.

**Symptom**

The CLI contains an unknown module _XXX_.

**Possible Causes**

The module name in the command does not exist in the project-level **build-profile.json5** file.

**Solution**

Ensure that the module is set in the **modules** field of the project-level **build-profile.json5** file.

#### 00302019 Incorrect Return Value Type of the Custom Plugin

**Error Message**

File XXX exports an invalid plugin XXX with invalid order return XXX. Must return a number value.

**Symptom**

The return value type of the custom plugin is incorrect.

**Possible Causes**

The plugin exported from the specified file has an incorrect return value type.

**Solution**

Ensure that the return value of the exported plugin is a number.

#### 00302020 Duplicate Custom Plugin Name

**Error Message**

File XXX exports an invalid plugin XXX whose name XXX duplicate with other plugins. Please rename this plugin.

**Symptom**

The custom plugin name is duplicated.

**Possible Causes**

The name of the custom plugin exported from the specified file conflicts with other plugin names.

**Solution**

Check for duplicate custom hvigor plugin names and rename the conflicting plugin if necessary.

#### 00302021 No Default Export in the Custom Plugin

**Error Message**

File XXX has no default export.

**Symptom**

The custom plugin does not have a default export.

**Possible Causes**

The hvigor custom plugin in the specified file does not have a default export.

**Solution**

Add **export default** to the hvigor plugin defined in the specified file.

#### 00302022 Undefined Plugin Export

**Error Message**

File XXX exports an undefined plugin.

**Symptom**

An undefined plugin is exported.

**Possible Causes**

An undefined hvigor plugin is exported from the specified file.

**Solution**

Ensure that the correct hvigor plugin is exported.

#### 00302023 Incorrect Custom Plugin Type

**Error Message**

File XXX exports an invalid plugin with type XXX.

**Symptom**

The custom plugin type is incorrect.

**Possible Causes**

The plugin exported from the specified file has an incorrect type.

**Solution**

Check the type of the exported plugin to ensure it is an object.

#### 00302024 Missing Custom Plugin Name

**Error Message**

File XXX exports an invalid plugin without a name.

**Symptom**

A plugin without a name is exported from the specified file.

**Possible Causes**

The plugin exported from the specified file does not have a name.

**Solution**

Ensure that the exported plugin has a name.

#### 00302025 Invalid Plugin Name Type

**Error Message**

File XXX exports an invalid plugin whose name is not a string.

**Symptom**

A plugin with a non-string name is exported from the specified file.

**Possible Causes**

The name of the plugin exported from the specified file is not a string.

**Solution**

Ensure that the name of the exported plugin is a string.

#### 00302026 Unknown Plugin Execution Order

**Error Message**

File XXX exports an invalid plugin YYY with unknown order ZZZ.

**Symptom**

A plugin with an unknown execution order is exported from the specified file.

**Possible Causes**

The execution order of the plugin exported from the specified file is unknown.

**Solution**

Ensure that the exported plugin has the correct execution order.

#### 00302027 Invalid Hook Type in the Custom Plugin

**Error Message**

File XXX exports an invalid plugin YYY whose hook ZZZ is not a function.

**Symptom**

A plugin with a non-function hook is exported from the specified file.

**Possible Causes**

The hook of the plugin exported from the specified file is not a function.

**Solution**

Ensure that the hook of the exported plugin is correctly defined as a function.

#### 00302029 Plug-in and Module Type Mismatch

**Error Message**

The plugin referenced in the hvigorfile does not match moduleType in the module.json5/config.json file.

**Symptom**

The plugin referenced in **hvigorfile** is inconsistent with the module type in the **module.json5/config.json** file.

**Possible Causes**

The task type (such as **hapTasks**) registered in **hvigorfile** is inconsistent with the module type (such as HAR module). For example, the HAP module references **harPlugin**.

**Solution**

Ensure that the task type matches the module type.

#### 00302030 API Type Mismatch

**Error Message**

Mismatch with apiType at 'XXX'.

**Symptom**

The **apiType** configuration at _XXX_ does not match.

**Possible Causes**

**apiType** configured in the module-level **hvigorfile.ts** file is inconsistent with that in the module-level **build-profile.json5** file.

**Solution**

Set **apiType** to the same values in module-level **hvigorfile.ts** file and module-level **build-profile.json5** file.

#### 00302031 Lack of System Plugins in hvigorfile.ts of the FA Model Project

**Error Message**

Invalid exports, no system plugins were found in hvigorfile. At file: XXX.

**Symptom**

Export failed. No system plug-ins are found in **hvigorfile**.

**Possible Causes**

1.  The **system** field is missing in **hvigorfile.ts**.
2.  **legacyAppTasks**, **legacyHapTasks**, or **legacyHarTasks** used in **hvigorfile.ts** does not exist.
3.  The **hvigorfile.ts** file does not use **export default** for its export.

**Solution**

1.  Ensure that the **system** field exists in **hvigorfile.ts**.
2.  Verify that the project-level **hvigorfile.ts** uses **legacyAppTasks**, and the module-level **hvigorfile.ts** uses **legacyHapTasks** or **legacyHarTasks**.
3.  Ensure that **hvigorfile.ts** uses **export default** for its export.

Example:

export default {
    system: legacyAppTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

#### 00302032 Lack of System Plugins in hvigorfile.ts of the Stage Model Project

**Error Message**

Invalid exports, no system plugins were found in hvigorfile.

**Symptom**

Export failed. No system plug-ins are found in **hvigorfile**.

**Possible Causes**

1.  The **system** field is missing in **hvigorfile.ts**.
2.  **appTasks**, **hapTasks**, **hspTasks**, or **harTasks** used in **hvigorfile.ts** does not exist.
3.  The **hvigorfile.ts** file does not use **export default** for its export.

**Solution**

1.  Ensure that the **system** field exists in **hvigorfile.ts**.
2.  Verify that the project-level **hvigorfile.ts** uses **appTasks**, and the module-level **hvigorfile.ts** uses **hapTasks**, **hspTasks**, or **harTasks**.
3.  Ensure that **hvigorfile.ts** uses **export default** for its export.

Example:

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

#### 00302033 SetProperty Method in hvigorfile.ts Failed to Be Verified

**Error Message**

Method setProperty validate failed in hvigorfile.ts.

**Symptom**

The **setProperty** method in the **hvigorfile.ts** file fails to be validated.

**Possible Causes**

The parameters passed to the **setProperty** method fail schema validation.

**Solution**

Modify the fields in the **hvigorfile.ts** file based on the error message.

#### 00302034 Failed to Execute the XXX Lifecycle

**Error Message**

Failed to execute hook 'XXX': YYY.

**Symptom**

The _XXX_ lifecycle fails to be executed.

**Possible Causes**

An error is reported when the code in the _XXX_ lifecycle is executed.

**Solution**

1.  Check the code in the _XXX_ lifecycle based on the error message _YYY_.
2.  Set **stacktrace** in **hvigor-config.json5** to **true** and rectify the fault based on the stack information.

#### 00302035 Failed to Execute the XXX Function of the Custom Plugin YYY

**Error Message**

Failed to execute function 'XXX' of the custom plugin whose pluginId is 'YYY': ZZZ.

**Symptom**

The _XXX_ function of the custom plugin _YYY_ fails to be executed.

**Possible Causes**

An error is reported when the code in the _XXX_ function of the custom plugin _YYY_ is executed.

**Solution**

1.  Check the code in the _XXX_ function of the custom plugin _YYY_ based on the error message _ZZZ_.
2.  Set **stacktrace** in **hvigor-config.json5** to **true** and rectify the fault based on the stack information.

#### 00302036 Failed to Execute the XXX Lifecycle

**Error Message**

Failed to execute node hook 'XXX': YYY.

**Symptom**

The _XXX_ lifecycle fails to be executed.

**Possible Causes**

An error is reported when the code in the _XXX_ lifecycle is executed.

**Solution**

1.  Check the code in the _XXX_ lifecycle based on the error message _YYY_.
2.  Set **stacktrace** in **hvigor-config.json5** to **true** and rectify the fault based on the stack information.

#### 00302037 Failed to Execute YYY in hvigorfile.ts

**Error Message**

Failed to load or execute hvigorfile.ts: XXX At file: YYY.

**Symptom**

The code _YYY_ in the **hvigorfile.ts** file fails to be executed.

**Possible Causes**

An error is reported when the code _YYY_ in the **hvigorfile.ts** file is executed.

**Solution**

1.  Check the code _YYY_ in the **hvigorfile.ts** file according to the error message _XXX_.
2.  Set **stacktrace** in **hvigor-config.json5** to **true** and rectify the fault based on the stack information.
