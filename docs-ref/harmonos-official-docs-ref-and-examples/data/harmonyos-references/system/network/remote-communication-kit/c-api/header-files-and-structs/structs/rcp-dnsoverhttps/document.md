# Rcp\_DnsOverHttps

#### Overview

DNS over HTTPS. If this information is configured, addresses resolved by the DOH DNS server will be preferred.

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

const char \* [url](#a0fc9b58ce0b550bc7dc5b5b1bbacb69d)

 | 

URL of the DOH server.

 |
| 

bool [skipCertificatesValidation](#acb53e2ac8bdc62816a7046c8d40d6173)

 | 

Indicates whether to skip certificate verification. The default value is **false**.

 |

#### Member Variable Description

#### \[h2\]skipCertificatesValidation

bool Rcp\_DnsOverHttps::skipCertificatesValidation

**Description**

Indicates whether to skip certificate verification. The default value is **false**.

#### \[h2\]url

const char\* Rcp\_DnsOverHttps::url

**Description**

URL of the DOH server.
