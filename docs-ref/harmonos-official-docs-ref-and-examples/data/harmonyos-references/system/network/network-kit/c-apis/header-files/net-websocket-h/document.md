# net\_websocket.h

#### Overview

Defines the WebSocket client module APIs.

**File to include**: <network/netstack/net\_websocket.h>

**Library**: libnet\_websocket.so

**System capability**: SystemCapability.Communication.NetStack

**Since**: 11

**Related module**: [netstack](../../modules/netstack/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [struct WebSocket \*OH\_WebSocketClient\_Constructor(WebSocket\_OnOpenCallback onOpen, WebSocket\_OnMessageCallback onMessage,WebSocket\_OnErrorCallback onError, WebSocket\_OnCloseCallback onclose)](#oh_websocketclient_constructor) | Constructor used to create a WebSocket client. |
| [int OH\_WebSocketClient\_AddHeader(struct WebSocket \*client, struct WebSocket\_Header header)](#oh_websocketclient_addheader) | Adds the header information to the client request. |
| [int OH\_WebSocketClient\_Connect(struct WebSocket \*client, const char \*url, struct WebSocket\_RequestOptions options)](#oh_websocketclient_connect) | Connects the WebSocket client to the server. |
| [int OH\_WebSocketClient\_Send(struct WebSocket \*client, char \*data, size\_t length)](#oh_websocketclient_send) | Sends data from the WebSocket client to the server. |
| [int OH\_WebSocketClient\_Close(struct WebSocket \*client, struct WebSocket\_CloseOption options)](#oh_websocketclient_close) | Closes the connection on the WebSocket client. |
| [int OH\_WebSocketClient\_Destroy(struct WebSocket \*client)](#oh_websocketclient_destroy) | Destroys the WebSocket client and releases the context and resources of the WebSocket connection. |

#### Function Description

#### \[h2\]OH\_WebSocketClient\_Constructor()

struct WebSocket \*OH\_WebSocketClient\_Constructor(WebSocket\_OnOpenCallback onOpen, WebSocket\_OnMessageCallback onMessage,WebSocket\_OnErrorCallback onError, WebSocket\_OnCloseCallback onclose)

**Description**

Constructor used to create a WebSocket client.

**System capability**: SystemCapability.Communication.NetStack

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [WebSocket\_OnOpenCallback](../net-websocket-type-h/document.md#websocket_onopencallback) onOpen | Callback invoked when the WebSocket client receives an **open** message. |
| [WebSocket\_OnMessageCallback](../net-websocket-type-h/document.md#websocket_onmessagecallback) onMessage | Callback invoked when the WebSocket client receives a **Message** message. |
| [WebSocket\_OnErrorCallback](../net-websocket-type-h/document.md#websocket_onerrorcallback) onError | Callback invoked when the WebSocket client receives an **error** message. |
| [WebSocket\_OnCloseCallback](../net-websocket-type-h/document.md#websocket_onclosecallback) onclose | Callback invoked when the WebSocket client receives a **close** message. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct WebSocket](../../structs/websocket/document.md) \* | Pointer to the WebSocket client if the operation is successful; **NULL** otherwise. |

#### \[h2\]OH\_WebSocketClient\_AddHeader()

int OH\_WebSocketClient\_AddHeader(struct WebSocket \*client, struct WebSocket\_Header header)

**Description**

Adds the header information to the client request.

**System capability**: SystemCapability.Communication.NetStack

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct WebSocket](../../structs/websocket/document.md) \*client | Pointer to the WebSocket client. |
| [struct WebSocket\_Header](../../structs/websocket-header/document.md) header | Header information. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | **0** if the operation is successful; a non-0 value otherwise. For details about the return values, see **OH\_Websocket\_ErrCode**. |

#### \[h2\]OH\_WebSocketClient\_Connect()

int OH\_WebSocketClient\_Connect(struct WebSocket \*client, const char \*url, struct WebSocket\_RequestOptions options)

**Description**

Connects the WebSocket client to the server.

**System capability**: SystemCapability.Communication.NetStack

**Required permission**: ohos.permission.INTERNET

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct WebSocket](../../structs/websocket/document.md) \*client | Pointer to the WebSocket client. |
| const char \*url | IP address for the WebSocket client to connect to the server. |
| [struct WebSocket\_RequestOptions](../../structs/websocket-requestoptions/document.md) options | Optional parameters for connection establishment. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | **0** if the operation is successful; a non-0 value otherwise. For details about the return values, see **OH\_Websocket\_ErrCode**. |

#### \[h2\]OH\_WebSocketClient\_Send()

int OH\_WebSocketClient\_Send(struct WebSocket \*client, char \*data, size\_t length)

**Description**

Sends data from the WebSocket client to the server.

**System capability**: SystemCapability.Communication.NetStack

**Required permission**: ohos.permission.INTERNET

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct WebSocket](../../structs/websocket/document.md) \*client | WebSocket client. |
| char \*data | Data sent by the WebSocket client. |
| size\_t length | Length of the data sent by the WebSocket client. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | **0** if the operation is successful; a non-0 value otherwise. For details about the return values, see **OH\_Websocket\_ErrCode**. |

#### \[h2\]OH\_WebSocketClient\_Close()

int OH\_WebSocketClient\_Close(struct WebSocket \*client, struct WebSocket\_CloseOption options)

**Description**

Closes the connection on the WebSocket client.

**System capability**: SystemCapability.Communication.NetStack

**Required permission**: ohos.permission.INTERNET

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct WebSocket](../../structs/websocket/document.md) \*client | WebSocket client. |
| [struct WebSocket\_CloseOption](../../structs/websocket-closeoption/document.md) options | Optional parameters for connection closure. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | **0** if the operation is successful; a non-0 value otherwise. For details about the return values, see **OH\_Websocket\_ErrCode**. |

#### \[h2\]OH\_WebSocketClient\_Destroy()

int OH\_WebSocketClient\_Destroy(struct WebSocket \*client)

**Description**

Destroys the WebSocket client and releases the context and resources of the WebSocket connection. Usage:

1.  Call [WebSocket\_OnCloseCallback](../net-websocket-type-h/document.md#websocket_onclosecallback) to subscribe to the WebSocket connection close event, and call the [OH\_WebSocketClient\_Destroy](#oh_websocketclient_destroy) method in the callback function.
    
2.  Call [OH\_WebSocketClient\_Close](#oh_websocketclient_close) to close the WebSocket connection.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/HAz-aTMaQyajx_XTGEDptg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062347Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=465B7C2E25457A163161C5D4404B4DF36B19B0A260751E08DBA5309A86AF9E87)

\>

\>Ensure that this API is called after the [WebSocket\_OnCloseCallback](../net-websocket-type-h/document.md#websocket_onclosecallback) callback is triggered. Otherwise, socket leaks may occur and the connection may not be closed after the system memory resources are released.

**System capability**: SystemCapability.Communication.NetStack

**Required permission**: ohos.permission.INTERNET

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct WebSocket](../../structs/websocket/document.md) \*client | WebSocket client. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | **0** if the operation is successful; a non-0 value otherwise. For details about the return values, see **OH\_Websocket\_ErrCode**. |
