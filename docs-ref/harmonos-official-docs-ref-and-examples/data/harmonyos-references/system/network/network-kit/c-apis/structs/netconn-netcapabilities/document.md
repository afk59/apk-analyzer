# NetConn\_NetCapabilities

typedef struct NetConn\_NetCapabilities {...} NetConn\_NetCapabilities

#### Overview

Defines network capability sets.

**Since**: 11

**Related module**: [NetConnection](../../modules/netconnection/document.md)

**Header file**: [net\_connection\_type.h](../../header-files/net-connection-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t linkUpBandwidthKbps | Uplink bandwidth. |
| uint32\_t linkDownBandwidthKbps | Downlink bandwidth. |
| [NetConn\_NetCap](../../header-files/net-connection-type-h/document.md#netconn_netcap) netCaps[\[NETCONN\_MAX\_CAP\_SIZE\]](../../header-files/net-connection-type-h/document.md#macros) | Network capability list. |
| int32\_t netCapsSize | Actual size of the network capability list. |
| [NetConn\_NetBearerType](../../header-files/net-connection-type-h/document.md#netconn_netbearertype) bearerTypes[\[NETCONN\_MAX\_BEARER\_TYPE\_SIZE\]](../../header-files/net-connection-type-h/document.md#macros) | Bearer type list. |
| int32\_t bearerTypesSize | Actual size of the bearer type list. |
