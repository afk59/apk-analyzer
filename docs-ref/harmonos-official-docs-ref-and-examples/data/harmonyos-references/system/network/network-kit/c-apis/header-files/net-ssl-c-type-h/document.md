# net\_ssl\_c\_type.h

#### Overview

Defines data structures for the C APIs of the SSL/TLS certificate chain verification module.

**File to include**: <network/netstack/net\_ssl/net\_ssl\_c\_type.h>

**Library**: libnet\_ssl.so

**System capability**: SystemCapability.Communication.NetStack

**Since**: 11

**Related module**: [netstack](../../modules/netstack/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [NetStack\_CertBlob](../../structs/netstack-certblob/document.md) | \- | Certificate data structure. |
| [NetStack\_CertificatePinning](../../structs/netstack-certificatepinning/document.md) | NetStack\_CertificatePinning | Defines certificate pinning information. |
| [NetStack\_Certificates](../../structs/netstack-certificates/document.md) | NetStack\_Certificates | Define certificate information. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [NetStack\_CertType](#netstack_certtype) | \- | Certificate type enums. |
| [NetStack\_CertificatePinningKind](#netstack_certificatepinningkind) | NetStack\_CertificatePinningKind | Certificate pinning type enums. |
| [NetStack\_HashAlgorithm](#netstack_hashalgorithm) | NetStack\_HashAlgorithm | Hash algorithm enums. |

#### Enum Description

#### \[h2\]NetStack\_CertType

enum NetStack\_CertType

**Description**

Certificate type enums.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| NETSTACK\_CERT\_TYPE\_PEM = 0 | PEM certificate. |
| NETSTACK\_CERT\_TYPE\_DER = 1 | DER certificate. |
| NETSTACK\_CERT\_TYPE\_INVALID | Invalid certificate. |

#### \[h2\]NetStack\_CertificatePinningKind

enum NetStack\_CertificatePinningKind

**Description**

Certificate pinning type enums.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| PUBLIC\_KEY | Public key lock type. |

#### \[h2\]NetStack\_HashAlgorithm

enum NetStack\_HashAlgorithm

**Description**

Hash algorithm enums.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| SHA\_256 | Sha256 |
