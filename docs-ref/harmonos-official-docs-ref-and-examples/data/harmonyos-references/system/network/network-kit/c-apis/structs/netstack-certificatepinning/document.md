# NetStack\_CertificatePinning

typedef struct NetStack\_CertificatePinning {...} NetStack\_CertificatePinning

#### Overview

Defines certificate pinning information.

**Since**: 12

**Related module**: [netstack](../../modules/netstack/document.md)

**Header file**: [net\_ssl\_c\_type.h](../../header-files/net-ssl-c-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [NetStack\_CertificatePinningKind](../../header-files/net-ssl-c-type-h/document.md#netstack_certificatepinningkind) kind | Certificate lock type. |
| [NetStack\_HashAlgorithm](../../header-files/net-ssl-c-type-h/document.md#netstack_hashalgorithm) hashAlgorithm | Hash algorithm. |
| char \*publicKeyHash | Hash value. |
