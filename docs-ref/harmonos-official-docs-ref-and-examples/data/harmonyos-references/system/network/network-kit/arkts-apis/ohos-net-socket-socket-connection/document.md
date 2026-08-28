# @ohos.net.socket (Socket Connection)

The **socket** module implements data transfer over TCP, UDP, Web, and TLS socket connections.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/mk-3EJmpR5mmz0ZfQ5HF1A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8AD8E0EF34AB11B45623BC6227822B761EB24ED5851A705709BEF73F804B29B0)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

You are advised to call the APIs of this module in the worker thread or taskpool to perform network-related operations. Otherwise, the UI thread may be suspended.

#### Modules to Import

import { socket } from '@kit.NetworkKit';

#### socket.constructUDPSocketInstance

constructUDPSocketInstance(): UDPSocket

Creates a **UDPSocket** object.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| [UDPSocket](#udpsocket) | **UDPSocket** object. |

**Example**

import { socket } from '@kit.NetworkKit';
let udp: socket.UDPSocket = socket.constructUDPSocketInstance();

#### UDPSocket

Defines a UDP socket connection. Before calling UDPSocket APIs, you need to call [socket.constructUDPSocketInstance](#socketconstructudpsocketinstance) to create a **UDPSocket** object.

#### \[h2\]bind

bind(address: NetAddress, callback: AsyncCallback<void>): void

Binds the IP address and port number. The port number can be customized or randomly allocated by the system. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | Yes | Local address. For details, see [NetAddress](#netaddress). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, no value is returned. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx', // Local IP address
  port: 1234
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});

#### \[h2\]bind

bind(address: NetAddress): Promise<void>

Binds the IP address and port number. The port number can be customized or randomly allocated by the system. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | Yes | Local address. For details, see [NetAddress](#netaddress). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx', // Local IP address
  port: 8080
}
udp.bind(bindAddr).then(() => {
  console.info('bind success');
}).catch((err: BusinessError) => {
  console.error('bind fail');
});

#### \[h2\]send

send(options: UDPSendOptions, callback: AsyncCallback<void>): void

Sends data over a UDP socket connection. This API uses an asynchronous callback to return the result.

Before sending data, call [UDPSocket.bind()](#bind) to bind the IP address and port. Call the API in the worker thread or taskpool thread as this operation is time-consuming.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [UDPSendOptions](#udpsendoptions) | Yes | Parameters for sending data over a UDP socket connection. For details, see [UDPSendOptions](#udpsendoptions). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, no value is returned. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301206 | Socks5 failed to connect to the proxy server. |
| 2301207 | Socks5 username or password is invalid. |
| 2301208 | Socks5 failed to connect to the remote server. |
| 2301209 | Socks5 failed to negotiate the authentication method. |
| 2301210 | Socks5 failed to send the message. |
| 2301211 | Socks5 failed to receive the message. |
| 2301212 | Socks5 serialization error. |
| 2301213 | Socks5 deserialization error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx', // Local IP address
  port: 1234
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx', // Peer IP address
  port: 8080
}
let sendOptions: socket.UDPSendOptions = {
  data: 'Hello, server!',
  address: netAddress
}
udp.send(sendOptions, (err: BusinessError) => {
  if (err) {
    console.error('send fail');
    return;
  }
  console.info('send success');
});

**Example (with socket proxy):**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx', // Local IP address
  port: 1234
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx', // Peer IP address
  port: 8080
}
let socks5Server: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let proxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let sendOptions: socket.UDPSendOptions = {
  data: 'Hello, server!',
  address: netAddress,
  proxy: proxyOptions,
}
udp.send(sendOptions, (err: BusinessError) => {
  if (err) {
    console.error('send fail');
    return;
  }
  console.info('send success');
});

#### \[h2\]send

send(options: UDPSendOptions): Promise<void>

Sends data over a UDP socket connection. This API uses a promise to return the result.

Before sending data, call [UDPSocket.bind()](#bind) to bind the IP address and port. Call the API in the worker thread or taskpool thread as this operation is time-consuming.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [UDPSendOptions](#udpsendoptions) | Yes | Parameters for sending data over a UDP socket connection. For details, see [UDPSendOptions](#udpsendoptions). |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301206 | Socks5 failed to connect to the proxy server. |
| 2301207 | Socks5 username or password is invalid. |
| 2301208 | Socks5 failed to connect to the remote server. |
| 2301209 | Socks5 failed to negotiate the authentication method. |
| 2301210 | Socks5 failed to send the message. |
| 2301211 | Socks5 failed to receive the message. |
| 2301212 | Socks5 serialization error. |
| 2301213 | Socks5 deserialization error. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx', // Local IP address
  port: 8080
}
udp.bind(bindAddr).then(() => {
  console.info('bind success');
}).catch((err: BusinessError) => {
  console.error('bind fail');
  return;
});
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx', // Peer IP address
  port: 8080
}
let sendOptions: socket.UDPSendOptions = {
  data: 'Hello, server!',
  address: netAddress
}
udp.send(sendOptions).then(() => {
  console.info('send success');
}).catch((err: BusinessError) => {
  console.error('send fail');
});

**Example (with socket proxy):**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx', // Local IP address
  port: 8080
}
udp.bind(bindAddr).then(() => {
  console.info('bind success');
}).catch((err: BusinessError) => {
  console.error('bind fail');
  return;
});
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx', // Peer IP address
  port: 8080
}
let socks5Server: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let proxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let sendOptions: socket.UDPSendOptions = {
  data: 'Hello, server!',
  address: netAddress,
  proxy: proxyOptions,
}
udp.send(sendOptions).then(() => {
  console.info('send success');
}).catch((err: BusinessError) => {
  console.error('send fail');
});

#### \[h2\]close

close(callback: AsyncCallback<void>): void

Closes a UDP socket connection. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
udp.close((err: BusinessError) => {
  if (err) {
    console.error('close fail');
    return;
  }
  console.info('close success');
})

#### \[h2\]close

close(): Promise<void>

Closes a UDP socket connection. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
udp.close().then(() => {
  console.info('close success');
}).catch((err: BusinessError) => {
  console.error('close fail');
});

#### \[h2\]getState

getState(callback: AsyncCallback<SocketStateBase>): void

Obtains the status of the UDP socket connection. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/IegaIbQ2RW6452KRySlO_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ECAFDFA59F8AEB7D0FAC129EC049640CFC494175A039EB4DAB539C285A94E9A0)

This API can be called only after **bind** is successfully called.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[SocketStateBase](#socketstatebase)\> | Yes | Callback used to return the result. If the operation is successful, the status of the UDP socket connection is returned. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.error('bind success');
  udp.getState((err: BusinessError, data: socket.SocketStateBase) => {
    if (err) {
      console.error('getState fail');
      return;
    }
    console.info('getState success:' + JSON.stringify(data));
  })
})

#### \[h2\]getState

getState(): Promise<SocketStateBase>

Obtains the status of the UDP socket connection. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/7RUTRXZFR1G-L5ERZoBb-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0604AD7D034C4395BCE448F90A564C5EC388E0318674AC3654AA9255E7C89BC)

This API can be called only after **bind** is successfully called.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SocketStateBase](#socketstatebase)\> | Promise used to return the result. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
  udp.getState().then((data: socket.SocketStateBase) => {
    console.info('getState success:' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error('getState fail' + JSON.stringify(err));
  });
});

#### \[h2\]setExtraOptions

setExtraOptions(options: UDPExtraOptions, callback: AsyncCallback<void>): void

Sets other properties of the **UDPSocket** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/WUCIdowqRiimDHNomInN9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6967D38311D30D30B4F6327DCDB3ABCADC90CDF39CB160FE1531616341FC5E4)

This API can be called only after **bind** is successfully called.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [UDPExtraOptions](#udpextraoptions) | Yes | Other properties of the **UDPSocket** object. For details, see [UDPExtraOptions](#udpextraoptions). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, no value is returned. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();

let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
  let udpextraoptions: socket.UDPExtraOptions = {
    receiveBufferSize: 8192,
    sendBufferSize: 8192,
    reuseAddress: false,
    socketTimeout: 6000,
    broadcast: true
  }
  udp.setExtraOptions(udpextraoptions, (err: BusinessError) => {
    if (err) {
      console.error('setExtraOptions fail');
      return;
    }
    console.info('setExtraOptions success');
  })
})

#### \[h2\]setExtraOptions

setExtraOptions(options: UDPExtraOptions): Promise<void>

Sets other properties of the **UDPSocket** object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/OES6SBUERaOCWgJAH2RZwQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=379EE890F290A17721F2A62FCCD559E5DBF5EB51DB4C3CF9E82C72595C302AEA)

This API can be called only after **bind** is successfully called.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [UDPExtraOptions](#udpextraoptions) | Yes | Other properties of the **UDPSocket** object. For details, see [UDPExtraOptions](#udpextraoptions). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();

let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
  let udpextraoptions: socket.UDPExtraOptions = {
    receiveBufferSize: 8192,
    sendBufferSize: 8192,
    reuseAddress: false,
    socketTimeout: 6000,
    broadcast: true
  }
  udp.setExtraOptions(udpextraoptions).then(() => {
    console.info('setExtraOptions success');
  }).catch((err: BusinessError) => {
    console.error('setExtraOptions fail');
  });
})

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

Obtains the local socket address of a **UDPSocket** connection. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/AKqt0XbsTau1XMCRYswEbw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C5E3200E66EF3EEC22C885C21C4C349940A227FEEFEB099D737D3EC335CFB2EE)

This API can be called only after **bind** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();

let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
udp.bind(bindAddr).then(() => {
  console.info('bind success');
  udp.getLocalAddress().then((localAddress: socket.NetAddress) => {
        console.info("UDP\_Socket get SUCCESS! Address: " + JSON.stringify(localAddress));
      }).catch((err: BusinessError) => {
        console.error("UDP\_Socket get FAILED! Error: " + JSON.stringify(err));
      })
}).catch((err: BusinessError) => {
  console.error('bind fail');
});

#### \[h2\]on('message')

on(type: 'message', callback: Callback<SocketMessageInfo>): void

Subscribes to **message** events of the **UDPSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**message**: message receiving event.

 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | Yes | Callback used to return the result. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();

udp.on('message', (value: socket.SocketMessageInfo) => {
  let messageView = '';
  let uint8Array = new Uint8Array(value.message);
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let messages = uint8Array\[i\];
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
});

#### \[h2\]off('message')

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

Unsubscribes from **message** events of the **UDPSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**message**: message receiving event.

 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let messageView = '';
let callback = (value: socket.SocketMessageInfo) => {
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let uint8Array = new Uint8Array(value.message)
    let messages = uint8Array\[i\]
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
}
udp.on('message', callback);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
udp.off('message', callback);
udp.off('message');

#### \[h2\]on('listening' | 'close')

on(type: 'listening' | 'close', callback: Callback<void>): void

Subscribes to **listening** events or **close** events of the **UDPSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- **listening**: data packet message event.

\- **close**: close event.

 |
| callback | Callback<void> | Yes | Callback used to return the result. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
udp.on('listening', () => {
  console.info("on listening success");
});
udp.on('close', () => {
  console.info("on close success");
});

#### \[h2\]off('listening' | 'close')

off(type: 'listening' | 'close', callback?: Callback<void>): void

Unsubscribes from **listening** events or **close** events of the **UDPSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- **listening**: data packet message event.

\- **close**: close event.

 |
| callback | Callback<void> | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let callback1 = () => {
  console.info("on listening, success");
}
udp.on('listening', callback1);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
udp.off('listening', callback1);
udp.off('listening');
let callback2 = () => {
  console.info("on close, success");
}
udp.on('close', callback2);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
udp.off('close', callback2);
udp.off('close');

#### \[h2\]on('error')

on(type: 'error', callback: ErrorCallback): void

Subscribes to **error** events of the **UDPSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: error event.

 |
| callback | ErrorCallback | Yes | Callback used to return the result. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
udp.on('error', (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err))
});

#### \[h2\]off('error')

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from **error** events of the **UDPSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: error event.

 |
| callback | ErrorCallback | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let callback = (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err));
}
udp.on('error', callback);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
udp.off('error', callback);
udp.off('error');

#### NetAddress

Defines the destination address.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| address11+ | string | No | No | Bound IP address. |
| port | number | No | No | Port number. The value ranges from **0** to **65535**. If this parameter is not specified, the system randomly allocates a port. |
| family | number | No | No | 
Network protocol type.

\- **1**: IPv4 The default value is **1**.

\- **2**: IPv6 For an IPv6 address, this field must be explicitly set to **2**.

