# SafetyDetect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/2xwR9dIbSGmoD5567Lpjrw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062334Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B976110EB0FDDA8934BE33590EA927E8088DB74E9B20D3CEC4991BE868AA3403)

This section describes only module-specific client error codes and provides the cause analysis. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 201 Permission Verification Failed

**Description**

Permission verification failed.

**Possible causes**

Device Security Kit has not been enabled for the HAP.

**Solution**

1.  Enable **Safety Detect** in AppGallery Connect. For details, please refer to [Enabling Device Security Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice).
2.  [Request a new profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-debugprofile-0000001914423102), and use it as the signature file of the project to try again.

#### 401 Parameter Check Failed

**Description**

Parameter check failed.

**Possible causes**

A mandatory parameter is missing, or the parameter type or specifications are invalid.

**Solution**

Make sure all the mandatory parameters are passed and the parameter types and specifications are valid.

#### 801 API Not Supported

**Description**

This API is not supported on the current device.

This error code is added since version 5.1.0(18).

**Possible causes**

The current device does not support this function.

**Solution**

Do not call this API on devices that do not support this API.

#### 1010800001 Internal Error

**Description**

Internal error.

**Possible causes**

An exception occurred when other system APIs are called in the API execution process.

**Solution**

Try again first. If the retry fails, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1010800002 Device Network Error

**Description**

Device network error.

**Possible causes**

The device is not connected to the network.

**Solution**

Connect to the network and send the request again.

#### 1010800003 An Exception Occurred When Accessing the Cloud Server

**Description**

An exception occurred when accessing the cloud server.

**Possible causes**

The cloud service is unstable or faulty.

**Solution**

Send the request again.

#### 1010800004 Capability Verification Failure

**Description**

The SafetyDetect service is not enabled for the app.

**Possible causes**

The SafetyDetect service is not enabled for the app.

**Solution**

Enable the SafetyDetect service.

1.  Enable **Safety Detect** in AppGallery Connect. For details, please refer to [Enabling Device Security Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice).
2.  [Request a new profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-debugprofile-0000001914423102), and use it as the signature file of the project to try again.

#### 1010800005 Number of Concurrent API Calls Exceeds Upper Limit

**Description**

The number of concurrent API calls exceeds the upper limit.

This error code is added since version 5.1.0(18).

**Possible causes**

Your app or other apps concurrently call the API, resulting in that the number of API calls exceeds the upper limit.

A maximum of five concurrent calls are supported on each device.

**Solution**

You are advised to retry after a while, for example, 1 second.

#### 1010800006 API Call Frequency Exceeds Upper limit

**Description**

The number of times that the API is called within the specified time exceeds the upper limit.

This error code is added since version 5.1.0(18).

Each app can call the system integrity check API for up to 10,000 times per day and five times per minute on each device.

**Possible causes**

The API is called too many times in the specified time.

**Solution**

Adjust your API call frequency based on the frequency limit. Call the API again in the next statistical period.

#### 1010800007 Operation Timeout

**Description**

The API execution timed out.

This error code is added since version 5.1.0(18).

**Possible causes**

The system is overloaded or the network is congested.

**Solution**

Send the request again.

#### 1010800008 Cloud Service Traffic Exceeds Threshold

**Description**

The number of cloud service requests exceeds the threshold.

This error code is added since version 5.1.0(18).

**Possible causes**

A large number of devices call cloud service APIs at the same time.

**Solution**

You are advised to retry after a while, for example, 5 seconds. If the retry fails again, retry with an exponentially increasing interval each time.
