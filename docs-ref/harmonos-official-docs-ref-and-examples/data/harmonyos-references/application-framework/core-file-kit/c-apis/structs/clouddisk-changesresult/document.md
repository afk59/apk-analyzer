# CloudDisk\_ChangesResult

typedef struct CloudDisk\_ChangesResult {...} CloudDisk\_ChangesResult

#### Overview

A struct that encapsulates the file change result under the sync root path. It includes the next change sequence number, end flag, and an array of change data items.

**Since**: 21

**Related module**: [CloudDisk](../../modules/clouddisk/document.md)

**Header file**: [oh\_cloud\_disk\_manager.h](../../header-files/oh-cloud-disk-manager-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint64\_t nextUsn{0} | Valid start change sequence number that can be queried next time. |
| bool isEof{false} | Whether the change is the last entry in the sync root path's change history. The value **true** means it is the last one; the value **false** means it is not. |
| size\_t bufferLength{0} | Number of elements in the change history array. |
| [CloudDisk\_ChangeData](../clouddisk-changedata/document.md) changeDatas\[\] | Change history array. |
