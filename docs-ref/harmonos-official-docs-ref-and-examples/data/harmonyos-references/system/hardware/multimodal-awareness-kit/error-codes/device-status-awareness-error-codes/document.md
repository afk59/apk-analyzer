# Device Status Awareness Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/wjGRw6dETcG2uYpTdMFXhQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062410Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72824114ECA678E71BD6A86B947BCD70B502990ACCFCD8933D0649FB80398486)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 32500001 Abnormal Service

**Error Message**

Service exception.

**Symptom**

This error code is reported if a service exception occurs when the **on** or **off** API of the deviceStatus module is called.

**Possible Causes**

The service status is abnormal.

**Solution**

1.  Retry the operation at a specified interval (for example, 1s) or at an exponential increase interval.
2.  If the operation fails for three consecutive times, stop the retry. You can also attempt to obtain the sensor list to check for device availability.

#### 32500002 Subscription Failed

**Error Message**

Subscribe Failed.

**Symptom**

This error code is reported if subscription fails when the **on** API of the deviceStatus module is called.

**Possible Causes**

Subscription to change events has failed.

**Solution**

1.  Retry the operation at a specified interval (for example, 1s) or at an exponential increase interval.
2.  If the operation fails for three consecutive times, stop the retry.

#### 32500003 Unsubscription Failed

**Error Message**

UnSubscribe Failed.

**Symptom**

This error code is reported if unsubscription fails when the **off** API of the deviceStatus module is called.

**Possible Causes**

Unsubscription from change events has failed.

**Solution**

1.  Retry the operation at a specified interval (for example, 1s) or at an exponential increase interval.
2.  If the operation fails for three consecutive times, stop the retry.
