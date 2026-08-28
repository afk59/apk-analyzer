# FIDO2\_PublicKeyCredentialCreationOptions

#### Overview

Defines the options for credential creation.

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

[FIDO2\_PublicKeyCredentialRpEntity](../fido2-publickeycredentialrpentity/document.md) [rp](#a73116b439c5f43f84087e894ed664ad1)

 | 

Relying party attributes provided during credential creation.

 |
| 

[FIDO2\_PublicKeyCredentialUserEntity](../fido2-publickeycredentialuserentity/document.md) [user](#a92cb44322ca7e1007c8736632cd0964b)

 | 

User attributes provided during credential creation.

 |
| 

[Uint8Buff](../uint8buff/document.md) [challenge](#aeba2a19abf19398c6d4292e3f144ab94)

 | 

Challenge value.

 |
| 

[FIDO2\_CredentialCreationOptionArray](../fido2-credentialcreationoptionarray/document.md) [pubKeyCredParams](#aee42ffb77c2581dcc04b49fd0fcc8f41)

 | 

Array of additional parameters of an authentication credential.

 |
| 

uint32\_t [timeout](#afc2e551c307244eb5ac213e0cad9e2ac)

 | 

Maximum duration of the registration operation, in ms. The default value is **300000** (5 minutes). Optional.

 |
| 

[FIDO2\_PublicKeyCredentialDescriptorArray](../fido2-publickeycredentialdescriptorarray/document.md) [excludeCredentials](#ae5ada7403f89bbe3d9e1c8e09c6c8a5e)

 | 

List of credentials already registered with the FIDO server. The default value is **\[\]**. Optional.

 |
| 

[FIDO2\_AuthenticatorSelectionCriteria](../fido2-authenticatorselectioncriteria/document.md) [authenticatorSelection](#a7eef9101b8235fc4ef31e22cb7f43af9)

 | 

Authenticator selection criteria.

 |
| 

[FIDO2\_PublicKeyCredentialHintArray](../fido2-publickeycredentialhintarray/document.md) [hints](#a5ca0d3727ad8d0b262af8592b2a5bbbb)

 | 

Authentication mode hints. The default value is **\[\]**. Optional.

 |
| 

[FIDO2\_AttestationConveyancePreference](../../../modules/passkeys/document.md#ga1e33947b822678781f03c849ade9f45f) [attestation](#a7f6d16e60e5fc64bb54a3299a975e539)

 | 

Attestation conveyance preference. The default value is **none**. Optional.

 |
| 

[FIDO2\_AttestationFormatsArray](../fido2-attestationformatsarray/document.md) [attestationFormats](#a94e9ebb712dd404ac3807bc52549d6dd)

 | 

Preference regarding the attestation statement format used by the authenticator. It is specified by the relying party. The default value is **\[\]**.

 |
| 

char \* [extensions](#acbb159628fcd36243f29b10d4d04449d)

 | 

Extensions, which must be a JSON string representing a Map<string, Object> object. By default, it is left empty. Optional.

 |

#### Member Variable Description

#### \[h2\]attestation

[FIDO2\_AttestationConveyancePreference](../../../modules/passkeys/document.md#ga1e33947b822678781f03c849ade9f45f) FIDO2\_PublicKeyCredentialCreationOptions::attestation

**Description**

Attestation conveyance preference. The default value is **none**. Optional.

#### \[h2\]attestationFormats

[FIDO2\_AttestationFormatsArray](../fido2-attestationformatsarray/document.md) FIDO2\_PublicKeyCredentialCreationOptions::attestationFormats

**Description**

Preference regarding the attestation statement format used by the authenticator. It is specified by the relying party. The default value is **\[\]**.

#### \[h2\]authenticatorSelection

[FIDO2\_AuthenticatorSelectionCriteria](../fido2-authenticatorselectioncriteria/document.md) FIDO2\_PublicKeyCredentialCreationOptions::authenticatorSelection

**Description**

Authenticator selection criteria.

#### \[h2\]challenge

[Uint8Buff](../uint8buff/document.md) FIDO2\_PublicKeyCredentialCreationOptions::challenge

**Description**

Challenge.

#### \[h2\]excludeCredentials

[FIDO2\_PublicKeyCredentialDescriptorArray](../fido2-publickeycredentialdescriptorarray/document.md) FIDO2\_PublicKeyCredentialCreationOptions::excludeCredentials

**Description**

List of credentials already registered with the FIDO server. The default value is **\[\]**. Optional.

#### \[h2\]extensions

char\* FIDO2\_PublicKeyCredentialCreationOptions::extensions

**Description**

Extensions, which must be a JSON string representing a Map<string, Object> object. Optional.

#### \[h2\]hints

[FIDO2\_PublicKeyCredentialHintArray](../fido2-publickeycredentialhintarray/document.md) FIDO2\_PublicKeyCredentialCreationOptions::hints

**Description**

Authentication mode hints. The default value is **\[\]**. Optional.

#### \[h2\]pubKeyCredParams

[FIDO2\_CredentialCreationOptionArray](../fido2-credentialcreationoptionarray/document.md) FIDO2\_PublicKeyCredentialCreationOptions::pubKeyCredParams

**Description**

Array of additional parameters of an authentication credential.

#### \[h2\]rp

[FIDO2\_PublicKeyCredentialRpEntity](../fido2-publickeycredentialrpentity/document.md) FIDO2\_PublicKeyCredentialCreationOptions::rp

**Description**

Relying party attributes provided during credential creation.

#### \[h2\]timeout

uint32\_t FIDO2\_PublicKeyCredentialCreationOptions::timeout

**Description**

Maximum duration of the registration operation, in ms. Optional.

#### \[h2\]user

[FIDO2\_PublicKeyCredentialUserEntity](../fido2-publickeycredentialuserentity/document.md) FIDO2\_PublicKeyCredentialCreationOptions::user

**Description**

User attributes provided during credential creation.
