# ipc\_cparcel.h

#### Overview

Provides C APIs for IPC serialization and deserialization.

**File to include**: <IPCKit/ipc\_cparcel.h>

**Library**: libipc\_capi.so

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Related module**: [OHIPCParcel](../../modules/ohipcparcel/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OHIPCParcel](../../structs/ohipcparcel/document.md) | OHIPCParcel | Defines an IPC serialized object. |
| [OHIPCRemoteProxy](../../structs/ohipcremoteproxy/document.md) | OHIPCRemoteProxy | Defines an IPC remote proxy object. |
| [OHIPCRemoteStub](../../structs/ohipcremotestub/document.md) | OHIPCRemoteStub | Defines an IPC remote service object. |

#### \[h2\]Function

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void\* (\*OH\_IPC\_MemAllocator)(int32\_t len)](#oh_ipc_memallocator) | OH\_IPC\_MemAllocator | Defines the type of a memory allocation function. |
| [OHIPCParcel\* OH\_IPCParcel\_Create(void)](#oh_ipcparcel_create) | \- | Creates an **OHIPCParcel** object, which cannot exceed 204,800 bytes. |
| [void OH\_IPCParcel\_Destroy(OHIPCParcel \*parcel)](#oh_ipcparcel_destroy) | \- | Destroys an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_GetDataSize(const OHIPCParcel \*parcel)](#oh_ipcparcel_getdatasize) | \- | Obtains the size of the data contained in an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_GetWritableBytes(const OHIPCParcel \*parcel)](#oh_ipcparcel_getwritablebytes) | \- | Obtains the number of bytes that can be written to an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_GetReadableBytes(const OHIPCParcel \*parcel)](#oh_ipcparcel_getreadablebytes) | \- | Obtains the number of bytes that can be read from an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_GetReadPosition(const OHIPCParcel \*parcel)](#oh_ipcparcel_getreadposition) | \- | Obtains the position where data is read in an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_GetWritePosition(const OHIPCParcel \*parcel)](#oh_ipcparcel_getwriteposition) | \- | Obtains the position where data is written in an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_RewindReadPosition(OHIPCParcel \*parcel, uint32\_t newReadPos)](#oh_ipcparcel_rewindreadposition) | \- | Resets the position to read data in an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_RewindWritePosition(OHIPCParcel \*parcel, uint32\_t newWritePos)](#oh_ipcparcel_rewindwriteposition) | \- | Resets the position to write data in an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_WriteInt8(OHIPCParcel \*parcel, int8\_t value)](#oh_ipcparcel_writeint8) | \- | Writes an int8\_t value to an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_ReadInt8(const OHIPCParcel \*parcel, int8\_t \*value)](#oh_ipcparcel_readint8) | \- | Reads an int8\_t value from an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_WriteInt16(OHIPCParcel \*parcel, int16\_t value)](#oh_ipcparcel_writeint16) | \- | Writes an int16\_t value to an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_ReadInt16(const OHIPCParcel \*parcel, int16\_t \*value)](#oh_ipcparcel_readint16) | \- | Reads an int16\_t value from an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_WriteInt32(OHIPCParcel \*parcel, int32\_t value)](#oh_ipcparcel_writeint32) | \- | Writes an int32\_t value to an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_ReadInt32(const OHIPCParcel \*parcel, int32\_t \*value)](#oh_ipcparcel_readint32) | \- | Reads an int32\_t value from an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_WriteInt64(OHIPCParcel \*parcel, int64\_t value)](#oh_ipcparcel_writeint64) | \- | Writes an int64\_t value to an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_ReadInt64(const OHIPCParcel \*parcel, int64\_t \*value)](#oh_ipcparcel_readint64) | \- | Reads an int64\_t value from an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_WriteFloat(OHIPCParcel \*parcel, float value)](#oh_ipcparcel_writefloat) | \- | Writes a float value to an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_ReadFloat(const OHIPCParcel \*parcel, float \*value)](#oh_ipcparcel_readfloat) | \- | Reads a float value from an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_WriteDouble(OHIPCParcel \*parcel, double value)](#oh_ipcparcel_writedouble) | \- | Writes a double value to an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_ReadDouble(const OHIPCParcel \*parcel, double \*value)](#oh_ipcparcel_readdouble) | \- | Reads a double value from an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_WriteString(OHIPCParcel \*parcel, const char \*str)](#oh_ipcparcel_writestring) | \- | Writes a string including a string terminator to an **OHIPCParcel** object. |
| [const char\* OH\_IPCParcel\_ReadString(const OHIPCParcel \*parcel)](#oh_ipcparcel_readstring) | \- | Reads a string from an **OHIPCParcel** object. You can obtain the length of the string from **strlen**. |
| [int OH\_IPCParcel\_Writebuffer(OHIPCParcel \*parcel, const uint8\_t \*buffer, int32\_t len)](#oh_ipcparcel_writebuffer) | \- | Writes data of the specified length from the memory to an **OHIPCParcel** object. |
| [const uint8\_t\* OH\_IPCParcel\_ReadBuffer(const OHIPCParcel \*parcel, int32\_t len)](#oh_ipcparcel_readbuffer) | \- | Reads memory information of the specified length from an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_WriteRemoteStub(OHIPCParcel \*parcel, const OHIPCRemoteStub \*stub)](#oh_ipcparcel_writeremotestub) | \- | Writes an **OHIPCRemoteStub** object to an **OHIPCParcel** object. |
| [OHIPCRemoteStub\* OH\_IPCParcel\_ReadRemoteStub(const OHIPCParcel \*parcel)](#oh_ipcparcel_readremotestub) | \- | Reads the **OHIPCRemoteStub** object from an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_WriteRemoteProxy(OHIPCParcel \*parcel, const OHIPCRemoteProxy \*proxy)](#oh_ipcparcel_writeremoteproxy) | \- | Writes an **OHIPCRemoteProxy** object to an **OHIPCParcel** object. |
| [OHIPCRemoteProxy\* OH\_IPCParcel\_ReadRemoteProxy(const OHIPCParcel \*parcel)](#oh_ipcparcel_readremoteproxy) | \- | Reads the **OHIPCRemoteProxy** object from an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_WriteFileDescriptor(OHIPCParcel \*parcel, int32\_t fd)](#oh_ipcparcel_writefiledescriptor) | \- | Writes a file descriptor to an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_ReadFileDescriptor(const OHIPCParcel \*parcel, int32\_t \*fd)](#oh_ipcparcel_readfiledescriptor) | \- | Reads a file descriptor from an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_Append(OHIPCParcel \*parcel, const OHIPCParcel \*data)](#oh_ipcparcel_append) | \- | Appends data to an **OHIPCParcel** object. |
| [int OH\_IPCParcel\_WriteInterfaceToken(OHIPCParcel \*parcel, const char \*token)](#oh_ipcparcel_writeinterfacetoken) | \- | Writes an interface token to an **OHIPCParcel** object for interface identity verification. |
| [int OH\_IPCParcel\_ReadInterfaceToken(const OHIPCParcel \*parcel, char \*\*token, int32\_t \*len, OH\_IPC\_MemAllocator allocator)](#oh_ipcparcel_readinterfacetoken) | \- | Reads an interface token from an **OHIPCParcel** object for interface identity verification. |

#### Function Description

#### \[h2\]OH\_IPC\_MemAllocator()

typedef void\* (\*OH\_IPC\_MemAllocator)(int32\_t len)

**Description**

Defines the type of a memory allocation function.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t len | Length of the memory to be allocated. |

**Returns**

| Type | Description |
| :-- | :-- |
| void\* | Returns the address of the memory allocated if the operation is successful; returns NULL otherwise. |

#### \[h2\]OH\_IPCParcel\_Create()

OHIPCParcel\* OH\_IPCParcel\_Create(void)

**Description**

Creates an **OHIPCParcel** object, which cannot exceed 204,800 bytes.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| OHIPCParcel\* | Returns the pointer to the **OHIPCParcel** object created if the operation is successful; returns NULL otherwise. |

#### \[h2\]OH\_IPCParcel\_Destroy()

void OH\_IPCParcel\_Destroy(OHIPCParcel \*parcel)

**Description**

Destroys an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object to destroy. |

#### \[h2\]OH\_IPCParcel\_GetDataSize()

int OH\_IPCParcel\_GetDataSize(const OHIPCParcel \*parcel)

**Description**

Obtains the size of the data contained in an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns the data size obtained if the operation is successful; returns **\-1** if invalid parameters are found. |

#### \[h2\]OH\_IPCParcel\_GetWritableBytes()

int OH\_IPCParcel\_GetWritableBytes(const OHIPCParcel \*parcel)

**Description**

Obtains the number of bytes that can be written to an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns the number of bytes that can be written to the **OHIPCParcel** object; returns **\-1** if invalid parameters are found. |

#### \[h2\]OH\_IPCParcel\_GetReadableBytes()

int OH\_IPCParcel\_GetReadableBytes(const OHIPCParcel \*parcel)

**Description**

Obtains the number of bytes that can be read from an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the number of bytes that can be read from the **OHIPCParcel** object.

Returns **\-1** if invalid parameters are found.

 |

#### \[h2\]OH\_IPCParcel\_GetReadPosition()

int OH\_IPCParcel\_GetReadPosition(const OHIPCParcel \*parcel)

**Description**

Obtains the position where data is read in an **OHIPCParcel** object.

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns the current read position obtained if the operation is successful; returns **\-1** if invalid parameters are found. |

#### \[h2\]OH\_IPCParcel\_GetWritePosition()

int OH\_IPCParcel\_GetWritePosition(const OHIPCParcel \*parcel)

**Description**

Obtains the position where data is written in an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns the current write position obtained if the operation is successful; returns **\-1** if invalid parameters are found. |

#### \[h2\]OH\_IPCParcel\_RewindReadPosition()

int OH\_IPCParcel\_RewindReadPosition(OHIPCParcel \*parcel, uint32\_t newReadPos)

**Description**

Resets the position to read data in an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| uint32\_t newReadPos | New position to read data. The value ranges from **0** to the current data size. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

 |

#### \[h2\]OH\_IPCParcel\_RewindWritePosition()

int OH\_IPCParcel\_RewindWritePosition(OHIPCParcel \*parcel, uint32\_t newWritePos)

**Description**

Resets the position to write data in an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| uint32\_t newWritePos | New position to write data. The value ranges from **0** to the current data size. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

 |

#### \[h2\]OH\_IPCParcel\_WriteInt8()

int OH\_IPCParcel\_WriteInt8(OHIPCParcel \*parcel, int8\_t value)

**Description**

Writes an int8\_t value to an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| int8\_t value | Value to write. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the write operation fails.

 |

#### \[h2\]OH\_IPCParcel\_ReadInt8()

int OH\_IPCParcel\_ReadInt8(const OHIPCParcel \*parcel, int8\_t \*value)

**Description**

Reads an int8\_t value from an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| int8\_t \*value | Pointer to the buffer for holding the read data. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the read operation fails.

 |

#### \[h2\]OH\_IPCParcel\_WriteInt16()

int OH\_IPCParcel\_WriteInt16(OHIPCParcel \*parcel, int16\_t value)

**Description**

Writes an int16\_t value to an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| int16\_t value | Value to write. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the write operation fails.

 |

#### \[h2\]OH\_IPCParcel\_ReadInt16()

int OH\_IPCParcel\_ReadInt16(const OHIPCParcel \*parcel, int16\_t \*value)

**Description**

Reads an int16\_t value from an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| int16\_t \*value | Pointer to the buffer for holding the read data. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the read operation fails.

 |

#### \[h2\]OH\_IPCParcel\_WriteInt32()

int OH\_IPCParcel\_WriteInt32(OHIPCParcel \*parcel, int32\_t value)

**Description**

Writes an int32\_t value to an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| int32\_t value | Value to write. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the write operation fails.

 |

#### \[h2\]OH\_IPCParcel\_ReadInt32()

int OH\_IPCParcel\_ReadInt32(const OHIPCParcel \*parcel, int32\_t \*value)

**Description**

Reads an int32\_t value from an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| int32\_t \*value | Pointer to the buffer for holding the read data. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the read operation fails.

 |

#### \[h2\]OH\_IPCParcel\_WriteInt64()

int OH\_IPCParcel\_WriteInt64(OHIPCParcel \*parcel, int64\_t value)

**Description**

Writes an int64\_t value to an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| int64\_t value | Value to write. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the write operation fails.

 |

#### \[h2\]OH\_IPCParcel\_ReadInt64()

int OH\_IPCParcel\_ReadInt64(const OHIPCParcel \*parcel, int64\_t \*value)

**Description**

Reads an int64\_t value from an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| int64\_t \*value | Pointer to the buffer for holding the read data. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the read operation fails.

 |

#### \[h2\]OH\_IPCParcel\_WriteFloat()

int OH\_IPCParcel\_WriteFloat(OHIPCParcel \*parcel, float value)

**Description**

Writes a float value to an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| float value | Value to write. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the write operation fails.

 |

#### \[h2\]OH\_IPCParcel\_ReadFloat()

int OH\_IPCParcel\_ReadFloat(const OHIPCParcel \*parcel, float \*value)

**Description**

Reads a float value from an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| float \*value | Pointer to the buffer for holding the read data. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the read operation fails.

 |

#### \[h2\]OH\_IPCParcel\_WriteDouble()

int OH\_IPCParcel\_WriteDouble(OHIPCParcel \*parcel, double value)

**Description**

Writes a double value to an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| double value | Value to write. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the write operation fails.

 |

#### \[h2\]OH\_IPCParcel\_ReadDouble()

int OH\_IPCParcel\_ReadDouble(const OHIPCParcel \*parcel, double \*value)

**Description**

Reads a double value from an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| double \*value | Pointer to the buffer for holding the read data. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the read operation fails.

 |

#### \[h2\]OH\_IPCParcel\_WriteString()

int OH\_IPCParcel\_WriteString(OHIPCParcel \*parcel, const char \*str)

**Description**

Writes a string including a string terminator to an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| const char \*str | Pointer to the string to write. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the write operation fails.

 |

#### \[h2\]OH\_IPCParcel\_ReadString()

const char\* OH\_IPCParcel\_ReadString(const OHIPCParcel \*parcel)

**Description**

Reads a string from an **OHIPCParcel** object. You can obtain the length of the string from **strlen**.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns the address of the string read if the operation is successful; returns NULL if the operation fails or invalid parameters are found. |

#### \[h2\]OH\_IPCParcel\_WriteBuffer()

int OH\_IPCParcel\_WriteBuffer(OHIPCParcel \*parcel, const uint8\_t \*buffer, int32\_t len)

**Description**

Writes data of the specified length from the memory to an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| const uint8\_t \*buffer | Pointer to the address of the memory information to write. |
| int32\_t len | Length of the data to write. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the write operation fails.

 |

#### \[h2\]OH\_IPCParcel\_ReadBuffer()

const uint8\_t\* OH\_IPCParcel\_ReadBuffer(const OHIPCParcel \*parcel, int32\_t len)

**Description**

Reads memory information of the specified length from an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| int32\_t len | Length of the memory to be read. |

**Returns**

| Type | Description |
| :-- | :-- |
| const uint8\_t\* | Returns the memory address read if the operation is successful; returns NULL if invalid parameters are found or **len** exceeds the readable length of **parcel**. |

#### \[h2\]OH\_IPCParcel\_WriteRemoteStub()

int OH\_IPCParcel\_WriteRemoteStub(OHIPCParcel \*parcel, const OHIPCRemoteStub \*stub)

**Description**

Writes an **OHIPCRemoteStub** object to an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| const [OHIPCRemoteStub](../../structs/ohipcremotestub/document.md) \*stub | Pointer to the **OHIPCRemoteStub** object to write. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the write operation fails.

 |

#### \[h2\]OH\_IPCParcel\_ReadRemoteStub()

OHIPCRemoteStub\* OH\_IPCParcel\_ReadRemoteStub(const OHIPCParcel \*parcel)

**Description**

Reads the **OHIPCRemoteStub** object from an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| OHIPCRemoteStub\* | Returns the pointer to the **OHIPCRemoteStub** object read if the operation is successful; returns NULL otherwise. |

#### \[h2\]OH\_IPCParcel\_WriteRemoteProxy()

int OH\_IPCParcel\_WriteRemoteProxy(OHIPCParcel \*parcel, const OHIPCRemoteProxy \*proxy)

**Description**

Writes an **OHIPCRemoteProxy** object to an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| const [OHIPCRemoteProxy](../../structs/ohipcremoteproxy/document.md) \*proxy | Pointer to the **OHIPCRemoteProxy** object to write. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the write operation fails.

 |

#### \[h2\]OH\_IPCParcel\_ReadRemoteProxy()

OHIPCRemoteProxy\* OH\_IPCParcel\_ReadRemoteProxy(const OHIPCParcel \*parcel)

**Description**

Reads the **OHIPCRemoteProxy** object from an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| OHIPCRemoteProxy\* | Returns the pointer to the **OHIPCRemoteProxy** object created if the operation is successful; returns NULL otherwise. |

#### \[h2\]OH\_IPCParcel\_WriteFileDescriptor()

int OH\_IPCParcel\_WriteFileDescriptor(OHIPCParcel \*parcel, int32\_t fd)

**Description**

Writes a file descriptor to an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| int32\_t fd | Pointer to the file descriptor to write. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the write operation fails.

 |

#### \[h2\]OH\_IPCParcel\_ReadFileDescriptor()

int OH\_IPCParcel\_ReadFileDescriptor(const OHIPCParcel \*parcel, int32\_t \*fd)

**Description**

Reads a file descriptor from an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| int32\_t \*fd | Pointer to the file descriptor to read. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the read operation fails.

 |

#### \[h2\]OH\_IPCParcel\_Append()

int OH\_IPCParcel\_Append(OHIPCParcel \*parcel, const OHIPCParcel \*data)

**Description**

Appends data to an **OHIPCParcel** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*data | Pointer to the data to append. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the concatenation fails.

 |

#### \[h2\]OH\_IPCParcel\_WriteInterfaceToken()

int OH\_IPCParcel\_WriteInterfaceToken(OHIPCParcel \*parcel, const char \*token)

**Description**

Writes an interface token to an **OHIPCParcel** object for interface identity verification.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| const char \*token | Pointer to the interface token to write. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the write operation fails.

 |

#### \[h2\]OH\_IPCParcel\_ReadInterfaceToken()

int OH\_IPCParcel\_ReadInterfaceToken(const OHIPCParcel \*parcel, char \*\*token, int32\_t \*len, OH\_IPC\_MemAllocator allocator)

**Description**

Reads an interface token from an **OHIPCParcel** object for interface identity verification.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*parcel | Pointer to the **OHIPCParcel** object. It cannot be NULL. |
| char \*\*token | Double pointer to the interface token to read. The memory is allocated by the allocator provided by the user and needs to be released. This pointer cannot be NULL. If an error code is returned, you still need to check whether the memory is empty and release the memory. Otherwise, memory leaks may occur. |
| int32\_t \*len | Pointer to the length of the interface token read, including the terminator. It cannot be NULL. |
| [OH\_IPC\_MemAllocator](#oh_ipc_memallocator) allocator | Memory allocator specified by the user for allocating memory for **token**. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found. Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the read operation fails.

 |
