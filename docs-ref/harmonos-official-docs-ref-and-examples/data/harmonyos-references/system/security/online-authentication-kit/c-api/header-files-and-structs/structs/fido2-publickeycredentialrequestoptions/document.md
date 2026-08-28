# FIDO2\_PublicKeyCredentialRequestOptions

#### Overview

Defines the passkey authentication request parameters.

**Start version**: 6.0.0(20)

**Related module**: [FIDO2](../../../modules/passkeys/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[Uint8Buff](../uint8buff/document.md) [challenge](#a1e9595b070a8f14c84584caac9fe4b12)

 | 

Challenge.

 |
| 

uint32\_t [timeout](#af40a180a55e9ec9ccdbdfbc0663fa6a0)

 | 

Maximum duration of the authentication operation, in ms. The default value is **300000** (5 minutes). Optional.

 |
| 

char \* [rpId](#af1e1f8a828c88c2baace9cc97e13253d)

 | 

Relying party identifier (such as a domain name). By default, it is left empty. Optional.

 |
| 

[FIDO2\_PublicKeyCredentialDescriptorArray](../fido2-publickeycredentialdescriptorarray/document.md) [allowCredentials](#a8b1b230c4537756fdedfa3d3011efa7f)

 | 

Additional parameter list of an authentication credential. By default, the list is empty. Optional.

 |
| 

[FIDO2\_UserVerificationRequirement](../../../modules/passkeys/document.md#ga632b7b26c16a519650398ccfc3515f7a) [userVerification](#a56ab962fc3732a25608cb0be55b1bc03)

 | 

Enum of user verification requirements. The default value is **preferred**. Optional.

 |
| 

[FIDO2\_PublicKeyCredentialHintArray](../fido2-publickeycredentialhintarray/document.md) [hints](#a5397cbbb234b741cbc00b288b289a3a0)

 | 

Authentication mode hints. The default value is **\[\]**. Optional.

 |
| 

char \* [extensions](#ad9695387a2b91111848f47232235e2d3)

 | 

Extensions, which must be a JSON string representing a Map<string, Object> object. By default, it is left empty. Optional.

 |

#### Member Variable Description

#### \[h2\]allowCredentials

[FIDO2\_PublicKeyCredentialDescriptorArray](../fido2-publickeycredentialdescriptorarray/document.md) FIDO2\_PublicKeyCredentialRequestOptions::allowCredentials

**Description**

Additional parameter list of an authentication credential. Optional.

#### \[h2\]challenge

[Uint8Buff](../uint8buff/document.md) FIDO2\_PublicKeyCredentialRequestOptions::challenge

**Description**

Challenge.

#### \[h2\]extensions

char\* FIDO2\_PublicKeyCredentialRequestOptions::extensions

**Description**

Extensions, which must be a JSON string representing a Map<string, Object> object. Optional.

#### \[h2\]hints

[FIDO2\_PublicKeyCredentialHintArray](../fido2-publickeycredentialhintarray/document.md) FIDO2\_PublicKeyCredentialRequestOptions::hints

**Description**

Authentication mode hints. The default value is **\[\]**. Optional.

#### \[h2\]rpId

char\* FIDO2\_PublicKeyCredentialRequestOptions::rpId

**Description**

Relying party identifier. Optional.

#### \[h2\]timeout

uint32\_t FIDO2\_PublicKeyCredentialRequestOptions::timeout

**Description**

Maximum duration of the authentication operation, in ms. Optional.

#### \[h2\]userVerification

[FIDO2\_UserVerificationRequirement](../../../modules/passkeys/document.md#ga632b7b26c16a519650398ccfc3515f7a) FIDO2\_PublicKeyCredentialRequestOptions::userVerification

**Description**

Enum of user verification requirements. The default value is **preferred**. Optional.
