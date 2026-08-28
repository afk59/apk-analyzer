# FIDO2\_AuthenticatorResponse

#### Overview

Defines the authenticator assertion response.

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

[Uint8Buff](../uint8buff/document.md) [authenticatorData](#a4885e9778d931bf68044939fe6a9b895)

 | 

Authenticator data.

 |
| 

[Uint8Buff](../uint8buff/document.md) [signature](#ad51a95561a84021c8bb2bd5070ca07ec)

 | 

Signature.

 |
| 

[Uint8Buff](../uint8buff/document.md) [userHandle](#a09d4f78982031d057d0235ca225a137e)

 | 

User handle (user ID). Optional.

 |
| 

[Uint8Buff](../uint8buff/document.md) [clientDataJson](#aa98421c9febb5f460cbe4c9b9420cc69)

 | 

Client data, which represents the contextual bindings of the WebAuthn relying party and the client. The data includes the type, challenge, and origin.

 |

#### Member Variable Description

#### \[h2\]authenticatorData

[Uint8Buff](../uint8buff/document.md) FIDO2\_AuthenticatorResponse::authenticatorData

**Description**

Authenticator data.

#### \[h2\]clientDataJson

[Uint8Buff](../uint8buff/document.md) FIDO2\_AuthenticatorResponse::clientDataJson

**Description**

Client data, which represents the contextual bindings of the WebAuthn relying party and the client. The data includes the type, challenge, and origin.

#### \[h2\]signature

[Uint8Buff](../uint8buff/document.md) FIDO2\_AuthenticatorResponse::signature

**Description**

Signature.

#### \[h2\]userHandle

[Uint8Buff](../uint8buff/document.md) FIDO2\_AuthenticatorResponse::userHandle

**Description**

User handle. Optional.
