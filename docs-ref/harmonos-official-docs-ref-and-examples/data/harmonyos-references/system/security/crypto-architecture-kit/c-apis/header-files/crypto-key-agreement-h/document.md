# crypto\_key\_agreement.h

#### Overview

Defines key agreement APIs.

**Header file**: <CryptoArchitectureKit/crypto\_key\_agreement.h>

**Library**: libohcrypto.so

**System capability**: SystemCapability.Security.CryptoFramework

**Since**: 20

**Related module**: [CryptoKeyAgreementApi](../../modules/cryptokeyagreementapi/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_CryptoKeyAgreement](../../structs/oh-cryptokeyagreement/document.md) | OH\_CryptoKeyAgreement | Defines a struct for key agreement. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode OH\_CryptoKeyAgreement\_Create(const char \*algoName, OH\_CryptoKeyAgreement \*\*ctx)](#oh_cryptokeyagreement_create) | 
Creates a key agreement instance based on the given algorithm name.

Note: The created resource must be destroyed by calling [OH\_CryptoKeyAgreement\_Destroy](#oh_cryptokeyagreement_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoKeyAgreement\_GenerateSecret(OH\_CryptoKeyAgreement \*ctx, OH\_CryptoPrivKey \*privkey, OH\_CryptoPubKey \*pubkey, Crypto\_DataBlob \*secret)](#oh_cryptokeyagreement_generatesecret) | 

Generates the secret value of key agreement.

Note: After the use is complete, the memory for storing the **secret** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [void OH\_CryptoKeyAgreement\_Destroy(OH\_CryptoKeyAgreement \*ctx)](#oh_cryptokeyagreement_destroy) | Destroys a key agreement instance. |

#### Function Description

#### \[h2\]OH\_CryptoKeyAgreement\_Create()

OH\_Crypto\_ErrCode OH\_CryptoKeyAgreement\_Create(const char \*algoName, OH\_CryptoKeyAgreement \*\*ctx)

**Description**

Creates a key agreement instance based on the given algorithm name.

Note: The created resource must be destroyed by calling [OH\_CryptoKeyAgreement\_Destroy](#oh_cryptokeyagreement_destroy).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*algoName | 
Algorithm name of the key agreement instance to be created.

For example, **ECC** or **X25519**.

 |
| [OH\_CryptoKeyAgreement](../../structs/oh-cryptokeyagreement/document.md) \*\*ctx | Key agreement instance. |

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

#### \[h2\]OH\_CryptoKeyAgreement\_GenerateSecret()

OH\_Crypto\_ErrCode OH\_CryptoKeyAgreement\_GenerateSecret(OH\_CryptoKeyAgreement \*ctx, OH\_CryptoPrivKey \*privkey, OH\_CryptoPubKey \*pubkey, Crypto\_DataBlob \*secret)

**Description**

Generates the secret value of key agreement.

Note: After the use is complete, the memory for storing the **secret** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoKeyAgreement](../../structs/oh-cryptokeyagreement/document.md) \*ctx | Key agreement instance. |
| [OH\_CryptoPrivKey](../../structs/oh-cryptoprivkey/document.md) \*privkey | Private key. |
| [OH\_CryptoPubKey](../../structs/oh-cryptopubkey/document.md) \*pubkey | Public key. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*secret | Secret value. |

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

#### \[h2\]OH\_CryptoKeyAgreement\_Destroy()

void OH\_CryptoKeyAgreement\_Destroy(OH\_CryptoKeyAgreement \*ctx)

**Description**

Destroys a key agreement instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoKeyAgreement](../../structs/oh-cryptokeyagreement/document.md) \*ctx | Key agreement instance. |
