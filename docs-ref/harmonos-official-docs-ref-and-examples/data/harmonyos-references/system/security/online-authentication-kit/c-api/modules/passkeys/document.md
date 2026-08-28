# Passkeys

#### Overview

Provides passkey capabilities.

**System capability**: SystemCapability.Security.FIDO2

**Start version**: 6.0.0(20)

#### Summary

#### \[h2\]Files

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[fido2\_api.h](../../header-files-and-structs/header-files/fido2-api-h/document.md)

 | 

Declares the APIs used to access FIDO2. APIs related to FIDO2 (passkey) capabilities are provided. The basic core capabilities of FIDO2 include obtaining supported FIDO2 capabilities, obtaining platform authenticator capabilities, registering passkeys, and using passkeys for authentication.

 |

#### \[h2\]Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [Uint8Buff](../../header-files-and-structs/structs/uint8buff/document.md)

 | 

Defines a uint8\_t byte stream.

 |
| 

struct [AuthenticationExtensionsClientOutputs](../../header-files-and-structs/structs/authenticationextensionsclientoutputs/document.md)

 | 

Defines authentication extensions.

 |
| 

struct [FIDO2\_AuthenticatorResponse](../../header-files-and-structs/structs/fido2-authenticatorresponse/document.md)

 | 

Defines the authenticator assertion response.

 |
| 

struct [FIDO2\_PublicKeyAssertionCredential](../../header-files-and-structs/structs/fido2-publickeyassertioncredential/document.md)

 | 

Defines the authentication result.

 |
| 

struct [FIDO2\_AuthenticatorTransportArray](../../header-files-and-structs/structs/fido2-authenticatortransportarray/document.md)

 | 

Defines the array of authenticator transports.

 |
| 

struct [FIDO2\_AuthenticatorAttestationResponse](../../header-files-and-structs/structs/fido2-authenticatorattestationresponse/document.md)

 | 

Defines the authenticator attestation response.

 |
| 

struct [FIDO2\_PublicKeyAttestationCredential](../../header-files-and-structs/structs/fido2-publickeyattestationcredential/document.md)

 | 

Defines the registration result.

 |
| 

struct [FIDO2\_AuthenticatorSelectionCriteria](../../header-files-and-structs/structs/fido2-authenticatorselectioncriteria/document.md)

 | 

Defines the authenticator selection criteria, which are specified by a WebAuthn relying party (an app or a website).

 |
| 

struct [FIDO2\_PublicKeyCredentialDescriptor](../../header-files-and-structs/structs/fido2-publickeycredentialdescriptor/document.md)

 | 

Defines the credential parameters during registration or authentication.

 |
| 

struct [FIDO2\_PublicKeyCredentialParameters](../../header-files-and-structs/structs/fido2-publickeycredentialparameters/document.md)

 | 

Defines the additional parameters of an authentication credential.

 |
| 

struct [FIDO2\_PublicKeyCredentialUserEntity](../../header-files-and-structs/structs/fido2-publickeycredentialuserentity/document.md)

 | 

Defines the user attributes provided during credential creation.

 |
| 

struct [FIDO2\_PublicKeyCredentialRpEntity](../../header-files-and-structs/structs/fido2-publickeycredentialrpentity/document.md)

 | 

Defines the relying party attributes provided during credential creation.

 |
| 

struct [FIDO2\_PublicKeyCredentialDescriptorArray](../../header-files-and-structs/structs/fido2-publickeycredentialdescriptorarray/document.md)

 | 

Defines the array of public key credential descriptors.

 |
| 

struct [FIDO2\_PublicKeyCredentialHintArray](../../header-files-and-structs/structs/fido2-publickeycredentialhintarray/document.md)

 | 

Defines the array of authentication mode hints.

 |
| 

struct [FIDO2\_PublicKeyCredentialRequestOptions](../../header-files-and-structs/structs/fido2-publickeycredentialrequestoptions/document.md)

 | 

Defines the passkey authentication request parameters.

 |
| 

struct [FIDO2\_CredentialCreationOptionArray](../../header-files-and-structs/structs/fido2-credentialcreationoptionarray/document.md)

 | 

Defines the array of additional parameters of an authentication credential.

 |
| 

struct [FIDO2\_AttestationFormatsArray](../../header-files-and-structs/structs/fido2-attestationformatsarray/document.md)

 | 

Defines preferences regarding the attestation statement format used by the authenticator. It is an array defined by the relying party.

 |
| 

struct [FIDO2\_PublicKeyCredentialCreationOptions](../../header-files-and-structs/structs/fido2-publickeycredentialcreationoptions/document.md)

 | 

Defines the options for credential creation.

 |
| 

struct [FIDO2\_CredentialCreationOptions](../../header-files-and-structs/structs/fido2-credentialcreationoptions/document.md)

 | 

Defines the credential request options.

 |
| 

struct [FIDO2\_AuthenticatorMetadata](../../header-files-and-structs/structs/fido2-authenticatormetadata/document.md)

 | 

Defines the authenticator metadata.

 |
| 

struct [FIDO2\_CredentialRequestOptions](../../header-files-and-structs/structs/fido2-credentialrequestoptions/document.md)

 | 

Defines the authentication information dictionary object.

 |
| 

struct [FIDO2\_AuthenticatorMetadataArray](../../header-files-and-structs/structs/fido2-authenticatormetadataarray/document.md)

 | 

Defines the array of supported authenticators.

 |
| 

struct [FIDO2\_Capability](../../header-files-and-structs/structs/fido2-capability/document.md)

 | 

Defines passkey capabilities.

 |
| 

struct [FIDO2\_CapabilityArray](../../header-files-and-structs/structs/fido2-capabilityarray/document.md)

 | 

Defines the array of capabilities.

 |
| 

struct [FIDO2\_TokenBinding](../../header-files-and-structs/structs/fido2-tokenbinding/document.md)

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

