# Rcp\_DnsRule

#### Overview

DNS rule configuration.

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

[Rcp\_DnsRuleType](../../../modules/remotecommunication/document.md#ga995c92778c5b31c9b4b586c737cfdd3c) [type](#aaeb277a1dfd6466a972da818b6967203)

 | 

Data type used in the union structure.

 |
| 

union {

 | 

Union structure. The **type** variable defines the data type used in **data**.

 |
| 

[Rcp\_DnsServers](../rcp-dnsservers/document.md) \* [dnsServers](#a652a56e711427feec1cc98d291958d8e)

 | 

**dnsServers**: DNS server.

 |
| 

[Rcp\_StaticDnsRule](../rcp-staticdnsrule/document.md) \* [staticDnsRule](#a3a84de8e04f9875303db8047fe7461c5)

 | 

**staticDnsRule**: static DNS rule.

 |
| 

[Rcp\_DynamicDnsRuleFunction](../../../modules/remotecommunication/document.md#gad0ace0c83dd20972b34ff1538700eab3) [dynamicDnsRule](#a6609c6f2fb05f16974b745b6738d1448)

 | 

**dynamicDnsRule**: dynamic DNS rule.

 |
| 

} **data**

 | 

The **type** variable defines the data type used in **data**.

 |

#### Member Variable Description

#### \[h2\]dnsServers

[Rcp\_DnsServers](../rcp-dnsservers/document.md)\* Rcp\_DnsRule::dnsServers

**Description**

DNS server.

#### \[h2\]dynamicDnsRule

[Rcp\_DynamicDnsRuleFunction](../../../modules/remotecommunication/document.md#gad0ace0c83dd20972b34ff1538700eab3) Rcp\_DnsRule::dynamicDnsRule

**Description**

Dynamic DNS rule.

#### \[h2\]staticDnsRule

[Rcp\_StaticDnsRule](../rcp-staticdnsrule/document.md)\* Rcp\_DnsRule::staticDnsRule

**Description**

Static DNS rule.

#### \[h2\]type

[Rcp\_DnsRuleType](../../../modules/remotecommunication/document.md#ga995c92778c5b31c9b4b586c737cfdd3c) Rcp\_DnsRule::type

**Description**

Data type used in the union structure.
