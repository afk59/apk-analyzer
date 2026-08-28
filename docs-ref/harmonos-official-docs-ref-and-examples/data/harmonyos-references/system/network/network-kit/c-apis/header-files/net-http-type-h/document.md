# net\_http\_type.h

#### Overview

Defines the data structures for the C APIs of the HTTP request module.

**File to include**: <network/netstack/net\_http\_type.h>

**Library**: libnet\_http.so

**System capability**: SystemCapability.Communication.NetStack

**Since**: 20

**Related module**: [netstack](../../modules/netstack/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Http\_Buffer](../../structs/http-buffer/document.md) | Http\_Buffer | Defines the HTTP buffer structure. |
| [Http\_HeaderValue](../../structs/http-headervalue/document.md) | Http\_HeaderValue | Defines the type of a mapped value in a request or response header. |
| [Http\_HeaderEntry](../../structs/http-headerentry/document.md) | Http\_HeaderEntry | Defines all key-value pairs in the request or response header. |
| [Http\_ClientCert](../../structs/http-clientcert/document.md) | Http\_ClientCert | Defines the client certificate sent to a remote server, which will be used by the server to verify the identity of the client. |
| [Http\_CustomProxy](../../structs/http-customproxy/document.md) | Http\_CustomProxy | Defines the custom proxy configuration. |
| [Http\_Proxy](../../structs/http-proxy/document.md) | Http\_Proxy | Defines the proxy configuration structure. |
| [Http\_PerformanceTiming](../../structs/http-performancetiming/document.md) | Http\_PerformanceTiming | Defines the HTTP response timing information, which will be collected via [Http\_Response.performanceTiming](../../structs/http-response/document.md#member-variables). |
| [Http\_RequestOptions](../../structs/http-requestoptions/document.md) | Http\_RequestOptions | Defines the structure of HTTP requests. |
| [Http\_Response](../../structs/http-response/document.md) | Http\_Response | Defines the structure of HTTP responses. |
| [Http\_Request](../../structs/http-request/document.md) | Http\_Request | Defines an HTTP request. |
| [Http\_EventsHandler](../../structs/http-eventshandler/document.md) | Http\_EventsHandler | Defines the callback for various HTTP events. |
| [Http\_Headers](../../structs/http-headers/document.md) | Http\_Headers | Defines the header of an HTTP request or response. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Http\_ErrCode](#http_errcode) | Http\_ErrCode | Enumerates the error codes of an HTTP request. |
| [Http\_ResponseCode](#http_responsecode) | Http\_ResponseCode | Enumerates the result codes of an HTTP response. |
| [Http\_AddressFamilyType](#http_addressfamilytype) | Http\_AddressFamilyType | Enumerates the IP address family of the target domain name. |
| [Http\_HttpProtocol](#http_httpprotocol) | Http\_HttpProtocol | Enumerates HTTP protocol versions. |
| [Http\_CertType](#http_certtype) | Http\_CertType | Enumerates certificate types. |
| [Http\_ProxyType](#http_proxytype) | Http\_ProxyType | Enumerates proxy types. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| OHOS\_HTTP\_MAX\_PATH\_LEN 128 | 
Defines the maximum path length of an HTTP request.

**Since**: 20

 |
| OHOS\_HTTP\_MAX\_STR\_LEN 256 | 

Defines the maximum string length of an HTTP request.

**Since**: 20

 |
| OHOS\_HTTP\_DNS\_SERVER\_NUM\_MAX 3 | 

Defines the maximum number of DNS servers for an HTTP request.

**Since**: 20

 |
| NET\_HTTP\_METHOD\_GET "GET" | 

Sets the HTTP request method to GET.

**Since**: 20

 |
| NET\_HTTPMETHOD\_HEAD "HEAD" | 

Sets the HTTP request method to HEAD.

**Since**: 20

 |
| NET\_HTTPMETHOD\_OPTIONS "OPTIONS" | 

Sets the HTTP request method to OPTIONS.

**Since**: 20

 |
| NET\_HTTPMETHOD\_TRACE "TRACE" | 

Sets the HTTP request method to TRACE.

**Since**: 20

 |
| NET\_HTTPMETHOD\_DELETE "DELETE" | 

Sets the HTTP request method to DELETE.

**Since**: 20

 |
| NET\_HTTP\_METHOD\_POST "POST" | 

Sets the HTTP request method to POST.

**Since**: 20

 |
| NET\_HTTP\_METHOD\_PUT "PUT" | 

Sets the HTTP request method to PUT.

**Since**: 20

 |
| NET\_HTTP\_METHOD\_PATCH "CONNECT" | 

Sets the HTTP request method to CONNECT.

**Since**: 20

 |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*Http\_ResponseCallback)(struct Http\_Response \*response, uint32\_t errCode)](#http_responsecallback) | Http\_ResponseCallback | Callback invoked when an HTTP response is received. |
| [typedef void (\*Http\_OnDataReceiveCallback)(const char \*data, size\_t length)](#http_ondatareceivecallback) | Http\_OnDataReceiveCallback | Callback invoked when data is received. |
| [typedef void (\*Http\_OnProgressCallback)(uint64\_t totalSize, uint64\_t transferredSize)](#http_onprogresscallback) | Http\_OnProgressCallback | Callback invoked during request/response data transmission. |
| [typedef void (\*Http\_OnHeaderReceiveCallback)(Http\_Headers \*headers)](#http_onheaderreceivecallback) | Http\_OnHeaderReceiveCallback | Callback invoked when an HTTP response header is received. |
| [typedef void (\*Http\_OnVoidCallback)(void)](#http_onvoidcallback) | Http\_OnVoidCallback | Callback invoked when a DataEnd or Cancel event is received. |

#### Enum Description

#### \[h2\]Http\_ErrCode

enum Http\_ErrCode

**Overview**

Enumerates the error codes of an HTTP request.

**Since**: 20

| Enum | Description |
| :-- | :-- |
| OH\_HTTP\_RESULT\_OK = 0 | Request succeeded. |
| OH\_HTTP\_PARAMETER\_ERROR = 401 | Invalid parameter. |
| OH\_HTTP\_PERMISSION\_DENIED = 201 | Permission denied. |
| OH\_HTTP\_NETSTACK\_E\_BASE = 2300000 | Base error code offset. |
| OH\_HTTP\_UNSUPPORTED\_PROTOCOL = (OH\_HTTP\_NETSTACK\_E\_BASE + 1) | Unsupported protocol. |
| OH\_HTTP\_INVALID\_URL = (OH\_HTTP\_NETSTACK\_E\_BASE + 3) | Incorrect URL format. |
| OH\_HTTP\_RESOLVE\_PROXY\_FAILED = (OH\_HTTP\_NETSTACK\_E\_BASE + 5) | Failed to resolve the domain name of the proxy server. |
| OH\_HTTP\_RESOLVE\_HOST\_FAILED = (OH\_HTTP\_NETSTACK\_E\_BASE + 6) | Failed to resolve the domain name. |
| OH\_HTTP\_CONNECT\_SERVER\_FAILED = (OH\_HTTP\_NETSTACK\_E\_BASE + 7) | Failed to connect to the server. |
| OH\_HTTP\_INVALID\_SERVER\_RESPONSE = (OH\_HTTP\_NETSTACK\_E\_BASE + 8) | Invalid data returned by the server. |
| OH\_HTTP\_ACCESS\_REMOTE\_DENIED = (OH\_HTTP\_NETSTACK\_E\_BASE + 9) | Access to remote resources denied. |
| OH\_HTTP\_HTTP2\_FRAMING\_ERROR = (OH\_HTTP\_NETSTACK\_E\_BASE + 16) | Error detected at the HTTP2 framework layer. |
| OH\_HTTP\_TRANSFER\_PARTIAL\_FILE = (OH\_HTTP\_NETSTACK\_E\_BASE + 18) | Files partially transferred. |
| OH\_HTTP\_WRITE\_DATA\_FAILED = (OH\_HTTP\_NETSTACK\_E\_BASE + 23) | Failed to write the received data to the disk or application. |
| OH\_HTTP\_UPLOAD\_FAILED = (OH\_HTTP\_NETSTACK\_E\_BASE + 25) | Failed to upload data. |
| OH\_HTTP\_OPEN\_LOCAL\_DATA\_FAILED = (OH\_HTTP\_NETSTACK\_E\_BASE + 26) | Failed to open or read the local data in the file or application. |
| OH\_HTTP\_OUT\_OF\_MEMORY = (OH\_HTTP\_NETSTACK\_E\_BASE + 27) | Insufficient memory. |
| OH\_HTTP\_OPERATION\_TIMEOUT = (OH\_HTTP\_NETSTACK\_E\_BASE + 28) | Operation timeout. |
| OH\_HTTP\_TOO\_MANY\_REDIRECTIONS = (OH\_HTTP\_NETSTACK\_E\_BASE + 47) | Number of redirections reaching the maximum. |
| OH\_HTTP\_SERVER\_RETURNED\_NOTHING = (OH\_HTTP\_NETSTACK\_E\_BASE + 52) | No content (header or data) returned by the server. |
| OH\_HTTP\_SEND\_DATA\_FAILED = (OH\_HTTP\_NETSTACK\_E\_BASE + 55) | Failed to send data via Bluetooth. |
| OH\_HTTP\_RECEIVE\_DATA\_FAILED = (OH\_HTTP\_NETSTACK\_E\_BASE + 56) | Failed to receive data. |
| OH\_HTTP\_SSL\_CERTIFICATE\_ERROR = (OH\_HTTP\_NETSTACK\_E\_BASE + 58) | Invalid local SSL certificate. |
| OH\_HTTP\_SSL\_CIPHER\_USED\_ERROR = (OH\_HTTP\_NETSTACK\_E\_BASE + 59) | Specified cipher suite unavailable. |
| OH\_HTTP\_INVALID\_SSL\_PEER\_CERT = (OH\_HTTP\_NETSTACK\_E\_BASE + 60) | Invalid SSL peer certificate or SSH remote key. |
| OH\_HTTP\_INVALID\_ENCODING\_FORMAT = (OH\_HTTP\_NETSTACK\_E\_BASE + 61) | Invalid HTTP encoding format. |
| OH\_HTTP\_FILE\_TOO\_LARGE = (OH\_HTTP\_NETSTACK\_E\_BASE + 63) | Maximum file size exceeded. |
| OH\_HTTP\_REMOTE\_DISK\_FULL = (OH\_HTTP\_NETSTACK\_E\_BASE + 70) | Remote disk fully occupied. |
| OH\_HTTP\_REMOTE\_FILE\_EXISTS = (OH\_HTTP\_NETSTACK\_E\_BASE + 73) | Remote file already exists. |
| OH\_HTTP\_SSL\_CA\_NOT\_EXIST = (OH\_HTTP\_NETSTACK\_E\_BASE + 77) | SSL CA certificate inexistent or inaccessible. |
| OH\_HTTP\_REMOTE\_FILE\_NOT\_FOUND = (OH\_HTTP\_NETSTACK\_E\_BASE + 78) | Remote file not found. |
| OH\_HTTP\_AUTHENTICATION\_ERROR = (OH\_HTTP\_NETSTACK\_E\_BASE + 94) | Identity authentication error. |
| OH\_HTTP\_ACCESS\_DOMAIN\_NOT\_ALLOWED = (OH\_HTTP\_NETSTACK\_E\_BASE + 998) | Access to the domain denied. |
| OH\_HTTP\_UNKNOWN\_ERROR = (OH\_HTTP\_NETSTACK\_E\_BASE + 999) | Unknown error. |

#### \[h2\]Http\_ResponseCode

enum Http\_ResponseCode

**Overview**

Enumerates the result codes of an HTTP response.

**Since**: 20

| Enum | Description |
| :-- | :-- |
| OH\_HTTP\_OK = 200 | Request succeeded. |
| OH\_HTTP\_CREATED = 201 | "Created." The request has been successfully sent and a new resource is created. |
| OH\_HTTP\_ACCEPTED = 202 | "Accepted." The request has been accepted for processing, but the processing has not been completed. |
| OH\_HTTP\_NON\_AUTHORITATIVE\_INFO = 203 | "Non-Authoritative Information." The request was successfully processed, but the returned response body contains non-authoritative information. |
| OH\_HTTP\_NO\_CONTENT = 204 | "No Content." The server has successfully fulfilled the request but there is no additional content to send in the response payload body. |
| OH\_HTTP\_RESET = 205 | "Reset Content." The server has successfully fulfilled the request and desires that the user agent reset the content. |
| OH\_HTTP\_PARTIAL = 206 | "Partial Content." The server has successfully fulfilled the partial GET request for a given resource. |
| OH\_HTTP\_MULTI\_CHOICE = 300 | "Multiple Choices." The requested resource corresponds to any one of a set of representations. |
| OH\_HTTP\_MOVED\_PERM = 301 | "Moved Permanently." The requested resource has been assigned a new permanent URI and any future references to this resource will be redirected to this URI. |
| OH\_HTTP\_MOVED\_TEMP = 302 | "Moved Temporarily." The requested resource is moved temporarily to a different URI. |
| OH\_HTTP\_SEE\_OTHER = 303 | "See Other." The response to the request can be found under a different URI. |
| OH\_HTTP\_NOT\_MODIFIED = 304 | "Not Modified." The client has performed a conditional GET request and access is allowed, but the content has not been modified. |
| OH\_HTTP\_USE\_PROXY = 305 | "Use Proxy." The requested resource can only be accessed through the proxy. |
| OH\_HTTP\_BAD\_REQUEST = 400 | "Bad Request." The request could not be understood by the server due to incorrect syntax. |
| OH\_HTTP\_UNAUTHORIZED = 401 | "Unauthorized." The request requires user authentication. |
| OH\_HTTP\_PAYMENT\_REQUIRED = 402 | "Payment Required." This code is reserved for future use. |
| OH\_HTTP\_FORBIDDEN = 403 | "Forbidden." The server understands the request but refuses to process it. |
| OH\_HTTP\_NOT\_FOUND = 404 | "Not Found." The server does not find anything matching the Request-URI. |
| OH\_HTTP\_BAD\_METHOD = 405 | "Method Not Allowed." The method specified in the request is not allowed for the resource identified by the Request-URI. |
| OH\_HTTP\_NOT\_ACCEPTABLE = 406 | "Not Acceptable." The server cannot fulfill the request according to the content characteristics of the request. |
| OH\_HTTP\_PROXY\_AUTH = 407 | "Proxy Authentication Required." The request requires user authentication with the proxy. |
| OH\_HTTP\_CLIENT\_TIMEOUT = 408 | "Request Timeout." The client fails to generate a request within the timeout period. |
| OH\_HTTP\_CONFLICT = 409 | "Conflict." The request cannot be fulfilled due to a conflict with the current state of the resource. Conflicts are most likely to occur in response to a PUT request. |
| OH\_HTTP\_GONE = 410 | "Gone." The requested resource has been deleted permanently and is no longer available. |
| OH\_HTTP\_LENGTH\_REQUIRED = 411 | "Length Required." The server refuses to process the request without a defined Content-Length. |
| OH\_HTTP\_PRECON\_FAILED = 412 | "Precondition Failed." The precondition in the request is incorrect. |
| OH\_HTTP\_ENTITY\_TOO\_LARGE = 413 | "Request Entity Too Large." The server refuses to process a request because the request entity is larger than the server is able to process. |
| OH\_HTTP\_REQUEST\_TOO\_LONG = 414 | "Request-URI Too Long." The Request-URI is too long for the server to process. |
| OH\_HTTP\_UNSUPPORTED\_TYPE = 415 | "Unsupported Media Type." The server is unable to process the media format in the request. |
| OH\_HTTP\_RANGE\_NOT\_MET = 416 | "Range Not Satisfiable." The server cannot serve the requested ranges. |
| OH\_HTTP\_INTERNAL\_ERROR = 500 | "Internal Server Error." The server encounters an unexpected error that prevents it from fulfilling the request. |
| OH\_HTTP\_NOT\_IMPLEMENTED = 501 | "Not Implemented." The server does not support the function required to fulfill the request. |
| OH\_HTTP\_BAD\_GATEWAY = 502 | "Bad Gateway." The server acting as a gateway or proxy receives an invalid response from the upstream server. |
| OH\_HTTP\_UNAVAILABLE = 503 | "Service Unavailable." The server is currently unable to process the request due to a temporary overload or system maintenance. |
| OH\_HTTP\_GATEWAY\_TIMEOUT = 504 | "Gateway Timeout." The server acting as a gateway or proxy does not receive requests from the remote server within the timeout period. |
| OH\_HTTP\_VERSION = 505 | "HTTP Version Not Supported." The server does not support the HTTP protocol version used in the request. |

#### \[h2\]Http\_AddressFamilyType

enum Http\_AddressFamilyType

**Overview**

Enumerates the IP address family of the target domain name.

**Since**: 20

| Enum | Description |
| :-- | :-- |
| HTTP\_ADDRESS\_FAMILY\_DEFAULT = 0 | Default value. The system determines whether to use the IPv4 or IPv6 address of the target domain name. |
| HTTP\_ADDRESS\_FAMILY\_ONLY\_V4 = 1 | The system resolves only the IPv4 address of the target domain name and ignores the IPv6 address. |
| HTTP\_ADDRESS\_FAMILY\_ONLY\_V6 = 2 | The system resolves only the IPv6 address of the target domain name and ignores the IPv4 address. |

#### \[h2\]Http\_HttpProtocol

enum Http\_HttpProtocol

**Overview**

Enumerates HTTP protocol versions.

**Since**: 20

| Enum | Description |
| :-- | :-- |
| OH\_HTTP\_NONE = 0 | Protocol version complies with cURL. |
| OH\_HTTP1\_1 | HTTP 1.1 version. |
| OH\_HTTP2 | HTTP 2 version. |
| OH\_HTTP3 | HTTP 3 version. |

#### \[h2\]Http\_CertType

enum Http\_CertType

**Overview**

Enumerates certificate types.

**Since**: 20

| Enum | Description |
| :-- | :-- |
| OH\_HTTP\_PEM = 0 | PEM certificate. |
| OH\_HTTP\_DER = 1 | DER certificate. |
| OH\_HTTP\_P12 = 2 | P12 certificate. |

#### \[h2\]Http\_ProxyType

enum Http\_ProxyType

**Overview**

Enumerates proxy types.

**Since**: 20

| Enum | Description |
| :-- | :-- |
| HTTP\_PROXY\_NOT\_USE | No proxy. |
| HTTP\_PROXY\_SYSTEM | The system proxy is used. |
| HTTP\_PROXY\_CUSTOM | The custom proxy is used. |

#### Function Description

#### \[h2\]Http\_ResponseCallback()

typedef void (\*Http\_ResponseCallback)(struct Http\_Response \*response, uint32\_t errCode)

**Overview**

Callback invoked when an HTTP response is received.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct Http\_Response](../../structs/http-response/document.md) \*response | Pointer to the HTTP response. For details, see [Http\_Response](../../structs/http-response/document.md). |
| uint32\_t errCode | Response code. |

#### \[h2\]Http\_OnDataReceiveCallback()

typedef void (\*Http\_OnDataReceiveCallback)(const char \*data, size\_t length)

**Overview**

Callback invoked when data is received.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*data | Response body. |
| size\_t length | Length of the response body. |

#### \[h2\]Http\_OnProgressCallback()

typedef void (\*Http\_OnProgressCallback)(uint64\_t totalSize, uint64\_t transferredSize)

**Overview**

Callback invoked during request/response data transmission.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| uint64\_t totalSize | Total data size. |
| uint64\_t transferredSize | Size of transferred data. |

#### \[h2\]Http\_OnHeaderReceiveCallback()

typedef void (\*Http\_OnHeaderReceiveCallback)(Http\_Headers \*headers)

**Overview**

Callback invoked when an HTTP response header is received.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Http\_Headers](../../structs/http-headers/document.md) \*headers | Pointer to the received request header. For details, see [Http\_Headers](../../structs/http-headers/document.md). |

#### \[h2\]Http\_OnVoidCallback()

typedef void (\*Http\_OnVoidCallback)(void)

**Overview**

Callback invoked when a DataEnd or Cancel event is received.

**Since**: 20
