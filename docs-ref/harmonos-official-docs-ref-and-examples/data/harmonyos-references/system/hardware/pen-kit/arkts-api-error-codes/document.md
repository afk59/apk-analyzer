# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/jndNkuymTwiTths2koUuhQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062411Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F52B48076527DA619F1DC52FFDA4681FA63F7350CC782B8A0B8DF7127C3A5BF)

This section describes only error codes related to this module. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 1010410001 Internal System Error

**Error message**

internal recognition engine has been released.

**Description**

The internal recognition engine has been released.

**Possible causes**

The recognition engine has been released, but recognition-related APIs are still being called.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1010400001 Loading Failure

**Error message**

load failed.

**Description**

The file fails to be loaded.

**Possible causes**

The file path is incorrect.

**Solution**

Check the path of the file to be loaded and try again, or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1010400002 Saving Failure

**Error message**

save failed.

**Description**

The file fails to be saved.

**Possible causes**

An unknown error occurs.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1013900001 IPC Connection Failure

**Error message**

IPC communication failed.

**Description**

IPC connection fails.

**Possible causes**

The request was blocked by the firewall.

**Solution**

Check the firewall settings and try again, or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1013900002 Insufficient Memory

**Error message**

memory is insufficient.

**Description**

The API fails to be called due to insufficient memory.

**Possible causes**

The memory is insufficient.

**Solution**

Check the cause of memory shortage and try again, or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1013900003 Invalid Service

**Error message**

service is invalid.

**Description**

The service is invalid.

**Possible causes**

An unknown error occurs.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1013900004 Repeated Calling

**Error message**

multi app call.

**Description**

The current API is repeatedly called by the app.

**Possible causes**

This API is called repeatedly before the color pick-up result is returned.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1013900005 Background Service Calling

**Error message**

background service call.

**Description**

Background service calling.

**Possible causes**

The API is called in the background.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).
