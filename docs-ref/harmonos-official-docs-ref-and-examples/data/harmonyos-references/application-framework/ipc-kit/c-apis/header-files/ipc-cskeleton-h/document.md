# ipc\_cskeleton.h

#### Overview

Provides C APIs for managing the token IDs, credentials, process IDs (PIDs), user IDs (UIDs), and thread pool in the IPC framework.

**File to include**: <IPCKit/ipc\_cskeleton.h>

**Library**: libipc\_capi.so

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Related module**: [OHIPCSkeleton](../../modules/ohipcskeleton/document.md)

#### Summary

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [void OH\_IPCSkeleton\_JoinWorkThread(void)](#oh_ipcskeleton_joinworkthread) | Joints this thread to the IPC worker thread pool. |
| [void OH\_IPCSkeleton\_StopWorkThread(void)](#oh_ipcskeleton_stopworkthread) | Stops this thread. |
| [uint64\_t OH\_IPCSkeleton\_GetCallingTokenId(void)](#oh_ipcskeleton_getcallingtokenid) | Obtains the token ID of the caller. This function must be called in the IPC context. Otherwise, the local token ID is returned. |
| [uint64\_t OH\_IPCSkeleton\_GetFirstTokenId(void)](#oh_ipcskeleton_getfirsttokenid) | Obtains the token ID of the first caller. |
| [uint64\_t OH\_IPCSkeleton\_GetSelfTokenId(void)](#oh_ipcskeleton_getselftokenid) | Obtains the local token ID. |
| [uint64\_t OH\_IPCSkeleton\_GetCallingPid(void)](#oh_ipcskeleton_getcallingpid) | Obtains the PID of the caller. This function must be called in the IPC context. Otherwise, the local PID is returned. |
| [uint64\_t OH\_IPCSkeleton\_GetCallingUid(void)](#oh_ipcskeleton_getcallinguid) | Obtains the UID of the caller. This function must be called in the IPC context. Otherwise, the local UID is returned. |
| [int OH\_IPCSkeleton\_IsLocalCalling(void)](#oh_ipcskeleton_islocalcalling) | Checks whether a local calling is being made. |
| [int OH\_IPCSkeleton\_SetMaxWorkThreadNum(const int maxThreadNum)](#oh_ipcskeleton_setmaxworkthreadnum) | Sets the maximum number of worker threads. |
| [int OH\_IPCSkeleton\_ResetCallingIdentity(char \*\*identity, int32\_t \*len, OH\_IPC\_MemAllocator allocator)](#oh_ipcskeleton_resetcallingidentity) | Resets the caller identity credential (including the token ID, UID, and PID) to that of this process and returns the caller credential information. The credential information is used in **OH\_IPCSkeleton\_SetCallingIdentity**. |
| [int OH\_IPCSkeleton\_SetCallingIdentity(const char \*identity)](#oh_ipcskeleton_setcallingidentity) | Sets the caller credential information to the IPC context. |
| [int OH\_IPCSkeleton\_IsHandlingTransaction(void)](#oh_ipcskeleton_ishandlingtransaction) | Checks whether an IPC request is being handled. |

#### Function Description

#### \[h2\]OH\_IPCSkeleton\_JoinWorkThread()

void OH\_IPCSkeleton\_JoinWorkThread(void)

**Description**

Joints this thread to the IPC worker thread pool.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

#### \[h2\]OH\_IPCSkeleton\_StopWorkThread()

void OH\_IPCSkeleton\_StopWorkThread(void)

**Description**

Stops this thread.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

#### \[h2\]OH\_IPCSkeleton\_GetCallingTokenId()

uint64\_t OH\_IPCSkeleton\_GetCallingTokenId(void)

**Description**

Obtains the token ID of the caller. This function must be called in the IPC context. Otherwise, the local token ID is returned.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| uint64\_t | Returns the caller token ID. |

#### \[h2\]OH\_IPCSkeleton\_GetFirstTokenId()

uint64\_t OH\_IPCSkeleton\_GetFirstTokenId(void)

**Description**

Obtains the token ID of the first caller.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| uint64\_t | Returns the token ID of the first caller. |

#### \[h2\]OH\_IPCSkeleton\_GetSelfTokenId()

uint64\_t OH\_IPCSkeleton\_GetSelfTokenId(void)

**Description**

Obtains the local token ID.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| uint64\_t | Returns the local token ID. |

#### \[h2\]OH\_IPCSkeleton\_GetCallingPid()

uint64\_t OH\_IPCSkeleton\_GetCallingPid(void)

**Description**

Obtains the PID of the caller. This function must be called in the IPC context. Otherwise, the local PID is returned.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| uint64\_t | Returns the caller PID. |

#### \[h2\]OH\_IPCSkeleton\_GetCallingUid()

uint64\_t OH\_IPCSkeleton\_GetCallingUid(void)

**Description**

Obtains the UID of the caller. This function must be called in the IPC context. Otherwise, the local UID is returned.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| uint64\_t | Returns the caller UID. |

#### \[h2\]OH\_IPCSkeleton\_IsLocalCalling()

int OH\_IPCSkeleton\_IsLocalCalling(void)

**Description**

Checks whether a local calling is being made.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **1** if a local calling is in progress; returns **0** otherwise. |

#### \[h2\]OH\_IPCSkeleton\_SetMaxWorkThreadNum()

int OH\_IPCSkeleton\_SetMaxWorkThreadNum(const int maxThreadNum)

**Description**

Sets the maximum number of worker threads.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const int maxThreadNum | 
Maximum number of worker threads.

Value range: \[1, 32\]

Default value: **16**

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the parameters are incorrect.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_INNER\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) in other cases.

 |

#### \[h2\]OH\_IPCSkeleton\_ResetCallingIdentity()

int OH\_IPCSkeleton\_ResetCallingIdentity(char \*\*identity, int32\_t \*len, OH\_IPC\_MemAllocator allocator)

**Description**

Resets the caller identity credential (including the token ID, UID, and PID) to that of this process and returns the caller credential information. The credential information is used in **OH\_IPCSkeleton\_SetCallingIdentity**.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| char \*\*identity | Double pointer to the address of the memory for holding the caller identity information. The memory is allocated by the allocator provided by the user and needs to be released. This pointer cannot be NULL. |
| int32\_t \*len | Pointer to the length of the data written to the identity. The value cannot be empty. |
| [OH\_IPC\_MemAllocator](../ipc-cparcel-h/document.md#oh_ipc_memallocator) allocator | Memory allocator specified by the user for allocating memory for **identity**. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the parameters are incorrect.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_MEM\_ALLOCATOR\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the memory allocation fails.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_INNER\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) in other cases.

 |

#### \[h2\]OH\_IPCSkeleton\_SetCallingIdentity()

int OH\_IPCSkeleton\_SetCallingIdentity(const char \*identity)

**Description**

Sets the caller credential information to the IPC context.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*identity | Pointer to the caller credential, which cannot be empty. The value is returned by **OH\_IPCSkeleton\_ResetCallingIdentity**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the parameters are incorrect.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_INNER\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) in other cases.

 |

#### \[h2\]OH\_IPCSkeleton\_IsHandlingTransaction()

int OH\_IPCSkeleton\_IsHandlingTransaction(void)

**Description**

Checks whether an IPC request is being handled.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **1** if an IPC request is being handled; returns **0** otherwise. |
