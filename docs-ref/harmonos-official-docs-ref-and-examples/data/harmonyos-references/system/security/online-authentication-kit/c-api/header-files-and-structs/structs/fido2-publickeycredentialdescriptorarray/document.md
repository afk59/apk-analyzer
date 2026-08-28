# FIDO2\_PublicKeyCredentialDescriptorArray

#### Overview

Defines the array of public key credential descriptors.

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

uint32\_t [allowCredentiallNum](#a1085b6c76d592a26a86e2502d44312e3)

 | 

Number of allowed credentials.

 |
| 

[FIDO2\_PublicKeyCredentialDescriptor](../fido2-publickeycredentialdescriptor/document.md) \* [allowCredentials](#aaccb43d445bbaacfabcd5d9a37152c3f)

 | 

Additional parameter list of an authentication credential. The default value is **\[\]**.

 |

#### Member Variable Description

#### \[h2\]allowCredentiallNum

uint32\_t FIDO2\_PublicKeyCredentialDescriptorArray::allowCredentiallNum

**Description**

Number of allowed credentials.

#### \[h2\]allowCredentials

[FIDO2\_PublicKeyCredentialDescriptor](../fido2-publickeycredentialdescriptor/document.md)\* FIDO2\_PublicKeyCredentialDescriptorArray::allowCredentials

**Description**

Additional parameter list of an authentication credential. The default value is **\[\]**.
