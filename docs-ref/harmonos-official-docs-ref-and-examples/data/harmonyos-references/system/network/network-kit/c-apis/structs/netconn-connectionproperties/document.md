# NetConn\_ConnectionProperties

typedef struct NetConn\_ConnectionProperties {...} NetConn\_ConnectionProperties

#### Overview

Defines the network connection properties.

**Since**: 11

**Related module**: [NetConnection](../../modules/netconnection/document.md)

**Header file**: [net\_connection\_type.h](../../header-files/net-connection-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char ifaceName[\[NETCONN\_MAX\_STR\_LEN\]](../../header-files/net-connection-type-h/document.md#macros) | Network interface name. |
| char domain[\[NETCONN\_MAX\_STR\_LEN\]](../../header-files/net-connection-type-h/document.md#macros) | Domain name of the network connection. |
| char tcpBufferSizes[\[NETCONN\_MAX\_STR\_LEN\]](../../header-files/net-connection-type-h/document.md#macros) | TCP buffer size. |
| uint16\_t mtu | Maximum transmission unit. |
| [NetConn\_NetAddr](../netconn-netaddr/document.md) netAddrList[\[NETCONN\_MAX\_ADDR\_SIZE\]](../../header-files/net-connection-type-h/document.md#macros) | Address list. |
| int32\_t netAddrListSize | Actual size of the address list. |
| [NetConn\_NetAddr](../netconn-netaddr/document.md) dnsList[\[NETCONN\_MAX\_ADDR\_SIZE\]](../../header-files/net-connection-type-h/document.md#macros) | DNS list. |
| int32\_t dnsListSize | Actual size of the DNS list. |
| [NetConn\_Route](../netconn-route/document.md) routeList[\[NETCONN\_MAX\_ROUTE\_SIZE\]](../../header-files/net-connection-type-h/document.md#macros) | Route list. |
| int32\_t routeListSize | Actual size of the route list. |
| [NetConn\_HttpProxy](../netconn-httpproxy/document.md) httpProxy | HTTP proxy information. |
