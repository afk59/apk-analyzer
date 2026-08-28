# arkweb\_net\_error\_list.h

#### Overview

The **arkweb\_error\_code.h** file declares the error codes of the ArkWeb network protocol stack.

**File to include**: <web/arkweb\_net\_error\_list.h>

**Library**: libohweb.so

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Related module**: [Web](../../modules/web/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkWeb\_NetError](#arkweb_neterror) | ArkWeb\_NetError | Enumerates the error codes of the ArkWeb network protocol stack. |

#### Enum Description

#### \[h2\]ArkWeb\_NetError

enum ArkWeb\_NetError

**Description**

Enumerates the error codes of the ArkWeb network protocol stack.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

| Enumerated Value | Description |
| :-- | :-- |
| ARKWEB\_NET\_OK = 0 | The operation is normal. |
| ARKWEB\_ERR\_IO\_PENDING = -1 | The asynchronous I/O operation is pending. This usually does not mean a fatal error. Typically, this error is generated as a notification to wait for an external notification indicating that the I/O operation is finally completed. |
| ARKWEB\_ERR\_FAILED = -2 | The operation fails. |
| ARKWEB\_ERR\_ABORTED = -3 | The operation is aborted (due to user operation). |
| ARKWEB\_ERR\_INVALID\_ARGUMENT = -4 | The parameter is invalid. |
| ARKWEB\_ERR\_INVALID\_HANDLE = -5 | The handle or file descriptor is invalid. |
| ARKWEB\_ERR\_FILE\_NOT\_FOUND = -6 | The file or directory cannot be found. |
| ARKWEB\_ERR\_TIMED\_OUT = -7 | The operation times out. |
| ARKWEB\_ERR\_FILE\_TOO\_LARGE = -8 | The file is too large. |
| ARKWEB\_ERR\_UNEXPECTED = -9 | An unexpected error occurs. This may be caused by programming errors or invalid assumptions. |
| ARKWEB\_ERR\_ACCESS\_DENIED = -10 | Access to non-network resources is denied. |
| ARKWEB\_ERR\_NOT\_IMPLEMENTED = -11 | The operation fails because the feature is not implemented. |
| ARKWEB\_ERR\_INSUFFICIENT\_RESOURCES = -12 | Resources are insufficient to complete the operation. |
| ARKWEB\_ERR\_OUT\_OF\_MEMORY = -13 | A memory overflow occurs. |
| ARKWEB\_ERR\_UPLOAD\_FILE\_CHANGED = -14 | The file fails to be loaded because its modification time is not as expected. |
| ARKWEB\_ERR\_SOCKET\_NOT\_CONNECTED = -15 | The socket is not connected. |
| ARKWEB\_ERR\_FILE\_EXISTS = -16 | The file already exists. |
| ARKWEB\_ERR\_FILE\_PATH\_TOO\_LONG = -17 | The file path or file name is too long. |
| ARKWEB\_ERR\_FILE\_NO\_SPACE = -18 | The disk space is insufficient. |
| ARKWEB\_ERR\_FILE\_VIRUS\_INFECTED = -19 | The file is infected. |
| ARKWEB\_ERR\_BLOCKED\_BY\_CLIENT = -20 | The request is blocked by the client. |
| ARKWEB\_ERR\_NETWORK\_CHANGED = -21 | The network changes. |
| ARKWEB\_ERR\_BLOCKED\_BY\_ADMINISTRATOR = -22 | The request is blocked by the URL blocking list configured by the domain administrator. |
| ARKWEB\_ERR\_SOCKET\_CONNECTED = -23 | The socket is connected. |
| ARKWEB\_ERR\_UPLOAD\_STREAM\_REWIND\_NOT\_SUPPORTED = -25 | The upload stream must be rewound for retry or redirection, but the upload fails because rewinding is not supported. |
| ARKWEB\_ERR\_CONTEXT\_SHUT\_DOWN = -26 | The request fails because **URLRequestContext** is shut down or being shut down. |
| ARKWEB\_ERR\_BLOCKED\_BY\_RESPONSE = -27 | The request is blocked by response from headers such as X-Frame-Options, Content Security Policy, and Cross Origin Resource Policy. |
| ARKWEB\_ERR\_CLEARTEXT\_NOT\_PERMITTED = -29 | The request is blocked because some or all cleartext requests are not permitted by the system policy. |
| ARKWEB\_ERR\_BLOCKED\_BY\_CSP = -30 | The request is blocked by the Content Security Policy. |
| ARKWEB\_ERR\_H2\_OR\_QUIC\_REQUIRED = -31 | The request is blocked because there is no H/2 or QUIC session. |
| ARKWEB\_ERR\_BLOCKED\_BY\_ORB = -32 | The request is blocked by Cross-Origin Read Blocking (CORB) or ORB. |
| ARKWEB\_ERR\_CONNECTION\_CLOSED = -100 | The connection is closed, which corresponds to **TCP FIN**. |
| ARKWEB\_ERR\_CONNECTION\_RESET = -101 | The connection is reset, which corresponds to **TCP RST**. |
| ARKWEB\_ERR\_CONNECTION\_REFUSED = -102 | The connection is refused. |
| ARKWEB\_ERR\_CONNECTION\_ABORTED = -103 | The connection is aborted because the ACK for sending data is not received. This may include FIN packets. |
| ARKWEB\_ERR\_CONNECTION\_FAILED = -104 | The connection failed. |
| ARKWEB\_ERR\_NAME\_NOT\_RESOLVED = -105 | The domain name cannot be resolved. |
| ARKWEB\_ERR\_INTERNET\_DISCONNECTED = -106 | The Internet is disconnected. |
| ARKWEB\_ERR\_SSL\_PROTOCOL\_ERROR = -107 | An SSL protocol error occurs. |
| ARKWEB\_ERR\_ADDRESS\_INVALID = -108 | The IP address or port number is invalid (for example, IP address 0 or port 0 cannot be connected). |
| ARKWEB\_ERR\_ADDRESS\_UNREACHABLE = -109 | The IP address cannot be accessed. This means that there is no route to the specified host or network. |
| ARKWEB\_ERR\_SSL\_CLIENT\_AUTH\_CERT\_NEEDED = -110 | The server needs SSL client authentication certificate. |
| ARKWEB\_ERR\_TUNNEL\_CONNECTION\_FAILED = -111 | The tunnel connection failed to be established through the proxy. |
| ARKWEB\_ERR\_NO\_SSL\_VERSIONS\_ENABLED = -112 | No SSL protocol version is enabled. |
| ARKWEB\_ERR\_SSL\_VERSION\_OR\_CIPHER\_MISMATCH = -113 | The client and server do not support the common SSL protocol version or cipher suite. |
| ARKWEB\_ERR\_SSL\_RENEGOTIATION\_REQUESTED = -114 | The server requests re-negotiation (re-handshake). |
| ARKWEB\_ERR\_PROXY\_AUTH\_UNSUPPORTED = -115 | The proxy requests authentication for establishing a tunnel, but the method used is not supported. |
| ARKWEB\_ERR\_BAD\_SSL\_CLIENT\_AUTH\_CERT = -117 | The SSL handshake fails because the client certificate is incorrect or missing. |
| ARKWEB\_ERR\_CONNECTION\_TIMED\_OUT = -118 | The connection times out. |
| ARKWEB\_ERR\_HOST\_RESOLVER\_QUEUE\_TOO\_LARGE = -119 | There are too many DNS resolutions to be processed, and one of the requests in the queue is terminated. |
| ARKWEB\_ERR\_SOCKS\_CONNECTION\_FAILED = -120 | The connection between the target host and the SOCKS proxy server failed. |
| ARKWEB\_ERR\_SOCKS\_CONNECTION\_HOST\_UNREACHABLE = -121 | The SOCKS proxy server cannot connect to the target host because the target host is unreachable. |
| ARKWEB\_ERR\_ALPN\_NEGOTIATION\_FAILED = -122 | The request of ALPN failed. |
| ARKWEB\_ERR\_SSL\_NO\_RENEGOTIATION = -123 | The peer sent an **SSL no\_renegotiation** alert message. |
| ARKWEB\_ERR\_WINSOCK\_UNEXPECTED\_WRITTEN\_BYTES = -124 | Winsock sometimes reports unexpected written bytes. This may be caused by LSP damage. |
| ARKWEB\_ERR\_SSL\_DECOMPRESSION\_FAILURE\_ALERT = -125 | The SSL peer sent us a fatal **decompression\_failure** alert. This usually occurs when the peer falsely considers that it supports **DEFLATE** and selects it. |
| ARKWEB\_ERR\_SSL\_BAD\_RECORD\_MAC\_ALERT = -126 | The SSL peer sent us a fatal **BAD\_RECORD\_MAC** alert. This usually occurs on the server cannot support **DEFLATE** normally. |
| ARKWEB\_ERR\_PROXY\_AUTH\_REQUESTED = -127 | The proxy requests authentication for establishing a tunnel. |
| ARKWEB\_ERR\_PROXY\_CONNECTION\_FAILED = -130 | The connection to the proxy server fails. This is because an error occurs when the host resolves the name or connects its socket to the proxy server. Note that this does not include errors during the **HTTP CONNECT**. |
| ARKWEB\_ERR\_MANDATORY\_PROXY\_CONFIGURATION\_FAILED = -131 | The mandatory proxy configuration failed. Currently, this means that a mandatory PAC script cannot be obtained, parsed, or executed. |
| ARKWEB\_ERR\_PRECONNECT\_MAX\_SOCKET\_LIMIT = -133 | The maximum socket limit of the socket pool is reached during pre-connect. No more sockets need to be pre-connected. |
| ARKWEB\_ERR\_SSL\_CLIENT\_AUTH\_PRIVATE\_KEY\_ACCESS\_DENIED = -134 | The access to the private key of the SSL client certificate is denied. |
| ARKWEB\_ERR\_SSL\_CLIENT\_AUTH\_CERT\_NO\_PRIVATE\_KEY = -135 | The SSL client certificate does not have a private key. |
| ARKWEB\_ERR\_PROXY\_CERTIFICATE\_INVALID = -136 | The certificate provided by the HTTPS proxy is invalid. |
| ARKWEB\_ERR\_NAME\_RESOLUTION\_FAILED = -137 | The name (DNS) resolution failed. |
| ARKWEB\_ERR\_NETWORK\_ACCESS\_DENIED = -138 | The access to the network is denied. This error is distinguished from errors that are likely to be caused by firewalls and other errors caused by denied access. For details, see **ERR\_ACCESS\_DENIED**. |
| ARKWEB\_ERR\_TEMPORARILY\_THROTTLED = -139 | The request is temporarily throttled to avoid DDoS attacks. |
| ARKWEB\_ERR\_HTTPS\_PROXY\_TUNNEL\_RESPONSE\_REDIRECT = -140 | The request for creating an SSL tunnel connection through the HTTPS proxy receives a 302 (temporary redirection) response. The response body may contain the description of the failure cause. |
| ARKWEB\_ERR\_SSL\_CLIENT\_AUTH\_SIGNATURE\_FAILED = -141 | The **CertificateVerify** data of the SSL client authentication handshake cannot be signed using the private key of the client certificate. |
| ARKWEB\_ERR\_MSG\_TOO\_BIG = -142 | The message is too big to transfer. (For example, the UDP message exceeds the size limit). |
| ARKWEB\_ERR\_WS\_PROTOCOL\_ERROR = -145 | The WebSocket protocol is incorrect. This indicates that the connection is terminating due to a frame format error or other protocol violation. |
| ARKWEB\_ERR\_ADDRESS\_IN\_USE = -147 | The address is in use. |
| ARKWEB\_ERR\_SSL\_HANDSHAKE\_NOT\_COMPLETED = -148 | The operation failed because the SSL handshake is not completed. |
| ARKWEB\_ERR\_SSL\_BAD\_PEER\_PUBLIC\_KEY = -149 | The public key of the SSL peer is invalid. |
| ARKWEB\_ERR\_SSL\_PINNED\_KEY\_NOT\_IN\_CERT\_CHAIN = -150 | The certificate does not match the built-in public key Pins of the host name. Pin is set in **net/http/transport\_security\_state.cc**, and it is required that one of a set of public keys exist on the path from the leaf node to the root node. |
| ARKWEB\_ERR\_CLIENT\_AUTH\_CERT\_TYPE\_UNSUPPORTED = -151 | The server requests the client certificate, but the request does not contain any of the certificates we support. |
| ARKWEB\_ERR\_SSL\_DECRYPT\_ERROR\_ALERT = -153 | The SSL peer sent us a fatal **DECRYPT\_ERROR** alert. This usually occurs when the peer cannot verify the signature (in **CertificateVerify** or **ServerKeyExchange**) or verify the **Finished** message. |
| ARKWEB\_ERR\_WS\_THROTTLE\_QUEUE\_TOO\_LARGE = -154 | There are too many **WebSocketJob** instances to be processed. Therefore, new tasks are not pushed to the queue. |
| ARKWEB\_ERR\_SSL\_SERVER\_CERT\_CHANGED = -156 | During the renegotiation, the SSL server certificate is changed. |
| ARKWEB\_ERR\_SSL\_UNRECOGNIZED\_NAME\_ALERT = -159 | The SSL server sends us a fatal **unrecognized\_name** alert. |
| ARKWEB\_ERR\_SOCKET\_SET\_RECEIVE\_BUFFER\_SIZE\_ERROR = -160 | The size of the socket receive buffer cannot be set as requested. |
| ARKWEB\_ERR\_SOCKET\_SET\_SEND\_BUFFER\_SIZE\_ERROR = -161 | The size of the socket send buffer cannot be set as requested. |
| ARKWEB\_ERR\_SOCKET\_RECEIVE\_BUFFER\_SIZE\_UNCHANGEABLE = -162 | **setsockopt** returns a success code, but the socket's receive buffer size cannot be set to the requested value. |
| ARKWEB\_ERR\_SOCKET\_SEND\_BUFFER\_SIZE\_UNCHANGEABLE = -163 | **setsockopt** returns a success code, but the socket's send buffer size cannot be set to the requested value. |
| ARKWEB\_ERR\_SSL\_CLIENT\_AUTH\_CERT\_BAD\_FORMAT = -164 | The client certificate cannot be imported into the SSL library from the platform store. |
| ARKWEB\_ERR\_ICANN\_NAME\_COLLISION = -166 | When a host name is resolved to an IP address list, the IPv4 address **127.0.53.53** is included. This is a special IP address recommended by ICANN. It is used to indicate a name conflict and remind administrators of potential problems. |
| ARKWEB\_ERR\_SSL\_SERVER\_CERT\_BAD\_FORMAT = -167 | The SSL server provides a certificate that cannot be decoded. This is not a certificate error code because no **X509Certificate** object is available. This error is fatal. |
| ARKWEB\_ERR\_CT\_STH\_PARSING\_FAILED = -168 | Certificate Transparency: The received **Signed Tree Head** cannot be parsed. |
| ARKWEB\_ERR\_CT\_STH\_INCOMPLETE = -169 | Certificate transparency: The received **Signed Tree Head** can be successfully parsed into JSON, but some fields are missing. |
| ARKWEB\_ERR\_UNABLE\_TO\_REUSE\_CONNECTION\_FOR\_PROXY\_AUTH = -170 | The connection to send proxy authentication credentials cannot be reused before **AuthController** is start. The caller should reconnect the **AuthController**. This error is only used internally in the network stack. |
| ARKWEB\_ERR\_CT\_CONSISTENCY\_PROOF\_PARSING\_FAILED = -171 | Certificate transparency: The received consistency proof cannot be parsed. |
| ARKWEB\_ERR\_SSL\_OBSOLETE\_CIPHER = -172 | The SSL server requires an obsolete cipher suite. In one or two version updates after this cipher suite is removed, as a rollback policy, this error is temporarily signaled and then the rollback policy is removed. |
| ARKWEB\_ERR\_WS\_UPGRADE = -173 | This error code is used to cancel the **URLRequest** when the WebSocket handshake is successful and the connection has been upgraded. |
| ARKWEB\_ERR\_READ\_IF\_READY\_NOT\_IMPLEMENTED = -174 | The socket **ReadIfReady** is not implemented. This error should not be seen by the user because the normal **Read** method will be used as an alternative. |
| ARKWEB\_ERR\_NO\_BUFFER\_SPACE = -176 | No socket buffer space is available. |
| ARKWEB\_ERR\_SSL\_CLIENT\_AUTH\_NO\_COMMON\_ALGORITHMS = -177 | There is no common signing algorithm between the private key of the client certificate and the preferences of the server. |
| ARKWEB\_ERR\_EARLY\_DATA\_REJECTED = -178 | The server rejected TLS 1.3 Early Data. This error will be received before any data is returned from the socket. Early Data should be disabled and the request should be retried. |
| ARKWEB\_ERR\_WRONG\_VERSION\_ON\_EARLY\_DATA = -179 | The server responds with TLS 1.2 or earlier when TLS 1.3 Early Data is provided. This is an internal error code to solve the backward compatibility problem between Early Data and TLS 1.2. |
| ARKWEB\_ERR\_TLS13\_DOWNGRADE\_DETECTED = -180 | The server negotiated an earlier version when TLS 1.3 is supported. |
| ARKWEB\_ERR\_SSL\_KEY\_USAGE\_INCOMPATIBLE = -181 | The server's certificate has a keyUsage extension that is incompatible with the negotiated TLS key exchange method. |
| ARKWEB\_ERR\_INVALID\_ECH\_CONFIG\_LIST = -182 | The **ECHConfigList** obtained through DNS cannot be resolved. |
| ARKWEB\_ERR\_ECH\_NOT\_NEGOTIATED = -183 | **Encrypted Client Hello (ECH)** is enabled, but the server cannot decrypt the encrypted **ClientHello**. |
| ARKWEB\_ERR\_ECH\_FALLBACK\_CERTIFICATE\_INVALID = -184 | **Encrypted Client Hello (ECH)** is enabled, but the server cannot decrypt the encrypted **ClientHello** and does not provide a certificate valid for the public name. |
| ARKWEB\_ERR\_CERT\_COMMON\_NAME\_INVALID = -200 | The server responds with a certificate whose common name does not match the host name. The possible causes are: 1. The attacker redirects the traffic to its server and presents a certificate that they know the private key. |
| ARKWEB\_ERR\_CERT\_DATE\_INVALID = -201 | The server responds with a certificate, but according to the host clock, the certificate does not take effect or is expired. The possible causes are: 1. The attacker provides an old certificate and obtains the private key.2. The server is incorrectly configured and no valid certificate is provided.3. The host clock is wrong. |
| ARKWEB\_ERR\_CERT\_AUTHORITY\_INVALID = -202 | The server responds with a certificate signed by an authority that we do not trust. The possible causes are: 1. The attacker replaces the real certificate with a certificate that contains its public key and is signed by its associates. |
| ARKWEB\_ERR\_CERT\_CONTAINS\_ERRORS = -203 | The certificate returned by the server contains an error, which cannot be rectified. MSDN describes this error as "The SSL certificate contains an error". Note: It is not clear how this error differs from **ERR\_CERT\_INVALID**. |
| ARKWEB\_ERR\_CERT\_NO\_REVOCATION\_MECHANISM = -204 | The certificate does not have a revocation mechanism. In other words, this certificate cannot be revoked. |
| ARKWEB\_ERR\_CERT\_UNABLE\_TO\_CHECK\_REVOCATION = -205 | Revocation information for this website's security certificate is not available. The possible causes are: 1. The attacker has cracked the private key in the certificate and prevented the host from finding out that the certificate is revoked.2. The certificate is not revoked, but the revocation server is busy or unavailable. |
| ARKWEB\_ERR\_CERT\_REVOKED = -206 | The certificate responded by the server is revoked. This error could but not should be ignored. |
| ARKWEB\_ERR\_CERT\_INVALID = -207 | The server responds with an invalid certificate. This error cannot be rectified. MSDN describes this error as follows: "The SSL certificate is invalid." |
| ARKWEB\_ERR\_CERT\_WEAK\_SIGNATURE\_ALGORITHM = -208 | The server responds with a certificate signed using a weak signing algorithm. |
| ARKWEB\_ERR\_CERT\_NON\_UNIQUE\_NAME = -210 | The host name specified in the certificate is not unique. |
| ARKWEB\_ERR\_CERT\_WEAK\_KEY = -211 | The server responds with a certificate containing a weak key (for example, a too small RSA key). |
| ARKWEB\_ERR\_CERT\_NAME\_CONSTRAINT\_VIOLATION = -212 | The **DNS** name declared in the certificate violates the name constraint. |
| ARKWEB\_ERR\_CERT\_VALIDITY\_TOO\_LONG = -213 | The validity period of the certificate is too long. |
| ARKWEB\_ERR\_CERTIFICATE\_TRANSPARENCY\_REQUIRED = -214 | Certificate Transparency is required, but the server does not provide CT information that complies with the policy. |
| ARKWEB\_ERR\_CERT\_SYMANTEC\_LEGACY = -215 | The certificate is linked to an old Symantec certificate or its subsidiaries that are no longer trusted. |
| ARKWEB\_ERR\_CERT\_KNOWN\_INTERCEPTION\_BLOCKED = -217 | The certificate is intercepted by an entity other than the device owner. |
| ARKWEB\_ERR\_SSL\_OBSOLETE\_VERSION\_OR\_CIPHER = -218 | The connection uses an obsolete version of SSL/TLS or an encryption algorithm. |
| ARKWEB\_ERR\_CERT\_END = -219 | The error immediately follows the last certificate error code. |
| ARKWEB\_ERR\_INVALID\_URL = -300 | The URL is invalid. |
| ARKWEB\_ERR\_DISALLOWED\_URL\_SCHEME = -301 | The URL scheme is not allowed. |
| ARKWEB\_ERR\_UNKNOWN\_URL\_SCHEME = -302 | The URL scheme is unknown. |
| ARKWEB\_ERR\_INVALID\_REDIRECT = -303 | An invalid URL redirection occurs when a URL is loaded. |
| ARKWEB\_ERR\_TOO\_MANY\_REDIRECTS = -310 | Too many URL redirections occurred when a URL is being loaded. |
| ARKWEB\_ERR\_UNSAFE\_REDIRECT = -311 | An insecure URL redirection occurs when a URL is loaded (for example, redirection to **file://** is considered insecure). |
| ARKWEB\_ERR\_UNSAFE\_PORT = -312 | The port number of the URL to be loaded is unsafe. |
| ARKWEB\_ERR\_INVALID\_RESPONSE = -320 | The response from the server is invalid. |
| ARKWEB\_ERR\_INVALID\_CHUNKED\_ENCODING = -321 | The chunked encoding is invalid. |
| ARKWEB\_ERR\_METHOD\_UNSUPPORTED = -322 | The server does not support the request method. |
| ARKWEB\_ERR\_UNEXPECTED\_PROXY\_AUTH = -323 | The response value is **407**, indicating proxy authentication is required, but the host does not send the request to the proxy. |
| ARKWEB\_ERR\_EMPTY\_RESPONSE = -324 | The server closes the connection and does not response. |
| ARKWEB\_ERR\_RESPONSE\_HEADERS\_TOO\_BIG = -325 | The response headers are too big. |
| ARKWEB\_ERR\_PAC\_SCRIPT\_FAILED = -327 | The PAC script failed. |
| ARKWEB\_ERR\_REQUEST\_RANGE\_NOT\_SATISFIABLE = -328 | The response code is 416, indicating the server cannot meet the request range. |
| ARKWEB\_ERR\_MALFORMED\_IDENTITY = -329 | The identity is malformed. |
| ARKWEB\_ERR\_CONTENT\_DECODING\_FAILED = -330 | The content decoding of the response body failed. |
| ARKWEB\_ERR\_NETWORK\_IO\_SUSPENDED = -331 | The operation failed because all network I/Os are suspended. |
| ARKWEB\_ERR\_SYN\_REPLY\_NOT\_RECEIVED = -332 | FLIP data is received before **SYN\_REPLY** is received on the flow. |
| ARKWEB\_ERR\_ENCODING\_CONVERSION\_FAILED = -333 | The response failed to be converted to the target encoding. |
| ARKWEB\_ERR\_UNRECOGNIZED\_FTP\_DIRECTORY\_LISTING\_FORMAT = -334 | The server sent an unrecognized FTP directory listing format. |
| ARKWEB\_ERR\_NO\_SUPPORTED\_PROXIES = -336 | There are no supported proxies in the list provided. |
| ARKWEB\_ERR\_HTTP2\_PROTOCOL\_ERROR = -337 | An HTTP/2 protocol error occurs. |
| ARKWEB\_ERR\_INVALID\_AUTH\_CREDENTIALS = -338 | The HTTP authentication credentials are invalid. |
| ARKWEB\_ERR\_UNSUPPORTED\_AUTH\_SCHEME = -339 | The HTTP authentication scheme is not supported. |
| ARKWEB\_ERR\_ENCODING\_DETECTION\_FAILED = -340 | The encoding detection failed. |
| ARKWEB\_ERR\_MISSING\_AUTH\_CREDENTIALS = -341 | (GSSAPI) The Kerberos credentials of HTTP authentication are missing. |
| ARKWEB\_ERR\_UNEXPECTED\_SECURITY\_LIBRARY\_STATUS = -342 | The SSPI or GSSAPI status code is unexpected. |
| ARKWEB\_ERR\_MISCONFIGURED\_AUTH\_ENVIRONMENT = -343 | The authentication environment is misconfigured. (For example, the KDC cannot be found or the principal is unknown). |
| ARKWEB\_ERR\_UNDOCUMENTED\_SECURITY\_LIBRARY\_STATUS = -344 | The SSPI or GSSAPI status code is undocumented. |
| ARKWEB\_ERR\_RESPONSE\_BODY\_TOO\_BIG\_TO\_DRAIN = -345 | The HTTP response body is too big to drain. |
| ARKWEB\_ERR\_RESPONSE\_HEADERS\_MULTIPLE\_CONTENT\_LENGTH = -346 | Multiple Content-Length response headers are included in an HTTP response. |
| ARKWEB\_ERR\_INCOMPLETE\_HTTP2\_HEADERS = -347 | The HTTP/2 response headers are incomplete. Therefore, more frames are needed to complete them. |
| ARKWEB\_ERR\_PAC\_NOT\_IN\_DHCP = -348 | The PAC URL configuration cannot be retrieved from DHCP. This may indicate that the retrieving failed, or that the PAC URL is not configured in DHCP. |
| ARKWEB\_ERR\_RESPONSE\_HEADERS\_MULTIPLE\_CONTENT\_DISPOSITION = -349 | Multiple **Content-Disposition** headers are included in an HTTP response. |
| ARKWEB\_ERR\_RESPONSE\_HEADERS\_MULTIPLE\_LOCATION = -350 | Multiple **Location** headers are included in an HTTP response. |
| ARKWEB\_ERR\_HTTP2\_SERVER\_REFUSED\_STREAM = -351 | The HTTP/2 server rejects the request without processing it and sends a **GOAWAY** frame with the error code **NO\_ERROR** and a **Last-Stream-ID** lower than the stream ID of the request. |
| ARKWEB\_ERR\_HTTP2\_PING\_FAILED = -352 | The HTTP/2 server does not respond to the **PING**. |
| ARKWEB\_ERR\_CONTENT\_LENGTH\_MISMATCH = -354 | When the connection is closed, the number of bytes transmitted in the HTTP response body is less than the number of bytes advertised in the **Content-Length** header. |
| ARKWEB\_ERR\_INCOMPLETE\_CHUNKED\_ENCODING = -355 | The HTTP response body is transmitted using chunked encoding, and the terminated zero-length block is not sent when the connection is closed. |
| ARKWEB\_ERR\_QUIC\_PROTOCOL\_ERROR = -356 | A QUIC protocol error occurs. |
| ARKWEB\_ERR\_RESPONSE\_HEADERS\_TRUNCATED = -357 | The HTTP response headers are truncated by the end of file (EOF). |
| ARKWEB\_ERR\_QUIC\_HANDSHAKE\_FAILED = -358 | The QUIC encryption handshake failed. This means that the server cannot read any requests, so they may be resent. |
| ARKWEB\_ERR\_HTTP2\_INADEQUATE\_TRANSPORT\_SECURITY = -360 | The transport security is inadequate to HTTP/2. |
| ARKWEB\_ERR\_HTTP2\_FLOW\_CONTROL\_ERROR = -361 | The peer violates HTTP/2 flow control. |
| ARKWEB\_ERR\_HTTP2\_FRAME\_SIZE\_ERROR = -362 | The peer sends an HTTP/2 frame with an incorrect size. |
| ARKWEB\_ERR\_HTTP2\_COMPRESSION\_ERROR = -363 | The decoding or encoding of the compressed HTTP/2 response header information failed. |
| ARKWEB\_ERR\_PROXY\_AUTH\_REQUESTED\_WITH\_NO\_CONNECTION = -364 | The proxy authentication of a request does not have a valid client socket handle. |
| ARKWEB\_ERR\_HTTP\_1\_1\_REQUIRED = -365 | The HTTP/2 session receives an **HTTP\_1\_1\_REQUIRED** error code. |
| ARKWEB\_ERR\_PROXY\_HTTP\_1\_1\_REQUIRED = -366 | The **HTTP\_1\_1\_REQUIRED** error code is received when the HTTP/2 session proxy is used. |
| ARKWEB\_ERR\_PAC\_SCRIPT\_TERMINATED = -367 | The PAC script has been terminated and must be reloaded. |
| ARKWEB\_ERR\_INVALID\_HTTP\_RESPONSE = -370 | The server should return an **HTTP/1.x** response. But it returns an **HTTP/0.9** response. |
| ARKWEB\_ERR\_CONTENT\_DECODING\_INIT\_FAILED = -371 | The content decoding fails to be initialized. |
| ARKWEB\_ERR\_HTTP2\_RST\_STREAM\_NO\_ERROR\_RECEIVED = -372 | An **HTTP/2 RST\_STREAM** frame with **NO\_ERROR** is received. This error should be handled internally by HTTP/2 and should not exceed the SpdyStream layer. |
| ARKWEB\_ERR\_HTTP2\_PUSHED\_STREAM\_NOT\_AVAILABLE = -373 | The pushed stream claimed by the request is not available. |
| ARKWEB\_ERR\_HTTP2\_CLAIMED\_PUSHED\_STREAM\_RESET\_BY\_SERVER = -374 | The claimed pushed stream is reset by the server. In this case, the request should be retried. |
| ARKWEB\_ERR\_TOO\_MANY\_RETRIES = -375 | There are too many retries due to invalid authentication or certificate. |
| ARKWEB\_ERR\_HTTP2\_STREAM\_CLOSED = -376 | An HTTP/2 frame is received on the closed stream. |
| ARKWEB\_ERR\_HTTP2\_CLIENT\_REFUSED\_STREAM = -377 | The client refuses an HTTP/2 stream. |
| ARKWEB\_ERR\_HTTP2\_PUSHED\_RESPONSE\_DOES\_NOT\_MATCH = -378 | Based on the matched URL and request header, an HTTP/2 pushed stream is received by the request, but the pushed response header does not match the request. |
| ARKWEB\_ERR\_HTTP\_RESPONSE\_CODE\_FAILURE = -379 | The server returns a non-2xx HTTP response code. |
| ARKWEB\_ERR\_QUIC\_UNKNOWN\_CERT\_ROOT = -380 | The certificate displayed on the QUIC connection is not linked to a known root certificate, and the connected original server is not in the list of domain names that allow unknown root certificates. |
| ARKWEB\_ERR\_QUIC\_GOAWAY\_REQUEST\_CAN\_BE\_RETRIED = -381 | A **GOAWAY** frame has been received, indicating that the request has not been processed and therefore can be safely retried on a different connection. |
| ARKWEB\_ERR\_TOO\_MANY\_ACCEPT\_CH\_RESTARTS = -382 | **ACCEPT\_CH\_RESTARTS** has been triggered too many times. |
| ARKWEB\_ERR\_INCONSISTENT\_IP\_ADDRESS\_SPACE = -383 | In the same request, the IP address space of the remote endpoint is different from the previous one. Cache entries for any affected requests should be marked as invalid. |
| ARKWEB\_ERR\_CACHED\_IP\_ADDRESS\_SPACE\_BLOCKED\_BY\_LOCAL\_NETWORK\_ACCESS\_POLICY = -384 | The cached IP address space of the remote endpoint is blocked by a local network access policy. |
| ARKWEB\_ERR\_CACHE\_MISS = -400 | The entry for the request is not in the cache. |
| ARKWEB\_ERR\_CACHE\_READ\_FAILURE = -401 | The entry cannot be read from the cache. |
| ARKWEB\_ERR\_CACHE\_WRITE\_FAILURE = -402 | The entry cannot be written to the cache. |
| ARKWEB\_ERR\_CACHE\_OPERATION\_UNSUPPORTED = -403 | The entry does not support this operation. |
| ARKWEB\_ERR\_CACHE\_OPEN\_FAILURE = -404 | The cache could not open this entry. |
| ARKWEB\_ERR\_CACHE\_CREATE\_FAILURE = -405 | The cache could not create this entry. |
| ARKWEB\_ERR\_CACHE\_RACE = -406 | Multiple transactions are competing to create disk cache entries. |
| ARKWEB\_ERR\_CACHE\_CHECKSUM\_READ\_FAILURE = -407 | The cache could not read the checksum on the entry. |
| ARKWEB\_ERR\_CACHE\_CHECKSUM\_MISMATCH = -408 | An entry with an invalid checksum is found in the cache. |
| ARKWEB\_ERR\_CACHE\_LOCK\_TIMEOUT = -409 | The HTTP cache contains an error code. |
| ARKWEB\_ERR\_CACHE\_AUTH\_FAILURE\_AFTER\_READ = -410 | A challenge is received after the transaction reads some data, but the credentials are unavailable. |
| ARKWEB\_ERR\_CACHE\_ENTRY\_NOT\_SUITABLE = -411 | An internal non-standard error code used for the HTTP cache. |
| ARKWEB\_ERR\_CACHE\_DOOM\_FAILURE = -412 | The cache cannot delete this entry. |
| ARKWEB\_ERR\_CACHE\_OPEN\_OR\_CREATE\_FAILURE = -413 | The cache cannot open or create the entry. |
| ARKWEB\_ERR\_INSECURE\_RESPONSE = -501 | The server response is insecure (for example, there is a certificate error). |
| ARKWEB\_ERR\_NO\_PRIVATE\_KEY\_FOR\_CERT = -502 | The client certificate failed to be imported because the user's key database does not have a private key. |
| ARKWEB\_ERR\_ADD\_USER\_CERT\_FAILED = -503 | The certificate failed to be added to the OS certificate database. |
| ARKWEB\_ERR\_INVALID\_SIGNED\_EXCHANGE = -504 | The signed exchange is invalid. |
| ARKWEB\_ERR\_INVALID\_WEB\_BUNDLE = -505 | The web bundle resources are invalid. |
| ARKWEB\_ERR\_TRUST\_TOKEN\_OPERATION\_FAILED = -506 | The request for performing the Trust Tokens protocol operation failed. The possible causes include prerequisite failure, internal error, and bad response. |
| ARKWEB\_ERR\_TRUST\_TOKEN\_OPERATION\_SUCCESS\_WITHOUT\_SENDING\_REQUEST = -507 | When processing an operation execution request related to the Trust Tokens protocol, the system performs the Trust Tokens operation in the request, but does not send the request to the specified destination. |
| ARKWEB\_ERR\_FTP\_FAILED = -601 | The FTP control connection command failed. If possible, replace this error code with a more specific one. |
| ARKWEB\_ERR\_FTP\_SERVICE\_UNAVAILABLE = -602 | The server cannot support the request. This is a temporary error. The FTP response code is 421. |
| ARKWEB\_ERR\_FTP\_TRANSFER\_ABORTED = -603 | The server aborts the transfer. The FTP response code is 426. |
| ARKWEB\_ERR\_FTP\_FILE\_BUSY = -604 | The file is in use, or some other temporary errors occur when the file is opened. The FTP response code is 450. |
| ARKWEB\_ERR\_FTP\_SYNTAX\_ERROR = -605 | The server rejects the command from the host due to a syntax error. The FTP response code is 500 or 501. |
| ARKWEB\_ERR\_FTP\_COMMAND\_UNSUPPORTED = -606 | The server does not support the command. The FTP response code is 502 or 504. |
| ARKWEB\_ERR\_FTP\_BAD\_COMMAND\_SEQUENCE = -607 | The server rejects the commands from the host because the host does not send the commands in the correct sequence. The FTP response code is 503. |
| ARKWEB\_ERR\_PKCS12\_IMPORT\_BAD\_PASSWORD = -701 | The **PKCS #12** file cannot be imported because the password is incorrect. |
| ARKWEB\_ERR\_PKCS12\_IMPORT\_FAILED = -702 | The **PKCS #12** file cannot be imported due to other errors. |
| ARKWEB\_ERR\_IMPORT\_CA\_CERT\_NOT\_CA = -703 | The CA certificate cannot be imported because it is not a real CA certificate. |
| ARKWEB\_ERR\_IMPORT\_CERT\_ALREADY\_EXISTS = -704 | The certificate cannot be imported because it already exists in the database. |
| ARKWEB\_ERR\_IMPORT\_CA\_CERT\_FAILED = -705 | The CA failed to be imported due to other errors. |
| ARKWEB\_ERR\_IMPORT\_SERVER\_CERT\_FAILED = -706 | The server certificate failed to be imported due to some internal errors. |
| ARKWEB\_ERR\_PKCS12\_IMPORT\_INVALID\_MAC = -707 | The **PKCS #12** file failed to be imported because the message authentication code (MAC) is invalid. |
| ARKWEB\_ERR\_PKCS12\_IMPORT\_INVALID\_FILE = -708 | The **PKCS #12** file failed to be imported because the file is invalid or corrupted. |
| ARKWEB\_ERR\_PKCS12\_IMPORT\_UNSUPPORTED = -709 | The **PKCS #12** file failed to be imported due to its unsupported features. |
| ARKWEB\_ERR\_KEY\_GENERATION\_FAILED = -710 | The key generation failed. |
| ARKWEB\_ERR\_PRIVATE\_KEY\_EXPORT\_FAILED = -712 | The private key failed to be exported. |
| ARKWEB\_ERR\_SELF\_SIGNED\_CERT\_GENERATION\_FAILED = -713 | The self-signed certificate failed to be generated. |
| ARKWEB\_ERR\_CERT\_DATABASE\_CHANGED = -714 | The certificate database is changed. |
| ARKWEB\_ERR\_CERT\_VERIFIER\_CHANGED = -716 | The certificate verifier configuration is changed. |
| ARKWEB\_ERR\_DNS\_MALFORMED\_RESPONSE = -800 | The DNS resolver receives a response that the format is incorrect. |
| ARKWEB\_ERR\_DNS\_SERVER\_REQUIRES\_TCP = -801 | The DNS server requires TCP. |
| ARKWEB\_ERR\_DNS\_SERVER\_FAILED = -802 | The DNS server failed. This error code is returned for all of the following errors: 1 - Format error - The name server cannot interpret the query. 2 - Server failure - The name server cannot process the query due to its own problems. 3 - Not supported - The name server does not support the query type of the request. |
| ARKWEB\_ERR\_DNS\_TIMED\_OUT = -803 | The DNS transaction timed out. |
| ARKWEB\_ERR\_DNS\_CACHE\_MISS = -804 | The entry is not found in the cache or other local sources. |
| ARKWEB\_ERR\_DNS\_SEARCH\_EMPTY = -805 | The suffix search list rule prevents the resolution of a given host name. |
| ARKWEB\_ERR\_DNS\_SORT\_ERROR = -806 | Addresses are not sorted according to RFC 3484. |
| ARKWEB\_ERR\_DNS\_SECURE\_RESOLVER\_HOSTNAME\_RESOLUTION\_FAILED = -808 | The host name of the DNS-over-HTTPS server cannot be resolved. |
| ARKWEB\_ERR\_DNS\_NAME\_HTTPS\_ONLY = -809 | DNS has identified that the request is prohibited due to insecure connections (HTTP/WS). The application should handle this error like HTTP redirection, redirecting the connection to secure HTTPS or WSS. |
| ARKWEB\_ERR\_DNS\_REQUEST\_CANCELED = -810 | All DNS requests related to this task are canceled. |
| ARKWEB\_ERR\_DNS\_NO\_MATCHING\_SUPPORTED\_ALPN = -811 | The host name resolution of the HTTPS record is not resolved using the ALPN value of the supported protocol. |
