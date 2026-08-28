# native\_huks\_external\_crypto\_type.h

#### Overview

Defines the structs and enums for external key management extensions.

**File to include**: <huks/native\_huks\_external\_crypto\_type.h>

**Library**: libhuks\_external\_crypto.z.so

**System capability**: SystemCapability.Security.Huks.CryptoExtension

**Since**: 22

**Related module**: [HuksExternalCryptoTypeApi](../../modules/huksexternalcryptotypeapi/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Huks\_ExternalCryptoParam](../../structs/oh-huks-externalcryptoparam/document.md) | OH\_Huks\_ExternalCryptoParam | Defines a single parameter in a parameter set. |
| [OH\_Huks\_ExternalCryptoParamSet](../../structs/oh-huks-externalcryptoparamset/document.md) | OH\_Huks\_ExternalCryptoParamSet | Defines an external cryptographic parameter set. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Huks\_ExternalCryptoTag](#oh_huks_externalcryptotag) | OH\_Huks\_ExternalCryptoTag | Enumerates the tag values used in a parameter set. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| OH\_HUKS\_EXTERNAL\_CRYPTO\_MAX\_PROVIDER\_NAME\_LEN 100 | 
Defines the maximum length of the provider name.

**Since**: 22

 |
| OH\_HUKS\_EXTERNAL\_CRYPTO\_MAX\_RESOURCE\_ID\_LEN 512 | 

Defines the maximum length of the resource ID.

**Since**: 22

 |

#### Enum Description

#### \[h2\]OH\_Huks\_ExternalCryptoTag

enum OH\_Huks\_ExternalCryptoTag

**Description**

Enumerates the tag values used in a parameter set.

**Since**: 22

| Value | Description |
| :-- | :-- |
| OH\_HUKS\_EXT\_CRYPTO\_TAG\_UKEY\_PIN = OH\_HUKS\_TAG\_TYPE\_BYTES | 200001 | PIN code. |
| OH\_HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_NAME = OH\_HUKS\_TAG\_TYPE\_BYTES | 200002 | Ability name. |
| OH\_HUKS\_EXT\_CRYPTO\_TAG\_EXTRA\_DATA = OH\_HUKS\_TAG\_TYPE\_BYTES | 200003 | Extra data. |
| OH\_HUKS\_EXT\_CRYPTO\_TAG\_UID = OH\_HUKS\_TAG\_TYPE\_INT | 200004 | UID of the caller. |
| OH\_HUKS\_EXT\_CRYPTO\_TAG\_PURPOSE = OH\_HUKS\_TAG\_TYPE\_INT | 200005 | Purpose of the certificate chain. |
| OH\_HUKS\_EXT\_CRYPTO\_TAG\_TIMEOUT = OH\_HUKS\_TAG\_TYPE\_UINT | 200006 | Timeout interval for obtaining properties, in seconds. |

#### \[h2\]OH\_Huks\_ExternalPinAuthState

enum OH\_Huks\_ExternalPinAuthState

**Description**

Enumerates the Ukey PIN authentication states.

**Since**: 22

| Value | Description |
| :-- | :-- |
| OH\_HUKS\_EXT\_CRYPTO\_PIN\_NO\_AUTH = 0 | PIN code not authenticated. |
| OH\_HUKS\_EXT\_CRYPTO\_PIN\_AUTH\_SUCCEEDED = 1 | PIN code authentication succeeded. |
| OH\_HUKS\_EXT\_CRYPTO\_PIN\_LOCKED = 2 | PIN code locked. |
