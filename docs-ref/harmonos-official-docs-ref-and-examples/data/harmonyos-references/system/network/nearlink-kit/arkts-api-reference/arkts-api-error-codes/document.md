# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/dQgjmnbTTkGBvFdP03PgYw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49EE61B245AF60C233754E6CF3ADC160D77129B934475281AF4D491C81E8CF3B)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 1009700003

**Message**

NearLink is off.

**Description**

This error code is returned if a relevant API is called when NearLink is off.

**Possible causes**

NearLink is not turned on.

**Solution**

Go to **Settings** > **More connectivity options** > **NearLink** on a device (or **Settings** > **NearLink & Bluetooth** > **NearLink** for different products or OS versions), turn on NearLink, and try again. [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) if the issue persists.

#### 1009700020

**Message**

The UUID is already registered.

**Description**

This error code is returned when the port corresponding to the UUID has been registered.

**Possible causes**

The API for registering a port is repeatedly called with the same UUID passed.

**Solution**

Call the **dataTransfer.destroyPort** API to destroy the port corresponding to the UUID, or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1009700021

**Message**

The number of ports exceeds the upper limit.

**Description**

This error code is returned when the number of registered ports exceeds the upper limit.

**Possible causes**

The number of ports allocated for data transfer reaches the upper limit.

**Solution**

Call the **dataTransfer.destroyPort** API to destroy other registered ports, or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1009700023

**Message**

The data writing process is congested.

**Description**

The data sending is abnormal.

**Possible causes**

Data processing congestion occurs at the protocol layer or within the chip architecture.

**Solution**

Control the traffic of data to be written, or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1009700099

**Message**

Operation failed.

**Description**

This error code is returned when an internal processing error occurs in the system.

**Possible causes**

An unknown error occurred.

If the device has been paired, this error code will be returned when you call [startPairing](../remotedevice-capability-to-connect-to-a-remote-device/document.md#section65252361113) to initiate pairing.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).
