# crypto\_asym\_key.h

#### Overview

Defines APIs for asymmetric keys.

**Header file**: <CryptoArchitectureKit/crypto\_asym\_key.h>

**Library**: libohcrypto.so

**System capability**: SystemCapability.Security.CryptoFramework

**Since**: 12

**Related module**: [CryptoAsymKeyApi](../../modules/cryptoasymkeyapi/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_CryptoKeyPair](../../structs/oh-cryptokeypair/document.md) | OH\_CryptoKeyPair | Defines a struct for an asymmetric key pair. |
| [OH\_CryptoPubKey](../../structs/oh-cryptopubkey/document.md) | OH\_CryptoPubKey | Defines a struct for the public key in an asymmetric key pair. |
| [OH\_CryptoPrivKey](../../structs/oh-cryptoprivkey/document.md) | OH\_CryptoPrivKey | Defines a struct for a private key. |
| [OH\_CryptoAsymKeyGenerator](../../structs/oh-cryptoasymkeygenerator/document.md) | OH\_CryptoAsymKeyGenerator | Defines a struct for an asymmetric key generator. |
| [OH\_CryptoPrivKeyEncodingParams](../../structs/oh-cryptoprivkeyencodingparams/document.md) | OH\_CryptoPrivKeyEncodingParams | Defines a struct for private key encoding parameters. |
| [OH\_CryptoAsymKeySpec](../../structs/oh-cryptoasymkeyspec/document.md) | OH\_CryptoAsymKeySpec | Defines a struct for asymmetric key specifications. |
| [OH\_CryptoAsymKeyGeneratorWithSpec](../../structs/oh-cryptoasymkeygeneratorwithspec/document.md) | OH\_CryptoAsymKeyGeneratorWithSpec | Defines a struct for an asymmetric key generator with specifications. |
| [OH\_CryptoEcPoint](../../structs/oh-cryptoecpoint/document.md) | OH\_CryptoEcPoint | Defines a struct for an EC point. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [CryptoAsymKey\_ParamType](#cryptoasymkey_paramtype) | CryptoAsymKey\_ParamType | Enumerates the types of the asymmetric key parameters. |
| [Crypto\_EncodingType](#crypto_encodingtype) | Crypto\_EncodingType | Enumerates the encoding types. |
| [CryptoPrivKeyEncoding\_ParamType](#cryptoprivkeyencoding_paramtype) | CryptoPrivKeyEncoding\_ParamType | Defines the parameter type for private key encoding. |
| [CryptoAsymKeySpec\_Type](#cryptoasymkeyspec_type) | CryptoAsymKeySpec\_Type | Defines the specification type of an asymmetric key. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeyGenerator\_Create(const char \*algoName, OH\_CryptoAsymKeyGenerator \*\*ctx)](#oh_cryptoasymkeygenerator_create) | 
Creates an asymmetric key generator instance based on the specified algorithm.

Note: The created resource must be destroyed by calling [OH\_CryptoAsymKeyGenerator\_Destroy](#oh_cryptoasymkeygenerator_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeyGenerator\_Generate(OH\_CryptoAsymKeyGenerator \*ctx, OH\_CryptoKeyPair \*\*keyCtx)](#oh_cryptoasymkeygenerator_generate) | 

Randomly generates an asymmetric key pair.

Note: After the use is complete, the memory for storing the **keyCtx** parameter must be destroyed by calling [OH\_CryptoKeyPair\_Destroy](#oh_cryptokeypair_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeyGenerator\_Convert(OH\_CryptoAsymKeyGenerator \*ctx, Crypto\_EncodingType type, Crypto\_DataBlob \*pubKeyData, Crypto\_DataBlob \*priKeyData, OH\_CryptoKeyPair \*\*keyCtx)](#oh_cryptoasymkeygenerator_convert) | 

Converts asymmetric key data into a key pair.

Note: After the use is complete, the memory for storing the **keyCtx** parameter must be destroyed by calling [OH\_CryptoKeyPair\_Destroy](#oh_cryptokeypair_destroy).

 |
| [const char \*OH\_CryptoAsymKeyGenerator\_GetAlgoName(OH\_CryptoAsymKeyGenerator \*ctx)](#oh_cryptoasymkeygenerator_getalgoname) | Obtains the asymmetric key algorithm. |
| [void OH\_CryptoAsymKeyGenerator\_Destroy(OH\_CryptoAsymKeyGenerator \*ctx)](#oh_cryptoasymkeygenerator_destroy) | Destroys an asymmetric key generator instance. |
| [void OH\_CryptoKeyPair\_Destroy(OH\_CryptoKeyPair \*keyCtx)](#oh_cryptokeypair_destroy) | Destroys an asymmetric key pair instance. |
| [OH\_CryptoPubKey \*OH\_CryptoKeyPair\_GetPubKey(OH\_CryptoKeyPair \*keyCtx)](#oh_cryptokeypair_getpubkey) | Obtains the public key instance from a key pair. |
| [OH\_CryptoPrivKey \*OH\_CryptoKeyPair\_GetPrivKey(OH\_CryptoKeyPair \*keyCtx)](#oh_cryptokeypair_getprivkey) | Obtains the private key of a key pair. |
| [OH\_Crypto\_ErrCode OH\_CryptoPubKey\_Encode(OH\_CryptoPubKey \*key, Crypto\_EncodingType type, const char \*encodingStandard, Crypto\_DataBlob \*out)](#oh_cryptopubkey_encode) | 

Encodes the public key data in the specified format.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoPubKey\_GetParam(OH\_CryptoPubKey \*key, CryptoAsymKey\_ParamType item, Crypto\_DataBlob \*value)](#oh_cryptopubkey_getparam) | 

Obtains the specified parameter from a public key instance.

Note: After the use is complete, the memory for storing the **value** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeyGenerator\_SetPassword(OH\_CryptoAsymKeyGenerator \*ctx, const unsigned char \*password, uint32\_t passwordLen)](#oh_cryptoasymkeygenerator_setpassword) | Sets the password of the asymmetric key generator context. |
| [OH\_Crypto\_ErrCode OH\_CryptoPrivKeyEncodingParams\_Create(OH\_CryptoPrivKeyEncodingParams \*\*ctx)](#oh_cryptoprivkeyencodingparams_create) | 

Creates private key encoding parameters.

Note: The created resource must be destroyed by calling [OH\_CryptoPrivKeyEncodingParams\_Destroy](#oh_cryptoprivkeyencodingparams_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoPrivKeyEncodingParams\_SetParam(OH\_CryptoPrivKeyEncodingParams \*ctx, CryptoPrivKeyEncoding\_ParamType type, Crypto\_DataBlob \*value)](#oh_cryptoprivkeyencodingparams_setparam) | Sets a private key encoding parameter. |
| [void OH\_CryptoPrivKeyEncodingParams\_Destroy(OH\_CryptoPrivKeyEncodingParams \*ctx)](#oh_cryptoprivkeyencodingparams_destroy) | Destroys a private key encoding parameter. |
| [OH\_Crypto\_ErrCode OH\_CryptoPrivKey\_Encode(OH\_CryptoPrivKey \*key, Crypto\_EncodingType type, const char \*encodingStandard, OH\_CryptoPrivKeyEncodingParams \*params, Crypto\_DataBlob \*out)](#oh_cryptoprivkey_encode) | 

Obtains the specified parameter from a private key instance.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoPrivKey\_GetParam(OH\_CryptoPrivKey \*key, CryptoAsymKey\_ParamType item, Crypto\_DataBlob \*value)](#oh_cryptoprivkey_getparam) | 

Obtains the specified parameter of a private key.

Note: After the use is complete, the memory for storing the **value** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeySpec\_GenEcCommonParamsSpec(const char \*curveName, OH\_CryptoAsymKeySpec \*\*spec)](#oh_cryptoasymkeyspec_geneccommonparamsspec) | 

Generates EC common parameter specifications.

Note: After the use is complete, the memory for storing the **spec** parameter must be destroyed by calling [OH\_CryptoAsymKeySpec\_Destroy](#oh_cryptoasymkeyspec_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeySpec\_GenDhCommonParamsSpec(int pLen, int skLen, OH\_CryptoAsymKeySpec \*\*spec)](#oh_cryptoasymkeyspec_gendhcommonparamsspec) | 

Generates DH common parameter specifications.

Note: After the use is complete, the memory for storing the **spec** parameter must be destroyed by calling [OH\_CryptoAsymKeySpec\_Destroy](#oh_cryptoasymkeyspec_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeySpec\_Create(const char \*algoName, CryptoAsymKeySpec\_Type type, OH\_CryptoAsymKeySpec \*\*spec)](#oh_cryptoasymkeyspec_create) | 

Creates asymmetric key specifications based on the given algorithm name and specification type.

Note: The created resource must be destroyed by calling [OH\_CryptoAsymKeySpec\_Destroy](#oh_cryptoasymkeyspec_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeySpec\_SetParam(OH\_CryptoAsymKeySpec \*spec, CryptoAsymKey\_ParamType type, Crypto\_DataBlob \*value)](#oh_cryptoasymkeyspec_setparam) | Sets the specified parameters for asymmetric key specifications. |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeySpec\_SetCommonParamsSpec(OH\_CryptoAsymKeySpec \*spec, OH\_CryptoAsymKeySpec \*commonParamsSpec)](#oh_cryptoasymkeyspec_setcommonparamsspec) | Sets the common parameter specifications for asymmetric key specifications. |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeySpec\_GetParam(OH\_CryptoAsymKeySpec \*spec, CryptoAsymKey\_ParamType type, Crypto\_DataBlob \*value)](#oh_cryptoasymkeyspec_getparam) | 

Obtains the specified parameters for asymmetric key specifications.

Note: After the use is complete, the memory for storing the **value** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [void OH\_CryptoAsymKeySpec\_Destroy(OH\_CryptoAsymKeySpec \*spec)](#oh_cryptoasymkeyspec_destroy) | Destroys asymmetric key specifications. |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeyGeneratorWithSpec\_Create(OH\_CryptoAsymKeySpec \*keySpec, OH\_CryptoAsymKeyGeneratorWithSpec \*\*generator)](#oh_cryptoasymkeygeneratorwithspec_create) | 

Creates a struct for an asymmetric key generator with specifications.

Note: The created resource must be destroyed by calling [OH\_CryptoAsymKeyGeneratorWithSpec\_Destroy](#oh_cryptoasymkeygeneratorwithspec_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeyGeneratorWithSpec\_GenKeyPair(OH\_CryptoAsymKeyGeneratorWithSpec \*generator, OH\_CryptoKeyPair \*\*keyPair)](#oh_cryptoasymkeygeneratorwithspec_genkeypair) | 

Generates a key pair based on asymmetric key specifications.

Note: After the use is complete, the memory for storing the **keyPair** parameter must be released by calling [OH\_CryptoKeyPair\_Destroy](#oh_cryptokeypair_destroy).

 |
| [void OH\_CryptoAsymKeyGeneratorWithSpec\_Destroy(OH\_CryptoAsymKeyGeneratorWithSpec \*generator)](#oh_cryptoasymkeygeneratorwithspec_destroy) | Destroys a struct for an asymmetric key generator with specifications. |
| [OH\_Crypto\_ErrCode OH\_CryptoEcPoint\_Create(const char \*curveName, Crypto\_DataBlob \*ecKeyData, OH\_CryptoEcPoint \*\*point)](#oh_cryptoecpoint_create) | 

Creates an EC point.

Note: The created resource must be destroyed by calling [OH\_CryptoEcPoint\_Destroy](#oh_cryptoecpoint_destroy).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoEcPoint\_GetCoordinate(OH\_CryptoEcPoint \*point, Crypto\_DataBlob \*x, Crypto\_DataBlob \*y)](#oh_cryptoecpoint_getcoordinate) | 

Obtains the X and Y coordinates of an EC point.

Note: After the use is complete, the memory for storing the **x** and **y** parameters must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [OH\_Crypto\_ErrCode OH\_CryptoEcPoint\_SetCoordinate(OH\_CryptoEcPoint \*point, Crypto\_DataBlob \*x, Crypto\_DataBlob \*y)](#oh_cryptoecpoint_setcoordinate) | Sets the X and Y coordinates of an EC point. |
| [OH\_Crypto\_ErrCode OH\_CryptoEcPoint\_Encode(OH\_CryptoEcPoint \*point, const char \*format, Crypto\_DataBlob \*out)](#oh_cryptoecpoint_encode) | 

Encodes an EC point in a specified format.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

 |
| [void OH\_CryptoEcPoint\_Destroy(OH\_CryptoEcPoint \*point)](#oh_cryptoecpoint_destroy) | Destroys an EC point. |

#### Enum Description

#### \[h2\]CryptoAsymKey\_ParamType

enum CryptoAsymKey\_ParamType

**Description**

Enumerates the types of the asymmetric key parameters.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| CRYPTO\_DSA\_P\_DATABLOB = 101 | Prime modulus **p** in the DSA algorithm. |
| CRYPTO\_DSA\_Q\_DATABLOB = 102 | Parameter **q**, prime factor of (p – 1) in the DSA algorithm. |
| CRYPTO\_DSA\_G\_DATABLOB = 103 | Parameter **g** in the DSA algorithm. |
| CRYPTO\_DSA\_SK\_DATABLOB = 104 | Private key **sk** in the DSA algorithm. |
| CRYPTO\_DSA\_PK\_DATABLOB = 105 | Public key **pk** in the DSA algorithm. |
| CRYPTO\_ECC\_FP\_P\_DATABLOB = 201 | Prime number **p** in the **Fp** field of the elliptic curve in the ECC algorithm. |
| CRYPTO\_ECC\_A\_DATABLOB = 202 | First coefficient **a** of the elliptic curve in the ECC algorithm. |
| CRYPTO\_ECC\_B\_DATABLOB = 203 | Second coefficient **b** of the elliptic curve in the ECC algorithm. |
| CRYPTO\_ECC\_G\_X\_DATABLOB = 204 | X coordinate of the base point **g** in the ECC algorithm. |
| CRYPTO\_ECC\_G\_Y\_DATABLOB = 205 | Y coordinate of the base point **g** in the ECC algorithm. |
| CRYPTO\_ECC\_N\_DATABLOB = 206 | Order **n** of the base point **g** in the ECC algorithm. |
| CRYPTO\_ECC\_H\_INT = 207 | Cofactor **h** in the ECC algorithm. |
| CRYPTO\_ECC\_SK\_DATABLOB = 208 | Private key **sk** in the ECC algorithm. |
| CRYPTO\_ECC\_PK\_X\_DATABLOB = 209 | X coordinate of the public key **pk** (a point on the elliptic curve) in the ECC algorithm. |
| CRYPTO\_ECC\_PK\_Y\_DATABLOB = 210 | Y coordinate of the public key **pk** (a point on the elliptic curve) in the ECC algorithm. |
| CRYPTO\_ECC\_FIELD\_TYPE\_STR = 211 | Elliptic curve field type in the ECC algorithm. Currently, only the **Fp** field is supported. |
| CRYPTO\_ECC\_FIELD\_SIZE\_INT = 212 | 
Size of the field in the ECC algorithm, in bits.

Note: The size of the **Fp** field is the length of the prime **p**, in bits.

 |
| CRYPTO\_ECC\_CURVE\_NAME\_STR = 213 | Standards for Efficient Cryptography Group (SECG) curve name in the ECC algorithm. |
| CRYPTO\_RSA\_N\_DATABLOB = 301 | Modulus **n** in the RSA algorithm. |
| CRYPTO\_RSA\_D\_DATABLOB = 302 | Private key **sk** (private key exponent **d**) in the RSA algorithm. |
| CRYPTO\_RSA\_E\_DATABLOB = 303 | Public key **pk** (public key exponent **e**) in the RSA algorithm. |
| CRYPTO\_DH\_P\_DATABLOB = 401 | Prime **p** in the DH algorithm. |
| CRYPTO\_DH\_G\_DATABLOB = 402 | Parameter **g** in the DH algorithm. |
| CRYPTO\_DH\_L\_INT = 403 | Length of the private key in the DH algorithm, in bits. |
| CRYPTO\_DH\_SK\_DATABLOB = 404 | Private key **sk** in the DH algorithm. |
| CRYPTO\_DH\_PK\_DATABLOB = 405 | Public key **pk** in the DH algorithm. |
| CRYPTO\_ED25519\_SK\_DATABLOB = 501 | Private key **sk** in the Ed25519 algorithm. |
| CRYPTO\_ED25519\_PK\_DATABLOB = 502 | Public key **pk** in the Ed25519 algorithm. |
| CRYPTO\_X25519\_SK\_DATABLOB = 601 | Private key **sk** in the X25519 algorithm. |
| CRYPTO\_X25519\_PK\_DATABLOB = 602 | Public key **pk** in the X25519 algorithm. |

#### \[h2\]Crypto\_EncodingType

enum Crypto\_EncodingType

**Description**

Enumerates the encoding types.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| CRYPTO\_PEM = 0 | PEM. |
| CRYPTO\_DER = 1 | DER. |

#### \[h2\]CryptoPrivKeyEncoding\_ParamType

enum CryptoPrivKeyEncoding\_ParamType

**Description**

Defines the parameter type for private key encoding.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| CRYPTO\_PRIVATE\_KEY\_ENCODING\_PASSWORD\_STR = 0 | Password string. |
| CRYPTO\_PRIVATE\_KEY\_ENCODING\_SYMMETRIC\_CIPHER\_STR = 1 | Symmetric cipher string. |

#### \[h2\]CryptoAsymKeySpec\_Type

enum CryptoAsymKeySpec\_Type

**Description**

Defines the specification type of an asymmetric key.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| CRYPTO\_ASYM\_KEY\_COMMON\_PARAMS\_SPEC = 0 | Common parameter specifications. |
| CRYPTO\_ASYM\_KEY\_PRIVATE\_KEY\_SPEC = 1 | Private key specifications. |
| CRYPTO\_ASYM\_KEY\_PUBLIC\_KEY\_SPEC = 2 | Public key specifications. |
| CRYPTO\_ASYM\_KEY\_KEY\_PAIR\_SPEC = 3 | Key pair specifications. |

#### Function Description

#### \[h2\]OH\_CryptoAsymKeyGenerator\_Create()

OH\_Crypto\_ErrCode OH\_CryptoAsymKeyGenerator\_Create(const char \*algoName, OH\_CryptoAsymKeyGenerator \*\*ctx)

**Description**

Creates an asymmetric key generator instance based on the specified algorithm.

Note: The created resource must be destroyed by calling [OH\_CryptoAsymKeyGenerator\_Destroy](#oh_cryptoasymkeygenerator_destroy).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*algoName | 
Pointer the algorithm used to create a generator.

For example, **RSA1024|PRIMES\_2**.

 |
| [OH\_CryptoAsymKeyGenerator](../../structs/oh-cryptoasymkeygenerator/document.md) \*\*ctx | Pointer to the asymmetric key generator context created. |

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

#### \[h2\]OH\_CryptoAsymKeyGenerator\_Generate()

OH\_Crypto\_ErrCode OH\_CryptoAsymKeyGenerator\_Generate(OH\_CryptoAsymKeyGenerator \*ctx, OH\_CryptoKeyPair \*\*keyCtx)

**Description**

Randomly generates an asymmetric key pair.

Note: After the use is complete, the memory for storing the **keyCtx** parameter must be destroyed by calling [OH\_CryptoKeyPair\_Destroy](#oh_cryptokeypair_destroy).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoAsymKeyGenerator](../../structs/oh-cryptoasymkeygenerator/document.md) \*ctx | Pointer to the asymmetric key generator instance. |
| [OH\_CryptoKeyPair](../../structs/oh-cryptokeypair/document.md) \*\*keyCtx | Pointer to the asymmetric key pair instance. |

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

#### \[h2\]OH\_CryptoAsymKeyGenerator\_Convert()

OH\_Crypto\_ErrCode OH\_CryptoAsymKeyGenerator\_Convert(OH\_CryptoAsymKeyGenerator \*ctx, Crypto\_EncodingType type, Crypto\_DataBlob \*pubKeyData, Crypto\_DataBlob \*priKeyData, OH\_CryptoKeyPair \*\*keyCtx)

**Description**

Converts asymmetric key data into a key pair.

Note: After the use is complete, the memory for storing the **keyCtx** parameter must be destroyed by calling [OH\_CryptoKeyPair\_Destroy](#oh_cryptokeypair_destroy).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoAsymKeyGenerator](../../structs/oh-cryptoasymkeygenerator/document.md) \*ctx | Pointer to the asymmetric key generator instance. |
| [Crypto\_EncodingType](#crypto_encodingtype) type | Encoding type. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*pubKeyData | Pointer to the public key data to convert. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*priKeyData | Pointer to the private key data to convert. |
| [OH\_CryptoKeyPair](../../structs/oh-cryptokeypair/document.md) \*\*keyCtx | Pointer to the asymmetric key pair instance. |

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

#### \[h2\]OH\_CryptoAsymKeyGenerator\_GetAlgoName()

const char \*OH\_CryptoAsymKeyGenerator\_GetAlgoName(OH\_CryptoAsymKeyGenerator \*ctx)

**Description**

Obtains the asymmetric key algorithm.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoAsymKeyGenerator](../../structs/oh-cryptoasymkeygenerator/document.md) \*ctx | Pointer to the asymmetric key generator instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char \* | Name of the asymmetric key algorithm obtained. |

#### \[h2\]OH\_CryptoAsymKeyGenerator\_Destroy()

void OH\_CryptoAsymKeyGenerator\_Destroy(OH\_CryptoAsymKeyGenerator \*ctx)

**Description**

Destroys an asymmetric key generator instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoAsymKeyGenerator](../../structs/oh-cryptoasymkeygenerator/document.md) \*ctx | Pointer to the asymmetric key generator instance. |

#### \[h2\]OH\_CryptoKeyPair\_Destroy()

void OH\_CryptoKeyPair\_Destroy(OH\_CryptoKeyPair \*keyCtx)

**Description**

Destroys an asymmetric key pair instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoKeyPair](../../structs/oh-cryptokeypair/document.md) \*keyCtx | Pointer to the key pair instance. |

#### \[h2\]OH\_CryptoKeyPair\_GetPubKey()

OH\_CryptoPubKey \*OH\_CryptoKeyPair\_GetPubKey(OH\_CryptoKeyPair \*keyCtx)

**Description**

Obtains the public key from a key pair.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoKeyPair](../../structs/oh-cryptokeypair/document.md) \*keyCtx | Pointer to the key pair instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_CryptoPubKey](../../structs/oh-cryptopubkey/document.md) \* | Public key obtained. |

#### \[h2\]OH\_CryptoKeyPair\_GetPrivKey()

OH\_CryptoPrivKey \*OH\_CryptoKeyPair\_GetPrivKey(OH\_CryptoKeyPair \*keyCtx)

**Description**

Obtains the private key of a key pair.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoKeyPair](../../structs/oh-cryptokeypair/document.md) \*keyCtx | Pointer to the key pair instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_CryptoPrivKey](../../structs/oh-cryptoprivkey/document.md) \* | Private key obtained. |

#### \[h2\]OH\_CryptoPubKey\_Encode()

OH\_Crypto\_ErrCode OH\_CryptoPubKey\_Encode(OH\_CryptoPubKey \*key, Crypto\_EncodingType type, const char \*encodingStandard, Crypto\_DataBlob \*out)

**Description**

Encodes the public key data in the specified format.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoPubKey](../../structs/oh-cryptopubkey/document.md) \*key | Ponter to the public key data. |
| [Crypto\_EncodingType](#crypto_encodingtype) type | Encoding type. |
| const char \*encodingStandard | Encoding type. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*out | Pointer to the public key encoded in the specified format. |

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

#### \[h2\]OH\_CryptoPubKey\_GetParam()

OH\_Crypto\_ErrCode OH\_CryptoPubKey\_GetParam(OH\_CryptoPubKey \*key, CryptoAsymKey\_ParamType item, Crypto\_DataBlob \*value)

**Description**

Obtains the specified parameter from a public key instance.

Note: After the use is complete, the memory for storing the **value** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoPubKey](../../structs/oh-cryptopubkey/document.md) \*key | Ponter to the public key data. |
| [CryptoAsymKey\_ParamType](#cryptoasymkey_paramtype) item | Type of the asymmetric key parameter to obtain. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*value | Pointer to the parameter value obtained. |

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

#### \[h2\]OH\_CryptoAsymKeyGenerator\_SetPassword()

OH\_Crypto\_ErrCode OH\_CryptoAsymKeyGenerator\_SetPassword(OH\_CryptoAsymKeyGenerator \*ctx, const unsigned char \*password, uint32\_t passwordLen)

**Description**

Sets the password of the asymmetric key generator context.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoAsymKeyGenerator](../../structs/oh-cryptoasymkeygenerator/document.md) \*ctx | Pointer to the asymmetric encryption context. |
| const unsigned char \*password | Pointer to the password. |
| uint32\_t passwordLen | Password length. |

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

#### \[h2\]OH\_CryptoPrivKeyEncodingParams\_Create()

OH\_Crypto\_ErrCode OH\_CryptoPrivKeyEncodingParams\_Create(OH\_CryptoPrivKeyEncodingParams \*\*ctx)

**Description**

Creates private key encoding parameters.

Note: The created resource must be destroyed by calling [OH\_CryptoPrivKeyEncodingParams\_Destroy](#oh_cryptoprivkeyencodingparams_destroy).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoPrivKeyEncodingParams](../../structs/oh-cryptoprivkeyencodingparams/document.md) \*\*ctx | Pointer to the private key encoding parameters. |

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

#### \[h2\]OH\_CryptoPrivKeyEncodingParams\_SetParam()

OH\_Crypto\_ErrCode OH\_CryptoPrivKeyEncodingParams\_SetParam(OH\_CryptoPrivKeyEncodingParams \*ctx, CryptoPrivKeyEncoding\_ParamType type, Crypto\_DataBlob \*value)

**Description**

Sets a private key encoding parameter.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoPrivKeyEncodingParams](../../structs/oh-cryptoprivkeyencodingparams/document.md) \*ctx | Pointer to the private key encoding parameters. |
| [CryptoPrivKeyEncoding\_ParamType](#cryptoprivkeyencoding_paramtype) type | Parameter type for private key encoding. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*value | Pointer to the parameter values for private key encoding. |

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

#### \[h2\]OH\_CryptoPrivKeyEncodingParams\_Destroy()

void OH\_CryptoPrivKeyEncodingParams\_Destroy(OH\_CryptoPrivKeyEncodingParams \*ctx)

**Description**

Destroys a private key encoding parameter.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoPrivKeyEncodingParams](../../structs/oh-cryptoprivkeyencodingparams/document.md) \*ctx | Pointer to the private key encoding parameters. |

#### \[h2\]OH\_CryptoPrivKey\_Encode()

OH\_Crypto\_ErrCode OH\_CryptoPrivKey\_Encode(OH\_CryptoPrivKey \*key, Crypto\_EncodingType type, const char \*encodingStandard, OH\_CryptoPrivKeyEncodingParams \*params, Crypto\_DataBlob \*out)

**Description**

Obtains the specified parameter from a private key instance.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoPrivKey](../../structs/oh-cryptoprivkey/document.md) \*key | Pointer to the private key. |
| [Crypto\_EncodingType](#crypto_encodingtype) type | Private key encoding type. |
| const char \*encodingStandard | 
Pointer to the encoding standard,

for example, **PKCS8**.

 |
| [OH\_CryptoPrivKeyEncodingParams](../../structs/oh-cryptoprivkeyencodingparams/document.md) \*params | Pointer to the private key encoding parameters, which can be **NULL**. Set this parameter if you need to encrypt a private key. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*out | Pointer to the encoding output. |

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

#### \[h2\]OH\_CryptoPrivKey\_GetParam()

OH\_Crypto\_ErrCode OH\_CryptoPrivKey\_GetParam(OH\_CryptoPrivKey \*key, CryptoAsymKey\_ParamType item, Crypto\_DataBlob \*value)

**Description**

Obtains the specified parameter of a private key.

Note: After the use is complete, the memory for storing the **value** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoPrivKey](../../structs/oh-cryptoprivkey/document.md) \*key | Pointer to the private key. |
| [CryptoAsymKey\_ParamType](#cryptoasymkey_paramtype) item | Type of the asymmetric key parameter to obtain. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*value | Pointer to the output data. |

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

#### \[h2\]OH\_CryptoAsymKeySpec\_GenEcCommonParamsSpec()

OH\_Crypto\_ErrCode OH\_CryptoAsymKeySpec\_GenEcCommonParamsSpec(const char \*curveName, OH\_CryptoAsymKeySpec \*\*spec)

**Description**

Generates EC common parameter specifications.

Note: After the use is complete, the memory for storing the **spec** parameter must be destroyed by calling [OH\_CryptoAsymKeySpec\_Destroy](#oh_cryptoasymkeyspec_destroy).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*curveName | Pointer to the ECC curve name. |
| [OH\_CryptoAsymKeySpec](../../structs/oh-cryptoasymkeyspec/document.md) \*\*spec | Pointer to the EC common parameter specifications. |

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

#### \[h2\]OH\_CryptoAsymKeySpec\_GenDhCommonParamsSpec()

OH\_Crypto\_ErrCode OH\_CryptoAsymKeySpec\_GenDhCommonParamsSpec(int pLen, int skLen, OH\_CryptoAsymKeySpec \*\*spec)

**Description**

Generates DH common parameter specifications.

Note: After the use is complete, the memory for storing the **spec** parameter must be destroyed by calling [OH\_CryptoAsymKeySpec\_Destroy](#oh_cryptoasymkeyspec_destroy).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| int pLen | Length of the prime number **p**, in bytes. |
| int skLen | Length of the private key, in bytes. |
| [OH\_CryptoAsymKeySpec](../../structs/oh-cryptoasymkeyspec/document.md) \*\*spec | Pointer to the DH common parameter specifications. |

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

#### \[h2\]OH\_CryptoAsymKeySpec\_Create()

OH\_Crypto\_ErrCode OH\_CryptoAsymKeySpec\_Create(const char \*algoName, CryptoAsymKeySpec\_Type type, OH\_CryptoAsymKeySpec \*\*spec)

**Description**

Creates asymmetric key specifications based on the given algorithm name and specification type.

Note: The created resource must be destroyed by calling [OH\_CryptoAsymKeySpec\_Destroy](#oh_cryptoasymkeyspec_destroy).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*algoName | 
Pointer to the algorithm used to generate specifications.

For example, **RSA**.

 |
| [CryptoAsymKeySpec\_Type](#cryptoasymkeyspec_type) type | Specification type of an asymmetric key. |
| [OH\_CryptoAsymKeySpec](../../structs/oh-cryptoasymkeyspec/document.md) \*\*spec | Pointer to the asymmetric key specifications. |

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

#### \[h2\]OH\_CryptoAsymKeySpec\_SetParam()

OH\_Crypto\_ErrCode OH\_CryptoAsymKeySpec\_SetParam(OH\_CryptoAsymKeySpec \*spec, CryptoAsymKey\_ParamType type, Crypto\_DataBlob \*value)

**Description**

Sets the specified parameters for asymmetric key specifications.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoAsymKeySpec](../../structs/oh-cryptoasymkeyspec/document.md) \*spec | Pointer to the asymmetric key specifications. |
| [CryptoAsymKey\_ParamType](#cryptoasymkey_paramtype) type | Type of the asymmetric key parameter to obtain. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*value | Pointer to the input data. |

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

#### \[h2\]OH\_CryptoAsymKeySpec\_SetCommonParamsSpec()

OH\_Crypto\_ErrCode OH\_CryptoAsymKeySpec\_SetCommonParamsSpec(OH\_CryptoAsymKeySpec \*spec, OH\_CryptoAsymKeySpec \*commonParamsSpec)

**Description**

Sets the common parameter specifications for asymmetric key specifications.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoAsymKeySpec](../../structs/oh-cryptoasymkeyspec/document.md) \*spec | Pointer to the asymmetric key specifications. |
| [OH\_CryptoAsymKeySpec](../../structs/oh-cryptoasymkeyspec/document.md) \*commonParamsSpec | Pointer to the common parameter specifications. |

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

#### \[h2\]OH\_CryptoAsymKeySpec\_GetParam()

OH\_Crypto\_ErrCode OH\_CryptoAsymKeySpec\_GetParam(OH\_CryptoAsymKeySpec \*spec, CryptoAsymKey\_ParamType type, Crypto\_DataBlob \*value)

**Description**

Obtains the specified parameters for asymmetric key specifications.

Note: After the use is complete, the memory for storing the **value** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoAsymKeySpec](../../structs/oh-cryptoasymkeyspec/document.md) \*spec | Pointer to the asymmetric key specifications. |
| [CryptoAsymKey\_ParamType](#cryptoasymkey_paramtype) type | Type of the asymmetric key parameter to obtain. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*value | Pointer to the output data. |

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

#### \[h2\]OH\_CryptoAsymKeySpec\_Destroy()

void OH\_CryptoAsymKeySpec\_Destroy(OH\_CryptoAsymKeySpec \*spec)

**Description**

Destroys asymmetric key specifications.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoAsymKeySpec](../../structs/oh-cryptoasymkeyspec/document.md) \*spec | Pointer to the asymmetric key specifications. |

#### \[h2\]OH\_CryptoAsymKeyGeneratorWithSpec\_Create()

OH\_Crypto\_ErrCode OH\_CryptoAsymKeyGeneratorWithSpec\_Create(OH\_CryptoAsymKeySpec \*keySpec, OH\_CryptoAsymKeyGeneratorWithSpec \*\*generator)

**Description**

Creates a struct for an asymmetric key generator with specifications.

Note: The created resource must be destroyed by calling [OH\_CryptoAsymKeyGeneratorWithSpec\_Destroy](#oh_cryptoasymkeygeneratorwithspec_destroy).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoAsymKeySpec](../../structs/oh-cryptoasymkeyspec/document.md) \*keySpec | Pointer to the asymmetric key specifications. |
| [OH\_CryptoAsymKeyGeneratorWithSpec](../../structs/oh-cryptoasymkeygeneratorwithspec/document.md) \*\*generator | Pointer to the asymmetric key generator with specifications. |

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

#### \[h2\]OH\_CryptoAsymKeyGeneratorWithSpec\_GenKeyPair()

OH\_Crypto\_ErrCode OH\_CryptoAsymKeyGeneratorWithSpec\_GenKeyPair(OH\_CryptoAsymKeyGeneratorWithSpec \*generator, OH\_CryptoKeyPair \*\*keyPair)

**Description**

Generates a key pair based on asymmetric key specifications.

Note: After the use is complete, the memory for storing the **keyPair** parameter must be released by calling [OH\_CryptoKeyPair\_Destroy](#oh_cryptokeypair_destroy).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoAsymKeyGeneratorWithSpec](../../structs/oh-cryptoasymkeygeneratorwithspec/document.md) \*generator | Pointer to the asymmetric key generator with specifications. |
| [OH\_CryptoKeyPair](../../structs/oh-cryptokeypair/document.md) \*\*keyPair | Pointer to the key pair. |

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

#### \[h2\]OH\_CryptoAsymKeyGeneratorWithSpec\_Destroy()

void OH\_CryptoAsymKeyGeneratorWithSpec\_Destroy(OH\_CryptoAsymKeyGeneratorWithSpec \*generator)

**Description**

Destroys a struct for an asymmetric key generator with specifications.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoAsymKeyGeneratorWithSpec](../../structs/oh-cryptoasymkeygeneratorwithspec/document.md) \*generator | Pointer to the asymmetric key generator with specifications. |

#### \[h2\]OH\_CryptoEcPoint\_Create()

OH\_Crypto\_ErrCode OH\_CryptoEcPoint\_Create(const char \*curveName, Crypto\_DataBlob \*ecKeyData, OH\_CryptoEcPoint \*\*point)

**Description**

Creates an EC point.

Note: The created resource must be destroyed by calling [OH\_CryptoEcPoint\_Destroy](#oh_cryptoecpoint_destroy).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*curveName | Pointer to the curve name. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*ecKeyData | Pointer to the EC point data, in **04 || x || y**, **02 || x**, or **03 || x** format. If **ecKeyData** is **NULL**, an empty EC point specification is created. |
| [OH\_CryptoEcPoint](../../structs/oh-cryptoecpoint/document.md) \*\*point | Pointer to the EC point. |

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

#### \[h2\]OH\_CryptoEcPoint\_GetCoordinate()

OH\_Crypto\_ErrCode OH\_CryptoEcPoint\_GetCoordinate(OH\_CryptoEcPoint \*point, Crypto\_DataBlob \*x, Crypto\_DataBlob \*y)

**Description**

Obtains the X and Y coordinates of an EC point.

Note: After the use is complete, the memory for storing the **x** and **y** parameters must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoEcPoint](../../structs/oh-cryptoecpoint/document.md) \*point | Pointer to the EC point. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*x | Pointer to the X coordinate of an EC point. The value can be **NULL**. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*y | Pointer to the Y coordinate of an EC point. The value can be **NULL**. |

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

#### \[h2\]OH\_CryptoEcPoint\_SetCoordinate()

OH\_Crypto\_ErrCode OH\_CryptoEcPoint\_SetCoordinate(OH\_CryptoEcPoint \*point, Crypto\_DataBlob \*x, Crypto\_DataBlob \*y)

**Description**

Sets the X and Y coordinates of an EC point.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoEcPoint](../../structs/oh-cryptoecpoint/document.md) \*point | Pointer to the EC point. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*x | Pointer to the X coordinate of the EC point. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*y | Pointer to the Y coordinate of the EC point. |

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

#### \[h2\]OH\_CryptoEcPoint\_Encode()

OH\_Crypto\_ErrCode OH\_CryptoEcPoint\_Encode(OH\_CryptoEcPoint \*point, const char \*format, Crypto\_DataBlob \*out)

**Description**

Encodes an EC point in a specified format.

Note: After the use is complete, the memory for storing the **out** parameter must be released by calling [OH\_Crypto\_FreeDataBlob](../crypto-common-h/document.md#oh_crypto_freedatablob).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoEcPoint](../../structs/oh-cryptoecpoint/document.md) \*point | Pointer to the EC point. |
| const char \*format | Pointer to the encoding format. The value can be **UNCOMPRESSED** or **COMPRESSED**. |
| [Crypto\_DataBlob](../../structs/crypto-datablob/document.md) \*out | Pointer to the encoded EC point data. |

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

#### \[h2\]OH\_CryptoEcPoint\_Destroy()

void OH\_CryptoEcPoint\_Destroy(OH\_CryptoEcPoint \*point)

**Description**

Destroys an EC point.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_CryptoEcPoint](../../structs/oh-cryptoecpoint/document.md) \*point | Pointer to the EC point. |
