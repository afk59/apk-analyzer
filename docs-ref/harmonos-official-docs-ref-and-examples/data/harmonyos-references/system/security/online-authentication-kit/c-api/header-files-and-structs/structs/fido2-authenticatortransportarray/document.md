# FIDO2\_AuthenticatorTransportArray

#### Overview

Defines the array of authenticator transports.

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

uint32\_t [transportNum](#acd67a9c618c8f8c40d3cebcdc21922d1)

 | 

Number of transports.

 |
| 

[FIDO2\_AuthenticatorTransport](../../../modules/passkeys/document.md#ga02592e5b749c266e7297333afce03cec) \* [transports](#aa3c4f2f321d482ae32dc3b795ecc2c65)

 | 

Authenticator access type (USB, NFC, or Bluetooth).

 |

#### Member Variable Description

#### \[h2\]transportNum

uint32\_t FIDO2\_AuthenticatorTransportArray::transportNum

**Description**

Number of transports.

#### \[h2\]transports

[FIDO2\_AuthenticatorTransport](../../../modules/passkeys/document.md#ga02592e5b749c266e7297333afce03cec)\* FIDO2\_AuthenticatorTransportArray::transports

**Description**

Authenticator access type (USB, NFC, or Bluetooth).
