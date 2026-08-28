# walletPass (Pass Capability)

This module provides the capabilities for accessing Wallet Kit.

**Start version**: 5.0.0(12)

#### Module Import

import { walletPass } from '@kit.WalletKit';

#### WalletPassClient

Main entrance for accessing Wallet pass functions. All Wallet pass-related methods are accessed through this entrance.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

#### \[h2\]constructor

constructor(context: common.UIAbilityContext)

Constructor.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

**Parameters:**

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

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

**UIAbility** context.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';

private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
private callback: rpc.RemoteObject | null = null;
private jweContent: string = '';
private passType: string = '';
private targetDeviceType: string = '';
private serialNumber: string = '';
private registerName: string = '';
private rkeCommand: string = '';

#### \[h2\]queryPassDeviceInfo

queryPassDeviceInfo(passStr: string): Promise<string>

Queries the unique ID and supported capabilities of the current device, which are used to match activated passes on the HUAWEI Wallet server. When a pass is activated, the target device ID can be specified to enhance security.

This API returns the result asynchronously through a promise.

Multi-thread calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

passStr

 | 

string

 | 

Yes

 | 

Information passed via a JSON string in _key_\-_value_ format.

The values of **key** are as follows:

-   **passType**: service ID registered when [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations) in AppGallery Connect.
-   **targetDeviceType**: target device type. The options are as follows:
    -   **phone**: mobile phone
    -   **wear**: wearable
    -   **all**: mobile phone and wearable

 |

**Returns**:

| 
Type

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<string>

 | 

**Promise** object, which is used to return information via a JSON string of the array type in _key_\-_value_ format.

The values of **key** are as follows:

-   **deviceType**: device type. The options are as follows:
    -   **phone**: mobile phone
    -   **wear**: wearable
-   **passDeviceId**: identifier that specifies the pass-device association.
-   **deviceModel**: device model that is supported.
-   **passCapabilityVersion**: pass capability version number, which is used for compatibility processing. The initial value is **1**.
-   **deviceModelNumber**: device model number, which is used to obtain matched calibration data.
-   **deviceCapabilities**: set of the supported capabilities. In the result, whether NFC/BLE/UWB/SLE is supported is returned synchronously. The mapping between codes and capabilities is as follows:
    -   NFC: 0200
    -   NFC + BLE: 0201
    -   UWB: 0202
    -   SLE: 0203

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: Mandatory parameters are left unspecified.

 |
| 

1010200001

 | 

No permission to access the Wallet APIs.

 |
| 

1010200002

 | 

Wallet app not found.

 |
| 

1010200003

 | 

The environment of the wallet is not ready.

 |
| 

1010200006

 | 

The device's remote paired watch cannot be connected

 |
| 

1010220003

 | 

Pass service is temporarily unavailable.

 |
| 

1010200013

 | 

Operation failed because of an internal error.

 |
| 

1010200014

 | 

The Wallet APIs can be called by the device owner only.

 |
| 

1010200010

 | 

Network connection error.

 |

**Example**:

