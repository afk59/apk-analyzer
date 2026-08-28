# BusinessRiskIntelligentDetection

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/vFX1g4z0SU-EntpNnmNm9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062334Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A77F8F73A941F36B95704ED8ECE6A3812231B44A2AF9B7F148D67DF92113AF2A)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

#### 1012500001 Internal Error

**Message**

Internal error.

**Description**

Internal error.

**Possible causes**

The number of API calls exceeds the upper limit, or an exception occurred when other system APIs are called in the API execution process.

**Solution**

Try again first. If the retry fails, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1012500002 Device Network Error

**Message**

The network is unreachable.

**Description**

Device network error.

**Possible causes**

The device is not connected to the network.

**Solution**

Connect to the network and send the request again.

#### 1012500003 An Exception Occurred When Accessing the Cloud Server

**Message**

Access cloud server fail.

**Description**

An exception occurred when accessing the cloud server.

**Possible causes**

The cloud service is unstable or faulty.

**Solution**

Send the request again.

#### 1012500004 Permission Verification Failed

**Message**

Verify cloud capability fail.

**Description**

Permission verification failed.

**Possible causes**

Device Security Kit has not been enabled for the HAP.

**Solution**

Enable Device Security Kit in AppGallery Connect by referring to [Enabling Device Security Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice). Then try again.

#### 1012500005 API Calls Reaching Upper Limit

**Message**

The interface access frequency exceeds the limit.

**Description**

The number of API calls exceeds the upper limit.

In 6.0.0(20) and later versions, this error code is returned if the number of API calls exceeds the upper limit.

**Possible causes**

The number of times that an API is called by an app exceeds the upper limit in the current period. For details, please refer to [Service Quota](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-quota).

**Solution**

Call the API again in the next period.

#### 1012500006 API Call Timeout

**Message**

Internal timeout.

**Description**

The API call times out.

**Possible causes**

The call to the specific API times out.

**Solution**

Call the API again.

#### 1012500007 Parameter Check Failed

**Message**

Invalid parameters.

**Description**

Parameter check failed.

This error code is added since version 6.0.0(20).

**Possible causes**

A mandatory parameter is missing, or the parameter type or value is incorrect.

**Solution**

Make sure all the mandatory parameters are passed and the parameter types and values are correct.
