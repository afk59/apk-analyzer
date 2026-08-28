# OH\_CM\_Credential

typedef struct {...} OH\_CM\_Credential

#### Overview

Defines a struct for the certificate credential details.

**Since**: 22

**Related module**: [CertManagerType](../../modules/certmanagertype/document.md)

**Header file**: [cm\_native\_type.h](../../header-files/cm-native-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t isExist | Whether a certificate data exists. |
| char type\[OH\_CM\_MAX\_LEN\_TYPE\_NAME\] | Type of a credential. The value contains up to 8 bytes, including the terminator **'\\0'**. |
| char alias\[OH\_CM\_MAX\_LEN\_CERT\_ALIAS\] | Alias of a credential. The value contains up to 128 bytes, including the terminator **'\\0'**. |
| char keyUri\[OH\_CM\_MAX\_LEN\_URI\] | URI of a credential. The value contains up to 256 bytes, including the terminator **'\\0'**. |
| uint32\_t certNum | Number of certificates contained in the credential. |
| uint32\_t keyNum | Number of keys contained in the credential. |
| [OH\_CM\_Blob](../oh-cm-blob/document.md) credData | Binary data of a credential. The value contains up to 20480 bytes. |
| [OH\_CM\_CertificatePurpose](../../header-files/cm-native-type-h/document.md#oh_cm_certificatepurpose) certPurpose | Purpose of a certificate credential. |