typedef struct [Uint8Buff](../../header-files-and-structs/structs/uint8buff/document.md) [Uint8Buff](#ga8cab8c65834776e285ccd286c92a642b)

 | 

Defines a struct of a uint8\_t byte stream.

 |
| 

typedef enum [FIDO2\_TokenBindingStatus](#ga3a0c5c93081cd75c8ecd7a1efac8252e) [FIDO2\_TokenBindingStatus](#ga1ae0f0eb0c0c608a7fcc72f7cf406c16)

 | 

Defines an enum of token binding statuses.

 |
| 

typedef enum [FIDO2\_AttestationConveyancePreference](#ga1e33947b822678781f03c849ade9f45f) [FIDO2\_AttestationConveyancePreference](#ga49ab300e6aeca4a1c98c345431155ca4)

 | 

Defines an enum of attestation conveyance preferences, which are referenced by a WebAuthn relying party during credential generation.

 |
| 

typedef enum [FIDO2\_UserVerificationRequirement](#ga632b7b26c16a519650398ccfc3515f7a) [FIDO2\_UserVerificationRequirement](#ga0c7660a5c83a231ad0c1f7c6d874bd06)

 | 

Defines an enum of requirements for user verification (to check whether the current user is the intended user) by a relying party. User verification is required for some operations but not for others.

 |
| 

typedef enum [FIDO2\_AuthenticatorAttachment](#gaa6aa2fca2e7690e98f6d1d273324e471) [FIDO2\_AuthenticatorAttachment](#ga4dc2ec8c4f6c553dd2852726c9a79c3b)

 | 

Defines an enum of authenticator information (platform or roaming).

 |
| 

typedef enum [FIDO2\_AuthenticatorTransport](#ga02592e5b749c266e7297333afce03cec) [FIDO2\_AuthenticatorTransport](#gad4101bf2c242b7ff9263b0f8ad146856)

 | 

Defines an enum of authenticator transports.

 |
| 

typedef enum [FIDO2\_Algorithm](#ga27cd96fc7f972c4cd8cfe4d92737920a) [FIDO2\_Algorithm](#ga273bffd9251572eac19da58a910b9bb6)

 | 

Defines an enum of cryptographic algorithms.

 |
| 

typedef enum [FIDO2\_PublicKeyCredentialHint](#gab7b1367ea48debe767ae103f8ac9e96c) [FIDO2\_PublicKeyCredentialHint](#ga4a6398c601fd44bf26ff2b2953cb2532)

 | 

Defines an enum of authentication mode hints.

 |
| 

typedef enum [FIDO2\_PublicKeyCredentialType](#gaa46edbba8f1162737d26681080eea727) [FIDO2\_PublicKeyCredentialType](#ga72f2e8f694b926204f917ae7c5d54715)

 | 

Defines an enum of public key credential types.

 |
| 

typedef enum [FIDO2\_Uvm](#ga60fda18b064802349b186de072b43e98) [FIDO2\_Uvm](#ga432d421e134e783bfab234fee9c9a81a)

 | 

Defines an enum of UVMs.

 |
| 

typedef enum [FIDO2\_ClientCapability](#gae8cdc5641132b84e0313c7412d13bbbe) [FIDO2\_ClientCapability](#gae997777dcf71d750e456a9eecafbd3ea)

 | 

Defines an enum of client capabilities.

 |
| 

typedef enum [FIDO2\_CredentialMediationRequirement](#ga16035d1941d25a1ea71203ad72809b93) [FIDO2\_CredentialMediationRequirement](#gafdaefa0e120bb74bf4ebafef76437242)

 | 

Defines an enum of user mediation requirements.

 |
| 

typedef enum [FIDO2\_ErrorCode](#ga759dad4964a084008360c4b99e2ec693) [FIDO2\_ErrorCode](#ga313648b7100419fc2cd6c1a73b0ad7ec)

 | 

Defines an enum of error codes.

 |
| 

typedef struct [AuthenticationExtensionsClientOutputs](../../header-files-and-structs/structs/authenticationextensionsclientoutputs/document.md) [AuthenticationExtensionsClientOutputs](#ga880558921a13840936325beb26efe45b)

 | 

Defines a struct of authentication extensions.

 |
| 

typedef struct [FIDO2\_AuthenticatorResponse](../../header-files-and-structs/structs/fido2-authenticatorresponse/document.md) [FIDO2\_AuthenticatorResponse](#gaca490762d995a753f559380626aa60ee)

 | 

Defines a struct of the authenticator assertion response.

 |
| 

typedef struct [FIDO2\_PublicKeyAssertionCredential](../../header-files-and-structs/structs/fido2-publickeyassertioncredential/document.md) [FIDO2\_PublicKeyAssertionCredential](#gaf60e65485855aee47dbad266920de8a7)

 | 

Defines a struct of the authentication result.

 |
| 

typedef struct [FIDO2\_AuthenticatorTransportArray](../../header-files-and-structs/structs/fido2-authenticatortransportarray/document.md) [FIDO2\_AuthenticatorTransportArray](#ga5d080d620d78fd43051d4af61fef77a9)

 | 

Defines a struct of the array of authenticator transports.

 |
| 

typedef struct [FIDO2\_AuthenticatorAttestationResponse](../../header-files-and-structs/structs/fido2-authenticatorattestationresponse/document.md) [FIDO2\_AuthenticatorAttestationResponse](#ga006189911a767560f30a97e22b9be84e)

 | 

Defines a struct of the authenticator attestation response.

 |
| 

typedef struct [FIDO2\_PublicKeyAttestationCredential](../../header-files-and-structs/structs/fido2-publickeyattestationcredential/document.md) [FIDO2\_PublicKeyAttestationCredential](#gaeb82b4593aeff244d31cd40be08eb368)

 | 

Defines a struct of the registration result.

 |
| 

typedef struct [FIDO2\_AuthenticatorSelectionCriteria](../../header-files-and-structs/structs/fido2-authenticatorselectioncriteria/document.md) [FIDO2\_AuthenticatorSelectionCriteria](#ga0816ff84d850cc5bc64fd60b0198765e)

 | 

Defines a struct of the authenticator selection criteria, which are specified by a WebAuthn relying party.

 |
| 

typedef struct [FIDO2\_PublicKeyCredentialDescriptor](../../header-files-and-structs/structs/fido2-publickeycredentialdescriptor/document.md) [FIDO2\_PublicKeyCredentialDescriptor](#gaa99238931c603213556f2d4742a7af04)

 | 

Defines a struct of credential parameters during registration or authentication.

 |
| 

typedef struct [FIDO2\_PublicKeyCredentialParameters](../../header-files-and-structs/structs/fido2-publickeycredentialparameters/document.md) [FIDO2\_PublicKeyCredentialParameters](#gac43d4448abcb19a8ef63ebfb83b1ad6a)

 | 

Defines a struct of the additional parameters of an authentication credential.

 |
| 

typedef struct [FIDO2\_PublicKeyCredentialUserEntity](../../header-files-and-structs/structs/fido2-publickeycredentialuserentity/document.md) [FIDO2\_PublicKeyCredentialUserEntity](#gafdbfb4f0e894bfe4b9bffa2e04a6d3eb)

 | 

Defines a struct of the user attributes provided during credential creation.

 |
| 

typedef struct [FIDO2\_PublicKeyCredentialRpEntity](../../header-files-and-structs/structs/fido2-publickeycredentialrpentity/document.md) [FIDO2\_PublicKeyCredentialRpEntity](#ga810af4d05788d90543b3b10a5ffadf9e)

 | 

Defines a struct of the relying party attributes provided during credential creation.

 |
| 

typedef struct [FIDO2\_PublicKeyCredentialDescriptorArray](../../header-files-and-structs/structs/fido2-publickeycredentialdescriptorarray/document.md) [FIDO2\_PublicKeyCredentialDescriptorArray](#gaaa0a2bd23e9d18811cd1cf0ea04bc9a6)

 | 

Defines a struct of the array of public key credential descriptors.

 |
| 

typedef struct [FIDO2\_PublicKeyCredentialHintArray](../../header-files-and-structs/structs/fido2-publickeycredentialhintarray/document.md) [FIDO2\_PublicKeyCredentialHintArray](#ga49183130db95a71da3c945452e702676)

 | 

Defines a struct of the array of authentication mode hints.

 |
| 

typedef struct [FIDO2\_PublicKeyCredentialRequestOptions](../../header-files-and-structs/structs/fido2-publickeycredentialrequestoptions/document.md) [FIDO2\_PublicKeyCredentialRequestOptions](#ga509d2dcd89ac955c0f03bb5e4238abb5)

 | 

Defines a struct of the passkey authentication request parameters.

 |
| 

typedef struct [FIDO2\_CredentialCreationOptionArray](../../header-files-and-structs/structs/fido2-credentialcreationoptionarray/document.md) [FIDO2\_CredentialCreationOptionArray](#ga2c517a89040b570e15517f7719ed4cad)

 | 

Defines a struct of the additional parameter array of an authentication credential.

 |
| 

typedef struct [FIDO2\_AttestationFormatsArray](../../header-files-and-structs/structs/fido2-attestationformatsarray/document.md) [FIDO2\_AttestationFormatsArray](#gae6d363b5e0bb786bbb1b28d4863c84c2)

 | 

Defines a struct of preferences regarding the attestation statement format used by the authenticator. It is an array defined by the relying party.

 |
| 

typedef struct [FIDO2\_PublicKeyCredentialCreationOptions](../../header-files-and-structs/structs/fido2-publickeycredentialcreationoptions/document.md) [FIDO2\_PublicKeyCredentialCreationOptions](#ga41d2d104407689b7cfc1ed38c1ed2726)

 | 

Defines a struct of the options for credential creation.

 |
| 

typedef struct [FIDO2\_CredentialCreationOptions](../../header-files-and-structs/structs/fido2-credentialcreationoptions/document.md) [FIDO2\_CredentialCreationOptions](#ga6cd8020c0afbf089d298aaf751345bff)

 | 

Defines a struct of the credential request options.

 |
| 

typedef struct [FIDO2\_AuthenticatorMetadata](../../header-files-and-structs/structs/fido2-authenticatormetadata/document.md) [FIDO2\_AuthenticatorMetadata](#gafdb5807d009529053a96c737b2ee7c55)

 | 

Defines a struct of the authenticator metadata.

 |
| 

typedef struct [FIDO2\_CredentialRequestOptions](../../header-files-and-structs/structs/fido2-credentialrequestoptions/document.md) [FIDO2\_CredentialRequestOptions](#ga4db55935548b74ad18c5fb6f15f80a7b)

 | 

Defines a struct of the authentication information dictionary object.

 |
| 

typedef struct [FIDO2\_AuthenticatorMetadataArray](../../header-files-and-structs/structs/fido2-authenticatormetadataarray/document.md) [FIDO2\_AuthenticatorMetadataArray](#ga1e40d19100575390959d7d7dfe13a52a)

 | 

Defines a struct of the array of supported authenticators.

 |
| 

typedef struct [FIDO2\_Capability](../../header-files-and-structs/structs/fido2-capability/document.md) [FIDO2\_Capability](#ga483e50693a9bf926f524ba9ed1178f0b)

 | 

Defines a struct of passkey capabilities.

 |
| 

typedef struct [FIDO2\_CapabilityArray](../../header-files-and-structs/structs/fido2-capabilityarray/document.md) [FIDO2\_CapabilityArray](#ga674019e8f264253ca8f3390ce93ad46f)

 | 

Defines a struct of the array of capabilities.

 |
| 

typedef struct [FIDO2\_TokenBinding](../../header-files-and-structs/structs/fido2-tokenbinding/document.md) [FIDO2\_TokenBinding](#ga80db96062ec07eff0f2807e516b5a5f1)

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

[FIDO2\_TokenBindingStatus](#ga3a0c5c93081cd75c8ecd7a1efac8252e) { FIDO2\_PRESENT = 0, FIDO2\_SUPPORTED = 1 }

 | 

Enumerates the token binding statuses.

 |
| 

[FIDO2\_AttestationConveyancePreference](#ga1e33947b822678781f03c849ade9f45f) { FIDO2\_NONE = 0, FIDO2\_INDIRECT = 1, FIDO2\_DIRECT = 2, FIDO2\_ENTERPRISE = 3 }

 | 

Enumerates the attestation conveyance preferences, which are referenced by a WebAuthn relying party during credential generation.

 |
| 

[FIDO2\_UserVerificationRequirement](#ga632b7b26c16a519650398ccfc3515f7a) { FIDO2\_REQUIRED = 0, FIDO2\_PREFERRED = 1, FIDO2\_DISCOURAGED = 2 }

 | 

Enumerates the requirements for user verification (to check whether the current user is the intended user) by a relying party. User verification is required for some operations but not for others.

 |
| 

[FIDO2\_AuthenticatorAttachment](#gaa6aa2fca2e7690e98f6d1d273324e471) { FIDO2\_PLATFORM = 0, FIDO2\_CROSS\_PLATFORM = 1 }

 | 

Enumerates the authenticator information (platform or roaming).

 |
| 

[FIDO2\_AuthenticatorTransport](#ga02592e5b749c266e7297333afce03cec) {

FIDO2\_USB = 0, FIDO2\_NFC = 1, FIDO2\_BLE = 2, FIDO2\_SMART\_CARD = 3,

FIDO2\_HYBRID = 4, FIDO2\_INTERNAL = 5

}

 | 

Enumerates the authenticator transports.

 |
| 

[FIDO2\_Algorithm](#ga27cd96fc7f972c4cd8cfe4d92737920a) {

FIDO2\_ES256 = -7, FIDO2\_ES384 = -35, FIDO2\_ES512 = -36, FIDO2\_RS256 = -257,

FIDO2\_RS384 = -258, FIDO2\_RS512 = -259, FIDO2\_PS256 = -37, FIDO2\_PS384 = -38,

FIDO2\_PS512 = -39

}

 | 

Enumerates the algorithms.

 |
| 

[FIDO2\_PublicKeyCredentialHint](#gab7b1367ea48debe767ae103f8ac9e96c) { FIDO2\_SECURITY\_KEY = 0, FIDO2\_CLIENT\_DEVICE = 1, FIDO2\_HINT\_HYBRID = 2 }

 | 

Enumerates the authentication mode hints.

 |
| 

[FIDO2\_PublicKeyCredentialType](#gaa46edbba8f1162737d26681080eea727) { FIDO2\_PUBLIC\_KEY = 0 }

 | 

Enumerates the public key credential types.

 |
| 

[FIDO2\_Uvm](#ga60fda18b064802349b186de072b43e98) { FIDO2\_UVM\_FINGERPRINT = 2, FIDO2\_UVM\_PIN = 4, FIDO2\_UVM\_FACEPRINT = 16 }

 | 

Enumerates the UVMs.

 |
| 

[FIDO2\_ClientCapability](#gae8cdc5641132b84e0313c7412d13bbbe) {

FIDO2\_CONDITIONAL\_CREATE = 0, FIDO2\_CONDITIONAL\_GET = 1, FIDO2\_HYBRID\_TRANSPORT = 2, FIDO2\_PASSKEY\_PLATFORM\_AUTHENTICATOR = 3,

FIDO2\_USER\_VERIFYING\_PLATFORM\_AUTHENTICATOR = 4, FIDO2\_RELATED\_ORIGINS = 5, FIDO2\_SIGNAL\_ALL\_ACCEPTED\_CREDENTIALS = 6, FIDO2\_SIGNAL\_CURRENT\_USER\_DETAILS = 7,

FIDO2\_SIGNAL\_UNKNOWN\_CREDENTIAL = 8, FIDO2\_EXTENSION\_UVI = 9

}

 | 

Enumerates the client capabilities.

 |
| 

[FIDO2\_CredentialMediationRequirement](#ga16035d1941d25a1ea71203ad72809b93) { FIDO2\_SILENT = 0, FIDO2\_OPTIONAL = 1, FIDO2\_CONDITIONAL = 2, FIDO2\_MEDIATION\_REQUIRED = 3 }

 | 

Enumerates the user mediation requirements.

 |
| 

[FIDO2\_ErrorCode](#ga759dad4964a084008360c4b99e2ec693) {

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

void [HMS\_FIDO2\_initCreationOptions](#ga1d655e31c512e2cb8dfc3c1e616d03aa) ([FIDO2\_CredentialCreationOptions](../../header-files-and-structs/structs/fido2-credentialcreationoptions/document.md) \*options)

 | 

Initializes the **FIDO2\_CredentialCreationOptions** struct.

 |
| 

void [HMS\_FIDO2\_initTokenBinding](#ga46853c19611bf506dca76820b2446c19) ([FIDO2\_TokenBinding](../../header-files-and-structs/structs/fido2-tokenbinding/document.md) \*tokenBinding)

 | 

Initializes the **FIDO2\_TokenBinding** struct.

 |
| 

void [HMS\_FIDO2\_initRequestOptions](#ga5ae4e44e8d06e0c247308d7329970c3a) ([FIDO2\_CredentialRequestOptions](../../header-files-and-structs/structs/fido2-credentialrequestoptions/document.md) \*options)

 | 

Initializes the **FIDO2\_CredentialRequestOptions** struct.

 |
| 

[FIDO2\_ErrorCode](#ga759dad4964a084008360c4b99e2ec693) [HMS\_FIDO2\_getClientCapability](#ga3745265749b2776403960fbeece3de77) ([FIDO2\_CapabilityArray](../../header-files-and-structs/structs/fido2-capabilityarray/document.md) \*\*capability)

 | 

Queries the client capabilities supported by the current device or version. When the value for a given capability is **true**, it indicates that the capability is supported.

 |
| 

[FIDO2\_ErrorCode](#ga759dad4964a084008360c4b99e2ec693) [HMS\_FIDO2\_getPlatformAuthenticator](#ga18b569cb28a659f4282acbb64e198195) ([FIDO2\_AuthenticatorMetadataArray](../../header-files-and-structs/structs/fido2-authenticatormetadataarray/document.md) \*\*authenticators)

 | 

Obtains the list of supported platform authenticators.

 |
| 

[FIDO2\_ErrorCode](#ga759dad4964a084008360c4b99e2ec693) [HMS\_FIDO2\_register](#gaaaed812197e7dc4d5f9a3354d5349665) (const [FIDO2\_CredentialCreationOptions](../../header-files-and-structs/structs/fido2-credentialcreationoptions/document.md) options, const [FIDO2\_TokenBinding](../../header-files-and-structs/structs/fido2-tokenbinding/document.md) tokenBinding, const char \*origin, [FIDO2\_PublicKeyAttestationCredential](../../header-files-and-structs/structs/fido2-publickeyattestationcredential/document.md) \*\*publicKeyAttestationCredential)

 | 

Registers a passkey.

 |
| 

[FIDO2\_ErrorCode](#ga759dad4964a084008360c4b99e2ec693) [HMS\_FIDO2\_authenticate](#gaac4365229064efc78dc25dceb7c932a3) (const [FIDO2\_CredentialRequestOptions](../../header-files-and-structs/structs/fido2-credentialrequestoptions/document.md) options, const [FIDO2\_TokenBinding](../../header-files-and-structs/structs/fido2-tokenbinding/document.md) tokenBinding, const char \*origin, [FIDO2\_PublicKeyAssertionCredential](../../header-files-and-structs/structs/fido2-publickeyassertioncredential/document.md) \*\*publicKeyAssertionCredential)

 | 

Performs FIDO2 authentication.

 |
| 

void [HMS\_FIDO2\_CapabilityArray\_Destroy](#ga4287e078ad1dbe55804ea73133173949) ([FIDO2\_CapabilityArray](../../header-files-and-structs/structs/fido2-capabilityarray/document.md) \*capability)

 | 

Destroys the array of capabilities.

 |
| 

void [HMS\_FIDO2\_AuthenticatorMetadataArray\_Destroy](#gaa5f5050def714db82bfed358922c897c) ([FIDO2\_AuthenticatorMetadataArray](../../header-files-and-structs/structs/fido2-authenticatormetadataarray/document.md) \*authenticators)

 | 

Destroys the array of authenticator metadata.

 |
| 

void [HMS\_FIDO2\_PublicKeyAttestationCredential\_Destroy](#ga10cff1c35e596a604fbd4289abc5696b) ([FIDO2\_PublicKeyAttestationCredential](../../header-files-and-structs/structs/fido2-publickeyattestationcredential/document.md) \*publicKeyAttestationCredential)

 | 

Destroys the **PublicKeyAttestationCredential** struct.

 |
| 

void [HMS\_FIDO2\_PublicKeyAssertionCredential\_Destroy](#gaba286b4df1149f3632d5a44c15a5ee1e) ([FIDO2\_PublicKeyAssertionCredential](../../header-files-and-structs/structs/fido2-publickeyassertioncredential/document.md) \*publicKeyAssertionCredential)

 | 

Destroys the **PublicKeyAssertionCredential** struct.

 |

#### Type Description

#### \[h2\]AuthenticationExtensionsClientOutputs

typedef struct [AuthenticationExtensionsClientOutputs](../../header-files-and-structs/structs/authenticationextensionsclientoutputs/document.md) [AuthenticationExtensionsClientOutputs](../../header-files-and-structs/structs/authenticationextensionsclientoutputs/document.md)

**Description**

Defines a struct of authentication extensions.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_Algorithm

typedef enum [FIDO2\_Algorithm](#ga27cd96fc7f972c4cd8cfe4d92737920a) [FIDO2\_Algorithm](#ga27cd96fc7f972c4cd8cfe4d92737920a)

**Description**

Defines an enum of algorithms.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_AttestationConveyancePreference

typedef enum [FIDO2\_AttestationConveyancePreference](#ga1e33947b822678781f03c849ade9f45f) [FIDO2\_AttestationConveyancePreference](#ga1e33947b822678781f03c849ade9f45f)

**Description**

Defines an enum of attestation conveyance preferences, which are referenced by a WebAuthn relying party during credential generation.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_AttestationFormatsArray

typedef struct [FIDO2\_AttestationFormatsArray](../../header-files-and-structs/structs/fido2-attestationformatsarray/document.md) [FIDO2\_AttestationFormatsArray](../../header-files-and-structs/structs/fido2-attestationformatsarray/document.md)

**Description**

Defines a struct of preferences regarding the attestation statement format used by the authenticator. It is an array defined by the relying party.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_AuthenticatorAttachment

typedef enum [FIDO2\_AuthenticatorAttachment](#gaa6aa2fca2e7690e98f6d1d273324e471) [FIDO2\_AuthenticatorAttachment](#gaa6aa2fca2e7690e98f6d1d273324e471)

**Description**

Defines an enum of authenticator information (platform or roaming).

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_AuthenticatorAttestationResponse

typedef struct [FIDO2\_AuthenticatorAttestationResponse](../../header-files-and-structs/structs/fido2-authenticatorattestationresponse/document.md) [FIDO2\_AuthenticatorAttestationResponse](../../header-files-and-structs/structs/fido2-authenticatorattestationresponse/document.md)

**Description**

Defines a struct of the authenticator attestation response.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_AuthenticatorMetadata

typedef struct [FIDO2\_AuthenticatorMetadata](../../header-files-and-structs/structs/fido2-authenticatormetadata/document.md) [FIDO2\_AuthenticatorMetadata](../../header-files-and-structs/structs/fido2-authenticatormetadata/document.md)

**Description**

Defines a struct of the authenticator metadata.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_AuthenticatorMetadataArray

typedef struct [FIDO2\_AuthenticatorMetadataArray](../../header-files-and-structs/structs/fido2-authenticatormetadataarray/document.md) [FIDO2\_AuthenticatorMetadataArray](../../header-files-and-structs/structs/fido2-authenticatormetadataarray/document.md)

**Description**

Defines a struct of the array of supported authenticators.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_AuthenticatorResponse

typedef struct [FIDO2\_AuthenticatorResponse](../../header-files-and-structs/structs/fido2-authenticatorresponse/document.md) [FIDO2\_AuthenticatorResponse](../../header-files-and-structs/structs/fido2-authenticatorresponse/document.md)

**Description**

Defines a struct of the authenticator assertion response.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_AuthenticatorSelectionCriteria

typedef struct [FIDO2\_AuthenticatorSelectionCriteria](../../header-files-and-structs/structs/fido2-authenticatorselectioncriteria/document.md) [FIDO2\_AuthenticatorSelectionCriteria](../../header-files-and-structs/structs/fido2-authenticatorselectioncriteria/document.md)

**Description**

Defines a struct of the authenticator selection criteria, which are specified by a WebAuthn relying party.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_AuthenticatorTransport

typedef enum [FIDO2\_AuthenticatorTransport](#ga02592e5b749c266e7297333afce03cec) [FIDO2\_AuthenticatorTransport](#ga02592e5b749c266e7297333afce03cec)

**Description**

Defines an enum of authenticator transports.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_AuthenticatorTransportArray

typedef struct [FIDO2\_AuthenticatorTransportArray](../../header-files-and-structs/structs/fido2-authenticatortransportarray/document.md) [FIDO2\_AuthenticatorTransportArray](../../header-files-and-structs/structs/fido2-authenticatortransportarray/document.md)

**Description**

Defines a struct of the array of authenticator transports.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_Capability

typedef struct [FIDO2\_Capability](../../header-files-and-structs/structs/fido2-capability/document.md) [FIDO2\_Capability](../../header-files-and-structs/structs/fido2-capability/document.md)

**Description**

Defines a struct of passkey capabilities.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_CapabilityArray

typedef struct [FIDO2\_CapabilityArray](../../header-files-and-structs/structs/fido2-capabilityarray/document.md) [FIDO2\_CapabilityArray](../../header-files-and-structs/structs/fido2-capabilityarray/document.md)

**Description**

Defines a struct of the array of capabilities.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_ClientCapability

typedef enum [FIDO2\_ClientCapability](#gae8cdc5641132b84e0313c7412d13bbbe) [FIDO2\_ClientCapability](#gae8cdc5641132b84e0313c7412d13bbbe)

**Description**

Defines an enum of client capabilities.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_CredentialCreationOptionArray

typedef struct [FIDO2\_CredentialCreationOptionArray](../../header-files-and-structs/structs/fido2-credentialcreationoptionarray/document.md) [FIDO2\_CredentialCreationOptionArray](../../header-files-and-structs/structs/fido2-credentialcreationoptionarray/document.md)

**Description**

Defines a struct of the additional parameter array of an authentication credential.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_CredentialCreationOptions

typedef struct [FIDO2\_CredentialCreationOptions](../../header-files-and-structs/structs/fido2-credentialcreationoptions/document.md) [FIDO2\_CredentialCreationOptions](../../header-files-and-structs/structs/fido2-credentialcreationoptions/document.md)

**Description**

Defines a struct of the credential request options.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_CredentialMediationRequirement

typedef enum [FIDO2\_CredentialMediationRequirement](#ga16035d1941d25a1ea71203ad72809b93) [FIDO2\_CredentialMediationRequirement](#ga16035d1941d25a1ea71203ad72809b93)

**Description**

Defines an enum of user mediation requirements.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_CredentialRequestOptions

typedef struct [FIDO2\_CredentialRequestOptions](../../header-files-and-structs/structs/fido2-credentialrequestoptions/document.md) [FIDO2\_CredentialRequestOptions](../../header-files-and-structs/structs/fido2-credentialrequestoptions/document.md)

**Description**

Defines a struct of the authentication information dictionary object.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_ErrorCode

typedef enum [FIDO2\_ErrorCode](#ga759dad4964a084008360c4b99e2ec693) [FIDO2\_ErrorCode](#ga759dad4964a084008360c4b99e2ec693)

**Description**

Defines an enum of error codes.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_PublicKeyAssertionCredential

typedef struct [FIDO2\_PublicKeyAssertionCredential](../../header-files-and-structs/structs/fido2-publickeyassertioncredential/document.md) [FIDO2\_PublicKeyAssertionCredential](../../header-files-and-structs/structs/fido2-publickeyassertioncredential/document.md)

**Description**

Defines a struct of the authentication result.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_PublicKeyAttestationCredential

typedef struct [FIDO2\_PublicKeyAttestationCredential](../../header-files-and-structs/structs/fido2-publickeyattestationcredential/document.md) [FIDO2\_PublicKeyAttestationCredential](../../header-files-and-structs/structs/fido2-publickeyattestationcredential/document.md)

**Description**

Defines a struct of the registration result.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_PublicKeyCredentialCreationOptions

typedef struct [FIDO2\_PublicKeyCredentialCreationOptions](../../header-files-and-structs/structs/fido2-publickeycredentialcreationoptions/document.md) [FIDO2\_PublicKeyCredentialCreationOptions](../../header-files-and-structs/structs/fido2-publickeycredentialcreationoptions/document.md)

**Description**

Defines a struct of the options for credential creation.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_PublicKeyCredentialDescriptor

typedef struct [FIDO2\_PublicKeyCredentialDescriptor](../../header-files-and-structs/structs/fido2-publickeycredentialdescriptor/document.md) [FIDO2\_PublicKeyCredentialDescriptor](../../header-files-and-structs/structs/fido2-publickeycredentialdescriptor/document.md)

**Description**

Defines a struct of credential parameters during registration or authentication.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_PublicKeyCredentialDescriptorArray

typedef struct [FIDO2\_PublicKeyCredentialDescriptorArray](../../header-files-and-structs/structs/fido2-publickeycredentialdescriptorarray/document.md) [FIDO2\_PublicKeyCredentialDescriptorArray](../../header-files-and-structs/structs/fido2-publickeycredentialdescriptorarray/document.md)

**Description**

Defines a struct of the array of public key credential descriptors.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_PublicKeyCredentialHint

typedef enum [FIDO2\_PublicKeyCredentialHint](#gab7b1367ea48debe767ae103f8ac9e96c) [FIDO2\_PublicKeyCredentialHint](#gab7b1367ea48debe767ae103f8ac9e96c)

**Description**

Defines an enum of authentication mode hints.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_PublicKeyCredentialHintArray

typedef struct [FIDO2\_PublicKeyCredentialHintArray](../../header-files-and-structs/structs/fido2-publickeycredentialhintarray/document.md) [FIDO2\_PublicKeyCredentialHintArray](../../header-files-and-structs/structs/fido2-publickeycredentialhintarray/document.md)

**Description**

Defines a struct of the array of authentication mode hints.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_PublicKeyCredentialParameters

typedef struct [FIDO2\_PublicKeyCredentialParameters](../../header-files-and-structs/structs/fido2-publickeycredentialparameters/document.md) [FIDO2\_PublicKeyCredentialParameters](../../header-files-and-structs/structs/fido2-publickeycredentialparameters/document.md)

**Description**

Defines a struct of the additional parameters of an authentication credential.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_PublicKeyCredentialRequestOptions

typedef struct [FIDO2\_PublicKeyCredentialRequestOptions](../../header-files-and-structs/structs/fido2-publickeycredentialrequestoptions/document.md) [FIDO2\_PublicKeyCredentialRequestOptions](../../header-files-and-structs/structs/fido2-publickeycredentialrequestoptions/document.md)

**Description**

Defines a struct of the passkey authentication request parameters.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_PublicKeyCredentialRpEntity

typedef struct [FIDO2\_PublicKeyCredentialRpEntity](../../header-files-and-structs/structs/fido2-publickeycredentialrpentity/document.md) [FIDO2\_PublicKeyCredentialRpEntity](../../header-files-and-structs/structs/fido2-publickeycredentialrpentity/document.md)

**Description**

Defines a struct of the relying party attributes provided during credential creation.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_PublicKeyCredentialType

typedef enum [FIDO2\_PublicKeyCredentialType](#gaa46edbba8f1162737d26681080eea727) [FIDO2\_PublicKeyCredentialType](#gaa46edbba8f1162737d26681080eea727)

**Description**

Defines an enum of public key credential types.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_PublicKeyCredentialUserEntity

typedef struct [FIDO2\_PublicKeyCredentialUserEntity](../../header-files-and-structs/structs/fido2-publickeycredentialuserentity/document.md) [FIDO2\_PublicKeyCredentialUserEntity](../../header-files-and-structs/structs/fido2-publickeycredentialuserentity/document.md)

**Description**

Defines a struct of the user attributes provided during credential creation.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_TokenBinding

typedef struct [FIDO2\_TokenBinding](../../header-files-and-structs/structs/fido2-tokenbinding/document.md) [FIDO2\_TokenBinding](../../header-files-and-structs/structs/fido2-tokenbinding/document.md)

**Description**

Defines a struct of the token binding protocol, which is used by the client to communicate with the relying party.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_TokenBindingStatus

typedef enum [FIDO2\_TokenBindingStatus](#ga3a0c5c93081cd75c8ecd7a1efac8252e) [FIDO2\_TokenBindingStatus](#ga3a0c5c93081cd75c8ecd7a1efac8252e)

**Description**

Defines an enum of token binding statuses.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_UserVerificationRequirement

typedef enum [FIDO2\_UserVerificationRequirement](#ga632b7b26c16a519650398ccfc3515f7a) [FIDO2\_UserVerificationRequirement](#ga632b7b26c16a519650398ccfc3515f7a)

**Description**

Defines an enum of requirements for user verification (to check whether the current user is the intended user) by a relying party. User verification is required for some operations but not for others.

**Start version**: 6.0.0(20)

#### \[h2\]FIDO2\_Uvm

typedef enum [FIDO2\_Uvm](#ga60fda18b064802349b186de072b43e98) [FIDO2\_Uvm](#ga60fda18b064802349b186de072b43e98)

**Description**

Defines an enum of UVMs.

**Start version**: 6.0.0(20)

#### \[h2\]Uint8Buff

typedef struct [Uint8Buff](../../header-files-and-structs/structs/uint8buff/document.md) [Uint8Buff](../../header-files-and-structs/structs/uint8buff/document.md)

**Description**

Defines a struct of a uint8\_t byte stream.

**Start version**: 6.0.0(20)

#### Enumeration Description

#### \[h2\]FIDO2\_Algorithm

enum [FIDO2\_Algorithm](#ga27cd96fc7f972c4cd8cfe4d92737920a)

**Description**

Enumerates the cryptographic algorithms.

**Start version**: 6.0.0(20)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FIDO2\_ES256

 | 

ES256 algorithm.

 |
| 

FIDO2\_ES384

 | 

ES384 algorithm.

 |
| 

FIDO2\_ES512

 | 

ES512 algorithm.

 |
| 

FIDO2\_RS256

 | 

RS256 algorithm.

 |
| 

FIDO2\_RS384

 | 

RS384 algorithm.

 |
| 

FIDO2\_RS512

 | 

RS512 algorithm

 |
| 

FIDO2\_PS256

 | 

PS256 algorithm.

 |
| 

FIDO2\_PS384

 | 

PS384 algorithm.

 |
| 

FIDO2\_PS512

 | 

PS512 algorithm.

 |

#### \[h2\]FIDO2\_AttestationConveyancePreference

enum [FIDO2\_AttestationConveyancePreference](#ga1e33947b822678781f03c849ade9f45f)

**Description**

Enumerates the attestation conveyance preferences, which are referenced by a WebAuthn relying party during credential generation.

**Start version**: 6.0.0(20)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FIDO2\_NONE

 | 

The relying party is not interested in authenticator attestation. This is the default value.

 |
| 

FIDO2\_INDIRECT

 | 

The indirect relying party wants to receive a verifiable attestation statement, but allows the client to decide how to obtain such an attestation statement.

 |
| 

FIDO2\_DIRECT

 | 

The direct relying party wants to receive the attestation statement as generated by the authenticator.

 |
| 

FIDO2\_ENTERPRISE

 | 

The relying party wants to receive an enterprise attestation statement which may include information that uniquely identifies the authenticator.

 |

#### \[h2\]FIDO2\_AuthenticatorAttachment

enum [FIDO2\_AuthenticatorAttachment](#gaa6aa2fca2e7690e98f6d1d273324e471)

**Description**

Enumerates the authenticator information (platform or roaming).

**Start version**: 6.0.0(20)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FIDO2\_PLATFORM

 | 

Platform authenticator, such as a PIN, fingerprint, or face.

 |
| 

FIDO2\_CROSS\_PLATFORM

 | 

Cross-platform authenticator, also called roaming authenticator, which includes Bluetooth, NFC, and USB.

 |

#### \[h2\]FIDO2\_AuthenticatorTransport

enum [FIDO2\_AuthenticatorTransport](#ga02592e5b749c266e7297333afce03cec)

**Description**

Enumerates the authenticator transports. It specifies the modes of transmitting authentication data between the authenticator and the client device.

**Start version**: 6.0.0(20)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FIDO2\_USB

 | 

USB.

 |
| 

FIDO2\_NFC

 | 

Near Field Communication (NFC).

 |
| 

FIDO2\_BLE

 | 

Bluetooth Low Energy (BLE).

 |
| 

FIDO2\_SMART\_CARD

 | 

Smart card.

 |
| 

FIDO2\_HYBRID

 | 

Hybrid, indicating multiple data transport modes.

 |
| 

FIDO2\_INTERNAL

 | 

Internal (built-in device transport).

 |

#### \[h2\]FIDO2\_ClientCapability

enum [FIDO2\_ClientCapability](#gae8cdc5641132b84e0313c7412d13bbbe)

**Description**

Enumerates the client capabilities.

**Start version**: 6.0.0(20)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FIDO2\_CONDITIONAL\_CREATE

 | 

Passkey registration.

 |
| 

FIDO2\_CONDITIONAL\_GET

 | 

Authentication using a passkey.

 |
| 

FIDO2\_HYBRID\_TRANSPORT

 | 

Hybrid transport, indicating multiple data transport modes.

 |
| 

FIDO2\_PASSKEY\_PLATFORM\_AUTHENTICATOR

 | 

Passkey platform authenticator.

 |
| 

FIDO2\_USER\_VERIFYING\_PLATFORM\_AUTHENTICATOR

 | 

User-verifying platform authenticator.

 |
| 

FIDO2\_RELATED\_ORIGINS

 | 

Supporting related origin requests.

 |
| 

FIDO2\_SIGNAL\_ALL\_ACCEPTED\_CREDENTIALS

 | 

Sending all accepted credentials.

 |
| 

FIDO2\_SIGNAL\_CURRENT\_USER\_DETAILS

 | 

Sending detailed information about the current user.

 |
| 

FIDO2\_SIGNAL\_UNKNOWN\_CREDENTIAL

 | 

Sending unknown credentials.

 |
| 

FIDO2\_EXTENSION\_UVI

 | 

User Verification Index (UVI) extension parameter.

 |

#### \[h2\]FIDO2\_CredentialMediationRequirement

enum [FIDO2\_CredentialMediationRequirement](#ga16035d1941d25a1ea71203ad72809b93)

**Description**

Enumerates the user mediation requirements.

**Start version**: 6.0.0(20)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FIDO2\_SILENT

 | 

User mediation is suppressed for a given operation. If the operation can be performed without user involvement, wonderful. If user involvement is necessary, then the operation will return null rather than involving the user.

 |
| 

FIDO2\_OPTIONAL

 | 

User mediation is optional. If credentials can be handed over for a given operation without user mediation, they will be. If user mediation is required, then the user agent will involve the user in the decision.

 |
| 

FIDO2\_CONDITIONAL

 | 

User mediation is required conditionally. In the authentication scenario, if the device has credentials, user mediation is required for selecting credentials. In the registration scenario, if the user has already agreed to create credentials, the credentials can be created without user mediation.

 |
| 

FIDO2\_MEDIATION\_REQUIRED

 | 

The user agent will not hand over credentials without user mediation.

 |

#### \[h2\]FIDO2\_ErrorCode

enum [FIDO2\_ErrorCode](#ga759dad4964a084008360c4b99e2ec693)

**Description**

Enumerates the error codes.

**Start version**: 6.0.0(20)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FIDO2\_SUCCESS

 | 

Successful.

 |
| 

FIDO2\_PERMISSION\_DENIED

 | 

Permission denied.

 |
| 

FIDO2\_DEVICE\_NOT\_SUPPORT

 | 

Device type error.

**Start version**: 6.0.1(21)

 |
| 

FIDO2\_NOT\_SUPPORT

 | 

Not supported by the system.

 |
| 

FIDO2\_INVALID\_STATE

 | 

Invalid state.

 |
| 

FIDO2\_INTEGRITY\_CHECK\_FAILED

 | 

System integrity check failed.

 |
| 

FIDO2\_USER\_ABORT

 | 

Terminated by the user.

 |
| 

FIDO2\_TIMEOUT

 | 

Timeout.

 |
| 

FIDO2\_ENCODING\_ERROR

 | 

Encoding error.

 |
| 

FIDO2\_UNKNOWN\_ERROR

 | 

Unknown error.

 |
| 

FIDO2\_CONSTRAINT\_ERROR

 | 

Incorrect constraint condition.

 |
| 

FIDO2\_DATA\_ERROR

 | 

Data error.

 |
| 

FIDO2\_USER\_REJECTS

 | 

Rejected by the user.

 |
| 

FIDO2\_CONNECT\_SERVICE\_FAILED

 | 

Failed to connect to the service.

 |
| 

FIDO2\_MAX\_CRED\_NUM\_REACHED

 | 

The number of credentials reaches the maximum.

 |
| 

FIDO2\_INVALID\_CTAP\_COMMAND

 | 

Invalid CTAP command.

 |
| 

FIDO2\_INVALID\_PARAMETERS

 | 

Invalid parameters in the command.

 |
| 

FIDO2\_INVALID\_MESSAGE\_OR\_ATTRIBUTE\_LENGTH

 | 

Invalid message or attribute length.

 |
| 

FIDO2\_INVALID\_CBOR\_OR\_UNPREDICTABLE

 | 

Invalid CBOR or unpredictable error.

 |
| 

FIDO2\_PARSE\_CBOR\_FAILED

 | 

CBOR parsing failed.

 |
| 

FIDO2\_INVALID\_CREDENTIALS

 | 

Invalid credentials.

 |
| 

FIDO2\_NOT\_ALLOWED

 | 

Not allowed.

 |
| 

FIDO2\_USER\_VERIFICATION\_FAILED

 | 

User verification failed.

 |
| 

FIDO2\_OTHER\_ERROR

 | 

Other errors.

 |

#### \[h2\]FIDO2\_PublicKeyCredentialHint

enum [FIDO2\_PublicKeyCredentialHint](#gab7b1367ea48debe767ae103f8ac9e96c)

**Description**

Enumerates the authentication mode hints. It specifies the authentication mode selected by the user.

**Start version**: 6.0.0(20)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FIDO2\_SECURITY\_KEY

 | 

Security key.

 |
| 

FIDO2\_CLIENT\_DEVICE

 | 

Client device.

 |
| 

FIDO2\_HINT\_HYBRID

 | 

Hybrid.

 |

#### \[h2\]FIDO2\_PublicKeyCredentialType

enum [FIDO2\_PublicKeyCredentialType](#gaa46edbba8f1162737d26681080eea727)

**Description**

Enumerates the public key credential types.

**Start version**: 6.0.0(20)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FIDO2\_PUBLIC\_KEY

 | 

Public key.

 |

#### \[h2\]FIDO2\_TokenBindingStatus

enum [FIDO2\_TokenBindingStatus](#ga3a0c5c93081cd75c8ecd7a1efac8252e)

**Description**

Enumerates the token binding statuses.

**Start version**: 6.0.0(20)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FIDO2\_PRESENT

 | 

Normal communication.

 |
| 

FIDO2\_SUPPORTED

 | 

Token binding is supported, but no negotiation is performed during communication with the relying party.

 |

#### \[h2\]FIDO2\_UserVerificationRequirement

enum [FIDO2\_UserVerificationRequirement](#ga632b7b26c16a519650398ccfc3515f7a)

**Description**

Enumerates the requirements for user verification (to check whether the current user is the intended user) by a relying party. User verification is required for some operations but not for others.

**Start version**: 6.0.0(20)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FIDO2\_REQUIRED

 | 

User verification is required.

 |
| 

FIDO2\_PREFERRED

 | 

The relying party prefers user verification for the operation if possible, but will not fail the operation if the response does not have the user verification flag set.

 |
| 

FIDO2\_DISCOURAGED

 | 

The relying party does not want user verification employed during the operation.

 |

#### \[h2\]FIDO2\_Uvm

enum [FIDO2\_Uvm](#ga60fda18b064802349b186de072b43e98)

**Description**

Enumerates the UVMs.

**Start version**: 6.0.0(20)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FIDO2\_UVM\_FINGERPRINT

 | 

Fingerprint.

 |
| 

FIDO2\_UVM\_PIN

 | 

PIN.

 |
| 

FIDO2\_UVM\_FACEPRINT

 | 

3D face.

 |

#### Function Description

#### \[h2\]HMS\_FIDO2\_authenticate()

[FIDO2\_ErrorCode](#ga759dad4964a084008360c4b99e2ec693) HMS\_FIDO2\_authenticate (const [FIDO2\_CredentialRequestOptions](../../header-files-and-structs/structs/fido2-credentialrequestoptions/document.md) options, const [FIDO2\_TokenBinding](../../header-files-and-structs/structs/fido2-tokenbinding/document.md) tokenBinding, const char \* origin, [FIDO2\_PublicKeyAssertionCredential](../../header-files-and-structs/structs/fido2-publickeyassertioncredential/document.md) \*\* publicKeyAssertionCredential)

**Description**

Performs authentication using a passkey. It can be called only by non-UI threads.

**Required permission**: ohos.permission.ACCESS\_FIDO2\_ONLINEAUTH

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

options

 | 

Authentication request options.

 |
| 

tokenBinding

 | 

Token binding.

 |
| 

origin

 | 

Secure origin from which the method is called. The length ranges from 0 to 256 characters.

 |
| 

publicKeyAssertionCredential

 | 

Authentication response.

 |

**Returns**:

If the function is executed successfully, **FIDO2\_SUCCESS** is returned. If the function fails to be executed, a specific error code is returned. For details, please refer to [FIDO2\_ErrorCode](#ga313648b7100419fc2cd6c1a73b0ad7ec).

#### \[h2\]HMS\_FIDO2\_AuthenticatorMetadataArray\_Destroy()

void HMS\_FIDO2\_AuthenticatorMetadataArray\_Destroy ([FIDO2\_AuthenticatorMetadataArray](../../header-files-and-structs/structs/fido2-authenticatormetadataarray/document.md) \* authenticators)

**Description**

Destroys the array of authenticator metadata.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

authenticators

 | 

Array of the authenticator metadata to be destroyed.

 |

#### \[h2\]HMS\_FIDO2\_CapabilityArray\_Destroy()

void HMS\_FIDO2\_CapabilityArray\_Destroy ([FIDO2\_CapabilityArray](../../header-files-and-structs/structs/fido2-capabilityarray/document.md) \* capability)

**Description**

Destroys the array of capabilities.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

capability

 | 

Array of capabilities to be destroyed.

 |

#### \[h2\]HMS\_FIDO2\_getClientCapability()

[FIDO2\_ErrorCode](#ga759dad4964a084008360c4b99e2ec693) HMS\_FIDO2\_getClientCapability ([FIDO2\_CapabilityArray](../../header-files-and-structs/structs/fido2-capabilityarray/document.md) \*\* capability)

**Description**

Queries the client capabilities supported by the current device or version. When the value for a given capability is **true**, it indicates that the capability is supported.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

capability

 | 

Indicates whether a client capability is supported.

 |

**Returns**:

If the function is executed successfully, **FIDO2\_SUCCESS** is returned. If the function fails to be executed, an error code is returned. For details, please refer to [FIDO2\_ErrorCode](#ga313648b7100419fc2cd6c1a73b0ad7ec).

#### \[h2\]HMS\_FIDO2\_getPlatformAuthenticator()

[FIDO2\_ErrorCode](#ga759dad4964a084008360c4b99e2ec693) HMS\_FIDO2\_getPlatformAuthenticator ([FIDO2\_AuthenticatorMetadataArray](../../header-files-and-structs/structs/fido2-authenticatormetadataarray/document.md) \*\* authenticators)

**Description**

Obtains the list of supported platform authenticators.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

authenticators

 | 

List of supported platform authenticators.

 |

**Returns**:

If the function is executed successfully, **FIDO2\_SUCCESS** is returned. If the function fails to be executed, an error code is returned. For details, please refer to [FIDO2\_ErrorCode](#ga313648b7100419fc2cd6c1a73b0ad7ec).

#### \[h2\]HMS\_FIDO2\_initCreationOptions()

void HMS\_FIDO2\_initCreationOptions ([FIDO2\_CredentialCreationOptions](../../header-files-and-structs/structs/fido2-credentialcreationoptions/document.md) \* options)

**Description**

Initializes the **FIDO2\_CredentialCreationOptions** struct.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

options

 | 

Pointer to the **FIDO2\_CredentialCreationOptions** struct to be initialized.

 |

#### \[h2\]HMS\_FIDO2\_initRequestOptions()

void HMS\_FIDO2\_initRequestOptions ([FIDO2\_CredentialRequestOptions](../../header-files-and-structs/structs/fido2-credentialrequestoptions/document.md) \* options)

**Description**

Initializes the **FIDO2\_CredentialRequestOptions** struct.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

options

 | 

Pointer to the **FIDO2\_CredentialRequestOptions** struct to be initialized.

 |

#### \[h2\]HMS\_FIDO2\_initTokenBinding()

void HMS\_FIDO2\_initTokenBinding ([FIDO2\_TokenBinding](../../header-files-and-structs/structs/fido2-tokenbinding/document.md) \* tokenBinding)

**Description**

Initializes the **FIDO2\_TokenBinding** struct.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

tokenBinding

 | 

Pointer to the **FIDO2\_TokenBinding** struct to be initialized.

 |

#### \[h2\]HMS\_FIDO2\_PublicKeyAssertionCredential\_Destroy()

void HMS\_FIDO2\_PublicKeyAssertionCredential\_Destroy ([FIDO2\_PublicKeyAssertionCredential](../../header-files-and-structs/structs/fido2-publickeyassertioncredential/document.md) \* publicKeyAssertionCredential)

**Description**

Destroys the **PublicKeyAssertionCredential** struct.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

publicKeyAssertionCredential

 | 

**PublicKeyAssertionCredential** struct to be destroyed.

 |

#### \[h2\]HMS\_FIDO2\_PublicKeyAttestationCredential\_Destroy()

void HMS\_FIDO2\_PublicKeyAttestationCredential\_Destroy ([FIDO2\_PublicKeyAttestationCredential](../../header-files-and-structs/structs/fido2-publickeyattestationcredential/document.md) \* publicKeyAttestationCredential)

**Description**

Destroys the **PublicKeyAttestationCredential** struct.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

publicKeyAttestationCredential

 | 

**PublicKeyAttestationCredential** struct to be destroyed.

 |

#### \[h2\]HMS\_FIDO2\_register()

[FIDO2\_ErrorCode](#ga759dad4964a084008360c4b99e2ec693) HMS\_FIDO2\_register (const [FIDO2\_CredentialCreationOptions](../../header-files-and-structs/structs/fido2-credentialcreationoptions/document.md) options, const [FIDO2\_TokenBinding](../../header-files-and-structs/structs/fido2-tokenbinding/document.md) tokenBinding, const char \* origin, [FIDO2\_PublicKeyAttestationCredential](../../header-files-and-structs/structs/fido2-publickeyattestationcredential/document.md) \*\* publicKeyAttestationCredential)

**Description**

Registers a passkey. It can be called only by non-UI threads.

**Required permission**: ohos.permission.ACCESS\_FIDO2\_ONLINEAUTH

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

options

 | 

Registration request options.

 |
| 

tokenBinding

 | 

Token binding.

 |
| 

origin

 | 

Origin from which the method is called. The length ranges from 0 to 256 characters.

 |
| 

publicKeyAttestationCredential

 | 

Registration response.

 |

**Returns**:

If the function is executed successfully, **FIDO2\_SUCCESS** is returned. If the function fails to be executed, an error code is returned. For details, please refer to [FIDO2\_ErrorCode](#ga313648b7100419fc2cd6c1a73b0ad7ec).
