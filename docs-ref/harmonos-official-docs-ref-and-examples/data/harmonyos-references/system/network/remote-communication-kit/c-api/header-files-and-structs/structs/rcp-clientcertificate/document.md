# Rcp\_ClientCertificate

#### Overview

Client certificate sent to a remote server, which will be used by the server to verify the identity of the client.

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

char \* [content](#aa6630a26570a25349dab3e9280f782b9)

 | 

Client certificate content. The certificate file must be in PEM, DER, or P12 format.

 |
| 

char \* [filePath](#a8d7f4b03387823946edd84952772998b)

 | 

Path of the client certificate. The certificate file must be in PEM, DER, or P12 format.

 |
| 

char \* [key](#ac6d5c955c1cfeefc9a70cf45131ad25f)

 | 

Name of the private key file of the client certificate.

 |
| 

char \* [keyPassword](#a05de541cd1c59f9f0bd1305ebc11a56a)

 | 

Password of the private key of the client certificate.

 |
| 

[Rcp\_CertType](../../../modules/remotecommunication/document.md#ga4f79c1d41b9c586d99f1c22ed81b9aee) [type](#a50eedad042bd9de8ef3c5dad02af78af)

 | 

Client certificate type.

 |

#### Member Variable Description

#### \[h2\]content

char\* Rcp\_ClientCertificate::content

**Description**

Client certificate content. The certificate file must be in PEM, DER, or P12 format.

#### \[h2\]filePath

char\* Rcp\_ClientCertificate::filePath

**Description**

Path of the client certificate. The certificate file must be in PEM, DER, or P12 format.

#### \[h2\]key

char\* Rcp\_ClientCertificate::key

**Description**

Name of the private key file of the client certificate.

#### \[h2\]keyPassword

char\* Rcp\_ClientCertificate::keyPassword

**Description**

Password of the private key of the client certificate.

#### \[h2\]type

[Rcp\_CertType](../../../modules/remotecommunication/document.md#ga4f79c1d41b9c586d99f1c22ed81b9aee) Rcp\_ClientCertificate::type

**Description**

Client certificate type.
