# WebSocket\_CloseOption

struct WebSocket\_CloseOption {...}

#### Overview

Defines the parameters for the proactive connection closure initiated by the WebSocket client.

**Since**: 11

**Related module**: [netstack](../../modules/netstack/document.md)

**Header file**: [net\_websocket\_type.h](../../header-files/net-websocket-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t code | Error code. |
| const char \*reason | Error cause. |
