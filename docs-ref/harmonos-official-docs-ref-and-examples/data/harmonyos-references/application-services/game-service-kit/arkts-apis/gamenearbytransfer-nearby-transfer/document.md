# gameNearbyTransfer (Nearby Transfer)

This module provides the nearby transfer capability of Game Service Kit.

**Start version**: 5.1.0(18)

#### Module Import

import { gameNearbyTransfer } from '@kit.GameServiceKit';

#### CreateParameters

Parameter creation class.

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

moduleName

 | 

string

 | 

No

 | 

No

 | 

Module name. The value length range is \[1, 1024\].

 |
| 

abilityName

 | 

string

 | 

No

 | 

No

 | 

Ability name. The value length range is \[1, 1024\].

 |
| 

needShowSystemUI

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to display the system UI.

-   **true**: yes
-   **false**: no

The default value is **false**.

 |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

No

 | 

Yes

 | 

**UIAbility** context. This parameter is mandatory when **needShowSystemUI** is set to **true**.

 |
| 

mode

 | 

[Mode](#section133441432193816)

 | 

No

 | 

Yes

 | 

Connection mode. The API mode is used by default.

**Start version**: 6.0.0(20)

 |

#### ConnectNotification

Connection notification class.

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

connectState

 | 

[ConnectState](#section13891254145017)

 | 

No

 | 

No

 | 

Connection status.

 |
| 

message

 | 

string

 | 

No

 | 

Yes

 | 

Message about the connection result.

 |
| 

remoteDeviceName

 | 

string

 | 

No

 | 

Yes

 | 

Name of a remote device.

 |

#### BindParameters

Binding parameter class.

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 6.0.0(20)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

deviceId

 | 

string

 | 

No

 | 

No

 | 

Device ID. The value length range is \[1, 128\].

 |
| 

networkId

 | 

string

 | 

No

 | 

No

 | 

Device network ID. The value length range is \[1, 128\].

 |

#### NearbyGameDevice

Class of the device that uses the nearby transfer service.

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 6.0.0(20)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

deviceName

 | 

string

 | 

No

 | 

No

 | 

Device name.

 |
| 

deviceId

 | 

string

 | 

No

 | 

No

 | 

Device ID.

 |
| 

networkId

 | 

string

 | 

No

 | 

No

 | 

Device network ID.

 |

#### DiscoveryResult

Discovery result class.

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 6.0.0(20)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

nearbyGameDevices

 | 

Array<[NearbyGameDevice](#section12406114523413)\>

 | 

No

 | 

No

 | 

List of discovered devices.

 |

#### CreateResult

Result creation class.

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

localDeviceName

 | 

string

 | 

No

 | 

No

 | 

Name of the local device.

 |

#### TransferNotification

Transfer notification class.

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

transferState

 | 

[TransferState](#section1346841562510)

 | 

No

 | 

No

 | 

Transfer status.

 |
| 

transferInfo

 | 

[TransferInfo](#section12485171912281)

 | 

No

 | 

No

 | 

Transfer information.

 |
| 

fileStoragePath

 | 

string

 | 

No

 | 

Yes

 | 

Path for storing received files in the receiver app, which is a sandbox path. For details, please refer to [Application Sandbox](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory). This parameter is returned after the file transfer is complete.

 |

#### FileInfo

File information class.

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

No

 | 

No

 | 

File path, which is a sandbox path. For details, please refer to [Application Sandbox](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory). The value length range is \[1, 2048\].

 |
| 

hash

 | 

string

 | 

No

 | 

Yes

 | 

Hash value of a file. The value length range is \[0, 256\].

 |

#### PackageInfo

Package information class.

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

name

 | 

string

 | 

No

 | 

Yes

 | 

Package name. The value length range is \[0, 2048\].

 |
| 

version

 | 

string

 | 

No

 | 

Yes

 | 

Version number, whose format can be defined by yourself. The value length range is \[0, 256\].

 |
| 

files

 | 

Array<[FileInfo](#section3844175954711)\>

 | 

No

 | 

Yes

 | 

File list. The list contains a maximum of 10,000 files.

 |
| 

extraData

 | 

string

 | 

No

 | 

Yes

 | 

Extended data. The value length range is \[0, 2048\].

 |

#### PackageFile

Class of package files to be transferred.

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

srcPath

 | 

string

 | 

No

 | 

No

 | 

Source file path, which is a sandbox path of the sender app. For details, please refer to [Application Sandbox](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory). The value length range is \[1, 2048\]. Complete path.

 |
| 

destPath

 | 

string

 | 

No

 | 

No

 | 

Destination file path, which is a sandbox path of the receiver app. For details, please refer to [Application Sandbox](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory). The value length range is \[1, 2048\]. Relative path. The complete path is [fileStoragePath](#section116223815415)+**destPath**.

 |

#### PackageData

Class of package data to be transferred.

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

name

 | 

string

 | 

No

 | 

Yes

 | 

Package name. The value length range is \[0, 2048\].

 |
| 

version

 | 

string

 | 

No

 | 

Yes

 | 

Version number. The value length range is \[0, 256\].

 |
| 

files

 | 

Array<[PackageFile](#section1535311105717)\>

 | 

No

 | 

No

 | 

List of files to be transferred. The list contains a maximum of 10,000 files.

 |

#### ReturnResult

Return result class.

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

code

 | 

number

 | 

No

 | 

No

 | 

Result code. For details, see [NearbyTransferErrorCode](#section5696144516164).

 |
| 

message

 | 

string

 | 

No

 | 

Yes

 | 

Error message.

 |

#### PackageInfoResult

Class of the package information comparison result.

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

packageInfoResultCode

 | 

[PackageInfoResultCode](#section247073673213)

 | 

No

 | 

No

 | 

Comparison result code.

 |
| 

message

 | 

string

 | 

No

 | 

Yes

 | 

Information about the comparison result.

 |

#### TransferInfo

Transfer information class.

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

expectedTime

 | 

number

 | 

No

 | 

No

 | 

Remaining transfer time, in seconds.

 |
| 

transferredPackageSize

 | 

number

 | 

No

 | 

No

 | 

Transferred package size, in bytes.

 |
| 

totalPackageSize

 | 

number

 | 

No

 | 

No

 | 

Total package size, in bytes.

 |
| 

rate

 | 

number

 | 

No

 | 

No

 | 

Transfer rate, in bytes/s.

 |

#### Mode

Enumerates connection modes.

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 6.0.0(20)

| 
**Parameter**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

API

 | 

1

 | 

API mode. That is, connect to the nearby transfer service using relevant APIs.

 |
| 

KNOCK

 | 

2

 | 

Knock mode. For details, please refer to [Tap to Transfer](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/knock-share).

 |

#### ConnectState

Enumeration object of connection statuses.

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

| 
**Parameter**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

CONNECTED

 | 

0

 | 

Connected.

 |
| 

DISCONNECTED

 | 

1

 | 

Disconnected.

 |

#### TransferState

Enumeration object of transfer statuses.

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

| 
**Parameter**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

SEND\_START

 | 

0

 | 

About to send.

 |
| 

SEND\_PROCESS

 | 

1

 | 

Sending.

 |
| 

SEND\_FINISH

 | 

2

 | 

Sent.

 |
| 

SEND\_ERROR

 | 

3

 | 

Sending error.

 |
| 

RECEIVE\_START

 | 

4

 | 

About to receive.

 |
| 

RECEIVE\_PROCESS

 | 

5

 | 

Receiving.

 |
| 

RECEIVE\_FINISH

 | 

6

 | 

Received.

 |
| 

RECEIVE\_ERROR

 | 

7

 | 

Receiving error.

 |

#### PackageInfoResultCode

Enumerates the package information comparison result codes.

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

| 
**Parameter**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

ERROR

 | 

\-1

 | 

Comparison error.

 |
| 

PACKAGE\_AVAILABLE\_COMPARED

 | 

0

 | 

Available after comparison.

 |
| 

PACKAGE\_UNAVAILABLE\_COMPARED

 | 

1

 | 

Unavailable after comparison.

 |

#### NearbyTransferErrorCode

Error code class.

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Parameter**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

INTERNAL\_ERROR

 | 

1018300001

 | 

Internal system error.

 |
| 

AUTH\_FAILED

 | 

1018300002

 | 

Authentication failure.

 |
| 

INVALID\_REQUEST

 | 

1018300003

 | 

Invalid request.

 |
| 

NO\_SERVICE\_AVAILABLE

 | 

1018300004

 | 

Service unavailable.

 |
| 

WLAN\_BLUETOOTH\_MUST\_BE\_ON

 | 

1018300005

 | 

WLAN and Bluetooth must be enabled at the same time.

 |
| 

PUBLISH\_FAILED

 | 

1018300006

 | 

Publishing failed.

 |
| 

DISCOVERY\_FAILED

 | 

1018300007

 | 

Discovery failed.

 |
| 

INVALID\_PARAMETER

 | 

1018300008

 | 

Invalid parameter.

**Start version**: 6.0.0(20)

 |

#### gameNearbyTransfer.on('connectNotify')

on(type: 'connectNotify', callback: Callback<ConnectNotification>): void

Subscribes to the connection notification event. This API returns the result through a callback.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event to be monitored. The **connectNotify** event is supported and will be triggered after a link is set up.

 |
| 

callback

 | 

Callback<[ConnectNotification](#section12288563197)\>

 | 

Yes

 | 

Callback that returns the connection notification object.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

Parameter error. Possible causes: 3. Parameter verification failed.

 |

**Example**:

import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";

try {
  gameNearbyTransfer.on('connectNotify', connectNotifyCallBack);
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}

function connectNotifyCallBack(callback: gameNearbyTransfer.ConnectNotification) {
  hilog.info(0x0000, '\[nearby\]', '%{public}s', callback.connectState);
}

#### gameNearbyTransfer.off('connectNotify')

off(type: 'connectNotify', callback?: Callback<ConnectNotification>): void

Unsubscribes from the connection notification event. This API returns the result through a callback.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event to be monitored. The **connectNotify** event is supported and will be triggered after a link is set up.

 |
| 

callback

 | 

Callback<[ConnectNotification](#section12288563197)\>

 | 

No

 | 

Callback that returns the connection notification object.

If this parameter is specified, the corresponding callback subscription will be canceled. If this parameter is left empty, all callback subscriptions for the **connectNotify** event will be canceled.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

Parameter error. Possible causes: 3. Parameter verification failed.

 |

**Example**:

import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";

try {
  gameNearbyTransfer.off('connectNotify', connectNotifyCallBack);
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}

function connectNotifyCallBack(callback: gameNearbyTransfer.ConnectNotification) {
  hilog.info(0x0000, '\[nearby\]', '%{public}s', callback.connectState);
}

#### gameNearbyTransfer.on('discovery')

on(type: 'discovery', callback: Callback<DiscoveryResult>): void

Subscribes to the discovery result event. This API returns the result through a callback.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 6.0.0(20)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event to be monitored. The **discovery** event is supported and will be triggered after a device is discovered.

 |
| 

callback

 | 

Callback<[DiscoveryResult](#section1411541513618)\>

 | 

Yes

 | 

Callback that returns the discovery result.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

1018300008

 | 

Invalid parameter.

 |

**Example**:

import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";

try {
  gameNearbyTransfer.on('discovery', discoveryCallBack);
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}

function discoveryCallBack(callback: gameNearbyTransfer.DiscoveryResult) {
  // Obtain the discovered devices and display the device list.
  callback.nearbyGameDevices.forEach((device: gameNearbyTransfer.NearbyGameDevice, index: number) => { 
  });
}

#### gameNearbyTransfer.off('discovery')

off(type: 'discovery', callback?: Callback<DiscoveryResult>): void

Unsubscribes from the discovery result event. This API returns the result through a callback.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 6.0.0(20)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event to be monitored. The **discovery** event is supported and will be triggered after a device is discovered.

 |
| 

callback

 | 

Callback<[DiscoveryResult](#section1411541513618)\>

 | 

No

 | 

Callback that returns the discovery result.

If this parameter is specified, the corresponding callback subscription will be canceled. If this parameter is left empty, all callback subscriptions for the **discovery** event will be canceled.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

1018300008

 | 

Invalid parameter.

 |

**Example**:

import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";

try {
  gameNearbyTransfer.off('discovery', discoveryCallBack);
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}
function discoveryCallBack(callback: gameNearbyTransfer.DiscoveryResult) {
  // Obtain the discovered devices and display the device list.
  callback.nearbyGameDevices.forEach((device: gameNearbyTransfer.NearbyGameDevice, index: number) => {    
  });
}

#### gameNearbyTransfer.on('receivePackageInfo')

on(type: 'receivePackageInfo', callback: Callback<PackageInfo>): void

Subscribes to the package information receiving event. This API returns the result through a callback.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event to be monitored. The **receivePackageInfo** event is supported and will be triggered after the file information sent by the receiver is received.

 |
| 

callback

 | 

Callback<[PackageInfo](#section10841101134814)\>

 | 

Yes

 | 

Callback that returns the package information object.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

Parameter error. Possible causes: 3. Parameter verification failed.

 |

**Example**:

import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";

try {
  gameNearbyTransfer.on('receivePackageInfo', receivePackageInfoCallBack);
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}
function receivePackageInfoCallBack(callback: gameNearbyTransfer.PackageInfo) {
  hilog.info(0x0000, '\[nearby\]', '%{public}s', callback.version);
}

#### gameNearbyTransfer.off('receivePackageInfo')

off(type: 'receivePackageInfo', callback?: Callback<PackageInfo>): void

Unsubscribes from the package information receiving event. This API returns the result through a callback.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event to be monitored. The **receivePackageInfo** event is supported and will be triggered after the file information sent by the receiver is received.

 |
| 

callback

 | 

Callback<[PackageInfo](#section10841101134814)\>

 | 

No

 | 

Callback that returns the package information object.

If this parameter is specified, the corresponding callback subscription will be canceled. If this parameter is left empty, all callback subscriptions for the **receivePackageInfo** event will be canceled.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

Parameter error. Possible causes: 3. Parameter verification failed.

 |

**Example**:

import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";

try {
  gameNearbyTransfer.off('receivePackageInfo', receivePackageInfoCallBack);
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}

function receivePackageInfoCallBack(callback: gameNearbyTransfer.PackageInfo) {
  hilog.info(0x0000, '\[nearby\]', '%{public}s', callback.version);
}

#### gameNearbyTransfer.on('transferNotify')

on(type: 'transferNotify', callback: Callback<TransferNotification>): void

Subscribes to the transfer notification event. This API returns the result through a callback.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event to be monitored. The **transferNotify** event is supported and will be triggered during file transfer.

 |
| 

callback

 | 

Callback<[TransferNotification](#section116223815415)\>

 | 

Yes

 | 

Callback that returns the transfer notification object.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

Parameter error. Possible causes: 3. Parameter verification failed.

 |

**Example**:

import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";

try {
  gameNearbyTransfer.on('transferNotify', transferNotifyCallBack);
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}

function transferNotifyCallBack(callback: gameNearbyTransfer.TransferNotification) {
  hilog.info(0x0000, '\[nearby\]', '%{public}s', callback.transferState);
}

#### gameNearbyTransfer.off('transferNotify')

off(type: 'transferNotify', callback?: Callback<TransferNotification>): void

Unsubscribes from the transfer notification event. This API returns the result through a callback.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event to be monitored. The **transferNotify** event is supported and will be triggered during file transfer.

 |
| 

callback

 | 

Callback<[TransferNotification](#section116223815415)\>

 | 

No

 | 

Callback that returns the transfer notification object.

If this parameter is specified, the corresponding callback subscription will be canceled. If this parameter is left empty, all callback subscriptions for the **transferNotify** event will be canceled.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

Parameter error. Possible causes: 3. Parameter verification failed.

 |

**Example**:

import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";

try {
  gameNearbyTransfer.off('transferNotify', transferNotifyCallBack);
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}

function transferNotifyCallBack(callback: gameNearbyTransfer.TransferNotification) {
  hilog.info(0x0000, '\[nearby\]', '%{public}s', callback.transferState);
}

#### gameNearbyTransfer.on('error')

on(type: 'error', callback: Callback<ReturnResult>): void

Subscribes to the error event. This API returns the result through a callback.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event to be monitored. The **error** event is supported and will be triggered when an internal error occurs.

 |
| 

callback

 | 

Callback<[ReturnResult](#section2401441273)\>

 | 

Yes

 | 

Callback that returns the result information object.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

Parameter error. Possible causes: 3. Parameter verification failed.

 |

**Example**:

import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";

try {
  gameNearbyTransfer.on('error', errorCallBack);
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}

function errorCallBack(callback: gameNearbyTransfer.ReturnResult) {
  hilog.info(0x0000, '\[nearby\]', '%{public}s', callback.code);
}

#### gameNearbyTransfer.off('error')

off(type: 'error', callback?: Callback<ReturnResult>): void

Unsubscribes from the error event. This API returns the result through a callback.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event to be monitored. The **error** event is supported.

 |
| 

callback

 | 

Callback<[ReturnResult](#section2401441273)\>

 | 

No

 | 

Callback that returns the result information object.

If this parameter is specified, the corresponding callback subscription will be canceled. If this parameter is left empty, all callback subscriptions for the **error** event will be canceled.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

Parameter error. Possible causes: 3. Parameter verification failed.

 |

**Example**:

import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";

try {
  gameNearbyTransfer.off('error', errorCallBack);
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}

function errorCallBack(callback: gameNearbyTransfer.ReturnResult) {
  hilog.info(0x0000, '\[nearby\]', '%{public}s', callback.code);
}

#### gameNearbyTransfer.create

create(createParameters: CreateParameters): Promise<CreateResult>

Creates a nearby transfer service for the game. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

createParameters

 | 

[CreateParameters](#section1033653365917)

 | 

Yes

 | 

Parameters for creating the service.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[CreateResult](#section55661711201613)\>

 | 

Promise that returns the creation result.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

Parameter error. Possible causes: 3. Parameter verification failed.

 |
| 

1018300001

 | 

System internal error.

 |
| 

1018300002

 | 

Authentication failed.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from "@kit.BasicServicesKit";

let uiAbilityContext = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
let initParam: gameNearbyTransfer.CreateParameters = {
  abilityName: uiAbilityContext.abilityInfo.name,
  context: uiAbilityContext,
  moduleName: uiAbilityContext.abilityInfo.moduleName,
  needShowSystemUI: false
};

try {
  gameNearbyTransfer.create(initParam).then((createResult) => {
    hilog.info(0x0000, '\[nearby\]', '%{public}s', 'create success' + createResult.localDeviceName);
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, '\[nearby\]', '%{public}s', 'create error' + (err as Error).message);
  })
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}

#### gameNearbyTransfer.publishNearbyGame

publishNearbyGame(): Promise<void>

Publishes the nearby transfer service. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

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

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

1018300001

 | 

System internal error.

 |
| 

1018300003

 | 

Invalid request.

 |
| 

1018300005

 | 

The wireless network and Bluetooth should be enabled at the same time.

 |
| 

1018300006

 | 

Publishing failed.

 |

**Example**:

import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from "@kit.BasicServicesKit";

try {
  gameNearbyTransfer.publishNearbyGame().then(() => {
    hilog.info(0x0000, '\[nearby\]', '%{public}s', 'publishNearbyGame success');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, '\[nearby\]', '%{public}s', 'publishNearbyGame error' + (err as Error).message);
  })
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}

#### gameNearbyTransfer.discoveryNearbyGame

discoveryNearbyGame(): Promise<void>

Discovers nearby devices by the sender. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 6.0.0(20)

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

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

1018300001

 | 

System internal error.

 |
| 

1018300003

 | 

Invalid request.

 |
| 

1018300005

 | 

The wireless network and Bluetooth should be enabled at the same time.

 |
| 

1018300007

 | 

Discovery failed.

 |

**Example**:

import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from "@kit.BasicServicesKit";

try {
  gameNearbyTransfer.discoveryNearbyGame().then(() => {
    hilog.info(0x0000, '\[nearby\]', '%{public}s', 'discoveryNearbyGame success');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, '\[nearby\]', '%{public}s', 'discoveryNearbyGame error' + (err as Error).message);
  })
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}

#### gameNearbyTransfer.bindNearbyGame

bindNearbyGame(bindParameters: BindParameters): Promise<void>

Binds to the nearby transfer service by the sender. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 6.0.0(20)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

bindParameters

 | 

[BindParameters](#section1259101510331)

 | 

Yes

 | 

Binding parameters.

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

**Promise** object. Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

1018300001

 | 

System internal error.

 |
| 

1018300003

 | 

Invalid request.

 |
| 

1018300005

 | 

The wireless network and Bluetooth should be enabled at the same time.

 |
| 

1018300008

 | 

Invalid parameter.

 |

**Example**:

import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from "@kit.BasicServicesKit";

let bindInfo: gameNearbyTransfer.BindParameters = {
  deviceId: 'deviceId',
  networkId: 'networkId'
};
try {
  gameNearbyTransfer.bindNearbyGame(bindInfo).then(() => {
    hilog.info(0x0000, '\[nearby\]', '%{public}s', 'bindNearbyGame success');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, '\[nearby\]', '%{public}s', 'bindNearbyGame error' + (err as Error).message);
  })
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}

#### gameNearbyTransfer.autoBindNearbyGame

autoBindNearbyGame(): Promise<void>

Automatically binds to the nearby transfer service. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

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

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

1018300001

 | 

System internal error.

 |
| 

1018300003

 | 

Invalid request.

 |
| 

1018300007

 | 

Discovery failed.

 |

**Example**:

import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from "@kit.BasicServicesKit";

try {
  gameNearbyTransfer.autoBindNearbyGame().then(() => {
    hilog.info(0x0000, '\[nearby\]', '%{public}s', 'autoBindNearbyGame success');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, '\[nearby\]', '%{public}s', 'autoBindNearbyGame error' + (err as Error).message);
  })
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}

#### gameNearbyTransfer.acceptCollaboration

acceptCollaboration(acceptParameters: Record<string, object>): Promise<void>

Accepts the collaboration request. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

acceptParameters

 | 

Record<string, object>

 | 

Yes

 | 

Parameters for collaboration acceptance. The number of records can range from 1 to 1024.

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

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

Parameter error. Possible causes: 3. Parameter verification failed.

 |
| 

1018300001

 | 

System internal error.

 |
| 

1018300003

 | 

Invalid request.

 |

**Example**:

import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { AbilityConstant, UIAbility } from "@kit.AbilityKit";
import { hilog } from "@kit.PerformanceAnalysisKit";

export default class EntryAbility extends UIAbility { 
  // Collaboration callback.
  onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult {
    try {
      gameNearbyTransfer.acceptCollaboration(wantParam);
    } catch (err) {
      hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
    }
    hilog.info(0x0000, '\[nearby\]', '%{public}s', 'onCollaborate: accept collaborate');
    return AbilityConstant.CollaborateResult.ACCEPT;
  }
}

#### gameNearbyTransfer.sendPackageInfo

sendPackageInfo(packageInfo: PackageInfo): Promise<void>

Sends its own file information (performed by the receiver). This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

packageInfo

 | 

[PackageInfo](#section10841101134814)

 | 

Yes

 | 

Package information.

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

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

Parameter error. Possible causes: 3. Parameter verification failed.

 |
| 

1018300001

 | 

System internal error.

 |
| 

1018300003

 | 

Invalid request.

 |

**Example**:

import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from "@kit.BasicServicesKit";

let packageInfo: gameNearbyTransfer.PackageInfo = {
  name: 'com.huawei.xxxx',
  files: \[\],
  version: '1.1.0',
  extraData: 'extraData'
};
let fileInfo: gameNearbyTransfer.FileInfo = {
  path: "/xxx/xxxx/files/data.zip",
  hash: 'fileHash' // Optional.
};
packageInfo.files?.push(fileInfo);
try {
  gameNearbyTransfer.sendPackageInfo(packageInfo).then(() => {
    hilog.info(0x0000, '\[nearby\]', '%{public}s', 'sendPackageInfo success');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, '\[nearby\]', '%{public}s', 'sendPackageInfo error' + (err as Error).message);
  })
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}

#### gameNearbyTransfer.replyPackageInfoResult

replyPackageInfoResult(packageInfoResult: PackageInfoResult): Promise<void>

Reports the package information comparison result to the nearby transfer service (performed by the sender). This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

packageInfoResult

 | 

[PackageInfoResult](#section18372104173416)

 | 

Yes

 | 

Package information comparison result.

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

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

Parameter error. Possible causes: 3. Parameter verification failed.

 |
| 

1018300001

 | 

System internal error.

 |
| 

1018300003

 | 

Invalid request.

 |

**Example**:

import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from "@kit.BasicServicesKit";

let packageInfoResult: gameNearbyTransfer.PackageInfoResult = {
  packageInfoResultCode: gameNearbyTransfer.PackageInfoResultCode.PACKAGE\_AVAILABLE\_COMPARED
};

try {
  gameNearbyTransfer.replyPackageInfoResult(packageInfoResult).then(() => {
    hilog.info(0x0000, '\[nearby\]', '%{public}s', 'replyPackage success');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, '\[nearby\]', '%{public}s', 'replyPackage error' + (err as Error).message);
  })
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}

#### gameNearbyTransfer.transferPackageData

transferPackageData(packageData: PackageData): Promise<void>

Starts to transfer package data. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

packageData

 | 

[PackageData](#section138783245711)

 | 

Yes

 | 

Package data to be transferred.

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

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

Parameter error. Possible causes: 3. Parameter verification failed.

 |
| 

1018300001

 | 

System internal error.

 |
| 

1018300003

 | 

Invalid request.

 |

**Example**:

import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from "@kit.BasicServicesKit";

let packageData: gameNearbyTransfer.PackageData = {
  name: 'com.huawei.gamenearbydemo',
  version: '1.0.1',
  files: \[\]
};
packageData.files.push({ srcPath: "/xxx/xxxx/a.db", destPath: "xxxx/b.db" });
try {
  gameNearbyTransfer.transferPackageData(packageData).then(() => {
    hilog.info(0x0000, '\[nearby\]', '%{public}s', 'transferPackageData success');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, '\[nearby\]', '%{public}s', 'transferPackageData error' + (err as Error).message);
  })
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}

#### gameNearbyTransfer.destroy

destroy(): Promise<void>

Destroys the nearby transfer service if it is no longer used. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.GameService.GameNearby

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

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |

**Example**:

import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from "@kit.BasicServicesKit";

// Destroy the service.
try {
  gameNearbyTransfer.destroy().then(() => {
    hilog.info(0x0000, '\[nearby\]', '%{public}s', 'destroy success');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, '\[nearby\]', '%{public}s', 'destroy error' + (err as Error).message);
  })
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}
