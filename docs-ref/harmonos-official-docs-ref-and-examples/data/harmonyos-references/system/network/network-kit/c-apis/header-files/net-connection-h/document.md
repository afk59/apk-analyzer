# net\_connection.h

#### Overview

Provides the C APIs of the network connection module for network management.

**File to include**: <network/netmanager/net\_connection.h>

**Library**: libnet\_connection.so

**System capability**: SystemCapability.Communication.NetManager.Core

**Since**: 11

**Related module**: [NetConnection](../../modules/netconnection/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_NetConn\_HasDefaultNet(int32\_t \*hasDefaultNet)](#oh_netconn_hasdefaultnet) | Checks whether a default activated data network is available. |
| [int32\_t OH\_NetConn\_GetDefaultNet(NetConn\_NetHandle \*netHandle)](#oh_netconn_getdefaultnet) | Obtains the default activated data network. |
| [int32\_t OH\_NetConn\_IsDefaultNetMetered(int32\_t \*isMetered)](#oh_netconn_isdefaultnetmetered) | Checks whether data traffic usage on the current network is metered. |
| [int32\_t OH\_NetConn\_GetConnectionProperties(NetConn\_NetHandle \*netHandle, NetConn\_ConnectionProperties \*prop)](#oh_netconn_getconnectionproperties) | Obtains the link information of a data network. |
| [int32\_t OH\_NetConn\_GetNetCapabilities(NetConn\_NetHandle \*netHandle, NetConn\_NetCapabilities \*netCapabilities)](#oh_netconn_getnetcapabilities) | Obtains the capabilities of a data network. |
| [int32\_t OH\_NetConn\_GetDefaultHttpProxy(NetConn\_HttpProxy \*httpProxy)](#oh_netconn_getdefaulthttpproxy) | Obtains the default network proxy. |
| [int32\_t OH\_NetConn\_GetAddrInfo(char \*host, char \*serv, struct addrinfo \*hint, struct addrinfo \*\*res, int32\_t netId)](#oh_netconn_getaddrinfo) | Obtains the DNS result based on the specified **netId**. |
| [int32\_t OH\_NetConn\_FreeDnsResult(struct addrinfo \*res)](#oh_netconn_freednsresult) | Releases the DNS query result. |
| [int32\_t OH\_NetConn\_GetAllNets(NetConn\_NetHandleList \*netHandleList)](#oh_netconn_getallnets) | Obtains all activated data networks. |
| [int32\_t OHOS\_NetConn\_RegisterDnsResolver(OH\_NetConn\_CustomDnsResolver resolver)](#ohos_netconn_registerdnsresolver) | Registers a custom DNS resolver. |
| [int32\_t OHOS\_NetConn\_UnregisterDnsResolver(void)](#ohos_netconn_unregisterdnsresolver) | Unregisters a custom DNS resolver. |
| [int32\_t OH\_NetConn\_RegisterDnsResolver(OH\_NetConn\_CustomDnsResolver resolver)](#oh_netconn_registerdnsresolver) | Registers a custom DNS resolver. |
| [int32\_t OH\_NetConn\_UnregisterDnsResolver(void)](#oh_netconn_unregisterdnsresolver) | Unregisters a custom DNS resolver. |
| [int32\_t OH\_NetConn\_BindSocket(int32\_t socketFd, NetConn\_NetHandle \*netHandle)](#oh_netconn_bindsocket) | Binds a socket to the specified network. |
| [int32\_t OH\_NetConn\_SetAppHttpProxy(NetConn\_HttpProxy \*httpProxy)](#oh_netconn_setapphttpproxy) | Sets an HTTP proxy for the current application. |
| [int32\_t OH\_NetConn\_RegisterAppHttpProxyCallback(OH\_NetConn\_AppHttpProxyChange appHttpProxyChange, uint32\_t \*callbackId)](#oh_netconn_registerapphttpproxycallback) | Registers a callback for application-level HTTP proxy changes. |
| [void OH\_NetConn\_UnregisterAppHttpProxyCallback(uint32\_t callbackId)](#oh_netconn_unregisterapphttpproxycallback) | Unregisters the callback for HTTP proxy changes of the application. |
| [int32\_t OH\_NetConn\_RegisterNetConnCallback(NetConn\_NetSpecifier \*specifier, NetConn\_NetConnCallback \*netConnCallback,uint32\_t timeout, uint32\_t \*callbackId)](#oh_netconn_registernetconncallback) | Registers a callback for network status changes. |
| [int32\_t OH\_NetConn\_RegisterDefaultNetConnCallback(NetConn\_NetConnCallback \*netConnCallback, uint32\_t \*callbackId)](#oh_netconn_registerdefaultnetconncallback) | Registers a callback for status changes of the default network. |
| [int32\_t OH\_NetConn\_UnregisterNetConnCallback(uint32\_t callBackId)](#oh_netconn_unregisternetconncallback) | Unregisters the callback for network status changes. |
| [NetConn\_ErrorCode OH\_NetConn\_SetPacUrl(const char \*pacUrl)](#oh_netconn_setpacurl) | Sets the URL of the system-level proxy auto-config (PAC) script. |
| [NetConn\_ErrorCode OH\_NetConn\_GetPacUrl(char \*pacUrl)](#oh_netconn_getpacurl) | Obtains the URL of the system-level PAC script. |
| [int32\_t OH\_NetConn\_QueryProbeResult(char \*destination, int32\_t duration, NetConn\_ProbeResultInfo \*probeResultInfo)](#oh_netconn_queryproberesult) | Queries network probe results. |
| [int32\_t OH\_NetConn\_QueryTraceRoute(char \*destination, NetConn\_TraceRouteOption \*option,NetConn\_TraceRouteInfo \*traceRouteInfo)](#oh_netconn_querytraceroute) | Queries network trace route information. |

#### Function Description

#### \[h2\]OH\_NetConn\_HasDefaultNet()

int32\_t OH\_NetConn\_HasDefaultNet(int32\_t \*hasDefaultNet)

**Description**

Checks whether a default activated data network is available.

**System capability**: SystemCapability.Communication.NetManager.Core

**Required permissions**: ohos.permission.GET\_NETWORK\_INFO

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t \*hasDefaultNet | Whether there is a default network. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success. **201**: Missing permissions.

**401**: Parameter error. **2100002**: Service connection failure.

**2100003**: Internal error.

 |

#### \[h2\]OH\_NetConn\_GetDefaultNet()

int32\_t OH\_NetConn\_GetDefaultNet(NetConn\_NetHandle \*netHandle)

**Description**

Obtains the default activated data network.

**System capability**: SystemCapability.Communication.NetManager.Core

**Required permissions**: ohos.permission.GET\_NETWORK\_INFO

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [NetConn\_NetHandle](../../structs/netconn-nethandle/document.md) \*netHandle | Network ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success. **201**: Missing permissions.

**401**: Parameter error. **2100002**: Service connection failure.

**2100003**: Internal error.

 |

#### \[h2\]OH\_NetConn\_IsDefaultNetMetered()

int32\_t OH\_NetConn\_IsDefaultNetMetered(int32\_t \*isMetered)

**Description**

Checks whether metering is enabled for the default data network.

**System capability**: SystemCapability.Communication.NetManager.Core

**Required permissions**: ohos.permission.GET\_NETWORK\_INFO

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t \*isMetered | Whether metering is enabled. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success. **201**: Missing permissions.

**401**: Parameter error. **2100002**: Service connection failure.

**2100003**: Internal error.

 |

#### \[h2\]OH\_NetConn\_GetConnectionProperties()

int32\_t OH\_NetConn\_GetConnectionProperties(NetConn\_NetHandle \*netHandle, NetConn\_ConnectionProperties \*prop)

**Description**

Obtains the link information of a data network.

**System capability**: SystemCapability.Communication.NetManager.Core

**Required permissions**: ohos.permission.GET\_NETWORK\_INFO

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [NetConn\_NetHandle](../../structs/netconn-nethandle/document.md) \*netHandle | Network ID. |
| [NetConn\_ConnectionProperties](../../structs/netconn-connectionproperties/document.md) \*prop | Link information. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success. **201**: Missing permissions.

**401**: Parameter error. **2100002**: Service connection failure.

**2100003**: Internal error.

 |

#### \[h2\]OH\_NetConn\_GetNetCapabilities()

int32\_t OH\_NetConn\_GetNetCapabilities(NetConn\_NetHandle \*netHandle, NetConn\_NetCapabilities \*netCapabilities)

**Description**

Obtains the capabilities of a data network.

**System capability**: SystemCapability.Communication.NetManager.Core

**Required permissions**: ohos.permission.GET\_NETWORK\_INFO

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [NetConn\_NetHandle](../../structs/netconn-nethandle/document.md) \*netHandle | Network ID. |
| [NetConn\_NetCapabilities](../../structs/netconn-netcapabilities/document.md) \*netCapabilities | Capability set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success. **201**: Missing permissions.

**401**: Parameter error. **2100002**: Service connection failure.

**2100003**: Internal error.

 |

#### \[h2\]OH\_NetConn\_GetDefaultHttpProxy()

int32\_t OH\_NetConn\_GetDefaultHttpProxy(NetConn\_HttpProxy \*httpProxy)

**Description**

Obtains the default network proxy.

**System capability**: SystemCapability.Communication.NetManager.Core

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [NetConn\_HttpProxy](../../structs/netconn-httpproxy/document.md) \*httpProxy | Proxy configuration. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success. **201**: Missing permissions.

**401**: Parameter error. **2100002**: Service connection failure.

**2100003**: Internal error.

 |

#### \[h2\]OH\_NetConn\_GetAddrInfo()

int32\_t OH\_NetConn\_GetAddrInfo(char \*host, char \*serv, struct addrinfo \*hint, struct addrinfo \*\*res, int32\_t netId)

**Description**

Obtains the DNS result based on the specified **netId**.

**System capability**: SystemCapability.Communication.NetManager.Core

**Required permission**: ohos.permission.INTERNET

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| char \*host | Host name. |
| char \*serv | Service name. |
| struct addrinfo \*hint | Pointer to the addrinfo structure. |
| struct addrinfo \*\*res | DNS query result, which is in the format of linked lists. |
| int32\_t netId | If **netId** is set to **0**, the default **netid** is used for query. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success. **201**: Missing permissions.

**401**: Parameter error. **2100002**: Service connection failure.

**2100003**: Internal error.

 |

#### \[h2\]OH\_NetConn\_FreeDnsResult()

int32\_t OH\_NetConn\_FreeDnsResult(struct addrinfo \*res)

**Description**

Releases the DNS query result.

**System capability**: SystemCapability.Communication.NetManager.Core

**Required permission**: ohos.permission.INTERNET

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| struct addrinfo \*res | Header of the DNS query result, which is in the format of linked lists. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success. **201**: Missing permissions.

**401**: Parameter error. **2100002**: Service connection failure.

**2100003**: Internal error.

 |

#### \[h2\]OH\_NetConn\_GetAllNets()

int32\_t OH\_NetConn\_GetAllNets(NetConn\_NetHandleList \*netHandleList)

**Description**

Obtains all activated data networks.

**System capability**: SystemCapability.Communication.NetManager.Core

**Required permissions**: ohos.permission.GET\_NETWORK\_INFO

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [NetConn\_NetHandleList](../../structs/netconn-nethandlelist/document.md) \*netHandleList | Network information list. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success. **201**: Missing permissions.

**401**: Parameter error. **2100002**: Service connection failure.

**2100003**: Internal error.

 |

#### \[h2\]OHOS\_NetConn\_RegisterDnsResolver()

int32\_t OHOS\_NetConn\_RegisterDnsResolver(OH\_NetConn\_CustomDnsResolver resolver)

**Description**

Registers a custom DNS resolver.

**System capability**: SystemCapability.Communication.NetManager.Core

**Since**: 11

**Deprecated from**: 13

**Substitute**: OH\_NetConn\_RegisterDnsResolver

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NetConn\_CustomDnsResolver](../net-connection-type-h/document.md#oh_netconn_customdnsresolver) resolver | Pointer to the custom DNS resolver. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success. **401**: Parameter error.

**2100002**: Service connection failure. **2100003**: Internal error.

 |

#### \[h2\]OHOS\_NetConn\_UnregisterDnsResolver()

int32\_t OHOS\_NetConn\_UnregisterDnsResolver(void)

**Description**

Unregisters a custom DNS resolver.

**System capability**: SystemCapability.Communication.NetManager.Core

**Since**: 11

**Deprecated from**: 13

**Substitute**: OH\_NetConn\_UnregisterDnsResolver

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success.

**2100002**: Service connection failure.

**2100003**: Internal error.

 |

#### \[h2\]OH\_NetConn\_RegisterDnsResolver()

int32\_t OH\_NetConn\_RegisterDnsResolver(OH\_NetConn\_CustomDnsResolver resolver)

**Description**

Registers a custom DNS resolver.

**System capability**: SystemCapability.Communication.NetManager.Core

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NetConn\_CustomDnsResolver](../net-connection-type-h/document.md#oh_netconn_customdnsresolver) resolver | Pointer to the custom DNS resolver. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

**NETMANAGER\_EXT\_SUCCESS**: Operation success.

**NETMANAGER\_ERR\_PARAMETER\_ERROR**: Parameter error. Enter a correct parameter.

 |

#### \[h2\]OH\_NetConn\_UnregisterDnsResolver()

int32\_t OH\_NetConn\_UnregisterDnsResolver(void)

**Description**

Unregisters a custom DNS resolver.

**System capability**: SystemCapability.Communication.NetManager.Core

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success.

**2100002**: Service connection failure.

**2100003**: Internal error.

 |

#### \[h2\]OH\_NetConn\_BindSocket()

int32\_t OH\_NetConn\_BindSocket(int32\_t socketFd, NetConn\_NetHandle \*netHandle)

**Description**

Binds a socket to the specified network.

**System capability**: SystemCapability.Communication.NetManager.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t socketFd | Socket constructed by the user. |
| [NetConn\_NetHandle](../../structs/netconn-nethandle/document.md) \*netHandle | Pointer to the network handle containing the network ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success.

**401**: Parameter error.

**2100002**: Service connection failure.

**2100003**: Internal error.

 |

#### \[h2\]OH\_NetConn\_SetAppHttpProxy()

int32\_t OH\_NetConn\_SetAppHttpProxy(NetConn\_HttpProxy \*httpProxy)

**Description**

Sets an HTTP proxy for the current application.

**System capability**: SystemCapability.Communication.NetManager.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [NetConn\_HttpProxy](../../structs/netconn-httpproxy/document.md) \*httpProxy | HTTP proxy to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success.

**401**: Parameter error.

 |

#### \[h2\]OH\_NetConn\_RegisterAppHttpProxyCallback()

int32\_t OH\_NetConn\_RegisterAppHttpProxyCallback(OH\_NetConn\_AppHttpProxyChange appHttpProxyChange, uint32\_t \*callbackId)

**Description**

Registers a callback for HTTP proxy changes of the application.

**System capability**: SystemCapability.Communication.NetManager.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NetConn\_AppHttpProxyChange](../net-connection-type-h/document.md#oh_netconn_apphttpproxychange) appHttpProxyChange | Callback to register. |
| uint32\_t \*callbackId | ID of the registered callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success.

**401**: Parameter error.

 |

#### \[h2\]OH\_NetConn\_UnregisterAppHttpProxyCallback()

void OH\_NetConn\_UnregisterAppHttpProxyCallback(uint32\_t callbackId)

**Description**

Unregisters the callback for HTTP proxy changes of the application.

**System capability**: SystemCapability.Communication.NetManager.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| uint32\_t callbackId | ID of the callback to unregister. |

#### \[h2\]OH\_NetConn\_RegisterNetConnCallback()

int32\_t OH\_NetConn\_RegisterNetConnCallback(NetConn\_NetSpecifier \*specifier, NetConn\_NetConnCallback \*netConnCallback,uint32\_t timeout, uint32\_t \*callbackId)

**Description**

Registers a callback for network status changes.

**System capability**: SystemCapability.Communication.NetManager.Core

**Required permissions**: ohos.permission.GET\_NETWORK\_INFO

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| netSpecifier | Network feature set. |
| callback | Registered callbacks. |
| uint32\_t timeout | Timeout duration, in milliseconds. The value **0** indicates infinite waiting. |
| uint32\_t \*callbackId | Callback IDs. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success.

**201**: Missing permissions.

**401**: Parameter error.

**2100002**: Service connection failure.

**2100003**: Internal error.

**2101008**: Callback already registered.

**2101022**: Maximum number of requests exceeded.

 |

#### \[h2\]OH\_NetConn\_RegisterDefaultNetConnCallback()

int32\_t OH\_NetConn\_RegisterDefaultNetConnCallback(NetConn\_NetConnCallback \*netConnCallback, uint32\_t \*callbackId)

**Description**

Registers a callback for status changes of the default network.

**System capability**: SystemCapability.Communication.NetManager.Core

**Required permissions**: ohos.permission.GET\_NETWORK\_INFO

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| callback | Registered callbacks. |
| uint32\_t \*callbackId | Callback IDs. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success.

**201**: Missing permissions.

**401**: Parameter error.

**2100002**: Service connection failure.

**2100003**: Internal error.

**2101008**: Callback already registered.

**2101022**: Maximum number of requests exceeded.

 |

#### \[h2\]OH\_NetConn\_UnregisterNetConnCallback()

int32\_t OH\_NetConn\_UnregisterNetConnCallback(uint32\_t callBackId)

**Description**

Unregisters the callback for network status changes.

**System capability**: SystemCapability.Communication.NetManager.Core

**Required permissions**: ohos.permission.GET\_NETWORK\_INFO

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| uint32\_t callBackId | ID of the callback to unregister. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success.

**201**: Missing permissions.

**401**: Parameter error.

**2100002**: Service connection failure.

**2100003**: Internal error.

**2101007**: Callback not exist.

 |

#### \[h2\]OH\_NetConn\_SetPacUrl()

NetConn\_ErrorCode OH\_NetConn\_SetPacUrl(const char \*pacUrl)

**Description**

Sets the URL of the system-level Proxy Auto Config (PAC) script, for example, **[http://127.0.0.1:21998/PacProxyScript.pac](http://127.0.0.1:21998/PacProxyScript.pac)**. You can obtain the proxy information by parsing the URL.

**Required permissions**: ohos.permission.SET\_PAC\_URL

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*pacUrl | Address of the PAC script. |

**Returns**

| Type | Description |
| :-- | :-- |
| [NetConn\_ErrorCode](../net-connection-type-h/document.md#netconn_errorcode) | 
Result code defined in [NetConn\_ErrorCode](../net-connection-type-h/document.md#netconn_errorcode).

[NETCONN\_SUCCESS](../net-connection-type-h/document.md#netconn_errorcode): success.

[NETCONN\_PERMISSION\_DENIED](../net-connection-type-h/document.md#netconn_errorcode): permission denied.

[NETCONN\_PARAMETER\_ERROR](../net-connection-type-h/document.md#netconn_errorcode): parameter error.

[NETCONN\_OPERATION\_FAILED](../net-connection-type-h/document.md#netconn_errorcode): unable to connect to the service.

[NETCONN\_INTERNAL\_ERROR](../net-connection-type-h/document.md#netconn_errorcode): internal error.

 |

#### \[h2\]OH\_NetConn\_GetPacUrl()

NetConn\_ErrorCode OH\_NetConn\_GetPacUrl(char \*pacUrl)

**Description**

Obtains the URL of the system-level PAC script.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| char \*pacUrl | URL of the PAC script. |

**Returns**

| Type | Description |
| :-- | :-- |
| [NetConn\_ErrorCode](../net-connection-type-h/document.md#netconn_errorcode) | 
Result code defined in [NetConn\_ErrorCode](../net-connection-type-h/document.md#netconn_errorcode).

[NETCONN\_SUCCESS](../net-connection-type-h/document.md#netconn_errorcode): success.

[NETCONN\_PARAMETER\_ERROR](../net-connection-type-h/document.md#netconn_errorcode): parameter error.

[NETCONN\_OPERATION\_FAILED](../net-connection-type-h/document.md#netconn_errorcode): unable to connect to the service.

[NETCONN\_INTERNAL\_ERROR](../net-connection-type-h/document.md#netconn_errorcode): internal error.

 |

#### \[h2\]OH\_NetConn\_QueryProbeResult()

int32\_t OH\_NetConn\_QueryProbeResult(char \*destination, int32\_t duration, NetConn\_ProbeResultInfo \*probeResultInfo)

**Description**

Queries network probe results. If an exception (for example, network disconnection) occurs and the request fails to be sent, the API immediately returns the result without performing subsequent detection. This API involves network operations. Do not call it in the main process. Otherwise, the UI may freeze.

**System capability**: SystemCapability.Communication.NetManager.Core

**Required permission**: ohos.permission.INTERNET

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| char \*destination | Target domain name or IP address to be detected. For a domain name, the domain name is resolved to the target IP address before the detection, and then the detection is initiated. The domain name resolution time is not included in the probe duration indicated by duration. |
| int32\_t duration | Probe duration. in seconds. The detection interval is 1 second. Therefore, you can use this field to control the number of detections. |
| [NetConn\_ProbeResultInfo](../../structs/netconn-proberesultinfo/document.md) \*probeResultInfo | Packet loss rate and round-trip time (RTT). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success.

**201**: Missing permissions.

**401**: Parameter error.

**2100003**: Internal error.

 |

#### \[h2\]OH\_NetConn\_QueryTraceRoute()

int32\_t OH\_NetConn\_QueryTraceRoute(char \*destination, NetConn\_TraceRouteOption \*option,NetConn\_TraceRouteInfo \*traceRouteInfo)

**Description**

Queries network trace route information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/koXf2s3LTyyX7vBrd69Aag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062347Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0DF3B0175D9ECAB11609EF14DA46717EDF2A0B62848DB896D472C1248BAB6CAD)

To call this API, the app needs to apply for the precise location permission. According to [Applying for Location Permissions (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/location-permission-guidelines), the caller needs to apply for both ohos.permission.APPROXIMATELY\_LOCATION and ohos.permission.LOCATION.

**Required permissions**: ohos.permission.INTERNET, ohos.permission.LOCATION, and ohos.permission.ACCESS\_NET\_TRACE\_INFO

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| char \*destination | Destination address. |
| [NetConn\_TraceRouteOption](../../structs/netconn-tracerouteoption/document.md) \*option | Route options. |
| [NetConn\_TraceRouteInfo](../../structs/netconn-tracerouteinfo/document.md) \*traceRouteInfo | Route result. An array pointer needs to be passed. The array size indicates the number of route hops, which is **30** by default. If you customize the number of hops, ensure that the array size is the same as the value of **maxJumpNumber** in the **option** field. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success.

**201**: Missing permissions.

 |
