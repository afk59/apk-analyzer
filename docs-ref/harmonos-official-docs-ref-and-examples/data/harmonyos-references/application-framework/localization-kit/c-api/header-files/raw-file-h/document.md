# raw\_file.h

#### Overview

Provides functions related to rawfiles, including searching for, reading, and closing rawfiles.

**File to include**: <rawfile/raw\_file.h>

**Library**: librawfile.z.so

**System capability**: SystemCapability.Global.ResourceManager

**Since**: 8

**Related module**: [rawfile](../../modules/rawfile/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [RawFileDescriptor](../../structs/rawfiledescriptor/document.md) | RawFileDescriptor | Defines the file descriptor information of a file in the **rawfile** directory. **RawFileDescriptor** is an output parameter of [OH\_ResourceManager\_GetRawFileDescriptor](#oh_resourcemanager_getrawfiledescriptor). It contains the file descriptor of a rawfile and the start position and length of the rawfile in the HAP. |
| [RawFileDescriptor64](../../structs/rawfiledescriptor64/document.md) | RawFileDescriptor64 | Defines the file descriptor of a large rawfile. **RawFileDescriptor64** is an output parameter of [OH\_ResourceManager\_GetRawFileDescriptor64](#oh_resourcemanager_getrawfiledescriptor64). It contains the file descriptor of a rawfile and the start position and length of the rawfile in the HAP. |
| [RawFile](../../structs/rawfile/document.md) | RawFile | Provides access to rawfiles. |
| [RawFile64](../../structs/rawfile64/document.md) | RawFile64 | Provides access to large rawfiles. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int OH\_ResourceManager\_ReadRawFile(const RawFile \*rawFile, void \*buf, size\_t length)](#oh_resourcemanager_readrawfile) | Reads data of the specified length from the current position in a rawfile. |
| [int OH\_ResourceManager\_SeekRawFile(const RawFile \*rawFile, long offset, int whence)](#oh_resourcemanager_seekrawfile) | Searches for the data read/write position in a rawfile based on the specified offset. |
| [long OH\_ResourceManager\_GetRawFileSize(RawFile \*rawFile)](#oh_resourcemanager_getrawfilesize) | Obtains the length of the rawfile, in long. |
| [long OH\_ResourceManager\_GetRawFileRemainingLength(const RawFile \*rawFile)](#oh_resourcemanager_getrawfileremaininglength) | Obtains the remaining length of the rawfile, in long. |
| [void OH\_ResourceManager\_CloseRawFile(RawFile \*rawFile)](#oh_resourcemanager_closerawfile) | Closes a [RawFile](../../structs/rawfile/document.md) and releases all associated resources. |
| [long OH\_ResourceManager\_GetRawFileOffset(const RawFile \*rawFile)](#oh_resourcemanager_getrawfileoffset) | Obtains the current offset of a rawfile, in long. |
| [bool OH\_ResourceManager\_GetRawFileDescriptor(const RawFile \*rawFile, RawFileDescriptor &descriptor)](#oh_resourcemanager_getrawfiledescriptor) | Opens a rawfile based on the specified offset (in long) and file length (in long) and obtains the file descriptor. The file descriptor obtained can be used to read the file. (It is deprecated in API version 12.) |
| [bool OH\_ResourceManager\_GetRawFileDescriptorData(const RawFile \*rawFile, RawFileDescriptor \*descriptor)](#oh_resourcemanager_getrawfiledescriptordata) | Opens a rawfile based on the specified offset (in long) and file length (in long) and obtains the file descriptor. The file descriptor obtained can be used to read the file. |
| [bool OH\_ResourceManager\_ReleaseRawFileDescriptor(const RawFileDescriptor &descriptor)](#oh_resourcemanager_releaserawfiledescriptor) | Releases the file descriptor of a rawfile. To prevent file descriptor leakage, you are advised to release a rawfile descriptor immediately after use. (It is deprecated in API version 12.) |
| [bool OH\_ResourceManager\_ReleaseRawFileDescriptorData(const RawFileDescriptor \*descriptor)](#oh_resourcemanager_releaserawfiledescriptordata) | Releases the file descriptor of a rawfile. To prevent file descriptor leakage, you are advised to release a rawfile descriptor immediately after use. |
| [int64\_t OH\_ResourceManager\_ReadRawFile64(const RawFile64 \*rawFile, void \*buf, int64\_t length)](#oh_resourcemanager_readrawfile64) | Reads data of the specified length from the current position in a large rawfile. |
| [int OH\_ResourceManager\_SeekRawFile64(const RawFile64 \*rawFile, int64\_t offset, int whence)](#oh_resourcemanager_seekrawfile64) | Searches for the data read/write position in a large rawfile based on the specified offset. |
| [int64\_t OH\_ResourceManager\_GetRawFileSize64(RawFile64 \*rawFile)](#oh_resourcemanager_getrawfilesize64) | Obtains the length of a large rawfile, in int64\_t. |
| [int64\_t OH\_ResourceManager\_GetRawFileRemainingLength64(const RawFile64 \*rawFile)](#oh_resourcemanager_getrawfileremaininglength64) | Obtains the remaining length of a large rawfile, in int64\_t. |
| [void OH\_ResourceManager\_CloseRawFile64(RawFile64 \*rawFile)](#oh_resourcemanager_closerawfile64) | Closes an opened [RawFile64](../../structs/rawfile64/document.md) and releases all associated resources. |
| [int64\_t OH\_ResourceManager\_GetRawFileOffset64(const RawFile64 \*rawFile)](#oh_resourcemanager_getrawfileoffset64) | Obtains the offset of a large rawfile, in int64\_t. |
| [bool OH\_ResourceManager\_GetRawFileDescriptor64(const RawFile64 \*rawFile, RawFileDescriptor64 \*descriptor)](#oh_resourcemanager_getrawfiledescriptor64) | Opens a large rawfile based on the specified offset (in int64\_t) and file length (in int64\_t) and obtains the file descriptor. The file descriptor obtained can be used to read the file. |
| [bool OH\_ResourceManager\_ReleaseRawFileDescriptor64(const RawFileDescriptor64 \*descriptor)](#oh_resourcemanager_releaserawfiledescriptor64) | Releases the file descriptor of a rawfile. To prevent file descriptor leakage, you are advised to release a rawfile descriptor immediately after use. |

#### Function Description

#### \[h2\]OH\_ResourceManager\_ReadRawFile()

int OH\_ResourceManager\_ReadRawFile(const RawFile \*rawFile, void \*buf, size\_t length)

**Description**

Reads data of the specified length from the current position in a rawfile.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [const RawFile](../../structs/rawfile/document.md) \*rawFile | Pointer to [RawFile](../../structs/rawfile/document.md). |
| void \*buf | Pointer to the buffer for receiving the read data. |
| size\_t length | Length of the data to read. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Number of read bytes. If the read length exceeds the length of the file end or rawfile is empty, **0** is returned. |

#### \[h2\]OH\_ResourceManager\_SeekRawFile()

int OH\_ResourceManager\_SeekRawFile(const RawFile \*rawFile, long offset, int whence)

**Description**

Searches for the data read/write position in a rawfile based on the specified offset.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [const RawFile](../../structs/rawfile/document.md) \*rawFile | Pointer to [RawFile](../../structs/rawfile/document.md). |
| long offset | Specified offset. |
| int whence | 
Read/Write position. The options are as follows:

**0**: The read/write position is the start position of the file plus the offset.

**1**: The read/write position is the current position plus the offset.

**2**: The read/write position is the end position of the file plus the offset.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int | **0** if the search is successful; **\-1** otherwise. |

#### \[h2\]OH\_ResourceManager\_GetRawFileSize()

long OH\_ResourceManager\_GetRawFileSize(RawFile \*rawFile)

**Description**

Obtains the length of the rawfile, in long.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [RawFile](../../structs/rawfile/document.md) \*rawFile | Pointer to [RawFile](../../structs/rawfile/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| long | Overall length of the rawfile. If the rawfile is empty, **0** is returned. |

#### \[h2\]OH\_ResourceManager\_GetRawFileRemainingLength()

long OH\_ResourceManager\_GetRawFileRemainingLength(const RawFile \*rawFile)

**Description**

Obtains the remaining length of the rawfile, in long.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const RawFile](../../structs/rawfile/document.md) \*rawFile | Pointer to [RawFile](../../structs/rawfile/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| long | Remaining length of the rawfile. If the rawfile is empty, **0** is returned. |

#### \[h2\]OH\_ResourceManager\_CloseRawFile()

void OH\_ResourceManager\_CloseRawFile(RawFile \*rawFile)

**Description**

Closes a [RawFile](../../structs/rawfile/document.md) and releases all associated resources.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [RawFile](../../structs/rawfile/document.md) \*rawFile | Pointer to [RawFile](../../structs/rawfile/document.md). |

**Reference**

[OH\_ResourceManager\_OpenRawFile](../raw-file-manager-h/document.md#oh_resourcemanager_openrawfile)

#### \[h2\]OH\_ResourceManager\_GetRawFileOffset()

long OH\_ResourceManager\_GetRawFileOffset(const RawFile \*rawFile)

**Description**

Obtains the current offset of a rawfile, in long.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [const RawFile](../../structs/rawfile/document.md) \*rawFile | Pointer to [RawFile](../../structs/rawfile/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| long | Current offset of the rawfile. If the rawfile is empty, **0** is returned. |

#### \[h2\]OH\_ResourceManager\_GetRawFileDescriptor()

bool OH\_ResourceManager\_GetRawFileDescriptor(const RawFile \*rawFile, RawFileDescriptor &descriptor)

**Description**

Opens a rawfile based on the specified offset (in long) and file length (in long) and obtains the file descriptor. The file descriptor obtained can be used to read the file.

**Since**: 8

**Deprecated from**: 12

**Substitute**: [OH\_ResourceManager\_GetRawFileDescriptorData](#oh_resourcemanager_getrawfiledescriptordata)

**Parameters**

| Name | Description |
| :-- | :-- |
| [const RawFile](../../structs/rawfile/document.md) \*rawFile | Pointer to [RawFile](../../structs/rawfile/document.md). |
| RawFileDescriptor &descriptor | File descriptor of the rawfile, start position of the rawfile in the HAP, and length of the rawfile. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | **true** if the file is opened; returns **false** if the access to the file is rejected. |

#### \[h2\]OH\_ResourceManager\_GetRawFileDescriptorData()

bool OH\_ResourceManager\_GetRawFileDescriptorData(const RawFile \*rawFile, RawFileDescriptor \*descriptor)

**Description**

Opens a rawfile based on the specified offset (in long) and file length (in long) and obtains the file descriptor. The file descriptor obtained can be used to read the file.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const RawFile](../../structs/rawfile/document.md) \*rawFile | Pointer to [RawFile](../../structs/rawfile/document.md). |
| [RawFileDescriptor](../../structs/rawfiledescriptor/document.md) \*descriptor | File descriptor of the rawfile, start position of the rawfile in the HAP, and length of the rawfile. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | **true** if the file is opened; returns **false** if the access to the file is rejected. |

#### \[h2\]OH\_ResourceManager\_ReleaseRawFileDescriptor()

bool OH\_ResourceManager\_ReleaseRawFileDescriptor(const RawFileDescriptor &descriptor)

**Description**

Releases the file descriptor of a rawfile. To prevent file descriptor leakage, you are advised to release a rawfile descriptor immediately after use.

**Since**: 8

**Deprecated from**: 12

**Substitute**: [OH\_ResourceManager\_ReleaseRawFileDescriptorData](#oh_resourcemanager_releaserawfiledescriptordata)

**Parameters**

| Name | Description |
| :-- | :-- |
| [const RawFileDescriptor](../../structs/rawfiledescriptor/document.md) &descriptor | File descriptor of the rawfile. It contains the file descriptor, start position in the HAP, and file length. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the file descriptor is released; returns **false** otherwise. |

#### \[h2\]OH\_ResourceManager\_ReleaseRawFileDescriptorData()

bool OH\_ResourceManager\_ReleaseRawFileDescriptorData(const RawFileDescriptor \*descriptor)

**Description**

Releases the file descriptor of a rawfile. To prevent file descriptor leakage, you are advised to release a rawfile descriptor immediately after use.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const RawFileDescriptor](../../structs/rawfiledescriptor/document.md) \*descriptor | File descriptor of the rawfile. It contains the file descriptor, start position in the HAP, and file length. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the file descriptor is released; returns **false** otherwise. |

#### \[h2\]OH\_ResourceManager\_ReadRawFile64()

int64\_t OH\_ResourceManager\_ReadRawFile64(const RawFile64 \*rawFile, void \*buf, int64\_t length)

**Description**

Reads data of the specified length from the current position in a large rawfile.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const RawFile64](../../structs/rawfile64/document.md) \*rawFile | Pointer to [RawFile64](../../structs/rawfile64/document.md). |
| void \*buf | Pointer to the buffer for receiving the read data. |
| int64\_t length | Length of the data to read. |

**Returns**

| Type | Description |
| :-- | :-- |
| int64\_t | Number of read bytes. If the read length exceeds the length of the file end or rawfile is empty, **0** is returned. |

#### \[h2\]OH\_ResourceManager\_SeekRawFile64()

int OH\_ResourceManager\_SeekRawFile64(const RawFile64 \*rawFile, int64\_t offset, int whence)

**Description**

Searches for the data read/write position in a large rawfile based on the specified offset.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const RawFile64](../../structs/rawfile64/document.md) \*rawFile | Pointer to [RawFile64](../../structs/rawfile64/document.md). |
| int64\_t offset | Specified offset. |
| int whence | 
Read/Write position. The options are as follows:

**0**: The read/write position is the start position of the file plus the offset.

**1**: The read/write position is the current position plus the offset.

**2**: The read/write position is the end position of the file plus the offset.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int | **0** if the search is successful; **\-1** otherwise. |

#### \[h2\]OH\_ResourceManager\_GetRawFileSize64()

int64\_t OH\_ResourceManager\_GetRawFileSize64(RawFile64 \*rawFile)

**Description**

Obtains the length of a large rawfile, in int64\_t.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [RawFile64](../../structs/rawfile64/document.md) \*rawFile | Pointer to [RawFile64](../../structs/rawfile64/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int64\_t | Overall length of the rawfile. If the rawfile is empty, **0** is returned. |

#### \[h2\]OH\_ResourceManager\_GetRawFileRemainingLength64()

int64\_t OH\_ResourceManager\_GetRawFileRemainingLength64(const RawFile64 \*rawFile)

**Description**

Obtains the remaining length of a large rawfile, in int64\_t.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const RawFile64](../../structs/rawfile64/document.md) \*rawFile | Pointer to [RawFile64](../../structs/rawfile64/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int64\_t | Remaining length of the rawfile. If the rawfile is empty, **0** is returned. |

#### \[h2\]OH\_ResourceManager\_CloseRawFile64()

void OH\_ResourceManager\_CloseRawFile64(RawFile64 \*rawFile)

**Description**

Closes an opened [RawFile64](../../structs/rawfile64/document.md) and releases all associated resources.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [RawFile64](../../structs/rawfile64/document.md) \*rawFile | Pointer to [RawFile64](../../structs/rawfile64/document.md). |

**Reference**

[OH\_ResourceManager\_OpenRawFile64](../raw-file-manager-h/document.md#oh_resourcemanager_openrawfile64)

#### \[h2\]OH\_ResourceManager\_GetRawFileOffset64()

int64\_t OH\_ResourceManager\_GetRawFileOffset64(const RawFile64 \*rawFile)

**Description**

Obtains the offset of a large rawfile, in int64\_t.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const RawFile64](../../structs/rawfile64/document.md) \*rawFile | Pointer to [RawFile64](../../structs/rawfile64/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int64\_t | Current offset of the rawfile. If the rawfile is empty, **0** is returned. |

#### \[h2\]OH\_ResourceManager\_GetRawFileDescriptor64()

bool OH\_ResourceManager\_GetRawFileDescriptor64(const RawFile64 \*rawFile, RawFileDescriptor64 \*descriptor)

**Description**

Opens a large rawfile based on the specified offset (in int64\_t) and file length (in int64\_t) and obtains the file descriptor. The file descriptor obtained can be used to read the file.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const RawFile64](../../structs/rawfile64/document.md) \*rawFile | Pointer to [RawFile64](../../structs/rawfile64/document.md). |
| [RawFileDescriptor64](../../structs/rawfiledescriptor64/document.md) \*descriptor | File descriptor of the rawfile, start position of the rawfile in the HAP, and length of the rawfile. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | **true** if the file is opened; returns **false** if the access to the file is rejected. |

#### \[h2\]OH\_ResourceManager\_ReleaseRawFileDescriptor64()

bool OH\_ResourceManager\_ReleaseRawFileDescriptor64(const RawFileDescriptor64 \*descriptor)

**Description**

Releases the file descriptor of a rawfile. To prevent file descriptor leakage, you are advised to release a rawfile descriptor immediately after use.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const RawFileDescriptor64](../../structs/rawfiledescriptor64/document.md) \*descriptor | File descriptor of the rawfile. It contains the file descriptor, start position in the HAP, and file length. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the file descriptor is released; returns **false** otherwise. |
