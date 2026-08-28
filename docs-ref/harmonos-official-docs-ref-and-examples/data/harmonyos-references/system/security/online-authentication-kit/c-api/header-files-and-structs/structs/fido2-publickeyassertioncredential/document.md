# FIDO2\_PublicKeyAssertionCredential

#### Overview

Defines the authentication result.

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

[Uint8Buff](../uint8buff/document.md) [rawId](#a8adf6d21e094b1cf4b0a1e751014f2a3)

 | 

Raw credential identifier.

 |
| 

const char \* [id](#ad4fcc71b65296eec9da4fe4d759b1103)

 | 

Credential identifier. The requirements for the identifier are distinct for each type of credential.

 |
| 

const char \* [type](#a0bc28b95c86cbecf8818b9d12918ca44)

 | 

Value of a credential object's interface object's \[\[type\]\] slot, which is a JSON string. It specifies the credential type represented by this object.

 |
| 

[FIDO2\_AuthenticatorResponse](../fido2-authenticatorresponse/document.md) [response](#a219c84e621a4f6039bbdfa774d33439b)

 | 

Authenticator assertion response.

 |
| 

[FIDO2\_AuthenticatorAttachment](../../../modules/passkeys/document.md#gaa6aa2fca2e7690e98f6d1d273324e471) [authenticatorAttachment](#ac29d396433f47c6230ccca4fd046dfa1)

 | 

Authenticator information (platform or roaming). The default value is **FIDO2\_PLATFORM**. Optional.

 |
| 

[AuthenticationExtensionsClientOutputs](../authenticationextensionsclientoutputs/document.md) [clientExtensionResults](#a62824d1fe883644cda1960e011fede7c)

 | 

Client extension result. The current version does not support extensions, so the placeholder is always **NULL** and the value corresponding to the **clientExtensionResults** key must be parsed into **{}**.

 |

#### Member Variable Description

#### \[h2\]authenticatorAttachment

[FIDO2\_AuthenticatorAttachment](../../../modules/passkeys/document.md#gaa6aa2fca2e7690e98f6d1d273324e471) FIDO2\_PublicKeyAssertionCredential::authenticatorAttachment

**Description**

Authenticator information (platform or roaming). Optional.

#### \[h2\]clientExtensionResults

[AuthenticationExtensionsClientOutputs](../authenticationextensionsclientoutputs/document.md) FIDO2\_PublicKeyAssertionCredential::clientExtensionResults

**Description**

Client extension result. The current version does not support extensions, so the placeholder is always **NULL** and the value corresponding to the **clientExtensionResults** key must be parsed into **{}**.

#### \[h2\]id

const char\* FIDO2\_PublicKeyAssertionCredential::id

**Description**

Credential identifier. The requirements for the identifier are distinct for each type of credential.

#### \[h2\]rawId

[Uint8Buff](../uint8buff/document.md) FIDO2\_PublicKeyAssertionCredential::rawId

**Description**

Raw credential identifier.

#### \[h2\]response

[FIDO2\_AuthenticatorResponse](../fido2-authenticatorresponse/document.md) FIDO2\_PublicKeyAssertionCredential::response

**Description**

Authenticator assertion response.

#### \[h2\]type

const char\* FIDO2\_PublicKeyAssertionCredential::type

**Description**

Value of a credential object's interface object's \[\[type\]\] slot, which is a JSON string. It specifies the credential type represented by this object.
