# Overview

API protocol: HTTPS

Response data format: JSON

Data charset: UTF-8

-   The APIs support the POST method.
-   Encoding format: UTF-8
-   POST content type: application/json;charset=UTF-8, application/x-www-form-urlencoded
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/RexR1KaRQtSNX1ZBjIoUEQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062508Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45CC204977A68532D5A7244DC81D3B53C9C8069DA271365D2F1A1B0937D1E796)
    
    If the **content-type** field is not set to **application/json**, the APIs may fail to be called in some cases.
    
-   Authentication information is specified based on the request header. The token is in JWT format.
    
    Authorization: Bearer <Token in JWT format>
    
-   The language information is specified by **Accept-Language** in the request header. The value is a standard locale.

#### Site Information

| 
Site

 | 

Address

 |
| :-- | :-- |
| 

China

 | 

https://iap.cloud.huawei.com

 |

#### Cipher Suites

| 
TLS Version

 | 

Cipher Suite (IANA Name)

 |
| :-- | :-- |
| 

TLS 1.3

 | 

TLS\_AES\_128\_GCM\_SHA256

TLS\_AES\_256\_GCM\_SHA384

TLS\_CHACHA20\_POLY1305\_SHA256

 |
| 

TLS 1.2

 | 

TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384

TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256

TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384

TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256

 |

#### Certificate Verification

If the certificate on the server side is not verified or is tampered with, the client may connect to an unexpected server. This will cause security issues like man-in-the-middle attacks and data leakage. To ensure connection security, it is necessary for your server to verify the certificate provided by the IAP server, when your server accesses the IAP server. The verification consists of two parts: first, check whether the certificate is from a trusted source; second, check whether the IAP server provides the correct certificate.
