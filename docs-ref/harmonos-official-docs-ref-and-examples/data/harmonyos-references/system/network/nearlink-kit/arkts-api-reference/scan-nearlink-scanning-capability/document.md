# scan (NearLink Scanning Capability)

This module provides NearLink scanning functions.

**Start version**: 5.0.1(13)

#### Module Import

import { scan } from '@kit.NearLinkKit';

#### startScan

startScan(filters: Array<ScanFilters>, options?: ScanOptions): Promise<void>

Starts NearLink scanning. This API returns the result asynchronously through a promise.

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

filters

 | 

Array<[ScanFilters](#section14720175812465)\>

 | 

Yes

 | 

Scan filters, which are used to configure information such as the name and address of the device to be scanned. All fields in **ScanFilters** are optional. If all of these fields are not configured, the **ScanFilters** indicates a set of empty filters and is considered invalid, which will be ignored. Do not leave all **ScanFilters** fields empty for the **filters** parameter. Otherwise, error code 401 will be returned.

 |
| 

options

 | 

[ScanOptions](#section74475912491)

 | 

No

 | 

Scan options. The low-power mode is used by default.

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

import { scan } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let scanFilter: scan.ScanFilters = {
  address:"11:22:33:44:AA:FF", // Address of the peripheral device that is expected to be scanned.
  deviceName:"device name" // Name of the peripheral device that is expected to be scanned.
};
let scanOptions: scan.ScanOptions = {
  scanMode: scan.ScanMode.SCAN\_MODE\_LOW\_POWER
}
try {
  scan.startScan(\[scanFilter\], scanOptions).then(() => {
    console.info("start scan success");
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### stopScan

stopScan(): Promise<void>

Stops NearLink scanning. This API returns the result asynchronously through a promise.

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

import { scan } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  scan.stopScan().then(() => {
    console.info("stop scan success");
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### on( 'deviceFound')

on(type: 'deviceFound', callback: Callback<Array<ScanResults>>): void

Subscribes to NearLink scanning results. The random address of a remote device is carried through the callback.

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

This parameter must be set to **deviceFound**, indicating the NearLink scanned device discovery event.

 |
| 

callback

 | 

Callback<Array<[ScanResults](#section1622511479139)\>>

 | 

Yes

 | 

Callback for NearLink scanning results. You can create such a callback and register it through this API.

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

import { scan } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onReceiveEvent:(data: Array<scan.ScanResults>) => void = (data: Array<scan.ScanResults>) => {
  console.info('scan result addr:'+ data\[0\].address + 'name:' + data\[0\].deviceName);
}
try {
  scan.on("deviceFound", onReceiveEvent);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### off( 'deviceFound')

off(type: 'deviceFound', callback?: Callback<Array<ScanResults>>): void

Unsubscribes from NearLink scanning results.

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

This parameter must be set to **deviceFound**, indicating the NearLink scanned device discovery event.

 |
| 

callback

 | 

Callback<Array<[ScanResults](#section1622511479139)\>>

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

import { scan } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  scan.off('deviceFound');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### ScanResults

Scanning results.

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

Address of a scanned device. The address format is 11:22:33:AA:BB:FF.

 |
| 

rssi

 | 

number

 | 

No

 | 

No

 | 

Received Signal Strength Indicator (RSSI) of a scanned device.

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

Advertising packet data.

 |
| 

deviceName

 | 

string

 | 

No

 | 

No

 | 

Name of a scanned device. The value contains 0 to 30 characters.

 |
| 

isConnectable

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether a scanned device is connectable. **true**: yes; **false**: no.

 |
| 

deviceClass

 | 

[constant.DeviceClass](../constant-nearlink-common-constants/document.md#section1589220571714)

 | 

No

 | 

Yes

 | 

Type of a scanned device.

**Start version**: 5.1.0(18)

 |

#### ScanFilters

Scan filters.

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

Yes

 | 

Device address. By default, this field is not used if not set. The address format is 11:22:33:AA:BB:FF.

 |
| 

deviceName

 | 

string

 | 

No

 | 

Yes

 | 

Device name. The value contains 0 to 30 characters. By default, this field is not used if not set.

 |
| 

manufacturerId

 | 

number

 | 

No

 | 

Yes

 | 

Manufacturer ID. The value range is (0, 65535\]. By default, this field is not used if not set.

 |
| 

manufacturerData

 | 

ArrayBuffer

 | 

No

 | 

Yes

 | 

Manufacturer data. By default, this field is not used if not set. **manufacturerId** must be set along with the field.

 |
| 

manufacturerDataMask

 | 

ArrayBuffer

 | 

No

 | 

Yes

 | 

Manufacturer data mask. By default, this field is not used if not set. This field must be configured together with manufacturerData, and the lengths of the two fields must be the same.

 |

#### ScanOptions

Scan options.

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

scanMode

 | 

[ScanMode](#section757023015351)

 | 

No

 | 

Yes

 | 

Scan mode. The default value is **SCAN\_MODE\_LOW\_POWER**.

 |
| 

duration

 | 

number

 | 

No

 | 

Yes

 | 

Scan duration, in seconds. The value range is \[10, 60\]. Full-time scanning is used by default.

 |

#### ScanMode

Enumerated values of scan modes.

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

SCAN\_MODE\_LOW\_POWER

 | 

0

 | 

Low-power scan mode. The scan frequency and power consumption are low. This is the default value.

 |
| 

SCAN\_MODE\_BALANCED

 | 

1

 | 

Balanced scan mode. The scan frequency and power consumption are medium.

 |
