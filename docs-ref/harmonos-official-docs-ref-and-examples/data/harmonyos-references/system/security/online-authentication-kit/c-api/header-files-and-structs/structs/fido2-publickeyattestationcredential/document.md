# FIDO2\_PublicKeyAttestationCredential

#### Overview

Defines the registration result.

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

[Uint8Buff](../uint8buff/document.md) [rawId](#abc90a2b565a8e48d6d965ccc27c32445)

 | 

Raw credential identifier.

 |
| 

[FIDO2\_AuthenticatorAttestationResponse](../fido2-authenticatorattestationresponse/document.md) [response](#ad1c1c4fd329dc63e5332d26dc404b405)

 | 

Authenticator attestation response.

 |
| 

[FIDO2\_AuthenticatorAttachment](../../../modules/passkeys/document.md#gaa6aa2fca2e7690e98f6d1d273324e471) [authenticatorAttachment](#ae15ff75bfa90c5c79c8ddbe3cf464366)

 | 

Authenticator information (platform or roaming). The default value is **FIDO2\_PLATFORM**. Optional.

 |
| 

const char \* [id](#afa23550117d766125eca72390af0632e)

 | 

Credential identifier. The requirements for the identifier are distinct for each type of credential.

 |
| 

const char \* [type](#a180d55f4eff94208c319c1b5f3d40e20)

 | 

Value of a credential object's interface object's \[\[type\]\] slot. It specifies the credential type represented by this object.

 |
| 

[AuthenticationExtensionsClientOutputs](../authenticationextensionsclientoutputs/document.md) [clientExtensionResults](#aef514f978325f0a09305b10353f8ec3c)

 | 

Client extension result. The current version does not support extensions, so the placeholder is always **NULL** and the value corresponding to the **clientExtensionResults** key must be parsed into **{}**.

 |

#### Member Variable Description

#### \[h2\]authenticatorAttachment

[FIDO2\_AuthenticatorAttachment](../../../modules/passkeys/document.md#gaa6aa2fca2e7690e98f6d1d273324e471) FIDO2\_PublicKeyAttestationCredential::authenticatorAttachment

**Description**

Authenticator information (platform or roaming). Optional.

#### \[h2\]clientExtensionResults

[AuthenticationExtensionsClientOutputs](../authenticationextensionsclientoutputs/document.md) FIDO2\_PublicKeyAttestationCredential::clientExtensionResults

**Description**

Client extension result. The current version does not support extensions, so the placeholder is always **NULL** and the value corresponding to the **clientExtensionResults** key must be parsed into **{}**.

#### \[h2\]id

const char\* FIDO2\_PublicKeyAttestationCredential::id

**Description**

Credential identifier. The requirements for the identifier are distinct for each type of credential.

#### \[h2\]rawId

[Uint8Buff](../uint8buff/document.md) FIDO2\_PublicKeyAttestationCredential::rawId

**Description**

Raw credential identifier.

#### \[h2\]response

[FIDO2\_AuthenticatorAttestationResponse](../fido2-authenticatorattestationresponse/document.md) FIDO2\_PublicKeyAttestationCredential::response

**Description**

Authenticator attestation response.

#### \[h2\]type

const char\* FIDO2\_PublicKeyAttestationCredential::type

**Description**

Value of a credential object's interface object's \[\[type\]\] slot. It specifies the credential type represented by this object.
