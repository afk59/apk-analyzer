# ipc\_cremote\_object.h

#### Overview

Provides C APIs for creating and destroying a remote object, transferring data, and observing the dead status of a remote object.

**File to include**: <IPCKit/ipc\_cremote\_object.h>

**Library**: libipc\_capi.so

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Related module**: [OHIPCRemoteObject](../../modules/ohipcremoteobject/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_IPC\_MessageOption](../../structs/oh-ipc-messageoption/document.md) | \- | Defines an IPC message. |
| [OHIPCDeathRecipient](../../structs/ohipcdeathrecipient/document.md) | OHIPCDeathRecipient | Defines an object that receives death notifications. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_IPC\_RequestMode](#oh_ipc_requestmode) | OH\_IPC\_RequestMode | Enumerates the IPC request modes. |

#### \[h2\]Function

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef int (\*OH\_OnRemoteRequestCallback)(uint32\_t code, const OHIPCParcel \*data, OHIPCParcel \*reply, void \*userData)](#oh_onremoterequestcallback) | OH\_OnRemoteRequestCallback | Called to process the peer request at the stub. |
| [typedef void (\*OH\_OnRemoteDestroyCallback)(void \*userData)](#oh_onremotedestroycallback) | OH\_OnRemoteDestroyCallback | Called when an observed object is destroyed. |
| [OHIPCRemoteStub\* OH\_IPCRemoteStub\_Create(const char \*descriptor, OH\_OnRemoteRequestCallback requestCallback, OH\_OnRemoteDestroyCallback destroyCallback, void \*userData)](#oh_ipcremotestub_create) | \- | Creates an **OHIPCRemoteStub** object. |
| [void OH\_IPCRemoteStub\_Destroy(OHIPCRemoteStub \*stub)](#oh_ipcremotestub_destroy) | \- | Destroys an **OHIPCRemoteStub** object. |
| [void OH\_IPCRemoteProxy\_Destroy(OHIPCRemoteProxy \*proxy)](#oh_ipcremoteproxy_destroy) | \- | Destroys an **OHIPCRemoteProxy** object. |
| [int OH\_IPCRemoteProxy\_SendRequest(const OHIPCRemoteProxy \*proxy, uint32\_t code, const OHIPCParcel \*data, OHIPCParcel \*reply, const OH\_IPC\_MessageOption \*option)](#oh_ipcremoteproxy_sendrequest) | \- | Sends an IPC message. |
| [int OH\_IPCRemoteProxy\_GetInterfaceDescriptor(OHIPCRemoteProxy \*proxy, char \*\*descriptor, int32\_t \*len, OH\_IPC\_MemAllocator allocator)](#oh_ipcremoteproxy_getinterfacedescriptor) | \- | Obtains the interface descriptor from the stub. |
| [typedef void (\*OH\_OnDeathRecipientCallback)(void \*userData)](#oh_ondeathrecipientcallback) | OH\_OnDeathRecipientCallback | Defines a callback to be invoked when the remote **OHIPCRemoteStub** object dies unexpectedly. |
| [typedef void (\*OH\_OnDeathRecipientDestroyCallback)(void \*userData)](#oh_ondeathrecipientdestroycallback) | OH\_OnDeathRecipientDestroyCallback | Defines a callback to be invoked when the **OHIPCDeathRecipient** object is destroyed. |
| [OHIPCDeathRecipient\* OH\_IPCDeathRecipient\_Create(OH\_OnDeathRecipientCallback deathRecipientCallback, OH\_OnDeathRecipientDestroyCallback destroyCallback, void \*userData)](#oh_ipcdeathrecipient_create) | \- | Creates an **OHIPCDeathRecipient** object. |
| [void OH\_IPCDeathRecipient\_Destroy(OHIPCDeathRecipient \*recipient)](#oh_ipcdeathrecipient_destroy) | \- | Destroys an **OHIPCDeathRecipient** object. |
| [int OH\_IPCRemoteProxy\_AddDeathRecipient(OHIPCRemoteProxy \*proxy, OHIPCDeathRecipient \*recipient)](#oh_ipcremoteproxy_adddeathrecipient) | \- | Subscribes to the death of an **OHIPCRemoteStub** object for an **OHIPCRemoteProxy** object. |
| [int OH\_IPCRemoteProxy\_RemoveDeathRecipient(OHIPCRemoteProxy \*proxy, OHIPCDeathRecipient \*recipient)](#oh_ipcremoteproxy_removedeathrecipient) | \- | Unsubscribes from the death of the **OHIPCRemoteStub** object for an **OHIPCRemoteProxy** object. |
| [int OH\_IPCRemoteProxy\_IsRemoteDead(const OHIPCRemoteProxy \*proxy)](#oh_ipcremoteproxy_isremotedead) | \- | Checks whether the **OHIPCRemoteStub** object corresponding to the **OHIPCRemoteProxy** object is dead. |

#### Enum Description

#### \[h2\]OH\_IPC\_RequestMode

enum OH\_IPC\_RequestMode

**Description**

Enumerates the IPC request modes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| OH\_IPC\_REQUEST\_MODE\_SYNC = 0 | Synchronous request. |
| OH\_IPC\_REQUEST\_MODE\_ASYNC = 1 | Asynchronous request. |

#### Function Description

#### \[h2\]OH\_OnRemoteRequestCallback()

typedef int(\*OH\_OnRemoteRequestCallback)(uint32\_t code, const OHIPCParcel \*data, OHIPCParcel \*reply, void \*userData)

**Description**

Called to process the peer request at the stub.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| uint32\_t code | 
Customized communication command word.

Value range: \[0x01, 0x00ffffff\]

 |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*data | Pointer to the requested data object. It cannot be NULL or released in the function. |
| [OHIPCParcel](../../modules/ohipcparcel/document.md) \*reply | Pointer to the response data object. It cannot be NULL or released in the function. If this function returns an error, data cannot be written to this parameter. |
| void \*userData | Pointer to the private user data. It can be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns a custom error code in the range \[1909001, 1909999\] or a system error code otherwise.

If the custom error code is out of range, [OH\_IPC\_ErrorCode#OH\_IPC\_INVALID\_USER\_ERROR\_CODE](../ipc-error-code-h/document.md#oh_ipc_errorcode) is returned.

 |

#### \[h2\]OH\_OnRemoteDestroyCallback()

typedef void(\*OH\_OnRemoteDestroyCallback)(void \*userData)

**Description**

Called when an observed object is destroyed.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| void \*userData | Pointer to the private user data. It can be NULL. |

#### \[h2\]OH\_IPCRemoteStub\_Create()

OHIPCRemoteStub\* OH\_IPCRemoteStub\_Create(const char \*descriptor, OH\_OnRemoteRequestCallback requestCallback, OH\_OnRemoteDestroyCallback destroyCallback, void \*userData)

**Description**

Creates an **OHIPCRemoteStub** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*descriptor | Pointer to the descriptor of the **OHIPCRemoteStub** object to create. It cannot be NULL. |
| [OH\_OnRemoteRequestCallback](#oh_onremoterequestcallback) requestCallback | Callback used to process the data request. It cannot be NULL. |
| [OH\_OnRemoteDestroyCallback](#oh_onremotedestroycallback) destroyCallback | Callback to be invoked when the object is destroyed. It can be NULL. |
| void \*userData | Pointer to the private user data. It can be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| OHIPCRemoteStub\* | Returns the pointer to the **OHIPCRemoteStub** object created if the operation is successful; returns NULL otherwise. |

#### \[h2\]OH\_IPCRemoteStub\_Destroy()

void OH\_IPCRemoteStub\_Destroy(OHIPCRemoteStub \*stub)

**Description**

Destroys an **OHIPCRemoteStub** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCRemoteStub](../../structs/ohipcremotestub/document.md) \*stub | Pointer to the **OHIPCRemoteStub** object to destroy. |

#### \[h2\]OH\_IPCRemoteProxy\_Destroy()

void OH\_IPCRemoteProxy\_Destroy(OHIPCRemoteProxy \*proxy)

**Description**

Destroys an **OHIPCRemoteProxy** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCRemoteProxy](../../structs/ohipcremoteproxy/document.md) \*proxy | Pointer to the **OHIPCRemoteProxy** object to destroy. |

#### \[h2\]OH\_IPCRemoteProxy\_SendRequest()

int OH\_IPCRemoteProxy\_SendRequest(const OHIPCRemoteProxy \*proxy, uint32\_t code, const OHIPCParcel \*data, OHIPCParcel \*reply, const OH\_IPC\_MessageOption \*option)

**Description**

Sends an IPC message.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OHIPCRemoteProxy](../../structs/ohipcremoteproxy/document.md) \*proxy | Pointer to the **OHIPCRemoteProxy** object. It cannot be NULL. |
| uint32\_t code | Customized IPC command word, in the range \[0x01, 0x00ffffff\]. |
| const [OHIPCParcel](../../modules/ohipcparcel/document.md) \*data | Pointer to the requested data object. It cannot be NULL. |
| [OHIPCParcel](../../modules/ohipcparcel/document.md) \*reply | Pointer to the response data object. It cannot be NULL in the case of a synchronous request, and can be NULL in the case of an asynchronous request. |
| const [OH\_IPC\_MessageOption](../../structs/oh-ipc-messageoption/document.md) \*option | Pointer to the message option. It can be NULL, which indicates a synchronous request. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the message is sent successfully.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if invalid parameters are found.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_DEAD\_REMOTE\_OBJECT](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the remote **OHIPCRemoteStub** object dies.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CODE\_OUT\_OF\_RANGE](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the code is out of range.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_INNER\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) or a custom error code in other cases.

 |

#### \[h2\]OH\_IPCRemoteProxy\_GetInterfaceDescriptor()

int OH\_IPCRemoteProxy\_GetInterfaceDescriptor(OHIPCRemoteProxy \*proxy, char \*\*descriptor, int32\_t \*len, OH\_IPC\_MemAllocator allocator)

**Description**

Obtains the interface descriptor from the stub.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCRemoteProxy](../../structs/ohipcremoteproxy/document.md) \*proxy | Pointer to the **OHIPCRemoteProxy** object. It cannot be NULL. |
| char \*\*descriptor | Pointer to the address of the memory for holding the interface descriptor. The memory is allocated by the allocator provided by the user and needs to be released. This pointer cannot be NULL. If an error code is returned, you still need to check whether the memory is empty and release the memory. Otherwise, memory leaks may occur. |
| int32\_t \*len | Pointer to the length of the data written to the descriptor, including the terminator. It cannot be NULL. |
| [OH\_IPC\_MemAllocator](../ipc-cparcel-h/document.md#oh_ipc_memallocator) allocator | Memory allocator specified by the user for allocating memory for **identity**. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the message is sent successfully.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the parameters are incorrect.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_DEAD\_REMOTE\_OBJECT](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the remote **OHIPCRemoteStub** object dies.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_MEM\_ALLOCATOR\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the memory allocation fails.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) or a custom error code if the data in the serialized object fails to be read.

 |

#### \[h2\]OH\_OnDeathRecipientCallback()

typedef void (\*OH\_OnDeathRecipientCallback)(void \*userData)

**Description**

Defines a callback to be invoked when the remote **OHIPCRemoteStub** object dies unexpectedly.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| void \*userData | Pointer to the private user data. It can be NULL. |

#### \[h2\]OH\_OnDeathRecipientDestroyCallback()

typedef void (\*OH\_OnDeathRecipientDestroyCallback)(void \*userData)

**Description**

Defines a callback to be invoked when the **OHIPCDeathRecipient** object is destroyed.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| void \*userData | Pointer to the private user data. It can be NULL. |

#### \[h2\]OH\_IPCDeathRecipient\_Create()

OHIPCDeathRecipient\* OH\_IPCDeathRecipient\_Create(OH\_OnDeathRecipientCallback deathRecipientCallback, OH\_OnDeathRecipientDestroyCallback destroyCallback, void \*userData)

**Description**

Creates an **OHIPCDeathRecipient** object, which triggers a notification when the **OHIPCRemoteStub** object dies unexpectedly.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_OnDeathRecipientCallback](#oh_ondeathrecipientcallback) deathRecipientCallback | Callback to be invoked when the **OHIPCRemoteStub** object is dead. It cannot be NULL. |
| [OH\_OnDeathRecipientDestroyCallback](#oh_ondeathrecipientdestroycallback) destroyCallback | Callback to be invoked when the object is destroyed. It can be NULL. |
| void \*userData | Pointer to the private user data. It can be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| OHIPCDeathRecipient\* | Returns the pointer to the **OHIPCDeathRecipient** object created if the operation is successful; returns NULL otherwise. |

#### \[h2\]OH\_IPCDeathRecipient\_Destroy()

void OH\_IPCDeathRecipient\_Destroy(OHIPCDeathRecipient \*recipient)

**Description**

Destroys an **OHIPCDeathRecipient** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCDeathRecipient](../../structs/ohipcdeathrecipient/document.md) \*recipient | Pointer to the **OHIPCDeathRecipient** object to destroy. |

#### \[h2\]OH\_IPCRemoteProxy\_AddDeathRecipient()

int OH\_IPCRemoteProxy\_AddDeathRecipient(OHIPCRemoteProxy \*proxy, OHIPCDeathRecipient \*recipient)

**Description**

Subscribes to the death of an **OHIPCRemoteStub** object for an **OHIPCRemoteProxy** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCRemoteProxy](../../structs/ohipcremoteproxy/document.md) \*proxy | Pointer to the **OHIPCRemoteProxy** object that subscribes to the death notification. It cannot be NULL. |
| [OHIPCDeathRecipient](../../structs/ohipcdeathrecipient/document.md) \*recipient | Pointer to the object that receives the death notification of the **OHIPCRemoteStub** object. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the parameters are incorrect.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_INNER\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) in other cases.

 |

#### \[h2\]OH\_IPCRemoteProxy\_RemoveDeathRecipient()

int OH\_IPCRemoteProxy\_RemoveDeathRecipient(OHIPCRemoteProxy \*proxy, OHIPCDeathRecipient \*recipient)

**Description**

Unsubscribes from the death of the **OHIPCRemoteStub** object for an **OHIPCRemoteProxy** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCRemoteProxy](../../structs/ohipcremoteproxy/document.md) \*proxy | Pointer to the **OHIPCRemoteProxy** object that unsubscribes from the death notification. It cannot be NULL. |
| [OHIPCDeathRecipient](../../structs/ohipcdeathrecipient/document.md) \*recipient | Pointer to the object that receives the death notification of the **OHIPCRemoteStub** object. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns [OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the operation is successful.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) if the parameters are incorrect.

Returns [OH\_IPC\_ErrorCode#OH\_IPC\_INNER\_ERROR](../ipc-error-code-h/document.md#oh_ipc_errorcode) in other cases.

 |

#### \[h2\]OH\_IPCRemoteProxy\_IsRemoteDead()

int OH\_IPCRemoteProxy\_IsRemoteDead(const OHIPCRemoteProxy \*proxy)

**Description**

Checks whether the **OHIPCRemoteStub** object corresponding to the **OHIPCRemoteProxy** object is dead.

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OHIPCRemoteProxy](../../structs/ohipcremoteproxy/document.md) \*proxy | Pointer to the **OHIPCRemoteProxy** object to check. It cannot be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **1** if the **OHIPCRemoteStub** object is dead or invalid parameters are found; returns **0** otherwise. If invalid parameters are found, the **OHIPCRemoteStub** object does not exist. |
