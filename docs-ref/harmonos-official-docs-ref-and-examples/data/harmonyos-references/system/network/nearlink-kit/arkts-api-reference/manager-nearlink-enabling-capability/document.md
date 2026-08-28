# manager (NearLink Enabling Capability)

This module provides basic NearLink management capabilities, including obtaining device information and subscribing to the status change event.

**Start version**: 5.0.1(13)

#### Module Import

import { manager } from '@kit.NearLinkKit';

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

#### getState

getState(): NearlinkState

Queries NearLink status.

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

[NearlinkState](#section454667203316)

 | 

NearLink status.

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

import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let state: manager.NearlinkState = manager.getState();
  console.info('state:' + JSON.stringify(state));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### getLocalName

getLocalName(): string

Queries the NearLink name on the local device.

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

Local name of the NearLink device. The value contains a maximum of 30 characters.

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

import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let name: string = manager.getLocalName();
  console.info('state:' + JSON.stringify(name));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### getPairedDevices

getPairedDevices(): Array<string>

Obtains the list of devices paired with the current device.

**Required permission**: ohos.permission.ACCESS\_NEARLINK

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 6.0.1(21)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Array<string>

 | 

List of paired device addresses.

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

import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let pairedDevices: Array<string> = manager.getPairedDevices();
  if (pairedDevices.length > 0) {
        console.info('getPairedDevices return: ' + JSON.stringify(pairedDevices));
    } else {
        console.info('No Paired Devices found.');
    }
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### on( 'stateChange')

on(type: 'stateChange', callback: Callback<NearlinkState>): void

Subscribes to the NearLink status change event.

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

This parameter must be set to **stateChange**, indicating the NearLink status change event.

 |
| 

callback

 | 

Callback<[NearlinkState](#section454667203316)\>

 | 

Yes

 | 

Callback for status changes. You can create such a callback and register it through this API.

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

import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<manager.NearlinkState> = (data: manager.NearlinkState) => {
  if (data === manager.NearlinkState.STATE\_TURNING\_ON) {
    console.info('nearlink STATE\_TURNING\_ON');
  } else if (data === manager.NearlinkState.STATE\_ON) {
    console.info('nearlink STATE\_ON');
  } else if (data === manager.NearlinkState.STATE\_TURNING\_OFF) {
    console.info('nearlink STATE\_TURNING\_OFF');
  } else if (data === manager.NearlinkState.STATE\_OFF) {
    console.info('nearlink STATE\_OFF');
  }
};
try {
  manager.on('stateChange', callback);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### off( 'stateChange')

off(type: 'stateChange', callback?: Callback<NearlinkState>): void

Unsubscribes from the NearLink status change event.

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

This parameter must be set to **stateChange**, indicating the NearLink status change event.

 |
| 

callback

 | 

Callback<[NearlinkState](#section454667203316)\>

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

import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  manager.off('stateChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### on( 'pairingStateChange')

on(type: 'pairingStateChange', callback: Callback<PairingStateParam>): void

Subscribes to the pairing request event. The random address of a remote device is carried through the callback.

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

This parameter must be set to **pairingStateChange**, indicating the pairing request event.

 |
| 

callback

 | 

Callback<[PairingStateParam](#section185441313151716)\>

 | 

Yes

 | 

Callback for pairing status changes. You can create such a callback and register it through this API.

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

import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onPairingStateEvent:(data: manager.PairingStateParam) => void = (data: manager.PairingStateParam) => {
  console.info('onPairStateChange addr: '+ data.address + 'state:' + data.state);
}
try {
  manager.on('pairingStateChange', onPairingStateEvent);
} catch (err) {
  console.info('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### off( 'pairingStateChange')

off(type: 'pairingStateChange', callback?: Callback<PairingStateParam>): void

Unsubscribes from the pairing request event.

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

This parameter must be set to **pairingStateChange**, indicating the pairing request event.

 |
| 

callback

 | 

Callback<[PairingStateParam](#section185441313151716)\>

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

import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  manager.off('pairingStateChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### on( 'connectionStateChange')

on(type: 'connectionStateChange', callback: Callback<ConnectionStateParam>): void

Subscribes to the connection status change event. The random address of a remote device is carried through the callback.

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

Callback<[ConnectionStateParam](#section477651052718)\>

 | 

Yes

 | 

Callback for connection status changes. You can create such a callback and register it through this API.

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

import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<manager.ConnectionStateParam> = (data: manager.ConnectionStateParam) => {
  console.info('data:' + JSON.stringify(data));
};
try {
  manager.on('connectionStateChange', callback);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### off( 'connectionStateChange')

off(type: 'connectionStateChange', callback?: Callback<ConnectionStateParam>): void

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

Callback<[ConnectionStateParam](#section477651052718)\>

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

import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  manager.off('connectionStateChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### on('acbStateChange')

on(type: 'acbStateChange', callback: Callback<[AcbStateParam](#section58892382115)\>): void

Subscribes to the logical link connection status change event. The random address of a remote device is carried through the callback.

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

This parameter must be set to **acbStateChange**, indicating the logical link connection status change event.

 |
| 

callback

 | 

Callback<[AcbStateParam](#section58892382115)\>

 | 

Yes

 | 

Callback for logical link connection status changes. You can create such a callback and register it through this API.

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

1009700099

 | 

Operation failed

 |

**Example**:

import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<manager.AcbStateParam> = (data: manager.AcbStateParam) => {
  console.info('data:' + JSON.stringify(data));
};
try {
  manager.on('acbStateChange', callback);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### off( 'acbStateChange')

off(type: 'acbStateChange', callback?: Callback<[AcbStateParam](#section58892382115)\>): void

Unsubscribes from the logical link connection status change event.

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

This parameter must be set to **acbStateChange**, indicating the logical link connection status change event.

 |
| 

callback

 | 

Callback<[AcbStateParam](#section58892382115)\>

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

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

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

import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  manager.off('acbStateChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### PairingStateParam

Result of the pairing status change event.

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

Device address, indicating that the pairing status with the device changes. The address format is 11:22:33:AA:BB:FF.

 |
| 

preState

 | 

[PairingState](../constant-nearlink-common-constants/document.md#section1976472485918)

 | 

No

 | 

No

 | 

Pairing status before this report.

 |
| 

state

 | 

[PairingState](../constant-nearlink-common-constants/document.md#section1976472485918)

 | 

No

 | 

No

 | 

Current pairing status.

 |
| 

reason

 | 

[PairingReason](#section985712528369)

 | 

No

 | 

No

 | 

Cause value.

 |

#### PairingRequestParam

Result of the pairing request event.

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

Device address, indicating that the pairing request from the device is received. The address format is 11:22:33:AA:BB:FF.

 |
| 

passkey

 | 

string

 | 

No

 | 

No

 | 

Code for pairing interaction, which is displayed to you for confirmation. The value is a string of six digits.

 |
| 

pairingType

 | 

[PairingType](#section1080014428381)

 | 

No

 | 

No

 | 

Pairing type.

 |

#### ConnectionStateParam

Result of the connection status change event.

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

Device address, indicating that the connection status with the device changes. The address format is 11:22:33:AA:BB:FF.

 |
| 

preState

 | 

[ConnectionState](../constant-nearlink-common-constants/document.md#section14942121015417)

 | 

No

 | 

No

 | 

Connection status before this report.

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

Current connection status.

 |
| 

connectionReason

 | 

[ConnectionReason](#section189609817294)

 | 

No

 | 

No

 | 

Cause value.

 |

#### NearlinkState

Enumerated values of NearLink statuses.

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

STATE\_TURNING\_ON

 | 

0

 | 

NearLink is being turned on.

 |
| 

STATE\_ON

 | 

1

 | 

NearLink has been turned on.

 |
| 

STATE\_TURNING\_OFF

 | 

2

 | 

NearLink is being turned off.

 |
| 

STATE\_OFF

 | 

3

 | 

NearLink has been turned off.

 |

#### PairingReason

Enumerated values of causes of the NearLink pairing status change result.

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

PAIRING\_REASON\_SUCCESS

 | 

0

 | 

The pairing is successful.

 |
| 

PAIRING\_REASON\_FAILURE

 | 

1

 | 

The pairing fails.

 |
| 

PAIRING\_REASON\_PROFILE\_UNSUPPORTED

 | 

2

 | 

The pairing fails because the remote device does not support the service.

**Start version**: 5.1.0(18)

 |
| 

PAIRING\_REASON\_EXCEED\_ACB\_MAX

 | 

3

 | 

The pairing fails because the number of connected devices has reached the upper limit.

**Start version**: 5.1.0(18)

 |
| 

PAIRING\_REASON\_REMOTE\_CANCELED

 | 

4

 | 

The pairing fails because the remote device cancels the pairing.

**Start version**: 5.1.0(18)

 |
| 

PAIRING\_REASON\_LOCAL\_CANCELED

 | 

5

 | 

The pairing fails because the local device cancels the pairing.

**Start version**: 5.1.0(18)

 |

#### PairingType

Enumerated values of NearLink pairing types.

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

NO\_PASSKEY\_CONFIRMATION

 | 

0

 | 

Pairing type that does not require a passkey. Users do not need to check the pairing code.

 |
| 

PAIRING\_TYPE\_PASSCODE

 | 

1

 | 

Pairing type with passcode authentication. Users need to enter the pairing code displayed on one device into the other device.

**Start version**: 5.1.0(18)

 |
| 

PAIRING\_TYPE\_NUMBER\_COMPARE

 | 

2

 | 

Pairing type with number comparison-based authentication. Users must ensure that the pairing codes on both devices are the same.

**Start version**: 5.1.0(18)

 |

#### ConnectionReason

Cause value of the result of a NearLink connection status change.

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

CONNECTION\_SUCCESS

 | 

0

 | 

The connection is successful.

 |
| 

CONNECTION\_FAILURE

 | 

1

 | 

The connection fails.

 |

#### AcbStateParam

Result of the logical link connection status change event.

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

Device address, indicating that the logical link connection status with the device changes. The address format is 11:22:33:AA:BB:FF.

 |
| 

state

 | 

[AcbState](../constant-nearlink-common-constants/document.md#section144650555553)

 | 

No

 | 

No

 | 

Current logical link connection status.

 |
