# cm\_native\_type.h

#### Overview

Provides the enums, structs, macros, and error codes used by **CertManager** APIs.

**Header file**: <device\_certificate/certmanager/cm\_native\_type.h>

**Library**: libohcert\_manager.so

**System capability**: SystemCapability.Security.CertificateManager

**Since**: 22

**Related module**: [CertManagerType](../../modules/certmanagertype/document.md)

#### Summary

## Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_CM\_Blob](../../structs/oh-cm-blob/document.md) | OH\_CM\_Blob | Defines a struct for a binary large object (BLOB). |
| [OH\_CM\_Credential](../../structs/oh-cm-credential/document.md) | OH\_CM\_Credential | Defines a struct for the certificate credential details. |
| [OH\_CM\_CredentialDetailList](../../structs/oh-cm-credentialdetaillist/document.md) | OH\_CM\_CredentialDetailList | Defines a struct for the certificate credential detail list. |
| [OH\_CM\_UkeyInfo](../../structs/oh-cm-ukeyinfo/document.md) | OH\_CM\_UkeyInfo | Defines a struct for the USB certificate credential information. |

## Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_CM\_ErrorCode](#oh_cm_errorcode) | OH\_CM\_ErrorCode | Enumerates error codes. |
| [OH\_CM\_CertificatePurpose](#oh_cm_certificatepurpose) | OH\_CM\_CertificatePurpose | Enumerates the certificate credential purposes. |

## Macros

| Name | Description |
| :-- | :-- |
| OH\_CM\_MAX\_LEN\_CERTIFICATE\_CHAIN 24588 | 
Maximum length of a certificate chain.

**Since**: 22

 |
| OH\_CM\_MAX\_LEN\_URI 256 | 

Maximum length of a URI.

**Since**: 22

 |
| OH\_CM\_MAX\_LEN\_CERT\_ALIAS 129 | 

Maximum length of a certificate alias.

**Since**: 22

 |
| OH\_CM\_MAX\_LEN\_TYPE\_NAME 1025 | 

Maximum length of a certificate type.

**Since**: 22

 |

#### Enum Description

## OH\_CM\_ErrorCode

enum OH\_CM\_ErrorCode

**Description**

Enumerates error codes.

**Since**: 22

| Enum Item | Description |
| :-- | :-- |
| OH\_CM\_SUCCESS = 0 | Operation succeeded. |
| OH\_CM\_HAS\_NO\_PERMISSION = 201 | Permission verification failed. |
| OH\_CM\_CAPABILITY\_NOT\_SUPPORTED = 801 | Not supported by the device. |
| OH\_CM\_INNER\_FAILURE = 17500001 | Internal error. Possible causes: 1. IPC failure. 2. Memory operation error. 3. File operation error. |
| OH\_CM\_NOT\_FOUND = 17500002 | The certificate does not exist. |
| OH\_CM\_INVALID\_CERT\_FORMAT = 17500003 | The keystore format is invalid or the keystore password is incorrect. |
| OH\_CM\_MAX\_CERT\_COUNT\_REACHED = 17500004 | The number of certificates or credentials reaches the upper limit. |
| OH\_CM\_NO\_AUTHORIZATION = 17500005 | The application is not authorized. |
| OH\_CM\_DEVICE\_ENTER\_ADVSECMODE = 17500007 | The device enters the advanced security mode. |
| OH\_CM\_STORE\_PATH\_NOT\_SUPPORTED = 17500009 | The device does not support the specified certificate storage path. |
| OH\_CM\_ACCESS\_UKEY\_SERVICE\_FAILED = 17500010 | Failed to access the USB certificate credential. |
| OH\_CM\_PARAMETER\_VALIDATION\_FAILED = 17500011 | Parameter verification fails. For example, the parameter format or range is invalid. |

## OH\_CM\_CertificatePurpose

enum OH\_CM\_CertificatePurpose

**Description**

Enumerates the certificate credential purposes.

**Since**: 22

| Enum Item | Description |
| :-- | :-- |
| OH\_CM\_CERT\_PURPOSE\_DEFAULT = 0 | Default purpose, which is used for credential signing. |
| OH\_CM\_CERT\_PURPOSE\_ALL = 1 | All purposes, which are used to query credential functionalities. |
| OH\_CM\_CERT\_PURPOSE\_SIGN = 2 | Signing purpose. |
| OH\_CM\_CERT\_PURPOSE\_ENCRYPT = 3 | Encryption purpose. |
