# SafetyDetect

-   This module checks whether the device environment is secure, for example, whether the device environment is jailbroken or simulated. You can determine how to respond accordingly.

-   This module checks whether the URL accessed by a user is malicious. If the URL is malicious, you can evaluate the risk and either warn the user of the risk or block the URL.

**Start version**: 5.0.0(12)

#### Module Import

import { safetyDetect } from '@kit.DeviceSecurityKit';

#### SysIntegrityRequest

Request parameter for system integrity check.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.SafetyDetect

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

nonce

 | 

string

 | 

No

 | 

No

 | 

A randomly generated nonce value passed by your app, which is used to prevent replay attacks. The check result contains this value.

 |

#### SysIntegrityResponse

Return value of system integrity check.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.SafetyDetect

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

result

 | 

string

 | 

No

 | 

No

 | 

System integrity check result in JWS format. For details about JWS, please refer to [Development Procedure](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-sysintegrity-check#section9187179113620) of system integrity check in the _Device Security Kit Development Guide_.

 |

#### UrlCheckRequest

Request parameter for URL check.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.SafetyDetect

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

urls

 | 

Array<string>

 | 

No

 | 

No

 | 

List of URLs to be checked.

 |

#### UrlCheckResponse

Return value of URL check.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.SafetyDetect

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

results

 | 

Array<[UrlCheckResult](#section13695147172010)\>

 | 

No

 | 

No

 | 

URL check result.

 |

#### UrlCheckResult

URL check result details.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.SafetyDetect

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

url

 | 

string

 | 

No

 | 

No

 | 

Corresponds to the URL to be checked in the request parameter.

 |
| 

threat

 | 

[UrlThreatType](#section3468103822215)

 | 

No

 | 

No

 | 

URL threat type.

 |

#### UrlThreatType

Enumerated URL threat types.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.SafetyDetect

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

NORMAL

 | 

0

 | 

No threat detected.

 |
| 

MALWARE

 | 

1

 | 

Malicious URL.

 |
| 

PHISHING

 | 

2

 | 

Phishing URL.

 |
| 

OTHERS

 | 

3

 | 

Other URL threats.

 |

#### checkSysIntegrity

checkSysIntegrity(req: [SysIntegrityRequest](#section208107205467)): Promise<[SysIntegrityResponse](#section1584743916458)\>

Obtains the online system integrity check result of the current device. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/xhohVejfTGGM5D-ex_Dt6A/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=402138C661C07915A44BC0FE2C560C0098B5422D8A26784483FB236FC389FC8B)

This API involves device-cloud synergy and time-consuming operations such as network connection. Therefore, do not execute this API in the UI thread, in order to avoid UI thread blocking.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.SafetyDetect

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

req

 | 

[SysIntegrityRequest](#section208107205467)

 | 

Yes

 | 

Request parameter, including the nonce value.

A nonce value must contain 16 to 66 bytes and be encoded using Base64.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[SysIntegrityResponse](#section1584743916458)\>

 | 

Promise used to return the system integrity check result.

 |

**Error codes:**

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

Permission denied.

 |
| 

401

 | 

Invalid parameters.

Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

801

 | 

API is not supported.

 |
| 

1010800001

 | 

Internal error

 |
| 

1010800002

 | 

The network is unreachable.

 |
| 

1010800003

 | 

Access cloud server fail.

 |
| 

1010800005

 | 

The number of calls exceeds the parallel threshold.

 |
| 

1010800006

 | 

The invoking frequency exceeds the threshold.

 |
| 

1010800007

 | 

Operation timeout.

 |
| 

1010800008

 | 

The cloud service traffic exceeds the threshold.

 |

**Example:**

import { safetyDetect } from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SafetyDetectJsTest";

// Request system integrity check and process the result.
let req : safetyDetect.SysIntegrityRequest = {
  nonce : 'imEe1PCRcjGkBCAhOCh6ImADztOZ8ygxlWRs' // Random nonce value generated by the server.
};
try {
  hilog.info(0x0000, TAG, 'CheckSysIntegrity begin.');
  const data: safetyDetect.SysIntegrityResponse = await safetyDetect.checkSysIntegrity(req);
  hilog.info(0x0000, TAG, 'Succeeded in checkSysIntegrity: %{public}s', data.result);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'CheckSysIntegrity failed: %{public}d %{public}s', e.code, e.message);
}

#### checkUrlThreat

checkUrlThreat(req: [UrlCheckRequest](#section1991313125213)): Promise<[UrlCheckResponse](#section7578162151315)\>

Checks whether a URL is malicious. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/W0mgM1EDTT-qTAeJ87FBHQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8A13D17530FB5BF80D66D0909FB7C3FC4ECBEF6609AA8D2B9800B1AF0A2F0C4)

This API involves device-cloud synergy and time-consuming operations such as network connection. Therefore, do not execute this API in the UI thread, in order to avoid UI thread blocking.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.SafetyDetect

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

req

 | 

[UrlCheckRequest](#section1991313125213)

 | 

Yes

 | 

Request parameter, including the list of URLs to be checked.

A maximum of 10 URLs can be passed in, and the length of each URL cannot exceed 4096 bytes.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[UrlCheckResponse](#section7578162151315)\>

 | 

Promise used to return the URL check result.

 |

**Error codes:**

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

Invalid parameters.

Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

801

 | 

API is not supported.

 |
| 

1010800001

 | 

Internal error

 |
| 

1010800002

 | 

The network is unreachable.

 |
| 

1010800003

 | 

Access cloud server fail.

 |
| 

1010800005

 | 

The number of calls exceeds the parallel threshold.

 |
| 

1010800006

 | 

The invoking frequency exceeds the threshold.

 |
| 

1010800007

 | 

Operation timeout.

 |
| 

1010800008

 | 

The cloud service traffic exceeds the threshold.

 |

**Example:**

import { safetyDetect } from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SafetyDetectJsTest";

// Request URL check and process the result.
let req : safetyDetect.UrlCheckRequest = {
  urls : \['https://test1.com'\]
};
try {
  hilog.info(0x0000, TAG, 'CheckUrlThreat begin.');
  const data: safetyDetect.UrlCheckResponse = await safetyDetect.checkUrlThreat(req);
  hilog.info(0x0000, TAG, 'Succeeded in checkUrlThreat: %{public}s %{public}d', data.results\[0\].url, data.results\[0\].threat);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'CheckUrlThreat failed: %{public}d %{public}s', e.code, e.message);
}

#### checkSysIntegrityOnLocal

checkSysIntegrityOnLocal(): Promise<string>

Obtains the local system integrity check result of the current device. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.1.0(18).

**System capability**: SystemCapability.Security.SafetyDetect

**Start version**: 5.1.0(18)

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<string>

 | 

Promise used to return the system integrity check result in JSON format. For details about the JSON string, please refer to [Development Procedure](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-sysintegrity-check-onlocal#section153394149504) of local system integrity check in the _Device Security Kit Development Guide_.

 |

**Error codes:**

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

API is not supported.

 |
| 

1010800001

 | 

Internal error

 |
| 

1010800004

 | 

Verify capability fail.

 |
| 

1010800005

 | 

The number of calls exceeds the parallel threshold.

 |
| 

1010800006

 | 

The invoking frequency exceeds the threshold.

 |
| 

1010800007

 | 

Operation timeout.

 |

**Example:**

import { safetyDetect } from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SafetyDetectJsTest";

// Request local system integrity check and process the result.
try {
  hilog.info(0x0000, TAG, 'CheckSysIntegrityOnLocal begin.');
  const result: string = await safetyDetect.checkSysIntegrityOnLocal();
  hilog.info(0x0000, TAG, 'Succeeded in checkSysIntegrityOnLocal: %{public}s', result);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'CheckSysIntegrityOnLocal failed: %{public}d %{public}s', e.code, e.message);
}

#### checkSysIntegrityEnhanced

checkSysIntegrityEnhanced(req: [SysIntegrityRequest](#section208107205467)): Promise<[SysIntegrityResponse](#section1584743916458)\>

Obtains the enhanced online system integrity check result of the current device. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/jhynGOoGS3KrcM5GW7huSQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B2A4E97D994451F64A1A106570BC890551F3CE7451B2CA5FB9897B4D7A1E9C1)

This API involves device-cloud synergy and time-consuming operations such as network connection. Therefore, do not execute this API in the UI thread, in order to avoid UI thread blocking.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.SafetyDetect

**Start version**: 6.0.0(20)

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

req

 | 

[SysIntegrityRequest](#section208107205467)

 | 

Yes

 | 

Request parameter, including the nonce value.

A nonce value must contain 16 to 66 bytes and be encoded using Base64.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[SysIntegrityResponse](#section1584743916458)\>

 | 

Promise used to return the enhanced system integrity check result.

 |

**Error codes:**

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

API is not supported.

 |
| 

1010800001

 | 

Internal error

 |
| 

1010800002

 | 

The network is unreachable.

 |
| 

1010800003

 | 

Access cloud server fail.

 |
| 

1010800004

 | 

Verify capability fail.

 |
| 

1010800005

 | 

The number of calls exceeds the parallel threshold.

 |
| 

1010800006

 | 

The invoking frequency exceeds the threshold.

 |
| 

1010800007

 | 

Operation timeout.

 |
| 

1010800008

 | 

The cloud service traffic exceeds the threshold.

 |

**Example:**

import { safetyDetect } from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SafetyDetectJsTest";

// Request enhanced system integrity check and process the result.
let req : safetyDetect.SysIntegrityRequest = {
  nonce : 'imEe1PCRcjGkBCAhOCh6ImADztOZ8ygxlWRs' // Random nonce value generated by the server.
};
try {
  hilog.info(0x0000, TAG, 'CheckSysIntegrityEnhanced begin.');
  const data: safetyDetect.SysIntegrityResponse = await safetyDetect.checkSysIntegrityEnhanced(req);
  hilog.info(0x0000, TAG, 'Succeeded in checkSysIntegrityEnhanced: %{public}s', data.result);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'CheckSysIntegrityEnhanced failed: %{public}d %{public}s', e.code, e.message);
}
