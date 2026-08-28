# Access Control Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/KrUHg3l_TjGHrlH6b9SCjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F782620D98D38CF8A5B409000935A1E00849D8889F70E0D80AB17409BA4B267)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 12100001 Invalid Parameters

**Error Message**

Invalid Parameter. Error message: messageInfo.

**Description**

The input parameter is incorrect.

**Possible Causes**

1.  The value of **tokenId** is **0**.
2.  The permission name is empty or exceeds 256 characters.
3.  The **flag** value in the permission authorization or revocation request is invalid.
4.  The parameters specified for registering a listener are incorrect.
5.  The specified context does not belong to the current application.
6.  The requested permissions do not belong to the same permission group.
7.  The requested permissions include permissions that are not declared by the application.
8.  The type of the requested global switch is invalid.
9.  The specified permission is not [a user\_grant permission](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/permissions-for-all-user).
10.  The number of array members exceeds 1024 or all members are invalid.
11.  The start time and end time of the permission usage record to be viewed are invalid.
12.  The specified permission is not declared in the application.

**Solution**

Check that the input parameters are set to valid values by referring to the [API parameters](../../arkts-apis/both-models-recommended/ohos-abilityaccessctrl-application-access-control/document.md).

#### 12100004 Listener APIs Not Used in Pairs

**Error Message**

The API is not used in pair with others.

**Description**

The API is not used in pair with its counterpart.

**Possible Causes**

1.  One of the listener APIs that must be used in pairs is repeatedly called.
2.  One of the listener APIs that must be used in pairs is independently called.

**Solution**

1.  For the APIs that must be used in pairs, for example, **on()** and **off()**, check whether **on()** with the same parameters is called again before **off()** is called.
2.  For the APIs that must be used in pairs, for example, **on()** and **off()**, check whether **off()** is called before **on()**.

#### 12100005 Listener Overflows

**Error Message**

The number of listeners exceeds the limit.

**Description**

The number of listeners exceeds the upper limit.

**Possible Causes**

The number of listeners exceeds 200.

**Solution**

Release unused listeners in a timely manner.

#### 12100007 System Service Not Working Properly

**Error Message**

The service is abnormal.

**Description**

The system service is abnormal.

**Possible Causes**

1.  The permission management service cannot start properly.
2.  The read or write of IPC data fails.

**Solution**

Try again later or restart the device.

#### 12100009 Internal Service Error

**Error Message**

Common inner error.

**Description**

An internal service error occurs.

**Possible Causes**

1.  An internal error occurs in the system service.
2.  A database error occurs.
3.  Failed to create the pop-up window or obtain the user selection result.
4.  Failed to query all applications of the user.

**Solution**

Analyze the fault log to identify the error.

#### 12100010 Pending Request

**Error Message**

The request already exists.

**Description**

An unprocessed request exists.

**Possible Causes**

The last request has not been processed yet.

**Solution**

Wait until the last request is processed.

#### 12100011 All Requested Permissions Granted

**Error Message**

All permissions in the permission list have been granted.

**Description**

All input permissions have been granted.

**Possible Causes**

All requested permissions have been granted.

**Solution**

No action is required. If this error code is returned, the permission has been granted and the permission settings dialog box will not be displayed.

#### 12100012 Not All Permissions Are Rejected by the User

**Error Message**

The permission list contains the permission that has not been revoked by the user.

**Description**

Some input permissions have not been denied by the user.

**Possible Causes**

The requested permissions include the permissions that are not rejected by the user.

**Solution**

Call **requestPermissionsFromUser** to request permissions from the user first.

#### 12100013 Global Switch Enabled

**Error Message**

The specific global switch is already open.

**Description**

The global switch is enabled.

**Possible Causes**

The global switch is already turned on.

**Solution**

No action is required. If this error code is returned, the global switch has been enabled and the dialog box for setting the global switch will not be displayed.

#### 12100014 Unexpected Permission

**Error Message**

Unexpected permission.

**Description**

The input permission does not meet the requirements.

**Possible Causes**

1.  When the [permission setting dialog box is displayed again](../../arkts-apis/both-models-recommended/ohos-abilityaccessctrl-application-access-control/document.md#requestpermissiononsetting12), the permission of the manual\_settings authorization mode is passed.
2.  During authorization or authorization cancellation, the permission of the non-user\_grant or manual\_settings authorization mode is passed.
3.  When the [permission setting dialog box is displayed again](../../arkts-apis/both-models-recommended/ohos-abilityaccessctrl-application-access-control/document.md#openpermissiononsetting22), the permission of the non-manual\_settings authorization mode is passed.

**Solution**

Check whether the input permission meets the requirements.
