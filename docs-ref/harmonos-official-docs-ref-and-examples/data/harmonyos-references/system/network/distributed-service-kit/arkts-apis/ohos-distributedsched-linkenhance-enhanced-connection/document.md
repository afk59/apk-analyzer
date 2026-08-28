# @ohos.distributedsched.linkEnhance (Enhanced Connection)

The **linkEnhance** module delivers highly efficient Bluetooth connectivity and data transmission capabilities, significantly enhancing the cross-device connection stability. By employing a multi-channel merging algorithm, it not only increases the number of available cross-device connections but also strengthens cross-device data transmission capabilities, thereby improving the overall user experience.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/hxk5ioLPTl6H-RIjFAddew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062344Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C8EC7C1F4A98F6CF79DAC7B63C2B17513952289D2BD314A6E6901768D2D11A8E)

The initial APIs of this module are supported since API version 20. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { linkEnhance } from '@kit.DistributedServiceKit';

#### linkEnhance.createServer

createServer(name: string): Server

Creates a **Server** object. After **start()** is called, the device can be connected to other devices as a server.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | **Server** object name. The value is a string of up to 255 bytes. It cannot be empty. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Server](#server) | **Server** object created. |

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 32390203 | Duplicate server name. |
| 32390206 | Invalid parameter. |

**Example**

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let name: string = "demo";
  hilog.info(0x0000, TAG, 'start server name = ' + name);
  // Construct a Server object using the specified name.
  let server: linkEnhance.Server = linkEnhance.createServer(name);
} catch (err) {
  hilog.error(0x0000, TAG, 'start server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}

#### linkEnhance.createConnection

createConnection(deviceId: string, name: string): Connection

Creates a **Connection** object on the device that functions as the client. The device can then initiate connection requests to the device that functions as the server.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Device ID of the peer device, that is, the BLE MAC address of the peer device. For details about how to obtain the BLE MAC address, see [BLE Advertising and Scanning](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ble-development-guide). |
| name | string | Yes | Server name of the device to be connected. The value is a string of up to 255 bytes. It cannot be empty. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Connection](#connection) | **Connection** object created. |

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**Example**

On the device that functions as the client, call the **createConnection()** to create a **Connection** object.

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}

#### Server

Represents a **Server** object, which provides methods for starting, stopping, and closing the server, and registering or unregistering event callbacks.

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

The following APIs are used on the server.

#### \[h2\]start()

start(): void

Starts a server so that it can be connected by the client. A maximum of 10 servers are supported.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 32390202 | The number of servers exceeds the limit. |
| 32390300 | Internal error. |

**Example**

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let name: string = "demo";
  hilog.info(0x0000, TAG, 'start server name = ' + name);
  let server: linkEnhance.Server = linkEnhance.createServer(name);
  server.start();
} catch (err) {
  hilog.error(0x0000, TAG, 'start server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}

#### \[h2\]stop()

stop(): void

Stops the server. After the server is stopped, you can call start to start it again.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let name: string = "demo";
  hilog.info(0x0000, TAG, 'start server name = ' + name);
  let server: linkEnhance.Server = linkEnhance.createServer(name);
  server.start();
  server.stop();
} catch (err) {
  hilog.error(0x0000, TAG, 'start server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}

#### \[h2\]close()

close(): void

Destroys the **Server** object to release related resources. To interact with the peer device again, create a new **Server** object.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let name: string = "demo";
  hilog.info(0x0000, TAG, 'start server name = ' + name);
  let server: linkEnhance.Server = linkEnhance.createServer(name);
  server.start();
  server.close();
} catch (err) {
  hilog.error(0x0000, TAG, 'start server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}

#### \[h2\]on('connectionAccepted')

on(type: 'connectionAccepted', callback: Callback<Connection>): void

Registers a callback listener for **connectionAccepted** events. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **connectionAccepted**. This event is triggered when a connection from the peer end is received. |
| callback | Callback<[Connection](#connection)\> | Yes | Registered callback, which is used to return the [Connection](#connection) object. |

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 32390206 | Parameter invalid. |

**Example**

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let name: string = "demo";
  hilog.info(0x0000, TAG, 'start server name = ' + name);
  // Construct a Server object using the specified name.
  let server: linkEnhance.Server = linkEnhance.createServer(name);

  // Subscribe to connectionAccepted events.
  server.on('connectionAccepted', (connection: linkEnhance.Connection): void => {
    hilog.info(0x0000, TAG, 'serverOnCallback = ' + JSON.stringify(connection));
  });
  // Start the server.
  server.start();
} catch (err) {
  hilog.error(0x0000, TAG, 'start server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}

#### \[h2\]off('connectionAccepted')

off(type: 'connectionAccepted', callback?: Callback<Connection>): void

Unregisters the callback listener for **connectionAccepted** events. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **connectionAccepted**. This event is triggered when a connection from the peer end is received. |
| callback | Callback<[Connection](#connection)\> | No | Registered callback, which is used to return the [Connection](#connection) object. |

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 32390206 | Parameter invalid. |

**Example**

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let name: string = "demo";
  hilog.info(0x0000, TAG, 'start server name = ' + name);
  // Construct a Server object using the specified name.
  let server: linkEnhance.Server = linkEnhance.createServer(name);
  server.on('connectionAccepted', (connection: linkEnhance.Connection): void => {
    hilog.info(0x0000, TAG, 'accept new connection');
  });
  // Unsubscribe from connectionAccepted events.
  server.off('connectionAccepted', (connection: linkEnhance.Connection): void => {
    hilog.info(0x0000, TAG, 'accept new connection');
  });
} catch (err) {
  hilog.error(0x0000, TAG, 'start server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}

#### \[h2\]on('serverStopped')

on(type: 'serverStopped', callback: Callback<number>): void

Registers a callback listener for **serverStopped** events. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **serverStopped**. This event is triggered when the server is stopped abnormally. |
| callback | Callback<number> | Yes | Registered callback, where **number** indicates the returned error code. |

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 32390206 | Parameter invalid. |

**Example**

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let name: string = "demo";
  hilog.info(0x0000, TAG, 'start server name = ' + name);
  // Construct a Server object using the specified name.
  let server: linkEnhance.Server = linkEnhance.createServer(name);

  // Unsubscribe from serverStopped events.
  server.on('serverStopped', (reason: number): void => {
    hilog.info(0x0000, TAG, 'serverStopped, reason= ' + reason);
  });
  // Start the server.
  server.start();
} catch (err) {
  hilog.error(0x0000, TAG, 'start server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}

#### \[h2\]off('serverStopped')

off(type: 'serverStopped', callback?: Callback<number>): void

Unregisters the callback listener for **serverStopped** events. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **serverStopped**. This event is triggered when the server is stopped abnormally. |
| callback | Callback<number> | No | Registered callback, where **number** indicates the returned error code. |

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 32390206 | Parameter invalid. |

**Example**

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let name: string = "demo";
  hilog.info(0x0000, TAG, 'start server name = ' + name);
  // Construct a Server object using the specified name.
  let server: linkEnhance.Server = linkEnhance.createServer(name);
  server.on('serverStopped', (reason: number): void => {
    hilog.info(0x0000, TAG, 'serverStopped, reason= ' + reason);
  });
  // Unsubscribe from serverStopped events.
  server.off('serverStopped', (reason: number): void => {
    hilog.info(0x0000, TAG, 'serverStopped, reason= ' + reason);
  });
} catch (err) {
  hilog.error(0x0000, TAG, 'start server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}

#### ConnectResult

Represents the connection result, which is returned after the client calls **connect()**.

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

| **Name** | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | No | ID of the peer device. If the connection is successful, the device ID of the peer device is returned. If the connection fails, an empty string is returned. |
| success | boolean | No | No | Connection result. The value **true** indicates that the connection is successful, and the value **false** indicates the opposite. |
| reason | number | No | No | 
Number indicating the result code. If the connection is successful, **0** is returned. If the connection fails, an error code is returned:

\- 32390200: The client connection times out.

\- 32390201: The server service is not started.

\- 32390300: Internal error.

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

 |

#### Connection

Represents a **Connection** object, which provides methods for connecting to and disconnecting from a peer device, obtaining the device's ID, sending data, and registering or unregistering event callbacks.

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

#### \[h2\]connect()

connect(): void

Connects to the server on the client. A maximum number of 10 connections are supported.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 32390204 | The number of connection exceeds the limit. |
| 32390300 | Internal error. |

**Example**

After creating a **Connection** object, the application on the client device calls **connect()** to connect to the target device (that is, the server).

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  // Subscribe to connectResult events.
  connection.on('connectResult', (result: linkEnhance.ConnectResult): void => {
    hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
  });
  // Initiate a connection.
  connection.connect();
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}

#### \[h2\]disconnect()

disconnect(): void

Disconnects from the peer device. The created **Connection** object remains valid after this API is called. You can call **connect()** to reconnect to the peer device if necessary.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  connection.on('connectResult', (result: linkEnhance.ConnectResult): void => {
    hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
    if (result.success) {
      connection.disconnect();
    }
  });
  connection.connect();
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}

#### \[h2\]close()

close(): void

Destroys the **Connection** object to release resources. If the device needs to interact with the peer device again, create a **Connection** object again and call connect() to initiate a connection.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  connection.on('connectResult', (result: linkEnhance.ConnectResult): void => {
    hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
    if (result.success) {
      connection.close();
    }
  });
  connection.connect();
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}

#### \[h2\]getPeerDeviceId()

getPeerDeviceId(): string

Obtains the device ID of the peer device. This API is called when the connection is established successfully either by initiating a connection or accepting an incoming connection.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Returns**

| Type | Description |
| :-- | :-- |
| string | Device ID of the peer device, that is, the BLE MAC address of the peer device. An empty string is returned if no device ID is obtained. |

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  connection.getPeerDeviceId();
  hilog.info(0x0000, TAG, "peerDeviceId=%{public}s" + connection.getPeerDeviceId());
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}

#### \[h2\]sendData()

sendData(data: ArrayBuffer): void

Sends data to the server after a connection is established successfully. When the server receives the connection callback, it can also send data to the client.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [ArrayBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arraybuffer-object) | Yes | Data to send. The maximum length is 1024 bytes. |

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 32390205 | Connection is not ready. |
| 32390206 | Invalid parameter. |
| 32390300 | Internal error. |

**Example**

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  connection.on('connectResult', (result: linkEnhance.ConnectResult): void => {
    hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
    if (result.success) {
      let len = 1;
      let arraybuffer = new ArrayBuffer(len); // Create the data to send.
      connection.sendData(arraybuffer);
      hilog.info(0x0000, TAG, "sendData data connection peerDeviceId=%{public}s" + connection.getPeerDeviceId());
      connection.disconnect();
    }
  });
  connection.connect();
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}

#### \[h2\]on('connectResult')

on(type: 'connectResult', callback: Callback<ConnectResult>): void

Registers a listener for **connectResult** events. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **connectResult**. This event is triggered when connect() is called. |
| callback | Callback<[ConnectResult](#connectresult)\> | Yes | Registered callback. |

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**Example**

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  // Subscribe to connectResult events.
  connection.on('connectResult', (result: linkEnhance.ConnectResult): void => {
    hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
  });

  // Initiate a connection.
  connection.connect();
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}

#### \[h2\]off('connectResult')

off(type: 'connectResult', callback?: Callback<ConnectResult>): void

Unregisters the listener for **connectResult** events.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **connectResult**. This event is triggered when connect() is called. |
| callback | Callback<[ConnectResult](#connectresult)\> | No | Registered callback. |

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**Example**

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  connection.on('connectResult', (result: linkEnhance.ConnectResult): void => {
    hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
  });
  // Unsubscribe from connectResult events.
  connection.off('connectResult', (result: linkEnhance.ConnectResult): void => {
    hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
  });
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}

#### \[h2\]on('disconnected')

on(type: 'disconnected', callback: Callback<number>): void

Registers a listener for **disconnected** events. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **disconnected**. This event is triggered when the connection is passively terminated or encounters an exception. |
| callback | Callback<number> | Yes | Registered callback, where **number** indicates the returned error code. |

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**Example**

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  // Subscribe to disconnected events.
  connection.on('disconnected', (number: number) => {
    hilog.info(0x0000, TAG, 'connection disconnected reason = ' + number);
  });
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}

#### \[h2\]off('disconnected')

off(type: 'disconnected', callback?: Callback<number>): void

Unregisters the listener for **disconnected** events. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **disconnected**. This event is triggered when the connection is passively terminated or encounters an exception. |
| callback | Callback<number> | No | Registered callback, where **number** indicates the returned error code. |

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**Example**

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  connection.on('disconnected', (number: number) => {
    hilog.info(0x0000, TAG, 'connection disconnected reason = ' + number);
  });
  // Unsubscribe from disconnected events.
  connection.off('disconnected', (number: number) => {
    hilog.info(0x0000, TAG, 'connection disconnected reason = ' + number);
  });
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}

#### \[h2\]on('dataReceived')

on(type: 'dataReceived', callback: Callback<ArrayBuffer>): void

Registers a listener for the **dataReceived** events. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **dataReceived**. This event is triggered when data is received. |
| callback | Callback<[ArrayBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arraybuffer-object)\> | Yes | Registered callback. |

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**Example**

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  // Initiate a connection.
  connection.connect();
  // Subscribe to data receiving notifications.
  connection.on('dataReceived', (data: ArrayBuffer) => {
    hilog.info(0x0000, TAG, 'recv dataLen = ' + data.byteLength);
  });
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}

#### \[h2\]off('dataReceived')

off(type: 'dataReceived', callback?: Callback<ArrayBuffer>): void

Unregisters the listener for **dataReceived** events.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **dataReceived**. This event is triggered when data is received. |
| callback | Callback<[ArrayBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arraybuffer-object)\> | No | Registered callback. |

**Error codes**

For details about the error codes, see [Link Enhancement Error Codes](../../error-codes/link-enhancement-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**Example**

import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  // Subscribe to data receiving notifications.
  connection.on('dataReceived', (data: ArrayBuffer) => {
    hilog.info(0x0000, TAG, 'recv dataLen = ' + data.byteLength);
  });
  // Unsubscribe from data receiving notifications.
  connection.off('dataReceived', (data: ArrayBuffer) => {
    hilog.info(0x0000, TAG, 'recv dataLen = ' + data.byteLength);
  });
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
