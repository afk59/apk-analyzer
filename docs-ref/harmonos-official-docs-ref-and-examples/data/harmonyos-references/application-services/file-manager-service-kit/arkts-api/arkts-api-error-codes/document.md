# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/wUnupm3uTtK8_SgMCil6TA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062506Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDE09CAD03900924AD5F9BF26E96D94CEC0DA571FD6B77E75DDA2CED2FB7C877)

This section describes only error codes related to this module. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md)

#### 1014000001 Operation Not Permitted

**Error message**

Operation not permitted

**Description**

The operation is not permitted.

**Possible cause**

The operation on the user's file is not permitted because the caller does not have the permission to access the file URI or path.

**Solution**

1\. Use **FilePicker** to [select the user file](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/select-user-file) to obtain the temporary URI permission.

2\. [Request user authorization](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/request-user-authorization) to access the directory through the program access control mechanism.

#### 1014000002 No Such File or Directory

**Error message**

No such file or directory

**Description**

The file or directory cannot be found.

**Possible cause**

The file or directory does not exist.

**Solution**

Ensure that the file path exists.

#### 1014000003 Insufficient Storage Space

**Error message**

No space left on device

**Description**

Insufficient storage space.

**Possible cause**

Insufficient storage space.

**Solution**

Clear up the storage space on the device.

#### 1014000004 Internal System Error

**Error message**

System inner fail

**Description**

An internal system error occurs.

**Possible cause**

The system is malfunctioning due to an error.

**Solution**

Reboot the device or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).
