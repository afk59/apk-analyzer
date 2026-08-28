# RemoteCommunication

#### Overview

Provides APIs related to remote communication.

This module supports HTTP sessions.

**Start version**: 5.0.0(12)

#### Summary

#### \[h2\]Files

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[rcp.h](../../header-files-and-structs/header-files/rcp-h/document.md)

 | 

Declares the APIs used to access Remote Communication, and defines basic functions, structs, and constants.

 |

#### \[h2\]Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [Rcp\_Buffer](../../header-files-and-structs/structs/rcp-buffer/document.md)

 | 

Text storage struct.

 |
| 

struct [Rcp\_ContentOrPathOrCallback](../../header-files-and-structs/structs/rcp-contentorpathorcallback/document.md)

 | 

Simple form data field value used in [Rcp\_FormFieldFileValue](../../header-files-and-structs/structs/rcp-formfieldfilevalue/document.md).

 |
| 

struct [Rcp\_FormFieldFileValue](../../header-files-and-structs/structs/rcp-formfieldfilevalue/document.md)

 | 

Form field file value.

 |
| 

struct [Rcp\_FormFieldValue](../../header-files-and-structs/structs/rcp-formfieldvalue/document.md)

 | 

Simple form data field value. For details, please refer to [Rcp\_Form](#ga40787f67faf4ea7111e4cda03f3f16be) and [Rcp\_MultipartFormFieldValue](../../header-files-and-structs/structs/rcp-multipartformfieldvalue/document.md).

 |
| 

struct [Rcp\_MultipartFormFieldValue](../../header-files-and-structs/structs/rcp-multipartformfieldvalue/document.md)

 | 

Multi-part form field value, which will be used in [Rcp\_MultipartForm](#ga9f974771548d3ed2054aba0e7506fef9).

 |
| 

struct [Rcp\_RequestContent](../../header-files-and-structs/structs/rcp-requestcontent/document.md)

 | 

Request content.

 |
| 

struct [Rcp\_HeaderValue](../../header-files-and-structs/structs/rcp-headervalue/document.md)

 | 

Value type of a mapped value in a request or response header.

 |
| 

struct [Rcp\_HeaderEntry](../../header-files-and-structs/structs/rcp-headerentry/document.md)

 | 

All key-value pairs in the request or response header.

 |
| 

struct [Rcp\_Credential](../../header-files-and-structs/structs/rcp-credential/document.md)

 | 

Credential, required by some servers or proxy servers.

 |
| 

struct [Rcp\_ServerAuthentication](../../header-files-and-structs/structs/rcp-serverauthentication/document.md)

 | 

Server identity verification information.

 |
| 

struct [Rcp\_Urls](../../header-files-and-structs/structs/rcp-urls/document.md)

 | 

URL, which is used to determine whether a host is using a proxy.

 |
| 

struct [Rcp\_Exclusions](../../header-files-and-structs/structs/rcp-exclusions/document.md)

 | 

URLs excluded from proxy processing.

 |
| 

struct [Rcp\_CertificateAuthority](../../header-files-and-structs/structs/rcp-certificateauthority/document.md)

 | 

CA used to verify the identity of a remote server.

 |
| 

struct [Rcp\_ClientCertificate](../../header-files-and-structs/structs/rcp-clientcertificate/document.md)

 | 

Client certificate sent to a remote server, which will be used by the server to verify the identity of the client.

 |
| 

struct [Rcp\_SecurityConfiguration](../../header-files-and-structs/structs/rcp-securityconfiguration/document.md)

 | 

Request security configuration.

 |
| 

struct [Rcp\_WebProxy](../../header-files-and-structs/structs/rcp-webproxy/document.md)

 | 

Custom proxy configuration.

 |
| 

struct [Rcp\_IpAndPort](../../header-files-and-structs/structs/rcp-ipandport/document.md)

 | 

IP address and port number of a DNS server, which will be used in [Rcp\_DnsServers](../../header-files-and-structs/structs/rcp-dnsservers/document.md).

 |
| 

struct [Rcp\_DnsServers](../../header-files-and-structs/structs/rcp-dnsservers/document.md)

 | 

DNS server, which is one of the types defined in [Rcp\_DnsConfiguration.dnsRules](../../header-files-and-structs/structs/rcp-dnsconfiguration/document.md#ab09aacb68c682d9beea100cae481eaa4).

 |
| 

struct [Rcp\_IpAddress](../../header-files-and-structs/structs/rcp-ipaddress/document.md)

 | 

IP address group used by the static DNS rule [Rcp\_StaticDnsRuleItem](../../header-files-and-structs/structs/rcp-staticdnsruleitem/document.md).

 |
| 

struct [Rcp\_StaticDnsRuleItem](../../header-files-and-structs/structs/rcp-staticdnsruleitem/document.md)

 | 

Description about a single static DNS rule.

 |
| 

struct [Rcp\_StaticDnsRule](../../header-files-and-structs/structs/rcp-staticdnsrule/document.md)

 | 

Static DNS rule.

 |
| 

struct [Rcp\_DnsRule](../../header-files-and-structs/structs/rcp-dnsrule/document.md)

 | 

DNS rule configuration.

 |
| 

struct [Rcp\_OnDataReceiveCallback](../../header-files-and-structs/structs/rcp-ondatareceivecallback/document.md)

 | 

Callback triggered upon data receiving events, which is configured in [Rcp\_EventsHandler](../../header-files-and-structs/structs/rcp-eventshandler/document.md).

 |
| 

struct [Rcp\_OnProgressCallback](../../header-files-and-structs/structs/rcp-onprogresscallback/document.md)

 | 

Callback triggered upon data transmission events, which is configured in [Rcp\_EventsHandler](../../header-files-and-structs/structs/rcp-eventshandler/document.md).

 |
| 

struct [Rcp\_OnHeaderReceiveCallback](../../header-files-and-structs/structs/rcp-onheaderreceivecallback/document.md)

 | 

Callback triggered upon header receiving events, which is configured in [Rcp\_EventsHandler](../../header-files-and-structs/structs/rcp-eventshandler/document.md).

 |
| 

struct [Rcp\_OnVoidCallback](../../header-files-and-structs/structs/rcp-onvoidcallback/document.md)

 | 

Callback triggered upon transmigration ending or cancellation events, which is configured in [Rcp\_EventsHandler](../../header-files-and-structs/structs/rcp-eventshandler/document.md).

 |
| 

struct [Rcp\_EventsHandler](../../header-files-and-structs/structs/rcp-eventshandler/document.md)

 | 

Callback function for listening on various HTTP events.

 |
| 

struct [Rcp\_Timeout](../../header-files-and-structs/structs/rcp-timeout/document.md)

 | 

Request timeout configuration.

 |
| 

struct [Rcp\_DnsOverHttps](../../header-files-and-structs/structs/rcp-dnsoverhttps/document.md)

 | 

DNS over HTTPS. If this information is configured, addresses resolved by the DOH DNS server will be preferred.

 |
| 

struct [Rcp\_TransferConfiguration](../../header-files-and-structs/structs/rcp-transferconfiguration/document.md)

 | 

Transmission configuration.

 |
| 

struct [Rcp\_InfoToCollect](../../header-files-and-structs/structs/rcp-infotocollect/document.md)

 | 

Request processing events to be collected. You can check the response object for collected events.

 |
| 

struct [Rcp\_TracingConfiguration](../../header-files-and-structs/structs/rcp-tracingconfiguration/document.md)

 | 

Request tracing configuration.

 |
| 

struct [Rcp\_ProxyConfiguration](../../header-files-and-structs/structs/rcp-proxyconfiguration/document.md)

 | 

Proxy configuration.

 |
| 

struct [Rcp\_DnsConfiguration](../../header-files-and-structs/structs/rcp-dnsconfiguration/document.md)

 | 

DNS resolution configuration.

 |
| 

struct [Rcp\_Configuration](../../header-files-and-structs/structs/rcp-configuration/document.md)

 | 

Request configuration.

 |
| 

struct [Rcp\_TransferRange](../../header-files-and-structs/structs/rcp-transferrange/document.md)

 | 

HTTP transmission range. This configuration will be converted into the HTTP Range header. An HTTP request with such a header requires the server to return only a part of the HTTP response.

 |
| 

struct [Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md)

 | 

Network request.

 |
| 

struct [Rcp\_RequestCookieEntry](../../header-files-and-structs/structs/rcp-requestcookieentry/document.md)

 | 

All cookie key-value pairs in the request.

 |
| 

struct [Rcp\_DebugInfo](../../header-files-and-structs/structs/rcp-debuginfo/document.md)

 | 

Structure of the debugging information stored in [Rcp\_Response](../../header-files-and-structs/structs/rcp-response/document.md).

 |
| 

struct [Rcp\_CookieAttributeEntry](../../header-files-and-structs/structs/rcp-cookieattributeentry/document.md)

 | 

Response cookie attribute entry.

 |
| 

struct [Rcp\_ResponseCookies](../../header-files-and-structs/structs/rcp-responsecookies/document.md)

 | 

Response cookies.

 |
| 

struct [Rcp\_TimeInfo](../../header-files-and-structs/structs/rcp-timeinfo/document.md)

 | 

Response timer information.

 |
| 

struct [Rcp\_ResponseCallbackObject](../../header-files-and-structs/structs/rcp-responsecallbackobject/document.md)

 | 

Response callback struct.

 |
| 

struct [Rcp\_Response](../../header-files-and-structs/structs/rcp-response/document.md)

 | 

Response to a network request.

 |
| 

struct [Rcp\_Interceptor](../../header-files-and-structs/structs/rcp-interceptor/document.md)

 | 

Asynchronous interceptor.

 |
| 

struct [Rcp\_SyncInterceptor](../../header-files-and-structs/structs/rcp-syncinterceptor/document.md)

 | 

Synchronous interceptor.

 |
| 

struct [Rcp\_InterceptorArray](../../header-files-and-structs/structs/rcp-interceptorarray/document.md)

 | 

Asynchronous interceptor array.

 |
| 

struct [Rcp\_SyncInterceptorArray](../../header-files-and-structs/structs/rcp-syncinterceptorarray/document.md)

 | 

Synchronous interceptor array.

 |
| 

struct [Rcp\_SessionListener](../../header-files-and-structs/structs/rcp-sessionlistener/document.md)

 | 

Callback function for listening on session closing or cancellation events.

 |
| 

struct [Rcp\_ConnectionConfiguration](../../header-files-and-structs/structs/rcp-connectionconfiguration/document.md)

 | 

Connection configuration.

 |
| 

struct [Rcp\_SessionConfiguration](../../header-files-and-structs/structs/rcp-sessionconfiguration/document.md)

 | 

Session configuration.

 |
| 

struct [Rcp\_OnBinaryReceiveCallback](../../header-files-and-structs/structs/rcp-onbinaryreceivecallback/document.md)

 | 

Callback triggered when the binary data in the response is received.

 |
| 

struct [Rcp\_OnStatusCodeReceiveCallback](../../header-files-and-structs/structs/rcp-onstatuscodereceivecallback/document.md)

 | 

Callback triggered when a response status code is received.

 |

#### \[h2\]Macro Definition

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[RCP\_MAX\_REQUEST\_ID\_LEN](#ga34b7468983f894581c9e908295c6d92e) 32

 | 

Maximum length of a request ID.

 |
| 

[RCP\_MAX\_CONTENT\_TYPE\_LEN](#ga994193494eac9591a85c49f1e3200930) 64

 | 

Maximum length of the content type.

 |
| 

[RCP\_MAX\_FILENAME\_LEN](#gaef0f15d9c2cacf9df70ba148cfff171b) 128

 | 

Maximum length of a file name.

 |
| 

[RCP\_MAX\_PATH\_LEN](#ga3dac667ae8b6fa64f2fede1e77804e12) 128

 | 

Maximum path length.

 |
| 

[RCP\_METHOD\_GET](#ga2f2cc4bec6023047b63a1b3aaca7e8ff) "GET"

 | 

HTTP GET method.

 |
| 

[RCP\_METHOD\_HEAD](#ga01f80464137185de1b1c9d4a84a20328) "HEAD"

 | 

HTTP HEAD method.

 |
| 

[RCP\_METHOD\_OPTIONS](#gac3a9a3250402418f4a59875e5e98cfc7) "OPTIONS"

 | 

HTTP OPTIONS method.

 |
| 

[RCP\_METHOD\_TRACE](#ga3676dd73393ff05d3c487140ac5c3a88) "TRACE"

 | 

HTTP TRACE method.

 |
| 

[RCP\_METHOD\_DELETE](#ga865bfb4de54f47a05b3adc17eccfccf7) "DELETE"

 | 

HTTP DELETE method.

 |
| 

[RCP\_METHOD\_POST](#ga5c3de5092bf8c0b6556ccdf35b433b85) "POST"

 | 

HTTP POST method.

 |
| 

[RCP\_METHOD\_PUT](#gada60d0d101fce537636d5d38ebdcd5b1) "PUT"

 | 

HTTP PUT method.

 |
| 

[RCP\_METHOD\_PATCH](#ga34617da18b0341c7111d0853834a12a1) "PATCH"

 | 

HTTP PATCH method.

 |
| 

[RCP\_IP\_MAX\_LEN](#gaedd78171e1671e9ec89b59ecf6e96730) 40

 | 

Maximum length of an IP address.

 |
| 

[RCP\_HOST\_MAX\_LEN](#gaf8dd4d8c5c99712c29f29211ad2a76ae) 256

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

typedef enum [Rcp\_FormValueType](#ga9d851389347a39bd4bb849ac31cfa478) [Rcp\_FormValueType](#gaa1493419cc430c47cef7ec7ddfb74220)

 | 

Form value type.

 |
| 

typedef int(\* [Rcp\_GetDataCallback](#gac0ac73f33252239ff47a648fe3aa6bd5)) (char \*out, uint32\_t size)

 | 

Data obtained through a callback function. This callback is used when the API needs to send the next part of the data to the server.

 |
| 

typedef enum [Rcp\_ContentOrPathOrCallbackType](#gaa5a592f4e68a1dd43f5f41e95199a5e4) [Rcp\_ContentOrPathOrCallbackType](#gaa0382cf2e96821ed741ad9f99dd9e37a)

 | 

Content, path, or callback type, which is used to distinguish the data used in [Rcp\_ContentOrPathOrCallback](../../header-files-and-structs/structs/rcp-contentorpathorcallback/document.md).

 |
| 

typedef struct [Rcp\_Buffer](../../header-files-and-structs/structs/rcp-buffer/document.md) [Rcp\_Buffer](#ga74d7d9dd56fabaa773cf1659c2d2eace)

 | 

Text storage struct.

 |
| 

typedef struct [Rcp\_ContentOrPathOrCallback](../../header-files-and-structs/structs/rcp-contentorpathorcallback/document.md) [Rcp\_ContentOrPathOrCallback](#gaebb5b634a56751ae23ac2610e230ec72)

 | 

Simple form data field value used in [Rcp\_FormFieldFileValue](../../header-files-and-structs/structs/rcp-formfieldfilevalue/document.md).

 |
| 

typedef enum [Rcp\_MultipartValueType](#ga76d003b4f9a244c9d11def4128ceeda8) [Rcp\_MultipartValueType](#gafeeacbc819f33dae11912a0c59f4a678)

 | 

Multi-part form value type, which is used to distinguish the data used in [Rcp\_MultipartFormFieldValue](../../header-files-and-structs/structs/rcp-multipartformfieldvalue/document.md).

 |
| 

typedef struct [Rcp\_FormFieldFileValue](../../header-files-and-structs/structs/rcp-formfieldfilevalue/document.md) [Rcp\_FormFieldFileValue](#ga774f6381467f16c39aaa2988c69ad7fd)

 | 

Form field file value.

 |
| 

typedef struct [Rcp\_FormFieldValue](../../header-files-and-structs/structs/rcp-formfieldvalue/document.md) [Rcp\_FormFieldValue](#gaf68638c39567d0c7b1e9ed0f145ebc65)

 | 

Simple form data field value. For details, please refer to [Rcp\_Form](#ga40787f67faf4ea7111e4cda03f3f16be) and [Rcp\_MultipartFormFieldValue](../../header-files-and-structs/structs/rcp-multipartformfieldvalue/document.md).

 |
| 

typedef struct [Rcp\_MultipartFormFieldValue](../../header-files-and-structs/structs/rcp-multipartformfieldvalue/document.md) [Rcp\_MultipartFormFieldValue](#ga64c7e2addc25dd589c5f65237eded576)

 | 

Multi-part form field value, which will be used in [Rcp\_MultipartForm](#ga9f974771548d3ed2054aba0e7506fef9).

 |
| 

typedef enum [Rcp\_ContentType](#ga05daeab5ad8d265834b4a1b4e61cd8fa) [Rcp\_ContentType](#gacb1c467d93e50c5cdd7ace89f1369975)

 | 

Content type in [Rcp\_RequestContent](../../header-files-and-structs/structs/rcp-requestcontent/document.md).

 |
| 

typedef struct [Rcp\_Form](#ga40787f67faf4ea7111e4cda03f3f16be) [Rcp\_Form](#ga40787f67faf4ea7111e4cda03f3f16be)

 | 

Simple form data.

 |
| 

typedef struct [Rcp\_MultipartForm](#ga9f974771548d3ed2054aba0e7506fef9) [Rcp\_MultipartForm](#ga9f974771548d3ed2054aba0e7506fef9)

 | 

Multi-part form data.

 |
| 

typedef struct [Rcp\_RequestContent](../../header-files-and-structs/structs/rcp-requestcontent/document.md) [Rcp\_RequestContent](#gaaf7ad4248342bb42ae9af6eb883e7679)

 | 

Request content.

 |
| 

typedef struct [Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982) [Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982)

 | 

Header of a request or response.

 |
| 

typedef struct [Rcp\_HeaderValue](../../header-files-and-structs/structs/rcp-headervalue/document.md) [Rcp\_HeaderValue](#gac6096559a00691522790022a9335922a)

 | 

Value type of a mapped value in a request or response header.

 |
| 

typedef struct [Rcp\_HeaderEntry](../../header-files-and-structs/structs/rcp-headerentry/document.md) [Rcp\_HeaderEntry](#gae0d149375558a4b9de6058ee281a49c3)

 | 

All key-value pairs in the request or response header.

 |
| 

typedef enum [Rcp\_AuthenticationType](#gaa1b9ec2bd61b2c95492f45eb0a447bff) [Rcp\_AuthenticationType](#ga60aa25edf4cc00a574abb8ffebcb7f60)

 | 

Server identity verification type, which is an enumeration. If the type is not set, negotiation with the server is required.

 |
| 

typedef struct [Rcp\_Credential](../../header-files-and-structs/structs/rcp-credential/document.md) [Rcp\_Credential](#ga15452ad2af919bfffeb3a1f723e1eb5d)

 | 

Credential, required by some servers or proxy servers.

 |
| 

typedef struct [Rcp\_ServerAuthentication](../../header-files-and-structs/structs/rcp-serverauthentication/document.md) [Rcp\_ServerAuthentication](#ga9977de0042837319e439fdfe28ec6af8)

 | 

Server identity verification information.

 |
| 

typedef bool(\* [Rcp\_ExclusionFunction](#gac6517b72e4a8c0feaf864f3669d2c127)) (const char \*url)

 | 

Pointer to the function for determining whether a host uses a proxy.

 |
| 

typedef struct [Rcp\_Urls](../../header-files-and-structs/structs/rcp-urls/document.md) [Rcp\_Urls](#ga4580ece64cbef2ce6cd66e0153f31721)

 | 

URL, which is used to determine whether a host is using a proxy.

 |
| 

typedef enum [Rcp\_ExclusionsValueType](#ga1f5ed8748d80bca8e803ea26d63d1ecf) [Rcp\_ExclusionsValueType](#gae691e3a52b7d410309e096d3a6083385)

 | 

Data type in [Rcp\_Exclusions](../../header-files-and-structs/structs/rcp-exclusions/document.md).

 |
| 

typedef struct [Rcp\_Exclusions](../../header-files-and-structs/structs/rcp-exclusions/document.md) [Rcp\_Exclusions](#gac98e0508b4e76da5550bdf49b00a28de)

 | 

URLs excluded from proxy processing.

 |
| 

typedef enum [Rcp\_CertType](#ga4f79c1d41b9c586d99f1c22ed81b9aee) [Rcp\_CertType](#ga1862154a92f9f18850df7981e4eb7835)

 | 

Client certificate type.

 |
| 

typedef struct [Rcp\_CertificateAuthority](../../header-files-and-structs/structs/rcp-certificateauthority/document.md) [Rcp\_CertificateAuthority](#ga5f3dcd559a5c06922af97232ef415a25)

 | 

CA used to verify the identity of a remote server.

 |
| 

typedef struct [Rcp\_ClientCertificate](../../header-files-and-structs/structs/rcp-clientcertificate/document.md) [Rcp\_ClientCertificate](#ga845e91b33e622fea75ca06bda166e5e9)

 | 

Client certificate sent to a remote server, which will be used by the server to verify the identity of the client.

 |
| 

typedef enum [Rcp\_RemoteValidationType](#gaf9356aea6a8c2e447efe3cf7fa889b87) [Rcp\_RemoteValidationType](#ga188c30a5aa5e064b2b366cfc04c901e7)

 | 

Remote server validation type.

 |
| 

typedef struct [Rcp\_SecurityConfiguration](../../header-files-and-structs/structs/rcp-securityconfiguration/document.md) [Rcp\_SecurityConfiguration](#gae90019e06749ddcbc625d7b466b39d6b)

 | 

Request security configuration.

 |
| 

typedef enum [Rcp\_ProxyTunnelMode](#ga7ae11929cb19cd85be3dd97e712e2ac6) [Rcp\_ProxyTunnelMode](#ga2c01e03e43784509918e5d3641371e6b)

 | 

Indicates when a proxy tunnel needs to be established. Tunneling, or tunnel transmission, is a process where an HTTP CONNECT request is sent to a proxy server, instructing it to establish a connection to the remote host of a specified port number. Once this connection is set up, all subsequent traffic is routed through the proxy. The value **auto** indicates that a tunnel will be created for HTTPS traffic but not for HTTP traffic. The value **always** indicates that tunneling is enabled for all traffic.

 |
| 

typedef struct [Rcp\_WebProxy](../../header-files-and-structs/structs/rcp-webproxy/document.md) [Rcp\_WebProxy](#ga389f9fb59be18ed6ac4ae970eeb4a1a8)

 | 

Custom proxy configuration.

 |
| 

typedef struct [Rcp\_IpAndPort](../../header-files-and-structs/structs/rcp-ipandport/document.md) [Rcp\_IpAndPort](#gaad7a7752372c8b74f57204678240ad56)

 | 

IP address and port number of a DNS server, which will be used in [Rcp\_DnsServers](../../header-files-and-structs/structs/rcp-dnsservers/document.md).

 |
| 

typedef struct [Rcp\_DnsServers](../../header-files-and-structs/structs/rcp-dnsservers/document.md) [Rcp\_DnsServers](#ga58948b274c22ba906ac5527c6b5a8a75)

 | 

DNS server, which is one of the types defined in [Rcp\_DnsConfiguration.dnsRules](../../header-files-and-structs/structs/rcp-dnsconfiguration/document.md#ab09aacb68c682d9beea100cae481eaa4).

 |
| 

typedef struct [Rcp\_IpAddress](../../header-files-and-structs/structs/rcp-ipaddress/document.md) [Rcp\_IpAddress](#gaeaf532cd57e6cfc944f77bd0ac9cd205)

 | 

IP address group used by the static DNS rule [Rcp\_StaticDnsRuleItem](../../header-files-and-structs/structs/rcp-staticdnsruleitem/document.md).

 |
| 

typedef struct [Rcp\_StaticDnsRuleItem](../../header-files-and-structs/structs/rcp-staticdnsruleitem/document.md) [Rcp\_StaticDnsRuleItem](#gad8ad9f5130bca04060b5ffad30a915e8)

 | 

Description about a single static DNS rule.

 |
| 

typedef struct [Rcp\_StaticDnsRule](../../header-files-and-structs/structs/rcp-staticdnsrule/document.md) [Rcp\_StaticDnsRule](#ga2fb8b04fec14262d27e95ec33f5a8349)

 | 

Static DNS rule.

 |
| 

typedef [Rcp\_IpAddress](../../header-files-and-structs/structs/rcp-ipaddress/document.md) \*(\* [Rcp\_DynamicDnsRuleFunction](#gad0ace0c83dd20972b34ff1538700eab3)) (const char \*host, uint16\_t port)

 | 

Function that can directly return an IP address based on the host name and port number. It is used for dynamic DNS resolution.

 |
| 

typedef enum [Rcp\_DnsRuleType](#ga995c92778c5b31c9b4b586c737cfdd3c) [Rcp\_DnsRuleType](#ga925086d48b97774cc082773be635e3a1)

 | 

DNS rule type in [Rcp\_DnsRule](../../header-files-and-structs/structs/rcp-dnsrule/document.md).

 |
| 

typedef struct [Rcp\_DnsRule](../../header-files-and-structs/structs/rcp-dnsrule/document.md) [Rcp\_DnsRule](#ga8acd52cb973f1ce65afffb719fe4026d)

 | 

DNS rule configuration.

 |
| 

typedef size\_t(\* [Rcp\_OnDataReceiveCallbackFunc](#gadc4e28c213ddc694e3c0ec76296ef5c0)) (void \*usrObject, const char \*data)

 | 

Callback function triggered when a response body (character data type) is returned.

 |
| 

typedef size\_t(\* [Rcp\_OnBinaryReceiveCallbackFunc](#section1476912410533)) (void \*usrObject, [Rcp\_Buffer](../../header-files-and-structs/structs/rcp-buffer/document.md) \*buffer)

 | 

Callback function triggered when a response body (binary data type) is returned.

 |
| 

typedef void (\* [Rcp\_OnStatusCodeReceiveCallbackFunc](#section1961611617339))(void \*usrObject, uint32\_t statusCode)

 | 

Callback function triggered when a response status code is returned.

 |
| 

typedef void(\* [Rcp\_OnProgressCallbackFunc](#gaaf74ce6d5578d28829955208318d3fbe)) (void \*usrObject, uint64\_t totalSize, uint64\_t transferredSize)

 | 

Callback function triggered during request/response data transmission.

 |
| 

typedef void(\* [Rcp\_OnHeaderReceiveCallbackFunc](#gae90a801a6c386c246e5005eadfe7da0a)) (void \*usrObject, [Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982) \*headers)

 | 

Callback function triggered when all requests are received.

 |
| 

typedef void(\* [Rcp\_OnVoidCallbackFunc](#ga3d6a448e8f0bdcc2b4e70fa6ca00d475)) (void \*usrObject)

 | 

Callback function for listening on DataEnd and Canceled events of requests.

 |
| 

typedef struct [Rcp\_OnDataReceiveCallback](../../header-files-and-structs/structs/rcp-ondatareceivecallback/document.md) [Rcp\_OnDataReceiveCallback](#gacd66d521a147a876e340aed45a3ed1c4)

 | 

Callback triggered upon data receiving events, which is configured in [Rcp\_EventsHandler](../../header-files-and-structs/structs/rcp-eventshandler/document.md).

 |
| 

typedef struct [Rcp\_OnProgressCallback](../../header-files-and-structs/structs/rcp-onprogresscallback/document.md) [Rcp\_OnProgressCallback](#gabd25a25747d1c91772677f68ec8afc67)

 | 

Callback triggered upon data transmission events, which is configured in [Rcp\_EventsHandler](../../header-files-and-structs/structs/rcp-eventshandler/document.md).

 |
| 

typedef struct [Rcp\_OnHeaderReceiveCallback](../../header-files-and-structs/structs/rcp-onheaderreceivecallback/document.md) [Rcp\_OnHeaderReceiveCallback](#gab23c23acd8c159dfbaf00e439a08caf4)

 | 

Callback triggered upon header receiving events, which is configured in [Rcp\_EventsHandler](../../header-files-and-structs/structs/rcp-eventshandler/document.md).

 |
| 

typedef struct [Rcp\_OnVoidCallback](../../header-files-and-structs/structs/rcp-onvoidcallback/document.md) [Rcp\_OnVoidCallback](#gadda85b3a46176f92d45f30d97a78494f)

 | 

Callback triggered upon transmigration ending or cancellation events, which is configured in [Rcp\_EventsHandler](../../header-files-and-structs/structs/rcp-eventshandler/document.md).

 |
| 

typedef struct [Rcp\_EventsHandler](../../header-files-and-structs/structs/rcp-eventshandler/document.md) [Rcp\_EventsHandler](#ga7d9b30e24c4f42e2da0938c04977b6a4)

 | 

Callback function for listening on various HTTP events.

 |
| 

typedef struct [Rcp\_Timeout](../../header-files-and-structs/structs/rcp-timeout/document.md) [Rcp\_Timeout](#ga4e16d4d91f394ab2070adc42d07b16fa)

 | 

Request timeout configuration.

 |
| 

typedef struct [Rcp\_DnsOverHttps](../../header-files-and-structs/structs/rcp-dnsoverhttps/document.md) [Rcp\_DnsOverHttps](#ga514d31fc0e2abc3d0138226287c35aa4)

 | 

DNS over HTTPS. If this information is configured, addresses resolved by the DOH DNS server will be preferred.

 |
| 

typedef enum [Rcp\_PathPreference](#ga9498d24addbd529f258fd6faacfd9c67) [Rcp\_PathPreference](#ga4f6c04d042df5e2835f1d771205aad24)

 | 

Request path preferences.

 |
| 

typedef struct [Rcp\_TransferConfiguration](../../header-files-and-structs/structs/rcp-transferconfiguration/document.md) [Rcp\_TransferConfiguration](#ga1b92400a50ef056d4490220cf2cefbda)

 | 

Transmission configuration.

 |
| 

typedef struct [Rcp\_InfoToCollect](../../header-files-and-structs/structs/rcp-infotocollect/document.md) [Rcp\_InfoToCollect](#ga571eceac21f6acbf6fb846ac5a1abd55)

 | 

Request processing events to be collected. You can check the response object for collected events.

 |
| 

typedef struct [Rcp\_TracingConfiguration](../../header-files-and-structs/structs/rcp-tracingconfiguration/document.md) [Rcp\_TracingConfiguration](#ga8a0a1aa17cd22e2ac5389d55101fe4c5)

 | 

Request tracing configuration.

 |
| 

typedef enum [Rcp\_ProxyType](#gacfad61d189683cbc02c969a63e246ca1) [Rcp\_ProxyType](#ga54cfc687bda5aafc6199dfe678e3a2c9)

 | 

Proxy type, which will be used to determine which proxy configuration will be used.

 |
| 

typedef struct [Rcp\_ProxyConfiguration](../../header-files-and-structs/structs/rcp-proxyconfiguration/document.md) [Rcp\_ProxyConfiguration](#gabc9a05c4bd32b7293392423797fb8e73)

 | 

Proxy configuration.

 |
| 

typedef struct [Rcp\_DnsConfiguration](../../header-files-and-structs/structs/rcp-dnsconfiguration/document.md) [Rcp\_DnsConfiguration](#ga5f45694c1825bec6ceb5c7a8591d5127)

 | 

DNS resolution configuration.

 |
| 

typedef struct [Rcp\_Configuration](../../header-files-and-structs/structs/rcp-configuration/document.md) [Rcp\_Configuration](#ga4ecea20272b8fe673f842e5486ba463b)

 | 

Request configuration.

 |
| 

typedef struct [Rcp\_TransferRange](../../header-files-and-structs/structs/rcp-transferrange/document.md) [Rcp\_TransferRange](#gaf0e1f4ea19d1c9efa13dc794c6c6590b)

 | 

HTTP transmission range. This configuration will be converted into the HTTP Range header. An HTTP request with such a header requires the server to return only a part of the HTTP response.

 |
| 

typedef struct [Rcp\_RequestCookies](#ga44f2b679fefd37e78c43dbcba59d6d50) [Rcp\_RequestCookies](#ga44f2b679fefd37e78c43dbcba59d6d50)

 | 

Request cookies.

 |
| 

typedef struct [Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md) [Rcp\_Request](#ga98dde966841135537e05053bf4da4d5b)

 | 

Network request.

 |
| 

typedef struct [Rcp\_RequestCookieEntry](../../header-files-and-structs/structs/rcp-requestcookieentry/document.md) [Rcp\_RequestCookieEntry](#gab2690d1fbefb9998606757527f1b7b15)

 | 

All cookie key-value pairs in the request.

 |
| 

typedef enum [Rcp\_StatusCode](#ga97929a5349f04300f50318f50393b93e) [Rcp\_StatusCode](#gae926416f69908e790e9bc67bb1e2d1f3)

 | 

Response status code.

 |
| 

typedef enum [Rcp\_DebugEvent](#gadff9eaa1b517bf01defd1273b2eeddbc) [Rcp\_DebugEvent](#ga79f61404bcc66d914e298c5362d73d69)

 | 

Debugging event type.

 |
| 

typedef struct [Rcp\_DebugInfo](../../header-files-and-structs/structs/rcp-debuginfo/document.md) [Rcp\_DebugInfo](#ga5738cb7a4a2768ecf909a22cfba77e0f)

 | 

Structure of the debugging information stored in [Rcp\_Response](../../header-files-and-structs/structs/rcp-response/document.md).

 |
| 

typedef struct [Rcp\_CookieAttributes](#ga08c7b992199bec7e5acdc50ce8ae2651) [Rcp\_CookieAttributes](#ga08c7b992199bec7e5acdc50ce8ae2651)

 | 

Cookie attribute type in [Rcp\_Response](../../header-files-and-structs/structs/rcp-response/document.md).

 |
| 

typedef struct [Rcp\_CookieAttributeEntry](../../header-files-and-structs/structs/rcp-cookieattributeentry/document.md) [Rcp\_CookieAttributeEntry](#gaaff95756175ea20a41b1134c6aefb45e)

 | 

Response cookie attribute entry.

 |
| 

typedef struct [Rcp\_ResponseCookies](../../header-files-and-structs/structs/rcp-responsecookies/document.md) [Rcp\_ResponseCookies](#ga71bcf6497f4d94dc7bbc50adcfee081f)

 | 

Response cookies.

 |
| 

typedef struct [Rcp\_TimeInfo](../../header-files-and-structs/structs/rcp-timeinfo/document.md) [Rcp\_TimeInfo](#ga0ca30b26b3aeba0a436ac9bbd41c484b)

 | 

Response timer information.

 |
| 

typedef struct [Rcp\_Response](../../header-files-and-structs/structs/rcp-response/document.md) [Rcp\_Response](#gaefca0869b44c6d31f91db0b3476f7863)

 | 

Response to a network request.

 |
| 

typedef void(\* [Rcp\_ResponseCallback](#ga9403920c5b3bbe62d14816c693f5e024)) (void \*usrCtx, [Rcp\_Response](../../header-files-and-structs/structs/rcp-response/document.md) \*response, uint32\_t errCode)

 | 

Pointer to the response callback function.

 |
| 

typedef struct [Rcp\_ResponseCallbackObject](../../header-files-and-structs/structs/rcp-responsecallbackobject/document.md) [Rcp\_ResponseCallbackObject](#ga815137188d22749aff74afef7387860a)

 | 

Response callback struct.

 |
| 

typedef struct [Rcp\_RequestHandler](#ga5ac080855c3aaef66c58d5b5b371be2b) [Rcp\_RequestHandler](#ga5ac080855c3aaef66c58d5b5b371be2b)

 | 

Asynchronous handler associated with [Rcp\_Interceptor](../../header-files-and-structs/structs/rcp-interceptor/document.md).

 |
| 

typedef struct [Rcp\_SyncRequestHandler](#ga2067d1b09b33afa0b8237a049687e9ea) [Rcp\_SyncRequestHandler](#ga2067d1b09b33afa0b8237a049687e9ea)

 | 

Synchronous handler associated with [Rcp\_SyncInterceptor](../../header-files-and-structs/structs/rcp-syncinterceptor/document.md).

 |
| 

typedef struct [Rcp\_Interceptor](../../header-files-and-structs/structs/rcp-interceptor/document.md) [Rcp\_Interceptor](#ga574aa47231df9c57b58c3aff0736c5e5)

 | 

Asynchronous interceptor.

 |
| 

typedef struct [Rcp\_SyncInterceptor](../../header-files-and-structs/structs/rcp-syncinterceptor/document.md) [Rcp\_SyncInterceptor](#ga43a43cc8e864121ada235f484ffefece)

 | 

Synchronous interceptor.

 |
| 

typedef struct [Rcp\_InterceptorArray](../../header-files-and-structs/structs/rcp-interceptorarray/document.md) [Rcp\_InterceptorArray](#ga58ca95fc666a9a5694e92da1ce9b5c0b)

 | 

Asynchronous interceptor array.

 |
| 

typedef struct [Rcp\_SyncInterceptorArray](../../header-files-and-structs/structs/rcp-syncinterceptorarray/document.md) [Rcp\_SyncInterceptorArray](#ga8612d3521508093ed36be72b7f5cb373)

 | 

Synchronous interceptor array.

 |
| 

typedef enum [Rcp\_SessionType](#ga4fa3aa6821b16425c260d837deace956) [Rcp\_SessionType](#ga5254a5bead7a2562f9593d33018f460c)

 | 

Session type.

 |
| 

typedef struct [Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd) [Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd)

 | 

Session.

 |
| 

typedef struct [Rcp\_SessionListener](../../header-files-and-structs/structs/rcp-sessionlistener/document.md) [Rcp\_SessionListener](#ga43cd805167e33b051ccbe940d75f5966)

 | 

Callback function for listening on session closing or cancellation events.

 |
| 

typedef struct [Rcp\_ConnectionConfiguration](../../header-files-and-structs/structs/rcp-connectionconfiguration/document.md) [Rcp\_ConnectionConfiguration](#gac814a198390d0e7a094b241542c9139d)

 | 

Connection configuration.

 |
| 

typedef struct [Rcp\_SessionConfiguration](../../header-files-and-structs/structs/rcp-sessionconfiguration/document.md) [Rcp\_SessionConfiguration](#ga2d8aab48bdb45313f589dbd8ec00e36c)

 | 

Session configuration.

 |
| 

typedef struct [Rcp\_OnBinaryReceiveCallback](../../header-files-and-structs/structs/rcp-onbinaryreceivecallback/document.md) [Rcp\_OnBinaryReceiveCallback](#section118171139416)

 | 

Callback triggered when the binary data in the response is received.

 |
| 

typedef struct [Rcp\_OnStatusCodeReceiveCallback](../../header-files-and-structs/structs/rcp-onstatuscodereceivecallback/document.md) [Rcp\_OnStatusCodeReceiveCallback](#section5616146153312)

 | 

Callback triggered when a response status code is received.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[Rcp\_FormValueType](#ga9d851389347a39bd4bb849ac31cfa478) {

RCP\_FORM\_VALUE\_TYPE\_INT32, RCP\_FORM\_VALUE\_TYPE\_INT64, RCP\_FORM\_VALUE\_TYPE\_BOOL, RCP\_FORM\_VALUE\_TYPE\_STRING,

RCP\_FORM\_VALUE\_TYPE\_DOUBLE

}

 | 

Form value type.

 |
| 

[Rcp\_ContentOrPathOrCallbackType](#gaa5a592f4e68a1dd43f5f41e95199a5e4) { RCP\_FILE\_VALUE\_TYPE\_CONTENT, RCP\_FILE\_VALUE\_TYPE\_PATH, RCP\_FILE\_VALUE\_TYPE\_CALLBACK }

 | 

Content, path, or callback type, which is used to distinguish the data used in [Rcp\_ContentOrPathOrCallback](../../header-files-and-structs/structs/rcp-contentorpathorcallback/document.md).

 |
| 

[Rcp\_MultipartValueType](#ga76d003b4f9a244c9d11def4128ceeda8) { RCP\_TYPE\_FORM\_FIELD\_VALUE, RCP\_TYPE\_FORM\_FIELD\_FILE\_VALUE }

 | 

Multi-part form value type, which is used to distinguish the data used in [Rcp\_MultipartFormFieldValue](../../header-files-and-structs/structs/rcp-multipartformfieldvalue/document.md).

 |
| 

[Rcp\_ContentType](#ga05daeab5ad8d265834b4a1b4e61cd8fa) { RCP\_CONTENT\_TYPE\_STRING, RCP\_CONTENT\_TYPE\_FORM, RCP\_CONTENT\_TYPE\_MULTIPARTFORM, RCP\_CONTENT\_TYPE\_GETCALLBACK }

 | 

Content type in [Rcp\_RequestContent](../../header-files-and-structs/structs/rcp-requestcontent/document.md).

 |
| 

[Rcp\_AuthenticationType](#gaa1b9ec2bd61b2c95492f45eb0a447bff) { RCP\_AUTHENTICATION\_AUTO, RCP\_AUTHENTICATION\_BASIC, RCP\_AUTHENTICATION\_NTLM, RCP\_AUTHENTICATION\_DIGEST }

 | 

Server identity verification type, which is an enumeration. If the type is not set, negotiation with the server is required.

 |
| 

[Rcp\_ExclusionsValueType](#ga1f5ed8748d80bca8e803ea26d63d1ecf) { RCP\_EXCLUSION\_USE\_URL\_ARRAY, RCP\_EXCLUSION\_USE\_CALLBACK }

 | 

Data type in [Rcp\_Exclusions](../../header-files-and-structs/structs/rcp-exclusions/document.md).

 |
| 

[Rcp\_CertType](#ga4f79c1d41b9c586d99f1c22ed81b9aee) { RCP\_CERT\_PEM, RCP\_CERT\_DER, RCP\_CERT\_P12 }

 | 

Client certificate type.

 |
| 

[Rcp\_RemoteValidationType](#gaf9356aea6a8c2e447efe3cf7fa889b87) { RCP\_REMOTE\_VALIDATION\_SYSTEM, RCP\_REMOTE\_VALIDATION\_SKIP, RCP\_REMOTE\_VALIDATION\_CERTIFICATE\_AUTHORITY }

 | 

Remote server validation type.

 |
| 

[Rcp\_ProxyTunnelMode](#ga7ae11929cb19cd85be3dd97e712e2ac6) { RCP\_PROXY\_TUNNEL\_AUTO, RCP\_PROXY\_TUNNEL\_ALWAYS }

 | 

Indicates when a proxy tunnel needs to be established. Tunneling, or tunnel transmission, is a process where an HTTP CONNECT request is sent to a proxy server, instructing it to establish a connection to the remote host of a specified port number. Once this connection is set up, all subsequent traffic is routed through the proxy. The value **auto** indicates that a tunnel will be created for HTTPS traffic but not for HTTP traffic. The value **always** indicates that tunneling is enabled for all traffic.

 |
| 

[Rcp\_DnsRuleType](#ga995c92778c5b31c9b4b586c737cfdd3c) { RCP\_DNS\_RULE\_DNS\_SERVERS, RCP\_DNS\_RULE\_STATIC, RCP\_DNS\_RULE\_DYNAMIC }

 | 

DNS rule type in [Rcp\_DnsRule](../../header-files-and-structs/structs/rcp-dnsrule/document.md).

 |
| 

[Rcp\_PathPreference](#ga9498d24addbd529f258fd6faacfd9c67) { RCP\_PATH\_PREFERENCE\_AUTO, RCP\_PATH\_PREFERENCE\_WIFI, RCP\_PATH\_PREFERENCE\_CELLULAR }

 | 

Request path preferences.

 |
| 

[Rcp\_ProxyType](#gacfad61d189683cbc02c969a63e246ca1) { RCP\_PROXY\_SYSTEM, RCP\_PROXY\_CUSTOM, RCP\_PROXY\_NO\_PROXY }

 | 

Proxy type, which will be used to determine which proxy configuration will be used.

 |
| 

[Rcp\_StatusCode](#ga97929a5349f04300f50318f50393b93e) {

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

[Rcp\_DebugEvent](#gadff9eaa1b517bf01defd1273b2eeddbc) {

RCP\_DEBUG\_EVENT\_TEXT, RCP\_DEBUG\_EVENT\_HEADER\_IN, RCP\_DEBUG\_EVENT\_HEADER\_OUT, RCP\_DEBUG\_EVENT\_DATA\_IN,

RCP\_DEBUG\_EVENT\_DATA\_OUT, RCP\_DEBUG\_EVENT\_SSL\_DATA\_IN, RCP\_DEBUG\_EVENT\_SSL\_DATA\_OUT

}

 | 

Debugging event type.

 |
| 

[Rcp\_SessionType](#ga4fa3aa6821b16425c260d837deace956) { RCP\_SESSION\_TYPE\_HTTP = 0, RCP\_SESSION\_TYPE\_MAX = 100 }

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

[Rcp\_Form](#ga40787f67faf4ea7111e4cda03f3f16be) \* [HMS\_Rcp\_CreateForm](#gaf46149196c94385e7d8af6c17d1cfab0) (void)

 | 

Creates a simple form.

 |
| 

void [HMS\_Rcp\_DestroyForm](#ga871fb9f3865c854e38594871b8e65b86) ([Rcp\_Form](#ga40787f67faf4ea7111e4cda03f3f16be) \*form)

 | 

Destroys a simple form.

 |
| 

uint32\_t [HMS\_Rcp\_SetFormValue](#ga58aba2b2c4bb1bf93aef474c4427638f) ([Rcp\_Form](#ga40787f67faf4ea7111e4cda03f3f16be) \*form, const char \*key, const [Rcp\_FormFieldValue](../../header-files-and-structs/structs/rcp-formfieldvalue/document.md) \*value)

 | 

Sets key-value pairs in a simple form.

 |
| 

[Rcp\_FormFieldValue](../../header-files-and-structs/structs/rcp-formfieldvalue/document.md) \* [HMS\_Rcp\_GetFormValue](#ga1b8e250780190403f0a0d63ab0604017) ([Rcp\_Form](#ga40787f67faf4ea7111e4cda03f3f16be) \*form, const char \*key)

 | 

Obtains a value based on a key from a simple form.

 |
| 

[Rcp\_MultipartForm](#ga9f974771548d3ed2054aba0e7506fef9) \* [HMS\_Rcp\_CreateMultipartForm](#ga2d3c7ad8cd5d670bb4c40b400da52a63) (void)

 | 

Creates a multi-part form.

 |
| 

void [HMS\_Rcp\_DestroyMultipartForm](#ga449c4206aec628b1a0a4a2b9b7aafd53) ([Rcp\_MultipartForm](#ga9f974771548d3ed2054aba0e7506fef9) \*multipartForm)

 | 

Destroys a multi-part form.

 |
| 

uint32\_t [HMS\_Rcp\_SetMultipartFormValue](#ga5148d54bff9d344085c3baa72918dbe9) ([Rcp\_MultipartForm](#ga9f974771548d3ed2054aba0e7506fef9) \*multipartForm, const char \*key, const [Rcp\_MultipartFormFieldValue](../../header-files-and-structs/structs/rcp-multipartformfieldvalue/document.md) \*value)

 | 

Sets key-value pairs in a multi-part form.

 |
| 

[Rcp\_MultipartFormFieldValue](../../header-files-and-structs/structs/rcp-multipartformfieldvalue/document.md) \* [HMS\_Rcp\_GetMultipartFormValue](#ga22d2c7c599edf491eabf84d1eeaee533) ([Rcp\_MultipartForm](#ga9f974771548d3ed2054aba0e7506fef9) \*multipartForm, const char \*key)

 | 

Obtains a value based on a key from a multi-part form.

 |
| 

[Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982) \* [HMS\_Rcp\_CreateHeaders](#gab797b6fcc146d8b181fb138d424c4800) (void)

 | 

Creates a header for a request or response.

 |
| 

void [HMS\_Rcp\_DestroyHeaders](#gaee22e11cc947ae599214df9e84a59ae5) ([Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982) \*headers)

 | 

Destroys the header of a request or response.

 |
| 

uint32\_t [HMS\_Rcp\_SetHeaderValue](#gafb04d92353985e2f4f9f6c2950019068) ([Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982) \*headers, const char \*name, const char \*value)

 | 

Sets key-value pairs in a request or response header.

 |
| 

[Rcp\_HeaderValue](../../header-files-and-structs/structs/rcp-headervalue/document.md) \* [HMS\_Rcp\_GetHeaderValue](#ga9c8f0d455b76b21dce29e7d425c31da3) ([Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982) \*headers, const char \*name)

 | 

Obtains a value based on a key from a request or response header.

 |
| 

[Rcp\_HeaderEntry](../../header-files-and-structs/structs/rcp-headerentry/document.md) \* [HMS\_Rcp\_GetHeaderEntries](#ga94edbbabc6b1b76d0e0f729ca618458a) ([Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982) \*headers)

 | 

Obtains all key-value pairs from a request or response header.

 |
| 

void [HMS\_Rcp\_DestroyHeaderEntries](#gabd8ecd09483ea431cd32cc7218a4ed27) ([Rcp\_HeaderEntry](../../header-files-and-structs/structs/rcp-headerentry/document.md) \*headerEntry)

 | 

Destroys all key-value pairs obtained in [HMS\_Rcp\_GetHeaderEntries](#ga94edbbabc6b1b76d0e0f729ca618458a).

 |
| 

[Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md) \* [HMS\_Rcp\_CreateRequest](#ga63b1b532e9b37754281c6bdfdf198597) (const char \*url)

 | 

Creates a request.

 |
| 

void [HMS\_Rcp\_DestroyRequest](#gae2eb219a9afd7ace912e071775058aa2) ([Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md) \*request)

 | 

Destroys a request.

 |
| 

[Rcp\_RequestCookies](#ga44f2b679fefd37e78c43dbcba59d6d50) \* [HMS\_Rcp\_CreateRequestCookies](#gadb2b6465c6c1966d7983f57dda8582fc) (void)

 | 

Creates empty request cookies.

 |
| 

void [HMS\_Rcp\_DestroyRequestCookies](#gaca5c542e4cb61a95d3fbd31ebc07d4d0) ([Rcp\_RequestCookies](#ga44f2b679fefd37e78c43dbcba59d6d50) \*cookies)

 | 

Destroys request cookies.

 |
| 

uint32\_t [HMS\_Rcp\_SetRequestCookieValue](#ga27ca41ecf30e0f3a2d10fad61494130a) ([Rcp\_RequestCookies](#ga44f2b679fefd37e78c43dbcba59d6d50) \*cookies, const char \*name, const char \*value)

 | 

Sets request cookies.

 |
| 

char \* [HMS\_Rcp\_GetRequestCookieValue](#ga43a79371dfb3ff211321d1c18d4864b2) ([Rcp\_RequestCookies](#ga44f2b679fefd37e78c43dbcba59d6d50) \*cookies, const char \*name)

 | 

Obtains the request cookie value by name.

 |
| 

[Rcp\_RequestCookieEntry](../../header-files-and-structs/structs/rcp-requestcookieentry/document.md) \* [HMS\_Rcp\_GetRequestCookieEntries](#ga5980d5baff59f1902ff009e557ae9756) ([Rcp\_RequestCookies](#ga44f2b679fefd37e78c43dbcba59d6d50) \*cookies)

 | 

Obtains all key-value pairs from the request cookies.

 |
| 

void [HMS\_Rcp\_DestroyRequestCookieEntries](#ga4a75fce3b4d0b690eef330836977da14) ([Rcp\_RequestCookieEntry](../../header-files-and-structs/structs/rcp-requestcookieentry/document.md) \*cookieEntry)

 | 

Destroys all key-value pairs related to request cookies obtained from [HMS\_Rcp\_GetRequestCookieValue](#ga43a79371dfb3ff211321d1c18d4864b2).

 |
| 

const char \* [HMS\_Rcp\_GetResponseCookieAttrValue](#ga6538a77ca1dcabe15bb2891f941c377e) ([Rcp\_CookieAttributes](#ga08c7b992199bec7e5acdc50ce8ae2651) \*cookieAttributes, const char \*name)

 | 

Obtains the cookie attribute value by name.

 |
| 

[Rcp\_CookieAttributeEntry](../../header-files-and-structs/structs/rcp-cookieattributeentry/document.md) \* [HMS\_Rcp\_GetResponseCookieAttrEntries](#ga8304b7906b7e81b7135a50d77d6eaf48) ([Rcp\_CookieAttributes](#ga08c7b992199bec7e5acdc50ce8ae2651) \*cookieAttributes)

 | 

Obtains all response cookie attributes from [Rcp\_CookieAttributes](#ga08c7b992199bec7e5acdc50ce8ae2651).

 |
| 

void [HMS\_Rcp\_DestroyResponseCookieAttrEntries](#ga83afc8703c589133bf3768e631157413) ([Rcp\_CookieAttributeEntry](../../header-files-and-structs/structs/rcp-cookieattributeentry/document.md) \*entries)

 | 

Destroys response cookie attributes.

 |
| 

uint32\_t [HMS\_Rcp\_CallNextRequestHandler](#gaa12f2da13b0aa095b7c6ae5e195c1536) ([Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md) \*request, const [Rcp\_RequestHandler](#ga5ac080855c3aaef66c58d5b5b371be2b) \*next, const [Rcp\_ResponseCallbackObject](../../header-files-and-structs/structs/rcp-responsecallbackobject/document.md) \*responseCallback)

 | 

Calls the next interceptor or the **defaultHandler** in [Rcp\_Interceptor](../../header-files-and-structs/structs/rcp-interceptor/document.md).

 |
| 

[Rcp\_Response](../../header-files-and-structs/structs/rcp-response/document.md) \* [HMS\_Rcp\_CallNextSyncRequestHandler](#ga2a4e9df33b7f4c146e6fb1ddc46dc84f) ([Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md) \*request, const [Rcp\_SyncRequestHandler](#ga2067d1b09b33afa0b8237a049687e9ea) \*next, uint32\_t \*errCode)

 | 

Calls the next interceptor or the default handler in [Rcp\_SyncInterceptor](../../header-files-and-structs/structs/rcp-syncinterceptor/document.md).

 |
| 

[Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd) \* [HMS\_Rcp\_CreateSession](#gafc04f552e9d6b90d9d73abbc9535766e) (const [Rcp\_SessionConfiguration](../../header-files-and-structs/structs/rcp-sessionconfiguration/document.md) \*configuration, uint32\_t \*errCode)

 | 

Creates a session.

 |
| 

const char \* [HMS\_Rcp\_GetSessionId](#ga10f2bd857b521b631838b9e2428925c3) ([Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd) \*session)

 | 

Obtains the session ID.

 |
| 

const [Rcp\_SessionConfiguration](../../header-files-and-structs/structs/rcp-sessionconfiguration/document.md) \* [HMS\_Rcp\_GetSessionConfiguration](#ga990339ef86baed18b48fe3ef10031388) ([Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd) \*session)

 | 

Obtains the session configuration.

 |
| 

[Rcp\_Response](../../header-files-and-structs/structs/rcp-response/document.md) \* [HMS\_Rcp\_FetchSync](#ga48a83535a4658e9872ded4b0dd8c812f) ([Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd) \*session, [Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md) \*request, uint32\_t \*errCode)

 | 

Sends a synchronous request and obtains a response.

 |
| 

uint32\_t [HMS\_Rcp\_Fetch](#ga7ea546b69b9ea60ea4716ee64e8b04cb) ([Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd) \*session, [Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md) \*request, const [Rcp\_ResponseCallbackObject](../../header-files-and-structs/structs/rcp-responsecallbackobject/document.md) \*responseCallback)

 | 

Sends an asynchronous request and obtains a response.

 |
| 

uint32\_t [HMS\_Rcp\_CancelRequest](#gae7974f60c9b17a16e853befd391b7f81) ([Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd) \*session, const [Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md) \*request)

 | 

Cancels a request.

 |
| 

uint32\_t [HMS\_Rcp\_CancelSession](#ga4ef7303528c1ce13cf5f1267c0650221) ([Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd) \*session)

 | 

Cancels a session.

 |
| 

uint32\_t [HMS\_Rcp\_CloseSession](#gaf659dbbb59360b9c587fb4081b52dd14) ([Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd) \*\*session)

 | 

Closes a session.

 |
| 

uint32\_t [HMS\_Rcp\_SetRequestOnBinaryDataRecvCallback](#section207321113884) ([Rcp\_Request](#ga98dde966841135537e05053bf4da4d5b) \*request, [Rcp\_OnBinaryReceiveCallback](#section118171139416) onBinaryReceiveCallback)

 | 

Sets a callback function for receiving binary data upon a request. The callback function works the same as [Rcp\_OnDataReceiveCallback](#gacd66d521a147a876e340aed45a3ed1c4) in [Rcp\_Configuration](../../header-files-and-structs/structs/rcp-configuration/document.md). Once set, the callback function will replace [Rcp\_OnDataReceiveCallback](#gacd66d521a147a876e340aed45a3ed1c4) configured in [Rcp\_Configuration](../../header-files-and-structs/structs/rcp-configuration/document.md).

 |
| 

uint32\_t [HMS\_Rcp\_SetRequestOnStatusCodeReceiveCallback](#section10194153116201) ([Rcp\_Request](#ga98dde966841135537e05053bf4da4d5b) \*request, [Rcp\_OnStatusCodeReceiveCallback](#section5616146153312) onStatusCodeReceiveCallback)

 | 

Sets the callback function for receiving a response status code.

 |

#### Macro Description

#### \[h2\]RCP\_HOST\_MAX\_LEN

#define RCP\_HOST\_MAX\_LEN   256

**Description**

Maximum length of a host name.

**Start version**: 5.0.0(12)

#### \[h2\]RCP\_IP\_MAX\_LEN

#define RCP\_IP\_MAX\_LEN   40

**Description**

Maximum length of an IP address.

**Start version**: 5.0.0(12)

#### \[h2\]RCP\_MAX\_CONTENT\_TYPE\_LEN

#define RCP\_MAX\_CONTENT\_TYPE\_LEN   64

**Description**

Maximum length of the content type.

**Start version**: 5.0.0(12)

#### \[h2\]RCP\_MAX\_FILENAME\_LEN

#define RCP\_MAX\_FILENAME\_LEN   128

**Description**

Maximum length of a file name.

**Start version**: 5.0.0(12)

#### \[h2\]RCP\_MAX\_PATH\_LEN

#define RCP\_MAX\_PATH\_LEN   128

**Description**

Maximum path length.

**Start version**: 5.0.0(12)

#### \[h2\]RCP\_MAX\_REQUEST\_ID\_LEN

#define RCP\_MAX\_REQUEST\_ID\_LEN   32

**Description**

Maximum length of a request ID.

**Start version**: 5.0.0(12)

#### \[h2\]RCP\_METHOD\_DELETE

#define RCP\_METHOD\_DELETE   "DELETE"

**Description**

HTTP DELETE method.

**Start version**: 5.0.0(12)

#### \[h2\]RCP\_METHOD\_GET

#define RCP\_METHOD\_GET   "GET"

**Description**

HTTP GET method.

**Start version**: 5.0.0(12)

#### \[h2\]RCP\_METHOD\_HEAD

#define RCP\_METHOD\_HEAD   "HEAD"

**Description**

HTTP HEAD method.

**Start version**: 5.0.0(12)

#### \[h2\]RCP\_METHOD\_OPTIONS

#define RCP\_METHOD\_OPTIONS   "OPTIONS"

**Description**

HTTP OPTIONS method.

**Start version**: 5.0.0(12)

#### \[h2\]RCP\_METHOD\_PATCH

#define RCP\_METHOD\_PATCH   "PATCH"

**Description**

HTTP PATCH method.

**Start version**: 5.0.0(12)

#### \[h2\]RCP\_METHOD\_POST

#define RCP\_METHOD\_POST   "POST"

**Description**

HTTP POST method.

**Start version**: 5.0.0(12)

#### \[h2\]RCP\_METHOD\_PUT

#define RCP\_METHOD\_PUT   "PUT"

**Description**

HTTP PUT method.

**Start version**: 5.0.0(12)

#### \[h2\]RCP\_METHOD\_TRACE

#define RCP\_METHOD\_TRACE   "TRACE"

**Description**

HTTP TRACE method.

**Start version**: 5.0.0(12)

#### Type Description

#### \[h2\]Rcp\_AuthenticationType

typedef enum [Rcp\_AuthenticationType](#gaa1b9ec2bd61b2c95492f45eb0a447bff) [Rcp\_AuthenticationType](#gaa1b9ec2bd61b2c95492f45eb0a447bff)

**Description**

Enumeration type, which indicates the server identity verification type. If the type is not set, negotiation with the server is required.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_Buffer

typedef struct [Rcp\_Buffer](../../header-files-and-structs/structs/rcp-buffer/document.md) [Rcp\_Buffer](../../header-files-and-structs/structs/rcp-buffer/document.md)

**Description**

Text storage struct.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_CertificateAuthority

typedef struct [Rcp\_CertificateAuthority](../../header-files-and-structs/structs/rcp-certificateauthority/document.md) [Rcp\_CertificateAuthority](../../header-files-and-structs/structs/rcp-certificateauthority/document.md)

**Description**

CA used to verify the identity of a remote server.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_CertType

typedef enum [Rcp\_CertType](#ga4f79c1d41b9c586d99f1c22ed81b9aee) [Rcp\_CertType](#ga4f79c1d41b9c586d99f1c22ed81b9aee)

**Description**

Client certificate type.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_ClientCertificate

typedef struct [Rcp\_ClientCertificate](../../header-files-and-structs/structs/rcp-clientcertificate/document.md) [Rcp\_ClientCertificate](../../header-files-and-structs/structs/rcp-clientcertificate/document.md)

**Description**

Client certificate sent to a remote server, which will be used by the server to verify the identity of the client.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_Configuration

typedef struct [Rcp\_Configuration](../../header-files-and-structs/structs/rcp-configuration/document.md) [Rcp\_Configuration](../../header-files-and-structs/structs/rcp-configuration/document.md)

**Description**

Request configuration.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_ConnectionConfiguration

typedef struct [Rcp\_ConnectionConfiguration](../../header-files-and-structs/structs/rcp-connectionconfiguration/document.md) [Rcp\_ConnectionConfiguration](../../header-files-and-structs/structs/rcp-connectionconfiguration/document.md)

**Description**

Connection configuration.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_ContentOrPathOrCallback

typedef struct [Rcp\_ContentOrPathOrCallback](../../header-files-and-structs/structs/rcp-contentorpathorcallback/document.md) [Rcp\_ContentOrPathOrCallback](../../header-files-and-structs/structs/rcp-contentorpathorcallback/document.md)

**Description**

Simple form data field value used in [Rcp\_FormFieldFileValue](../../header-files-and-structs/structs/rcp-formfieldfilevalue/document.md).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_ContentOrPathOrCallbackType

typedef enum [Rcp\_ContentOrPathOrCallbackType](#gaa5a592f4e68a1dd43f5f41e95199a5e4) [Rcp\_ContentOrPathOrCallbackType](#gaa5a592f4e68a1dd43f5f41e95199a5e4)

**Description**

Content, path, or callback type, which is used to distinguish the data used in [Rcp\_ContentOrPathOrCallback](../../header-files-and-structs/structs/rcp-contentorpathorcallback/document.md).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_ContentType

typedef enum [Rcp\_ContentType](#ga05daeab5ad8d265834b4a1b4e61cd8fa) [Rcp\_ContentType](#ga05daeab5ad8d265834b4a1b4e61cd8fa)

**Description**

Content type in [Rcp\_RequestContent](../../header-files-and-structs/structs/rcp-requestcontent/document.md).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_CookieAttributeEntry

typedef struct [Rcp\_CookieAttributeEntry](../../header-files-and-structs/structs/rcp-cookieattributeentry/document.md) [Rcp\_CookieAttributeEntry](../../header-files-and-structs/structs/rcp-cookieattributeentry/document.md)

**Description**

Response cookie attribute entry.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_CookieAttributes

typedef struct [Rcp\_CookieAttributes](#ga08c7b992199bec7e5acdc50ce8ae2651) [Rcp\_CookieAttributes](#ga08c7b992199bec7e5acdc50ce8ae2651)

**Description**

Cookie attribute type in [Rcp\_Response](../../header-files-and-structs/structs/rcp-response/document.md).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_Credential

typedef struct [Rcp\_Credential](../../header-files-and-structs/structs/rcp-credential/document.md) [Rcp\_Credential](../../header-files-and-structs/structs/rcp-credential/document.md)

**Description**

Credential, which needs to be set based on your needs. Some servers or proxy servers require a user name and password for access.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_DebugEvent

typedef enum [Rcp\_DebugEvent](#gadff9eaa1b517bf01defd1273b2eeddbc) [Rcp\_DebugEvent](#gadff9eaa1b517bf01defd1273b2eeddbc)

**Description**

Debugging event type.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_DebugInfo

typedef struct [Rcp\_DebugInfo](../../header-files-and-structs/structs/rcp-debuginfo/document.md) [Rcp\_DebugInfo](../../header-files-and-structs/structs/rcp-debuginfo/document.md)

**Description**

Structure of the debugging information stored in [Rcp\_Response](../../header-files-and-structs/structs/rcp-response/document.md).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_DnsConfiguration

typedef struct [Rcp\_DnsConfiguration](../../header-files-and-structs/structs/rcp-dnsconfiguration/document.md) [Rcp\_DnsConfiguration](../../header-files-and-structs/structs/rcp-dnsconfiguration/document.md)

**Description**

DNS resolution configuration.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_DnsOverHttps

typedef struct [Rcp\_DnsOverHttps](../../header-files-and-structs/structs/rcp-dnsoverhttps/document.md) [Rcp\_DnsOverHttps](../../header-files-and-structs/structs/rcp-dnsoverhttps/document.md)

**Description**

DNS over HTTPS. If this information is configured, addresses resolved by the DOH DNS server will be preferred.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_DnsRule

typedef struct [Rcp\_DnsRule](../../header-files-and-structs/structs/rcp-dnsrule/document.md) [Rcp\_DnsRule](../../header-files-and-structs/structs/rcp-dnsrule/document.md)

**Description**

DNS rule configuration.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_DnsRuleType

typedef enum [Rcp\_DnsRuleType](#ga995c92778c5b31c9b4b586c737cfdd3c) [Rcp\_DnsRuleType](#ga995c92778c5b31c9b4b586c737cfdd3c)

**Description**

DNS rule type in [Rcp\_DnsRule](../../header-files-and-structs/structs/rcp-dnsrule/document.md).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_DnsServers

typedef struct [Rcp\_DnsServers](../../header-files-and-structs/structs/rcp-dnsservers/document.md) [Rcp\_DnsServers](../../header-files-and-structs/structs/rcp-dnsservers/document.md)

**Description**

DNS server, which is one of the types defined in [Rcp\_DnsConfiguration.dnsRules](../../header-files-and-structs/structs/rcp-dnsconfiguration/document.md#ab09aacb68c682d9beea100cae481eaa4).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_DynamicDnsRuleFunction

typedef [Rcp\_IpAddress](../../header-files-and-structs/structs/rcp-ipaddress/document.md)\*(\* Rcp\_DynamicDnsRuleFunction) (const char \*host, uint16\_t port)

**Description**

Function that can directly return an IP address based on the host name and port number. It is used for dynamic DNS resolution.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

host

 | 

Host name.

 |
| 

port

 | 

Port number.

 |

**Returns**:

**Rcp\_IpAddress\***: pointer to [Rcp\_IpAddress](../../header-files-and-structs/structs/rcp-ipaddress/document.md). The IP address is matched based on the host name and port number.

#### \[h2\]Rcp\_EventsHandler

typedef struct [Rcp\_EventsHandler](../../header-files-and-structs/structs/rcp-eventshandler/document.md) [Rcp\_EventsHandler](../../header-files-and-structs/structs/rcp-eventshandler/document.md)

**Description**

Callback function for listening on various HTTP events.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_ExclusionFunction

typedef bool(\* Rcp\_ExclusionFunction) (const char \*url)

**Description**

Pointer to the function for determining whether a host uses a proxy.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

url

 | 

Requested URL.

 |

**Returns**:

A Boolean value indicating that whether to use a proxy server.

#### \[h2\]Rcp\_Exclusions

typedef struct [Rcp\_Exclusions](../../header-files-and-structs/structs/rcp-exclusions/document.md) [Rcp\_Exclusions](../../header-files-and-structs/structs/rcp-exclusions/document.md)

**Description**

URLs excluded from proxy processing.

If [Rcp\_Request.url](../../header-files-and-structs/structs/rcp-request/document.md#a39a1cc0a1ad666d8d9ad40eec4b52de7) matches a pattern defined in [Rcp\_Exclusions](../../header-files-and-structs/structs/rcp-exclusions/document.md), [Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md) will not go through proxy processing.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_ExclusionsValueType

typedef enum [Rcp\_ExclusionsValueType](#ga1f5ed8748d80bca8e803ea26d63d1ecf) [Rcp\_ExclusionsValueType](#ga1f5ed8748d80bca8e803ea26d63d1ecf)

**Description**

Data type in [Rcp\_Exclusions](../../header-files-and-structs/structs/rcp-exclusions/document.md).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_Form

typedef struct [Rcp\_Form](#ga40787f67faf4ea7111e4cda03f3f16be) [Rcp\_Form](#ga40787f67faf4ea7111e4cda03f3f16be)

**Description**

Simple form data.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_FormFieldFileValue

typedef struct [Rcp\_FormFieldFileValue](../../header-files-and-structs/structs/rcp-formfieldfilevalue/document.md) [Rcp\_FormFieldFileValue](../../header-files-and-structs/structs/rcp-formfieldfilevalue/document.md)

**Description**

Form field file value.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_FormFieldValue

typedef struct [Rcp\_FormFieldValue](../../header-files-and-structs/structs/rcp-formfieldvalue/document.md) [Rcp\_FormFieldValue](../../header-files-and-structs/structs/rcp-formfieldvalue/document.md)

**Description**

Simple form data field value. For details, please refer to [Rcp\_Form](#ga40787f67faf4ea7111e4cda03f3f16be) and [Rcp\_MultipartFormFieldValue](../../header-files-and-structs/structs/rcp-multipartformfieldvalue/document.md).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_FormValueType

typedef enum [Rcp\_FormValueType](#ga9d851389347a39bd4bb849ac31cfa478) [Rcp\_FormValueType](#ga9d851389347a39bd4bb849ac31cfa478)

**Description**

Form value type.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_GetDataCallback

typedef int(\* Rcp\_GetDataCallback) (char \*out, uint32\_t size)

**Description**

Data obtained through a callback function. This callback is used when the API needs to send the next part of the data to the server.

This callback function can be used in [Rcp\_FormFieldFileValue.contentOrPathOrCb](../../header-files-and-structs/structs/rcp-formfieldfilevalue/document.md#ae23c275b9e2f237b5e4492f998a7e7e4) and [Rcp\_RequestContent](../../header-files-and-structs/structs/rcp-requestcontent/document.md).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

out

 | 

Output data.

 |
| 

size

 | 

Data size.

 |

**Returns**:

**\-1** if an error occurs and **0** if the transmission stops. The return value is an integer.

#### \[h2\]Rcp\_HeaderEntry

typedef struct [Rcp\_HeaderEntry](../../header-files-and-structs/structs/rcp-headerentry/document.md) [Rcp\_HeaderEntry](../../header-files-and-structs/structs/rcp-headerentry/document.md)

**Description**

All key-value pairs in the request or response header.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_Headers

typedef struct [Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982) [Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982)

**Description**

Header of a request or response.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_HeaderValue

typedef struct [Rcp\_HeaderValue](../../header-files-and-structs/structs/rcp-headervalue/document.md) [Rcp\_HeaderValue](../../header-files-and-structs/structs/rcp-headervalue/document.md)

**Description**

Value type of a mapped value in a request or response header.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_InfoToCollect

typedef struct [Rcp\_InfoToCollect](../../header-files-and-structs/structs/rcp-infotocollect/document.md) [Rcp\_InfoToCollect](../../header-files-and-structs/structs/rcp-infotocollect/document.md)

**Description**

Request processing events to be collected. You can check the response object for collected events.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_Interceptor

typedef struct [Rcp\_Interceptor](../../header-files-and-structs/structs/rcp-interceptor/document.md) [Rcp\_Interceptor](../../header-files-and-structs/structs/rcp-interceptor/document.md)

**Description**

Asynchronous interceptor.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_InterceptorArray

typedef struct [Rcp\_InterceptorArray](../../header-files-and-structs/structs/rcp-interceptorarray/document.md) [Rcp\_InterceptorArray](../../header-files-and-structs/structs/rcp-interceptorarray/document.md)

**Description**

Asynchronous interceptor array.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_IpAddress

typedef struct [Rcp\_IpAddress](../../header-files-and-structs/structs/rcp-ipaddress/document.md) [Rcp\_IpAddress](../../header-files-and-structs/structs/rcp-ipaddress/document.md)

**Description**

IP address group used by the static DNS rule [Rcp\_StaticDnsRuleItem](../../header-files-and-structs/structs/rcp-staticdnsruleitem/document.md).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_IpAndPort

typedef struct [Rcp\_IpAndPort](../../header-files-and-structs/structs/rcp-ipandport/document.md) [Rcp\_IpAndPort](../../header-files-and-structs/structs/rcp-ipandport/document.md)

**Description**

IP address and port number of a DNS server, which will be used in [Rcp\_DnsServers](../../header-files-and-structs/structs/rcp-dnsservers/document.md).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_MultipartForm

typedef struct [Rcp\_MultipartForm](#ga9f974771548d3ed2054aba0e7506fef9) [Rcp\_MultipartForm](#ga9f974771548d3ed2054aba0e7506fef9)

**Description**

Multi-part form data.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_MultipartFormFieldValue

typedef struct [Rcp\_MultipartFormFieldValue](../../header-files-and-structs/structs/rcp-multipartformfieldvalue/document.md) [Rcp\_MultipartFormFieldValue](../../header-files-and-structs/structs/rcp-multipartformfieldvalue/document.md)

**Description**

Multi-part form field value, which will be used in [Rcp\_MultipartForm](#ga9f974771548d3ed2054aba0e7506fef9).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_MultipartValueType

typedef enum [Rcp\_MultipartValueType](#ga76d003b4f9a244c9d11def4128ceeda8) [Rcp\_MultipartValueType](#ga76d003b4f9a244c9d11def4128ceeda8)

**Description**

Multi-part form value type, which is used to distinguish the data used in [Rcp\_MultipartFormFieldValue](../../header-files-and-structs/structs/rcp-multipartformfieldvalue/document.md).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_OnDataReceiveCallback

typedef struct [Rcp\_OnDataReceiveCallback](../../header-files-and-structs/structs/rcp-ondatareceivecallback/document.md) [Rcp\_OnDataReceiveCallback](../../header-files-and-structs/structs/rcp-ondatareceivecallback/document.md)

**Description**

Callback triggered upon data receiving events, which is configured in [Rcp\_EventsHandler](../../header-files-and-structs/structs/rcp-eventshandler/document.md).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_OnDataReceiveCallbackFunc

typedef size\_t(\* Rcp\_OnDataReceiveCallbackFunc) (void \*usrObject, const char \*data)

**Description**

Callback function triggered when a response body is returned.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

usrObject

 | 

Custom object.

 |
| 

data

 | 

Response body.

 |

**Returns**:

Length of the response body. The value is of the size\_t type.

#### \[h2\]Rcp\_OnBinaryReceiveCallback

typedef struct [Rcp\_OnBinaryReceiveCallback](../../header-files-and-structs/structs/rcp-onbinaryreceivecallback/document.md) [Rcp\_OnBinaryReceiveCallback](../../header-files-and-structs/structs/rcp-onbinaryreceivecallback/document.md)

**Description**

Callback function for receiving binary data in a response.

**Start version**: 5.0.1(13)

#### \[h2\]Rcp\_OnBinaryReceiveCallbackFunc

typedef size\_t(\* Rcp\_OnBinaryReceiveCallbackFunc) (void \*usrObject, [Rcp\_Buffer](#ga74d7d9dd56fabaa773cf1659c2d2eace) \*buffer)

**Description**

Defines the binary data callback function triggered when a response body is returned. The callback point is the same as [Rcp\_OnDataReceiveCallback](#gacd66d521a147a876e340aed45a3ed1c4) in [Rcp\_Configuration](../../header-files-and-structs/structs/rcp-configuration/document.md). If the callback function is configured, it will substitute [Rcp\_OnDataReceiveCallback](#gacd66d521a147a876e340aed45a3ed1c4) configured in [Rcp\_Configuration](../../header-files-and-structs/structs/rcp-configuration/document.md) for receiving data of the character type.

**Start version**: 5.0.1(13)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

usrObject

 | 

Custom object.

 |
| 

buffer

 | 

Binary data in the response body.

 |

**Returns**:

size\_t, which indicates length of the binary data in the response body.

#### \[h2\]Rcp\_OnStatusCodeReceiveCallback

typedef struct [Rcp\_OnStatusCodeReceiveCallback](../../header-files-and-structs/structs/rcp-onstatuscodereceivecallback/document.md) [Rcp\_OnStatusCodeReceiveCallback](../../header-files-and-structs/structs/rcp-onstatuscodereceivecallback/document.md)

**Description**

Callback function used to receive a response status code.

**Start version**: 6.0.1(21)

#### \[h2\]Rcp\_OnStatusCodeReceiveCallbackFunc

typedef void (\*Rcp\_OnStatusCodeReceiveCallbackFunc) (void \*usrObject, uint32\_t statusCode)

**Description**

Callback function triggered when a response status code is returned.

**Start version**: 6.0.1(21)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

usrObject

 | 

Custom object.

 |
| 

statusCode

 | 

Response status code.

 |

#### \[h2\]Rcp\_OnHeaderReceiveCallback

typedef struct [Rcp\_OnHeaderReceiveCallback](../../header-files-and-structs/structs/rcp-onheaderreceivecallback/document.md) [Rcp\_OnHeaderReceiveCallback](../../header-files-and-structs/structs/rcp-onheaderreceivecallback/document.md)

**Description**

Callback triggered upon header receiving events, which is configured in [Rcp\_EventsHandler](../../header-files-and-structs/structs/rcp-eventshandler/document.md).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_OnHeaderReceiveCallbackFunc

typedef void(\* Rcp\_OnHeaderReceiveCallbackFunc) (void \*usrObject, [Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982) \*headers)

**Description**

Callback function triggered when all requests are received.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

usrObject

 | 

Custom object.

 |
| 

headers

 | 

Pointer to [Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982).

 |

#### \[h2\]Rcp\_OnProgressCallback

typedef struct [Rcp\_OnProgressCallback](../../header-files-and-structs/structs/rcp-onprogresscallback/document.md) [Rcp\_OnProgressCallback](../../header-files-and-structs/structs/rcp-onprogresscallback/document.md)

**Description**

Callback triggered upon data transmission events, which is configured in [Rcp\_EventsHandler](../../header-files-and-structs/structs/rcp-eventshandler/document.md).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_OnProgressCallbackFunc

typedef void(\* Rcp\_OnProgressCallbackFunc) (void \*usrObject, uint64\_t totalSize, uint64\_t transferredSize)

**Description**

Callback function triggered during request/response data transmission.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

usrObject

 | 

Custom object.

 |
| 

totalSize

 | 

Total data size.

 |
| 

transferredSize

 | 

Size of transferred data.

 |

#### \[h2\]Rcp\_OnVoidCallback

typedef struct [Rcp\_OnVoidCallback](../../header-files-and-structs/structs/rcp-onvoidcallback/document.md) [Rcp\_OnVoidCallback](../../header-files-and-structs/structs/rcp-onvoidcallback/document.md)

**Description**

Callback triggered upon transmigration ending or cancellation events, which is configured in [Rcp\_EventsHandler](../../header-files-and-structs/structs/rcp-eventshandler/document.md).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_OnVoidCallbackFunc

typedef void(\* Rcp\_OnVoidCallbackFunc) (void \*usrObject)

**Description**

Callback function for listening on DataEnd and Canceled events of requests.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

usrObject

 | 

Custom object.

 |

#### \[h2\]Rcp\_PathPreference

typedef enum [Rcp\_PathPreference](#ga9498d24addbd529f258fd6faacfd9c67) [Rcp\_PathPreference](#ga9498d24addbd529f258fd6faacfd9c67)

**Description**

Request path preferences.

The configuration is only for system reference and the final path is determined by the system.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_ProxyConfiguration

typedef struct [Rcp\_ProxyConfiguration](../../header-files-and-structs/structs/rcp-proxyconfiguration/document.md) [Rcp\_ProxyConfiguration](../../header-files-and-structs/structs/rcp-proxyconfiguration/document.md)

**Description**

Proxy configuration.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_ProxyTunnelMode

typedef enum [Rcp\_ProxyTunnelMode](#ga7ae11929cb19cd85be3dd97e712e2ac6) [Rcp\_ProxyTunnelMode](#ga7ae11929cb19cd85be3dd97e712e2ac6)

**Description**

Indicates when a proxy tunnel needs to be established. Tunneling, or tunnel transmission, is a process where an HTTP CONNECT request is sent to a proxy server, instructing it to establish a connection to the remote host of a specified port number. Once this connection is set up, all subsequent traffic is routed through the proxy. The value **auto** indicates that a tunnel will be created for HTTPS traffic but not for HTTP traffic. The value **always** indicates that tunneling is enabled for all traffic.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_ProxyType

typedef enum [Rcp\_ProxyType](#gacfad61d189683cbc02c969a63e246ca1) [Rcp\_ProxyType](#gacfad61d189683cbc02c969a63e246ca1)

**Description**

Proxy type, which will be used to determine which proxy configuration will be used.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_RemoteValidationType

typedef enum [Rcp\_RemoteValidationType](#gaf9356aea6a8c2e447efe3cf7fa889b87) [Rcp\_RemoteValidationType](#gaf9356aea6a8c2e447efe3cf7fa889b87)

**Description**

Remote server validation type.

It is used to specify the CA used to verify the identity of the remote server and is described in [Rcp\_SecurityConfiguration](../../header-files-and-structs/structs/rcp-securityconfiguration/document.md).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_Request

typedef struct [Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md) [Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md)

**Description**

Network request.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_RequestContent

typedef struct [Rcp\_RequestContent](../../header-files-and-structs/structs/rcp-requestcontent/document.md) [Rcp\_RequestContent](../../header-files-and-structs/structs/rcp-requestcontent/document.md)

**Description**

Request content.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_RequestCookieEntry

typedef struct [Rcp\_RequestCookieEntry](../../header-files-and-structs/structs/rcp-requestcookieentry/document.md) [Rcp\_RequestCookieEntry](../../header-files-and-structs/structs/rcp-requestcookieentry/document.md)

**Description**

All cookie key-value pairs in the request.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_RequestCookies

typedef struct [Rcp\_RequestCookies](#ga44f2b679fefd37e78c43dbcba59d6d50) [Rcp\_RequestCookies](#ga44f2b679fefd37e78c43dbcba59d6d50)

**Description**

Request cookies.

You can specify all cookies you need in an object, for example, {'name1':'value1','name2':'value2'}.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_RequestHandler

typedef struct [Rcp\_RequestHandler](#ga5ac080855c3aaef66c58d5b5b371be2b) [Rcp\_RequestHandler](#ga5ac080855c3aaef66c58d5b5b371be2b)

**Description**

Asynchronous handler associated with [Rcp\_Interceptor](../../header-files-and-structs/structs/rcp-interceptor/document.md).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_Response

typedef struct [Rcp\_Response](../../header-files-and-structs/structs/rcp-response/document.md) [Rcp\_Response](../../header-files-and-structs/structs/rcp-response/document.md)

**Description**

Response to a network request.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_ResponseCallback

typedef void(\* Rcp\_ResponseCallback) (void \*usrCtx, [Rcp\_Response](../../header-files-and-structs/structs/rcp-response/document.md) \*response, uint32\_t errCode)

**Description**

Pointer to the response callback function.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

usrCtx

 | 

User context.

 |
| 

response

 | 

Pointer to [Rcp\_Response](../../header-files-and-structs/structs/rcp-response/document.md).

 |
| 

errCode

 | 

\[out\]: common error codes.

-   **0**: Request successful.
-   **1007900001**: Unsupported protocol.
-   **1007900003**: Invalid URL format or missing URL.
-   **1007900005**: Unable to resolve the proxy name.
-   **1007900006**: Unable to resolve the host name.
-   **1007900007**: Unable to connect to the server.
-   **1007900008**: Abnormal server response.
-   **1007900009**: Access to a remote resource was rejected.
-   **1007900016**: An HTTP/2-frame error occurred.
-   **1007900018**: A part of the file has been transmitted.
-   **1007900025**: Upload failed.
-   **1007900026**: Failed to open or read local data from a file or app.
-   **1007900027**: Insufficient memory.
-   **1007900028**: The timeout interval has expired.
-   **1007900047**: The number of redirections has reached the maximum.
-   **1007900052**: No data returned from the server.
-   **1007900055**: Failed to send data to the peer.
-   **1007900056**: Failed to receive data from the peer.
-   **1007900058**: Invalid local SSL certificate.
-   **1007900059**: Unable to use the specified SSL key.
-   **1007900060**: The SSL peer certificate or SSH remote key is invalid.
-   **1007900061**: The HTTP content or transport encoding cannot be identified or is incorrect.
-   **1007900063**: The file size exceeded the maximum.
-   **1007900070**: The disk is full or the allocated quota is used up.
-   **1007900073**: The remote file already exists.
-   **1007900077**: Invalid SSL CA certificate.
-   **1007900078**: Cannot find the remote file.
-   **1007900992**: The request has been canceled.
-   **1007900993**: The session is closed or invalid.
-   **1007900094**: The identity verification function returned an error.
-   **1007900995**: Failed to obtain the system proxy.
-   **1007900996**: The proxy type is not supported.
-   **1007900997**: Invalid content type.
-   **1007900998**: The method is not supported.
-   **1007900999**: Internal error.

Other error codes are in the format of 1007900000 + Curl error code. For more error codes, please refer to [Curl error codes](https://curl.se/libcurl/c/libcurl-errors.html).

 |

#### \[h2\]Rcp\_ResponseCallbackObject

typedef struct [Rcp\_ResponseCallbackObject](../../header-files-and-structs/structs/rcp-responsecallbackobject/document.md) [Rcp\_ResponseCallbackObject](../../header-files-and-structs/structs/rcp-responsecallbackobject/document.md)

**Description**

Response callback struct.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_ResponseCookies

typedef struct [Rcp\_ResponseCookies](../../header-files-and-structs/structs/rcp-responsecookies/document.md) [Rcp\_ResponseCookies](../../header-files-and-structs/structs/rcp-responsecookies/document.md)

**Description**

Response cookies.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_SecurityConfiguration

typedef struct [Rcp\_SecurityConfiguration](../../header-files-and-structs/structs/rcp-securityconfiguration/document.md) [Rcp\_SecurityConfiguration](../../header-files-and-structs/structs/rcp-securityconfiguration/document.md)

**Description**

Request security configuration.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_ServerAuthentication

typedef struct [Rcp\_ServerAuthentication](../../header-files-and-structs/structs/rcp-serverauthentication/document.md) [Rcp\_ServerAuthentication](../../header-files-and-structs/structs/rcp-serverauthentication/document.md)

**Description**

Server identity verification information.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_Session

typedef struct [Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd) [Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd)

**Description**

Session.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_SessionConfiguration

typedef struct [Rcp\_SessionConfiguration](../../header-files-and-structs/structs/rcp-sessionconfiguration/document.md) [Rcp\_SessionConfiguration](../../header-files-and-structs/structs/rcp-sessionconfiguration/document.md)

**Description**

Session configuration.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_SessionListener

typedef struct [Rcp\_SessionListener](../../header-files-and-structs/structs/rcp-sessionlistener/document.md) [Rcp\_SessionListener](../../header-files-and-structs/structs/rcp-sessionlistener/document.md)

**Description**

Callback function for listening on session closing or cancellation events.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_SessionType

typedef enum [Rcp\_SessionType](#ga4fa3aa6821b16425c260d837deace956) [Rcp\_SessionType](#ga4fa3aa6821b16425c260d837deace956)

**Description**

Session type.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_StaticDnsRule

typedef struct [Rcp\_StaticDnsRule](../../header-files-and-structs/structs/rcp-staticdnsrule/document.md) [Rcp\_StaticDnsRule](../../header-files-and-structs/structs/rcp-staticdnsrule/document.md)

**Description**

Static DNS rule.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_StaticDnsRuleItem

typedef struct [Rcp\_StaticDnsRuleItem](../../header-files-and-structs/structs/rcp-staticdnsruleitem/document.md) [Rcp\_StaticDnsRuleItem](../../header-files-and-structs/structs/rcp-staticdnsruleitem/document.md)

**Description**

Description about a single static DNS rule.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_StatusCode

typedef enum [Rcp\_StatusCode](#ga97929a5349f04300f50318f50393b93e) [Rcp\_StatusCode](#ga97929a5349f04300f50318f50393b93e)

**Description**

Response status code.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_SyncInterceptor

typedef struct [Rcp\_SyncInterceptor](../../header-files-and-structs/structs/rcp-syncinterceptor/document.md) [Rcp\_SyncInterceptor](../../header-files-and-structs/structs/rcp-syncinterceptor/document.md)

**Description**

Synchronous interceptor.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_SyncInterceptorArray

typedef struct [Rcp\_SyncInterceptorArray](../../header-files-and-structs/structs/rcp-syncinterceptorarray/document.md) [Rcp\_SyncInterceptorArray](../../header-files-and-structs/structs/rcp-syncinterceptorarray/document.md)

**Description**

Synchronous interceptor array.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_SyncRequestHandler

typedef struct [Rcp\_SyncRequestHandler](#ga2067d1b09b33afa0b8237a049687e9ea) [Rcp\_SyncRequestHandler](#ga2067d1b09b33afa0b8237a049687e9ea)

**Description**

Synchronous handler associated with [Rcp\_SyncInterceptor](../../header-files-and-structs/structs/rcp-syncinterceptor/document.md).

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_TimeInfo

typedef struct [Rcp\_TimeInfo](../../header-files-and-structs/structs/rcp-timeinfo/document.md) [Rcp\_TimeInfo](../../header-files-and-structs/structs/rcp-timeinfo/document.md)

**Description**

Response timer information.

It will be collected in [Rcp\_Response.timeInfo](../../header-files-and-structs/structs/rcp-response/document.md#a57d437be63e686ada47b96b3126067d8). [Rcp\_TracingConfiguration.collectTimeInfo](../../header-files-and-structs/structs/rcp-tracingconfiguration/document.md#aded07a3d27e7524e18362082264b9b94) specifies whether to collect the information.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_Timeout

typedef struct [Rcp\_Timeout](../../header-files-and-structs/structs/rcp-timeout/document.md) [Rcp\_Timeout](../../header-files-and-structs/structs/rcp-timeout/document.md)

**Description**

Request timeout configuration.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_TracingConfiguration

typedef struct [Rcp\_TracingConfiguration](../../header-files-and-structs/structs/rcp-tracingconfiguration/document.md) [Rcp\_TracingConfiguration](../../header-files-and-structs/structs/rcp-tracingconfiguration/document.md)

**Description**

Request tracing configuration.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_TransferConfiguration

typedef struct [Rcp\_TransferConfiguration](../../header-files-and-structs/structs/rcp-transferconfiguration/document.md) [Rcp\_TransferConfiguration](../../header-files-and-structs/structs/rcp-transferconfiguration/document.md)

**Description**

Transmission configuration.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_TransferRange

typedef struct [Rcp\_TransferRange](../../header-files-and-structs/structs/rcp-transferrange/document.md) [Rcp\_TransferRange](../../header-files-and-structs/structs/rcp-transferrange/document.md)

**Description**

HTTP transmission range. This configuration will be converted into the HTTP Range header. An HTTP request with such a header requires the server to return only a part of the HTTP response.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_Urls

typedef struct [Rcp\_Urls](../../header-files-and-structs/structs/rcp-urls/document.md) [Rcp\_Urls](../../header-files-and-structs/structs/rcp-urls/document.md)

**Description**

URLs, which are used to determine whether a host is using a proxy.

**Start version**: 5.0.0(12)

#### \[h2\]Rcp\_WebProxy

typedef struct [Rcp\_WebProxy](../../header-files-and-structs/structs/rcp-webproxy/document.md) [Rcp\_WebProxy](../../header-files-and-structs/structs/rcp-webproxy/document.md)

**Description**

Custom proxy configuration.

**Start version**: 5.0.0(12)

#### Enumeration Description

#### \[h2\]Rcp\_AuthenticationType

enum [Rcp\_AuthenticationType](#gaa1b9ec2bd61b2c95492f45eb0a447bff)

**Description**

Server identity verification type, which is an enumeration. If the type is not set, negotiation with the server is required.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

RCP\_AUTHENTICATION\_AUTO

 | 

Automatic.

 |
| 

RCP\_AUTHENTICATION\_BASIC

 | 

Basic.

 |
| 

RCP\_AUTHENTICATION\_NTLM

 | 

NTLM.

 |
| 

RCP\_AUTHENTICATION\_DIGEST

 | 

DIGEST.

 |

#### \[h2\]Rcp\_CertType

enum [Rcp\_CertType](#ga4f79c1d41b9c586d99f1c22ed81b9aee)

**Description**

Client certificate type.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

RCP\_CERT\_PEM

 | 

PEM.

 |
| 

RCP\_CERT\_DER

 | 

DER.

 |
| 

RCP\_CERT\_P12

 | 

P12.

 |

#### \[h2\]Rcp\_ContentOrPathOrCallbackType

enum [Rcp\_ContentOrPathOrCallbackType](#gaa5a592f4e68a1dd43f5f41e95199a5e4)

**Description**

Content, path, or callback type, which is used to distinguish the data used in [Rcp\_ContentOrPathOrCallback](../../header-files-and-structs/structs/rcp-contentorpathorcallback/document.md).

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

RCP\_FILE\_VALUE\_TYPE\_CONTENT

 | 

Content.

 |
| 

RCP\_FILE\_VALUE\_TYPE\_PATH

 | 

Path.

 |
| 

RCP\_FILE\_VALUE\_TYPE\_CALLBACK

 | 

Callback.

 |

#### \[h2\]Rcp\_ContentType

enum [Rcp\_ContentType](#ga05daeab5ad8d265834b4a1b4e61cd8fa)

**Description**

Content type in [Rcp\_RequestContent](../../header-files-and-structs/structs/rcp-requestcontent/document.md).

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

RCP\_CONTENT\_TYPE\_STRING

 | 

Text.

 |
| 

RCP\_CONTENT\_TYPE\_FORM

 | 

Simple form.

 |
| 

RCP\_CONTENT\_TYPE\_MULTIPARTFORM

 | 

Multi-part form.

 |
| 

RCP\_CONTENT\_TYPE\_GETCALLBACK

 | 

Callback function.

 |

#### \[h2\]Rcp\_DebugEvent

enum [Rcp\_DebugEvent](#gadff9eaa1b517bf01defd1273b2eeddbc)

**Description**

Debugging event type.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

RCP\_DEBUG\_EVENT\_TEXT

 | 

Text event.

 |
| 

RCP\_DEBUG\_EVENT\_HEADER\_IN

 | 

Header transfer-in event.

 |
| 

RCP\_DEBUG\_EVENT\_HEADER\_OUT

 | 

Header transfer-out event.

 |
| 

RCP\_DEBUG\_EVENT\_DATA\_IN

 | 

Data transfer-in event.

 |
| 

RCP\_DEBUG\_EVENT\_DATA\_OUT

 | 

Data transfer-out event.

 |
| 

RCP\_DEBUG\_EVENT\_SSL\_DATA\_IN

 | 

SSL/TLS transfer-in event.

 |
| 

RCP\_DEBUG\_EVENT\_SSL\_DATA\_OUT

 | 

SSL/TLS transfer-out event.

 |

#### \[h2\]Rcp\_DnsRuleType

enum [Rcp\_DnsRuleType](#ga995c92778c5b31c9b4b586c737cfdd3c)

**Description**

DNS rule type in [Rcp\_DnsRule](../../header-files-and-structs/structs/rcp-dnsrule/document.md).

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

RCP\_DNS\_RULE\_DNS\_SERVERS

 | 

DNS server.

 |
| 

RCP\_DNS\_RULE\_STATIC

 | 

Static DNS rule.

 |
| 

RCP\_DNS\_RULE\_DYNAMIC

 | 

Dynamic DNS rule.

 |

#### \[h2\]Rcp\_ExclusionsValueType

enum [Rcp\_ExclusionsValueType](#ga1f5ed8748d80bca8e803ea26d63d1ecf)

**Description**

Data type in [Rcp\_Exclusions](../../header-files-and-structs/structs/rcp-exclusions/document.md).

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

RCP\_EXCLUSION\_USE\_URL\_ARRAY

 | 

URLs are used in [Rcp\_Exclusions](../../header-files-and-structs/structs/rcp-exclusions/document.md).

 |
| 

RCP\_EXCLUSION\_USE\_CALLBACK

 | 

The callback function [Rcp\_ExclusionFunction](#gac6517b72e4a8c0feaf864f3669d2c127) is used in [Rcp\_Exclusions](../../header-files-and-structs/structs/rcp-exclusions/document.md).

 |

#### \[h2\]Rcp\_FormValueType

enum [Rcp\_FormValueType](#ga9d851389347a39bd4bb849ac31cfa478)

**Description**

Form value type.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

RCP\_FORM\_VALUE\_TYPE\_INT32

 | 

Int32 data.

 |
| 

RCP\_FORM\_VALUE\_TYPE\_INT64

 | 

Int64 data.

 |
| 

RCP\_FORM\_VALUE\_TYPE\_BOOL

 | 

Boolean data.

 |
| 

RCP\_FORM\_VALUE\_TYPE\_STRING

 | 

String.

 |
| 

RCP\_FORM\_VALUE\_TYPE\_DOUBLE

 | 

Double data.

 |

#### \[h2\]Rcp\_MultipartValueType

enum [Rcp\_MultipartValueType](#ga76d003b4f9a244c9d11def4128ceeda8)

**Description**

Multi-part form value type, which is used to distinguish the data used in [Rcp\_MultipartFormFieldValue](../../header-files-and-structs/structs/rcp-multipartformfieldvalue/document.md).

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

RCP\_TYPE\_FORM\_FIELD\_VALUE

 | 

[Rcp\_FormFieldValue](../../header-files-and-structs/structs/rcp-formfieldvalue/document.md).

 |
| 

RCP\_TYPE\_FORM\_FIELD\_FILE\_VALUE

 | 

[Rcp\_FormFieldFileValue](../../header-files-and-structs/structs/rcp-formfieldfilevalue/document.md).

 |

#### \[h2\]Rcp\_PathPreference

enum [Rcp\_PathPreference](#ga9498d24addbd529f258fd6faacfd9c67)

**Description**

Request path preferences.

The configuration is only for system reference and the final path is determined by the system.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

RCP\_PATH\_PREFERENCE\_AUTO

 | 

Automatic.

 |
| 

RCP\_PATH\_PREFERENCE\_WIFI

 | 

Wi-Fi network preferred.

 |
| 

RCP\_PATH\_PREFERENCE\_CELLULAR

 | 

Cellular network preferred.

 |

#### \[h2\]Rcp\_ProxyTunnelMode

enum [Rcp\_ProxyTunnelMode](#ga7ae11929cb19cd85be3dd97e712e2ac6)

**Description**

Indicates when a proxy tunnel needs to be established. Tunneling, or tunnel transmission, is a process where an HTTP CONNECT request is sent to a proxy server, instructing it to establish a connection to the remote host of a specified port number. Once this connection is set up, all subsequent traffic is routed through the proxy. The value **auto** indicates that a tunnel will be created for HTTPS traffic but not for HTTP traffic. The value **always** indicates that tunneling is enabled for all traffic.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

RCP\_PROXY\_TUNNEL\_AUTO

 | 

Automatic.

 |
| 

RCP\_PROXY\_TUNNEL\_ALWAYS

 | 

Tunneling is enabled for all traffic.

 |

#### \[h2\]Rcp\_ProxyType

enum [Rcp\_ProxyType](#gacfad61d189683cbc02c969a63e246ca1)

**Description**

Proxy type, which will be used to determine which proxy configuration will be used.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

RCP\_PROXY\_SYSTEM

 | 

System proxy.

 |
| 

RCP\_PROXY\_CUSTOM

 | 

Custom proxy. If this option is selected, [Rcp\_ProxyConfiguration.customProxy](../../header-files-and-structs/structs/rcp-proxyconfiguration/document.md#a01dc17cde923a3499c90dd116ad68468) will be resolved.

 |
| 

RCP\_PROXY\_NO\_PROXY

 | 

No proxy.

 |

#### \[h2\]Rcp\_RemoteValidationType

enum [Rcp\_RemoteValidationType](#gaf9356aea6a8c2e447efe3cf7fa889b87)

**Description**

Remote server validation type.

It is used to specify the CA used to verify the identity of the remote server and is described in [Rcp\_SecurityConfiguration](../../header-files-and-structs/structs/rcp-securityconfiguration/document.md).

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

RCP\_REMOTE\_VALIDATION\_SYSTEM

 | 

System verification.

 |
| 

RCP\_REMOTE\_VALIDATION\_SKIP

 | 

Verification skipped.

 |
| 

RCP\_REMOTE\_VALIDATION\_CERTIFICATE\_AUTHORITY

 | 

CA verification.

 |

#### \[h2\]Rcp\_SessionType

enum [Rcp\_SessionType](#ga4fa3aa6821b16425c260d837deace956)

**Description**

Session type.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

RCP\_SESSION\_TYPE\_HTTP

 | 

HTTP session.

 |
| 

RCP\_SESSION\_TYPE\_MAX

 | 

Session represented by the maximum value of **Rcp\_SessionType**.

 |

#### \[h2\]Rcp\_StatusCode

enum [Rcp\_StatusCode](#ga97929a5349f04300f50318f50393b93e)

**Description**

Response status code.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

RCP\_NONE

 | 

Status code 0.

 |
| 

RCP\_OK

 | 

Status code 200.

 |
| 

RCP\_CREATED

 | 

Status code 201.

 |
| 

RCP\_ACCEPTED

 | 

Status code 202.

 |
| 

RCP\_NOT\_AUTHORITATIVE

 | 

Status code 203

 |
| 

RCP\_NO\_CONTENT

 | 

Status code 204.

 |
| 

RCP\_RESET

 | 

Status code 205.

 |
| 

RCP\_PARTIAL

 | 

Status code 206.

 |
| 

RCP\_MULTI\_CHOICE

 | 

Status code 300.

 |
| 

RCP\_MOVED\_PERMANENTLY

 | 

Status code 301.

 |
| 

RCP\_MOVED\_TEMPORARILY

 | 

Status code 302.

 |
| 

RCP\_SEE\_OTHER

 | 

Status code 303.

 |
| 

RCP\_NOT\_MODIFIED

 | 

Status code 304.

 |
| 

RCP\_USE\_PROXY

 | 

Status code 305.

 |
| 

RCP\_BAD\_REQUEST

 | 

Status code 400.

 |
| 

RCP\_UNAUTHORIZED

 | 

Status code 401.

 |
| 

RCP\_PAYMENT\_REQUIRED

 | 

Status code 402.

 |
| 

RCP\_FORBIDDEN

 | 

Status code 403.

 |
| 

RCP\_NOT\_FOUND

 | 

Status code 404.

 |
| 

RCP\_BAD\_METHOD

 | 

Status code 405.

 |
| 

RCP\_NOT\_ACCEPTABLE

 | 

Status code 406.

 |
| 

RCP\_PROXY\_AUTH

 | 

Status code 407.

 |
| 

RCP\_CLIENT\_TIMEOUT

 | 

Status code 408.

 |
| 

RCP\_CONFLICT

 | 

Status code 409.

 |
| 

RCP\_GONE

 | 

Status code 410.

 |
| 

RCP\_LENGTH\_REQUIRED

 | 

Status code 411.

 |
| 

RCP\_PRECON\_FAILED

 | 

Status code 412.

 |
| 

RCP\_ENTITY\_TOO\_LARGE

 | 

Status code 413.

 |
| 

RCP\_REQ\_TOO\_LONG

 | 

Status code 414.

 |
| 

RCP\_UNSUPPORTED\_TYPE

 | 

Status code 415.

 |
| 

RCP\_INTERNAL\_ERROR

 | 

Status code 500.

 |
| 

RCP\_NOT\_IMPLEMENTED

 | 

Status code 501.

 |
| 

RCP\_BAD\_GATEWAY

 | 

Status code 502.

 |
| 

RCP\_UNAVAILABLE

 | 

Status code 503.

 |
| 

RCP\_GATEWAY\_TIMEOUT

 | 

Status code 504.

 |
| 

RCP\_VERSION

 | 

Status code 505.

 |

#### Function Description

#### \[h2\]HMS\_Rcp\_CallNextRequestHandler()

uint32\_t HMS\_Rcp\_CallNextRequestHandler ([Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md) \* request, const [Rcp\_RequestHandler](#ga5ac080855c3aaef66c58d5b5b371be2b) \* next, const [Rcp\_ResponseCallbackObject](../../header-files-and-structs/structs/rcp-responsecallbackobject/document.md) \* responseCallback )

**Description**

Calls the next interceptor or the **defaultHandler** in [Rcp\_Interceptor](../../header-files-and-structs/structs/rcp-interceptor/document.md).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

request

 | 

Pointer to [Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md).

 |
| 

next

 | 

Pointer to the next asynchronous handler [Rcp\_RequestHandler](#ga5ac080855c3aaef66c58d5b5b371be2b).

 |
| 

responseCallback

 | 

Pointer to [Rcp\_ResponseCallbackObject](../../header-files-and-structs/structs/rcp-responsecallbackobject/document.md).

 |

**Returns**:

**401** (parameter error) or a return value representing the next synchronous handler. The value is of the uint32\_t type.

#### \[h2\]HMS\_Rcp\_CallNextSyncRequestHandler()

[Rcp\_Response](../../header-files-and-structs/structs/rcp-response/document.md)\* HMS\_Rcp\_CallNextSyncRequestHandler ([Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md) \* request, const [Rcp\_SyncRequestHandler](#ga2067d1b09b33afa0b8237a049687e9ea) \* next, uint32\_t \* errCode )

**Description**

Calls the next interceptor or the default handler in [Rcp\_SyncInterceptor](../../header-files-and-structs/structs/rcp-syncinterceptor/document.md).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

request

 | 

Pointer to [Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md).

 |
| 

next

 | 

Pointer to the next synchronous handler [Rcp\_SyncRequestHandler](#ga2067d1b09b33afa0b8237a049687e9ea).

 |
| 

errCode

 | 

Output value, which is **401**: Parameter error or a return value representing the next synchronous handler.

 |

**Returns**:

**Rcp\_Response\***: pointer to the response.

#### \[h2\]HMS\_Rcp\_CancelRequest()

uint32\_t HMS\_Rcp\_CancelRequest ([Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd) \* session, const [Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md) \* request )

**Description**

Cancels a request.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

Pointer to the [Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd), which will be destroyed.

 |
| 

request

 | 

Pointer to the [Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md), which will be canceled.

 |

**Returns**:

Error code of the uint32\_t type.

**0**: Success.

**201**: Insufficient permission.

**401**: Parameter error.

**1007900993**: The session is closed or invalid.

#### \[h2\]HMS\_Rcp\_CancelSession()

uint32\_t HMS\_Rcp\_CancelSession ([Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd) \* session)

**Description**

Cancels a session.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

Pointer to the [Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd), which will be canceled.

 |

**Returns**:

Error code of the uint32\_t type.

**0**: Success.

**201**: Insufficient permission.

**401**: Parameter error.

**1007900993**: The session is closed or invalid.

#### \[h2\]HMS\_Rcp\_CloseSession()

uint32\_t HMS\_Rcp\_CloseSession ([Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd) \*\* session)

**Description**

Closes a session.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

Pointer to the [Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd), which will be closed.

 |

**Returns**:

Error code of the uint32\_t type.

**0**: Success.

**201**: Insufficient permission.

**1007900993**: The session is closed or invalid.

#### \[h2\]HMS\_Rcp\_CreateForm()

[Rcp\_Form](#ga40787f67faf4ea7111e4cda03f3f16be)\* HMS\_Rcp\_CreateForm (void)

**Description**

Creates a simple form.

**Start version**: 5.0.0(12)

**Returns**:

**Rcp\_Form\***: pointer to [Rcp\_Form](#ga40787f67faf4ea7111e4cda03f3f16be).

#### \[h2\]HMS\_Rcp\_CreateHeaders()

[Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982)\* HMS\_Rcp\_CreateHeaders (void)

**Description**

Creates a header for a request or response.

**Start version**: 5.0.0(12)

**Returns**:

**Rcp\_Headers\***: pointer to [Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982).

#### \[h2\]HMS\_Rcp\_CreateMultipartForm()

[Rcp\_MultipartForm](#ga9f974771548d3ed2054aba0e7506fef9)\* HMS\_Rcp\_CreateMultipartForm (void)

**Description**

Creates a multi-part form.

**Start version**: 5.0.0(12)

**Returns**:

**Rcp\_MultipartForm\***: pointer to [Rcp\_MultipartForm](#ga9f974771548d3ed2054aba0e7506fef9).

#### \[h2\]HMS\_Rcp\_CreateRequest()

[Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md)\* HMS\_Rcp\_CreateRequest (const char \* url)

**Description**

Creates a request.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

url

 | 

Request URL.

 |

**Returns**:

**Rcp\_Request\***: pointer to [Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md).

#### \[h2\]HMS\_Rcp\_CreateRequestCookies()

[Rcp\_RequestCookies](#ga44f2b679fefd37e78c43dbcba59d6d50)\* HMS\_Rcp\_CreateRequestCookies (void)

**Description**

Creates empty request cookies.

**Start version**: 5.0.0(12)

**Returns**:

**Rcp\_RequestCookies\***: pointer to [Rcp\_RequestCookies](#ga44f2b679fefd37e78c43dbcba59d6d50).

#### \[h2\]HMS\_Rcp\_CreateSession()

[Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd)\* HMS\_Rcp\_CreateSession (const [Rcp\_SessionConfiguration](../../header-files-and-structs/structs/rcp-sessionconfiguration/document.md) \* configuration, uint32\_t \* errCode )

**Description**

Creates a session. A maximum of 16 session instances can be created through **HMS\_Rcp\_CreateSession()**.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

configuration

 | 

Session configuration.

 |
| 

errCode

 | 

-   **0**: Request successful.
-   **401**: Parameter error.
-   **201**: Insufficient permission.
-   **1007900027**: Insufficient memory.

 |

**Returns**:

**Rcp\_Session\***: pointer to [Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd).

#### \[h2\]HMS\_Rcp\_DestroyForm()

void HMS\_Rcp\_DestroyForm ([Rcp\_Form](#ga40787f67faf4ea7111e4cda03f3f16be) \* form)

**Description**

Destroys a simple form.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

form

 | 

Pointer to the [Rcp\_Form](#ga40787f67faf4ea7111e4cda03f3f16be) to be destroyed.

 |

#### \[h2\]HMS\_Rcp\_DestroyHeaderEntries()

void HMS\_Rcp\_DestroyHeaderEntries ([Rcp\_HeaderEntry](../../header-files-and-structs/structs/rcp-headerentry/document.md) \* headerEntry)

**Description**

Destroys all key-value pairs obtained in [HMS\_Rcp\_GetHeaderEntries](#ga94edbbabc6b1b76d0e0f729ca618458a).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

headerEntry

 | 

Pointer to the [Rcp\_HeaderEntry](../../header-files-and-structs/structs/rcp-headerentry/document.md) to be destroyed.

 |

#### \[h2\]HMS\_Rcp\_DestroyHeaders()

void HMS\_Rcp\_DestroyHeaders ([Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982) \* headers)

**Description**

Destroys the header of a request or response.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

headers

 | 

Pointer to the [Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982) to be destroyed.

 |

#### \[h2\]HMS\_Rcp\_DestroyMultipartForm()

void HMS\_Rcp\_DestroyMultipartForm ([Rcp\_MultipartForm](#ga9f974771548d3ed2054aba0e7506fef9) \* multipartForm)

**Description**

Destroys a multi-part form.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

multipartForm

 | 

Pointer to the [Rcp\_MultipartForm](#ga9f974771548d3ed2054aba0e7506fef9) to be destroyed.

 |

#### \[h2\]HMS\_Rcp\_DestroyRequest()

void HMS\_Rcp\_DestroyRequest ([Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md) \* request)

**Description**

Destroys a request.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

request

 | 

Pointer to the [Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md) to be destroyed.

 |

#### \[h2\]HMS\_Rcp\_DestroyRequestCookieEntries()

void HMS\_Rcp\_DestroyRequestCookieEntries ([Rcp\_RequestCookieEntry](../../header-files-and-structs/structs/rcp-requestcookieentry/document.md) \* cookieEntry)

**Description**

Destroys all key-value pairs related to request cookies obtained from [HMS\_Rcp\_GetRequestCookieValue](#ga43a79371dfb3ff211321d1c18d4864b2).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

cookieEntry

 | 

Pointer to the [Rcp\_RequestCookieEntry](../../header-files-and-structs/structs/rcp-requestcookieentry/document.md) to be destroyed.

 |

#### \[h2\]HMS\_Rcp\_DestroyRequestCookies()

void HMS\_Rcp\_DestroyRequestCookies ([Rcp\_RequestCookies](#ga44f2b679fefd37e78c43dbcba59d6d50) \* cookies)

**Description**

Destroys request cookies.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

cookies

 | 

Pointer to the [Rcp\_RequestCookies](#ga44f2b679fefd37e78c43dbcba59d6d50) to be destroyed.

 |

#### \[h2\]HMS\_Rcp\_DestroyResponseCookieAttrEntries()

void HMS\_Rcp\_DestroyResponseCookieAttrEntries ([Rcp\_CookieAttributeEntry](../../header-files-and-structs/structs/rcp-cookieattributeentry/document.md) \* entries)

**Description**

Destroys response cookie attributes.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

entries

 | 

Pointer to the [Rcp\_CookieAttributeEntry](../../header-files-and-structs/structs/rcp-cookieattributeentry/document.md) to be destroyed.

 |

#### \[h2\]HMS\_Rcp\_Fetch()

uint32\_t HMS\_Rcp\_Fetch ([Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd) \* session, [Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md) \* request, const [Rcp\_ResponseCallbackObject](../../header-files-and-structs/structs/rcp-responsecallbackobject/document.md) \* responseCallback )

**Description**

Sends an asynchronous request and obtains a response.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

Pointer to [Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd), which is used to initiate a request.

 |
| 

request

 | 

Pointer to [Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md).

 |
| 

responseCallback

 | 

Pointer to the custom response callback function. For details, please refer to [Rcp\_ResponseCallbackObject](../../header-files-and-structs/structs/rcp-responsecallbackobject/document.md).

 |

**Returns**:

Error code of the uint32\_t type. **0**: Success. **201**: Insufficient permission. **401**: Parameter error. **1007900993**: The session is closed or invalid.

**Permissions**:

ohos.permission.INTERNET

ohos.permission.GET\_NETWORK\_INFO: Request this permission if you want to use the cellular network in **PathPreference**.

#### \[h2\]HMS\_Rcp\_FetchSync()

[Rcp\_Response](../../header-files-and-structs/structs/rcp-response/document.md)\* HMS\_Rcp\_FetchSync ([Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd) \* session, [Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md) \* request, uint32\_t \* errCode )

**Description**

Sends a synchronous request and obtains a response.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

Pointer to [Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd), which is used to initiate a request.

 |
| 

request

 | 

Pointer to [Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md).

 |
| 

errCode

 | 

\[out\]: common error codes.

-   **0**: Request successful.
-   **201**: Insufficient permission.
-   **401**: Parameter error.
-   **1007900001**: Unsupported protocol.
-   **1007900003**: Invalid URL format or missing URL.
-   **1007900005**: Unable to resolve the proxy name.
-   **1007900006**: Unable to resolve the host name.
-   **1007900007**: Unable to connect to the server.
-   **1007900008**: Abnormal server response.
-   **1007900009**: Access to a remote resource was rejected.
-   **1007900016**: An HTTP/2-frame error occurred.
-   **1007900018**: A part of the file has been transmitted.
-   **1007900025**: Upload failed.
-   **1007900026**: Failed to open or read local data from a file or app.
-   **1007900027**: Insufficient memory.
-   **1007900028**: The timeout interval has expired.
-   **1007900047**: The number of redirections has reached the maximum.
-   **1007900052**: No data returned from the server.
-   **1007900055**: Failed to send data to the peer.
-   **1007900056**: Failed to receive data from the peer.
-   **1007900058**: Invalid local SSL certificate.
-   **1007900059**: Unable to use the specified SSL key.
-   **1007900060**: The SSL peer certificate or SSH remote key is invalid.
-   **1007900061**: The HTTP content or transport encoding cannot be identified or is incorrect.
-   **1007900063**: The file size exceeded the maximum.
-   **1007900070**: The disk is full or the allocated quota is used up.
-   **1007900073**: The remote file already exists.
-   **1007900077**: Invalid SSL CA certificate.
-   **1007900078**: Cannot find the remote file.
-   **1007900992**: The request has been canceled.
-   **1007900993**: The session is closed or invalid.
-   **1007900094**: The identity verification function returned an error.
-   **1007900995**: Failed to obtain the system proxy.
-   **1007900996**: The proxy type is not supported.
-   **1007900997**: Invalid content type.
-   **1007900998**: The method is not supported.
-   **1007900999**: Internal error.

Other error codes are in the format of 1007900000 + Curl error code. For more error codes, please refer to [Curl error codes](https://curl.se/libcurl/c/libcurl-errors.html).

 |

**Returns**:

**Rcp\_Response\***: pointer to [Rcp\_Response](../../header-files-and-structs/structs/rcp-response/document.md).

**Permissions**:

ohos.permission.INTERNET

ohos.permission.GET\_NETWORK\_INFO: Request this permission if you want to use the cellular network in **PathPreference**.

#### \[h2\]HMS\_Rcp\_GetFormValue()

[Rcp\_FormFieldValue](../../header-files-and-structs/structs/rcp-formfieldvalue/document.md)\* HMS\_Rcp\_GetFormValue ([Rcp\_Form](#ga40787f67faf4ea7111e4cda03f3f16be) \* form, const char \* key )

**Description**

Obtains a value based on a key from a simple form.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

form

 | 

Pointer to [Rcp\_Form](#ga40787f67faf4ea7111e4cda03f3f16be).

 |
| 

key

 | 

Key.

 |

**Returns**:

**Rcp\_FormFieldValue\***: pointer to **{@Rcp\_FormFieldValue}**.

#### \[h2\]HMS\_Rcp\_GetHeaderEntries()

[Rcp\_HeaderEntry](../../header-files-and-structs/structs/rcp-headerentry/document.md)\* HMS\_Rcp\_GetHeaderEntries ([Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982) \* headers)

**Description**

Obtains all key-value pairs from a request or response header.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

headers

 | 

Pointer to [Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982) for which all key-value pairs need to be obtained.

 |

**Returns**:

**Rcp\_HeaderEntry\***: pointer to the obtained [Rcp\_HeaderEntry](../../header-files-and-structs/structs/rcp-headerentry/document.md).

#### \[h2\]HMS\_Rcp\_GetHeaderValue()

[Rcp\_HeaderValue](../../header-files-and-structs/structs/rcp-headervalue/document.md)\* HMS\_Rcp\_GetHeaderValue ([Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982) \* headers, const char \* name )

**Description**

Obtains a value based on a key from a request or response header.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

headers

 | 

Pointer to the [Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982) to be obtained.

 |
| 

name

 | 

Key.

 |

**Returns**:

**Rcp\_HeaderValue\***: pointer to the obtained [Rcp\_HeaderValue](../../header-files-and-structs/structs/rcp-headervalue/document.md).

#### \[h2\]HMS\_Rcp\_GetMultipartFormValue()

[Rcp\_MultipartFormFieldValue](../../header-files-and-structs/structs/rcp-multipartformfieldvalue/document.md)\* HMS\_Rcp\_GetMultipartFormValue ([Rcp\_MultipartForm](#ga9f974771548d3ed2054aba0e7506fef9) \* multipartForm, const char \* key )

**Description**

Obtains a value based on a key from a multi-part form.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

multipartForm

 | 

Pointer to the [Rcp\_MultipartForm](#ga9f974771548d3ed2054aba0e7506fef9) for which the value needs to be obtained.

 |
| 

key

 | 

Key.

 |

**Returns**:

**Rcp\_MultipartFormFieldValue\***: pointer to [Rcp\_MultipartFormFieldValue](../../header-files-and-structs/structs/rcp-multipartformfieldvalue/document.md).

#### \[h2\]HMS\_Rcp\_GetRequestCookieEntries()

[Rcp\_RequestCookieEntry](../../header-files-and-structs/structs/rcp-requestcookieentry/document.md)\* HMS\_Rcp\_GetRequestCookieEntries ([Rcp\_RequestCookies](#ga44f2b679fefd37e78c43dbcba59d6d50) \* cookies)

**Description**

Obtains all key-value pairs from the request cookies.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

cookies

 | 

Pointer to the [Rcp\_RequestCookies](#ga44f2b679fefd37e78c43dbcba59d6d50) for which all key-value paris need to be obtained.

 |

**Returns**:

**Rcp\_RequestCookieEntry\***: pointer to [Rcp\_RequestCookieEntry](../../header-files-and-structs/structs/rcp-requestcookieentry/document.md).

#### \[h2\]HMS\_Rcp\_GetRequestCookieValue()

char\* HMS\_Rcp\_GetRequestCookieValue ([Rcp\_RequestCookies](#ga44f2b679fefd37e78c43dbcba59d6d50) \* cookies, const char \* name )

**Description**

Obtains the request cookie value by name.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

cookies

 | 

Pointer to the [Rcp\_RequestCookies](#ga44f2b679fefd37e78c43dbcba59d6d50) for which the value needs to be obtained.

 |
| 

name

 | 

Key.

 |

**Returns**:

**char\***: pointer to the returned cookie value.

#### \[h2\]HMS\_Rcp\_GetResponseCookieAttrEntries()

[Rcp\_CookieAttributeEntry](../../header-files-and-structs/structs/rcp-cookieattributeentry/document.md)\* HMS\_Rcp\_GetResponseCookieAttrEntries ([Rcp\_CookieAttributes](#ga08c7b992199bec7e5acdc50ce8ae2651) \* cookieAttributes)

**Description**

Obtains all response cookie attributes from [Rcp\_CookieAttributes](#ga08c7b992199bec7e5acdc50ce8ae2651).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

cookieAttributes

 | 

Pointer to the [Rcp\_CookieAttributes](#ga08c7b992199bec7e5acdc50ce8ae2651) for which all cookie attribute values need to be obtained.

 |

**Returns**:

[Rcp\_CookieAttributeEntry](../../header-files-and-structs/structs/rcp-cookieattributeentry/document.md) \*: list of cookie attributes.

#### \[h2\]HMS\_Rcp\_GetResponseCookieAttrValue()

const char\* HMS\_Rcp\_GetResponseCookieAttrValue ([Rcp\_CookieAttributes](#ga08c7b992199bec7e5acdc50ce8ae2651) \* cookieAttributes, const char \* name )

**Description**

Obtains the cookie attribute value by name.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

cookieAttributes

 | 

Pointer to the [Rcp\_CookieAttributes](#ga08c7b992199bec7e5acdc50ce8ae2651) to be obtained.

 |
| 

name

 | 

Key.

 |

**Returns**:

**char\***: pointer to cookie attribute values.

#### \[h2\]HMS\_Rcp\_GetSessionConfiguration()

const [Rcp\_SessionConfiguration](../../header-files-and-structs/structs/rcp-sessionconfiguration/document.md)\* HMS\_Rcp\_GetSessionConfiguration ([Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd) \* session)

**Description**

Obtains the session configuration.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

Pointer to the [Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd), for which the session configuration will be obtained.

 |

**Returns**:

**Rcp\_SessionConfiguration\***: pointer to [Rcp\_SessionConfiguration](../../header-files-and-structs/structs/rcp-sessionconfiguration/document.md).

#### \[h2\]HMS\_Rcp\_GetSessionId()

const char\* HMS\_Rcp\_GetSessionId ([Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd) \* session)

**Description**

Obtains the session ID.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

Pointer to the [Rcp\_Session](#ga4f3a7d39c18fe6fdf01c52759213ddcd), for which the session ID will be obtained.

 |

**Returns**:

**char\***: pointer to the returned session ID.

#### \[h2\]HMS\_Rcp\_SetFormValue()

uint32\_t HMS\_Rcp\_SetFormValue ([Rcp\_Form](#ga40787f67faf4ea7111e4cda03f3f16be) \* form, const char \* key, const [Rcp\_FormFieldValue](../../header-files-and-structs/structs/rcp-formfieldvalue/document.md) \* value )

**Description**

Sets key-value pairs in a simple form.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

form

 | 

Pointer to [Rcp\_Form](#ga40787f67faf4ea7111e4cda03f3f16be), for which a key-value pair needs to be set.

 |
| 

key

 | 

Key.

 |
| 

value

 | 

Value.

 |

**Returns**:

A status code of the uint32\_t type. **0**: Success. **401**: Parameter error. **1007900027**: Insufficient memory.

#### \[h2\]HMS\_Rcp\_SetHeaderValue()

uint32\_t HMS\_Rcp\_SetHeaderValue ([Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982) \* headers, const char \* name, const char \* value )

**Description**

Sets key-value pairs in a request or response header.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

headers

 | 

Pointer to [Rcp\_Headers](#gac4f343ec02dec34268e93ce746e6c982).

 |
| 

name

 | 

Key.

 |
| 

value

 | 

Value.

 |

**Returns**:

A status code of the uint32\_t type. **0**: Success. **401**: Parameter error. **1007900027**: Insufficient memory.

#### \[h2\]HMS\_Rcp\_SetMultipartFormValue()

uint32\_t HMS\_Rcp\_SetMultipartFormValue ([Rcp\_MultipartForm](#ga9f974771548d3ed2054aba0e7506fef9) \* multipartForm, const char \* key, const [Rcp\_MultipartFormFieldValue](../../header-files-and-structs/structs/rcp-multipartformfieldvalue/document.md) \* value )

**Description**

Sets key-value pairs in a multi-part form.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

multipartForm

 | 

Pointer to [Rcp\_MultipartForm](#ga9f974771548d3ed2054aba0e7506fef9).

 |
| 

key

 | 

Key.

 |
| 

value

 | 

Value.

 |

**Returns**:

A status code of the uint32\_t type. **0**: Success. **401**: Parameter error. **1007900027**: Insufficient memory.

#### \[h2\]HMS\_Rcp\_SetRequestCookieValue()

uint32\_t HMS\_Rcp\_SetRequestCookieValue ([Rcp\_RequestCookies](#ga44f2b679fefd37e78c43dbcba59d6d50) \* cookies, const char \* name, const char \* value )

**Description**

Sets request cookies.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

cookies

 | 

Pointer to [Rcp\_RequestCookies](#ga44f2b679fefd37e78c43dbcba59d6d50).

 |
| 

name

 | 

Key.

 |
| 

value

 | 

Value.

 |

**Returns**:

A status code of the uint32\_t type. **0**: Success. **401**: Parameter error. **1007900027**: Insufficient memory.

#### \[h2\]HMS\_Rcp\_SetRequestOnBinaryDataRecvCallback()

uin32\_t HMS\_SetRequestOnBinaryDataRecvCallback ([Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md) \* request, [Rcp\_OnBinaryReceiveCallback](../../header-files-and-structs/structs/rcp-onbinaryreceivecallback/document.md) onBinaryReceiveCallback);

**Description**

Sets a callback function for receiving binary data upon a request. The callback function works the same as [Rcp\_OnDataReceiveCallback](#gacd66d521a147a876e340aed45a3ed1c4) in [Rcp\_Configuration](../../header-files-and-structs/structs/rcp-configuration/document.md). Once set, the callback function will replace [Rcp\_OnDataReceiveCallback](#gacd66d521a147a876e340aed45a3ed1c4) configured in [Rcp\_Configuration](../../header-files-and-structs/structs/rcp-configuration/document.md).

**Start version**: 5.0.1(13)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

request

 | 

Request for which the binary data callback needs to be set, which points to [Rcp\_Request](#ga98dde966841135537e05053bf4da4d5b).

 |
| 

onBinaryReceiveCallback

 | 

Callback function for receiving binary data streams.

 |

**Returns**:

A status code of the uint32\_t type. **0**: Success. **401**: Parameter error.

#### \[h2\]HMS\_Rcp\_SetRequestOnStatusCodeReceiveCallback()

uin32\_t HMS\_Rcp\_SetRequestOnStatusCodeReceiveCallback ([Rcp\_Request](../../header-files-and-structs/structs/rcp-request/document.md) \* request, [Rcp\_OnStatusCodeReceiveCallback](../../header-files-and-structs/structs/rcp-onstatuscodereceivecallback/document.md) onStatusCodeReceiveCallback);

**Description**

Sets the callback function for a response status code. This callback function is triggered when a response status code is received from the peer end. You cannot cancel listening by setting [Rcp\_OnStatusCodeReceiveCallbackFunc](#section1961611617339) to **NULL**.

**Start version**: 6.0.1(21)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

request

 | 

Request for which the response status code callback function is set, which points to [Rcp\_Request](#ga98dde966841135537e05053bf4da4d5b).

 |
| 

onStatusCodeReceiveCallback

 | 

Callback function for receiving a response status code.

 |

**Returns**:

A status code of the uint32\_t type. **0**: Success. **401**: Parameter error.
