# WebSocket\_CloseResult

struct WebSocket\_CloseResult {...}

#### Overview

Defines the parameters for the connection closure received by the WebSocket client.

**Since**: 11

**Related module**: [netstack](../../modules/netstack/document.md)

**Header file**: [net\_websocket\_type.h](../../header-files/net-websocket-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t code | Error code. |
| const char \*reason | Error cause. |
