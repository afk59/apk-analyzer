# Mechanic Manager Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/v1g4zwJXTVi6cl9yY9ShpQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=501AF4EAAA22CC671C4A7399C4462827E49C6D01BAA50B172EA36A3ACDA7775C)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 33300001 System Error

**Error Message**

Service exception.

**Description**

This error code is reported if a system error occurs.

**Possible Causes**

An unrecoverable error occurs in the service logic processing on the server.

**Solution**

The system error cannot be rectified.

#### 33300002 Device Not Connected

**Error Message**

Device not connected.

**Description**

This error code is reported if the mechanical device is not connected.

**Possible Causes**

No connected device is available.

**Solution**

Ensure that the development device is properly connected to the mechanical device through Bluetooth.

#### 33300003 Function Not Supported

**Error Message**

Feature not supported.

**Description**

This error code is reported if the function is not supported by the current development device.

**Possible Causes**

The camera driver of the current development device does not support the object detection function.

**Solution**

Add the object detection function to the camera driver of the current development device or replace the development device with one that supports the object detection function.
