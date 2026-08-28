# dataTransfer (NearLink Data Transfer Capability)

This module provides the NearLink data transfer capability.

**Start version**: 5.1.0(18)

#### Module Import

import { dataTransfer } from '@kit.NearLinkKit';

#### ConnectionState

type ConnectionState = [constant.ConnectionState](../constant-nearlink-common-constants/document.md#section14942121015417)

Enumerated values of connection statuses with a remote device.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

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

#### createPort

createPort(uuid: string): void

Registers a port.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

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

uuid

 | 

string

 | 

Yes

 | 

Set this parameter to a16-byte base UUID or a 2-byte UUID of a standardized NearLink service that supports data transfer. For details about the UUID format, please refer to [UUID Format for a Standard NearLink Service](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/nearlink-faq#section1263634155618).

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

1009700020

 | 

The UUID is already registered

 |
| 

1009700021

 | 

Port is exceeds the upper limit

 |
| 

1009700099

 | 

Operation failed

 |

**Example**:

import { dataTransfer} from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let uuid: string = 'FFFFFFFF-FC70-11EA-B720-000078951234'; // NearLink service UUID.
  dataTransfer.createPort(uuid);
  console.info('create port success');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### destroyPort

destroyPort(uuid: string): void

Destroys a port.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

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

uuid

 | 

string

 | 

Yes

 | 

Set this parameter to a16-byte base UUID or a 2-byte UUID of a standardized NearLink service that supports data transfer. For details about the UUID format, please refer to [UUID Format for a Standard NearLink Service](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/nearlink-faq#section1263634155618).

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

1009700022

 | 

The UUID is not registered

 |
| 

1009700099

 | 

Operation failed

 |

**Example**:

import { dataTransfer} from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let uuid: string = 'FFFFFFFF-FC70-11EA-B720-000078951234'; // NearLink service UUID.
  dataTransfer.destroyPort(uuid);
  console.info('destroy port success');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### connect

connect(params: ConnectionParams): Promise<void>

Connects to a remote device and establishes a port. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

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

params

 | 

[ConnectionParams](#section85111632162516)

 | 

Yes

 | 

Parameters for port connection.

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

import { dataTransfer} from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Construct parameters for establishing a port.
  let connectionParams:dataTransfer.ConnectionParams = {
    address: '01:02:03:04:05:06', // Address of the remote NearLink device.
    uuid: '37BEA880-FC70-11EA-B720-00000000060D', // NearLink service UUID.
    mtu: 1024, // Size of the data packet expected to be sent, in bytes. This parameter is optional.
  };
  dataTransfer.connect(connectionParams).then(()=>{
    console.info('connect success');
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### disconnect

disconnect(params: ConnectionParams): Promise<void>

Disconnects from a remote device and destroys a port. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

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

params

 | 

[ConnectionParams](#section85111632162516)

 | 

Yes

 | 

Parameters for port connection.

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

import { dataTransfer} from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Construct parameters for establishing a port.
  let connectionParams:dataTransfer.ConnectionParams = {
    address: '01:02:03:04:05:06', // Address of the remote NearLink device.
    uuid: '37BEA880-FC70-11EA-B720-00000000060D', // NearLink service UUID.
    mtu: 1024, // Size of the data packet expected to be sent, in bytes. This parameter is optional.
  };
  dataTransfer.disconnect(connectionParams).then(()=>{
    console.info('disconnect success');
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### on('connectionStateChanged')

on(type: 'connectionStateChanged', callback: Callback<ConnectionResult>): void

Subscribes to the port connection status change event.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

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

This parameter must be set to **connectionStateChanged**, indicating the port connection status change event.

 |
| 

callback

 | 

Callback<[ConnectionResult](#section149561050194010)\>

 | 

Yes

 | 

Callback for port connection status changes. You can create such a callback and register it through this API.

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

1009700099

 | 

Operation failed

 |

**Example**:

import { dataTransfer} from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<dataTransfer.ConnectionResult> = (data: dataTransfer.ConnectionResult) => {
  console.info('data: ' + JSON.stringify(data));
};
try {
  dataTransfer.on('connectionStateChanged', callback);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### off('connectionStateChanged')

off(type: 'connectionStateChanged', callback?: Callback<ConnectionResult>): void

Unsubscribes from the port connection status change event.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

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

This parameter must be set to **connectionStateChanged**, indicating the port connection status change event.

 |
| 

callback

 | 

Callback<[ConnectionResult](#section149561050194010)\>

 | 

No

 | 

Callback to be unregistered, which must be the same as that passed for subscription. If this parameter is not passed, all callbacks will be unregistered.

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

1009700099

 | 

Operation failed

 |

**Example**:

import { dataTransfer} from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dataTransfer.off('connectionStateChanged');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### getConnectionState

getConnectionState(params: ConnectionStateParams): ConnectionState

Obtains the connection status of the port channel between a local device and a remote device.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

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

params

 | 

[ConnectionStateParams](#section1230716832813)

 | 

Yes

 | 

Parameters for port connection.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ConnectionState](../constant-nearlink-common-constants/document.md#section14942121015417)

 | 

NearLink port channel connection status with a remote device.

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

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

 |
| 

801

 | 

Capability not supported

 |
| 

1009700003

 | 

NearLink is off

 |
| 

1009700099

 | 

Operation failed

 |

**Example**:

import { dataTransfer } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let connectionStateParams:dataTransfer.ConnectionStateParams = {
    address: '01:02:03:04:05:06', // Address of the remote device obtained through scanning.
    uuid: 'FFFFFFFF-FC70-11EA-B720-000078951234' // NearLink service UUID.
  };
  let state:dataTransfer.ConnectionState = dataTransfer.getConnectionState (connectionStateParams);
  console.info('state:' + JSON.stringify(state));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### writeData

writeData(params: DataParams): Promise<void>

Sends data to a remote device using the device address and UUID. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

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

params

 | 

[DataParams](#section181874974014)

 | 

Yes

 | 

Parameters for data sending, including the remote device address, service UUID, and data packet to be sent.

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

1009700023

 | 

Write data congest

 |
| 

1009700099

 | 

Operation failed

 |

**Example**:

import { dataTransfer} from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Construct parameters for data sending.
  let transferValueBuffer: Uint8Array = new Uint8Array(4);
  transferValueBuffer\[0\] = 1;
  transferValueBuffer\[1\] = 2;
  transferValueBuffer\[2\] = 3;
  transferValueBuffer\[3\] = 4;
  let dataParams: dataTransfer.DataParams = {
    address: '01:02:03:04:05:06', // Address of the remote NearLink device.
    uuid: '37BEA880-FC70-11EA-B720-00000000060D', // NearLink service UUID.
    data: transferValueBuffer.buffer, // Data transferred between NearLink devices.
  };
  dataTransfer.writeData(dataParams).then(() => {
    console.info('writeData success');
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### on('readData')

on(type: 'readData', callback: Callback<DataParams>): void

Subscribes to the port data receiving event.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

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

This parameter must be set to **readData**, indicating the port data receiving event.

 |
| 

callback

 | 

Callback<[DataParams](#section181874974014)\>

 | 

Yes

 | 

Callback for the port data receiving event. You can create such a callback and register it through this API.

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

1009700099

 | 

Operation failed

 |

**Example**:

import { dataTransfer} from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<dataTransfer.DataParams> = (data: dataTransfer.DataParams) => {
  console.info('data: ' + JSON.stringify(data));
};
try {
  dataTransfer.on('readData', callback);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### off('readData')

off(type: 'readData', callback?: Callback<DataParams>): void

Unsubscribes from the port data receiving event.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

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

This parameter must be set to **readData**, indicating the port data receiving event.

 |
| 

callback

 | 

Callback<[DataParams](#section181874974014)\>

 | 

No

 | 

Callback to be unregistered, which must be the same as that passed for subscription. If this parameter is not passed, all callbacks will be unregistered.

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

1009700099

 | 

Operation failed

 |

**Example**:

import { dataTransfer} from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dataTransfer.off('readData');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### ConnectionParams

Parameters for port connection.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

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

Address of a remote NearLink device. The address format is 11:22:33:AA:BB:FF.

 |
| 

uuid

 | 

string

 | 

No

 | 

No

 | 

NearLink service UUID, for example, **37bea880-fc70-11ea-b720-000000004386**. For details about the UUID format, please refer to [UUID Format for a Standard NearLink Service](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/nearlink-faq#section1263634155618).

 |
| 

mtu

 | 

number

 | 

No

 | 

Yes

 | 

Size of the data packet expected to be sent, in bytes. The value range is \[0, 65535\]. The default value is **512**.

 |
| 

transferMode

 | 

[TransferMode](#section757023015351)

 | 

No

 | 

Yes

 | 

Data transfer mode with a remote device. The default value is **BASIC**.

 |

#### DataParams

Parameters for data sending and receiving through a port.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

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

Address of a remote NearLink device. The address format is 11:22:33:AA:BB:FF.

 |
| 

uuid

 | 

string

 | 

No

 | 

No

 | 

NearLink service UUID, for example, **37bea880-fc70-11ea-b720-000000004386**. For details about the UUID format, please refer to [UUID Format for a Standard NearLink Service](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/nearlink-faq#section1263634155618).

 |
| 

data

 | 

ArrayBuffer

 | 

No

 | 

No

 | 

Data packet to be sent.

 |

#### ConnectionResult

Result of parameter negotiation with a remote device.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

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

Address of a remote NearLink device. The address format is 11:22:33:AA:BB:FF.

 |
| 

uuid

 | 

string

 | 

No

 | 

No

 | 

NearLink service UUID, for example, **37bea880-fc70-11ea-b720-000000004386**. For details about the UUID format, please refer to [UUID Format for a Standard NearLink Service](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/nearlink-faq#section1263634155618).

 |
| 

mtu

 | 

number

 | 

No

 | 

No

 | 

Negotiated packet size of data to be sent and received, in bytes. The value range is \[0, 65535\].

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

#### ConnectionStateParams

Parameters for obtaining port channel connection statuses.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

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

Address of a remote NearLink device. The address format is 11:22:33:AA:BB:FF.

 |
| 

uuid

 | 

string

 | 

No

 | 

No

 | 

NearLink service UUID, for example, **37bea880-fc70-11ea-b720-000000004386**. For details about the UUID format, please refer to [UUID Format for a Standard NearLink Service](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/nearlink-faq#section1263634155618).

 |

#### TransferMode

Enumerated values of data transfer modes with a remote device.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

| 
Parameter

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

BASIC

 | 

0

 | 

Basic mode, without a data retransfer mechanism.

 |
| 

RELIABLE

 | 

1

 | 

Reliable mode, with a data retransfer mechanism.

 |
