# CloudDisk\_ResultList

typedef struct CloudDisk\_ResultList {...} CloudDisk\_ResultList

#### Overview

A struct that encapsulates the file sync result. It includes the absolute path of the file, sync result, and sync state or failure cause.

**Since**: 21

**Related module**: [CloudDisk](../../modules/clouddisk/document.md)

**Header file**: [oh\_cloud\_disk\_manager.h](../../header-files/oh-cloud-disk-manager-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [CloudDisk\_PathInfo](../clouddisk-pathinfo/document.md) pathInfo | Absolute path information of the file. |
| bool isSuccess{false} | Whether the operation is successful. The value **true** indicates the operation is successful; the value **false** (default) indicates the opposite. |
| [CloudDisk\_SyncState](../../header-files/oh-cloud-disk-manager-h/document.md#clouddisk_syncstate) syncState | File sync state. It takes effect only when **isSuccess** is set to true. |
| [CloudDisk\_ErrorReason](../../header-files/oh-cloud-disk-manager-h/document.md#clouddisk_errorreason) errorReason | Reason why the file sync state fails to be obtained. It takes effect only when **isSuccess** is set to **false**. |
