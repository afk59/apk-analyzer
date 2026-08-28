# ohos.screenLockFileManager Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/kUoYJWaoSTGL4WtsnFriCg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2ECC425D93A9749D1A8BA167121944AC270669B4DDA31A52421F4C07014E8249)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 29300002 System Service Abnormal

**Error Message**

The system ability work abnormally.

**Possible Causes**

System services are not working properly. The possible causes are as follows:

1.  Sensitive data access management on the lock screen is not started properly.
2.  The read or write of IPC data fails.

**Solution**

System services do not work properly. Try again later or restart the device.

#### 29300003 Sensitive Data Access Management Under Lock Screen Is Not Enabled

**Error Message**

The application has not enabled the data protection under lock screen.

**Possible Causes**

1.  The ohos.permission.PROTECT\_SCREEN\_LOCK\_DATA permission is not configured through [requestpermissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/declare-permissions#declaring-permissions-in-the-configuration-file) to enable sensitive data access management on the lock screen.
2.  The device does not support sensitive data access management on the lock screen.

**Solution**

Configure the ohos.permission.PROTECT\_SCREEN\_LOCK\_DATA permission through [requestpermissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/declare-permissions#declaring-permissions-in-the-configuration-file) to enable sensitive data access management on the lock screen.

#### 29300004 Permission to Access Sensitive Data on the Lock Screen Has Been Revoked

**Error Message**

File access is denied.

**Possible Causes**

The permission to access sensitive data on the lock screen has been revoked.

**Solution**

Sensitive data cannot be accessed on the lock screen. If necessary, ask the user to unlock the screen again. The sensitive data can be used only after the screen is unlocked.

#### 29300005 Permission to Access Sensitive Data on the Lock Screen Is Not Requested

**Error Message**

File access was not acquired.

**Possible Causes**

The permission to access sensitive data on the lock screen is not requested.

**Solution**

Ensure that the permission to access sensitive data on the lock screen is requested before calling the API to revoke the permission.
