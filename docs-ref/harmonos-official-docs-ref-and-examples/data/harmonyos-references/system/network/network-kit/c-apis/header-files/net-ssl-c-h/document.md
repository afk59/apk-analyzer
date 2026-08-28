# net\_ssl\_c.h

#### Overview

Defines data structures for the C APIs of the SSL/TLS certificate chain verification module.

**File to include**: <network/netstack/net\_ssl/net\_ssl\_c.h>

**Library**: libnet\_ssl.so

**System capability**: SystemCapability.Communication.NetStack

**Since**: 11

**Related module**: [netstack](../../modules/netstack/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [uint32\_t OH\_NetStack\_CertVerification(const struct NetStack\_CertBlob \*cert, const struct NetStack\_CertBlob \*caCert)](#oh_netstack_certverification) | Verifies the certificate chain. |
| [int32\_t OH\_NetStack\_GetPinSetForHostName(const char \*hostname, NetStack\_CertificatePinning \*pin)](#oh_netstack_getpinsetforhostname) | Obtains the certificate lock information. |
| [int32\_t OH\_NetStack\_GetCertificatesForHostName(const char \*hostname, NetStack\_Certificates \*certs)](#oh_netstack_getcertificatesforhostname) | Obtains certificate information. |
| [void OH\_Netstack\_DestroyCertificatesContent(NetStack\_Certificates \*certs)](#oh_netstack_destroycertificatescontent) | Releases the certificate content. |
| [int32\_t OH\_Netstack\_IsCleartextPermitted(bool \*isCleartextPermitted)](#oh_netstack_iscleartextpermitted) | Boolean value indicating whether plaintext HTTP is allowed. |
| [int32\_t OH\_Netstack\_IsCleartextPermittedByHostName(const char \*hostname, bool \*isCleartextPermitted)](#oh_netstack_iscleartextpermittedbyhostname) | Boolean value indicating whether host name–based plaintext HTTP is allowed. |
| [int32\_t OH\_Netstack\_IsCleartextCfgByComponent(const char \*component, bool \*componentCfg)](#oh_netstack_iscleartextcfgbycomponent) | Checks whether plaintext HTTP interception is enabled. |

#### Function Description

#### \[h2\]OH\_NetStack\_CertVerification()

uint32\_t OH\_NetStack\_CertVerification(const struct NetStack\_CertBlob \*cert, const struct NetStack\_CertBlob \*caCert)

**Description**

Provides certificate chain verification APIs for external systems.

**System capability**: SystemCapability.Communication.NetStack

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct NetStack\_CertBlob](../../structs/netstack-certblob/document.md) \*cert | Certificate to be verified. |
| [const struct NetStack\_CertBlob](../../structs/netstack-certblob/document.md) \*caCert | Certificate specified by the user. If this parameter is left blank, the preset certificate is used for verification. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | 
**0**: Success.

**2305001**: Unknown error.

**2305002**: Failed to obtain the issuer certificate.

**2305003**: Failed to obtain the certificate revocation list (CRL).

**2305004**: Failed to decrypt the certificate signature.

**2305005**: Failed to decrypt the CRL signature.

**2305006**: Failed to decode the issuer public key.

**2305007**: Failed to sign the certificate.

**2305008**: Failed to sign the CRL.

**2305009**: Certificate not activated.

**2305010**: Certificate expired.

**2305011**: CRL not activated.

**2305012**: CRL expired.

**2305023**: Certificate revoked.

**2305024**: Invalid certificate authority (CA).

**2305027**: Untrusted certificate.

 |

#### \[h2\]OH\_NetStack\_GetPinSetForHostName()

int32\_t OH\_NetStack\_GetPinSetForHostName(const char \*hostname, NetStack\_CertificatePinning \*pin)

**Description**

Obtains the certificate lock information.

**System capability**: SystemCapability.Communication.NetStack

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*hostname | Host name. |
| [NetStack\_CertificatePinning](../../structs/netstack-certificatepinning/document.md) \*pin | Defines the certificate lock information structure. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success.

**401**: Parameter error.

**2305999**: Memory error.

 |

#### \[h2\]OH\_NetStack\_GetCertificatesForHostName()

int32\_t OH\_NetStack\_GetCertificatesForHostName(const char \*hostname, NetStack\_Certificates \*certs)

**Description**

Obtains the certificate information.

**System capability**: SystemCapability.Communication.NetStack

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*hostname | Host name. |
| [NetStack\_Certificates](../../structs/netstack-certificates/document.md) \*certs | Defines the certificate information structure. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success.

**401**: Parameter error.

**2305999**: Memory error.

 |

#### \[h2\]OH\_Netstack\_DestroyCertificatesContent()

void OH\_Netstack\_DestroyCertificatesContent(NetStack\_Certificates \*certs)

**Description**

Releases the certificate content.

**System capability**: SystemCapability.Communication.NetStack

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [NetStack\_Certificates](../../structs/netstack-certificates/document.md) \*certs | Represents the certificate information. |

#### \[h2\]OH\_Netstack\_IsCleartextPermitted()

int32\_t OH\_Netstack\_IsCleartextPermitted(bool \*isCleartextPermitted)

**Description**

Boolean value indicating whether plaintext HTTP is allowed.

**Required permission**: ohos.permission.INTERNET

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| bool \*isCleartextPermitted | Boolean value indicating whether plaintext HTTP is allowed. The value **true** means that plaintext HTTP is allowed, and the value **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success.

**201**: Permission denied.

**401**: Parameter error.

 |

#### \[h2\]OH\_Netstack\_IsCleartextPermittedByHostName()

int32\_t OH\_Netstack\_IsCleartextPermittedByHostName(const char \*hostname, bool \*isCleartextPermitted)

**Description**

Boolean value indicating whether host name–based plaintext HTTP is allowed.

**Required permission**: ohos.permission.INTERNET

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*hostname | Host name. |
| bool \*isCleartextPermitted | Boolean value indicating whether host name–based plaintext HTTP is allowed. The value **true** means that host name–based plaintext HTTP is allowed, and the value **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success.

**201**: Permission denied.

**401**: Parameter error.

 |

#### \[h2\]OH\_Netstack\_IsCleartextCfgByComponent

int32\_t OH\_Netstack\_IsCleartextCfgByComponent(const char \*component, bool \*componentCfg);

**Description**

Checks whether plaintext HTTP interception is enabled.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*component | Component name. The following components are supported: Network Kit and ArkWeb. |
| bool \*componentCfg | Output parameter, which indicates whether plaintext HTTP interception is enabled. The value **true** indicates that plaintext HTTP interception is enabled, and the value **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
**0**: Success.

**2100001**: Invalid parameter value.

 |
