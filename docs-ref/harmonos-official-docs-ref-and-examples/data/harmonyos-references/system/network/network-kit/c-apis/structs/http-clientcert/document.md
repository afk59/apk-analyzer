# Http\_ClientCert

typedef struct Http\_ClientCert {...} Http\_ClientCert

#### Overview

Defines the client certificate sent to a remote server, which will be used by the server to verify the identity of the client.

**Since**: 20

**Related module**: [netstack](../../modules/netstack/document.md)

**Header file**: [net\_http\_type.h](../../header-files/net-http-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char \*certPath | Path of the certificate file. |
| [Http\_CertType](../../header-files/net-http-type-h/document.md#http_certtype) type | Certificate type. The default value is **PEM**. For details, see [Http\_CertType](../../header-files/net-http-type-h/document.md#http_certtype). |
| char \*keyPath | Path of the certificate key file. |
| char \*keyPassword | Password of the certificate key file. |
