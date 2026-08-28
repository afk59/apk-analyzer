# Rcp\_IpAndPort

#### Overview

IP address and port number of a DNS server, which will be used in [Rcp\_DnsServers](../rcp-dnsservers/document.md).

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

char [ip](#ab94eb927a982d2e062cbb4266d1f5425) \[[RCP\_IP\_MAX\_LEN](../../../modules/remotecommunication/document.md#gaedd78171e1671e9ec89b59ecf6e96730)\]

 | 

IPv4 or IPv6 address.

 |
| 

uint16\_t [port](#acde1a98de31e0b6bcc636efd60bda511)

 | 

Port number. Value range: \[0, 65535\]

 |

#### Member Variable Description

#### \[h2\]ip

char Rcp\_IpAndPort::ip\[[RCP\_IP\_MAX\_LEN](../../../modules/remotecommunication/document.md#gaedd78171e1671e9ec89b59ecf6e96730)\]

**Description**

IPv4 or IPv6 address.

#### \[h2\]port

uint16\_t Rcp\_IpAndPort::port

**Description**

Port number. Value range: \[0, 65535\]
