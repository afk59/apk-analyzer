# CloudDisk\_ChangeData

typedef struct CloudDisk\_ChangeData  {...} CloudDisk\_ChangeData

#### Overview

A struct that encapsulates the event data generated when a single file under the sync root path is changed. It includes the file's unique ID, the parent directory's unique ID, relative path, change type, file size, and timestamp.

**Since**: 21

**Related module**: [CloudDisk](../../modules/clouddisk/document.md)

**Header file**: [oh\_cloud\_disk\_manager.h](../../header-files/oh-cloud-disk-manager-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint64\_t updateSequenceNumber{0} | Update sequence number of the change event. It is incremented by 1 monotonically each time a file is changed, and is used for incremental change query. Value range: \[0, 2^64 – 1\] |
| CloudDisk\_FileIdInfo fileId | Globally unique file ID. It remains unchanged within the lifecycle of the file. |
| CloudDisk\_FileIdInfo parentFileId | Unique ID of the parent directory to which the file or directory belongs. |
| [CloudDisk\_PathInfo](../clouddisk-pathinfo/document.md) relativePathInfo | Relative path of the file under the sync root path. |
| [CloudDisk\_OperationType](../../header-files/oh-cloud-disk-manager-h/document.md#clouddisk_operationtype) operationType | Change operation type of the file (for example, create, delete, and move). |
| uint64\_t size{0} | File size, in bytes. |
| uint64\_t mtime{0} | File modification time, in milliseconds. |
| uint64\_t timeStamp{0} | Time when a change event occurs, in milliseconds. |
