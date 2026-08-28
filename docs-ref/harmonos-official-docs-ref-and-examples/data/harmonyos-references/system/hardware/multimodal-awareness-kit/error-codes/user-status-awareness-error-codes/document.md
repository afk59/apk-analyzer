# User Status Awareness Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/Pbqv5P1wQi2E5pypeiUWBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062410Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83E4D5D4F8DACD2D19C355C8D92C0FD0223A167AB7F4E7DBE5276CEA3113935F)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 33900001 Service Exception

**Error Message**

Service exception. Possible causes:

1\. System error, such as a null pointer and container-related exception.

2\. Node-API invocation exception, such as invalid Node-API status.

**Description**

This error code is reported if a service exception occurs when the **on** or **off** API of the userStatus module is called.

**Possible Causes**

The service status is abnormal.

**Solution**

1.  Retry the operation at a specified interval (for example, 1s) or at an exponential increase interval.
2.  If the operation fails for three consecutive times, stop the retry. During this period, you can preferentially obtain the device list to check for device availability.

#### 33900002 Subscription Failed

**Error Message**

Subscription failed. Possible causes:

1\. Callback registration failed.

2\. Failed to bind the native object to the JS wrapper.

3\. Node-API invocation exception, such as invalid Node-API status.

4\. IPC request exception.

**Description**

This error code is reported if subscription fails when the **on** API of the userStatus module is called.

**Possible Causes**

Subscription to status change events has failed.

**Solution**

1.  Retry the operation at a specified interval (for example, 1s) or at an exponential increase interval.
2.  If the operation fails for three consecutive times, stop the retry.

#### 33500003 Unsubscription Failed

**Error Message**

Unsubscription failed. Possible causes:

1\. Callback failure.

2\. Node-API invocation exception, such as invalid Node-API status.

3\. IPC request exception.

**Description**

This error code is reported if unsubscription fails when the **off** API of the userStatus module is called.

**Possible Causes**

Unsubscription from status change events has failed.

**Solution**

1.  Retry the operation at a specified interval (for example, 1s) or at an exponential increase interval.
2.  If the operation fails for three consecutive times, stop the retry.
