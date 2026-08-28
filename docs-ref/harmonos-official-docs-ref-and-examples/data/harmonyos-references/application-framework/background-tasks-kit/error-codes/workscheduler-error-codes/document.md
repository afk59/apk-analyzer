# workScheduler Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/VA4lBWVuTAOjNJEOstELng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C31001A5C4CA942C25B4EF776230953935F53A165F155345B12F798B5F6B91B)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 9700001 Memory Operation Failure

**Error Message**

Memory operation failed.

**Description**

This error code is reported when a memory operation fails.

**Possible Causes**

1.  A memory leak occurs.
2.  The system memory is insufficient.

**Solution**

1.  Release the memory.
2.  Check whether memory leak occurs.

#### 9700002 Parcel Operation Failure

**Error Message**

Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory.

**Description**

This error code is reported when parcel data fails to be read or written during IPC.

**Possible Causes**

1.  The data object fails to be read or written during IPC.
2.  The memory fails to be allocated for the read or write operation.

**Solution**

Try again later or restart the device.

#### 9700003 System Service Failure

**Error Message**

System service operation failed.

**Description**

This error code is reported when the client process fails to obtain the system service.

**Possible Causes**

1.  The system service is not started.
2.  The system service is abnormal.

**Solution**

Try again later or restart the device.

#### 9700004 workInfo Verification Failure

**Error Message**

Check on workInfo failed.

**Description**

This error code is reported when the **workInfo** parameter is abnormal.

**Possible Causes**

1.  The value of **bundleName** in **workInfo** does not match the UID of the application.
2.  The Work Scheduler task to cancel or query does not exist.

**Solution**

Check the **workInfo** parameters.

#### 9700005 startWork Call Failure

**Error Message**

Calling startWork failed.

**Description**

This error code is reported when the request for a deferred task fails.

**Possible Causes**

1.  The Work Scheduler task already exists.
2.  The application has already requested 10 Work Scheduler tasks.
3.  The repeat interval of a Work Scheduler task must be at least 20 minutes.

**Solution**

Check the input parameters and application code.
