# NetConn\_TraceRouteInfo

typedef struct NetConn\_TraceRouteInfo {...} NetConn\_TraceRouteInfo

#### Overview

Defines the trace route information.

**Since**: 20

**Related module**: [NetConnection](../../modules/netconnection/document.md)

**Header file**: [net\_connection\_type.h](../../header-files/net-connection-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t jumpNo | Number of hops. |
| char address[\[NETCONN\_MAX\_STR\_LEN\]](../../header-files/net-connection-type-h/document.md#macros) | Host name or address. |
| uint32\_t rtt[\[NETCONN\_MAX\_RTT\_NUM\]](../../header-files/net-connection-type-h/document.md#macros) | Round-trip time in ms, including the maximum, minimum, average, and standard deviations. |
