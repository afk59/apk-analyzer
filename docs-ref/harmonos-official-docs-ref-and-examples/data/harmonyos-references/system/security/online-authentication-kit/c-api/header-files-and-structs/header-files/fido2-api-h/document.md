# fido2\_api.h

#### Overview

Defines the APIs for authentication extensions.

**Library**: libfido2\_ndk.z.so

**Reference file**: <OnlineAuthenticationKit/fido2\_api.h>

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

**Related module**: [FIDO2](../../../modules/passkeys/document.md)

#### Summary

#### \[h2\]Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [Uint8Buff](../../structs/uint8buff/document.md)

 | 

Defines a uint8\_t byte stream.

 |
| 

struct [AuthenticationExtensionsClientOutputs](../../structs/authenticationextensionsclientoutputs/document.md)

 | 

Defines authentication extensions.

 |
| 

struct [FIDO2\_AuthenticatorResponse](../../structs/fido2-authenticatorresponse/document.md)

 | 

Defines the authenticator assertion response.

 |
| 

struct [FIDO2\_PublicKeyAssertionCredential](../../structs/fido2-publickeyassertioncredential/document.md)

 | 

Defines the authentication result.

 |
| 

struct [FIDO2\_AuthenticatorTransportArray](../../structs/fido2-authenticatortransportarray/document.md)

 | 

Defines the array of authenticator transports.

 |
| 

struct [FIDO2\_AuthenticatorAttestationResponse](../../structs/fido2-authenticatorattestationresponse/document.md)

 | 

Defines the authenticator attestation response.

 |
| 

struct [FIDO2\_PublicKeyAttestationCredential](../../structs/fido2-publickeyattestationcredential/document.md)

 | 

Defines the registration result.

 |
| 

struct [FIDO2\_AuthenticatorSelectionCriteria](../../structs/fido2-authenticatorselectioncriteria/document.md)

 | 

Defines the authenticator selection criteria, which are specified by a WebAuthn relying party (an app or a website).

 |
| 

struct [FIDO2\_PublicKeyCredentialDescriptor](../../structs/fido2-publickeycredentialdescriptor/document.md)

 | 

Defines the credential parameters during registration or authentication.

 |
| 

struct [FIDO2\_PublicKeyCredentialParameters](../../structs/fido2-publickeycredentialparameters/document.md)

 | 

Defines the additional parameters of an authentication credential.

 |
| 

struct [FIDO2\_PublicKeyCredentialUserEntity](../../structs/fido2-publickeycredentialuserentity/document.md)

 | 

Defines the user attributes provided during credential creation.

 |
| 

struct [FIDO2\_PublicKeyCredentialRpEntity](../../structs/fido2-publickeycredentialrpentity/document.md)

 | 

Defines the relying party attributes provided during credential creation.

 |
| 

struct [FIDO2\_PublicKeyCredentialDescriptorArray](../../structs/fido2-publickeycredentialdescriptorarray/document.md)

 | 

Defines the array of public key credential descriptors.

 |
| 

struct [FIDO2\_PublicKeyCredentialHintArray](../../structs/fido2-publickeycredentialhintarray/document.md)

 | 

Defines the array of authentication mode hints.

 |
| 

struct [FIDO2\_PublicKeyCredentialRequestOptions](../../structs/fido2-publickeycredentialrequestoptions/document.md)

 | 

Defines the passkey authentication request parameters.

 |
| 

struct [FIDO2\_CredentialCreationOptionArray](../../structs/fido2-credentialcreationoptionarray/document.md)

 | 

Defines the array of additional parameters of an authentication credential.

 |
| 

struct [FIDO2\_AttestationFormatsArray](../../structs/fido2-attestationformatsarray/document.md)

 | 

Defines preferences regarding the attestation statement format used by the authenticator. It is an array defined by the relying party.

 |
| 

struct [FIDO2\_PublicKeyCredentialCreationOptions](../../structs/fido2-publickeycredentialcreationoptions/document.md)

 | 

Defines the options for credential creation.

 |
| 

struct [FIDO2\_CredentialCreationOptions](../../structs/fido2-credentialcreationoptions/document.md)

 | 

Defines the credential request options.

 |
| 

struct [FIDO2\_AuthenticatorMetadata](../../structs/fido2-authenticatormetadata/document.md)

 | 

Defines the authenticator metadata.

 |
