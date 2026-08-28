# CloudDisk\_FailedList

typedef struct CloudDisk\_FailedList {...} CloudDisk\_FailedList

#### Overview

A struct that encapsulates the list of files that failed to synchronize. It includes the file path information and the specific failure cause.

**Since**: 21

**Related module**: [CloudDisk](../../modules/clouddisk/document.md)

**Header file**: [oh\_cloud\_disk\_manager.h](../../header-files/oh-cloud-disk-manager-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [CloudDisk\_PathInfo](../clouddisk-pathinfo/document.md) pathInfo | Absolute path information of the file that failed to synchronize. |
| [CloudDisk\_ErrorReason](../../header-files/oh-cloud-disk-manager-h/document.md#clouddisk_errorreason) errorReason | Reason why the file fails to be synchronized. |
