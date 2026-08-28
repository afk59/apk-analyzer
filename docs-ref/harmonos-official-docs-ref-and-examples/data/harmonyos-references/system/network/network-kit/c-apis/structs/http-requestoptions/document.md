# Http\_RequestOptions

typedef struct Http\_RequestOptions {...} Http\_RequestOptions

#### Overview

Defines the structure of HTTP requests.

**Since**: 20

**Related module**: [netstack](../../modules/netstack/document.md)

**Header file**: [net\_http\_type.h](../../header-files/net-http-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| const char \*method | HTTP request method. |
| uint32\_t priority | HTTP request priority. |
| [Http\_Headers](../http-headers/document.md) \*headers | Pointer to the HTTP request header. For details, see [Http\_Headers](../http-headers/document.md). |
| uint32\_t readTimeout | Read timeout duration. |
| uint32\_t connectTimeout | Connection timeout duration. |
| [Http\_HttpProtocol](../../header-files/net-http-type-h/document.md#http_httpprotocol) httpProtocol | HTTP protocol. For details, see [Http\_HttpProtocol](../../header-files/net-http-type-h/document.md#http_httpprotocol). |
| [Http\_Proxy](../http-proxy/document.md) \*httpProxy | Pointer to the HTTP proxy configuration, which indicates whether to use a proxy. By default, proxy is not used. For details, see [Http\_Proxy](../http-proxy/document.md). |
| const char \*caPath | Certificate path. If the CA certificate path is set, the system uses the CA certificate in the specified path. Otherwise, the system uses the preset CA certificate. |
| int64\_t resumeFrom | Download start position. This field can be used only for the GET method. |
| int64\_t resumeTo | Download end position. This field can be used only for the GET method. |
| [Http\_ClientCert](../http-clientcert/document.md) \*clientCert | Pointer to the client certificate configuration. For details, see [Http\_ClientCert](../http-clientcert/document.md). |
| const char \*dnsOverHttps | HTTPS server for DNS resolution. |
| [Http\_AddressFamilyType](../../header-files/net-http-type-h/document.md#http_addressfamilytype) addressFamily | IP address family. For details, see [Http\_AddressFamilyType](../../header-files/net-http-type-h/document.md#http_addressfamilytype). |
