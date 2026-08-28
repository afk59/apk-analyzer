# FIDO2\_AttestationFormatsArray

#### Overview

Defines preferences regarding the attestation statement format used by the authenticator. It is an array defined by the relying party.

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

uint32\_t [attestationFormatsNum](#a9a5c37c7c8d200a5172cea8211abf188)

 | 

Number of parameters in **PubKeyCredParam**.

 |
| 

char \*\* [attestationFormats](#a892d146b5f52e312bafa619a6eb792fc)

 | 

Additional parameter list of an authentication credential.

 |

#### Member Variable Description

#### \[h2\]attestationFormats

char\*\* FIDO2\_AttestationFormatsArray::attestationFormats

**Description**

Additional parameter list of an authentication credential.

#### \[h2\]attestationFormatsNum

uint32\_t FIDO2\_AttestationFormatsArray::attestationFormatsNum

**Description**

Length of the additional parameter list of an authentication credential.
