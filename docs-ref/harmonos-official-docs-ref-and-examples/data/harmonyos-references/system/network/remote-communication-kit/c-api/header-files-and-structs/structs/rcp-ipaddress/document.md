# Rcp\_IpAddress

#### Overview

IP address group used by the static DNS rule [Rcp\_StaticDnsRuleItem](../rcp-staticdnsruleitem/document.md).

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

char [ipAddress](#a3f54f15797c4c306245e1d5bb282f300) \[[RCP\_IP\_MAX\_LEN](../../../modules/remotecommunication/document.md#gaedd78171e1671e9ec89b59ecf6e96730)\]

 | 

IP address.

 |
| 

struct [Rcp\_IpAddress](#) \* [next](#a73eede3d8fd7459aac9ef1d03512e276)

 | 

Pointer to the next [Rcp\_IpAddress](#) in the data chain.

 |

#### Member Variable Description

#### \[h2\]ipAddress

char Rcp\_IpAddress::ipAddress\[[RCP\_IP\_MAX\_LEN](../../../modules/remotecommunication/document.md#gaedd78171e1671e9ec89b59ecf6e96730)\]

**Description**

IP address.

#### \[h2\]next

struct [Rcp\_IpAddress](#)\* Rcp\_IpAddress::next

**Description**

Pointer to the next [Rcp\_IpAddress](#) in the data chain.