\- **3**: domain address18+ For a domain address, this field must be explicitly set to **3**. Currently, only [TCPSocket.connect](#connect) and [TLSSocket.connect](#connect9) are supported.

 |

#### ProxyOptions18+

Defines the socket proxy information.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [ProxyTypes](#proxytypes18) | No | No | Proxy type. |
| address | [NetAddress](#netaddress) | No | No | Proxy address. |
| username | string | No | Yes | User name. This field must be specified if the user password authentication mode is used. |
| password | string | No | Yes | Password. This field must be specified if the user password authentication mode is used. |

#### ProxyTypes18+

Enumerates socket proxy types.

**System capability**: SystemCapability.Communication.NetStack

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | No proxy. |
| SOCKS5 | 1 | SOCKS5 proxy. |

#### UDPSendOptions

Defines the parameters for sending data over a UDP socket connection.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| data | string | ArrayBuffer | No | No | Data to send. |
| address | [NetAddress](#netaddress) | No | No | Destination address. |
| proxy18+ | [ProxyOptions](#proxyoptions18) | No | Yes | Proxy option. By default, no proxy is used. |

#### UDPExtraOptions

Defines other properties of the **UDPSocket** object. This object is inherited from \[ExtraOptionsBase\] (#extraoptionsbase).

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| broadcast | boolean | No | Yes | Whether to send broadcast messages. The value **true** indicates that broadcast messages can be sent, and the value **false** indicates the opposite. The default value is **false**. |

#### SocketMessageInfo11+

Defines the socket connection information.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| message | ArrayBuffer | No | No | Received **message** event. |
| remoteInfo | [SocketRemoteInfo](#socketremoteinfo) | No | No | Socket connection information. |

#### SocketStateBase

Defines the status of the socket connection.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isBound | boolean | No | No | Whether the connection is in the bound state. The value **true** indicates that the connection is in the bound state, and the value **false** indicates the opposite. |
| isClose | boolean | No | No | Whether the connection is in the closed state. The value **true** indicates that the connection is in the closed state, and the value **false** indicates the opposite. |
| isConnected | boolean | No | No | Whether the connection is in the connected state. The value **true** indicates that the connection is in the connected state, and the value **false** indicates the opposite. |

#### SocketRemoteInfo

Defines information about the socket connection.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| address | string | No | No | Bound IP address. |
| family | 'IPv4' | 'IPv6' | No | No | 
Network protocol type.

\- IPv4

\- IPv6

The default value is **IPv4**.

 |
| port | number | No | No | Port number. The value ranges from **0** to **65535**. |
| size | number | No | No | Length of the server response message, in bytes. |

#### Description of UDP Error Codes

The UDP error code mapping is in the format of 2301000 + Linux kernel error code.

For details about error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md).

#### socket.constructMulticastSocketInstance11+

constructMulticastSocketInstance(): MulticastSocket

Creates a **MulticastSocket** object.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| [MulticastSocket](#multicastsocket11) | **MulticastSocket** object. |

**Example**

import { socket } from '@kit.NetworkKit';
let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();

#### MulticastSocket11+

Defines a **MulticastSocket** connection. Before calling MulticastSocket APIs, you need to call [socket.constructMulticastSocketInstance](#socketconstructmulticastsocketinstance11) to create a **MulticastSocket** object.

#### \[h2\]addMembership11+

addMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>): void

Adds a member to a multicast group. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/JwNYj_wjRQuNQ2bxlv6S7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3662353F5F919763B45D280A7F8B515186C65AB93482C274033143BFFCF2373)

The IP addresses used for multicast belong to a specific range, for example, 224.0.0.0 to 239.255.255.255.

A member in a multicast group can serve as a sender or a receiver. Data is transmitted in broadcast mode, regardless of the client or server.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| multicastAddress | [NetAddress](#netaddress) | Yes | Destination address. For details, see [NetAddress](#netaddress). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301022 | Invalid argument. |
| 2301088 | Not a socket. |
| 2301098 | Address in use. |

**Example**

import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
let addr: socket.NetAddress = {
  address: '239.255.0.1',
  port: 8080
}
multicast.addMembership(addr, (err: Object) => {
  if (err) {
    console.error('add membership fail, err: ' + JSON.stringify(err));
    return;
  }
  console.info('add membership success');
})

#### \[h2\]addMembership11+

addMembership(multicastAddress: NetAddress): Promise<void>

Adds a member to a multicast group. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/PgMzB4lyRIC9cZl28kyJxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF338B146479FFBE2BF0E8541AFF5704E9B81044F79B3E9CD7B85F73833B80E2)

The IP addresses used for multicast belong to a specific range, for example, 224.0.0.0 to 239.255.255.255.

A member in a multicast group can serve as a sender or a receiver. Data is transmitted in broadcast mode, regardless of the client or server.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| multicastAddress | [NetAddress](#netaddress) | Yes | Destination address. For details, see [NetAddress](#netaddress). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301088 | Not a socket. |
| 2301098 | Address in use. |

**Example**

import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
let addr: socket.NetAddress = {
  address: '239.255.0.1',
  port: 8080
}
multicast.addMembership(addr).then(() => {
  console.info('addMembership success');
}).catch((err: Object) => {
  console.error('addMembership fail');
});

#### \[h2\]dropMembership11+

dropMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>): void

Drops a member from a multicast group. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/YgxeOwyuQmSwPgajVAMS5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10FFB6B2AFC6C0E56755F0268F8977255D52027B0E6C90E5985DDC30AF889A0F)

The IP addresses used for multicast belong to a specific range, for example, 224.0.0.0 to 239.255.255.255.

You can drop only a member that has been added to a multicast group by using [addMembership](#addmembership11).

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| multicastAddress | [NetAddress](#netaddress) | Yes | Destination address. For details, see [NetAddress](#netaddress). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301088 | Not a socket. |
| 2301098 | Address in use. |

**Example**

import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
let addr: socket.NetAddress = {
  address: '239.255.0.1',
  port: 8080
}
multicast.dropMembership(addr, (err: Object) => {
  if (err) {
    console.error('drop membership fail, err: ' + JSON.stringify(err));
    return;
  }
  console.info('drop membership success');
})

#### \[h2\]dropMembership11+

dropMembership(multicastAddress: NetAddress): Promise<void>

Drops a member from a multicast group. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/Rxhw1BpbT_OdiGSxeCEqcQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67218F7876EA82D1231C873E70162BB11993FD12124B4326E4E0F3096A8D39AB)

The IP addresses used for multicast belong to a specific range, for example, 224.0.0.0 to 239.255.255.255.

You can drop only a member that has been added to a multicast group by using [addMembership](#addmembership11).

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| multicastAddress | [NetAddress](#netaddress) | Yes | Destination address. For details, see [NetAddress](#netaddress). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301088 | Not a socket. |
| 2301098 | Address in use. |

**Example**

import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
let addr: socket.NetAddress = {
  address: '239.255.0.1',
  port: 8080
}
multicast.dropMembership(addr).then(() => {
  console.info('drop membership success');
}).catch((err: Object) => {
  console.error('drop membership fail');
});

#### \[h2\]setMulticastTTL11+

setMulticastTTL(ttl: number, callback: AsyncCallback<void>): void

Sets the time to live (TTL) for multicast packets. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/M_-600ErRlmBZKrCHw0PIw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F6B2E6A70E27B9F88B5617A0A88C9277B510965500D047DB48F7C85295AC4F2)

TTL is used to limit the maximum number of router hops for packet transmission on a network.

The value ranges from 0 to 255. The default value is **1**.

If the TTL value is **1**, multicast packets can be transmitted only to the host directly connected to the sender. If the TTL is set to a large value, multicast packets can be transmitted over a longer distance.

This API is effective only after [addMembership](#addmembership11) is called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ttl | number | Yes | TTL value. The value is of the number type. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2301022 | Invalid argument. |
| 2301088 | Not a socket. |

**Example**

import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
let ttl = 8
multicast.setMulticastTTL(ttl, (err: Object) => {
  if (err) {
    console.error('set ttl fail, err: ' + JSON.stringify(err));
    return;
  }
  console.info('set ttl success');
})

#### \[h2\]setMulticastTTL11+

setMulticastTTL(ttl: number): Promise<void>

Sets the TTL for multicast packets. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/JNK-Pe_GTCWXiwpBiQ7NGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F74DE27C925C38C837F3E43DC53214A4B24B4F6CEC2507BEBD96B3C6A97648DE)

TTL is used to limit the maximum number of router hops for packet transmission on a network.

The value ranges from 0 to 255. The default value is **1**.

If the TTL value is **1**, multicast packets can be transmitted only to the host directly connected to the sender. If the TTL is set to a large value, multicast packets can be transmitted over a longer distance.

This API is effective only after [addMembership](#addmembership11) is called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ttl | number | Yes | TTL value. The value is of the number type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2301022 | Invalid argument. |
| 2301088 | Not a socket. |

**Example**

import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.setMulticastTTL(8).then(() => {
  console.info('set ttl success');
}).catch((err: Object) => {
  console.error('set ttl failed');
});

#### \[h2\]getMulticastTTL11+

getMulticastTTL(callback: AsyncCallback<number>): void

Obtains the TTL for multicast packets. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/fSl4iiFATAul8VGYFnMTQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C431F63D93ADE730264C0AAF1275EDD218E6626A8CDE7E28CB5A96E7915A59A7)

TTL is used to limit the maximum number of router hops for packet transmission on a network.

The value ranges from 0 to 255. The default value is **1**.

If the TTL value is **1**, multicast packets can be transmitted only to the host directly connected to the sender. If the TTL is set to a large value, multicast packets can be transmitted over a longer distance.

This API is effective only after [addMembership](#addmembership11) is called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2301088 | Not a socket. |

**Example**

import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.getMulticastTTL((err: Object, value: Number) => {
  if (err) {
    console.error('set ttl fail, err: ' + JSON.stringify(err));
    return;
  }
  console.info('set ttl success, value: ' + JSON.stringify(value));
})

#### \[h2\]getMulticastTTL11+

getMulticastTTL(): Promise<number>

Obtains the TTL for multicast packets. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/6GbdSJ1IT76ssqf7H-DUrw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C8576DA9ED8E99946C34FFF2C938ADDCA745F3E947C31D2634181313D71E0491)

TTL is used to limit the maximum number of router hops for packet transmission on a network.

The value ranges from 0 to 255. The default value is **1**.

If the TTL value is **1**, multicast packets can be transmitted only to the host directly connected to the sender. If the TTL is set to a large value, multicast packets can be transmitted over a longer distance.

This API is effective only after [addMembership](#addmembership11) is called.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2301088 | Not a socket. |

**Example**

import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.getMulticastTTL().then((value: Number) => {
  console.info('ttl: ', JSON.stringify(value));
}).catch((err: Object) => {
  console.error('set ttl failed');
});

#### \[h2\]setLoopbackMode11+

setLoopbackMode(flag: boolean, callback: AsyncCallback<void>): void

Sets the loopback mode flag for multicast communication. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/SfvXQySkS06JFv2Rth5gXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7BD05A08B8F71E3CCC41D351F995801CF942DFE15CA527D95BB92EEDC981C9BE)

Use this API to enable or disable the loopback mode. By default, the loopback mode is enabled.

The value **true** indicates that the host is allowed to receive the multicast packets sent by itself, and the value **false** indicates the opposite.

This API is effective only after [addMembership](#addmembership11) is called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| flag | boolean | Yes | Whether to enable the loopback mode. The value **true** means to enable the loopback mode, and the value **false** means the opposite. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2301088 | Not a socket. |

**Example**

import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.setLoopbackMode(false, (err: Object) => {
  if (err) {
    console.error('set loopback mode fail, err: ' + JSON.stringify(err));
    return;
  }
  console.info('set loopback mode success');
})

#### \[h2\]setLoopbackMode11+

setLoopbackMode(flag: boolean): Promise<void>

Sets the loopback mode flag for multicast communication. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/6SQAIAVtTl-e93cM7uV8CQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=530C31AC2CA249AAF4C9DDEDA3D853B4099A262A6853612B343CA268E0E22363)

Use this API to enable or disable the loopback mode. By default, the loopback mode is enabled.

The value **true** indicates that the host is allowed to receive the multicast packets sent by itself, and the value **false** indicates the opposite.

This API is effective only after [addMembership](#addmembership11) is called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| flag | boolean | Yes | Whether to enable the loopback mode. The value **true** means to enable the loopback mode, and the value **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2301088 | Not a socket. |

**Example**

import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.setLoopbackMode(false).then(() => {
  console.info('set loopback mode success');
}).catch((err: Object) => {
  console.error('set loopback mode failed');
});

#### \[h2\]getLoopbackMode11+

getLoopbackMode(callback: AsyncCallback<boolean>): void

Obtains the loopback mode flag for multicast communication. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/Wse8K9BeQyOVa3sXTL_puA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6302ABF31213DA341B05FB9034831E20F39CF85543A6CB78C6717314DDEB1192)

Use this API to check whether the loopback mode is enabled.

The value **true** indicates that the loopback mode is enabled, and the value **false** indicates the opposite. When the loopback mode is disabled, the host does not receive the multicast packets sent by itself.

This API is effective only after [addMembership](#addmembership11) is called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the loopback mode is enabled, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2301088 | Not a socket. |

**Example**

import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.getLoopbackMode((err: Object, value: Boolean) => {
  if (err) {
    console.error('get loopback mode fail, err: ' + JSON.stringify(err));
    return;
  }
  console.info('get loopback mode success, value: ' + JSON.stringify(value));
})

#### \[h2\]getLoopbackMode11+

getLoopbackMode(): Promise<boolean>

Obtains the loopback mode flag for multicast communication. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/U88KYoG9TdKNz9Yj0rBTFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=494080E3391BEF5BB20F27E0A434C135F2C87B2226B302D2D99861C726C487DF)

Use this API to check whether the loopback mode is enabled.

The value **true** indicates that the loopback mode is enabled, and the value **false** indicates the opposite. When the loopback mode is disabled, the host does not receive the multicast packets sent by itself.

This API is effective only after [addMembership](#addmembership11) is called.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the loopback mode is enabled, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2301088 | Not a socket. |

**Example**

import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.getLoopbackMode().then((value: Boolean) => {
  console.info('loopback mode: ', JSON.stringify(value));
}).catch((err: Object) => {
  console.error('get loopback mode failed');
});

#### socket.constructTCPSocketInstance

constructTCPSocketInstance(): TCPSocket

Creates a **TCPSocket** object.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| [TCPSocket](#tcpsocket) | **TCPSocket** object. |

**Example**

import { socket } from '@kit.NetworkKit';
let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();

#### TCPSocket

Defines a TCP socket connection. Before calling TCPSocket APIs, you need to call [socket.constructTCPSocketInstance](#socketconstructtcpsocketinstance) to create a **TCPSocket** object.

#### \[h2\]bind

bind(address: NetAddress, callback: AsyncCallback<void>): void

Binds an IP address and a port number. The port number can be customized or randomly allocated by the system. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/d-D_w27_TjGS9UNmHI1p_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67FDEF6EB5766BBF1D5FC6B2C5753A42B2B8F7690754D6B2148830FAD4CFA360)

If the bind operation fails due to a port conflict, the system will randomly allocate a port number.

The TCP client can call **tcp.bind** to explicitly bind the IP address and port number, and then call **tcp.connect** to connect to the server. Alternatively, the TCP client can directly call **tcp.connect** to automatically bind the IP address and port number to connect to the server.

If the IP address is **localhost** or **127.0.0.1**, only local loopback access is allowed; that is, the TCP client and the server are deployed on the same device.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | Yes | Local address. For details, see [NetAddress](#netaddress). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tcp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
})

#### \[h2\]bind

bind(address: NetAddress): Promise<void>

Binds an IP address and a port number. The port number can be customized or randomly allocated by the system. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/8xEF9LUbRJucm-EpotGQyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21D923CF4B9DEDC59474881F5B47CD3F1C030B3FCCCD425B19E4903C286EBC43)

If the bind operation fails due to a port conflict, the system will randomly allocate a port number.

The TCP client can call **tcp.bind** to explicitly bind the IP address and port number, and then call **tcp.connect** to connect to the server. Alternatively, the TCP client can directly call **tcp.connect** to automatically bind the IP address and port number to connect to the server.

If the IP address is **localhost** or **127.0.0.1**, only local loopback access is allowed; that is, the TCP client and the server are deployed on the same device.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | Yes | Local address. For details, see [NetAddress](#netaddress). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tcp.bind(bindAddr).then(() => {
  console.info('bind success');
}).catch((err: BusinessError) => {
  console.error('bind fail');
});

#### \[h2\]connect

connect(options: TCPConnectOptions, callback: AsyncCallback<void>): void

Sets up a connection to the specified IP address and port number. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/vpdd7FksR_msWSBD7Qez3A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18606F2E0E8AA8CF83836801CDDF3664946656A552C0A6BA8C7FD8FF129525B3)

This API allows you to connect to the TCP server without first executing **tcp.bind**.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TCPConnectOptions](#tcpconnectoptions) | Yes | TCP socket connection parameters. For details, see [TCPConnectOptions](#tcpconnectoptions). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301206 | Socks5 failed to connect to the proxy server. |
| 2301207 | Socks5 username or password is invalid. |
| 2301208 | Socks5 failed to connect to the remote server. |
| 2301209 | Socks5 failed to negotiate the authentication method. |
| 2301210 | Socks5 failed to send the message. |
| 2301211 | Socks5 failed to receive the message. |
| 2301212 | Socks5 serialization error. |
| 2301213 | Socks5 deserialization error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions, (err: BusinessError) => {
  if (err) {
    console.error('connect fail');
    return;
  }
  console.info('connect success');
})

**Example (with socket proxy):**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let socks5Server: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let proxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000,
  proxy: proxyOptions,
}
tcp.connect(tcpconnectoptions, (err: BusinessError) => {
  if (err) {
    console.error('connect fail');
    return;
  }
  console.info('connect success');
})

#### \[h2\]connect

connect(options: TCPConnectOptions): Promise<void>

Sets up a connection to the specified IP address and port number. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/JLOqeBI6TFiVFhdNV9ln3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90275886633A4A024BFAB1885A851419D230955AB53E348D270147154696B696)

This API allows you to connect to the TCP server without first executing **tcp.bind**.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TCPConnectOptions](#tcpconnectoptions) | Yes | TCP socket connection parameters. For details, see [TCPConnectOptions](#tcpconnectoptions). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301206 | Socks5 failed to connect to the proxy server. |
| 2301207 | Socks5 username or password is invalid. |
| 2301208 | Socks5 failed to connect to the remote server. |
| 2301209 | Socks5 failed to negotiate the authentication method. |
| 2301210 | Socks5 failed to send the message. |
| 2301211 | Socks5 failed to receive the message. |
| 2301212 | Socks5 serialization error. |
| 2301213 | Socks5 deserialization error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions).then(() => {
  console.info('connect success')
}).catch((err: BusinessError) => {
  console.error('connect fail');
});

**Example (with socket proxy):**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let socks5Server: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let proxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000,
  proxy: proxyOptions,
}
tcp.connect(tcpconnectoptions).then(() => {
  console.info('connect success')
}).catch((err: BusinessError) => {
  console.error('connect fail');
});

#### \[h2\]send

send(options: TCPSendOptions, callback: AsyncCallback<void>): void

Sends data over a TCP socket connection. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/Saknis9nRWO6e4FmBULMMQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5FD63CC21C7D22D40C3F81C78E0B5F67DF97EAE994742BDFCF8C3F6302EA024E)

This API can be called only after **connect** is successfully called. Call the API in the worker thread or taskpool thread as this operation is time-consuming.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TCPSendOptions](#tcpsendoptions) | Yes | Parameters for sending data over a TCP socket connection. For details, see [TCPSendOptions](#tcpsendoptions). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions, () => {
  console.info('connect success');
  let tcpSendOptions: socket.TCPSendOptions = {
    data: 'Hello, server!'
  }
  tcp.send(tcpSendOptions, (err: BusinessError) => {
    if (err) {
      console.error('send fail');
      return;
    }
    console.info('send success');
  })
})

#### \[h2\]send

send(options: TCPSendOptions): Promise<void>

Sends data over a TCP socket connection. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/NTIhx-yuTG29ML4DBxRF5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=136D6F4F323A479A59094AC1A7378FC5DCE4DFA36FB73EC2620FE570F839CBEA)

This API can be called only after **connect** is successfully called. Call the API in the worker thread or taskpool thread as this operation is time-consuming.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TCPSendOptions](#tcpsendoptions) | Yes | Parameters for sending data over a TCP socket connection. For details, see [TCPSendOptions](#tcpsendoptions). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions, () => {
  console.info('connect success');
  let tcpSendOptions: socket.TCPSendOptions = {
    data: 'Hello, server!'
  }
  tcp.send(tcpSendOptions).then(() => {
    console.info('send success');
  }).catch((err: BusinessError) => {
    console.error('send fail');
  });
})

#### \[h2\]close

close(callback: AsyncCallback<void>): void

Closes a TCP socket connection. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();

tcp.close((err: BusinessError) => {
  if (err) {
    console.error('close fail');
    return;
  }
  console.info('close success');
})

#### \[h2\]close

close(): Promise<void>

Closes a TCP socket connection. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();

tcp.close().then(() => {
  console.info('close success');
}).catch((err: BusinessError) => {
  console.error('close fail');
});

#### \[h2\]getRemoteAddress

getRemoteAddress(callback: AsyncCallback<NetAddress>): void

Obtains the remote address of a socket connection. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/HCuFjageShaMjg7lv9iEeg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F82A01974D690AEA773423C12155D8366C2D65C2975B7BC45F3EFCD7974CD8D2)

