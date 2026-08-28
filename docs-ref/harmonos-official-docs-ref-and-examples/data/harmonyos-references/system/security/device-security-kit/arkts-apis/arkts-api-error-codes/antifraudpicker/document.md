# AntifraudPicker

#### 201 Permission Verification Failed

**Description**

Permission verification failed.

**Possible causes**

The HAP has not obtained the **ohos.permission.USE\_FRAUD\_MESSAGES\_PICKER** or **ohos.permission.USE\_FRAUD\_CALL\_LOG\_PICKER** permission.

**Solution**

Only apps that meet the application scenario requirements can apply for these permissions. To use the fraudulent message picker in the fraudulent message reporting scenario, you need to apply for the **ohos.permission.USE\_FRAUD\_MESSAGES\_PICKER** permission. To use the fraudulent call log picker in the fraudulent call reporting scenario, you need to apply for the **ohos.permission.USE\_FRAUD\_CALL\_LOG\_PICKER** permission. For details about how to apply for a restricted permission, please refer to [Requesting Restricted Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/declare-permissions-in-acl).

#### 401 Parameter Check Failed

**Description**

Parameter check failed.

**Possible causes**

A mandatory parameter is missing, or the parameter type or specifications are invalid.

**Solution**

Make sure all the mandatory parameters are passed and the parameter types and specifications are valid.

#### 1017100001 Unknown Error

**Description**

Internal error.

**Possible causes**

An exception occurred when other system APIs are called in the API execution process.

**Solution**

Try again first. If the retry fails, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1017100002 Unsupported Device Type

**Description**

The device type is not supported.

**Possible causes**

The device is not a phone or tablet.

**Solution**

Use a phone or tablet to send the request again.

#### 1017600001 Unknown Error

**Description**

An internal error occurred in the fraudulent app picker.

**Possible causes**

An exception occurred when other system APIs are called in the API execution process.

**Solution**

Try again first. If the retry fails, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1017600002 Unsupported Device Type

**Description**

The device type is not supported by the fraudulent app picker.

**Possible causes**

The device is not a phone or tablet.

**Solution**

Use a phone or tablet to send the request again.

#### 1017600003 Parameter Check Failed

**Description**

Failed to check the AntifraudPicker API parameters.

**Possible causes**

A mandatory parameter is missing, or the parameter type or specifications are invalid.

**Solution**

Make sure all the mandatory parameters are passed and the parameter types and specifications are valid.
