# NetConn\_TraceRouteOption

typedef struct NetConn\_TraceRouteOption {...} NetConn\_TraceRouteOption

#### Overview

Defines the network trace route options.

**Since**: 20

**Related module**: [NetConnection](../../modules/netconnection/document.md)

**Header file**: [net\_connection\_type.h](../../header-files/net-connection-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t maxJumpNumber | Maximum number of hops in the probe result. The value must be the same as that of **TraceRouteInfo**. The maximum number of hops is 30, which is also the default value. |
| NetConn\_PacketsType packetsType | Protocol type of the probe packet. The default value is **NETCONN\_PACKETS\_ICMP**. |
