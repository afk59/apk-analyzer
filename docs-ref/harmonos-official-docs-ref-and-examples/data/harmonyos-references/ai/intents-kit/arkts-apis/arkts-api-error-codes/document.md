# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/iPqiUo2BSGmiPBNF9mrSSA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062523Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FAB9AEFBADA899E763DD0FB7CF85DB847A5D58CA93F936F4280552FED073A90E)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 1000101101 App Not Registered

**Message**

The application has not been registered with the InsightIntent.

**Description**

This error code is generated if the app has not been registered with **InsightIntent**.

**Possible causes**

The app has not been registered with **InsightIntent** (the app has not been added to the trustlist).

**Solution**

Follow instructions in the [development guide](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/intents-access-flow) to register with **InsightIntent** (that is, add the app to the trustlist).

#### 1000101102 Celia Is Not Working

**Message**

HUAWEI Assistant has stopped providing services.

**Description**

This error code is generated when intent sharing fails because Celia is not working.

**Possible causes**

Celia has not been enabled.

**Solution**

Enable Celia.

#### 1000101104 Number of Sharings from an App Exceeding the Limit

**Message**

The number of sharing times exceeds the limit.

**Description**

This error code is generated if the number of sharings from an app exceeds the limit.

**Possible causes**

The app performs sharing too frequently.

**Solution**

Optimize the business logic of the app to reduce the number of sharings.

#### 1000101105 Size of Data Shared at a Time Exceeding the Limit

**Message**

The size of a single shared data exceeds the limit.

**Description**

This error code is generated if the size of data shared at a time exceeds the specified limit.

**Possible causes**

The amount of data shared at a time is too large.

**Solution**

Reduce the amount of data shared at a time.

#### 1000101106 Number of Sharings from All Apps Exceeding the Limit

**Message**

Exceeded the maximum number of sharing times of all applications.

**Description**

This error code is generated if the total number of sharings from all apps exceeds the daily limit.

**Possible causes**

The total number of sharings from all apps exceeds the daily limit.

**Solution**

Postpone excess sharings to the next day.

#### 1000101107 Excessive SID Update Requests

**Message**

Too many Service Open ID renew requests.

**Description**

This error code is generated when the number of SID update requests exceeds the limit.

**Possible causes**

SID update requests are sent too frequently.

**Solution**

Postpone excess requests to the next day, or set **renew** to **false** to obtain the cached SID.

#### 1000101201 Service Abnormal

**Message**

The service is abnormal.

**Description**

This error code is generated if the service is abnormal.

**Possible causes**

A system error occurs.

**Solution**

Restart the system and try again.
