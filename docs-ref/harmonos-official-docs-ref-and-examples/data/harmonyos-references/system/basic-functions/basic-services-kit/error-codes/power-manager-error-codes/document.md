# Power Manager Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/y6yh0vDvTfidOMLx2-vPNg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4298123752CB785609B9FB47976D7E73EDB541BF48439EF134A86868385F39D7)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 4900101 Service Connection Failure

**Error Message**

Failed to connect to the service.

**Description**

This error code is reported if a service connection failure occurs.

**Possible Causes**

1.  The system service stops running.
    
2.  The internal communication of system services is abnormal.
    

**Procedure**

Check whether the system services are running properly.

1.  Run the following command on the console to view the current system service list:
    
    \> hdc shell hidumper -ls
    
2.  Check whether **PowerManagerService** is included in the system service list.
    

#### 4900102 System Shutting Down

**Error Message**

Operation failed. The system is shutting down.

**Description**

This error code is reported when an operation failed during system shutting down.

**Possible Causes**

The system is shutting down.

**Procedure**

Make sure that the operation is performed when the system is running properly.

#### 4900201 Frequent Status Refreshes

**Error Message**

The device activity is being refreshed too frequently; the minimum time interval is 100 ms.

**Description**

This error code is reported if the refresh of the device activity status fails due to short intervals (< 100 ms).

**Possible Causes**

The device activity status is frequently refreshed.

**Procedure**

No more refresh is needed if the device activity status has been refreshed within 100 ms. Try another refresh 100 ms later.
