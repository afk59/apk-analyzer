# @ohos.net.webSocket (WebSocket Connection)

The **webSocket** module implements bidirectional connections between the WebSocket client and WebSocket server for third-party applications. Currently, the WebSocket server is available only for smart TVs.

On the WebSocket client: You can use WebSocket to establish a bidirectional connection between the server and client. Before doing this, you need to use the [createWebSocket](#websocketcreatewebsocket) API to create a [WebSocket](#websocket) object and then use the [connect](#connect) API to connect to the server. If the connection is successful, the client will receive a callback of the [open](#onopen) event. Then, the client can communicate with the server using the [send](#send) API. When the server sends a message to the client, the client will receive a callback of the [message](#onmessage) event. If the connection is no longer needed, the client can call the [close](#close) API to close the connection. After successful disconnection, the client will receive a callback of the [close](#onclose) event. If an error occurs in any of the preceding processes, the client will receive a callback of the [error](#onerror) event.

On the WebSocket server: You can use WebSocket to establish a bidirectional connection between the server and client. Before doing this, you need to use the [createWebSocketServer](#websocketcreatewebsocketserver19) API to create a [WebSocketServer](#websocketserver19) object and then use the [start](#start19) API to start the server to listen for connection requests from the client. If the connection is successful, the server receives the callback of the [connect](#onconnect19) event. The server can then communicate with the client by using the [send](#send19) API or obtain information about all connected clients by using the [listAllConnections](#listallconnections19) API. When the client sends a message to the server, the server receives the callback of the [messageReceive](#onmessagereceive19) event. If the connection is no longer needed, the server can call the [close](#close19) API to close the connection. After successful disconnection, the server will receive a callback of the [close](#onclose19) event. To stop the service, the server can use the [stop](#stop19) API. If an error occurs in any of the preceding processes, the server will receive a callback of the [error](#onerror19) event.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/5zfkRCgGSFyccp1csOfOqw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A39CA7CFAA5668EDFA90C06AA60351F1B68A98BE550411D0CA98D3E10580EA24)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { webSocket } from '@kit.NetworkKit';

#### webSocket.createWebSocket

createWebSocket(): WebSocket

Creates a **WebSocket** object, which provides methods to create or close a WebSocket connection, send data over the connection, and enable or disable listening for the **open**, **close**, **message**, and **error** events.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| [WebSocket](#websocket) | A **WebSocket** object, which contains the **connect**, **send**, **close**, **on**, or **off** method. |

**Example**

let ws: webSocket.WebSocket = webSocket.createWebSocket();

#### WebSocket

Defines a **WebSocket** object. Before invoking WebSocket APIs, you need to call [webSocket.createWebSocket](#websocketcreatewebsocket) to create a **WebSocket** object.

#### \[h2\]connect

connect(url: string, callback: AsyncCallback<boolean>): void

Initiates a WebSocket request to establish a WebSocket connection to a given URL. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/VQxBbg4NRACkT_RSnqKvxA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7FB4CF75AEE65CA3F04E732F4096D62B92A426455506CA6D3BFE5ABD3F7053E)

The boolean value returned in the callback indicates only whether the connection request is created successfully. To detect whether the WebSocket connection is successful, you need to subscribe to the **open** event via [on('open')](#onopen) before calling this API.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/ME1xHiJ8QvOt5nNfQ2tJ_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F166DB1BAAAF50BF480D6FE90D4AE1591AB3AD7EDC17E5AD7E160355A3634BD)

The URL cannot contain more than 1024 characters. Otherwise, the connection fails. Since API version 15, the maximum length of URLs is changed from 1024 characters to 2048 characters.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL for establishing a WebSocket connection. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [webSocket Error Codes](../../error-codes/websocket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2302001 | Websocket url error. |
| 2302002 | Websocket certificate file does not exist. |
| 2302003 | Websocket connection already exists. |
| 2302998 | It is not allowed to access this domain. |
| 2302999 | Internal error. |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
let url = "ws://";
ws.connect(url, (err: BusinessError, value: boolean) => {
  if (!err) {
    console.info("connect success")
  } else {
    console.error(\`connect fail. Code: ${err.code}, message: ${err.message}\`)
  }
});

#### \[h2\]connect

connect(url: string, options: WebSocketRequestOptions, callback: AsyncCallback<boolean>): void

Initiates a WebSocket request to establish a WebSocket connection to a given URL. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/kl9cZ2mcRxuiZJGY9L19Bg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C498FCD70B9C245B2DA723CF39606F6921DE410CF38AD36A0D915E2BF5345A78)

The boolean value returned in the callback indicates only whether the connection request is created successfully. To detect whether the WebSocket connection is successful, you need to subscribe to the **open** event via [on('open')](#onopen) before calling this API.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/gPx3rg-iRQerYW-QRPyFyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F82D85C90CA318D03642BEEF1ED529E22B565A6AEAB2B988CEB38E170F32AC12)

The URL cannot contain more than 1024 characters. Otherwise, the connection fails. Since API version 15, the maximum length of URLs is changed from 1024 characters to 2048 characters.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL for establishing a WebSocket connection. |
| options | WebSocketRequestOptions | Yes | Request options. For details, see [WebSocketRequestOptions](#websocketrequestoptions). |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [webSocket Error Codes](../../error-codes/websocket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2302001 | Websocket url error. |
| 2302002 | Websocket certificate file does not exist. |
| 2302003 | Websocket connection already exists. |
| 2302998 | It is not allowed to access this domain. |
| 2302999 | Internal error. |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
let options: webSocket.WebSocketRequestOptions | undefined;
if (options !=undefined) {
  options.header = {
     name1: "value1",
     name2: "value2",
     name3: "value3"
  };
  options.caPath = "";
}
let url = "ws://"
ws.connect(url, options, (err: BusinessError, value: Object) => {
  if (!err) {
    console.info("connect success")
  } else {
    console.error(\`connect fail. Code: ${err.code}, message: ${err.message}\`)
  }
});

#### \[h2\]connect

connect(url: string, options?: WebSocketRequestOptions): Promise<boolean>

Establishes a WebSocket connection to a given URL. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/F30eeI2fTDCZC9cpk8yUdA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11EE42AE5031A83BECA9E28E70E9FF9B4423668E784EEA7B386C54DCE5C8D623)

The boolean value returned in the callback indicates only whether the connection request is created successfully. To detect whether the WebSocket connection is successful, you need to subscribe to the **open** event via [on('open')](#onopen) before calling this API.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/tMggdkuWRCS1v9wClzXBHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4EE8356149BC4E846809F7333558417E0BC587C1065351BBEC0F6E8C8067A2E7)

The URL cannot contain more than 1024 characters. Otherwise, the connection fails. Since API version 15, the maximum length of URLs is changed from 1024 characters to 2048 characters.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL for establishing a WebSocket connection. |
| options | WebSocketRequestOptions | No | Request options. For details, see [WebSocketRequestOptions](#websocketrequestoptions). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Callback used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [webSocket Error Codes](../../error-codes/websocket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2302001 | Websocket url error. |
| 2302002 | Websocket certificate file does not exist. |
| 2302003 | Websocket connection already exists. |
| 2302998 | It is not allowed to access this domain. |
| 2302999 | Internal error. |

**Example**

import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
let url = "ws://"
let promise = ws.connect(url);
promise.then((value: boolean) => {
  console.info("connect success")
}).catch((err:string) => {
  console.error("connect fail, error:" + JSON.stringify(err))
});

#### \[h2\]send

send(data: string | ArrayBuffer, callback: AsyncCallback<boolean>): void

Sends data through a WebSocket connection. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | string | ArrayBuffer | Yes | 
Data to send.

Only the string type is supported for API version 6 or earlier. Both the string and ArrayBuffer types are supported for API version 8 or later. A maximum of 5,242,864 bytes (that is, 5 x 1024 x 1024 - 16) can be sent. If the data size exceeds the upper limit, error code 401 will be returned.

 |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
let url = "ws://"
class OutValue {
  status: number = 0
  message: string = ""
}
ws.connect(url, (err: BusinessError, value: boolean) => {
    if (!err) {
      console.info("connect success")
    } else {
      console.error(\`connect fail. Code: ${err.code}, message: ${err.message}\`)
    }
});
ws.on('open', (err: BusinessError, value: Object) => {
  console.info("on open, status:" + (value as OutValue).status + ", message:" + (value as OutValue).message)
    ws.send("Hello, server!", (err: BusinessError, value: boolean) => {
    if (!err) {
      console.info("send success")
    } else {
      console.error(\`send fail. Code: ${err.code}, message: ${err.message}\`)
    }
  });
});

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/5JWbeO1-SwykT2P9w-QnyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7809C84B6BDC46325112A05A68A9CF598AE699AA264CDC6C1E76F43F924EDCCF)

The **send** API can be called only after an **open** event is listened.

#### \[h2\]send

send(data: string | ArrayBuffer): Promise<boolean>

Sends data through the WebSocket connection. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | string | ArrayBuffer | Yes | 
Data to send.

Only the string type is supported for API version 6 or earlier. Both the string and ArrayBuffer types are supported for API version 8 or later. A maximum of 5,242,864 bytes (that is, 5 x 1024 x 1024 - 16) can be sent. If the data size exceeds the upper limit, error code 401 will be returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
let url = "ws://"
class OutValue {
  status: number = 0
  message: string = ""
}
ws.connect(url, (err: BusinessError, value: boolean) => {
    if (!err) {
      console.info("connect success")
    } else {
      console.error("connect fail. Code: ${err.code}, message: ${err.message}")
    }
});

ws.on('open', (err: BusinessError, value: Object) => {
  console.info("on open, status:" + (value as OutValue).status + ", message:" + (value as OutValue).message)
  let promise = ws.send("Hello, server!");
  promise.then((value: boolean) => {
    console.info("send success")
  }).catch((err:string) => {
    console.error("send fail, error:" + JSON.stringify(err))
  });
});

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/aFKTjqUjQS2uvndehMj2bQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0AF85E134167D68FCC7949DC4467D53FEB50D039762BE975150073333106C4F2)

The **send** API can be called only after an **open** event is listened.

#### \[h2\]close

close(callback: AsyncCallback<boolean>): void

Closes the WebSocket connection. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
ws.close((err: BusinessError) => {
  if (!err) {
    console.info("close success")
  } else {
    console.error(\`close fail. Code: ${err.code}, message: ${err.message}\`)
  }
});

#### \[h2\]close

close(options: WebSocketCloseOptions, callback: AsyncCallback<boolean>): void

Closes the WebSocket connection based on the options parameter. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | WebSocketCloseOptions | Yes | Request options. For details, see [WebSocketCloseOptions](#websocketcloseoptions). |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();

let options: webSocket.WebSocketCloseOptions | undefined;
if (options != undefined) {
    options.code = 1000
    options.reason = "your reason"
}
ws.close(options, (err: BusinessError) => {
    if (!err) {
        console.info("close success")
    } else {
        console.error(\`close fail. Code: ${err.code}, message: ${err.message}\`)
    }
});

#### \[h2\]close

close(options?: WebSocketCloseOptions): Promise<boolean>

Closes a WebSocket connection based on the specified options. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | WebSocketCloseOptions | No | Request options. For details, see [WebSocketCloseOptions](#websocketcloseoptions). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**Example**

import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
let options: webSocket.WebSocketCloseOptions | undefined;
if (options != undefined) {
    options.code = 1000
    options.reason = "your reason"
}
let promise = ws.close();
promise.then((value: boolean) => {
    console.info("close success")
}).catch((err:string) => {
    console.error("close fail, error:" + JSON.stringify(err))
});

#### \[h2\]on('open')

on(type: 'open', callback: AsyncCallback<Object>): void

Subscribes to WebSocket open events. This API uses an asynchronous callback to return the result. This event indicates whether the WebSocket connection is successful. This API must be called before [connect](#connect) is called to initiate a connection request.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**open**: event indicating that a WebSocket connection has been opened.

 |
| callback | AsyncCallback<Object> | Yes | Callback used to return the result. |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let ws= webSocket.createWebSocket();
class OutValue {
  status: number = 0
  message: string = ""
}
ws.on('open', (err: BusinessError, value: Object) => {
  console.info("on open, status:" + (value as OutValue).status + ", message:" + (value as OutValue).message)
});

#### \[h2\]off('open')

off(type: 'open', callback?: AsyncCallback<Object>): void

Unsubscribes from WebSocket open events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/nFNdGPNWS-CXbnXePDJ-2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF33D8D9CB30F48FF71FD2F2F12C8DFB1EB7585B74EB0EAC8B243DCE54010BE5)

You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If you do not pass the callback, you will cancel listening for all events.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**open**: event indicating that a WebSocket connection has been opened.

 |
| callback | AsyncCallback<Object> | No | Callback used to return the result. |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
class OutValue {
  status: number = 0
  message: string = ""
}
let callback1 = (err: BusinessError, value: Object) => {
 console.info("on open, status:" + ((value as OutValue).status + ", message:" + (value as OutValue).message))
}
ws.on('open', callback1);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
ws.off('open', callback1);

#### \[h2\]on('message')

on(type: 'message', callback: AsyncCallback<string | ArrayBuffer>): void

Subscribes to WebSocket server message receiving events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/Ys_j_hjKR1-a8GphpjTaHg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D3D65B856B4D661204AC73EAA6EBE00BAC355D3E4A802C2DB21C25983956F42E)

The data in **AsyncCallback** can be in the format of string (API version 6) or ArrayBuffer (API version 8).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**message**: event indicating that a message has been received from the server.

 |
| callback | AsyncCallback<string | ArrayBuffer 8+\> | Yes | Callback used to return the result. |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
ws.on('message', (err: BusinessError<void>, value: string | ArrayBuffer) => {
  console.info("on message, message:" + value)
});

#### \[h2\]off('message')

off(type: 'message', callback?: AsyncCallback<string | ArrayBuffer>): void

Unsubscribes from WebSocket server message receiving events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/W6fEpbQhSHWtL6bxYc_FGA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A6CF29B90217727C5BF88380FAF03F28EE0EFBDC09C19726A87DDABB120951F5)

The data in **AsyncCallback** can be in the format of string (API version 6) or ArrayBuffer (API version 8).

You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If you do not pass the callback, you will cancel listening for all events.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**message**: event indicating that a message has been received from the server.

 |
| callback | AsyncCallback<string |ArrayBuffer 8+\> | No | Callback used to return the result. |

**Example**

import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('message');

#### \[h2\]on('close')

on(type: 'close', callback: AsyncCallback<CloseResult>): void

Subscribes to WebSocket close events. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**close**: event indicating that a WebSocket connection has been closed.

 |
| callback | AsyncCallback<CloseResult> | Yes | 

Callback used to return the result.

**close** and **reason** indicate the error code and error cause for closing the connection, respectively.

 |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
ws.on('close', (err: BusinessError, value: webSocket.CloseResult) => {
  console.info("on close, code is " + value.code + ", reason is " + value.reason)
});

#### \[h2\]off('close')

off(type: 'close', callback?: AsyncCallback<CloseResult>): void

Unsubscribes from WebSocket close events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/gaQHLgIxQg259LFGkQS9HA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1E11974B45E1875135A5DF0AE6B691F6FBEF6FC4B29EB0E658D9F7E7325C75F)

You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If you do not pass the callback, you will cancel listening for all events.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**close**: event indicating that a WebSocket connection has been closed.

 |
| callback | AsyncCallback<CloseResult> | No | 

Callback used to return the result.

**close** and **reason** indicate the error code and error cause for closing the connection, respectively.

 |

**Example**

import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('close');

#### \[h2\]on('error')

on(type: 'error', callback: ErrorCallback): void

Subscribes to WebSocket error events. This API uses an asynchronous callback to return the result.

The error code of the [error](#onerror) event callback is described as follows: WebSocket is essentially an HTTP protocol upgrade. If the server agrees to the upgrade, the server returns 101. The status code indicates that the protocol is switched from HTTP to WebSocket (the **open** callback is triggered). If the server rejects the upgrade or other exceptions occur, the server returns 200, indicating that the server only processes the request as a common HTTP request.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: event indicating the WebSocket connection has encountered an error.

 |
| callback | ErrorCallback | Yes | Callback used to return the result. |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
ws.on('error', (err: BusinessError) => {
  console.error(\`on error. Code: ${err.code}, message: ${err.message}\`)
});

#### \[h2\]off('error')

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from WebSocket error events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/b7Naua-XROa1fX1nb9lxBQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11D42FBA2DAF7A04A2FB5D7BC1416E6C35D03E21ADC25C4709E5F161ACB1B6E0)

You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If you do not pass the callback, you will cancel listening for all events.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: event indicating the WebSocket connection has encountered an error.

 |
| callback | ErrorCallback | No | Callback used to return the result. |

**Example**

import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('error');

#### \[h2\]on('dataEnd')11+

on(type: 'dataEnd', callback: Callback<void>): void

Subscribes to the WebSocket data receiving end event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**dataEnd**: event indicating the data receiving over the WebSocket connection has ended.

 |
| callback | Callback<void> | Yes | Callback used to return the result. |

**Example**

import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.on('dataEnd', () => {
  console.info("on dataEnd")
});

#### \[h2\]off('dataEnd')11+

off(type: 'dataEnd', callback?: Callback<void>): void

Unsubscribes from WebSocket data receiving end events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/22A9bvceQyWzoAb092rXMg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F7C401AB7ACB52686C6F096A8213A8421B766DA09CC8816CC601DAF19242F98)

You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If you do not pass the callback, you will cancel listening for all events.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**dataEnd**: event indicating the data receiving over the WebSocket connection has ended.

 |
| callback | Callback<void> | No | Callback used to return the result. |

**Example**

import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('dataEnd');

#### \[h2\]on('headerReceive')12+

on(type: 'headerReceive', callback: Callback<ResponseHeaders>): void

Subscribes to HTTP response header events. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

Event type. The value is **headerReceive**.

 |
| callback | Callback<ResponseHeaders> | Yes | Callback used to return the result. |

**Example**

import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.on('headerReceive', (data) => {
  console.info("on headerReceive " + JSON.stringify(data))
});

#### \[h2\]off('headerReceive')12+

off(type: 'headerReceive', callback?: Callback<ResponseHeaders>): void

Unsubscribes from HTTP response header events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/5gKfC-mFSyu4-SU_HYYk8g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A6B35F0038C4778C0D2DAFABAA8AF68490E5AEBF9084307692179142BC86BD7)

You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If you do not pass the callback, you will cancel listening for all events.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

Event type. The value is **headerReceive**.

 |
| callback | Callback<ResponseHeaders> | No | Callback used to return the result. |

**Example**

import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('headerReceive');

#### webSocket.createWebSocketServer19+

createWebSocketServer(): WebSocketServer

Creates a **WebSocketServer** object, which provides methods to start or stop the WebSocketServer service, send data over the connection, close the connection, list all connections, and enable or disable listening for the **open**, **close**, **message**, and **error** events.

**System capability**: SystemCapability.Communication.NetStack

**Device behavior differences**: This API can be properly called on smart TVs. If it is called on other device types, **nullptr** is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| [WebSocketServer](#websocketserver19) | **WebSocketServer** object, which provides the **start**, **listAllConnections**, **send**, **close**, **stop**, **on**, and **off** methods. |

**Example**

let ws: webSocket.WebSocketServer = webSocket.createWebSocketServer();

#### WebSocketServer19+

Defines a **WebSocketServer** object. You need to use [webSocket.createWebSocketServer](#websocketcreatewebsocketserver19) to create a **WebSocketServer** object before using its methods.

#### \[h2\]start19+

start(config: WebSocketServerConfig): Promise<boolean>

Starts the WebSocketServer service based on the specified **config**. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/5mhr7LAPQZizMsw8a8yB1A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=690872B5FF64EA891B7C1B714BBF064A315382F87CBA010D6A917575D7CB5DF9)

You are advised not to listen for the same port when calling this API multiple times.

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [WebSocketServerConfig](#websocketserverconfig19) | Yes | Starts the WebSocket server. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [WebSocket Error Codes](../../error-codes/websocket-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2302002 | Websocket certificate file does not exist. |
| 2302004 | Can't listen on the given NIC. |
| 2302005 | Can't listen on the given Port. |
| 2302999 | Websocket other unknown error. |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // Listening port
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(\`Failed to start. Code: ${error.code}, message: ${error.message}\`);
});

#### \[h2\]send19+

send(data: string | ArrayBuffer, connection: WebSocketConnection): Promise<boolean>

Sends data through the WebSocket connection. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/07eTBa3HSLCGVwN_So7f1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6101438CBA196C604DE4642725D130CBDFC8683526E93A78CE0AE1B476BE19E3)

The **send** API can be called only after a **connect** event is listened.

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | string | ArrayBuffer | Yes | Data to send, which can be of the string or ArrayBuffer type. A maximum of 5,242,864 bytes (that is, 5 x 1024 x 1024 - 16) can be sent. If the data size exceeds the upper limit, error code 401 will be returned. |
| connection | [WebSocketConnection](#websocketconnection19) | Yes | Client information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [WebSocket Error Codes](../../error-codes/websocket-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2302006 | websocket connection does not exist. |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // Listening port
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(\`Failed to start. Code: ${error.code}, message: ${error.message}\`);
});

localServer.on('connect', async (connection: webSocket.WebSocketConnection) => {
  console.info(\`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}\`);
  // Use send() to send data to the client when the on('connect') event is received.
  localServer.send("Hello, I'm server!", connection).then((success: boolean) => {
    if (success) {
      console.info('message send successfully');
    } else {
      console.error('message send failed');
    }
  }).catch((error: BusinessError) => {
    console.error(\`message send failed, Code: ${error.code}, message: ${error.message}\`);
  });
});

#### \[h2\]listAllConnections19+

listAllConnections(): WebSocketConnection\[\]

Obtains information about all clients connected to the server.

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/VUI-7b1ISY-5hC9iCk792Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2FA6D608293CA59CD5591F39533A05F5CB76A26EA0ACB2A0B8FB95E993BB6DC4)

This API is called asynchronously. The **await** keyword needs to be used to wait until the asynchronous operation is complete, ensuring that information about all clients connected to the server can be correctly obtained.

**Return value**

| Type | Description |
| :-- | :-- |
| [WebSocketConnection\[\]](#websocketconnection19) | Information about all clients connected to the server, which is of the string array type. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let connections: webSocket.WebSocketConnection\[\] = \[\];
let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // Listening port
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(\`Failed to start. Code: ${error.code}, message: ${error.message}\`);
});

localServer.on('connect', async (connection: webSocket.WebSocketConnection) => {
  console.info(\`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}\`);
  try {
    connections = await localServer.listAllConnections();
    if (connections.length === 0) {
      console.info('client list is empty');
    } else {
      console.info(\`client list cnt: ${connections.length}, client connections list is: ${connections}\`);
    }
  } catch (error) {
    console.error(\`Failed to listAllConnections. Code: ${error.code}, message: ${error.message}\`);
  }
});

#### \[h2\]close19+

close(connection: WebSocketConnection, options?: webSocket.WebSocketCloseOptions): Promise<boolean>

Closes a WebSocket connection. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| connection | [WebSocketConnection](#websocketconnection19) | Yes | Client information, including the IP address and port number. |
| options | [webSocket.WebSocketCloseOptions](#websocketcloseoptions) | No | 
Optional parameters carried in the request for closing a WebSocket connection.

By default, the error code is 200, and the cause is **Websocket connect failed**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [WebSocket Error Codes](../../error-codes/websocket-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2302006 | websocket connection does not exist. |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // Listening port
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(\`Failed to start. Code: ${error.code}, message: ${error.message}\`);
});

localServer.on('connect', (connection: webSocket.WebSocketConnection) => {
  console.info(\`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}\`);
  localServer.close(connection).then((success: boolean) => {
    if (success) {
      console.info('close client successfully');
    } else {
      console.error('close client failed');
    }
  });
});

#### \[h2\]stop19+

stop(): Promise<boolean>

Stops the WebSocketServer service. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // Listening port
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(\`Failed to start. Code: ${error.code}, message: ${error.message}\`);
});

localServer.stop().then((success: boolean) => {
  if (success) {
    console.info('server stop service successfully');
  } else {
    console.error('server stop service failed');
  }
});

#### \[h2\]on('connect')19+

on(type: 'connect', callback: Callback<WebSocketConnection>): void

Subscribes to the WebSocketServer connection event (the connection between the client and server is successfully established). This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **connect**. Successful calling of **onconnect()** indicates that a connection is established between the client and server. |
| callback | Callback<[WebSocketConnection](#websocketconnection19)\> | Yes | Callback used to return the information about connected clients. |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.on('connect', (connection: webSocket.WebSocketConnection) => {
  console.info(\`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}\`);
});

#### \[h2\]off('connect')19+

off(type: 'connect', callback?: Callback<WebSocketConnection>): void

Unsubscribes from WebSocketServer connection events (the connection between the client and server is successfully established). This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/rbhDHr9tT4WCzoE7CDsYng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A25013F751A3F458CA54FC0DC96705A0CAE99E03ACF1CA2A5F05E2A3086B99D)

You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If you do not pass the callback, you will cancel listening for all events.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **connect**. Successful calling of **offconnect()** indicates that listening for connection events is canceled successful. |
| callback | Callback<[WebSocketConnection](#websocketconnection19)\> | No | Callback used to return the information about connected clients. |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('connect');

#### \[h2\]on('messageReceive')19+

on(type: 'messageReceive', callback: Callback<WebSocketMessage>): void

Subscribes to the WebSocketServer event of receiving client messages. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **messageReceive**. Successful calling of **onmessageReceive()** indicates that a message is received from the client. |
| callback | Callback<[WebSocketMessage](#websocketmessage19)\> | Yes | 
Callback used to return the result.

**clientconnection** indicates the client information and **data** indicates the data message sent by the client.

 |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.on('messageReceive', (message: webSocket.WebSocketMessage) => {
  console.info(\`on message received, client: ${message.clientConnection}, data: ${message.data}\`);
});

#### \[h2\]off('messageReceive')19+

off(type: 'messageReceive', callback?: Callback<WebSocketMessage>): void

Unsubscribes from the WebSocketServer event of receiving client messages. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/lP4J2Oj_Qba8P5TVhVJC6w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1CD0D271024D7651FD8F04940398EAA1BEB3BEA1F85E6AC8949BEB520ACAC866)

You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If you do not pass the callback, you will cancel listening for all events.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **messageReceive**. Successful calling of **offmessageReceive()** indicates that listening for **messageReceive** events is canceled successfully. |
| callback | Callback<[WebSocketMessage](#websocketmessage19)\> | No | 
Callback used to return the result, which contains:

\- **clientconnection**: client information.

\- **data**: data sent by the client.

 |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('messageReceive');

#### \[h2\]on('close')19+

on(type: 'close', callback: ClientConnectionCloseCallback): void

Subscribes to WebSocketServer close events. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **close**. Successful calling of **onclose()** indicates that the connection is closed successfully. |
| callback | [ClientConnectionCloseCallback](#clientconnectionclosecallback19) | Yes | 
Callback used to return the result.

**close** and **reason** indicate the error code and error cause for closing the connection, respectively.

 |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.on('close', (clientConnection: webSocket.WebSocketConnection, closeReason: webSocket.CloseResult) => {
  console.info(\`client close, client: ${clientConnection}, closeReason: Code: ${closeReason.code}, reason: ${closeReason.reason}\`);
});

#### \[h2\]off('close')19+

off(type: 'close', callback?: ClientConnectionCloseCallback): void

Unsubscribes from WebSocketServer close events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/xyqdcz53SRqevC6BAhCUWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B368AAE782094BD870CCC3D9047B37EBBC3E759EB0859046A8FB2DB5B913CCF9)

You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If you do not pass the callback, you will cancel listening for all events.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **close**. Successful calling of **offclose()** indicates that listening for the **close** events is canceled successfully. |
| callback | [ClientConnectionCloseCallback](#clientconnectionclosecallback19) | No | 
Callback used to return the result.

**close** and **reason** indicate the error code and error cause for closing the connection, respectively.

 |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('close');

#### \[h2\]on('error')19+

on(type: 'error', callback: ErrorCallback): void

Subscribes to WebSocketServer error events. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **error**. Successful calling of **onerror()** indicates that an error has occurred. |
| callback | [ErrorCallback](../../../../basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | Yes | Callback used to return the result. |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wsServer: webSocket.WebSocketServer = webSocket.createWebSocketServer();
wsServer.on('error', (err: BusinessError) => {
  console.error(\`error. Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]off('error')19+

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from WebSocketServer error events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/usxT07M-Sha7W4EGtgotsw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F18127CBCA19D53CCE3C8347EB5F885A04BD49226D18EE368ECF929230BC8878)

You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If you do not pass the callback, you will cancel listening for all events.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **error**. Successful calling of **offerror()** indicates that listening for the **error** events is canceled successfully. |
| callback | [ErrorCallback](../../../../basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | No | Callback used to return the error code (default value: **200**). |

**Example**

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('error');

#### WebSocketRequestOptions

Defines the optional parameters carried in the request for establishing a WebSocket connection.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| header | Object | No | Yes | 
Header carrying optional parameters in the request for establishing a WebSocket connection. You can customize the parameter or leave it unspecified.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| caPath11+ | string | No | Yes | Path of CA certificates. If a path is set, the system uses the CA certificates in this path. If a path is not set, the system uses the preset CA certificate, namely, **/etc/ssl/certs/cacert.pem**. This path is the sandbox mapping path, which can be obtained by using **UIAbilityContext** APIs. Currently, only text certificates in PEM format are supported. |
| clientCert11+ | [ClientCert](#clientcert11) | No | Yes | Client certificate. |
| proxy12+ | [ProxyConfiguration](#proxyconfiguration12) | No | Yes | Proxy configuration. By default, the system network proxy is used. |
| protocol12+ | string | No | Yes | Custom **Sec-WebSocket-Protocol** field. The default value is "". |
| skipServerCertVerification20+ | boolean | No | Yes | Whether to skip server certificate verification. The value **true** means to skip server certificate verification, and the value **false** means the opposite. Default value: **false**. |
| pingInterval21+ | number | No | Yes | Custom [heartbeat detection interval](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/websocket-connection). The default value is 30s. Heartbeat detection is initiated at the specified interval. If the value is set to **0**, heartbeat detection is disabled. The maximum value is 30000s, and the minimum value is 0s. |
| pongTimeout21+ | number | No | Yes | Timeout interval for disconnecting a connection after heartbeat detection is initiated. The default value is 30s. If no response is received during the specified interval, the connection is disconnected. The maximum value is 30000s, and the minimum value is 0s. **pongTimeout** must be less than or equal to **pingInterval**. |

#### ClientCert11+

Defines the client certificate type.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| certPath | string | No | No | Path of the certificate file. |
| keyPath | string | No | No | Path of the certificate key file. |
| keyPassword | string | No | Yes | Password of the certificate key file. The default value is an empty string. |

#### ProxyConfiguration12+

type ProxyConfiguration = 'system' | 'no-proxy' | HttpProxy

Represents the HTTP proxy configuration.

**System capability**: SystemCapability.Communication.NetStack

| Type | Description |
| :-- | :-- |
| 'system' | The default network proxy is used. |
| 'no-proxy' | No network proxy is used. |
| [HttpProxy](../ohos-net-connection-network-connection-management/document.md#httpproxy10) | The specified network proxy is used. |

#### WebSocketCloseOptions

Defines the optional parameters carried in the request for closing a WebSocket connection.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| code | number | No | Yes | Error code. Set this parameter based on the actual situation. The value must be a positive integer ranging from 1000 to 1015. If no error code is specified or the input value is not within the preceding range, the code will be set to the default value **1000**. |
| reason | string | No | Yes | Error cause. Set this parameter based on the actual situation. If no reason value is specified, the reason value is set to the default value **CLOSE\_NORMAL**. |

#### CloseResult10+

Represents the result obtained from the **close** event reported when the WebSocket connection is closed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| code | number | No | No | Error code for closing the connection. |
| reason | string | No | No | Error cause for closing the connection. |

#### ResponseHeaders12+

type ResponseHeaders = { \[k: string\]: string | string\[\] | undefined; }

Enumerates the response headers sent by the server.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| \[k:string\] | string | string\[\] | undefined | No | Key-value pairs. The key can be any character string and the value can be any character string, character array, or **undefined**. |

#### Result Codes for Connection Closing

The error code sent to the server must be a positive integer ranging from 1000 to 1015. You can define the error code as required. If no error code is specified or the input value is not within the preceding range, the error code is set to the default value **1000**. The following list is for reference.

**System capability**: SystemCapability.Communication.NetStack

| Value | Description |
| :-- | :-- |
| 1000 | Normally closed. |
| 1001 | Connection closed by the server. |
| 1002 | Incorrect protocol. |
| 1003 | Data unable to be processed. |
| 1004~1015 | Reserved. |

#### HttpProxy12+

type HttpProxy = connection.HttpProxy

Defines the global HTTP proxy configuration of the network.

**System capability**: SystemCapability.Communication.NetManager.Core

| Type | Description |
| :-- | :-- |
| connection.HttpProxy | The specified network proxy is used. |

#### WebSocketServerConfig19+

Defines the WebSocketServer configuration.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| serverIP | string | No | Yes | IP address of the WebSocketServer. The default value is **0.0.0.0**. |
| serverPort | number | No | No | Port of the WebSocketServer. |
| serverCert | [ServerCert](#servercert19) | No | Yes | Certificate information, which includes the paths of the WebSocketServer certificate file and private key file. |
| protocol | string | No | Yes | Custom protocol. |
| maxConcurrentClientsNumber | number | No | No | Maximum number of concurrent clients. When the number of concurrent clients reaches the maximum, the server rejects new connections. The default value is **10**. |
| maxConnectionsForOneClient | number | No | No | Maximum number of connections for each client. The default value is **10**. |

#### ServerCert19+

Certificate information, which includes the paths of the WebSocketServer certificate file and private key file.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| certPath | string | No | No | Path of the server certificate file. |
| keyPath | string | No | No | Path of the private key file of the server certificate. |

#### WebSocketMessage19+

Callback used to return the result, which contains:

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| data | string |ArrayBuffer | No | No | Message data sent by the client. |
| clientConnection | [WebSocketConnection](#websocketconnection19) | No | No | Client information, including the IP address and port number. |

#### WebSocketConnection19+

Client information, including the IP address and port number.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| clientIP | string | No | No | IP address of the client. |
| clientPort | number | No | No | Port number of the client. |

#### ClientConnectionCloseCallback19+

type ClientConnectionCloseCallback = (clientConnection: WebSocketConnection, closeReason: CloseResult) => void

Callback invoked when the WebSocketServer connection is closed.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| clientConnection | [WebSocketConnection](#websocketconnection19) | Yes | Client information, including the IP address and port number. |
| closeReason | [CloseResult](#closeresult10) | Yes | Represents the result obtained from the **close** event reported when the WebSocket connection is closed. |
