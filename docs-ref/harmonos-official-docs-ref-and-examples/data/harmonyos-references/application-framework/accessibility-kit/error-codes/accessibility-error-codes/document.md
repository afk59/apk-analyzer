# Accessibility Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/fUnJpH4STQul_rYEDclSBw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42F865DC6044D80B16C8D0E32B1A12C6CF0B8B10F0732516AD04C85A54D2B574)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 9300003 No Accessibility Permission to Perform the Operation

**Error Message**

No accessibility permission to perform the operation.

**Description**

This error code is reported when an application performs an accessibility operation for which the related permission has not been granted.

**Possible Causes**

The permission for performing the accessibility operation is not granted when the accessibility application is enabled.

**Solution**

1.  Request from the user the permission for performing the accessibility operation, stating the reason for the request.
2.  Have the accessibility application re-enabled and the required accessibility operation enabled.

#### 9300004 Property Not Found

**Error Message**

This property does not exist.

**Description**

This error code is reported when the entered property of the accessibility element does not exist.

**Possible Causes**

The property does not exist in the accessibility element.

**Solution**

Make sure the accessibility element has the target property.

#### 9300005 Operation Not Supported

**Error Message**

This action is not supported.

**Description**

This error code is reported when the application performs an operation that is not supported by the accessibility element.

**Possible Causes**

The accessibility element does not support the target operation.

**Solution**

Make sure the operation is included in the list of operations supported by the accessibility element.

#### 9300006 Failed to Connect the Target Application and Accessibility Services

**Error Message**

The connection between the target application and accessibility services failed.

**Description**

This error code is reported when the connection handle between the target application and the accessibility framework does not exist.

**Possible Causes**

The target application has not registered the connection with the accessibility framework service.

**Solution**

Call this method later.

#### 9300007 Failed to Trigger Amplification

**Error Message**

Trigger magnification failed.

**Description**

This error code is reported when the amplification feature fails to be triggered.

**Possible Causes**

1.  The amplification feature is not enabled.
2.  The amplification mode is not configured.

**Solution**

Enable the amplification feature and configure the amplification mode.
