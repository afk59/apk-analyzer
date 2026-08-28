# FIDO2\_PublicKeyCredentialUserEntity

#### Overview

Defines the user attributes provided during credential creation.

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

[Uint8Buff](../uint8buff/document.md) [id](#a89acdc47998ced27b3e55b7f99c90797)

 | 

Credential identifier.

 |
| 

char \* [displayName](#af3d18ba7f46b81ffe1d54660c0cfe4be)

 | 

User name displayed on the foreground.

 |
| 

char \* [name](#ae25422337bd8154afbfc7272698f3978)

 | 

User name.

 |

#### Member Variable Description

#### \[h2\]displayName

char\* FIDO2\_PublicKeyCredentialUserEntity::displayName

**Description**

User name displayed on the foreground.

#### \[h2\]id

[Uint8Buff](../uint8buff/document.md) FIDO2\_PublicKeyCredentialUserEntity::id

**Description**

Credential identifier.

#### \[h2\]name

char\* FIDO2\_PublicKeyCredentialUserEntity::name

**Description**

User name.
