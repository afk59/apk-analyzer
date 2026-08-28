# crypto\_signature.h

#### Overview

Defines APIs for signature verification.

**Header file**: <CryptoArchitectureKit/crypto\_signature.h>

**Library**: libohcrypto.so

**System capability**: SystemCapability.Security.CryptoFramework

**Since**: 12

**Related module**: [CryptoSignatureApi](../../modules/cryptosignatureapi/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_CryptoVerify](../../structs/oh-cryptoverify/document.md) | OH\_CryptoVerify | Defines the data used for signature verification. |
| [OH\_CryptoSign](../../structs/oh-cryptosign/document.md) | OH\_CryptoSign | Defines a struct for signing. |
| [OH\_CryptoEccSignatureSpec](../../structs/oh-cryptoeccsignaturespec/document.md) | OH\_CryptoEccSignatureSpec | Defines a struct for ECC signing specifications. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [CryptoSignature\_ParamType](#cryptosignature_paramtype) | CryptoSignature\_ParamType | Enumerates the types of signature verification parameters. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode OH\_CryptoVerify\_Create(const char \*algoName, OH\_CryptoVerify \*\*verify)](#oh_cryptoverify_create) | 
Creates a **Verify** instance for signature verification.

Note: The created resource must be destroyed by calling [OH\_CryptoVerify\_Destroy](#oh_cryptoverify_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoVerify\_Init(OH\_CryptoVerify \*ctx, OH\_CryptoPubKey \*pubKey)](#oh_cryptoverify_init) | Initializes a **Verify** instance by using the public key. |
| [OH\_Crypto\_ErrCode OH\_CryptoVerify\_Update(OH\_CryptoVerify \*ctx, Crypto\_DataBlob \*in)](#oh_cryptoverify_update) | Updates the data to be verified. |
| [bool OH\_CryptoVerify\_Final(OH\_CryptoVerify \*ctx, Crypto\_DataBlob \*in, Crypto\_DataBlob \*signData)](#oh_cryptoverify_final) | Verifies the signature of the data. |
| [OH\_Crypto\_ErrCode OH\_CryptoVerify\_Recover(OH\_CryptoVerify \*ctx, Crypto\_DataBlob \*signData, Crypto\_DataBlob \*rawSignData)](#oh_cryptoverify_recover) | 

Restores the raw signature data.

Note: After the use is complete, the memory for storing the **rawSignData** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [const char \*OH\_CryptoVerify\_GetAlgoName(OH\_CryptoVerify \*ctx)](#oh_cryptoverify_getalgoname) | Obtains the signature verification algorithm. |
| [OH\_Crypto\_ErrCode OH\_CryptoVerify\_SetParam(OH\_CryptoVerify \*ctx, CryptoSignature\_ParamType type, Crypto\_DataBlob \*value)](#oh_cryptoverify_setparam) | Sets a signature verification parameter. |
| [OH\_Crypto\_ErrCode OH\_CryptoVerify\_GetParam(OH\_CryptoVerify \*ctx, CryptoSignature\_ParamType type, Crypto\_DataBlob \*value)](#oh_cryptoverify_getparam) | 

Obtains a signature verification parameter.

Note: After the use is complete, the memory for storing the **value** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [void OH\_CryptoVerify\_Destroy(OH\_CryptoVerify \*ctx)](#oh_cryptoverify_destroy) | Destroys a **Verify** instance. |
| [OH\_Crypto\_ErrCode OH\_CryptoSign\_Create(const char \*algoName, OH\_CryptoSign \*\*sign)](#oh_cryptosign_create) | 

Creates a signature instance based on the given algorithm name.

Note: The created resource must be destroyed by calling [OH\_CryptoSign\_Destroy](#oh_cryptosign_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoSign\_Init(OH\_CryptoSign \*ctx, OH\_CryptoPrivKey \*privKey)](#oh_cryptosign_init) | Initializes a signature instance. |
| [OH\_Crypto\_ErrCode OH\_CryptoSign\_Update(OH\_CryptoSign \*ctx, const Crypto\_DataBlob \*in)](#oh_cryptosign_update) | Updates the data to be signed. |
| [OH\_Crypto\_ErrCode OH\_CryptoSign\_Final(OH\_CryptoSign \*ctx, const Crypto\_DataBlob \*in, Crypto\_DataBlob \*out)](#oh_cryptosign_final) | 

Finalizes the signing operation.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [const char \*OH\_CryptoSign\_GetAlgoName(OH\_CryptoSign \*ctx)](#oh_cryptosign_getalgoname) | Obtains the algorithm name of a signature instance. |
| [OH\_Crypto\_ErrCode OH\_CryptoSign\_SetParam(OH\_CryptoSign \*ctx, CryptoSignature\_ParamType type, const Crypto\_DataBlob \*value)](#oh_cryptosign_setparam) | Sets parameters for a signature instance. |
| [OH\_Crypto\_ErrCode OH\_CryptoSign\_GetParam(OH\_CryptoSign \*ctx, CryptoSignature\_ParamType type, Crypto\_DataBlob \*value)](#oh_cryptosign_getparam) | 

Obtains the specified parameter from a signature instance.

Note: After the use is complete, the memory for storing the **value** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [void OH\_CryptoSign\_Destroy(OH\_CryptoSign \*ctx)](#oh_cryptosign_destroy) | Destroys a signature instance. |
| [OH\_Crypto\_ErrCode OH\_CryptoEccSignatureSpec\_Create(Crypto\_DataBlob \*eccSignature, OH\_CryptoEccSignatureSpec \*\*spec)](#oh_cryptoeccsignaturespec_create) | 

Creates ECC signing specifications.

Note: The created resource must be destroyed by calling [OH\_CryptoEccSignatureSpec\_Destroy](#oh_cryptoeccsignaturespec_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoEccSignatureSpec\_GetRAndS(OH\_CryptoEccSignatureSpec \*spec, Crypto\_DataBlob \*r, Crypto\_DataBlob \*s)](#oh_cryptoeccsignaturespec_getrands) | 

Obtains the **r** and **s** values of an ECC signature.

Note: After the use is complete, the memory for storing the **r** and **s** parameters must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoEccSignatureSpec\_SetRAndS(OH\_CryptoEccSignatureSpec \*spec, Crypto\_DataBlob \*r, Crypto\_DataBlob \*s)](#oh_cryptoeccsignaturespec_setrands) | Sets the **r** and **s** values of an ECC signature. |
| [OH\_Crypto\_ErrCode OH\_CryptoEccSignatureSpec\_Encode(OH\_CryptoEccSignatureSpec \*spec, Crypto\_DataBlob \*out)](#oh_cryptoeccsignaturespec_encode) | 

Encodes ECC signing specifications into a signature in DER format.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [void OH\_CryptoEccSignatureSpec\_Destroy(OH\_CryptoEccSignatureSpec \*spec)](#oh_cryptoeccsignaturespec_destroy) | Destroys ECC signing specifications. |

#### Enum Description

#### \[h2\]CryptoSignature\_ParamType

enum CryptoSignature\_ParamType

**Description**

Enumerates the types of signature verification parameters.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| CRYPTO\_PSS\_MD\_NAME\_STR = 100 | MD algorithm used with the PSS padding mode in RSA. |
| CRYPTO\_PSS\_MGF\_NAME\_STR = 101 | Mask generation algorithm used with the PSS padding mode in RSA. Currently, only MGF1 is supported. |
| CRYPTO\_PSS\_MGF1\_NAME\_STR = 102 | MD parameters for the MGF1 mask generation used with the PSS padding mode in RSA. |
| CRYPTO\_PSS\_SALT\_LEN\_INT = 103 | Length of the salt in bytes used with the PSS padding mode in RSA. |
| CRYPTO\_PSS\_TRAILER\_FIELD\_INT = 104 | Trailer field used in the encoding operation when PSS padding mode is used in RSA. The value is **1**. |
| CRYPTO\_SM2\_USER\_ID\_DATABLOB = 105 | User ID field in SM2. |

#### Function Description

#### \[h2\]OH\_CryptoVerify\_Create()

OH\_Crypto\_ErrCode OH\_CryptoVerify\_Create(const char \*algoName, OH\_CryptoVerify \*\*verify)

**Description**

Creates a **Verify** instance for signature verification.

Note: The created resource must be destroyed by calling [OH\_CryptoVerify\_Destroy](#oh_cryptoverify_destroy).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*algoName | 
Pointer to the algorithm used to generate the **Verify** instance.

For example, **RSA1024|PKCS1|SHA256**.

 |
| [OH\_CryptoVerify](../../structs/oh-cryptoverify/document.md) \*\*verify | Pointer to the **Verify** instance created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](../crypto-common-h/document.md#oh_crypto_errcode) | 
**CRYPTO\_SUCCESS**: The operation is successful.

**CRYPTO\_INVALID\_PARAMS**: A parameter is invalid.

**CRYPTO\_NOT\_SUPPORTED**: The operation is not supported.

**CRYPTO\_MEMORY\_ERROR**: A memory error occurs.

**CRYPTO\_OPERATION\_ERROR**: An error occurs when the API of a third-party algorithm library is called.

 |

#### \[h2\]OH\_CryptoVerify\_Init()

OH\_Crypto\_ErrCode OH\_CryptoVerify\_Init(OH\_CryptoVerify \*ctx, OH\_CryptoPubKey \*pubKey)

**Description**

Initializes a **Verify** instance by using the public key.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoVerify](../../structs/oh-cryptoverify/document.md) \*ctx | Pointer to the **Verify** instance. |
| [OH\_CryptoPubKey](../../structs/oh-cryptopubkey/document.md) \*pubKey | Pointer to the public key. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](../crypto-common-h/document.md#oh_crypto_errcode) | 
**CRYPTO\_SUCCESS**: The operation is successful.

**CRYPTO\_INVALID\_PARAMS**: A parameter is invalid.

**CRYPTO\_NOT\_SUPPORTED**: The operation is not supported.

**CRYPTO\_MEMORY\_ERROR**: A memory error occurs.

**CRYPTO\_OPERATION\_ERROR**: An error occurs when the API of a third-party algorithm library is called.

 |

**Reference**

[OH\_CryptoVerify\_Update](#oh_cryptoverify_update)

[OH\_CryptoVerify\_Final](#oh_cryptoverify_final)

#### \[h2\]OH\_CryptoVerify\_Update()

OH\_Crypto\_ErrCode OH\_CryptoVerify\_Update(OH\_CryptoVerify \*ctx, Crypto\_DataBlob \*in)

**Description**

Updates the data to be verified.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoVerify](../../structs/oh-cryptoverify/document.md) \*ctx | Pointer to the **Verify** instance. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*in | Pointer to the data to pass in. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](../crypto-common-h/document.md#oh_crypto_errcode) | 
**CRYPTO\_SUCCESS**: The operation is successful.

**CRYPTO\_INVALID\_PARAMS**: A parameter is invalid.

**CRYPTO\_NOT\_SUPPORTED**: The operation is not supported.

**CRYPTO\_MEMORY\_ERROR**: A memory error occurs.

**CRYPTO\_OPERATION\_ERROR**: An error occurs when the API of a third-party algorithm library is called.

 |

**Reference**

[OH\_CryptoVerify\_Init](#oh_cryptoverify_init)

[OH\_CryptoVerify\_Final](#oh_cryptoverify_final)

#### \[h2\]OH\_CryptoVerify\_Final()

bool OH\_CryptoVerify\_Final(OH\_CryptoVerify \*ctx, Crypto\_DataBlob \*in, Crypto\_DataBlob \*signData)

**Description**

Verifies the signature of the data.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoVerify](../../structs/oh-cryptoverify/document.md) \*ctx | Pointer to the **Verify** instance. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*in | Pointer to the data passed in. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*signData | Pointer to the signature data. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | **true** if the signature verification is successful; **false** otherwise. |

**Reference**

[OH\_CryptoVerify\_Init](#oh_cryptoverify_init)

[OH\_CryptoVerify\_Update](#oh_cryptoverify_update)

#### \[h2\]OH\_CryptoVerify\_Recover()

OH\_Crypto\_ErrCode OH\_CryptoVerify\_Recover(OH\_CryptoVerify \*ctx, Crypto\_DataBlob \*signData, Crypto\_DataBlob \*rawSignData)

**Description**

Restores the raw signature data.

Note: After the use is complete, the memory for storing the **rawSignData** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoVerify](../../structs/oh-cryptoverify/document.md) \*ctx | Pointer to the **Verify** instance. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*signData | Pointer to the signature data. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*rawSignData | Pointer to the raw data restored. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](../crypto-common-h/document.md#oh_crypto_errcode) | 
**CRYPTO\_SUCCESS**: The operation is successful.

**CRYPTO\_INVALID\_PARAMS**: A parameter is invalid.

**CRYPTO\_NOT\_SUPPORTED**: The operation is not supported.

**CRYPTO\_MEMORY\_ERROR**: A memory error occurs.

**CRYPTO\_OPERATION\_ERROR**: An error occurs when the API of a third-party algorithm library is called.

 |

#### \[h2\]OH\_CryptoVerify\_GetAlgoName()

const char \*OH\_CryptoVerify\_GetAlgoName(OH\_CryptoVerify \*ctx)

**Description**

Obtains the signature verification algorithm.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoVerify](../../structs/oh-cryptoverify/document.md) \*ctx | Pointer to the **Verify** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char \* | Signature verification algorithm obtained. |

#### \[h2\]OH\_CryptoVerify\_SetParam()

OH\_Crypto\_ErrCode OH\_CryptoVerify\_SetParam(OH\_CryptoVerify \*ctx, CryptoSignature\_ParamType type, Crypto\_DataBlob \*value)

**Description**

Sets a signature verification parameter.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoVerify](../../structs/oh-cryptoverify/document.md) \*ctx | Pointer to the **Verify** instance. |
| [CryptoSignature\_ParamType](#cryptosignature_paramtype) type | Name of the signature verification parameter to set. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*value | Pointer to the value of the signature verification parameter to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](../crypto-common-h/document.md#oh_crypto_errcode) | 
**CRYPTO\_SUCCESS**: The operation is successful.

**CRYPTO\_INVALID\_PARAMS**: A parameter is invalid.

**CRYPTO\_NOT\_SUPPORTED**: The operation is not supported.

**CRYPTO\_MEMORY\_ERROR**: A memory error occurs.

**CRYPTO\_OPERATION\_ERROR**: An error occurs when the API of a third-party algorithm library is called.

 |

#### \[h2\]OH\_CryptoVerify\_GetParam()

OH\_Crypto\_ErrCode OH\_CryptoVerify\_GetParam(OH\_CryptoVerify \*ctx, CryptoSignature\_ParamType type, Crypto\_DataBlob \*value)

**Description**

Obtains a signature verification parameter.

Note: After the use is complete, the memory for storing the **value** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoVerify](../../structs/oh-cryptoverify/document.md) \*ctx | Pointer to the **Verify** instance. |
| [CryptoSignature\_ParamType](#cryptosignature_paramtype) type | Name of the signature verification parameter to obtain. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*value | Pointer to the parameter value obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode](../crypto-common-h/document.md#oh_crypto_errcode) | 
**CRYPTO\_SUCCESS**: The operation is successful.

**CRYPTO\_INVALID\_PARAMS**: A parameter is invalid.

**CRYPTO\_NOT\_SUPPORTED**: The operation is not supported.

**CRYPTO\_MEMORY\_ERROR**: A memory error occurs.

**CRYPTO\_OPERATION\_ERROR**: An error occurs when the API of a third-party algorithm library is called.

 |

#### \[h2\]OH\_CryptoVerify\_Destroy()

void OH\_CryptoVerify\_Destroy(OH\_CryptoVerify \*ctx)

**Description**

Destroys a **Verify** instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoVerify](../../structs/oh-cryptoverify/document.md) \*ctx | Pointer to the **Verify** instance. |

#### \[h2\]OH\_CryptoSign\_Create()

OH\_Crypto\_ErrCode OH\_CryptoSign\_Create(const char \*algoName, OH\_CryptoSign \*\*sign)

**Description**

Creates a signature instance based on the given algorithm name.

Note: The created resource must be destroyed by calling [OH\_CryptoSign\_Destroy](#oh_cryptosign_destroy).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*algoName | 
Pointer to the algorithm used to generate the signature instance.

For example, **RSA|PKCS1|SHA384** or **ECC|SHA384**.

 |
| [OH\_CryptoSign](../../structs/oh-cryptosign/document.md) \*\*sign | Pointer to the signature instance. |

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

#### \[h2\]OH\_CryptoSign\_Init()

OH\_Crypto\_ErrCode OH\_CryptoSign\_Init(OH\_CryptoSign \*ctx, OH\_CryptoPrivKey \*privKey)

**Description**

Initializes a signature instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoSign](../../structs/oh-cryptosign/document.md) \*ctx | Pointer to the signature instance. |
| [OH\_CryptoPrivKey](../../structs/oh-cryptoprivkey/document.md) \*privKey | Pointer to the private key. |

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

[OH\_CryptoSign\_Update](#oh_cryptosign_update)

[OH\_CryptoSign\_Final](#oh_cryptosign_final)

#### \[h2\]OH\_CryptoSign\_Update()

OH\_Crypto\_ErrCode OH\_CryptoSign\_Update(OH\_CryptoSign \*ctx, const Crypto\_DataBlob \*in)

**Description**

Updates the data to be signed.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoSign](../../structs/oh-cryptosign/document.md) \*ctx | Pointer to the signature instance. |
| [const Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*in | Pointer to the data to be signed. |

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

[OH\_CryptoSign\_Init](#oh_cryptosign_init)

[OH\_CryptoSign\_Final](#oh_cryptosign_final)

#### \[h2\]OH\_CryptoSign\_Final()

OH\_Crypto\_ErrCode OH\_CryptoSign\_Final(OH\_CryptoSign \*ctx, const Crypto\_DataBlob \*in, Crypto\_DataBlob \*out)

**Description**

Finalizes the signing operation.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoSign](../../structs/oh-cryptosign/document.md) \*ctx | Pointer to the signature instance. |
| [const Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*in | Pointer to the data to be signed. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*out | Pointer to the signing result. |

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

[OH\_CryptoSign\_Init](#oh_cryptosign_init)

[OH\_CryptoSign\_Update](#oh_cryptosign_update)

#### \[h2\]OH\_CryptoSign\_GetAlgoName()

const char \*OH\_CryptoSign\_GetAlgoName(OH\_CryptoSign \*ctx)

**Description**

Obtains the algorithm name of a signature instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoSign](../../structs/oh-cryptosign/document.md) \*ctx | Pointer to the signature instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char \* | Algorithm name of the signature instance. |

#### \[h2\]OH\_CryptoSign\_SetParam()

OH\_Crypto\_ErrCode OH\_CryptoSign\_SetParam(OH\_CryptoSign \*ctx, CryptoSignature\_ParamType type, const Crypto\_DataBlob \*value)

**Description**

Sets parameters for a signature instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoSign](../../structs/oh-cryptosign/document.md) \*ctx | Pointer to the signature instance. |
| [CryptoSignature\_ParamType](#cryptosignature_paramtype) type | Pointer to the signature parameter type. |
| [const Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*value | Pointer to the input data. |

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

#### \[h2\]OH\_CryptoSign\_GetParam()

OH\_Crypto\_ErrCode OH\_CryptoSign\_GetParam(OH\_CryptoSign \*ctx, CryptoSignature\_ParamType type, Crypto\_DataBlob \*value)

**Description**

Obtains the specified parameter from a signature instance.

Note: After the use is complete, the memory for storing the **value** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoSign](../../structs/oh-cryptosign/document.md) \*ctx | Pointer to the signature instance. |
| [CryptoSignature\_ParamType](#cryptosignature_paramtype) type | Pointer to the signature parameter type. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*value | Pointer to the output data. |

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

#### \[h2\]OH\_CryptoSign\_Destroy()

void OH\_CryptoSign\_Destroy(OH\_CryptoSign \*ctx)

**Description**

Destroys a signature instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoSign](../../structs/oh-cryptosign/document.md) \*ctx | Pointer to the signature instance. |

#### \[h2\]OH\_CryptoEccSignatureSpec\_Create()

OH\_Crypto\_ErrCode OH\_CryptoEccSignatureSpec\_Create(Crypto\_DataBlob \*eccSignature, OH\_CryptoEccSignatureSpec \*\*spec)

**Description**

Creates ECC signing specifications.

Note: The created resource must be destroyed by calling [OH\_CryptoEccSignatureSpec\_Destroy](#oh_cryptoeccsignaturespec_destroy).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*eccSignature | Pointer to the ECC signature (in DER format). If **EccSignature** is **NULL**, an empty ECC signing specification is created. |
| [OH\_CryptoEccSignatureSpec](../../structs/oh-cryptoeccsignaturespec/document.md) \*\*spec | Pointer to the ECC signing specifications. |

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

#### \[h2\]OH\_CryptoEccSignatureSpec\_GetRAndS()

OH\_Crypto\_ErrCode OH\_CryptoEccSignatureSpec\_GetRAndS(OH\_CryptoEccSignatureSpec \*spec, Crypto\_DataBlob \*r, Crypto\_DataBlob \*s)

**Description**

Obtains the **r** and **s** values of an ECC signature.

Note: After the use is complete, the memory for storing the **r** and **s** parameters must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoEccSignatureSpec](../../structs/oh-cryptoeccsignaturespec/document.md) \*spec | Pointer to the ECC signing specifications. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*r | Pointer to the **r** value. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*s | Pointer to the **s** value. |

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

#### \[h2\]OH\_CryptoEccSignatureSpec\_SetRAndS()

OH\_Crypto\_ErrCode OH\_CryptoEccSignatureSpec\_SetRAndS(OH\_CryptoEccSignatureSpec \*spec, Crypto\_DataBlob \*r, Crypto\_DataBlob \*s)

**Description**

Sets the **r** and **s** values of an ECC signature.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoEccSignatureSpec](../../structs/oh-cryptoeccsignaturespec/document.md) \*spec | Pointer to the ECC signing specifications. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*r | Pointer to the **r** value. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*s | Pointer to the **s** value. |

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

#### \[h2\]OH\_CryptoEccSignatureSpec\_Encode()

OH\_Crypto\_ErrCode OH\_CryptoEccSignatureSpec\_Encode(OH\_CryptoEccSignatureSpec \*spec, Crypto\_DataBlob \*out)

**Description**

Encodes ECC signing specifications into a signature in DER format.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoEccSignatureSpec](../../structs/oh-cryptoeccsignaturespec/document.md) \*spec | Pointer to the ECC signing specifications. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*out | Pointer to the output data. |

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

#### \[h2\]OH\_CryptoEccSignatureSpec\_Destroy()

void OH\_CryptoEccSignatureSpec\_Destroy(OH\_CryptoEccSignatureSpec \*spec)

**Description**

Destroys ECC signing specifications.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoEccSignatureSpec](../../structs/oh-cryptoeccsignaturespec/document.md) \*spec | Pointer to the ECC signing specifications. |
