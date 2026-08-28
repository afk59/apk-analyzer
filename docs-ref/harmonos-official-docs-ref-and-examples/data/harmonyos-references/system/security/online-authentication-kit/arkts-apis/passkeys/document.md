# Passkeys

This module provides the following capabilities:

-   Passkey registration: A passkey for an app or website can be created on a local device, using a user's authentication factors (such as their face, fingerprint, or PIN) as the platform authenticator.
-   Local passwordless authentication: A passkey can be used for passwordless authentication during app or website sign-in on the local device, using a user's authentication factors (such as their face, fingerprint, or PIN) as the platform authenticator.
-   Cross-device authentication through QR code scanning: A mobile device with a registered passkey can function as a roaming authenticator for passwordless sign-in to apps or websites on another device through cross-device QR code scanning.

**Start version**: 6.0.0(20)

#### Module Import

import { fido2 } from '@kit.OnlineAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit'

#### AuthenticatorAttestationResponse

Authenticator attestation response in Uint8Array format.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

attestationObject

 | 

Uint8Array

 | 

Yes

 | 

No

 | 

Attestation object.

 |
| 

clientDataJson

 | 

Uint8Array

 | 

Yes

 | 

No

 | 

Client data, which represents the contextual bindings of the WebAuthn relying party and the client. The data includes the type, challenge, and origin.

 |
| 

publicKeyAlgorithm

 | 

