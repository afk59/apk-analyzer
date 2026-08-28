# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/cIbcQUslR5C1qI75-Nvwjg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E9DECCE9228C1E0FBEA850682626CBD15DF620E6853F1E330E27DC8F982EE34)

This section describes only error codes related to this module. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md)

#### 1007200001 Invalid Parameter

**Error Message**

Invalid parameter value.

**Description**

Incorrect parameter settings.

**Possible Cause**

1\. The number of parameters is incorrect. For example, mandatory parameters are not passed.

2\. The call status is incorrect. The most common error is that an outgoing call is not reported because its status is not set to **VOIP\_CALL\_STATE\_DIALING**.

3\. The call type is incorrect. Currently, only **VOIP\_CALL\_VOICE** (voice calls) and **VOIP\_CALL\_VIDEO** (video calls) are supported.

4\. The call ID does not match the call. For example, when a call status change or audio status change is reported, if the passed call ID cannot be found in the call record, the report will fail.

5\. The call is repeatedly reported. For example, if an outgoing call is reported twice, the second report fails.

**Solution**

1\. Ensure that the preceding parameters are correctly passed.

2\. [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei technical support will get back to you as soon as possible.

#### 1007200002 Service Not Started

**Error Message**

Operation failed. Cannot connect to service.

**Description**

Call Service Kit is not started.

**Possible Cause**

Call Service Kit fails to be started after the API is called.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei technical support will get back to you as soon as possible.

#### 1007200003 Internal Error

**Error Message**

System internal error.

**Description**

Call Service Kit encounters an internal error.

**Possible Cause**

1\. The number of calls exceeds the upper limit. A maximum of three incoming calls and one outgoing call are allowed. Otherwise, an error will be reported.

2\. The call conflicts with a carrier call. For example, an outgoing in-app call cannot be initiated when a carrier call is in progress.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei technical support will get back to you as soon as possible.

#### 1007200099 Unknown Error

**Error Message**

Unknown error code.

**Description**

Call Service Kit encounters an unknown error.

**Possible Cause**

Unknown.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei technical support will get back to you as soon as possible.
