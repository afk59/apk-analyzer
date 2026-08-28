# BusinessRiskIntelligentDetection

-   This module identifies fraud risks of a device.

**Start version**: 5.0.0(12)

-   This module detects cheating behaviors like automated clicks and device farming.

**Start version**: 6.0.0(20)

#### Module Import

import { businessRiskIntelligentDetection } from '@kit.DeviceSecurityKit';

#### FraudDetectionRequest

Fraud detection request parameters.

**System capability**: SystemCapability.Security.BusinessRiskIntelligentDetection

**Start version**: 5.0.0(12)

| 
Name

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

nonce

 | 

Uint8Array

 | 

No

 | 

No

 | 

A randomly generated nonce value passed by your app, which is used to prevent replay attacks. The detection result contains this value. A nonce value must contain 24 to 80 bytes.

 |
| 

algorithm

 | 

[SigningAlgorithm](#section10182122284411)

 | 

No

 | 

No

 | 

Digital signature algorithm.

 |
| 

version

 | 

number

 | 

No

 | 

Yes

 | 

Version number of a detection result message format. The value can be **1** (default value) or **2**. When the value is **2**, the detection result tags contain the time and risk level attributes, in which the time attribute indicates the last occurrence time of the clue corresponding to the specified tag and the risk level attribute indicates the risk level of the specified tag. When the value is **1**, the detection result tags do not contain the time and risk level attributes.

**Start version**: 5.1.0(18)

 |

#### SimulatedClickDetectionRequest

Request parameters for simulated click detection.

**System capability**: SystemCapability.Security.BusinessRiskIntelligentDetection

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

version

 | 

number

 | 

No

 | 

Yes

 | 

Version number of a detection result message format. The default value is **1**. Currently, the value can only be **1**.

 |

#### SimulatedClickDetectionEnhancedRequest

Request parameters for enhanced simulated click detection.

**System capability**: SystemCapability.Security.BusinessRiskIntelligentDetection

**Start version**: 6.0.2(22)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

nonce

 | 

Uint8Array

 | 

No

 | 

No

 | 

A randomly generated nonce value passed by your app, which is used to prevent replay attacks. The detection result contains this value. A nonce value must contain 24 to 80 bytes.

 |
| 

algorithm

 | 

[SigningAlgorithm](#section10182122284411)

 | 

No

 | 

No

 | 

Digital signature algorithm.

 |
| 

version

 | 

number

 | 

No

 | 

Yes

 | 

Version number of a detection result message format. The default value is **1**. Currently, the value can only be **1**.

 |

#### SigningAlgorithm

Digital signature algorithm.

**System capability**: SystemCapability.Security.BusinessRiskIntelligentDetection

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

ES256

 | 

0

 | 

SHA256withECDSA.

 |

#### detectFraudRisk

detectFraudRisk(params: [FraudDetectionRequest](#section165215281222)): Promise<string>

Obtains the fraud risks of a device. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Security.BusinessRiskIntelligentDetection

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

params

 | 

[FraudDetectionRequest](#section165215281222)

 | 

Yes

 | 

Request parameters.

 |

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

Fraud detection result, which is a JWS string encoded using Base64URL and returned through a promise. If an exception or error occurs, an error code will be returned.

Fields in JWS-format **Header** are as follows:

{
    "alg": "ES256",
    "x5c": \["",""\]
}

-   **alg**: digital signature algorithm. The value **ES256** indicates SHA256withECDSA.
-   **x5c**: certificate chain used by the Huawei signature server for JWS signing. **x5c\[0\]** indicates the certificate for JWS signing and **x5c\[1\]** indicates the CA certificate of a Huawei device.

Fields in JWS-format **Payload** are as follows:

1\. When the value of **version** in **FraudDetectionRequest** is **1**, the payload example is as follows:

{
    "timestampMs": 9xxxxxxxxx,
    "nonce": "Rxxxxxxxxx",
    "appId": "xxxxxxxxx",
    "version": 1,
    "riskScore": 90,
    "tags": \[
        "phishing",
        "malware",
        "interdiction",
        "control"
    \]
}

2\. When the value of **version** in **FraudDetectionRequest** is **2**, the payload example is as follows:

{
    "timestampMs": 9xxxxxxxxx,
    "nonce": "Rxxxxxxxxx",
    "appId": "xxxxxxxxx",
    "version": 2,
    "riskScore": 90,
    "tags": \[
        {"tag": "phishing", "level": "high", "lastTime": 9876543216548},
        {"tag": "malware", "level": "low", "lastTime": 965432198756},
        {"tag": "interdiction", "level": "medium", "lastTime": 965432198756},
        {"tag": "control", "level": "medium", "lastTime": 965432198123}
    \]
}

NOTE:

-   **nonce**: Base64-encoding result of the nonce value passed when the **detectFraudRisk** API is called.
-   **timestampMs**: timestamp generated by the Huawei signature server.
-   **appId**: same as that in the signature information.
-   **riskScore**: fraud risk score of a device. The value ranges from 0 to 100. A higher score indicates a higher risk.
-   **tags**: fraud risk clues. If this field is empty, no fraud risk is found.
-   **version**: version number of the detection result message format.

 |

Description of values of **tags**

| 
Value of tags

 | 

Description

 |
| :-- | :-- |
| 

phishing

 | 

Over the past period, a device was involved in one or more of the following activities that led to fraudulent information:

Answered fraudulent calls

Received fraudulent SMS messages

Accessed fraudulent websites

 |
| 

malware

 | 

Over the past period, apps that might be used for fraudulent activities were installed or running on a device. These apps include:

Recently installed or running niche chat apps

Recently installed or running finance apps

Recently installed or running video conferencing apps

 |
| 

interdiction

 | 

A device is preventing the user from receiving calls because the device is in one or more of the following states:

Call forwarding enabled

Airplane mode on

Currently in a voice call

 |
| 

control

 | 

A device may be at risk of being manipulated due to the following reason:

Screen sharing enabled

 |

Description of values of **level**

| 
Value of level

 | 

Description

 |
| :-- | :-- |
| 

low

 | 

Low risk.

 |
| 

medium

 | 

Medium risk.

 |
| 

high

 | 

High risk.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/businessriskintelligentdetection/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

Invalid parameters.

 |
| 

1012500001

 | 

Internal error.

 |
| 

1012500002

 | 

The network is unreachable.

 |
| 

1012500003

 | 

Access cloud server fail.

 |
| 

1012500004

 | 

Verify cloud capability fail.

 |

**Example:**

import { businessRiskIntelligentDetection } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

const TAG = "\[BusinessRiskIntelligentDetectionModel\]";

let rand = cryptoFramework.createRandom();
let len = 48;
let randData = rand.generateRandomSync(len);
let params = {
  nonce: randData.data,
  algorithm: businessRiskIntelligentDetection.SigningAlgorithm.ES256
} as businessRiskIntelligentDetection.FraudDetectionRequest;
try {
  hilog.info(0x0000, TAG, 'Detect fraud risk begin.');
  businessRiskIntelligentDetection.detectFraudRisk(params).then((result: string) => {
    hilog.info(0x0000, TAG, 'Detect fraud risk success: %{public}s', result);
  }).catch((error: Error) => {
    let e: BusinessError = error as BusinessError;
    hilog.error(0x0000, TAG, 'Detect fraud risk failed: %{public}d %{public}s', e.code, e.message);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, TAG, 'Detect fraud risk failed: %{public}d %{public}s', e.code, e.message);
}

#### detectSimulatedClickRisk

detectSimulatedClickRisk(params: [SimulatedClickDetectionRequest](#section157731058201714)): Promise<string>

Obtains detection results for cheating behaviors such as automated clicks and device farming. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Security.BusinessRiskIntelligentDetection

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

params

 | 

[SimulatedClickDetectionRequest](#section157731058201714)

 | 

Yes

 | 

Request parameters.

 |

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

Promise used to return the simulated click detection result.

The JSON fields are as follows:

{
    "timestampMs": 9860437986543,
    "version": 1,
    "riskDecision": "fake",
    "tags": \["AbnormalTap"\]
}

NOTE:

-   **timestampMs**: timestamp generated when a request is initiated.
-   **riskDecision**: risk detection result.
-   **version**: version number of the detection result message format. The default value is **1**. Currently, the value can only be **1**.
-   **tags**: key features of simulated clicks. If this field is empty, no key feature is found. If this field is not empty, key features are found.

 |

| 
Value of tags

 | 

Description

 |
| :-- | :-- |
| 

AbnormalDeviceIntegrity

 | 

The device integrity is compromised.

 |
| 

AbnormalDeviceBehavior

 | 

Abnormal device behavior, such as device connection error and incorrect sensor status.

 |
| 

AbnormalTap

 | 

Abnormal clicks, such as click event injection and automated clicks.

 |

| 
Value of riskDecision

 | 

Description

 |
| :-- | :-- |
| 

fake

 | 

This device has cheating risks, such as automated device control and device farming. For details, please refer to **tags**.

 |
| 

likelyReal

 | 

It's highly likely that a real user is currently operating the device.

 |
| 

unknown

 | 

Cannot determine whether there is a risk since no obvious feature is detected.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/businessriskintelligentdetection/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1012500001

 | 

Internal error.

 |
| 

1012500002

 | 

The network is unreachable.

 |
| 

1012500003

 | 

Access cloud server fail.

 |
| 

1012500004

 | 

Verify cloud capability fail.

 |
| 

1012500005

 | 

The interface access frequency exceeds the limit.

 |
| 

1012500006

 | 

Internal timeout.

 |
| 

1012500007

 | 

Invalid parameters.

 |

**Example:**

import { businessRiskIntelligentDetection } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "BusinessRiskIntelligentDetectionJsTest";

let params = {
    version: 1
} as businessRiskIntelligentDetection.SimulatedClickDetectionRequest;
try {
    hilog.info(0x0000, TAG, 'Detect simulated click risk begin.');
    businessRiskIntelligentDetection.detectSimulatedClickRisk(params).then((result: string) => {
        hilog.info(0x0000, TAG, 'Detect simulated click risk success: %{public}s', result);
    }).catch((error: Error) => {
        let e: BusinessError = error as BusinessError;
        hilog.error(0x0000, TAG, 'Detect simulated click risk failed: %{public}d %{public}s', e.code, e.message);
    });
} catch (error) {
    let e: BusinessError = error as BusinessError;
    hilog.error(0x0000, TAG, 'Detect simulated click risk failed: %{public}d %{public}s', e.code, e.message);
}

#### detectSimulatedClickRiskEnhanced

detectSimulatedClickRiskEnhanced(params: SimulatedClickDetectionEnhancedRequest): Promise<string>

Obtains enhanced detection results for cheating behaviors such as automated clicks and device farming. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Security.BusinessRiskIntelligentDetection

**Start version**: 6.0.2(22)

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

params

 | 

[SimulatedClickDetectionEnhancedRequest](#section97791919183510)

 | 

Yes

 | 

Request parameters.

 |

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

Enhanced simulated click detection result, which is a JWS string encoded using Base64URL and returned through a promise. If an exception or error occurs, an error code will be returned.

Fields in JWS-format **Header** are as follows:

{
    "alg": "ES256",
    "x5c": \["",""\],
    "nonce": "R2Rra24fVm5xa2Mg",
    "appId": "xxxxxxxxx",
    "typ": "JWT"
}

NOTE:

**alg**: digital signature algorithm. The value **ES256** indicates SHA256withECDSA.

**x5c**: certificate chain used by the Huawei signature server for JWS signing. **x5c\[0\]** indicates the certificate for JWS signing and **x5c\[1\]** indicates the level-2 CA certificate.

**nonce**: Base64-encoded nonce value in the **SimulatedClickDetectionEnhancedRequest** parameter.

**appId**: app ID obtained from [HUAWEI Developers](https://developer.huawei.com/consumer/en).

**typ**: indicates that the result is in JWT format.

Fields in JWS-format **Payload** are as follows:

{
    "timestampMs": 9860437986543,
    "version": 1,
    "riskDecision": "fake",
    "tags": \["AbnormalTap"\]
}

NOTE:

-   **timestampMs**: timestamp generated by the Huawei signature server.
-   **riskDecision**: risk detection result.
-   **version**: version number of the detection result message format. The default value is **1**. Currently, the value can only be **1**.
-   **tags**: key features of simulated clicks. If this field is empty, no key feature is found. If this field is not empty, key features are found.

 |

| 
Value of tags

 | 

Description

 |
| :-- | :-- |
| 

AbnormalDeviceIntegrity

 | 

The device integrity is compromised.

 |
| 

AbnormalDeviceBehavior

 | 

Abnormal device behavior, such as device connection error and incorrect sensor status.

 |
| 

AbnormalTap

 | 

Abnormal clicks, such as click event injection and automated clicks.

 |

| 
Value of riskDecision

 | 

Description

 |
| :-- | :-- |
| 

fake

 | 

This device has cheating risks, such as automated device control and device farming. For details, please refer to **tags**.

 |
| 

likelyReal

 | 

It's highly likely that a real user is currently operating the device.

 |
| 

unknown

 | 

Cannot determine whether there is a risk since no obvious feature is detected.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/businessriskintelligentdetection/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1012500001

 | 

Internal error

 |
| 

1012500002

 | 

The network is unreachable.

 |
| 

1012500003

 | 

Access cloud server fail.

 |
| 

1012500005

 | 

The interface access frequency exceeds the limit.

 |
| 

1012500006

 | 

Internal timeout.

 |
| 

1012500007

 | 

Invalid parameters.

 |

**Example:**

import { businessRiskIntelligentDetection } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

const TAG = "BusinessRiskIntelligentDetectionJsTest";

let nonceLength = 48;
let nonceBlob = cryptoFramework.createRandom().generateRandomSync(nonceLength);
let params = {
    version: 1,
    nonce: nonceBlob.data,
    algorithm: businessRiskIntelligentDetection.SigningAlgorithm.ES256
} as businessRiskIntelligentDetection.SimulatedClickDetectionEnhancedRequest;
try {
    hilog.info(0x0000, TAG, 'Detect simulated click risk enhanced begin.');
    businessRiskIntelligentDetection.detectSimulatedClickRiskEnhanced(params).then((result: string) => {
        hilog.info(0x0000, TAG, 'Detect simulated click risk enhanced success: %{public}s', result);
    }).catch((error: Error) => {
        let e: BusinessError = error as BusinessError;    
        hilog.error(0x0000, TAG, 'Detect simulated click risk enhanced failed: %{public}d %{public}s', e.code, e.message);
    });
} catch (error) {
    let e: BusinessError = error as BusinessError;
    hilog.error(0x0000, TAG, 'Detect simulated click risk enhanced failed: %{public}d %{public}s', e.code, e.message);
}
