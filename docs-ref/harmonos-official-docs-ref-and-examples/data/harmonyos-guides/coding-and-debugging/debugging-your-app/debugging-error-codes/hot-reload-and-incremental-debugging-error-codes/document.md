# Hot Reload and Incremental Debugging Error Codes

#### 00402001 SDK Not Found

**Error Message**

Install the SDK first.

**Symptom**

Install the SDK.

**Possible Causes**

The SDK cannot be found.

**Solution**

Check whether the **ets** directory exists in the **sdk/default/openharmony** directory under the DevEco Studio installation directory. If it does not exist, [download DevEco Studio](https://developer.huawei.com/consumer/en/download/deveco-studio) again from the official website.

#### 00402002 Hot Reload Only Supports Stage Model Projects

**Error Message**

Hot Reload Feature is only supported in STAGE and esmodule project.

**Symptom**

Hot reload supports only stage model projects.

**Possible Causes**

The current project is not a stage model project.

**Solution**

Use a stage model project or select a non-hot reload run configuration.

#### 00402003 Node.js Path Not Found During Hot Reload Startup

**Error Message**

The nodejs path configured for the project is invalid or not found.

**Symptom**

The Node.js path cannot be found.

**Possible Causes**

The configured Node.js path does not exist.

**Solution**

Check whether the Node.js tool exists in the **tools** directory under the DevEco Studio installation directory. If it does not exist, [download DevEco Studio](https://developer.huawei.com/consumer/en/download/deveco-studio) again from the official website.

#### 00402004 Hot Reload Does Not Support Current Code Changes

**Error Message**

The current modification does not support hot reload. Please reinstall and restart.

**Symptom**

The current code changes are not supported by hot reload.

**Possible Causes**

The type of code changes made is not supported by hot reload.

**Solution**

Check whether code changes comply with the [usage constraints](../../code-debugging/hot-reload/document.md#section995453874915) of hot reload. If they are not supported, click the Run or Debug button, then restart hot reload.

#### 00402005 Hot Reload Supports File Modifications Only, Not Additions or Deletions

**Error Message**

Hot reload is supported only for file change, but not file addition and deletion.

**Symptom**

Hot reload supports modifications to existing files but does not support additions or deletions.

**Possible Causes**

You added or deleted files while running in hot reload mode.

**Solution**

Click the Run or Debug button, then restart hot reload.

#### 00402006 Failed to Obtain Node.js Path for File Comparison

**Error Message**

The nodejs path configured in the IDE is invalid or not found.

**Symptom**

The Node.js path cannot be found.

**Possible Causes**

The Node.js path cannot be found for file comparison.

**Solution**

Check whether the Node.js tool exists in the **tools** directory under the DevEco Studio installation directory. If it does not exist, [download DevEco Studio](https://developer.huawei.com/consumer/en/download/deveco-studio) again from the official website.

#### 00402007 Hot Reload Operation Times Out

**Error Message**

Execute hot-reload timeout, please reinstall and restart.

**Symptom**

The hot reload operation times out. Restart hot reload.

**Possible Causes**

The quick fix operation during hot reload times out.

**Solution**

Click the Run or Debug button, then restart hot reload.

#### 00402008 Hot Reload Build Failed

**Error Message**

Build failed, check the error information in the console, rectify the fault, and try again.

**Symptom**

The build failed. Check the error message in the console, fix the fault, and try again.

**Possible Causes**

The build failed.

**Solution**

Check the error message in the console, fix the fault, and try again.

#### 00402009 Failed to Sign the Incremental Patch Package

**Error Message**

Failed to sign the patch package, please check the signingConfigs in build-profile.json5.

**Symptom**

The incremental patch package failed to be signed.

**Possible Causes**

Incorrect signing configuration.

**Solution**

Check the **signingConfigs** configuration in the **build-profile.json5** file. [Reconfigure the signing](../../../configuring-a-debug-signature/document.md) and try again if the configuration is incorrect.

#### 00402010 No .abc Patch File Generated During Build

**Error Message**

PatchAbc was not generated, please clean and restart project.

**Symptom**

No .abc patch file is generated during the build process.

**Possible Causes**

The .abc patch file fails to be generated during the build process.

**Solution**

Choose **Build** > **Clean Project** on the menu bar to clear the cache and try again.

#### 00402011 Failed to Generate the .hqf Incremental Package

**Error Message**

Failed to create the patch package, please clean and restart project.

**Symptom**

The .hqf incremental package failed to be generated.

**Possible Causes**

Failed to generate the .hqf incremental package.

**Solution**

Choose **Build** > **Clean Project** on the menu bar to clear the cache and try again.

#### 00402012 Failed to Reload the File

**Error Message**

Reloaded XXX files failed. Please reinstall and restart.

**Symptom**

The file failed to be reloaded.

**Possible Causes**

The **bm quickfix** command fails to be executed during hot reload.

**Solution**

Check the following items:

1.  Verify the project signing configuration. Hot reload requires signing with a debug certificate and does not support release certificate signing. For details, see [Configuring a Debug Signature](../../../configuring-a-debug-signature/document.md).
2.  Verify the project build mode setting. Hot reload requires the debug mode and does not support the release mode. For details, see [Specifying a Build Mode](../../../../building-an-app/customizing-your-build/customizing-build-options/introduction/document.md#section192461528194916).

#### 00402013 Apply Changes Execution Timeout

**Error Message**

Execute apply-change timeout, please restart and reinstall.

**Symptom**

The Apply Changes execution times out.

**Possible Causes**

Abnormal hdc process or unstable device connection, resulting in **hdc** command execution timeout during Apply Changes.

**Solution**

Unplug and replug the device, or run the **hdc kill -r** command to restart the hdc process, and try again.

#### 00402014 Failed to Build the .hqf Incremental Package

**Error Message**

Build failed, please reinstall and restart.

**Symptom**

The .hqf incremental package failed to be built.

**Possible Causes**

Failed to build the .hqf incremental package.

**Solution**

Check the build console for detailed error message, address the issues, and try again.

#### 00402015 Apply Changes Not Supported on the Previewer

**Error Message**

Apply Changes not supported when device type is Previewer.

**Symptom**

The Apply Changes feature cannot be used with the Previewer.

**Possible Causes**

Apply Changes is used during debugging with the Previewer.

**Solution**

Use a real device or an emulator instead for Apply Changes.

#### 00402016 Failed to Start or Debug the Project Before Apply Changes

**Error Message**

Start or debug the project first.

**Symptom**

Failed to start or debug the project before Apply Changes.

**Possible Causes**

You tried to execute Apply Changes before starting or debugging the project.

**Solution**

Click the Run or Debug button to launch the project first. After modifying the code, execute Apply Changes.

#### 00402017 Apply Changes Not Supported for HSP Modules

**Error Message**

Apply Changes not supported for shared modules.

**Symptom**

Apply Changes is not supported for HSP modules.

**Possible Causes**

The current module is an HSP module, which does not support Apply Changes.

**Solution**

Select a HAP module and try again.

#### 00402018 Apply Changes Not Supported for FA Model Projects

**Error Message**

Apply Changes not supported for projects in the FA model.

**Symptom**

Apply Changes is not supported for FA model projects.

**Possible Causes**

Your project uses the FA model, which does not support Apply Changes.

**Solution**

Do not use the Apply Changes feature for FA model projects.

#### 00402019 Apply Changes Not Supported with the Launch Option Set to Nothing

**Error Message**

Apply Changes not supported when Launch module is set to Nothing.

**Symptom**

Apply Changes cannot be executed when the **Launch** option is set to **Nothing**.

**Possible Causes**

The **Launch** option under **Launch Options** in the **Run/Debug Configurations** panel is set to **Nothing**.

**Solution**

In the **Run/Debug Configurations** panel, select an ability in the **Launch** option under **Launch Options** and try again.

#### 00402020 Empty Run Configuration

**Error Message**

XXX: settings is null.

**Symptom**

No run configuration is currently selected.

**Possible Causes**

No run configuration is selected.

**Solution**

Select a valid run configuration.

#### 00402021 No Changes Detected in C++ or Resource Files

**Error Message**

No changes detected on C++ files or resource files. If you have made changes to files in other types, click the Run/Debug icon instead.

**Symptom**

No changes are detected in C++ or resource files. If you have modified files of other types, click the Run or Debug button.

**Possible Causes**

You modified only ETS files or made no file changes that qualify for incremental deployment.

**Solution**

To use Apply Changes, modify C++ or resource files. If you modified files of other types (such as ETS), click the Run or Debug button.

#### 00402024 Failed to Deploy Incremental Changes on the Device

**Error Message**

Failed to deploy the incremental changes on the device. Update the device image to the latest version and try again, or click the Run/Debug icon to deploy all changes.

**Symptom**

Failed to deploy incremental changes on the connected device.

**Possible Causes**

1.  The **bm quickfix** command failed to execute, potentially due to an outdated device image version.
2.  For a 2-in-1 device, the app acceleration service may be enabled.

**Solution**

1.  Update the device image to the latest version and retry, or click the Run or Debug button to deploy all changes.
2.  For a 2-in-1 device, go to **Settings** > **Apps & services** > **App acceleration** and disable the app acceleration service.

#### 00402025 Inconsistent Sanitizer Configuration Between the HQF and HAP

**Error Message**

Apply change fail, please confirm whether ASan/TSan/UBSan/HWASan is same as the hap and reinstall.

**Symptom**

Apply Changes failed due to a mismatch in sanitizer configurations of the HQF and HAP.

**Possible Causes**

ASan, TSan, UBSan, and HWASan cannot be enabled simultaneously; only one of these sanitizers can be active at a time.

**Solution**

Ensure the sanitizer configuration of the HQF matches that of the HAP, or uninstall the app and run it again.

#### 00402026 Failed to Execute Apply Changes

**Error Message**

Apply change fail.

**Symptom**

Failed to execute Apply Changes.

**Possible Causes**

The device connection or the HDC service is abnormal.

**Solution**

Unplug and replug the device, or run the **hdc kill -r** command, and try again.

#### 00402027 Device Screen Locked

**Error Message**

The screen is locked. Please unlock the screen and try again.

**Symptom**

The device screen is locked.

**Possible Causes**

The device screen is locked during the app launch or Apply Changes operation.

**Solution**

Unlock the screen and try again.

#### 00402028 Invisible Ability During App Launch

**Error Message**

Ability is not visible.

**Symptom**

The target ability is invisible during app launch.

**Possible Causes**

The ability launched by the **aa start** command is invisible.

**Solution**

-   For projects developed using the stage model, open the **module.json5** file and set **exported** under **abilities** to **true**.
-   For projects developed using the FA model, open the **config.json** file and set **visible** under **abilities** to **true**.

#### 00402030 Failed to Create changedFileList.json File

**Error Message**

Failed to create changedFileList.json, please clean and restart project.

**Symptom**

Failed to create the **changedFileList.json** file.

**Possible Causes**

The creation process for the **changedFileList.json** file failed.

**Solution**

Choose **Build** > **Clean Project** on the menu bar to clear the cache and try again.

#### 00402031 Failed to Obtain the Node.js Script for File Comparison

**Error Message**

Failed to obtain the node script for file comparison. Please reinstall the IDE.

**Symptom**

The Node.js script required for file comparison cannot be obtained.

**Possible Causes**

The Node.js script required for file comparison cannot be obtained.

**Solution**

[Download and reinstall DevEco Studio](https://developer.huawei.com/consumer/en/download/deveco-studio).

#### 00402032 Hot Reload and Hot Restart Unavailable for Changes

**Error Message**

Hot reload and hot restart unavailable for the following changes.

**Symptom**

The listed code changes are not supported by either hot reload or hot restart.

**Possible Causes**

The changes fall outside the supported scenarios for both hot reload and hot restart.

**Solution**

Check if your changes comply with the [constraints](../../code-debugging/hot-reload/document.md#section995453874915) for hot reload and hot restart. If they are not supported, click the Run or Debug button, then restart hot reload or hot restart.

#### 00402033 Empty or Missing ChangedFileList.json

**Error Message**

ChangedFileList.json is null or empty, please clean and rerun project.

**Symptom**

The **ChangedFileList.json** file is empty or does not exist.

**Possible Causes**

The **ChangedFileList.json** file is empty or does not exist.

**Solution**

Choose **Build** > **Clean Project** on the menu bar to clear the cache and try again.

#### 00402034 Hot Reload Unavailable for Changes

**Error Message**

Hot reload unavailable for the following changes.

**Symptom**

Hot reload is not available for the listed code changes.

**Possible Causes**

The changes are only supported by hot restart, but the **Enable hot restart** option is disabled.

**Solution**

[Enable hot restart](../../code-debugging/hot-reload/document.md#section1724105718289), click the Run or Debug button, and restart hot reload.

#### 00402035 Hot Reload Not Supported in Release Mode

**Error Message**

Cannot hot reload the project when its build mode is release. Change the build mode to debug and try again.

**Symptom**

The hot reload feature cannot be used because the project is in release build mode.

**Possible Causes**

The build mode of the current project is release.

**Solution**

Change the build mode to debug and try again.

#### 00402036 Incompatible HDC Version

**Error Message**

Incompatible hdc version. Use the one in sdk\\default\\openharmony\\toolchains under the DevEco Studio installation directory.

**Symptom**

The HDC version in use is incompatible.

**Possible Causes**

An earlier version of HDC is configured in the environment variable.

**Solution**

Update the environment variable to point to the HDC file located in **sdk\\default\\openharmony\\toolchains** under the DevEco Studio installation directory, then restart DevEco Studio.
