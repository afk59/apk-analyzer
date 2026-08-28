# oh\_file\_share.h

#### Overview

Provides APIs for persisting permissions, activating or deactivating persistent permissions, and checking the persistent permissions on files or directories based on their URIs.

**File to include**: <filemanagement/fileshare/oh\_file\_share.h>

**Library**: libohfileshare.so

**System capability**: SystemCapability.FileManagement.AppFileService.FolderAuthorization

**Since**: 12

**Related module**: [fileShare](../../modules/fileshare/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [FileShare\_PolicyErrorResult](../../structs/fileshare-policyerrorresult/document.md) | FileShare\_PolicyErrorResult | Represents the permission policy error result. |
| [FileShare\_PolicyInfo](../../structs/fileshare-policyinfo/document.md) | FileShare\_PolicyInfo | Represents the permission policy information. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [FileShare\_OperationMode](#fileshare_operationmode) | FileShare\_OperationMode | Enumerates the URI operation mode. |
| [FileShare\_PolicyErrorCode](#fileshare_policyerrorcode) | FileShare\_PolicyErrorCode | Enumerates the error codes for a permission policy. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [FileManagement\_ErrCode OH\_FileShare\_PersistPermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum)](#oh_fileshare_persistpermission) | Persists the permissions on files or directories. |
| [FileManagement\_ErrCode OH\_FileShare\_RevokePermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum)](#oh_fileshare_revokepermission) | Revokes the permissions from files or directories. |
| [FileManagement\_ErrCode OH\_FileShare\_ActivatePermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum)](#oh_fileshare_activatepermission) | Activates the persistent permissions on files or directories. |
| [FileManagement\_ErrCode OH\_FileShare\_DeactivatePermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum)](#oh_fileshare_deactivatepermission) | Deactivates the persistent permissions on files or directories. |
| [FileManagement\_ErrCode OH\_FileShare\_CheckPersistentPermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, bool \*\*result, unsigned int \*resultNum)](#oh_fileshare_checkpersistentpermission) | Checks the persistent permissions on files or directories. |
| [void OH\_FileShare\_ReleasePolicyErrorResult(FileShare\_PolicyErrorResult \*errorResult, unsigned int resultNum)](#oh_fileshare_releasepolicyerrorresult) | Releases the memory, to which **FileShare\_PolicyErrorResult** points. |

#### Enum Description

#### \[h2\]FileShare\_OperationMode

enum FileShare\_OperationMode

**Description**

Enumerates the URI operation mode.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| READ\_MODE = 1 << 0 | Read. |
| WRITE\_MODE = 1 << 1 | Write. |

#### \[h2\]FileShare\_PolicyErrorCode

enum FileShare\_PolicyErrorCode

**Description**

Enumerates the error codes for a permission policy.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| PERSISTENCE\_FORBIDDEN = 1 | The permission on the URI cannot be persisted. |
| INVALID\_MODE = 2 | Invalid mode. |
| INVALID\_PATH = 3 | Invalid path. |
| PERMISSION\_NOT\_PERSISTED = 4 | The permission is not persisted. |

#### Function Description

#### \[h2\]OH\_FileShare\_PersistPermission()

FileManagement\_ErrCode OH\_FileShare\_PersistPermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum)

**Description**

Persists the permissions on files or directories.

**Required permissions**: ohos.permission.FILE\_ACCESS\_PERSIST

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const FileShare\_PolicyInfo](../../structs/fileshare-policyinfo/document.md) \*policies | Pointer to a **FileShare\_PolicyInfo** instance. |
| unsigned int policyNum | Number of policies in the **FileShare\_PolicyInfo** array. |
| [FileShare\_PolicyErrorResult](../../structs/fileshare-policyerrorresult/document.md) \*\*result | Double pointer to the **FileShare\_PolicyErrorResult** array. Use **OH\_FileShare\_ReleasePolicyErrorResult()** to release the memory allocated. |
| unsigned int \*resultNum | Pointer to the size of the **FileShare\_PolicyErrorResult** array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [FileManagement\_ErrCode](../error-code-h/document.md#filemanagement_errcode) | 
Returns [FileManagement\_ErrCode](../error-code-h/document.md#filemanagement_errcode).

ERR\_INVALID\_PARAMETER 401 - The input parameter is invalid. Possible causes:

1\. The **policies**, **result**, or **resultNum** parameter is a null pointer.

2\. The value of **policyNum** is **0** or exceeds the maximum length (500).

3\. The value of **uri** in the **policies** parameter is empty, the value of **length** is **0**, or the value of **uri** is different from the value of **length**.

ERR\_DEVICE\_NOT\_SUPPORTED 801 - The device does not support this API.

ERR\_PERMISSION\_ERROR 201 - The permission verification fails.

ERR\_ENOMEM 13900011 - The memory allocation or copy fails.

ERR\_EPERM 13900001 - The operation is not allowed.

ERR\_OK 0 - The API is called successfully.

 |

#### \[h2\]OH\_FileShare\_RevokePermission()

FileManagement\_ErrCode OH\_FileShare\_RevokePermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum)

**Description**

Revokes the permissions from files or directories.

**Required permissions**: ohos.permission.FILE\_ACCESS\_PERSIST

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const FileShare\_PolicyInfo](../../structs/fileshare-policyinfo/document.md) \*policies | Pointer to a **FileShare\_PolicyInfo** instance. |
| unsigned int policyNum | Number of policies in the **FileShare\_PolicyInfo** array. |
| [FileShare\_PolicyErrorResult](../../structs/fileshare-policyerrorresult/document.md) \*\*result | Double pointer to the **FileShare\_PolicyErrorResult** array. Use **OH\_FileShare\_ReleasePolicyErrorResult()** to release the memory allocated. |
| unsigned int \*resultNum | Pointer to the size of the **FileShare\_PolicyErrorResult** array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [FileManagement\_ErrCode](../error-code-h/document.md#filemanagement_errcode) | 
Returns [FileManagement\_ErrCode](../error-code-h/document.md#filemanagement_errcode).

ERR\_INVALID\_PARAMETER 401 - The input parameter is invalid. Possible causes:

1\. The **policies**, **result**, or **resultNum** parameter is a null pointer.

2\. The value of **policyNum** is **0** or exceeds the maximum length (500).

3\. The value of **uri** in the **policies** parameter is empty, the value of **length** is **0**, or the value of **uri** is different from the value of **length**.

ERR\_DEVICE\_NOT\_SUPPORTED 801 - The device does not support this API.

ERR\_PERMISSION\_ERROR 201 - The permission verification fails.

ERR\_ENOMEM 13900011 - The memory allocation or copy fails.

ERR\_EPERM 13900001 - The operation is not allowed.

ERR\_OK 0 - The API is called successfully.

 |

#### \[h2\]OH\_FileShare\_ActivatePermission()

FileManagement\_ErrCode OH\_FileShare\_ActivatePermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum)

**Description**

Activates the persistent permissions on files or directories.

**Required permissions**: ohos.permission.FILE\_ACCESS\_PERSIST

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const FileShare\_PolicyInfo](../../structs/fileshare-policyinfo/document.md) \*policies | Pointer to a **FileShare\_PolicyInfo** instance. |
| unsigned int policyNum | Number of policies in the **FileShare\_PolicyInfo** array. |
| [FileShare\_PolicyErrorResult](../../structs/fileshare-policyerrorresult/document.md) \*\*result | Double pointer to the **FileShare\_PolicyErrorResult** array. Use **OH\_FileShare\_ReleasePolicyErrorResult()** to release the memory allocated. |
| unsigned int \*resultNum | Pointer to the size of the **FileShare\_PolicyErrorResult** array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [FileManagement\_ErrCode](../error-code-h/document.md#filemanagement_errcode) | 
Returns [FileManagement\_ErrCode](../error-code-h/document.md#filemanagement_errcode).

ERR\_INVALID\_PARAMETER 401 - The input parameter is invalid. Possible causes:

1\. The **policies**, **result**, or **resultNum** parameter is a null pointer.

2\. The value of **policyNum** is **0** or exceeds the maximum length (500).

3\. The value of **uri** in the **policies** parameter is empty, the value of **length** is **0**, or the value of **uri** is different from the value of **length**.

ERR\_DEVICE\_NOT\_SUPPORTED 801 - The device does not support this API.

ERR\_PERMISSION\_ERROR 201 - The permission verification fails.

ERR\_ENOMEM 13900011 - The memory allocation or copy fails.

ERR\_EPERM 13900001 - The operation is not allowed.

ERR\_OK 0 - The API is called successfully.

 |

#### \[h2\]OH\_FileShare\_DeactivatePermission()

FileManagement\_ErrCode OH\_FileShare\_DeactivatePermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum)

**Description**

Deactivates the persistent permissions on files or directories.

**Required permissions**: ohos.permission.FILE\_ACCESS\_PERSIST

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const FileShare\_PolicyInfo](../../structs/fileshare-policyinfo/document.md) \*policies | Pointer to a **FileShare\_PolicyInfo** instance. |
| unsigned int policyNum | Number of policies in the **FileShare\_PolicyInfo** array. |
| [FileShare\_PolicyErrorResult](../../structs/fileshare-policyerrorresult/document.md) \*\*result | Double pointer to the **FileShare\_PolicyErrorResult** array. Use **OH\_FileShare\_ReleasePolicyErrorResult()** to release the memory allocated. |
| unsigned int \*resultNum | Pointer to the size of the **FileShare\_PolicyErrorResult** array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [FileManagement\_ErrCode](../error-code-h/document.md#filemanagement_errcode) | 
Returns [FileManagement\_ErrCode](../error-code-h/document.md#filemanagement_errcode).

ERR\_INVALID\_PARAMETER 401 - The input parameter is invalid. Possible causes:

1\. The **policies**, **result**, or **resultNum** parameter is a null pointer.

2\. The value of **policyNum** is **0** or exceeds the maximum length (500).

3\. The value of **uri** in the **policies** parameter is empty, the value of **length** is **0**, or the value of **uri** is different from the value of **length**.

ERR\_DEVICE\_NOT\_SUPPORTED 801 - The device does not support this API.

ERR\_PERMISSION\_ERROR 201 - The permission verification fails.

ERR\_ENOMEM 13900011 - The memory allocation or copy fails.

ERR\_EPERM 13900001 - The operation is not allowed.

ERR\_OK 0 - The API is called successfully.

 |

#### \[h2\]OH\_FileShare\_CheckPersistentPermission()

FileManagement\_ErrCode OH\_FileShare\_CheckPersistentPermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, bool \*\*result, unsigned int \*resultNum)

**Description**

Checks the persistent permissions on files or directories.

**Required permissions**: ohos.permission.FILE\_ACCESS\_PERSIST

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const FileShare\_PolicyInfo](../../structs/fileshare-policyinfo/document.md) \*policies | Pointer to a **FileShare\_PolicyInfo** instance. |
| unsigned int policyNum | Number of policies in the **FileShare\_PolicyInfo** array. |
| bool \*\*result | Double pointer to the check result obtained. You also need to include **malloc.h** and use **free()** to release the memory allocated. |
| unsigned int \*resultNum | Pointer to the size of the check result array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [FileManagement\_ErrCode](../error-code-h/document.md#filemanagement_errcode) | 
Returns [FileManagement\_ErrCode](../error-code-h/document.md#filemanagement_errcode).

ERR\_INVALID\_PARAMETER 401 - The input parameter is invalid. Possible causes:

1\. The **policies**, **result**, or **resultNum** parameter is a null pointer.

2\. The value of **policyNum** is **0** or exceeds the maximum length (500).

3\. The value of **uri** in the **policies** parameter is empty, the value of **length** is **0**, or the value of **uri** is different from the value of **length**.

ERR\_DEVICE\_NOT\_SUPPORTED 801 - The device does not support this API.

ERR\_PERMISSION\_ERROR 201 - The permission verification fails.

ERR\_ENOMEM 13900011 - The memory allocation or copy fails.

ERR\_EPERM 13900001 - The operation is not allowed. All URIs carried in **policies** do not meet the specifications, or the path converted from the URI does not exist.

ERR\_OK 0 - The API is called successfully.

 |

#### \[h2\]OH\_FileShare\_ReleasePolicyErrorResult()

void OH\_FileShare\_ReleasePolicyErrorResult(FileShare\_PolicyErrorResult \*errorResult, unsigned int resultNum)

**Description**

Releases the memory, to which **FileShare\_PolicyErrorResult** points.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [FileShare\_PolicyErrorResult](../../structs/fileshare-policyerrorresult/document.md) \*errorResult | Pointer to a **FileShare\_PolicyErrorResult** instance. |
| unsigned int resultNum | Size of the **FileShare\_PolicyErrorResult** array. |