[Algorithm](#section19820253379)

 | 

No

 | 

No

 | 

Cryptographic algorithm.

 |
| 

publicKey

 | 

Uint8Array

 | 

No

 | 

Yes

 | 

Options of the public key credential request. By default, this parameter is left empty.

 |
| 

authenticatorData

 | 

Uint8Array

 | 

No

 | 

No

 | 

Authenticator data.

 |
| 

transports

 | 

string\[\]

 | 

No

 | 

No

 | 

Authenticator transports. The values are enumerated values of [AuthenticatorTransport](#section117661146498).

 |

#### AuthenticatorAttestationResponseJson

Authenticator attestation response, which is a JSON string.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

clientDataJson

 | 

string

 | 

No

 | 

No

 | 

Client data, which represents the contextual bindings of the WebAuthn relying party and the client. The data includes the type, challenge, and origin. The length ranges from 0 to 4096 characters.

 |
| 

authenticatorData

 | 

string

 | 

No

 | 

No

 | 

Authenticator data. The length ranges from 0 to 4096 characters.

 |
| 

transports

 | 

Array<string>

 | 

No

 | 

No

 | 

Authenticator transports. The values are enumerated values of [AuthenticatorTransport](#section117661146498).

 |
| 

publicKey

 | 

string

 | 

No

 | 

Yes

 | 

Options of the public key credential request. By default, this parameter is left empty. The length ranges from 0 to 4096 characters.

 |
| 

publicKeyAlgorithm

 | 

[Algorithm](#section19820253379)

 | 

No

 | 

No

 | 

Cryptographic algorithm.

 |
| 

attestationObject

 | 

string

 | 

No

 | 

No

 | 

Attestation object. The length ranges from 0 to 10,000 characters.

 |

#### AuthenticationExtensionsClientOutputsJson

Results of processing client extensions requested by a relying party when the relying party calls **create()** or **get()**.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

#### AuthenticatorAssertionResponseJson

Authenticator assertion response, which is a JSON string.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

clientDataJson

 | 

string

 | 

No

 | 

No

 | 

Client data. The length ranges from 0 to 4096 characters.

 |
| 

authenticatorData

 | 

string

 | 

No

 | 

No

 | 

Authenticator data. The length ranges from 0 to 4096 characters.

 |
| 

signature

 | 

string

 | 

No

 | 

No

 | 

Signature. The length ranges from 0 to 4096 characters.

 |
| 

userHandle

 | 

string

 | 

No

 | 

Yes

 | 

User handle. By default, this parameter is left empty. The length ranges from 0 to 4096 characters.

 |

#### AuthenticatorAssertionResponse

Authenticator assertion response.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

authenticatorData

 | 

Uint8Array

 | 

Yes

 | 

No

 | 

Authenticator data.

 |
| 

signature

 | 

Uint8Array

 | 

Yes

 | 

No

 | 

Signature.

 |
| 

userHandle

 | 

Uint8Array

 | 

Yes

 | 

Yes

 | 

User handle. By default, this parameter is left empty.

 |
| 

clientDataJson

 | 

Uint8Array

 | 

Yes

 | 

No

 | 

Client data.

 |

#### AuthenticationExtensionsClientOutputs

Authentication extensions.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

#### PublicKeyAttestationCredential

Registration response parameters.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

rawId

 | 

Uint8Array

 | 

Yes

 | 

No

 | 

Unique index of a credential.

 |
| 

response

 | 

[AuthenticatorAttestationResponse](#section116196263442)

 | 

Yes

 | 

No

 | 

Returned message.

 |
| 

authenticatorAttachment

 | 

[AuthenticatorAttachment](#section354238124118)

 | 

Yes

 | 

Yes

 | 

Authenticator information (platform or roaming). The default value is **platform**.

 |
| 

id

 | 

string

 | 

Yes

 | 

No

 | 

Credential ID (in Base64 format). The length ranges from 0 to 512 characters.

 |
| 

type

 | 

string

 | 

Yes

 | 

No

 | 

Credential type. The length ranges from 0 to 512 characters.

 |
| 

clientExtensionResults

 | 

[AuthenticationExtensionsClientOutputs](#section182993334919)

 | 

Yes

 | 

No

 | 

Client extension result.

 |
| 

registrationResponseJson

 | 

[RegistrationResponseJson](#section8630134312122)

 | 

No

 | 

No

 | 

Authentication result in JSON format.

 |

#### RegistrationResponseJson

Registration response parameters in JSON format.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

id

 | 

string

 | 

No

 | 

No

 | 

Credential identifier. The requirements for the identifier are distinct for each type of credential. The length ranges from 0 to 512 characters.

 |
| 

rawId

 | 

string

 | 

No

 | 

No

 | 

Raw credential identifier. The length ranges from 0 to 512 characters.

 |
| 

response

 | 

[AuthenticatorAttestationResponseJson](#section1679071213552)

 | 

No

 | 

No

 | 

Authenticator attestation response.

 |
| 

authenticatorAttachment

 | 

string

 | 

No

 | 

Yes

 | 

Authenticator information (platform or roaming). The default value is **platform**. The length ranges from 0 to 512 characters.

 |
| 

clientExtensionResults

 | 

[AuthenticationExtensionsClientOutputsJson](#section66671169415)

 | 

No

 | 

No

 | 

Client extension result. The current version does not support extensions, so the placeholder is always **NULL** and the value corresponding to the **clientExtensionResults** key must be parsed into **{}**.

 |
| 

type

 | 

string

 | 

No

 | 

No

 | 

Value of a credential object's interface object's \[\[type\]\] slot. It specifies the credential type represented by this object. The length ranges from 0 to 512 characters.

 |

#### PublicKeyCredentialRequestOptions

Passkey authentication request parameters.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

challenge

 | 

Uint8Array

 | 

No

 | 

No

 | 

Challenge.

 |
| 

timeout

 | 

number

 | 

No

 | 

Yes

 | 

Maximum duration of the authentication operation, in ms. The default value is **300000**.

 |
| 

rpId

 | 

string

 | 

No

 | 

Yes

 | 

Relying party identifier. By default, this parameter is left empty. The length ranges from 0 to 512 characters.

 |
| 

allowCredentials

 | 

Array<[PublicKeyCredentialDescriptor](#section453614462519)\>

 | 

No

 | 

Yes

 | 

Additional parameter list of an authentication credential. By default, this parameter is left empty.

 |
| 

userVerification

 | 

[UserVerificationRequirement](#section41573116347)

 | 

No

 | 

Yes

 | 

User verification requirement. The default value is **preferred**.

 |
| 

hints

 | 

Array<[PublicKeyCredentialHint](#section3221184619427)\>

 | 

No

 | 

Yes

 | 

Hints about the authentication mode. The default value is **\[\]**.

 |
| 

extensions

 | 

Map<string, Object>

 | 

No

 | 

Yes

 | 

The extensions must be a JSON string representing a Map<string, Object> object. By default, this parameter is left empty.

 |

#### PublicKeyAssertionCredential

Authentication response parameters.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

rawId

 | 

Uint8Array

 | 

Yes

 | 

No

 | 

Unique index of a credential.

 |
| 

response

 | 

[AuthenticatorAssertionResponse](#section2146056964)

 | 

Yes

 | 

No

 | 

Returned message.

 |
| 

authenticatorAttachment

 | 

[AuthenticatorAttachment](#section354238124118)

 | 

Yes

 | 

Yes

 | 

Authenticator information (platform or roaming). The default value is **platform**.

 |
| 

id

 | 

string

 | 

Yes

 | 

No

 | 

Credential ID (in Base64 format). The length ranges from 0 to 512 characters.

 |
| 

type

 | 

string

 | 

Yes

 | 

No

 | 

Credential type. The length ranges from 0 to 512 characters.

 |
| 

clientExtensionResults

 | 

[AuthenticationExtensionsClientOutputs](#section182993334919)

 | 

No

 | 

No

 | 

Client extension result.

 |
| 

authenticationResponseJson

 | 

[AuthenticationResponseJson](#section94791352208)

 | 

No

 | 

No

 | 

Authentication response data, which is a JSON string.

 |

#### AuthenticationResponseJson

Authentication response parameters in JSON format.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

id

 | 

string

 | 

No

 | 

No

 | 

Credential identifier, which is a JSON string. The requirements for the identifier are distinct for each type of credential. The length ranges from 0 to 512 characters.

 |
| 

rawId

 | 

string

 | 

No

 | 

No

 | 

Raw credential identifier, which is a JSON string. The length ranges from 0 to 512 characters.

 |
| 

response

 | 

[AuthenticatorAssertionResponseJson](#section1333349185918)

 | 

No

 | 

No

 | 

Authenticator assertion response, which is a JSON string.

 |
| 

authenticatorAttachment

 | 

string

 | 

No

 | 

Yes

 | 

Authenticator information (platform or roaming). The default value is **platform**. The length ranges from 0 to 512 characters.

 |
| 

clientExtensionResults

 | 

[AuthenticationExtensionsClientOutputsJson](#section66671169415)

 | 

No

 | 

No

 | 

Client extension result. The current version does not support extensions, so the placeholder is always **NULL** and the value corresponding to the **clientExtensionResults** key must be parsed into **{}**.

 |
| 

type

 | 

string

 | 

No

 | 

No

 | 

Value of a credential object's interface object's \[\[type\]\] slot, which is a JSON string. It specifies the credential type represented by this object. The length ranges from 0 to 512 characters.

 |

#### CredentialMediationRequirement

Enum of user mediation requirements.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

| 
Name

 | 

**Value**

 | 

Description

 |
| :-- | :-- | :-- |
| 

SILENT

 | 

'silent'

 | 

User mediation is suppressed for a given operation. If the operation can be performed without user involvement, wonderful. If user involvement is necessary, then the operation will return null rather than involving the user.

 |
| 

OPTIONAL

 | 

'optional'

 | 

User mediation is optional. If credentials can be handed over for a given operation without user mediation, they will be. If user mediation is required, then the user agent will involve the user in the decision.

 |
| 

CONDITIONAL

 | 

'conditional'

 | 

User mediation is required conditionally. In the authentication scenario, if the device has credentials, user mediation is required for selecting credentials. In the registration scenario, if the user has already agreed to create credentials, the credentials can be created without user mediation.

 |
| 

REQUIRED

 | 

'required'

 | 

The user agent will not hand over credentials without user mediation.

 |

#### CredentialCreationOptions

Dictionary object of registration information, which contains the raw registration message.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

mediation

 | 

[CredentialMediationRequirement](#section191181130202510)

 | 

No

 | 

Yes

 | 

Indicates whether a given operation requires user mediation. The default value is **optional**.

 |
| 

publicKey

 | 

[PublicKeyCredentialCreationOptions](#section155669563012)

 | 

No

 | 

No

 | 

FIDO2 registration message, which contains the challenge, relying party, user information, and authenticator selection result.

 |

#### CredentialRequestOptions

Dictionary object of authentication information, which contains the raw authentication message and the option of whether user mediation is required.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

mediation

 | 

[CredentialMediationRequirement](#section191181130202510)

 | 

No

 | 

Yes

 | 

Indicates whether a given operation requires user mediation. The default value is **optional**.

 |
| 

publicKey

 | 

[PublicKeyCredentialRequestOptions](#section12880914141610)

 | 

No

 | 

No

 | 

FIDO2 authentication message, which contains the challenge, relying party information, user information, and authenticator selection result.

 |

#### TokenBindingStatus

Enum of token binding statuses.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

| 
Name

 | 

**Value**

 | 

Description

 |
| :-- | :-- | :-- |
| 

PRESENT

 | 

'present'

 | 

Normal communication.

 |
| 

SUPPORTED

 | 

'supported'

 | 

Token binding is supported, but communication is not yet available.

 |

#### TokenBinding

Token binding protocol, which is used by the client to communicate with the relying party.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

status

 | 

[TokenBindingStatus](#section15870155832812)

 | 

No

 | 

No

 | 

Token binding status of the client.

 |
| 

id

 | 

string

 | 

No

 | 

No

 | 

Identifier. The length ranges from 0 to 512 characters.

 |

#### AttestationConveyancePreference

Enum of attestation conveyance preferences, which are referenced by a WebAuthn relying party during credential generation.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

| 
Name

 | 

**Value**

 | 

Description

 |
| :-- | :-- | :-- |
| 

NONE

 | 

'none'

 | 

The relying party is not interested in authenticator attestation. This is the default value.

 |
| 

INDIRECT

 | 

'indirect'

 | 

The indirect relying party wants to receive a verifiable attestation statement, but allows the client to decide how to obtain such an attestation statement.

 |
| 

DIRECT

 | 

'direct'

 | 

The direct relying party wants to receive the attestation statement as generated by the authenticator.

 |
| 

ENTERPRISE

 | 

'enterprise'

 | 

The relying party wants to receive an enterprise attestation statement which may include information that uniquely identifies the authenticator.

 |

#### UserVerificationRequirement

Enum of user verification requirements. A relying party may require user verification (to check whether the current user is the intended user) for some operations but not for others.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

| 
Name

 | 

**Value**

 | 

Description

 |
| :-- | :-- | :-- |
| 

REQUIRED

 | 

'required'

 | 

User verification is required.

 |
| 

PREFERRED

 | 

'preferred'

 | 

The relying party prefers user verification for the operation if possible, but will not fail the operation if the response does not have the user verification flag set.

 |
| 

DISCOURAGED

 | 

'discouraged'

 | 

The relying party does not want user verification employed during the operation.

 |

#### ResidentKeyRequirement

Enum of whether discoverable credentials are required.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

| 
Name

 | 

**Value**

 | 

Description

 |
| :-- | :-- | :-- |
| 

DISCOURAGED

 | 

'discouraged'

 | 

The relying party prefers creating a server-side credential, but will accept a client-side discoverable credential. The client and authenticator must create server-side credentials whenever possible.

 |
| 

PREFERRED

 | 

'preferred'

 | 

The relying party strongly prefers creating a client-side discoverable credential, but will accept a server-side credential.

 |
| 

REQUIRED

 | 

'required'

 | 

The relying party requires a client-side discoverable credential. If a client-side discoverable credential cannot be created, the client must return an error.

 |

#### AuthenticatorAttachment

Authenticator information (platform or roaming). The default value is **platform**.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

| 
Name

 | 

**Value**

 | 

Description

 |
| :-- | :-- | :-- |
| 

PLATFORM

 | 

'platform'

 | 

Platform authenticator, such as a PIN, fingerprint, or face.

 |
| 

CROSS\_PLATFORM

 | 

'cross-platform'

 | 

Cross-platform authenticator, also called roaming authenticator, which includes Bluetooth, NFC, and USB.

 |

#### AuthenticatorSelectionCriteria

Authenticator selection criteria, which are specified by a WebAuthn relying party.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

authenticatorAttachment

 | 

[AuthenticatorAttachment](#section354238124118)

 | 

No

 | 

Yes

 | 

Authenticator information. The default value is **platform**.

 |
| 

residentKey

 | 

string

 | 

No

 | 

Yes

 | 

Resident key. By default, this parameter is left empty. The length ranges from 0 to 4096 characters.

 |
| 

requireResidentKey

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether a resident key is required. The value **true** indicates yes, and the value **false** indicates no. The default value is **false**.

 |
| 

userVerification

 | 

[UserVerificationRequirement](#section41573116347)

 | 

No

 | 

Yes

 | 

User verification requirement. The default value is **preferred**.

 |

#### AuthenticatorTransport

Enum of authenticator transports.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

USB

 | 

'usb'

 | 

USB.

 |
| 

NFC

 | 

'nfc'

 | 

Near Field Communication (NFC).

 |
| 

BLE

 | 

'ble'

 | 

Bluetooth Low Energy (BLE).

 |
| 

SMART\_CARD

 | 

'smart-card'

 | 

Smart card.

 |
| 

HYBRID

 | 

'hybrid'

 | 

Hybrid, indicating multiple data transport modes.

 |
| 

INTERNAL

 | 

'internal'

 | 

Internal (built-in device transport).

 |

#### PublicKeyCredentialDescriptor

Credential parameters during registration or authentication.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

type

 | 

[PublicKeyCredentialType](#section384116164912)

 | 

No

 | 

No

 | 

Credential type.

 |
| 

id

 | 

Uint8Array

 | 

No

 | 

No

 | 

Credential identifier.

 |
| 

transports

 | 

Array<[AuthenticatorTransport](#section117661146498)\>

 | 

No

 | 

Yes

 | 

Authenticator transports. The values are enumerated values of [AuthenticatorTransport](#section117661146498). By default, the value is an empty list.

 |

#### Algorithm

Enum of algorithms.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

\-7

 | 

ES256 algorithm.

 |
| 

ES384

 | 

\-35

 | 

ES384 algorithm.

 |
| 

ES512

 | 

\-36

 | 

ES512 algorithm.

 |
| 

RS256

 | 

\-257

 | 

RS256 algorithm.

 |
| 

RS384

 | 

\-258

 | 

RS384 algorithm.

 |
| 

RS512

 | 

\-259

 | 

RS512 algorithm

 |
| 

PS256

 | 

\-37

 | 

PS256 algorithm.

 |
| 

PS384

 | 

\-38

 | 

PS384 algorithm.

 |
| 

PS512

 | 

\-39

 | 

PS512 algorithm.

 |

#### PublicKeyCredentialHint

Enum of public key credential hints.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

SECURITY\_KEY

 | 

'security-key'

 | 

Security key.

 |
| 

CLIENT\_DEVICE

 | 

'client-device'

 | 

Client device.

 |
| 

HYBRID

 | 

'hybrid'

 | 

Hybrid.

 |

#### PublicKeyCredentialType

Enum of public key credential types.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

PUBLIC\_KEY

 | 

'public-key'

 | 

Public key.

 |

#### PublicKeyCredentialParameters

Additional parameters of an authentication credential.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

type

 | 

[PublicKeyCredentialType](#section384116164912)

 | 

No

 | 

No

 | 

Credential type.

 |
| 

alg

 | 

[Algorithm](#section19820253379)

 | 

No

 | 

No

 | 

Algorithm.

 |

#### PublicKeyCredentialUserEntity

Additional user attributes provided during credential creation.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

id

 | 

Uint8Array

 | 

No

 | 

No

 | 

Credential identifier. The length ranges from 0 to 64 characters.

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

User name displayed on the foreground. The length ranges from 0 to 512 characters.

 |
| 

name

 | 

string

 | 

No

 | 

No

 | 

User name. The length ranges from 0 to 512 characters.

 |

#### PublicKeyCredentialRpEntity

Relying party attributes provided during credential creation.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

id

 | 

string

 | 

No

 | 

Yes

 | 

Credential identifier. By default, this parameter is left empty. The length ranges from 0 to 512 characters.

 |
| 

name

 | 

string

 | 

No

 | 

No

 | 

User name. The length ranges from 0 to 512 characters.

 |

#### PublicKeyCredentialCreationOptions

Credential creation options.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

rp

 | 

[PublicKeyCredentialRpEntity](#section143231528100)

 | 

No

 | 

No

 | 

Relying party attributes provided during credential creation.

 |
| 

user

 | 

[PublicKeyCredentialUserEntity](#section151096116327)

 | 

No

 | 

No

 | 

User information.

 |
| 

challenge

 | 

Uint8Array

 | 

No

 | 

No

 | 

Challenge value. The length ranges from 16 to 512 characters.

 |
| 

pubKeyCredParams

 | 

Array<[PublicKeyCredentialParameters](#section105667308366)\>

 | 

No

 | 

No

 | 

Additional parameter list of an authentication credential.

 |
| 

timeout

 | 

number

 | 

No

 | 

Yes

 | 

Timeout interval, in ms. The default value is **300000**. The timeout interval must range from 300s to 600s.

 |
| 

excludeCredentials

 | 

Array<[PublicKeyCredentialDescriptor](#section453614462519)\>

 | 

No

 | 

Yes

 | 

List of credentials already registered with the FIDO server. By default, the value is an empty array.

 |
| 

authenticatorSelection

 | 

[AuthenticatorSelectionCriteria](#section16855415432)

 | 

No

 | 

Yes

 | 

Authenticator selection criteria. By default, this parameter is left empty.

 |
| 

hints

 | 

Array<[PublicKeyCredentialHint](#section3221184619427)\>

 | 

No

 | 

Yes

 | 

Hints. By default, the value is an empty array.

 |
| 

attestation

 | 

[AttestationConveyancePreference](#section1199618304321)

 | 

No

 | 

Yes

 | 

Credential conveyance preference. The default value is **none**.

 |
| 

attestationFormats

 | 

Array<string>

 | 

No

 | 

Yes

 | 

Preference regarding the attestation statement format used by the authenticator. It is specified by the relying party. By default, the value is an empty array.

 |
| 

extensions

 | 

Map<string, Object>

 | 

No

 | 

Yes

 | 

Extensions. By default, this parameter is left empty.

 |

#### Uvm

Enum of platform authenticators.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

| 
Name

 | 

**Value**

 | 

Description

 |
| :-- | :-- | :-- |
| 

UVM\_FINGERPRINT

 | 

2

 | 

Fingerprint.

 |
| 

UVM\_PIN

 | 

4

 | 

PIN.

 |
| 

UVM\_FACE

 | 

16

 | 

Face.

 |

#### ClientCapability

Enum of client capabilities supported by the current device or version.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

| 
Name

 | 

**Value**

 | 

Description

 |
| :-- | :-- | :-- |
| 

CONDITIONAL\_CREATE

 | 

'conditionalCreate'

 | 

Passkey registration.

 |
| 

CONDITIONAL\_GET

 | 

'conditionalGet'

 | 

Authentication using a passkey.

 |
| 

HYBRID\_TRANSPORT

 | 

'hybridTransport'

 | 

Hybrid transport, indicating multiple data transport modes.

 |
| 

PASSKEY\_PLATFORM\_AUTHENTICATOR

 | 

'passkeyPlatformAuthenticator'

 | 

Passkey platform authenticator.

 |
| 

USER\_VERIFYING\_PLATFORM\_AUTHENTICATOR

 | 

'userVerifyingPlatformAuthenticator'

 | 

User-verifying platform authenticator.

 |
| 

RELATED\_ORIGINS

 | 

'relatedOrigins'

 | 

Supporting related origin requests.

 |
| 

SIGNAL\_ALL\_ACCEPTED\_CREDENTIALS

 | 

'signalAllAcceptedCredentials'

 | 

Sending all accepted credentials.

 |
| 

SIGNAL\_CURRENT\_USER\_DETAILS

 | 

'signalCurrentUserDetails'

 | 

Sending detailed information about the current user.

 |
| 

SIGNAL\_UNKNOWN\_CREDENTIAL

 | 

'signalUnknownCredential'

 | 

Sending unknown credentials.

 |

#### AuthenticatorMetadata

Authenticator metadata.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

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

aaguid

 | 

string

 | 

Yes

 | 

No

 | 

Authenticator attestation globally unique identifier. The length ranges from 0 to 512 characters.

 |
| 

uvm

 | 

[Uvm](#section17462111214112)

 | 

Yes

 | 

No

 | 

Supported platform authenticator type, such as face, fingerprint, and PIN.

 |
| 

isAvailable

 | 

boolean

 | 

Yes

 | 

No

 | 

Indicates whether an authenticator is available. The value **true** indicates yes, and the value **false** indicates no.

 |

#### getClientCapabilities

getClientCapabilities(context: common.Context): Promise<Map<ClientCapability, boolean>>

Queries the client capabilities supported by the current device or version. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

Context of the current ability.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<Map<[ClientCapability](#section44620019103), boolean>>

 | 

Promise object, which returns the capability enumeration. The value **true** indicates that a capability is supported and the value **false** indicates not.

 |

**Error codes**:

For details about the error codes, please refer to [passkey service error codes](../arkts-api-error-codes/passkeys/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

801

 | 

Device type error.

 |
| 

1021300007

 | 

Unknown error.

 |
| 

1021300011

 | 

Failed to connect to the service.

 |

**Example**:

import { common } from '@kit.AbilityKit'

uiContext1: UIContext = this.getUIContext();
uiContext: common.UIAbilityContext = this.uiContext1.getHostContext() as common.UIAbilityContext; // To use **uiContext**, you need to obtain the context of the UIAbility of the screen. For each screen, you need to obtain the context only once.

try {
    let clientCapabilities: Map<fido2.ClientCapability, boolean> =
      await fido2.getClientCapabilities(this.uiContext); // Obtain the authentication capability list.
    console.info("Succeeded in doing getClientCapabilities.");
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(\`Failed to call discover. Code is ${err.code}, message is ${err.message}\`);
}

#### getPlatformAuthenticators

getPlatformAuthenticators(context: common.Context): Promise<Array<AuthenticatorMetadata>>

Queries the platform authenticator capabilities (face, fingerprint, and PIN) currently supported. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

Context of the current ability.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<Array<[AuthenticatorMetadata](#section107571524911)\>>

 | 

Authenticator metadata list returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [passkey service error codes](../arkts-api-error-codes/passkeys/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

801

 | 

Device type error.

 |
| 

1021300007

 | 

Unknown error.

 |
| 

1021300011

 | 

Failed to connect to the service.

 |

**Example**:

import { common } from '@kit.AbilityKit';

uiContext1: UIContext = this.getUIContext();
uiContext: common.UIAbilityContext = this.uiContext1.getHostContext() as common.UIAbilityContext; // To use **uiContext**, you need to obtain the context of the UIAbility of the screen. For each screen, you need to obtain the context only once.

try{
  let platformAuthenticators: Array<fido2.AuthenticatorMetadata> =
    await fido2.getPlatformAuthenticators(this.uiContext); // Obtain platform authenticator information.
  console.info("Succeeded in doing getPlatformAuthenticators.");
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(\`Failed to call discover. Code is ${err.code}, message is ${err.message}\`);
}

#### register

register(context: common.Context, options: CredentialCreationOptions, tokenBinding?: TokenBinding): Promise<PublicKeyAttestationCredential>

Registers a passkey. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

Context of the current ability.

 |
| 

options

 | 

[CredentialCreationOptions](#section3125554145615)

 | 

Yes

 | 

Registration message options.

 |
| 

tokenBinding

 | 

[TokenBinding](#section3745131173015)

 | 

No

 | 

Channel parameter. By default, this parameter is left empty.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[PublicKeyAttestationCredential](#section10797172295315)\>

 | 

Registration result returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [passkey service error codes](../arkts-api-error-codes/passkeys/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

801

 | 

Device type error.

 |
| 

1021300001

 | 

The system does not support.

 |
| 

1021300002

 | 

Invalid state.

 |
| 

1021300003

 | 

System integrity check failed.

 |
| 

1021300004

 | 

User abort.

 |
| 

1021300005

 | 

Time out.

 |
| 

1021300006

 | 

Encoding error.

 |
| 

1021300007

 | 

Unknown error.

 |
| 

1021300008

 | 

The constraint condition is incorrect.

 |
| 

1021300009

 | 

Data error.

 |
| 

1021300010

 | 

User Rejects.

 |
| 

1021300011

 | 

Failed to connect to the service.

 |
| 

1021300012

 | 

The number of credentials has reached the maximum limit.

 |

**Example**:

import { common } from '@kit.AbilityKit';

uiContext1: UIContext = this.getUIContext();
uiContext: common.UIAbilityContext = this.uiContext1.getHostContext() as common.UIAbilityContext; // To use **uiContext**, you need to obtain the context of the UIAbility of the screen. For each screen, you need to obtain the context only once.

try {
  let credentialCreationOp: fido2.CredentialCreationOptions = {
    publicKey: pkOptions // **pkOptions** is the registration message obtained from the FIDO server.
  } // **credentialCreationOp** is the registration information assembled by the app.
  let publicKeyAttestationCredential: fido2.PublicKeyAttestationCredential =
    await fido2.register(this.uiContext, credentialCreationOp); // Perform FIDO2 registration.
  console.info("Succeeded in doing register.");
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(\`Failed to call discover. Code is ${err.code}, message is ${err.message}\`);
}

#### authenticate

authenticate(context: common.Context, options: CredentialRequestOptions, tokenBinding?: TokenBinding): Promise<PublicKeyAssertionCredential>

Performs authentication using a passkey. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

Context of the current ability.

 |
| 

options

 | 

[CredentialRequestOptions](#section433810416530)

 | 

Yes

 | 

Authentication message options.

 |
| 

tokenBinding

 | 

[TokenBinding](#section3745131173015)

 | 

No

 | 

Channel parameter. By default, this parameter is left empty.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[PublicKeyAssertionCredential](#section16498195211554)\>

 | 

Authentication result returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [passkey service error codes](../arkts-api-error-codes/passkeys/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

801

 | 

Device type error.

 |
| 

1021300002

 | 

Invalid state.

 |
| 

1021300003

 | 

System integrity check failed.

 |
| 

1021300004

 | 

User abort.

 |
| 

1021300005

 | 

Time out.

 |
| 

1021300006

 | 

Encoding error.

 |
| 

1021300007

 | 

Unknown error.

 |
| 

1021300009

 | 

Data error.

 |
| 

1021300010

 | 

User Rejects.

 |
| 

1021300011

 | 

Failed to connect to the service.

 |
| 

1021310001

 | 

Invalid CTAP command.

 |
| 

1021310002

 | 

The command contains invalid parameters.

 |
| 

1021310003

 | 

Invalid message or attribute length.

 |
| 

1021310004

 | 

Invalid CBOR or unpredictable error.

 |
| 

1021310005

 | 

Failed to parse the CBOR.

 |
| 

1021310006

 | 

Not found valid credentials.

 |
| 

1021310007

 | 

Not allowed.

 |
| 

1021310008

 | 

User verification failed.

 |
| 

1021310009

 | 

Other error.

 |

**Example**:

import { common } from '@kit.AbilityKit';

uiContext1: UIContext = this.getUIContext();
uiContext: common.UIAbilityContext = this.uiContext1.getHostContext() as common.UIAbilityContext; // To use **uiContext**, you need to obtain the context of the UIAbility of the screen. For each screen, you need to obtain the context only once.

try {
  let authCredentialRequestOptions: fido2.CredentialRequestOptions = {
    publicKey: authPub, // **authPub** is the authentication message obtained from the FIDO server.
    mediation: "optional" as fido2.CredentialMediationRequirement // 
  } // **authCredentialRequestOptions** is the authentication information assembled by the app.
  let pkAssertionCredential: fido2.PublicKeyAssertionCredential =
    await fido2.authenticate(this.uiContext, authCredentialRequestOptions); // Perform FIDO2 authentication.
  console.info("Succeeded in doing authenticate.");
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(\`Failed to call discover. Code is ${err.code}, message is ${err.message}\`);
}
