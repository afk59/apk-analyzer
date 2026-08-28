# net\_connection\_type.h

#### Overview

Provides the C APIs of the network connection module for network management.

**File to include**: <network/netmanager/net\_connection\_type.h>

**Library**: libnet\_connection.so

**System capability**: SystemCapability.Communication.NetManager.Core

**Since**: 11

**Related module**: [NetConnection](../../modules/netconnection/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [NetConn\_NetHandle](../../structs/netconn-nethandle/document.md) | NetConn\_NetHandle | Network ID. |
| [NetConn\_NetCapabilities](../../structs/netconn-netcapabilities/document.md) | NetConn\_NetCapabilities | Network capability set. |
| [NetConn\_NetAddr](../../structs/netconn-netaddr/document.md) | NetConn\_NetAddr | Network address. |
| [NetConn\_Route](../../structs/netconn-route/document.md) | NetConn\_Route | Route configuration. |
| [NetConn\_HttpProxy](../../structs/netconn-httpproxy/document.md) | NetConn\_HttpProxy | Proxy configuration. |
| [NetConn\_ConnectionProperties](../../structs/netconn-connectionproperties/document.md) | NetConn\_ConnectionProperties | Network connection properties. |
| [NetConn\_NetHandleList](../../structs/netconn-nethandlelist/document.md) | NetConn\_NetHandleList | Network list. |
| [NetConn\_NetSpecifier](../../structs/netconn-netspecifier/document.md) | NetConn\_NetSpecifier | Network feature sets. |
| [NetConn\_NetConnCallback](../../structs/netconn-netconncallback/document.md) | NetConn\_NetConnCallback | Network status callback. |
| [NetConn\_ProbeResultInfo](../../structs/netconn-proberesultinfo/document.md) | NetConn\_ProbeResultInfo | Probe result. |
| [NetConn\_TraceRouteOption](../../structs/netconn-tracerouteoption/document.md) | NetConn\_TraceRouteOption | Network trace route options. |
| [NetConn\_TraceRouteInfo](../../structs/netconn-tracerouteinfo/document.md) | NetConn\_TraceRouteInfo | Trace route information. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [NetConn\_NetCap](#netconn_netcap) | NetConn\_NetCap | Network capability set. |
| [NetConn\_NetBearerType](#netconn_netbearertype) | NetConn\_NetBearerType | Network carrier type. |
| [NetConn\_ErrorCode](#netconn_errorcode) | NetConn\_ErrorCode | Network connection error code. |
| [NetConn\_PacketsType](#netconn_packetstype) | NetConn\_PacketsType | Trace route packet type. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| NETCONN\_MAX\_RTT\_NUM 4 | 
Length of the **rtt** array of the [NetConn\_ProbeResultInfo](../../structs/netconn-proberesultinfo/document.md) member variable.

**Since**: 11

 |
| NETCONN\_MAX\_NET\_SIZE 32 | 

Length of the **netHandles** array of the [NetConn\_NetHandleList](../../structs/netconn-nethandlelist/document.md) member variable.

**Since**: 11

 |
| NETCONN\_MAX\_BEARER\_TYPE\_SIZE 32 | 

Length of the **bearerTypes** array of the [NetConn\_NetCapabilities](../../structs/netconn-netcapabilities/document.md) member variable.

**Since**: 11

 |
| NETCONN\_MAX\_CAP\_SIZE 32 | 

Length of the **netCaps** array of the [NetConn\_NetCapabilities](../../structs/netconn-netcapabilities/document.md) member variable.

**Since**: 11

 |
| NETCONN\_MAX\_ADDR\_SIZE 32 | 

Length of the **netAddrList** and **dnsList** arrays of the [NetConn\_ConnectionProperties](../../structs/netconn-connectionproperties/document.md) member variable.

**Since**: 11

 |
| NETCONN\_MAX\_ROUTE\_SIZE 64 | 

Length of **routeList** array of [NetConn\_ConnectionProperties](../../structs/netconn-connectionproperties/document.md) member variable.

**Since**: 11

 |
| NETCONN\_MAX\_EXCLUSION\_SIZE 256 | 

Length of the **exclusionList** array of [NetConn\_HttpProxy](../../structs/netconn-httpproxy/document.md) member variable.

**Since**: 11

 |
| NETCONN\_MAX\_STR\_LEN 256 | 

Length of the **host** array of [NetConn\_HttpProxy](../../structs/netconn-httpproxy/document.md) member variable.

**Since**: 11

 |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef int (\*OH\_NetConn\_CustomDnsResolver)(const char \*host, const char \*serv,const struct addrinfo \*hint, struct addrinfo \*\*res)](#oh_netconn_customdnsresolver) | OH\_NetConn\_CustomDnsResolver | Pointer to the custom DNS resolver. |
| [typedef void (\*OH\_NetConn\_AppHttpProxyChange)(NetConn\_HttpProxy \*proxy)](#oh_netconn_apphttpproxychange) | OH\_NetConn\_AppHttpProxyChange | Callback invoked when the HTTP proxy information of the application changes. |
| [typedef void (\*OH\_NetConn\_NetworkAvailable)(NetConn\_NetHandle \*netHandle)](#oh_netconn_networkavailable) | OH\_NetConn\_NetworkAvailable | Callback invoked when the network is available. |
| [typedef void (\*OH\_NetConn\_NetCapabilitiesChange)(NetConn\_NetHandle \*netHandle,NetConn\_NetCapabilities \*netCapabilities)](#oh_netconn_netcapabilitieschange) | OH\_NetConn\_NetCapabilitiesChange | Callback invoked when the network capabilities change. |
| [typedef void (\*OH\_NetConn\_NetConnectionPropertiesChange)(NetConn\_NetHandle \*netHandle,NetConn\_ConnectionProperties \*connConnetionProperties)](#oh_netconn_netconnectionpropertieschange) | OH\_NetConn\_NetConnectionPropertiesChange | Callback invoked when network connection properties change. |
| [typedef void (\*OH\_NetConn\_NetLost)(NetConn\_NetHandle \*netHandle)](#oh_netconn_netlost) | OH\_NetConn\_NetLost | Callback invoked when the network is disconnected. |
| [typedef void (\*OH\_NetConn\_NetUnavailable)(void)](#oh_netconn_netunavailable) | OH\_NetConn\_NetUnavailable | Callback invoked when the network is unavailable. This callback is triggered when the network is not activated within the specified timeout interval. If the timeout interval is not set, this callback is not triggered. |
| [typedef void (\*OH\_NetConn\_NetBlockStatusChange)(NetConn\_NetHandle \*netHandle, bool blocked)](#oh_netconn_netblockstatuschange) | OH\_NetConn\_NetBlockStatusChange | Callback invoked when the network blocking status changes. |

#### Enum Description

#### \[h2\]NetConn\_NetCap

enum NetConn\_NetCap

**Description**

Enumerates the network capabilities.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| NETCONN\_NET\_CAPABILITY\_MMS = 0 | MMS. |
| NETCONN\_NET\_CAPABILITY\_NOT\_METERED = 11 | Non-metered network. |
| NETCONN\_NET\_CAPABILITY\_INTERNET = 12 | Internet. |
| NETCONN\_NET\_CAPABILITY\_NOT\_VPN = 15 | Non-VPN. |
| NETCONN\_NET\_CAPABILITY\_VALIDATED = 16 | Verified. |
| NETCONN\_NET\_CAPABILITY\_PORTAL = 17 | 
Portal.

**Since**: 12

 |
| NETCONN\_NET\_CAPABILITY\_CHECKING\_CONNECTIVITY = 31 | 

Connectivity check.

**Since**: 12

 |

#### \[h2\]NetConn\_NetBearerType

enum NetConn\_NetBearerType

**Description**

Enumerates the network carrier types.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| NETCONN\_BEARER\_CELLULAR = 0 | Cellular network. |
| NETCONN\_BEARER\_WIFI = 1 | Wi-Fi. |
| NETCONN\_BEARER\_BLUETOOTH = 2 | 
Bluetooth.

**Since**: 12

 |
| NETCONN\_BEARER\_ETHERNET = 3 | Ethernet. |
| NETCONN\_BEARER\_VPN = 4 | 

VPN.

**Since**: 12

 |

#### \[h2\]NetConn\_ErrorCode

enum NetConn\_ErrorCode

**Description**

Enumerates network connection error codes.

**Since**: 15

| Enum Item | Description |
| :-- | :-- |
| NETCONN\_SUCCESS = 0 | Success. |
| NETCONN\_PERMISSION\_DENIED = 201 | Missing permissions. |
| NETCONN\_PARAMETER\_ERROR = 401 | Invalid parameter. |
| NETCONN\_OPERATION\_FAILED = 2100002 | Service connection failure. |
| NETCONN\_INTERNAL\_ERROR = 2100003 | Internal error.1. Memory-related error, for example, insufficient memory, memory data copy failure, or memory request failure.2. Null pointer, for example, access to a released memory pointer. |

#### \[h2\]NetConn\_PacketsType

enum NetConn\_PacketsType

**Description**

Enumerates trace route packet types.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| NETCONN\_PACKETS\_ICMP = 0 | Internet Control Message Protocol. |
| NETCONN\_PACKETS\_UDP = 1 | User Datagram Protocol. |

#### Function Description

#### \[h2\]OH\_NetConn\_CustomDnsResolver()

typedef int (\*OH\_NetConn\_CustomDnsResolver)(const char \*host, const char \*serv,const struct addrinfo \*hint, struct addrinfo \*\*res)

**Description**

Defines the pointer to the custom DNS resolver.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*host | Host name. |
| const char \*serv | Service name. |
| const struct addrinfo \*hint | Pointer to the addrinfo structure. |
| struct addrinfo \*\*res | DNS query result, which is in the format of linked lists. |

#### \[h2\]OH\_NetConn\_AppHttpProxyChange()

typedef void (\*OH\_NetConn\_AppHttpProxyChange)(NetConn\_HttpProxy \*proxy)

**Description**

Defines the callback invoked when the HTTP proxy information of the application changes.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [NetConn\_HttpProxy](../../structs/netconn-httpproxy/document.md) \*proxy | Proxy configuration information (probably a null pointer). |

#### \[h2\]OH\_NetConn\_NetworkAvailable()

typedef void (\*OH\_NetConn\_NetworkAvailable)(NetConn\_NetHandle \*netHandle)

**Description**

Defines the callback invoked when the network is available.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [NetConn\_NetHandle](../../structs/netconn-nethandle/document.md) \*netHandle | Network handle. |

#### \[h2\]OH\_NetConn\_NetCapabilitiesChange()

typedef void (\*OH\_NetConn\_NetCapabilitiesChange)(NetConn\_NetHandle \*netHandle,NetConn\_NetCapabilities \*netCapabilities)

**Description**

Defines the callback invoked when the network capabilities change.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [NetConn\_NetHandle](../../structs/netconn-nethandle/document.md) \*netHandle | Network handle. |
| [NetConn\_NetCapabilities](../../structs/netconn-netcapabilities/document.md) \*netCapabilities | Network capability set. |

#### \[h2\]OH\_NetConn\_NetConnectionPropertiesChange()

typedef void (\*OH\_NetConn\_NetConnectionPropertiesChange)(NetConn\_NetHandle \*netHandle,NetConn\_ConnectionProperties \*connConnetionProperties)

**Description**

Defines the callback invoked when network connection properties change.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [NetConn\_NetHandle](../../structs/netconn-nethandle/document.md) \*netHandle | Network handle. |
| [NetConn\_ConnectionProperties](../../structs/netconn-connectionproperties/document.md) \*connConnetionProperties | Network connection properties. |

#### \[h2\]OH\_NetConn\_NetLost()

typedef void (\*OH\_NetConn\_NetLost)(NetConn\_NetHandle \*netHandle)

**Description**

Defines the callback invoked when the network is disconnected.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [NetConn\_NetHandle](../../structs/netconn-nethandle/document.md) \*netHandle | Network handle. |

#### \[h2\]OH\_NetConn\_NetUnavailable()

typedef void (\*OH\_NetConn\_NetUnavailable)(void)

**Description**

Defines the callback invoked when the network is unavailable. This callback is triggered when the network is not activated within the specified timeout interval. If the timeout interval is not set, this callback is not triggered.

**Since**: 12

#### \[h2\]OH\_NetConn\_NetBlockStatusChange()

typedef void (\*OH\_NetConn\_NetBlockStatusChange)(NetConn\_NetHandle \*netHandle, bool blocked)

**Description**

Defines the callback invoked when the network blocking status changes.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [NetConn\_NetHandle](../../structs/netconn-nethandle/document.md) \*netHandle | Network handle. |
| bool blocked | Whether the network is blocked. The value true indicates that the network is blocked, and the value false indicates the opposite. |
