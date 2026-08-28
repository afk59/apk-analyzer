# Thermal Manager Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/ypL_9OhPSymUg5ULOj_e0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5AAE869DA629C40908BEB9A679124FBA396406399B5D37FBFA7712AE0B539D7C)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 4800101 Service Connection Failure

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
    
2.  Check whether **ThermalService** is included in the system service list.
