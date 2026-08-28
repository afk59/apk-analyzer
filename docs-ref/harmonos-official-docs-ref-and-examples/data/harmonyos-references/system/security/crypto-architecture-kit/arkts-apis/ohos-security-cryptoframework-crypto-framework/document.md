# @ohos.security.cryptoFramework (Crypto Framework)

The **cryptoFramework** module provides APIs for cryptographic operations, shielding the underlying hardware and algorithm library.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/mrY42O7GT92HTpqJ8qkXiA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4304F6C381CB3E4EBACEED4ECE4097E69EEA5038AA6BB870699470635E39DCAE)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

#### Result

Enumerates the operation results.

**System capability**: SystemCapability.Security.CryptoFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| INVALID\_PARAMS | 401 | 
Invalid parameter.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| NOT\_SUPPORT | 801 | 

Unsupported operation.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ERR\_OUT\_OF\_MEMORY | 17620001 | 

The memory operation failed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| ERR\_RUNTIME\_ERROR | 17620002 | 

The parameter conversion between ArkTS and C failed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ERR\_PARAMETER\_CHECK\_FAILED20+ | 17620003 | 

The parameter check failed.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| ERR\_CRYPTO\_OPERATION | 17630001 | 

Cryptographic operation error.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### DataBlob

Encapsulates binary data. The core field **data** is of the Uint8Array type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Security.CryptoFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| data | Uint8Array | No | No | Binary data array. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/47TRydUuR0yH_F7G1PWlTg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42CB8BA13B9AA8BBAEBCE2DEA2F0F4AB4749A0795506769A8B3183FE7C852F4A)

The Uint8Array typed array represents an array of 8-bit unsigned integers.

#### ParamsSpec

