# FileShare\_PolicyErrorResult

typedef struct FileShare\_PolicyErrorResult {...} FileShare\_PolicyErrorResult

#### Overview

Represents the permission policy error result.

**Since**: 12

**Related module**: [fileShare](../../modules/fileshare/document.md)

**Header file**: [oh\_file\_share.h](../../header-files/oh-file-share-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char \*uri | Pointer to the URI, on which the permission fails to be granted or activated. |
| [FileShare\_PolicyErrorCode](../../header-files/oh-file-share-h/document.md#fileshare_policyerrorcode) code | Error code corresponding to the URI. |
| char \*message | Pointer to the error message. |
