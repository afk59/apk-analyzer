# Http\_PerformanceTiming

typedef struct Http\_PerformanceTiming {...} Http\_PerformanceTiming

#### Overview

Defines the HTTP response timing information, which will be collected via {@link Http\_Response.performanceTiming}.

**Since**: 20

**Related module**: [netstack](../../modules/netstack/document.md)

**Header file**: [net\_http\_type.h](../../header-files/net-http-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| double dnsTiming | Duration from the time when the request is initiated to the time when the DNS resolution is complete. |
| double tcpTiming | Duration from the time when the request is initiated to the time when the TCP connection is complete. |
| double tlsTiming | Duration from the time when the request is initiated to the time when the TLS connection is complete. |
| double firstSendTiming | Duration from the time when the request is initiated to the time when the first byte is sent. |
| double firstReceiveTiming | Duration from the time when the request is initiated to the time when the first byte is received. |
| double totalFinishTiming | Duration from the time when the request is initiated to the time when the request is complete. |
| double redirectTiming | Duration from the time when the request is initiated to the time when all redirection steps are complete. |
