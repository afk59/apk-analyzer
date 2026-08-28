# Render State Listening Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/Nb3SIa7bRkCINUy7CJHN5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062311Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F602178F82D7C3BB3B8C4E6AFA8E43EA5D22F42F7A79E2A6017D794EC1E0753)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 161001 Number of Nodes Listening for Render State Exceeds the Limit

**Error Message**

The count of nodes monitoring render state is over the limitation.

**Description**

This error code is reported when the number of nodes registered to listen for render state exceeds the system limit.

**Possible Causes**

The number of nodes listening for render state exceeds the maximum allowed limit.

**Solution**

Ensure that less than 64 nodes are registered to listen for render state.
