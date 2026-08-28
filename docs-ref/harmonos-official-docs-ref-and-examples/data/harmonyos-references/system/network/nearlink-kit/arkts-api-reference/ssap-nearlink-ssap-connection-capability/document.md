# ssap (NearLink SSAP Connection Capability)

This module provides the SSAP (SparkLink Service Access Protocol) connection function.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

#### Module Import

import { ssap } from '@kit.NearLinkKit';

#### ConnectionState

type ConnectionState = [constant.ConnectionState](../constant-nearlink-common-constants/document.md#section14942121015417)

Enumerated values of connection statuses with a remote device.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[constant.ConnectionState](../constant-nearlink-common-constants/document.md#section14942121015417)

 | 

Connection status with a remote device.

 |

#### createClient

createClient(address: string): Client

Creates an SSAP client instance.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

address

 | 

string

 | 

Yes

 | 

Address of the remote server device. The address format is 11:22:33:AA:BB:FF.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[Client](#section124191030153618)

 | 

SSAP client instance.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |
| 

1009700003

 | 

Nearlink is off

 |
| 

1009700099

 | 

Operation failed

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let client: ssap.Client;
try {
  client = ssap.createClient(addr);
  console.info('client: ' + JSON.stringify(client));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### createServer

createServer(): Server

Creates an SSAP server instance.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[Server](#section159881148173016)

 | 

SSAP server instance.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

801

 | 

Capability not supported

 |
| 

1009700003

 | 

Nearlink is off

 |
| 

1009700099

 | 

Operation failed

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let server: ssap.Server;
try {
  server = ssap.createServer();
  console.info('server: ' + JSON.stringify(server));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### Client

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/yWyjyQsxTwmoMYSaO1rNRA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=858998989B874F5B9F1E1F071521FDAB7368DEF4D3EBF2508FD94FDD79801AD6)

This capability allows your app to interact with a remote device through SSAP. Before doing so, you must create a [client](#section124191030153618) instance using the [ssap.createClient](#section1855815061418) method.

You need to create only one instance for a remote device per app.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

#### \[h2\]connect

connect(): Promise<void>

Initiates a connection to the server. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

801

 | 

Capability not supported

 |
| 

1009700003

 | 

Nearlink is off

 |
| 

1009700099

 | 

Operation failed

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // You need to create only one instance for a remote device per app.
  client.connect().then(() => {
    console.info("connect success");
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]disconnect

disconnect(): Promise<void>

Disconnects from the server, regardless of whether a connection exists or is in progress. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

801

 | 

Capability not supported

 |
| 

1009700003

 | 

Nearlink is off

 |
| 

1009700099

 | 

Operation failed

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // You need to create only one instance for a remote device per app.
  client.connect().then(() => {
    console.info("connect success"); // Set up a connection.
  });
  client.disconnect().then(() => {
    console.info("disconnect success"); // Disconnect the connection.
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]close

close(): void

Closes the client instance.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

801

 | 

Capability not supported

 |
| 

1009700003

 | 

Nearlink is off

 |
| 

1009700099

 | 

Operation failed

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let client: ssap.Client;
try { 
  client = ssap.createClient(addr); // You need to create only one instance for a remote device per app.
  client.close();
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]getServices

getServices(): Promise<Array<Service>>

Obtains a list of services supported by the server. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<Array<[Service](#section1622511479139)\>>

 | 

Promise used to return the list of services supported on the server.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

801

 | 

Capability not supported

 |
| 

1009700003

 | 

Nearlink is off

 |
| 

1009700099

 | 

Operation failed

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // You need to create only one instance for a remote device per app.
  client.connect().then(() => {
    console.info('connect success');
  });
  // The connection takes a long time, and the service can only be accessed once the connection is set up. You can adjust the timer length based on the connection speed.
  setTimeout(() => {
    client.getServices().then((result: Array<ssap.Service>) => {
      console.info('getServices successfully:' + JSON.stringify(result));
    });
  }, 3000);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]readProperty

readProperty(property: Property): Promise<Property>

Reads a property from the server. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

property

 | 

[Property](#section9708731141914)

 | 

Yes

 | 

Property from the server.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Property](#section9708731141914)\>

 | 

Promise used to return properties from the server.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |
| 

1009700003

 | 

Nearlink is off

 |
| 

1009700099

 | 

Operation failed

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // You need to create only one instance for a remote device per app.
  client.connect().then(() => {
    console.info('connect success');
  });
  // Create a property. During actual development, the property needs to be obtained from the server through the **getServices** API.
  let arrayBufferC = new ArrayBuffer(8);
  let properV = new Uint8Array(arrayBufferC);
  properV\[0\] = 1;
  let property: ssap.Property = {
    serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
    propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
    value: arrayBufferC
  };
  // The connection takes a long time, and the service can only be accessed once the connection is set up. You can adjust the timer length based on the connection speed.
  setTimeout(()=>{
    client.readProperty(property).then((result: ssap.Property) => {
      console.info('readProperty successfully:' + JSON.stringify(result));
    });
  }, 3000);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]writeProperty

writeProperty(property: Property, writeType: PropertyWriteType): Promise<void>

Writes a property from the server. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

property

 | 

[Property](#section9708731141914)

 | 

Yes

 | 

Property from the server.

 |
| 

writeType

 | 

[PropertyWriteType](#section1976472485918)

 | 

Yes

 | 

Write type. The server can respond with or without returning results.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |
| 

1009700003

 | 

Nearlink is off

 |
| 

1009700099

 | 

Operation failed

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // You need to create only one instance for a remote device per app.
  client.connect().then(() => {
    console.info('connect success');
  });
// Create a property. During actual development, the property needs to be obtained from the server through the **getServices** API.
  let arrayBufferC = new ArrayBuffer(8);
  // Desired property value.
  let properV = new Uint8Array(arrayBufferC);
  properV\[0\] = 1;
  let property: ssap.Property = {
    serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
    propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
    value: arrayBufferC
  };
  // The connection takes a long time, and the service can only be accessed once the connection is set up. You can adjust the timer length based on the connection speed.
  setTimeout(()=>{
    client.writeProperty(property, ssap.PropertyWriteType.WRITE\_NO\_RESPONSE).then(() => {
      console.info('writeProperty success');
    });
  }, 3000);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]setPropertyNotification

setPropertyNotification(property: Property, enable: boolean): Promise<void>

Sets a property change notification. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

property

 | 

[Property](#section9708731141914)

 | 

Yes

 | 

Property from the server.

 |
| 

enable

 | 

boolean

 | 

Yes

 | 

**true**: The notification function is enabled. **false**: The notification function is disabled.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |
| 

1009700003

 | 

Nearlink is off

 |
| 

1009700099

 | 

Operation failed

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // You need to create only one instance for a remote device per app.
  client.connect().then(() => {
    console.info('connect success');
  });
// Create a property. During actual development, the property needs to be obtained from the server through the **getServices** API.
  let arrayBufferC = new ArrayBuffer(8);
  // Desired property value.
  let properV = new Uint8Array(arrayBufferC);
  properV\[0\] = 1;
  let property: ssap.Property = {
    serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
    propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
    value: arrayBufferC
  };
  // The connection takes a long time, and the service can only be accessed once the connection is set up. You can adjust the timer length based on the connection speed.
  setTimeout(()=>{
    client.setPropertyNotification(property, true).then(() => {
      console.info('setPropertyNotification success');
    });
  }, 3000);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]requestMtuSize

requestMtuSize(mtu: number): Promise<void>

Initiates a Maximum Transmission Unit (MTU) negotiation request. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

mtu

 | 

number

 | 

Yes

 | 

MTU. The value ranges from 22 to 512 bytes. The default value is **256**.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |
| 

1009700003

 | 

Nearlink is off

 |
| 

1009700099

 | 

Operation failed

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // You need to create only one instance for a remote device per app.
  client.connect().then(() => {
    console.info('connect success');
  });
  // The connection takes a long time, and the service can only be accessed once the connection is set up. You can adjust the timer length based on the connection speed.
  setTimeout(()=>{
    client.requestMtuSize(128).then(() => {
      console.info('requestMtuSize success');
    });
  }, 3000);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]on( 'propertyChange')

on(type: 'propertyChange', callback: Callback<Property>): void

Subscribes to the property change event.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

This parameter must be set to **propertyChange**, indicating the property change event.

 |
| 

callback

 | 

Callback<[Property](#section9708731141914)\>

 | 

Yes

 | 

Callback for the NearLink property change event. You can create such a callback and register it through this API.

 |

**Error codes**:

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onPropertyChange:(data: ssap.Property) => void = (data: ssap.Property) => {
  console.info('data:'+ JSON.stringify(data));
}
  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // You need to create only one instance for a remote device per app.
  client.on('propertyChange', onPropertyChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]off( 'propertyChange')

off(type: 'propertyChange', callback?: Callback<Property>): void

Unsubscribes from the property change event.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

This parameter must be set to **propertyChange**, indicating the property change event.

 |
| 

callback

 | 

Callback<[Property](#section9708731141914)\>

 | 

No

 | 

Callback to be unregistered, which must be the same as that passed for subscription. If this parameter is not passed, all callbacks will be unregistered.

 |

**Error codes**:

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onPropertyChange:(data: ssap.Property) => void = (data: ssap.Property) => {
  console.info('data:'+ JSON.stringify(data));
}
  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // You need to create only one instance for a remote device per app.
  client.off('propertyChange', onPropertyChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]on( 'connectionStateChange')

on(type: 'connectionStateChange', callback: Callback<ConnectionChangeState>): void

Subscribes to the connection status change event.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

This parameter must be set to **connectionStateChange**, indicating the connection status change event.

 |
| 

callback

 | 

Callback<[ConnectionChangeState](#section8290102785216)\>

 | 

Yes

 | 

Callback for the connection status change event. You can create such a callback and register it through this API.

 |

**Error codes**:

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onConnectionStateChange:(data: ssap.ConnectionChangeState) => void = (data: ssap.ConnectionChangeState) => {
  console.info('data:'+ JSON.stringify(data));
}
  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // You need to create only one instance for a remote device per app.
  client.on('connectionStateChange', onConnectionStateChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]off( 'connectionStateChange')

off(type: 'connectionStateChange', callback?: Callback<ConnectionChangeState>): void

Unsubscribes from the connection status change event.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

This parameter must be set to **connectionStateChange**, indicating the connection status change event.

 |
| 

callback

 | 

Callback<[ConnectionChangeState](#section8290102785216)\>

 | 

No

 | 

Callback to be unregistered, which must be the same as that passed for subscription. If this parameter is not passed, all callbacks will be unregistered.

 |

**Error codes**:

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onConnectionStateChange:(data: ssap.ConnectionChangeState) => void = (data: ssap.ConnectionChangeState) => {
  console.info('data:'+ JSON.stringify(data));
}
  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // You need to create only one instance for a remote device per app.
  client.off('connectionStateChange', onConnectionStateChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]on( 'mtuChange')

on(type: 'mtuChange', callback: Callback<number>): void

Subscribes to the MTU change event.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

This parameter must be set to **mtuChange**, indicating the MTU change event.

 |
| 

callback

 | 

Callback<number>

 | 

Yes

 | 

Callback for the MTU change event. You can create such a callback and register it through this API.

 |

**Error codes**:

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onMtuChange:(data: number) => void = (data: number) => {
  console.info('data:'+ data);
}
  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // You need to create only one instance for a remote device per app.
  client.on('mtuChange', onMtuChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]off( 'mtuChange')

off(type: 'mtuChange', callback?: Callback<number>): void

Unsubscribes from the MTU change event.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

This parameter must be set to **mtuChange**, indicating the MTU change event.

 |
| 

callback

 | 

Callback<number>

 | 

No

 | 

Callback to be unregistered, which must be the same as that passed for subscription. If this parameter is not passed, all callbacks will be unregistered.

 |

**Error codes**:

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onMtuChange:(data: number) => void = (data: number) => {
  console.info('data:'+ data);
}
  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let client: ssap.Client;
try {
  client = ssap.createClient(addr); // You need to create only one instance for a remote device per app.
  client.off('mtuChange', onMtuChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### Server

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/TtD7lYy8Shq2c6OuWqOS0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9F8E8770115567963CD59755F4139219D0798F4FC772F3D21CA88E3AF98B8AD)

This capability allows your app to interact with a remote device through SSAP. Before doing so, you must create a **Server** instance using the **createServer** method.

You need to create only one instance for a remote device per app.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

#### \[h2\]addService

addService(service: Service): void

Adds a service to the server.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

service

 | 

[Service](#section1622511479139)

 | 

Yes

 | 

Information about a service provided by the server. Multiple services can be added, identified by their UUIDs.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |
| 

1009700003

 | 

Nearlink is off

 |
| 

1009700099

 | 

Operation failed

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Construct a descriptor.
let descriptorsArray: Array<ssap.PropertyDescriptor> = \[\];
let arrayBuffer = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBuffer);
descValue\[0\] = 11;
descValue\[1\] = 22;
let descriptor: ssap.PropertyDescriptor = {
  serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
  propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
  value: arrayBuffer,
  descriptorType: ssap.PropertyDescriptorType.PROPERTY,
  isWriteable: true
};
descriptorsArray\[0\] = descriptor;
// Construct properties.
let propertiesArray: Array<ssap.Property> = \[\];
let arrayBufferProperty = new ArrayBuffer(8);
let properValue = new Uint8Array(arrayBufferProperty);
properValue\[0\] = 1;
let property1: ssap.Property = {
  serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
  propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
  value: arrayBufferProperty,
  descriptors:descriptorsArray
};
let property2: ssap.Property = {
  serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
  propertyUuid: '37bea880-fc70-11ea-b720-000000003421',
  value: arrayBufferProperty,
  descriptors:descriptorsArray,
  operation:12
};
propertiesArray\[0\] = property1;
propertiesArray\[1\] = property2;
// Construct a service.
let Service: ssap.Service = {
  serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
  properties:propertiesArray
};
let server: ssap.Server;
try {
  server = ssap.createServer();
  server.addService(Service);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]removeService

removeService(serviceUuid: string): void

Removes a service from the server.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

serviceUuid

 | 

string

 | 

Yes

 | 

Service UUID, that is, UUID displayed when users add a service, for example, **37bea880-fc70-11ea-b720-000000004386**. For details about the UUID format, please refer to [UUID Format for a Standard NearLink Service](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/nearlink-faq#section1263634155618).

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |
| 

1009700003

 | 

Nearlink is off

 |
| 

1009700099

 | 

Operation failed

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let server: ssap.Server;
try {
  server = ssap.createServer();
  // The service has been added using **addService**. You can remove a service by specifying its UUID.
  let serviceUuid = '37bea880-fc70-11ea-b720-000000004386';
  server.removeService(serviceUuid);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]close

close(): void

Closes the server instance.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

801

 | 

Capability not supported

 |
| 

1009700003

 | 

Nearlink is off

 |
| 

1009700099

 | 

Operation failed

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let server: ssap.Server;
try {
  server = ssap.createServer();
  server.close();
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]notifyPropertyChanged

notifyPropertyChanged(address: string, property: Property): Promise<void>

Notifies the client of property value updates. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

address

 | 

string

 | 

Yes

 | 

Address of a client device. The address format is 11:22:33:AA:BB:FF.

 |
| 

property

 | 

[Property](#section9708731141914)

 | 

Yes

 | 

Property whose value changes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |
| 

1009700003

 | 

Nearlink is off

 |
| 

1009700099

 | 

Operation failed

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Construct a descriptor.
let descriptorsArray: Array<ssap.PropertyDescriptor> = \[\];
let arrayBuffer = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBuffer);
descValue\[0\] = 11;
descValue\[1\] = 22;
let descriptor: ssap.PropertyDescriptor = {
  serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
  propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
  value: arrayBuffer,
  descriptorType:ssap.PropertyDescriptorType.PROPERTY,
  isWriteable:true
};
descriptorsArray\[0\] = descriptor;
// Construct properties.
let arrayBufferProperty = new ArrayBuffer(8);
let properValue = new Uint8Array(arrayBufferProperty);
properValue\[0\] = 123; // Value after the update.
let property: ssap.Property = {
  serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
  propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
  value: arrayBufferProperty,
  descriptors:descriptorsArray
};
let server: ssap.Server;
try {
  server = ssap.createServer();
  // This address is that of the connected client device and is cached on the server.
  server.notifyPropertyChanged('00:11:22:33:AA:FF', property).then(() => {
    console.info('notifyPropertyChanged success');
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]sendResponse

sendResponse(response: ServerResponse): void

Replies to read or write requests from the client.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

response

 | 

[ServerResponse](#section18988175925012)

 | 

Yes

 | 

Response data for the client.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |
| 

1009700003

 | 

Nearlink is off

 |
| 

1009700099

 | 

Operation failed

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// After receiving a read or write request, reply to the request through this API.
let arrayBuffer = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBuffer);
descValue\[0\] = 11;
descValue\[1\] = 22;
let resp: ssap.ServerResponse = {
  address: '00:11:22:33:AA:FF', // Address of a requester client.
  requestId: 1, // Request ID.
  value: arrayBuffer // Response data.
};
let server: ssap.Server;
try {
  server = ssap.createServer();
  // This address is that of the connected client device and is cached on the server.
  server.sendResponse(resp);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]on('connectionStateChange')

on(type: 'connectionStateChange', callback: Callback<ConnectionChangeState>): void

Subscribes to the connection status change event.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

This parameter must be set to **connectionStateChange**, indicating the connection status change event.

 |
| 

callback

 | 

Callback<[ConnectionChangeState](#section8290102785216)\>

 | 

Yes

 | 

Callback for the connection status change event. You can create such a callback and register it through this API.

 |

**Error codes**:

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onConnectionStateChange:(data: ssap.ConnectionChangeState) => void = (data: ssap.ConnectionChangeState) => {
  console.info('data:'+ JSON.stringify(data));
}
let server: ssap.Server;
try {
  server = ssap.createServer();
  server.on('connectionStateChange', onConnectionStateChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]off( 'connectionStateChange')

off(type: 'connectionStateChange', callback?: Callback<ConnectionChangeState>): void

Unsubscribes from the connection status change event.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

This parameter must be set to **connectionStateChange**, indicating the connection status change event.

 |
| 

callback

 | 

Callback<[ConnectionChangeState](#section8290102785216)\>

 | 

No

 | 

Callback to be unregistered, which must be the same as that passed for subscription. If this parameter is not passed, all callbacks will be unregistered.

 |

**Error codes**:

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onConnectionStateChange:(data: ssap.ConnectionChangeState) => void = (data: ssap.ConnectionChangeState) => {
  console.info('data:'+ JSON.stringify(data));
}
let server: ssap.Server;
try {
  server = ssap.createServer();
  server.off('connectionStateChange', onConnectionStateChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]on( 'propertyRead')

on(type: 'propertyRead', callback: Callback<PropertyReadRequest>): void

Subscribes to the client read request event.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

This parameter must be set to **propertyRead**, indicating the read request event.

 |
| 

callback

 | 

Callback<[PropertyReadRequest](#section20432111694316)\>

 | 

Yes

 | 

Callback for the read request event. You can create such a callback and register it through this API.

 |

**Error codes**:

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onPropertyReadRequest:(data: ssap.PropertyReadRequest) => void = (data: ssap.PropertyReadRequest) => {
  console.info('data:'+ JSON.stringify(data));
}
let server: ssap.Server;
try {
  server = ssap.createServer();
  server.on('propertyRead', onPropertyReadRequest);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]off( 'propertyRead')

off(type: 'propertyRead', callback?: Callback<PropertyReadRequest>): void

Unsubscribes from the client read request event.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

This parameter must be set to **propertyRead**, indicating the read request event.

 |
| 

callback

 | 

Callback<[PropertyReadRequest](#section20432111694316)\>

 | 

No

 | 

Callback to be unregistered, which must be the same as that passed for subscription. If this parameter is not passed, all callbacks will be unregistered.

 |

**Error codes**:

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onPropertyReadRequest:(data: ssap.PropertyReadRequest) => void = (data: ssap.PropertyReadRequest) => {
  console.info('data:'+ JSON.stringify(data));
}
let server: ssap.Server;
try {
  server = ssap.createServer();
  server.off('propertyRead', onPropertyReadRequest);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]on( 'propertyWrite')

on(type: 'propertyWrite', callback: Callback<PropertyWriteRequest>): void

Subscribes to the client write request event.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

This parameter must be set to **propertyWrite**, indicating the write request event.

 |
| 

callback

 | 

Callback<[PropertyWriteRequest](#section383578205013)\>

 | 

Yes

 | 

Callback for the write request event. You can create such a callback and register it through this API.

 |

**Error codes**:

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onPropertyWriteRequest:(data: ssap.PropertyWriteRequest) => void = (data: ssap.PropertyWriteRequest) => {
  console.info('data:'+ JSON.stringify(data));
}
let server: ssap.Server;
try {
  server = ssap.createServer();
  server.on('propertyWrite', onPropertyWriteRequest);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]off( 'propertyWrite')

off(type: 'propertyWrite', callback?: Callback<PropertyWriteRequest>): void

Unsubscribes from the client write request event.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

This parameter must be set to **propertyWrite**, indicating the write request event.

 |
| 

callback

 | 

Callback<[PropertyWriteRequest](#section383578205013)\>

 | 

No

 | 

Callback to be unregistered, which must be the same as that passed for subscription. If this parameter is not passed, all callbacks will be unregistered.

 |

**Error codes**:

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onPropertyWriteRequest:(data: ssap.PropertyWriteRequest) => void = (data: ssap.PropertyWriteRequest) => {
  console.info('data:'+ JSON.stringify(data));
}
let server: ssap.Server;
try {
  server = ssap.createServer();
  server.off('propertyWrite', onPropertyWriteRequest);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]on( 'mtuChange')

on(type: 'mtuChange', callback: Callback<number>): void

Subscribes to the MTU change event.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

This parameter must be set to **mtuChange**, indicating the MTU change event.

 |
| 

callback

 | 

Callback<number>

 | 

Yes

 | 

Callback for the MTU change event. You can create such a callback and register it through this API.

 |

**Error codes**:

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onMtuChange:(data: number) => void = (data: number) => {
  console.info('data:'+ data);
}
let server: ssap.Server;
try {
  server = ssap.createServer();
  server.on('mtuChange', onMtuChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]off( 'mtuChange')

off(type: 'mtuChange', callback?: Callback<number>): void

Unsubscribes from the MTU change event.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

This parameter must be set to **mtuChange**, indicating the MTU change event.

 |
| 

callback

 | 

Callback<number>

 | 

No

 | 

Callback to be unregistered, which must be the same as that passed for subscription. If this parameter is not passed, all callbacks will be unregistered.

 |

**Error codes**:

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied

 |
| 

401

 | 

Invalid parameter

 |
| 

801

 | 

Capability not supported

 |

**Example**:

import { ssap } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onMtuChange:(data: number) => void = (data: number) => {
  console.info('data:'+ data);
}
let server: ssap.Server;
try {
  server = ssap.createServer();
  server.off('mtuChange', onMtuChange);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### Service

NearLink service.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

serviceUuid

 | 

string

 | 

No

 | 

No

 | 

Service UUID, for example, **37bea880-fc70-11ea-b720-000000004386**. For details about the UUID format, please refer to [UUID Format for a Standard NearLink Service](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/nearlink-faq#section1263634155618).

 |
| 

properties

 | 

Array<[Property](#section9708731141914)\>

 | 

No

 | 

No

 | 

Property list of a service.

 |

#### Property

Property of a service.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

serviceUuid

 | 

string

 | 

No

 | 

No

 | 

Service UUID, for example, **37bea880-fc70-11ea-b720-000000004386**. For details about the UUID format, please refer to [UUID Format for a Standard NearLink Service](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/nearlink-faq#section1263634155618).

 |
| 

propertyUuid

 | 

string

 | 

No

 | 

No

 | 

Property UUID, in the same format as **serviceUuid**.

 |
| 

value

 | 

ArrayBuffer

 | 

No

 | 

No

 | 

Data value of a property.

 |
| 

descriptors

 | 

Array<[PropertyDescriptor](#section8390185620919)\>

 | 

No

 | 

Yes

 | 

Descriptor list of the current property. By default, this field is not carried if not set.

 |
| 

operation

 | 

number

 | 

No

 | 

Yes

 | 

Indicates the operation supported by a property. The default value is **0**, indicating that no operation is supported. To enable a property to support an operation, you need to assign a value to this parameter, for example, **READABLE|WRITE\_NO\_RESPONSE**. The value range is \[0, 15\]. For details about the operation corresponding to each bit, please refer to [Operation](#section1491191314579).

 |

#### PropertyDescriptor

Descriptor of a property.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

serviceUuid

 | 

string

 | 

No

 | 

No

 | 

Service UUID, for example, **37bea880-fc70-11ea-b720-000000004386**. For details about the UUID format, please refer to [UUID Format for a Standard NearLink Service](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/nearlink-faq#section1263634155618).

 |
| 

propertyUuid

 | 

string

 | 

No

 | 

No

 | 

Property UUID, in the same format as **serviceUuid**.

 |
| 

value

 | 

ArrayBuffer

 | 

No

 | 

No

 | 

Data value of a descriptor.

 |
| 

descriptorType

 | 

[PropertyDescriptorType](#section757023015351)

 | 

No

 | 

No

 | 

Descriptor type of a property.

 |
| 

isWriteable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether a descriptor is writable. **true**: yes; **false**: no. The default value is **true**.

 |

#### PropertyReadRequest

Client property read request.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

address

 | 

string

 | 

No

 | 

No

 | 

Address of a client device. The address format is 11:22:33:AA:BB:FF.

 |
| 

serviceUuid

 | 

string

 | 

No

 | 

No

 | 

Service UUID, for example, **37bea880-fc70-11ea-b720-000000004386**. For details about the UUID format, please refer to [UUID Format for a Standard NearLink Service](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/nearlink-faq#section1263634155618).

 |
| 

propertyUuid

 | 

string

 | 

No

 | 

No

 | 

Property UUID, in the same format as **serviceUuid**.

 |
| 

requestId

 | 

number

 | 

No

 | 

No

 | 

Request ID. The value range is \[0, 65535\].

 |

#### PropertyWriteRequest

Client property write request.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

address

 | 

string

 | 

No

 | 

No

 | 

Address of a client device. The address format is 11:22:33:AA:BB:FF.

 |
| 

serviceUuid

 | 

string

 | 

No

 | 

No

 | 

Service UUID, for example, **37bea880-fc70-11ea-b720-000000004386**. For details about the UUID format, please refer to [UUID Format for a Standard NearLink Service](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/nearlink-faq#section1263634155618).

 |
| 

propertyUuid

 | 

string

 | 

No

 | 

No

 | 

Property UUID, in the same format as **serviceUuid**.

 |
| 

value

 | 

ArrayBuffer

 | 

No

 | 

No

 | 

Value written by the client.

 |
| 

requestId

 | 

number

 | 

No

 | 

No

 | 

Write request ID of the client. This ID must be carried in the response returned by the server. The value range is \[0, 65535\].

 |
| 

writeType

 | 

[PropertyWriteType](#section1976472485918)

 | 

No

 | 

No

 | 

Property write type of the client.

 |

#### ServerResponse

Response to a client request.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

address

 | 

string

 | 

No

 | 

No

 | 

Address of a client device. The address format is 11:22:33:AA:BB:FF.

 |
| 

requestId

 | 

number

 | 

No

 | 

No

 | 

Request ID. The value range is \[0, 65535\].

 |
| 

value

 | 

ArrayBuffer

 | 

No

 | 

No

 | 

Returned data value.

 |

#### ConnectionChangeState

Connection status.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

address

 | 

string

 | 

No

 | 

No

 | 

Address of a remote device. The address format is 11:22:33:AA:BB:FF.

 |
| 

state

 | 

[ConnectionState](../constant-nearlink-common-constants/document.md#section14942121015417)

 | 

No

 | 

No

 | 

Connection status with a remote device.

 |

#### PropertyDescriptorType

Enumerated values of property descriptor types.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

| 
Parameter

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

PROPERTY

 | 

1

 | 

Property.

 |
| 

CLIENT\_PROPERTY\_CONFIG

 | 

2

 | 

Property configuration on the client.

 |
| 

SERVER\_PROPERTY\_CONFIG

 | 

3

 | 

Property configuration on the server.

 |
| 

PROPERTY\_FORMAT

 | 

4

 | 

Property format.

 |
| 

TYPE\_VENDOR

 | 

255

 | 

Manufacturer-defined field.

 |

#### Operation

Enumerated values of operation types supported by a property.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

| 
Parameter

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

READABLE

 | 

0x01

 | 

Indicates the data is readable.

 |
| 

WRITE\_NO\_RESPONSE

 | 

0x02

 | 

Indicates that write requests without responses are supported.

 |
| 

WRITE\_WITH\_RESPONSE

 | 

0x04

 | 

Indicates that write requests with responses are supported.

 |
| 

NOTIFY

 | 

0x08

 | 

Indicates that notifications are supported.

 |

#### PropertyWriteType

Enumerated values of write types supported by a property.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

| 
Parameter

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

WRITE

 | 

1

 | 

Write request, which waits for the server to respond.

 |
| 

WRITE\_NO\_RESPONSE

 | 

2

 | 

Write request, without requiring a response from the server.

 |