| 

struct [FIDO2\_CredentialRequestOptions](../../structs/fido2-credentialrequestoptions/document.md)

 | 

Defines the authentication information dictionary object.

 |
| 

struct [FIDO2\_AuthenticatorMetadataArray](../../structs/fido2-authenticatormetadataarray/document.md)

 | 

Defines the array of supported authenticators.

 |
| 

struct [FIDO2\_Capability](../../structs/fido2-capability/document.md)

 | 

Defines passkey capabilities.

 |
| 

struct [FIDO2\_CapabilityArray](../../structs/fido2-capabilityarray/document.md)

 | 

Defines the array of capabilities.

 |
| 

struct [FIDO2\_TokenBinding](../../structs/fido2-tokenbinding/document.md)

 | 

Defines the token binding protocol, which is used by the client to communicate with the relying party.

 |

#### \[h2\]Types

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef struct [Uint8Buff](../../structs/uint8buff/document.md) [Uint8Buff](../../../modules/passkeys/document.md#ga8cab8c65834776e285ccd286c92a642b)

 | 

Defines a struct of a uint8\_t byte stream.

 |
| 

typedef enum [FIDO2\_TokenBindingStatus](../../../modules/passkeys/document.md#ga3a0c5c93081cd75c8ecd7a1efac8252e) [FIDO2\_TokenBindingStatus](../../../modules/passkeys/document.md#ga1ae0f0eb0c0c608a7fcc72f7cf406c16)

 | 

Defines an enum of token binding statuses.

 |
| 

typedef enum [FIDO2\_AttestationConveyancePreference](../../../modules/passkeys/document.md#ga1e33947b822678781f03c849ade9f45f) [FIDO2\_AttestationConveyancePreference](../../../modules/passkeys/document.md#ga49ab300e6aeca4a1c98c345431155ca4)

 | 

Defines an enum of attestation conveyance preferences, which are referenced by a WebAuthn relying party during credential generation.

 |
| 

typedef enum [FIDO2\_UserVerificationRequirement](../../../modules/passkeys/document.md#ga632b7b26c16a519650398ccfc3515f7a) [FIDO2\_UserVerificationRequirement](../../../modules/passkeys/document.md#ga0c7660a5c83a231ad0c1f7c6d874bd06)

 | 

Defines an enum of requirements for user verification (to check whether the current user is the intended user) by a relying party. User verification is required for some operations but not for others.

 |
| 

typedef enum [FIDO2\_AuthenticatorAttachment](../../../modules/passkeys/document.md#gaa6aa2fca2e7690e98f6d1d273324e471) [FIDO2\_AuthenticatorAttachment](../../../modules/passkeys/document.md#ga4dc2ec8c4f6c553dd2852726c9a79c3b)

 | 

Defines an enum of authenticator information (platform or roaming).

 |
| 

typedef enum [FIDO2\_AuthenticatorTransport](../../../modules/passkeys/document.md#ga02592e5b749c266e7297333afce03cec) [FIDO2\_AuthenticatorTransport](../../../modules/passkeys/document.md#gad4101bf2c242b7ff9263b0f8ad146856)

 | 

Defines an enum of authenticator transports.

 |
| 

typedef enum [FIDO2\_Algorithm](../../../modules/passkeys/document.md#ga27cd96fc7f972c4cd8cfe4d92737920a) [FIDO2\_Algorithm](../../../modules/passkeys/document.md#ga273bffd9251572eac19da58a910b9bb6)

 | 

Defines an enum of cryptographic algorithms.

 |
| 

typedef enum [FIDO2\_PublicKeyCredentialHint](../../../modules/passkeys/document.md#gab7b1367ea48debe767ae103f8ac9e96c) [FIDO2\_PublicKeyCredentialHint](../../../modules/passkeys/document.md#ga4a6398c601fd44bf26ff2b2953cb2532)

 | 

Defines an enum of authentication mode hints.

 |
| 

typedef enum [FIDO2\_PublicKeyCredentialType](../../../modules/passkeys/document.md#gaa46edbba8f1162737d26681080eea727) [FIDO2\_PublicKeyCredentialType](../../../modules/passkeys/document.md#ga72f2e8f694b926204f917ae7c5d54715)

 | 

Defines an enum of public key credential types.

 |
| 

typedef enum [FIDO2\_Uvm](../../../modules/passkeys/document.md#ga60fda18b064802349b186de072b43e98) [FIDO2\_Uvm](../../../modules/passkeys/document.md#ga432d421e134e783bfab234fee9c9a81a)

 | 

Defines an enum of UVMs.

 |
| 

typedef enum [FIDO2\_ClientCapability](../../../modules/passkeys/document.md#gae8cdc5641132b84e0313c7412d13bbbe) [FIDO2\_ClientCapability](../../../modules/passkeys/document.md#gae997777dcf71d750e456a9eecafbd3ea)

 | 

Defines an enum of client capabilities.

 |
| 

typedef enum [FIDO2\_CredentialMediationRequirement](../../../modules/passkeys/document.md#ga16035d1941d25a1ea71203ad72809b93) [FIDO2\_CredentialMediationRequirement](../../../modules/passkeys/document.md#gafdaefa0e120bb74bf4ebafef76437242)

 | 

Defines an enum of user mediation requirements.

 |
| 

typedef enum [FIDO2\_ErrorCode](../../../modules/passkeys/document.md#ga759dad4964a084008360c4b99e2ec693) [FIDO2\_ErrorCode](../../../modules/passkeys/document.md#ga313648b7100419fc2cd6c1a73b0ad7ec)

 | 

Defines an enum of error codes.

 |
| 

typedef struct [AuthenticationExtensionsClientOutputs](../../structs/authenticationextensionsclientoutputs/document.md) [AuthenticationExtensionsClientOutputs](../../../modules/passkeys/document.md#ga880558921a13840936325beb26efe45b)

 | 

Defines a struct of authentication extensions.

 |
| 

typedef struct [FIDO2\_AuthenticatorResponse](../../structs/fido2-authenticatorresponse/document.md) [FIDO2\_AuthenticatorResponse](../../../modules/passkeys/document.md#gaca490762d995a753f559380626aa60ee)

 | 

Defines a struct of the authenticator assertion response.

 |
| 

typedef struct [FIDO2\_PublicKeyAssertionCredential](../../structs/fido2-publickeyassertioncredential/document.md) [FIDO2\_PublicKeyAssertionCredential](../../../modules/passkeys/document.md#gaf60e65485855aee47dbad266920de8a7)

 | 

Defines a struct of the authentication result.

 |
| 

typedef struct [FIDO2\_AuthenticatorTransportArray](../../structs/fido2-authenticatortransportarray/document.md) [FIDO2\_AuthenticatorTransportArray](../../../modules/passkeys/document.md#ga5d080d620d78fd43051d4af61fef77a9)

 | 

Defines a struct of the array of authenticator transports.

 |
| 

typedef struct [FIDO2\_AuthenticatorAttestationResponse](../../structs/fido2-authenticatorattestationresponse/document.md) [FIDO2\_AuthenticatorAttestationResponse](../../../modules/passkeys/document.md#ga006189911a767560f30a97e22b9be84e)

 | 

Defines a struct of the authenticator attestation response.

 |
| 

typedef struct [FIDO2\_PublicKeyAttestationCredential](../../structs/fido2-publickeyattestationcredential/document.md) [FIDO2\_PublicKeyAttestationCredential](../../../modules/passkeys/document.md#gaeb82b4593aeff244d31cd40be08eb368)

 | 

Defines a struct of the registration result.

 |
| 

typedef struct [FIDO2\_AuthenticatorSelectionCriteria](../../structs/fido2-authenticatorselectioncriteria/document.md) [FIDO2\_AuthenticatorSelectionCriteria](../../../modules/passkeys/document.md#ga0816ff84d850cc5bc64fd60b0198765e)

 | 

Defines a struct of the authenticator selection criteria, which are specified by a WebAuthn relying party.

 |
| 

typedef struct [FIDO2\_PublicKeyCredentialDescriptor](../../structs/fido2-publickeycredentialdescriptor/document.md) [FIDO2\_PublicKeyCredentialDescriptor](../../../modules/passkeys/document.md#gaa99238931c603213556f2d4742a7af04)

 | 

Defines a struct of credential parameters during registration or authentication.

 |
| 

typedef struct [FIDO2\_PublicKeyCredentialParameters](../../structs/fido2-publickeycredentialparameters/document.md) [FIDO2\_PublicKeyCredentialParameters](../../../modules/passkeys/document.md#gac43d4448abcb19a8ef63ebfb83b1ad6a)

 | 

Defines a struct of the additional parameters of an authentication credential.

 |
| 

typedef struct [FIDO2\_PublicKeyCredentialUserEntity](../../structs/fido2-publickeycredentialuserentity/document.md) [FIDO2\_PublicKeyCredentialUserEntity](../../../modules/passkeys/document.md#gafdbfb4f0e894bfe4b9bffa2e04a6d3eb)

 | 

Defines a struct of the user attributes provided during credential creation.

 |
| 

typedef struct [FIDO2\_PublicKeyCredentialRpEntity](../../structs/fido2-publickeycredentialrpentity/document.md) [FIDO2\_PublicKeyCredentialRpEntity](../../../modules/passkeys/document.md#ga810af4d05788d90543b3b10a5ffadf9e)

 | 

Defines a struct of the relying party attributes provided during credential creation.

 |
| 

typedef struct [FIDO2\_PublicKeyCredentialDescriptorArray](../../structs/fido2-publickeycredentialdescriptorarray/document.md) [FIDO2\_PublicKeyCredentialDescriptorArray](../../../modules/passkeys/document.md#gaaa0a2bd23e9d18811cd1cf0ea04bc9a6)

 | 

Defines a struct of the array of public key credential descriptors.

 |
| 

typedef struct [FIDO2\_PublicKeyCredentialHintArray](../../structs/fido2-publickeycredentialhintarray/document.md) [FIDO2\_PublicKeyCredentialHintArray](../../../modules/passkeys/document.md#ga49183130db95a71da3c945452e702676)

 | 

Defines a struct of the array of authentication mode hints.

 |
| 

typedef struct [FIDO2\_PublicKeyCredentialRequestOptions](../../structs/fido2-publickeycredentialrequestoptions/document.md) [FIDO2\_PublicKeyCredentialRequestOptions](../../../modules/passkeys/document.md#ga509d2dcd89ac955c0f03bb5e4238abb5)

 | 

Defines a struct of the passkey authentication request parameters.

 |
| 

typedef struct [FIDO2\_CredentialCreationOptionArray](../../structs/fido2-credentialcreationoptionarray/document.md) [FIDO2\_CredentialCreationOptionArray](../../../modules/passkeys/document.md#ga2c517a89040b570e15517f7719ed4cad)

 | 

Defines a struct of the additional parameter array of an authentication credential.

 |
| 

typedef struct [FIDO2\_AttestationFormatsArray](../../structs/fido2-attestationformatsarray/document.md) [FIDO2\_AttestationFormatsArray](../../../modules/passkeys/document.md#gae6d363b5e0bb786bbb1b28d4863c84c2)

 | 

Defines a struct of preferences regarding the attestation statement format used by the authenticator. It is an array defined by the relying party.

 |
| 

typedef struct [FIDO2\_PublicKeyCredentialCreationOptions](../../structs/fido2-publickeycredentialcreationoptions/document.md) [FIDO2\_PublicKeyCredentialCreationOptions](../../../modules/passkeys/document.md#ga41d2d104407689b7cfc1ed38c1ed2726)

 | 

Defines a struct of the options for credential creation.

 |
| 

typedef struct [FIDO2\_CredentialCreationOptions](../../structs/fido2-credentialcreationoptions/document.md) [FIDO2\_CredentialCreationOptions](../../../modules/passkeys/document.md#ga6cd8020c0afbf089d298aaf751345bff)

 | 

Defines a struct of the credential request options.

 |
| 

typedef struct [FIDO2\_AuthenticatorMetadata](../../structs/fido2-authenticatormetadata/document.md) [FIDO2\_AuthenticatorMetadata](../../../modules/passkeys/document.md#gafdb5807d009529053a96c737b2ee7c55)

 | 

Defines a struct of the authenticator metadata.

 |
| 

typedef struct [FIDO2\_CredentialRequestOptions](../../structs/fido2-credentialrequestoptions/document.md) [FIDO2\_CredentialRequestOptions](../../../modules/passkeys/document.md#ga4db55935548b74ad18c5fb6f15f80a7b)

 | 

Defines a struct of the authentication information dictionary object.

 |
| 

typedef struct [FIDO2\_AuthenticatorMetadataArray](../../structs/fido2-authenticatormetadataarray/document.md) [FIDO2\_AuthenticatorMetadataArray](../../../modules/passkeys/document.md#ga1e40d19100575390959d7d7dfe13a52a)

 | 

Defines a struct of the array of supported authenticators.

 |
| 

typedef struct [FIDO2\_Capability](../../structs/fido2-capability/document.md) [FIDO2\_Capability](../../../modules/passkeys/document.md#ga483e50693a9bf926f524ba9ed1178f0b)

 | 

Defines a struct of passkey capabilities.

 |
| 

typedef struct [FIDO2\_CapabilityArray](../../structs/fido2-capabilityarray/document.md) [FIDO2\_CapabilityArray](../../../modules/passkeys/document.md#ga674019e8f264253ca8f3390ce93ad46f)

 | 

Defines a struct of the array of capabilities.

 |
| 

typedef struct [FIDO2\_TokenBinding](../../structs/fido2-tokenbinding/document.md) [FIDO2\_TokenBinding](../../../modules/passkeys/document.md#ga80db96062ec07eff0f2807e516b5a5f1)

 | 

Defines a struct of the token binding protocol, which is used by the client to communicate with the relying party.

 |

#### \[h2\]Enums

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[FIDO2\_TokenBindingStatus](../../../modules/passkeys/document.md#ga3a0c5c93081cd75c8ecd7a1efac8252e) { FIDO2\_PRESENT = 0, FIDO2\_SUPPORTED = 1 }

 | 

Enumerates the token binding statuses.

 |
| 

[FIDO2\_AttestationConveyancePreference](../../../modules/passkeys/document.md#ga1e33947b822678781f03c849ade9f45f) { FIDO2\_NONE = 0, FIDO2\_INDIRECT = 1, FIDO2\_DIRECT = 2, FIDO2\_ENTERPRISE = 3 }

 | 

Enumerates the attestation conveyance preferences, which are referenced by a WebAuthn relying party during credential generation.

 |
| 

[FIDO2\_UserVerificationRequirement](../../../modules/passkeys/document.md#ga632b7b26c16a519650398ccfc3515f7a) { FIDO2\_REQUIRED = 0, FIDO2\_PREFERRED = 1, FIDO2\_DISCOURAGED = 2 }

 | 

Enumerates the requirements for user verification (to check whether the current user is the intended user) by a relying party. User verification is required for some operations but not for others.

 |
| 

[FIDO2\_AuthenticatorAttachment](../../../modules/passkeys/document.md#gaa6aa2fca2e7690e98f6d1d273324e471) { FIDO2\_PLATFORM = 0, FIDO2\_CROSS\_PLATFORM = 1 }

 | 

Enumerates the authenticator information (platform or roaming).

 |
| 

[FIDO2\_AuthenticatorTransport](../../../modules/passkeys/document.md#ga02592e5b749c266e7297333afce03cec) {

FIDO2\_USB = 0, FIDO2\_NFC = 1, FIDO2\_BLE = 2, FIDO2\_SMART\_CARD = 3,

FIDO2\_HYBRID = 4, FIDO2\_INTERNAL = 5

}

 | 

Enumerates the authenticator transports.

 |
| 

[FIDO2\_Algorithm](../../../modules/passkeys/document.md#ga27cd96fc7f972c4cd8cfe4d92737920a) {

FIDO2\_ES256 = -7, FIDO2\_ES384 = -35, FIDO2\_ES512 = -36, FIDO2\_RS256 = -257,

FIDO2\_RS384 = -258, FIDO2\_RS512 = -259, FIDO2\_PS256 = -37, FIDO2\_PS384 = -38,

FIDO2\_PS512 = -39

}

 | 

Enumerates the algorithms.

 |
| 

[FIDO2\_PublicKeyCredentialHint](../../../modules/passkeys/document.md#gab7b1367ea48debe767ae103f8ac9e96c) { FIDO2\_SECURITY\_KEY = 0, FIDO2\_CLIENT\_DEVICE = 1, FIDO2\_HINT\_HYBRID = 2 }

 | 

Enumerates the authentication mode hints.

 |
| 

[FIDO2\_PublicKeyCredentialType](../../../modules/passkeys/document.md#gaa46edbba8f1162737d26681080eea727) { FIDO2\_PUBLIC\_KEY = 0 }

 | 

Enumerates the public key credential types.

 |
| 

[FIDO2\_Uvm](../../../modules/passkeys/document.md#ga60fda18b064802349b186de072b43e98) { FIDO2\_UVM\_FINGERPRINT = 2, FIDO2\_UVM\_PIN = 4, FIDO2\_UVM\_FACEPRINT = 16 }

 | 

Enumerates the UVMs.

 |
| 

[FIDO2\_ClientCapability](../../../modules/passkeys/document.md#gae8cdc5641132b84e0313c7412d13bbbe) {

FIDO2\_CONDITIONAL\_CREATE = 0, FIDO2\_CONDITIONAL\_GET = 1, FIDO2\_HYBRID\_TRANSPORT = 2, FIDO2\_PASSKEY\_PLATFORM\_AUTHENTICATOR = 3,

FIDO2\_USER\_VERIFYING\_PLATFORM\_AUTHENTICATOR = 4, FIDO2\_RELATED\_ORIGINS = 5, FIDO2\_SIGNAL\_ALL\_ACCEPTED\_CREDENTIALS = 6, FIDO2\_SIGNAL\_CURRENT\_USER\_DETAILS = 7,

FIDO2\_SIGNAL\_UNKNOWN\_CREDENTIAL = 8, FIDO2\_EXTENSION\_UVI = 9

}

 | 

Enumerates the client capabilities.

 |
| 

[FIDO2\_CredentialMediationRequirement](../../../modules/passkeys/document.md#ga16035d1941d25a1ea71203ad72809b93) { FIDO2\_SILENT = 0, FIDO2\_OPTIONAL = 1, FIDO2\_CONDITIONAL = 2, FIDO2\_MEDIATION\_REQUIRED = 3 }

 | 

Enumerates the user mediation requirements.

 |
| 

[FIDO2\_ErrorCode](../../../modules/passkeys/document.md#ga759dad4964a084008360c4b99e2ec693) {

FIDO2\_SUCCESS = 0, FIDO2\_PERMISSION\_DENIED = 201, FIDO2\_DEVICE\_NOT\_SUPPORT = 801, FIDO2\_NOT\_SUPPORT = 1021300001, FIDO2\_INVALID\_STATE = 1021300002,

FIDO2\_INTEGRITY\_CHECK\_FAILED = 1021300003, FIDO2\_USER\_ABORT = 1021300004, FIDO2\_TIMEOUT = 1021300005, FIDO2\_ENCODING\_ERROR = 1021300006,

FIDO2\_UNKNOWN\_ERROR = 1021300007, FIDO2\_CONSTRAINT\_ERROR = 1021300008, FIDO2\_DATA\_ERROR = 1021300009, FIDO2\_USER\_REJECTS = 1021300010,

FIDO2\_CONNECT\_SERVICE\_FAILED = 1021300011, FIDO2\_MAX\_CRED\_NUM\_REACHED = 1021300012, FIDO2\_INVALID\_CTAP\_COMMAND = 1021310001, FIDO2\_INVALID\_PARAMETERS = 1021310002, FIDO2\_INVALID\_MESSAGE\_OR\_ATTRIBUTE\_LENGTH = 1021310003,

FIDO2\_INVALID\_CBOR\_OR\_UNPREDICTABLE = 1021310004, FIDO2\_PARSE\_CBOR\_FAILED = 1021310005, FIDO2\_INVALID\_CREDENTIALS = 1021310006, FIDO2\_NOT\_ALLOWED = 1021310007,

FIDO2\_USER\_VERIFICATION\_FAILED = 1021310008, FIDO2\_OTHER\_ERROR = 1021310009

}

 | 

Enumerates the error codes.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

void [HMS\_FIDO2\_initCreationOptions](../../../modules/passkeys/document.md#ga1d655e31c512e2cb8dfc3c1e616d03aa) ([FIDO2\_CredentialCreationOptions](../../structs/fido2-credentialcreationoptions/document.md) \*options)

 | 

Initializes the **FIDO2\_CredentialCreationOptions** struct.

 |
| 

void [HMS\_FIDO2\_initTokenBinding](../../../modules/passkeys/document.md#ga46853c19611bf506dca76820b2446c19) ([FIDO2\_TokenBinding](../../structs/fido2-tokenbinding/document.md) \*tokenBinding)

 | 

Initializes the **FIDO2\_TokenBinding** struct.

 |
| 

void [HMS\_FIDO2\_initRequestOptions](../../../modules/passkeys/document.md#ga5ae4e44e8d06e0c247308d7329970c3a) ([FIDO2\_CredentialRequestOptions](../../structs/fido2-credentialrequestoptions/document.md) \*options)

 | 

Initializes the **FIDO2\_CredentialRequestOptions** struct.

 |
| 

[FIDO2\_ErrorCode](../../../modules/passkeys/document.md#ga759dad4964a084008360c4b99e2ec693) [HMS\_FIDO2\_getClientCapability](../../../modules/passkeys/document.md#ga3745265749b2776403960fbeece3de77) ([FIDO2\_CapabilityArray](../../structs/fido2-capabilityarray/document.md) \*\*capability)

 | 

Queries the client capabilities supported by the current device or version. When the value for a given capability is **true**, it indicates that the capability is supported.

 |
| 

[FIDO2\_ErrorCode](../../../modules/passkeys/document.md#ga759dad4964a084008360c4b99e2ec693) [HMS\_FIDO2\_getPlatformAuthenticator](../../../modules/passkeys/document.md#ga18b569cb28a659f4282acbb64e198195) ([FIDO2\_AuthenticatorMetadataArray](../../structs/fido2-authenticatormetadataarray/document.md) \*\*authenticators)

 | 

Obtains the list of supported platform authenticators.

 |
| 

[FIDO2\_ErrorCode](../../../modules/passkeys/document.md#ga759dad4964a084008360c4b99e2ec693) [HMS\_FIDO2\_register](../../../modules/passkeys/document.md#gaaaed812197e7dc4d5f9a3354d5349665) (const [FIDO2\_CredentialCreationOptions](../../structs/fido2-credentialcreationoptions/document.md) options, const [FIDO2\_TokenBinding](../../structs/fido2-tokenbinding/document.md) tokenBinding, const char \*origin, [FIDO2\_PublicKeyAttestationCredential](../../structs/fido2-publickeyattestationcredential/document.md) \*\*publicKeyAttestationCredential)

 | 

Registers a passkey.

 |
| 

[FIDO2\_ErrorCode](../../../modules/passkeys/document.md#ga759dad4964a084008360c4b99e2ec693) [HMS\_FIDO2\_authenticate](../../../modules/passkeys/document.md#gaac4365229064efc78dc25dceb7c932a3) (const [FIDO2\_CredentialRequestOptions](../../structs/fido2-credentialrequestoptions/document.md) options, const [FIDO2\_TokenBinding](../../structs/fido2-tokenbinding/document.md) tokenBinding, const char \*origin, [FIDO2\_PublicKeyAssertionCredential](../../structs/fido2-publickeyassertioncredential/document.md) \*\*publicKeyAssertionCredential)

 | 

Performs FIDO2 authentication.

 |
| 

void [HMS\_FIDO2\_CapabilityArray\_Destroy](../../../modules/passkeys/document.md#ga4287e078ad1dbe55804ea73133173949) ([FIDO2\_CapabilityArray](../../structs/fido2-capabilityarray/document.md) \*capability)

 | 

Destroys the array of capabilities.

 |
| 

void [HMS\_FIDO2\_AuthenticatorMetadataArray\_Destroy](../../../modules/passkeys/document.md#gaa5f5050def714db82bfed358922c897c) ([FIDO2\_AuthenticatorMetadataArray](../../structs/fido2-authenticatormetadataarray/document.md) \*authenticators)

 | 

Destroys the array of authenticator metadata.

 |
| 

void [HMS\_FIDO2\_PublicKeyAttestationCredential\_Destroy](../../../modules/passkeys/document.md#ga10cff1c35e596a604fbd4289abc5696b) ([FIDO2\_PublicKeyAttestationCredential](../../structs/fido2-publickeyattestationcredential/document.md) \*publicKeyAttestationCredential)

 | 

Destroys the **PublicKeyAttestationCredential** struct.

 |
| 

void [HMS\_FIDO2\_PublicKeyAssertionCredential\_Destroy](../../../modules/passkeys/document.md#gaba286b4df1149f3632d5a44c15a5ee1e) ([FIDO2\_PublicKeyAssertionCredential](../../structs/fido2-publickeyassertioncredential/document.md) \*publicKeyAssertionCredential)

 | 

Destroys the **PublicKeyAssertionCredential** struct.

 |
