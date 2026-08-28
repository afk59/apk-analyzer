# Rcp\_ServerAuthentication

#### Overview

Server identity verification information.

**Start version**: 5.0.0(12)

**Related module**: [RemoteCommunication](../../../modules/remotecommunication/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[Rcp\_Credential](../rcp-credential/document.md) [credential](#a01fbe231a7a2302e66e9582d617ef73b)

 | 

Server credential.

 |
| 

[Rcp\_AuthenticationType](../../../modules/remotecommunication/document.md#gaa1b9ec2bd61b2c95492f45eb0a447bff) [authenticationType](#accd28314a33f1ded057b40e33322292a)

 | 

Server identity verification type. If the type is not set, negotiation with the server is required.

 |

#### Member Variable Description

#### \[h2\]authenticationType

[Rcp\_AuthenticationType](../../../modules/remotecommunication/document.md#gaa1b9ec2bd61b2c95492f45eb0a447bff) Rcp\_ServerAuthentication::authenticationType

**Description**

Server identity verification type. If the type is not set, negotiation with the server is required.

#### \[h2\]credential

[Rcp\_Credential](../rcp-credential/document.md) Rcp\_ServerAuthentication::credential

**Description**

Server credential.
