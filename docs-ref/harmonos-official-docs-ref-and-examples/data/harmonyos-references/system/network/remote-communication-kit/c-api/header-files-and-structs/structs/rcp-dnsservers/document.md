# Rcp\_DnsServers

#### Overview

DNS server. which is one of the types defined in [Rcp\_DnsConfiguration.dnsRules](../rcp-dnsconfiguration/document.md#ab09aacb68c682d9beea100cae481eaa4).

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

[Rcp\_IpAndPort](../rcp-ipandport/document.md) [ipAndPort](#a4cd8b8fb177386081b28758bb0b2f97c)

 | 

IP address and port number.

 |
| 

struct [Rcp\_DnsServers](#) \* [next](#a89103c531bba6cd8cf60fd5d30dba8ef)

 | 

Pointer to the next [Rcp\_DnsServers](#) in the data chain.

 |

#### Member Variable Description

#### \[h2\]ipAndPort

[Rcp\_IpAndPort](../rcp-ipandport/document.md) Rcp\_DnsServers::ipAndPort

**Description**

IP address and port number.

#### \[h2\]next

struct [Rcp\_DnsServers](#)\* Rcp\_DnsServers::next

**Description**

Pointer to the next [Rcp\_DnsServers](#) in the data chain.
