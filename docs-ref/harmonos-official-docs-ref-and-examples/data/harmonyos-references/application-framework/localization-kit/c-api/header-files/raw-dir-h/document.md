# raw\_dir.h

#### Overview

Provides functions related to rawfile directories, including traversing and closing rawfile directories.

**File to include**: <rawfile/raw\_dir.h>

**Library**: librawfile.z.so

**System capability**: SystemCapability.Global.ResourceManager

**Since**: 8

**Related module**: [rawfile](../../modules/rawfile/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [RawDir](../../structs/rawdir/document.md) | RawDir | Provides access to the **rawfile** directory. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [const char \*OH\_ResourceManager\_GetRawFileName(RawDir \*rawDir, int index)](#oh_resourcemanager_getrawfilename) | Obtains the name of a file in **rawfile** based on the index. You can use this function to traverse the **rawfile** directory. |
| [int OH\_ResourceManager\_GetRawFileCount(RawDir \*rawDir)](#oh_resourcemanager_getrawfilecount) | Obtains the number of rawfiles in [RawDir](../../structs/rawdir/document.md). You can use this function to obtain available indexes in [OH\_ResourceManager\_GetRawFileName](#oh_resourcemanager_getrawfilename). |
| [void OH\_ResourceManager\_CloseRawDir(RawDir \*rawDir)](#oh_resourcemanager_closerawdir) | Closes an opened [RawDir](../../structs/rawdir/document.md) and releases all associated resources. |

#### Function Description

#### \[h2\]OH\_ResourceManager\_GetRawFileName()

const char \*OH\_ResourceManager\_GetRawFileName(RawDir \*rawDir, int index)

**Description**

Obtains the name of a file in **rawfile** based on the index. You can use this function to traverse the **rawfile** directory.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [RawDir](../../structs/rawdir/document.md) \*rawDir | Pointer to [RawDir](../../structs/rawdir/document.md). |
| int index | Index of the rawfile in [RawDir](../../structs/rawdir/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| const char \* | 
File name obtained if the rawfile exists in the directory. The file name returned can be used as the input parameter of [OH\_ResourceManager\_OpenRawFile](../raw-file-manager-h/document.md#oh_resourcemanager_openrawfile).

If no file is found after all files in the directory are traversed, **NULL** is returned.

 |

**Reference**

[OH\_ResourceManager\_OpenRawFile](../raw-file-manager-h/document.md#oh_resourcemanager_openrawfile)

#### \[h2\]OH\_ResourceManager\_GetRawFileCount()

int OH\_ResourceManager\_GetRawFileCount(RawDir \*rawDir)

**Description**

Obtains the number of rawfiles in [RawDir](../../structs/rawdir/document.md). You can use this function to obtain available indexes in [OH\_ResourceManager\_GetRawFileName](#oh_resourcemanager_getrawfilename).

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [RawDir](../../structs/rawdir/document.md) \*rawDir | Pointer to [RawDir](../../structs/rawdir/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Number of files in **rawDir**. If **rawDir** is empty, **0** is returned. |

**Reference**

[OH\_ResourceManager\_GetRawFileName](#oh_resourcemanager_getrawfilename)

#### \[h2\]OH\_ResourceManager\_CloseRawDir()

void OH\_ResourceManager\_CloseRawDir(RawDir \*rawDir)

**Description**

Closes an opened [RawDir](../../structs/rawdir/document.md) and releases all associated resources.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [RawDir](../../structs/rawdir/document.md) \*rawDir | Pointer to [RawDir](../../structs/rawdir/document.md). |

**Reference**

[OH\_ResourceManager\_OpenRawDir](../raw-file-manager-h/document.md#oh_resourcemanager_openrawdir)
