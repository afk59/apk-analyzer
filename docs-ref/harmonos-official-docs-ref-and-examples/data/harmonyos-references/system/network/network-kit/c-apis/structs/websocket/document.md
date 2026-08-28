# WebSocket

struct WebSocket {...}

#### Overview

Defines the WebSocket client struct.

**Since**: 11

**Related module**: [netstack](../../modules/netstack/document.md)

**Header file**: [net\_websocket\_type.h](../../header-files/net-websocket-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [WebSocket\_OnOpenCallback](../../header-files/net-websocket-type-h/document.md#websocket_onopencallback) onOpen | Pointer to the callback invoked when the WebSocket client receives a connection message. |
| [WebSocket\_OnMessageCallback](../../header-files/net-websocket-type-h/document.md#websocket_onmessagecallback) onMessage | Pointer to the callback invoked when the WebSocket client receives a message. |
| [WebSocket\_OnErrorCallback](../../header-files/net-websocket-type-h/document.md#websocket_onerrorcallback) onError | Pointer to the callback invoked when the WebSocket client receives an error message. |
| [WebSocket\_OnCloseCallback](../../header-files/net-websocket-type-h/document.md#websocket_onclosecallback) onClose | Pointer to the callback invoked when the WebSocket client receives a **close** message. |
| [WebSocket\_RequestOptions](../websocket-requestoptions/document.md) requestOptions | Options of the connection request. |
