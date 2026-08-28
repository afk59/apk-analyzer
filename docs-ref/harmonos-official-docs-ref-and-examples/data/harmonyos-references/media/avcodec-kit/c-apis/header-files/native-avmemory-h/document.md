# native\_avmemory.h

#### Overview

The file declares the attribute definition of the media struct AVMemory.

**File to include**: <multimedia/player\_framework/native\_avmemory.h>

**Library**: libnative\_media\_core.so

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Related module**: [Core](../../modules/core/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVMemory](../../structs/oh-avmemory/document.md) | OH\_AVMemory | Describes a native object for the audio and video memory interface. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_AVMemory \*OH\_AVMemory\_Create(int32\_t size)](#oh_avmemory_create) | Creates an OH\_AVMemory instance. |
| [uint8\_t \*OH\_AVMemory\_GetAddr(struct OH\_AVMemory \*mem)](#oh_avmemory_getaddr) | Obtains the virtual memory address. |
| [int32\_t OH\_AVMemory\_GetSize(struct OH\_AVMemory \*mem)](#oh_avmemory_getsize) | Obtains the memory length. |
| [OH\_AVErrCode OH\_AVMemory\_Destroy(struct OH\_AVMemory \*mem)](#oh_avmemory_destroy) | Releases an OH\_AVMemory instance. |

#### Function Description

#### \[h2\]OH\_AVMemory\_Create()

OH\_AVMemory \*OH\_AVMemory\_Create(int32\_t size)

**Description**

Creates an OH\_AVMemory instance.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 10

**Deprecated from**: 11

**Substitute**: [OH\_AVBuffer\_Create](../native-avbuffer-h/document.md#oh_avbuffer_create)

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t size | Size of the created memory, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVMemory](../../structs/oh-avmemory/document.md) \* | 
Pointer to the OH\_AVMemory instance created. If the operation fails, NULL is returned.

The instance must be released by calling **OH\_AVMemory\_Destroy** when it is no longer required.

The possible causes of an operation failure are as follows:

1\. The value of **size** is less than or equal to **0**.

2\. The OH\_AVMemory instance fails to be created.

3\. Memory allocation fails.

 |

#### \[h2\]OH\_AVMemory\_GetAddr()

uint8\_t \*OH\_AVMemory\_GetAddr(struct OH\_AVMemory \*mem)

**Description**

Obtains the virtual memory address.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Deprecated from**: 11

**Substitute**: [OH\_AVBuffer\_GetAddr](../native-avbuffer-h/document.md#oh_avbuffer_getaddr)

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVMemory](../../structs/oh-avmemory/document.md) \*mem | Pointer to an OH\_AVMemory instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint8\_t \* | 
Pointer to the virtual memory address. If the memory is invalid, NULL is returned.

The possible causes of an operation failure are as follows:

1\. The value of **mem** is nullptr.

2\. The value of **mem** fails parameter structure verification.

3\. The memory in the passed-in value of **mem** is nullptr.

 |

#### \[h2\]OH\_AVMemory\_GetSize()

int32\_t OH\_AVMemory\_GetSize(struct OH\_AVMemory \*mem)

**Description**

Obtains the memory length.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Deprecated from**: 11

**Substitute**: [OH\_AVBuffer\_GetCapacity](../native-avbuffer-h/document.md#oh_avbuffer_getcapacity)

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVMemory](../../structs/oh-avmemory/document.md) \*mem | Pointer to an OH\_AVMemory instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Memory size. If the memory is invalid, **\-1** is returned.

The possible causes of an operation failure are as follows:

1\. The value of **mem** is nullptr.

2\. The value of **mem** fails parameter structure verification.

3\. The memory in the passed-in value of **mem** is nullptr.

 |

#### \[h2\]OH\_AVMemory\_Destroy()

OH\_AVErrCode OH\_AVMemory\_Destroy(struct OH\_AVMemory \*mem)

**Description**

Releases an OH\_AVMemory instance.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 10

**Deprecated from**: 11

**Substitute**: [OH\_AVBuffer\_Destroy](../native-avbuffer-h/document.md#oh_avbuffer_destroy)

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVMemory](../../structs/oh-avmemory/document.md) \*mem | Pointer to an OH\_AVMemory instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The release operation is successful.

**AV\_ERR\_INVALID\_VAL**:

1\. The value of **mem** is nullptr.

2\. The value of **mem** fails parameter structure verification.

3\. The value of **mem** is not created by the caller.

 |