This API can be called only after **connect** is successfully called.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[NetAddress](#netaddress)\> | Yes | Callback used to return the result. If the operation is successful, the remote address is returned. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions, () => {
  console.info('connect success');
  tcp.getRemoteAddress((err: BusinessError, data: socket.NetAddress) => {
    if (err) {
      console.error('getRemoteAddressfail');
      return;
    }
    console.info('getRemoteAddresssuccess:' + JSON.stringify(data));
  })
});

#### \[h2\]getRemoteAddress

getRemoteAddress(): Promise<NetAddress>

Obtains the remote address of a socket connection. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/QGzb04zuQH2uhLXyPs8ydA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=004B4249A0DB88EDDE3FB648EF7276774530A3D8260E52656159AC2FE0191CC0)

This API can be called only after **connect** is successfully called.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions).then(() => {
  console.info('connect success');
  tcp.getRemoteAddress().then(() => {
    console.info('getRemoteAddress success');
  }).catch((err: BusinessError) => {
    console.error('getRemoteAddressfail');
  });
}).catch((err: BusinessError) => {
  console.error('connect fail');
});

#### \[h2\]getState

getState(callback: AsyncCallback<SocketStateBase>): void

Obtains the status of the TCP socket connection. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/cjDOkNJYSdiXag3i6N4CeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DF3998D744D5E28B05FE66E3A49C6C4C3C6FEF20112625D8215686B6927DCFF)

This API can be called only after **bind** or **connect** is successfully called.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[SocketStateBase](#socketstatebase)\> | Yes | Callback used to return the result. If the operation is successful, the status of the TCP socket is returned. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions, () => {
  console.info('connect success');
  tcp.getState((err: BusinessError, data: socket.SocketStateBase) => {
    if (err) {
      console.error('getState fail');
      return;
    }
    console.info('getState success:' + JSON.stringify(data));
  });
});

#### \[h2\]getState

getState(): Promise<SocketStateBase>

Obtains the status of the TCP socket connection. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/AK24xVNBQGCR65EYQNnDSA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DFE2039DE220B084734A95BE150FDB8312A85314781619876C7D13216FC7AFC)

This API can be called only after **bind** or **connect** is successfully called.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SocketStateBase](#socketstatebase)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions).then(() => {
  console.info('connect success');
  tcp.getState().then(() => {
    console.info('getState success');
  }).catch((err: BusinessError) => {
    console.error('getState fail');
  });
}).catch((err: BusinessError) => {
  console.error('connect fail');
});

#### \[h2\]getSocketFd10+

getSocketFd(callback: AsyncCallback<number>): void

Obtains the file descriptor of the **TCPSocket** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/IXUNI29STZq7_rUbSA8XfA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3061D4544F2E6D088B3B56962A3CFFEE06913154132F8FDC8BAC53EC1B59360B)

This API can be called only after **bind** or **connect** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, the file descriptor of the socket is returned. Otherwise, **undefined** is returned. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  // Bind the specified network API.
}
tcp.bind(bindAddr)
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions)
tcp.getSocketFd((err: BusinessError, data: number) => {
  console.error("getSocketFd failed: " + err);
  console.info("socketFd: " + data);
})

#### \[h2\]getSocketFd10+

getSocketFd(): Promise<number>

Obtains the file descriptor of the **TCPSocket** object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/gfnpdHTPRdWW0YEVON0RTg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F90870B7E9D4631D5E2050A0BB45F8A380C257D20191243353FBF4DBEE2AC43C)

This API can be called only after **bind** or **connect** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let bindAddr: socket.NetAddress = {
    address: '192.168.xx.xxx',
  // Bind the specified network API.
}
tcp.bind(bindAddr)
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions)
tcp.getSocketFd().then((data: number) => {
  console.info("socketFd: " + data);
})

#### \[h2\]setExtraOptions

setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void

Sets other properties of the **TCPSocket** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/1wOnWNkMR1WWi2a9d4k4XQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD2E321D8A01075972C1E21222BF32EAFFF94B7690F6DD182439C55CD90644A3)

This API can be called only after **bind** or **connect** is successfully called.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TCPExtraOptions](#tcpextraoptions) | Yes | Other properties of the **TCPSocket** object. For details, see [TCPExtraOptions](#tcpextraoptions). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}

interface SocketLinger {
  on: boolean;
  linger: number;
}

tcp.connect(tcpconnectoptions, () => {
  console.info('connect success');
  let tcpExtraOptions: socket.TCPExtraOptions = {
    keepAlive: true,
    OOBInline: true,
    TCPNoDelay: true,
    socketLinger: { on: true, linger: 10 } as SocketLinger,
    receiveBufferSize: 8192,
    sendBufferSize: 8192,
    reuseAddress: true,
    socketTimeout: 3000
  }
  tcp.setExtraOptions(tcpExtraOptions, (err: BusinessError) => {
    if (err) {
      console.error('setExtraOptions fail');
      return;
    }
    console.info('setExtraOptions success');
  });
});

#### \[h2\]setExtraOptions

setExtraOptions(options: TCPExtraOptions): Promise<void>

Sets other properties of the **TCPSocket** object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/30kSi0v-TmyCokAUo5Ru4Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=586AB7275C6789D984D4BE7878268C8B84BF4A62E72DB2E67133680257D7B8D5)

This API can be called only after **bind** or **connect** is successfully called.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TCPExtraOptions](#tcpextraoptions) | Yes | Other properties of the **TCPSocket** object. For details, see [TCPExtraOptions](#tcpextraoptions). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}

interface SocketLinger {
  on: boolean;
  linger: number;
}

tcp.connect(tcpconnectoptions, () => {
  console.info('connect success');
  let tcpExtraOptions: socket.TCPExtraOptions = {
    keepAlive: true,
    OOBInline: true,
    TCPNoDelay: true,
    socketLinger: { on: true, linger: 10 } as SocketLinger,
    receiveBufferSize: 8192,
    sendBufferSize: 8192,
    reuseAddress: true,
    socketTimeout: 3000
  }
  tcp.setExtraOptions(tcpExtraOptions).then(() => {
    console.info('setExtraOptions success');
  }).catch((err: BusinessError) => {
    console.error('setExtraOptions fail');
  });
});

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

Obtains the local socket address of a **TCPSocket** connection. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/yDf_Ut53TkWpVCA0RfZWMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0653FAFCF041430F39047F4B8CB671DDDDC470DCDAD19632CD9DBD5B975F71D7)

This API can be called only after **bind** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  family: 1,
  port: 8080
}
tcp.bind(bindAddr).then(() => {
  tcp.getLocalAddress().then((localAddress: socket.NetAddress) => {
    console.info("SUCCESS! Address:" + JSON.stringify(localAddress));
  }).catch((err: BusinessError) => {
    console.error("FAILED! Error:" + JSON.stringify(err));
  })
}).catch((err: BusinessError) => {
  console.error('bind fail');
});

#### \[h2\]on('message')

on(type: 'message', callback: Callback<SocketMessageInfo>): void

Subscribes to **message** events of the **TCPSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**message**: message receiving event.

 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | Yes | Callback used to return the result. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
tcp.on('message', (value: socket.SocketMessageInfo) => {
  let messageView = '';
  let uint8Array = new Uint8Array(value.message) ;
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let messages = uint8Array\[i\];
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
});

#### \[h2\]off('message')

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

Unsubscribes from **message** events of the **TCPSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**message**: message receiving event.

 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let messageView = '';
let callback = (value: socket.SocketMessageInfo) => {
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let uint8Array = new Uint8Array(value.message)
    let messages = uint8Array\[i\]
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
}
tcp.on('message', callback);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
tcp.off('message', callback);
tcp.off('message');

#### \[h2\]on('connect' | 'close')

on(type: 'connect' | 'close', callback: Callback<void>): void

Subscribes to **connect** or **close** events of the **TCPSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- **connect**: connection event.

\- **close**: close event.

 |
| callback | Callback<void> | Yes | Callback used to return the result. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
tcp.on('connect', () => {
  console.info("on connect success")
});
tcp.on('close', () => {
  console.info("on close success")
});

#### \[h2\]off('connect' | 'close')

off(type: 'connect' | 'close', callback?: Callback<void>): void

Unsubscribes from **connect** or **close** events of the **TCPSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- **connect**: connection event.

\- **close**: close event.

 |
| callback | Callback<void> | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let callback1 = () => {
  console.info("on connect success");
}
tcp.on('connect', callback1);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
tcp.off('connect', callback1);
tcp.off('connect');
let callback2 = () => {
  console.info("on close success");
}
tcp.on('close', callback2);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
tcp.off('close', callback2);
tcp.off('close');

#### \[h2\]on('error')

on(type: 'error', callback: ErrorCallback): void

Subscribes to **error** events of the **TCPSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: error event.

 |
| callback | ErrorCallback | Yes | Callback used to return the result. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
tcp.on('error', (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err))
});

#### \[h2\]off('error')

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from **error** events of the **TCPSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: error event.

 |
| callback | ErrorCallback | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let callback = (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err));
}
tcp.on('error', callback);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
tcp.off('error', callback);
tcp.off('error');

#### TCPConnectOptions

Defines TCP socket connection parameters.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | No | No | Bound IP address and port number. |
| timeout | number | No | Yes | Timeout duration of the TCP socket connection, in ms. The default value is **5000**. |
| proxy18+ | [ProxyOptions](#proxyoptions18) | No | Yes | Proxy option. By default, no proxy is used. |

#### TCPSendOptions

Defines the parameters for sending data over a TCP socket connection.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| data | string| ArrayBuffer | No | No | Data to send. |
| encoding | string | No | Yes | Character encoding format. The options are as follows: **UTF-8**, **UTF-16BE**, **UTF-16LE**, **UTF-16**, **US-AECII**, and **ISO-8859-1**. The default value is **UTF-8**. |

#### TCPExtraOptions

Defines other properties of the **TCPSocket** object. This object is inherited from [ExtraOptionsBase](#extraoptionsbase).

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| keepAlive | boolean | No | Yes | Whether to keep the connection alive. The default value is **false**. The value **true** means to keep the connection alive, and the value **false** indicates the opposite. |
| OOBInline | boolean | No | Yes | Whether to enable OOBInline. The default value is **false**. The value **true** means to enable OOBInline, and the value **false** indicates the opposite. |
| TCPNoDelay | boolean | No | Yes | Whether to enable no-delay on the TCP socket connection. The default value is **false**. The value **true** means to enable no-delay on the TCP socket connection, and the value **false** indicates the opposite. |
| socketLinger | {on:boolean, linger:number} | No | Yes | 
Socket linger.

\- **on**: whether to enable socket linger. The value true means to enable socket linger and false means the opposite.

\- **linger**: linger time, in ms. The value ranges from **0** to **65535**.

Specify this parameter only when **on** is set to **true**.

 |

#### socket.constructTCPSocketServerInstance10+

constructTCPSocketServerInstance(): TCPSocketServer

Creates a **TCPSocketServer** object.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| [TCPSocketServer](#tcpsocketserver10) | **TCPSocketServer** object. |

**Example**

import { socket } from '@kit.NetworkKit';
let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

#### TCPSocketServer10+

Defines a TCP socket server connection. Before calling TCPSocketServer APIs, you need to call [socket.constructTCPSocketServerInstance](#socketconstructtcpsocketserverinstance10) to create a **TCPSocketServer** object.

#### \[h2\]listen10+

listen(address: NetAddress, callback: AsyncCallback<void>): void

Binds the IP address and port number. The port number can be specified or randomly allocated by the system. The server listens to and accepts TCP socket connections established over the socket. Multiple threads are used to process client data concurrently. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/nO2faiCnSBCQ2Kj61WTsjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B293F78E43D85A4F39DD375E98B1F6F25B762868926FF15E56473C5ABAF7CAF)

The server uses this API to perform the **bind**, **listen**, and **accept** operations. If the **bind** operation fails, the system randomly allocates a port number.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | Yes | Destination address. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303109 | Bad file number. |
| 2303111 | Resource temporarily unavailable. Try again. |
| 2303198 | Address already in use. |
| 2303199 | Cannot assign requested address. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
})

#### \[h2\]listen10+

listen(address: NetAddress): Promise<void>

Binds the IP address and port number. The port number can be specified or randomly allocated by the system. The server listens to and accepts TCP socket connections established over the socket. Multiple threads are used to process client data concurrently. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/Wv9fpHr1TRWCvLFlOcZzEA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F645344382A1FBBE0D56469E72AEB0F59113699CD8C85C7AC307F08672DAF23D)

The server uses this API to perform the **bind**, **listen**, and **accept** operations. If the **bind** operation fails, the system randomly allocates a port number.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | Yes | Destination address. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303109 | Bad file number. |
| 2303111 | Resource temporarily unavailable. Try again. |
| 2303198 | Address already in use. |
| 2303199 | Cannot assign requested address. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr).then(() => {
  console.info('listen success');
}).catch((err: BusinessError) => {
  console.error('listen fail');
});

#### \[h2\]getState10+

getState(callback: AsyncCallback<SocketStateBase>): void

Obtains the status of a TCP socket server connection. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/7KO2U3IwQq-pnROLUOd_8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84A54856A31F952A0504DDCCA9AB2DA2BFE323B1214A01A9CC09E13B40A96A01)

This API can be called only after **listen** is successfully called.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[SocketStateBase](#socketstatebase)\> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303188 | Socket operation on non-socket. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
})
tcpServer.getState((err: BusinessError, data: socket.SocketStateBase) => {
  if (err) {
    console.error('getState fail');
    return;
  }
  console.info('getState success:' + JSON.stringify(data));
})

#### \[h2\]getState10+

getState(): Promise<SocketStateBase>

Obtains the status of a TCP socket server connection. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/I6jbT60TSVadqi2iUNpW4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39D454A5A748200301D3BDDA261C0506FAE27367CAADC0C8CF280C264D43B957)

This API can be called only after **listen** is successfully called.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SocketStateBase](#socketstatebase)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303188 | Socket operation on non-socket. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
})
tcpServer.getState().then((data: socket.SocketStateBase) => {
  console.info('getState success' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error('getState fail');
});

#### \[h2\]setExtraOptions10+

setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void

Sets other properties of the **TCPSocketServer** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/js1p3tgEQ6S83usrmi7qvA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0C25F9DD7D2F1FB033222524748F2E234E3FD3B1CAE040338CF8F3A748A3AE4)

This API can be called only after **listen** is successfully called.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TCPExtraOptions](#tcpextraoptions) | Yes | Other properties of the **TCPSocketServer** object. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303188 | Socket operation on non-socket. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
})

interface SocketLinger {
  on: boolean;
  linger: number;
}

let tcpExtraOptions: socket.TCPExtraOptions = {
  keepAlive: true,
  OOBInline: true,
  TCPNoDelay: true,
  socketLinger: { on: true, linger: 10 } as SocketLinger,
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  reuseAddress: true,
  socketTimeout: 3000
}
tcpServer.setExtraOptions(tcpExtraOptions, (err: BusinessError) => {
  if (err) {
    console.error('setExtraOptions fail');
    return;
  }
  console.info('setExtraOptions success');
});

#### \[h2\]setExtraOptions10+

setExtraOptions(options: TCPExtraOptions): Promise<void>

Sets other properties of the **TCPSocketServer** object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/BZPHV_iFS9O9atKaCrzV2Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F84AF503E1674C4A9A7708D198D430961CC8477D3F27453C32866491DD386239)

This API can be called only after **listen** is successfully called.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TCPExtraOptions](#tcpextraoptions) | Yes | Other properties of the **TCPSocketServer** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303188 | Socket operation on non-socket. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}

interface SocketLinger {
  on: boolean;
  linger: number;
}

tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
})

let tcpExtraOptions: socket.TCPExtraOptions = {
  keepAlive: true,
  OOBInline: true,
  TCPNoDelay: true,
  socketLinger: { on: true, linger: 10 } as SocketLinger,
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  reuseAddress: true,
  socketTimeout: 3000
}
tcpServer.setExtraOptions(tcpExtraOptions).then(() => {
  console.info('setExtraOptions success');
}).catch((err: BusinessError) => {
  console.error('setExtraOptions fail');
});

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

Obtains the local socket address of a **TCPSocketServer** connection. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/K_nsFceQR86aEb5L5bKByw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=854A95170D7F3E6962D596EB9DA07D3DDC7A804F381BF580C76819AEF8F95FB4)

This API can be called only after **listen** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr).then(() => {
  tcpServer.getLocalAddress().then((localAddress: socket.NetAddress) => {
    console.info("SUCCESS! Address:" + JSON.stringify(localAddress));
  }).catch((err: BusinessError) => {
    console.error("FerrorAILED! Error:" + JSON.stringify(err));
  })
}).catch((err: BusinessError) => {
  console.error('listen fail');
});

#### \[h2\]on('connect')10+

on(type: 'connect', callback: Callback<TCPSocketConnection>): void

Subscribes to **connect** events of the **TCPSocketServer** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/1TLGrcuyRueeLwzqPg3XUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=299D0FA263D70BC7FC95ADD05BF354C04A1E9249496869F0729BBC9A4A2B520B)

This API can be called only after **listen** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**connect**: connection event.

 |
