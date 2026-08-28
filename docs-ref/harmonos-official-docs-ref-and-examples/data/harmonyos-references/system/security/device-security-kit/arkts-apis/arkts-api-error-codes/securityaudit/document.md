# SecurityAudit

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/js9UQ41nSweFlbFrsQMHxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062334Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D7043524545E631DC269CDEBB0EC1F3DB5A64C6808E130A4059629908D62F5CA)

This section describes only module-specific client error codes and provides the cause analysis. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 201 Permission Verification Failed

**Description**

Permission verification failed.

**Possible causes**

The app package has not obtained the **ohos.permission.QUERY\_AUDIT\_EVENT** or **ohos.permission.kernel.AUTH\_AUDIT\_EVENT** permission.

**Solution**

Only enterprise apps in the list can apply for this permission. For details about how to apply for this permission, please refer to [Permissions for Enterprise Applications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/permissions-for-enterprise-apps).

#### 401 Parameter Check Failed

**Description**

Parameter check failed.

**Possible causes**

A mandatory parameter is missing, or the parameter type or specifications are invalid.

**Solution**

Make sure all the mandatory parameters are passed and the parameter types and specifications are valid.

#### 1012000001 Internal Error

**Message**

Internal error.

**Description**

Internal error.

**Possible causes**

An exception occurred when other system APIs are called in the API execution process.

**Solution**

Try again first. If the retry fails, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1012000002 Client Quantity Exceeds Upper Limit

**Description**

The total number of clients exceeds the upper limit.

**Possible causes**

The number of client instances requested by the current device for audit event management exceeds the upper limit (16).

**Solution**

In the notification event application scenario, use the **deleteClient** API to delete unnecessary client instances and use the **newClient** API to apply for new notification client instances for audit event management.

In the authentication event application scenario, use the **deleteAuthClient** API to delete unnecessary client instances and use the **newAuthClient** API to apply for new authentication client instances for audit event management.

#### 1012000003 Client Instance Quantity in a Process Exceeds Upper Limit

**Description**

The number of client instances in a process exceeds the upper limit.

**Possible causes**

The number of client instances requested by the current process for audit event management exceeds the upper limit (2).

**Solution**

In the notification event application scenario, use the **deleteClient** API to delete unnecessary client instances and use the **newClient** API to apply for new notification client instances for audit event management.

In the authentication event application scenario, use the **deleteAuthClient** API to delete unnecessary client instances and use the **newAuthClient** API to apply for new authentication client instances for audit event management.

#### 1012000004 Filter Quantity Exceeds Upper Limit

**Description**

The number of filters exceeds the upper limit.

**Possible causes**

The number of filter values set for the client instance exceeds the upper limit (256).

**Solution**

Delete unnecessary filters using **removeFilter** of the client instance and set new filters using **addFilter** of the client instance based on the application scenario.

#### 1012000005 Filter Not Supported by Event

**Description**

The event does not support this filter.

**Possible causes**

The event with the specified ID does not support this filter.

**Solution**

Check whether the current event supports this filter. If not, change the filter.

#### 1012000007 Corresponding Authentication Event Not Found

**Description**

The corresponding authentication event is not found.

**Possible causes**

In the authentication event application scenario, the initiator of the authentication event subscribed by the user has exited unexpectedly, or the event has been processed. As a result, the authentication event is invalid.

**Solution**

Check whether the initiator has exited because the current event is not processed within the timeout interval or whether the event has been processed. Use an event for which no authentication policy is set.
