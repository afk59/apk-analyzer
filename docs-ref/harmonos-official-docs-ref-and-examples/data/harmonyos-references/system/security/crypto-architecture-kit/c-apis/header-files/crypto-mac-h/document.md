# crypto\_mac.h

#### Overview

Define message authentication code (MAC) APIs.

**Header file**: <CryptoArchitectureKit/crypto\_mac.h>

**Library**: libohcrypto.so

**System capability**: SystemCapability.Security.CryptoFramework

**Since**: 20

**Related module**: [CryptoMacApi](../../modules/cryptomacapi/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_CryptoMac](../../structs/oh-cryptomac/document.md) | OH\_CryptoMac | Defines a struct for a MAC. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [CryptoMac\_ParamType](#cryptomac_paramtype) | CryptoMac\_ParamType | Defines the parameter type for the MAC algorithm. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode OH\_CryptoMac\_Create(const char \*algoName, OH\_CryptoMac \*\*ctx)](#oh_cryptomac_create) | 
Creates a MAC instance based on the given algorithm name.

Note: The created resource must be destroyed by calling [OH\_CryptoMac\_Destroy](#oh_cryptomac_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoMac\_SetParam(OH\_CryptoMac \*ctx, CryptoMac\_ParamType type, const Crypto\_DataBlob \*value)](#oh_cryptomac_setparam) | Sets MAC parameters. |
| [OH\_Crypto\_ErrCode OH\_CryptoMac\_Init(OH\_CryptoMac \*ctx, const OH\_CryptoSymKey \*key)](#oh_cryptomac_init) | Initializes a MAC instance using a symmetric key. |
| [OH\_Crypto\_ErrCode OH\_CryptoMac\_Update(OH\_CryptoMac \*ctx, const Crypto\_DataBlob \*in)](#oh_cryptomac_update) | Updates a MAC instance. |
| [OH\_Crypto\_ErrCode OH\_CryptoMac\_Final(OH\_CryptoMac \*ctx, Crypto\_DataBlob \*out)](#oh_cryptomac_final) | 

Finalizes a MAC operation.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoMac\_GetLength(OH\_CryptoMac \*ctx, uint32\_t \*length)](#oh_cryptomac_getlength) | Obtains the MAC length. |
| [void OH\_CryptoMac\_Destroy(OH\_CryptoMac \*ctx)](#oh_cryptomac_destroy) | Destroys a MAC instance. |

#### Enum Description

#### \[h2\]CryptoMac\_ParamType

enum CryptoMac\_ParamType

**Description**

Defines the parameter type for the MAC algorithm.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| CRYPTO\_MAC\_DIGEST\_NAME\_STR = 0 | Algorithm name of the digest function used by the HMAC, for example, **SHA256**. |
| CRYPTO\_MAC\_CIPHER\_NAME\_STR = 1 | Name of the symmetric encryption algorithm used by the CMAC, for example, **AES256**. |

#### Function Description

#### \[h2\]OH\_CryptoMac\_Create()

OH\_Crypto\_ErrCode OH\_CryptoMac\_Create(const char \*algoName, OH\_CryptoMac \*\*ctx)

**Description**

Creates a MAC instance based on the given algorithm name.

Note: The created resource must be destroyed by calling [OH\_CryptoMac\_Destroy](#oh_cryptomac_destroy).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*algoName | 
Pointer to the algorithm used to generate the MAC instance.

For example, **HMAC** or **CMAC**.

 |
| [OH\_CryptoMac](../../structs/oh-cryptomac/document.md) \*\*ctx | MAC instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](../crypto-common-h/document.md#oh_crypto_errcode) | 
**CRYPTO\_SUCCESS**: The operation is successful.

**CRYPTO\_NOT\_SUPPORTED**: The operation is not supported.

**CRYPTO\_MEMORY\_ERROR**: A memory error occurs.

**CRYPTO\_PARAMETER\_CHECK\_FAILED**: The parameter check failed.

**CRYPTO\_OPERATION\_ERROR**: An error occurs when the API of a third-party algorithm library is called.

 |

#### \[h2\]OH\_CryptoMac\_SetParam()

OH\_Crypto\_ErrCode OH\_CryptoMac\_SetParam(OH\_CryptoMac \*ctx, CryptoMac\_ParamType type, const Crypto\_DataBlob \*value)

**Description**

Sets MAC parameters.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoMac](../../structs/oh-cryptomac/document.md) \*ctx | MAC instance. |
| [CryptoMac\_ParamType](#cryptomac_paramtype) type | MAC parameter type. |
| [const Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*value | MAC parameters. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](../crypto-common-h/document.md#oh_crypto_errcode) | 
**CRYPTO\_SUCCESS**: The operation is successful.

**CRYPTO\_NOT\_SUPPORTED**: The operation is not supported.

**CRYPTO\_MEMORY\_ERROR**: A memory error occurs.

**CRYPTO\_PARAMETER\_CHECK\_FAILED**: The parameter check failed.

**CRYPTO\_OPERATION\_ERROR**: An error occurs when the API of a third-party algorithm library is called.

 |

#### \[h2\]OH\_CryptoMac\_Init()

OH\_Crypto\_ErrCode OH\_CryptoMac\_Init(OH\_CryptoMac \*ctx, const OH\_CryptoSymKey \*key)

**Description**

Initializes a MAC instance using a symmetric key.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoMac](../../structs/oh-cryptomac/document.md) \*ctx | MAC instance. |
| [const OH\_CryptoSymKey](../../structs/oh-cryptosymkey/document.md) \*key | Symmetric key obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](../crypto-common-h/document.md#oh_crypto_errcode) | 
**CRYPTO\_SUCCESS**: The operation is successful.

**CRYPTO\_NOT\_SUPPORTED**: The operation is not supported.

**CRYPTO\_MEMORY\_ERROR**: A memory error occurs.

**CRYPTO\_PARAMETER\_CHECK\_FAILED**: The parameter check failed.

**CRYPTO\_OPERATION\_ERROR**: An error occurs when the API of a third-party algorithm library is called.

 |

**Reference**

[OH\_CryptoMac\_Update](#oh_cryptomac_update)

[OH\_CryptoMac\_Final](#oh_cryptomac_final)

#### \[h2\]OH\_CryptoMac\_Update()

OH\_Crypto\_ErrCode OH\_CryptoMac\_Update(OH\_CryptoMac \*ctx, const Crypto\_DataBlob \*in)

**Description**

Updates a MAC instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoMac](../../structs/oh-cryptomac/document.md) \*ctx | MAC instance. |
| [const Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*in | Data to be updated. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](../crypto-common-h/document.md#oh_crypto_errcode) | 
**CRYPTO\_SUCCESS**: The operation is successful.

**CRYPTO\_NOT\_SUPPORTED**: The operation is not supported.

**CRYPTO\_MEMORY\_ERROR**: A memory error occurs.

**CRYPTO\_PARAMETER\_CHECK\_FAILED**: The parameter check failed.

**CRYPTO\_OPERATION\_ERROR**: An error occurs when the API of a third-party algorithm library is called.

 |

**Reference**

[OH\_CryptoMac\_Init](#oh_cryptomac_init)

[OH\_CryptoMac\_Final](#oh_cryptomac_final)

#### \[h2\]OH\_CryptoMac\_Final()

OH\_Crypto\_ErrCode OH\_CryptoMac\_Final(OH\_CryptoMac \*ctx, Crypto\_DataBlob \*out)

**Description**

Finalizes a MAC operation.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoMac](../../structs/oh-cryptomac/document.md) \*ctx | MAC instance. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*out | MAC value. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](../crypto-common-h/document.md#oh_crypto_errcode) | 
**CRYPTO\_SUCCESS**: The operation is successful.

**CRYPTO\_NOT\_SUPPORTED**: The operation is not supported.

**CRYPTO\_MEMORY\_ERROR**: A memory error occurs.

**CRYPTO\_PARAMETER\_CHECK\_FAILED**: The parameter check failed.

**CRYPTO\_OPERATION\_ERROR**: An error occurs when the API of a third-party algorithm library is called.

 |

**Reference**

[OH\_CryptoMac\_Init](#oh_cryptomac_init)

[OH\_CryptoMac\_Update](#oh_cryptomac_update)

#### \[h2\]OH\_CryptoMac\_GetLength()

OH\_Crypto\_ErrCode OH\_CryptoMac\_GetLength(OH\_CryptoMac \*ctx, uint32\_t \*length)

**Description**

Obtains the MAC length.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoMac](../../structs/oh-cryptomac/document.md) \*ctx | MAC instance. |
| uint32\_t \*length | MAC length. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](../crypto-common-h/document.md#oh_crypto_errcode) | 
**CRYPTO\_SUCCESS**: The operation is successful.

**CRYPTO\_NOT\_SUPPORTED**: The operation is not supported.

**CRYPTO\_MEMORY\_ERROR**: A memory error occurs.

**CRYPTO\_PARAMETER\_CHECK\_FAILED**: The parameter check failed.

**CRYPTO\_OPERATION\_ERROR**: An error occurs when the API of a third-party algorithm library is called.

 |

#### \[h2\]OH\_CryptoMac\_Destroy()

void OH\_CryptoMac\_Destroy(OH\_CryptoMac \*ctx)

**Description**

Destroys a MAC instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoMac](../../structs/oh-cryptomac/document.md) \*ctx | MAC instance. |
