# crypto\_rand.h

#### Overview

Defines APIs for a random number generator.

**Header file**: <CryptoArchitectureKit/crypto\_rand.h>

**Library**: libohcrypto.so

**System capability**: SystemCapability.Security.CryptoFramework

**Since**: 20

**Related module**: [CryptoRandApi](../../modules/cryptorandapi/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_CryptoRand](../../structs/oh-cryptorand/document.md) | OH\_CryptoRand | Defines a struct for a random number generator. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode OH\_CryptoRand\_Create(OH\_CryptoRand \*\*ctx)](#oh_cryptorand_create) | 
Creates a random number generator.

Note: The created resource must be destroyed by calling [OH\_CryptoRand\_Destroy](#oh_cryptorand_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoRand\_GenerateRandom(OH\_CryptoRand \*ctx, int len, Crypto\_DataBlob \*out)](#oh_cryptorand_generaterandom) | 

Generates random numbers.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [const char \*OH\_CryptoRand\_GetAlgoName(OH\_CryptoRand \*ctx)](#oh_cryptorand_getalgoname) | Obtains the algorithm name of a random number generator instance. |
| [OH\_Crypto\_ErrCode OH\_CryptoRand\_SetSeed(OH\_CryptoRand \*ctx, Crypto\_DataBlob \*seed)](#oh_cryptorand_setseed) | Sets the seed of a random number generator. |
| [OH\_Crypto\_ErrCode OH\_CryptoRand\_EnableHardwareEntropy(OH\_CryptoRand \*ctx)](#oh_cryptorand_enablehardwareentropy) | Enables the hardware entropy source. |
| [void OH\_CryptoRand\_Destroy(OH\_CryptoRand \*ctx)](#oh_cryptorand_destroy) | Destroys a random number generator instance. |

#### Function Description

#### \[h2\]OH\_CryptoRand\_Create()

OH\_Crypto\_ErrCode OH\_CryptoRand\_Create(OH\_CryptoRand \*\*ctx)

**Description**

Creates a random number generator.

Note: The created resource must be destroyed by calling [OH\_CryptoRand\_Destroy](#oh_cryptorand_destroy).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoRand](../../structs/oh-cryptorand/document.md) \*\*ctx | Pointer to the random number generator instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](../crypto-common-h/document.md#oh_crypto_errcode) | 
**CRYPTO\_SUCCESS**: The operation is successful.

**CRYPTO\_NOT\_SUPPORTED**: The operation is not supported.

**CRYPTO\_MEMORY\_ERROR**: A memory error occurs.

**CRYPTO\_PARAMETER\_CHECK\_FAILED**: The parameter check failed.

**CRYPTO\_OPERTION\_ERROR**: Failed to call an API of a third-party algorithm library.

 |

#### \[h2\]OH\_CryptoRand\_GenerateRandom()

OH\_Crypto\_ErrCode OH\_CryptoRand\_GenerateRandom(OH\_CryptoRand \*ctx, int len, Crypto\_DataBlob \*out)

**Description**

Generates random numbers.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoRand](../../structs/oh-cryptorand/document.md) \*ctx | Random number generator instance. |
| int len | Length of the random number to generate, in bytes. The value range is \[1, INT\_MAX\]. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*out | Pointer to the random number. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](../crypto-common-h/document.md#oh_crypto_errcode) | 
**CRYPTO\_SUCCESS**: The operation is successful.

**CRYPTO\_NOT\_SUPPORTED**: The operation is not supported.

**CRYPTO\_MEMORY\_ERROR**: A memory error occurs.

**CRYPTO\_PARAMETER\_CHECK\_FAILED**: The parameter check failed.

**CRYPTO\_OPERTION\_ERROR**: Failed to call an API of a third-party algorithm library.

 |

#### \[h2\]OH\_CryptoRand\_GetAlgoName()

const char \*OH\_CryptoRand\_GetAlgoName(OH\_CryptoRand \*ctx)

**Description**

Obtains the algorithm name of a random number generator instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoRand](../../structs/oh-cryptorand/document.md) \*ctx | Pointer to the random number generator instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char \* | Algorithm name of a random number generator instance. |

#### \[h2\]OH\_CryptoRand\_SetSeed()

OH\_Crypto\_ErrCode OH\_CryptoRand\_SetSeed(OH\_CryptoRand \*ctx, Crypto\_DataBlob \*seed)

**Description**

Sets the seed of a random number generator.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoRand](../../structs/oh-cryptorand/document.md) \*ctx | Random number generator instance. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*seed | Seed data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](../crypto-common-h/document.md#oh_crypto_errcode) | 
**CRYPTO\_SUCCESS**: The operation is successful.

**CRYPTO\_NOT\_SUPPORTED**: The operation is not supported.

**CRYPTO\_MEMORY\_ERROR**: A memory error occurs.

**CRYPTO\_PARAMETER\_CHECK\_FAILED**: The parameter check failed.

**CRYPTO\_OPERTION\_ERROR**: Failed to call an API of a third-party algorithm library.

 |

#### \[h2\]OH\_CryptoRand\_EnableHardwareEntropy()

OH\_Crypto\_ErrCode OH\_CryptoRand\_EnableHardwareEntropy(OH\_CryptoRand \*ctx)

**Description**

Enables the hardware entropy source.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoRand](../../structs/oh-cryptorand/document.md) \*ctx | Random number generator instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](../crypto-common-h/document.md#oh_crypto_errcode) | 
**CRYPTO\_SUCCESS**: The operation is successful.

**CRYPTO\_NOT\_SUPPORTED**: The operation is not supported.

**CRYPTO\_MEMORY\_ERROR**: A memory error occurs.

**CRYPTO\_PARAMETER\_CHECK\_FAILED**: The parameter check failed.

**CRYPTO\_OPERTION\_ERROR**: Failed to call an API of a third-party algorithm library.

 |

#### \[h2\]OH\_CryptoRand\_Destroy()

void OH\_CryptoRand\_Destroy(OH\_CryptoRand \*ctx)

**Description**

Destroys a random number generator instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoRand](../../structs/oh-cryptorand/document.md) \*ctx | Random number generator instance. |
