# oh\_fileio.h

#### Overview

Defines the native APIs used to obtain the location of a file.

**File to include**: <filemanagement/fileio/oh\_fileio.h>

**Library**: libohfileio.so

**System capability**: SystemCapability.FileManagement.File.FileIO

**Since**: 12

**Related module**: [FileIO](../../modules/fileio/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [FileIO\_FileLocation](#fileio_filelocation) | FileIO\_FileLocation | Enumerates the file locations. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [FileManagement\_ErrCode OH\_FileIO\_GetFileLocation(char \*uri, int uriLength, FileIO\_FileLocation \*location)](#oh_fileio_getfilelocation) | Obtains the location of a file. |

#### Enum Description

#### \[h2\]FileIO\_FileLocation

enum FileIO\_FileLocation

**Description**

Enumerates the file locations.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| LOCAL = 1 | The file is stored on the local device. |
| CLOUD = 2 | The file is stored on the cloud. |
| LOCAL\_AND\_CLOUD = 3 | The file is stored on the local device and cloud. |

#### Function Description

#### \[h2\]OH\_FileIO\_GetFileLocation()

FileManagement\_ErrCode OH\_FileIO\_GetFileLocation(char \*uri, int uriLength, FileIO\_FileLocation \*location)

**Description**

Obtains the location of a file.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| char \*uri | Pointer to the URI of the file. |
| int uriLength | Length of the URI. |
| [FileIO\_FileLocation](#fileio_filelocation) \*location | Pointer to the location of the file obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [FileManagement\_ErrCode](../error-code-h/document.md#filemanagement_errcode) | Returns [FileManagement\_ErrCode](../error-code-h/document.md#filemanagement_errcode). |
