# net\_websocket\_type.h

#### Overview

Defines data structures for the C APIs of the WebSocket client module.

**File to include**: <network/netstack/net\_websocket\_type.h>

**Library**: libnet\_websocket.so

**System capability**: SystemCapability.Communication.NetStack

**Since**: 11

**Related module**: [netstack](../../modules/netstack/document.md)

#### Summary

#### \[h2\]Structs

| Name | Description |
| :-- | :-- |
| [WebSocket\_CloseResult](../../structs/websocket-closeresult/document.md) | Parameters for the **Close** message sent from the WebSocket server to client. |
| [WebSocket\_CloseOption](../../structs/websocket-closeoption/document.md) | Parameters for the connection closure initiated by the WebSocket client. |
| [WebSocket\_ErrorResult](../../structs/websocket-errorresult/document.md) | Parameters for the **Error** message sent from the WebSocket server to client. |
| [WebSocket\_OpenResult](../../structs/websocket-openresult/document.md) | Parameters for the **Open** message sent from the WebSocket server to client. |
| [WebSocket\_Header](../../structs/websocket-header/document.md) | Header linked list added to the WebSocket client. |
| [WebSocket\_RequestOptions](../../structs/websocket-requestoptions/document.md) | Parameters of the request for connection between the WebSocket client and server. |
| [WebSocket](../../structs/websocket/document.md) | WebSocket client structure. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*WebSocket\_OnOpenCallback)(struct WebSocket \*client, WebSocket\_OpenResult openResult)](#websocket_onopencallback) | WebSocket\_OnOpenCallback | Callback invoked when the WebSocket client receives an **Open** message. |
| [typedef void (\*WebSocket\_OnMessageCallback)(struct WebSocket \*client, char \*data, uint32\_t length)](#websocket_onmessagecallback) | WebSocket\_OnMessageCallback | Callback invoked when the WebSocket client receives data. |
| [typedef void (\*WebSocket\_OnErrorCallback)(struct WebSocket \*client, WebSocket\_ErrorResult errorResult)](#websocket_onerrorcallback) | WebSocket\_OnErrorCallback | Callback invoked when the WebSocket client receives an **Error** message. |
| [typedef void (\*WebSocket\_OnCloseCallback)(struct WebSocket \*client, WebSocket\_CloseResult closeResult)](#websocket_onclosecallback) | WebSocket\_OnCloseCallback | Callback invoked when the WebSocket client receives a **Close** message. |

#### Enum Description

#### \[h2\]WebSocket\_ErrCode

enum WebSocket\_ErrCode

**Description**

Defines the error codes of a WebSocket request.

**Since**: 11

| Value | Description |
| :-- | :-- |
| WEBSOCKET\_OK = 0 | Operation successful. |
| E\_BASE = 1000 | Base value of the error code. |
| WEBSOCKET\_CLIENT\_NULL = (E\_BASE + 1) | The WebSocket client is empty. |
| WEBSOCKET\_CLIENT\_NOT\_CREATED = (E\_BASE + 2) | The WebSocket client is not created. |
| WEBSOCKET\_CONNECTION\_ERROR = (E\_BASE + 3) | An error occurred during WebSocket connection establishment. |
| WEBSOCKET\_CONNECTION\_PARSE\_URL\_ERROR = (E\_BASE + 5) | An error occurred when parsing WebSocket connection parameters. |
| WEBSOCKET\_CONNECTION\_NO\_MEMORY = (E\_BASE + 6) | The memory is insufficient during WebSocket client connection establishment. |
| WEBSOCKET\_CONNECTION\_CLOSED\_BY\_PEER = (E\_BASE + 7) | The WebSocket connection is closed by the peer end. |
| WEBSOCKET\_DESTROYED = (E\_BASE + 8) | The WebSocket connection is disconnected. |
| WEBSOCKET\_PROTOCOL\_ERROR = (E\_BASE + 9) | Incorrect protocol. |
| WEBSOCKET\_SEND\_NO\_MEMORY = (E\_BASE + 10) | The system memory is insufficient when the WebSocket client sends data. |
| WEBSOCKET\_SEND\_DATA\_NULL = (E\_BASE + 11) | The sent data is empty. |
| WEBSOCKET\_DATA\_LENGTH\_EXCEEDED = (E\_BASE + 12) | The length of the sent data exceeds the limit. |
| WEBSOCKET\_QUEUE\_LENGTH\_EXCEEDED = (E\_BASE + 13) | The length of the sent data queue exceeds the limit. |
| WEBSOCKET\_NO\_CLIENT\_CONTEXT = (E\_BASE + 14) | The context of the WebSocket client is null. |
| WEBSOCKET\_NO\_HEADER\_CONTEXT = (E\_BASE + 15) | The protocol header of the WebSocket client is empty. |
| WEBSOCKET\_HEADER\_EXCEEDED = (E\_BASE + 16) | The protocol header of the WebSocket client exceeds the limit. |
| WEBSOCKET\_NO\_CONNECTION = (E\_BASE + 17) | The WebSocket client is not connected. |
| WEBSOCKET\_NO\_CONNECTION\_CONTEXT = (E\_BASE + 18) | No WebSocket connection context is released. |

#### Function Description

#### \[h2\]WebSocket\_OnOpenCallback()

typedef void (\*WebSocket\_OnOpenCallback)(struct WebSocket \*client, WebSocket\_OpenResult openResult)

**Description**

Callback invoked when the WebSocket client receives an **Open** message.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct WebSocket](../../structs/websocket/document.md) \*client | WebSocket client. |
| [WebSocket\_OpenResult](../../structs/websocket-openresult/document.md) openResult | Content of the **Open** message sent from the WebSocket server to client. |

#### \[h2\]WebSocket\_OnMessageCallback()

typedef void (\*WebSocket\_OnMessageCallback)(struct WebSocket \*client, char \*data, uint32\_t length)

**Description**

Callback invoked when the WebSocket client receives a **Message** message.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct WebSocket](../../structs/websocket/document.md) \*client | WebSocket client. |
| char \*data | Data received by the WebSocket client. |
| uint32\_t length | Length of the data received by the WebSocket client. |

#### \[h2\]WebSocket\_OnErrorCallback()

typedef void (\*WebSocket\_OnErrorCallback)(struct WebSocket \*client, WebSocket\_ErrorResult errorResult)

**Description**

Callback invoked when the WebSocket client receives an **Error** message.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct WebSocket](../../structs/websocket/document.md) \*client | WebSocket client. |
| [WebSocket\_ErrorResult](../../structs/websocket-errorresult/document.md) errorResult | Content of the **Error** message sent from the WebSocket server to client. |

#### \[h2\]WebSocket\_OnCloseCallback()

typedef void (\*WebSocket\_OnCloseCallback)(struct WebSocket \*client, WebSocket\_CloseResult closeResult)

**Description**

Callback invoked when the WebSocket client receives a **Close** message.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct WebSocket](../../structs/websocket/document.md) \*client | WebSocket client. |
| [WebSocket\_CloseResult](../../structs/websocket-closeresult/document.md) closeResult | Content of the **Close** message sent from the WebSocket server to client. |
