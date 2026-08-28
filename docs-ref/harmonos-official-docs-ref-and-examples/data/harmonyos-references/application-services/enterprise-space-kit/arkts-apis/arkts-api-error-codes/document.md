# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/2WFzR6Q6Ra-aqAxkqniy6g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062506Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD92749A55DC593B2C2DB2064E7C26CB362F9FAF088285FF7337486F550C0D53)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references-V13/errorcode-universal-V13). If any error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1020300001 System Service Exception

**Message**

System service exception.

**Description**

System service exception.

**Possible causes**

The workspace ID is invalid, or the file processing type is unknown.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1020300002 Invalid Request Parameter

**Message**

Parameter error.

**Description**

Invalid request parameter.

**Possible causes**

A mandatory parameter is left empty or the parameter type is incorrect.

**Solution**

Ensure that the parameters are set correctly.

#### 1020400001 System Service Exception

**Message**

System service exception.

**Description**

System service exception.

**Possible causes**

System services are busy, or the network is abnormal.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1020400002 Invalid Request Parameter

**Message**

Parameter error.

**Description**

Invalid request parameter.

**Possible causes**

A mandatory parameter is left empty or the parameter type is incorrect.

**Solution**

Ensure that the parameters are set correctly.

#### 1020400003 Invalid Workspace

**Message**

Invalid workspace.

**Description**

The workspace is invalid.

**Possible causes**

1.  The workspace does not exist.
2.  The workspace already exists.
3.  The workspace type is not supported.
4.  The number of workspaces has reached the upper limit.

**Solution**

Refer to [WorkspaceInfo](../spacemanager-workspace-management/document.md#section1528202625516) to ensure that all workspace information meets the requirements.

#### 1020400005 Configuration Not Set

**Message**

Configuration not set.

**Description**

The configuration was not set.

**Possible causes**

During the query, it was found that the configuration had not been set.

**Solution**

Ensure that the configuration is properly set.

#### 1020400006 SA Process Exited Unexpectedly, Interrupting the Connection

**Message**

Session disconnected.

**Description**

The SA process exited unexpectedly, interrupting the connection.

**Possible causes**

An app subscribes to a workspace event, causing the process to exit abnormally.

**Solution**

Re-subscribe to the workspace event.

#### 1020400007 Enterprise Workspace Not Enabled

**Message**

Enterprise workspace not enabled.

**Description**

The enterprise workspace is not enabled.

**Possible causes**

The enterprise administrator has not enabled the enterprise workspace function yet.

**Solution**

Enable the enterprise workspace function as the enterprise administrator.
