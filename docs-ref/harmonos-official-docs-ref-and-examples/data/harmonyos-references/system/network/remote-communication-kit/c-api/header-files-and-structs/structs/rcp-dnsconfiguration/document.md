# Rcp\_DnsConfiguration

#### Overview

DNS resolution configuration.

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

[Rcp\_DnsRule](../rcp-dnsrule/document.md) \* [dnsRules](#ab09aacb68c682d9beea100cae481eaa4)

 | 

DNS rule configuration.

 |
| 

[Rcp\_DnsOverHttps](../rcp-dnsoverhttps/document.md) [dnsOverHttps](#a7e3122dc7ea963e7864d4ff6c3f66f0f)

 | 

DOH configuration.

 |

#### Member Variable Description

#### \[h2\]dnsOverHttps

[Rcp\_DnsOverHttps](../rcp-dnsoverhttps/document.md) Rcp\_DnsConfiguration::dnsOverHttps

**Description**

DOH configuration.

#### \[h2\]dnsRules

[Rcp\_DnsRule](../rcp-dnsrule/document.md)\* Rcp\_DnsConfiguration::dnsRules

**Description**

DNS rule configuration.

[Rcp\_DnsServers](../rcp-dnsservers/document.md): A specified DNS server is preferentially used to resolve the host name.

[Rcp\_StaticDnsRule](../rcp-staticdnsrule/document.md): If the host name is matched, a specified address is used preferentially.

[Rcp\_DynamicDnsRuleFunction](../../../modules/remotecommunication/document.md#gad0ace0c83dd20972b34ff1538700eab3): The address returned in the function is used preferentially.
