# crypto\_common.h

#### **Overview**

Defines common APIs for cryptographic operations.

**Header file**: <CryptoArchitectureKit/crypto\_common.h>

**Library**: libohcrypto.so

**System capability**: SystemCapability.Security.CryptoFramework

**Since**: 12

**Related module**: [CryptoCommonApi](../../modules/cryptocommonapi/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) | Crypto\_DataBlob | Defines the data used for encryption and decryption. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Crypto\_ErrCode](#oh_crypto_errcode) | OH\_Crypto\_ErrCode | Enumerates the encryption and decryption error codes. |
| [Crypto\_CipherMode](#crypto_ciphermode) | Crypto\_CipherMode | Enumerates the cryptographic operation types. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [void OH\_Crypto\_FreeDataBlob(Crypto\_DataBlob \*dataBlob)](#oh_crypto_freedatablob) | Releases a **dataBlob** instance. |

#### Enum Description

#### \[h2\]OH\_Crypto\_ErrCode

enum OH\_Crypto\_ErrCode

**Description**

Enumerates the encryption and decryption error codes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| CRYPTO\_SUCCESS = 0 | The operation is successful. |
| CRYPTO\_INVALID\_PARAMS = 401 | The input parameter is invalid. |
| CRYPTO\_NOT\_SUPPORTED = 801 | The function or algorithm is not supported. |
| CRYPTO\_MEMORY\_ERROR = 17620001 | Memory error. |
| CRYPTO\_PARAMETER\_CHECK\_FAILED = 17620003 | 
Parameter check failed.

**Since**: 20

 |
| CRYPTO\_OPERTION\_ERROR = 17630001 | The encryption or decryption operation fails. |

#### \[h2\]Crypto\_CipherMode

enum Crypto\_CipherMode

**Description**

Enumerates the cryptographic operation types.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| CRYPTO\_ENCRYPT\_MODE = 0 | Encryption. |
| CRYPTO\_DECRYPT\_MODE = 1 | Decryption. |

#### Function Description

#### \[h2\]OH\_Crypto\_FreeDataBlob()

void OH\_Crypto\_FreeDataBlob(Crypto\_DataBlob \*dataBlob)

**Description**

Releases a **dataBlob** instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*dataBlob | Pointer to the **dataBlob** instance to release. |
