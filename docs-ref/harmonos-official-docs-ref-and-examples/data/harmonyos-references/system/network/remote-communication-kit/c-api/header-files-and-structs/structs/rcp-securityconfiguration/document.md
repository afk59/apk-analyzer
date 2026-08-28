# Rcp\_SecurityConfiguration

#### Overview

Request security configuration.

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

[Rcp\_RemoteValidationType](../../../modules/remotecommunication/document.md#gaf9356aea6a8c2e447efe3cf7fa889b87) [remoteValidationType](#a2b5f2905c3e2f904ec9b2820ae39f367)

 | 

Remote end authentication method.

 |
| 

[Rcp\_CertificateAuthority](../rcp-certificateauthority/document.md) [certificateAuthority](#a341651044da2a76bbb5eb9126b49b709)

 | 

CA used to verify the identity of a remote server. The default value is **system**, indicating that the system CA is used to verify the identity of a remote server.

 |
| 

[Rcp\_ClientCertificate](../rcp-clientcertificate/document.md) [certificate](#aed7e691dbb64dcfbd4935eced4099de6)

 | 

Client certificate sent to a remote server, which will be used by the server to verify the identity of the client.

 |
| 

[Rcp\_ServerAuthentication](../rcp-serverauthentication/document.md) [serverAuthentication](#a9e6d74aa37d2118852bf780075d466c0)

 | 

Server identity verification configuration. By default, identity verification is not performed.

 |

#### Member Variable Description

#### \[h2\]certificate

[Rcp\_ClientCertificate](../rcp-clientcertificate/document.md) Rcp\_SecurityConfiguration::certificate

**Description**

Client certificate sent to a remote server, which will be used by the server to verify the identity of the client.

#### \[h2\]certificateAuthority

[Rcp\_CertificateAuthority](../rcp-certificateauthority/document.md) Rcp\_SecurityConfiguration::certificateAuthority

**Description**

CA used to verify the identity of a remote server. The default value is **system**, indicating that the system CA is used to verify the identity of a remote server.

#### \[h2\]remoteValidationType

[Rcp\_RemoteValidationType](../../../modules/remotecommunication/document.md#gaf9356aea6a8c2e447efe3cf7fa889b87) Rcp\_SecurityConfiguration::remoteValidationType

**Description**

Remote end authentication method.

#### \[h2\]serverAuthentication

[Rcp\_ServerAuthentication](../rcp-serverauthentication/document.md) Rcp\_SecurityConfiguration::serverAuthentication

**Description**

Server identity verification configuration. By default, identity verification is not performed.
