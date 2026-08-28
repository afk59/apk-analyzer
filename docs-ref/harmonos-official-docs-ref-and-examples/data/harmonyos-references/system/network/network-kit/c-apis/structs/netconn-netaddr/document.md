# NetConn\_NetAddr

typedef struct NetConn\_NetAddr {...} NetConn\_NetAddr

#### Overview

Defines network addresses.

**Since**: 11

**Related module**: [NetConnection](../../modules/netconnection/document.md)

**Header file**: [net\_connection\_type.h](../../header-files/net-connection-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t family | Network address family. |
| uint8\_t prefixlen | Prefix length. |
| uint8\_t port | Port number. |
| char address[\[NETCONN\_MAX\_STR\_LEN\]](../../header-files/net-connection-type-h/document.md#macros) | Network address. |
