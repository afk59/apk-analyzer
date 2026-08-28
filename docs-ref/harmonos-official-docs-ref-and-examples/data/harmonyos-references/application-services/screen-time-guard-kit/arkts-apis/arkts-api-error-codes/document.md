# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/NV3CDFmnSCOVS77DvcRUyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062520Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF208EF8A01BC4FD88C9BBFBDE4FD8C518F0BD8A50A4EAE9F3989E222AE553FC)

This section describes only error codes related to this module. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 1019000001 Internal Error

**Message**

Internal error.

**Description**

Internal error.

**Possible cause**

A system service error or another internal error occurred.

**Solution**

1\. Restart your device and try again.

2\. If any error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei technical support will get back to you as soon as possible.

#### 1019000002 User Authorization Not Granted

**Message**

The user has not authorized the application to access this interface.

**Description**

The user has not authorized the app to access this API.

**Possible cause**

The user rejects to grant authorization.

**Solution**

1\. Call this API again after the user grants authorization.

2\. If the user has already granted authorization but the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1019000003 Operation Canceled by User

**Message**

The user canceled the operation.

**Description**

The user canceled the operation.

**Possible cause**

The user cancels the operation of accessing the **AppPicker** page.

**Solution**

1\. Check whether the user has canceled the operation.

2\. If the user did not cancel the operation but the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1019000004 Strategy Quantity Exceeded the Limit

**Message**

The number of strategies exceeds the upper limit.

**Description**

The number of strategies exceeds the upper limit.

**Possible cause**

The number of guard strategies added has exceeded the 50-strategy limit.

**Solution**

1\. Reduce the number of strategies.

2\. If the number of strategies is below the limit but the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1019000005 Duplicate Strategy Name

**Message**

The strategy name is already existed.

**Description**

The strategy name already exists.

**Possible cause**

The name of the strategy that you want to add already exists.

**Solution**

1\. Use the [strategy query API (queryGuardStrategies)](../guardservice-screen-time-guard-service/document.md#section1812105318579) to obtain the strategies of your app.

2\. Change the strategy name to a unique one.

3\. If the strategy name is unique but the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1019000006 Nonexistent Strategy

**Message**

Nonexistent strategy.

**Description**

No strategy with the specified name exists.

**Possible cause**

An attempt is made to modify, delete, enable, or disable a nonexistent strategy.

**Solution**

1\. Check whether the strategy that you want to operate exists.

2\. If the strategy exists but the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1019000007 Repeated Strategy Execution

**Message**

The strategy is already being executed.

**Description**

The strategy is being executed.

**Possible cause**

The strategy that you want to start is being executed.

**Solution**

1\. Check whether the strategy is being executed.

2\. If the strategy is not being executed but the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1019000008 Strategy Not Executed

**Message**

This strategy has not been started yet.

**Description**

The strategy has not been executed.

**Possible cause**

The strategy that you want to stop is not being executed.

**Solution**

1\. Check whether the strategy has been stopped.

2\. If the strategy is being executed but the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1019000009 Parameter Check Failed

**Message**

Parameter error. Possible causes:1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

**Description**

1\. A mandatory parameter is left empty.

2\. A parameter type is incorrect.

3\. Parameter verification failed. Regardless of whether the API is synchronous or asynchronous, this type of error is generally thrown in synchronous mode.

**Possible cause**

1\. A mandatory parameter is not passed.

2\. A parameter type is incorrect. (Type Error)

3\. The number of parameters is incorrect. (Argument Count Error)

4\. Null is passed to a parameter that requires a value. (Null Argument Error)

5\. A parameter format is incorrect. (Format Error)

6\. A parameter value is out of the valid range. (Value Range Error)

**Solution**

1\. Ensure that all the mandatory parameters are passed and the parameter types are valid. For parameter verification failures, read the parameter specifications and locate the fault based on the possible causes.

2\. If parameters are correctly set but the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.