| callback | Callback<[TCPSocketConnection](#tcpsocketconnection10)\> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
  tcpServer.on('connect', (data: socket.TCPSocketConnection) => {
    console.info(JSON.stringify(data))
  });
})

#### \[h2\]off('connect')10+

off(type: 'connect', callback?: Callback<TCPSocketConnection>): void

Unsubscribes from **connect** events of the **TCPSocketServer** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**connect**: connection event.

 |
| callback | Callback<[TCPSocketConnection](#tcpsocketconnection10)\> | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
  let callback = (data: socket.TCPSocketConnection) => {
    console.info('on connect message: ' + JSON.stringify(data));
  }
  tcpServer.on('connect', callback);
  // You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
  tcpServer.off('connect', callback);
  tcpServer.off('connect');
})

#### \[h2\]on('error')10+

on(type: 'error', callback: ErrorCallback): void

Subscribes to **error** events of the **TCPSocketServer** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/g9BR0dzNQtWs0MWTXAvPbw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4972FC243D3E7C0CCA06029BCABA764A98F456D12741AD5E3584B318EE29B55C)

This API can be called only after **listen** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: error event.

 |
| callback | ErrorCallback | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
  tcpServer.on('error', (err: BusinessError) => {
    console.error("on error, err:" + JSON.stringify(err))
  });
})

#### \[h2\]off('error')10+

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from **error** events of the **TCPSocketServer** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: error event.

 |
| callback | ErrorCallback | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
  let callback = (err: BusinessError) => {
    console.error("on error, err:" + JSON.stringify(err));
  }
  tcpServer.on('error', callback);
  // You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
  tcpServer.off('error', callback);
  tcpServer.off('error');
})

#### \[h2\]close20+

close(): Promise<void>

Stops listening for events of the **TCPSocketServer** object and releases the port bound by [listen](#listen10). If [listen](#listen10) has been called for multiple times, all listening ports of the **TCPSocketServer** object are released when this API is called. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/bClImdG2S-GvqwKNjF5ZlQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DBD6134B67C48EF829BF13BD6B5FBB66BC4CD4C40387935ECE7532A8BC33A839)

This API does not close existing connections. To close connections, call the [close](#close10) API of [TCPSocketConnection](#tcpsocketconnection10).

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.on('connect', (connection: socket.TCPSocketConnection) => {
  console.info("connection clientId: " + connection.clientId);
  // Logical processing
  tcpServer.close(); // Stop event listening.
  connection.close(); // Close the current connection.
});
tcpServer.listen(listenAddr).then(() => {
  console.info('listen success');
}).catch((err: BusinessError) => {
  console.error('listen fail: ' + err.code);
});

#### TCPSocketConnection10+

Defines a **TCPSocketConnection** object, that is, the connection between the TCPSocket client and the server. Before calling TCPSocketConnection APIs, you need to obtain a **TCPSocketConnection** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/u6kV2GOvRyGG5kbqyxq8Qg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7EDE8D8B84247811C88BC018F92DE7EBBF8EDE8234C036EE3489070A793D48F)

The TCPSocket client can call related APIs through the **TCPSocketConnection** object only after a connection is successfully established between the TCPSocket client and the server.

**System capability**: SystemCapability.Communication.NetStack

## Attributes

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| clientId | number | No | No | ID of the connection between the client and TCPSocketServer. |

#### \[h2\]send10+

send(options: TCPSendOptions, callback: AsyncCallback<void>): void

Sends data over a **TCPSocketConnection** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/qJe9GoXJQSOHonC1gxkmFA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE01919274EC765875519EA8C5D8DFC749516B72472DF6B883A188907DDEA579)

This API can be called only after a connection with the client is set up.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TCPSendOptions](#tcpsendoptions) | Yes | Defines the parameters for sending data over a TCP socket connection. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  let tcpSendOption: socket.TCPSendOptions = {
    data: 'Hello, client!'
  }
  client.send(tcpSendOption, () => {
    console.info('send success');
  });
});

#### \[h2\]send10+

send(options: TCPSendOptions): Promise<void>

Sends data over a **TCPSocketConnection** object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/TB-86vd-QYGgmIbViC68BA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF504CD3AC6731182AAFF4F764845A9BD826BB3892B5BF3A774DF203B820A7DF)

This API can be called only after a connection with the client is set up.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TCPSendOptions](#tcpsendoptions) | Yes | Defines the parameters for sending data over a TCP socket connection. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  let tcpSendOption: socket.TCPSendOptions = {
    data: 'Hello, client!'
  }
  client.send(tcpSendOption).then(() => {
    console.info('send success');
  }).catch((err: BusinessError) => {
    console.error('send fail');
  });
});

#### \[h2\]close10+

close(callback: AsyncCallback<void>): void

Closes a TCP socket connection. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.close((err: BusinessError) => {
    if (err) {
      console.error('close fail');
      return;
    }
    console.info('close success');
  });
});

#### \[h2\]close10+

close(): Promise<void>

Closes a TCP socket connection. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.close().then(() => {
    console.info('close success');
  }).catch((err: BusinessError) => {
    console.error('close fail');
  });
});

#### \[h2\]getRemoteAddress10+

getRemoteAddress(callback: AsyncCallback<NetAddress>): void

Obtains the remote address of a socket connection. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/UqAZog2MTjCVjCi7uyJFXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=712B9E8F83210294BE07AB408A93E80986CDAA92848FBFF8C1C0BA0D8BD66320)

This API can be called only after a connection with the client is set up.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[NetAddress](#netaddress)\> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303188 | Socket operation on non-socket. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.getRemoteAddress((err: BusinessError, data: socket.NetAddress) => {
    if (err) {
      console.error('getRemoteAddress fail');
      return;
    }
    console.info('getRemoteAddress success:' + JSON.stringify(data));
  });
});

#### \[h2\]getRemoteAddress10+

getRemoteAddress(): Promise<NetAddress>

Obtains the remote address of a socket connection. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/2-lHBfHRQiasixr3Up-CDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD6DC5B4BD9994A0FFB7250C524E8285A95073E08954C315899FBAD96E2A3EFD)

This API can be called only after a connection with the client is set up.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303188 | Socket operation on non-socket. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.getRemoteAddress().then(() => {
    console.info('getRemoteAddress success');
  }).catch((err: BusinessError) => {
    console.error('getRemoteAddress fail');
  });
});

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

Obtains the local socket address of a **TCPSocketConnection** connection. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address: "192.168.xx.xx",
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
  let netAddress: socket.NetAddress = {
    address: "192.168.xx.xx",
    port: 8080
  }
  let options: socket.TCPConnectOptions = {
    address: netAddress,
    timeout: 6000
  }
  tcp.connect(options, (err: BusinessError) => {
    if (err) {
      console.error('connect fail');
      return;
    }
    console.info('connect success!');
  })
  tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
    client.getLocalAddress().then((localAddress: socket.NetAddress) => {
      console.info("Family IP Port: " + JSON.stringify(localAddress));
    }).catch((err: BusinessError) => {
      console.error('Error:' + JSON.stringify(err));
    });
  })
})

#### \[h2\]on('message')10+

on(type: 'message', callback: Callback<SocketMessageInfo>): void

Subscribes to **message** events of the **TCPSocketConnection** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**message**: message receiving event.

 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.on('message', (value: socket.SocketMessageInfo) => {
    let messageView = '';
    let uint8Array = new Uint8Array(value.message);
    for (let i: number = 0; i < value.message.byteLength; i++) {
      let messages = uint8Array\[i\];
      let message = String.fromCharCode(messages);
      messageView += message;
    }
    console.info('on message message: ' + JSON.stringify(messageView));
    console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
  });
});

#### \[h2\]off('message')10+

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

Unsubscribes from **message** events of the **TCPSocketConnection** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**message**: message receiving event.

 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let callback = (value: socket.SocketMessageInfo) => {
  let messageView = '';
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let uint8Array = new Uint8Array(value.message)
    let messages = uint8Array\[i\]
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
}
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.on('message', callback);
  // You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
  client.off('message', callback);
  client.off('message');
});

#### \[h2\]on('close')10+

on(type: 'close', callback: Callback<void>): void

Subscribes to **close** events of the **TCPSocketConnection** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**close**: close event.

 |
| callback | Callback<void> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.on('close', () => {
    console.info("on close success")
  });
});

#### \[h2\]off('close')10+

off(type: 'close', callback?: Callback<void>): void

Unsubscribes from **close** events of the **TCPSocketConnection** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**close**: close event.

 |
| callback | Callback<void> | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let callback = () => {
  console.info("on close success");
}
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.on('close', callback);
  // You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
  client.off('close', callback);
  client.off('close');
});

#### \[h2\]on('error')10+

on(type: 'error', callback: ErrorCallback): void

Subscribes to **error** events of the **TCPSocketConnection** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: error event.

 |
| callback | ErrorCallback | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.on('error', (err: BusinessError) => {
    console.error("on error, err:" + JSON.stringify(err))
  });
});

#### \[h2\]off('error')10+

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from **error** events of the **TCPSocketConnection** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: error event.

 |
| callback | ErrorCallback | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let callback = (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err));
}
let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.on('error', callback);
  // You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
  client.off('error', callback);
  client.off('error');
});

#### Description of TCP Error Codes

The TCP error code mapping is in the format of 2301000 + Linux kernel error code.

For details about error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md).

#### socket.constructLocalSocketInstance11+

constructLocalSocketInstance(): LocalSocket

Creates a **LocalSocket** object.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| [LocalSocket](#localsocket11) | **LocalSocket** object. |

**Example**

import { socket } from '@kit.NetworkKit';
let client: socket.LocalSocket = socket.constructLocalSocketInstance();

#### LocalSocket11+

Defines a **LocalSocket** object. Before calling LocalSocket APIs, you need to call [socket.constructLocalSocketInstance](#socketconstructlocalsocketinstance11) to create a **LocalSocket** object.

#### \[h2\]bind11+

bind(address: LocalAddress): Promise<void>;

Binds the address of a local socket file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/7HE-LHNQTG2wZ34fMpLbNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8BD2CF9E2097CCDC769E0CAEFCECF93F318D5B0ECF464CCFC0085CA024D32129)

This API explicitly binds the client to a local socket file based on the specified address.

It is not mandatory in local socket communication.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| address | [LocalAddress](#localaddress11) | Yes | Local address. For details, see [LocalAddress](#localaddress11). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2301013 | Insufficient permissions. |
| 2301022 | Invalid argument. |
| 2301098 | Address already in use. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/5FOE8HFPTbO2URH2q7_MMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65130918676C0E11E752C6AA4631AD6ABC5D2387AEFC7053A31C14153BDF3D94)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance()
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let address : socket.LocalAddress = {
  address: sandboxPath
}
client.bind(address).then(() => {
  console.info('bind success')
}).catch((err: Object) => {
  console.error('failed to bind: ' + JSON.stringify(err))
})

#### \[h2\]connect11+

connect(options: LocalConnectOptions): Promise<void>

Connects to the specified socket file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/CO6KQupTTfybFIrKgNrSUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FEDC704FA1AE632B9115DA37FE08DE8B5D457ED833017001C6573C6139C691D9)

This API allows you to connect to the TCP server without first executing **localsocket.bind**.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [LocalConnectOptions](#localconnectoptions11) | Yes | Local socket connection parameters. For details, see [LocalConnectOptions](#localconnectoptions11). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2301013 | Insufficient permissions. |
| 2301022 | Invalid argument. |
| 2301111 | Connection refused. |
| 2301099 | Cannot assign requested address. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/f-AgH8yfTcuzzCHruqeVAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F519B5E0B9D2F8338AE27E82510DA6361C0A076B76EA76DFBE55DB65D62022DC)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddress : socket.LocalAddress = {
  address: sandboxPath
}
let connectOpt: socket.LocalConnectOptions = {
  address: localAddress,
  timeout: 6000
}
client.connect(connectOpt).then(() => {
  console.info('connect success')
}).catch((err: Object) => {
  console.error('connect fail: ' + JSON.stringify(err));
});

#### \[h2\]send11+

send(options: LocalSendOptions): Promise<void>

Sends data over a local socket connection. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/yLbPX4a1RfuqW27HB4pZoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FFCA58F08A065EC14EC715BAC222F83DB7FBF5E097CEE8FF8C1E22A1FDFE65C4)

This API can be called only after **connect** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [LocalSendOptions](#localsendoptions11) | Yes | Parameters for sending data over a local socket connection. For details, see [LocalSendOptions](#localsendoptions11). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2301011 | Operation would block. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/mCnsXuhsSs2b2kr-pOI1Vg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1EFE542C6C0F86E96793A705ED9A26E4909208066FB8FB5F5159F65FE5DF7E5)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance()
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddress : socket.LocalAddress = {
  address: sandboxPath
}
let connectOpt: socket.LocalConnectOptions = {
  address: localAddress,
  timeout: 6000
}
client.connect(connectOpt).then(() => {
  console.info('connect success')
}).catch((err: Object) => {
  console.error('connect failed: ' + JSON.stringify(err))
})
let sendOpt: socket.LocalSendOptions = {
  data: 'Hello world!'
}
client.send(sendOpt).then(() => {
  console.info('send success')
}).catch((err: Object) => {
  console.error('send fail: ' + JSON.stringify(err))
})

#### \[h2\]close11+

close(): Promise<void>

Closes a local socket connection. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 2301009 | Bad file descriptor. |

**Example**

import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();

client.close().then(() => {
  console.info('close success');
}).catch((err: Object) => {
  console.error('close fail: ' + JSON.stringify(err));
});

#### \[h2\]getState11+

getState(): Promise<SocketStateBase>

Obtains the local socket connection status. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/KVtBtoAFQJqTS9_fb-I1Jg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06FF98022B3AF8A194938F02EE51FA4CF87BF9B4645778FF30264A8EA911E01C)

This API can be called only after **bind** or **connect** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SocketStateBase](#socketstatebase)\> | Promise used to return the result. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/hJ6dbq09QpqyX-4mMu2Sog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=224165C7D3547D82F5F607090496C9AEF7DDAFBA7D78DB16E6BF46D705305B00)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddress : socket.LocalAddress = {
  address: sandboxPath
}
let connectOpt: socket.LocalConnectOptions = {
  address: localAddress,
  timeout: 6000
}
client.connect(connectOpt).then(() => {
  console.info('connect success');
  client.getState().then(() => {
    console.info('getState success');
  }).catch((err: Object) => {
    console.error('getState fail: ' + JSON.stringify(err))
  });
}).catch((err: Object) => {
  console.error('connect fail: ' + JSON.stringify(err));
});

#### \[h2\]getSocketFd11+

getSocketFd(): Promise<number>

Obtains the file descriptor of the **LocalSocket** object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/TmnA-Z9MRte78rrAw1QLFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40FB2DBDA40216607C6CD2B7CC35B5573D53A7EEAC8FBDDCCDD9A84BB4B88105)

This API can be called only after **bind** or **connect** is successfully called.

The file descriptor is allocated by the system kernel to uniquely identify the local socket in use.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/pCeHW3BMTzmAWxlzDgaHUA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=873C548BB902F7EB7E1C41DB027607142ED589D4411FAB13F7C7712CCE78F360)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddress : socket.LocalAddress = {
  address: sandboxPath
}
let connectOpt: socket.LocalConnectOptions = {
  address: localAddress,
  timeout: 6000
}
client.connect(connectOpt).then(() => {
  console.info('connect ok')
}).catch((err: Object) => {
  console.error('connect fail: ' + JSON.stringify(err))
})
client.getSocketFd().then((data: number) => {
  console.info("fd: " + data);
}).catch((err: Object) => {
  console.error("getSocketFd failed: " + JSON.stringify(err));
})

#### \[h2\]setExtraOptions11+

setExtraOptions(options: ExtraOptionsBase): Promise<void>

Sets the properties of the **LocalSocket** object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/QANR3pL9SQupmcs_0rTbjg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5FF09667D3E7CD1982FD9567219A4B02983CEF808775B23A83E7C0C551F7E077)

This API can be called only after **bind** or **connect** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ExtraOptionsBase](#extraoptionsbase) | Yes | Other properties of the LocalSocket connection. For details, see [ExtraOptionsBase](#extraoptionsbase). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2301009 | Bad file descriptor. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/-J9vv5X1RpC-nTBTGiFU6A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F15F8363EFFB10C29556AD8FCFC90784276D4840EF40904C184242EE55ABA42A)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddress : socket.LocalAddress = {
  address: sandboxPath
}
let connectOpt: socket.LocalConnectOptions = {
  address: localAddress,
  timeout: 6000
}
client.connect(connectOpt).then(() => {
  console.info('connect success');
  let options: socket.ExtraOptionsBase = {
    receiveBufferSize: 8192,
    sendBufferSize: 8192,
    socketTimeout: 3000
  }
  client.setExtraOptions(options).then(() => {
    console.info('setExtraOptions success');
  }).catch((err: Object) => {
    console.error('setExtraOptions fail: ' + JSON.stringify(err));
  });
}).catch((err: Object) => {
  console.error('connect fail: ' + JSON.stringify(err));
});

#### \[h2\]getExtraOptions11+

getExtraOptions(): Promise<ExtraOptionsBase>;

