# FIDO2\_AuthenticatorMetadataArray

#### Overview

Defines the array of supported authenticators.

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

uint32\_t [number](#a7c651eca3b7f544a7b233fcb23ab8717)

 | 

Number of authenticators.

 |
| 

[FIDO2\_AuthenticatorMetadata](../fido2-authenticatormetadata/document.md) \* [authenticators](#a25670f7508e2a20f0c72519db28c5c59)

 | 

Extensions supported by the authenticator.

 |

#### Member Variable Description

#### \[h2\]authenticators

[FIDO2\_AuthenticatorMetadata](../fido2-authenticatormetadata/document.md)\* FIDO2\_AuthenticatorMetadataArray::authenticators

**Description**

Extensions supported by the authenticator.

#### \[h2\]number

uint32\_t FIDO2\_AuthenticatorMetadataArray::number

**Description**

Number of authenticators.
