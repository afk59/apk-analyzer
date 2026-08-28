# raw\_file\_manager.h

#### Overview

Provides file management functions for the **rawfile** directory. You can use the **ResourceManager** to open a rawfile and perform operations such as data search and reading.

**File to include**: <rawfile/raw\_file\_manager.h>

**Library**: librawfile.z.so

**System capability**: SystemCapability.Global.ResourceManager

**Since**: 8

**Related module**: [rawfile](../../modules/rawfile/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [NativeResourceManager](../../structs/nativeresourcemanager/document.md) | NativeResourceManager | Represents the native **ResourceManager**. This class encapsulates the native implementation of the JavaScript resource manager. The **ResourceManager** pointer can be obtained by using [OH\_ResourceManager\_InitNativeResourceManager](#oh_resourcemanager_initnativeresourcemanager). |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [NativeResourceManager \*OH\_ResourceManager\_InitNativeResourceManager(napi\_env env, napi\_value jsResMgr)](#oh_resourcemanager_initnativeresourcemanager) | Obtains the native **ResourceManager** based on the JavaScript **ResourceManager** to implement rawfile-specific functions. |
| [void OH\_ResourceManager\_ReleaseNativeResourceManager(NativeResourceManager \*resMgr)](#oh_resourcemanager_releasenativeresourcemanager) | Releases the native **ResourceManager**. |
| [RawDir \*OH\_ResourceManager\_OpenRawDir(const NativeResourceManager \*mgr, const char \*dirName)](#oh_resourcemanager_openrawdir) | Traverses all files in the **rawfile** directory. |
| [RawFile \*OH\_ResourceManager\_OpenRawFile(const NativeResourceManager \*mgr, const char \*fileName)](#oh_resourcemanager_openrawfile) | Opens a rawfile and reads the data in it. |
| [RawFile64 \*OH\_ResourceManager\_OpenRawFile64(const NativeResourceManager \*mgr, const char \*fileName)](#oh_resourcemanager_openrawfile64) | Opens a large rawfile and reads the data in it. |
| [bool OH\_ResourceManager\_IsRawDir(const NativeResourceManager \*mgr, const char \*path)](#oh_resourcemanager_israwdir) | Checks whether the path of a rawfile is a subdirectory in the **rawfile** directory. |

#### Function Description

#### \[h2\]OH\_ResourceManager\_InitNativeResourceManager()

NativeResourceManager \*OH\_ResourceManager\_InitNativeResourceManager(napi\_env env, napi\_value jsResMgr)

**Description**

Obtains the native **ResourceManager** based on the JavaScript **ResourceManager** to implement rawfile-specific functions.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the JavaScript Native API (napi) environment. |
| napi\_value jsResMgr | JavaScript **ResourceManager** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [NativeResourceManager \*](../../structs/nativeresourcemanager/document.md) | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). If the operation fails, a null pointer is returned. |

#### \[h2\]OH\_ResourceManager\_ReleaseNativeResourceManager()

void OH\_ResourceManager\_ReleaseNativeResourceManager(NativeResourceManager \*resMgr)

**Description**

Releases the native **ResourceManager**.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*resMgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). |

#### \[h2\]OH\_ResourceManager\_OpenRawDir()

RawDir \*OH\_ResourceManager\_OpenRawDir(const NativeResourceManager \*mgr, const char \*dirName)

**Description**

Traverses all files in the **rawfile** directory.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md), which is obtained by calling [OH\_ResourceManager\_InitNativeResourceManager](#oh_resourcemanager_initnativeresourcemanager). |
| const char \*dirName | Pointer to the name of the directory to open. If this field is left empty, the root directory will be opened. |

**Returns**

| Type | Description |
| :-- | :-- |
| [RawDir \*](../../structs/rawdir/document.md) | Pointer to [RawDir](../../structs/rawdir/document.md). After using the pointer, call [OH\_ResourceManager\_CloseRawDir](../raw-dir-h/document.md#oh_resourcemanager_closerawdir) to release it. If the operation fails or **mgr** is empty, a null pointer is returned. |

**Reference**

[OH\_ResourceManager\_InitNativeResourceManager](#oh_resourcemanager_initnativeresourcemanager)

[OH\_ResourceManager\_CloseRawDir](../raw-dir-h/document.md#oh_resourcemanager_closerawdir)

#### \[h2\]OH\_ResourceManager\_OpenRawFile()

RawFile \*OH\_ResourceManager\_OpenRawFile(const NativeResourceManager \*mgr, const char \*fileName)

**Description**

Opens a rawfile and reads the data in it.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md), which is obtained by calling [OH\_ResourceManager\_InitNativeResourceManager](#oh_resourcemanager_initnativeresourcemanager). |
| const char \*fileName | Pointer to the name of the file in the relative path of the **rawfile** root directory. |

**Returns**

| Type | Description |
| :-- | :-- |
| [RawFile \*](../../structs/rawfile/document.md) | Pointer to [RawFile](../../structs/rawfile/document.md). After using the pointer, call [OH\_ResourceManager\_CloseRawFile](../raw-file-h/document.md#oh_resourcemanager_closerawfile) to release it. If the operation fails or **mgr** or **fileName** is empty, a null pointer is returned. |

**Reference**

[OH\_ResourceManager\_InitNativeResourceManager](#oh_resourcemanager_initnativeresourcemanager)

[OH\_ResourceManager\_CloseRawFile](../raw-file-h/document.md#oh_resourcemanager_closerawfile)

#### \[h2\]OH\_ResourceManager\_OpenRawFile64()

RawFile64 \*OH\_ResourceManager\_OpenRawFile64(const NativeResourceManager \*mgr, const char \*fileName)

**Description**

Opens a large rawfile and reads the data in it.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md), which is obtained by calling [OH\_ResourceManager\_InitNativeResourceManager](#oh_resourcemanager_initnativeresourcemanager). |
| const char \*fileName | Pointer to the name of the file in the relative path of the **rawfile** root directory. |

**Returns**

| Type | Description |
| :-- | :-- |
| [RawFile64 \*](../../structs/rawfile64/document.md) | Pointer to [RawFile64](../../structs/rawfile64/document.md). After using this pointer, call [OH\_ResourceManager\_CloseRawFile64](../raw-file-h/document.md#oh_resourcemanager_closerawfile64) to release it. If the operation fails or **mgr** or **fileName** is empty, a null pointer is returned. |

**Reference**

[OH\_ResourceManager\_InitNativeResourceManager](#oh_resourcemanager_initnativeresourcemanager)

[OH\_ResourceManager\_CloseRawFile64](../raw-file-h/document.md#oh_resourcemanager_closerawfile64)

#### \[h2\]OH\_ResourceManager\_IsRawDir()

bool OH\_ResourceManager\_IsRawDir(const NativeResourceManager \*mgr, const char \*path)

**Description**

Checks whether the path of a raw file is a subdirectory in the **rawfile** directory.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md), which is obtained by calling [OH\_ResourceManager\_InitNativeResourceManager](#oh_resourcemanager_initnativeresourcemanager). |
| const char \*path | Path of a rawfile. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | **true** if the path is a subdirectory in the **rawfile** directory; **false** otherwise. |
