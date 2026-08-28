# TrustedAppService

This module provides the security attestation service for app data, including creating attestation keys, destroying attestation keys, initializing attestation sessions, ending attestation sessions, and obtaining the data to verify location security. This module provides security attestation for image security verification and location security verification, ensuring that the image or location data is not tampered with.

**Start version**: 5.0.0(12)

#### Module Import

import { trustedAppService } from '@kit.DeviceSecurityKit';

#### createAttestKey

createAttestKey(options: AttestOptions): Promise<void>

Creates an attestation key. This API is called when the attestation key does not exist or is unavailable. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.TrustedAppService.Core

**Start version**: 5.0.0(12)

**Parameters:**

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

options

 | 

[AttestOptions](#section18297145185618)

 | 

Yes

 | 

Parameters for generating an attestation key. You need to specify the key type and key size.

 |

**Returns:**

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

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/trustedappservice/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

argument is invalid.

 |
| 

1011500001

 | 

algorithm param is invalid.

 |
| 

1011500002

 | 

algorithm param is missing.

 |
| 

1011500003

 | 

create attestation key failed.

 |
| 

1011500004

 | 

create anonymous certificate failed.

 |
| 

1011500005

 | 

operating file failed.

 |
| 

1011500006

 | 

IPC communication failed.

 |

**Example:**

import { trustedAppService } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let properties: Array<trustedAppService.AttestParam> = \[
  {
    tag: trustedAppService.AttestTag.ATTEST\_TAG\_ALGORITHM,
    value: trustedAppService.AttestKeyAlg.ATTEST\_ALG\_ECC
  },
  {
    tag: trustedAppService.AttestTag.ATTEST\_TAG\_KEY\_SIZE,
    value: trustedAppService.AttestKeySize.ATTEST\_ECC\_KEY\_SIZE\_256
  }
\];
let options: trustedAppService.AttestOptions = {
  properties: properties,
};
await trustedAppService.createAttestKey(options)
  .then(
    (): void => {
      hilog.info(0x0000, 'testTag', 'Succeeded in creating attest key');
    }
  ).catch(
    (error: BusinessError): void => {
      let err = error as BusinessError;
      hilog.error(0x0000, 'testTag', \`Failed to create attest key, code:${err.code}, message:${err.message}\`);
    });

#### AttestOptions

Request parameter of the [createAttestKey](#section81796536265) API.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.TrustedAppService.Core

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

properties

 | 

Array<[AttestParam](#section0633210102)\>

 | 

No

 | 

No

 | 

Data passed by your app for generating the attestation key configuration.

 |

#### AttestParam

Parameters in [AttestOptions](#section18297145185618).

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.TrustedAppService.Core

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

tag

 | 

[AttestTag](#section1427551613315)

 | 

No

 | 

No

 | 

Tag passed by your app for generating the attestation key configuration.

 |
| 

value

 | 

boolean|number|bigint|Uint8Array

 | 

No

 | 

No

 | 

Value of the tag passed by your app for generating the attestation key configuration.

**boolean**:

Reserved.

**number**:

(1) When **tag** is **ATTEST\_TAG\_ALGORITHM**, its value is of the [AttestKeyAlg](#section17268105152417) type.

(2) When **tag** is **ATTEST\_TAG\_KEY\_SIZE**, its value is of the [AttestKeySize](#section932031292912) type.

(3) When **tag** is **ATTEST\_TAG\_DEVICE\_TYPE**, its value is of the [AttestType](#section8803148183419) type.

**bigint**:

When **tag** is **ATTEST\_TAG\_DEVICE\_ID**, its value is a device ID, which is a random value of the int64 type.

**Uint8Array**:

Reserved.

 |

#### AttestTag

Attestation configuration tag, whose definition is extended by [AttestTagType](#section18511411417).

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.TrustedAppService.Core

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

ATTEST\_TAG\_INVALID

 | 

AttestTagType.ATTEST\_TAG\_TYPE\_INVALID|0

 | 

Invalid tag.

 |
| 

ATTEST\_TAG\_ALGORITHM

 | 

AttestTagType.ATTEST\_TAG\_TYPE\_UINT|1

 | 

Algorithm tag.

 |
| 

ATTEST\_TAG\_KEY\_SIZE

 | 

AttestTagType.ATTEST\_TAG\_TYPE\_UINT|2

 | 

Key size tag.

 |
| 

ATTEST\_TAG\_DEVICE\_TYPE

 | 

AttestTagType.ATTEST\_TAG\_TYPE\_UINT|3

 | 

Device type tag.

 |
| 

ATTEST\_TAG\_DEVICE\_ID

 | 

AttestTagType.ATTEST\_TAG\_TYPE\_UINT|4

 | 

Device serial number tag.

 |

#### AttestTagType

Tag's data type definition.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.TrustedAppService.Core

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

ATTEST\_TAG\_TYPE\_INVALID

 | 

0<<28

 | 

Invalid tag type.

 |
| 

ATTEST\_TAG\_TYPE\_INT

 | 

1<<28

 | 

INT data type.

 |
| 

ATTEST\_TAG\_TYPE\_UINT

 | 

2<<28

 | 

UINT data type.

 |
| 

ATTEST\_TAG\_TYPE\_ULONG

 | 

3<<28

 | 

ULONG data type.

 |
| 

ATTEST\_TAG\_TYPE\_BOOL

 | 

4<<28

 | 

Bool data type.

 |
| 

ATTEST\_TAG\_TYPE\_BYTES

 | 

5<<28

 | 

Bytes data type.

 |

#### AttestKeyAlg

Attestation key algorithm.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.TrustedAppService.Core

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

ATTEST\_ALG\_ECC

 | 

1

 | 

ECC algorithm.

 |

#### AttestKeySize

Attestation key length.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.TrustedAppService.Core

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

ATTEST\_ECC\_KEY\_SIZE\_256

 | 

256

 | 

Indicates that the attestation key length is 256 bits.

 |
| 

ATTEST\_ECC\_KEY\_SIZE\_384

 | 

384

 | 

Indicates that the attestation key length is 384 bits.

 |

#### destroyAttestKey

destroyAttestKey(): Promise<void>

Destroys an attestation key. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.TrustedAppService.Core

**Start version**: 5.0.0(12)

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/trustedappservice/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1011500005

 | 

operating file failed.

 |
| 

1011500006

 | 

IPC communication failed.

 |
| 

1011500007

 | 

item not found.

 |

**Returns:**

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

**Example:**

import { trustedAppService } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

await trustedAppService.destroyAttestKey().then(
  (): void => {
    hilog.info(0x0000, 'testTag', 'Succeeded in destroying attest key');
  }
).catch(
  (error: BusinessError): void => {
    let err = error as BusinessError;
    hilog.error(0x0000, 'testTag', \`Failed to destroy attest key, code:${err.code}, message:${err.message}\`);
  }
);

#### initializeAttestContext

initializeAttestContext(userData: string, options: AttestOptions): Promise<AttestReturnResult>

Initializes an attestation session, which is used after the attestation key is successfully created. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.TrustedAppService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

userData

 | 

string

 | 

Yes

 | 

User data passed for initializing an attestation session. The value contains 16 to 127 bytes.

 |
| 

options

 | 

[AttestOptions](#section18297145185618)

 | 

Yes

 | 

Parameters for initializing an attestation session. You need to specify the device type and device ID.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AttestReturnResult](#section1348925811317)\>

 | 

Generated anonymous certificate chain.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/trustedappservice/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

argument is invalid.

 |
| 

1011500002

 | 

param is missing.

 |
| 

1011500005

 | 

operating file failed.

 |
| 

1011500006

 | 

IPC communication failed.

 |
| 

1011500007

 | 

item not found.

 |
| 

1011500008

 | 

anonymous certificate verify failed.

 |
| 

1011500009

 | 

anonymous certificate has expired.

 |
| 

1011500010

 | 

get attestation key failed.

 |
| 

1011500011

 | 

initialize secure camera failed.

 |

#### AttestType

Attestation session type.

**System capability**: SystemCapability.Security.TrustedAppService.Core

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

ATTEST\_TYPE\_LOCATION

 | 

1

 | 

Location security attestation session.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

ATTEST\_TYPE\_CAMERA

 | 

2

 | 

Image security attestation session.

 |
| 

ATTEST\_TYPE\_SECIMAGE\_PROCESS

 | 

3

 | 

Attestation session for secure image processing. Start version: 5.1.0(18).

 |

#### AttestReturnResult

Return value of the [initializeAttestContext](#section166716269293) API.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.TrustedAppService.Core

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

certChains

 | 

Array<string>

 | 

No

 | 

No

 | 

Anonymous certificate chain returned after an attestation session is successfully initialized.

 |

**Example:**

import { trustedAppService } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// **device\_id** must be set to the Bigint type.
let device\_id\_tt = 12581;
// The user data length must be greater than 16 bytes and not exceed 127 bytes.
let user\_data = "test\_user\_data\_0000"
let properties2: Array<trustedAppService.AttestParam> = \[
  {
    tag: trustedAppService.AttestTag.ATTEST\_TAG\_DEVICE\_TYPE,
    value: trustedAppService.AttestType.ATTEST\_TYPE\_LOCATION
  },
  {
    tag: trustedAppService.AttestTag.ATTEST\_TAG\_DEVICE\_ID,
    value: BigInt(device\_id\_tt)
  },
\];
let options2: trustedAppService.AttestOptions = {
  properties: properties2,
};
await trustedAppService.initializeAttestContext(user\_data, options2).then(
  (returnResult: trustedAppService.AttestReturnResult): void => {
    let chains = returnResult.certChains as Array<string>;
    for (const item of chains) {
      hilog.info(0x0000, 'testTag', 'item: ' + item);
    };
  }
).catch(
  (error: BusinessError): void => {
    let err = error as BusinessError;
    hilog.error(0x0000, 'testTag', \`Failed to initialize attest context, code:${err.code}, message:${err.message}\`);
  }
);

#### AttestExceptionErrCode

Error codes of the APIs provided by the TrustedAppService for creating an attestation key, destroying an attestation key, initializing an attestation session, ending an attestation session, and obtaining the data to verify location security.

**System capability**: SystemCapability.Security.TrustedAppService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

ATTEST\_ERROR\_NO\_PERMISSION

 | 

201

 | 

Permission verification failed.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

ATTEST\_ERROR\_ILLEGAL\_ARGUMENT

 | 

401

 | 

Parameter check failed.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

ATTEST\_ERROR\_INVALID\_ALG\_ARGUMENT

 | 

1011500001

 | 

Invalid algorithm parameter.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

ATTEST\_ERROR\_MISSING\_ARGUMENT

 | 

1011500002

 | 

Some parameters are missing.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

ATTEST\_ERROR\_KEY\_GENERATOR\_FAILED

 | 

1011500003

 | 

Key generation failed.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

ATTEST\_ERROR\_CERTS\_CREATION\_FAILED

 | 

1011500004

 | 

Certificate creation failed.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

ATTEST\_ERROR\_FILE\_OPERATION\_FAILED

 | 

1011500005

 | 

File operation failed.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

ATTEST\_ERROR\_COMMUNICATION\_FAILED

 | 

1011500006

 | 

IPC failed.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

ATTEST\_ERROR\_ITEM\_NOT\_FOUND

 | 

1011500007

 | 

The key does not exist.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

ATTEST\_ERROR\_CERTS\_VERIFICATION\_FAILED

 | 

1011500008

 | 

Certificate verification failed.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

ATTEST\_ERROR\_CERTS\_EXPIRED

 | 

1011500009

 | 

The certificate has expired.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

ATTEST\_ERROR\_KEY\_NOT\_MATCHED

 | 

1011500010

 | 

The key does not match.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

ATTEST\_ERROR\_SECURE\_CAMERA\_INITIALIZATION\_FAILED

 | 

1011500011

 | 

Failed to initialize the camera in secure mode.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

ATTEST\_ERROR\_CONTEXT\_BAD\_STATE

 | 

1011500012

 | 

The attestation session context is abnormal.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

ATTEST\_ERROR\_KEY\_EXPIRED

 | 

1011500013

 | 

The key has expired.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

ATTEST\_ERROR\_LOCATION\_SERVICE\_UNAVAILABLE

 | 

1011500014

 | 

The location service is not available.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

ATTEST\_ERROR\_LOCATION\_SWITCH\_OFF

 | 

1011500015

 | 

The location service is disabled.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

ATTEST\_ERROR\_LOCATION\_FAILED

 | 

1011500016

 | 

Failed to obtain the location information.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

ATTEST\_ERROR\_SIGNATURE\_VERIFICATION\_FAILED

 | 

1011500017

 | 

Signature verification failed.

**Start version: 5.1.0(18).**

 |
| 

ATTEST\_ERROR\_SECIMAGE\_PROCESS\_FAILED

 | 

1011500018

 | 

Failed to process the secure image.

**Start version: 5.1.0(18).**

 |

#### finalizeAttestContext

finalizeAttestContext(options: AttestOptions): Promise<void>

Ends an attestation session. This API is called after the security attestation service is ended. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.TrustedAppService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

options

 | 

[AttestOptions](#section18297145185618)

 | 

Yes

 | 

Parameters for ending an attestation session. You need to specify the device type.

 |

**Returns:**

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

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/trustedappservice/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

argument is invalid.

 |
| 

1011500002

 | 

param is missing.

 |
| 

1011500006

 | 

IPC communication failed.

 |
| 

1011500007

 | 

item not found.

 |

**Example:**

import { trustedAppService } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let properties: Array<trustedAppService.AttestParam> = \[
  {
    tag: trustedAppService.AttestTag.ATTEST\_TAG\_DEVICE\_TYPE,
    value: trustedAppService.AttestType.ATTEST\_TYPE\_CAMERA
  }
\];
let options: trustedAppService.AttestOptions = {
  properties: properties,
};
await trustedAppService.finalizeAttestContext(options).then(
  (): void => {
    hilog.info(0x0000, 'testTag', 'Succeeded in finalizing attest context');
  }
).catch(
  (error: BusinessError): void => {
    let err = error as BusinessError;
    hilog.error(0x0000, 'testTag', \`Failed to finalize attest context, code:${err.code}, message:${err.message}\`);
  }
);

#### getCurrentSecureLocation

getCurrentSecureLocation(timeout : number, priority: LocatingPriority): Promise<SecureLocation>

Obtains the data to verify location security. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.TrustedAppService.Location

**Required permissions**: ohos.permission.LOCATION and ohos.permission.APPROXIMATELY\_LOCATION

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

timeout

 | 

number

 | 

Yes

 | 

Timeout interval of a single location obtaining request, in milliseconds. The value must be greater than or equal to 1000.

 |
| 

priority

 | 

[LocatingPriority](#section6450421300)

 | 

Yes

 | 

Priority policy for obtaining the data to verify location security.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[SecureLocation](#section168048435326)\>

 | 

Data obtained to verify location security.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/trustedappservice/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

201

 | 

has no permission.

 |
| 

401

 | 

argument is invalid.

 |
| 

1011500012

 | 

attestation context not initialized.

 |
| 

1011500013

 | 

attestation key has expired.

 |
| 

1011500014

 | 

location service is unavailable.

 |
| 

1011500015

 | 

The location switch is off.

 |
| 

1011500016

 | 

Failed to obtain the secure geographical location.

 |

#### LocatingPriority

Priority policy for obtaining the data to verify location security.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.TrustedAppService.Location

**Start version**: 5.0.0(12)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

PRIORITY\_ACCURACY

 | 

0

 | 

Accuracy first. The location data accuracy takes precedence.

 |
| 

PRIORITY\_LOCATING\_SPEED

 | 

1

 | 

Speed first. The location obtaining speed takes precedence.

 |

#### SecureLocation

Data obtained to verify location security.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.TrustedAppService.Location

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

originalLocation

 | 

[Location](#section7212957123210)

 | 

No

 | 

No

 | 

Geographical location information.

 |
| 

userData

 | 

String

 | 

No

 | 

No

 | 

User data. The value contains 16 to 127 bytes.

 |
| 

signature

 | 

String

 | 

No

 | 

No

 | 

Signature result.

When the attestation key length is 256 bits, the signature length is 96 bytes.

When the attestation key length is 384 bits, the signature length is 136 or 140 bytes.

 |

#### Location

Geographical location information.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.TrustedAppService.Location

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

latitude

 | 

number

 | 

No

 | 

No

 | 

Latitude. A positive value indicates north latitude, and a negative value indicates south latitude. The value ranges from –90 to 90. Only the WGS84 coordinate system is supported.

 |
| 

longitude

 | 

number

 | 

No

 | 

No

 | 

Longitude. A positive value indicates east longitude, and a negative value indicates west longitude. The value ranges from –180 to 180. Only the WGS84 coordinate system is supported.

 |
| 

altitude

 | 

number

 | 

No

 | 

No

 | 

Height, in meters.

 |
| 

accuracy

 | 

number

 | 

No

 | 

No

 | 

Precision, in meters. The value must be greater than or equal to 0.

 |
| 

timestamp

 | 

number

 | 

No

 | 

No

 | 

Timestamp, in milliseconds. The value must be greater than or equal to 0.

 |

**Example:**

import { trustedAppService } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const secureLocation = await trustedAppService.getCurrentSecureLocation(3000, trustedAppService.LocatingPriority.PRIORITY\_LOCATING\_SPEED);
  hilog.info(0x0000, 'testTag', 'Succeeded in getting secure location, result = ${JSON.stringify(secureLocation)}');
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', \`Failed to get secure location, code:${err.code}, message:${err.message}\`);
}

#### procSecImageTransform

procSecImageTransform(srcSecImage: ArrayBuffer, procParams: SecImageProcParamsArray): Promise<SecImageBuffer>

Compresses and crops a secure image. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Security.TrustedAppService.Core

**Start version**: 5.1.0(18)

**Parameters:**

| 
Parameter

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

srcSecImage

 | 

ArrayBuffer

 | 

Yes

 | 

Signed secure image returned by the camera in secure mode.

 |
| 

procParams

 | 

[SecImageProcParamsArray](#section1429553183618)

 | 

Yes

 | 

Secure image compression and cropping parameters.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[SecImageBuffer](#section147282975418)\>

 | 

Signed secure image after compression and cropping.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/trustedappservice/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

1011500012

 | 

attestation context not initialized.

 |
| 

1011500013

 | 

attestation key has expired.

 |
| 

1011500017

 | 

signature verification failed.

 |
| 

1011500018

 | 

secure image process failed.

 |

#### SecImageProcParamsArray

Request parameters for the [procSecImageTransform](#section4271646181318) API.

**System capability**: SystemCapability.Security.TrustedAppService.Core

**Start version**: 5.1.0(18)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

properties

 | 

Array<[SecImageProcParams](#section152961316368)\>

 | 

No

 | 

No

 | 

Configuration passed by your app for secure image compression and cropping.

 |

#### SecImageProcParams

Parameters in [SecImageProcParamsArray](#section1429553183618).

**System capability**: SystemCapability.Security.TrustedAppService.Core

**Start version**: 5.1.0(18)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

tag

 | 

[SecImageProcTag](#section918018974416)

 | 

No

 | 

No

 | 

Tag passed by your app for secure image compression and cropping.

 |
| 

value

 | 

number | [CropRegion](#section5236627181910)

 | 

No

 | 

No

 | 

Value of the tag passed by your app for secure image compression and cropping.

**number**:

(1) When **tag** is **SECIMAGE\_TAG\_SRC\_IMAGE\_FORMAT** or

**SECIMAGE\_TAG\_DEST\_IMAGE\_FORMAT**,

its value is of the [SecImageProcParamsArray](#section1429553183618) type.

(2) When **tag** is **SECIMAGE\_TAG\_PROC\_OPERATION**, its value is of the [SecImageProcOperation](#section118088168584) type.

(3) When **tag** is **SECIMAGE\_TAG\_COMPRESSION\_QUALITY**, its value ranges from 1 to 100.

**CropRegion**:

When **tag** is **SECIMAGE\_TAG\_CROP\_REGION**, its value is of the [CropRegion](#section5236627181910) type.

 |

#### SecImageProcTag

Configuration tag for secure image compression and cropping, whose type is defined using [AttestTagType](#section18511411417).

**System capability**: SystemCapability.Security.TrustedAppService.Core

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

SECIMAGE\_TAG\_INVALID

 | 

AttestTagType.ATTEST\_TAG\_TYPE\_INVALID|0

 | 

Invalid tag.

 |
| 

SECIMAGE\_TAG\_SRC\_IMAGE\_FORMAT

 | 

AttestTagType.ATTEST\_TAG\_TYPE\_UINT|1

 | 

Format of the input secure image.

 |
| 

SECIMAGE\_TAG\_DEST\_IMAGE\_FORMAT

 | 

AttestTagType.ATTEST\_TAG\_TYPE\_UINT|2

 | 

Format of the secure image after compression and cropping.

 |
| 

SECIMAGE\_TAG\_PROC\_OPERATION

 | 

AttestTagType.ATTEST\_TAG\_TYPE\_UINT|3

 | 

Secure image processing command, including compression, cropping, and compression + cropping.

 |
| 

SECIMAGE\_TAG\_COMPRESSION\_QUALITY

 | 

AttestTagType.ATTEST\_TAG\_TYPE\_UINT|4

 | 

Compression quality for secure image compression.

 |
| 

SECIMAGE\_TAG\_CROP\_REGION

 | 

AttestTagType.ATTEST\_TAG\_TYPE\_UINT|5

 | 

Cropping area for secure image cropping.

 |

#### SecImageProcOperation

Secure image processing command.

**System capability**: SystemCapability.Security.TrustedAppService.Core

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

SECIMAGE\_COMPRESSION

 | 

0

 | 

Secure image compression command.

 |
| 

SECIMAGE\_CROPPING

 | 

1

 | 

Secure image cropping command.

 |
| 

SECIMAGE\_COMPRESSION\_AND\_CROPPING

 | 

2

 | 

Secure image compression and cropping command.

 |

#### SecImageProcFormat

Secure image format.

**System capability**: SystemCapability.Security.TrustedAppService.Core

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

SECIMAGE\_FORMAT\_INVALID

 | 

0

 | 

Invalid secure image format.

 |
| 

SECIMAGE\_FORMAT\_YUV\_NV21

 | 

1

 | 

YUV420 NV21. The input secure image format and the secure image format returned by the cropping command are both **SECIMAGE\_FORMAT\_YUV\_NV21**.

 |
| 

SECIMAGE\_FORMAT\_JPEG

 | 

2

 | 

JPEG. The secure image format returned by the compression command and the compression + cropping command is **SECIMAGE\_FORMAT\_JPEG**.

 |

#### CropRegion

Cropping area for secure image cropping. The following figure shows the cropping area parameters.

**System capability**: SystemCapability.Security.TrustedAppService.Core

**Start version**: 5.1.0(18)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

x

 | 

number

 | 

No

 | 

No

 | 

Horizontal offset of the top-left corner of the cropping area relative to the left edge of the entire image. The value is an even number ranging from 0 to 640. The unit is pixel.

 |
| 

y

 | 

number

 | 

No

 | 

No

 | 

Vertical offset of the top-left corner of the cropping area relative to the upper edge of the entire image. The value is an even number ranging from 0 to 480. The unit is pixel.

 |
| 

width

 | 

number

 | 

No

 | 

No

 | 

Width of the cropping area (horizontal length). The value is an even number ranging from 0 to 640. The sum of **x** and **width** must be less than or equal to 640. The unit is pixel.

 |
| 

height

 | 

number

 | 

No

 | 

No

 | 

Height of the cropping area (vertical length). The value is an even number ranging from 0 to 480. The sum of **y** and **height** must be less than or equal to 480. The unit is pixel.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/Ho-jGVIWTPu4ktGQ_WzgeA/en-us_image_0000002515108505.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ECAFB0152737FD36C036E5465E58588B4227DF0895CAD298ECAB7DE2FE553BBA "Click to enlarge")

#### SecImageBuffer

Obtains the signed secure image after compression and cropping.

**System capability**: SystemCapability.Security.TrustedAppService.Core

**Start version**: 5.1.0(18)

| 
**Parameter**

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

secImage

 | 

ArrayBuffer

 | 

No

 | 

No

 | 

Signed secure image after compression and cropping.

 |

**Example of secure image compression:**

import { trustedAppService } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const srcSecImageBuffer = new  ArrayBuffer(461844);// Replace it with the secure image buffer obtained from Camera Kit.

let properties: Array<trustedAppService.SecImageProcParams> = \[
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_PROC\_OPERATION,
    value: trustedAppService.SecImageProcOperation.SECIMAGE\_COMPRESSION,
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_SRC\_IMAGE\_FORMAT,
    value: trustedAppService.SecImageProcFormat.SECIMAGE\_FORMAT\_YUV\_NV21, // The input image format is YUV420 NV21 for both the secure image compression and cropping commands.
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_DEST\_IMAGE\_FORMAT,
    value: trustedAppService.SecImageProcFormat.SECIMAGE\_FORMAT\_JPEG, // The image format returned by the secure image compression command is JPEG.
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_COMPRESSION\_QUALITY,
    value: 90, // Replace it with the compression quality required by the service scenario.
  },
\];
let procParams: trustedAppService.SecImageProcParamsArray = {
  properties: properties,
};
await trustedAppService.procSecImageTransform(srcSecImageBuffer, procParams).then(
  (returnResult: trustedAppService.SecImageBuffer): void => {
    let returnSecImageBuffer = returnResult.secImage;
  }
).catch(
  (error: BusinessError): void => {
    let err = error as BusinessError;
    hilog.error(0x0000, 'testTag', \`Failed to process secureImage compression, code:${err.code}, message:${err.message}\`);
  }
);

**Example of secure image cropping:**

import { trustedAppService } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const srcSecImageBuffer = new  ArrayBuffer(461844);// Replace it with the secure image buffer obtained from Camera Kit.

let properties: Array<trustedAppService.SecImageProcParams> = \[
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_PROC\_OPERATION,
    value: trustedAppService.SecImageProcOperation.SECIMAGE\_CROPPING,
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_SRC\_IMAGE\_FORMAT,
    value: trustedAppService.SecImageProcFormat.SECIMAGE\_FORMAT\_YUV\_NV21, // The input image format is YUV420 NV21 for both the secure image compression and cropping commands.
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_DEST\_IMAGE\_FORMAT,
    value: trustedAppService.SecImageProcFormat.SECIMAGE\_FORMAT\_YUV\_NV21, // The image format returned by the secure image compression command is JPEG.
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_CROP\_REGION,
    value: { x : 0, y : 0, width : 320, height : 240 }, // Replace the value with the cropping area range required by the service scenario.
  },
\];
let procParams: trustedAppService.SecImageProcParamsArray = {
  properties: properties,
};
await trustedAppService.procSecImageTransform(srcSecImageBuffer, procParams).then(
  (returnResult: trustedAppService.SecImageBuffer): void => {
    let returnSecImageBuffer = returnResult.secImage;
  }
).catch(
  (error: BusinessError): void => {
    let err = error as BusinessError;
    hilog.error(0x0000, 'testTag', \`Failed to process secureImage cropping, code:${err.code}, message:${err.message}\`);
  }
);

**Example of secure image compression and cropping:**

import { trustedAppService } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const srcSecImageBuffer = new  ArrayBuffer(461844);// Replace it with the secure image buffer obtained from Camera Kit.

let properties: Array<trustedAppService.SecImageProcParams> = \[
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_PROC\_OPERATION,
    value: trustedAppService.SecImageProcOperation.SECIMAGE\_COMPRESSION\_AND\_CROPPING,
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_SRC\_IMAGE\_FORMAT,
    value: trustedAppService.SecImageProcFormat.SECIMAGE\_FORMAT\_YUV\_NV21,
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_DEST\_IMAGE\_FORMAT,
    value: trustedAppService.SecImageProcFormat.SECIMAGE\_FORMAT\_JPEG,
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_COMPRESSION\_QUALITY,
    value: 90, // Replace it with the compression quality required by the service scenario.
  },
  {
    tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_CROP\_REGION,
    value: { x : 0, y : 0, width : 320, height : 240 }, // Replace the value with the cropping area range required by the service scenario.
  },
\];
let procParams: trustedAppService.SecImageProcParamsArray = {
  properties: properties,
};
await trustedAppService.procSecImageTransform(srcSecImageBuffer, options).then(
  (returnResult: trustedAppService.SecImageBuffer): void => {
    let returnSecImageBuffer = returnResult.secImage;
  }
).catch(
  (error: BusinessError): void => {
    let err = error as BusinessError;
    hilog.error(0x0000, 'testTag', \`Failed to process secureImage cropping, code:${err.code}, message:${err.message}\`);
  }
);