Obtains the socket properties of the **LocalSocket** object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/Rk_wNDdITWeZBo5jrACBAg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD8FC99A56A2C9439486976B1DECCDFCAD649C091B308E838440F183C4FD724D)

This API can be called only after **bind** or **connect** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ExtraOptionsBase](#extraoptionsbase)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 2301009 | Bad file descriptor. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/yw-QANybSDW2Zz41MGXKxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B194714E8C3AE35DB3FC1268110F9ACFD7DF4D1CF8D7BD9AC43D947792A59F89)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddress : socket.LocalAddress = {
  address: sandboxPath
}
let connectOpt: socket.LocalConnectOptions = {
  address: localAddress,
  timeout: 6000
}
client.connect(connectOpt).then(() => {
  console.info('connect success');
  client.getExtraOptions().then((options : socket.ExtraOptionsBase) => {
    console.info('options: ' + JSON.stringify(options));
  }).catch((err: Object) => {
    console.error('setExtraOptions fail: ' + JSON.stringify(err));
  });
}).catch((err: Object) => {
  console.error('connect fail: ' + JSON.stringify(err));
});

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<string>

Obtains the local socket address of a **LocalSocket** connection. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/3vTetOhfQJynqG6dLP0X_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77AF8CD643FF5C15B8BB5EADCEA5C1517F767311341D1CB3EBEF2EAC984D4257)

This API can be called only after **bind** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/2i9dpDvrRjmICcJhuO7GMg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8AA1B7DC76AA6F68D5194017E4AB6E1A98D1CB83B8ABB5EEB9D14FBEA98A8A8D)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { common } from '@kit.AbilityKit';
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let address : socket.LocalAddress = {
  address: sandboxPath
}
client.bind(address).then(() => {
  console.error('bind success');
  client.getLocalAddress().then((localPath: string) => {
    console.info("SUCCESS " + JSON.stringify(localPath));
  }).catch((err: BusinessError) => {
    console.error("FAIL " + JSON.stringify(err));
  })
}).catch((err: Object) => {
  console.error('failed to bind: ' + JSON.stringify(err));
})

#### \[h2\]on('message')11+

on(type: 'message', callback: Callback<LocalSocketMessageInfo>): void

Subscribes to **message** events of the **LocalSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**message**: message receiving event.

 |
| callback | Callback<[LocalSocketMessageInfo](#localsocketmessageinfo11)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
client.on('message', (value: socket.LocalSocketMessageInfo) => {
  const uintArray = new Uint8Array(value.message)
  let messageView = '';
  for (let i = 0; i < uintArray.length; i++) {
    messageView += String.fromCharCode(uintArray\[i\]);
  }
  console.info('total: ' + JSON.stringify(value));
  console.info('message information: ' + messageView);
});

#### \[h2\]off('message')11+

off(type: 'message', callback?: Callback<LocalSocketMessageInfo>): void

Unsubscribes from **message** events of the **LocalSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**message**: message receiving event.

 |
| callback | Callback<[LocalSocketMessageInfo](#localsocketmessageinfo11)\> | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let messageView = '';
let callback = (value: socket.LocalSocketMessageInfo) => {
  const uintArray = new Uint8Array(value.message)
  let messageView = '';
  for (let i = 0; i < uintArray.length; i++) {
    messageView += String.fromCharCode(uintArray\[i\]);
  }
  console.info('total: ' + JSON.stringify(value));
  console.info('message information: ' + messageView);
}
client.on('message', callback);
client.off('message');

#### \[h2\]on('connect')11+

on(type: 'connect', callback: Callback<void>): void

Subscribes to **connect** events of the **LocalSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

 |
| callback | Callback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
client.on('connect', () => {
  console.info("on connect success")
});

#### \[h2\]off('connect')11+

off(type: 'connect', callback?: Callback<void>): void

Unsubscribes from **connect** events of the **LocalSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

'connect': connection event.

 |
| callback | Callback<void> | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let callback = () => {
  console.info("on connect success");
}
client.on('connect', callback);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
client.off('connect', callback);
client.off('connect');

#### \[h2\]on('close')11+

on(type: 'close', callback: Callback<void>): void

Subscribes to **close** events of the **LocalSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. |
| callback | Callback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let callback = () => {
  console.info("on close success");
}
client.on('close', callback);

#### \[h2\]off('close')11+

off(type: 'close', callback?: Callback<void>): void

Unsubscribes from **close** events of the **LocalSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**close**: close event.

 |
| callback | Callback<void> | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let callback = () => {
  console.info("on close success");
}
client.on('close', callback);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
client.off('close', callback);
client.off('close');

#### \[h2\]on('error')11+

on(type: 'error', callback: ErrorCallback): void

Subscribes to **error** events of the **LocalSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. |
| callback | ErrorCallback | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
client.on('error', (err: Object) => {
  console.error("on error, err:" + JSON.stringify(err))
});

#### \[h2\]off('error')11+

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from **error** events of the **LocalSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

'error': error event.

 |
| callback | ErrorCallback | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let callback = (err: Object) => {
  console.error("on error, err:" + JSON.stringify(err));
}
client.on('error', callback);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
client.off('error', callback);
client.off('error');

#### LocalSocketMessageInfo11+

Defines the data received by the client over a local socket connection.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| message | ArrayBuffer | No | No | Data received. |
| address | string | No | No | Local socket connection address. |
| size | number | No | No | Data length. |

#### LocalAddress11+

Defines the address of a local socket file. When the address is passed for binding, a socket file is created at this address.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| address | string | No | No | Address of the local socket file. |

#### LocalConnectOptions11+

Defines local socket connection parameters.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| address | [LocalAddress](#localaddress11) | No | No | Address of the local socket file. |
| timeout | number | No | Yes | Timeout duration of the local socket connection, in ms. **Default value**: 0 You need to manually set this parameter for your application. The recommended value is **5000**. |

#### LocalSendOptions11+

Defines the request parameters for the **LocalSocket** object.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| data | string | ArrayBuffer | No | No | Data to be transmitted. |
| encoding | string | No | Yes | Encoding format of the string. |

#### ExtraOptionsBase

Defines base properties of the **LocalSocket** object.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| receiveBufferSize | number | No | Yes | Size of the RX buffer, in bytes. The value ranges from 0 to 262144. If this parameter is left unspecified or the unspecified value exceeds the value range, the default value **8192** is used. |
| sendBufferSize | number | No | Yes | Size of the TX buffer, in bytes. The value ranges from 0 to 262144. If this parameter is left unspecified or the unspecified value exceeds the value range, the default value **8192** is used. |
| reuseAddress | boolean | No | Yes | Whether to reuse addresses. The value **true** means to reuse addresses, and the value **false** means the opposite. |
| socketTimeout | number | No | Yes | Timeout duration of the local socket connection, in ms. |

#### socket.constructLocalSocketServerInstance11+

constructLocalSocketServerInstance(): LocalSocketServer

Creates a **LocalSocketServer** object.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| [LocalSocketServer](#localsocketserver11) | **LocalSocketServer** object. |

**Example**

import { socket } from '@kit.NetworkKit';
let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();

#### LocalSocketServer11+

Defines a local socket server connection. Before calling LocalSocketServer APIs, you need to call [socket.constructLocalSocketServerInstance](#socketconstructlocalsocketserverinstance11) to create a **LocalSocketServer** object.

#### \[h2\]listen11+

listen(address: LocalAddress): Promise<void>

Binds the address of the local socket file. The server listens to and accepts local socket connections established over the socket. Multiple threads are used to process client data concurrently. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/zJH9mw8CQBaDlBUntSNdWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F84E2B48D281E0B3545F9CC650DBEBF94EA3ECB1D91C82CB0E2EC0C0B83A82E5)

The server uses this API to complete the **bind**, **listen**, and **accept** operations. If the address of the local socket file is passed for binding, a socket file is automatically created when this API is called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| address | [LocalAddress](#localaddress11) | Yes | Destination address. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the operation is successful, no value is returned. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303109 | Bad file number. |
| 2301013 | Insufficient permissions. |
| 2301022 | Invalid argument. |
| 2301098 | Address already in use. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/uGUhFIPBRsGuwhyUXxU8WA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CD44639E955D25BE2A618CEA68F669649A49C86D24D78CD9DAF06191CAE279D)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let addr: socket.LocalAddress = {
  address: sandboxPath
}
server.listen(addr).then(() => {
  console.info('listen success');
}).catch((err: Object) => {
  console.error('listen fail: ' + JSON.stringify(err));
});

#### \[h2\]getState11+

getState(): Promise<SocketStateBase>

Obtains the status of a local socket server connection. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/MHy3vL4ZT9KHgim48SzB1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84346CAB1A21383000D77700D4806F72BE62390B8E3A978C0E5F4C025803C7AF)

This API can be called only after **listen** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SocketStateBase](#socketstatebase)\> | Promise used to return the result. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/_owSiTlHQv6W3Hy0Vmtl3A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF8114251EB85DB09C4BB1FF619A4792922ED2D16E1FE2D655826A82D6A6FC44)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let listenAddr: socket.LocalAddress = {
  address: sandboxPath
}
server.listen(listenAddr).then(() => {
  console.info("listen success");
}).catch((err: Object) => {
  console.error("listen fail: " + JSON.stringify(err));
})
server.getState().then((data: socket.SocketStateBase) => {
  console.info('getState success: ' + JSON.stringify(data));
}).catch((err: Object) => {
  console.error('getState fail: ' + JSON.stringify(err));
});

#### \[h2\]setExtraOptions11+

setExtraOptions(options: ExtraOptionsBase): Promise<void>

Sets the socket properties of the **LocalSocketServer** object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/dLZlVHPvSV6CAsHuNkh6Mw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB140F618D28F8E9BBCEC40C879C7EDD84910601191D351FCC328DF661220B6F)

This API can be called only after **listen** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ExtraOptionsBase](#extraoptionsbase) | Yes | Other properties of the **LocalSocketServer** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2301009 | Bad file descriptor. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/o6p_2KBJTaiexhEHdYLnIA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A59107A228C30C41709A296369B85DBDE47715FD4F43F3D54CC98C030B562B0)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let listenAddr: socket.NetAddress = {
  address: sandboxPath
}
server.listen(listenAddr).then(() => {
  console.info("listen success");
}).catch((err: Object) => {
  console.error("listen fail: " + JSON.stringify(err));
})

let options: socket.ExtraOptionsBase = {
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  socketTimeout: 3000
}
server.setExtraOptions(options).then(() => {
  console.info('setExtraOptions success');
}).catch((err: Object) => {
  console.error('setExtraOptions fail: ' + JSON.stringify(err));
});

#### \[h2\]getExtraOptions11+

getExtraOptions(): Promise<ExtraOptionsBase>;

Obtains the socket properties of the **LocalSocketServer** object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/4gnow080RF21LYsnrh88YQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3AECBD19E56B596EBCBBD8721077A7017CE4A0922924DF2490D012B4FDADBB34)

This API can be called only after **listen** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ExtraOptionsBase](#extraoptionsbase)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/05FufdPxQJGyELbUn9tC1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20D1B4C66A8C862E60BFC692E7F4A27A022DAB946682A59B353C995A6D5010D8)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let listenAddr: socket.LocalAddress = {
  address: sandboxPath
}
server.listen(listenAddr).then(() => {
  console.info("listen success");
}).catch((err: Object) => {
  console.error("listen fail: " + JSON.stringify(err));
})
server.getExtraOptions().then((options: socket.ExtraOptionsBase) => {
  console.info('options: ' + JSON.stringify(options));
}).catch((err: Object) => {
  console.error('getExtraOptions fail: ' + JSON.stringify(err));
});

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<string>

Obtains the local socket address of a **LocalSocketServer** connection. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/C85HWW5HSmSkyhXphluo9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27D1EC2177BEB7DF6F0CBBE87155A6A9DAEBF4B595E2B671E662B8BF88162135)

This API can be called only after **listen** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/9fBgy7i7RTufCUazXZytfg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9AF2A392E60E0F0AE845350B6FDB36A374B7AE7B02C1BC030E051B3303EC2398)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { common } from '@kit.AbilityKit';
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let listenAddr: socket.LocalAddress = {
  address: sandboxPath
}
server.listen(listenAddr).then(() => {
  console.info("listen success");
  server.getLocalAddress().then((localPath: string) => {
    console.info("SUCCESS " + JSON.stringify(localPath));
  }).catch((err: BusinessError) => {
    console.error("FAIL " + JSON.stringify(err));
  })
}).catch((err: Object) => {
  console.error("listen fail: " + JSON.stringify(err));
})

#### \[h2\]on('connect')11+

on(type: 'connect', callback: Callback<LocalSocketConnection>): void

Subscribes to **connect** events of the **LocalSocketServer** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/hSYvTLZIS6C0NLWgi2raRw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D15B135597141CA1FCC466A6ADBC6369CD00657156F85E2323469B70864FE77E)

This API can be called only after **listen** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**connect**: connection event.

 |
| callback | Callback<[LocalSocketConnection](#localsocketconnection11)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
server.on('connect', (connection: socket.LocalSocketConnection) => {
  if (connection) {
    console.info('accept a client')
  }
});

#### \[h2\]off('connect')11+

off(type: 'connect', callback?: Callback<LocalSocketConnection>): void

Unsubscribes from **connect** events of the **LocalSocketServer** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

'connect': connection event.

 |
| callback | Callback<[LocalSocketConnection](#localsocketconnection11)\> | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let callback = (connection: socket.LocalSocketConnection) => {
  if (connection) {
    console.info('accept a client')
  }
}
server.on('connect', callback);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
server.off('connect', callback);
server.off('connect');

#### \[h2\]on('error')11+

on(type: 'error', callback: ErrorCallback): void

Subscribes to **error** events of the **LocalSocketServer** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/4mzvTJ5TTziDNUXQNQORVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F1996C40774618485331C3F005EF527D149CAA0833BF8A1592F90336B4A36C55)

This API can be called only after **listen** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: error event.

 |
| callback | ErrorCallback | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
server.on('error', (err: Object) => {
  console.error("on error, err:" + JSON.stringify(err))
});

#### \[h2\]off('error')11+

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from **error** events of the **LocalSocketServer** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: error event.

 |
| callback | ErrorCallback | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let callback = (err: Object) => {
  console.error("on error, err:" + JSON.stringify(err));
}
server.on('error', callback);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
server.off('error', callback);
server.off('error');

#### \[h2\]close20+

close(): Promise<void>

Stops listening for events of the **LocalSocketServer** object and releases the port bound by [listen](#listen11). This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/fR4q7Qt0Sua2s8erPK2ybw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DB583A5B621DD216419D25A67C17734066D986DD9BD7F8393C126C54D529C89)

This API does not close existing connections. To close the connection, call the \[close\] (#close11-1) API of \[LocalSocketConnection\] (#localsocketconnection11).

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 2300002 | System internal error. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/M6vB1aReQSOb-CfL0_TpkQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E15457FBD4A2DCE0462E2BE3CEAD61D645A60A5BA6C45F114410008F8AD9D51C)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localserver: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let addr: socket.LocalAddress = {
  address: sandboxPath
}
localserver.on('connect', (connection: socket.LocalSocketConnection) => {
  console.info("connection clientId: " + connection.clientId);
  // Logical processing
  localserver.close(); // Stop event listening.
  connection.close(); // Close the current connection.
});
localserver.listen(addr).then(() => {
  console.info('listen success');
}).catch((err: BusinessError) => {
  console.error('listen fail: ' + err.code);
});

#### LocalSocketConnection11+

Defines a local socket connection, that is, the session between the local socket client and the server. Before calling LocalSocketConnection APIs, you need to obtain a **LocalSocketConnection** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/7mHGpbd0T82szoSrfiVU9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=547230034321116C1793552155BEEFDA56DF6D06DDBE050630E830076DE0AE19)

The LocalSocketConnection client can call related APIs through the **LocalSocketConnection** object only after a connection is successfully established between the local socket client and the server.

**System capability**: SystemCapability.Communication.NetStack

## Attributes

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| clientId | number | No | No | ID of the session between the client and the server. |

#### \[h2\]send11+

send(options: LocalSendOptions): Promise<void>

Sends data through a local socket connection. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/xcR5sDpOTJeqUk-Rukg6fQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A346B7DF5513B94BCA903627C91C2DCC65A60F72050DB245B51EAA964C5AE4C)

This API can be used only after the server obtains a **LocalSocketConnection** object through the **callback** of the **connect** event.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [LocalSendOptions](#localsendoptions11) | Yes | Defines the parameters for sending data over a local socket connection. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2301011 | Operation would block. |

**Example**

import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();

server.on('connect', (connection: socket.LocalSocketConnection) => {
  let sendOptions: socket.LocalSendOptions = {
    data: 'Hello, client!'
  }
  connection.send(sendOptions).then(() => {
    console.info('send success');
  }).catch((err: Object) => {
    console.error('send fail: ' + JSON.stringify(err));
  });
});

#### \[h2\]close11+

close(): Promise<void>

Closes a local socket connection. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 2301009 | Bad file descriptor. |

**Example**

import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.close().then(() => {
    console.info('close success');
  }).catch((err: Object) => {
    console.error('close fail: ' + JSON.stringify(err));
  });
});

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<string>

