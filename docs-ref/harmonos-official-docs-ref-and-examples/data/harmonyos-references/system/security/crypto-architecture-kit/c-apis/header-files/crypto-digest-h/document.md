# crypto\_digest.h

#### Overview

Defines APIs for MD algorithms.

**Header file**: <CryptoArchitectureKit/crypto\_digest.h>

**Library**: libohcrypto.so

**System capability**: SystemCapability.Security.CryptoFramework

**Since**: 12

**Related module**: [CryptoDigestApi](../../modules/cryptodigestapi/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_CryptoDigest](../../structs/oh-cryptodigest/document.md) | OH\_CryptoDigest | Defines an MD. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode OH\_CryptoDigest\_Create(const char \*algoName, OH\_CryptoDigest \*\*ctx)](#oh_cryptodigest_create) | 
Creates an MD instance based on the given algorithm name.

Note: The created resource must be destroyed by calling [OH\_DigestCrypto\_Destroy](#oh_digestcrypto_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoDigest\_Update(OH\_CryptoDigest \*ctx, Crypto\_DataBlob \*in)](#oh_cryptodigest_update) | Updates MD data. |
| [OH\_Crypto\_ErrCode OH\_CryptoDigest\_Final(OH\_CryptoDigest \*ctx, Crypto\_DataBlob \*out)](#oh_cryptodigest_final) | 

Implements MD calculation.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [uint32\_t OH\_CryptoDigest\_GetLength(OH\_CryptoDigest \*ctx)](#oh_cryptodigest_getlength) | Obtains the length of an MD. |
| [const char \*OH\_CryptoDigest\_GetAlgoName(OH\_CryptoDigest \*ctx)](#oh_cryptodigest_getalgoname) | Obtains the name of an MD algorithm. |
| [void OH\_DigestCrypto\_Destroy(OH\_CryptoDigest \*ctx)](#oh_digestcrypto_destroy) | Destroys an MD instance. |

#### Function Description

#### \[h2\]OH\_CryptoDigest\_Create()

OH\_Crypto\_ErrCode OH\_CryptoDigest\_Create(const char \*algoName, OH\_CryptoDigest \*\*ctx)

**Description**

Creates an MD instance based on the given algorithm name.

Note: The created resource must be destroyed by calling [OH\_DigestCrypto\_Destroy](#oh_digestcrypto_destroy).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*algoName | 
Pointer to the algorithm used to generate the MD instance.

For example, **SHA256**.

 |
| [OH\_CryptoDigest](../../structs/oh-cryptodigest/document.md) \*\*ctx | Pointer to the MD instance created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](../crypto-common-h/document.md#oh_crypto_errcode) | 
**CRYPTO\_SUCCESS**: The operation is successful.

**CRYPTO\_INVALID\_PARAMS**: A parameter is invalid.

**CRYPTO\_NOT\_SUPPORTED**: The operation is not supported.

**CRYPTO\_MEMORY\_ERROR**: A memory error occurs.

**CRYPTO\_OPERTION\_ERROR**: Failed to call an API of a third-party algorithm library.

 |

#### \[h2\]OH\_CryptoDigest\_Update()

OH\_Crypto\_ErrCode OH\_CryptoDigest\_Update(OH\_CryptoDigest \*ctx, Crypto\_DataBlob \*in)

**Description**

Updates MD data.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoDigest](../../structs/oh-cryptodigest/document.md) \*ctx | Pointer to the MD instance. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*in | Pointer to the data to pass in. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](../crypto-common-h/document.md#oh_crypto_errcode) | 
**CRYPTO\_SUCCESS**: The operation is successful.

**CRYPTO\_INVALID\_PARAMS**: A parameter is invalid.

**CRYPTO\_NOT\_SUPPORTED**: The operation is not supported.

**CRYPTO\_MEMORY\_ERROR**: A memory error occurs.

**CRYPTO\_OPERTION\_ERROR**: Failed to call an API of a third-party algorithm library.

 |

**See also**

[OH\_CryptoDigest\_Final](#oh_cryptodigest_final)

#### \[h2\]OH\_CryptoDigest\_Final()

OH\_Crypto\_ErrCode OH\_CryptoDigest\_Final(OH\_CryptoDigest \*ctx, Crypto\_DataBlob \*out)

**Description**

Implements MD calculation.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoDigest](../../structs/oh-cryptodigest/document.md) \*ctx | Pointer to the MD instance. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*out | Pointer to the MD generated. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](../crypto-common-h/document.md#oh_crypto_errcode) | 
**CRYPTO\_SUCCESS**: The operation is successful.

**CRYPTO\_INVALID\_PARAMS**: A parameter is invalid.

**CRYPTO\_NOT\_SUPPORTED**: The operation is not supported.

**CRYPTO\_MEMORY\_ERROR**: A memory error occurs.

**CRYPTO\_OPERTION\_ERROR**: Failed to call an API of a third-party algorithm library.

 |

**See also**

[OH\_CryptoDigest\_Update](#oh_cryptodigest_update)

#### \[h2\]OH\_CryptoDigest\_GetLength()

uint32\_t OH\_CryptoDigest\_GetLength(OH\_CryptoDigest \*ctx)

**Description**

Obtains the length of an MD.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoDigest](../../structs/oh-cryptodigest/document.md) \*ctx | Pointer to the MD instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | 
MD length.

If the input parameter **ctx** is **NULL**, **401** is returned. In other cases, **0** is returned.

 |

#### \[h2\]OH\_CryptoDigest\_GetAlgoName()

const char \*OH\_CryptoDigest\_GetAlgoName(OH\_CryptoDigest \*ctx)

**Description**

Obtains the name of an MD algorithm.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoDigest](../../structs/oh-cryptodigest/document.md) \*ctx | Pointer to the MD instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char \* | MD algorithm name. |

#### \[h2\]OH\_DigestCrypto\_Destroy()

void OH\_DigestCrypto\_Destroy(OH\_CryptoDigest \*ctx)

**Description**

Destroys an MD instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoDigest](../../structs/oh-cryptodigest/document.md) \*ctx | Pointer to the MD instance. |
