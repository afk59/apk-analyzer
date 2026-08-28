# walletTransitCard (Transportation Card Capability)

This module provides the capabilities for accessing the HUAWEI Wallet transportation card service.

**Start version**: 5.0.0(12)

#### Module Import

import { walletTransitCard } from '@kit.WalletKit';

#### TransitCardClient

Main entrance for accessing Wallet transportation card functions. All Wallet transportation card-related methods are accessed through this entrance.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

#### \[h2\]constructor

constructor(context: common.UIAbilityContext, callerId: string)

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

Mandatory

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
| 

callerId

 | 

string

 | 

Yes

 | 

Caller ID. Obtain the ID from the operations personnel of Wallet Kit when applying for the transportation card service. Only **invited apps** can request this information.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { walletTransitCard } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

#### \[h2\]getCardMetadataInDevice

getCardMetadataInDevice(specifiedDeviceType: DeviceType, callerToken?: string): Promise<CardMetadataInDevice\[\]>

Obtains information about transportation cards that can be activated or have already been activated on the current device, including the device information and supported transportation card metadata. If no embedded secure element (eSE) is available, an empty array will be returned. If the device does not support any transportation card, the **CardMetadataInDevice** cannot be added to the array for the device.

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

specifiedDeviceType

 | 

[DeviceType](#section423812461512)

 | 

Yes

 | 

Device type, which is an enumeration.

 |
| 

callerToken

 | 

string

 | 

No

 | 

JWT used for authenticating an applet in apps such as WeChat and Alipay.

 |

**Returns**:

| 
Type

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<[CardMetadataInDevice](#section691675771410)\[\]>

 | 

**Promise** object, which is used to return a **CardMetadataInDevice** metadata array containing device information and card metadata.

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

Parameter error. Possible causes: Parameter verification failed.

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

1010200010

 | 

Network connection error.

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

1010210701

 | 

Failed to verify the caller token.

 |
| 

1010210702

 | 

Failed to get the metadata of the cards.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { walletTransitCard } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');
async getCardMetadataInDevice() {
  this.transitCardClient.getCardMetadataInDevice(walletTransitCard.DeviceType.DEVICE\_PHONE).then((result) => {
    console.info(\`Succeeded in getting cardMetadataInDevice\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get CardMetadataInDevice, code:${err.code}, message:${err.message}\`);
  })
}

#### \[h2\]getTransitCardInfo

getTransitCardInfo(logicalCardNumber: string, specifiedDeviceId: string, callerToken?: string): Promise<TransitCardInfo>

Queries information about a transportation card specified by **cardNumber**.

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

logicalCardNumber

 | 

string

 | 

Yes

 | 

Card number.

 |
| 

specifiedDeviceId

 | 

string

 | 

Yes

 | 

ID of the device where the specified card is added.

 |
| 

callerToken

 | 

string

 | 

No

 | 

JWT used for authenticating an applet in apps such as WeChat and Alipay.

 |

**Returns**:

| 
Type

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<[TransitCardInfo](#section1175310561152)\>

 | 

**Promise** object, which is used to return the details about the card specified by **cardNumber**.

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

Parameter error. Possible causes: Parameter verification failed.

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

1010200010

 | 

Network connection error.

 |
| 

1010200013

 | 

Operation failed because of an internal error.

 |
| 

1010210101

 | 

The card status is not correct.

 |
| 

1010210119

 | 

Failed to read the card data.

 |
| 

1010200014

 | 

The Wallet APIs can be called by the device owner only.

 |
| 

1010210102

 | 

Failed to verify the caller token.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { walletTransitCard } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');
async getTransitCardInfo() {
  // Numbers of activated transportation cards, returned by the [getCardMetadataInDevice](#section3931434195115) API.
  const logicalCardNumber = 'logicalCardNumber';
  // The value of **specifiedDeviceId** is returned by [getCardMetadataInDevice](#section3931434195115).
  const specifiedDeviceId = 'specifiedDeviceId';
  // JWT used for authenticating an applet in apps such as WeChat and Alipay.
  const callerToken= 'callerToken';
  this.transitCardClient.getTransitCardInfo(logicalCardNumber, specifiedDeviceId, callerToken).then((result) => {
    console.info(\`Succeeded in getting TransitCardInfo\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get TransitCardInfo, code:${err.code}, message:${err.message}\`);
  }) 
}

#### \[h2\]canAddTransitCard

canAddTransitCard(issuerId: string, specifiedDeviceId: string): Promise<string>

Checks whether the card associated with the specified **issuerId** can be activated on the current device and returns a token string.

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

issuerId

 | 

string

 | 

Yes

 | 

ID of a city transportation card product.

 |
| 

specifiedDeviceId

 | 

string

 | 

Yes

 | 

ID of the device where the specified card is activated.

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

**Promise** object, which is used to return a token for activating a card.

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

Parameter error. Possible causes: Parameter verification failed.

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

1010200007

 | 

The OS version is too old. Please upgrade the OS version.

 |
| 

1010200008

 | 

The wallet version is too old.

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

1010200016

 | 

This card is not available for the current country or region.

 |
| 

1010210201

 | 

The device does not support adding the card specified by issuerId.

 |
| 

1010210202

 | 

A card conflicting with the specified card already exists in the device.

 |
| 

1010210203

 | 

The specified card already exists.

 |
| 

1010210204

 | 

The card addition service is temporarily offline.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { walletTransitCard } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');
async canAddTransitCard() {
  // The value of **issuerId** must be the data returned by [getCardMetadataInDevice](#section3931434195115).
  const issuerId = 'issuerId';
  // The value of **specifiedDeviceId** is returned by [getCardMetadataInDevice](#section3931434195115).
  const specifiedDeviceId = 'specifiedDeviceId';
  this.transitCardClient.canAddTransitCard(issuerId, specifiedDeviceId).then((result) => {
    console.info(\`Succeeded in canning AddTransitCard\`);
  }).catch((err: BusinessError) => {
     console.error(\`Failed to can AddTransitCard, code:${err.code}, message:${err.message}\`);
  })
}

#### \[h2\]setupWalletEnvironment

setupWalletEnvironment(): Promise<void>

Sets up the environment of the HUAWEI Wallet app. If any API returns error code 1010200003, you need to call this API to set up the HUAWEI Wallet app.

This API returns the result asynchronously through a promise.

Multi-thread calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

**Description**

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
| 

1010200014

 | 

The Wallet APIs can be called by the device owner only.

 |
| 

1010200011

 | 

Failed to initialize the environment.

 |
| 

1010200017

 | 

The Wallet app was closed by the user.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { walletTransitCard } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');
async setupWalletEnvironment() {
  this.transitCardClient.setupWalletEnvironment().then(() => {
    console.info(\`Succeeded in setting up WalletEnvironment\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to setup WalletEnvironment, code:${err.code}, message:${err.message}\`);
  })
}

#### \[h2\]addTransitCard

addTransitCard(addCardOpaqueData: string, serverOrderId: string): Promise<CardMetadata>

Adds a specified card to HUAWEI Wallet and returns **CardMetadata**.

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

addCardOpaqueData

 | 

string

 | 

Yes

 | 

Result returned by the **canAddTransitCard** function.

 |
| 

serverOrderId

 | 

string

 | 

Yes

 | 

Order ID generated for the card activation service on the service provider server.

 |

**Returns**:

| 
Type

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<[CardMetadata](#section16396135219146)\>

 | 

**Promise** object, which is used to return the activated card data.

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

Parameter error. Possible causes: Parameter verification failed.

 |
| 

1010200001

 | 

No permission to access the Wallet APIs.

 |
| 

1010200010

 | 

Network connection error.

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

1010210301

 | 

The card adding conditions are not met. The order can be refunded to end the card addition process.

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

1010210319

 | 

Failed to add the card.

 |
| 

1010210302

 | 

Failed to confirm the order. The order can be refunded to end the card addition process.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { walletTransitCard } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');
async addTransitCard() {
  // Order ID generated in your app after payment, which is implemented by you.
  let serverOrderId = 'serverOrderId';
  // **addCardOpaqueData** obtained from [canAddTransitCard](#section842743618139).
  let addCardOpaqueData = 'addCardOpaqueData';
  this.transitCardClient.addTransitCard(addCardOpaqueData, serverOrderId).then((result) => {
    console.info(\`Succeeded in adding TransitCard\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to add TransitCard, code:${err.code}, message:${err.message}\`);
  })
}

#### \[h2\]rechargeTransitCard

rechargeTransitCard(logicalCardNumber: string, specifiedDeviceId: string, serverOrderId: string): Promise<number>

Tops up a transportation card specified by **logicalCardNumber** based on the order ID **serverOrderId** and returns the new balance.

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

logicalCardNumber

 | 

string

 | 

Yes

 | 

Serial number of a transportation card.

 |
| 

specifiedDeviceId

 | 

string

 | 

Yes

 | 

ID of the device where the transportation card is added.

 |
| 

serverOrderId

 | 

string

 | 

Yes

 | 

Order ID generated for the top-up service on the service provider server.

 |

**Returns**:

| 
Type

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<number>

 | 

**Promise** object, which is used to return the new balance of the transportation card.

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

Parameter error. Possible causes: Parameter verification failed.

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

1010200010

 | 

Network connection error.

 |
| 

1010200013

 | 

Operation failed because of an internal error.

 |
| 

1010210401

 | 

The specified card does not exist.

 |
| 

1010210402

 | 

The status of the specified card is incorrect.

 |
| 

1010210419

 | 

Failed to recharge the card.

 |
| 

1010200014

 | 

The Wallet APIs can be called by the device owner only.

 |
| 

1010210403

 | 

Failed to confirm the order. The order can be refunded to end the recharging process.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { walletTransitCard } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');
async rechargeTransitCard() {
  // Numbers of activated transportation cards, returned by the [getCardMetadataInDevice](#section3931434195115) API.
  const logicalCardNumber = 'logicalCardNumber';
  // The value of **specifiedDeviceId** is returned by [getCardMetadataInDevice](#section3931434195115).
  const specifiedDeviceId = 'specifiedDeviceId';
  // Order ID generated in your app after payment, which is implemented by you.
  const serverOrderId = 'serverOrderId';
  this.transitCardClient.rechargeTransitCard(logicalCardNumber, specifiedDeviceId, serverOrderId).then((result) => {
    console.info(\`Succeeded in recharging TransitCard\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to recharge TransitCard, code:${err.code}, message:${err.message}\`);
  })
}

#### \[h2\]updateTransitCard

updateTransitCard(logicalCardNumber: string, specifiedDeviceId: string, serverOrderId: string): Promise<void>

Updates the information for the transportation card specified by **logicalCardNumber** based on the payment order ID **serverOrderId**.

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

logicalCardNumber

 | 

string

 | 

Yes

 | 

Card number.

 |
| 

specifiedDeviceId

 | 

string

 | 

Yes

 | 

ID of the device where the transportation card is added.

 |
| 

serverOrderId

 | 

string

 | 

Yes

 | 

Order ID generated for the card information update service on the service provider server.

 |

**Returns**:

| 
Type

 | 

**Description**

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

Parameter error. Possible causes: Parameter verification failed.

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

1010200010

 | 

Network connection error.

 |
| 

1010200013

 | 

Operation failed because of an internal error.

 |
| 

1010210501

 | 

The specified card does not exist.

 |
| 

1010210502

 | 

The status of the specified card is incorrect.

 |
| 

1010210503

 | 

Failed to confirm the order.

 |
| 

1010210519

 | 

Failed to update the card data.

 |
| 

1010200014

 | 

The Wallet APIs can be called by the device owner only.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { walletTransitCard } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');
async updateTransitCard() {
  // Numbers of activated transportation cards, returned by the [getCardMetadataInDevice](#section3931434195115) API.
  const logicalCardNumber = 'logicalCardNumber';
  // The value of **specifiedDeviceId** is returned by [getCardMetadataInDevice](#section3931434195115).
  const specifiedDeviceId = 'specifiedDeviceId';
  // Order ID generated in your app after payment, which is implemented by you.
  const serverOrderId = 'serverOrderId';
  this.transitCardClient.updateTransitCard(logicalCardNumber, specifiedDeviceId, serverOrderId).then(() => {
    console.info(\`Succeeded in updating TransitCard\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to update TransitCard, code:${err.code}, message:${err.message}\`);
  })
}

#### \[h2\]deleteTransitCard

deleteTransitCard(logicalCardNumber: string, specifiedDeviceId: string, serverOrderId: string): Promise<void>

Deletes a transportation card specified by **logicalCardNumber** based on the payment order ID **serverOrderId**.

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

logicalCardNumber

 | 

string

 | 

Yes

 | 

Card number.

 |
| 

specifiedDeviceId

 | 

string

 | 

Yes

 | 

ID of the device where the transportation card is added.

 |
| 

serverOrderId

 | 

string

 | 

Yes

 | 

Order ID generated for the card deletion service on the service provider server.

 |

**Returns**:

| 
Type

 | 

**Description**

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

Parameter error. Possible causes: Parameter verification failed.

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

1010200010

 | 

Network connection error.

 |
| 

1010200013

 | 

Operation failed because of an internal error.

 |
| 

1010210619

 | 

Failed to delete the card.

 |
| 

1010200014

 | 

The Wallet APIs can be called by the device owner only.

 |
| 

1010210601

 | 

Failed to confirm the order.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { walletTransitCard } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');
async deleteTransitCard() {
  // Numbers of activated transportation cards, returned by the [getCardMetadataInDevice](#section3931434195115) API.
  const logicalCardNumber = 'logicalCardNumber';
  // The value of **specifiedDeviceId** is returned by [getCardMetadataInDevice](#section3931434195115).
  const specifiedDeviceId = 'specifiedDeviceId';
  // Order ID generated in your app after payment, which is implemented by you.
  const serverOrderId = 'serverOrderId';
  this.transitCardClient.deleteTransitCard(logicalCardNumber, specifiedDeviceId, serverOrderId).then(() => {
    console.info(\`Succeeded in deleting TransitCard\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to delete TransitCard, code:${err.code}, message:${err.message}\`);
  })
}

#### CardMetadata

Describes the metadata information of a transportation card.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

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

issuerId

 | 

string

 | 

No

 | 

No

 | 

ID of a transportation card product.

 |
| 

aid

 | 

string

 | 

No

 | 

No

 | 

ID of the applet of the card in the SE chipset.

 |
| 

logicalCardNumber

 | 

string

 | 

No

 | 

Yes

 | 

Serial number of a transportation card. This parameter is available only when a transportation card adapter exists on the device.

 |
| 

cardNumber

 | 

string

 | 

No

 | 

Yes

 | 

Card number that is displayed, with a maximum of 30 characters. This parameter is returned if the specified transportation card exists on the device.

 |
| 

balance

 | 

number

 | 

No

 | 

Yes

 | 

Card balance, which is returned if the specified transportation card exists on the device.

 |

#### CardMetadataInDevice

Obtains the card metadata supported by the device.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

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

deviceType

 | 

[DeviceType](#section423812461512)

 | 

No

 | 

No

 | 

Device type.

 |
| 

displayName

 | 

string

 | 

No

 | 

No

 | 

Device name that is displayed.

 |
| 

cardMetadata

 | 

[CardMetadata](#section16396135219146)\[\]

 | 

No

 | 

No

 | 

Card metadata supported by the device.

 |

#### TransitCardInfo

Defines transportation card information.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

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

cardNumber

 | 

string

 | 

No

 | 

No

 | 

Displayed card number.

 |
| 

customCardData

 | 

string

 | 

No

 | 

Yes

 | 

Custom card data provided by the service provider. The JSON data structure is as follows:

-   **balance**: card balance, in cents.
-   **expireDate**: card expiration time.
-   **metroStatus**: metro card swiping status. This field is available only for metro cards. The options are as follows:
    -   **1**: entered the station
    -   **2**: exited the station
    -   **3**: unknown
-   **records**: transaction records, including top-up and consumption records. Each transaction record includes the following fields:
    -   **type**: record type. The options are **1** (top-up) and **2** (consumption).
    -   **amount**: transaction amount, in cents.
    -   **transDate**: transaction date.
    -   **transactionNo**: transaction sequence number.

 |

#### DeviceType

Defines the device type enumeration.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.Wallet

**Start version**: 5.0.0(12)

| 
Enumeration

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

DEVICE\_PHONE

 | 

0

 | 

Mobile phone.

 |
| 

DEVICE\_WATCH

 | 

1

 | 

Wearable.

 |
