# Using WebSocket for Network Access

#### When to Use

WebSocket is a network communication protocol that enables the establishment of a persistent connection between a client and a server, while facilitating full-duplex communication over this connection. Once the connection is established, both the client and the server can actively send data simultaneously. This constitutes the most significant difference between WebSocket and the traditional HTTP protocol. Unlike WebSocket, HTTP primarily relies on one-way (unidirectional) communication: a client initiates a request, the server side responds with data, and the connection is terminated once a single transfer is complete. Generally, HTTP is applicable to one-off data retrieval (such as web content loading). In contrast, WebSocket is ideal for scenarios with high real-time requirements (such as online chat and real-time games), preventing frequent connection establishment from affecting user experience.

The **webSocket** module implements bidirectional connections between the WebSocket client and WebSocket server for third-party applications. Currently, the WebSocket server is available only for smart TVs.

On the WebSocket client: Use WebSocket to establish a bidirectional connection between the server and the client. Before doing this, you need to use [createWebSocket()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#websocketcreatewebsocket) to create a [WebSocket](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#websocket) object and then use [connect()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#connect) to connect to the server. If the connection is successful, the client will receive a callback of the [open](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#onopen) event. Then, the client can communicate with the server by using [send()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#send). When the server sends a message to the client, the client will receive a callback of the [message](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#onmessage) event. If the connection is no longer needed, the client can call [close()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#close) to close the connection. After successful disconnection, the client will receive a callback of the [close](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#onclose) event. If an error occurs in any of the preceding processes, the client will receive a callback of the [error](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#onerror) event.

On the WebSocket server (available only for smart TVs): Use WebSocket to establish a bidirectional connection between the server and client. Before doing this, you need to use [createWebSocketServer()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#websocketcreatewebsocketserver19) to create a [WebSocketServer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#websocketserver19) object and then use [start()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#start19) to start the server to listen for connection requests from the client. If the connection is successful, the server receives the callback of the [connect](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#onconnect19) event. The server can then communicate with the client by using [send()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#send19) or obtain information about all connected clients by using [listAllConnections()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#listallconnections19). When the client sends a message to the server, the server receives the callback of the [messageReceive](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#onmessagereceive19) event. If the connection is no longer needed, the server can call [close()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#close19) to close the connection. After successful disconnection, the server will receive a callback of the [close](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#onclose19) event. To stop the service, the server can use the [stop()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#stop19) API. If an error occurs in any of the preceding processes, the server will receive a callback of the [error](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#onerror19) event.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/Lm98Y_M3ROaOFkIbk5LAdw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7635706C93DD6BA05BDD7FF95FB4270787F7EA6518163719C46D560E124469FD)

The WebSocket module supports the [heartbeat detection mechanism](https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.2). After a WebSocket connection is established between the client and server or before the client receives a Pong frame from the server, the client sends a Ping frame to the server at an interval specified by **pingInterval**. If the WebSocket server supports the WebSocket protocol, it automatically replies with a Pong frame after receiving a Ping frame, indicating that the connection is normal. If the server is abnormal or does not support the WebSocket protocol, the server does not reply with a Pong frame. If no Pong frame is received within the duration specified by **pongTimeout**, the connection is disconnected. You can enable the heartbeat detection mechanism and customize **pingInterval** and **pongTimeout** on demand. For details, see [WebsocketRequestOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-websocket#websocketrequestoptions).

The WebSocket server is supported since API version 19.

#### Client Development Procedure

1.  Import the **webSocket** and **BusinessError** modules.

import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

1.  Create a WebSocket connection. A **WebSocket** object is returned.

let defaultIpAddress = 'wss://echo.websocket.org'; // WebSocket address
let ws: webSocket.WebSocket = webSocket.createWebSocket();

1.  (Optional) Subscribe to the **open**, **message**, **close**, and **error** events of the **WebSocket** object. When receiving the on('open') event, the client can use the send() API to communicate with the server. When receiving the bye message (the actual message name may differ) from the server, the client proactively disconnects from the server.

ws.on('open', (err: BusinessError, value: Object) => {
  hilog.info(0x0000, 'testTag', 'on open, status:' + JSON.stringify(value));
  // When receiving the on('open') event, the client can use the send() API to communicate with the server.
// ···
});

ws.on('message', (err: BusinessError, value: string | ArrayBuffer) => {
// ···
  hilog.info(0x0000, 'testTag', 'on message, message:' + value);
  // When receiving the \`bye\` message (the actual message name may differ) from the server, the client proactively disconnects from the server.
  if (value === 'bye') {
    ws!.close((err: BusinessError) => {
      if (!err) {
        // ···
        hilog.info(0x0000, 'testTag', \`WebSocket closed successfully\`);
      } else {
        // ···
        hilog.error(0x0000, 'testTag', \`WebSocket closing failed: \` + JSON.stringify(err));
      }
    });
  }
})

ws.on('close', (err: BusinessError, value: webSocket.CloseResult) => {
 hilog.info(0x0000, 'testTag', 'on close, code is ' + value.code + ', reason is ' + value.reason);
// ···
});

ws.on('error', (err: BusinessError) => {
// ···
  hilog.error(0x0000, 'testTag', 'WebSocket error: ' + JSON.stringify(err));
});

1.  Establish a WebSocket connection to a given URL.

ws.connect(defaultIpAddress, (err: BusinessError, value: boolean) => {
  if (!err) {
    hilog.info(0x0000, 'testTag', 'Connected successfully');
  } else {
    // ···
    hilog.error(0x0000, 'testTag', \`WebSocket connection failed: \` + JSON.stringify(err));
  }
});

1.  After receiving the **on('open')** callback event, use the **send()** method to send data to the server.

ws.send('Hello, server!', (err: BusinessError, value: boolean) => {
  if (!err) {
    // ···
    hilog.info(0x0000, 'testTag', 'Message sent successfully');
  } else {
    // ···
    hilog.error(0x0000, 'testTag', \`Message sending failed: \` + JSON.stringify(err));
  }
});

#### Server Development Procedure

1.  Import the **webSocket** and **BusinessError** modules.
    
    import { webSocket } from '@kit.NetworkKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Create a **WebSocketServer** object.
    
    let localServer: webSocket.WebSocketServer;
    localServer = webSocket.createWebSocketServer();
    
3.  Subscribe to the **connect**, **message**, **close**, and **error** (optional) events of the **WebSocketServer** object. When receiving the on('connect') event, the server can use the **send()** API to communicate with the client. When receiving the bye message (the actual message name may differ) from the client, the server proactively disconnects from the client.
    
    localServer.on('connect', async (connection: webSocket.WebSocketConnection) => {
      hilog.info(0x0000, 'testTag', \`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}\`);
      // Use send() to send data to the client when the on('connect') event is received.
      localServer.send("Hello, I'm server!", connection).then((success: boolean) => {
        if (success) {
          hilog.info(0x0000, 'testTag', 'message send successfully');
        } else {
          hilog.error(0x0000, 'testTag', 'message send failed');
        }
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'testTag', \`message send failed, Code: ${error.code}, message: ${error.message}\`);
      });
    });
    
    localServer.on('messageReceive', (message: webSocket.WebSocketMessage) => {
      try {
        hilog.info(0x0000, 'testTag', \`on message received, client: ${message.clientConnection}, data: ${message.data}\`);
        // When receiving the bye message (the actual message name may differ) from the client, the server proactively disconnects from the client.
        if (message.data === 'bye') {
          localServer.close(message.clientConnection).then((success: boolean) => {
            if (success) {
              hilog.info(0x0000, 'testTag', 'close client successfully');
            } else {
              hilog.error(0x0000, 'testTag', 'close client failed');
            }
          });
        }
      } catch (error) {
        hilog.error(0x0000, 'testTag', \`on messageReceive failed. Code: ${error.code}, message: ${error.message}\`);
      }
    });
    
    localServer.on('close', (clientConnection: webSocket.WebSocketConnection, closeReason: webSocket.CloseResult) => {
      hilog.info(0x0000, 'testTag', \`client close, client: ${clientConnection}, closeReason: Code: ${closeReason.code}, reason: ${closeReason.reason}\`);
    });
    
    localServer.on('error', (error: BusinessError) => {
      hilog.error(0x0000, 'testTag', \`error. Code: ${error.code}, message: ${error.message}\`);
    });
    
4.  Configure **config** parameters for starting the WebSocket server.
    
    let config: webSocket.WebSocketServerConfig = {
      // Configure the listening port.
      serverPort: 8080,
      maxConcurrentClientsNumber: 10,
      maxConnectionsForOneClient: 10,
    }
    localServer.start(config).then((success: boolean) => {
      if (success) {
        hilog.info(0x0000, 'testTag', 'WebSocket server started successfully');
      } else {
        hilog.error(0x0000, 'testTag', 'Failed to start WebSocket server');
      }
    }).catch((error: BusinessError) => {
      hilog.error(0x0000, 'testTag', \`Failed to start. Code: ${error.code}, message: ${error.message}\`);
    });
    
5.  (Optional) Enable listening for the connection status of all clients.
    
    let connections: webSocket.WebSocketConnection\[\] = \[\];
    
    // ···
      try {
        connections = await localServer.listAllConnections();
        if (connections.length === 0) {
          hilog.info(0x0000, 'testTag', 'client list is empty');
        // ···
        } else {
          hilog.info(0x0000, 'testTag', \`client list cnt: ${connections.length}, client connections list is: ${connections}\`);
        }
      } catch (error) {
        hilog.error(0x0000, 'testTag', \`Failed to listAllConnections. Code: ${error.code}, message: ${error.message}\`);
        // ···
      }
    
6.  Call **stop()** to stop the WebSocket server if it is no longer needed.
    
    localServer.stop().then((success: boolean) => {
      if (success) {
        hilog.info(0x0000, 'testTag', 'server stop service successfully');
        // ···
      } else {
        hilog.error(0x0000, 'testTag', 'server stop service failed');
        // ···
      }
    });
