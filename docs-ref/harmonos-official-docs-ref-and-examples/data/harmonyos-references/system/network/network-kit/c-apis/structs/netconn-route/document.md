# NetConn\_Route

typedef struct NetConn\_Route {...} NetConn\_Route

#### Overview

Defines the route configuration.

**Since**: 11

**Related module**: [NetConnection](../../modules/netconnection/document.md)

**Header file**: [net\_connection\_type.h](../../header-files/net-connection-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char iface[\[NETCONN\_MAX\_STR\_LEN\]](../../header-files/net-connection-type-h/document.md#macros) | Network interface. |
| [NetConn\_NetAddr](../netconn-netaddr/document.md) destination | Destination address. |
| [NetConn\_NetAddr](../netconn-netaddr/document.md) gateway | Gateway IP address. |
| int32\_t hasGateway | Whether a gateway exists. |
| int32\_t isDefaultRoute | Whether the default route is used. |
