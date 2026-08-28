# Running Lock Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/_6pTkxV9SG6uAzRmrceF_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F50F6901DA02993A4AB2FB31E06173B1D3C324DFCCED223A4C2CA77F4FD0D682)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 4900101 Service Connection Failure

**Error Message**

Failed to connect to the service.

**Description**

This error code is reported if a service connection failure occurs.

**Possible causes**

1.  The system service stops running.
    
2.  The internal communication of system services is abnormal.
    

**Solution**

Check whether the system services are running properly.

1.  Run the following command on the console to view the current system service list:
    
    \> hdc shell hidumper -ls
    
2.  Check whether **PowerManagerService** is included in the system service list.
