# FIDO2\_PublicKeyCredentialDescriptor

#### Overview

Defines the credential parameters during registration or authentication.

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

[FIDO2\_PublicKeyCredentialType](../../../modules/passkeys/document.md#gaa46edbba8f1162737d26681080eea727) [type](#af26b9b07b0b456f01d527439dab91bc7)

 | 

Credential type.

 |
| 

[Uint8Buff](../uint8buff/document.md) [id](#a1667f2884a9b3fbc969a80196510fe24)

 | 

Credential identifier.

 |
| 

[FIDO2\_AuthenticatorTransportArray](../fido2-authenticatortransportarray/document.md) [transports](#a97de56cc6859f743b46c399502460d34)

 | 

Authenticator access type (USB, NFC, or Bluetooth).

 |

#### Member Variable Description

#### \[h2\]id

[Uint8Buff](../uint8buff/document.md) FIDO2\_PublicKeyCredentialDescriptor::id

**Description**

Credential identifier.

#### \[h2\]transports

[FIDO2\_AuthenticatorTransportArray](../fido2-authenticatortransportarray/document.md) FIDO2\_PublicKeyCredentialDescriptor::transports

**Description**

Authenticator access type (USB, NFC, or Bluetooth).

#### \[h2\]type

[FIDO2\_PublicKeyCredentialType](../../../modules/passkeys/document.md#gaa46edbba8f1162737d26681080eea727) FIDO2\_PublicKeyCredentialDescriptor::type

**Description**

Credential type.
