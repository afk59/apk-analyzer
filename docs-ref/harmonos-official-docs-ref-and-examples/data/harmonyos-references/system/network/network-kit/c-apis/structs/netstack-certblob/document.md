# NetStack\_CertBlob

struct NetStack\_CertBlob {...}

#### Overview

Defines the certificate data structure.

**Since**: 11

**Related module**: [netstack](../../modules/netstack/document.md)

**Header file**: [net\_ssl\_c\_type.h](../../header-files/net-ssl-c-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| enum [NetStack\_CertType](../../header-files/net-ssl-c-type-h/document.md#netstack_certtype) type | Certificate type. |
| uint32\_t size | Certificate content length. |
| uint8\_t \*data | Certificate data. |