async queryPassDeviceInfo() {
  let passStr = JSON.stringify({
    passType: this.passType,
    targetDeviceType: this.targetDeviceType
  });
  this.walletPassClient.queryPassDeviceInfo(passStr).then((result: string) => {
    console.info(\`Succeeded in querying passDeviceInfo, result:${result}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to query passDeviceInfo, code:${err.code}, message:${err.message}\`);
  })
}

#### \[h2\]canAddPass

canAddPass(passStr: string): Promise<string>

Checks whether a pass can be activated on the current device and returns a result code.

This API returns the result asynchronously through a promise.

Multi-thread calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

passStr

 | 

string

 | 

Yes

 | 

Information passed via a JSON string in _key_\-_value_ format.

The values of **key** are as follows:

-   **passType**: service ID registered when [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations) in AppGallery Connect.
-   **targetDeviceType**: target device type. The options are as follows:
    -   **phone**: mobile phone
    -   **wear**: wearable
    -   **all**: mobile phone and wearable

 |

**Returns**:

| 
Type

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<string>

 | 

**Promise** object, which is used to return information via a JSON string of the array type in _key_\-_value_ format.

The values of **key** are as follows:

-   **passType**: service ID.
-   **deviceType**: device type. The options are as follows:
    -   **phone**: mobile phone
    -   **wear**: wearable
-   **passDeviceId**: identifier that specifies the pass-device association.
-   **deviceModel**: device model that is supported.
-   **result**: result code. The options are as follows:
    -   **0**: The pass can be activated.
    -   **1**. The ROM version is out of date.
    -   **2**: The HUAWEI Wallet version is out of date.
    -   **3**: The ROM version and HUAWEI Wallet version are both out of date.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: Mandatory parameters are left unspecified.

 |
| 

1010200001

 | 

No permission to access the Wallet APIs.

 |
| 

1010200002

 | 

Wallet app not found.

 |
| 

1010200003

 | 

The environment of the wallet is not ready.

 |
| 

1010200004

 | 

The device does not support this card.

 |
| 

1010200006

 | 

The device's remote paired watch cannot be connected.

 |
| 

1010200009

 | 

The chip space is full, and no more cards can be added.

 |
| 

1010200010

 | 

Network connection error.

 |
| 

1010220002

 | 

The card already exists in the specified device.

 |
| 

1010220003

 | 

Pass service is temporarily unavailable.

 |
| 

1010200013

 | 

Operation failed because of an internal error.

 |
| 

1010200014

 | 

The Wallet APIs can be called by the device owner only.

 |
| 

1010200015

 | 

This card is not available for a child account.

 |
| 

1010200016

 | 

This card is not available for the current country or region.

 |
| 

1010220005

 | 

The number of cards has reached the upper limit.

 |

**Example**:

async canAddPass() {
  let passStr = JSON.stringify({
    passType: this.passType,
    targetDeviceType: this.targetDeviceType
  });
  this.walletPassClient.canAddPass(passStr).then((result: string) => {
    console.info(\`Succeeded in checking addPass, result:${result}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to check addPass, code:${err.code}, message:${err.message}\`);
  })
}

#### \[h2\]initWalletEnvironment

initWalletEnvironment(passStr: string): Promise<void>

Initializes HUAWEI Wallet and prompts a user to agree to the agreement for pass activation or sign in to their account.

This API returns the result asynchronously through a promise.

Multi-thread calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

passStr

 | 

string

 | 

Yes

 | 

Information passed via a JSON string in _key_\-_value_ format.

The value of **key** can only be **targetDeviceType**.

-   **targetDeviceType**: target device type. The options are as follows:
    -   **phone**: mobile phone
    -   **wear**: wearable
    -   **all**: mobile phone and wearable

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

**Promise** object. No result is returned.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: Mandatory parameters are left unspecified.

 |
| 

1010200002

 | 

Wallet app not found.

 |
| 

1010200005

 | 

The operation was canceled by the user.

 |
| 

1010200011

 | 

Failed to initialize the environment.

 |
| 

1010200013

 | 

Operation failed because of an internal error.

 |
| 

1010200014

 | 

The Wallet APIs can be called by the device owner only.

 |
| 

1010200017

 | 

The Wallet app was closed by the user.

 |

**Example**:

async initWalletEnvironment() {
  let passStr = JSON.stringify({
    targetDeviceType: this.targetDeviceType
  });
  this.walletPassClient.initWalletEnvironment(passStr).then(() => {
    console.info(\`Succeeded in initiating walletEnvironment\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to initiate walletEnvironment, code:${err.code}, message:${err.message}\`);
  })
}

#### \[h2\]addPass

addPass(passStr: string): Promise<string>

Launches HUAWEI Wallet with the JSON web encryption (JWE) data and activates the pass as requested by a user.

This API returns the result asynchronously through a promise.

Multi-thread calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

passStr

 | 

string

 | 

Yes

 | 

Information passed via a JSON string in _key_\-_value_ format.

The value of **key** can only be **jweContent**.

-   **jweContent**: JWE data generated in [Generating JWE Data](../../rest-api-reference/digital-car-key-apis/document.md#section1310081523717).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<string>

 | 

**Promise** object, which is used to return information via a JSON string in _key_\-_value_ format.

The values of **key** are as follows:

-   **passType**: service ID for which the pass is activated.
-   **serialNumber**: unique ID of the pass.
-   **deviceType**: type of the device for which the pass is activated. The options are as follows:
    -   **phone**: mobile phone
    -   **wear**: wearable
    -   **all**: mobile phone and wearable
-   **passDeviceId**: account-device ID of the device for which the pass is activated.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: Mandatory parameters are left unspecified.

 |
| 

1010200002

 | 

Wallet app not found.

 |
| 

1010200004

 | 

The device does not support this card.

 |
| 

1010200005

 | 

The operation was canceled by the user.

 |
| 

1010200006

 | 

The device's remote paired watch cannot be connected.

 |
| 

1010200009

 | 

The chip space is full, and no more cards can be added.

 |
| 

1010200012

 | 

Duplicate request.

 |
| 

1010220002

 | 

The card already exists in the specified device.

 |
| 

1010220003

 | 

Pass service is temporarily unavailable.

 |
| 

1010220401

 | 

Failed to add the card because the signature verification failed.

 |
| 

1010220402

 | 

Failed to add the card because the data decryption failed.

 |
| 

1010220403

 | 

Failed to add the card because the instance ID does not exist.

 |
| 

1010220404

 | 

Failed to add the card because the instance ID has been used.

 |
| 

1010200013

 | 

Operation failed because of an internal error.

 |
| 

1010200014

 | 

The Wallet APIs can be called by the device owner only.

 |
| 

1010200015

 | 

This card is not available for a child account.

 |
| 

1010200016

 | 

This card is not available for the current country or region.

 |
| 

1010200017

 | 

The Wallet app was closed by the user.

 |
| 

1010220005

 | 

The number of cards has reached the upper limit.

 |

**Example**:

async addPass() {
  let passStr = JSON.stringify({
    jweContent: this.jweContent
  });
  this.walletPassClient.addPass(passStr).then((result: string) => {
    console.info(\`Succeeded in adding pass, result:${result}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to add pass, code:${err.code}, message:${err.message}\`);
  })
}

#### \[h2\]queryPass

queryPass(passStr: string): Promise<string>

Checks whether a specified pass is activated on the current device.

This API returns the result asynchronously through a promise.

Multi-thread calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

**Parameters:**

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

passStr

 | 

string

 | 

Yes

 | 

Information passed via a JSON string in _key_\-_value_ format.

The values of **key** are as follows:

-   **passType**: service ID registered when [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations) in AppGallery Connect.
-   **serialNumber**: unique identifier of a pass, which is defined in [Applying for a Key Card](../../rest-api-reference/digital-car-key-apis/document.md#section129511211195).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<string>

 | 

**Promise** object, which is used to return information via a JSON string of the array type in _key_\-_value_ format.

The values of **key** are as follows:

-   **passType**: service ID.
-   **serialNumber**: unique identifier of a pass.
-   **deviceType**: device type. The options are as follows:
    -   **phone**: mobile phone
    -   **wear**: wearable
-   **passDeviceId**: identifier that specifies the pass-device association.
-   **deviceModel**: device model that is supported.
-   **cardStatus**: pass status. The options are as follows:
    -   **0**: available.
    -   **1**: unavailable.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: Mandatory parameters are left unspecified.

 |
| 

1010200001

 | 

No permission to access the Wallet APIs.

 |
| 

1010200002

 | 

Wallet app not found.

 |
| 

1010200003

 | 

The environment of the wallet is not ready.

 |
| 

1010200006

 | 

The device's remote paired watch cannot be connected.

 |
| 

1010220501

 | 

No card that meets the search criteria is found.

 |
| 

1010200013

 | 

Operation failed because of an internal error.

 |
| 

1010200014

 | 

The Wallet APIs can be called by the device owner only.

 |

**Example**:

async queryPass() {
  let passStr = JSON.stringify({
    passType: this.passType,
    serialNumber: this.serialNumber
  });
  this.walletPassClient.queryPass(passStr).then((result: string) => {
    console.info(\`Succeeded in querying pass, result: ${result}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to query pass, code:${err.code}, message:${err.message}\`);
  })
}

#### \[h2\]viewPass

viewPass(passStr: string): Promise<void>

Redirects a user to HUAWEI Wallet to check the details of an activated pass.

This API returns the result asynchronously through a promise.

Multi-thread calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

passStr

 | 

string

 | 

Yes

 | 

Information passed via a JSON string in _key_\-_value_ format.

The values of **key** are as follows:

-   **passType**: service ID registered when [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations) in AppGallery Connect.
-   **serialNumber**: unique identifier of a pass, which is defined in [Applying for a Key Card](../../rest-api-reference/digital-car-key-apis/document.md#section129511211195).

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

**Promise** object. No result is returned.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1010200002

 | 

Wallet app not found.

 |
| 

1010200013

 | 

Operation failed because of an internal error.

 |

**Example**:

async viewPass() {
  let passStr = JSON.stringify({
    passType: this.passType,
    serialNumber: this.serialNumber
  });
  try {
    await this.walletPassClient.viewPass(passStr);
    console.info(\`Succeeded in viewing pass\`);
  } catch (err) {
    console.error(\`Failed to view pass, code:${err.code}, message:${err.message}\`);
  }
}

#### \[h2\]updatePass

updatePass(passStr: string): Promise<string>

Updates a pass. (This API is reserved and does not provide specific functionality currently.)

This API returns the result asynchronously through a promise.

Multi-thread calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

passStr

 | 

string

 | 

Yes

 | 

Information passed via a JSON string in _key_\-_value_ format.

The values of **key** are as follows:

-   **passType**: service ID registered when [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations) in AppGallery Connect.
-   **serialNumber**: unique identifier of a pass, which is defined in [Applying for a Key Card](../../rest-api-reference/digital-car-key-apis/document.md#section129511211195).

 |

**Returns**:

| 
Type

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<string>

 | 

**Promise** object, which is used to return information via a JSON string in _key_\-_value_ format.

The value of **key** can only be **result**.

-   **result**: pass update result. The code **0** is returned if the update is successful.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: Mandatory parameters are left unspecified.

 |
| 

1010200001

 | 

No permission to access the Wallet APIs.

 |
| 

1010200002

 | 

Wallet app not found.

 |
| 

1010200005

 | 

The operation was canceled by the user.

 |
| 

1010200006

 | 

The device's remote paired watch cannot be connected.

 |
| 

1010220003

 | 

Pass service is temporarily unavailable.

 |
| 

1010220004

 | 

The card does not exist in the specified device.

 |
| 

1010220701

 | 

Failed to update the card because no update is detected.

 |
| 

1010200013

 | 

Operation failed because of an internal error.

 |
| 

1010200014

 | 

The Wallet APIs can be called by the device owner only.

 |
| 

1010200010

 | 

Network connection error.

 |

**Example**:

async updatePass() {
  let passStr = JSON.stringify({
    passType: this.passType,
    serialNumber: this.serialNumber
  });
  this.walletPassClient.updatePass(passStr).then((result: string) => {
    console.info(\`Succeeded in updating pass,result: ${result}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to update pass, code:${err.code}, message:${err.message}\`);
  })
}

#### \[h2\]deletePass

deletePass(passStr: string): Promise<string>

Deletes a pass. (This API is reserved and does not provide specific functionality currently.)

This API returns the result asynchronously through a promise.

Multi-thread calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

**Parameters:**

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

passStr

 | 

string

 | 

Yes

 | 

Information passed via a JSON string in _key_\-_value_ format.

The values of **key** are as follows:

-   **passType**: service ID registered when [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations) in AppGallery Connect.
-   **serialNumber**: unique identifier of a pass, which is defined in [Applying for a Key Card](../../rest-api-reference/digital-car-key-apis/document.md#section129511211195).

 |

**Returns**:

| 
Type

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<string>

 | 

**Promise** object, which is used to return information via a JSON string in _key_\-_value_ format.

The value of **key** can only be **result**.

-   **result**: pass deletion result. The code **0** is returned if the deletion is successful.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: Mandatory parameters are left unspecified.

 |
| 

1010200001

 | 

No permission to access the Wallet APIs.

 |
| 

1010200002

 | 

Wallet app not found.

 |
| 

1010200005

 | 

The operation was canceled by the user.

 |
| 

1010200006

 | 

The device's remote paired watch cannot be connected.

 |
| 

1010200012

 | 

Duplicate request.

 |
| 

1010220003

 | 

Pass service is temporarily unavailable.

 |
| 

1010220004

 | 

The card does not exist in the specified device.

 |
| 

1010200013

 | 

Operation failed because of an internal error.

 |
| 

1010200014

 | 

The Wallet APIs can be called by the device owner only.

 |
| 

1010200010

 | 

Network connection error.

 |
| 

1010220801

 | 

Failed to delete the card because the signature verification failed.

 |

**Example**:

async deletePass() {
  let passStr = JSON.stringify({
    passType: this.passType,
    serialNumber: this.serialNumber
  });
  this.walletPassClient.deletePass(passStr).then((result: string) => {
    console.info(\`Succeeded in deleting pass, result: ${result}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to delete pass, code:${err.code}, message:${err.message}\`);
  })
}

#### \[h2\]queryICCEConnectionState

queryICCEConnectionState(rkeStr: string): Promise<string>

Queries the car control connection status.

This API returns the result asynchronously through a promise.

Multi-thread calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

**Parameters:**

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

rkeStr

 | 

string

 | 

Yes

 | 

Information passed via a JSON string in _key_\-_value_ format.

The values of **key** are as follows:

-   **passType**: service ID registered when [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations) in AppGallery Connect.
-   **serialNumber**: unique identifier of a pass, which is defined in [Applying for a Key Card](../../rest-api-reference/digital-car-key-apis/document.md#section129511211195).

 |

**Returns**:

| 
Type

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<string>

 | 

**Promise** object, which is used to return information via a JSON string in _key_\-_value_ format.

The values of **key** are as follows:

-   **deviceType**: device type. The options are as follows:
    -   **phone**: mobile phone
    -   **wear**: wearable
-   **passDeviceId**: identifier that specifies the pass-device association.
-   **deviceModel**: device model that is supported.
-   **connectionState**: connection status. The options are as follows:
    -   **0**: abnormal
    -   **1**: connecting
    -   **2**: connected
    -   **3**: not connected
    -   **4**: connection timed out
    -   **10**: not paired
    -   **11**: pairing
    -   **12**: paired
-   **authState**: authentication status. The options are as follows:
    -   **0**: not authenticated or authentication failed
    -   **1**: authentication successful

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: Mandatory parameters are left unspecified.

 |
| 

1010200001

 | 

No permission to access the Wallet APIs.

 |
| 

1010200002

 | 

Wallet app not found.

 |
| 

1010200006

 | 

The device's remote paired watch cannot be connected.

 |
| 

1010220004

 | 

The card does not exist in the specified device.

 |
| 

1010220006

 | 

Bluetooth permission is not granted.

 |
| 

1010200013

 | 

Operation failed because of an internal error.

 |
| 

1010200014

 | 

The Wallet APIs can be called by the device owner only.

 |

**Example**:

async queryICCEConnectionState() {
  let passStr = JSON.stringify({
    passType: this.passType,
    serialNumber: this.serialNumber
  });
  this.walletPassClient.queryICCEConnectionState(passStr).then((result: string) => {
    console.info(\`Succeeded in querying ICCEConnectionState, result: ${result}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to query ICCEConnectionState, code:${err.code}, message:${err.message}\`);
  })
}

#### \[h2\]startICCEConnection

startICCEConnection(rkeStr: string): Promise<string>

Connects to car control.

This API returns the result asynchronously through a promise.

Multi-thread calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

**Parameters:**

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

rkeStr

 | 

string

 | 

Yes

 | 

Information passed via a JSON string in _key_\-_value_ format.

The values of **key** are as follows:

-   **passType**: service ID registered when [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations) in AppGallery Connect.
-   **serialNumber**: unique identifier of a pass, which is defined in [Applying for a Key Card](../../rest-api-reference/digital-car-key-apis/document.md#section129511211195).

 |

**Returns**:

| 
Type

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<string>

 | 

**Promise** object, which is used to return information via a JSON string in _key_\-_value_ format.

The values of **key** are as follows:

-   **result**: authentication status. The options are as follows:
    -   **0**: paired and connected
    -   **1**: paired but not connected
    -   **2**: not paired

-   **deviceType**: device type. The options are as follows:
    -   **phone**: mobile phone
    -   **wear**: wearable
-   **passDeviceId**: identifier that specifies the pass-device association.
-   **deviceModel**: device model that is supported.
-   **connectionState**: connection status. The options are as follows:
    -   **0**: abnormal
    -   **1**: connecting
    -   **2**: connected
    -   **3**: not connected
    -   **4**: connection timed out
    -   **10**: not paired
    -   **11**: pairing
    -   **12**: paired
-   **authState**: authentication status. The options are as follows:
    -   **0**: not authenticated or authentication failed
    -   **1**: authentication successful

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: Mandatory parameters are left unspecified.

 |
| 

1010200001

 | 

No permission to access the Wallet APIs.

 |
| 

1010200002

 | 

Wallet app not found.

 |
| 

1010200005

 | 

The operation was canceled by the user.

 |
| 

1010200006

 | 

The device's remote paired watch cannot be connected.

 |
| 

1010200010

 | 

Network connection error.

 |
| 

1010200012

 | 

Duplicate request.

 |
| 

1010221001

 | 

Connection failed because the pairing code is not obtained.

 |
| 

1010220004

 | 

The card does not exist in the specified device.

 |
| 

1010220006

 | 

Bluetooth permission is not granted.

 |
| 

1010200013

 | 

Operation failed because of an internal error.

 |
| 

1010200014

 | 

The Wallet APIs can be called by the device owner only.

 |

**Example**:

async startICCEConnection() {
  let passStr = JSON.stringify({
    passType: this.passType,
    serialNumber: this.serialNumber
  });
  this.walletPassClient.startICCEConnection(passStr).then((result: string) => {
    console.info(\`Succeeded in starting ICCEConnection, result: ${result}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to start ICCEConnection, code:${err.code}, message:${err.message}\`);
  })
}

#### \[h2\]registerICCEListener

registerICCEListener(rkeStr: string, eventNotifyListener: rpc.RemoteObject): Promise<string>

Registers a listener.

This API returns the result asynchronously through a promise.

Multi-thread calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

**Parameters:**

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

rkeStr

 | 

string

 | 

Yes

 | 

Information passed via a JSON string in _key_\-_value_ format.

The values of **key** are as follows:

-   **passType**: service ID registered when [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations) in AppGallery Connect.
-   **registerName**: name of the app for which a listener needs to be registered, which is usually the app package name.

 |
| 

eventNotifyListener

 | 

rpc.RemoteObject

 | 

Yes

 | 

Callback event in **rpc.RemoteObject** format.

 |

**Returns**:

| 
Type

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<string>

 | 

**Promise** object, which is used to return information via a JSON string in _key_\-_value_ format.

The value of **key** can only be **result**.

-   **result**: registration result. The code **0** is returned if the registration is successful.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: Mandatory parameters are left unspecified.

 |
| 

1010200001

 | 

No permission to access the Wallet APIs.

 |
| 

1010200002

 | 

Wallet app not found.

 |
| 

1010221101

 | 

Registration failed because of duplicate register name.

 |
| 

1010200012

 | 

Duplicate request.

 |
| 

1010200013

 | 

Operation failed because of an internal error.

 |
| 

1010200014

 | 

The Wallet APIs can be called by the device owner only.

 |

**Example**:

import { ICCECallBack } from './ICCECallBack';

async registerICCEListener() {
  let passStr = JSON.stringify({
     passType: this.passType,
     registerName: this.registerName
  });
  this.callback = new ICCECallBack();
  this.walletPassClient.registerICCEListener(passStr, this.callback).then((result: string) => {
    console.info(\`Succeeded in registering ICCEListener, result: ${result}\`);
   }).catch((err: BusinessError) => {
    console.error(\`Failed to register ICCEListener, code:${err.code}, message:${err.message}\`);
  })
}

// ICCECallBack.ets
export class ICCECallBack extends rpc.RemoteObject {
  constructor() {
    super('ICCECallBack');
  }

  async onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence, option: rpc.MessageOption): Promise<boolean> {
    let codeInt = data.readInt();
    return true;
  }
}

#### \[h2\]unregisterICCEListener

unregisterICCEListener(rkeStr: string): Promise<string>

Unregisters a listener.

This API returns the result asynchronously through a promise.

Multi-thread calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

**Parameters:**

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

rkeStr

 | 

string

 | 

Yes

 | 

Information passed via a JSON string in _key_\-_value_ format.

The values of **key** are as follows:

-   **passType**: service ID registered when [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations) in AppGallery Connect.
-   **registerName**: name of the app for which a listener needs to be unregistered, which is usually the app package name.

 |

**Returns**:

| 
Type

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<string>

 | 

**Promise** object, which is used to return information via a JSON string in _key_\-_value_ format.

The value of **key** can only be **result**.

-   **result**: unregistration result. The code **0** is returned if the unregistration is successful.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: Mandatory parameters are left unspecified.

 |
| 

1010200001

 | 

No permission to access the Wallet APIs.

 |
| 

1010200002

 | 

Wallet app not found.

 |
| 

1010221201

 | 

The registration may have been unregistered before.

 |
| 

1010200013

 | 

Operation failed because of an internal error.

 |
| 

1010200014

 | 

The Wallet APIs can be called by the device owner only.

 |

**Example**:

async unregisterICCEListener() {
  let passStr = JSON.stringify({
    passType: this.passType,
    registerName: this.registerName
  });

  this.walletPassClient.unregisterICCEListener(passStr).then((result: string) => {
    console.info(\`Succeeded in unregistering ICCEListener, result: ${result}\`);
    this.callback = null;
  }).catch((err: BusinessError) => {
    console.error(\`Failed to unregister ICCEListener, code:${err.code}, message:${err.message}\`);
  })
}

#### \[h2\]sendICCERKEMessage

sendICCERKEMessage(rkeStr: string): Promise<string>

Sends car control commands.

This API returns the result asynchronously through a promise.

Multi-thread calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

**Parameters:**

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

rkeStr

 | 

string

 | 

Yes

 | 

Information passed via a JSON string in _key_\-_value_ format.

The values of **key** are as follows:

-   **passType**: service ID registered when [applying for Wallet Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wallet-preparations) in AppGallery Connect.
-   **serialNumber**: unique identifier of a pass, which is defined in [Applying for a Key Card](../../rest-api-reference/digital-car-key-apis/document.md#section129511211195).
-   **rkeCommand**: command.
-   **encryptFlag**: encryption flag. The options are as follows:
    -   **0**: Encryption is not required.
    -   **1**: Encryption based on the channel session key is required.
-   **directionFlag**: direction flag. The options are as follows:
    -   **0**: Report the result.
    -   **1**: Send a command.

 |

**Returns**:

| 
Type

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<string>

 | 

**Promise** object, which is used to return information via a JSON string in _key_\-_value_ format.

The values of **key** are as follows:

-   **deviceType**: device type. The options are as follows:
    -   **phone**: mobile phone
    -   **wear**: wearable
-   **passDeviceId**: identifier that specifies the pass-device association.
-   **deviceModel**: device model that is supported.
-   **result**: car control command sending result, which is returned immediately when the command reaches the car control. The options are as follows:
    -   **0**: The command is sent successfully.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: Mandatory parameters are left unspecified.

 |
| 

1010200001

 | 

No permission to access the Wallet APIs.

 |
| 

1010200002

 | 

Wallet app not found.

 |
| 

1010200006

 | 

The device's remote paired watch cannot be connected.

 |
| 

1010200012

 | 

Duplicate request.

 |
| 

1010220004

 | 

The card does not exist in the specified device.

 |
| 

1010220006

 | 

Bluetooth permission is not granted.

 |
| 

1010221301

 | 

Failed to send the RKE message because of a connection failure.

 |
| 

1010221302

 | 

Failed to send the RKE message because of an authentication failure.

 |
| 

1010200013

 | 

Operation failed because of an internal error.

 |
| 

1010200014

 | 

The Wallet APIs can be called by the device owner only.

 |

**Example**:

async sendICCERKEMessage() {
  let passStr = JSON.stringify({
    passType: this.passType,
    serialNumber: this.serialNumber,
    rkeCommand: this.rkeCommand,
    encryptFlag: '0',
    directionFlag: '1'
  });
  this.walletPassClient.sendICCERKEMessage(passStr).then((result: string) => {
    console.info(\`Succeeded in sending ICCERKEMessage, result: ${result}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to send ICCERKEMessage, code:${err.code}, message:${err.message}\`);
  })
}
