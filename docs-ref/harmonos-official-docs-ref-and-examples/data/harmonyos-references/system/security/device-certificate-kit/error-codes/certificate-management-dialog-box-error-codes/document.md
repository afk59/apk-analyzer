# Certificate Management Dialog Box Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/bmDcatAjRAee0MvF7SpR7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062338Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1FB086AA29215C42AB8AC2C0BD7B2EF8174A921B2FBB5F00199F46B3357528D6)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 29700001 Internal Error

**Error Message**

Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error.

**Possible Causes**

An internal error occurs when the API is called.

**Solution**

Check for and rectify the internal error.

#### 29700002 Operation Canceled

**Error Message**

The user cancels the installation operation.

**Possible Causes**

The user canceled the operation when the API was called.

**Solution**

No action is required.

#### 29700003 Failed to Install the Certificate

**Error Message**

The user install certificate failed in the certificate manager dialog, such as the certificate is in an invalid format.

**Possible Causes**

The certificate format is incorrect.

**Solution**

Check for incorrect certificate format and data.

#### 29700004 Operation Not Supported by the Device

**Error Message**

The API is not supported on this device.

**Possible Causes**

The API is available only for a PC application.

**Solution**

Ensure that the caller is running on a PC.

#### 29700005 Non-secure Operation

**Error Message**

The operation does not comply with the device security policy, such as the device does not allow users to manage the ca certificate of the global user.

**Possible Causes**

The device is not an enterprise device.

**Solution**

Call the API on an enterprise device.
