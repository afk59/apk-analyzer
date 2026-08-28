# CloudDisk\_PathInfo

typedef struct CloudDisk\_PathInfo {...} CloudDisk\_PathInfo
typedef struct CloudDisk\_PathInfo CloudDisk\_FieldInfo
typedef struct CloudDisk\_PathInfo CloudDisk\_SyncFolderPath

#### Overview

A struct that encapsulates the file path information.

**Since**: 21

**Related module**: [CloudDisk](../../modules/clouddisk/document.md)

**Header file**: [oh\_cloud\_disk\_manager.h](../../header-files/oh-cloud-disk-manager-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char \*value | Pointer to the file path, which ends with '\\0'. |
| size\_t length | Length of the file path, excluding the '\\0' character at the end. |
