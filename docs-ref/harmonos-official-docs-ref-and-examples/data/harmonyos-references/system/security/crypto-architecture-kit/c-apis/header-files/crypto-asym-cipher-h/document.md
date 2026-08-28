# crypto\_asym\_cipher.h

#### Overview

Defines APIs for encrypting and decrypting asymmetric keys.

**Header file**: <CryptoArchitectureKit/crypto\_asym\_cipher.h>

**Library**: libohcrypto.so

**System capability**: SystemCapability.Security.CryptoFramework

**Since**: 20

**Related module**: [CryptoAsymCipherApi](../../modules/cryptoasymcipherapi/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_CryptoAsymCipher](../../structs/oh-cryptoasymcipher/document.md) | OH\_CryptoAsymCipher | Defines asymmetric encryption. |
| [OH\_CryptoSm2CiphertextSpec](../../structs/oh-cryptosm2ciphertextspec/document.md) | OH\_CryptoSm2CiphertextSpec | Defines SM2 ciphertext specifications. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [CryptoSm2CiphertextSpec\_item](#cryptosm2ciphertextspec_item) | CryptoSm2CiphertextSpec\_item | Defines the type of SM2 ciphertext specification items. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymCipher\_Create(const char \*algoName, OH\_CryptoAsymCipher \*\*ctx)](#oh_cryptoasymcipher_create) | 
Creates an asymmetric encryption instance based on the given algorithm name.

Note: The created resource must be destroyed by calling [OH\_CryptoAsymCipher\_Destroy](#oh_cryptoasymcipher_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymCipher\_Init(OH\_CryptoAsymCipher \*ctx, Crypto\_CipherMode mode, OH\_CryptoKeyPair \*key)](#oh_cryptoasymcipher_init) | Initializes asymmetric encryption. |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymCipher\_Final(OH\_CryptoAsymCipher \*ctx, const Crypto\_DataBlob \*in, Crypto\_DataBlob \*out)](#oh_cryptoasymcipher_final) | 

Finalizes asymmetric encryption.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [void OH\_CryptoAsymCipher\_Destroy(OH\_CryptoAsymCipher \*ctx)](#oh_cryptoasymcipher_destroy) | Destroys an asymmetric encryption context. |
| [OH\_Crypto\_ErrCode OH\_CryptoSm2CiphertextSpec\_Create(Crypto\_DataBlob \*sm2Ciphertext, OH\_CryptoSm2CiphertextSpec \*\*spec)](#oh_cryptosm2ciphertextspec_create) | 

Creates SM2 ciphertext specifications.

Note: The created resource must be destroyed by calling [OH\_CryptoSm2CiphertextSpec\_Destroy](#oh_cryptosm2ciphertextspec_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoSm2CiphertextSpec\_GetItem(OH\_CryptoSm2CiphertextSpec \*spec, CryptoSm2CiphertextSpec\_item item, Crypto\_DataBlob \*out)](#oh_cryptosm2ciphertextspec_getitem) | 

Obtains a specified item in SM2 ciphertext specifications.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoSm2CiphertextSpec\_SetItem(OH\_CryptoSm2CiphertextSpec \*spec, CryptoSm2CiphertextSpec\_item item, Crypto\_DataBlob \*in)](#oh_cryptosm2ciphertextspec_setitem) | Sets a specified item in SM2 ciphertext specifications. |
| [OH\_Crypto\_ErrCode OH\_CryptoSm2CiphertextSpec\_Encode(OH\_CryptoSm2CiphertextSpec \*spec, Crypto\_DataBlob \*out)](#oh_cryptosm2ciphertextspec_encode) | 

Encodes SM2 ciphertext specifications into DER ciphertext.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [void OH\_CryptoSm2CiphertextSpec\_Destroy(OH\_CryptoSm2CiphertextSpec \*spec)](#oh_cryptosm2ciphertextspec_destroy) | Destroys SM2 ciphertext specifications. |

#### Enum Description

#### \[h2\]CryptoSm2CiphertextSpec\_item

enum CryptoSm2CiphertextSpec\_item

**Description**

Defines the type of SM2 ciphertext specification items.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| CRYPTO\_SM2\_CIPHERTEXT\_C1\_X = 0 | Public key x, also called C1x. |
| CRYPTO\_SM2\_CIPHERTEXT\_C1\_Y = 1 | Public key y, also called C1y. |
| CRYPTO\_SM2\_CIPHERTEXT\_C2 = 2 | Hash value, also called C2. |
| CRYPTO\_SM2\_CIPHERTEXT\_C3 = 3 | Ciphertext data, also called C3. |

#### Function Description

#### \[h2\]OH\_CryptoAsymCipher\_Create()

OH\_Crypto\_ErrCode OH\_CryptoAsymCipher\_Create(const char \*algoName, OH\_CryptoAsymCipher \*\*ctx)

**Description**

Creates an asymmetric encryption instance based on the given algorithm name.

Note: The created resource must be destroyed by calling [OH\_CryptoAsymCipher\_Destroy](#oh_cryptoasymcipher_destroy).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*algoName | 
Pointer to the algorithm used to generate an encryption instance.

For example, **RSA|PKCS1\_OAEP|SHA384|MGF1\_SHA384** or **SM2|SM3**.

 |
| [OH\_CryptoAsymCipher](../../structs/oh-cryptoasymcipher/document.md) \*\*ctx | Pointer to the asymmetric encryption context. |

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

#### \[h2\]OH\_CryptoAsymCipher\_Init()

OH\_Crypto\_ErrCode OH\_CryptoAsymCipher\_Init(OH\_CryptoAsymCipher \*ctx, Crypto\_CipherMode mode, OH\_CryptoKeyPair \*key)

**Description**

Initializes asymmetric encryption.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoAsymCipher](../../structs/oh-cryptoasymcipher/document.md) \*ctx | Pointer to the asymmetric encryption context. |
| [Crypto\_CipherMode](../crypto-common-h/document.md#crypto_ciphermode) mode | Cipher mode (encryption or decryption). |
| [OH\_CryptoKeyPair](../../structs/oh-cryptokeypair/document.md) \*key | Pointer to the asymmetric key. |

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

**Reference**

[OH\_CryptoAsymCipher\_Final](#oh_cryptoasymcipher_final)

#### \[h2\]OH\_CryptoAsymCipher\_Final()

OH\_Crypto\_ErrCode OH\_CryptoAsymCipher\_Final(OH\_CryptoAsymCipher \*ctx, const Crypto\_DataBlob \*in, Crypto\_DataBlob \*out)

**Description**

Finalizes asymmetric encryption.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoAsymCipher](../../structs/oh-cryptoasymcipher/document.md) \*ctx | Pointer to the asymmetric encryption context. |
| [const Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*in | Pointer to the data to be encrypted or decrypted. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*out | Pointer to the encrypted or decrypted data. |

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

**Reference**

[OH\_CryptoAsymCipher\_Init](#oh_cryptoasymcipher_init)

#### \[h2\]OH\_CryptoAsymCipher\_Destroy()

void OH\_CryptoAsymCipher\_Destroy(OH\_CryptoAsymCipher \*ctx)

**Description**

Destroys an asymmetric encryption context.

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoAsymCipher](../../structs/oh-cryptoasymcipher/document.md) \*ctx | Pointer to the asymmetric encryption context. |

#### \[h2\]OH\_CryptoSm2CiphertextSpec\_Create()

OH\_Crypto\_ErrCode OH\_CryptoSm2CiphertextSpec\_Create(Crypto\_DataBlob \*sm2Ciphertext, OH\_CryptoSm2CiphertextSpec \*\*spec)

**Description**

Creates SM2 ciphertext specifications.

Note: The created resource must be destroyed by calling [OH\_CryptoSm2CiphertextSpec\_Destroy](#oh_cryptosm2ciphertextspec_destroy).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*sm2Ciphertext | Pointer to the SM2 ciphertext in DER format. If the value is **NULL**, an empty SM2 ciphertext specification is created. |
| [OH\_CryptoSm2CiphertextSpec](../../structs/oh-cryptosm2ciphertextspec/document.md) \*\*spec | Pointer to the output SM2 ciphertext specifications. |

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

#### \[h2\]OH\_CryptoSm2CiphertextSpec\_GetItem()

OH\_Crypto\_ErrCode OH\_CryptoSm2CiphertextSpec\_GetItem(OH\_CryptoSm2CiphertextSpec \*spec, CryptoSm2CiphertextSpec\_item item, Crypto\_DataBlob \*out)

**Description**

Obtains a specified item in SM2 ciphertext specifications.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoSm2CiphertextSpec](../../structs/oh-cryptosm2ciphertextspec/document.md) \*spec | Pointer to the SM2 ciphertext specifications. |
| [CryptoSm2CiphertextSpec\_item](#cryptosm2ciphertextspec_item) item | Pointer to the SM2 ciphertext specifications. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*out | Pointer to the output data. |

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

#### \[h2\]OH\_CryptoSm2CiphertextSpec\_SetItem()

OH\_Crypto\_ErrCode OH\_CryptoSm2CiphertextSpec\_SetItem(OH\_CryptoSm2CiphertextSpec \*spec, CryptoSm2CiphertextSpec\_item item, Crypto\_DataBlob \*in)

**Description**

Sets a specified item in SM2 ciphertext specifications.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoSm2CiphertextSpec](../../structs/oh-cryptosm2ciphertextspec/document.md) \*spec | Pointer to the SM2 ciphertext specifications. |
| [CryptoSm2CiphertextSpec\_item](#cryptosm2ciphertextspec_item) item | Pointer to the SM2 ciphertext specifications. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*in | Pointer to the input data. |

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

#### \[h2\]OH\_CryptoSm2CiphertextSpec\_Encode()

OH\_Crypto\_ErrCode OH\_CryptoSm2CiphertextSpec\_Encode(OH\_CryptoSm2CiphertextSpec \*spec, Crypto\_DataBlob \*out)

**Description**

Encodes SM2 ciphertext specifications into DER ciphertext.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoSm2CiphertextSpec](../../structs/oh-cryptosm2ciphertextspec/document.md) \*spec | Pointer to the SM2 ciphertext specifications. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*out | Pointer to the output data. |

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

#### \[h2\]OH\_CryptoSm2CiphertextSpec\_Destroy()

void OH\_CryptoSm2CiphertextSpec\_Destroy(OH\_CryptoSm2CiphertextSpec \*spec)

**Description**

Destroys SM2 ciphertext specifications.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoSm2CiphertextSpec](../../structs/oh-cryptosm2ciphertextspec/document.md) \*spec | Pointer to the SM2 ciphertext specifications. |