Obtains the local socket address of a **LocalSocketConnection** connection. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/P0sKtv4TT6aAjqR18r44eg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=947D6D4DBC7690BBF8746980A5F72435F43535D8B996F61C3BE8B713ABBEB78C)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { common } from '@kit.AbilityKit';
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddr: socket.LocalAddress = {
  address: sandboxPath
}
server.listen(localAddr).then(() => {
  console.info('listen success');
  let client: socket.LocalSocket = socket.constructLocalSocketInstance();
  let connectOpt: socket.LocalConnectOptions = {
    address: localAddr,
    timeout: 6000
  }
  client.connect(connectOpt).then(() => {
    server.getLocalAddress().then((localPath: string) => {
      console.info("success, localPath is" + JSON.stringify(localPath));
    }).catch((err: BusinessError) => {
      console.error("FAIL " + JSON.stringify(err));
    })
  }).catch((err: Object) => {
    console.error('connect fail: ' + JSON.stringify(err));
  });
});

#### \[h2\]on('message')11+

on(type: 'message', callback: Callback<LocalSocketMessageInfo>): void

Subscribes to **message** events of the **LocalSocketConnection** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**message**: message receiving event.

 |
| callback | Callback<[LocalSocketMessageInfo](#localsocketmessageinfo11)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/Hnu_KEslSwGfxxn0OGYr-Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56E5F1F49A097D2E007901E9DA8460D95A5014BBBFE3EB61C331236A46B65C81)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let listenAddr: socket.LocalAddress = {
  address: sandboxPath
}
server.listen(listenAddr).then(() => {
  console.info("listen success");
}).catch((err: Object) => {
  console.error("listen fail: " + JSON.stringify(err));
});
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.on('message', (value: socket.LocalSocketMessageInfo) => {
    const uintArray = new Uint8Array(value.message);
    let messageView = '';
    for (let i = 0; i < uintArray.length; i++) {
      messageView += String.fromCharCode(uintArray\[i\]);
    }
    console.info('total: ' + JSON.stringify(value));
    console.info('message information: ' + messageView);
  });
});

#### \[h2\]off('message')11+

off(type: 'message', callback?: Callback<LocalSocketMessageInfo>): void

Unsubscribes from **message** events of the **LocalSocketConnection** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**message**: message receiving event.

 |
| callback | Callback<[LocalSocketMessageInfo](#localsocketmessageinfo11)\> | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let callback = (value: socket.LocalSocketMessageInfo) => {
  const uintArray = new Uint8Array(value.message)
  let messageView = '';
  for (let i = 0; i < uintArray.length; i++) {
    messageView += String.fromCharCode(uintArray\[i\]);
  }
  console.info('total: ' + JSON.stringify(value));
  console.info('message information: ' + messageView);
}
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.on('message', callback);
  // You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
  connection.off('message', callback);
  connection.off('message');
});

#### \[h2\]on('close')11+

on(type: 'close', callback: Callback<void>): void

Unsubscribes from **close** events of the **LocalSocketConnection** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**close**: close event.

 |
| callback | Callback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.on('close', () => {
    console.info("on close success")
  });
});

#### \[h2\]off('close')11+

off(type: 'close', callback?: Callback<void>): void

Unsubscribes from **close** events of the **LocalSocketConnection** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**close**: close event.

 |
| callback | Callback<void> | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let callback = () => {
  console.info("on close success");
}
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.on('close', callback);
  // You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
  connection.off('close', callback);
  connection.off('close');
});

#### \[h2\]on('error')11+

on(type: 'error', callback: ErrorCallback): void

Subscribes to **error** events of the **LocalSocketConnection** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: error event.

 |
| callback | ErrorCallback | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.on('error', (err: Object) => {
    console.error("on error, err:" + JSON.stringify(err))
  });
});

#### \[h2\]off('error')11+

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from **error** events of the **LocalSocketConnection** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: error event.

 |
| callback | ErrorCallback | No | Callback used to return the result. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';

let callback = (err: Object) => {
  console.error("on error, err: " + JSON.stringify(err));
}
let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.on('error', callback);
  // You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
  connection.off('error', callback);
  connection.off('error');
});

#### Description of LocalSocket Error Codes

The LocalSocket error code mapping is in the format of 2301000 + Linux kernel error code.

For details about error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md).

#### socket.constructTLSSocketInstance9+

constructTLSSocketInstance(): TLSSocket

Creates a **TLSSocket** object.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| [TLSSocket](#tlssocket9) | **TLSSocket** object. |

**Example**

import { socket } from '@kit.NetworkKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();

#### socket.constructTLSSocketInstance12+

constructTLSSocketInstance(tcpSocket: TCPSocket): TLSSocket

Upgrades a **TCPSocket** connection to a **TLSSocket** connection.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/u-42eZIaT82YstY0-kDevQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4368DE60AFC973C2BE6BC4DF8752CFD5F9772C719E5BDEC4AF78CA88A09F756D)

Before calling **constructTLSSocketInstance**, ensure that a **TCPSocket** connection has been established and no data is transmitted. After a successful upgrade, you do not need to call the **close** API for the **TCPSocket** object.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tcpSocket | [TCPSocket](#tcpsocket) | Yes | **TCPSocket** connection to be upgraded. |

**Return value**

| Type | Description |
| :-- | :-- |
| [TLSSocket](#tlssocket9) | **TLSSocket** object. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2300002 | System internal error. |
| 2303601 | Invalid socket FD. |
| 2303602 | Socket is not connected. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}

tcp.connect(tcpconnectoptions, (err: BusinessError) => {
  if (err) {
    console.error('connect fail');
    return;
  }
  console.info('connect success');

  // Ensure that a TCPSocket connection has been established before upgrading it to a TLSSocket connection.
  let tls: socket.TLSSocket = socket.constructTLSSocketInstance(tcp);
})

#### TLSSocket9+

Defines a TLS socket connection. Before calling TLSSocket APIs, you need to call [socket.constructTLSSocketInstance](#socketconstructtlssocketinstance9) to create a **TLSSocket** object.

#### \[h2\]bind9+

bind(address: NetAddress, callback: AsyncCallback<void>): void

Binds the IP address and port number. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/sq64Z5QQTQ-KtZeo37egsg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88445E00557BA5AF0E11E3F8460746AAB26B0B1A5B6E184CD97002154876CBF8)

If the **TLSSocket** object is upgraded from a **TCPSocket** object, you do not need to execute the **bind** API.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | Yes | Local address. For details, see [NetAddress](#netaddress). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, the result of binding the local IP address and port number is returned. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2303198 | Address already in use. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});

#### \[h2\]bind9+

bind(address: NetAddress): Promise<void>

Binds the IP address and port number. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/W5o3VT-9RQ-KCG6pexb9Mg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=480EC4C940D112AF7C1509438B68B4294D11E77EF6738122A97E2427497836C1)

If the **TLSSocket** object is upgraded from a **TCPSocket** object, you do not need to execute the **bind** API.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | Yes | Local address. For details, see [NetAddress](#netaddress). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2303198 | Address already in use. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr).then(() => {
  console.info('bind success');
}).catch((err: BusinessError) => {
  console.error('bind fail');
});

#### \[h2\]getState9+

getState(callback: AsyncCallback<SocketStateBase>): void

Obtains the status of the TLS socket connection. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[SocketStateBase](#socketstatebase)\> | Yes | Callback used to return the result. If the operation is successful, the status of the TLS socket connection is returned. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
tls.getState((err: BusinessError, data: socket.SocketStateBase) => {
  if (err) {
    console.error('getState fail');
    return;
  }
  console.info('getState success:' + JSON.stringify(data));
});

#### \[h2\]getState9+

getState(): Promise<SocketStateBase>

Obtains the status of the TLS socket connection. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SocketStateBase](#socketstatebase)\> | Promise used to return the result. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
tls.getState().then(() => {
  console.info('getState success');
}).catch((err: BusinessError) => {
  console.error('getState fail');
});

#### \[h2\]setExtraOptions9+

setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void

Sets other properties of the **TCPSocket** object after **bind** is successfully called. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TCPExtraOptions](#tcpextraoptions) | Yes | Other properties of the **TCPSocket** object. For details, see [TCPExtraOptions](#tcpextraoptions). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, the result of setting other properties of the **TCPSocket** object is returned. If the operation fails, an error message is returned. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});

interface SocketLinger {
  on: boolean;
  linger: number;
}

let tcpExtraOptions: socket.TCPExtraOptions = {
  keepAlive: true,
  OOBInline: true,
  TCPNoDelay: true,
  socketLinger: { on: true, linger: 10 } as SocketLinger,
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  reuseAddress: true,
  socketTimeout: 3000
}
tls.setExtraOptions(tcpExtraOptions, (err: BusinessError) => {
  if (err) {
    console.error('setExtraOptions fail');
    return;
  }
  console.info('setExtraOptions success');
});

#### \[h2\]setExtraOptions9+

setExtraOptions(options: TCPExtraOptions): Promise<void>

Sets other properties of the **TCPSocket** object after **bind** is successfully called. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TCPExtraOptions](#tcpextraoptions) | Yes | Other properties of the **TCPSocket** object. For details, see [TCPExtraOptions](#tcpextraoptions). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});

interface SocketLinger {
  on: boolean;
  linger: number;
}

let tcpExtraOptions: socket.TCPExtraOptions = {
  keepAlive: true,
  OOBInline: true,
  TCPNoDelay: true,
  socketLinger: { on: true, linger: 10 } as SocketLinger,
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  reuseAddress: true,
  socketTimeout: 3000
}
tls.setExtraOptions(tcpExtraOptions).then(() => {
  console.info('setExtraOptions success');
}).catch((err: BusinessError) => {
  console.error('setExtraOptions fail');
});

#### \[h2\]on('message')9+

on(type: 'message', callback: Callback<SocketMessageInfo>): void

Subscribes to **message** events of the **TLSSocket** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/XSZy8iVcQ0aSykgVWQguGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC3F0B48BC963193BA3958A0EEC231F4FE9D47A535B124B3CBE56C3ADB373D94)

This API can be called only after **bind** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**message**: message receiving event.

 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
  tls.on('message', (value: socket.SocketMessageInfo) => {
    let messageView = '';
    let uint8Array = new Uint8Array(value.message);
    for (let i: number = 0; i < value.message.byteLength; i++) {
      let messages = uint8Array\[i\];
      let message = String.fromCharCode(messages);
      messageView += message;
    }
    console.info('on message message: ' + JSON.stringify(messageView));
    console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
  });
});

#### \[h2\]off('message')9+

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

Unsubscribes from **message** events of the **TLSSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**message**: message receiving event.

 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | No | Callback used to return the result. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let messageView = '';
let callback = (value: socket.SocketMessageInfo) => {
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let uint8Array = new Uint8Array(value.message)
    let messages = uint8Array\[i\]
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
}
tls.on('message', callback);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
tls.off('message', callback);

#### \[h2\]on('connect' | 'close')9+

on(type: 'connect' | 'close', callback: Callback<void>): void

Subscribes to **connect** or **close** events of the **TLSSocket** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/9KIyKIUxRO-SaINWvnLWXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D635C9AEE96038CA96DA459C96D3C5E1A426DD02D7C38AC3B6E7F56BCFF80467)

This API can be called only after **bind** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- **connect**: connection event.

\- **close**: close event.

 |
| callback | Callback<void> | Yes | Callback used to return the result. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
  tls.on('connect', () => {
    console.info("on connect success")
  });
  tls.on('close', () => {
    console.info("on close success")
  });
});

#### \[h2\]off('connect' | 'close')9+

off(type: 'connect' | 'close', callback?: Callback<void>): void

Unsubscribes from **connect** or **close** events of the **TLSSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- **connect**: connection event.

\- **close**: close event.

 |
| callback | Callback<void> | No | Callback used to return the result. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let callback1 = () => {
  console.info("on connect success");
}
tls.on('connect', callback1);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
tls.off('connect', callback1);
tls.off('connect');
let callback2 = () => {
  console.info("on close success");
}
tls.on('close', callback2);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
tls.off('close', callback2);

#### \[h2\]on('error')9+

on(type: 'error', callback: ErrorCallback): void

Subscribes to **error** events of the **TLSSocket** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/u0REz_dMTrSPd5IR5jNM6A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E8B3A301EA50D6AB57655354792AD489DE4AA8A734AAB75B6E5C42BBB13FD4B9)

This API can be called only after **bind** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: error event.

 |
| callback | ErrorCallback | Yes | Callback used to return the result. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
  tls.on('error', (err: BusinessError) => {
    console.error("on error, err:" + JSON.stringify(err))
  });
});

#### \[h2\]off('error')9+

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from **error** events of the **TLSSocket** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: error event.

 |
| callback | ErrorCallback | No | Callback used to return the result. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let callback = (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err));
}
tls.on('error', callback);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
tls.off('error', callback);

#### \[h2\]connect9+

connect(options: TLSConnectOptions, callback: AsyncCallback<void>): void

Sets up a **TLSSocket** connection, and creates and initializes a TLS session after **bind** is successfully called. During this process, a TLS/SSL handshake is performed between the application and the server to implement data transmission. This API uses an asynchronous callback to return the result. Note that **ca** in **secureOptions** of the **options** parameter is mandatory in API version 11 or earlier. You need to enter the CA certificate of the server for certificate authentication. The certificate content starts with "-----BEGIN CERTIFICATE-----" and ends with "-----END CERTIFICATE-----". This field is optional since API version 12.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TLSConnectOptions](#tlsconnectoptions9) | Yes | Parameters required for the TLS socket connection. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, no value is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303104 | Interrupted system call. |
| 2303109 | Bad file number. |
| 2303111 | Resource temporarily unavailable. Try again. |
| 2303188 | Socket operation on non-socket. |
| 2303191 | Incorrect socket protocol type. |
| 2303198 | Address already in use. |
| 2303199 | Cannot assign requested address. |
| 2303210 | Connection timed out. |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |
| 2301206 | Socks5 failed to connect to the proxy server. |
| 2301207 | Socks5 username or password is invalid. |
| 2301208 | Socks5 failed to connect to the remote server. |
| 2301209 | Socks5 failed to negotiate the authentication method. |
| 2301210 | Socks5 failed to send the message. |
| 2301211 | Socks5 failed to receive the message. |
| 2301212 | Socks5 serialization error. |
| 2301213 | Socks5 deserialization error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsTwoWay: socket.TLSSocket = socket.constructTLSSocketInstance();  // Two way authentication
let bindAddr: socket.NetAddress = {
    address: '192.168.xx.xxx',
  // Bind the specified network API.
}
tlsTwoWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let twoWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let twoWaySecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: twoWayNetAddr,
  secureOptions: twoWaySecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}

tlsTwoWay.connect(tlsConnectOptions, (err: BusinessError) => {
  console.error("connect callback error" + err);
});

let tlsOneWay: socket.TLSSocket = socket.constructTLSSocketInstance(); // One way authentication
tlsOneWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let oneWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let oneWaySecureOptions: socket.TLSSecureOptions = {
  ca: \["xxxx", "xxxx"\],
  cipherSuite: "AES256-SHA256"
}
let tlsOneWayConnectOptions: socket.TLSConnectOptions = {
  address: oneWayNetAddr,
  secureOptions: oneWaySecureOptions
}
tlsOneWay.connect(tlsOneWayConnectOptions, (err: BusinessError) => {
  console.error("connect callback error" + err);
});

**Example (with socket proxy):**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsTwoWay: socket.TLSSocket = socket.constructTLSSocketInstance(); // Two-way authentication
let bindAddr: socket.NetAddress = {
   address: '192.168.xx.xxx',
  // Bind the specified network API.
}
tlsTwoWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let twoWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let socks5Server: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let twoWaySecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let proxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: twoWayNetAddr,
  secureOptions: twoWaySecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\],
  proxy: proxyOptions,
}

tlsTwoWay.connect(tlsConnectOptions, (err: BusinessError) => {
  console.error("connect callback error" + err);
});

let tlsOneWay: socket.TLSSocket = socket.constructTLSSocketInstance(); // One-way authentication
tlsOneWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let oneWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let oneWaySecureOptions: socket.TLSSecureOptions = {
  ca: \["xxxx", "xxxx"\],
  cipherSuite: "AES256-SHA256"
}
let oneWayProxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let tlsOneWayConnectOptions: socket.TLSConnectOptions = {
  address: oneWayNetAddr,
  secureOptions: oneWaySecureOptions,
  proxy: oneWayProxyOptions,
}
tlsOneWay.connect(tlsOneWayConnectOptions, (err: BusinessError) => {
  console.error("connect callback error" + err);
});

#### \[h2\]connect9+

connect(options: TLSConnectOptions): Promise<void>

