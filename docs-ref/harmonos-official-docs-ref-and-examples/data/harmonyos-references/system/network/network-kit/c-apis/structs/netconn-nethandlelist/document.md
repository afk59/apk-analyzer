# NetConn\_NetHandleList

typedef struct NetConn\_NetHandleList {...} NetConn\_NetHandleList

#### Overview

Defines the network list.

**Since**: 11

**Related module**: [NetConnection](../../modules/netconnection/document.md)

**Header file**: [net\_connection\_type.h](../../header-files/net-connection-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [NetConn\_NetHandle](../netconn-nethandle/document.md) netHandles[\[NETCONN\_MAX\_NET\_SIZE\]](../../header-files/net-connection-type-h/document.md#macros) | Network handle list. |
| int32\_t netHandleListSize | Actual size of the network handle list. |
