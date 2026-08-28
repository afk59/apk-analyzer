# FIDO2\_AuthenticatorMetadata

#### Overview

Defines the authenticator metadata.

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

[Uint8Buff](../uint8buff/document.md) [aaguid](#a69443cd171e66c315384775a12ef5528)

 | 

Authenticator attestation globally unique identifier.

 |
| 

[FIDO2\_Uvm](../../../modules/passkeys/document.md#ga60fda18b064802349b186de072b43e98) [uvm](#af352363afd660f220c988b515fd0bba5)

 | 

Supported authenticator type.

 |
| 

bool [isAvailable](#a9918ca9079143bbd93a5f977223a0421)

 | 

Indicates whether an authenticator is available.

 |

#### Member Variable Description

#### \[h2\]aaguid

[Uint8Buff](../uint8buff/document.md) FIDO2\_AuthenticatorMetadata::aaguid

**Description**

Authenticator attestation globally unique identifier.

#### \[h2\]isAvailable

bool FIDO2\_AuthenticatorMetadata::isAvailable

**Description**

Indicates whether an authenticator is available. If **true** is returned, the authenticator is available. If **false** is returned, the authenticator is unavailable.

#### \[h2\]uvm

[FIDO2\_Uvm](../../../modules/passkeys/document.md#ga60fda18b064802349b186de072b43e98) FIDO2\_AuthenticatorMetadata::uvm

**Description**

Supported authenticator type.
