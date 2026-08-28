# crypto\_sym\_key.h

#### Overview

Provides APIs for symmetric keys.

**Header file**: <CryptoArchitectureKit/crypto\_sym\_key.h>

**Library**: libohcrypto.so

**System capability**: SystemCapability.Security.CryptoFramework

**Since**: 12

**Related module**: [CryptoSymKeyApi](../../modules/cryptosymkeyapi/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_CryptoSymKey](../../structs/oh-cryptosymkey/document.md) | OH\_CryptoSymKey | Defines a struct for a symmetric key generator. |
| [OH\_CryptoSymKeyGenerator](../../structs/oh-cryptosymkeygenerator/document.md) | OH\_CryptoSymKeyGenerator | Defines a struct for a symmetric key. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode OH\_CryptoSymKeyGenerator\_Create(const char \*algoName, OH\_CryptoSymKeyGenerator \*\*ctx)](#oh_cryptosymkeygenerator_create) | 
Creates a symmetric key generator instance based on the given algorithm name.

Note: The created resource must be destroyed by calling [OH\_CryptoSymKeyGenerator\_Destroy](#oh_cryptosymkeygenerator_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoSymKeyGenerator\_Generate(OH\_CryptoSymKeyGenerator \*ctx, OH\_CryptoSymKey \*\*keyCtx)](#oh_cryptosymkeygenerator_generate) | 

Randomly generates a symmetric key.

Note: After the use is complete, the memory for storing the **keyCtx** parameter must be destroyed by calling [OH\_CryptoSymKey\_Destroy](#oh_cryptosymkey_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoSymKeyGenerator\_Convert(OH\_CryptoSymKeyGenerator \*ctx, const Crypto\_DataBlob \*keyData, OH\_CryptoSymKey \*\*keyCtx)](#oh_cryptosymkeygenerator_convert) | 

Converts binary data into a symmetric key.

Note: After the use is complete, the memory for storing the **keyCtx** parameter must be destroyed by calling [OH\_CryptoSymKey\_Destroy](#oh_cryptosymkey_destroy).

 |
| [const char \*OH\_CryptoSymKeyGenerator\_GetAlgoName(OH\_CryptoSymKeyGenerator \*ctx)](#oh_cryptosymkeygenerator_getalgoname) | Obtains the algorithm of a symmetric key generator instance. |
| [void OH\_CryptoSymKeyGenerator\_Destroy(OH\_CryptoSymKeyGenerator \*ctx)](#oh_cryptosymkeygenerator_destroy) | Destroys a symmetric key generator instance. |
| [const char \*OH\_CryptoSymKey\_GetAlgoName(OH\_CryptoSymKey \*keyCtx)](#oh_cryptosymkey_getalgoname) | Obtains the algorithm of a symmetric key. |
| [OH\_Crypto\_ErrCode OH\_CryptoSymKey\_GetKeyData(OH\_CryptoSymKey \*keyCtx, Crypto\_DataBlob \*out)](#oh_cryptosymkey_getkeydata) | 

Obtains symmetric key data from a key instance.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [void OH\_CryptoSymKey\_Destroy(OH\_CryptoSymKey \*keyCtx)](#oh_cryptosymkey_destroy) | Destroys a symmetric key instance. |

#### Function Description

#### \[h2\]OH\_CryptoSymKeyGenerator\_Create()

OH\_Crypto\_ErrCode OH\_CryptoSymKeyGenerator\_Create(const char \*algoName, OH\_CryptoSymKeyGenerator \*\*ctx)

**Description**

Creates a symmetric key generator instance based on the given algorithm name.

Note: The created resource must be destroyed by calling [OH\_CryptoSymKeyGenerator\_Destroy](#oh_cryptosymkeygenerator_destroy).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*algoName | 
Pointer the algorithm used to create a generator.

For example, **AES256**, **AES128**, and **SM4**.

 |
| [OH\_CryptoSymKeyGenerator](../../structs/oh-cryptosymkeygenerator/document.md) \*\*ctx | Double pointer to the symmetric key generator instance created. |

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

#### \[h2\]OH\_CryptoSymKeyGenerator\_Generate()

OH\_Crypto\_ErrCode OH\_CryptoSymKeyGenerator\_Generate(OH\_CryptoSymKeyGenerator \*ctx, OH\_CryptoSymKey \*\*keyCtx)

**Description**

Randomly generates a symmetric key.

Note: After the use is complete, the memory for storing the **keyCtx** parameter must be destroyed by calling [OH\_CryptoSymKey\_Destroy](#oh_cryptosymkey_destroy).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoSymKeyGenerator](../../structs/oh-cryptosymkeygenerator/document.md) \*ctx | Pointer to the symmetric key generator instance. |
| [OH\_CryptoSymKey](../../structs/oh-cryptosymkey/document.md) \*\*keyCtx | Pointer to the symmetric key created. |

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

#### \[h2\]OH\_CryptoSymKeyGenerator\_Convert()

OH\_Crypto\_ErrCode OH\_CryptoSymKeyGenerator\_Convert(OH\_CryptoSymKeyGenerator \*ctx, const Crypto\_DataBlob \*keyData, OH\_CryptoSymKey \*\*keyCtx)

**Description**

Converts binary data into a symmetric key.

Note: After the use is complete, the memory for storing the **keyCtx** parameter must be destroyed by calling [OH\_CryptoSymKey\_Destroy](#oh_cryptosymkey_destroy).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoSymKeyGenerator](../../structs/oh-cryptosymkeygenerator/document.md) \*ctx | Pointer to the symmetric key generator instance. |
| [const Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*keyData | Pointer to the data to convert. |
| [OH\_CryptoSymKey](../../structs/oh-cryptosymkey/document.md) \*\*keyCtx | Pointer to the symmetric key obtained. |

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

#### \[h2\]OH\_CryptoSymKeyGenerator\_GetAlgoName()

const char \*OH\_CryptoSymKeyGenerator\_GetAlgoName(OH\_CryptoSymKeyGenerator \*ctx)

**Description**

Obtains the algorithm of a symmetric key generator instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoSymKeyGenerator](../../structs/oh-cryptosymkeygenerator/document.md) \*ctx | Double pointer to the symmetric key generator instance created. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char \* | Algorithm of a symmetric key generator instance. |

#### \[h2\]OH\_CryptoSymKeyGenerator\_Destroy()

void OH\_CryptoSymKeyGenerator\_Destroy(OH\_CryptoSymKeyGenerator \*ctx)

**Description**

Destroys a symmetric key generator instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoSymKeyGenerator](../../structs/oh-cryptosymkeygenerator/document.md) \*ctx | Double pointer to the symmetric key generator instance created. |

#### \[h2\]OH\_CryptoSymKey\_GetAlgoName()

const char \*OH\_CryptoSymKey\_GetAlgoName(OH\_CryptoSymKey \*keyCtx)

**Description**

Obtains the algorithm of a symmetric key.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoSymKey](../../structs/oh-cryptosymkey/document.md) \*keyCtx | Pointer to the symmetric key instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char \* | Symmetric key algorithm obtained. |

#### \[h2\]OH\_CryptoSymKey\_GetKeyData()

OH\_Crypto\_ErrCode OH\_CryptoSymKey\_GetKeyData(OH\_CryptoSymKey \*keyCtx, Crypto\_DataBlob \*out)

**Description**

Obtains symmetric key data from a key instance.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoSymKey](../../structs/oh-cryptosymkey/document.md) \*keyCtx | Pointer to the symmetric key instance. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*out | Pointer to the data obtained. |

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

#### \[h2\]OH\_CryptoSymKey\_Destroy()

void OH\_CryptoSymKey\_Destroy(OH\_CryptoSymKey \*keyCtx)

**Description**

Destroys a symmetric key instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoSymKey](../../structs/oh-cryptosymkey/document.md) \*keyCtx | Pointer to the symmetric key instance. |