Sets up a **TLSSocket** connection, and creates and initializes a TLS session after **bind** is successfully called. During this process, a TLS/SSL handshake is performed between the application and the server to implement data transmission. Both two-way and one-way authentication modes are supported. This API uses a promise to return the result. Note that **ca** in **secureOptions** of the **options** parameter is mandatory in API version 11 or earlier. You need to enter the CA certificate of the server for certificate authentication. The certificate content starts with "-----BEGIN CERTIFICATE-----" and ends with "-----END CERTIFICATE-----". This field is optional since API version 12.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TLSConnectOptions](#tlsconnectoptions9) | Yes | Parameters required for the connection. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the operation is successful, no value is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303104 | Interrupted system call. |
| 2303109 | Bad file number. |
| 2303111 | Resource temporarily unavailable. Try again. |
| 2303188 | Socket operation on non-socket. |
| 2303191 | Incorrect socket protocol type. |
| 2303198 | Address already in use. |
| 2303199 | Cannot assign requested address. |
| 2303210 | Connection timed out. |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |
| 2301206 | Socks5 failed to connect to the proxy server. |
| 2301207 | Socks5 username or password is invalid. |
| 2301208 | Socks5 failed to connect to the remote server. |
| 2301209 | Socks5 failed to negotiate the authentication method. |
| 2301210 | Socks5 failed to send the message. |
| 2301211 | Socks5 failed to receive the message. |
| 2301212 | Socks5 serialization error. |
| 2301213 | Socks5 deserialization error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsTwoWay: socket.TLSSocket = socket.constructTLSSocketInstance();  // Two way authentication
let bindAddr: socket.NetAddress = {
   address: '192.168.xx.xxx',
  // Bind the specified network API.
}
tlsTwoWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let twoWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let twoWaySecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: twoWayNetAddr,
  secureOptions: twoWaySecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}

tlsTwoWay.connect(tlsConnectOptions).then(() => {
  console.info("connect successfully");
}).catch((err: BusinessError) => {
  console.error("connect failed " + JSON.stringify(err));
});

let tlsOneWay: socket.TLSSocket = socket.constructTLSSocketInstance(); // One way authentication
tlsOneWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let oneWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let oneWaySecureOptions: socket.TLSSecureOptions = {
  ca: \["xxxx", "xxxx"\],
  cipherSuite: "AES256-SHA256"
}
let tlsOneWayConnectOptions: socket.TLSConnectOptions = {
  address: oneWayNetAddr,
  secureOptions: oneWaySecureOptions
}
tlsOneWay.connect(tlsOneWayConnectOptions).then(() => {
  console.info("connect successfully");
}).catch((err: BusinessError) => {
  console.error("connect failed " + JSON.stringify(err));
});

**Example (with socket proxy):**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsTwoWay: socket.TLSSocket = socket.constructTLSSocketInstance(); // Two-way authentication
let bindAddr: socket.NetAddress = {
   address: '192.168.xx.xxx',
  // Bind the specified network API.
}
tlsTwoWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let twoWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let socks5Server: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let twoWaySecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let proxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: twoWayNetAddr,
  secureOptions: twoWaySecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\],
  proxy: proxyOptions,
}

tlsTwoWay.connect(tlsConnectOptions).then(() => {
  console.info("connect successfully");
}).catch((err: BusinessError) => {
  console.error("connect failed " + JSON.stringify(err));
});

let tlsOneWay: socket.TLSSocket = socket.constructTLSSocketInstance(); // One-way authentication
tlsOneWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let oneWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let oneWaySecureOptions: socket.TLSSecureOptions = {
  ca: \["xxxx", "xxxx"\],
  cipherSuite: "AES256-SHA256"
}
let oneWayProxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let tlsOneWayConnectOptions: socket.TLSConnectOptions = {
  address: oneWayNetAddr,
  secureOptions: oneWaySecureOptions,
  proxy: oneWayProxyOptions,
}
tlsOneWay.connect(tlsOneWayConnectOptions).then(() => {
  console.info("connect successfully");
}).catch((err: BusinessError) => {
  console.error("connect failed " + JSON.stringify(err));
});

#### \[h2\]getRemoteAddress9+

getRemoteAddress(callback: AsyncCallback<NetAddress>): void

Obtains the remote address of a TLS socket connection. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[NetAddress](#netaddress)\> | Yes | Callback used to return the result. If the operation is successful, the remote address is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getRemoteAddress((err: BusinessError, data: socket.NetAddress) => {
  if (err) {
    console.error('getRemoteAddress fail');
    return;
  }
  console.info('getRemoteAddress success:' + JSON.stringify(data));
});

#### \[h2\]getRemoteAddress9+

getRemoteAddress(): Promise<NetAddress>

Obtains the remote address of a TLS socket connection. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | Promise used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getRemoteAddress().then(() => {
  console.info('getRemoteAddress success');
}).catch((err: BusinessError) => {
  console.error('getRemoteAddress fail');
});

#### \[h2\]getCertificate9+

getCertificate(callback: AsyncCallback<[X509CertRawData](#x509certrawdata9)\>): void

Obtains the local digital certificate after a **TLSSocket** connection is established. This API is applicable to two-way authentication. It uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[X509CertRawData](#x509certrawdata9)\> | Yes | Callback used to return the result. If the operation is successful, the local certificate is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303504 | An error occurred when verifying the X.509 certificate. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getCertificate((err: BusinessError, data: socket.X509CertRawData) => {
  if (err) {
    console.error("getCertificate callback error = " + err);
  } else {
    console.info("getCertificate callback = " + data);
  }
});

#### \[h2\]getCertificate9+

getCertificate():Promise<[X509CertRawData](#x509certrawdata9)\>

Obtains the local digital certificate after a **TLSSocket** connection is established. This API is applicable to two-way authentication. It uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[X509CertRawData](#x509certrawdata9)\> | Promise used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303504 | An error occurred when verifying the X.509 certificate. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getCertificate().then((data: socket.X509CertRawData) => {
  const decoder = util.TextDecoder.create();
  const str = decoder.decodeToString(data.data);
  console.info("getCertificate: " + str);
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

#### \[h2\]getRemoteCertificate9+

getRemoteCertificate(callback: AsyncCallback<[X509CertRawData](#x509certrawdata9)\>): void

Obtains the digital certificate of the server after a **TLSSocket** connection is established. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[X509CertRawData](#x509certrawdata9)\> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getRemoteCertificate((err: BusinessError, data: socket.X509CertRawData) => {
  if (err) {
    console.error("getRemoteCertificate callback error = " + err);
  } else {
    const decoder = util.TextDecoder.create();
    const str = decoder.decodeToString(data.data);
    console.info("getRemoteCertificate callback = " + str);
  }
});

#### \[h2\]getRemoteCertificate9+

getRemoteCertificate():Promise<[X509CertRawData](#x509certrawdata9)\>

Obtains the digital certificate of the server after a **TLSSocket** connection is established. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[X509CertRawData](#x509certrawdata9)\> | Promise used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getRemoteCertificate().then((data: socket.X509CertRawData) => {
  const decoder = util.TextDecoder.create();
  const str = decoder.decodeToString(data.data);
  console.info("getRemoteCertificate:" + str);
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

#### \[h2\]getProtocol9+

getProtocol(callback: AsyncCallback<string>): void

Obtains the communication protocol version after a **TLSSocket** connection is established. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getProtocol((err: BusinessError, data: string) => {
  if (err) {
    console.error("getProtocol callback error = " + err);
  } else {
    console.info("getProtocol callback = " + data);
  }
});

#### \[h2\]getProtocol9+

getProtocol():Promise<string>

Obtains the communication protocol version after a **TLSSocket** connection is established. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getProtocol().then((data: string) => {
  console.info(data);
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

#### \[h2\]getCipherSuite9+

getCipherSuite(callback: AsyncCallback<Array<string>>): void

Obtains the cipher suite negotiated by both communication parties after a **TLSSocket** connection is established. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<string>> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getCipherSuite((err: BusinessError, data: Array<string>) => {
  if (err) {
    console.error("getCipherSuite callback error = " + err);
  } else {
    console.info("getCipherSuite callback = " + data);
  }
});

#### \[h2\]getCipherSuite9+

getCipherSuite(): Promise<Array<string>>

Obtains the cipher suite negotiated by both communication parties after a **TLSSocket** connection is established. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getCipherSuite().then((data: Array<string>) => {
  console.info('getCipherSuite success:' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

#### \[h2\]getSignatureAlgorithms9+

getSignatureAlgorithms(callback: AsyncCallback<Array<string>>): void

Obtains the signing algorithm negotiated by both communication parties after a **TLSSocket** connection is established. This API is applicable to two-way authentication. It uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<string>> | Yes | Callback used to return the result. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getSignatureAlgorithms((err: BusinessError, data: Array<string>) => {
  if (err) {
    console.error("getSignatureAlgorithms callback error = " + err);
  } else {
    console.info("getSignatureAlgorithms callback = " + data);
  }
});

#### \[h2\]getSignatureAlgorithms9+

getSignatureAlgorithms(): Promise<Array<string>>

Obtains the signing algorithm negotiated by both communication parties after a **TLSSocket** connection is established. This API is applicable to two-way authentication. It uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the result. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getSignatureAlgorithms().then((data: Array<string>) => {
  console.info("getSignatureAlgorithms success" + data);
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

Obtains the local socket address of a **TLSSocket** connection. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Xaxf_6QbSz2en_zpCmXcGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=126FAC1E29C293EE297204237E906A5706C55A0A0A198E8AE5E0B6E74F81EB45)

Call this API only after the **TLSSocketServer** connection is successfully established.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | Promise used to return the result. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getLocalAddress().then((localAddress: socket.NetAddress) => {
  console.info("Get success: " + JSON.stringify(localAddress));
}).catch((err: BusinessError) => {
  console.error("Get failed, error: " + JSON.stringify(err));
})

#### \[h2\]getSocketFd16+

getSocketFd(): Promise<number>

Obtains the file descriptor of the **TLSSocket** object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/rCcwwXJVTBCraoCgTfvhkg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD1BAE981AF998F857F69368C999B0E9A5FFDFD409BF9723B0BDDCEEB4658DEE)

This API can be called only after **bind** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
tls.getSocketFd().then((data: number) => {
  console.info("tls socket fd: " + data);
})

#### \[h2\]send9+

send(data: string | ArrayBuffer, callback: AsyncCallback<void>): void

Sends a message to the server after a **TLSSocket** connection is established. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | string | ArrayBuffer | Yes | Data content of the message to send. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.send("xxxx", (err: BusinessError) => {
  if (err) {
    console.error("send callback error = " + err);
  } else {
    console.info("send success");
  }
});

#### \[h2\]send9+

send(data: string | ArrayBuffer): Promise<void>

Sends a message to the server after a **TLSSocket** connection is established. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | string | ArrayBuffer | Yes | Data content of the message to send. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the operation fails, an error message is returned. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.send("xxxx").then(() => {
  console.info("send success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

#### \[h2\]close9+

close(callback: AsyncCallback<void>): void

Closes a **TLSSocket** connection. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.close((err: BusinessError) => {
  if (err) {
    console.error("close callback error = " + err);
  } else {
    console.info("close success");
  }
});

#### \[h2\]close9+

close(): Promise<void>

Closes a **TLSSocket** connection. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.close().then(() => {
  console.info("close success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

#### TLSConnectOptions9+

Defines TLS connection options.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | No | No | Gateway address. |
| secureOptions | [TLSSecureOptions](#tlssecureoptions9) | No | No | TLS security options. |
| ALPNProtocols | Array<string> | No | Yes | ALPN protocol. The value range is \["spdy/1", "http/1.1"\]. The default value is **\[\]**. |
| skipRemoteValidation12+ | boolean | No | Yes | Whether to skip certificate authentication on the server. The default value is **false**. The value **true** means to skip certificate authentication on the server, and the value **false** means the opposite. |
| proxy18+ | [ProxyOptions](#proxyoptions18) | No | Yes | Proxy option. By default, no proxy is used. |
| timeout22+ | number | No | Yes | Connection timeout interval, in milliseconds. The default value is **0**. The input value must be an integer ranging from 0 to 4294967295. The TLS socket connection fails after the timeout interval. |

#### TLSSecureOptions9+

TLS security options. When **cert** (local certificate) and **key** (private key) are not empty, the two-way authentication mode is enabled. If **cert** or **key** is empty, one-way authentication is enabled.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ca | string | Array<string> | No | Yes | CA certificate of the server, which is used to authenticate the digital certificate of the server. The default value is the preset CA certificate12+. |
| cert | string | No | Yes | Digital certificate of the local client. |
| key | string | No | Yes | Private key of the local digital certificate. |
| password | string | No | Yes | Password for reading the private key. |
| protocols | [Protocol](#protocol9) |Array<[Protocol](#protocol9)\> | No | Yes | TLS protocol version. The default value is **TLSv1.2**. |
| useRemoteCipherPrefer | boolean | No | Yes | Whether to use the remote cipher suite preferentially. The value **true** means to use the remote cipher suite preferentially, and the value **false** means the opposite. |
| signatureAlgorithms | string | No | Yes | Signing algorithm used during communication. The default value is **""**. |
| cipherSuite | string | No | Yes | Cipher suite used during communication. The default value is **""**. |
| isBidirectionalAuthentication12+ | boolean | No | Yes | Two-way authentication. The default value is **false**. The value **true** means to enable two-way authentication, and the value **false** means the opposite. |

#### Protocol9+

Enumerates TLS protocol versions.

**System capability**: SystemCapability.Communication.NetStack

| Name | Value | Description |
| :-- | :-- | :-- |
| TLSv12 | "TLSv1.2" | TLSv1.2. |
| TLSv13 | "TLSv1.3" | TLSv1.3. |

#### X509CertRawData9+

type X509CertRawData = cert.EncodingBlob

Defines the certificate raw data.

**System capability**: SystemCapability.Communication.NetStack

| Type | Description |
| :-- | :-- |
| cert.EncodingBlob | Certificate encoding BLOB type. |

#### socket.constructTLSSocketServerInstance10+

constructTLSSocketServerInstance(): TLSSocketServer

Creates a **TLSSocketServer** object.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| [TLSSocketServer](#tlssocketserver10) | **TLSSocketServer** object. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();

#### TLSSocketServer10+

Defines a TLS socket server connection. Before calling TLSSocketServer APIs, you need to call [socket.constructTLSSocketServerInstance](#socketconstructtlssocketserverinstance10) to create a **TLSSocketServer** object.

#### \[h2\]listen10+

listen(options: TLSConnectOptions, callback: AsyncCallback<void>): void

Listens for client connections after **bind** is successfully called to bind the IP address and port of **TLSSocketServer**. This API uses an asynchronous callback to return the result. After a connection is established, a TLS session will be created and initialized and a certificate key will be loaded and verified.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/NCRD6CLKS9uAWYdtrYDBHg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E8E7E905462F86472E4A84550DFD34294CF495112B973A3BB452102ADB89B4E3)

If the IP address is set to 0.0.0.0, all local IP addresses can be listened on.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TLSConnectOptions](#tlsconnectoptions9) | Yes | Parameters required for the connection. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, no value is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303109 | Bad file number. |
| 2303111 | Resource temporarily unavailable. Try again. |
| 2303198 | Address already in use. |
| 2303199 | Cannot assign requested address. |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\],
  skipRemoteValidation: false
}
tlsServer.listen(tlsConnectOptions, (err: BusinessError) => {
  console.error("listen callback error" + err);
});

#### \[h2\]listen10+

listen(options: TLSConnectOptions): Promise<void>

Listens for client connections after **bind** is successfully called to bind the IP address and port of **TLSSocketServer**. This API uses an asynchronous callback to return the result. After a connection is established, a TLS session will be created and initialized and a certificate key will be loaded and verified.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TLSConnectOptions](#tlsconnectoptions9) | Yes | Parameters required for the connection. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the operation is successful, no value is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303109 | Bad file number. |
| 2303111 | Resource temporarily unavailable. Try again. |
| 2303198 | Address already in use. |
| 2303199 | Cannot assign requested address. |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\],
  skipRemoteValidation: false
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});

#### \[h2\]getState10+

getState(callback: AsyncCallback<SocketStateBase>): void

Obtains the status of the TLS socket server connection upon successful listening. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/Pddj2UQjSmee3JzoeqiUxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04E71FB3FCF2C10533E9683098CBF5AE14B0832799DA4EF477DAE41939520AB7)

This API can be called only after **listen** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[SocketStateBase](#socketstatebase)\> | Yes | Callback used to return the result. If the operation is successful, the status of the TLS socket server connection is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.getState((err: BusinessError, data: socket.SocketStateBase) => {
  if (err) {
    console.error('getState fail');
    return;
  }
  console.info('getState success:' + JSON.stringify(data));
});

#### \[h2\]getState10+

getState(): Promise<SocketStateBase>

Obtains the status of the TLS socket server connection upon successful listening. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/IiWc_uorQQyFewNXm05Zlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BB848C076C7A302C29B772185155CE142DC549D8B367068DD2C2ACC92E463AD)

This API can be called only after **listen** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SocketStateBase](#socketstatebase)\> | Promise used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.getState().then(() => {
  console.info('getState success');
}).catch((err: BusinessError) => {
  console.error('getState fail');
});

#### \[h2\]setExtraOptions10+

setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void

Sets other properties of the **TLSSocketServer** object after **listen** is successfully called. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/NUFAYn9vRG-58oGg3sz0Yw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DA5B45A24323A4C1D141D5F3C0420D07646F848F94BCE4B7443DA5C7CE47E52)

This API can be called only after **listen** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TCPExtraOptions](#tcpextraoptions) | Yes | Other properties of the **TLSSocketServer** object. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, no value is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});

interface SocketLinger {
  on: boolean;
  linger: number;
}

let tcpExtraOptions: socket.TCPExtraOptions = {
  keepAlive: true,
  OOBInline: true,
  TCPNoDelay: true,
  socketLinger: { on: true, linger: 10 } as SocketLinger,
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  reuseAddress: true,
  socketTimeout: 3000
}
tlsServer.setExtraOptions(tcpExtraOptions, (err: BusinessError) => {
  if (err) {
    console.error('setExtraOptions fail');
    return;
  }
  console.info('setExtraOptions success');
});

#### \[h2\]setExtraOptions10+

setExtraOptions(options: TCPExtraOptions): Promise<void>

Sets other properties of the **TLSSocketServer** object after **listen** is successfully called. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/1fxXab-LTViSjTbBrZx3rQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD3CFEFF6C5CB1B29C457B6BC3CE0A109E67F2C67320EB01CB94491A25F9413C)

This API can be called only after **listen** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TCPExtraOptions](#tcpextraoptions) | Yes | Other properties of the **TLSSocketServer** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the operation is successful, no value is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});

interface SocketLinger {
  on: boolean;
  linger: number;
}

let tcpExtraOptions: socket.TCPExtraOptions = {
  keepAlive: true,
  OOBInline: true,
  TCPNoDelay: true,
  socketLinger: { on: true, linger: 10 } as SocketLinger,
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  reuseAddress: true,
  socketTimeout: 3000
}
tlsServer.setExtraOptions(tcpExtraOptions).then(() => {
  console.info('setExtraOptions success');
}).catch((err: BusinessError) => {
  console.error('setExtraOptions fail');
});

#### \[h2\]getCertificate10+

getCertificate(callback: AsyncCallback<[X509CertRawData](#x509certrawdata9)\>): void

Obtains the local digital certificate after a **TLSSocketServer** connection is established. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/x4Ajpd0wSs6CVmHy2uScXA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=62AE3E1C7767201A69F0525F45F8BBAFAC1DD3FCC0EF7DFE9B6377D5CFFED30B)

This API can be called only after **listen** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[X509CertRawData](#x509certrawdata9)\> | Yes | Callback used to return the result. If the operation is successful, the local certificate is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303504 | An error occurred when verifying the X.509 certificate. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.getCertificate((err: BusinessError, data: socket.X509CertRawData) => {
  if (err) {
    console.error("getCertificate callback error = " + err);
  } else {
    const decoder = util.TextDecoder.create();
    const str = decoder.decodeToString(data.data);
    console.info("getCertificate callback: " + str);
  }
});

#### \[h2\]getCertificate10+

getCertificate():Promise<[X509CertRawData](#x509certrawdata9)\>

Obtains the local digital certificate after a **TLSSocketServer** connection is established. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/uUFfRcnST5-qNV2xPzUkAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A730A53CEF686B9CE3F4834AE4B6CBCA995C5069D553AFCFC704A2DA8BBF708)

This API can be called only after **listen** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[X509CertRawData](#x509certrawdata9)\> | Promise used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303504 | An error occurred when verifying the X.509 certificate. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.getCertificate().then((data: socket.X509CertRawData) => {
  const decoder = util.TextDecoder.create();
  const str = decoder.decodeToString(data.data);
  console.info("getCertificate: " + str);
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

#### \[h2\]getProtocol10+

getProtocol(callback: AsyncCallback<string>): void

Obtains the communication protocol version after a **TLSSocketServer** connection is established. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/o34ogDqTQ5aakS4rBi94VQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48471DBE9A9DDF206F64AACB8446CBB37A41433B29DFC64599263129CBE06444)

This API can be called only after **listen** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.getProtocol((err: BusinessError, data: string) => {
  if (err) {
    console.error("getProtocol callback error = " + err);
  } else {
    console.info("getProtocol callback = " + data);
  }
});

#### \[h2\]getProtocol10+

getProtocol():Promise<string>

Obtains the communication protocol version after a **TLSSocketServer** connection is established. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/8eKfrmb8QkqPpt5OGVH1lw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C732CE6E41BAC3639F2244379F25279CB0299FA2BB70576A57C5A7B98726FD7F)

This API can be called only after **listen** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.getProtocol().then((data: string) => {
  console.info(data);
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

Obtains the local socket address of a **TLSSocketServer** connection. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/Y51usEocSFWlI4jD3DvhlA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0B66910B34C97A7A80CA61E668BFEEBFF7C41195DEC46DBF31F085B794833A0)

Call this API only after the **TLSSocketServer** connection is successfully established.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | Promise used to return the result. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
tlsServer.getLocalAddress().then((localAddress: socket.NetAddress) => {
  console.info("Get success: " + JSON.stringify(localAddress));
}).catch((err: BusinessError) => {
  console.error("Get failed, error: " + JSON.stringify(err));
})

#### \[h2\]on('connect')10+

on(type: 'connect', callback: Callback<TLSSocketConnection>): void

Subscribes to TLS socket server connection events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/i-W0RYWhS0uvF7jXBV4mXA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C05641F1B5BE825E11975C72DA1C85B912D0DE1A3379FEFA79D614D9871B526)

This API can be called only after **listen** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**connect**: connection event.

 |
| callback | Callback<[TLSSocketConnection](#tlssocketconnection10)\> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
  tlsServer.on('connect', (data: socket.TLSSocketConnection) => {
    console.info(JSON.stringify(data));
  });
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});

#### \[h2\]off('connect')10+

off(type: 'connect', callback?: Callback<TLSSocketConnection>): void

Unsubscribes from **connect** events of the **TLSSocketServer** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/18s00BFLRs64RA7pPtANrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88EDBD4AF8A45ABBCFDC1BEF302B836016F84CE65F19F26EC757BE420367D159)

This API can be called only after **listen** is successfully called.

You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**connect**: connection event.

 |
| callback | Callback<[TLSSocketConnection](#tlssocketconnection10)\> | No | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});

let callback = (data: socket.TLSSocketConnection) => {
  console.info('on connect message: ' + JSON.stringify(data));
}
tlsServer.on('connect', callback);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
tlsServer.off('connect', callback);
tlsServer.off('connect');

#### \[h2\]on('error')10+

on(type: 'error', callback: ErrorCallback): void

Subscribes to **error** events of the **TLSSocketServer** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/TdZ98O7lQBqj0Tfbl2wlXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A811F5BAD19DC1436B4D9A3CD5B15805B6856F3732960454117E74675045AA6)

This API can be called only after **listen** is successfully called.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: error event.

 |
| callback | ErrorCallback | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.on('error', (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err))
});

#### \[h2\]off('error')10+

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from **error** events of the **TLSSocketServer** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/oH6cvOCXSk-Kk7Cu1ZRtLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D17F4DFDCEBF01EADB78683A81DF83431350D4EC9271A5DE43E837D044BBE289)

This API can be called only after **listen** is successfully called.

You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: error event.

 |
| callback | ErrorCallback | No | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});

let callback = (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err));
}
tlsServer.on('error', callback);
// You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
tlsServer.off('error', callback);
tlsServer.off('error');

