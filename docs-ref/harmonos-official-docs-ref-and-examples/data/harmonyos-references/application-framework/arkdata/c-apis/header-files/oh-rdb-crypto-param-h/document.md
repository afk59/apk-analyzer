# oh\_rdb\_crypto\_param.h

#### Overview

Defines functions and enums related to encryption parameters of the RDB store.

**File to include**: <database/rdb/oh\_rdb\_crypto\_param.h>

**Library**: libnative\_rdb\_ndk.z.so

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Since**: 20

**Related module**: [RDB](../../modules/rdb/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) | OH\_Rdb\_CryptoParam | Defines the encryption parameters used to open an encrypted database. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Rdb\_EncryptionAlgo](#rdb_encryptionalgo) | Rdb\_EncryptionAlgo | Enumerates database encryption algorithms. |
| [Rdb\_HmacAlgo](#rdb_hmacalgo) | Rdb\_HmacAlgo | Enumerates HMAC algorithms. |
| [Rdb\_KdfAlgo](#rdb_kdfalgo) | Rdb\_KdfAlgo | Enumerates KDF algorithms. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_CryptoParam \*OH\_Rdb\_CreateCryptoParam(void)](#oh_rdb_createcryptoparam) | Creates an [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) instance. |
| [int OH\_Rdb\_DestroyCryptoParam(OH\_Rdb\_CryptoParam \*param)](#oh_rdb_destroycryptoparam) | Destroys an [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) instance. |
| [int OH\_Crypto\_SetEncryptionKey(OH\_Rdb\_CryptoParam \*param, const uint8\_t \*key, int32\_t length)](#oh_crypto_setencryptionkey) | Sets the key data of an [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) instance. |
| [int OH\_Crypto\_SetIteration(OH\_Rdb\_CryptoParam \*param, int64\_t iteration)](#oh_crypto_setiteration) | Sets the number of iterations of the KDF algorithm used when opening an encrypted database. |
| [int OH\_Crypto\_SetEncryptionAlgo(OH\_Rdb\_CryptoParam \*param, int32\_t algo)](#oh_crypto_setencryptionalgo) | Sets the encryption algorithm used when opening an encrypted database. |
| [int OH\_Crypto\_SetHmacAlgo(OH\_Rdb\_CryptoParam \*param, int32\_t algo)](#oh_crypto_sethmacalgo) | Sets the HMAC algorithm used when opening an encrypted database. |
| [int OH\_Crypto\_SetKdfAlgo(OH\_Rdb\_CryptoParam \*param, int32\_t algo)](#oh_crypto_setkdfalgo) | Sets the KDF algorithm used when opening an encrypted database. |
| [int OH\_Crypto\_SetCryptoPageSize(OH\_Rdb\_CryptoParam \*param, int64\_t size)](#oh_crypto_setcryptopagesize) | Sets the page size used when opening an encrypted database. |

#### Enum Description

#### \[h2\]Rdb\_EncryptionAlgo

enum Rdb\_EncryptionAlgo

**Description**

Enumerates database encryption algorithms.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| RDB\_AES\_256\_GCM = 0 | RDB\_AES\_256\_GCM. |
| RDB\_AES\_256\_CBC | RDB\_AES\_256\_CBC. |
| RDB\_PLAIN\_TEXT | 
No encryption is required.

**Since**: 22

 |

#### \[h2\]Rdb\_HmacAlgo

enum Rdb\_HmacAlgo

**Description**

Enumerates HMAC algorithms.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| RDB\_HMAC\_SHA1 = 0 | RDB\_HMAC\_SHA1. |
| RDB\_HMAC\_SHA256 | RDB\_HMAC\_SHA256. |
| RDB\_HMAC\_SHA512 | RDB\_HMAC\_SHA512. |

#### \[h2\]Rdb\_KdfAlgo

enum Rdb\_KdfAlgo

**Description**

Enumerates KDF algorithms.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| RDB\_KDF\_SHA1 = 0 | RDB\_KDF\_SHA1. |
| RDB\_KDF\_SHA256 | RDB\_KDF\_SHA256. |
| RDB\_KDF\_SHA512 | RDB\_KDF\_SHA512. |

#### Function Description

#### \[h2\]OH\_Rdb\_CreateCryptoParam()

OH\_Rdb\_CryptoParam \*OH\_Rdb\_CreateCryptoParam(void)

**Description**

Creates an [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) instance.

**Since**: 20

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) | Returns a pointer to the [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) instance if the operation is successful; returns **nullptr** otherwise. Use [OH\_Rdb\_DestroyCryptoParam](#oh_rdb_destroycryptoparam) to release the memory in time. |

#### \[h2\]OH\_Rdb\_DestroyCryptoParam()

int OH\_Rdb\_DestroyCryptoParam(OH\_Rdb\_CryptoParam \*param)

**Description**

Destroys an [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) \*param | Pointer to the [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an execution result.

**RDB\_OK** indicates that the execution is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Crypto\_SetEncryptionKey()

int OH\_Crypto\_SetEncryptionKey(OH\_Rdb\_CryptoParam \*param, const uint8\_t \*key, int32\_t length)

**Description**

Sets the key data of an [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) \*param | Pointer to the [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) instance. |
| const uint8\_t \*key | Pointer to the array data. |
| int32\_t length | Size of the key array. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an execution result.

**RDB\_OK** indicates that the execution is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Crypto\_SetIteration()

int OH\_Crypto\_SetIteration(OH\_Rdb\_CryptoParam \*param, int64\_t iteration)

**Description**

Sets the number of iterations of the KDF algorithm used when opening an encrypted database.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) \*param | Pointer to the [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) instance. |
| int64\_t iteration | Number of iterations. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an execution result.

**RDB\_OK** indicates that the execution is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Crypto\_SetEncryptionAlgo()

int OH\_Crypto\_SetEncryptionAlgo(OH\_Rdb\_CryptoParam \*param, int32\_t algo)

**Description**

Sets the encryption algorithm used when opening an encrypted database.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) \*param | Pointer to the [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) instance. |
| int32\_t algo | Encryption algorithm. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an execution result.

**RDB\_OK** indicates that the execution is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Crypto\_SetHmacAlgo()

int OH\_Crypto\_SetHmacAlgo(OH\_Rdb\_CryptoParam \*param, int32\_t algo)

**Description**

Sets the HMAC algorithm used when opening an encrypted database.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) \*param | Pointer to the [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) instance. |
| int32\_t algo | HMAC algorithm. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an execution result.

**RDB\_OK** indicates that the execution is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Crypto\_SetKdfAlgo()

int OH\_Crypto\_SetKdfAlgo(OH\_Rdb\_CryptoParam \*param, int32\_t algo)

**Description**

Sets the KDF algorithm used when opening an encrypted database.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) \*param | Pointer to the [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) instance. |
| int32\_t algo | KDF algorithm. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an execution result.

**RDB\_OK** indicates that the execution is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Crypto\_SetCryptoPageSize()

int OH\_Crypto\_SetCryptoPageSize(OH\_Rdb\_CryptoParam \*param, int64\_t size)

**Description**

Sets the page size used when opening an encrypted database.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) \*param | Pointer to the [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) instance. |
| int64\_t size | Page size, in bytes. The value must be a power of 2 and ranges from 1024 to 65536. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an execution result.

**RDB\_OK** indicates that the execution is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |
