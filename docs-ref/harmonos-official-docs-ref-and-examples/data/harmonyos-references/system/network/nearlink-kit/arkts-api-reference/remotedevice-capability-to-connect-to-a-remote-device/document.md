# remoteDevice (Capability to Connect to a Remote Device)

This module provides functions such as querying remote device information as well as starting and stopping connections.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

#### Module Import

import { remoteDevice } from '@kit.NearLinkKit';

#### PairingState

type PairingState = [constant.PairingState](../constant-nearlink-common-constants/document.md#section1976472485918)

Enumerated values of pairing statuses with a remote device.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[constant.PairingState](../constant-nearlink-common-constants/document.md#section1976472485918)

 | 

Pairing status with a remote device.

 |

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

#### DeviceClass

type DeviceClass = [constant.DeviceClass](../constant-nearlink-common-constants/document.md#section1589220571714)

Enumerated values of device types.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[constant.DeviceClass](../constant-nearlink-common-constants/document.md#section1589220571714)

 | 

Device type.

 |

#### AcbState

type AcbState = [constant.AcbState](../constant-nearlink-common-constants/document.md#section144650555553)

Enumerated values of logical link connection statuses with a remote device.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[constant.AcbState](../constant-nearlink-common-constants/document.md#section144650555553)

 | 

Logical link connection status with a remote device.

 |

#### createRemoteDevice

createRemoteDevice(address: string): RemoteDevice

Creates a remote device instance.

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

Address of a remote device. The address format is 11:22:33:AA:BB:FF.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[RemoteDevice](#section124191030153618)

 | 

Remote device instance.

 |

**Error codes**:

| 
Error Code

 | 

Message

 |
| :-- | :-- |
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

import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  console.info('device: ' + JSON.stringify(device));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### RemoteDevice

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/Siovv4BRQu-AhPoGVxA6LQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062344Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D127FD4786433EF1F075AD4CE586335C1E83E0FBEF8E7A3CB3DAEBFF7E0CDC3F)

It provides the method for operating on a remote device. Before using this API, you need to use the [remoteDevice.createRemoteDevice](#section1855815061418) method to create a [RemoteDevice](#section124191030153618) instance. You need to create only one instance for a device.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

#### \[h2\]startPairing

startPairing(): Promise<void>

Initiates pairing with a remote device. This API returns the result asynchronously through a promise. After the pairing is initiated, different types of dialog boxes will be displayed based on the input and output capability flags of both the local and remote devices. The user will need to confirm the pairing.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

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

import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  device.startPairing().then(()=>{
    console.info('start pairing success');
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]getPairingState

getPairingState(): PairingState

Obtains the pairing status with a remote device.

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

[PairingState](../constant-nearlink-common-constants/document.md#section1976472485918)

 | 

Pairing status with a remote device.

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

import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  let state: remoteDevice.PairingState = device.getPairingState();
  console.info('state:' + JSON.stringify(state));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]getDeviceName

getDeviceName(): string

Obtains the name of a remote device.

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

string

 | 

Name of a remote device. The value contains a maximum of 30 characters.

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

import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  let name: string = device.getDeviceName();
  console.info('state:' + JSON.stringify(name));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]getDeviceClass

getDeviceClass(): DeviceClass

Obtains the type of a remote device.

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

[DeviceClass](../constant-nearlink-common-constants/document.md#section1589220571714)

 | 

Type of a remote device.

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

import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  let type: remoteDevice.DeviceClass = device.getDeviceClass();
  console.info('type:' + JSON.stringify(type));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]getConnectionState

getConnectionState(): ConnectionState

Obtains the connection status between the local device and a remote device.

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

[ConnectionState](../constant-nearlink-common-constants/document.md#section14942121015417)

 | 

Connection status between the local device and a remote device.

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

import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  let state: remoteDevice.ConnectionState = device.getConnectionState();
  console.info('state:' + JSON.stringify(state));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### \[h2\]getAcbState

getAcbState(): AcbState

Obtains the logical link connection status with a remote device.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[AcbState](../constant-nearlink-common-constants/document.md#section144650555553)

 | 

Logical link connection status with a remote device.

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

import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

  let addr: string = '00:11:22:33:AA:FF'; // Address of the remote device obtained through scanning.
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  let state: remoteDevice.AcbState = device.getAcbState();
  console.info('state:' + JSON.stringify(state));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