#### \[h2\]close20+

close(): Promise<void>

Stops listening for events of the **TLSSocketServer** object and releases the port bound by [listen](#listen10-2). This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/VVFtTy48QUKyY3oIQIoLKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D57C02BD2E05D5DADF7924EF8AC0F46C0C2EC150178EC67309844DF36F3F51AF)

This API does not close existing connections. To close the connection, call the [close](#close10-2) API of [TLSSocketConnection](#tlssocketconnection10).

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Socket Error Codes](../../error-codes/socket-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.on('connect', (connection: socket.TLSSocketConnection) => {
  console.info("connection clientId: " + connection.clientId);
  // Logical processing
  tlsServer.close(); // Stop event listening.
  connection.close(); // Close the current connection.
});
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("listen failed: " + err.code);
});

#### TLSSocketConnection10+

Defines a **TLSSocketConnection** object, that is, the connection between the TLSSocket client and the server. Before calling TLSSocketConnection APIs, you need to obtain a **TLSSocketConnection** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/ny-n80RCSTuZswwatVWdCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BFD459C89796FC6500DDCA81FEDBCDBCD431E40913E218B2188E7F8A625B6D8E)

The TLSSocket client can call related APIs through the **TLSSocketConnection** object only after a connection is successfully established between the TLSSocket client and the server.

**System capability**: SystemCapability.Communication.NetStack

## Attributes

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| clientId | number | No | No | ID of the connection between the client and TLSSocketServer. |

#### \[h2\]send10+

send(data: string | ArrayBuffer, callback: AsyncCallback<void>): void

Sends a message to the client after a **TLSSocketServer** connection is established. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | string | ArrayBuffer | Yes | Parameters for sending data over a TLS socket server connection. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, no value is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.send('Hello, client!', (err: BusinessError) => {
    if (err) {
      console.error('send fail');
      return;
    }
    console.info('send success');
  });
});

#### \[h2\]send10+

send(data: string | ArrayBuffer): Promise<void>

Sends a message to the server after a **TLSSocketServer** connection is established. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | string | ArrayBuffer | Yes | Parameters for sending data over a TLS socket server connection. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the operation is successful, no value is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.send('Hello, client!').then(() => {
    console.info('send success');
  }).catch((err: BusinessError) => {
    console.error('send fail');
  });
});

#### \[h2\]close10+

close(callback: AsyncCallback<void>): void

Closes a **TLSSocketServer** connection. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, no value is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.close((err: BusinessError) => {
    if (err) {
      console.error('close fail');
      return;
    }
    console.info('close success');
  });
});

#### \[h2\]close10+

close(): Promise<void>

Closes a **TLSSocketServer** connection. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the operation is successful, no value is returned. If the operation fails, an error message is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.close().then(() => {
    console.info('close success');
  }).catch((err: BusinessError) => {
    console.error('close fail');
  });
});

#### \[h2\]getRemoteAddress10+

getRemoteAddress(callback: AsyncCallback<NetAddress>): void

Obtains the remote address of a TLS socket server connection. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[NetAddress](#netaddress)\> | Yes | Callback used to return the result. If the operation is successful, the remote address is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getRemoteAddress((err: BusinessError, data: socket.NetAddress) => {
    if (err) {
      console.error('getRemoteAddress fail');
      return;
    }
    console.info('getRemoteAddress success:' + JSON.stringify(data));
  });
});

#### \[h2\]getRemoteAddress10+

getRemoteAddress(): Promise<NetAddress>

Obtains the remote address of a TLS socket server connection. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | Promise used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getRemoteAddress().then((data: socket.NetAddress) => {
    console.info('getRemoteAddress success:' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error("failed" + err);
  });
});

#### \[h2\]getRemoteCertificate10+

getRemoteCertificate(callback: AsyncCallback<[X509CertRawData](#x509certrawdata9)\>): void

Obtains the digital certificate of the peer end after a **TLSSocketServer** connection is established. This API uses an asynchronous callback to return the result. It applies only to the scenario where the client sends a certificate to the server.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[X509CertRawData](#x509certrawdata9)\> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getRemoteCertificate((err: BusinessError, data: socket.X509CertRawData) => {
    if (err) {
      console.error("getRemoteCertificate callback error: " + err);
    } else {
      const decoder = util.TextDecoder.create();
      const str = decoder.decodeToString(data.data);
      console.info("getRemoteCertificate callback: " + str);
    }
  });
});

#### \[h2\]getRemoteCertificate10+

getRemoteCertificate():Promise<[X509CertRawData](#x509certrawdata9)\>

Obtains the digital certificate of the peer end after a **TLSSocketServer** connection is established. This API uses a promise to return the result. It applies only to the scenario where the client sends a certificate to the server.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[X509CertRawData](#x509certrawdata9)\> | Promise used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getRemoteCertificate().then((data: socket.X509CertRawData) => {
    const decoder = util.TextDecoder.create();
    const str = decoder.decodeToString(data.data);
    console.info("getRemoteCertificate success: " + str);
  }).catch((err: BusinessError) => {
    console.error("failed" + err);
  });
});

#### \[h2\]getCipherSuite10+

getCipherSuite(callback: AsyncCallback<Array<string>>): void

Obtains the cipher suite negotiated by both communication parties after a **TLSSocketServer** connection is established. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<string>> | Yes | Callback used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getCipherSuite((err: BusinessError, data: Array<string>) => {
    if (err) {
      console.error("getCipherSuite callback error = " + err);
    } else {
      console.info("getCipherSuite callback = " + data);
    }
  });
});

#### \[h2\]getCipherSuite10+

getCipherSuite(): Promise<Array<string>>

Obtains the cipher suite negotiated by both communication parties after a **TLSSocketServer** connection is established. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the result. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getCipherSuite().then((data: Array<string>) => {
    console.info('getCipherSuite success:' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error("failed" + err);
  });
});

#### \[h2\]getSignatureAlgorithms10+

getSignatureAlgorithms(callback: AsyncCallback<Array<string>>): void

Obtains the signing algorithm negotiated by both communication parties after a **TLSSocketServer** connection is established. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<string>> | Yes | Callback used to return the result. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getSignatureAlgorithms((err: BusinessError, data: Array<string>) => {
    if (err) {
      console.error("getSignatureAlgorithms callback error = " + err);
    } else {
      console.info("getSignatureAlgorithms callback = " + data);
    }
  });
});

#### \[h2\]getSignatureAlgorithms10+

getSignatureAlgorithms(): Promise<Array<string>>

Obtains the signing algorithm negotiated by both communication parties after a **TLSSocketServer** connection is established. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the result. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getSignatureAlgorithms().then((data: Array<string>) => {
    console.info("getSignatureAlgorithms success" + data);
  }).catch((err: BusinessError) => {
    console.error("failed" + err);
  });
});

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

Obtains the local socket address of a **TLSSocketConnection** connection. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/EtA9rVrkQHCTl46H7A51bQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4532DB7FF23B0C25640E167B06DD2E5D3F8A5E950748DD924A38BC5F653D8F2)

Call this API only after the **TLSSocketServer** connection is successfully established.

**System capability**: SystemCapability.Communication.NetStack

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | Promise used to return the result. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getLocalAddress().then((localAddress: socket.NetAddress) => {
    console.info("Family IP Port: " + JSON.stringify(localAddress));
  }).catch((err: BusinessError) => {
    console.error("TLS Client Get Family IP Port failed, error: " + JSON.stringify(err));
  })
});

#### \[h2\]on('message')10+

on(type: 'message', callback: Callback<SocketMessageInfo>): void

Subscribes to **message** events of the **TLSSocketConnection** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**message**: message receiving event.

 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | Yes | Callback used to return the result. If the operation is successful, the TLS socket connection information is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.on('message', (value: socket.SocketMessageInfo) => {
    let messageView = '';
    let uint8Array = new Uint8Array(value.message);
    for (let i: number = 0; i < value.message.byteLength; i++) {
      let messages = uint8Array\[i\];
      let message = String.fromCharCode(messages);
      messageView += message;
    }
    console.info('on message message: ' + JSON.stringify(messageView));
    console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
  });
});

#### \[h2\]off('message')10+

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

Unsubscribes from **message** events of the **TLSSocketConnection** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**message**: message receiving event.

 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | No | Callback used to return the result. If the operation is successful, the TLS socket connection information is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

let callback = (value: socket.SocketMessageInfo) => {
  let messageView = '';
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let uint8Array = new Uint8Array(value.message)
    let messages = uint8Array\[i\]
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
}
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.on('message', callback);
  // You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
  client.off('message', callback);
  client.off('message');
});

#### \[h2\]on('close')10+

on(type: 'close', callback: Callback<void>): void

Subscribes to **close** events of the **TLSSocketConnection** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**close**: close event.

 |
| callback | Callback<void> | Yes | Callback used to return the result. If the operation is successful, no value is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.on('close', () => {
    console.info("on close success")
  });
});

#### \[h2\]off('close')10+

off(type: 'close', callback?: Callback<void>): void

Unsubscribes from **close** events of the **TLSSocketConnection** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**close**: close event.

 |
| callback | Callback<void> | No | Callback used to return the result. If the operation is successful, no value is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

let callback = () => {
  console.info("on close success");
}
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.on('close', callback);
  // You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
  client.off('close', callback);
  client.off('close');
});

#### \[h2\]on('error')10+

on(type: 'error', callback: ErrorCallback): void

Subscribes to **error** events of the **TLSSocketConnection** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: error event.

 |
| callback | ErrorCallback | Yes | Callback used to return the result. If the operation is successful, no value is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.on('error', (err: BusinessError) => {
    console.error("on error, err:" + JSON.stringify(err))
  });
});

#### \[h2\]off('error')10+

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from **error** events of the **TLSSocketConnection** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

**error**: error event.

 |
| callback | ErrorCallback | No | Callback used to return the result. If the operation is successful, no value is returned. If the operation fails, an error message is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: \["xxxx"\],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa\_pss\_rsae\_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: \["spdy/1", "http/1.1"\]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

let callback = (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err));
}
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.on('error', callback);
  // You can pass the callback of the on function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events.
  client.off('error', callback);
  client.off('error');
});
