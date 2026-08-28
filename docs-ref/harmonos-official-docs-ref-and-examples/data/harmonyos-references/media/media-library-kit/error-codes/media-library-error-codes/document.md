# Media Library Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/j4DdMlHgRxOsUZQ5tznxzQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062444Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2CDAB0CB910C854885626E9A48FA6A558DB50471AF424259A603455AAB604DC6)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 23800301 System Internal Error

**Error Message**

System inner fail.

**Description**

This error code is reported if an internal error occurs in the media library.

**Possible Causes**

1.  The database is abnormal.
    
2.  The file system is abnormal.
    
3.  The IPC message times out.
    

**Solution**

Clear the background or restart the device.

#### 23800151 Failed to Verify Scene Parameters

**Error Message**

Scene parameter validation failed.

**Description**

This error code is reported if a parameter is abnormal.

**Possible Causes**

1.  Mandatory parameters do not meet the specified range.
    
2.  The provided record already exists.
    
3.  The number of provided records exceeds the maximum allowed.
    

**Solution**

Check the parameter values and ensure they meet the required criteria.

#### 23800104 Input Parameter Verification Failure

**Error Message**

The provided member must be a property name of PhotoKey.

**Description**

This error code is reported if a parameter is abnormal.

**Possible Causes**

This error code is reported if the parameter is not within the range of the [PhotoKeys](../../arkts-apis/ohos-file-photoaccesshelper-album-management/enums/document.md#photokeys) enum.

**Solution**

Ensure that the input parameter is within the range of the PhotoKeys enum.
