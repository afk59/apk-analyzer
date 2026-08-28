# Time and Time Zone Service Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/lFxSm7kXSXOEVwy55ckQ3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=05107F4AF878967106A0D1EDAF2754C62A2C70CCD06362676B834041804E49C8)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### \-1 Time and Time Zone Service Error

**Error Message**

Parameter check failed, permission denied, or system error.

**Description**

This error code is reported when the time and time zone service error occurs.

**Possible Cause**

The system is not running properly due to a common kernel error, such as a memory allocation and multi-thread processing error.

**Solution**

Make sure that the memory is sufficient.

#### 13000001 Network or OS Error

**Error Message**

Network connection error or OS error.

**Description**

This error code is reported when the network or OS error occurs.

**Possible Cause**

The network or OS is not running properly due to a system error, such as network connection failure or socket creation failure.

**Solution**

Make sure the network is connected and the system resources are sufficient.
