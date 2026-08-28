# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/WnoUH7JES1OzygTXxglPGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062349Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1D0D5C60BE6F7B9FE0AA325D4709DECA1207406A788DD851EA2AFBE7EC782A7)

-   This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 1013600001 Internal Error

**Message**

Internal error.

**Description**

Internal error.

**Possible causes**

System processing error. For example, the internal state machine is faulty, or the internal message queue is congested.

**Solution**

Call the API later.

#### 1013600002 System Service Processing Error

**Message**

System service error.

**Description**

System processing error. For example, IPC fails or the network management service fails to be started.

**Possible causes**

IPC error.

**Solution**

Call the API later.

#### 1013620000 Multi-Network Concurrency Not Enabled

**Message**

Multi-path capability is disabled.

**Description**

Multi-network concurrency is not enabled.

**Possible causes**

The network acceleration is turned off, or the airplane mode is turned on.

**Solution**

Ensure that network acceleration is turned on, and the airplane mode is turned off.

#### 1013620001 Multi-Network Concurrency Has Been Activated or Is Being Activated

**Message**

Multi-path links are already active or in the process of being established.

**Description**

Multi-network concurrency has been activated or is being activated.

**Possible causes**

Multi-network concurrency has been activated or is being activated, and cannot be activated again.

**Solution**

Register the multi-network concurrency status change API to learn about the multi-network concurrency information.

#### 1013620002 Multi-Network Concurrency Requests Reached the Upper Limit

**Message**

App request limit reached.

**Description**

The number of multi-network concurrency requests has reached the upper limit.

**Possible causes**

The number of multi-network concurrency requests that can be sent in a day is limited. An error is reported once the upper limit is reached.

**Solution**

Multi-network concurrency requests cannot be initiated currently. Try again 24 hours later.

#### 1013620003 Multi-Network Concurrency Cannot Be Initiated Due To Power Consumption Restrictions

**Message**

Request denied due to power consumption restrictions.

**Description**

Multi-network concurrency cannot be initiated due to power consumption restrictions.

**Possible causes**

In power-sensitive scenarios, when the device is overheated, or under any other conditions where power consumption is deemed inappropriate, multi-network concurrency is not allowed.

**Solution**

Request multi-network concurrency later.

#### 1013620004 Quota Exhausted

**Message**

No quota.

**Description**

The quota is exhausted.

**Possible causes**

The multi-network concurrency quota (session count or duration) specified for the app or device is used up.

**Solution**

Multi-network concurrency requests cannot be initiated currently due to quota exhaustion. Try again 24 hours later.

#### 1013620005 Multi-Network Concurrency Request Conflict

**Message**

Conflict.

**Description**

A multi-network concurrency request conflict occurs.

**Possible causes**

The app cannot request multi-network concurrency currently because the device determines that another higher-priority service is currently using it.

**Solution**

Request multi-network concurrency later.

#### 1013620006 Multi-Network Concurrency Initiated Too Frequently

**Message**

Requests are too frequent.

**Description**

Multi-network concurrency is initiated too frequently.

**Possible causes**

The app requests multi-network concurrency multiple times in a short period of time or starts multi-network concurrency again promptly after releasing it. This will impact the device or network connection.

**Solution**

Check whether multiple multi-network concurrency requests are initiated in a short period of time or multi-network concurrency is started again promptly after it is released. If so, ensure compliance with the principle of minimizing multi-network concurrency usage.

#### 1013620007 No Available Path for Muti-network Concurrency

**Message**

No suitable path.

**Description**

No path other than the current connected path is available for muti-network concurrency.

**Possible causes**

The requested path does not exist, the path signal is poor, the data switch is not turned on, or the smart data switch function is not enabled.

**Solution**

Check whether the signal is poor and ensure that the data switch is turned on.

#### 1013620008 Insufficient Data Traffic Quota

**Message**

Insufficient traffic.

**Description**

The data traffic quota of the device is insufficient.

**Possible causes**

Multi-network concurrency consumes data traffic. It is not allowed if the data traffic quota is insufficient according to the traffic management settings of the device.

**Solution**

Check whether the device is experiencing insufficient data traffic. If the secondary SIM card is expected to be used, enable the unlimited data switch for it.

#### 1013620009 Multi-Network Concurrency Not Supported

**Message**

Concurrency is not allowed.

**Description**

Multi-network concurrency is not supported.

**Possible causes**

The device determines that multi-network concurrency is not supported currently. For example, dual-SIM dual-active (DSDA) is not supported under the current network conditions, or the device does not support multi-network concurrency in dual-SIM scenarios due to hardware restrictions.

**Solution**

Try again later or change a device for testing.

#### 1013620100 Multi-Network Concurrency Release Information Mismatch

**Message**

Release request mismatch.

**Description**

Multi-network concurrency release information mismatch.

**Possible causes**

Multi-network concurrency is initiated by an app different from the one that sends the release request. Ensure that the release request is sent by the same app that initiated multi-network concurrency.

**Solution**

Check whether it was your app that initiated the multi-network concurrency and whether the initiation was successful.

#### 1013620101 Multi-Network Concurrency Not Activated

**Message**

Multi-path not activated.

**Description**

Multi-network concurrency is not activated.

**Possible causes**

Multi-network concurrency is not activated, and it is improper to release it.

**Solution**

Check whether multi-network concurrency is activated.
