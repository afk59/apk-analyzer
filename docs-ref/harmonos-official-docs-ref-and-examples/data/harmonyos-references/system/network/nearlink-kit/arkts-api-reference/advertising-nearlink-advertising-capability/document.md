# advertising (NearLink Advertising Capability)

This module provides Nearlink advertising functions, including starting and stopping advertising as well as subscribing to advertising status.

**Start version**: 5.0.1(13)

#### Module Import

import { advertising } from '@kit.NearLinkKit';

#### AdvertisingParams

Parameters carried during advertising.

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

advertisingSettings

 | 

[AdvertisingSettings](#section1525727766)

 | 

No

 | 

No

 | 

Advertising settings.

 |
| 

advertisingData

 | 

[AdvertisingData](#section1235325161112)

 | 

No

 | 

No

 | 

Advertising data packets.

 |

#### AdvertisingSettings

Advertising settings.

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

interval

 | 

number

 | 

No

 | 

Yes

 | 

Advertising interval. The value ranges from 160 to 16777215, in slots. The default value is **5000**. One slot is equal to 0.125 milliseconds. Example: 5000 slots = 625 ms.

 |
| 

power

 | 

[TxPowerMode](#section185441313151716)

 | 

No

 | 

Yes

 | 

Advertising transmission power. If it is not set, the default value **ADV\_TX\_POWER\_LOW** will be used.

 |
| 

isConnectable

 | 

boolean

 | 

No

 | 

Yes

 | 

**true**: advertising connectable. **false**: advertising not connectable. The default value is **true**.

 |

#### AdvertisingData

Advertising data packets.

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

serviceUuids

 | 

Array<string>

 | 

No

 | 

Yes

 | 

Service UUID list. By default, this field is not carried if not set. For details about the UUID format, please refer to [UUID Format for a Standard NearLink Service](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/nearlink-faq#section1263634155618).

 |
| 

manufacturerData

 | 

Array<[ManufacturerData](#section1622511479139)\>

 | 

No

 | 

Yes

 | 

Manufacturer data. By default, this field is not carried if not set.

 |
| 

serviceData

 | 

Array<[ServiceData](#section15831210191613)\>

 | 

No

 | 

Yes

 | 

Service data. By default, this field is not carried if not set.

 |
| 

includeDeviceName

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the advertising data contains the local device name. **true**: yes. **false**: no. The default value is **false**.

 |

#### ManufacturerData

Manufacturer data.

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

manufacturerId

 | 

number

 | 

No

 | 

No

 | 

Manufacturer ID. The value range is (0, 65535\].

 |
| 

manufacturerData

 | 

ArrayBuffer

 | 

No

 | 

No

 | 

Manufacturer data.

 |

#### ServiceData

Service-related data.

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

Service UUID. For details about the UUID format, please refer to [UUID Format for a Standard NearLink Service](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/nearlink-faq#section1263634155618).

 |
| 

serviceData

 | 

ArrayBuffer

 | 

No

 | 

No

 | 

Service data.

 |

#### AdvertisingStateChangeInfo

Advertising status change information.

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

advertisingId

 | 

number

 | 

No

 | 

No

 | 

Advertising ID. The value range is \[0, 255\].

 |
| 

state

 | 

[AdvertisingState](#section757023015351)

 | 

No

 | 

No

 | 

Current advertising status.

 |

#### TxPowerMode

Enumerated value of an advertising mode.

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

ADV\_TX\_POWER\_LOW

 | 

1

 | 

Low-power mode.

 |
| 

ADV\_TX\_POWER\_MEDIUM

 | 

2

 | 

Medium-power mode.

 |
| 

ADV\_TX\_POWER\_HIGH

 | 

3

 | 

High-power mode.

 |

#### AdvertisingState

Enumerated value of advertising status.

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

STARTED

 | 

1

 | 

Advertising has been started.

 |
| 

STOPPED

 | 

2

 | 

Advertising has been stopped.

 |

#### startAdvertising

startAdvertising(advertisingParams: AdvertisingParams): Promise<number>

Starts NearLink advertising. This API returns the result asynchronously through a promise.

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

advertisingParams

 | 

[AdvertisingParams](#section295015817218)

 | 

Yes

 | 

Advertising-related parameters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<number>

 | 

Promise used to return the advertising ID. An advertising ID is a unique identifier value randomly allocated.

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

import { advertising } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let manufactureValueBuffer = new Uint8Array(4);
manufactureValueBuffer\[0\] = 1;
manufactureValueBuffer\[1\] = 2;
manufactureValueBuffer\[2\] = 3;
manufactureValueBuffer\[3\] = 4;
let serviceValueBuffer = new Uint8Array(4);
serviceValueBuffer\[0\] = 4;
serviceValueBuffer\[1\] = 6;
serviceValueBuffer\[2\] = 7;
serviceValueBuffer\[3\] = 8;
console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
let setting: advertising.AdvertisingSettings = {
  interval:5000,
  power:advertising.TxPowerMode.ADV\_TX\_POWER\_LOW
};
let manufactureDataUnit: advertising.ManufacturerData = {
  manufacturerId:4567,
  manufacturerData:manufactureValueBuffer.buffer
};
let serviceDataUnit: advertising.ServiceData = {
  serviceUuid:"37bea880-fc70-11ea-b720-000000001234",
  serviceData:serviceValueBuffer.buffer
};
let advData: advertising.AdvertisingData = {
  serviceUuids:\["37bea880-fc70-11ea-b720-000000001234"\],
  manufacturerData:\[manufactureDataUnit\],
  serviceData:\[serviceDataUnit\]
};
let advertisingParams: advertising.AdvertisingParams = {
  advertisingSettings: setting,
  advertisingData: advData
}
let advId = -1;
try {
  advertising.startAdvertising(advertisingParams).then((advertisingId:number) => {
    advId = advertisingId;
    console.info('advertising id:'+ JSON.stringify(advId));
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### stopAdvertising

stopAdvertising(advertisingId: number): Promise<void>

Stops NearLink advertising. This API returns the result asynchronously through a promise.

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

advertisingId

 | 

number

 | 

Yes

 | 

Advertising ID, which is obtained when advertising is started. The value range is \[0, 255\].

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

import { advertising } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let advId: number = 1; // **advId** is obtained when advertising is started. For details, please refer to return values of the **startAdvertising** API.
  advertising.stopAdvertising(advId).then(() => {
    console.info("stop advertising success");
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### on( 'advertisingStateChange')

on(type: 'advertisingStateChange', callback: Callback<AdvertisingStateChangeInfo>): void

Subscribes to the NearLink advertising status change event.

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

NearLink advertising status change event, which must be set to **advertisingStateChange**.

 |
| 

callback

 | 

Callback<[AdvertisingStateChangeInfo](#section188870256234)\>

 | 

Yes

 | 

Callback for advertising status changes.

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

import { advertising } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onReceiveEvent:(data: advertising.AdvertisingStateChangeInfo) => void = (data: advertising.AdvertisingStateChangeInfo) => {
  console.info('advertisingId:'+ data.advertisingId);
  console.info('advertisingState:'+ data.state);
}
try {
  advertising.on('advertisingStateChange', onReceiveEvent);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### off( 'advertisingStateChange')

off(type: 'advertisingStateChange', callback?: Callback<AdvertisingStateChangeInfo>): void

Unsubscribes from the NearLink advertising status change event.

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

NearLink advertising status change event, which must be set to **advertisingStateChange**.

 |
| 

callback

 | 

Callback<[AdvertisingStateChangeInfo](#section188870256234)\>

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

import { advertising } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  advertising.off('advertisingStateChang_e_');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
