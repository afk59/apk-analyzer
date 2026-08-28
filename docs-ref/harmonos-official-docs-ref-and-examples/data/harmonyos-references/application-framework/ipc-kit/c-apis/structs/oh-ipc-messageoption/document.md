# OH\_IPC\_MessageOption

typedef struct {...} OH\_IPC\_MessageOption

#### Overview

Defines an IPC message.

**Since**: 12

**Related module**: [OHIPCRemoteObject](../../modules/ohipcremoteobject/document.md)

**Header file**: [ipc\_cremote\_object.h](../../header-files/ipc-cremote-object-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [OH\_IPC\_RequestMode](../../header-files/ipc-cremote-object-h/document.md#oh_ipc_requestmode) mode | Message request mode. |
| uint32\_t timeout | Parameter reserved for RPC. It is invalid for IPC. |
| void\* reserved | Reserved parameter, which must be NULL. |
