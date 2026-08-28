# FileShare\_PolicyInfo

typedef struct FileShare\_PolicyInfo {...} FileShare\_PolicyInfo

#### Overview

Represents the permission policy information.

**Since**: 12

**Related module**: [fileShare](../../modules/fileshare/document.md)

**Header file**: [oh\_file\_share.h](../../header-files/oh-file-share-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char \*uri | Pointer to the URI, on which the permission is to be granted or activated. |
| unsigned int length | Length of the URI, in bytes. |
| unsigned int operationMode | 
URI operation mode.

Example:

FileShare\_OperationMode.READ\_MODE

FileShare\_OperationMode.WRITE\_MODE

Or FileShare\_OperationMode.READ\_MODE|FileShare\_OperationMode.WRITE\_MODE

 |
