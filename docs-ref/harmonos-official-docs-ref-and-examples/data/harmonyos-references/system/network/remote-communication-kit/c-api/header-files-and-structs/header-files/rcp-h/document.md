# rcp.h

#### Overview

Declares the APIs used to access Remote Communication, and defines basic functions, structs, and constants.

**Library**: librcp\_c.so

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Related module**: [RemoteCommunication](../../../modules/remotecommunication/document.md)

#### Summary

#### \[h2\]Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [Rcp\_Buffer](../../structs/rcp-buffer/document.md)

 | 

Text storage struct.

 |
| 

struct [Rcp\_ContentOrPathOrCallback](../../structs/rcp-contentorpathorcallback/document.md)

 | 

Simple form data field value used in [Rcp\_FormFieldFileValue](../../structs/rcp-formfieldfilevalue/document.md).

 |
| 

struct [Rcp\_FormFieldFileValue](../../structs/rcp-formfieldfilevalue/document.md)

 | 

Form field file value.

 |
| 

struct [Rcp\_FormFieldValue](../../structs/rcp-formfieldvalue/document.md)

 | 

Simple form data field value. For details, please refer to [Rcp\_Form](../../../modules/remotecommunication/document.md#ga40787f67faf4ea7111e4cda03f3f16be) and [Rcp\_MultipartFormFieldValue](../../structs/rcp-multipartformfieldvalue/document.md).

 |
| 

struct [Rcp\_MultipartFormFieldValue](../../structs/rcp-multipartformfieldvalue/document.md)

 | 

Multi-part form field value, which will be used in [Rcp\_MultipartForm](../../../modules/remotecommunication/document.md#ga9f974771548d3ed2054aba0e7506fef9).

 |
| 

struct [Rcp\_RequestContent](../../structs/rcp-requestcontent/document.md)

 | 

Request content.

 |
| 

struct [Rcp\_HeaderValue](../../structs/rcp-headervalue/document.md)

 | 

Value type of a mapped value in a request or response header.

 |
| 

struct [Rcp\_HeaderEntry](../../structs/rcp-headerentry/document.md)

 | 

All key-value pairs in the request or response header.

 |
| 

struct [Rcp\_Credential](../../structs/rcp-credential/document.md)

 | 

Credential, required by some servers or proxy servers.

 |
| 

struct [Rcp\_ServerAuthentication](../../structs/rcp-serverauthentication/document.md)

 | 

Server identity verification information.

 |
| 

struct [Rcp\_Urls](../../structs/rcp-urls/document.md)

 | 

URL, which is used to determine whether a host is using a proxy.

 |
| 

struct [Rcp\_Exclusions](../../structs/rcp-exclusions/document.md)

 | 

URLs excluded from proxy processing.

 |
| 

struct [Rcp\_CertificateAuthority](../../structs/rcp-certificateauthority/document.md)

 | 

CA used to verify the identity of a remote server.

 |
| 

struct [Rcp\_ClientCertificate](../../structs/rcp-clientcertificate/document.md)

 | 

Client certificate sent to a remote server, which will be used by the server to verify the identity of the client.

 |
| 

struct [Rcp\_SecurityConfiguration](../../structs/rcp-securityconfiguration/document.md)

 | 

Request security configuration.

 |
| 

struct [Rcp\_WebProxy](../../structs/rcp-webproxy/document.md)

 | 

Custom proxy configuration.

 |
| 

struct [Rcp\_IpAndPort](../../structs/rcp-ipandport/document.md)

 | 

IP address and port number of a DNS server, which will be used in [Rcp\_DnsServers](../../structs/rcp-dnsservers/document.md).

 |
| 

struct [Rcp\_DnsServers](../../structs/rcp-dnsservers/document.md)

 | 

DNS server, which is one of the types defined in [Rcp\_DnsConfiguration.dnsRules](../../structs/rcp-dnsconfiguration/document.md#ab09aacb68c682d9beea100cae481eaa4).

 |
| 

struct [Rcp\_IpAddress](../../structs/rcp-ipaddress/document.md)

 | 

IP address group used by the static DNS rule [Rcp\_StaticDnsRuleItem](../../structs/rcp-staticdnsruleitem/document.md).

 |
| 

struct [Rcp\_StaticDnsRuleItem](../../structs/rcp-staticdnsruleitem/document.md)

 | 

Description about a single static DNS rule.

 |
| 

struct [Rcp\_StaticDnsRule](../../structs/rcp-staticdnsrule/document.md)

 | 

Static DNS rule.

 |
| 

struct [Rcp\_DnsRule](../../structs/rcp-dnsrule/document.md)

 | 

DNS rule configuration.

 |
| 

struct [Rcp\_OnDataReceiveCallback](../../structs/rcp-ondatareceivecallback/document.md)

 | 

Callback triggered upon data receiving events, which is configured in [Rcp\_EventsHandler](../../structs/rcp-eventshandler/document.md).

 |
| 

struct [Rcp\_OnProgressCallback](../../structs/rcp-onprogresscallback/document.md)

 | 

Callback triggered upon data transmission events, which is configured in [Rcp\_EventsHandler](../../structs/rcp-eventshandler/document.md).

 |
| 

struct [Rcp\_OnHeaderReceiveCallback](../../structs/rcp-onheaderreceivecallback/document.md)

 | 

Callback triggered upon header receiving events, which is configured in [Rcp\_EventsHandler](../../structs/rcp-eventshandler/document.md).

 |
| 

struct [Rcp\_OnVoidCallback](../../structs/rcp-onvoidcallback/document.md)

 | 

Callback triggered upon transmigration ending or cancellation events, which is configured in [Rcp\_EventsHandler](../../structs/rcp-eventshandler/document.md).

 |
| 

struct [Rcp\_EventsHandler](../../structs/rcp-eventshandler/document.md)

 | 

Callback function for listening on various HTTP events.

 |
| 

struct [Rcp\_Timeout](../../structs/rcp-timeout/document.md)

 | 

Request timeout configuration.

 |
| 

struct [Rcp\_DnsOverHttps](../../structs/rcp-dnsoverhttps/document.md)

 | 

DNS over HTTPS. If this information is configured, addresses resolved by the DOH DNS server will be preferred.

 |
| 

struct [Rcp\_TransferConfiguration](../../structs/rcp-transferconfiguration/document.md)

 | 

Transmission configuration.

 |
| 

struct [Rcp\_InfoToCollect](../../structs/rcp-infotocollect/document.md)

 | 

Request processing events to be collected. You can check the response object for collected events.

 |
| 

struct [Rcp\_TracingConfiguration](../../structs/rcp-tracingconfiguration/document.md)

 | 

Request tracing configuration.

 |
| 

struct [Rcp\_ProxyConfiguration](../../structs/rcp-proxyconfiguration/document.md)

 | 

Proxy configuration.

 |
| 

struct [Rcp\_DnsConfiguration](../../structs/rcp-dnsconfiguration/document.md)

 | 

DNS resolution configuration.

 |
| 

struct [Rcp\_Configuration](../../structs/rcp-configuration/document.md)

 | 

Request configuration.

 |
| 

struct [Rcp\_TransferRange](../../structs/rcp-transferrange/document.md)

 | 

HTTP transmission range. This configuration will be converted into the HTTP Range header. An HTTP request with such a header requires the server to return only a part of the HTTP response.

 |
| 

struct [Rcp\_Request](../../structs/rcp-request/document.md)

 | 

Network request.

 |
| 

struct [Rcp\_RequestCookieEntry](../../structs/rcp-requestcookieentry/document.md)

 | 

All cookie key-value pairs in the request.

 |
| 

struct [Rcp\_DebugInfo](../../structs/rcp-debuginfo/document.md)

 | 

Structure of the debugging information stored in [Rcp\_Response](../../structs/rcp-response/document.md).

 |
| 

struct [Rcp\_CookieAttributeEntry](../../structs/rcp-cookieattributeentry/document.md)

 | 

Response cookie attribute entry.

 |
| 

struct [Rcp\_ResponseCookies](../../structs/rcp-responsecookies/document.md)

 | 

Response cookies.

 |
| 

struct [Rcp\_TimeInfo](../../structs/rcp-timeinfo/document.md)

 | 

Response timer information.

 |
| 

struct [Rcp\_ResponseCallbackObject](../../structs/rcp-responsecallbackobject/document.md)

 | 

Response callback struct.

 |
| 

struct [Rcp\_Response](../../structs/rcp-response/document.md)

 | 

Response to a network request.

 |
| 

struct [Rcp\_Interceptor](../../structs/rcp-interceptor/document.md)

 | 

Asynchronous interceptor.

 |
| 

struct [Rcp\_SyncInterceptor](../../structs/rcp-syncinterceptor/document.md)

 | 

Synchronous interceptor.

 |
| 

struct [Rcp\_InterceptorArray](../../structs/rcp-interceptorarray/document.md)

 | 

Asynchronous interceptor array.

 |
| 

struct [Rcp\_SyncInterceptorArray](../../structs/rcp-syncinterceptorarray/document.md)

 | 

Synchronous interceptor array.

 |
| 

struct [Rcp\_SessionListener](../../structs/rcp-sessionlistener/document.md)

 | 

Callback function for listening on session closing or cancellation events.

 |
| 

struct [Rcp\_ConnectionConfiguration](../../structs/rcp-connectionconfiguration/document.md)

 | 

Connection configuration.

 |
| 

struct [Rcp\_SessionConfiguration](../../structs/rcp-sessionconfiguration/document.md)

 | 

Session configuration.

 |
| 

struct [Rcp\_OnBinaryReceiveCallback](../../structs/rcp-onbinaryreceivecallback/document.md)

 | 

Callback triggered when a response is received, which supports binary data reception. You can call [HMS\_Rcp\_SetRequestOnBinaryDataRecvCallback](../../../modules/remotecommunication/document.md#section207321113884) to set the callback for a request.

 |
| 

struct [Rcp\_OnStatusCodeReceiveCallback](../../structs/rcp-onstatuscodereceivecallback/document.md)

 | 

Callback triggered when a response status code is received. You can call [HMS\_Rcp\_SetRequestOnStatusCodeReceiveCallback](../../../modules/remotecommunication/document.md#section10194153116201) to set the callback for a request.

 |

#### \[h2\]Macro Definition

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[RCP\_MAX\_REQUEST\_ID\_LEN](../../../modules/remotecommunication/document.md#ga34b7468983f894581c9e908295c6d92e) 32

 | 

Maximum length of a request ID.

 |
| 

[RCP\_MAX\_CONTENT\_TYPE\_LEN](../../../modules/remotecommunication/document.md#ga994193494eac9591a85c49f1e3200930) 64

 | 

Maximum length of the content type.

 |
| 

[RCP\_MAX\_FILENAME\_LEN](../../../modules/remotecommunication/document.md#gaef0f15d9c2cacf9df70ba148cfff171b) 128

 | 

Maximum length of a file name.

 |
| 

[RCP\_MAX\_PATH\_LEN](../../../modules/remotecommunication/document.md#ga3dac667ae8b6fa64f2fede1e77804e12) 128

 | 

Maximum path length.

 |
| 

[RCP\_METHOD\_GET](../../../modules/remotecommunication/document.md#ga2f2cc4bec6023047b63a1b3aaca7e8ff) "GET"

 | 

HTTP GET method.

 |
| 

[RCP\_METHOD\_HEAD](../../../modules/remotecommunication/document.md#ga01f80464137185de1b1c9d4a84a20328) "HEAD"

 | 

HTTP HEAD method.

 |
| 

[RCP\_METHOD\_OPTIONS](../../../modules/remotecommunication/document.md#gac3a9a3250402418f4a59875e5e98cfc7) "OPTIONS"

 | 

HTTP OPTIONS method.

 |
| 

[RCP\_METHOD\_TRACE](../../../modules/remotecommunication/document.md#ga3676dd73393ff05d3c487140ac5c3a88) "TRACE"

 | 

HTTP TRACE method.

 |
| 

[RCP\_METHOD\_DELETE](../../../modules/remotecommunication/document.md#ga865bfb4de54f47a05b3adc17eccfccf7) "DELETE"

 | 

HTTP DELETE method.

 |
| 

[RCP\_METHOD\_POST](../../../modules/remotecommunication/document.md#ga5c3de5092bf8c0b6556ccdf35b433b85) "POST"

 | 

HTTP POST method.

 |
| 

[RCP\_METHOD\_PUT](../../../modules/remotecommunication/document.md#gada60d0d101fce537636d5d38ebdcd5b1) "PUT"

 | 

HTTP PUT method.

 |
| 

[RCP\_METHOD\_PATCH](../../../modules/remotecommunication/document.md#ga34617da18b0341c7111d0853834a12a1) "PATCH"

 | 

HTTP PATCH method.

 |
| 

[RCP\_IP\_MAX\_LEN](../../../modules/remotecommunication/document.md#gaedd78171e1671e9ec89b59ecf6e96730) 40

 | 

Maximum length of an IP address.

 |
| 

[RCP\_HOST\_MAX\_LEN](../../../modules/remotecommunication/document.md#gaf8dd4d8c5c99712c29f29211ad2a76ae) 256

 | 

Maximum length of a host name.

 |

#### \[h2\]Types

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef enum [Rcp\_FormValueType](../../../modules/remotecommunication/document.md#ga9d851389347a39bd4bb849ac31cfa478) [Rcp\_FormValueType](../../../modules/remotecommunication/document.md#gaa1493419cc430c47cef7ec7ddfb74220)

 | 

Form value type.

 |
| 

typedef int(\* [Rcp\_GetDataCallback](../../../modules/remotecommunication/document.md#gac0ac73f33252239ff47a648fe3aa6bd5)) (char \*out, uint32\_t size)

 | 

Data obtained through a callback function. This callback is used when the API needs to send the next part of the data to the server.

 |
| 

typedef enum [Rcp\_ContentOrPathOrCallbackType](../../../modules/remotecommunication/document.md#gaa5a592f4e68a1dd43f5f41e95199a5e4) [Rcp\_ContentOrPathOrCallbackType](../../../modules/remotecommunication/document.md#gaa0382cf2e96821ed741ad9f99dd9e37a)

 | 

Content, path, or callback type, which is used to distinguish the data used in [Rcp\_ContentOrPathOrCallback](../../structs/rcp-contentorpathorcallback/document.md).

 |
| 

typedef struct [Rcp\_Buffer](../../structs/rcp-buffer/document.md) [Rcp\_Buffer](../../../modules/remotecommunication/document.md#ga74d7d9dd56fabaa773cf1659c2d2eace)

 | 

Text storage struct.

 |
| 

typedef struct [Rcp\_ContentOrPathOrCallback](../../structs/rcp-contentorpathorcallback/document.md) [Rcp\_ContentOrPathOrCallback](../../../modules/remotecommunication/document.md#gaebb5b634a56751ae23ac2610e230ec72)

 | 

Simple form data field value used in [Rcp\_FormFieldFileValue](../../structs/rcp-formfieldfilevalue/document.md).

 |
| 

typedef enum [Rcp\_MultipartValueType](../../../modules/remotecommunication/document.md#ga76d003b4f9a244c9d11def4128ceeda8) [Rcp\_MultipartValueType](../../../modules/remotecommunication/document.md#gafeeacbc819f33dae11912a0c59f4a678)

 | 

Multi-part form value type, which is used to distinguish the data used in [Rcp\_MultipartFormFieldValue](../../structs/rcp-multipartformfieldvalue/document.md).

 |
| 

typedef struct [Rcp\_FormFieldFileValue](../../structs/rcp-formfieldfilevalue/document.md) [Rcp\_FormFieldFileValue](../../../modules/remotecommunication/document.md#ga774f6381467f16c39aaa2988c69ad7fd)

 | 

Form field file value.

 |
| 

typedef struct [Rcp\_FormFieldValue](../../structs/rcp-formfieldvalue/document.md) [Rcp\_FormFieldValue](../../../modules/remotecommunication/document.md#gaf68638c39567d0c7b1e9ed0f145ebc65)

 | 

Simple form data field value. For details, please refer to [Rcp\_Form](../../../modules/remotecommunication/document.md#ga40787f67faf4ea7111e4cda03f3f16be) and [Rcp\_MultipartFormFieldValue](../../structs/rcp-multipartformfieldvalue/document.md).

 |
| 

typedef struct [Rcp\_MultipartFormFieldValue](../../structs/rcp-multipartformfieldvalue/document.md) [Rcp\_MultipartFormFieldValue](../../../modules/remotecommunication/document.md#ga64c7e2addc25dd589c5f65237eded576)

 | 

Multi-part form field value, which will be used in [Rcp\_MultipartForm](../../../modules/remotecommunication/document.md#ga9f974771548d3ed2054aba0e7506fef9).

 |
| 

typedef enum [Rcp\_ContentType](../../../modules/remotecommunication/document.md#ga05daeab5ad8d265834b4a1b4e61cd8fa) [Rcp\_ContentType](../../../modules/remotecommunication/document.md#gacb1c467d93e50c5cdd7ace89f1369975)

 | 

Content type in [Rcp\_RequestContent](../../structs/rcp-requestcontent/document.md).

 |
| 

typedef struct [Rcp\_Form](../../../modules/remotecommunication/document.md#ga40787f67faf4ea7111e4cda03f3f16be) [Rcp\_Form](../../../modules/remotecommunication/document.md#ga40787f67faf4ea7111e4cda03f3f16be)

 | 

Simple form data.

 |
| 

typedef struct [Rcp\_MultipartForm](../../../modules/remotecommunication/document.md#ga9f974771548d3ed2054aba0e7506fef9) [Rcp\_MultipartForm](../../../modules/remotecommunication/document.md#ga9f974771548d3ed2054aba0e7506fef9)

 | 

Multi-part form data.

 |
| 

typedef struct [Rcp\_RequestContent](../../structs/rcp-requestcontent/document.md) [Rcp\_RequestContent](../../../modules/remotecommunication/document.md#gaaf7ad4248342bb42ae9af6eb883e7679)

 | 

Request content.

 |
| 

typedef struct [Rcp\_Headers](../../../modules/remotecommunication/document.md#gac4f343ec02dec34268e93ce746e6c982) [Rcp\_Headers](../../../modules/remotecommunication/document.md#gac4f343ec02dec34268e93ce746e6c982)

 | 

Header of a request or response.

 |
| 

typedef struct [Rcp\_HeaderValue](../../structs/rcp-headervalue/document.md) [Rcp\_HeaderValue](../../../modules/remotecommunication/document.md#gac6096559a00691522790022a9335922a)

 | 

Value type of a mapped value in a request or response header.

 |
| 

typedef struct [Rcp\_HeaderEntry](../../structs/rcp-headerentry/document.md) [Rcp\_HeaderEntry](../../../modules/remotecommunication/document.md#gae0d149375558a4b9de6058ee281a49c3)

 | 

All key-value pairs in the request or response header.

 |
| 

typedef enum [Rcp\_AuthenticationType](../../../modules/remotecommunication/document.md#gaa1b9ec2bd61b2c95492f45eb0a447bff) [Rcp\_AuthenticationType](../../../modules/remotecommunication/document.md#ga60aa25edf4cc00a574abb8ffebcb7f60)

 | 

Server identity verification type, which is an enumeration. If the type is not set, negotiation with the server is required.

 |
| 

typedef struct [Rcp\_Credential](../../structs/rcp-credential/document.md) [Rcp\_Credential](../../../modules/remotecommunication/document.md#ga15452ad2af919bfffeb3a1f723e1eb5d)

 | 

Credential, required by some servers or proxy servers.

 |
| 

typedef struct [Rcp\_ServerAuthentication](../../structs/rcp-serverauthentication/document.md) [Rcp\_ServerAuthentication](../../../modules/remotecommunication/document.md#ga9977de0042837319e439fdfe28ec6af8)

 | 

Server identity verification information.

 |
| 

typedef bool(\* [Rcp\_ExclusionFunction](../../../modules/remotecommunication/document.md#gac6517b72e4a8c0feaf864f3669d2c127)) (const char \*url)

 | 

Pointer to the function for determining whether a host uses a proxy.

 |
| 

typedef struct [Rcp\_Urls](../../structs/rcp-urls/document.md) [Rcp\_Urls](../../../modules/remotecommunication/document.md#ga4580ece64cbef2ce6cd66e0153f31721)

 | 

URL, which is used to determine whether a host is using a proxy.

 |
| 

typedef enum [Rcp\_ExclusionsValueType](../../../modules/remotecommunication/document.md#ga1f5ed8748d80bca8e803ea26d63d1ecf) [Rcp\_ExclusionsValueType](../../../modules/remotecommunication/document.md#gae691e3a52b7d410309e096d3a6083385)

 | 

Data type in [Rcp\_Exclusions](../../structs/rcp-exclusions/document.md).

 |
| 

typedef struct [Rcp\_Exclusions](../../structs/rcp-exclusions/document.md) [Rcp\_Exclusions](../../../modules/remotecommunication/document.md#gac98e0508b4e76da5550bdf49b00a28de)

 | 

URLs excluded from proxy processing.

 |
| 

typedef enum [Rcp\_CertType](../../../modules/remotecommunication/document.md#ga4f79c1d41b9c586d99f1c22ed81b9aee) [Rcp\_CertType](../../../modules/remotecommunication/document.md#ga1862154a92f9f18850df7981e4eb7835)

 | 

Client certificate type.

 |
| 

typedef struct [Rcp\_CertificateAuthority](../../structs/rcp-certificateauthority/document.md) [Rcp\_CertificateAuthority](../../../modules/remotecommunication/document.md#ga5f3dcd559a5c06922af97232ef415a25)

 | 

CA used to verify the identity of a remote server.

 |
| 

typedef struct [Rcp\_ClientCertificate](../../structs/rcp-clientcertificate/document.md) [Rcp\_ClientCertificate](../../../modules/remotecommunication/document.md#ga845e91b33e622fea75ca06bda166e5e9)

 | 

Client certificate sent to a remote server, which will be used by the server to verify the identity of the client.

 |
| 

typedef enum [Rcp\_RemoteValidationType](../../../modules/remotecommunication/document.md#gaf9356aea6a8c2e447efe3cf7fa889b87) [Rcp\_RemoteValidationType](../../../modules/remotecommunication/document.md#ga188c30a5aa5e064b2b366cfc04c901e7)

 | 

Remote server validation type.

 |
| 

typedef struct [Rcp\_SecurityConfiguration](../../structs/rcp-securityconfiguration/document.md) [Rcp\_SecurityConfiguration](../../../modules/remotecommunication/document.md#gae90019e06749ddcbc625d7b466b39d6b)

 | 

Request security configuration.

 |
| 

typedef enum [Rcp\_ProxyTunnelMode](../../../modules/remotecommunication/document.md#ga7ae11929cb19cd85be3dd97e712e2ac6) [Rcp\_ProxyTunnelMode](../../../modules/remotecommunication/document.md#ga2c01e03e43784509918e5d3641371e6b)

 | 

Indicates when a proxy tunnel needs to be established. Tunneling, or tunnel transmission, is a process where an HTTP CONNECT request is sent to a proxy server, instructing it to establish a connection to the remote host of a specified port number. Once this connection is set up, all subsequent traffic is routed through the proxy. The value **auto** indicates that tunneling is enabled only for HTTPS traffic. The value **always** indicates that tunneling is enabled for all traffic.

 |
| 

typedef struct [Rcp\_WebProxy](../../structs/rcp-webproxy/document.md) [Rcp\_WebProxy](../../../modules/remotecommunication/document.md#ga389f9fb59be18ed6ac4ae970eeb4a1a8)

 | 

Custom proxy configuration.

 |
| 

typedef struct [Rcp\_IpAndPort](../../structs/rcp-ipandport/document.md) [Rcp\_IpAndPort](../../../modules/remotecommunication/document.md#gaad7a7752372c8b74f57204678240ad56)

 | 

IP address and port number of a DNS server, which will be used in [Rcp\_DnsServers](../../structs/rcp-dnsservers/document.md).

 |
| 

typedef struct [Rcp\_DnsServers](../../structs/rcp-dnsservers/document.md) [Rcp\_DnsServers](../../../modules/remotecommunication/document.md#ga58948b274c22ba906ac5527c6b5a8a75)

 | 

DNS server, which is one of the types defined in [Rcp\_DnsConfiguration.dnsRules](../../structs/rcp-dnsconfiguration/document.md#ab09aacb68c682d9beea100cae481eaa4).

 |
| 

typedef struct [Rcp\_IpAddress](../../structs/rcp-ipaddress/document.md) [Rcp\_IpAddress](../../../modules/remotecommunication/document.md#gaeaf532cd57e6cfc944f77bd0ac9cd205)

 | 

IP address group used by the static DNS rule [Rcp\_StaticDnsRuleItem](../../structs/rcp-staticdnsruleitem/document.md).

 |
| 

typedef struct [Rcp\_StaticDnsRuleItem](../../structs/rcp-staticdnsruleitem/document.md) [Rcp\_StaticDnsRuleItem](../../../modules/remotecommunication/document.md#gad8ad9f5130bca04060b5ffad30a915e8)

 | 

Description about a single static DNS rule.

 |
| 

typedef struct [Rcp\_StaticDnsRule](../../structs/rcp-staticdnsrule/document.md) [Rcp\_StaticDnsRule](../../../modules/remotecommunication/document.md#ga2fb8b04fec14262d27e95ec33f5a8349)

 | 

Static DNS rule.

 |
| 

typedef [Rcp\_IpAddress](../../structs/rcp-ipaddress/document.md) \*(\* [Rcp\_DynamicDnsRuleFunction](../../../modules/remotecommunication/document.md#gad0ace0c83dd20972b34ff1538700eab3)) (const char \*host, uint16\_t port)

 | 

Function that can directly return an IP address based on the host name and port number. It is used for dynamic DNS resolution.

 |
| 

typedef enum [Rcp\_DnsRuleType](../../../modules/remotecommunication/document.md#ga995c92778c5b31c9b4b586c737cfdd3c) [Rcp\_DnsRuleType](../../../modules/remotecommunication/document.md#ga925086d48b97774cc082773be635e3a1)

 | 

DNS rule type in [Rcp\_DnsRule](../../structs/rcp-dnsrule/document.md).

 |
| 

typedef struct [Rcp\_DnsRule](../../structs/rcp-dnsrule/document.md) [Rcp\_DnsRule](../../../modules/remotecommunication/document.md#ga8acd52cb973f1ce65afffb719fe4026d)

 | 

DNS rule configuration.

 |
| 

typedef size\_t(\* [Rcp\_OnDataReceiveCallbackFunc](../../../modules/remotecommunication/document.md#gadc4e28c213ddc694e3c0ec76296ef5c0)) (void \*usrObject, const char \*data)

 | 

Callback function triggered when a response body is returned.

 |
| 

typedef size\_t(\* [Rcp\_OnBinaryReceiveCallbackFunc](../../../modules/remotecommunication/document.md#section1476912410533)) (void \*usrObject, [Rcp\_Buffer](../../structs/rcp-buffer/document.md) \*buffer)

 | 

Callback function triggered when a response body (binary data type) is returned.

 |
| 

typedef void (\* [Rcp\_OnStatusCodeReceiveCallbackFunc](../../../modules/remotecommunication/document.md#section1961611617339))(void \*usrObject, uint32\_t statusCode)

 | 

Callback function triggered when a response status code is returned.

 |
| 

typedef void(\* [Rcp\_OnProgressCallbackFunc](../../../modules/remotecommunication/document.md#gaaf74ce6d5578d28829955208318d3fbe)) (void \*usrObject, uint64\_t totalSize, uint64\_t transferredSize)

 | 

Callback function triggered during request/response data transmission.

 |
| 

typedef void(\* [Rcp\_OnHeaderReceiveCallbackFunc](../../../modules/remotecommunication/document.md#gae90a801a6c386c246e5005eadfe7da0a)) (void \*usrObject, [Rcp\_Headers](../../../modules/remotecommunication/document.md#gac4f343ec02dec34268e93ce746e6c982) \*headers)

 | 

Callback function triggered when all requests are received.

 |
| 

typedef void(\* [Rcp\_OnVoidCallbackFunc](../../../modules/remotecommunication/document.md#ga3d6a448e8f0bdcc2b4e70fa6ca00d475)) (void \*usrObject)

 | 

Callback function for listening on DataEnd and Canceled events of requests.

 |
| 

typedef struct [Rcp\_OnDataReceiveCallback](../../structs/rcp-ondatareceivecallback/document.md) [Rcp\_OnDataReceiveCallback](../../../modules/remotecommunication/document.md#gacd66d521a147a876e340aed45a3ed1c4)

 | 

Callback triggered upon data receiving events, which is configured in [Rcp\_EventsHandler](../../structs/rcp-eventshandler/document.md).

 |
| 

typedef struct [Rcp\_OnProgressCallback](../../structs/rcp-onprogresscallback/document.md) [Rcp\_OnProgressCallback](../../../modules/remotecommunication/document.md#gabd25a25747d1c91772677f68ec8afc67)

 | 

Callback triggered upon data transmission events, which is configured in [Rcp\_EventsHandler](../../structs/rcp-eventshandler/document.md).

 |
| 

typedef struct [Rcp\_OnHeaderReceiveCallback](../../structs/rcp-onheaderreceivecallback/document.md) [Rcp\_OnHeaderReceiveCallback](../../../modules/remotecommunication/document.md#gab23c23acd8c159dfbaf00e439a08caf4)

 | 

Callback triggered upon header receiving events, which is configured in [Rcp\_EventsHandler](../../structs/rcp-eventshandler/document.md).

 |
| 

typedef struct [Rcp\_OnVoidCallback](../../structs/rcp-onvoidcallback/document.md) [Rcp\_OnVoidCallback](../../../modules/remotecommunication/document.md#gadda85b3a46176f92d45f30d97a78494f)

 | 

Callback triggered upon transmigration ending or cancellation events, which is configured in [Rcp\_EventsHandler](../../structs/rcp-eventshandler/document.md).

 |
| 

typedef struct [Rcp\_EventsHandler](../../structs/rcp-eventshandler/document.md) [Rcp\_EventsHandler](../../../modules/remotecommunication/document.md#ga7d9b30e24c4f42e2da0938c04977b6a4)

 | 

Callback function for listening on various HTTP events.

 |
| 

typedef struct [Rcp\_Timeout](../../structs/rcp-timeout/document.md) [Rcp\_Timeout](../../../modules/remotecommunication/document.md#ga4e16d4d91f394ab2070adc42d07b16fa)

 | 

Request timeout configuration.

 |
| 

typedef struct [Rcp\_DnsOverHttps](../../structs/rcp-dnsoverhttps/document.md) [Rcp\_DnsOverHttps](../../../modules/remotecommunication/document.md#ga514d31fc0e2abc3d0138226287c35aa4)

 | 

DNS over HTTPS. If this information is configured, addresses resolved by the DOH DNS server will be preferred.

 |
| 

typedef enum [Rcp\_PathPreference](../../../modules/remotecommunication/document.md#ga9498d24addbd529f258fd6faacfd9c67) [Rcp\_PathPreference](../../../modules/remotecommunication/document.md#ga4f6c04d042df5e2835f1d771205aad24)

 | 

Request path preferences.

 |
| 

typedef struct [Rcp\_TransferConfiguration](../../structs/rcp-transferconfiguration/document.md) [Rcp\_TransferConfiguration](../../../modules/remotecommunication/document.md#ga1b92400a50ef056d4490220cf2cefbda)

 | 

Transmission configuration.

 |
| 

typedef struct [Rcp\_InfoToCollect](../../structs/rcp-infotocollect/document.md) [Rcp\_InfoToCollect](../../../modules/remotecommunication/document.md#ga571eceac21f6acbf6fb846ac5a1abd55)

 | 

Request processing events to be collected. You can check the response object for collected events.

 |
| 

typedef struct [Rcp\_TracingConfiguration](../../structs/rcp-tracingconfiguration/document.md) [Rcp\_TracingConfiguration](../../../modules/remotecommunication/document.md#ga8a0a1aa17cd22e2ac5389d55101fe4c5)

 | 

Request tracing configuration.

 |
| 

typedef enum [Rcp\_ProxyType](../../../modules/remotecommunication/document.md#gacfad61d189683cbc02c969a63e246ca1) [Rcp\_ProxyType](../../../modules/remotecommunication/document.md#ga54cfc687bda5aafc6199dfe678e3a2c9)

 | 

Proxy type, which will be used to determine which proxy configuration will be used.

 |
| 

typedef struct [Rcp\_ProxyConfiguration](../../structs/rcp-proxyconfiguration/document.md) [Rcp\_ProxyConfiguration](../../../modules/remotecommunication/document.md#gabc9a05c4bd32b7293392423797fb8e73)

 | 

Proxy configuration.

 |
| 

typedef struct [Rcp\_DnsConfiguration](../../structs/rcp-dnsconfiguration/document.md) [Rcp\_DnsConfiguration](../../../modules/remotecommunication/document.md#ga5f45694c1825bec6ceb5c7a8591d5127)

 | 

DNS resolution configuration.

 |
| 

typedef struct [Rcp\_Configuration](../../structs/rcp-configuration/document.md) [Rcp\_Configuration](../../../modules/remotecommunication/document.md#ga4ecea20272b8fe673f842e5486ba463b)

 | 

Request configuration.

 |
| 

typedef struct [Rcp\_TransferRange](../../structs/rcp-transferrange/document.md) [Rcp\_TransferRange](../../../modules/remotecommunication/document.md#gaf0e1f4ea19d1c9efa13dc794c6c6590b)

 | 

HTTP transmission range. This configuration will be converted into the HTTP Range header. An HTTP request with such a header requires the server to return only a part of the HTTP response.

 |
| 

typedef struct [Rcp\_RequestCookies](../../../modules/remotecommunication/document.md#ga44f2b679fefd37e78c43dbcba59d6d50) [Rcp\_RequestCookies](../../../modules/remotecommunication/document.md#ga44f2b679fefd37e78c43dbcba59d6d50)

 | 

Request cookies.

 |
| 

typedef struct [Rcp\_Request](../../structs/rcp-request/document.md) [Rcp\_Request](../../../modules/remotecommunication/document.md#ga98dde966841135537e05053bf4da4d5b)

 | 

Network request.

 |
| 

typedef struct [Rcp\_RequestCookieEntry](../../structs/rcp-requestcookieentry/document.md) [Rcp\_RequestCookieEntry](../../../modules/remotecommunication/document.md#gab2690d1fbefb9998606757527f1b7b15)

 | 

All cookie key-value pairs in the request.

 |
| 

typedef enum [Rcp\_StatusCode](../../../modules/remotecommunication/document.md#ga97929a5349f04300f50318f50393b93e) [Rcp\_StatusCode](../../../modules/remotecommunication/document.md#gae926416f69908e790e9bc67bb1e2d1f3)

 | 

Response status code.

 |
| 

typedef enum [Rcp\_DebugEvent](../../../modules/remotecommunication/document.md#gadff9eaa1b517bf01defd1273b2eeddbc) [Rcp\_DebugEvent](../../../modules/remotecommunication/document.md#ga79f61404bcc66d914e298c5362d73d69)

 | 

Debugging event type.

 |
| 

typedef struct [Rcp\_DebugInfo](../../structs/rcp-debuginfo/document.md) [Rcp\_DebugInfo](../../../modules/remotecommunication/document.md#ga5738cb7a4a2768ecf909a22cfba77e0f)

 | 

Structure of the debugging information stored in [Rcp\_Response](../../structs/rcp-response/document.md).

 |
| 

typedef struct [Rcp\_CookieAttributes](../../../modules/remotecommunication/document.md#ga08c7b992199bec7e5acdc50ce8ae2651) [Rcp\_CookieAttributes](../../../modules/remotecommunication/document.md#ga08c7b992199bec7e5acdc50ce8ae2651)

 | 

Cookie attribute type in [Rcp\_Response](../../structs/rcp-response/document.md).

 |
| 

typedef struct [Rcp\_CookieAttributeEntry](../../structs/rcp-cookieattributeentry/document.md) [Rcp\_CookieAttributeEntry](../../../modules/remotecommunication/document.md#gaaff95756175ea20a41b1134c6aefb45e)

 | 

Response cookie attribute entry.

 |
| 

typedef struct [Rcp\_ResponseCookies](../../structs/rcp-responsecookies/document.md) [Rcp\_ResponseCookies](../../../modules/remotecommunication/document.md#ga71bcf6497f4d94dc7bbc50adcfee081f)

 | 

Response cookies.

 |
| 

typedef struct [Rcp\_TimeInfo](../../structs/rcp-timeinfo/document.md) [Rcp\_TimeInfo](../../../modules/remotecommunication/document.md#ga0ca30b26b3aeba0a436ac9bbd41c484b)

 | 

Response timer information.

 |
| 

typedef struct [Rcp\_Response](../../structs/rcp-response/document.md) [Rcp\_Response](../../../modules/remotecommunication/document.md#gaefca0869b44c6d31f91db0b3476f7863)

 | 

Response to a network request.

 |
| 

typedef void(\* [Rcp\_ResponseCallback](../../../modules/remotecommunication/document.md#ga9403920c5b3bbe62d14816c693f5e024)) (void \*usrCtx, [Rcp\_Response](../../structs/rcp-response/document.md) \*response, uint32\_t errCode)

 | 

Pointer to the response callback function.

 |
| 

typedef struct [Rcp\_ResponseCallbackObject](../../structs/rcp-responsecallbackobject/document.md) [Rcp\_ResponseCallbackObject](../../../modules/remotecommunication/document.md#ga815137188d22749aff74afef7387860a)

 | 

Response callback struct.

 |
| 

typedef struct [Rcp\_RequestHandler](../../../modules/remotecommunication/document.md#ga5ac080855c3aaef66c58d5b5b371be2b) [Rcp\_RequestHandler](../../../modules/remotecommunication/document.md#ga5ac080855c3aaef66c58d5b5b371be2b)

 | 

Asynchronous handler associated with [Rcp\_Interceptor](../../structs/rcp-interceptor/document.md).

 |
| 

typedef struct [Rcp\_SyncRequestHandler](../../../modules/remotecommunication/document.md#ga2067d1b09b33afa0b8237a049687e9ea) [Rcp\_SyncRequestHandler](../../../modules/remotecommunication/document.md#ga2067d1b09b33afa0b8237a049687e9ea)

 | 

Synchronous handler associated with [Rcp\_SyncInterceptor](../../structs/rcp-syncinterceptor/document.md).

 |
| 

typedef struct [Rcp\_Interceptor](../../structs/rcp-interceptor/document.md) [Rcp\_Interceptor](../../../modules/remotecommunication/document.md#ga574aa47231df9c57b58c3aff0736c5e5)

 | 

Asynchronous interceptor.

 |
| 

typedef struct [Rcp\_SyncInterceptor](../../structs/rcp-syncinterceptor/document.md) [Rcp\_SyncInterceptor](../../../modules/remotecommunication/document.md#ga43a43cc8e864121ada235f484ffefece)

 | 

Synchronous interceptor.

 |
| 

typedef struct [Rcp\_InterceptorArray](../../structs/rcp-interceptorarray/document.md) [Rcp\_InterceptorArray](../../../modules/remotecommunication/document.md#ga58ca95fc666a9a5694e92da1ce9b5c0b)

 | 

Asynchronous interceptor array.

 |
| 

typedef struct [Rcp\_SyncInterceptorArray](../../structs/rcp-syncinterceptorarray/document.md) [Rcp\_SyncInterceptorArray](../../../modules/remotecommunication/document.md#ga8612d3521508093ed36be72b7f5cb373)

 | 

Synchronous interceptor array.

 |
| 

typedef enum [Rcp\_SessionType](../../../modules/remotecommunication/document.md#ga4fa3aa6821b16425c260d837deace956) [Rcp\_SessionType](../../../modules/remotecommunication/document.md#ga5254a5bead7a2562f9593d33018f460c)

 | 

Session type.

 |
| 

typedef struct [Rcp\_Session](../../../modules/remotecommunication/document.md#ga4f3a7d39c18fe6fdf01c52759213ddcd) [Rcp\_Session](../../../modules/remotecommunication/document.md#ga4f3a7d39c18fe6fdf01c52759213ddcd)

 | 

Session.

 |
| 

typedef struct [Rcp\_SessionListener](../../structs/rcp-sessionlistener/document.md) [Rcp\_SessionListener](../../../modules/remotecommunication/document.md#ga43cd805167e33b051ccbe940d75f5966)

 | 

Callback function for listening on session closing or cancellation events.

 |
| 

typedef struct [Rcp\_ConnectionConfiguration](../../structs/rcp-connectionconfiguration/document.md) [Rcp\_ConnectionConfiguration](../../../modules/remotecommunication/document.md#gac814a198390d0e7a094b241542c9139d)

 | 

Connection configuration.

 |
| 

typedef struct [Rcp\_SessionConfiguration](../../structs/rcp-sessionconfiguration/document.md) [Rcp\_SessionConfiguration](../../../modules/remotecommunication/document.md#ga2d8aab48bdb45313f589dbd8ec00e36c)

 | 

Session configuration.

 |
| 

typedef struct [Rcp\_OnBinaryReceiveCallback](../../structs/rcp-onbinaryreceivecallback/document.md) [Rcp\_OnBinaryReceiveCallback](../../structs/rcp-onbinaryreceivecallback/document.md)

 | 

Callback function for receiving binary data in a response.

 |
| 

typedef size\_t(\* [Rcp\_OnBinaryReceiveCallbackFunc](../../../modules/remotecommunication/document.md#section1476912410533)) (void \*usrObject, [Rcp\_Buffer](../../structs/rcp-buffer/document.md) \*buffer)

 | 

Pointer to the callback function for receiving binary data.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[Rcp\_FormValueType](../../../modules/remotecommunication/document.md#ga9d851389347a39bd4bb849ac31cfa478) {

RCP\_FORM\_VALUE\_TYPE\_INT32, RCP\_FORM\_VALUE\_TYPE\_INT64, RCP\_FORM\_VALUE\_TYPE\_BOOL, RCP\_FORM\_VALUE\_TYPE\_STRING,

RCP\_FORM\_VALUE\_TYPE\_DOUBLE

}

 | 

Form value type.

 |
| 

[Rcp\_ContentOrPathOrCallbackType](../../../modules/remotecommunication/document.md#gaa5a592f4e68a1dd43f5f41e95199a5e4) { RCP\_FILE\_VALUE\_TYPE\_CONTENT, RCP\_FILE\_VALUE\_TYPE\_PATH, RCP\_FILE\_VALUE\_TYPE\_CALLBACK}

 | 

Content, path, or callback type, which is used to distinguish the data used in [Rcp\_ContentOrPathOrCallback](../../structs/rcp-contentorpathorcallback/document.md).

 |
| 

[Rcp\_MultipartValueType](../../../modules/remotecommunication/document.md#ga76d003b4f9a244c9d11def4128ceeda8) { RCP\_TYPE\_FORM\_FIELD\_VALUE, RCP\_TYPE\_FORM\_FIELD\_FILE\_VALUE }

 | 

Multi-part form value type, which is used to distinguish the data used in [Rcp\_MultipartFormFieldValue](../../structs/rcp-multipartformfieldvalue/document.md).

 |
| 

[Rcp\_ContentType](../../../modules/remotecommunication/document.md#ga05daeab5ad8d265834b4a1b4e61cd8fa) { RCP\_CONTENT\_TYPE\_STRING, RCP\_CONTENT\_TYPE\_FORM, RCP\_CONTENT\_TYPE\_MULTIPARTFORM, RCP\_CONTENT\_TYPE\_GETCALLBACK }

 | 

Content type in [Rcp\_RequestContent](../../structs/rcp-requestcontent/document.md).

 |
| 

[Rcp\_AuthenticationType](../../../modules/remotecommunication/document.md#gaa1b9ec2bd61b2c95492f45eb0a447bff) { RCP\_AUTHENTICATION\_AUTO, RCP\_AUTHENTICATION\_BASIC, RCP\_AUTHENTICATION\_NTLM, RCP\_AUTHENTICATION\_DIGEST }

 | 

Server identity verification type, which is an enumeration. If the type is not set, negotiation with the server is required.

 |
| 

[Rcp\_ExclusionsValueType](../../../modules/remotecommunication/document.md#ga1f5ed8748d80bca8e803ea26d63d1ecf) { RCP\_EXCLUSION\_USE\_URL\_ARRAY, RCP\_EXCLUSION\_USE\_CALLBACK }

 | 

Data type in [Rcp\_Exclusions](../../structs/rcp-exclusions/document.md).

 |
| 

[Rcp\_CertType](../../../modules/remotecommunication/document.md#ga4f79c1d41b9c586d99f1c22ed81b9aee) { RCP\_CERT\_PEM, RCP\_CERT\_DER, RCP\_CERT\_P12 }

 | 

Client certificate type.

 |
| 

[Rcp\_RemoteValidationType](../../../modules/remotecommunication/document.md#gaf9356aea6a8c2e447efe3cf7fa889b87) { RCP\_REMOTE\_VALIDATION\_SYSTEM, RCP\_REMOTE\_VALIDATION\_SKIP, RCP\_REMOTE\_VALIDATION\_CERTIFICATE\_AUTHORITY }

 | 

Remote server validation type.

 |
| 

[Rcp\_ProxyTunnelMode](../../../modules/remotecommunication/document.md#ga7ae11929cb19cd85be3dd97e712e2ac6) { RCP\_PROXY\_TUNNEL\_AUTO, RCP\_PROXY\_TUNNEL\_ALWAYS }

 | 

Indicates when a proxy tunnel needs to be established. Tunneling, or tunnel transmission, is a process where an HTTP CONNECT request is sent to a proxy server, instructing it to establish a connection to the remote host of a specified port number. Once this connection is set up, all subsequent traffic is routed through the proxy. The value **auto** indicates that tunneling is enabled only for HTTPS traffic. The value **always** indicates that tunneling is enabled for all traffic.

 |
| 

[Rcp\_DnsRuleType](../../../modules/remotecommunication/document.md#ga995c92778c5b31c9b4b586c737cfdd3c) { RCP\_DNS\_RULE\_DNS\_SERVERS, RCP\_DNS\_RULE\_STATIC, RCP\_DNS\_RULE\_DYNAMIC }

 | 

DNS rule type in [Rcp\_DnsRule](../../structs/rcp-dnsrule/document.md).

 |
| 

[Rcp\_PathPreference](../../../modules/remotecommunication/document.md#ga9498d24addbd529f258fd6faacfd9c67) { RCP\_PATH\_PREFERENCE\_AUTO, RCP\_PATH\_PREFERENCE\_WIFI, RCP\_PATH\_PREFERENCE\_CELLULAR }

 | 

Request path preferences.

 |
| 

[Rcp\_ProxyType](../../../modules/remotecommunication/document.md#gacfad61d189683cbc02c969a63e246ca1) { RCP\_PROXY\_SYSTEM, RCP\_PROXY\_CUSTOM, RCP\_PROXY\_NO\_PROXY }

 | 

Proxy type, which will be used to determine which proxy configuration will be used.

 |
| 

[Rcp\_StatusCode](../../../modules/remotecommunication/document.md#ga97929a5349f04300f50318f50393b93e) {

RCP\_NONE = 0, RCP\_OK = 200, RCP\_CREATED, RCP\_ACCEPTED,

RCP\_NOT\_AUTHORITATIVE, RCP\_NO\_CONTENT, RCP\_RESET, RCP\_PARTIAL,

RCP\_MULTI\_CHOICE = 300, RCP\_MOVED\_PERMANENTLY, RCP\_MOVED\_TEMPORARILY, RCP\_SEE\_OTHER,

RCP\_NOT\_MODIFIED, RCP\_USE\_PROXY, RCP\_BAD\_REQUEST = 400, RCP\_UNAUTHORIZED,

RCP\_PAYMENT\_REQUIRED, RCP\_FORBIDDEN, RCP\_NOT\_FOUND, RCP\_BAD\_METHOD,

RCP\_NOT\_ACCEPTABLE, RCP\_PROXY\_AUTH, RCP\_CLIENT\_TIMEOUT, RCP\_CONFLICT,

RCP\_GONE, RCP\_LENGTH\_REQUIRED, RCP\_PRECON\_FAILED, RCP\_ENTITY\_TOO\_LARGE,

RCP\_REQ\_TOO\_LONG, RCP\_UNSUPPORTED\_TYPE, RCP\_INTERNAL\_ERROR = 500, RCP\_NOT\_IMPLEMENTED,

RCP\_BAD\_GATEWAY, RCP\_UNAVAILABLE, RCP\_GATEWAY\_TIMEOUT, RCP\_VERSION

}

 | 

Response status code.

 |
| 

[Rcp\_DebugEvent](../../../modules/remotecommunication/document.md#gadff9eaa1b517bf01defd1273b2eeddbc) {

RCP\_DEBUG\_EVENT\_TEXT, RCP\_DEBUG\_EVENT\_HEADER\_IN, RCP\_DEBUG\_EVENT\_HEADER\_OUT, RCP\_DEBUG\_EVENT\_DATA\_IN,

RCP\_DEBUG\_EVENT\_DATA\_OUT, RCP\_DEBUG\_EVENT\_SSL\_DATA\_IN, RCP\_DEBUG\_EVENT\_SSL\_DATA\_OUT

}

 | 

Debugging event type.

 |
| 

[Rcp\_SessionType](../../../modules/remotecommunication/document.md#ga4fa3aa6821b16425c260d837deace956) { RCP\_SESSION\_TYPE\_HTTP = 0, RCP\_SESSION\_TYPE\_MAX = 100}

 | 

Session type.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[Rcp\_Form](../../../modules/remotecommunication/document.md#ga40787f67faf4ea7111e4cda03f3f16be) \* [HMS\_Rcp\_CreateForm](../../../modules/remotecommunication/document.md#gaf46149196c94385e7d8af6c17d1cfab0) (void)

 | 

Creates a simple form.

 |
| 

void [HMS\_Rcp\_DestroyForm](../../../modules/remotecommunication/document.md#ga871fb9f3865c854e38594871b8e65b86) ([Rcp\_Form](../../../modules/remotecommunication/document.md#ga40787f67faf4ea7111e4cda03f3f16be) \*form)

 | 

Destroys a simple form.

 |
| 

uint32\_t [HMS\_Rcp\_SetFormValue](../../../modules/remotecommunication/document.md#ga58aba2b2c4bb1bf93aef474c4427638f) ([Rcp\_Form](../../../modules/remotecommunication/document.md#ga40787f67faf4ea7111e4cda03f3f16be) \*form, const char \*key, const [Rcp\_FormFieldValue](../../structs/rcp-formfieldvalue/document.md) \*value)

 | 

Sets key-value pairs in a simple form.

 |
| 

[Rcp\_FormFieldValue](../../structs/rcp-formfieldvalue/document.md) \* [HMS\_Rcp\_GetFormValue](../../../modules/remotecommunication/document.md#ga1b8e250780190403f0a0d63ab0604017) ([Rcp\_Form](../../../modules/remotecommunication/document.md#ga40787f67faf4ea7111e4cda03f3f16be) \*form, const char \*key)

 | 

Obtains a value based on a key from a simple form.

 |
| 

[Rcp\_MultipartForm](../../../modules/remotecommunication/document.md#ga9f974771548d3ed2054aba0e7506fef9) \* [HMS\_Rcp\_CreateMultipartForm](../../../modules/remotecommunication/document.md#ga2d3c7ad8cd5d670bb4c40b400da52a63) (void)

 | 

Creates a multi-part form.

 |
| 

void [HMS\_Rcp\_DestroyMultipartForm](../../../modules/remotecommunication/document.md#ga449c4206aec628b1a0a4a2b9b7aafd53) ([Rcp\_MultipartForm](../../../modules/remotecommunication/document.md#ga9f974771548d3ed2054aba0e7506fef9) \*multipartForm)

 | 

Destroys a multi-part form.

 |
| 

uint32\_t [HMS\_Rcp\_SetMultipartFormValue](../../../modules/remotecommunication/document.md#ga5148d54bff9d344085c3baa72918dbe9) ([Rcp\_MultipartForm](../../../modules/remotecommunication/document.md#ga9f974771548d3ed2054aba0e7506fef9) \*multipartForm, const char \*key, const [Rcp\_MultipartFormFieldValue](../../structs/rcp-multipartformfieldvalue/document.md) \*value)

 | 

Sets key-value pairs in a multi-part form.

 |
| 

[Rcp\_MultipartFormFieldValue](../../structs/rcp-multipartformfieldvalue/document.md) \* [HMS\_Rcp\_GetMultipartFormValue](../../../modules/remotecommunication/document.md#ga22d2c7c599edf491eabf84d1eeaee533) ([Rcp\_MultipartForm](../../../modules/remotecommunication/document.md#ga9f974771548d3ed2054aba0e7506fef9) \*multipartForm, const char \*key)

 | 

Obtains a value based on a key from a multi-part form.

 |
| 

[Rcp\_Headers](../../../modules/remotecommunication/document.md#gac4f343ec02dec34268e93ce746e6c982) \* [HMS\_Rcp\_CreateHeaders](../../../modules/remotecommunication/document.md#gab797b6fcc146d8b181fb138d424c4800) (void)

 | 

Creates a header for a request or response.

 |
| 

void [HMS\_Rcp\_DestroyHeaders](../../../modules/remotecommunication/document.md#gaee22e11cc947ae599214df9e84a59ae5) ([Rcp\_Headers](../../../modules/remotecommunication/document.md#gac4f343ec02dec34268e93ce746e6c982) \*headers)

 | 

Destroys the header of a request or response.

 |
| 

uint32\_t [HMS\_Rcp\_SetHeaderValue](../../../modules/remotecommunication/document.md#gafb04d92353985e2f4f9f6c2950019068) ([Rcp\_Headers](../../../modules/remotecommunication/document.md#gac4f343ec02dec34268e93ce746e6c982) \*headers, const char \*name, const char \*value)

 | 

Sets key-value pairs in a request or response header.

 |
| 

[Rcp\_HeaderValue](../../structs/rcp-headervalue/document.md) \* [HMS\_Rcp\_GetHeaderValue](../../../modules/remotecommunication/document.md#ga9c8f0d455b76b21dce29e7d425c31da3) ([Rcp\_Headers](../../../modules/remotecommunication/document.md#gac4f343ec02dec34268e93ce746e6c982) \*headers, const char \*name)

 | 

Obtains a value based on a key from a request or response header.

 |
| 

[Rcp\_HeaderEntry](../../structs/rcp-headerentry/document.md) \* [HMS\_Rcp\_GetHeaderEntries](../../../modules/remotecommunication/document.md#ga94edbbabc6b1b76d0e0f729ca618458a) ([Rcp\_Headers](../../../modules/remotecommunication/document.md#gac4f343ec02dec34268e93ce746e6c982) \*headers)

 | 

Obtains all key-value pairs from a request or response header.

 |
| 

void [HMS\_Rcp\_DestroyHeaderEntries](../../../modules/remotecommunication/document.md#gabd8ecd09483ea431cd32cc7218a4ed27) ([Rcp\_HeaderEntry](../../structs/rcp-headerentry/document.md) \*headerEntry)

 | 

Destroys all key-value pairs obtained in [HMS\_Rcp\_GetHeaderEntries](../../../modules/remotecommunication/document.md#ga94edbbabc6b1b76d0e0f729ca618458a).

 |
| 

[Rcp\_Request](../../structs/rcp-request/document.md) \* [HMS\_Rcp\_CreateRequest](../../../modules/remotecommunication/document.md#ga63b1b532e9b37754281c6bdfdf198597) (const char \*url)

 | 

Creates a request.

 |
| 

void [HMS\_Rcp\_DestroyRequest](../../../modules/remotecommunication/document.md#gae2eb219a9afd7ace912e071775058aa2) ([Rcp\_Request](../../structs/rcp-request/document.md) \*request)

 | 

Destroys a request.

 |
| 

[Rcp\_RequestCookies](../../../modules/remotecommunication/document.md#ga44f2b679fefd37e78c43dbcba59d6d50) \* [HMS\_Rcp\_CreateRequestCookies](../../../modules/remotecommunication/document.md#gadb2b6465c6c1966d7983f57dda8582fc) (void)

 | 

Creates empty request cookies.

 |
| 

void [HMS\_Rcp\_DestroyRequestCookies](../../../modules/remotecommunication/document.md#gaca5c542e4cb61a95d3fbd31ebc07d4d0) ([Rcp\_RequestCookies](../../../modules/remotecommunication/document.md#ga44f2b679fefd37e78c43dbcba59d6d50) \*cookies)

 | 

Destroys request cookies.

 |
| 

uint32\_t [HMS\_Rcp\_SetRequestCookieValue](../../../modules/remotecommunication/document.md#ga27ca41ecf30e0f3a2d10fad61494130a) ([Rcp\_RequestCookies](../../../modules/remotecommunication/document.md#ga44f2b679fefd37e78c43dbcba59d6d50) \*cookies, const char \*name, const char \*value)

 | 

Sets request cookies.

 |
| 

char \* [HMS\_Rcp\_GetRequestCookieValue](../../../modules/remotecommunication/document.md#ga43a79371dfb3ff211321d1c18d4864b2) ([Rcp\_RequestCookies](../../../modules/remotecommunication/document.md#ga44f2b679fefd37e78c43dbcba59d6d50) \*cookies, const char \*name)

 | 

Obtains the request cookie value by name.

 |
| 

[Rcp\_RequestCookieEntry](../../structs/rcp-requestcookieentry/document.md) \* [HMS\_Rcp\_GetRequestCookieEntries](../../../modules/remotecommunication/document.md#ga5980d5baff59f1902ff009e557ae9756) ([Rcp\_RequestCookies](../../../modules/remotecommunication/document.md#ga44f2b679fefd37e78c43dbcba59d6d50) \*cookies)

 | 

Obtains all key-value pairs from the request cookies.

 |
| 

void [HMS\_Rcp\_DestroyRequestCookieEntries](../../../modules/remotecommunication/document.md#ga4a75fce3b4d0b690eef330836977da14) ([Rcp\_RequestCookieEntry](../../structs/rcp-requestcookieentry/document.md) \*cookieEntry)

 | 

Destroys all key-value pairs related to request cookies obtained from [HMS\_Rcp\_GetRequestCookieValue](../../../modules/remotecommunication/document.md#ga43a79371dfb3ff211321d1c18d4864b2).

 |
| 

const char \* [HMS\_Rcp\_GetResponseCookieAttrValue](../../../modules/remotecommunication/document.md#ga6538a77ca1dcabe15bb2891f941c377e) ([Rcp\_CookieAttributes](../../../modules/remotecommunication/document.md#ga08c7b992199bec7e5acdc50ce8ae2651) \*cookieAttributes, const char \*name)

 | 

Obtains the cookie attribute value by name.

 |
| 

[Rcp\_CookieAttributeEntry](../../structs/rcp-cookieattributeentry/document.md) \* [HMS\_Rcp\_GetResponseCookieAttrEntries](../../../modules/remotecommunication/document.md#ga8304b7906b7e81b7135a50d77d6eaf48) ([Rcp\_CookieAttributes](../../../modules/remotecommunication/document.md#ga08c7b992199bec7e5acdc50ce8ae2651) \*cookieAttributes)

 | 

Obtains all response cookie attributes from [Rcp\_CookieAttributes](../../../modules/remotecommunication/document.md#ga08c7b992199bec7e5acdc50ce8ae2651).

 |
| 

void [HMS\_Rcp\_DestroyResponseCookieAttrEntries](../../../modules/remotecommunication/document.md#ga83afc8703c589133bf3768e631157413) ([Rcp\_CookieAttributeEntry](../../structs/rcp-cookieattributeentry/document.md) \*entries)

 | 

Destroys response cookie attributes.

 |
| 

uint32\_t [HMS\_Rcp\_CallNextRequestHandler](../../../modules/remotecommunication/document.md#gaa12f2da13b0aa095b7c6ae5e195c1536) ([Rcp\_Request](../../structs/rcp-request/document.md) \*request, const [Rcp\_RequestHandler](../../../modules/remotecommunication/document.md#ga5ac080855c3aaef66c58d5b5b371be2b) \*next, const [Rcp\_ResponseCallbackObject](../../structs/rcp-responsecallbackobject/document.md) \*responseCallback)

 | 

Calls the next interceptor or the **defaultHandler** in [Rcp\_Interceptor](../../structs/rcp-interceptor/document.md).

 |
| 

[Rcp\_Response](../../structs/rcp-response/document.md) \* [HMS\_Rcp\_CallNextSyncRequestHandler](../../../modules/remotecommunication/document.md#ga2a4e9df33b7f4c146e6fb1ddc46dc84f) ([Rcp\_Request](../../structs/rcp-request/document.md) \*request, const [Rcp\_SyncRequestHandler](../../../modules/remotecommunication/document.md#ga2067d1b09b33afa0b8237a049687e9ea) \*next, uint32\_t \*errCode)

 | 

Calls the next interceptor or the default handler in [Rcp\_SyncInterceptor](../../structs/rcp-syncinterceptor/document.md).

 |
| 

[Rcp\_Session](../../../modules/remotecommunication/document.md#ga4f3a7d39c18fe6fdf01c52759213ddcd) \* [HMS\_Rcp\_CreateSession](../../../modules/remotecommunication/document.md#gafc04f552e9d6b90d9d73abbc9535766e) (const [Rcp\_SessionConfiguration](../../structs/rcp-sessionconfiguration/document.md) \*configuration, uint32\_t \*errCode)

 | 

Creates a session.

 |
| 

const char \* [HMS\_Rcp\_GetSessionId](../../../modules/remotecommunication/document.md#ga10f2bd857b521b631838b9e2428925c3) ([Rcp\_Session](../../../modules/remotecommunication/document.md#ga4f3a7d39c18fe6fdf01c52759213ddcd) \*session)

 | 

Obtains the session ID.

 |
| 

const [Rcp\_SessionConfiguration](../../structs/rcp-sessionconfiguration/document.md) \* [HMS\_Rcp\_GetSessionConfiguration](../../../modules/remotecommunication/document.md#ga990339ef86baed18b48fe3ef10031388) ([Rcp\_Session](../../../modules/remotecommunication/document.md#ga4f3a7d39c18fe6fdf01c52759213ddcd) \*session)

 | 

Obtains the session configuration.

 |
| 

[Rcp\_Response](../../structs/rcp-response/document.md) \* [HMS\_Rcp\_FetchSync](../../../modules/remotecommunication/document.md#ga48a83535a4658e9872ded4b0dd8c812f) ([Rcp\_Session](../../../modules/remotecommunication/document.md#ga4f3a7d39c18fe6fdf01c52759213ddcd) \*session, [Rcp\_Request](../../structs/rcp-request/document.md) \*request, uint32\_t \*errCode)

 | 

Sends a synchronous request and obtains a response.

 |
| 

uint32\_t [HMS\_Rcp\_Fetch](../../../modules/remotecommunication/document.md#ga7ea546b69b9ea60ea4716ee64e8b04cb) ([Rcp\_Session](../../../modules/remotecommunication/document.md#ga4f3a7d39c18fe6fdf01c52759213ddcd) \*session, [Rcp\_Request](../../structs/rcp-request/document.md) \*request, const [Rcp\_ResponseCallbackObject](../../structs/rcp-responsecallbackobject/document.md) \*responseCallback)

 | 

Sends an asynchronous request and obtains a response.

 |
| 

uint32\_t [HMS\_Rcp\_CancelRequest](../../../modules/remotecommunication/document.md#gae7974f60c9b17a16e853befd391b7f81) ([Rcp\_Session](../../../modules/remotecommunication/document.md#ga4f3a7d39c18fe6fdf01c52759213ddcd) \*session, const [Rcp\_Request](../../structs/rcp-request/document.md) \*request)

 | 

Cancels a request.

 |
| 

uint32\_t [HMS\_Rcp\_CancelSession](../../../modules/remotecommunication/document.md#ga4ef7303528c1ce13cf5f1267c0650221) ([Rcp\_Session](../../../modules/remotecommunication/document.md#ga4f3a7d39c18fe6fdf01c52759213ddcd) \*session)

 | 

Cancels a session.

 |
| 

uint32\_t [HMS\_Rcp\_CloseSession](../../../modules/remotecommunication/document.md#gaf659dbbb59360b9c587fb4081b52dd14) ([Rcp\_Session](../../../modules/remotecommunication/document.md#ga4f3a7d39c18fe6fdf01c52759213ddcd) \*\*session)

 | 

Closes a session.

 |
| 

uint32\_t [HMS\_Rcp\_SetRequestOnBinaryDataRecvCallback](../../../modules/remotecommunication/document.md#section207321113884) ([Rcp\_Request](../../structs/rcp-request/document.md) \*request, [Rcp\_OnBinaryReceiveCallback](../../structs/rcp-onbinaryreceivecallback/document.md) onBinaryReceiveCallback)

 | 

Sets a callback function for receiving binary data upon a request. The callback function works the same as that of [Rcp\_OnDataReceiveCallback](../../structs/rcp-ondatareceivecallback/document.md), and the callback function can be used to receive both character and binary data.

 |
