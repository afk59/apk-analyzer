# @ohos.web.netErrorList(The List of ArkWeb Network Protocol Stack Errors)

Provides a list of ArkWeb network protocol stack errors.

The error codes of the ArkWeb network protocol stack are mapped to the Chromium error codes in [net\_error\_list.h](https://chromium.googlesource.com/chromium/src.git/+/refs/heads/main/net/base/net_error_list.h).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/dwWHJaz3QWu4w7DEMMVK3Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD8BADE10BF99093BFCAD065EDD8E0279ACFD48F0C464EA7FC25D8D91032890B)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { WebNetErrorList } from '@kit.ArkWeb';

#### WebNetErrorList

Provides a list of ArkWeb network protocol stack errors.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NET\_OK | 0 | The access is normal. |
| ERR\_IO\_PENDING | \-1 | The asynchronous I/O operation is pending. |
| ERR\_FAILED | \-2 | A common error occurs. |
| ERR\_ABORTED | \-3 | The operation is aborted. |
| ERR\_INVALID\_ARGUMENT | \-4 | The parameter is invalid. |
| ERR\_INVALID\_HANDLE | \-5 | The handle of the file descriptor is invalid. |
| ERR\_FILE\_NOT\_FOUND | \-6 | The file is not found. |
| ERR\_TIMED\_OUT | \-7 | The operation times out. |
| ERR\_FILE\_TOO\_LARGE | \-8 | The file is too large. |
| ERR\_UNEXPECTED | \-9 | The problem is not expected or specifically handled. |
| ERR\_ACCESS\_DENIED | \-10 | The access to resources other than the network is denied. |
| ERR\_NOT\_IMPLEMENTED | \-11 | The operation fails because the function is not implemented. |
| ERR\_INSUFFICIENT\_RESOURCES | \-12 | The resources required for system or program execution are insufficient. |
| ERR\_OUT\_OF\_MEMORY | \-13 | A memory overflow occurs. |
| ERR\_UPLOAD\_FILE\_CHANGED | \-14 | The file cannot be uploaded because the file modification time is not as expected. |
| ERR\_SOCKET\_NOT\_CONNECTED | \-15 | The socket is disconnected. |
| ERR\_FILE\_EXISTS | \-16 | The file already exists. |
| ERR\_FILE\_PATH\_TOO\_LONG | \-17 | The file path or file name is too long. |
| ERR\_FILE\_NO\_SPACE | \-18 | The disk space is insufficient. |
| ERR\_FILE\_VIRUS\_INFECTED | \-19 | The file contains viruses. |
| ERR\_BLOCKED\_BY\_CLIENT | \-20 | The request is blocked by the client. |
| ERR\_NETWORK\_CHANGED | \-21 | The network is changed. |
| ERR\_BLOCKED\_BY\_ADMINISTRATOR | \-22 | The request is blocked by the administrator. |
| ERR\_SOCKET\_CONNECTED | \-23 | The socket is already connected. |
| ERR\_UPLOAD\_STREAM\_REWIND\_NOT\_SUPPORTED | \-25 | The stream rewinding is not supported. |
| ERR\_CONTEXT\_SHUT\_DOWN | \-26 | The request fails because the context is closed. |
| ERR\_BLOCKED\_BY\_RESPONSE | \-27 | The request is blocked by response from headers such as X-Frame-Options, Content Security Policy, and Cross Origin Resource Policy. |
| ERR\_CLEARTEXT\_NOT\_PERMITTED | \-29 | The request fails because cleartext is not permitted by the system policy. |
| ERR\_BLOCKED\_BY\_CSP | \-30 | The request is blocked by the Content Security Policy. |
| ERR\_H2\_OR\_QUIC\_REQUIRED | \-31 | The request is blocked because there is no H/2 or QUIC session. |
| ERR\_BLOCKED\_BY\_ORB | \-32 | The request is blocked by CORB or ORB. |
| ERR\_CONNECTION\_CLOSED | \-100 | The connection has been closed. |
| ERR\_CONNECTION\_RESET | \-101 | The connection is reset. |
| ERR\_CONNECTION\_REFUSED | \-102 | The connection is refused. |
| ERR\_CONNECTION\_ABORTED | \-103 | The connection times out because the ACK message for sending data is not received. This may contain a FIN packet. |
| ERR\_CONNECTION\_FAILED | \-104 | The connection failed. |
| ERR\_NAME\_NOT\_RESOLVED | \-105 | The domain name cannot be resolved. |
| ERR\_INTERNET\_DISCONNECTED | \-106 | The Internet is disconnected. |
| ERR\_SSL\_PROTOCOL\_ERROR | \-107 | The SSL protocol is incorrect. |
| ERR\_ADDRESS\_INVALID | \-108 | The IP address or port number is invalid (for example, IP address 0 or port 0 cannot be connected). |
| ERR\_ADDRESS\_UNREACHABLE | \-109 | The IP address is unreachable. This means that there is no route to the specified host or network. |
| ERR\_SSL\_CLIENT\_AUTH\_CERT\_NEEDED | \-110 | The server specifies that the client needs to provide an SSL certificate for authentication. |
| ERR\_TUNNEL\_CONNECTION\_FAILED | \-111 | The tunnel connection to the proxy cannot be established. |
| ERR\_NO\_SSL\_VERSIONS\_ENABLED | \-112 | No version of the SSL protocol is supported. |
| ERR\_SSL\_VERSION\_OR\_CIPHER\_MISMATCH | \-113 | The client and server do not support the common SSL protocol version or cipher suite. |
| ERR\_SSL\_RENEGOTIATION\_REQUESTED | \-114 | The server requests renegotiation (rehandshake). |
| ERR\_PROXY\_AUTH\_UNSUPPORTED | \-115 | The proxy requests authentication when the method for tunnel connection is not supported. |
| ERR\_BAD\_SSL\_CLIENT\_AUTH\_CERT | \-117 | The SSL client certificate is incorrect. |
| ERR\_CONNECTION\_TIMED\_OUT | \-118 | The connection times out. |
| ERR\_HOST\_RESOLVER\_QUEUE\_TOO\_LARGE | \-119 | The request in the queue is aborted because there are too many pending DNS resolutions. |
| ERR\_SOCKS\_CONNECTION\_FAILED | \-120 | The connection between the SOCKS proxy server and the target host fails to be established. |
| ERR\_SOCKS\_CONNECTION\_HOST\_UNREACHABLE | \-121 | The domain name of the SOCKS proxy server is unreachable. |
| ERR\_ALPN\_NEGOTIATION\_FAILED | \-122 | The request for negotiating the standby protocol fails. |
| ERR\_SSL\_NO\_RENEGOTIATION | \-123 | The server sends an **SSL no\_renegotiation** alert message. |
| ERR\_WINSOCK\_UNEXPECTED\_WRITTEN\_BYTES | \-124 | Winsock sometimes reports that more data is written than is passed. This may be caused by LSP damage. |
| ERR\_SSL\_DECOMPRESSION\_FAILURE\_ALERT | \-125 | The SSL peer sent a decompression failure alert to the local end. This usually occurs when the peer mistakenly believes that it supports DEFLATE compression. |
| ERR\_SSL\_BAD\_RECORD\_MAC\_ALERT | \-126 | The SSL peer sent a **bad\_record\_mac** alert to the local end. This may occur on a server that is not support DELEGATE. |
| ERR\_PROXY\_AUTH\_REQUESTED | \-127 | The proxy requests authentication for tunnel establishment. |
| ERR\_PROXY\_CONNECTION\_FAILED | \-130 | The connection to the proxy server cannot be established. This is because an error occurs when resolving the domain name or connecting to the socket. Note that this does not include failures during the HTTP CONNECT. |
| ERR\_MANDATORY\_PROXY\_CONFIGURATION\_FAILED | \-131 | The forcible proxy configuration cannot be used. Currently, this means that a mandatory PAC script cannot be obtained, parsed, or executed. |
| ERR\_PRECONNECT\_MAX\_SOCKET\_LIMIT | \-133 | The limit of the socket pool is exceeded during pre-connection. Therefore, you do not need to try to pre-connect more sockets. |
| ERR\_SSL\_CLIENT\_AUTH\_PRIVATE\_KEY\_ACCESS\_DENIED | \-134 | The access to the private key of the SSL client certificate is denied. |
| ERR\_SSL\_CLIENT\_AUTH\_CERT\_NO\_PRIVATE\_KEY | \-135 | The SSL client certificate does not have a private key. |
| ERR\_PROXY\_CERTIFICATE\_INVALID | \-136 | The certificate provided by the HTTPS proxy is invalid. |
| ERR\_NAME\_RESOLUTION\_FAILED | \-137 | The domain name resolution (DNS) failed. |
| ERR\_NETWORK\_ACCESS\_DENIED | \-138 | The network is disabled. |
| ERR\_TEMPORARILY\_THROTTLED | \-139 | This request was canceled due to throttling to avoid DDoS. |
| ERR\_HTTPS\_PROXY\_TUNNEL\_RESPONSE\_REDIRECT | \-140 | The request for creating an SSL tunnel connection through the HTTPS proxy receives 302. (The response may contain the description of the request failure cause.) |
| ERR\_SSL\_CLIENT\_AUTH\_SIGNATURE\_FAILED | \-141 | The private key of the client certificate cannot be used to sign the CertificateVerify data in SSL handshake process. |
| ERR\_MSG\_TOO\_BIG | \-142 | The message is too large to be transmitted. (For example, UDP messages exceed the size threshold). |
| ERR\_WS\_PROTOCOL\_ERROR | \-145 | The WebSocket protocol is incorrect. This error indicates that the connection is being terminated due to a frame format error or a conflict with other protocols. |
| ERR\_ADDRESS\_IN\_USE | \-147 | The address is already in use. |
| ERR\_SSL\_HANDSHAKE\_NOT\_COMPLETED | \-148 | The operation failed because the SSL handshake is not complete. |
| ERR\_SSL\_BAD\_PEER\_PUBLIC\_KEY | \-149 | The SSL public key is incorrect. |
| ERR\_SSL\_PINNED\_KEY\_NOT\_IN\_CERT\_CHAIN | \-150 | The received certificate does not match the public key specified by the built-in domain name. |
| ERR\_CLIENT\_AUTH\_CERT\_TYPE\_UNSUPPORTED | \-151 | The server's request for a client certificate is not supported by the local host. |
| ERR\_SSL\_DECRYPT\_ERROR\_ALERT | \-153 | The SSL peer sent a **decrypt\_error** alert to the local end. This error usually occurs when the peer cannot verify the signature (in CertificateVerify or ServerKeyExchange) or validate the Finished message. |
| ERR\_WS\_THROTTLE\_QUEUE\_TOO\_LARGE | \-154 | There are too many suspended WebSocketJob instances. Therefore, new Job instances are not pushed to the queue. |
| ERR\_SSL\_SERVER\_CERT\_CHANGED | \-156 | The SSL server certificate is changed during renegotiation. |
| ERR\_SSL\_UNRECOGNIZED\_NAME\_ALERT | \-159 | The SSL server sent a fatal unknown alert to the local end. |
| ERR\_SOCKET\_SET\_RECEIVE\_BUFFER\_SIZE\_ERROR | \-160 | The receive buffer size of the socket is not set as requested. |
| ERR\_SOCKET\_SET\_SEND\_BUFFER\_SIZE\_ERROR | \-161 | The send buffer size of the socket is not set as requested. |
| ERR\_SOCKET\_RECEIVE\_BUFFER\_SIZE\_UNCHANGEABLE | \-162 | The **setsockopt()** returned a success code, but the receive buffer size of the socket is not set as requested. |
| ERR\_SOCKET\_SEND\_BUFFER\_SIZE\_UNCHANGEABLE | \-163 | The **setsockopt()** returned a success code, but the send buffer size of the socket is not set as requested. |
| ERR\_SSL\_CLIENT\_AUTH\_CERT\_BAD\_FORMAT | \-164 | The client certificate cannot be imported into the SSL library from the platform store. |
| ERR\_ICANN\_NAME\_COLLISION | \-166 | The host name is resolved to an IP address list containing the IPv4 address 127.0.53.53. This is a special IP address recommended by ICANN. It is used to indicate that there is a name conflict and remind administrators of potential problems. |
| ERR\_SSL\_SERVER\_CERT\_BAD\_FORMAT | \-167 | The SSL server provides a certificate that cannot be decoded. This is not a certificate error code because no X509Certificate object is available. This error is fatal. |
| ERR\_CT\_STH\_PARSING\_FAILED | \-168 | The Certificate Transparency failed to parse the signed tree head. |
| ERR\_CT\_STH\_INCOMPLETE | \-169 | The Certificate Transparency parsed signed tree head successfully, but some information is missing. |
| ERR\_UNABLE\_TO\_REUSE\_CONNECTION\_FOR\_PROXY\_AUTH | \-170 | The attempt to re-send proxy authentication credentials failed because the AuthController has not generated the credentials yet. The caller should reconnect the AuthController. |
| ERR\_CT\_CONSISTENCY\_PROOF\_PARSING\_FAILED | \-171 | The Certificate Transparency failed to parse the consistency proof. |
| ERR\_SSL\_OBSOLETE\_CIPHER | \-172 | The SSL server requires an unsupported cipher suite, which has been deleted. This error will immediately occur in a rollback of one or two versions after the cipher suite is deleted, after which the rollback will be deleted. |
| ERR\_WS\_UPGRADE | \-173 | The WebSocket handshake is completed, the connection has been upgraded, and the URLRequest is canceled. |
| ERR\_READ\_IF\_READY\_NOT\_IMPLEMENTED | \-174 | The ReadIfReady of socket is not implemented. |
| ERR\_NO\_BUFFER\_SPACE | \-176 | No socket buffer space is available. |
| ERR\_SSL\_CLIENT\_AUTH\_NO\_COMMON\_ALGORITHMS | \-177 | There is no common signing algorithm between the private key of the local end certificate and the preferences of the server. |
| ERR\_EARLY\_DATA\_REJECTED | \-178 | TLS 1.3 early data is rejected by the server. This error will be received before any data is returned from the socket. Retry the request when early data is disabled. |
| ERR\_WRONG\_VERSION\_ON\_EARLY\_DATA | \-179 | The TLS 1.3 early data version is incorrect. |
| ERR\_TLS13\_DOWNGRADE\_DETECTED | \-180 | TLS 1.3 is enabled, but an earlier version has been negotiated. This error indicates that it supports TLS 1.3. This is part of the security check in TLS 1.3, but it may also indicate that the user is using a problematic TLS-terminating proxy. |
| ERR\_SSL\_KEY\_USAGE\_INCOMPATIBLE | \-181 | The server's certificate has a keyUsage extension that is incompatible with the negotiated TLS key exchange method. |
| ERR\_INVALID\_ECH\_CONFIG\_LIST | \-182 | The ECHConfigList obtained through DNS cannot be resolved. |
| ERR\_ECH\_NOT\_NEGOTIATED | \-183 | ECH is enabled, but the server cannot decrypt ClientHello. |
| ERR\_ECH\_FALLBACK\_CERTIFICATE\_INVALID | \-184 | ECH is enabled, the server cannot decrypt ClientHello message, and no certificate valid for the public name is provided. |
| ERR\_CERT\_COMMON\_NAME\_INVALID | \-200 | The public name of the certificate used by the server in response does not match the host name. This may mean: 1. The attacker has redirected local traffic to their server and provided a certificate with a private key. 2. The server is incorrectly configured and uses an incorrect certificate to respond. 3. The user is on the wireless network and is redirected to the login page of the network. 4. The operating system uses the DNS search suffix, and the server does not have a certificate with such abbreviated name in the address box. |
| ERR\_CERT\_DATE\_INVALID | \-201 | The certificate has expired. This may mean: 1. The attacker provides an old certificate that they have obtained the private key. 2. The server is incorrectly configured and no valid certificate is provided. 3. The clock of the device is incorrect. |
| ERR\_CERT\_AUTHORITY\_INVALID | \-202 | The CA is not trusted. This may mean: 1. The attacker replaces a real certificate with a certificate that contains its public key and is signed by its cousin. 2. The server operator has a valid certificate from a CA that the local end does not know but should trust. 3. The server provides a self-signed certificate that cannot defend against active attackers. |
| ERR\_CERT\_CONTAINS\_ERRORS | \-203 | The certificate contains errors. |
| ERR\_CERT\_NO\_REVOCATION\_MECHANISM | \-204 | There is no revocation mechanism for this certificate. |
| ERR\_CERT\_UNABLE\_TO\_CHECK\_REVOCATION | \-205 | Revocation information for this website's security certificate is not available. This may mean that: 1. The attacker compromises the private key in the certificate and prevents the local end from discovering that the certificate has been revoked. 2. The certificate is not revoked, but the revocation server is busy or unavailable. |
| ERR\_CERT\_REVOKED | \-206 | The certificate is revoked. The local end can ignore this error, but it should not do this. |
| ERR\_CERT\_INVALID | \-207 | The certificate is invalid. |
| ERR\_CERT\_WEAK\_SIGNATURE\_ALGORITHM | \-208 | The server responds with a certificate signed with a weak signing algorithm. |
| ERR\_CERT\_NON\_UNIQUE\_NAME | \-210 | The domain name specified in the certificate is not unique. |
| ERR\_CERT\_WEAK\_KEY | \-211 | The server responds with a certificate that contains a weak key (for example, a small RSA key). |
| ERR\_CERT\_NAME\_CONSTRAINT\_VIOLATION | \-212 | The certificate name constraint is violated. |
| ERR\_CERT\_VALIDITY\_TOO\_LONG | \-213 | The certificate validity period is too long. |
| ERR\_CERTIFICATE\_TRANSPARENCY\_REQUIRED | \-214 | The server does not provide Certificate Transparency information required for this connection. |
| ERR\_CERT\_SYMANTEC\_LEGACY | \-215 | The certificate is linked to the old Symantec directory that is no longer trusted. |
| ERR\_CERT\_KNOWN\_INTERCEPTION\_BLOCKED | \-217 | The certificate is used for interception by an entity other than the device owner. |
| ERR\_SSL\_OBSOLETE\_VERSION\_OR\_CIPHER | \-218 | The connection uses an outdated version of SSL/TLS or password. |
| ERR\_CERT\_END | \-219 | This error follows the previous error code. |
| ERR\_INVALID\_URL | \-300 | Invalid URL. |
| ERR\_DISALLOWED\_URL\_SCHEME | \-301 | The URL scheme is not allowed to be used. |
| ERR\_UNKNOWN\_URL\_SCHEME | \-302 | The URL scheme is unknown. |
| ERR\_INVALID\_REDIRECT | \-303 | The attempt to load a URL causes a redirection to an invalid URL. |
| ERR\_TOO\_MANY\_REDIRECTS | \-310 | There are too many redirections. |
| ERR\_UNSAFE\_REDIRECT | \-311 | The redirection is unsafe. |
| ERR\_UNSAFE\_PORT | \-312 | The port is unsafe. |
| ERR\_INVALID\_RESPONSE | \-320 | The response is invalid. |
| ERR\_INVALID\_CHUNKED\_ENCODING | \-321 | The chunked encoding is invalid. |
| ERR\_METHOD\_UNSUPPORTED | \-322 | The method is not supported. |
| ERR\_UNEXPECTED\_PROXY\_AUTH | \-323 | The proxy authentication is unexpected. |
| ERR\_EMPTY\_RESPONSE | \-324 | The response is empty. |
| ERR\_RESPONSE\_HEADERS\_TOO\_BIG | \-325 | The value of response headers is too large. |
| ERR\_PAC\_SCRIPT\_FAILED | \-327 | The pac script is incorrect. |
| ERR\_REQUEST\_RANGE\_NOT\_SATISFIABLE | \-328 | The request range cannot be met. |
| ERR\_MALFORMED\_IDENTITY | \-329 | The identity used for authentication is invalid. |
| ERR\_CONTENT\_DECODING\_FAILED | \-330 | The response content failed to be decoded. |
| ERR\_NETWORK\_IO\_SUSPENDED | \-331 | The operation failed because all network I/Os are suspended. |
| ERR\_SYN\_REPLY\_NOT\_RECEIVED | \-332 | The **FLIP** data is received when **SYN\_REPLY** is not received on the stream. |
| ERR\_ENCODING\_CONVERSION\_FAILED | \-333 | The response failed to be converted to the target encoding. |
| ERR\_UNRECOGNIZED\_FTP\_DIRECTORY\_LISTING\_FORMAT | \-334 | The format of the FTP directory list cannot be recognized. |
| ERR\_NO\_SUPPORTED\_PROXIES | \-336 | There is no supported proxy. |
| ERR\_HTTP2\_PROTOCOL\_ERROR | \-337 | The HTTP/2 protocol occurs error. |
| ERR\_INVALID\_AUTH\_CREDENTIALS | \-338 | The authentication credentials are invalid. |
| ERR\_UNSUPPORTED\_AUTH\_SCHEME | \-339 | The authentication scheme is not supported. |
| ERR\_ENCODING\_DETECTION\_FAILED | \-340 | The encoding detection failed. |
| ERR\_MISSING\_AUTH\_CREDENTIALS | \-341 | The authentication credentials are missing. |
| ERR\_UNEXPECTED\_SECURITY\_LIBRARY\_STATUS | \-342 | The security library status is unexpected. |
| ERR\_MISCONFIGURED\_AUTH\_ENVIRONMENT | \-343 | The authentication environment is incorrectly configured. |
| ERR\_UNDOCUMENTED\_SECURITY\_LIBRARY\_STATUS | \-344 | The security library status is undocumented. |
| ERR\_RESPONSE\_BODY\_TOO\_BIG\_TO\_DRAIN | \-345 | The response body is too big. |
| ERR\_RESPONSE\_HEADERS\_MULTIPLE\_CONTENT\_LENGTH | \-346 | The response has multiple Content-Length headers. |
| ERR\_INCOMPLETE\_HTTP2\_HEADERS | \-347 | The HTTP/2 headers are incomplete. |
| ERR\_PAC\_NOT\_IN\_DHCP | \-348 | The PAC is not in DHCP. |
| ERR\_RESPONSE\_HEADERS\_MULTIPLE\_CONTENT\_DISPOSITION | \-349 | The response has multiple Content-Disposition headers. |
| ERR\_RESPONSE\_HEADERS\_MULTIPLE\_LOCATION | \-350 | The response headers are in multiple locations. |
| ERR\_HTTP2\_SERVER\_REFUSED\_STREAM | \-351 | The HTTP/2 server refuses the stream. |
| ERR\_HTTP2\_PING\_FAILED | \-352 | The HTTP/2 ping failed. |
| ERR\_CONTENT\_LENGTH\_MISMATCH | \-354 | When the connection is closed, the number of bytes transmitted in the HTTP response body is less than the number of bytes advertised in the Content-Length header. |
| ERR\_INCOMPLETE\_CHUNKED\_ENCODING | \-355 | The HTTP response body is transmitted using chunked encoding, but the zero-length chunk is not sent to terminate the encoding when the connection is closed. |
| ERR\_QUIC\_PROTOCOL\_ERROR | \-356 | A QUIC protocol error occurs. |
| ERR\_RESPONSE\_HEADERS\_TRUNCATED | \-357 | The HTTP headers are truncated by the end of file (EOF). |
| ERR\_QUIC\_HANDSHAKE\_FAILED | \-358 | The QUIC encryption handshake failed. This means that the server cannot read any requests, so they may be resent. |
| ERR\_HTTP2\_INADEQUATE\_TRANSPORT\_SECURITY | \-360 | The transport security is inadequate to HTTP/2. |
| ERR\_HTTP2\_FLOW\_CONTROL\_ERROR | \-361 | The peer violates HTTP/2 flow control. |
| ERR\_HTTP2\_FRAME\_SIZE\_ERROR | \-362 | The peer sends an HTTP/2 frame of an incorrect size. |
| ERR\_HTTP2\_COMPRESSION\_ERROR | \-363 | The decoding or encoding of the compressed HTTP/2 headers failed. |
| ERR\_PROXY\_AUTH\_REQUESTED\_WITH\_NO\_CONNECTION | \-364 | The requested proxy authentication does not have a valid client socket handle. |
| ERR\_HTTP\_1\_1\_REQUIRED | \-365 | The HTTP/2 session receives an **HTTP\_1\_1\_REQUIRED** error code. |
| ERR\_PROXY\_HTTP\_1\_1\_REQUIRED | \-366 | The **HTTP\_1\_1\_REQUIRED** error code is received when the HTTP/2 session proxy is used. |
| ERR\_PAC\_SCRIPT\_TERMINATED | \-367 | The PAC script has been terminated and must be reloaded. |
| ERR\_INVALID\_HTTP\_RESPONSE | \-370 | The server should return an **HTTP/1.x** response. But it returns an **HTTP/0.9** response. |
| ERR\_CONTENT\_DECODING\_INIT\_FAILED | \-371 | The content decoding failed to be initialized. |
| ERR\_HTTP2\_RST\_STREAM\_NO\_ERROR\_RECEIVED | \-372 | An **HTTP/2 RST\_STREAM** frame with **NO\_ERROR** is received. This error should be handled internally by HTTP/2 and should not exceed the SpdyStream layer. |
| ERR\_HTTP2\_PUSHED\_STREAM\_NOT\_AVAILABLE | \-373 | The pushed stream claimed by the request is not available. |
| ERR\_HTTP2\_CLAIMED\_PUSHED\_STREAM\_RESET\_BY\_SERVER | \-374 | The claimed pushed stream is reset by the server. In this case, the request should be retried. |
| ERR\_TOO\_MANY\_RETRIES | \-375 | The number of HTTP transaction retries is too large due to invalid authentication or certificate. |
| ERR\_HTTP2\_STREAM\_CLOSED | \-376 | An HTTP/2 frame is received on the closed stream. |
| ERR\_HTTP2\_CLIENT\_REFUSED\_STREAM | \-377 | The client refuses an HTTP/2 stream. |
| ERR\_HTTP2\_PUSHED\_RESPONSE\_DOES\_NOT\_MATCH | \-378 | Based on the matched URL and request header, an HTTP/2 push stream is received by the request, but the pushed response header does not match the request. |
| ERR\_HTTP\_RESPONSE\_CODE\_FAILURE | \-379 | The server returns a **non-2xx** HTTP response code. |
| ERR\_QUIC\_UNKNOWN\_CERT\_ROOT | \-380 | The certificate displayed on the QUIC connection is not linked to a known root certificate, and the connected original server is not in the list of domain names that allow unknown root certificates. |
| ERR\_QUIC\_GOAWAY\_REQUEST\_CAN\_BE\_RETRIED | \-381 | A **GOAWAY** frame has been received, indicating that the request has not been processed and therefore can be safely retried on a different connection. |
| ERR\_TOO\_MANY\_ACCEPT\_CH\_RESTARTS | \-382 | The **ACCEPT\_CH\_RESTARTS** has been triggered too many times. |
|  | \-383 | In the same request, the IP address space of the remote endpoint is different from the previous one. Cache entries for any affected requests should be marked as invalid. |
| ERR\_CACHED\_IP\_ADDRESS\_SPACE\_BLOCKED\_BY\_LOCAL\_NETWORK\_ACCESS\_POLICY | \-384 | The cached IP address space of the remote endpoint is blocked by a local network access policy. |
| ERR\_CACHE\_MISS | \-400 | There is no requested entry in the cache. |
| ERR\_CACHE\_READ\_FAILURE | \-401 | The data cannot be read from the disk cache. |
| ERR\_CACHE\_WRITE\_FAILURE | \-402 | The data cannot be written to the disk cache. |
| ERR\_CACHE\_OPERATION\_UNSUPPORTED | \-403 | The entry does not support this operation. |
| ERR\_CACHE\_OPEN\_FAILURE | \-404 | The disk cache could not open this entry. |
| ERR\_CACHE\_CREATE\_FAILURE | \-405 | The disk cache could not create this entry. |
| ERR\_CACHE\_RACE | \-406 | Multiple transactions are competing to create disk cache entries. |
| ERR\_CACHE\_CHECKSUM\_READ\_FAILURE | \-407 | The cache could not read the checksum on the entry. |
| ERR\_CACHE\_CHECKSUM\_MISMATCH | \-408 | An entry with an invalid checksum is found in the cache. |
| ERR\_CACHE\_LOCK\_TIMEOUT | \-409 | The HTTP cache contains error code. |
| ERR\_CACHE\_AUTH\_FAILURE\_AFTER\_READ | \-410 | A challenge is received after the transaction reads some data, but the credentials are unavailable. |
| ERR\_CACHE\_ENTRY\_NOT\_SUITABLE | \-411 | The entry is not suitable for the cache. |
| ERR\_CACHE\_DOOM\_FAILURE | \-412 | The disk cache cannot delete this entry. |
| ERR\_CACHE\_OPEN\_OR\_CREATE\_FAILURE | \-413 | The disk cache could not open or create this entry. |
| ERR\_INSECURE\_RESPONSE | \-501 | The response from the server is insecure (for example, there is a certificate error). |
| ERR\_NO\_PRIVATE\_KEY\_FOR\_CERT | \-502 | The client certificate failed to be imported because the user's key database does not have a private key. |
| ERR\_ADD\_USER\_CERT\_FAILED | \-503 | The certificate failed to be added to the operating system database. |
| ERR\_INVALID\_SIGNED\_EXCHANGE | \-504 | The signed exchange is invalid. |
| ERR\_INVALID\_WEB\_BUNDLE | \-505 | The Web Bundle resources are invalid. |
| ERR\_TRUST\_TOKEN\_OPERATION\_FAILED | \-506 | The request for performing the Trust Tokens protocol operation failed. The possible causes include prerequisite failure, internal error, and bad response. |
| ERR\_TRUST\_TOKEN\_OPERATION\_SUCCESS\_WITHOUT\_SENDING\_REQUEST | \-507 | When processing an operation execution request related to the Trust Tokens protocol, the system performs the Trust Tokens operation in the request, but does not send the request to the specified destination. |
| ERR\_FTP\_FAILED | \-601 | The FTP control connection command failed. |
| ERR\_FTP\_SERVICE\_UNAVAILABLE | \-602 | The server cannot meet the request. This is a temporary error. The FTP response code is 421. |
| ERR\_FTP\_TRANSFER\_ABORTED | \-603 | The server has aborted the transfer. The FTP response code is 426. |
| ERR\_FTP\_FILE\_BUSY | \-604 | The file is in use, or some other temporary error occurs when the file is opened. The FTP response code is 450. |
| ERR\_FTP\_SYNTAX\_ERROR | \-605 | The server rejects the command from the local end due to a syntax error. The FTP response code is 500 or 501. |
| ERR\_FTP\_COMMAND\_UNSUPPORTED | \-606 | The server does not support the command sent by the local end. The FTP response code is 502 or 504. |
| ERR\_FTP\_BAD\_COMMAND\_SEQUENCE | \-607 | The server rejects the commands from the local end because the local end does not send the commands in the correct sequence. The FTP response code is 503. |
| ERR\_PKCS12\_IMPORT\_BAD\_PASSWORD | \-701 | The **PKCS #12** file cannot be imported because the password is incorrect. |
| ERR\_PKCS12\_IMPORT\_FAILED | \-702 | The **PKCS #12** file cannot be imported due to other errors. |
| ERR\_IMPORT\_CA\_CERT\_NOT\_CA | \-703 | The CA certificate cannot be imported because it is not a real CA certificate. |
| ERR\_IMPORT\_CERT\_ALREADY\_EXISTS | \-704 | The certificate cannot be imported because it already exists in the database. |
| ERR\_IMPORT\_CA\_CERT\_FAILED | \-705 | The CA failed to be imported due to other errors. |
| ERR\_IMPORT\_SERVER\_CERT\_FAILED | \-706 | The server certificate failed to be imported due to some internal errors. |
| ERR\_PKCS12\_IMPORT\_INVALID\_MAC | \-707 | The **PKCS #12** file failed to be imported because the message authentication code (MAC) is invalid. |
| ERR\_PKCS12\_IMPORT\_INVALID\_FILE | \-708 | The **PKCS #12** file failed to be imported because the file is invalid or corrupted. |
| ERR\_PKCS12\_IMPORT\_UNSUPPORTED | \-709 | The **PKCS #12** file failed to be imported because the feature is not supported. |
| ERR\_KEY\_GENERATION\_FAILED | \-710 | The key generation failed. |
| ERR\_PRIVATE\_KEY\_EXPORT\_FAILED | \-712 | The private key failed to be exported. |
| ERR\_SELF\_SIGNED\_CERT\_GENERATION\_FAILED | \-713 | The self-signed certificate generation failed. |
| ERR\_CERT\_DATABASE\_CHANGED | \-714 | The certificate database is changed. |
| ERR\_CERT\_VERIFIER\_CHANGED | \-716 | The certificate verifier configuration is changed. |
| ERR\_DNS\_MALFORMED\_RESPONSE | \-800 | The DNS resolver receives a response that the format is incorrect. |
| ERR\_DNS\_SERVER\_REQUIRES\_TCP | \-801 | The DNS server requires TCP. |
| ERR\_DNS\_SERVER\_FAILED | \-802 | The DNS server failed. This error code is returned for all the following cases: 1-Incorrect format: The name server cannot interpret the query with an incorrect format. 2-Server failure: The name server cannot process the query due to its own problems. 3-Not Implemented: The name server does not support the query type of the request. 4-Rejection: The name server refuses to perform the specified operation for policy reasons. |
| ERR\_DNS\_TIMED\_OUT | \-803 | The DNS transaction times out. |
| ERR\_DNS\_CACHE\_MISS | \-804 | The entry is not found in the cache or other local sources. |
| ERR\_DNS\_SEARCH\_EMPTY | \-805 | The suffix search list rule prevents the resolution of a given host name. |
| ERR\_DNS\_SORT\_ERROR | \-806 | Addresses are not sorted according to RFC 3484. |
| ERR\_DNS\_SECURE\_RESOLVER\_HOSTNAME\_RESOLUTION\_FAILED | \-808 | The host name of the DNS-over-HTTPS server cannot be resolved. |
| ERR\_DNS\_NAME\_HTTPS\_ONLY | \-809 | DNS has identified that the request is prohibited due to insecure connections (HTTP/WS). The application should handle this error like HTTP redirection, redirecting the connection to secure HTTPS or WSS. |
| ERR\_DNS\_REQUEST\_CANCELED | \-810 | All DNS requests related to this task are canceled. |
| ERR\_DNS\_NO\_MATCHING\_SUPPORTED\_ALPN | \-811 | The host name resolution of the HTTPS record is not resolved using the ALPN value of the supported protocol. |
