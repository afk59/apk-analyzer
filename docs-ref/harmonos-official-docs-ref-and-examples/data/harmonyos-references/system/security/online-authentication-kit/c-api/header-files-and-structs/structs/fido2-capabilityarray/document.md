# FIDO2\_CapabilityArray

#### Overview

Defines the array of capabilities.

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

uint32\_t [number](#a76a1441a6186306388f5008c4e6a3c1c)

 | 

Number of capabilities.

 |
| 

[FIDO2\_Capability](../fido2-capability/document.md) \* [capability](#ab0bdcdf4d5eb6f72906334316629193c)

 | 

Array of capabilities.

 |

#### Member Variable Description

#### \[h2\]capability

[FIDO2\_Capability](../fido2-capability/document.md)\* FIDO2\_CapabilityArray::capability

**Description**

Array of capabilities.

#### \[h2\]number

uint32\_t FIDO2\_CapabilityArray::number

**Description**

Length of the capability array.
