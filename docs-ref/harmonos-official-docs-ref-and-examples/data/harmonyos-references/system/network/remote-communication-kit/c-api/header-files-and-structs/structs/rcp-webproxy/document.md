# Rcp\_WebProxy

#### Overview

Custom proxy configuration.

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

const char \* [url](#a16daba15d11690d1213ab06b6d037865)

 | 

URL of the proxy server. If the port number is not set, the port 1080 will be used.

 |
| 

[Rcp\_ProxyTunnelMode](../../../modules/remotecommunication/document.md#ga7ae11929cb19cd85be3dd97e712e2ac6) [createTunnel](#acacb9b6bb4c814b12b1aac1df60a873f)

 | 

Indicates when a proxy tunnel needs to be established.

 |
| 

[Rcp\_Exclusions](../rcp-exclusions/document.md) [exclusions](#a11817f43fef6b3e1afc3c9539f5b7808)

 | 

If [Rcp\_Request.url](../rcp-request/document.md#a39a1cc0a1ad666d8d9ad40eec4b52de7) matches a pattern defined in [Rcp\_Exclusions](../rcp-exclusions/document.md), [Rcp\_Request](../rcp-request/document.md) will not go through proxy processing.

 |
| 

[Rcp\_SecurityConfiguration](../rcp-securityconfiguration/document.md) [securityConfiguration](#acc58f45a01e990be428e5eb7d660d417)

 | 

[Rcp\_SecurityConfiguration](../rcp-securityconfiguration/document.md) in the proxy configuration.

 |

#### Member Variable Description

#### \[h2\]createTunnel

[Rcp\_ProxyTunnelMode](../../../modules/remotecommunication/document.md#ga7ae11929cb19cd85be3dd97e712e2ac6) Rcp\_WebProxy::createTunnel

**Description**

Indicates when a proxy tunnel needs to be established.

#### \[h2\]exclusions

[Rcp\_Exclusions](../rcp-exclusions/document.md) Rcp\_WebProxy::exclusions

**Description**

If [Rcp\_Request.url](../rcp-request/document.md#a39a1cc0a1ad666d8d9ad40eec4b52de7) matches a pattern defined in [Rcp\_Exclusions](../rcp-exclusions/document.md), [Rcp\_Request](../rcp-request/document.md) will not go through proxy processing.

#### \[h2\]securityConfiguration

[Rcp\_SecurityConfiguration](../rcp-securityconfiguration/document.md) Rcp\_WebProxy::securityConfiguration

**Description**

[Rcp\_SecurityConfiguration](../rcp-securityconfiguration/document.md) in the proxy configuration.

#### \[h2\]url

const char\* Rcp\_WebProxy::url

**Description**

URL of the proxy server. If the port number is not set, the port 1080 will be used.
