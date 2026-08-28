# Rcp\_StaticDnsRuleItem

#### Overview

Description about a single static DNS rule.

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

char [host](#a1d3b3f7dce4d6bc4cca968d9c039d4f0) \[[RCP\_HOST\_MAX\_LEN](../../../modules/remotecommunication/document.md#gaf8dd4d8c5c99712c29f29211ad2a76ae)\]

 | 

Host name.

 |
| 

uint16\_t [port](#a1171cd3cf4b10f590075fc44b62a6329)

 | 

Port number. Value range: \[0, 65535\]

 |
| 

[Rcp\_IpAddress](../rcp-ipaddress/document.md) \* [ipAddresses](#a1e201db9dd01adb4c6790dea4fd8b572)

 | 

IP address matching [Rcp\_StaticDnsRuleItem.host](#a1d3b3f7dce4d6bc4cca968d9c039d4f0).

 |

#### Member Variable Description

#### \[h2\]host

char Rcp\_StaticDnsRuleItem::host\[[RCP\_HOST\_MAX\_LEN](../../../modules/remotecommunication/document.md#gaf8dd4d8c5c99712c29f29211ad2a76ae)\]

**Description**

Host name.

#### \[h2\]ipAddresses

[Rcp\_IpAddress](../rcp-ipaddress/document.md)\* Rcp\_StaticDnsRuleItem::ipAddresses

**Description**

IP address matching [Rcp\_StaticDnsRuleItem.host](#a1d3b3f7dce4d6bc4cca968d9c039d4f0).

#### \[h2\]port

uint16\_t Rcp\_StaticDnsRuleItem::port

**Description**

Port number. Value range: \[0, 65535\]
