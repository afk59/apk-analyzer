# hdc Command Failure Error Codes

#### 00404035 HAP Installation Times Out

**Error Message**

Install hap timeout.

**Symptom**

The HAP installation times out.

**Possible Causes**

The device connection or the HDC service is abnormal.

**Solution**

Unplug and replug the device, or run the **hdc kill -r** command, and try again.

#### 00404036 Temporary Directory Deletion Times Out

**Error Message**

Remove Directory Timeout: XXX.

**Symptom**

The temporary directory deletion times out.

**Possible Causes**

The device connection or the HDC service is abnormal.

**Solution**

Unplug and replug the device, or run the **hdc kill -r** command, and try again.

#### 00404037 Temporary Directory Creation Times Out

**Error Message**

Create Directory Timeout.

**Symptom**

The temporary directory creation times out.

**Possible Causes**

The device connection or the HDC service is abnormal.

**Solution**

Unplug and replug the device, or run the **hdc kill -r** command, and try again.

#### 00404038 Empty Build Package Information

**Error Message**

Build package info list is empty.

**Symptom**

The build package information is empty.

**Possible Causes**

No valid app package information is generated during the build process.

**Solution**

Choose **Build** > **Clean Project** on the menu bar to clear the cache and try again.

#### 00404039 Failed to Create the Temporary Directory

**Error Message**

Failed to create temporary directory during hap push operation.

**Symptom**

Failed to create the temporary directory.

**Possible Causes**

The device connection or the HDC service is abnormal.

**Solution**

Unplug and replug the device, or run the **hdc kill -r** command, and try again.

#### 00404040 HAP Push Times Out

**Error Message**

Push Hap Timeout.

**Symptom**

The HAP push operation times out.

**Possible Causes**

A non-original data cable with lower transfer rates is used, or the HDC service is abnormal.

**Solution**

Use the original data cable, or run the **hdc kill -r** command, and try again.

#### 00404041 Enhanced Error Info Not Supported

**Error Message**

Start ability failed:The current device version does not support enhance error info. Update device version or deselect the Enhanced Error Info.

**Symptom**

Failed to start the ability because the device does not support Enhanced Error Info.

**Possible Causes**

The current device system version does not support the Enhanced Error Info feature.

**Solution**

Upgrade the device system, or clear the **Enhanced Error Info** check box in the **Run/Debug Configurations** panel.

#### 00404042 Multi Thread Check Not Supported

**Error Message**

The current device version does not support multi thread check. Update device version or deselect the Multi Thread Check.

**Symptom**

The device does not support Multi Thread Check.

**Possible Causes**

The current device system version does not support Multi Thread Check.

**Solution**

Upgrade the device system, or clear the **Multi Thread Check** check box in the **Run/Debug Configurations** panel.

#### 00404053 Wait-for-Debug Capability Not Supported

**Error Message**

The current device version does not support the waiting for debugging capability. Update or upgrade the device version.

**Symptom**

The current device system version does not support the wait-for-debug capability.

**Possible Causes**

The current device system version does not support the wait-for-debug capability.

**Solution**

Upgrade the current device system version.

#### 00404054 Wait-for-Debug Command Execution Times Out

**Error Message**

Waiting for the debug command times out.

**Symptom**

The command to set the app into wait-for-debug mode times out.

**Possible Causes**

The device connection or the HDC service is abnormal.

**Solution**

Unplug and replug the device, or run the **hdc kill -r** command, and try again.

#### 00404055 App Not Installed or Not Signed with a Debug Certificate

**Error Message**

This app is not installed or not signed with a debug signature.

**Symptom**

The target app is not installed or not signed with a debug certificate.

**Possible Causes**

1.  The command to set the app into wait-for-debug mode fails because the app is not installed or not signed with a debug certificate.
2.  The device connection is abnormal, causing command execution to fail.

**Solution**

1.  Check whether the app is installed and signed with a debug certificate.
2.  Check whether the device connection is normal. Try reconnecting the device and then restarting the wait-for-debug process.
