# oh\_environment.h

#### Overview

Defines the native APIs used to obtain the sandbox paths of the user files.

**Header file**: <filemanagement/environment/oh\_environment.h>

**Library**: libohenvironment.so

**System capability**: SystemCapability.FileManagement.File.Environment.FolderObtain

**Since**: 12

**Related module**: [Environment](../../modules/environment/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [FileManagement\_ErrCode OH\_Environment\_GetUserDownloadDir(char \*\*result)](#oh_environment_getuserdownloaddir) | Obtains the sandbox path of the **Download** root directory. |
| [FileManagement\_ErrCode OH\_Environment\_GetUserDesktopDir(char \*\*result)](#oh_environment_getuserdesktopdir) | Obtains the sandbox path of the **Desktop** root directory. |
| [FileManagement\_ErrCode OH\_Environment\_GetUserDocumentDir(char \*\*result)](#oh_environment_getuserdocumentdir) | Obtains the sandbox path of the **Document** root directory. |

#### Function Description

#### \[h2\]OH\_Environment\_GetUserDownloadDir()

FileManagement\_ErrCode OH\_Environment\_GetUserDownloadDir(char \*\*result)

**Description**

Obtains the sandbox path of the **Download** root directory.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| char \*\*result | Double pointer to the path of the **Download** root directory. You also need to include **malloc.h** and use **free()** to release the memory allocated. |

**Returns**

| Type | Description |
| :-- | :-- |
| [FileManagement\_ErrCode](../error-code-h/document.md#filemanagement_errcode) | Returns [FileManagement\_ErrCode](../error-code-h/document.md#filemanagement_errcode). |

#### \[h2\]OH\_Environment\_GetUserDesktopDir()

FileManagement\_ErrCode OH\_Environment\_GetUserDesktopDir(char \*\*result)

**Description**

Obtains the sandbox path of the **Desktop** root directory.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| char \*\*result | Double pointer to the path of the **Desktop** root directory. You also need to include **malloc.h** and use **free()** to release the memory allocated. |

**Returns**

| Type | Description |
| :-- | :-- |
| [FileManagement\_ErrCode](../error-code-h/document.md#filemanagement_errcode) | Returns [FileManagement\_ErrCode](../error-code-h/document.md#filemanagement_errcode). |

#### \[h2\]OH\_Environment\_GetUserDocumentDir()

FileManagement\_ErrCode OH\_Environment\_GetUserDocumentDir(char \*\*result)

**Description**

Obtains the sandbox path of the **Document** root directory.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| char \*\*result | Double pointer to the path of the **Document** root directory. You also need to include **malloc.h** and use **free()** to release the memory allocated. |

**Returns**

| Type | Description |
| :-- | :-- |
| [FileManagement\_ErrCode](../error-code-h/document.md#filemanagement_errcode) | Returns [FileManagement\_ErrCode](../error-code-h/document.md#filemanagement_errcode). |
