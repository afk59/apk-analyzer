# NetConn\_ProbeResultInfo

typedef struct NetConn\_ProbeResultInfo {...} NetConn\_ProbeResultInfo

#### Overview

Defines the probe result.

**Since**: 20

**Related module**: [NetConnection](../../modules/netconnection/document.md)

**Header file**: [net\_connection\_type.h](../../header-files/net-connection-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t lossRate | Packet loss rate, in percentage. The value **100** indicates 100% packet loss, and the value **50** indicates 50% packet loss. |
| uint32\_t rtt[\[NETCONN\_MAX\_RTT\_NUM\]](../../header-files/net-connection-type-h/document.md#macros) | Round-trip time in ms, including the maximum, minimum, average, and standard deviations. |
