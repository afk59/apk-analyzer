# crypto\_kdf.h

#### Overview

Defines key derivation function (KDF) APIs.

**Header file**: <CryptoArchitectureKit/crypto\_kdf.h>

**Library**: libohcrypto.so

**System capability**: SystemCapability.Security.CryptoFramework

**Since**: 20

**Related module**: [CryptoKdfApi](../../modules/cryptokdfapi/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_CryptoKdf](../../structs/oh-cryptokdf/document.md) | OH\_CryptoKdf | Defines a KDF. |
| [OH\_CryptoKdfParams](../../structs/oh-cryptokdfparams/document.md) | OH\_CryptoKdfParams | Defines KDF parameters. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [CryptoKdf\_ParamType](#cryptokdf_paramtype) | CryptoKdf\_ParamType | Defines KDF parameter types. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode OH\_CryptoKdfParams\_Create(const char \*algoName, OH\_CryptoKdfParams \*\*params)](#oh_cryptokdfparams_create) | 
Creates KDF parameters.

Note: The created resource must be destroyed by calling [OH\_CryptoKdfParams\_Destroy](#oh_cryptokdfparams_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoKdfParams\_SetParam(OH\_CryptoKdfParams \*params, CryptoKdf\_ParamType type, Crypto\_DataBlob \*value)](#oh_cryptokdfparams_setparam) | Sets KDF parameters. |
| [void OH\_CryptoKdfParams\_Destroy(OH\_CryptoKdfParams \*params)](#oh_cryptokdfparams_destroy) | Destroys KDF parameters. |
| [OH\_Crypto\_ErrCode OH\_CryptoKdf\_Create(const char \*algoName, OH\_CryptoKdf \*\*ctx)](#oh_cryptokdf_create) | 

Creates a KDF instance.

Note: The created resource must be destroyed by calling [OH\_CryptoKdf\_Destroy](#oh_cryptokdf_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoKdf\_Derive(OH\_CryptoKdf \*ctx, const OH\_CryptoKdfParams \*params, int keyLen, Crypto\_DataBlob \*key)](#oh_cryptokdf_derive) | 

Derives a key.

Note: After the use is complete, the memory for storing the **key** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [void OH\_CryptoKdf\_Destroy(OH\_CryptoKdf \*ctx)](#oh_cryptokdf_destroy) | Destroys a KDF instance. |

#### Enum Description

#### \[h2\]CryptoKdf\_ParamType

enum CryptoKdf\_ParamType

**Description**

Defines KDF parameter types.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| CRYPTO\_KDF\_KEY\_DATABLOB = 0 | Key or password of the KDF. |
| CRYPTO\_KDF\_SALT\_DATABLOB = 1 | Salt value of the KDF. |
| CRYPTO\_KDF\_INFO\_DATABLOB = 2 | Information of the KDF. |
| CRYPTO\_KDF\_ITER\_COUNT\_INT = 3 | Iteration count of PBKDF2. |
| CRYPTO\_KDF\_SCRYPT\_N\_UINT64 = 4 | Parameter **n** of the SCRYPT KDF. |
| CRYPTO\_KDF\_SCRYPT\_R\_UINT64 = 5 | Parameter **r** of the SCRYPT KDF. |
| CRYPTO\_KDF\_SCRYPT\_P\_UINT64 = 6 | Parameter **p** of the SCRYPT KDF. |
| CRYPTO\_KDF\_SCRYPT\_MAX\_MEM\_UINT64 = 7 | Maximum memory usage of the SCRYPT KDF. |

#### Function Description

#### \[h2\]OH\_CryptoKdfParams\_Create()

OH\_Crypto\_ErrCode OH\_CryptoKdfParams\_Create(const char \*algoName, OH\_CryptoKdfParams \*\*params)

**Description**

Creates KDF parameters.

Note: The created resource must be destroyed by calling [OH\_CryptoKdfParams\_Destroy](#oh_cryptokdfparams_destroy).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*algoName | 
KDF algorithm name.

For example, **HKDF|SHA384|EXTRACT\_AND\_EXPAND** or **PBKDF2|SHA384**.

 |
| [OH\_CryptoKdfParams](../../structs/oh-cryptokdfparams/document.md) \*\*params | KDF parameters. |

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

#### \[h2\]OH\_CryptoKdfParams\_SetParam()

OH\_Crypto\_ErrCode OH\_CryptoKdfParams\_SetParam(OH\_CryptoKdfParams \*params, CryptoKdf\_ParamType type, Crypto\_DataBlob \*value)

**Description**

Sets KDF parameters.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoKdfParams](../../structs/oh-cryptokdfparams/document.md) \*params | KDF parameters. |
| [CryptoKdf\_ParamType](#cryptokdf_paramtype) type | KDF parameter type. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*value | KDF parameter values. |

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

#### \[h2\]OH\_CryptoKdfParams\_Destroy()

void OH\_CryptoKdfParams\_Destroy(OH\_CryptoKdfParams \*params)

**Description**

Destroys KDF parameters.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoKdfParams](../../structs/oh-cryptokdfparams/document.md) \*params | KDF parameters. |

#### \[h2\]OH\_CryptoKdf\_Create()

OH\_Crypto\_ErrCode OH\_CryptoKdf\_Create(const char \*algoName, OH\_CryptoKdf \*\*ctx)

**Description**

Creates a KDF instance.

Note: The created resource must be destroyed by calling [OH\_CryptoKdf\_Destroy](#oh_cryptokdf_destroy).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*algoName | KDF algorithm name. |
| [OH\_CryptoKdf](../../structs/oh-cryptokdf/document.md) \*\*ctx | KDF instance. |

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

#### \[h2\]OH\_CryptoKdf\_Derive()

OH\_Crypto\_ErrCode OH\_CryptoKdf\_Derive(OH\_CryptoKdf \*ctx, const OH\_CryptoKdfParams \*params, int keyLen, Crypto\_DataBlob \*key)

**Description**

Derives a key.

Note: After the use is complete, the memory for storing the **key** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoKdf](../../structs/oh-cryptokdf/document.md) \*ctx | KDF instance. |
| [const OH\_CryptoKdfParams](../../structs/oh-cryptokdfparams/document.md) \*params | KDF parameters. |
| int keyLen | Length of the derived key. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*key | Derived key. |

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

#### \[h2\]OH\_CryptoKdf\_Destroy()

void OH\_CryptoKdf\_Destroy(OH\_CryptoKdf \*ctx)

**Description**

Destroys a KDF instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoKdf](../../structs/oh-cryptokdf/document.md) \*ctx | KDF instance. |
