# smartMobilityCommon (Smart Mobility)

**smartMobilityCommon** is provided as a common function for apps to listen to the status of distributed services (such as HiCar and Super Home Screen) and implement event listening.

**Start version**: 5.0.0(12)

#### Module Import

import { smartMobilityCommon } from '@kit.CarKit';

#### SmartMobilityEvent

Common event.

**System capability**: SystemCapability.CarService.DistributedEngine

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

eventName

 | 

string

 | 

No

 | 

No

 | 

Event name, which is defined by the service party.

 |
| 

type

 | 

[SmartMobilityType](#section12883193118184)

 | 

No

 | 

No

 | 

Service type.

 |
| 

data

 | 

Record<string, Object>

 | 

No

 | 

No

 | 

Detailed event information, which is determined jointly by the smart mobility service and app parties.

 |

#### SmartMobilityInfo

Smart mobility status information, including the current service type, connection status, and service data.

**System capability**: SystemCapability.CarService.DistributedEngine

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

status

 | 

[SmartMobilityStatus](#section66501518181418)

 | 

No

 | 

No

 | 

Service connection status.

 |
| 

type

 | 

[SmartMobilityType](#section12883193118184)

 | 

No

 | 

No

 | 

Service type.

 |
| 

data

 | 

Record<string, Object>

 | 

No

 | 

No

 | 

Detailed connection information, which is determined jointly by the smart mobility service and app parties.

 |

#### SmartMobilityStatus

Enumerated values of the service connection status.

**System capability**: SystemCapability.CarService.DistributedEngine

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

IDLE

 | 

0

 | 

The service is in the idle state. This is the default value when the service is not started.

 |
| 

RUNNING

 | 

1

 | 

The service is running.

 |

#### SmartMobilityType

Enumerated values of the service type.

**System capability**: SystemCapability.CarService.DistributedEngine

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

HICAR

 | 

0

 | 

HiCar.

 |
| 

SUPER\_LAUNCHER

 | 

1

 | 

Super Home Screen.

 |
| 

CAR\_HOP

 | 

2

 | 

Hop.

 |

#### getSmartMobilityAwareness

getSmartMobilityAwareness(): SmartMobilityAwareness

Obtains **SmartMobilityAwareness**.

**System capability**: SystemCapability.CarService.DistributedEngine

**Device behavior differences**: This API is supported on phones. On other devices, it returns error code 801.

**Required permission**: ohos.permission.ACCESS\_CAR\_DISTRIBUTED\_ENGINE

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[SmartMobilityAwareness](#section1135959103019)

 | 

Smart mobility management class.

 |

**Example**:

import { smartMobilityCommon } from '@kit.CarKit';

let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

801

 | 

Capability not supported.

 |

#### SmartMobilityAwareness

Smart mobility management class, which is used to call smart mobility APIs.

**System capability**: SystemCapability.CarService.DistributedEngine

**Start version**: 5.0.0(12)

#### \[h2\]on('smartMobilityEvent')

on(type: 'smartMobilityEvent', smartMobilityTypes: SmartMobilityType\[\],callback: Callback<SmartMobilityEvent>): void

Registers an event listener of the smart mobility service. For example, this callback is triggered when a navigation hop is complete.

**System capability**: SystemCapability.CarService.DistributedEngine

**Device behavior differences**: This API is supported on phones. On other devices, it returns error code 801.

**Required permission**: ohos.permission.ACCESS\_CAR\_DISTRIBUTED\_ENGINE

**Start version**: 5.0.0(12)

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

Subscription type. The value is a constant:

**smartMobilityEvent**: indicates registering an event listener.

 |
| 

smartMobilityTypes

 | 

[SmartMobilityType](#section12883193118184)\[\]

 | 

Yes

 | 

Service type array, which can contain multiple services.

 |
| 

callback

 | 

Callback<[SmartMobilityEvent](#section8760828151111)\>

 | 

Yes

 | 

Mobility service event callback function.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

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

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter type;

3\. Parameter verification failed;

4\. The size of specified type is greater than 255.

 |
| 

801

 | 

Capability not supported.

 |

**Example**:

import { smartMobilityCommon } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // Get single instance of SmartMobilityAwareness.
  let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
  // Service type.
  let types: smartMobilityCommon.SmartMobilityType\[\] = \[smartMobilityCommon.SmartMobilityType.CAR\_HOP\];
  // Mobility service event callback function.
  const callBack = (event: smartMobilityCommon.SmartMobilityEvent) => {
    hilog.info(0x0000, 'testTag', 'Received smart mobility event: ', JSON.stringify(event));
  };
  // Register a mobility service event listener.
  awareness.on('smartMobilityEvent', types, callBack);
} catch (e) {
  // Obtain the error code for an API call exception and handle the exception.
  hilog.error(0x0000, 'testTag', \`on smart mobility event error, error code: ${e?.code}\`);
}

#### \[h2\]off('smartMobilityEvent')

off(type: 'smartMobilityEvent', smartMobilityTypes: SmartMobilityType\[\], callback?: Callback<SmartMobilityEvent>): void

Unregisters a mobility service event listener.

**System capability**: SystemCapability.CarService.DistributedEngine

**Device behavior differences**: This API is supported on phones. On other devices, it returns error code 801.

**Required permission**: ohos.permission.ACCESS\_CAR\_DISTRIBUTED\_ENGINE

**Start version**: 5.0.0(12)

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

Subscription type. The value is a constant:

**smartMobilityEvent**: indicates unregistering an event listener

 |
| 

smartMobilityTypes

 | 

[SmartMobilityType](#section12883193118184)\[\]

 | 

Yes

 | 

Service type array, which can contain multiple services.

 |
| 

callback

 | 

Callback<[SmartMobilityEvent](#section8760828151111)\>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions will be unregistered.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

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

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter type;

3\. Parameter verification failed;

4\. The size of specified type is greater than 255.

 |
| 

801

 | 

Capability not supported.

 |

**Example**:

import { smartMobilityCommon } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // Get single instance of SmartMobilityAwareness.
  let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
  // Service type.
  let types: smartMobilityCommon.SmartMobilityType\[\] = \[smartMobilityCommon.SmartMobilityType.CAR\_HOP\];
  // Mobility service event callback function.
  const callBack = (event: smartMobilityCommon.SmartMobilityEvent) => {
    hilog.info(0x0000, 'testTag', 'Received smart mobility event: ', JSON.stringify(event));
  };

  // Unregister the mobility service event listener.
  awareness.off('smartMobilityEvent', types, callBack);
} catch (e) {
  // Obtain the error code for an API call exception and handle the exception.
  hilog.error(0x0000, 'testTag', \`off smart mobility event error, error code: ${e?.code}\`);
}

#### \[h2\]getSmartMobilityEvent

getSmartMobilityEvent(type: SmartMobilityType, eventName: string): SmartMobilityEvent

Obtains the information about a specified event.

**System capability**: SystemCapability.CarService.DistributedEngine

**Device behavior differences**: This API is supported on phones. On other devices, it returns error code 801.

**Required permission**: ohos.permission.ACCESS\_CAR\_DISTRIBUTED\_ENGINE

**Start version**: 5.0.0(12)

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

[SmartMobilityType](#section12883193118184)

 | 

Yes

 | 

Service type.

 |
| 

eventName

 | 

string

 | 

Yes

 | 

Event name. The options are as follows:

**CAR\_HOP\_EVENT**: hop event

**HICAR\_EVENT**: HiCar event

**SUPER\_LAUNCHER\_EVENT**: Super Home Screen event

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[SmartMobilityEvent](#section8760828151111)

 | 

Common event information.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

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

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter type;

3\. Parameter verification failed;

4\. The size of specified type is greater than 255.

 |
| 

801

 | 

Capability not supported.

 |

**Example**:

import { smartMobilityCommon } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // Get single instance of SmartMobilityAwareness.
  let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
  // Service type.
  let type = smartMobilityCommon.SmartMobilityType.CAR\_HOP;
  // Event name.
  let eventName: string = 'CAR\_HOP\_EVENT';
  // Obtain the common event information.
  let event: smartMobilityCommon.SmartMobilityEvent = awareness.getSmartMobilityEvent(type, eventName);
} catch (e) {
  // Obtain the error code for an API call exception and handle the exception.
  hilog.error(0x0000, 'testTag', \`get smart mobility event error, error code: ${e?.code}\`);
}

#### \[h2\]on('smartMobilityStatus')

on(type: 'smartMobilityStatus', smartMobilityTypes: SmartMobilityType\[\], callback: Callback<SmartMobilityInfo>): void

Registers a smart mobility connection status listener.

**System capability**: SystemCapability.CarService.DistributedEngine

**Device behavior differences**: This API is supported on phones. On other devices, it returns error code 801.

**Required permission**: ohos.permission.ACCESS\_CAR\_DISTRIBUTED\_ENGINE

**Start version**: 5.0.0(12)

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

Subscription type. The value is a constant:

**smartMobilityStatus**: indicates registering a service connection status listener

 |
| 

smartMobilityTypes

 | 

[SmartMobilityType](#section12883193118184)\[\]

 | 

Yes

 | 

Service type array, which can contain multiple services.

 |
| 

callback

 | 

Callback<[SmartMobilityInfo](#section153711644737)\>

 | 

Yes

 | 

Mobility connection status callback function.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

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

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter type;

3\. Parameter verification failed;

4\. The size of specified type is greater than 255.

 |
| 

801

 | 

Capability not supported.

 |

**Example**:

import { smartMobilityCommon } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // Get single instance of SmartMobilityAwareness.
  let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
  // Service type.
  let types: smartMobilityCommon.SmartMobilityType\[\] = \[smartMobilityCommon.SmartMobilityType.HICAR\];
  // Mobility connection status callback function.
  const callBack = (info: smartMobilityCommon.SmartMobilityInfo) => {
    hilog.info(0x0000, 'testTag', 'Received smart mobility info: ', JSON.stringify(info));
  };
  // Register a smart mobility connection status listener.
  awareness.on('smartMobilityStatus', types, callBack);
} catch (e) {
  // Obtain the error code for an API call exception and handle the exception.
  hilog.error(0x0000, 'testTag', \`on smart mobility status error, error code: ${e?.code}\`);
}

#### \[h2\]off('smartMobilityStatus')

off(type: 'smartMobilityStatus', smartMobilityTypes: SmartMobilityType\[\], callback?: Callback<SmartMobilityInfo>): void

Unregisters a smart mobility connection status listener.

**System capability**: SystemCapability.CarService.DistributedEngine

**Device behavior differences**: This API is supported on phones. On other devices, it returns error code 801.

**Required permission**: ohos.permission.ACCESS\_CAR\_DISTRIBUTED\_ENGINE

**Start version**: 5.0.0(12)

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

Subscription type. The value is a constant:

**smartMobilityStatus**: indicates unregistering a service connection status listener

 |
| 

smartMobilityTypes

 | 

[SmartMobilityType](#section12883193118184)\[\]

 | 

Yes

 | 

Service type array, which can contain multiple services.

 |
| 

callback

 | 

Callback<[SmartMobilityInfo](#section153711644737)\>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions will be unregistered.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

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

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter type;

3\. Parameter verification failed;

4\. The size of specified type is greater than 255.

 |
| 

801

 | 

Capability not supported.

 |

**Example**:

import { smartMobilityCommon } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // Get single instance of SmartMobilityAwareness.
  let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
  // Service type.
  let types: smartMobilityCommon.SmartMobilityType\[\] = \[smartMobilityCommon.SmartMobilityType.HICAR\];
  // Mobility connection status callback function.
  const callBack = (info: smartMobilityCommon.SmartMobilityInfo) => {
    hilog.info(0x0000, 'testTag', 'Received smart mobility info: ', JSON.stringify(info));
  };
  // Unregister the smart mobility connection status listener.
  awareness.off('smartMobilityStatus', types);
} catch (e) {
  // Obtain the error code for an API call exception and handle the exception.
  hilog.error(0x0000, 'testTag', \`off smart mobility status error, error code: ${e?.code}\`);
}

#### \[h2\]getSmartMobilityStatus

getSmartMobilityStatus(type: SmartMobilityType): SmartMobilityInfo

Obtains the smart mobility connection status.

**System capability**: SystemCapability.CarService.DistributedEngine

**Device behavior differences**: This API is supported on phones. On other devices, it returns error code 801.

**Required permission**: ohos.permission.ACCESS\_CAR\_DISTRIBUTED\_ENGINE

**Start version**: 5.0.0(12)

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

[SmartMobilityType](#section12883193118184)

 | 

Yes

 | 

Service type.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[SmartMobilityInfo](#section153711644737)

 | 

Service connection status information.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

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

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter type;

3\. Parameter verification failed;

4\. The size of specified type is greater than 255.

 |
| 

801

 | 

Capability not supported.

 |

**Example**:

import { smartMobilityCommon } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
  // Service type.
  let type = smartMobilityCommon.SmartMobilityType.HICAR;
  // Obtain the service status information.
  let ret = awareness.getSmartMobilityStatus(type);
} catch (e) {
  // Obtain the error code for an API call exception and handle the exception.
  hilog.error(0x0000, 'testTag', \`get smart mobility status error, error code: ${e?.code}\`);
}
