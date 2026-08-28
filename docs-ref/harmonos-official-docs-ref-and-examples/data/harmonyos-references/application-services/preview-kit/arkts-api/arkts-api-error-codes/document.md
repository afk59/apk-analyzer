# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/ol9qnx93S0qXG_oeZTff0g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062517Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D2794BB6FA38E12C05A974E7190650457DC14A1DEFBC81A49F1D58A65058AFA)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 1017220001 Internal Failure

**Message**

Internal failure.

**Description**

An unknown internal error is returned when the API is called.

**Possible cause**

An undefined error that is returned when the system processing is abnormal.

**Solution**

Create the service again or try again after a period of time and perform related logic judgment. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1017220002 Service Error

**Message**

Service unavailable.

**Description**

An error occurred during IPC service processing.

**Possible cause**

The system processing is abnormal, for example, system service restart or IPC exceptions.

**Solution**

Create the service again or try again after a period of time and perform related logic judgment. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1017220003 The Number of Files Exceeds the Upper Limit

**Message**

The number of files exceeds the upper limit.

**Description**

The number of added files exceeds the upper limit.

**Possible cause**

1\. The [openFileBoost.addFile](../openfileboost/document.md#section2046715683616) API is called to add a file without calling the [on('filePreloadStateChanged')](../openfileboost/document.md#section298512619713) API.

2\. The number of files added by calling the [openFileBoost.addFile](../openfileboost/document.md#section2046715683616) API is too large. (Currently, a maximum of 50 files can be added.)

**Solution**

1\. Ensure that the [on('filePreloadStateChanged')](../openfileboost/document.md#section298512619713) API is called before calling the [openFileBoost.addFile](../openfileboost/document.md#section2046715683616) API.

2\. Delete the listeners of unnecessary files by calling the [openFileBoost.removeFile](../openfileboost/document.md#section19623053194020) API and try again.
