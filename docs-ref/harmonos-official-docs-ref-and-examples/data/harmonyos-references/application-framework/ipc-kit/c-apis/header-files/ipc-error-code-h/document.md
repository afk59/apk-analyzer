# ipc\_error\_code.h

#### Overview

Defines the IPC error codes.

**File to include**: <IPCKit/ipc\_error\_code.h>

**Library**: libipc\_capi.so

**System capability**: SystemCapability.Communication.IPC.Core

**Since**: 12

**Related module**: [OHIPCErrorCode](../../modules/ohipcerrorcode/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_IPC\_ErrorCode](#oh_ipc_errorcode) | OH\_IPC\_ErrorCode | Enumerates IPC error messages. |

#### Enum Description

#### \[h2\]OH\_IPC\_ErrorCode

enum OH\_IPC\_ErrorCode

**Description**

Enumerates the IPC error codes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| OH\_IPC\_SUCCESS = 0 | Execution successful. |
| OH\_IPC\_ERROR\_CODE\_BASE = 1901000 | Start error code. |
| OH\_IPC\_CHECK\_PARAM\_ERROR = OH\_IPC\_ERROR\_CODE\_BASE | Invalid parameter. |
| OH\_IPC\_PARCEL\_WRITE\_ERROR = OH\_IPC\_ERROR\_CODE\_BASE + 1 | Failed to write data to the serialized object. |
| OH\_IPC\_PARCEL\_READ\_ERROR = OH\_IPC\_ERROR\_CODE\_BASE + 2 | Failed to read data from the serialized object. |
| OH\_IPC\_MEM\_ALLOCATOR\_ERROR = OH\_IPC\_ERROR\_CODE\_BASE + 3 | Failed to allocate memory. |
| OH\_IPC\_CODE\_OUT\_OF\_RANGE = OH\_IPC\_ERROR\_CODE\_BASE + 4 | The command word is out of the value range \[0x01, 0x00ffffff\]. |
| OH\_IPC\_DEAD\_REMOTE\_OBJECT = OH\_IPC\_ERROR\_CODE\_BASE + 5 | The remote object is dead. |
| OH\_IPC\_INVALID\_USER\_ERROR\_CODE = OH\_IPC\_ERROR\_CODE\_BASE + 6 | The custom error code is out of the range \[1900001, 1999999\]. |
| OH\_IPC\_INNER\_ERROR = OH\_IPC\_ERROR\_CODE\_BASE + 7 | IPC internal error. |
| OH\_IPC\_ERROR\_CODE\_MAX = OH\_IPC\_ERROR\_CODE\_BASE + 1000 | Maximum error code. |
| OH\_IPC\_USER\_ERROR\_CODE\_MIN = 1909000 | Minimum value for a custom error code. |
| OH\_IPC\_USER\_ERROR\_CODE\_MAX = 1909999 | Maximum value for a custom error code. |
