# User Preference Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/_tkPoYeiReaamJuCUZ7klw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062221Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E97AF59B0C91755A1DBF26A17550F794AB12F2AABB10CF6AAD3260C9E9138195)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 15500000 Internal Error

**Error Message**

Inner error.

**Description**

An internal error occurred.

**Possible Causes**

View the error log to determine the cause of the error. Possible causes include the following:

1.  The internal state is abnormal.
2.  There is an API that is incorrectly used.
3.  A system error, such as insufficient memory, I/O error, or JS engine exception, occurs.

**Solution**

1.  Check whether a closed object is reused.
2.  Check whether the APIs are correctly used.
3.  If the problem persists, ask the user to restart or update the application or upgrade the device version.

#### 15500010 Failed to Delete the User Preference Persistence File

**Error Message**

Failed to delete the user preferences persistence file.

**Description**

The operation of deleting the user preference persistence file failed.

**Possible Causes**

The possible causes are as follows:

1.  The file name is incorrect.
2.  The file path is incorrect.

**Solution**

1.  Check that the file name is correct.
2.  Check that the file path is correct.

#### 15500019 Failed to Obtain the Subscription Service

**Error Message**

Failed to obtain the subscription service.

**Description**

Failed to obtain the subscription service in inter-process event subscription.

**Possible Causes**

The platform does not support service subscription.

**Solution**

Deploy the subscription service on the platform.

#### 15501001 Stage Model Required

**Error Message**

The operation is supported in stage mode only.

**Description**

This operation can be performed only on the stage model.

**Possible Causes**

The context is not a stage model.

**Solution**

Perform the operation on the stage model.

#### 15501002 Invalid dataGroupId Parameter in Options

**Error Message**

Invalid dataGroupId.

**Description**

The **dataGroupId** parameter is invalid.

**Possible Causes**

The **dataGroupId** is not obtained from the AppGallery.

**Solution**

Obtain **dataGroupId** from the AppGallery and pass it correctly.
