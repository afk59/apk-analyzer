# FIDO2\_AuthenticatorAttestationResponse

#### Overview

Defines the authenticator attestation response.

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

[Uint8Buff](../uint8buff/document.md) [attestationObject](#a3e876d044501dcc3fb3f0433d7c2766b)

 | 

Attestation object.

 |
| 

[Uint8Buff](../uint8buff/document.md) [clientDataJson](#ab0b05a7e50e252583481e8b47404bd00)

 | 

Client data, which represents the contextual bindings of the WebAuthn relying party and the client. The data includes the type, challenge, and origin.

 |
| 

[Uint8Buff](../uint8buff/document.md) [publicKey](#a9479186904add89fc9a5cac11b4b64cd)

 | 

Options of the public key credential request, represented as a byte stream.

 |
| 

[Uint8Buff](../uint8buff/document.md) [authenticatorData](#ab9d09b1672f4690d8246200e8ce0d2ab)

 | 

Authenticator data, represented as a byte stream.

 |
| 

[FIDO2\_Algorithm](../../../modules/passkeys/document.md#ga27cd96fc7f972c4cd8cfe4d92737920a) [publicKeyAlgorithm](#a283dce979858a43e0185bb17d8e4ab32)

 | 

Cryptographic algorithm.

 |
| 

[FIDO2\_AuthenticatorTransportArray](../fido2-authenticatortransportarray/document.md) [transports](#a152f995f69179b1067d32cd2cabfadde)

 | 

Authenticator access type (USB, NFC, or Bluetooth).

 |

#### Member Variable Description

#### \[h2\]attestationObject

[Uint8Buff](../uint8buff/document.md) FIDO2\_AuthenticatorAttestationResponse::attestationObject

**Description**

Attestation object.

#### \[h2\]authenticatorData

[Uint8Buff](../uint8buff/document.md) FIDO2\_AuthenticatorAttestationResponse::authenticatorData

**Description**

Authenticator data, represented as a byte stream.

#### \[h2\]clientDataJson

[Uint8Buff](../uint8buff/document.md) FIDO2\_AuthenticatorAttestationResponse::clientDataJson

**Description**

Client data, which represents the contextual bindings of the WebAuthn relying party and the client. The data includes the type, challenge, and origin.

#### \[h2\]publicKey

[Uint8Buff](../uint8buff/document.md) FIDO2\_AuthenticatorAttestationResponse::publicKey

**Description**

Options of the public key credential request, represented as a byte stream.

#### \[h2\]publicKeyAlgorithm

[FIDO2\_Algorithm](../../../modules/passkeys/document.md#ga27cd96fc7f972c4cd8cfe4d92737920a) FIDO2\_AuthenticatorAttestationResponse::publicKeyAlgorithm

**Description**

Cryptographic algorithm.

#### \[h2\]transports

[FIDO2\_AuthenticatorTransportArray](../fido2-authenticatortransportarray/document.md) FIDO2\_AuthenticatorAttestationResponse::transports

**Description**

Authenticator access type (USB, NFC, or Bluetooth).
