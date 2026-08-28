# FIDO2\_CredentialCreationOptionArray

#### Overview

Defines the array of additional parameters of an authentication credential.

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

uint32\_t [pubKeyCredParamNum](#a06e70ab9f71fb6291e9b3df957a2ae17)

 | 

Number of parameters in **PubKeyCredParam**.

 |
| 

[FIDO2\_PublicKeyCredentialParameters](../fido2-publickeycredentialparameters/document.md) \* [pubKeyCredParams](#ab17a90ca7b76e6bca3cde9e18ce1f774)

 | 

Additional parameters of an authentication credential.

 |

#### Member Variable Description

#### \[h2\]pubKeyCredParamNum

uint32\_t FIDO2\_CredentialCreationOptionArray::pubKeyCredParamNum

**Description**

Number of parameters in **PubKeyCredParam**.

#### \[h2\]pubKeyCredParams

[FIDO2\_PublicKeyCredentialParameters](../fido2-publickeycredentialparameters/document.md)\* FIDO2\_CredentialCreationOptionArray::pubKeyCredParams

**Description**

Additional parameters of an authentication credential.
