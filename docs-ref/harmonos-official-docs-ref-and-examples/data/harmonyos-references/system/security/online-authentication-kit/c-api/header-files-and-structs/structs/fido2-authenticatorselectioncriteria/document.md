# FIDO2\_AuthenticatorSelectionCriteria

#### Overview

Defines the authenticator selection criteria, which are specified by a WebAuthn relying party.

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

[FIDO2\_AuthenticatorAttachment](../../../modules/passkeys/document.md#gaa6aa2fca2e7690e98f6d1d273324e471) [authenticatorAttachment](#a5a16c0b91ed4c2391957997fb3e88ef9)

 | 

Authenticator information (platform or roaming). The default value is **FIDO2\_PLATFORM**. Optional.

 |
| 

const char \* [residentKey](#a589e6893a729673451d1f96de44a5512)

 | 

Resident key. By default, it is left empty. Optional.

 |
| 

bool [requireResidentKey](#ad6ce444067958a3a44143642bc091404)

 | 

Indicates whether a resident key is required. The value **true** indicates yes, and the value **false** indicates no. The default value is **false**. Optional.

 |
| 

[FIDO2\_UserVerificationRequirement](../../../modules/passkeys/document.md#ga632b7b26c16a519650398ccfc3515f7a) [userVerification](#a0344ec93a5f4544e6bbc0a2d496c867f)

 | 

Enum of user verification requirements. The default value is **preferred**. Optional.

 |

#### Member Variable Description

#### \[h2\]authenticatorAttachment

[FIDO2\_AuthenticatorAttachment](../../../modules/passkeys/document.md#gaa6aa2fca2e7690e98f6d1d273324e471) FIDO2\_AuthenticatorSelectionCriteria::authenticatorAttachment

**Description**

Authenticator information (platform or roaming). Optional.

#### \[h2\]requireResidentKey

bool FIDO2\_AuthenticatorSelectionCriteria::requireResidentKey

**Description**

Indicates whether a resident key is required. The value **true** indicates yes, and the value **false** indicates no. The default value is **false**. Optional.

#### \[h2\]residentKey

const char\* FIDO2\_AuthenticatorSelectionCriteria::residentKey

**Description**

Resident key. Optional.

#### \[h2\]userVerification

[FIDO2\_UserVerificationRequirement](../../../modules/passkeys/document.md#ga632b7b26c16a519650398ccfc3515f7a) FIDO2\_AuthenticatorSelectionCriteria::userVerification

**Description**

Enum of user verification requirements. The default value is **preferred**. Optional.