Encapsulates the parameters used for encryption or decryption. You need to construct its child class object and pass it to [init()](#init-1) for symmetric encryption or decryption.

It applies to the symmetric block cipher modes that require parameters such as the initialization vector (IV). If the IV is not required (for example, the ECB mode), pass in **null** to [init()](#init-1).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/NO8820g8TnOS3lQbKSHiFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19577D01EA0D185852D8B1B32609E43AED769CA03BBC568B8BEBC484AC6D6DA5)

An initialization vector (IV) is a byte sequence used to introduce randomness or uniqueness in symmetric encryption modes (such as CBC, CTR, OFB, CFB, GCM, CCM, and Poly1305). It ensures that different ciphertexts are generated for the same plaintext under the same key.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Cipher** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| algName | string | No | No | 
Algorithm for symmetric encryption or decryption. The value can be:

\- **IvParamsSpec**: applicable to CBC,

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/P0dw_RxGRfKRg2WW4h6MjA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8798F55FF65B51454D69D26E640CE0DAAA7939437E49410E9031BDA338468BAA)

The **params** parameter in [init()](#init-1) is of the **ParamsSpec** type (parent class). However, a child class object (such as **IvParamsSpec**) needs to be passed in. When constructing the child class object, you must set **algName** for its parent class **ParamsSpec** to specify the child class object to be passed to **init()**.

#### IvParamsSpec

Encapsulates the parameters for encryption or decryption using a block cipher mode that requires an IV. It is a child class of [ParamsSpec](#paramsspec) and used as a parameter in [init()](#init-1) for symmetric encryption or decryption.

This class is applicable to block cipher modes that require an IV, such as CBC, CTR, OFB, CFB, and Poly1305.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Cipher** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| iv | [DataBlob](#datablob) | No | No | 
IV for encryption or decryption. Options:

\- AES CBC,

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/TJhwJhohQ9Ks4RjjXMBU6A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9EEAEA00072D67BA1CD4CEAD76D46A2B97982430922BAEB7BFE58D2B3F026E39)

Before passing a value to [init()](#init-1), specify **algName** for its parent class [ParamsSpec](#paramsspec).

#### GcmParamsSpec

Encapsulates the parameters for encryption or decryption using a block cipher mode that requires an IV. It is a child class of [ParamsSpec](#paramsspec) and used as a parameter in [init()](#init-1) for symmetric encryption or decryption.

**GcmParamsSpec** applies to the GCM mode.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Cipher** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| iv | [DataBlob](#datablob) | No | No | IV, which is of 1 to 16 bytes. A 12-byte IV is commonly used. |
| aad | [DataBlob](#datablob) | No | No | Additional authentication data (AAD), which is of 0 to INT\_MAX bytes. A 16-byte AAD is commonly used. |
| authTag | [DataBlob](#datablob) | No | No | 
Authentication tag, which is of 16 bytes.

When GCM mode is used for encryption, you need to extract the last 16 bytes from the [DataBlob](#datablob) returned by [doFinal()](#dofinal) or [doFinalSync()](#dofinalsync12) and use them as **authTag** in **GcmParamsSpec** for [init()](#init-1) or [initSync()](#initsync12).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/lghNQ-YBS569liQZqzD3vA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=15DC0A88B42A9061087D526233F36915AC5671068F7514D89D93DD04A3D96D81)

1.  Before passing a value to [init()](#init-1), specify **algName** for its parent class [ParamsSpec](#paramsspec).
2.  The Crypto framework imposes no additional restrictions on the IV of 1 to 16 bytes. However, the operation result depends on the underlying OpenSSL support.
3.  If **aad** is not required or the **aad** length is 0, you can set its **data** attribute to an empty Uint8Array in the **aad: { data: new Uint8Array() }** format when constructing **GcmParamsSpec**.

#### CcmParamsSpec

Encapsulates the parameters for encryption or decryption using a block cipher mode that requires an IV. It is a child class of [ParamsSpec](#paramsspec) and used as a parameter in [init()](#init-1) for symmetric encryption or decryption.

**CcmParamsSpec** applies to the CCM mode.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Cipher** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| iv | [DataBlob](#datablob) | No | No | IV for encryption and decryption. Only 7 bytes are supported. If the length of the input **iv** parameter exceeds 7 bytes, the excess part will be truncated. |
| aad | [DataBlob](#datablob) | No | No | AAD for encryption and decryption. The AAD value contains 1 to 2,048 bytes. |
| authTag | [DataBlob](#datablob) | No | No | 
Authentication tag, which is of 12 bytes.

When CCM mode is used for encryption, you need to extract the last 12 bytes from the [DataBlob](#datablob) returned by [doFinal()](#dofinal) or [doFinalSync()](#dofinalsync12) and use them as **authTag** in [CcmParamsSpec](#ccmparamsspec) for [init()](#init-1) or [initSync()](#initsync12).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/OjsCtxHTRmmzMfKMQvXh7Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FEFC18B653E70888A6DFA5558ED06B8A7785E238510AE626E80D5EF6C1B33A73)

Before passing a value to [init()](#init-1), specify **algName** for its parent class [ParamsSpec](#paramsspec).

#### Poly1305ParamsSpec22+

Encapsulates the parameters for encryption or decryption using a block cipher mode that requires an IV. It is a child class of [ParamsSpec](#paramsspec) and used as a parameter in [init()](#init-1) for symmetric encryption or decryption.

Applicable to the Poly1305 mode of [ChaCha20](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-sym-encrypt-decrypt-spec#chacha20).

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| iv | [DataBlob](#datablob) | No | No | IV, which is of 12 bytes. |
| aad | [DataBlob](#datablob) | No | No | AAD, which is of any bytes. |
| authTag | [DataBlob](#datablob) | No | No | Authentication tag, which is of 16 bytes. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/c2IGPG1MRx-a5vLBsk4xyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65366A750625B6EDB5C91B5578B41F7FB66338E18CDA1304AB97D42A69572E08)

Before passing a value to [init()](#init-1), specify **algName** for its parent class [ParamsSpec](#paramsspec).

When the Poly1305 mode is used for encryption, you need to extract the last 16 bytes from the [DataBlob](#datablob) returned by [doFinal()](#dofinal) or [doFinalSync()](#dofinalsync12) and use them as **authTag** in [Poly1305ParamsSpec](#poly1305paramsspec22) for [init()](#init-1) or [initSync()](#initsync12) during decryption.

#### CryptoMode

Enumerates the cryptographic operations.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Cipher** since API version 12.

| Name | Value | Description |
| :-- | :-- | :-- |
| ENCRYPT\_MODE | 0 | Encryption. |
| DECRYPT\_MODE | 1 | Decryption. |

#### AsyKeySpecItem10+

Enumerates the asymmetric key parameters.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Value | Description |
| :-- | :-- | :-- |
| DSA\_P\_BN | 101 | Prime modulus **p** in the DSA algorithm. |
| DSA\_Q\_BN | 102 | Parameter **q**, prime factor of (p-1) in the DSA algorithm. |
| DSA\_G\_BN | 103 | Parameter **g** in the DSA algorithm. |
| DSA\_SK\_BN | 104 | Private key **sk** in the DSA algorithm. |
| DSA\_PK\_BN | 105 | Public key **pk** in the DSA algorithm. |
| ECC\_FP\_P\_BN | 201 | Prime number **p** in the **Fp** field of the elliptic curve in the ECC algorithm. |
| ECC\_A\_BN | 202 | First coefficient **a** of the elliptic curve in the ECC algorithm. |
| ECC\_B\_BN | 203 | Second coefficient **b** of the elliptic curve in the ECC algorithm. |
| ECC\_G\_X\_BN | 204 | X coordinate of the base point **g** in the ECC algorithm. |
| ECC\_G\_Y\_BN | 205 | Y coordinate of the base point **g** in the ECC algorithm. |
| ECC\_N\_BN | 206 | Order **n** of the base point **g** in the ECC algorithm. |
| ECC\_H\_NUM | 207 | Cofactor **h** in the ECC algorithm. |
| ECC\_SK\_BN | 208 | Private key **sk** in the ECC algorithm. |
| ECC\_PK\_X\_BN | 209 | X coordinate of the public key **pk** (a point on the elliptic curve) in the ECC algorithm. |
| ECC\_PK\_Y\_BN | 210 | Y coordinate of the public key **pk** (a point on the elliptic curve) in the ECC algorithm. |
| ECC\_FIELD\_TYPE\_STR | 211 | Elliptic curve field type in the ECC algorithm. Currently, only the **Fp** field is supported. |
| ECC\_FIELD\_SIZE\_NUM | 212 | 
Size of the field in the ECC algorithm, in bits.

Note: The size of the **Fp** field is the length of the prime **p**, in bits.

 |
| ECC\_CURVE\_NAME\_STR | 213 | Standards for Efficient Cryptography Group (SECG) curve name in the ECC algorithm. |
| RSA\_N\_BN | 301 | Modulus **n** in the RSA algorithm. |
| RSA\_SK\_BN | 302 | Private key **sk** (private key exponent **d**) in the RSA algorithm. |
| RSA\_PK\_BN | 303 | Public key **pk** (public key exponent **e**) in the RSA algorithm. |
| DH\_P\_BN11+ | 401 | Prime **p** in the DH algorithm. |
| DH\_G\_BN11+ | 402 | Parameter **g** in the DH algorithm. |
| DH\_L\_NUM11+ | 403 | Length of the private key in the DH algorithm, in bits. |
| DH\_SK\_BN11+ | 404 | Private key **sk** in the DH algorithm. |
| DH\_PK\_BN11+ | 405 | Public key **pk** in the DH algorithm. |
| ED25519\_SK\_BN11+ | 501 | Private key **sk** in the Ed25519 algorithm. |
| ED25519\_PK\_BN11+ | 502 | Public key **pk** in the Ed25519 algorithm. |
| X25519\_SK\_BN11+ | 601 | Private key **sk** in the X25519 algorithm. |
| X25519\_PK\_BN11+ | 602 | Public key **pk** in the X25519 algorithm. |

#### AsyKeySpecType10+

Enumerates the key parameter types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Value | Description |
| :-- | :-- | :-- |
| COMMON\_PARAMS\_SPEC | 0 | Common parameter of the public and private keys. You can use [generateKeyPair](#generatekeypair10) to randomly generate a key pair based on the parameters of this type. |
| PRIVATE\_KEY\_SPEC | 1 | Parameter of the private key. You can use [generatePriKey](#generateprikey10) to generate a private key based on the parameters of this type. |
| PUBLIC\_KEY\_SPEC | 2 | Parameter of the public key. You can use [generatePubKey](#generatepubkey10) to generate a public key based on the parameters of this type. |
| KEY\_PAIR\_SPEC | 3 | Full parameters of the public and private keys. You can use [generateKeyPair](#generatekeypair10) to generate a key pair based on the parameters of this type. |

#### CipherSpecItem10+

Enumerates encryption and decryption parameters, which can be set by using [setCipherSpec](#setcipherspec10) and obtained by using [getCipherSpec](#getcipherspec10).

Currently, only RSA and SM2 are supported. Since API version 11, the **SM2\_MD\_NAME\_STR** parameter is supported. For details, see [Asymmetric Key Encryption and Decryption Algorithm Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-asym-encrypt-decrypt-spec).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Cipher** since API version 12.

| Name | Value | Description |
| :-- | :-- | :-- |
| OAEP\_MD\_NAME\_STR | 100 | Message digest (MD) algorithm used with the PKCS1\_OAEP padding mode in RSA. |
| OAEP\_MGF\_NAME\_STR | 101 | Mask generation algorithm used with the PKCS1\_OAEP padding mode in RSA. Currently, only MGF1 is supported. |
| OAEP\_MGF1\_MD\_STR | 102 | MD algorithm for the MGF1 mask generation used with the PKCS1\_OAEP padding mode in RSA. |
| OAEP\_MGF1\_PSRC\_UINT8ARR | 103 | **pSource** byte stream used with the PKCS1\_OAEP padding mode in RSA. |
| SM2\_MD\_NAME\_STR11+ | 104 | MD algorithm used in SM2. |

#### SignSpecItem10+

Enumerates the signing and signature verification parameters, which can be set by using [setSignSpec](#setsignspec10) and [setVerifySpec](#setverifyspec10), and obtained by using [getSignSpec](#getsignspec10) and [getVerifySpec](#getverifyspec10).

Currently, only RSA and SM2 are supported. Since API version 11, the **SM2\_USER\_ID\_UINT8ARR** parameter is supported. For details, see [Signing and Signature Verification Overview and Algorithm Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-sign-sig-verify-overview).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

| Name | Value | Description |
| :-- | :-- | :-- |
| PSS\_MD\_NAME\_STR | 100 | MD algorithm used with the PSS padding mode in RSA. |
| PSS\_MGF\_NAME\_STR | 101 | Mask generation algorithm used with the PSS padding mode in RSA. Currently, only MGF1 is supported. |
| PSS\_MGF1\_MD\_STR | 102 | MD parameters for the MGF1 mask generation used with the PSS padding mode in RSA. |
| PSS\_SALT\_LEN\_NUM | 103 | Length of the salt in bytes used with the PSS padding mode in RSA. |
| PSS\_TRAILER\_FIELD\_NUM | 104 | Trailer field used in the encoding operation when PSS padding mode is used in RSA. |
| SM2\_USER\_ID\_UINT8ARR11+ | 105 | User ID field in SM2. |

#### AsyKeySpec10+

Defines the asymmetric key parameters for creating a key generator. You need to construct a child class object and pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator. When constructing a child class object, use little-endian format for RSA keys and use big-endian format and positive numbers for other key parameters of the bigint type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| algName | string | No | No | Asymmetric key algorithm, for example, **RSA**, **DSA**, **ECC**, **SM2**, **Ed25519**, **X25519**, or **DH**. |
| specType | [AsyKeySpecType](#asykeyspectype10) | No | No | Key parameter type, which is used to distinguish public and private key parameters. |

#### DSACommonParamsSpec10+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify the common parameters of the public and private keys in the DSA algorithm. It can be used to randomly generate a public or private key.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| p | bigint | No | No | Prime modulus **p** in the DSA algorithm. |
| q | bigint | No | No | Parameter **q**, prime factor of (**p**\-1) in the DSA algorithm. |
| g | bigint | No | No | Parameter **g** in the DSA algorithm. |

#### DSAPubKeySpec10+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify the parameters of the public key in the DSA algorithm.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| params | [DSACommonParamsSpec](#dsacommonparamsspec10) | No | No | Common parameters of the public and private keys in the DSA algorithm. |
| pk | bigint | No | No | Public key in the DSA algorithm. |

#### DSAKeyPairSpec10+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify full parameters of the public and private keys in the DSA algorithm.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| params | [DSACommonParamsSpec](#dsacommonparamsspec10) | No | No | Common parameters of the public and private keys in the DSA algorithm. |
| sk | bigint | No | No | Private key **sk** in the DSA algorithm. |
| pk | bigint | No | No | Public key in the DSA algorithm. |

#### ECField10+

Defines the field type of an elliptic curve. Currently, only the **Fp** field is supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fieldType | string | No | No | Type of the elliptic curve field. Currently, only **Fp** is supported. |

#### ECFieldFp10+

Defines the prime field of the elliptic curve. It is a child class of [ECField](#ecfield10).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| p | bigint | No | No | Value of the prime number **p**. |

#### Point10+

Defines a point on the elliptic curve.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | bigint | No | No | X coordinate of the point on an elliptic curve. |
| y | bigint | No | No | Y coordinate of the point on an elliptic curve. |

#### ECCCommonParamsSpec10+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify the common parameters of the public and private keys in the ECC algorithm. It can be used to randomly generate a public or private key.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| field | [ECField](#ecfield10) | No | No | Field of the elliptic curve. Currently, only **Fp** is supported. |
| a | bigint | No | No | First coefficient **a** of the elliptic curve. |
| b | bigint | No | No | Second coefficient **b** of the elliptic curve. |
| g | [Point](#point10) | No | No | Base point g. |
| n | bigint | No | No | Order **n** of the base point **g**. |
| h | number | No | No | Cofactor **h**. |

#### ECCPriKeySpec10+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify the parameters of the private key in the ECC algorithm.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| params | [ECCCommonParamsSpec](#ecccommonparamsspec10) | No | No | Common parameters of the public and private keys in the ECC algorithm. |
| sk | bigint | No | No | Private key **sk** in the ECC algorithm. |

#### ECCPubKeySpec10+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify the parameters of the public key in the ECC algorithm.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| params | [ECCCommonParamsSpec](#ecccommonparamsspec10) | No | No | Common parameters of the public and private keys in the ECC algorithm. |
| pk | [Point](#point10) | No | No | Public key **pk** in the ECC algorithm. |

#### ECCKeyPairSpec10+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify full parameters of the public and private keys in the ECC algorithm.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| params | [ECCCommonParamsSpec](#ecccommonparamsspec10) | No | No | Common parameters of the public and private keys in the ECC algorithm. |
| sk | bigint | No | No | Private key **sk** in the ECC algorithm. |
| pk | [Point](#point10) | No | No | Public key **pk** in the ECC algorithm. |

#### RSACommonParamsSpec10+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify the common parameters of the public and private keys in the RSA algorithm. It can be used to randomly generate a public or private key.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| n | bigint | No | No | Modulus **n**. |

#### RSAPubKeySpec10+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify the parameters of the public key in the RSA algorithm.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| params | [RSACommonParamsSpec](#rsacommonparamsspec10) | No | No | Common parameters of the public and private keys in the RSA algorithm. |
| pk | bigint | No | No | Public key **pk** in the RSA algorithm. |

#### RSAKeyPairSpec10+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify full parameters of the public and private keys in the RSA algorithm.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| params | [RSACommonParamsSpec](#rsacommonparamsspec10) | No | No | Common parameters of the public and private keys in the RSA algorithm. |
| sk | bigint | No | No | Private key **sk** in the RSA algorithm. |
| pk | bigint | No | No | Public key **pk** in the RSA algorithm. |

#### ED25519PriKeySpec11+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify the parameters of the private key in the Ed25519 algorithm.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API version 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| sk | bigint | No | No | Private key **sk** in the Ed25519 algorithm. |

#### ED25519PubKeySpec11+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify the parameters of the public key in the Ed25519 algorithm.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API version 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pk | bigint | No | No | Public key **pk** in the Ed25519 algorithm. |

#### ED25519KeyPairSpec11+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify full parameters of the public and private keys in the Ed25519 algorithm.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API version 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| sk | bigint | No | No | Private key **sk** in the Ed25519 algorithm. |
| pk | bigint | No | No | Public key **pk** in the Ed25519 algorithm. |

#### X25519PriKeySpec11+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify the parameters of the private key in the X25519 algorithm.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API version 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| sk | bigint | No | No | Private key **sk** in the X25519 algorithm. |

#### X25519PubKeySpec11+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify the parameters of the public key in the X25519 algorithm.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API version 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pk | bigint | No | No | Public key **pk** in the X25519 algorithm. |

#### X25519KeyPairSpec11+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify full parameters of the public and private keys in the X25519 algorithm.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API version 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| sk | bigint | No | No | Private key **sk** in the X25519 algorithm. |
| pk | bigint | No | No | Public key **pk** in the X25519 algorithm. |

#### DHCommonParamsSpec11+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify the parameters of the public and private keys in the DH algorithm.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API version 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| p | bigint | No | No | Large prime **p** in the DH algorithm. |
| g | bigint | No | No | Parameter **g** in the DH algorithm. |
| l | number | No | No | Length of the private key in the DH algorithm, in bits. |

#### DHPriKeySpec11+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify the parameters of the private key in the DH algorithm.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API version 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| params | [DHCommonParamsSpec](#dhcommonparamsspec11) | No | No | Common parameters of the public and private keys in the DH algorithm. |
| sk | bigint | No | No | Private key **sk** in the DH algorithm. |

#### DHPubKeySpec11+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify the parameters of the public key in the DH algorithm.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API version 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| params | [DHCommonParamsSpec](#dhcommonparamsspec11) | No | No | Common parameters of the public and private keys in the DH algorithm. |
| pk | bigint | No | No | Public key **pk** in the DH algorithm. |

#### DHKeyPairSpec11+

Defines a child class of [AsyKeySpec](#asykeyspec10) used to specify full parameters of the public and private keys in the DH algorithm.

To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create a key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API version 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| params | [DHCommonParamsSpec](#dhcommonparamsspec11) | No | No | Common parameters of the public and private keys in the DH algorithm. |
| sk | bigint | No | No | Private key **sk** in the DH algorithm. |
| pk | bigint | No | No | Public key **pk** in the DH algorithm. |

#### KdfSpec11+

Defines the parameters of the key derivation function. When the key derivation function is used to derive a key, you need to construct and pass in a child class object of **KdfSpec**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Kdf

The system capability is **SystemCapability.Security.CryptoFramework** in API version 11, and **SystemCapability.Security.CryptoFramework.Kdf** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| algName | string | No | No | Algorithm of the key derivation function, for example, **PBKDF2**. |

#### PBKDF2Spec11+

Defines the child class of [KdfSpec](#kdfspec11). It is used as a parameter for PBKDF2 key derivation.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Kdf

The system capability is **SystemCapability.Security.CryptoFramework** in API version 11, and **SystemCapability.Security.CryptoFramework.Kdf** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| password | string | Uint8Array | No | No | Original password entered by the user. |
| salt | Uint8Array | No | No | Salt value. |
| iterations | number | No | No | Number of iterations. The value must be a positive integer. |
| keySize | number | No | No | Length of the derived key, in bytes. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/aiJvG_mTSbe9jMeEpWNqIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1ECD6B16D61CAF1C463021062D325B3C936FF66A303449FB4CBFA3D1F8540E3D)

**password** is the original password. If **password** of the string type is used, pass in the actual data for key derivation, rather than a HexString or Base64-encoded value. In addition, the string must be encoded in UTF-8, as other encodings may alter the derivation outcome.

#### HKDFSpec12+

Defines the child class of [KdfSpec](#kdfspec11). It is a parameter for HKDF key derivation.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Kdf

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| key | string | Uint8Array | No | No | Key material. |
| salt | Uint8Array | No | No | Salt value. |
| info | Uint8Array | No | No | Information used to expand the key. |
| keySize | number | No | No | Length of the derived key, in bytes. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/gb227gLkSjuvJIDdmqE0zg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E482CAF6E1D91395AB4239E1189CD1739923996C43A0DBF1DAB3D0D8089211B7)

**key** is the original key material entered by the user. **info** and **salt** are optional. An empty string can be passed in based on the mode.

For example, if the mode is **EXTRACT\_AND\_EXPAND**, all parameter values must be passed in. If the mode is **EXTRACT\_ONLY**, **info** can be empty. When **HKDFSpec** is constructed, pass in **null** to **info**.

The default mode is **EXTRACT\_AND\_EXPAND**. The value **HKDF|SHA256|EXTRACT\_AND\_EXPAND** is equivalent to **HKDF|SHA256**.

#### ScryptSpec18+

Defines the child class of [KdfSpec](#kdfspec11). It is a parameter for scrypt key derivation function (KDF).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Security.CryptoFramework.Kdf

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| passphrase | string | Uint8Array | No | No | Original password entered by the user. |
| salt | Uint8Array | No | No | Salt value. |
| n | number | No | No | Number of iterations. The value must be a positive integer. |
| p | number | No | No | Parallelization parameter. The value must be a positive integer. |
| r | number | No | No | Block size. The value must be a positive integer. |
| maxMemory | number | No | No | Maximum memory size. The value must be a positive integer. |
| keySize | number | No | No | Length of the derived key, in bytes. The value must be a positive integer. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/YDFnFhXKT0OOz-S07WwYig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3DC9139CF2DB625E4DD2FE143D202F50B978226302D2E2E17F386E568DE1A22A)

**passphrase** specifies the original password. If **password** is of the string type, pass in the data used for key derivation rather than a string of the HexString or Base64 type. In addition, the string must be in utf-8 format. Otherwise, the key derived may be different from the one expected.

#### X963KdfSpec22+

Defines the child class of [KdfSpec](#kdfspec11). It is a parameter for X963KDF key derivation function (KDF).

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Security.CryptoFramework.Kdf

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| key | string | Uint8Array | No | No | Key material. |
| info | Uint8Array | No | No | Additional description. |
| keySize | number | No | No | Length of the derived key, in bytes. The value must be a positive integer. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/WxpiOkd7RuqQSHIgkjiLCg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32C33E7116F84C8234AE9D2CD41E776265C89D5C5C33882116A299EA01DA2B43)

**key** is the original key material entered by the user.

#### SM2CipherTextSpec12+

Represents the SM2 ciphertext parameters. You can use this object to generate SM2 ciphertext in ASN.1 format or obtain SM2 parameters from the SM2 ciphertext in ASN.1 format.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| xCoordinate | bigint | No | No | Coordinate X. |
| yCoordinate | bigint | No | No | Coordinate Y. |
| cipherTextData | Uint8Array | No | No | Ciphertext. |
| hashData | Uint8Array | No | No | Hash value. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/l7uQTRFrSCm6wPREKIlGOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95C7725ED9E9C25E0C2B8117324EA0C7C235A3698BE236CD0D9F369416A3128F)

-   **hashData** is a value obtained by applying the SM3 algorithm to the plaintext. It has a fixed length of 256 bits.
    
-   **cipherTextData** is the ciphertext with the same length as the plaintext.
    
-   During the generation of ciphertext in C1C3C2 format, if the length of x (**C1\_X**) or y (**C1\_Y**) is less than 32 bytes, zeros must be added to the high-order bits to extend them to 32 bytes.
    

#### KeyEncodingConfig18+

Represents the RSA private key encoding parameters. You can use it to generate an encoded private key string with the specified algorithm and password.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| password | string | No | No | Password used for encoding the private key. |
| cipherName | string | No | No | Algorithm to use. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/-sT64J1jTAGfZt1XoRbGww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D308A47A5D664B671F110C07CCF0DF088B6013112967CFDFC4B96478460AB617)

-   **password** specifies the password used for encoding the private key. It is mandatory.
    
-   **cipherName** specifies the algorithm used for encoding. It is mandatory. Currently, only **AES-128-CBC**, **AES-192-CBC**, **AES-256-CBC**, and **DES-EDE3-CBC** are supported.
    

#### MacSpec18+

Represents the message authentication code (MAC) parameters. You need to construct a child class object and use it as a parameter when generating an HMAC or a CMAC.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Security.CryptoFramework.Mac

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| algName | string | No | No | Algorithm to use. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/l9A53w15Tzie7IV97fZiQQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9BF414D00E6B0F9BFEE8CD615FBD9B903649E3EA84C9176CFCDF0F2224A93EE1)

**algName** specifies the MAC algorithm to use. It is mandatory.

#### HmacSpec18+

Represents the child class of [MacSpec](#macspec18). It is used as an input parameter for HMAC generation.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Security.CryptoFramework.Mac

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| mdName | string | No | No | MD algorithm to use. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/uw0A3iCPS8KtxeLy-qb9Lg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F3B2C46C2AB16A6C60DDBB24EA5BCEB1715884E44282E9185076F6F17552731)

**mdName** specifies the HMAC digest algorithm. It is mandatory.

#### CmacSpec18+

Represents the child class of [MacSpec](#macspec18). It is used as an input parameter for CMAC generation.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Security.CryptoFramework.Mac

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| cipherName | string | No | No | Symmetric encryption algorithm to use. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/waB3yxg3TLG1NhzXKUY2Jg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24FBC70AF674A79E125E45923E103540DE35FA3D100A5BCB26BA8BE4D4B35D6B)

**cipherName** specifies the CMAC symmetric encryption algorithm. It is mandatory.

#### EccSignatureSpec20+

Represents the SM2 signature data that contains (r, s).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/w0gVaNwWRuanwCbVBCKyvA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2347935E6D167B7547C20A3E6EFA049C072446B2402339B8696DC4EC0F7EEDA)

**r** and **s** are each 256 bits long.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| r | bigint | No | No | Randomized value derived from the elliptic curve calculation using the ephemeral private key during signature generation. |
| s | bigint | No | No | Signature component, computed using the signer's private key, r, and the hashed message. |

#### Key

Provides APIs for key operations. Before performing cryptographic operations (such as encryption and decryption), you need to construct a child class object of **Key** and pass it to [init()](#init-1) of the [Cipher](#cipher) instance.

Keys can be generated by a child class key generator. For details, see the child class description. The child classes include [SymKey](#symkey), [PubKey](#pubkey), and [PriKey](#prikey).

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Key** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| format | string | Yes | No | Format of the key. |
| algName | string | Yes | No | Algorithm to use. This parameter contains the key length if the key is a symmetric key. |

#### \[h2\]getEncoded

getEncoded(): DataBlob

Obtains the byte stream of the key data. This API returns the result synchronously. The key can be a symmetric key, public key, or private key. The public key must comply with the ASN.1 syntax, X.509 specifications, and DER encoding. The private key must comply with the ASN.1 syntax, PKCS #8 specifications, and DER encoding.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/nHB5pbSEQNW4Dds6JSy2Gw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5EDA2BE98A78580879B76DF645038A38BE121DB9A71CF989B10F18318A38AE9B)

When the RSA algorithm generates a private key using key parameters, **getEncoded** is available for the private key object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Key** since API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| [DataBlob](#datablob) | Key obtained. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testGenerateAesKey() {
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES256');
  let symKey = await symKeyGenerator.generateSymKey();
  let encodedKey = symKey.getEncoded();
  console.info('key hex: ' + encodedKey.data);
}

#### SymKey

Provides APIs for symmetric key operations. It is a child class of [Key](#key). Its objects need to be passed to [init()](#init-1) of the [Cipher](#cipher) instance in symmetric encryption and decryption.

Symmetric keys can be generated by a [SymKeyGenerator](#symkeygenerator).

#### \[h2\]clearMem

clearMem(): void

Clears the keys in memory. This API returns the result synchronously. Call this API when the symmetric key instance is no longer required.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.SymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Key.SymKey** since API version 12.

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testGenerateAesKeyFun() {
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES256');
  let key = await symKeyGenerator.generateSymKey();
  let encodedKey = key.getEncoded();
  console.info('key blob: '+ encodedKey.data);
  key.clearMem();
  encodedKey = key.getEncoded();
  console.info('key blob: ' + encodedKey.data);
}

#### PubKey

Provides APIs for public key operations. **PubKey** is a child class of [Key](#key). It needs to be passed in during asymmetric encryption and decryption, signature verification, and key agreement.

The public key can be generated by using the asymmetric key generator [AsyKeyGenerator](#asykeygenerator) or [AsyKeyGeneratorBySpec](#asykeygeneratorbyspec10).

#### \[h2\]getAsyKeySpec10+

getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | number

Obtains a key parameter. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| itemType | [AsyKeySpecItem](#asykeyspecitem10) | Yes | Key parameter to obtain. |

**Return value**

| Type | Description |
| :-- | :-- |
| bigint | string | number | Content of the key parameter obtained. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// Construct the EccCommonSpec struct, which defines the common parameters of the ECC public and private keys.
function genEccCommonSpec(): cryptoFramework.ECCCommonParamsSpec {
  let fieldFp: cryptoFramework.ECFieldFp = {
    fieldType: 'Fp',
    p: BigInt('0xffffffffffffffffffffffffffffffff000000000000000000000001')
  }
  let G: cryptoFramework.Point = {
    x: BigInt('0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21'),
    y: BigInt('0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34')
  }
  let eccCommonSpec: cryptoFramework.ECCCommonParamsSpec = {
    algName: 'ECC',
    specType: cryptoFramework.AsyKeySpecType.COMMON\_PARAMS\_SPEC,
    field: fieldFp,
    a: BigInt('0xfffffffffffffffffffffffffffffffefffffffffffffffffffffffe'),
    b: BigInt('0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4'),
    g: G,
    n: BigInt('0xffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3d'),
    h: 1
  }
  return eccCommonSpec;
}

async function testgetAsyKeySpec() {
  let commKeySpec = genEccCommonSpec(); // Construct the EccCommonSpec object.
  let generatorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(commKeySpec); // Create an AsyKeyGenerator instance based on the EccCommonSpec object.
  let keyPair = await generatorBySpec.generateKeyPair();
  let key = keyPair.pubKey;
  let p = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC\_FP\_P\_BN);
  console.info('ecc item --- p: ' + p.toString(16));
}

#### \[h2\]getEncodedDer12+

getEncodedDer(format: string): DataBlob

Obtains the public key data that complies with the ASN.1 syntax and DER encoding format based on the specified key format (such as the specifications and compression status). Currently, only the ECC compressed and uncompressed public key data is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/A9ZSghdIQtWx0WUYqkXy3Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2832BED486FF24FC3B1CC36492D7925D4E5E4C89F828E5D15C6FA2A99D847897)

The difference between [Key.getEncoded()](#getencoded) and this API is as follows:

1.  You can specify the format of the data to be obtained in this API.
2.  The format of the key to be obtained cannot be specified in [Key.getEncoded()](#getencoded). It must match that of the original data, which is the format of the key object generated by [convertKey](#convertkey-3).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| format | string | Yes | Format of the key. The value can be **X509|COMPRESSED** or **X509|UNCOMPRESSED** only. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataBlob](#datablob) | Public key data obtained. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testGetEncodedDer() {
  let pkData = new Uint8Array(\[48, 90, 48, 20, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 9, 43, 36, 3, 3, 2, 8, 1, 1, 7, 3, 66, 0, 4, 143, 39, 57, 249, 145, 50, 63, 222, 35, 70, 178, 121, 202, 154, 21, 146, 129, 75, 76, 63, 8, 195, 157, 111, 40, 217, 215, 148, 120, 224, 205, 82, 83, 92, 185, 21, 211, 184, 5, 19, 114, 33, 86, 85, 228, 123, 242, 206, 200, 98, 178, 184, 130, 35, 232, 45, 5, 202, 189, 11, 46, 163, 156, 152\]);
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pkData };
  let generator = cryptoFramework.createAsyKeyGenerator('ECC\_BrainPoolP256r1');
  let keyPair = await generator.convertKey(pubKeyBlob, null);
  let key = keyPair.pubKey;
  let returnBlob = key.getEncodedDer('X509|UNCOMPRESSED');
  console.info('returnBlob data: ' + returnBlob.data);
}

#### \[h2\]getEncodedPem12+

getEncodedPem(format: string): string

Obtains the key data. This API returns the result synchronously. The key can be an RSA public or private key. The public key must comply with the X.509 and PKCS #1 specifications and be encoded in PEM.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| format | string | Yes | Encoding format of the key data to obtain. The format of a public key can be **'PKCS1'** or **'X509'**. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Key data obtained. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let publicPkcs1Str1024: string =
  '-----BEGIN RSA PUBLIC KEY-----\\n'
    + 'MIGJAoGBALAg3eavbX433pOjGdWdpL7HIr1w1EAeIcaCtuMfDpECPdX6X5ZjrwiE\\n'
    + 'h7cO51WXMT2gyN45DCQySr/8cLE2UiUVHo7qlrSatdLA9ETtgob3sJ4qTaBg5Lxg\\n'
    + 'SHy2gC+bvEpuIuRe64yXGuM/aP+ZvmIj9QBIVI9mJD8jLEOvQBBpAgMBAAE=\\n'
    + '-----END RSA PUBLIC KEY-----\\n';

function TestPubKeyPkcs1ToX509BySync1024() {
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let keyPair = rsaGenerator.convertPemKeySync(publicPkcs1Str1024, null);
  let pubPemKey = keyPair.pubKey;
  let pubString = pubPemKey.getEncodedPem('X509');
  console.info('\[sync\]TestPubKeyPkcs1ToX509BySync1024 pubString output = ' + pubString);
}

#### PriKey

Provides APIs for private key operations. **PriKey** is a child class of [Key](#key). It needs to be passed in during asymmetric encryption and decryption, signing, and key agreement.

The private key can be generated by using the asymmetric key generator [AsyKeyGenerator](#asykeygenerator) or [AsyKeyGeneratorBySpec](#asykeygeneratorbyspec10).

#### \[h2\]clearMem

clearMem(): void

Clear the keys in memory. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testClearMem() {
  let eccGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
    // Use AsyKeyGenerator to randomly generate an asymmetric key pair.
    let keyGenPromise = eccGenerator.generateKeyPair();
    keyGenPromise.then(keyPair => {
      let priKey = keyPair.priKey;
      let returnBlob = priKey.getEncodedDer('PKCS8');
      console.info('returnBlob data: ' + returnBlob.data);
      priKey.clearMem(); // For an asymmetric private key, clearMem() releases the internal key structure. After clearMem is executed, getEncoded() is not supported.
    });
}

#### \[h2\]getAsyKeySpec10+

getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | number

Obtains a key parameter. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| itemType | [AsyKeySpecItem](#asykeyspecitem10) | Yes | Key parameter type to obtain. |

**Return value**

| Type | Description |
| :-- | :-- |
| bigint | string | number | Content of the key parameter obtained. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
// Construct the EccCommonSpec struct, which defines the common parameters of the ECC public and private keys.
function genEccCommonSpec(): cryptoFramework.ECCCommonParamsSpec {
  let fieldFp: cryptoFramework.ECFieldFp = {
    fieldType: 'Fp',
    p: BigInt('0xffffffffffffffffffffffffffffffff000000000000000000000001')
  }
  let G: cryptoFramework.Point = {
    x: BigInt('0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21'),
    y: BigInt('0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34')
  }
  let eccCommonSpec: cryptoFramework.ECCCommonParamsSpec = {
    algName: 'ECC',
    specType: cryptoFramework.AsyKeySpecType.COMMON\_PARAMS\_SPEC,
    field: fieldFp,
    a: BigInt('0xfffffffffffffffffffffffffffffffefffffffffffffffffffffffe'),
    b: BigInt('0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4'),
    g: G,
    n: BigInt('0xffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3d'),
    h: 1
  }
  return eccCommonSpec;
}

async function testgetAsyKeySpec() {
  let commKeySpec = genEccCommonSpec(); // Construct the EccCommonSpec object.
  let generatorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(commKeySpec); // Create an AsyKeyGenerator instance based on the EccCommonSpec object.
  let keyPair = await generatorBySpec.generateKeyPair();
  let key = keyPair.priKey;
  let p = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC\_FP\_P\_BN);
  console.info('ecc item --- p: ' + p.toString(16));
}

#### \[h2\]getEncodedDer12+

getEncodedDer(format: string): DataBlob

Obtains the private key data that complies with the ASN.1 syntax and DER encoding based on the specified format (such as the key specifications). Currently, only the ECC private key data in PKCS #8 format can be obtained.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/jSFAMZ2jTAWJFe5NvpvPTA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F5540EFAF39F53F7AB05D59B6E2C43F59D5BA6B176D0CC40F903EC910B155CB)

The difference between [Key.getEncoded()](#getencoded) and this API is as follows:

1.  You can specify the format of the key data to be obtained in this API. Currently, the ECC private key data in PKCS #8 format is supported.
2.  The format of the key data to be obtained cannot be specified in [Key.getEncoded()](#getencoded).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| format | string | Yes | Format of the key. Currently, only **PKCS8** is supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataBlob](#datablob) | ECC private key data obtained. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testGetEncodedDer() {
  let eccGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
    // Use AsyKeyGenerator to randomly generate an asymmetric key pair.
    let keyGenPromise = eccGenerator.generateKeyPair();
    keyGenPromise.then(keyPair => {
      let priKey = keyPair.priKey;
      let returnBlob = priKey.getEncodedDer('PKCS8');
      console.info('returnBlob data: ' + returnBlob.data);
    });
}

#### \[h2\]getEncodedPem12+

getEncodedPem(format: string): string

Obtains the key data. This API returns the result synchronously. The key can be an RSA public or private key. The private key must comply with the PKCS #8 and PKCS #1 specifications and be encoded in PEM.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| format | string | Yes | Encoding format of the key data to obtain. The format of a private key can be **'PKCS1'** or **'PKCS8'**. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Key data obtained. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let priKeyPkcs1Str1024: string =
  '-----BEGIN RSA PRIVATE KEY-----\\n'
    + 'MIICXQIBAAKBgQCwIN3mr21+N96ToxnVnaS+xyK9cNRAHiHGgrbjHw6RAj3V+l+W\\n'
    + 'Y68IhIe3DudVlzE9oMjeOQwkMkq//HCxNlIlFR6O6pa0mrXSwPRE7YKG97CeKk2g\\n'
    + 'YOS8YEh8toAvm7xKbiLkXuuMlxrjP2j/mb5iI/UASFSPZiQ/IyxDr0AQaQIDAQAB\\n'
    + 'AoGAEvBFzBNa+7J4PXnRQlYEK/tvsd0bBZX33ceacMubHl6WVZbphltLq+fMTBPP\\n'
    + 'LjXmtpC+aJ7Lvmyl+wTi/TsxE9vxW5JnbuRT48rnZ/Xwq0eozDeEeIBRrpsr7Rvr\\n'
    + '7ctrgzr4m4yMHq9aDgpxj8IR7oHkfwnmWr0wM3FuiVlj650CQQDineeNZ1hUTkj4\\n'
    + 'D3O+iCi3mxEVEeJrpqrmSFolRMb+iozrIRKuJlgcOs+Gqi2fHfOTTL7LkpYe8SVg\\n'
    + 'e3JxUdVLAkEAxvcZXk+byMFoetrnlcMR13VHUpoVeoV9qkv6CAWLlbMdgf7uKmgp\\n'
    + 'a1Yp3QPDNQQqkPvrqtfR19JWZ4uy1qREmwJALTU3BjyBoH/liqb6fh4HkWk75Som\\n'
    + 'MzeSjFIOubSYxhq5tgZpBZjcpvUMhV7Zrw54kwASZ+YcUJvmyvKViAm9NQJBAKF7\\n'
    + 'DyXSKrem8Ws0m1ybM7HQx5As6l3EVhePDmDQT1eyRbKp+xaD74nkJpnwYdB3jyyY\\n'
    + 'qc7A1tj5J5NmeEFolR0CQQCn76Xp8HCjGgLHw9vg7YyIL28y/XyfFyaZAzzK+Yia\\n'
    + 'akNwQ6NeGtXSsuGCcyyfpacHp9xy8qXQNKSkw03/5vDO\\n'
    + '-----END RSA PRIVATE KEY-----\\n';

function TestPriKeyPkcs1ToPkcs8BySync1024() {
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let keyPair = rsaGenerator.convertPemKeySync(null, priKeyPkcs1Str1024);
  let priPemKey = keyPair.priKey;
  let priString = priPemKey.getEncodedPem('PKCS8');
  console.info('\[sync\]TestPriKeyPkcs1ToPkcs8BySync1024 priString output = ' + priString);
}

#### \[h2\]getEncodedPem18+

getEncodedPem(format: string, config: KeyEncodingConfig): string

Obtains the key data. This API returns the result synchronously. The key can be an RSA public or private key. The private key must comply with PKCS #8 or PKCS #1 specifications and be encoded in PEM.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| format | string | Yes | Encoding format of the key data to obtain. The format of a private key can be **'PKCS1'** or **'PKCS8'**. |
| config | [KeyEncodingConfig](#keyencodingconfig18) | Yes | Options (including the password and algorithm) for encoding the private key. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Key data obtained. If **config** is specified, the key obtained is encoded. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let priKeyPkcs1Str1024: string =
  '-----BEGIN RSA PRIVATE KEY-----\\n'
    + 'MIICXQIBAAKBgQCwIN3mr21+N96ToxnVnaS+xyK9cNRAHiHGgrbjHw6RAj3V+l+W\\n'
    + 'Y68IhIe3DudVlzE9oMjeOQwkMkq//HCxNlIlFR6O6pa0mrXSwPRE7YKG97CeKk2g\\n'
    + 'YOS8YEh8toAvm7xKbiLkXuuMlxrjP2j/mb5iI/UASFSPZiQ/IyxDr0AQaQIDAQAB\\n'
    + 'AoGAEvBFzBNa+7J4PXnRQlYEK/tvsd0bBZX33ceacMubHl6WVZbphltLq+fMTBPP\\n'
    + 'LjXmtpC+aJ7Lvmyl+wTi/TsxE9vxW5JnbuRT48rnZ/Xwq0eozDeEeIBRrpsr7Rvr\\n'
    + '7ctrgzr4m4yMHq9aDgpxj8IR7oHkfwnmWr0wM3FuiVlj650CQQDineeNZ1hUTkj4\\n'
    + 'D3O+iCi3mxEVEeJrpqrmSFolRMb+iozrIRKuJlgcOs+Gqi2fHfOTTL7LkpYe8SVg\\n'
    + 'e3JxUdVLAkEAxvcZXk+byMFoetrnlcMR13VHUpoVeoV9qkv6CAWLlbMdgf7uKmgp\\n'
    + 'a1Yp3QPDNQQqkPvrqtfR19JWZ4uy1qREmwJALTU3BjyBoH/liqb6fh4HkWk75Som\\n'
    + 'MzeSjFIOubSYxhq5tgZpBZjcpvUMhV7Zrw54kwASZ+YcUJvmyvKViAm9NQJBAKF7\\n'
    + 'DyXSKrem8Ws0m1ybM7HQx5As6l3EVhePDmDQT1eyRbKp+xaD74nkJpnwYdB3jyyY\\n'
    + 'qc7A1tj5J5NmeEFolR0CQQCn76Xp8HCjGgLHw9vg7YyIL28y/XyfFyaZAzzK+Yia\\n'
    + 'akNwQ6NeGtXSsuGCcyyfpacHp9xy8qXQNKSkw03/5vDO\\n'
    + '-----END RSA PRIVATE KEY-----\\n';

function TestPriKeyPkcs1Encoded() {
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let keyPair = rsaGenerator.convertPemKeySync(null, priKeyPkcs1Str1024);
  let options: cryptoFramework.KeyEncodingConfig = {
    password: '123456',
    cipherName: 'AES-128-CBC'
  }
  let priPemKey = keyPair.priKey;
  let priString = priPemKey.getEncodedPem('PKCS1', options);
  console.info('\[sync\]TestPriKeyPkcs1Encoded priString output = ' + priString);
}

#### KeyPair

Defines an asymmetric key pair, which includes a public key and a private key.

The asymmetric key pair can be generated by using the asymmetric key generator [AsyKeyGenerator](#asykeygenerator) or [AsyKeyGeneratorBySpec](#asykeygeneratorbyspec10).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/asy-PgXZQ3SyWjtpsgvKnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=857F5D9E397D43AFD41C5F0BD330B896752B83EF229DAD605EE2C556CE0A327F)

The **pubKey** and **priKey** objects are members of the **KeyPair** object. When the **KeyPair** object is out of the scope, its **pubKey** and **priKey** objects will be destructed.

The service must reference the **KeyPair** object instead of the internal **pubKey** or **priKey** object.

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| priKey | [PriKey](#prikey) | Yes | No | Private key. |
| pubKey | [PubKey](#pubkey) | Yes | No | Public key. |

#### cryptoFramework.createSymKeyGenerator

createSymKeyGenerator(algName: string): SymKeyGenerator

Creates a symmetric key generator instance with the specified algorithm.

For details about the supported specifications, see [Symmetric Key Generation and Conversion Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-sym-key-generation-conversion-spec).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.SymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Key.SymKey** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| algName | string | Yes | 
Algorithm to be used by the **symKeyGenerator** instance.

For details, see **String Parameter** in [Symmetric Key Generation and Conversion Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-sym-key-generation-conversion-spec).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [SymKeyGenerator](#symkeygenerator) | **symKeyGenerator** instance created. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 801 | this operation is not supported. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');

#### SymKeyGenerator

Provides APIs for using the **symKeyGenerator**.

Before using the APIs of this class, use [createSymKeyGenerator](#cryptoframeworkcreatesymkeygenerator) to create a **SymKeyGenerator** instance.

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.SymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Key.SymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| algName | string | Yes | No | Algorithm used by the **symKeyGenerator**. |

#### \[h2\]generateSymKey

generateSymKey(callback: AsyncCallback<SymKey>): void

Generates a random key using this symmetric key generator. This API uses an asynchronous callback to return the result.

This API can be used only after a **symKeyGenerator** instance is created by using [createSymKeyGenerator](#cryptoframeworkcreatesymkeygenerator).

**RAND\_priv\_bytes()** of OpenSSL can be used to generate random keys.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/Jv6cltChTniUrIl1pK0EzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C25F40DF9BED1BB9158FE07B7591D2C0B03FA2B95C6FDA028C52E8F87A7060C8)

For symmetric keys used in the HMAC algorithm, if a hash algorithm (for example, **HMAC|SHA256**) is specified when the symmetric key generator is created, a binary key matching the hash length (for example, a 256-bit key) will be randomly generated. If no hash algorithm is specified, for example, only **HMAC** is specified, random symmetric key generation is not supported. You can generate symmetric key data using [convertKey](#convertkey).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.SymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Key.SymKey** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[SymKey](#symkey)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the symmetric key generated. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17620001 | memory operation failed. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
  symKeyGenerator.generateSymKey((err, symKey) => {
    console.info('Generate symKey result: success, algName: ' + symKey.algName);
  });

#### \[h2\]generateSymKey

generateSymKey(): Promise<SymKey>

Generates a random key using this symmetric key generator. This API uses a promise to return the result.

This API can be used only after a **symKeyGenerator** instance is created by using [createSymKeyGenerator](#cryptoframeworkcreatesymkeygenerator).

**RAND\_priv\_bytes()** of OpenSSL can be used to generate random keys.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.SymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Key.SymKey** since API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SymKey](#symkey)\> | Promise used to return the symmetric key generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17620001 | memory operation failed. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  symKeyGenerator.generateSymKey()
    .then(symKey => {
      console.info('Generate symKey result: success, algName: ' + symKey.algName);
    }).catch((error: BusinessError) => {
      console.error(\`Generate symKey failed, ${error.code}, ${error.message}\`);
    });

#### \[h2\]generateSymKeySync12+

generateSymKeySync(): SymKey

Generates a random key using this symmetric key generator. This API returns the result synchronously.

This API can be used only after a **symKeyGenerator** instance is created by using [createSymKeyGenerator](#cryptoframeworkcreatesymkeygenerator).

**RAND\_priv\_bytes()** of OpenSSL can be used to generate random keys.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/9UTfG9CgSTu96mSIXUpX9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=696BC56C1862E2220C66F51A37D7ABD377388073AEE1A54C6490005FE02EC3F1)

For symmetric keys used in the HMAC algorithm, if a hash algorithm (for example, **HMAC|SHA256**) is specified when the symmetric key generator is created, a binary key matching the hash length (for example, a 256-bit key) will be randomly generated.

If no hash algorithm is specified, for example, only **HMAC** is specified, random symmetric key generation is not supported. You can generate symmetric key data using [convertKeySync](#convertkeysync12).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.SymKey

**Return value**

| Type | Description |
| :-- | :-- |
| [SymKey](#symkey) | Symmetric key generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17620001 | memory operation failed. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function testGenerateSymKeySync() {
  // Create a SymKeyGenerator instance.
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES256');
  // Use SymKeyGenerator to randomly generate a symmetric key.
  let key = symKeyGenerator.generateSymKeySync();
  let encodedKey = key.getEncoded();
  console.info('key hex:' + encodedKey.data);
}

#### \[h2\]convertKey

convertKey(key: DataBlob, callback: AsyncCallback<SymKey>): void

Generates a symmetric key based on specified data. This API uses an asynchronous callback to return the result.

This API can be used only after a **symKeyGenerator** instance is created by using [createSymKeyGenerator](#cryptoframeworkcreatesymkeygenerator).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/MOp-CohmTR-av0RuAMBSWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26490FBAC732BCA31E3539B163B168EB240D1B68256637669BCF740D5D1F81F6)

For symmetric keys used in the HMAC algorithm, if a hash algorithm (for example, **HMAC|SHA256**) is specified when the symmetric key generator is created, the binary key data passed in must match the hash length (for example, a 256-bit key for SHA256).

If no hash algorithm is specified when the symmetric key generator is created (for example, only **HMAC** is specified), any binary key data with a length of 1 to 4096 bytes is supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.SymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Key.SymKey** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | [DataBlob](#datablob) | Yes | Data to convert. |
| callback | AsyncCallback<[SymKey](#symkey)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the symmetric key generated. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function genKeyMaterialBlob(): cryptoFramework.DataBlob {
  let arr = \[
    0xba, 0x3d, 0xc2, 0x71, 0x21, 0x1e, 0x30, 0x56,
    0xad, 0x47, 0xfc, 0x5a, 0x46, 0x39, 0xee, 0x7c,
    0xba, 0x3b, 0xc2, 0x71, 0xab, 0xa0, 0x30, 0x72\]; // keyLen = 192 (24 bytes)
  let keyMaterial = new Uint8Array(arr);
  return { data: keyMaterial };
}

function testConvertKey() {
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
  let keyMaterialBlob = genKeyMaterialBlob();
  symKeyGenerator.convertKey(keyMaterialBlob, (err, symKey) => {
    console.info('Convert symKey result: success, algName: ' + symKey.algName);
  });
}

#### \[h2\]convertKey

convertKey(key: DataBlob): Promise<SymKey>

Generates a symmetric key based on specified data. This API uses a promise to return the result.

Before using this API, create a symmetric key generator by using [createSymKeyGenerator](#cryptoframeworkcreatesymkeygenerator).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.SymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Key.SymKey** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | [DataBlob](#datablob) | Yes | Data to convert. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SymKey](#symkey)\> | Promise used to return the symmetric key generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

function genKeyMaterialBlob(): cryptoFramework.DataBlob {
  let arr = \[
    0xba, 0x3d, 0xc2, 0x71, 0x21, 0x1e, 0x30, 0x56,
    0xad, 0x47, 0xfc, 0x5a, 0x46, 0x39, 0xee, 0x7c,
    0xba, 0x3b, 0xc2, 0x71, 0xab, 0xa0, 0x30, 0x72\]; // keyLen = 192 (24 bytes)
  let keyMaterial = new Uint8Array(arr);
  return { data: keyMaterial };
}

function testConvertKey() {
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
  let keyMaterialBlob = genKeyMaterialBlob();
  symKeyGenerator.convertKey(keyMaterialBlob)
    .then(symKey => {
      console.info('Convert symKey result: success, algName: ' + symKey.algName);
    }).catch((error: BusinessError) => {
      console.error(\`Convert symKey failed, ${error.code}, ${error.message}\`);
    });
}

#### \[h2\]convertKeySync12+

convertKeySync(key: DataBlob): SymKey

Generates a symmetric key based on specified data.

This API can be used only after a **symKeyGenerator** instance is created by using [createSymKeyGenerator](#cryptoframeworkcreatesymkeygenerator).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/mcltBQXwSrCrMJM3Nt81Cw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=675A4CADD76190BACCD23728EB6DD057092F9FA8C8D2355C28878B2BCDFADB14)

For symmetric keys used in the HMAC algorithm, if a hash algorithm (for example, **HMAC|SHA256**) is specified when the symmetric key generator is created, the binary key data passed in must match the hash length (for example, a 256-bit key for SHA256). If no hash algorithm is specified when the symmetric key generator is created (for example, only **HMAC** is specified), any binary key data with a length of 1 to 4096 bytes is supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.SymKey

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | [DataBlob](#datablob) | Yes | Data to convert. |

**Return value**

| Type | Description |
| :-- | :-- |
| [SymKey](#symkey) | Symmetric key obtained. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function testConvertKeySync() {
  // The symmetric key length is 64 bytes (512 bits).
  let keyMessage = '87654321abcdefgh87654321abcdefgh87654321abcdefgh87654321abcdefgh';
  let keyBlob: cryptoFramework.DataBlob = {
    data : new Uint8Array(buffer.from(keyMessage, 'utf-8').buffer)
  }
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('HMAC');
  let key = symKeyGenerator.convertKeySync(keyBlob);
  let encodedKey = key.getEncoded();
  console.info('key encoded data: ' + encodedKey.data);
}

#### cryptoFramework.createAsyKeyGenerator

createAsyKeyGenerator(algName: string): AsyKeyGenerator

Creates an **AsyKeyGenerator** instance based on the specified algorithm.

For details about the supported specifications, see [Asymmetric Key Generation and Conversion Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| algName | string | Yes | Algorithm used by the asymmetric keys. For details, see the string parameters in [Asymmetric Key Generation and Conversion Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec). |

**Return value**

| Type | Description |
| :-- | :-- |
| [AsyKeyGenerator](#asykeygenerator) | **AsyKeyGenerator** instance created. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');

#### AsyKeyGenerator

Provides APIs for using the **AsKeyGenerator**. Before using any API of the **AsKeyGenerator** class, you must create an **AsyKeyGenerator** instance by using **createAsyKeyGenerator()**.

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| algName | string | Yes | No | Algorithm used by the **AsKeyGenerator**. |

#### \[h2\]generateKeyPair

generateKeyPair(callback: AsyncCallback<KeyPair>): void

Generates a random key pair using this asymmetric key generator. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[KeyPair](#keypair)\> | Yes | Callback used to return the asymmetric key pair generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

Incorrect parameter types;

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
asyKeyGenerator.generateKeyPair((err, keyPair) => {
  if (err) {
    console.error('generateKeyPair result: fail.');
    return;
  }
  console.info('generateKeyPair result: success.');
})

#### \[h2\]generateKeyPair

generateKeyPair(): Promise<KeyPair>

Generates a random key pair using this asymmetric key generator. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[KeyPair](#keypair)\> | Promise used to return the asymmetric key pair generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
let keyGenPromise = asyKeyGenerator.generateKeyPair();
keyGenPromise.then(keyPair => {
  console.info('generateKeyPair result: success.');
}).catch((error: BusinessError) => {
  console.error('generateKeyPair result: fail.');
});

#### \[h2\]generateKeyPairSync12+

generateKeyPairSync(): KeyPair

Generates a random key pair using this asymmetric key generator. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

**Return value**

| Type | Description |
| :-- | :-- |
| [KeyPair](#keypair) | Asymmetric key pair generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
try {
  let keyPairData = asyKeyGenerator.generateKeyPairSync();
  if (keyPairData != null) {
    console.info('\[Sync\]: key pair result: success.');
  } else {
    console.error('\[Sync\]: get key pair result: fail.');
  }
} catch (e) {
  console.error(\`sync failed: errCode: ${e.code}, errMsg: ${e.message}\`);
}

#### \[h2\]convertKey

convertKey(pubKey: DataBlob | null, priKey: DataBlob | null, callback: AsyncCallback<KeyPair>): void

Converts data into an asymmetric key pair. This API uses an asynchronous callback to return the result. For details, see **Key Conversion**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pubKey | [DataBlob](#datablob) | null10+ | Yes | Public key material to convert. If no public key needs to be converted, set this parameter to **null**. In versions earlier than API version 10, only **DataBlob** is supported. Since API version 10, **null** is also supported. |
| priKey | [DataBlob](#datablob) | null10+ | Yes | Private key material to convert. If no private key needs to be converted, set this parameter to **null**. In versions earlier than API version 10, only **DataBlob** is supported. Since API version 10, **null** is also supported. |
| callback | AsyncCallback<[KeyPair](#keypair)\> | Yes | Callback used to return the asymmetric key pair generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let pubKeyArray =
  new Uint8Array(\[48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7, 3, 66, 0, 4,
    83, 96, 142, 9, 86, 214, 126, 106, 247, 233, 92, 125, 4, 128, 138, 105, 246, 162, 215, 71, 81, 58, 202, 121, 26,
    105, 211, 55, 130, 45, 236, 143, 55, 16, 248, 75, 167, 160, 167, 106, 2, 152, 243, 44, 68, 66, 0, 167, 99, 92, 235,
    215, 159, 239, 28, 106, 124, 171, 34, 145, 124, 174, 57, 92\]);
let priKeyArray =
  new Uint8Array(\[48, 49, 2, 1, 1, 4, 32, 115, 56, 137, 35, 207, 0, 60, 191, 90, 61, 136, 105, 210, 16, 27, 4, 171, 57,
    10, 61, 123, 40, 189, 28, 34, 207, 236, 22, 45, 223, 10, 189, 160, 10, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7\]);
let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyArray }; // Binary data of the public key.
let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyArray }; // Binary data of the private key.
let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
asyKeyGenerator.convertKey(pubKeyBlob, priKeyBlob, (err, keyPair) => {
  if (err) {
    console.error('convertKey result: fail.');
    return;
  }
  console.info('convertKey result: success.');
});

#### \[h2\]convertKey

convertKey(pubKey: DataBlob | null, priKey: DataBlob | null): Promise<KeyPair>

Converts data into an asymmetric key pair. This API uses a promise to return the result. For details, see **Key Conversion**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pubKey | [DataBlob](#datablob) | null10+ | Yes | Public key material to convert. If no public key needs to be converted, set this parameter to **null**. In versions earlier than API version 10, only **DataBlob** is supported. Since API version 10, **null** is also supported. |
| priKey | [DataBlob](#datablob) | null10+ | Yes | Private key material to convert. If no private key needs to be converted, set this parameter to **null**. In versions earlier than API version 10, only **DataBlob** is supported. Since API version 10, **null** is also supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[KeyPair](#keypair)\> | Promise used to return the asymmetric key pair generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let pubKeyArray =
  new Uint8Array(\[48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7, 3, 66, 0, 4,
    83, 96, 142, 9, 86, 214, 126, 106, 247, 233, 92, 125, 4, 128, 138, 105, 246, 162, 215, 71, 81, 58, 202, 121, 26,
    105, 211, 55, 130, 45, 236, 143, 55, 16, 248, 75, 167, 160, 167, 106, 2, 152, 243, 44, 68, 66, 0, 167, 99, 92, 235,
    215, 159, 239, 28, 106, 124, 171, 34, 145, 124, 174, 57, 92\]);
let priKeyArray =
  new Uint8Array(\[48, 49, 2, 1, 1, 4, 32, 115, 56, 137, 35, 207, 0, 60, 191, 90, 61, 136, 105, 210, 16, 27, 4, 171, 57,
    10, 61, 123, 40, 189, 28, 34, 207, 236, 22, 45, 223, 10, 189, 160, 10, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7\]);
let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyArray }; // Binary data of the public key.
let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyArray }; // Binary data of the private key.
let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
let keyGenPromise = asyKeyGenerator.convertKey(pubKeyBlob, priKeyBlob);
keyGenPromise.then(keyPair => {
  console.info('convertKey result: success.');
}).catch((error: BusinessError) => {
  console.error(\`convertKey failed, errCode: ${error.code}, errMsg: ${error.message}\`);
});

#### \[h2\]convertKeySync12+

convertKeySync(pubKey: DataBlob | null, priKey: DataBlob | null): KeyPair

Converts data into an asymmetric key pair. This API returns the result synchronously. For details, see **Key Conversion**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pubKey | [DataBlob](#datablob) | null10+ | Yes | Public key material. If no public key needs to be converted, set this parameter to **null**. Before API version 10, only **DataBlob** is supported. Since API version 10s, **null** can be passed in. |
| priKey | [DataBlob](#datablob) | null10+ | Yes | Private key material. If no private key needs to be converted, set this parameter to **null**. Before API version 10, only **DataBlob** is supported. Since API version 10s, **null** can be passed in. |

**Return value**

| Type | Description |
| :-- | :-- |
| [KeyPair](#keypair) | Asymmetric key pair generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let pubKeyArray =
  new Uint8Array(\[48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7, 3, 66, 0, 4,
    83, 96, 142, 9, 86, 214, 126, 106, 247, 233, 92, 125, 4, 128, 138, 105, 246, 162, 215, 71, 81, 58, 202, 121, 26,
    105, 211, 55, 130, 45, 236, 143, 55, 16, 248, 75, 167, 160, 167, 106, 2, 152, 243, 44, 68, 66, 0, 167, 99, 92, 235,
    215, 159, 239, 28, 106, 124, 171, 34, 145, 124, 174, 57, 92\]);
let priKeyArray =
  new Uint8Array(\[48, 49, 2, 1, 1, 4, 32, 115, 56, 137, 35, 207, 0, 60, 191, 90, 61, 136, 105, 210, 16, 27, 4, 171, 57,
    10, 61, 123, 40, 189, 28, 34, 207, 236, 22, 45, 223, 10, 189, 160, 10, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7\]);
let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyArray }; // Binary data of the public key.
let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyArray }; // Binary data of the private key.
let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
try {
  let keyPairData = asyKeyGenerator.convertKeySync(pubKeyBlob, priKeyBlob);
  if (keyPairData != null) {
    console.info('\[Sync\]: key pair result: success.');
  } else {
    console.error('\[Sync\]: convert key pair result: fail.');
  }
} catch (e) {
  console.error(\`sync failed: errCode: ${e.code}, errMsg: ${e.message}\`);
}

**Key Conversion**

1.  For asymmetric keys (RSA, ECC, and DSA), calling **getEncoded()** on the public key returns binary data in X.509 format, and calling **getEncoded()** on the private key returns binary data in PKCS #8 format. For ECC private keys, the data returned is in the format defined in RFC 5915. These key data can be passed across applications and stored persistently.
2.  When **convertKey()** is used to convert binary data into an asymmetric key object defined by the Crypto framework, the public key must comply with the ASN.1 syntax, X.509 specifications, and DER encoding format, and the private key must comply with the ASN.1 syntax, PKCS #8 specifications, and DER encoding format.
3.  In **convertKey()**, you can pass in either **pubKey** or **priKey**, or both of them. If one of them is passed in, the returned **KeyPair** instance contains only the key converted from the data you passed in.
4.  When **convertKey** or **convertKeySync** is used, the system does not verify whether the specifications of the generated key object are the same as the key specifications specified for the asymmetric key generator.

#### \[h2\]convertPemKey12+

convertPemKey(pubKey: string | null, priKey: string | null): Promise<KeyPair>

Converts data into an asymmetric key pair. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/LlgwUTFTS_e7lmVRTnXLuQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6ED205C73178E880DF11702C4BA5D3F33D392CA0962BFB157341818B5E0DDE75)

1.  When **convertPemKey()** is used to convert an external string into an asymmetric key object defined by the Crypto framework, the public key must comply with the ASN.1 syntax, X.509 specifications, and PEM encoding format, and the private key must comply with the ASN.1 syntax, PKCS #8 specifications, and PEM encoding format.
2.  In **convertPemKey()**, you can pass in either **pubKey** or **priKey**, or both of them. If one of them is passed in, the returned **KeyPair** instance contains only the key converted from the data you passed in.
3.  When **convertPemKey** is used to convert an external string into an asymmetric key object defined by the Crypto framework, the system does not verify whether the specifications of the generated key object are the same as the key specifications specified for the asymmetric key generator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pubKey | string | null | Yes | Public key material to convert. If no public key needs to be converted, set this parameter to **null**. |
| priKey | string | null | Yes | 
Private key material to convert. If no private key needs to be converted, set this parameter to **null**.

Note: The public key and private key materials cannot be both null or empty strings.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[KeyPair](#keypair)\> | Promise used to return the asymmetric key pair generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let priKeyPkcs1Str1024: string =
  '-----BEGIN RSA PRIVATE KEY-----\\n'
    + 'MIICXQIBAAKBgQCwIN3mr21+N96ToxnVnaS+xyK9cNRAHiHGgrbjHw6RAj3V+l+W\\n'
    + 'Y68IhIe3DudVlzE9oMjeOQwkMkq//HCxNlIlFR6O6pa0mrXSwPRE7YKG97CeKk2g\\n'
    + 'YOS8YEh8toAvm7xKbiLkXuuMlxrjP2j/mb5iI/UASFSPZiQ/IyxDr0AQaQIDAQAB\\n'
    + 'AoGAEvBFzBNa+7J4PXnRQlYEK/tvsd0bBZX33ceacMubHl6WVZbphltLq+fMTBPP\\n'
    + 'LjXmtpC+aJ7Lvmyl+wTi/TsxE9vxW5JnbuRT48rnZ/Xwq0eozDeEeIBRrpsr7Rvr\\n'
    + '7ctrgzr4m4yMHq9aDgpxj8IR7oHkfwnmWr0wM3FuiVlj650CQQDineeNZ1hUTkj4\\n'
    + 'D3O+iCi3mxEVEeJrpqrmSFolRMb+iozrIRKuJlgcOs+Gqi2fHfOTTL7LkpYe8SVg\\n'
    + 'e3JxUdVLAkEAxvcZXk+byMFoetrnlcMR13VHUpoVeoV9qkv6CAWLlbMdgf7uKmgp\\n'
    + 'a1Yp3QPDNQQqkPvrqtfR19JWZ4uy1qREmwJALTU3BjyBoH/liqb6fh4HkWk75Som\\n'
    + 'MzeSjFIOubSYxhq5tgZpBZjcpvUMhV7Zrw54kwASZ+YcUJvmyvKViAm9NQJBAKF7\\n'
    + 'DyXSKrem8Ws0m1ybM7HQx5As6l3EVhePDmDQT1eyRbKp+xaD74nkJpnwYdB3jyyY\\n'
    + 'qc7A1tj5J5NmeEFolR0CQQCn76Xp8HCjGgLHw9vg7YyIL28y/XyfFyaZAzzK+Yia\\n'
    + 'akNwQ6NeGtXSsuGCcyyfpacHp9xy8qXQNKSkw03/5vDO\\n'
    + '-----END RSA PRIVATE KEY-----\\n';
let publicPkcs1Str1024: string =
  '-----BEGIN RSA PUBLIC KEY-----\\n'
    + 'MIGJAoGBALAg3eavbX433pOjGdWdpL7HIr1w1EAeIcaCtuMfDpECPdX6X5ZjrwiE\\n'
    + 'h7cO51WXMT2gyN45DCQySr/8cLE2UiUVHo7qlrSatdLA9ETtgob3sJ4qTaBg5Lxg\\n'
    + 'SHy2gC+bvEpuIuRe64yXGuM/aP+ZvmIj9QBIVI9mJD8jLEOvQBBpAgMBAAE=\\n'
    + '-----END RSA PUBLIC KEY-----\\n';

async function TestConvertPemKeyByPromise() {
  let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  asyKeyGenerator.convertPemKey(publicPkcs1Str1024, priKeyPkcs1Str1024)
    .then(keyPair => {
      console.info('convertPemKey result: success.');
    }).catch((error: BusinessError) => {
    console.error(\`convertPemKey failed: errCode: ${error.code}, errMsg: ${error.message}\`);
  });
}

#### \[h2\]convertPemKey18+

convertPemKey(pubKey: string | null, priKey: string | null, password: string): Promise<KeyPair>

Converts data into an asymmetric key pair. Encrypted private keys are supported. The private key password is synchronously passed to decrypt the private key. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/kEcl6v08SZmZ4SViIgS0FA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED29E26A822B6713E088795EC9573B9107EE9EA0B9BBBC0F92E0A4AB984FD9DF)

1.  When **convertPemKey()** is used to convert an external string into an asymmetric key object defined by the Crypto framework, the public key must comply with the ASN.1 syntax, X.509 specifications, and PEM encoding format, and the private key must comply with the ASN.1 syntax, PKCS #8 specifications, and PEM encoding format.
2.  In **convertPemKey()**, you can pass in either **pubKey** or **priKey**, or both of them. If one of them is passed in, the returned **KeyPair** instance contains only the key converted from the data you passed in.
3.  When **convertPemKey** is used to convert an external string into an asymmetric key object defined by the Crypto framework, the system does not verify whether the specifications of the generated key object are the same as the key specifications specified for the asymmetric key generator.
4.  If **password** is passed in, it can be used to decrypt the encrypted private key.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pubKey | string | null | Yes | Public key material to convert. If no public key needs to be converted, set this parameter to **null**. |
| priKey | string | null | Yes | 
Private key material to convert. If no private key needs to be converted, set this parameter to **null**.

Note: The public key and private key materials cannot be both null or empty strings.

 |
| password | string | Yes | Password used to decrypt the private key. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[KeyPair](#keypair)\> | Promise used to return the asymmetric key pair generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let priKeyPkcs1EncodingStr: string =
  '-----BEGIN RSA PRIVATE KEY-----\\n'
    + 'Proc-Type: 4,ENCRYPTED\\n'
    + 'DEK-Info: AES-128-CBC,815A066131BF05CF87CE610A59CC69AE\\n\\n'
    + '7Jd0vmOmYGFZ2yRY8fqRl3+6rQlFtNcMILvcb5KWHDSrxA0ULmJE7CW0DSRikHoA\\n'
    + 't0KgafhYXeQXh0dRy9lvVRAFSLHCLJVjchx90V7ZSivBFEq7+iTozVp4AlbgYsJP\\n'
    + 'vx/1sfZD2WAcyMJ7IDmJyft7xnpVSXsyWGTT4f3eaHJIh1dqjwrso7ucAW0FK6rp\\n'
    + '/TONyOoXNfXtRbVtxNyCWBxt4HCSclDZFvS9y8fz9ZwmCUV7jei/YdzyQI2wnE13\\n'
    + 'W8cKlpzRFL6BWi8XPrUtAw5MWeHBAPUgPWMfcmiaeyi5BJFhQCrHLi+Gj4EEJvp7\\n'
    + 'mP5cbnQAx6+paV5z9m71SKrI/WSc4ixsYYdVmlL/qwAK9YliFfoPl030YJWW6rFf\\n'
    + 'T7J9BUlHGUJ0RB2lURNNLakM+UZRkeE9TByzCzgTxuQtyv5Lwsh2mAk3ia5x0kUO\\n'
    + 'LHg3Eoabhdh+YZA5hHaxnpF7VjspB78E0F9Btq+A41rSJ6zDOdToHey4MJ2nxdey\\n'
    + 'Z3bi81TZ6Fp4IuROrvZ2B/Xl3uNKR7n+AHRKnaAO87ywzyltvjwSh2y3xhJueiRs\\n'
    + 'BiYkyL3/fnocD3pexTdN6h3JgQGgO5GV8zw/NrxA85mw8o9im0HreuFObmNj36T9\\n'
    + 'k5N+R/QIXW83cIQOLaWK1ThYcluytf0tDRiMoKqULiaA6HvDMigExLxuhCtnoF8I\\n'
    + 'iOLN1cPdEVQjzwDHLqXP2DbWW1z9iRepLZlEm1hLRLEmOrTGKezYupVv306SSa6J\\n'
    + 'OA55lAeXMbyjFaYCr54HWrpt4NwNBX1efMUURc+1LcHpzFrBTTLbfjIyq6as49pH\\n'
    + '-----END RSA PRIVATE KEY-----\\n'

async function TestConvertPemKeyByPromise() {
  let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  asyKeyGenerator.convertPemKey(null, priKeyPkcs1EncodingStr, '123456')
    .then(keyPair => {
      console.info('convertPemKey result: success.');
    }).catch((error: BusinessError) => {
    console.error(\`convertPemKey failed: errCode: ${error.code}, errMsg: ${error.message}\`);
  });
}

#### \[h2\]convertPemKeySync12+

convertPemKeySync(pubKey: string | null, priKey: string | null): KeyPair

Converts data into an asymmetric key pair. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/3A04PEnBRp2BTC7iOcx0aQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65E073678E65177D6DFA0F26E7814B624BEEC12322942188446EB8B0F8B315EB)

The precautions for using **convertPemKeySync** are the same as those for **convertPemKey**. For details, see the description of [convertPemKey](#convertpemkey12).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pubKey | string | null | Yes | Public key material to convert. If no public key needs to be converted, set this parameter to **null**. |
| priKey | string | null | Yes | 
Private key material. If no private key needs to be converted, set this parameter to **null**.

Note: The public key and private key materials cannot be both null or empty strings.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [KeyPair](#keypair) | Asymmetric key pair generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let priKeyPkcs1Str1024: string =
  '-----BEGIN RSA PRIVATE KEY-----\\n'
    + 'MIICXQIBAAKBgQCwIN3mr21+N96ToxnVnaS+xyK9cNRAHiHGgrbjHw6RAj3V+l+W\\n'
    + 'Y68IhIe3DudVlzE9oMjeOQwkMkq//HCxNlIlFR6O6pa0mrXSwPRE7YKG97CeKk2g\\n'
    + 'YOS8YEh8toAvm7xKbiLkXuuMlxrjP2j/mb5iI/UASFSPZiQ/IyxDr0AQaQIDAQAB\\n'
    + 'AoGAEvBFzBNa+7J4PXnRQlYEK/tvsd0bBZX33ceacMubHl6WVZbphltLq+fMTBPP\\n'
    + 'LjXmtpC+aJ7Lvmyl+wTi/TsxE9vxW5JnbuRT48rnZ/Xwq0eozDeEeIBRrpsr7Rvr\\n'
    + '7ctrgzr4m4yMHq9aDgpxj8IR7oHkfwnmWr0wM3FuiVlj650CQQDineeNZ1hUTkj4\\n'
    + 'D3O+iCi3mxEVEeJrpqrmSFolRMb+iozrIRKuJlgcOs+Gqi2fHfOTTL7LkpYe8SVg\\n'
    + 'e3JxUdVLAkEAxvcZXk+byMFoetrnlcMR13VHUpoVeoV9qkv6CAWLlbMdgf7uKmgp\\n'
    + 'a1Yp3QPDNQQqkPvrqtfR19JWZ4uy1qREmwJALTU3BjyBoH/liqb6fh4HkWk75Som\\n'
    + 'MzeSjFIOubSYxhq5tgZpBZjcpvUMhV7Zrw54kwASZ+YcUJvmyvKViAm9NQJBAKF7\\n'
    + 'DyXSKrem8Ws0m1ybM7HQx5As6l3EVhePDmDQT1eyRbKp+xaD74nkJpnwYdB3jyyY\\n'
    + 'qc7A1tj5J5NmeEFolR0CQQCn76Xp8HCjGgLHw9vg7YyIL28y/XyfFyaZAzzK+Yia\\n'
    + 'akNwQ6NeGtXSsuGCcyyfpacHp9xy8qXQNKSkw03/5vDO\\n'
    + '-----END RSA PRIVATE KEY-----\\n';
let publicPkcs1Str1024: string =
  '-----BEGIN RSA PUBLIC KEY-----\\n'
    + 'MIGJAoGBALAg3eavbX433pOjGdWdpL7HIr1w1EAeIcaCtuMfDpECPdX6X5ZjrwiE\\n'
    + 'h7cO51WXMT2gyN45DCQySr/8cLE2UiUVHo7qlrSatdLA9ETtgob3sJ4qTaBg5Lxg\\n'
    + 'SHy2gC+bvEpuIuRe64yXGuM/aP+ZvmIj9QBIVI9mJD8jLEOvQBBpAgMBAAE=\\n'
    + '-----END RSA PUBLIC KEY-----\\n';

function TestConvertPemKeyBySync() {
  let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  try {
    let keyPairData = asyKeyGenerator.convertPemKeySync(publicPkcs1Str1024, priKeyPkcs1Str1024);
    if (keyPairData != null) {
      console.info('\[Sync\]: convert pem key pair result: success.');
    } else {
      console.error('\[Sync\]: convert pem key pair result: fail.');
    }
  } catch (e) {
    console.error(\`Sync failed: errCode: ${e.code}, errMsg: ${e.message}\`);
  }
}

#### \[h2\]convertPemKeySync18+

convertPemKeySync(pubKey: string | null, priKey: string | null, password: string): KeyPair

Converts data into an asymmetric key pair. Encrypted private keys are supported. The private key password is synchronously passed to decrypt the private key. This API is synchronous.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/4RDFrivTRKu_pvtPjD1hew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2BA451299B65759E033B63937B458AC307B4B60142A41C72E2400875321F274)

The precautions for using **convertPemKeySync** are the same as those for [convertPemKey](#convertpemkey18).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pubKey | string | null | Yes | Public key material to convert. If no public key needs to be converted, set this parameter to **null**. |
| priKey | string | null | Yes | 
Private key material. If no private key needs to be converted, set this parameter to **null**.

Note: **pubKey** and **priKey** cannot be **null** at the same time.

 |
| password | string | Yes | Password used to decrypt the private key. |

**Return value**

| Type | Description |
| :-- | :-- |
| [KeyPair](#keypair) | Asymmetric key pair generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let priKeyPkcs1EncodingStr: string =
  '-----BEGIN RSA PRIVATE KEY-----\\n'
    + 'Proc-Type: 4,ENCRYPTED\\n'
    + 'DEK-Info: AES-128-CBC,815A066131BF05CF87CE610A59CC69AE\\n\\n'
    + '7Jd0vmOmYGFZ2yRY8fqRl3+6rQlFtNcMILvcb5KWHDSrxA0ULmJE7CW0DSRikHoA\\n'
    + 't0KgafhYXeQXh0dRy9lvVRAFSLHCLJVjchx90V7ZSivBFEq7+iTozVp4AlbgYsJP\\n'
    + 'vx/1sfZD2WAcyMJ7IDmJyft7xnpVSXsyWGTT4f3eaHJIh1dqjwrso7ucAW0FK6rp\\n'
    + '/TONyOoXNfXtRbVtxNyCWBxt4HCSclDZFvS9y8fz9ZwmCUV7jei/YdzyQI2wnE13\\n'
    + 'W8cKlpzRFL6BWi8XPrUtAw5MWeHBAPUgPWMfcmiaeyi5BJFhQCrHLi+Gj4EEJvp7\\n'
    + 'mP5cbnQAx6+paV5z9m71SKrI/WSc4ixsYYdVmlL/qwAK9YliFfoPl030YJWW6rFf\\n'
    + 'T7J9BUlHGUJ0RB2lURNNLakM+UZRkeE9TByzCzgTxuQtyv5Lwsh2mAk3ia5x0kUO\\n'
    + 'LHg3Eoabhdh+YZA5hHaxnpF7VjspB78E0F9Btq+A41rSJ6zDOdToHey4MJ2nxdey\\n'
    + 'Z3bi81TZ6Fp4IuROrvZ2B/Xl3uNKR7n+AHRKnaAO87ywzyltvjwSh2y3xhJueiRs\\n'
    + 'BiYkyL3/fnocD3pexTdN6h3JgQGgO5GV8zw/NrxA85mw8o9im0HreuFObmNj36T9\\n'
    + 'k5N+R/QIXW83cIQOLaWK1ThYcluytf0tDRiMoKqULiaA6HvDMigExLxuhCtnoF8I\\n'
    + 'iOLN1cPdEVQjzwDHLqXP2DbWW1z9iRepLZlEm1hLRLEmOrTGKezYupVv306SSa6J\\n'
    + 'OA55lAeXMbyjFaYCr54HWrpt4NwNBX1efMUURc+1LcHpzFrBTTLbfjIyq6as49pH\\n'
    + '-----END RSA PRIVATE KEY-----\\n'

function TestConvertPemKeyBySync() {
  let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  try {
    let keyPairData = asyKeyGenerator.convertPemKeySync(null, priKeyPkcs1EncodingStr, '123456');
    if (keyPairData != null) {
      console.info('\[Sync\]: convert pem key pair result: success.');
    } else {
      console.error('\[Sync\]: convert pem key pair result: fail.');
    }
  } catch (e) {
    console.error(\`Sync failed: errCode: ${e.code}, errMsg: ${e.message}\`);
  }
}

#### cryptoFramework.createAsyKeyGeneratorBySpec10+

createAsyKeyGeneratorBySpec(asyKeySpec: AsyKeySpec): AsyKeyGeneratorBySpec

Obtains an asymmetric key generator instance with the specified key parameters.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| asyKeySpec | [AsyKeySpec](#asykeyspec10) | Yes | 
Key parameters. The **AsyKeyGenerator** generates the public/private key based on the specified parameters.

For details about the supported specifications, see [Asymmetric Key Generation and Conversion Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [AsyKeyGeneratorBySpec](#asykeygeneratorbyspec10) | Returns the **AsyKeyGenerator** instance created. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// Set the common parameters of the DSA1024 public and private keys.
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON\_PARAMS\_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// Set full parameters of the DSA1024 key pair.
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY\_PAIR\_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // The input in JS must be a positive number in big-endian format.
let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);

#### AsyKeyGeneratorBySpec10+

Provides APIs for using the **AsKeyGenerator**. Before using the APIs of this class, you need to use [createAsyKeyGeneratorBySpec()](#cryptoframeworkcreateasykeygeneratorbyspec10) to create an **AsyKeyGeneratorBySpec** instance.

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| algName | string | Yes | No | Algorithm used by the asymmetric key generator. |

#### \[h2\]generateKeyPair10+

generateKeyPair(callback: AsyncCallback<KeyPair>): void

Generates a key pair using this asymmetric key generator. This API uses an asynchronous callback to return the result.

If a key parameter of the [COMMON\_PARAMS\_SPEC](#asykeyspectype10) type is used to create the key generator, a key pair will be randomly generated. If a key parameter of the [KEY\_PAIR\_SPEC](#asykeyspectype10) type is used to create the key generator, you can obtain a key pair that is consistent with the specified key parameters.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[KeyPair](#keypair)\> | Yes | Callback used to return the asymmetric key pair generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

Incorrect parameter types;

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// Set the common parameters of the DSA1024 public and private keys.
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON\_PARAMS\_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// Set full parameters of the DSA1024 key pair.
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY\_PAIR\_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGenerateKeyPair() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // The input in JS must be a positive number in big-endian format.
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  asyKeyGeneratorBySpec.generateKeyPair((err, keyPair) => {
    if (err) {
      console.error('generateKeyPair result: fail.');
      return;
    }
    console.info('generateKeyPair result: success.');
  })
}

#### \[h2\]generateKeyPair10+

generateKeyPair(): Promise<KeyPair>

Generates a key pair using this asymmetric key generator. This API uses a promise to return the result.

If a key parameter of the [COMMON\_PARAMS\_SPEC](#asykeyspectype10) type is used to create the key generator, a key pair will be randomly generated. If a key parameter of the [KEY\_PAIR\_SPEC](#asykeyspectype10) type is used to create the key generator, you can obtain a key pair that is consistent with the specified key parameters.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[KeyPair](#keypair)\> | Promise used to return the asymmetric key pair generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Set the common parameters of the DSA1024 public and private keys.
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON\_PARAMS\_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// Set full parameters of the DSA1024 key pair.
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY\_PAIR\_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGenerateKeyPair() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // The input in JS must be a positive number in big-endian format.
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  let keyGenPromise = asyKeyGeneratorBySpec.generateKeyPair();
  keyGenPromise.then(keyPair => {
    console.info('generateKeyPair result: success.');
  }).catch((error: BusinessError) => {
    console.error(\`generateKeyPair failed: errCode: ${error.code}, errMsg: ${error.message}\`);
  });
}

#### \[h2\]generateKeyPairSync12+

generateKeyPairSync(): KeyPair

Generates a key pair using this asymmetric key generator. This API returns the result synchronously.

If a key parameter of the [COMMON\_PARAMS\_SPEC](#asykeyspectype10) type is used to create the key generator, a key pair will be randomly generated. If a key parameter of the [KEY\_PAIR\_SPEC](#asykeyspectype10) type is used to create the key generator, you can obtain a key pair that is consistent with the specified key parameters.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

**Return value**

| Type | Description |
| :-- | :-- |
| [KeyPair](#keypair) | Asymmetric key pair generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Set the common parameters of the DSA1024 public and private keys.
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON\_PARAMS\_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// Set full parameters of the DSA1024 key pair.
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY\_PAIR\_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGenerateKeyPairSync() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // The input in JS must be a positive number in big-endian format.
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  try {
    let keyPairData = asyKeyGeneratorBySpec.generateKeyPairSync();
    if (keyPairData != null) {
      console.info('\[Sync\]: key pair result: success.');
    } else {
      console.error('\[Sync\]: get key pair result: fail.');
    }
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`sync failed: errCode: ${error.code}, errMsg: ${error.message}\`);
  }
}

#### \[h2\]generatePriKey10+

generatePriKey(callback: AsyncCallback<PriKey>): void

Generates a private key using this asymmetric key generator. This API uses an asynchronous callback to return the result.

If [PRIVATE\_KEY\_SPEC](#asykeyspectype10) is used to create a key generator, the key generator generates the specified private key. If [KEY\_PAIR\_SPEC](#asykeyspectype10) is used to create a key generator, you can obtain the specified private key from the key pair generated.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[PriKey](#prikey)\> | Yes | Callback used to return the asymmetric key pair generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

Mandatory parameters are left unspecified;

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// Set the common parameters of the DSA1024 public and private keys.
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON\_PARAMS\_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// Set full parameters of the DSA1024 key pair.
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY\_PAIR\_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGeneratePriKey() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // The input in JS must be a positive number in big-endian format.
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  asyKeyGeneratorBySpec.generatePriKey((err, prikey) => {
    if (err) {
      console.error('generatePriKey result: fail.');
      return;
    }
    console.info('generatePriKey result: success.');
  })
}

#### \[h2\]generatePriKey10+

generatePriKey(): Promise<PriKey>

Generates a private key using this asymmetric key generator. This API uses a promise to return the result.

If a key parameter of the [PRIVATE\_KEY\_SPEC](#asykeyspectype10) type is used to create the key generator, a private key can be obtained. If a key parameter of the [KEY\_PAIR\_SPEC](#asykeyspectype10) type is used to create the key generator, you can obtain the private key from the key pair generated.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PriKey](#prikey)\> | Promise used to return the private key generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Set the common parameters of the DSA1024 public and private keys.
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON\_PARAMS\_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// Set full parameters of the DSA1024 key pair.
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY\_PAIR\_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGeneratePriKey() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // The input in JS must be a positive number in big-endian format.
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  let keyGenPromise = asyKeyGeneratorBySpec.generatePriKey();
  keyGenPromise.then(priKey => {
    console.info('generatePriKey result: success.');
  }).catch((error: BusinessError) => {
    console.error(\`generatePriKey failed: errCode: ${error.code}, errMsg: ${error.message}\`);
  });
}

#### \[h2\]generatePriKeySync12+

generatePriKeySync(): PriKey

Generates a private key using this asymmetric key generator. This API returns the result synchronously.

If a key parameter of the [PRIVATE\_KEY\_SPEC](#asykeyspectype10) type is used to create the key generator, a private key can be obtained. If a key parameter of the [KEY\_PAIR\_SPEC](#asykeyspectype10) type is used to create the key generator, you can obtain the private key from the key pair generated.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

**Return value**

| Type | Description |
| :-- | :-- |
| [PriKey](#prikey) | Private key generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// Set the common parameters of the DSA1024 public and private keys.
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON\_PARAMS\_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// Set full parameters of the DSA1024 key pair.
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY\_PAIR\_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGeneratePriKeySync() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // The input in JS must be a positive number in big-endian format.
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  try {
    let priKeyData = asyKeyGeneratorBySpec.generatePriKeySync();
    if (priKeyData != null) {
      console.info('\[Sync\]: pri key result: success.');
    } else {
      console.error('\[Sync\]: get pri key result: fail.');
    }
  } catch (e) {
    console.error(\`sync failed: errCode: ${e.code}, errMsg: ${e.message}\`);
  }
}

#### \[h2\]generatePubKey10+

generatePubKey(callback: AsyncCallback<PubKey>): void

Generates a public key using this asymmetric key generator. This API uses an asynchronous callback to return the result.

If a key parameter of the [PUBLIC\_KEY\_SPEC](#asykeyspectype10) type is used to create the key generator, the specified public key can be obtained. If a key parameter of the [KEY\_PAIR\_SPEC](#asykeyspectype10) type is used to create the key generator, you can obtain the specified public key from the key pair generated.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[PubKey](#pubkey)\> | Yes | Callback used to return the asymmetric key pair generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

Incorrect parameter types;

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// Set the common parameters of the DSA1024 public and private keys.
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON\_PARAMS\_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// Set full parameters of the DSA1024 key pair.
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY\_PAIR\_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGeneratePubKey() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // The input in JS must be a positive number in big-endian format.
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  asyKeyGeneratorBySpec.generatePubKey((err, pubKey) => {
    if (err) {
      console.error('generatePubKey result: fail.');
      return;
    }
    console.info('generatePubKey result: success.');
  })
}

#### \[h2\]generatePubKey10+

generatePubKey(): Promise<PubKey>

Generates a public key using this asymmetric key generator. This API uses a promise to return the result.

If a key parameter of the [PUBLIC\_KEY\_SPEC](#asykeyspectype10) type is used to create the key generator, the specified public key can be obtained. If a key parameter of the [KEY\_PAIR\_SPEC](#asykeyspectype10) type is used to create the key generator, you can obtain the specified public key from the key pair generated.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PubKey](#pubkey)\> | Promise used to return the public key generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Set the common parameters of the DSA1024 public and private keys.
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON\_PARAMS\_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// Set full parameters of the DSA1024 key pair.
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY\_PAIR\_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGeneratePubKey() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // The input in JS must be a positive number in big-endian format.
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  let keyGenPromise = asyKeyGeneratorBySpec.generatePubKey();
  keyGenPromise.then(pubKey => {
    console.info('generatePubKey result: success.');
  }).catch((error: BusinessError) => {
    console.error(\`generatePubKey failed: errCode: ${error.code}, errMsg: ${error.message}\`);
  });
}

#### \[h2\]generatePubKeySync12+

generatePubKeySync(): PubKey

Generates a public key using this asymmetric key generator. This API returns the result synchronously.

If [PUBLIC\_KEY\_SPEC](#asykeyspectype10) is used to create a key generator, the key generator generates the specified public key. If [KEY\_PAIR\_SPEC](#asykeyspectype10) is used to create a key generator, you can obtain the specified public key from the key pair generated.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

**Return value**

| Type | Description |
| :-- | :-- |
| [PubKey](#pubkey) | Public key generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// Set the common parameters of the DSA1024 public and private keys.
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON\_PARAMS\_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// Set full parameters of the DSA1024 key pair.
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY\_PAIR\_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGeneratePubKeySync() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // The input in JS must be a positive number in big-endian format.
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  try {
    let pubKeyData = asyKeyGeneratorBySpec.generatePubKeySync();
    if (pubKeyData != null) {
      console.info('\[Sync\]: pub key result: success.');
    } else {
      console.error('\[Sync\]: get pub key result: fail.');
    }
  } catch (e) {
    console.error(\`sync failed: errCode: ${e.code}, errMsg: ${e.message}\`);
  }
}

#### ECCKeyUtil11+

Generates common parameters for an asymmetric key pair based on the specified elliptic curve name.

#### \[h2\]genECCCommonParamsSpec11+

static genECCCommonParamsSpec(curveName: string): ECCCommonParamsSpec

Generates common parameters for an asymmetric key pair based on the specified name identifier (NID) of an elliptic curve. For details, see [ECC](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#ecc) and [SM2](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#sm2).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API version 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| curveName | string | Yes | NID of the elliptic curve. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ECCCommonParamsSpec](#ecccommonparamsspec10) | ECC common parameters generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let ECCCommonParamsSpec = cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID\_brainpoolP160r1');
    console.info('genECCCommonParamsSpec result: success.');
} catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(\`genECCCommonParamsSpec failed: errCode: ${e.code}, errMsg: ${e.message}\`);
}

#### \[h2\]convertPoint12+

static convertPoint(curveName: string, encodedPoint: Uint8Array): Point

Converts the specified point data into a **Point** object based on the curve name (NID). Currently, compressed and uncompressed point data is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/UrYLSWTETc-CQX0ePPluwg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=399D4F2BD39678C1649606BEC3C9750A45633FB8C6B4AD407706DB1B74BA3977)

According to section 2.2 in RFC 5480:

1.  The uncompressed point data is represented as **0x04**|x coordinate|y coordinate.
2.  The compressed point data in the **Fp** field (the **F2m** field is not supported currently) is represented as follows: **0x03**|x coordinate (when the coordinate y is an odd number); **0x02**|x coordinate (when the coordinate y is an even number).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| curveName | string | Yes | Elliptic curve name, that is, the NID. |
| encodedPoint | Uint8Array | Yes | Data of the point on the ECC elliptic curve to convert. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Point](#point10) | **Point** object obtained. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// Randomly generated uncompressed point data.
let pkData =
  new Uint8Array(\[4, 143, 39, 57, 249, 145, 50, 63, 222, 35, 70, 178, 121, 202, 154, 21, 146, 129, 75, 76, 63, 8, 195,
    157, 111, 40, 217, 215, 148, 120, 224, 205, 82, 83, 92, 185, 21, 211, 184, 5, 19, 114, 33, 86, 85, 228, 123, 242,
    206, 200, 98, 178, 184, 130, 35, 232, 45, 5, 202, 189, 11, 46, 163, 156, 152\]);
let returnPoint = cryptoFramework.ECCKeyUtil.convertPoint('NID\_brainpoolP256r1', pkData);
console.info('returnPoint: ' + returnPoint.x.toString(16));

#### \[h2\]getEncodedPoint12+

static getEncodedPoint(curveName: string, point: Point, format: string): Uint8Array

Obtains the point data in the specified format from a **Point** object. Currently, compressed and uncompressed point data is supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| curveName | string | Yes | Elliptic curve name, that is, the NID. |
| point | [Point](#point10) | Yes | **Point** object of the elliptic curve. |
| format | string | Yes | Format of the point data to obtain. Currently, the value can be **COMPRESSED** or **UNCOMPRESSED** only. |

**Return value**

| Type | Description |
| :-- | :-- |
| Uint8Array | Point data in the specified format. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function doTest() {
  let generator = cryptoFramework.createAsyKeyGenerator('ECC\_BrainPoolP256r1');
  let keyPair = await generator.generateKeyPair();
  let eccPkX = keyPair.pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC\_PK\_X\_BN);
  let eccPkY = keyPair.pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC\_PK\_Y\_BN);
  console.info('ECC\_PK\_X\_BN 16: ' + eccPkX.toString(16));
  console.info('ECC\_PK\_Y\_BN 16: ' + eccPkY.toString(16));
  // Place eccPkX.toString(16) in x and eccPkY.toString(16) in y.
  let returnPoint: cryptoFramework.Point = {
    x: BigInt('0x' + eccPkX.toString(16)),
    y: BigInt('0x' + eccPkY.toString(16))
  };
  let returnData = cryptoFramework.ECCKeyUtil.getEncodedPoint('NID\_brainpoolP256r1', returnPoint, 'UNCOMPRESSED');
  console.info('returnData: ' + returnData);
}

#### DHKeyUtil11+

Generates common parameters for a DH key based on the prime **p** length and the private key length.

#### \[h2\]genDHCommonParamsSpec11+

static genDHCommonParamsSpec(pLen: number, skLen?: number): DHCommonParamsSpec

Generates common parameters for a DH key based on the prime **p** length and the private key length. For details, see [DH](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#dh).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Key.AsymKey

The system capability is **SystemCapability.Security.CryptoFramework** in API version 11, and **SystemCapability.Security.CryptoFramework.Key.AsymKey** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pLen | number | Yes | Length of the prime **p**, in bits. |
| skLen | number | No | 
Maximum length of the generated DH private key, in bits. The default value is **0**.

When this parameter is set to **0**, the maximum length of the generated DH private key is as follows:

ffdhe2048: 255 bits.

ffdhe3072: 275 bits.

ffdhe4096: 325 bits.

ffdhe6144: 375 bits.

ffdhe8192: 400 bits.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DHCommonParamsSpec](#dhcommonparamsspec11) | DH common parameters generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let DHCommonParamsSpec = cryptoFramework.DHKeyUtil.genDHCommonParamsSpec(2048);
    console.info('genDHCommonParamsSpec result: success.');
} catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(\`genDHCommonParamsSpec failed: errCode: ${e.code}, errMsg: ${e.message}\`);
}

#### SM2CryptoUtil12+

Provides APIs for SM2 cryptographic operations.

#### \[h2\]genCipherTextBySpec12+

static genCipherTextBySpec(spec: SM2CipherTextSpec, mode?: string): DataBlob

Generates SM2 ciphertext in ASN.1 format.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| spec | [SM2CipherTextSpec](#sm2ciphertextspec12) | Yes | SM2 ciphertext parameters. |
| mode | string | No | Order of the SM2 parameters in the ciphertext. Currently, only C1C3C2 is supported. If this parameter is left empty or is an empty string, the default value is used. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataBlob](#datablob) | SM2 ciphertext in ASN.1 format. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let spec: cryptoFramework.SM2CipherTextSpec = {
    xCoordinate: BigInt('20625015362595980457695435345498579729138244358573902431560627260141789922999'),
    yCoordinate: BigInt('48563164792857017065725892921053777369510340820930241057309844352421738767712'),
    cipherTextData: new Uint8Array(\[100, 227, 78, 195, 249, 179, 43, 70, 242, 69, 169, 10, 65, 123\]),
    hashData: new Uint8Array(\[87, 167, 167, 247, 88, 146, 203, 234, 83, 126, 117, 129, 52, 142, 82, 54, 152, 226, 201,
      111, 143, 115, 169, 125, 128, 42, 157, 31, 114, 198, 109, 244\]),
  }
  let data = cryptoFramework.SM2CryptoUtil.genCipherTextBySpec(spec, 'C1C3C2');
  console.info('genCipherTextBySpec result: success.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(\`genCipherTextBySpec failed: errCode: ${e.code}, errMsg: ${e.message}\`);
}

#### \[h2\]getCipherTextSpec12+

static getCipherTextSpec(cipherText: DataBlob, mode?: string): SM2CipherTextSpec

Obtains SM2 ciphertext parameters from the SM2 ciphertext in ASN.1 format.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cipherText | [DataBlob](#datablob) | Yes | SM2 ciphertext in ASN.1 format. |
| mode | string | No | Order of the SM2 parameters in the ciphertext. Currently, only C1C3C2 is supported. If this parameter is left empty or is an empty string, the default value is used. |

**Return value**

| Type | Description |
| :-- | :-- |
| [SM2CipherTextSpec](#sm2ciphertextspec12) | SM2 ciphertext parameters obtained. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let cipherTextArray =
    new Uint8Array(\[48, 118, 2, 32, 45, 153, 88, 82, 104, 221, 226, 43, 174, 21, 122, 248, 5, 232, 105, 41, 92, 95, 102,
      224, 216, 149, 85, 236, 110, 6, 64, 188, 149, 70, 70, 183, 2, 32, 107, 93, 198, 247, 119, 18, 40, 110, 90, 156,
      193, 158, 205, 113, 170, 128, 146, 109, 75, 17, 181, 109, 110, 91, 149, 5, 110, 233, 209, 78, 229, 96, 4, 32, 87,
      167, 167, 247, 88, 146, 203, 234, 83, 126, 117, 129, 52, 142, 82, 54, 152, 226, 201, 111, 143, 115, 169, 125, 128,
      42, 157, 31, 114, 198, 109, 244, 4, 14, 100, 227, 78, 195, 249, 179, 43, 70, 242, 69, 169, 10, 65, 123\]);
  let cipherText: cryptoFramework.DataBlob = { data: cipherTextArray };
  let spec: cryptoFramework.SM2CipherTextSpec = cryptoFramework.SM2CryptoUtil.getCipherTextSpec(cipherText, 'C1C3C2');
  console.info('getCipherTextSpec result: success.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(\`getCipherTextSpec failed: errCode: ${e.code}, errMsg: ${e.message}\`);
}

#### cryptoFramework.createCipher

createCipher(transformation: string): Cipher

Creates a [Cipher](#cipher) instance based on the specified algorithm.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Cipher** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| transformation | string | Yes | 
Combination of the algorithm name (including the key length), encryption mode, and padding algorithm of the **Cipher** instance to create.

For details about the supported specifications, see [Symmetric Key Encryption and Decryption Algorithm Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-sym-encrypt-decrypt-spec) and [Asymmetric Key Encryption and Decryption Algorithm Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-asym-encrypt-decrypt-spec).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/ifvxs6dCQr-Syjf-JTgzpA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A5ADE9A791688FA351EC60188C103B989275898BC7A087B6EAE809FDE9335FA3)

1.  In symmetric encryption and decryption, PKCS #5 and PKCS #7 share the same implementation, with padding length and block size remaining consistent. In 3DES, padding is applied in 8-byte blocks; in AES, padding is applied in 16-byte blocks. **NoPadding** means no padding is applied.
    
    You need to understand the differences between different block cipher modes and use the correct parameter specifications. For example, padding is required for ECB and CBC. Otherwise, ensure that the plaintext length is an integer multiple of the block size. No padding is recommended for other modes. In this case, the ciphertext length is the same as the plaintext length.
    
2.  When RSA or SM2 is used for asymmetric encryption and decryption, two **Cipher** objects must be created to perform encryption and decryption separately. This is not required for symmetric encryption and decryption. If the algorithm specifications are the same, the same **Cipher** object can be used for encryption and decryption.

**Return value**

| Type | Description |
| :-- | :-- |
| [Cipher](#cipher) | [Cipher](#cipher) instance created. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let cipherAlgName = '3DES192|ECB|PKCS7';
try {
  let cipher = cryptoFramework.createCipher(cipherAlgName);
  console.info('cipher algName: ' + cipher.algName);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`sync failed: errCode: ${e.code}, errMsg: ${e.message}\`);
}

#### Cipher

Provides APIs for cipher operations. The [init()](#init-1), [update()](#update), and [doFinal()](#dofinal) APIs in this class are called in sequence to implement symmetric encryption or decryption and asymmetric encryption or decryption.

For details about the complete encryption and decryption process, see [Encryption and Decryption Overview](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-encryption-decryption-overview).

A complete symmetric encryption/decryption process is slightly different from the asymmetric encryption/decryption process.

-   Symmetric encryption and decryption: **init()** and **doFinal()** are mandatory. **update()** is optional and can be called multiple times to encrypt or decrypt big data. After **doFinal()** is called to complete an encryption or decryption operation, **init()** can be called to start a new encryption or decryption operation.
-   RSA or SM2 asymmetric encryption and decryption: **init()** and **doFinal()** are mandatory, and **update()** is not supported. **doFinal()** can be called multiple times to encrypt or decrypt big data. **init()** cannot be called repeatedly. If the encryption/decryption mode or padding mode is changed, a new **Cipher** object must be created.

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Cipher** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| algName | string | Yes | No | Algorithm. |

#### \[h2\]init

init(opMode: CryptoMode, key: Key, params: ParamsSpec | null, callback: AsyncCallback<void>): void

Initializes the [cipher](#cipher) object for encryption and decryption. This API uses an asynchronous callback to return the result. **init**, **update**, and **doFinal** must be used together. **init** and **doFinal** are mandatory, and **update** is optional.

This API can be used only after a [Cipher](#cipher) instance is created by using [createCipher](#cryptoframeworkcreatecipher).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Cipher** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| opMode | [CryptoMode](#cryptomode) | Yes | Operation (encryption or decryption) to perform. |
| key | [Key](#key) | Yes | Key for encryption or decryption. |
| params | [ParamsSpec](#paramsspec) | null10+ | Yes | Parameters for encryption or decryption. For algorithm modes without parameters (such as ECB), set this parameter to **null**. In versions earlier than API version 10, only **ParamsSpec** is supported. Since API version 10, **null** is also supported. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | 

parameter check failed. Possible causes:

1\. Invalid opMode value;

2\. Invalid iv length;

3\. Invalid key length.

 |
| 17630001 | crypto operation error. |

#### \[h2\]init

init(opMode: CryptoMode, key: Key, params: ParamsSpec | null): Promise<void>

Initializes the cipher object for encryption and decryption. This API uses a promise to return the result. **init**, **update**, and **doFinal** must be used together. **init** and **doFinal** are mandatory, and **update** is optional.

This API can be used only after a [Cipher](#cipher) instance is created by using [createCipher](#cryptoframeworkcreatecipher).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Cipher** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| opMode | [CryptoMode](#cryptomode) | Yes | Operation (encryption or decryption) to perform. |
| key | [Key](#key) | Yes | Key for encryption or decryption. |
| params | [ParamsSpec](#paramsspec) | null10+ | Yes | Parameters for encryption or decryption. For algorithm modes without parameters (such as ECB), set this parameter to **null**. Before API version 10, only **ParamsSpec** is supported. Since API version 10, **null** is also supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | 

parameter check failed. Possible causes:

1\. Invalid opMode value;

2\. Invalid iv length;

3\. Invalid key length.

 |
| 17630001 | crypto operation error. |

#### \[h2\]initSync12+

initSync(opMode: CryptoMode, key: Key, params: ParamsSpec | null): void

Initializes a [cipher](#cipher) instance. This API returns the result synchronously. **initSync**, **updateSync**, and **doFinalSync** must be used together. **initSync** and **doFinalSync** are mandatory, and **updateSync** is optional.

This API can be used only after a [Cipher](#cipher) instance is created by using [createCipher](#cryptoframeworkcreatecipher).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| opMode | [CryptoMode](#cryptomode) | Yes | Operation (encryption or decryption) to perform. |
| key | [Key](#key) | Yes | Key for encryption or decryption. |
| params | [ParamsSpec](#paramsspec) | null | Yes | Parameters for encryption or decryption. For algorithm modes without parameters (such as ECB), set this parameter to **null**. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | 

parameter check failed. Possible causes:

1\. Invalid opMode value;

2\. Invalid iv length;

3\. Invalid key length.

 |
| 17630001 | crypto operation error. |

#### \[h2\]update

update(data: DataBlob, callback: AsyncCallback<DataBlob>): void

Updates the data to encrypt or decrypt by segment. This API uses an asynchronous callback to return the result.

This API can be called only after the [Cipher](#cipher) instance is initialized by using [init()](#init-1).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/UrJE91BFSkSCjQLek7B09w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41831730A45315C63237FEEE7C44DD4F64E12F70EBE0F1543C643ADEAB0D82F0)

1.  The results of **update()** and **doFinal()** may vary with the block mode used. If you are not familiar with the block modes, you are advised to check each **update()** and **doFinal()** result to ensure that the results are not **null**. When a valid result is returned, extract and concatenate the data to form a complete ciphertext or plaintext.
    
    For example, in ECB and CBC modes, encryption and decryption are performed by block regardless of whether the data input by **update()** is an integer multiple of the block size, and **update()** returns the newly processed block data.
    
    That is, data is returned as long as the data passed in by **update()** reaches the size of a block. Otherwise, **null** is returned and the data will be retained until a block is formed in the next **update()** or **doFinal()**.
    
    In the final **doFinal()** operation, the remaining unprocessed data is padded based on the padding mode set in [createCipher](#cryptoframeworkcreatecipher) to the integer multiple of the block size to produce the final encrypted or decrypted data.
    
    For block cipher modes that can be converted to stream mode, the ciphertext length may be the same as the plaintext length.
    
2.  You can call **update()** multiple times or skip calling **update()** (call **doFinal()** directly after **init()**), depending on the data volume.
    
    The amount of the data to be passed in by **update()** (one-time or accumulative) is not limited. If there is a large amount of data, you are advised to pass data in multiple **update()** calls rather than processing it all at once.
    
    For details about the sample code for passing data in multiple **update()** calls, see [Encryption and Decryption by Segment with an AES Symmetric Key (GCM Mode)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm-by-segment).
    
3.  RSA or SM2 asymmetric encryption and decryption do not support **update()**.
    
4.  If CCM is used in symmetric encryption or decryption, **update()** can be called only once. In the encryption process, you can either use **update()** to encrypt data and use **doFinal()** to obtain **authTag** or use **doFinal()** without using **update()**. In the decryption process, you can either use **update()** or **doFinal()** once to decrypt data and verify the tag.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Cipher** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [DataBlob](#datablob) | Yes | Data to be encrypted or decrypted. It cannot be null. |
| callback | AsyncCallback<[DataBlob](#datablob)\> | Yes | Callback used to return the result. If the data is updated successfully, **err** is **undefined** and **data** is **DataBlob**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | 

parameter check failed. Possible causes:

1\. The data is too long.

 |
| 17630001 | crypto operation error. |

#### \[h2\]update

update(data: DataBlob): Promise<DataBlob>

Updates the data to encrypt or decrypt by segment. This API uses a promise to return the result.

This API can be called only after the [Cipher](#cipher) instance is initialized by using [init()](#init-1).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/d7GDjrxzTIKS_x1gveLZWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1176FAC7D1E1D58247FE62FFE95CD341D0DE943BD580A52D20E8B4B6377D072)

1.  The results of **update()** and **doFinal()** may vary with the block mode used. If you are not familiar with the block modes, you are advised to check each update() and doFinal() result to ensure that the results are not null. When a valid result is returned, extract and concatenate the data to form a complete ciphertext or plaintext.
    
    For example, in ECB and CBC modes, encryption and decryption are performed by block regardless of whether the data input by **update()** is an integer multiple of the block size, and **update()** returns the newly processed block data.
    
    That is, data is returned as long as the data passed in by **update()** reaches the size of a block. Otherwise, **null** is returned and the data will be retained until a block is formed in the next **update()** or **doFinal()**.
    
    In the final **doFinal()** operation, the remaining unprocessed data is padded based on the padding mode set in [createCipher](#cryptoframeworkcreatecipher) to the integer multiple of the block size to produce the final encrypted or decrypted data.
    
    For block cipher modes that can be converted to stream mode, the ciphertext length may be the same as the plaintext length.
    
2.  You can call **update()** multiple times or skip calling **update()** (call **doFinal()** directly after **init()**), depending on the data volume.
    
    The amount of the data to be passed in by **update()** (one-time or accumulative) is not limited. If there is a large amount of data, you are advised to pass data in multiple **update()** calls rather than processing it all at once.
    
    For details about the sample code for passing data in multiple **update()** calls, see [Encryption and Decryption by Segment with an AES Symmetric Key (GCM Mode)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm-by-segment).
    
3.  RSA or SM2 asymmetric encryption and decryption do not support **update()**.
4.  If CCM is used in symmetric encryption or decryption, **update()** can be called only once. In the encryption process, you can either use **update()** to encrypt data and use **doFinal()** to obtain **authTag** or use **doFinal()** without using **update()**. In the decryption process, you can either use **update()** or **doFinal()** once to decrypt data and verify the tag.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Cipher** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [DataBlob](#datablob) | Yes | Data to encrypt or decrypt. It cannot be null. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DataBlob](#datablob)\> | Promise used to return the **DataBlob** (containing the encrypted or decrypted data). |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | 

parameter check failed. Possible causes:

1\. The data is too long.

 |
| 17630001 | crypto operation error. |

#### \[h2\]updateSync12+

updateSync(data: DataBlob): DataBlob

Updates the data to encrypt or decrypt by segment. This API uses an asynchronous callback to return the encrypted or decrypted data.

This API can be called only after the [Cipher](#cipher) instance is initialized by using [initSync()](#initsync12).

See **NOTE** in **update()** for other precautions.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [DataBlob](#datablob) | Yes | Data to encrypt or decrypt. It cannot be null. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataBlob](#datablob) | Encryption/decryption result. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | 

parameter check failed. Possible causes:

1\. The data is too long.

 |
| 17630001 | crypto operation error. |

#### \[h2\]doFinal

doFinal(data: DataBlob | null, callback: AsyncCallback<DataBlob>): void

(1) Processes the remaining data and the data passed in this time, and completes the encryption or decryption operation for symmetric encryption and decryption. This API uses an asynchronous callback to return the encrypted or decrypted data. If a small amount of data needs to be encrypted or decrypted, you can use **doFinal()** to pass in all the data without using **update()**. If all the data has been passed in by [update()](#update), you can pass in **null** in **data** of **doFinal()**. The output of **doFinal()** varies with the symmetric block cipher mode in use.

-   In a single encryption process with GCM or CCM mode, concatenating the results of each **update()** and **doFinal()** procedures the ciphertext and **authTag**. In GCM mode, **authTag** is the last 16 bytes. In CCM mode, **authTag** is the last 12 bytes. The rest part is the ciphertext. If **data** passed to **doFinal()** is **null**, the **doFinal()** result is only the **authTag**. During decryption, **authTag** must be set in [GcmParamsSpec](#gcmparamsspec) or [CcmParamsSpec](#ccmparamsspec), and the ciphertext must be set in **data**.
-   For other symmetric encryption and decryption modes and GCM and CCM decryption modes, concatenating the results of **update()** and **doFinal()** throughout the process will yield the complete plaintext or ciphertext.

(2) Encrypts or decrypts the data passed in this time in RSA and SM2 asymmetric encryption or decryption. This API uses an asynchronous callback to return the encrypted or decrypted data. If a large amount of data needs to be encrypted/decrypted, call **doFinal()** multiple times and concatenate the result of each **doFinal()** to obtain the complete plaintext/ciphertext.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/eVubmDRwRyKToAhIh-9FZw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C457096D93E510BBC71BA304648DF7AFBBD099716B7669083E634A01BC5A0761)

1.  In symmetric encryption and decryption, after **doFinal** is called, the encryption and decryption process is complete and the [Cipher](#cipher) instance is cleared. When a new encryption and decryption process is started, **init()** must be called with a complete parameter list for initialization.
    
    Even if the same symmetric key is used to encrypt and decrypt the same **Cipher** instance, the **params** parameter must be set when **init** is called during decryption.
    
2.  If a decryption fails, check whether the data to be encrypted and decrypted matches the parameters in **init()**. For the GCM mode, check whether the **authTag** obtained after encryption is obtained from the **GcmParamsSpec** for decryption.
3.  The result of **doFinal()** may be **null**. To avoid exceptions, determine whether the result is **null** before using the **.data** field to access the **doFinal()** result.
    
    For encryption in CFB, OFB, or CTR mode, if **doFinal()** passes in **null**, the returned result is **null**.
    
    For decryption in GCM, CCM, CFB, OFB, or CTR mode, if **doFinal()** passes in **null**, the returned result is **null**. For decryption in other modes, if **update** is called to pass in all the plaintext, which is an integer multiple of the encryption block size, and **doFinal()** is called to pass in **null**, the returned result is **null**.
    
4.  For details about the sample code for calling **doFinal** multiple times in asymmetric encryption and decryption, see [Encryption and Decryption by Segment with an RSA Asymmetric Key Pair](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-by-segment). The operations are similar for SM2 and RSA.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Cipher** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [DataBlob](#datablob) | null10+ | Yes | Data to encrypt or decrypt. In symmetric encryption and decryption, this parameter can be **null**, but **{data: Uint8Array (empty)}** cannot be passed in. Before API version 10, only **DataBlob** is supported. Since API version 10, **null** is also supported. |
| callback | AsyncCallback<[DataBlob](#datablob)\> | Yes | Callback used to return the result. If the encryption or decryption is successful, **err** is **undefined**, and **data** is the encryption or decryption result **DataBlob**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | 

parameter check failed. Possible causes:

1\. The data is too long.

 |
| 17630001 | crypto operation error. |

**Encryption with AES GCM (example)**

For more encryption and decryption examples, see [Encryption and Decryption with an AES Symmetric Key (GCM Mode)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm).

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function generateRandom(len: number) {
  let rand = cryptoFramework.createRandom();
  let generateRandSync = rand.generateRandomSync(len);
  return generateRandSync;
}

function genGcmParamsSpec() {
  let ivBlob = generateRandom(12);
  let arr = \[1, 2, 3, 4, 5, 6, 7, 8\];
  let dataAad = new Uint8Array(arr);
  let aadBlob: cryptoFramework.DataBlob = { data: dataAad };
  arr = \[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0\];
  let dataTag = new Uint8Array(arr);
  let tagBlob: cryptoFramework.DataBlob = {
    data: dataTag
  };
  let gcmParamsSpec: cryptoFramework.GcmParamsSpec = {
    iv: ivBlob,
    aad: aadBlob,
    authTag: tagBlob,
    algName: 'GcmParamsSpec'
  };
  return gcmParamsSpec;
}

function cipherByCallback() {
  let gcmParams = genGcmParamsSpec();
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let cipher = cryptoFramework.createCipher('AES128|GCM|PKCS7');
  symKeyGenerator.generateSymKey((err, symKey) => {
    cipher.init(cryptoFramework.CryptoMode.ENCRYPT\_MODE, symKey, gcmParams, (err) => {
      let message = 'This is a test';
      let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
      cipher.update(plainText, (err, encryptUpdate) => {
        cipher.doFinal(null, (err, tag) => {
          gcmParams.authTag = tag;
          console.info('encryptUpdate plainText: ' + encryptUpdate.data);
        });
      });
    });
  });
}

#### \[h2\]doFinal

doFinal(data: DataBlob | null): Promise<DataBlob>

(1) Encrypts or decrypts the remaining data (generated by the block cipher mode) and the data passed in this time to finalize the symmetric encryption or decryption. This API uses a promise to return the encrypted or decrypted data.

If a small amount of data needs to be encrypted or decrypted, you can use **doFinal()** to pass in data without using **update()**. If all the data has been passed in by **update()**, you can pass in **null** in **data** of **doFinal()**.

The output of **doFinal()** varies with the symmetric encryption/decryption mode in use.

-   Symmetric encryption in GCM and CCM mode: The result consists of the ciphertext and **authTag** (the last 16 bytes for GCM and the last 12 bytes for CCM). If **data** in **doFinal** is null, the result of **doFinal** is **authTag**.
    
    During decryption, **authTag** must be set in [GcmParamsSpec](#gcmparamsspec) or [CcmParamsSpec](#ccmparamsspec), and the ciphertext must be set in **data**.
    
-   For other symmetric encryption and decryption modes and GCM and CCM decryption modes, concatenating the results of **update()** and **doFinal()** throughout the process will yield the complete plaintext or ciphertext.

(2) Encrypts or decrypts the data passed in RSA and SM2 asymmetric encryption or decryption. This API uses a promise to return the encrypted or decrypted data. If a large amount of data is to be processed, call **doFinal()** multiple times and concatenate the results to obtain the complete plaintext or ciphertext.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/X3EVWn1JQbWNk_BXUm2fDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A379F350EA9C31F86FD2DED4BF2433D909F35B068E0D5B28C47FA38312F0F3D)

1.  In symmetric encryption and decryption, calling **doFinal()** indicates the completion of an encryption and decryption process, meaning the [Cipher](#cipher) instance status is cleared. When a new encryption or decryption process is started, **init()** must be called again with a full set of parameters.
    
    Even if the same **Cipher** instance and symmetric key are used for encryption and decryption, the **params** parameter must be set in **init()** instead of being **null**.
    
2.  If decryption fails, check whether the data matches the parameters in **ini()**, for example, check whether **authTag** obtained during encryption in GCM mode is filled in **GcmParamsSpec** during decryption.
    
3.  The result of **doFinal()** may be **null**. To avoid exceptions, determine whether the result is **null** before using the **.data** field to access the **doFinal()** result.
    
    For encryption in CFB, OFB, or CTR mode, if **doFinal()** passes in **null**, the returned result is **null**.
    
    For decryption in GCM, CCM, CFB, OFB, or CTR mode, if **doFinal()** passes in **null**, the returned result is **null**. For decryption in other modes, if **update** is called to pass in all the plaintext, which is an integer multiple of the encryption block size, and **doFinal()** is called to pass in **null**, the returned result is **null**.
    
4.  For details about the sample code for calling **doFinal** multiple times in asymmetric encryption and decryption, see [Encryption and Decryption by Segment with an RSA Asymmetric Key Pair](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-by-segment). The operations are similar for SM2 and RSA.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Cipher** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [DataBlob](#datablob) | null10+ | Yes | Data to encrypt or decrypt. It can be **null**, but cannot be {data:Uint8Array(empty)}. In versions earlier than API version 10, only **DataBlob** is supported. Since API version 10, **null** is also supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DataBlob](#datablob)\> | Promise used to return the **DataBlob**, which is the encryption or decryption result of the remaining data. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | 

parameter check failed. Possible causes:

1\. The data is too long.

 |
| 17630001 | crypto operation error. |

**Encryption with AES GCM (example)**

For more encryption and decryption examples, see [Encryption and Decryption with an AES Symmetric Key (GCM Mode)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm).

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function generateRandom(len: number) {
  let rand = cryptoFramework.createRandom();
  let generateRandSync = rand.generateRandomSync(len);
  return generateRandSync;
}

function genGcmParamsSpec() {
  let ivBlob = generateRandom(12);
  let arr = \[1, 2, 3, 4, 5, 6, 7, 8\];
  let dataAad = new Uint8Array(arr);
  let aadBlob: cryptoFramework.DataBlob = { data: dataAad };
  arr = \[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0\];
  let dataTag = new Uint8Array(arr);
  let tagBlob: cryptoFramework.DataBlob = {
    data: dataTag
  };
  let gcmParamsSpec: cryptoFramework.GcmParamsSpec = {
    iv: ivBlob,
    aad: aadBlob,
    authTag: tagBlob,
    algName: 'GcmParamsSpec'
  };
  return gcmParamsSpec;
}

async function cipherByPromise() {
  let gcmParams = genGcmParamsSpec();
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let cipher = cryptoFramework.createCipher('AES128|GCM|PKCS7');
  let symKey = await symKeyGenerator.generateSymKey();
  await cipher.init(cryptoFramework.CryptoMode.ENCRYPT\_MODE, symKey, gcmParams);
  let message = 'This is a test';
  let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  let encryptUpdate = await cipher.update(plainText);
  gcmParams.authTag = await cipher.doFinal(null);
  console.info('encryptUpdate plainText: ' + encryptUpdate.data);
}

#### \[h2\]doFinalSync12+

doFinalSync(data: DataBlob | null): DataBlob

(1) Processes the remaining data and the data passed in this time, and completes the encryption or decryption operation for symmetric encryption and decryption. This API returns the encrypted or decrypted data synchronously.

If a small amount of data is to be processed, you can pass in all the data at a time in **doFinalSync()** without using **updateSync()**. If data has been passed in by using [updateSync](#updatesync12) in the current encryption and decryption process, you can pass in **null** to the **data** parameter of **doFinalSync()**.

The output of **doFinalSync()** varies with the symmetric block cipher mode in use.

-   In a single encryption process with GCM or CCM mode, concatenating the results of each **updateSync()** and **doFinalSync()** procedures the ciphertext and **authTag**. In GCM mode, **authTag** is the last 16 bytes. In CCM mode, **authTag** is the last 12 bytes. The rest part is the ciphertext. If **data** in **doFinalSync()** is **null**, the result of **doFinalSync()** is **authTag**.
    
    During decryption, **authTag** must be set in [GcmParamsSpec](#gcmparamsspec) or [CcmParamsSpec](#ccmparamsspec), and the ciphertext must be set in **data**.
    
-   For other symmetric encryption and decryption modes and GCM and CCM decryption modes, concatenating the results of **updateSync()** and **doFinalSync()** throughout the process will yield the complete plaintext or ciphertext.
    

(2) Encrypts or decrypts the input data for RSA or SM2 asymmetric encryption/decryption. This API returns the encrypted or decrypted data synchronously. If a large amount of data is to be processed, call **doFinalSync()** multiple times and concatenate the results to obtain the complete plaintext or ciphertext.

See **NOTE** in [doFinal()](#dofinal) for other precautions.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [DataBlob](#datablob) | null | Yes | Data to encrypt or decrypt. It can be **null** in symmetric encryption or decryption, but cannot be {data:Uint8Array(empty)}. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataBlob](#datablob) | Encrypted or decrypted data. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | 

parameter check failed. Possible causes:

1\. The data is too long.

 |
| 17630001 | crypto operation error. |

**Encryption with AES GCM (example)**

For more encryption and decryption examples, see [Encryption and Decryption with an AES Symmetric Key (GCM Mode)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm).

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function generateRandom(len: number) {
  let rand = cryptoFramework.createRandom();
  let generateRandSync = rand.generateRandomSync(len);
  return generateRandSync;
}

function genGcmParamsSpec() {
  let ivBlob = generateRandom(12);
  let arr = \[1, 2, 3, 4, 5, 6, 7, 8\];
  let dataAad = new Uint8Array(arr);
  let aadBlob: cryptoFramework.DataBlob = { data: dataAad };
  arr = \[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0\];
  let dataTag = new Uint8Array(arr);
  let tagBlob: cryptoFramework.DataBlob = {
    data: dataTag
  };
  let gcmParamsSpec: cryptoFramework.GcmParamsSpec = {
    iv: ivBlob,
    aad: aadBlob,
    authTag: tagBlob,
    algName: 'GcmParamsSpec'
  };
  return gcmParamsSpec;
}

async function cipherBySync() {
  let gcmParams = genGcmParamsSpec();
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let cipher = cryptoFramework.createCipher('AES128|GCM|PKCS7');
  let symKey = await symKeyGenerator.generateSymKey();
  await cipher.init(cryptoFramework.CryptoMode.ENCRYPT\_MODE, symKey, gcmParams);
  let message = 'This is a test';
  let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  let encryptUpdate = cipher.updateSync(plainText);
  gcmParams.authTag = cipher.doFinalSync(null);
  console.info('encryptUpdate plainText: ' + encryptUpdate.data);
}

#### \[h2\]setCipherSpec10+

setCipherSpec(itemType: CipherSpecItem, itemValue: Uint8Array): void

Sets cipher specifications. You can use this API to set cipher specifications that cannot be set by [createCipher](#cryptoframeworkcreatecipher). Currently, only RSA is supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Cipher** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| itemType | [CipherSpecItem](#cipherspecitem10) | Yes | Cipher parameter to set. |
| itemValue | Uint8Array | Yes | Value of the parameter to set. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17620003 | 

parameter check failed. Possible causes:

1\. Unsupported itemType.

 |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function testsetCipherSpec() {
  let cipher = cryptoFramework.createCipher('RSA2048|PKCS1\_OAEP|SHA256|MGF1\_SHA1');
  let pSource = new Uint8Array(\[1, 2, 3, 4\]);
  cipher.setCipherSpec(cryptoFramework.CipherSpecItem.OAEP\_MGF1\_PSRC\_UINT8ARR, pSource);
}

#### \[h2\]getCipherSpec10+

getCipherSpec(itemType: CipherSpecItem): string | Uint8Array

Obtains cipher specifications. Currently, only RSA and SM2 (available since API version 11) are supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Cipher

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Cipher** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| itemType | [CipherSpecItem](#cipherspecitem10) | Yes | Cipher parameter to obtain. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Uint8Array | Returns the value of the cipher parameter obtained. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17620003 | 

parameter check failed. Possible causes:

1\. Unsupported itemType.

 |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function testGetCipherSpec() {
  let cipher = cryptoFramework.createCipher('RSA2048|PKCS1\_OAEP|SHA256|MGF1\_SHA1');
  let mdName = cipher.getCipherSpec(cryptoFramework.CipherSpecItem.OAEP\_MD\_NAME\_STR);
  console.info('getCipherSpec: mdName =' + mdName);
}

#### cryptoFramework.createSign

createSign(algName: string): Sign

Creates a **Sign** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| algName | string | Yes | 
Signing algorithm to use. Currently, RSA, ECC, DSA, SM210+ and Ed2551911+ are supported. If RSA PKCS1 is used, you must set the digest. If RSA PSS is used, you must set the digest and mask digest. For signing, you can set **OnlySign** to enable the data digest to be used for signing only.

For details about the supported specifications, see [Signing and Signature Verification Overview and Algorithm Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-sign-sig-verify-overview).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [Sign](#sign) | Returns the **Sign** instance created. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let signer1 = cryptoFramework.createSign('RSA1024|PKCS1|SHA256');

let signer2 = cryptoFramework.createSign('RSA1024|PSS|SHA256|MGF1\_SHA256');

let signer3 = cryptoFramework.createSign('ECC224|SHA256');

let signer4 = cryptoFramework.createSign('DSA2048|SHA256');

let signer5 = cryptoFramework.createSign('RSA1024|PKCS1|SHA256|OnlySign');

#### Sign

Provides APIs for signing. Before using any API of the **Sign** class, you must create a **Sign** instance by using [createSign(algName: string): Sign](#cryptoframeworkcreatesign). Invoke **init()**, **update()**, and **sign()** in this class in sequence to complete the signing operation. For details about the sample code, see [Signing and Signature Verification with an RSA Key Pair (PKCS1 Mode)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1).

The **Sign** class does not support repeated initialization. When a new key is used for signing, you must create a new **Sign** instance and call **init()** for initialization.

The signing mode is determined by **createSign()**, and the key is set by **init()**.

If a small amount of data is to be signed, you can directly call **sign()** to pass in the data for signing after **ini()**.

If a large amount of data is to be signed, you can use **update()** to pass in the data by segment, and then use **sign()** to sign the entire data.

When **update()** is used, the **sign()** API supports only **DataBlob** in versions earlier than API version 10 and starts to support **null** since API version 10. After all the data is passed in by using **update()**, call **sign()** to sign the data.

If the DSA algorithm is used for signing and the digest algorithm is **NoHash**, the **update()** operation is not supported. If **update()** is called in this case, the error code **ERR\_CRYPTO\_OPERATION** will be returned.

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| algName | string | Yes | No | Algorithm to use. |

#### \[h2\]init

init(priKey: PriKey, callback: AsyncCallback<void>): void

Initializes the **Sign** object using a private key. This API uses an asynchronous callback to return the result. **init**, **update**, and **sign** must be used together. **init** and **sign** are mandatory, and **update** is optional.

The **Sign** class does not support repeated use of **ini**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| priKey | [PriKey](#prikey) | Yes | Private key used for the initialization. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### \[h2\]init

init(priKey: PriKey): Promise<void>

Initializes the **Sign** object using a private key. This API uses a promise to return the result. **init**, **update**, and **sign** must be used together. **init** and **sign** are mandatory, and **update** is optional.

The **Sign** class does not support repeated use of **ini**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| priKey | [PriKey](#prikey) | Yes | Private key used for the initialization. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### \[h2\]initSync12+

initSync(priKey: PriKey): void

Initializes the **Sign** instance with a private key. This API returns the result synchronously. **initSync**, **updateSync**, and **signSync** must be used together. **initSync** and **signSync** are mandatory, and **updateSync** is optional.

The **Sign** class does not support repeated use of **initSync**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| priKey | [PriKey](#prikey) | Yes | Private key used for the initialization. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### \[h2\]update

update(data: DataBlob, callback: AsyncCallback<void>): void

Updates data to be signed. This API uses an asynchronous callback to return the result.

This API can be called only after the [Sign](#sign) instance is initialized by using [init()](#init-2).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/gaGLUKR_Snm89ZO9m2jBRg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=891FF9B587E4E124C78FBFB6AB39115EEAE3FA77DD0353CA82624419F531C01C)

You can call **update** multiple times or do not use **update** (call [sign](#sign-1) after [init](#init-2)), depending on the data volume.

The amount of the data to be passed in by **update()** (one-time or accumulative) is not limited. If there is a large amount of data, you are advised to call **update()** multiple times to pass in the data by segment. This prevents too much memory from being requested at a time.

For details about the sample code for calling **update()** multiple times in signing, see [Signing and Signature Verification by Segment with an RSA Key Pair (PKCS1 Mode)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1-by-segment). The operations of other algorithms are similar.

**OnlySign** cannot be used with **update()**. If **OnlySign** is specified, use **sign()** to pass in data.

If the DSA algorithm is used for signing and the digest algorithm is **NoHash**, **update()** is not supported. If **update()** is called in this case, **ERR\_CRYPTO\_OPERATION** will be returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [DataBlob](#datablob) | Yes | Data to pass in. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### \[h2\]update

update(data: DataBlob): Promise<void>

Updates data to be signed. This API uses a promise to return the result.

Before using this API, you must use [Sign](#sign) to initialize the [init()](#init-3) instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/GsBqIZpKToSEZ6ABngNLJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C508618C3B787ABEE1A40C129A41EFCEB66A425A2C00C5691CB0E6A7CACD914)

You can call **update** multiple times or do not use **update** (call [sign](#sign-2) after [init](#init-3)), depending on the data volume.

The amount of the data to be passed in by **update()** (one-time or accumulative) is not limited. If there is a large amount of data, you are advised to call **update()** multiple times to pass in the data by segment. This prevents too much memory from being requested at a time.

For details about the sample code for calling **update()** multiple times in signing, see [Signing and Signature Verification by Segment with an RSA Key Pair (PKCS1 Mode)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1-by-segment). The operations of other algorithms are similar.

**OnlySign** cannot be used with **update()**. If **OnlySign** is specified, use **sign()** to pass in data.

If the DSA algorithm is used for signing and the digest algorithm is **NoHash**, **update()** is not supported. If **update()** is called in this case, **ERR\_CRYPTO\_OPERATION** will be returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [DataBlob](#datablob) | Yes | Data to pass in. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### \[h2\]updateSync12+

updateSync(data: DataBlob): void

Updates data to be signed. This API returns the result synchronously.

This API can be called only after the [Sign](#sign) instance is initialized by using [initSync()](#initsync12-1).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/uEJpxw18RfqVqb4fZYm3jA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0FFEF356878080CC673948ADC38972B5DBA67B49C7F5EE99C824DCA7588FFF42)

You can call **updateSync** multiple times or do not use **updateSync** (call [signSync](#signsync12) after [initSync](#initsync12-1)), depending on the data volume.

The amount of the data to be passed in by **updateSync** (one-time or accumulative) is not limited. If there is a large amount of data, you are advised to call **updateSync** multiple times to pass in the data by segment. This prevents too much memory from being requested at a time.

For details about the sample code for calling **updateSync** multiple times in signing, see [Signing and Signature Verification by Segment with an RSA Key Pair (PKCS1 Mode)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1-by-segment). The operations of other algorithms are similar.

**OnlySign** cannot be used with **updateSync**. If **OnlySign** is specified, use **signSync** to pass in data.

If the DSA algorithm is used for signing and the digest algorithm is **NoHash**, **updateSync** is not supported. If **updateSync** is called in this case, **ERR\_CRYPTO\_OPERATION** will be returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [DataBlob](#datablob) | Yes | Data to pass in. |

**Return value**

| Type | Description |
| :-- | :-- |
| void | No value is returned. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### \[h2\]sign

sign(data: DataBlob | null, callback: AsyncCallback<DataBlob>): void

Signs data. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [DataBlob](#datablob) | null10+ | Yes | Data to pass in. In versions earlier than API version 10, only **DataBlob** is supported. Since API version 10, **null** is also supported. |
| callback | AsyncCallback<[DataBlob](#datablob)\> | Yes | Callback used to return a **DataBlob** object. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### \[h2\]sign

sign(data: DataBlob | null): Promise<DataBlob>

Signs data. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [DataBlob](#datablob) | null10+ | Yes | Data to pass in. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DataBlob](#datablob)\> | Signature. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### \[h2\]signSync12+

signSync(data: DataBlob | null): DataBlob

Signs the data. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [DataBlob](#datablob) | null | Yes | Data to pass in. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataBlob](#datablob) | Signature. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

**Example (using the callback-based API)**

For more examples of signing and signature verification, see [Signing and Signature Verification with an RSA Key Pair (PKCS1 Mode)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1).

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function signByCallback() {
  let inputUpdate: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan1', 'utf-8').buffer) };
  let inputVerify: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan2', 'utf-8').buffer) };
  let pkData =
    new Uint8Array(\[48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
      2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166, 209, 250, 142, 74, 216,
      58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31, 172, 151, 252, 185, 123,
      20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31, 214, 93, 115, 247, 69,
      94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176, 57, 125, 235, 51, 88,
      135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50, 189, 88, 254, 255, 146,
      244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1\]);
  let skData =
    new Uint8Array(\[48, 130, 2, 120, 2, 1, 0, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 4, 130, 2, 98, 48,
      130, 2, 94, 2, 1, 0, 2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166,
      209, 250, 142, 74, 216, 58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31,
      172, 151, 252, 185, 123, 20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31,
      214, 93, 115, 247, 69, 94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176,
      57, 125, 235, 51, 88, 135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50,
      189, 88, 254, 255, 146, 244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1, 2, 129, 129, 0, 152, 111, 145, 203, 10,
      88, 116, 163, 112, 126, 9, 20, 68, 34, 235, 121, 98, 14, 182, 102, 151, 125, 114, 91, 210, 122, 215, 29, 212, 5,
      176, 203, 238, 146, 5, 190, 41, 21, 91, 56, 125, 239, 111, 133, 53, 200, 192, 56, 132, 202, 42, 145, 120, 3, 224,
      40, 223, 46, 148, 29, 41, 92, 17, 40, 12, 72, 165, 69, 192, 211, 142, 233, 81, 202, 177, 235, 156, 27, 179, 48,
      18, 85, 154, 101, 193, 45, 218, 91, 24, 143, 196, 248, 16, 83, 177, 198, 136, 77, 111, 134, 60, 219, 95, 246, 23,
      5, 45, 14, 83, 29, 137, 248, 159, 28, 132, 142, 205, 99, 226, 213, 84, 232, 57, 130, 156, 81, 191, 237, 2, 65, 0,
      255, 158, 212, 13, 43, 132, 244, 135, 148, 161, 232, 219, 20, 81, 196, 102, 103, 44, 110, 71, 100, 62, 73, 200,
      32, 138, 114, 209, 171, 150, 179, 92, 198, 5, 190, 218, 79, 227, 227, 37, 32, 57, 159, 252, 107, 211, 139, 198,
      202, 248, 137, 143, 186, 205, 106, 81, 85, 207, 134, 148, 110, 204, 243, 27, 2, 65, 0, 215, 4, 181, 121, 57, 224,
      170, 168, 183, 159, 152, 8, 74, 233, 80, 244, 146, 81, 48, 159, 194, 199, 36, 187, 6, 181, 182, 223, 115, 133,
      151, 171, 78, 219, 90, 161, 248, 69, 6, 207, 173, 3, 81, 161, 2, 60, 238, 204, 177, 12, 138, 17, 220, 179, 71,
      113, 200, 248, 159, 153, 252, 150, 180, 155, 2, 65, 0, 190, 202, 185, 211, 170, 171, 238, 40, 84, 84, 21, 13, 144,
      57, 7, 178, 183, 71, 126, 120, 98, 229, 235, 4, 40, 229, 173, 149, 185, 209, 29, 199, 29, 54, 164, 161, 38, 8, 30,
      62, 83, 179, 47, 42, 165, 0, 156, 207, 160, 39, 169, 229, 81, 180, 136, 170, 116, 182, 20, 233, 45, 90, 100, 9, 2,
      65, 0, 152, 255, 47, 198, 15, 201, 238, 133, 89, 11, 133, 153, 184, 252, 37, 239, 177, 65, 118, 80, 231, 190, 222,
      66, 250, 118, 72, 166, 221, 67, 156, 245, 119, 138, 28, 6, 142, 107, 71, 122, 116, 200, 156, 199, 237, 152, 191,
      239, 4, 184, 64, 114, 143, 81, 62, 48, 23, 233, 217, 95, 47, 221, 104, 171, 2, 64, 30, 219, 1, 230, 241, 70, 246,
      243, 121, 174, 67, 66, 11, 99, 202, 17, 52, 234, 78, 29, 3, 57, 51, 123, 149, 86, 64, 192, 73, 199, 108, 101, 55,
      232, 41, 114, 153, 237, 253, 52, 205, 148, 45, 86, 186, 241, 182, 183, 42, 77, 252, 195, 29, 158, 173, 3, 182,
      207, 254, 61, 71, 184, 167, 184\]);
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pkData };
  let priKeyBlob: cryptoFramework.DataBlob = { data: skData };
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let signer = cryptoFramework.createSign('RSA1024|PKCS1|SHA256');
  rsaGenerator.convertKey(pubKeyBlob, priKeyBlob, (err, keyPair) => {
    signer.init(keyPair.priKey, err => {
      signer.update(inputUpdate, err => {
        signer.sign(inputVerify, (err, signData) => {
          console.info('sign output = ' + signData.data);
        });
      });
    });
  });
}

**Example (using the promise-based API)**

For more examples of signing and signature verification, see [Signing and Signature Verification with an RSA Key Pair (PKCS1 Mode)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1).

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

async function genKeyPairByData(pubKeyData: Uint8Array, priKeyData: Uint8Array) {
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyData };
  let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyData };
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let keyPair = await rsaGenerator.convertKey(pubKeyBlob, priKeyBlob);
  console.info('convertKey result: success.');
  return keyPair;
}

async function signByPromise() {
  let pkData =
    new Uint8Array(\[48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
      2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166, 209, 250, 142, 74, 216,
      58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31, 172, 151, 252, 185, 123,
      20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31, 214, 93, 115, 247, 69,
      94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176, 57, 125, 235, 51, 88,
      135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50, 189, 88, 254, 255, 146,
      244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1\]);
  let skData =
    new Uint8Array(\[48, 130, 2, 120, 2, 1, 0, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 4, 130, 2, 98, 48,
      130, 2, 94, 2, 1, 0, 2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166,
      209, 250, 142, 74, 216, 58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31,
      172, 151, 252, 185, 123, 20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31,
      214, 93, 115, 247, 69, 94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176,
      57, 125, 235, 51, 88, 135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50,
      189, 88, 254, 255, 146, 244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1, 2, 129, 129, 0, 152, 111, 145, 203, 10,
      88, 116, 163, 112, 126, 9, 20, 68, 34, 235, 121, 98, 14, 182, 102, 151, 125, 114, 91, 210, 122, 215, 29, 212, 5,
      176, 203, 238, 146, 5, 190, 41, 21, 91, 56, 125, 239, 111, 133, 53, 200, 192, 56, 132, 202, 42, 145, 120, 3, 224,
      40, 223, 46, 148, 29, 41, 92, 17, 40, 12, 72, 165, 69, 192, 211, 142, 233, 81, 202, 177, 235, 156, 27, 179, 48,
      18, 85, 154, 101, 193, 45, 218, 91, 24, 143, 196, 248, 16, 83, 177, 198, 136, 77, 111, 134, 60, 219, 95, 246, 23,
      5, 45, 14, 83, 29, 137, 248, 159, 28, 132, 142, 205, 99, 226, 213, 84, 232, 57, 130, 156, 81, 191, 237, 2, 65, 0,
      255, 158, 212, 13, 43, 132, 244, 135, 148, 161, 232, 219, 20, 81, 196, 102, 103, 44, 110, 71, 100, 62, 73, 200,
      32, 138, 114, 209, 171, 150, 179, 92, 198, 5, 190, 218, 79, 227, 227, 37, 32, 57, 159, 252, 107, 211, 139, 198,
      202, 248, 137, 143, 186, 205, 106, 81, 85, 207, 134, 148, 110, 204, 243, 27, 2, 65, 0, 215, 4, 181, 121, 57, 224,
      170, 168, 183, 159, 152, 8, 74, 233, 80, 244, 146, 81, 48, 159, 194, 199, 36, 187, 6, 181, 182, 223, 115, 133,
      151, 171, 78, 219, 90, 161, 248, 69, 6, 207, 173, 3, 81, 161, 2, 60, 238, 204, 177, 12, 138, 17, 220, 179, 71,
      113, 200, 248, 159, 153, 252, 150, 180, 155, 2, 65, 0, 190, 202, 185, 211, 170, 171, 238, 40, 84, 84, 21, 13, 144,
      57, 7, 178, 183, 71, 126, 120, 98, 229, 235, 4, 40, 229, 173, 149, 185, 209, 29, 199, 29, 54, 164, 161, 38, 8, 30,
      62, 83, 179, 47, 42, 165, 0, 156, 207, 160, 39, 169, 229, 81, 180, 136, 170, 116, 182, 20, 233, 45, 90, 100, 9, 2,
      65, 0, 152, 255, 47, 198, 15, 201, 238, 133, 89, 11, 133, 153, 184, 252, 37, 239, 177, 65, 118, 80, 231, 190, 222,
      66, 250, 118, 72, 166, 221, 67, 156, 245, 119, 138, 28, 6, 142, 107, 71, 122, 116, 200, 156, 199, 237, 152, 191,
      239, 4, 184, 64, 114, 143, 81, 62, 48, 23, 233, 217, 95, 47, 221, 104, 171, 2, 64, 30, 219, 1, 230, 241, 70, 246,
      243, 121, 174, 67, 66, 11, 99, 202, 17, 52, 234, 78, 29, 3, 57, 51, 123, 149, 86, 64, 192, 73, 199, 108, 101, 55,
      232, 41, 114, 153, 237, 253, 52, 205, 148, 45, 86, 186, 241, 182, 183, 42, 77, 252, 195, 29, 158, 173, 3, 182,
      207, 254, 61, 71, 184, 167, 184\]);
  let keyPair = await genKeyPairByData(pkData, skData);
  let inputUpdate: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan1', 'utf-8').buffer) };
  let inputSign: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan2', 'utf-8').buffer) };
  let signer = cryptoFramework.createSign('RSA1024|PKCS1|SHA256');
  await signer.init(keyPair.priKey);
  await signer.update(inputUpdate);
  let signData = await signer.sign(inputSign);
  console.info('signData result: ' + signData.data);
}

**Example (using the sync API)**

For more examples of signing and signature verification, see [Signing and Signature Verification with an RSA Key Pair (PKCS1 Mode)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1).

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function genKeyPairByData(pubKeyData: Uint8Array, priKeyData: Uint8Array) {
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyData };
  let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyData };
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let keyPair = rsaGenerator.convertKeySync(pubKeyBlob, priKeyBlob);
  console.info('convertKeySync result: success.');
  return keyPair;
}

function signBySync() {
  let pkData =
    new Uint8Array(\[48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
      2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166, 209, 250, 142, 74, 216,
      58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31, 172, 151, 252, 185, 123,
      20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31, 214, 93, 115, 247, 69,
      94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176, 57, 125, 235, 51, 88,
      135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50, 189, 88, 254, 255, 146,
      244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1\]);
  let skData =
    new Uint8Array(\[48, 130, 2, 120, 2, 1, 0, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 4, 130, 2, 98, 48,
      130, 2, 94, 2, 1, 0, 2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166,
      209, 250, 142, 74, 216, 58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31,
      172, 151, 252, 185, 123, 20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31,
      214, 93, 115, 247, 69, 94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176,
      57, 125, 235, 51, 88, 135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50,
      189, 88, 254, 255, 146, 244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1, 2, 129, 129, 0, 152, 111, 145, 203, 10,
      88, 116, 163, 112, 126, 9, 20, 68, 34, 235, 121, 98, 14, 182, 102, 151, 125, 114, 91, 210, 122, 215, 29, 212, 5,
      176, 203, 238, 146, 5, 190, 41, 21, 91, 56, 125, 239, 111, 133, 53, 200, 192, 56, 132, 202, 42, 145, 120, 3, 224,
      40, 223, 46, 148, 29, 41, 92, 17, 40, 12, 72, 165, 69, 192, 211, 142, 233, 81, 202, 177, 235, 156, 27, 179, 48,
      18, 85, 154, 101, 193, 45, 218, 91, 24, 143, 196, 248, 16, 83, 177, 198, 136, 77, 111, 134, 60, 219, 95, 246, 23,
      5, 45, 14, 83, 29, 137, 248, 159, 28, 132, 142, 205, 99, 226, 213, 84, 232, 57, 130, 156, 81, 191, 237, 2, 65, 0,
      255, 158, 212, 13, 43, 132, 244, 135, 148, 161, 232, 219, 20, 81, 196, 102, 103, 44, 110, 71, 100, 62, 73, 200,
      32, 138, 114, 209, 171, 150, 179, 92, 198, 5, 190, 218, 79, 227, 227, 37, 32, 57, 159, 252, 107, 211, 139, 198,
      202, 248, 137, 143, 186, 205, 106, 81, 85, 207, 134, 148, 110, 204, 243, 27, 2, 65, 0, 215, 4, 181, 121, 57, 224,
      170, 168, 183, 159, 152, 8, 74, 233, 80, 244, 146, 81, 48, 159, 194, 199, 36, 187, 6, 181, 182, 223, 115, 133,
      151, 171, 78, 219, 90, 161, 248, 69, 6, 207, 173, 3, 81, 161, 2, 60, 238, 204, 177, 12, 138, 17, 220, 179, 71,
      113, 200, 248, 159, 153, 252, 150, 180, 155, 2, 65, 0, 190, 202, 185, 211, 170, 171, 238, 40, 84, 84, 21, 13, 144,
      57, 7, 178, 183, 71, 126, 120, 98, 229, 235, 4, 40, 229, 173, 149, 185, 209, 29, 199, 29, 54, 164, 161, 38, 8, 30,
      62, 83, 179, 47, 42, 165, 0, 156, 207, 160, 39, 169, 229, 81, 180, 136, 170, 116, 182, 20, 233, 45, 90, 100, 9, 2,
      65, 0, 152, 255, 47, 198, 15, 201, 238, 133, 89, 11, 133, 153, 184, 252, 37, 239, 177, 65, 118, 80, 231, 190, 222,
      66, 250, 118, 72, 166, 221, 67, 156, 245, 119, 138, 28, 6, 142, 107, 71, 122, 116, 200, 156, 199, 237, 152, 191,
      239, 4, 184, 64, 114, 143, 81, 62, 48, 23, 233, 217, 95, 47, 221, 104, 171, 2, 64, 30, 219, 1, 230, 241, 70, 246,
      243, 121, 174, 67, 66, 11, 99, 202, 17, 52, 234, 78, 29, 3, 57, 51, 123, 149, 86, 64, 192, 73, 199, 108, 101, 55,
      232, 41, 114, 153, 237, 253, 52, 205, 148, 45, 86, 186, 241, 182, 183, 42, 77, 252, 195, 29, 158, 173, 3, 182,
      207, 254, 61, 71, 184, 167, 184\]);
  let keyPair = genKeyPairByData(pkData, skData);
  let inputUpdate: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan1', 'utf-8').buffer) };
  let inputSign: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan2', 'utf-8').buffer) };
  let signer = cryptoFramework.createSign('RSA1024|PKCS1|SHA256');
  signer.initSync(keyPair.priKey);
  signer.updateSync(inputUpdate);
  let signData = signer.signSync(inputSign);
  console.info('signData result: ' + signData.data);
}

#### \[h2\]setSignSpec10+

setSignSpec(itemType: SignSpecItem, itemValue: number): void

setSignSpec(itemType: SignSpecItem, itemValue: number | Uint8Array): void

Sets signing specifications. You can use this API to set signing parameters that cannot be set by [createSign](#cryptoframeworkcreatesign).

Currently, only RSA and SM2 are supported. Since API version 11, SM2 signing parameters can be set.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| itemType | [SignSpecItem](#signspecitem10) | Yes | Signing parameter to set. |
| itemValue | number | Uint8Array11+ | Yes | Value of the signing parameter to set. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function testSetSignSpec() {
  let signer = cryptoFramework.createSign('RSA|PSS|SHA256|MGF1\_SHA256');
  let setN = 20;
  signer.setSignSpec(cryptoFramework.SignSpecItem.PSS\_SALT\_LEN\_NUM, setN);
}

#### \[h2\]getSignSpec10+

getSignSpec(itemType: SignSpecItem): string | number

Obtains signing specifications. Currently, only RSA is supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| itemType | [SignSpecItem](#signspecitem10) | Yes | Signing parameter to obtain. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | number | Returns the value of the signing parameter obtained. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function testGetSignSpec() {
  let signer = cryptoFramework.createSign('RSA|PSS|SHA256|MGF1\_SHA256');
  let setN = 32;
  signer.setSignSpec(cryptoFramework.SignSpecItem.PSS\_SALT\_LEN\_NUM, setN);
  signer.getSignSpec(cryptoFramework.SignSpecItem.PSS\_SALT\_LEN\_NUM);
}

#### cryptoFramework.createVerify

createVerify(algName: string): Verify

Creates a **Verify** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| algName | string | Yes | 
Signing algorithm to use. Currently, RSA, ECC, DSA, SM210+ and Ed2551911+ are supported. If RSA PKCS1 is used, you must set the digest. If RSA PSS is used, you must set the digest and mask digest. When the RSA algorithm is used for signature verification, you can use **Recover** to verify and recover the signed data.

For details about the supported specifications, see [Signing and Signature Verification Overview and Algorithm Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-sign-sig-verify-overview).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Verify | Returns the **Verify** instance created. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let verifier1 = cryptoFramework.createVerify('RSA1024|PKCS1|SHA256');

let verifier2 = cryptoFramework.createVerify('RSA1024|PSS|SHA256|MGF1\_SHA256');

let verifier3 = cryptoFramework.createVerify('RSA1024|PKCS1|SHA256|Recover');

#### Verify

Provides APIs for signature verification. Before using any API of the **Verify** class, you must create a **Verify** instance by using [createVerify(algName: string): Verify](#cryptoframeworkcreateverify). Invoke **init()**, **update()**, and **verify()** in this class in sequence to complete the signature verification. For details about the sample code, see [Signing and Signature Verification with an RSA Key Pair (PKCS1 Mode)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1).

The **Verify** class does not support repeated initialization. When a new key is used for signature verification, you must create a new **Verify** instance and call **init()** for initialization.

The signature verification mode is determined in **createVerify()**, and the key is set by **init()**.

If the signed message is short, you can call **verify()** to pass in the signed message and signature (**signatureData**) for signature verification after **init()**. That is, you do not need to use **update()**.

If the signed message is too long, you can call **update()** multiple times to pass in the signed message by segment, and then call **verify()** to verify the full text of the message. In versions earlier than API version 10, the input parameter **data** of **verify()** supports only **DataBlob**. Since API version 10, **data** also supports **null**. After all the data is passed in by using **update()**, **verify()** can be called to verify the signature data.

If the DSA algorithm is used for signature verification and the digest algorithm is **NoHash**, **update()** is not supported. If **update()** is called in this case, **ERR\_CRYPTO\_OPERATION** will be returned.

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| algName | string | Yes | No | Algorithm to be used for signature verification. |

#### \[h2\]init

init(pubKey: PubKey, callback: AsyncCallback<void>): void

Initializes the **Verify** object using a public key. This API uses an asynchronous callback to return the result. **init**, **update**, and **verify** must be used together. **init** and **verify** are mandatory, and **update** is optional.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pubKey | [PubKey](#pubkey) | Yes | Public key used to initialize the **Verify** instance. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### \[h2\]init

init(pubKey: PubKey): Promise<void>

Initializes the **Verify** object using a public key. This API uses a promise to return the result. **init**, **update**, and **verify** must be used together. **init** and **verify** are mandatory, and **update** is optional.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pubKey | [PubKey](#pubkey) | Yes | Public key used to initialize the **Verify** instance. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### \[h2\]initSync12+

initSync(pubKey: PubKey): void

Initializes the **Verify** instance with a public key. This API returns the result synchronously. **initSync**, **updateSync**, and **verifySync** must be used together. **initSync** and **verifySync** are mandatory, and **updateSync** is optional.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pubKey | [PubKey](#pubkey) | Yes | Public key used to initialize the **Verify** instance. |

**Return value**

| Type | Description |
| :-- | :-- |
| void | No value is returned. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### \[h2\]update

update(data: DataBlob, callback: AsyncCallback<void>): void

Updates the data for signature verifications. This API uses an asynchronous callback to return the result.

This API can be called only after the [Verify](#verify) instance is initialized using [init](#init-4).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/VH9SF4cdSQ6kYk0N3Cq2Qg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E70532469627BCD8D823DF97CB100D17F1E7028D6DF9445D488AA1DB27E3D21)

You can call **update** multiple times or do not use **update** (call [verify](#verify-1) after [init](#init-4)), depending on the data volume.

The amount of the data to be passed in by **update()** (one-time or accumulative) is not limited. If there is a large amount of data, you are advised to call **update()** multiple times to pass in the data by segment. This prevents too much memory from being requested at a time.

For details about the sample code for calling **update()** multiple times in signature verification, see [Signing and Signature Verification by Segment with an RSA Key Pair (PKCS1 Mode)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1-by-segment). The operations of other algorithms are similar.

If the DSA algorithm is used for signature verification and the digest algorithm is **NoHash**, **update()** is not supported. If **update()** is called in this case, **ERR\_CRYPTO\_OPERATION** will be returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [DataBlob](#datablob) | Yes | Data to pass in. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### \[h2\]update

update(data: DataBlob): Promise<void>

Updates the data for signature verifications. This API uses a promise to return the result.

This API can be called only after the [Verify](#verify) instance is initialized using [init()](#init-5).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/xaOctLw1SHqFxjVq6Hluzw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2D8D80CCBDCC8CBF42CAEBF656BFB480BF4A4303D320FB917DEADFF05F6A286)

You can call **update** multiple times or do not use **update** (call [verify](#verify-2) after [init](#init-5)), depending on the data volume.

The amount of the data to be passed in by **update()** (one-time or accumulative) is not limited. If there is a large amount of data, you are advised to call **update()** multiple times to pass in the data by segment. This prevents too much memory from being requested at a time.

For details about the sample code for calling **update()** multiple times in signature verification, see [Signing and Signature Verification by Segment with an RSA Key Pair (PKCS1 Mode)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1-by-segment). The operations of other algorithms are similar.

If the DSA algorithm is used for signature verification and the digest algorithm is **NoHash**, **update()** is not supported. If **update()** is called in this case, **ERR\_CRYPTO\_OPERATION** will be returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [DataBlob](#datablob) | Yes | Data to pass in. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### \[h2\]updateSync12+

updateSync(data: DataBlob): void

Updates the data for signature verifications. This API returns the result synchronously.

This API can be called only after the [Verify](#verify) instance is initialized by using [initSync()](#initsync12-2).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/w7E35VotQri0GjCKBhsxUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=670752DB7B92AC6D57D69666EB7D96CE442963EAF0CA2FB5E7F53A4C140C7425)

You can call **updateSync** multiple times or do not use **updateSync** (call [verifySync](#verifysync12) after [initSync](#initsync12-2)), depending on the data volume.

The amount of the data to be passed in by **updateSync** (one-time or accumulative) is not limited. If there is a large amount of data, you are advised to call **updateSync** multiple times to pass in the data by segment. This prevents too much memory from being requested at a time.

For details about the sample code for calling **updateSync** multiple times in signature verification, see [Signing and Signature Verification by Segment with an RSA Key Pair (PKCS1 Mode)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1-by-segment). The operations of other algorithms are similar.

If the DSA algorithm is used for signature verification and the digest algorithm is **NoHash**, **updateSync** is not supported. If **updateSync** is called in this case, **ERR\_CRYPTO\_OPERATION** will be returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [DataBlob](#datablob) | Yes | Data to pass in. |

**Return value**

| Type | Description |
| :-- | :-- |
| void | No value is returned. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### \[h2\]verify

verify(data: DataBlob | null, signatureData: DataBlob, callback: AsyncCallback<boolean>): void

Verifies the signature of the data. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [DataBlob](#datablob) | null10+ | Yes | Data to pass in. In versions earlier than API version 10, only **DataBlob** is supported. Since API version 10, **null** is also supported. |
| signatureData | [DataBlob](#datablob) | Yes | Signature data. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the signature verification result. **true** means that the signature verification is successful; **false** otherwise. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### \[h2\]verify

verify(data: DataBlob | null, signatureData: DataBlob): Promise<boolean>

Verifies the signature of the data. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [DataBlob](#datablob) | null10+ | Yes | Data to pass in. In versions earlier than API version 10, only **DataBlob** is supported. Since API version 10, **null** is also supported. |
| signatureData | [DataBlob](#datablob) | Yes | Signature data. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. **true**: passed; **false**: failed. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### \[h2\]verifySync12+

verifySync(data: DataBlob | null, signatureData: DataBlob): boolean

Verifies the signature. This API returns the verification result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [DataBlob](#datablob) | null | Yes | Data to pass in. |
| signatureData | [DataBlob](#datablob) | Yes | Signature data. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Signature verification result. **true**: passed; **false**: failed. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

**Example (using the callback-based API)**

For more examples of signing and signature verification, see [Signing and Signature Verification with an RSA Key Pair (PKCS1 Mode)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1).

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function verifyByCallback() {
  let inputUpdate: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan1', 'utf-8').buffer) };
  let inputVerify: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan2', 'utf-8').buffer) };
  // Key generated based on the key data and input data for signature verification. If the data in verify() is the same as that in sign(), the signature verification is successful.
  let pkData =
    new Uint8Array(\[48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
      2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166, 209, 250, 142, 74, 216,
      58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31, 172, 151, 252, 185, 123,
      20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31, 214, 93, 115, 247, 69,
      94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176, 57, 125, 235, 51, 88,
      135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50, 189, 88, 254, 255, 146,
      244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1\]);
  let skData =
    new Uint8Array(\[48, 130, 2, 120, 2, 1, 0, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 4, 130, 2, 98, 48,
      130, 2, 94, 2, 1, 0, 2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166,
      209, 250, 142, 74, 216, 58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31,
      172, 151, 252, 185, 123, 20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31,
      214, 93, 115, 247, 69, 94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176,
      57, 125, 235, 51, 88, 135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50,
      189, 88, 254, 255, 146, 244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1, 2, 129, 129, 0, 152, 111, 145, 203, 10,
      88, 116, 163, 112, 126, 9, 20, 68, 34, 235, 121, 98, 14, 182, 102, 151, 125, 114, 91, 210, 122, 215, 29, 212, 5,
      176, 203, 238, 146, 5, 190, 41, 21, 91, 56, 125, 239, 111, 133, 53, 200, 192, 56, 132, 202, 42, 145, 120, 3, 224,
      40, 223, 46, 148, 29, 41, 92, 17, 40, 12, 72, 165, 69, 192, 211, 142, 233, 81, 202, 177, 235, 156, 27, 179, 48,
      18, 85, 154, 101, 193, 45, 218, 91, 24, 143, 196, 248, 16, 83, 177, 198, 136, 77, 111, 134, 60, 219, 95, 246, 23,
      5, 45, 14, 83, 29, 137, 248, 159, 28, 132, 142, 205, 99, 226, 213, 84, 232, 57, 130, 156, 81, 191, 237, 2, 65, 0,
      255, 158, 212, 13, 43, 132, 244, 135, 148, 161, 232, 219, 20, 81, 196, 102, 103, 44, 110, 71, 100, 62, 73, 200,
      32, 138, 114, 209, 171, 150, 179, 92, 198, 5, 190, 218, 79, 227, 227, 37, 32, 57, 159, 252, 107, 211, 139, 198,
      202, 248, 137, 143, 186, 205, 106, 81, 85, 207, 134, 148, 110, 204, 243, 27, 2, 65, 0, 215, 4, 181, 121, 57, 224,
      170, 168, 183, 159, 152, 8, 74, 233, 80, 244, 146, 81, 48, 159, 194, 199, 36, 187, 6, 181, 182, 223, 115, 133,
      151, 171, 78, 219, 90, 161, 248, 69, 6, 207, 173, 3, 81, 161, 2, 60, 238, 204, 177, 12, 138, 17, 220, 179, 71,
      113, 200, 248, 159, 153, 252, 150, 180, 155, 2, 65, 0, 190, 202, 185, 211, 170, 171, 238, 40, 84, 84, 21, 13, 144,
      57, 7, 178, 183, 71, 126, 120, 98, 229, 235, 4, 40, 229, 173, 149, 185, 209, 29, 199, 29, 54, 164, 161, 38, 8, 30,
      62, 83, 179, 47, 42, 165, 0, 156, 207, 160, 39, 169, 229, 81, 180, 136, 170, 116, 182, 20, 233, 45, 90, 100, 9, 2,
      65, 0, 152, 255, 47, 198, 15, 201, 238, 133, 89, 11, 133, 153, 184, 252, 37, 239, 177, 65, 118, 80, 231, 190, 222,
      66, 250, 118, 72, 166, 221, 67, 156, 245, 119, 138, 28, 6, 142, 107, 71, 122, 116, 200, 156, 199, 237, 152, 191,
      239, 4, 184, 64, 114, 143, 81, 62, 48, 23, 233, 217, 95, 47, 221, 104, 171, 2, 64, 30, 219, 1, 230, 241, 70, 246,
      243, 121, 174, 67, 66, 11, 99, 202, 17, 52, 234, 78, 29, 3, 57, 51, 123, 149, 86, 64, 192, 73, 199, 108, 101, 55,
      232, 41, 114, 153, 237, 253, 52, 205, 148, 45, 86, 186, 241, 182, 183, 42, 77, 252, 195, 29, 158, 173, 3, 182,
      207, 254, 61, 71, 184, 167, 184\]);
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pkData };
  let priKeyBlob: cryptoFramework.DataBlob = { data: skData };
  // The data is signData.data in Sign().
  let signMessageBlob: cryptoFramework.DataBlob = {
    data: new Uint8Array(\[9, 68, 164, 161, 230, 155, 255, 153, 10, 12, 14, 22, 146, 115, 209, 167, 223, 133, 89, 173,
      50, 249, 176, 104, 10, 251, 219, 104, 117, 196, 105, 65, 249, 139, 119, 41, 15, 171, 191, 11, 177, 177, 1, 119,
      130, 142, 87, 183, 32, 220, 226, 28, 38, 73, 222, 172, 153, 26, 87, 58, 188, 42, 150, 67, 94, 214, 147, 64, 202,
      87, 155, 125, 254, 112, 95, 176, 255, 207, 106, 43, 228, 153, 131, 240, 120, 88, 253, 179, 207, 207, 110, 223,
      173, 15, 113, 11, 183, 122, 237, 205, 206, 123, 246, 33, 167, 169, 251, 237, 199, 26, 220, 152, 190, 117, 131, 74,
      232, 50, 39, 172, 232, 178, 112, 73, 251, 235, 131, 209\])
  }
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let verifier = cryptoFramework.createVerify('RSA1024|PKCS1|SHA256');
  rsaGenerator.convertKey(pubKeyBlob, priKeyBlob, (err, keyPair) => {
    verifier.init(keyPair.pubKey, err => {
      verifier.update(inputUpdate, err => {
        verifier.verify(inputVerify, signMessageBlob, (err, res) => {
          console.info('verify result = ' + res);
        });
      });
    });
  });
}

**Example (using the promise-based API)**

For more examples, see [Signing and Signature Verification with an RSA Key Pair](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1).

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

async function genKeyPairByData(pubKeyData: Uint8Array, priKeyData: Uint8Array) {
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyData };
  let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyData };
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let keyPair = await rsaGenerator.convertKey(pubKeyBlob, priKeyBlob);
  console.info('convertKey result: success.');
  return keyPair;
}

async function verifyByPromise() {
  // Key generated based on the key data and input data for signature verification. If the data in verify() is the same as that in sign(), the signature verification is successful.
  let pkData =
    new Uint8Array(\[48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
      2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166, 209, 250, 142, 74, 216,
      58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31, 172, 151, 252, 185, 123,
      20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31, 214, 93, 115, 247, 69,
      94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176, 57, 125, 235, 51, 88,
      135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50, 189, 88, 254, 255, 146,
      244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1\]);
  let skData =
    new Uint8Array(\[48, 130, 2, 120, 2, 1, 0, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 4, 130, 2, 98, 48,
      130, 2, 94, 2, 1, 0, 2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166,
      209, 250, 142, 74, 216, 58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31,
      172, 151, 252, 185, 123, 20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31,
      214, 93, 115, 247, 69, 94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176,
      57, 125, 235, 51, 88, 135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50,
      189, 88, 254, 255, 146, 244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1, 2, 129, 129, 0, 152, 111, 145, 203, 10,
      88, 116, 163, 112, 126, 9, 20, 68, 34, 235, 121, 98, 14, 182, 102, 151, 125, 114, 91, 210, 122, 215, 29, 212, 5,
      176, 203, 238, 146, 5, 190, 41, 21, 91, 56, 125, 239, 111, 133, 53, 200, 192, 56, 132, 202, 42, 145, 120, 3, 224,
      40, 223, 46, 148, 29, 41, 92, 17, 40, 12, 72, 165, 69, 192, 211, 142, 233, 81, 202, 177, 235, 156, 27, 179, 48,
      18, 85, 154, 101, 193, 45, 218, 91, 24, 143, 196, 248, 16, 83, 177, 198, 136, 77, 111, 134, 60, 219, 95, 246, 23,
      5, 45, 14, 83, 29, 137, 248, 159, 28, 132, 142, 205, 99, 226, 213, 84, 232, 57, 130, 156, 81, 191, 237, 2, 65, 0,
      255, 158, 212, 13, 43, 132, 244, 135, 148, 161, 232, 219, 20, 81, 196, 102, 103, 44, 110, 71, 100, 62, 73, 200,
      32, 138, 114, 209, 171, 150, 179, 92, 198, 5, 190, 218, 79, 227, 227, 37, 32, 57, 159, 252, 107, 211, 139, 198,
      202, 248, 137, 143, 186, 205, 106, 81, 85, 207, 134, 148, 110, 204, 243, 27, 2, 65, 0, 215, 4, 181, 121, 57, 224,
      170, 168, 183, 159, 152, 8, 74, 233, 80, 244, 146, 81, 48, 159, 194, 199, 36, 187, 6, 181, 182, 223, 115, 133,
      151, 171, 78, 219, 90, 161, 248, 69, 6, 207, 173, 3, 81, 161, 2, 60, 238, 204, 177, 12, 138, 17, 220, 179, 71,
      113, 200, 248, 159, 153, 252, 150, 180, 155, 2, 65, 0, 190, 202, 185, 211, 170, 171, 238, 40, 84, 84, 21, 13, 144,
      57, 7, 178, 183, 71, 126, 120, 98, 229, 235, 4, 40, 229, 173, 149, 185, 209, 29, 199, 29, 54, 164, 161, 38, 8, 30,
      62, 83, 179, 47, 42, 165, 0, 156, 207, 160, 39, 169, 229, 81, 180, 136, 170, 116, 182, 20, 233, 45, 90, 100, 9, 2,
      65, 0, 152, 255, 47, 198, 15, 201, 238, 133, 89, 11, 133, 153, 184, 252, 37, 239, 177, 65, 118, 80, 231, 190, 222,
      66, 250, 118, 72, 166, 221, 67, 156, 245, 119, 138, 28, 6, 142, 107, 71, 122, 116, 200, 156, 199, 237, 152, 191,
      239, 4, 184, 64, 114, 143, 81, 62, 48, 23, 233, 217, 95, 47, 221, 104, 171, 2, 64, 30, 219, 1, 230, 241, 70, 246,
      243, 121, 174, 67, 66, 11, 99, 202, 17, 52, 234, 78, 29, 3, 57, 51, 123, 149, 86, 64, 192, 73, 199, 108, 101, 55,
      232, 41, 114, 153, 237, 253, 52, 205, 148, 45, 86, 186, 241, 182, 183, 42, 77, 252, 195, 29, 158, 173, 3, 182,
      207, 254, 61, 71, 184, 167, 184\]);
  let keyPair = await genKeyPairByData(pkData, skData);
  let inputUpdate: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan1', 'utf-8').buffer) };
  let inputVerify: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan2', 'utf-8').buffer) };
  // The data is signData.data in Sign().
  let signMessageBlob: cryptoFramework.DataBlob = {
    data: new Uint8Array(\[9, 68, 164, 161, 230, 155, 255, 153, 10, 12, 14, 22, 146, 115, 209, 167, 223, 133, 89, 173,
      50, 249, 176, 104, 10, 251, 219, 104, 117, 196, 105, 65, 249, 139, 119, 41, 15, 171, 191, 11, 177, 177, 1, 119,
      130, 142, 87, 183, 32, 220, 226, 28, 38, 73, 222, 172, 153, 26, 87, 58, 188, 42, 150, 67, 94, 214, 147, 64, 202,
      87, 155, 125, 254, 112, 95, 176, 255, 207, 106, 43, 228, 153, 131, 240, 120, 88, 253, 179, 207, 207, 110, 223,
      173, 15, 113, 11, 183, 122, 237, 205, 206, 123, 246, 33, 167, 169, 251, 237, 199, 26, 220, 152, 190, 117, 131, 74,
      232, 50, 39, 172, 232, 178, 112, 73, 251, 235, 131, 209\])
  };
  let verifier = cryptoFramework.createVerify('RSA1024|PKCS1|SHA256');
  await verifier.init(keyPair.pubKey);
  await verifier.update(inputUpdate);
  let res = await verifier.verify(inputVerify, signMessageBlob);
  console.info('verify result: ' + res);
}

**Example (using the sync API)**

For more examples of signing and signature verification, see [Signing and Signature Verification with an RSA Key Pair (PKCS1 Mode)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1).

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function genKeyPairByData(pubKeyData: Uint8Array, priKeyData: Uint8Array) {
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyData };
  let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyData };
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let keyPair = rsaGenerator.convertKeySync(pubKeyBlob, priKeyBlob);
  console.info('convertKey result: success.');
  return keyPair;
}

function verifyBySync() {
  // Key generated based on the key data and input data for signature verification. If the data in verify() is the same as that in sign(), the signature verification is successful.
  let pkData =
    new Uint8Array(\[48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
      2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166, 209, 250, 142, 74, 216,
      58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31, 172, 151, 252, 185, 123,
      20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31, 214, 93, 115, 247, 69,
      94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176, 57, 125, 235, 51, 88,
      135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50, 189, 88, 254, 255, 146,
      244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1\]);
  let skData =
    new Uint8Array(\[48, 130, 2, 120, 2, 1, 0, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 4, 130, 2, 98, 48,
      130, 2, 94, 2, 1, 0, 2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166,
      209, 250, 142, 74, 216, 58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31,
      172, 151, 252, 185, 123, 20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31,
      214, 93, 115, 247, 69, 94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176,
      57, 125, 235, 51, 88, 135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50,
      189, 88, 254, 255, 146, 244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1, 2, 129, 129, 0, 152, 111, 145, 203, 10,
      88, 116, 163, 112, 126, 9, 20, 68, 34, 235, 121, 98, 14, 182, 102, 151, 125, 114, 91, 210, 122, 215, 29, 212, 5,
      176, 203, 238, 146, 5, 190, 41, 21, 91, 56, 125, 239, 111, 133, 53, 200, 192, 56, 132, 202, 42, 145, 120, 3, 224,
      40, 223, 46, 148, 29, 41, 92, 17, 40, 12, 72, 165, 69, 192, 211, 142, 233, 81, 202, 177, 235, 156, 27, 179, 48,
      18, 85, 154, 101, 193, 45, 218, 91, 24, 143, 196, 248, 16, 83, 177, 198, 136, 77, 111, 134, 60, 219, 95, 246, 23,
      5, 45, 14, 83, 29, 137, 248, 159, 28, 132, 142, 205, 99, 226, 213, 84, 232, 57, 130, 156, 81, 191, 237, 2, 65, 0,
      255, 158, 212, 13, 43, 132, 244, 135, 148, 161, 232, 219, 20, 81, 196, 102, 103, 44, 110, 71, 100, 62, 73, 200,
      32, 138, 114, 209, 171, 150, 179, 92, 198, 5, 190, 218, 79, 227, 227, 37, 32, 57, 159, 252, 107, 211, 139, 198,
      202, 248, 137, 143, 186, 205, 106, 81, 85, 207, 134, 148, 110, 204, 243, 27, 2, 65, 0, 215, 4, 181, 121, 57, 224,
      170, 168, 183, 159, 152, 8, 74, 233, 80, 244, 146, 81, 48, 159, 194, 199, 36, 187, 6, 181, 182, 223, 115, 133,
      151, 171, 78, 219, 90, 161, 248, 69, 6, 207, 173, 3, 81, 161, 2, 60, 238, 204, 177, 12, 138, 17, 220, 179, 71,
      113, 200, 248, 159, 153, 252, 150, 180, 155, 2, 65, 0, 190, 202, 185, 211, 170, 171, 238, 40, 84, 84, 21, 13, 144,
      57, 7, 178, 183, 71, 126, 120, 98, 229, 235, 4, 40, 229, 173, 149, 185, 209, 29, 199, 29, 54, 164, 161, 38, 8, 30,
      62, 83, 179, 47, 42, 165, 0, 156, 207, 160, 39, 169, 229, 81, 180, 136, 170, 116, 182, 20, 233, 45, 90, 100, 9, 2,
      65, 0, 152, 255, 47, 198, 15, 201, 238, 133, 89, 11, 133, 153, 184, 252, 37, 239, 177, 65, 118, 80, 231, 190, 222,
      66, 250, 118, 72, 166, 221, 67, 156, 245, 119, 138, 28, 6, 142, 107, 71, 122, 116, 200, 156, 199, 237, 152, 191,
      239, 4, 184, 64, 114, 143, 81, 62, 48, 23, 233, 217, 95, 47, 221, 104, 171, 2, 64, 30, 219, 1, 230, 241, 70, 246,
      243, 121, 174, 67, 66, 11, 99, 202, 17, 52, 234, 78, 29, 3, 57, 51, 123, 149, 86, 64, 192, 73, 199, 108, 101, 55,
      232, 41, 114, 153, 237, 253, 52, 205, 148, 45, 86, 186, 241, 182, 183, 42, 77, 252, 195, 29, 158, 173, 3, 182,
      207, 254, 61, 71, 184, 167, 184\]);
  let keyPair = genKeyPairByData(pkData, skData);
  let inputUpdate: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan1', 'utf-8').buffer) };
  let inputVerify: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan2', 'utf-8').buffer) };
  // The data is signData.data in Sign().
  let signMessageBlob: cryptoFramework.DataBlob = {
    data: new Uint8Array(\[9, 68, 164, 161, 230, 155, 255, 153, 10, 12, 14, 22, 146, 115, 209, 167, 223, 133, 89, 173,
      50, 249, 176, 104, 10, 251, 219, 104, 117, 196, 105, 65, 249, 139, 119, 41, 15, 171, 191, 11, 177, 177, 1, 119,
      130, 142, 87, 183, 32, 220, 226, 28, 38, 73, 222, 172, 153, 26, 87, 58, 188, 42, 150, 67, 94, 214, 147, 64, 202,
      87, 155, 125, 254, 112, 95, 176, 255, 207, 106, 43, 228, 153, 131, 240, 120, 88, 253, 179, 207, 207, 110, 223,
      173, 15, 113, 11, 183, 122, 237, 205, 206, 123, 246, 33, 167, 169, 251, 237, 199, 26, 220, 152, 190, 117, 131, 74,
      232, 50, 39, 172, 232, 178, 112, 73, 251, 235, 131, 209\])
  };
  let verifier = cryptoFramework.createVerify('RSA1024|PKCS1|SHA256');
  verifier.initSync(keyPair.pubKey);
  verifier.updateSync(inputUpdate);
  let res = verifier.verifySync(inputVerify, signMessageBlob);
  console.info('verify result: ' + res);
}

#### \[h2\]recover12+

recover(signatureData: DataBlob): Promise<DataBlob | null>

Recovers the original data from a signature. This API returns the result synchronously. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/CeweQOxxQ1uu-nakkon8Og/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=245DF1FB17E883FF09F76FFAE4FFC0774C5CFA0E79B4C35579F2543965F69431)

-   Currently, only RSA is supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| signatureData | [DataBlob](#datablob) | Yes | Signature data. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DataBlob](#datablob) | null> | Data restored. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function genKeyPairByData(pubKeyData: Uint8Array, priKeyData: Uint8Array) {
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyData };
  let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyData };
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let keyPair = await rsaGenerator.convertKey(pubKeyBlob, priKeyBlob);
  console.info('convertKey result: success.');
  return keyPair;
}

async function recoverByPromise() {
  // Key generated based on the key data and input data for signature verification. If the data in verify() is the same as that in sign(), the signature verification is successful.
  let pkData =
    new Uint8Array(\[48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
      2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166, 209, 250, 142, 74, 216,
      58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31, 172, 151, 252, 185, 123,
      20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31, 214, 93, 115, 247, 69,
      94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176, 57, 125, 235, 51, 88,
      135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50, 189, 88, 254, 255, 146,
      244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1\]);
  let skData =
    new Uint8Array(\[48, 130, 2, 120, 2, 1, 0, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 4, 130, 2, 98, 48,
      130, 2, 94, 2, 1, 0, 2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166,
      209, 250, 142, 74, 216, 58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31,
      172, 151, 252, 185, 123, 20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31,
      214, 93, 115, 247, 69, 94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176,
      57, 125, 235, 51, 88, 135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50,
      189, 88, 254, 255, 146, 244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1, 2, 129, 129, 0, 152, 111, 145, 203, 10,
      88, 116, 163, 112, 126, 9, 20, 68, 34, 235, 121, 98, 14, 182, 102, 151, 125, 114, 91, 210, 122, 215, 29, 212, 5,
      176, 203, 238, 146, 5, 190, 41, 21, 91, 56, 125, 239, 111, 133, 53, 200, 192, 56, 132, 202, 42, 145, 120, 3, 224,
      40, 223, 46, 148, 29, 41, 92, 17, 40, 12, 72, 165, 69, 192, 211, 142, 233, 81, 202, 177, 235, 156, 27, 179, 48,
      18, 85, 154, 101, 193, 45, 218, 91, 24, 143, 196, 248, 16, 83, 177, 198, 136, 77, 111, 134, 60, 219, 95, 246, 23,
      5, 45, 14, 83, 29, 137, 248, 159, 28, 132, 142, 205, 99, 226, 213, 84, 232, 57, 130, 156, 81, 191, 237, 2, 65, 0,
      255, 158, 212, 13, 43, 132, 244, 135, 148, 161, 232, 219, 20, 81, 196, 102, 103, 44, 110, 71, 100, 62, 73, 200,
      32, 138, 114, 209, 171, 150, 179, 92, 198, 5, 190, 218, 79, 227, 227, 37, 32, 57, 159, 252, 107, 211, 139, 198,
      202, 248, 137, 143, 186, 205, 106, 81, 85, 207, 134, 148, 110, 204, 243, 27, 2, 65, 0, 215, 4, 181, 121, 57, 224,
      170, 168, 183, 159, 152, 8, 74, 233, 80, 244, 146, 81, 48, 159, 194, 199, 36, 187, 6, 181, 182, 223, 115, 133,
      151, 171, 78, 219, 90, 161, 248, 69, 6, 207, 173, 3, 81, 161, 2, 60, 238, 204, 177, 12, 138, 17, 220, 179, 71,
      113, 200, 248, 159, 153, 252, 150, 180, 155, 2, 65, 0, 190, 202, 185, 211, 170, 171, 238, 40, 84, 84, 21, 13, 144,
      57, 7, 178, 183, 71, 126, 120, 98, 229, 235, 4, 40, 229, 173, 149, 185, 209, 29, 199, 29, 54, 164, 161, 38, 8, 30,
      62, 83, 179, 47, 42, 165, 0, 156, 207, 160, 39, 169, 229, 81, 180, 136, 170, 116, 182, 20, 233, 45, 90, 100, 9, 2,
      65, 0, 152, 255, 47, 198, 15, 201, 238, 133, 89, 11, 133, 153, 184, 252, 37, 239, 177, 65, 118, 80, 231, 190, 222,
      66, 250, 118, 72, 166, 221, 67, 156, 245, 119, 138, 28, 6, 142, 107, 71, 122, 116, 200, 156, 199, 237, 152, 191,
      239, 4, 184, 64, 114, 143, 81, 62, 48, 23, 233, 217, 95, 47, 221, 104, 171, 2, 64, 30, 219, 1, 230, 241, 70, 246,
      243, 121, 174, 67, 66, 11, 99, 202, 17, 52, 234, 78, 29, 3, 57, 51, 123, 149, 86, 64, 192, 73, 199, 108, 101, 55,
      232, 41, 114, 153, 237, 253, 52, 205, 148, 45, 86, 186, 241, 182, 183, 42, 77, 252, 195, 29, 158, 173, 3, 182,
      207, 254, 61, 71, 184, 167, 184\]);
  let keyPair = await genKeyPairByData(pkData, skData);
  // The data is signData.data in Sign().
  let signMessageBlob: cryptoFramework.DataBlob = {
    data: new Uint8Array(\[9, 68, 164, 161, 230, 155, 255, 153, 10, 12, 14, 22, 146, 115, 209, 167, 223, 133, 89, 173,
      50, 249, 176, 104, 10, 251, 219, 104, 117, 196, 105, 65, 249, 139, 119, 41, 15, 171, 191, 11, 177, 177, 1, 119,
      130, 142, 87, 183, 32, 220, 226, 28, 38, 73, 222, 172, 153, 26, 87, 58, 188, 42, 150, 67, 94, 214, 147, 64, 202,
      87, 155, 125, 254, 112, 95, 176, 255, 207, 106, 43, 228, 153, 131, 240, 120, 88, 253, 179, 207, 207, 110, 223,
      173, 15, 113, 11, 183, 122, 237, 205, 206, 123, 246, 33, 167, 169, 251, 237, 199, 26, 220, 152, 190, 117, 131, 74,
      232, 50, 39, 172, 232, 178, 112, 73, 251, 235, 131, 209\])
  };
  let verifier = cryptoFramework.createVerify('RSA1024|PKCS1|SHA256|Recover');
  await verifier.init(keyPair.pubKey);
  try {
    let rawSignData = await verifier.recover(signMessageBlob);
    if (rawSignData != null) {
      console.info('\[Promise\]: recover result: ' + rawSignData.data);
    } else {
      console.error('\[Promise\]: get verify recover result: fail.');
    }
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`promise failed: errCode: ${e.code}, errMsg: ${e.message}\`);
  }
}

#### \[h2\]recoverSync12+

recoverSync(signatureData: DataBlob): DataBlob | null

Recovers the original data from a signature. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/VMDYGeSOSJSxxSape8PiDA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=082CB6663D078666FD12B932EFCCD4EBB93109358EB09D3D4BCA42B2C0AC56E0)

-   Currently, only RSA is supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| signatureData | [DataBlob](#datablob) | Yes | Signature data. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataBlob](#datablob) | null | Data restored. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### \[h2\]setVerifySpec10+

setVerifySpec(itemType: SignSpecItem, itemValue: number): void

setVerifySpec(itemType: SignSpecItem, itemValue: number | Uint8Array): void

Sets signature verification specifications. You can use this API to set signature verification parameters that cannot be set by [createVerify](#cryptoframeworkcreateverify).

Currently, only RSA and SM2 are supported. Since API version 11, SM2 signing parameters can be set.

The parameters for signature verification must be the same as those for signing.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| itemType | [SignSpecItem](#signspecitem10) | Yes | Signature verification parameter to set. |
| itemValue | number | Uint8Array11+ | Yes | Value of the signature verification parameter to set. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function testSetVerifySpec() {
  let verifier = cryptoFramework.createVerify('RSA2048|PSS|SHA256|MGF1\_SHA256');
  let setN = 20;
  verifier.setVerifySpec(cryptoFramework.SignSpecItem.PSS\_SALT\_LEN\_NUM, setN);
}

#### \[h2\]getVerifySpec10+

getVerifySpec(itemType: SignSpecItem): string | number

Obtains signature verification specifications. Currently, only RSA is supported.

The parameters for signature verification must be the same as those for signing.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Signature** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| itemType | [SignSpecItem](#signspecitem10) | Yes | Signature verification parameter to obtain. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | number | Returns the value of the parameter obtained. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function testGetVerifySpec() {
  let verifier = cryptoFramework.createVerify('RSA2048|PSS|SHA256|MGF1\_SHA256');
  let setN = 20;
  verifier.setVerifySpec(cryptoFramework.SignSpecItem.PSS\_SALT\_LEN\_NUM, setN);
  verifier.getVerifySpec(cryptoFramework.SignSpecItem.PSS\_SALT\_LEN\_NUM);
}

#### cryptoFramework.createKeyAgreement

createKeyAgreement(algName: string): KeyAgreement

Creates a **KeyAgreement** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.KeyAgreement

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.KeyAgreement** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| algName | string | Yes | 
Key agreement algorithm to use. In addition to ECC, X25519 and DH are supported since API version 11.

For details about the supported specifications, see [Key Agreement Overview and Algorithm Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-key-agreement-overview).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| KeyAgreement | Returns the **KeyAgreement** instance created. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let keyAgreement = cryptoFramework.createKeyAgreement('ECC256');

#### KeyAgreement

Provides APIs for key agreement operations. Before using any API of the **KeyAgreement** class, you must create a **KeyAgreement** instance by using [createKeyAgreement(algName: string): KeyAgreement](#cryptoframeworkcreatekeyagreement).

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.KeyAgreement

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.KeyAgreement** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| algName | string | Yes | No | Algorithm used for key agreement. |

#### \[h2\]generateSecret

generateSecret(priKey: PriKey, pubKey: PubKey, callback: AsyncCallback<DataBlob>): void

Generates a shared secret based on the given private key and public key. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.KeyAgreement

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.KeyAgreement** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| priKey | [PriKey](#prikey) | Yes | Private key used for key agreement. |
| pubKey | [PubKey](#pubkey) | Yes | Public key used for key agreement. |
| callback | AsyncCallback<[DataBlob](#datablob)\> | Yes | Callback used to return the shared key. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### \[h2\]generateSecret

generateSecret(priKey: PriKey, pubKey: PubKey): Promise<DataBlob>

Generates a shared secret based on the given private key and public key. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.KeyAgreement

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.KeyAgreement** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| priKey | [PriKey](#prikey) | Yes | Private key used for key agreement. |
| pubKey | [PubKey](#pubkey) | Yes | Public key used for key agreement. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DataBlob](#datablob)\> | Promise used to return the shared secret generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### \[h2\]generateSecretSync12+

generateSecretSync(priKey: PriKey, pubKey: PubKey): DataBlob

Generates a shared secret based on the given private key and public key. This API returns the shared secret generated synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.KeyAgreement

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| priKey | [PriKey](#prikey) | Yes | Private key used for key agreement. |
| pubKey | [PubKey](#pubkey) | Yes | Public key used for key agreement. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataBlob](#datablob) | Promise used to return the shared secret generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

**Example (using the callback-based API)**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testGenerateSecret() {
  let eccGen = cryptoFramework.createAsyKeyGenerator('ECC256');
  let globalKeyPair = await eccGen.generateKeyPair();
  let keyAgreement = cryptoFramework.createKeyAgreement('ECC256');
  keyAgreement.generateSecret(globalKeyPair.priKey, globalKeyPair.pubKey, (err, secret) => {
    if (err) {
      console.error('keyAgreement result: fail.');
      return;
    }
    console.info('keyAgreement output = ' + secret.data);
  });
}

**Example (using the promise-based API)**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function testGenerateSecret() {
  let eccGen = cryptoFramework.createAsyKeyGenerator('ECC256');
  let globalKeyPair = await eccGen.generateKeyPair();
  let keyAgreement = cryptoFramework.createKeyAgreement('ECC256');
  let keyAgreementPromise = keyAgreement.generateSecret(globalKeyPair.priKey, globalKeyPair.pubKey);
  keyAgreementPromise.then(secret => {
    console.info('keyAgreement output = ' + secret.data);
  }).catch((error: BusinessError) => {
    console.error(\`keyAgreement failed: errCode: ${error.code}, errMsg: ${error.message}\`);
  });
}

**Example (using the sync API)**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testGenerateSecretSync() {
  let eccGen = cryptoFramework.createAsyKeyGenerator('ECC256');
  let globalKeyPair = await eccGen.generateKeyPair();
  let keyAgreement = cryptoFramework.createKeyAgreement('ECC256');
  let secret = keyAgreement.generateSecretSync(globalKeyPair.priKey, globalKeyPair.pubKey);
  console.info('\[Sync\]keyAgreement output = ' + secret.data);
}

#### cryptoFramework.createMd

createMd(algName: string): Md

Creates an **Md** instance for MD operations.

For details about the supported specifications, see [Supported Algorithms and Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-generate-message-digest-overview#supported-algorithms-and-specifications).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.MessageDigest

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.MessageDigest** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| algName | string | Yes | MD algorithm to use. For details about the supported algorithms, see [Supported Algorithms and Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-generate-message-digest-overview#supported-algorithms-and-specifications). |

**Return value**

| Type | Description |
| :-- | :-- |
| Md | Returns the [Md](#md) instance created. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Set algName based on the algorithm supported.
  let md = cryptoFramework.createMd('SHA256');
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`sync failed: errCode: ${e.code}, errMsg: ${e.message}\`);
}

#### Md

Provides APIs for message digest (MD) operations. Before using any API of the **Md** class, you must create an **Md** instance by using [createMd](#cryptoframeworkcreatemd).

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.MessageDigest

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.MessageDigest** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| algName | string | Yes | No | Digest algorithm. |

#### \[h2\]update

update(input: DataBlob, callback: AsyncCallback<void>): void

Updates the MD status. This API uses an asynchronous callback to return the result. **update** must be used with **digest** together. **digest** is mandatory, and **update** is optional.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/_Zhpc5a0SN-kepjxVMXQog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51A150F87157F87298125B00F80D6889AFF46615684C3E7A3B5F4C850E6A0DE2)

For details about the code for calling **update** multiple times in an MD operation, see [MD (Passing In Data by Segment)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-generate-message-digest#generating-an-md-by-passing-in-data-by-segment).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.MessageDigest

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.MessageDigest** since API version 12.

**Differentiated device support**: This API runs properly on phones, PCs/2-in-1 devices, tablets, TVs, and wearables. However, if it is called on a lite wearable, **undefined** is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| input | [DataBlob](#datablob) | Yes | Data to pass in. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

#### \[h2\]update

update(input: DataBlob): Promise<void>

Updates the MD status. This API uses a promise to return the result. **update** must be used with **digest** together. **digest** is mandatory, and **update** is optional.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/Dad2Bl25R8eOSGsnZVhSXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3E718B2A837F8274E4E7D9518F5B5BB865839361733684F9282FEC15FB76D5C)

For details about the code for calling **update** multiple times in an MD operation, see [MD (Passing In Data by Segment)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-generate-message-digest#generating-an-md-by-passing-in-data-by-segment).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.MessageDigest

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.MessageDigest** since API version 12.

**Differentiated device support**: This API runs properly on phones, PCs/2-in-1 devices, tablets, TVs, and wearables. However, if it is called on a lite wearable, **undefined** is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| input | [DataBlob](#datablob) | Yes | Data to pass in. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

#### \[h2\]updateSync12+

updateSync(input: DataBlob): void

Updates the MD digest status. This API returns the result synchronously. **updateSync** must be used with **digestSync** together. **digestSync** is mandatory, and **updateSync** is optional.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/Paqivh-oTPGyb2KDvjGSWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=193D02CE7E785FF7FE74C4A3DD0C040575124720FBF286CC48203465E51280E2)

For details about the code for calling **updateSync** multiple times in an MD operation, see [MD (Passing In Data by Segment)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-generate-message-digest#generating-an-md-by-passing-in-data-by-segment).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.MessageDigest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| input | [DataBlob](#datablob) | Yes | Data to pass in. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

#### \[h2\]digest

digest(callback: AsyncCallback<DataBlob>): void

Generates a message digest (MD). This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.MessageDigest

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.MessageDigest** since API version 12.

**Differentiated device support**: This API runs properly on phones, PCs/2-in-1 devices, tablets, TVs, and wearables. However, if it is called on a lite wearable, **undefined** is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[DataBlob](#datablob)\> | Yes | Callback used to return a **DataBlob** object. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function mdByCallback() {
  let md = cryptoFramework.createMd('SHA256');
  md.update({ data: new Uint8Array(buffer.from('mdTestMessage', 'utf-8').buffer) }, (err) => {
    md.digest((err, digestOutput) => {
      console.info('\[Callback\]: MD result: ' + digestOutput.data);
      console.info('\[Callback\]: MD len: ' + md.getMdLength());
    });
  });
}

#### \[h2\]digest

digest(): Promise<DataBlob>

Generates an MD. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.MessageDigest

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.MessageDigest** since API version 12.

**Differentiated device support**: This API runs properly on phones, PCs/2-in-1 devices, tablets, TVs, and wearables. However, if it is called on a lite wearable, **undefined** is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DataBlob](#datablob)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

async function mdByPromise() {
  let md = cryptoFramework.createMd('SHA256');
  await md.update({ data: new Uint8Array(buffer.from('mdTestMessage', 'utf-8').buffer) });
  let mdOutput = await md.digest();
  console.info('\[Promise\]: MD result: ' + mdOutput.data);
  console.info('\[Promise\]: MD len: ' + md.getMdLength());
}

#### \[h2\]digestSync12+

digestSync(): DataBlob

Generates an MD. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.MessageDigest

**Return value**

| Type | Description |
| :-- | :-- |
| [DataBlob](#datablob) | MD generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

async function mdBySync() {
  let md = cryptoFramework.createMd('SHA256');
  md.updateSync({ data: new Uint8Array(buffer.from('mdTestMessage', 'utf-8').buffer) });
  let mdOutput = md.digestSync();
  console.info('\[Sync\]: MD result: ' + mdOutput.data);
  console.info('\[Sync\]: MD len: ' + md.getMdLength());
}

#### \[h2\]getMdLength

getMdLength(): number

Obtains the MD length, in bytes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.MessageDigest

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.MessageDigest** since API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| number | MD length obtained. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function getLength() {
  let md = cryptoFramework.createMd('SHA256');
  console.info('\[Promise\]: MD len: ' + md.getMdLength());
}

#### cryptoFramework.createMac

createMac(algName: string): Mac

Creates a **Mac** instance for MAC operations.

For details about the supported specifications, see [MAC Overview and Algorithm Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-compute-mac-overview).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Mac

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Mac** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| algName | string | Yes | Specifies the digest algorithm. For details about the supported algorithms, see [MAC Overview and Algorithm Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-compute-mac-overview). |

**Return value**

| Type | Description |
| :-- | :-- |
| Mac | Returns the [Mac](#mac) instance created. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Set algName based on the algorithm supported.
  let mac = cryptoFramework.createMac('SHA256');
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`sync failed: errCode: ${e.code}, errMsg: ${e.message}\`);
}

#### cryptoFramework.createMac18+

createMac(macSpec: MacSpec): Mac

Creates a **Mac** instance for message authentication code (MAC) operations.

For details about the supported specifications, see [MAC Overview and Algorithm Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-compute-mac-overview).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Security.CryptoFramework.Mac

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| macSpec | [MacSpec](#macspec18) | Yes | Specifies the input parameter struct based on the MAC algorithm. For details about the supported algorithms, see [MAC Overview and Algorithm Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-compute-mac-overview). |

**Return value**

| Type | Description |
| :-- | :-- |
| Mac | [Mac](#mac) instance created. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Set algName based on the algorithm supported.
  let spec: cryptoFramework.HmacSpec = {
    algName: 'HMAC',
    mdName: 'SHA256',
  };
  let mac = cryptoFramework.createMac(spec);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`sync failed: errCode: ${error.code}, errMsg: ${error.message}\`);
}

#### Mac

Provides APIs for message authentication code (MAC) operations. Before using any API of the **Mac** class, you must create a **Mac** instance by using [createMac](#cryptoframeworkcreatemac).

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Mac

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Mac** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| algName | string | Yes | No | Digest algorithm. |

#### \[h2\]init

init(key: SymKey, callback: AsyncCallback<void>): void

Initializes the MAC computation using a symmetric key. This API uses an asynchronous callback to return the result. **init**, **update**, and **doFinal** must be used together. **init** and **doFinal** are mandatory, and **update** is optional.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/E7l-6IS2RK-5GGGtMpmPRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA42B8B4DA2AA452DCF60D41868D8A254B86A088082454EDD7E9EE9C5A5374B2)

You are advised to create a symmetric key generator based on the [HMAC key generation specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-sym-key-generation-conversion-spec#hmac) and use [generateSymKey](#generatesymkey) to randomly generate a symmetric key or use [convertKey](#convertkey) to convert the binary data (whose length is the same as the key specifications) into a key.

If **HMAC** is specified to generate the symmetric key generator, only [convertKey](#convertkey) can be called to pass in a binary key of 1 to 4096 bytes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Mac

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Mac** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | [SymKey](#symkey) | Yes | Symmetric key obtained. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

#### \[h2\]init

init(key: SymKey): Promise<void>

Initializes the MAC computation using a symmetric key. This API uses a promise to return the result. **init**, **update**, and **doFinal** must be used together. **init** and **doFinal** are mandatory, and **update** is optional.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Mac

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Mac** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | [SymKey](#symkey) | Yes | Symmetric key obtained. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

#### \[h2\]initSync12+

initSync(key: SymKey): void

Initializes the MAC computation using a symmetric key. This API returns the result synchronously. **initSync**, **updateSync**, and **doFinalSync** must be used together. **initSync** and **doFinalSync** are mandatory, and **updateSync** is optional.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Mac

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | [SymKey](#symkey) | Yes | Symmetric key obtained. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

#### \[h2\]update

update(input: DataBlob, callback: AsyncCallback<void>): void

Updates the MAC status. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/2rWGINrARlyKbrWUI3E7Dw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC4C32AAD7F07EE9A33C8648A2C26E9F530C9E07E5D49AA01F1A8BA08A31D908)

For details about the sample code for calling **update** multiple times in an HMAC operation, see [Generating an HMAC by Passing In Data by Segment](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-compute-hmac#generating-an-hmac-by-passing-in-data-by-segment).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Mac

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Mac** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| input | [DataBlob](#datablob) | Yes | Data to pass in. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

#### \[h2\]update

update(input: DataBlob): Promise<void>

Updates the MAC status. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/4LWhYBh_RPeXmO4E9LOE5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8E0DD4034A54D0DA91F41A80DB1236274EC8E5C66A3C56FA0287D5B3D996BD79)

For details about the sample code for calling **update** multiple times in an HMAC operation, see [Generating an HMAC by Passing In Data by Segment](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-compute-hmac#generating-an-hmac-by-passing-in-data-by-segment).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Mac

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Mac** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| input | [DataBlob](#datablob) | Yes | Data to pass in. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

#### \[h2\]updateSync12+

updateSync(input: DataBlob): void

Updates the MAC status. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/COzLrgc6STCImGv2lUXq3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062330Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83EFF26D544BC11EDD2B192F691F27ED6C2412A6F93C8F4F762C8A9C55700B92)

For details about the sample code for calling **updateSync** multiple times in an HMAC operation, see [Generating an HMAC by Passing In Data by Segment](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-compute-hmac#generating-an-hmac-by-passing-in-data-by-segment).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Mac

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| input | [DataBlob](#datablob) | Yes | Data to pass in. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

#### \[h2\]doFinal

doFinal(callback: AsyncCallback<DataBlob>): void

MAC computation result. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Mac

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Mac** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[DataBlob](#datablob)\> | Yes | Callback used to return a **DataBlob** object. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

For more HMAC operation examples, see [Generating an HMAC by Passing In Data by Segment](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-compute-hmac#generating-an-hmac-by-passing-in-data-by-segment).

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function hmacByCallback() {
  let mac = cryptoFramework.createMac('SHA256');
  let keyBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer) };
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  symKeyGenerator.convertKey(keyBlob, (err, symKey) => {
    mac.init(symKey, (err) => {
      mac.update({ data: new Uint8Array(buffer.from('hmacTestMessage', 'utf-8').buffer) }, (err) => {
        mac.doFinal((err, output) => {
          console.info('\[Callback\]: HMAC result: ' + output.data);
          console.info('\[Callback\]: MAC len: ' + mac.getMacLength());
        });
      });
    });
  });
}

#### \[h2\]doFinal

doFinal(): Promise<DataBlob>

MAC computation result. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Mac

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Mac** since API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DataBlob](#datablob)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

For more HMAC operation examples, see [Generating an HMAC by Passing In Data by Segment](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-compute-hmac#generating-an-hmac-by-passing-in-data-by-segment).

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

async function hmacByPromise() {
  let mac = cryptoFramework.createMac('SHA256');
  let keyBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer) };
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let symKey = await symKeyGenerator.convertKey(keyBlob);
  await mac.init(symKey);
  await mac.update({ data: new Uint8Array(buffer.from('hmacTestMessage', 'utf-8').buffer) });
  let macOutput = await mac.doFinal();
  console.info('\[Promise\]: HMAC result: ' + macOutput.data);
  console.info('\[Promise\]: MAC len: ' + mac.getMacLength());
}

#### \[h2\]doFinalSync12+

doFinalSync(): DataBlob

Finishes the MAC computation. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Mac

**Return value**

| Type | Description |
| :-- | :-- |
| [DataBlob](#datablob) | MAC computation result. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

**Example**

For more HMAC operation examples, see [Generating an HMAC by Passing In Data by Segment](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-compute-hmac#generating-an-hmac-by-passing-in-data-by-segment).

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function hmacBySync() {
  let mac = cryptoFramework.createMac('SHA256');
  let keyBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer) };
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let symKey = symKeyGenerator.convertKeySync(keyBlob);
  mac.initSync(symKey);
  mac.updateSync({ data: new Uint8Array(buffer.from('hmacTestMessage', 'utf-8').buffer) });
  let macOutput = mac.doFinalSync();
  console.info('\[Sync\]: HMAC result: ' + macOutput.data);
  console.info('\[Sync\]: MAC len: ' + mac.getMacLength());
}

#### \[h2\]getMacLength

getMacLength(): number

Obtains the MAC length, in bytes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Mac

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Mac** since API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| number | MAC length obtained. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

function testGetMacLength() {
  let mac = cryptoFramework.createMac('SHA256');
  console.info('Mac algName is: ' + mac.algName);
  let keyData = new Uint8Array(\[83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159\]);
  let keyBlob: cryptoFramework.DataBlob = { data: keyData };
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let promiseConvertKey = symKeyGenerator.convertKey(keyBlob);
  promiseConvertKey.then(symKey => {
    let promiseMacInit = mac.init(symKey);
    return promiseMacInit;
  })
    .then(() => {
      let blob: cryptoFramework.DataBlob = { data: new Uint8Array(\[83\]) };
      let promiseMacUpdate = mac.update(blob);
      return promiseMacUpdate;
    })
    .then(() => {
      let promiseMacDoFinal = mac.doFinal();
      return promiseMacDoFinal;
    })
    .then(macOutput => {
      console.info('\[Promise\]: HMAC result: ' + macOutput.data);
      let macLen = mac.getMacLength();
      console.info('MAC len: ' + macLen);
    })
    .catch((error: BusinessError) => {
      console.error(\`\[Promise\] failed: errCode: ${error.code}, errMsg: ${error.message}\`);
    });
}

#### cryptoFramework.createRandom

createRandom(): Random

Creates a **Random** instance for generating random numbers and setting seeds.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Security.CryptoFramework.Rand

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Rand** since API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| [Random](#random) | 
Returns the [Random](#random) instance created.

For details about the supported specifications, see [Supported Algorithms and Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-generate-random-number#supported-algorithms-and-specifications).

 |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17620001 | memory operation failed. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let rand = cryptoFramework.createRandom();
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`sync failed: errCode: ${e.code}, errMsg: ${e.message}\`);
}

#### Random

Provides APIs for random number operations. Before using any API of the **Random** class, you must create a **Random** instance by using [createRandom](#cryptoframeworkcreaterandom).

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Security.CryptoFramework.Rand

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Rand** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| algName10+ | string | Yes | No | Algorithm used to generate the random number. Currently, only **CTR\_DRBG** is supported. |

#### \[h2\]generateRandom

generateRandom(len: number, callback: AsyncCallback<DataBlob>): void

Generates a random number of the specified length. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Security.CryptoFramework.Rand

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Rand** since API version 12.

**Differentiated device support**: This API runs properly on phones, PCs/2-in-1 devices, tablets, TVs, and wearables. However, if it is called on a lite wearable, **undefined** is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| len | number | Yes | Length of the random number to generate, in bytes. The value range is \[1, INT\_MAX\]. |
| callback | AsyncCallback<[DataBlob](#datablob)\> | Yes | Callback used to return a **DataBlob** object. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let rand = cryptoFramework.createRandom();
rand.generateRandom(12, (err, randData) => {
  if (err) {
    console.error(\`\[Callback\] failed, errCode: ${err.code}, errMsg: ${err.message}\`);
  } else {
    console.info('\[Callback\]: generate random result: ' + randData.data);
  }
});

#### \[h2\]generateRandom

generateRandom(len: number): Promise<DataBlob>

Generates a random number of the specified length. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Security.CryptoFramework.Rand

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Rand** since API version 12.

**Differentiated device support**: This API runs properly on phones, PCs/2-in-1 devices, tablets, TVs, and wearables. However, if it is called on a lite wearable, **undefined** is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| len | number | Yes | Length of the random number to generate, in bytes. The value range is \[1, INT\_MAX\]. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DataBlob](#datablob)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rand = cryptoFramework.createRandom();
let promiseGenerateRand = rand.generateRandom(12);
promiseGenerateRand.then(randData => {
  console.info('\[Promise\]: rand result: ' + randData.data);
}).catch((error: BusinessError) => {
  console.error(\`\[Promise\] failed: errCode: ${error.code}, errMsg: ${error.message}\`);
});

#### \[h2\]generateRandomSync10+

generateRandomSync(len: number): DataBlob

Generates a random number of the specified length. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Security.CryptoFramework.Rand

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 10 to 11, and **SystemCapability.Security.CryptoFramework.Rand** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| len | number | Yes | Length of the random number to generate, in bytes. The value range is \[1, INT\_MAX\]. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataBlob](#datablob) | Returns the generated random number. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rand = cryptoFramework.createRandom();
try {
  let randData = rand.generateRandomSync(12);
  if (randData != null) {
    console.info('\[Sync\]: rand result: ' + randData.data);
  } else {
    console.error('\[Sync\]: get rand result: fail.');
  }
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`sync failed: errCode: ${e.code}, errMsg: ${e.message}\`);
}

#### \[h2\]enableHardwareEntropy21+

enableHardwareEntropy(): void

Enables the hardware entropy source.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.Security.CryptoFramework.Rand

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rand = cryptoFramework.createRandom();
rand.enableHardwareEntropy();
rand.generateRandom(12, (err, randData) => {
  if (err) {
    console.error('\[Callback\] err: ' + err.code);
  } else {
    console.info('\[Callback\]: generate random result: ' + randData.data);
    try {
      rand.setSeed(randData);
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(\`sync failed: errCode: ${e.code}, errMsg: ${e.message}\`);
    }
  }
});

#### \[h2\]setSeed

setSeed(seed: DataBlob): void

Sets a seed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Security.CryptoFramework.Rand

The system capability is **SystemCapability.Security.CryptoFramework** in API versions 9 to 11, and **SystemCapability.Security.CryptoFramework.Rand** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| seed | [DataBlob](#datablob) | Yes | Seed to set. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17620001 | memory operation failed. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rand = cryptoFramework.createRandom();
rand.generateRandom(12, (err, randData) => {
  if (err) {
    console.error('\[Callback\] err: ' + err.code);
  } else {
    console.info('\[Callback\]: generate random result: ' + randData.data);
    try {
      rand.setSeed(randData);
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(\`sync failed: errCode: ${e.code}, errMsg: ${e.message}\`);
    }
  }
});

#### cryptoFramework.createKdf11+

createKdf(algName: string): Kdf

Creates a key derivation function instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Kdf

The system capability is **SystemCapability.Security.CryptoFramework** in API version 11, and **SystemCapability.Security.CryptoFramework.Kdf** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| algName | string | Yes | 
Key derivation algorithm (including the hash function for the HMAC). Currently, only PBKDF2, HKDF, and scrypt are supported. For example, **PBKDF2|SHA256**, **HKDF|SHA256**, or **SCRYPT**.

For details about the supported specifications, see [Key Derivation Overview and Algorithm Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-key-derivation-overview).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [Kdf](#kdf11) | Key derivation function instance created. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |

**Example**

-   PBKDF2

import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');

#### Kdf11+

Defines the key derivation function class. Before using APIs of this class, you need to create an instance of this class by using **createKdf(algName: string): Kdf**.

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Kdf

The system capability is **SystemCapability.Security.CryptoFramework** in API version 11, and **SystemCapability.Security.CryptoFramework.Kdf** since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| algName | string | Yes | No | Algorithm of the key derivation function. |

#### \[h2\]generateSecret11+

generateSecret(params: KdfSpec, callback: AsyncCallback<DataBlob>): void

Generates a key based on the specified key derivation parameters. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Kdf

The system capability is **SystemCapability.Security.CryptoFramework** in API version 11, and **SystemCapability.Security.CryptoFramework.Kdf** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| params | [KdfSpec](#kdfspec11) | Yes | Parameters of the key derivation function. |
| callback | AsyncCallback<[DataBlob](#datablob)\> | Yes | Callback used to return the derived key generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620003 | 

parameter check failed. Possible causes:

1\. Invalid key length in the params;

2\. Invalid info length in the params;

3\. Invalid keySize in the params.

 |
| 17630001 | crypto operation error. |

**Example**

-   PBKDF2
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    
    let spec: cryptoFramework.PBKDF2Spec = {
      algName: 'PBKDF2',
      password: '123456',
      salt: new Uint8Array(16),
      iterations: 10000,
      keySize: 32
    };
    let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');
    kdf.generateSecret(spec, (err, secret) => {
      if (err) {
        console.error('key derivation result: fail.');
        return;
      }
      console.info('key derivation output = ' + secret.data);
    });
    
-   HKDF
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    
    let spec: cryptoFramework.HKDFSpec = {
      algName: 'HKDF',
      key: '123456',
      salt: new Uint8Array(16),
      info: new Uint8Array(16),
      keySize: 32
    };
    let kdf = cryptoFramework.createKdf('HKDF|SHA256|EXTRACT\_AND\_EXPAND');
    kdf.generateSecret(spec, (err, secret) => {
      if (err) {
        console.error('key derivation result: fail.');
        return;
      }
      console.info('key derivation output = ' + secret.data);
    });
    

#### \[h2\]generateSecret11+

generateSecret(params: KdfSpec): Promise<DataBlob>

Generates a key based on the specified key derivation parameters. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Kdf

The system capability is **SystemCapability.Security.CryptoFramework** in API version 11, and **SystemCapability.Security.CryptoFramework.Kdf** since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| params | [KdfSpec](#kdfspec11) | Yes | Parameters of the key derivation function. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DataBlob](#datablob)\> | Promise used to return the derived key generated. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620003 | 

parameter check failed. Possible causes:

1\. Invalid key length in the params;

2\. Invalid info length in the params;

3\. Invalid keySize in the params.

 |
| 17630001 | crypto operation error. |

**Example**

-   PBKDF2
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    let spec: cryptoFramework.PBKDF2Spec = {
      algName: 'PBKDF2',
      password: '123456',
      salt: new Uint8Array(16),
      iterations: 10000,
      keySize: 32
    };
    let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');
    let kdfPromise = kdf.generateSecret(spec);
    kdfPromise.then(secret => {
      console.info('key derivation output = ' + secret.data);
    }).catch((error: BusinessError) => {
      console.error(\`key derivation failed: errCode: ${error.code}, errMsg: ${error.message}\`);
    });
    
-   HKDF
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    let spec: cryptoFramework.HKDFSpec = {
      algName: 'HKDF',
      key: '123456',
      salt: new Uint8Array(16),
      info: new Uint8Array(16),
      keySize: 32
    };
    let kdf = cryptoFramework.createKdf('HKDF|SHA256|EXTRACT\_AND\_EXPAND');
    let kdfPromise = kdf.generateSecret(spec);
    kdfPromise.then(secret => {
      console.info('key derivation output = ' + secret.data);
    }).catch((error: BusinessError) => {
      console.error(\`key derivation failed: errCode: ${error.code}, errMsg: ${error.message}\`);
    });
    

#### \[h2\]generateSecretSync12+

generateSecretSync(params: KdfSpec): DataBlob

Generates a key based on the specified key derivation parameters. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Security.CryptoFramework.Kdf

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| params | [KdfSpec](#kdfspec11) | Yes | Parameters of the key derivation function. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataBlob](#datablob) | Key derived. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
invalid parameters. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | 

parameter check failed. Possible causes:

1\. Invalid key length in the params;

2\. Invalid info length in the params;

3\. Invalid keySize in the params.

 |
| 17630001 | crypto operation error. |

**Example**

-   PBKDF2
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    
    let spec: cryptoFramework.PBKDF2Spec = {
      algName: 'PBKDF2',
      password: '123456',
      salt: new Uint8Array(16),
      iterations: 10000,
      keySize: 32
    };
    let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');
    let secret = kdf.generateSecretSync(spec);
    console.info('\[Sync\]key derivation output = ' + secret.data);
    
-   HKDF
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    
    let spec: cryptoFramework.HKDFSpec = {
      algName: 'HKDF',
      key: '123456',
      salt: new Uint8Array(16),
      info: new Uint8Array(16),
      keySize: 32
    };
    let kdf = cryptoFramework.createKdf('HKDF|SHA256|EXTRACT\_AND\_EXPAND');
    let secret = kdf.generateSecretSync(spec);
    console.info('\[Sync\]key derivation output = ' + secret.data);
    

#### SignatureUtils20+

Provides utilities for converting SM2 data.

#### \[h2\]genEccSignatureSpec20+

static genEccSignatureSpec(data: Uint8Array): EccSignatureSpec

Generates r and s from the SM2 signature data in ASN1 DER format.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | Uint8Array | Yes | Signature data in ASN1 DER format. |

**Return value**

| Type | Description |
| :-- | :-- |
| [EccSignatureSpec](#eccsignaturespec20) | struct that contains r and s. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | 
parameter check failed. Possible causes:

1\. The length of the data parameter is 0 or too large.

 |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

function testGenEccSignatureSpec() {
  try {
    let data =
      new Uint8Array(\[48, 69, 2, 33, 0, 216, 15, 76, 238, 158, 165, 108, 76, 72, 63, 115, 52, 255, 51, 149, 54, 224,
        179, 49, 225, 70, 36, 117, 88, 154, 154, 27, 194, 161, 3, 1, 115, 2, 32, 51, 9, 53, 55, 248, 82, 7, 159, 179,
        144, 57, 151, 195, 17, 31, 106, 123, 32, 139, 219, 6, 253, 62, 240, 181, 134, 214, 107, 27, 230, 175, 40\])
    let spec: cryptoFramework.EccSignatureSpec = cryptoFramework.SignatureUtils.genEccSignatureSpec(data)
    console.info('genEccSignatureSpec result: success.');
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(\`ecc failed: errCode: ${e.code}, errMsg: ${e.message}\`);
  }
}

#### \[h2\]genEccSignature20+

static genEccSignature(spec: EccSignatureSpec): Uint8Array;

Converts an SM2 signature (r, s) to the ASN1 DER format.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Security.CryptoFramework.Signature

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| spec | [EccSignatureSpec](#eccsignaturespec20) | Yes | SM2 signature data to convert. |

**Return value**

| Type | Description |
| :-- | :-- |
| Uint8Array | Signature data in ASN1 DER format. |

**Error codes**

For details about the error codes, see [Crypto Framework Error Codes](../../error-codes/crypto-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | 
parameter check failed. Possible causes:

1\. The r or s value of the spec parameter is 0 or too large.

 |
| 17630001 | crypto operation error. |

**Example**

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

function testGenEccSignature() {
  try {
    let spec: cryptoFramework.EccSignatureSpec = {
      r: BigInt('97726608965854271693043443511967021777934035174185659091642456228829830775155'),
      s: BigInt('23084224202834231287427338597254751764391338275617140205467537273296855150376'),
    }

    let data = cryptoFramework.SignatureUtils.genEccSignature(spec)
    console.info('genEccSignature result: success.');
    console.info('data = ' + data)
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(\`ecc failed: errCode: ${e.code}, errMsg: ${e.message}\`);
  }
}
