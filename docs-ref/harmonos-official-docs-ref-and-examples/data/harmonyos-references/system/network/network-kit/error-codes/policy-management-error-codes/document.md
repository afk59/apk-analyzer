# Policy Management Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/-cS2i2TLTAyu-MlpZcHfCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062349Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D407134CAF90EDC3916CAD8883C7CDF90E9508BA21B7A867D9573CA4E81478A8)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 2100001 Invalid Parameters

**Error Message**

Invalid parameter value.

**Description**

This error code is reported if any input parameter value is incorrect.

**Cause**

The end time is earlier than the start time.

**Procedure**

Check whether the start time and end time are properly set.

#### 2100002 Service Connection Failure

**Error Message**

Failed to connect to the service.

**Description**

This error code is reported if a service connection failure occurs.

**Cause**

The service is abnormal.

**Procedure**

Check whether system services are running properly.

#### 2100003 System Internal Error

**Error Message**

System internal error.

**Description**

This error code is reported if a system internal error occurs.

**Cause**

1.  The memory is abnormal.
    
2.  A null pointer is present.
    

**Procedure**

1.  Check whether the memory space is sufficient. If not, clear the memory and try again.
    
2.  Check whether the system is normal. If not, try again later or restart the device.
