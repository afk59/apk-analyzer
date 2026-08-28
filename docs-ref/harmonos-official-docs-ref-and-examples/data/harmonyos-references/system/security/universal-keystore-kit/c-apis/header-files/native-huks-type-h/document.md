# native\_huks\_type.h

#### Overview

Defines the enums, structs, and macros used in the HUKS functions.

**File to include**: <huks/native\_huks\_type.h>

**Library**: libhuks\_ndk.z.so

**System capability**: SystemCapability.Security.Huks.Core

The preceding system capability is available since API version 20. From API versions 9 to 19, the system capability is **SystemCapability.Security.Huks.Core**.

**Since**: 9

**Related module**: [HuksTypeApi](../../modules/hukstypeapi/document.md)

#### Summary

#### \[h2\]Structs

| Name | Description |
| :-- | :-- |
| [OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | Defines the struct of the returned data, including a status code and related description. |
| [OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) | Defines the struct of a binary large object (BLOB). |
| [OH\_Huks\_Param](../../structs/oh-huks-param/document.md) | Defines the struct of the parameters in a parameter set. |
| [OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) | Defines the struct of a parameter set. |
| [OH\_Huks\_CertChain](../../structs/oh-huks-certchain/document.md) | Defines the struct of a certificate chain. |
| [OH\_Huks\_KeyInfo](../../structs/oh-huks-keyinfo/document.md) | Defines the struct of key information. |
| [OH\_Huks\_PubKeyInfo](../../structs/oh-huks-pubkeyinfo/document.md) | Defines the struct of the public key information. |
| [OH\_Huks\_KeyMaterialRsa](../../structs/oh-huks-keymaterialrsa/document.md) | Defines the struct of a Rivest-Shamir-Adleman (RSA) key. |
| [OH\_Huks\_KeyMaterialEcc](../../structs/oh-huks-keymaterialecc/document.md) | Defines the struct of an Elliptic Curve Cryptography (ECC) key. |
| [OH\_Huks\_KeyMaterialDsa](../../structs/oh-huks-keymaterialdsa/document.md) | Defines the struct of a DSA key. |
| [OH\_Huks\_KeyMaterialDh](../../structs/oh-huks-keymaterialdh/document.md) | Defines the struct of a Diffie-Hellman (DH) key. |
| [OH\_Huks\_KeyMaterial25519](../../structs/oh-huks-keymaterial25519/document.md) | Defines the struct of a 25519 key. |
| [OH\_Huks\_KeyAliasSet](../../structs/oh-huks-keyaliasset/document.md) | Defines the struct of a key alias set. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Huks\_KeyPurpose](#oh_huks_keypurpose) | \- | Enumerates the key purposes. |
| [OH\_Huks\_KeyDigest](#oh_huks_keydigest) | \- | Enumerates the digest algorithms. |
| [OH\_Huks\_KeyPadding](#oh_huks_keypadding) | \- | Enumerates the padding algorithm types. |
| [OH\_Huks\_CipherMode](#oh_huks_ciphermode) | \- | Cipher mode. |
| [OH\_Huks\_KeySize](#oh_huks_keysize) | \- | Enumerates the key sizes of different algorithms. |
| [OH\_Huks\_KeyAlg](#oh_huks_keyalg) | \- | Enumerates the algorithms for keys. |
| [OH\_Huks\_AlgSuite](#oh_huks_algsuite) | \- | Enumerates the algorithm suites that can be used for importing of a key in cipher text. |
| [OH\_Huks\_KeyGenerateType](#oh_huks_keygeneratetype) | \- | Enumerates the types of the key generated. |
| [OH\_Huks\_KeyFlag](#oh_huks_keyflag) | \- | Enumerates the key generation types. |
| [OH\_Huks\_KeyStorageType](#oh_huks_keystoragetype) | \- | Enumerates the key storage types. |
| [OH\_Huks\_ImportKeyType](#oh_huks_importkeytype) | \- | Enumerates the types of the key to import. By default, a public key is imported. This field is not required when a symmetric key is imported. |
| [OH\_Huks\_RsaPssSaltLenType](#oh_huks_rsapsssaltlentype) | \- | Enumerates the length types of the salt value in PSS padding mode. |
| [OH\_Huks\_ErrCode](#oh_huks_errcode) | \- | Enumerates error codes. |
| [OH\_Huks\_TagType](#oh_huks_tagtype) | \- | Enumerates the types of the parameters in a parameter set. |
| [OH\_Huks\_UserAuthType](#oh_huks_userauthtype) | \- | Enumerates the user authentication types in key access control. |
| [OH\_Huks\_AuthAccessType](#oh_huks_authaccesstype) | \- | Enumerates the rules for invalidating a key. |
| [OH\_Huks\_AuthStorageLevel](#oh_huks_authstoragelevel) | \- | Enumerates the security levels for storing the key generated or imported. |
| [OH\_Huks\_ChallengeType](#oh_huks_challengetype) | \- | Enumerates the types of the challenge generated when a key is used. |
| [OH\_Huks\_UserAuthMode](#oh_huks_userauthmode) | \- | Enumerates the user authentication modes in key access control. |
| [OH\_Huks\_ChallengePosition](#oh_huks_challengeposition) | \- | Enumerates the positions of the 8-byte valid value in a custom challenge generated. |
| [OH\_Huks\_SecureSignType](#oh_huks_securesigntype) | \- | Enumerates the signature types of the key generated or imported. |
| [OH\_Huks\_KeyClassType](#oh_huks_keyclasstype) | OH\_Huks\_KeyClassType | Key type. |
| [OH\_Huks\_KeyWrapType](#oh_huks_keywraptype) | \- | Enumerates the wrap type of the key generated or imported. |
| [OH\_Huks\_Tag](#oh_huks_tag) | \- | Enumerates the tags contained in a parameter set. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| OH\_HUKS\_AE\_TAG\_LEN 16 | 
Length of the AEAD authentication tag, in bytes.

**Since**: 9

 |
| OH\_HUKS\_BITS\_PER\_BYTE 8 | 

Number of bits in each byte.

**Since**: 9

 |
| OH\_HUKS\_MAX\_KEY\_SIZE 2048 | 

Maximum key size, in bytes.

**Since**: 9

 |
| OH\_HUKS\_AE\_NONCE\_LEN 12 | 

Length of the AEAD one-time random number, in bytes.

**Since**: 9

 |
| OH\_HUKS\_MAX\_KEY\_ALIAS\_LEN 64 | 

Maximum length of a key alias, in bytes.

**Since**: 9

 |
| OH\_HUKS\_MAX\_PROCESS\_NAME\_LEN 50 | 

Maximum length of a process name, in bytes.

**Since**: 9

 |
| OH\_HUKS\_MAX\_RANDOM\_LEN 1024 | 

Maximum length of a random number, in bytes.

**Since**: 9

 |
| OH\_HUKS\_SIGNATURE\_MIN\_SIZE 64 | 

Minimum length of the signature result, in bytes.

**Since**: 9

 |
| OH\_HUKS\_MAX\_OUT\_BLOB\_SIZE (5 \* 1024 \* 1024) | 

Maximum size of the exported data, in bytes.

**Since**: 9

 |
| OH\_HUKS\_WRAPPED\_FORMAT\_MAX\_SIZE (1024 \* 1024) | 

Maximum size of the key to be imported, in bytes.

**Since**: 9

 |
| OH\_HUKS\_IMPORT\_WRAPPED\_KEY\_TOTAL\_BLOBS 10 | 

Maximum number of data blocks of the key to be imported, in bytes.

**Since**: 9

 |
| TOKEN\_CHALLENGE\_LEN 32 | 

Byte length of the challenge value during access control.

**Since**: 9

 |
| SHA256\_SIGN\_LEN 32 | 

Byte length of the SHA-256 signature.

**Since**: 9

 |
| TOKEN\_SIZE 32 | 

Byte length of the challenge value during access control.

**Since**: 9

 |
| MAX\_AUTH\_TIMEOUT\_SECOND 60 | 

Maximum user authentication timeout.

**Since**: 9

 |
| SECURE\_SIGN\_VERSION 0x01000001 | 

Version of the secure signature data.

**Since**: 9

 |

#### Enum Description

#### \[h2\]OH\_Huks\_KeyPurpose

enum OH\_Huks\_KeyPurpose

**Description**

Enumerates the key purposes.

**Since**: 9

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_KEY\_PURPOSE\_ENCRYPT = 1 | Used to encrypt the plaintext. |
| OH\_HUKS\_KEY\_PURPOSE\_DECRYPT = 2 | Used to decrypt the cipher text. |
| OH\_HUKS\_KEY\_PURPOSE\_SIGN = 4 | Used for signing. |
| OH\_HUKS\_KEY\_PURPOSE\_VERIFY = 8 | Used to verify the signature. |
| OH\_HUKS\_KEY\_PURPOSE\_DERIVE = 16 | Used to derive a key. |
| OH\_HUKS\_KEY\_PURPOSE\_WRAP = 32 | Used for exporting a key in ciphertext. |
| OH\_HUKS\_KEY\_PURPOSE\_UNWRAP = 64 | Used for importing a key in ciphertext. |
| OH\_HUKS\_KEY\_PURPOSE\_MAC = 128 | Used to generate a message authentication code (MAC). |
| OH\_HUKS\_KEY\_PURPOSE\_AGREE = 256 | Used for key agreement. |

#### \[h2\]OH\_Huks\_KeyDigest

enum OH\_Huks\_KeyDigest

**Description**

Enumerates the digest algorithms.

**Since**: 9

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_DIGEST\_NONE = 0 | No digest algorithm. |
| OH\_HUKS\_DIGEST\_MD5 = 1 | MD5. |
| OH\_HUKS\_DIGEST\_SM3 = 2 | SM3. |
| OH\_HUKS\_DIGEST\_SHA1 = 10 | SHA-1. |
| OH\_HUKS\_DIGEST\_SHA224 = 11 | SHA-224. |
| OH\_HUKS\_DIGEST\_SHA256 = 12 | SHA-256. |
| OH\_HUKS\_DIGEST\_SHA384 = 13 | SHA-384. |
| OH\_HUKS\_DIGEST\_SHA512 = 14 | SHA-512. |

#### \[h2\]OH\_Huks\_KeyPadding

enum OH\_Huks\_KeyPadding

**Description**

Enumerates the padding algorithm types.

**Since**: 9

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_PADDING\_NONE = 0 | No padding algorithm. |
| OH\_HUKS\_PADDING\_OAEP = 1 | OAEP. |
| OH\_HUKS\_PADDING\_PSS = 2 | PSS. |
| OH\_HUKS\_PADDING\_PKCS1\_V1\_5 = 3 | PKCS1\_V1\_5. |
| OH\_HUKS\_PADDING\_PKCS5 = 4 | PKCS #5. |
| OH\_HUKS\_PADDING\_PKCS7 = 5 | PKCS #7. |
| OH\_HUKS\_PADDING\_ISO\_IEC\_9796\_2 = 6 | 
ISO IEC 9796-2.

**Since**: 18

 |
| OH\_HUKS\_PADDING\_ISO\_IEC\_9797\_1 = 7 | 

ISO IEC 9797-1.

**Since**: 18

 |

#### \[h2\]OH\_Huks\_CipherMode

enum OH\_Huks\_CipherMode

**Description**

Cipher mode.

**Since**: 9

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_MODE\_ECB = 1 | ECB. |
| OH\_HUKS\_MODE\_CBC = 2 | CBC. |
| OH\_HUKS\_MODE\_CTR = 3 | CTR. |
| OH\_HUKS\_MODE\_OFB = 4 | OFB. |
| OH\_HUKS\_MODE\_CFB = 5 | 
CFB.

**Since**: 12

 |
| OH\_HUKS\_MODE\_CCM = 31 | CCM. |
| OH\_HUKS\_MODE\_GCM = 32 | GCM. |

#### \[h2\]OH\_Huks\_KeySize

enum OH\_Huks\_KeySize

**Description**

Enumerates the key sizes of different algorithms.

**Since**: 9

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_RSA\_KEY\_SIZE\_512 = 512 | RSA key of 512 bits. |
| OH\_HUKS\_RSA\_KEY\_SIZE\_768 = 768 | RSA key of 768 bits. |
| OH\_HUKS\_RSA\_KEY\_SIZE\_1024 = 1024 | RSA key of 1024 bits. |
| OH\_HUKS\_RSA\_KEY\_SIZE\_2048 = 2048 | RSA key of 2048 bits. |
| OH\_HUKS\_RSA\_KEY\_SIZE\_3072 = 3072 | RSA key of 3072 bits. |
| OH\_HUKS\_RSA\_KEY\_SIZE\_4096 = 4096 | RSA key of 4096 bits. |
| OH\_HUKS\_ECC\_KEY\_SIZE\_224 = 224 | ECC key of 224 bits. |
| OH\_HUKS\_ECC\_KEY\_SIZE\_256 = 256 | ECC key of 256 bits. |
| OH\_HUKS\_ECC\_KEY\_SIZE\_384 = 384 | ECC key of 384 bits. |
| OH\_HUKS\_ECC\_KEY\_SIZE\_521 = 521 | ECC key of 521 bits. |
| OH\_HUKS\_AES\_KEY\_SIZE\_128 = 128 | AES key of 128 bits. |
| OH\_HUKS\_AES\_KEY\_SIZE\_192 = 192 | AES key of 192 bits. |
| OH\_HUKS\_AES\_KEY\_SIZE\_256 = 256 | AES key of 256 bits. |
| OH\_HUKS\_AES\_KEY\_SIZE\_512 = 512 | AES key of 512 bits. |
| OH\_HUKS\_CURVE25519\_KEY\_SIZE\_256 = 256 | Curve25519 key of 256 bits. |
| OH\_HUKS\_DH\_KEY\_SIZE\_2048 = 2048 | DH key of 2048 bits. |
| OH\_HUKS\_DH\_KEY\_SIZE\_3072 = 3072 | DH key of 3072 bits. |
| OH\_HUKS\_DH\_KEY\_SIZE\_4096 = 4096 | DH key of 4096 bits. |
| OH\_HUKS\_SM2\_KEY\_SIZE\_256 = 256 | SM2 key of 256 bits. |
| OH\_HUKS\_SM4\_KEY\_SIZE\_128 = 128 | SM4 key of 128 bits. |
| OH\_HUKS\_DES\_KEY\_SIZE\_64 = 64 | 
DES key of 64 bits.

**Since**: 18

 |
| OH\_HUKS\_3DES\_KEY\_SIZE\_128 = 128 | 

3DES key of 128 bits.

**Since**: 18

 |
| OH\_HUKS\_3DES\_KEY\_SIZE\_192 = 192 | 

3DES key of 192 bits.

**Since**: 18

 |

#### \[h2\]OH\_Huks\_KeyAlg

enum OH\_Huks\_KeyAlg

**Description**

Enumerates the algorithms for keys.

**Since**: 9

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_ALG\_RSA = 1 | RSA. |
| OH\_HUKS\_ALG\_ECC = 2 | ECC. |
| OH\_HUKS\_ALG\_DSA = 3 | DSA. |
| OH\_HUKS\_ALG\_AES = 20 | Advanced Encryption Standard (AES). |
| OH\_HUKS\_ALG\_HMAC = 50 | HMAC algorithm. |
| OH\_HUKS\_ALG\_HKDF = 51 | HKDF. |
| OH\_HUKS\_ALG\_PBKDF2 = 52 | PBKDF2. |
| OH\_HUKS\_ALG\_ECDH = 100 | ECDH. |
| OH\_HUKS\_ALG\_X25519 = 101 | X25519. |
| OH\_HUKS\_ALG\_ED25519 = 102 | Ed25519. |
| OH\_HUKS\_ALG\_DH = 103 | DH. |
| OH\_HUKS\_ALG\_SM2 = 150 | ShangMi2 (SM2). |
| OH\_HUKS\_ALG\_SM3 = 151 | SM3. |
| OH\_HUKS\_ALG\_SM4 = 152 | SM4. |
| OH\_HUKS\_ALG\_DES = 160 | 
DES.

**Since**: 18

 |
| OH\_HUKS\_ALG\_3DES = 161 | 

3DES.

**Since**: 18

 |
| OH\_HUKS\_ALG\_CMAC = 162 | 

CMAC.

**Since**: 18

 |

#### \[h2\]OH\_Huks\_AlgSuite

enum OH\_Huks\_AlgSuite

**Description**

Enumerates the algorithm suites that can be used for importing of a key in ciphertext.

Key material format for **OH\_HUKS\_UNWRAP\_SUITE\_X25519\_AES\_256\_GCM\_NOPADDING**:

| x25519\_plain\_pubkey\_length  (4 Byte) | x25519\_plain\_pubkey |  agreekey\_aad\_length (4 Byte) | agreekey\_aad
|   agreekey\_nonce\_length     (4 Byte) |   agreekey\_nonce    | agreekey\_aead\_tag\_len(4 Byte) | agreekey\_aead\_tag
|    kek\_enc\_data\_length      (4 Byte) |    kek\_enc\_data     |    kek\_aad\_length    (4 Byte) | kek\_aad
|      kek\_nonce\_length       (4 Byte) |      kek\_nonce      |   kek\_aead\_tag\_len   (4 Byte) | kek\_aead\_tag
|   key\_material\_size\_len     (4 Byte) |  key\_material\_size  |   key\_mat\_enc\_length (4 Byte) | key\_mat\_enc\_data

Key material format for **OH\_HUKS\_UNWRAP\_SUITE\_ECDH\_AES\_256\_GCM\_NOPADDING**:

|  ECC\_plain\_pubkey\_length    (4 Byte) |  ECC\_plain\_pubkey   |  agreekey\_aad\_length (4 Byte) | agreekey\_aad
|   agreekey\_nonce\_length     (4 Byte) |   agreekey\_nonce    | agreekey\_aead\_tag\_len(4 Byte) | agreekey\_aead\_tag
|    kek\_enc\_data\_length      (4 Byte) |    kek\_enc\_data     |    kek\_aad\_length    (4 Byte) | kek\_aad
|      kek\_nonce\_length       (4 Byte) |      kek\_nonce      |   kek\_aead\_tag\_len   (4 Byte) | kek\_aead\_tag
|   key\_material\_size\_len     (4 Byte) |  key\_material\_size  |   key\_mat\_enc\_length (4 Byte) | key\_mat\_enc\_data

**Since**: 9

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_UNWRAP\_SUITE\_X25519\_AES\_256\_GCM\_NOPADDING = 1 | Key material in Length-Value format, using X25519 for key agreement and AES-256-GCM for encryption and decryption. For details about the material format, see the preceding description. |
| OH\_HUKS\_UNWRAP\_SUITE\_ECDH\_AES\_256\_GCM\_NOPADDING = 2 | Key material in Length-Value format, using ECDH-p256 for key agreement and AES-256-GCM for encryption and decryption. For details about the material format, see the preceding description. |

#### \[h2\]OH\_Huks\_KeyGenerateType

enum OH\_Huks\_KeyGenerateType

**Description**

Enumerates the types of the key generated.

**Since**: 9

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_KEY\_GENERATE\_TYPE\_DEFAULT = 0 | Key generated by default. |
| OH\_HUKS\_KEY\_GENERATE\_TYPE\_DERIVE = 1 | Derived key. |
| OH\_HUKS\_KEY\_GENERATE\_TYPE\_AGREE = 2 | Key generated by key agreement. |

#### \[h2\]OH\_Huks\_KeyFlag

enum OH\_Huks\_KeyFlag

**Description**

Enumerates the key generation types.

**Since**: 9

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_KEY\_FLAG\_IMPORT\_KEY = 1 | Import a public key using a function. |
| OH\_HUKS\_KEY\_FLAG\_GENERATE\_KEY = 2 | Generate a key by using a function. |
| OH\_HUKS\_KEY\_FLAG\_AGREE\_KEY = 3 | Generate a key by using a key agreement function. |
| OH\_HUKS\_KEY\_FLAG\_DERIVE\_KEY = 4 | Derive a key by using a function. |

#### \[h2\]OH\_Huks\_KeyStorageType

enum OH\_Huks\_KeyStorageType

**Description**

Enumerates the key storage types.

**Since**: 9

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_STORAGE\_TEMP = 0 | Return the key to the service via the API. |
| OH\_HUKS\_STORAGE\_PERSISTENT = 1 | Store the key in HUKS. |
| OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS = 2 | Store the key generated from key derivation or key agreement in HUKS. |
| OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED = 3 | Return the key generated from key derivation or key agreement to the service. |

#### \[h2\]OH\_Huks\_ImportKeyType

enum OH\_Huks\_ImportKeyType

**Description**

Enumerates the types of the key to import. By default, a public key is imported. This field is not required when a symmetric key is imported.

**Since**: 9

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_KEY\_TYPE\_PUBLIC\_KEY = 0 | Public key. |
| OH\_HUKS\_KEY\_TYPE\_PRIVATE\_KEY = 1 | Private key. |
| OH\_HUKS\_KEY\_TYPE\_KEY\_PAIR = 2 | Public and private key pair. |

#### \[h2\]OH\_Huks\_RsaPssSaltLenType

enum OH\_Huks\_RsaPssSaltLenType

**Description**

Enumerates the length types of the salt value in PSS padding mode.

**Since**: 10

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_RSA\_PSS\_SALT\_LEN\_DIGEST = 0 | The salt length is set to the digest length. |
| OH\_HUKS\_RSA\_PSS\_SALT\_LEN\_MAX = 1 | The salt length is set to the maximum length. |

#### \[h2\]OH\_Huks\_ErrCode

enum OH\_Huks\_ErrCode

**Description**

Enumerates error codes.

**Since**: 9

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_SUCCESS = 0 | Success. |
| OH\_HUKS\_ERR\_CODE\_PERMISSION\_FAIL = 201 | Permission verification failed. |
| OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401 | Invalid parameter (universal). |
| OH\_HUKS\_ERR\_CODE\_NOT\_SUPPORTED\_API = 801 | The API is not supported. |
| OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001 | The feature is not supported. |
| OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002 | Key algorithm parameters are missing. |
| OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003 | Invalid key algorithm parameter. |
| OH\_HUKS\_ERR\_CODE\_FILE\_OPERATION\_FAIL = 12000004 | File operation failed. |
| OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005 | The process communication failed. |
| OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL = 12000006 | Crypto operation failed. |
| OH\_HUKS\_ERR\_CODE\_KEY\_AUTH\_PERMANENTLY\_INVALIDATED = 12000007 | Failed to access the key because the key has expired. |
| OH\_HUKS\_ERR\_CODE\_KEY\_AUTH\_VERIFY\_FAILED = 12000008 | Failed to access the key because the authentication has failed. |
| OH\_HUKS\_ERR\_CODE\_KEY\_AUTH\_TIME\_OUT = 12000009 | Key access timed out. |
| OH\_HUKS\_ERR\_CODE\_SESSION\_LIMIT = 12000010 | The number of key operation sessions has reached the limit. |
| OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011 | The entity does not exist. |
| OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012 | Internal error. |
| OH\_HUKS\_ERR\_CODE\_CREDENTIAL\_NOT\_EXIST = 12000013 | The authentication credential does not exist. |
| OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014 | Insufficient memory. |
| OH\_HUKS\_ERR\_CODE\_CALL\_SERVICE\_FAILED = 12000015 | Failed to invoke the service. |
| OH\_HUKS\_ERR\_CODE\_DEVICE\_PASSWORD\_UNSET = 12000016 | 
The lock screen password required is not set.

**Since**: 11

 |
| OH\_HUKS\_ERR\_CODE\_KEY\_ALREADY\_EXIST = 12000017 | 

A key with the same name already exists.

**Since**: 20

 |
| OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018 | 

An input parameter is invalid.

**Since**: 20

 |
| OH\_HUKS\_ERR\_CODE\_ITEM\_EXISTS = 12000019 | 

The entity already exists.

**Since**: 22

 |
| OH\_HUKS\_ERR\_CODE\_EXTERNAL\_MODULE = 12000020 | 

The provider or Ukey internal execution fails.

**Since**: 22

 |
| OH\_HUKS\_ERR\_CODE\_PIN\_LOCKED = 12000021 | 

The PIN is locked.

**Since**: 22

 |
| OH\_HUKS\_ERR\_CODE\_PIN\_INCORRECT = 12000022 | 

Incorrect PIN.

**Since**: 22

 |
| OH\_HUKS\_ERR\_CODE\_PIN\_NO\_AUTH = 12000023 | 

The PIN does not pass authentication.

**Since**: 22

 |
| OH\_HUKS\_ERR\_CODE\_BUSY = 12000024 | 

The provider or Ukey resources are being used.

**Since**: 22

 |
| OH\_HUKS\_ERR\_CODE\_EXCEED\_LIMIT = 12000025 | 

The resource limit is exceeded.

**Since**: 22

 |

#### \[h2\]OH\_Huks\_TagType

enum OH\_Huks\_TagType

**Description**

Enumerates the types of the parameters in a parameter set.

**Since**: 9

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_TAG\_TYPE\_INVALID = 0 << 28 | Invalid tag type. |
| OH\_HUKS\_TAG\_TYPE\_INT = 1 << 28 | int32\_t. |
| OH\_HUKS\_TAG\_TYPE\_UINT = 2 << 28 | uin32\_t. |
| OH\_HUKS\_TAG\_TYPE\_ULONG = 3 << 28 | uin64\_t. |
| OH\_HUKS\_TAG\_TYPE\_BOOL = 4 << 28 | Boolean. |
| OH\_HUKS\_TAG\_TYPE\_BYTES = 5 << 28 | [OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md). |

**Reference:**

[OH\_Huks\_Param](../../structs/oh-huks-param/document.md)

#### \[h2\]OH\_Huks\_UserAuthType

enum OH\_Huks\_UserAuthType

**Description**

Enumerates the user authentication types in key access control.

**Since**: 9

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_USER\_AUTH\_TYPE\_FINGERPRINT = 1 << 0 | Fingerprint authentication. |
| OH\_HUKS\_USER\_AUTH\_TYPE\_FACE = 1 << 1 | Facial authentication. |
| OH\_HUKS\_USER\_AUTH\_TYPE\_PIN = 1 << 2 | PIN authentication. |
| OH\_HUKS\_USER\_AUTH\_TYPE\_TUI\_PIN = 1 << 5 | 
TUI PIN authentication.

**Since**: 20

 |

#### \[h2\]OH\_Huks\_AuthAccessType

enum OH\_Huks\_AuthAccessType

**Description**

Enumerates the rules for invalidating a key.

**Since**: 9

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_AUTH\_ACCESS\_INVALID\_CLEAR\_PASSWORD = 1 << 0 | The key becomes invalid after the password is cleared. |
| OH\_HUKS\_AUTH\_ACCESS\_INVALID\_NEW\_BIO\_ENROLL = 1 << 1 | The key becomes invalid after a new biometric feature is enrolled. |
| OH\_HUKS\_AUTH\_ACCESS\_ALWAYS\_VALID = 1 << 2 | 
The key is always valid.

**Since**: 11

 |

#### \[h2\]OH\_Huks\_AuthStorageLevel

enum OH\_Huks\_AuthStorageLevel

**Description**

Enumerates the security levels for storing the key generated or imported.

**Since**: 11

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_AUTH\_STORAGE\_LEVEL\_DE = 0 | The key can be accessed only after the device is started. |
| OH\_HUKS\_AUTH\_STORAGE\_LEVEL\_CE = 1 | The key can be accessed only after the first unlock of the device. |
| OH\_HUKS\_AUTH\_STORAGE\_LEVEL\_ECE = 2 | The key can be accessed only when the device is unlocked. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/ebbteB4nR5O7s4ChwwSLWw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062339Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=15843B7B3E931DA2158960B4FC627D39C731D6A1C812716921E186BF3F8CE143)

When using a key whose storage level is ECE, you are advised to clear the session resources created using the key by detecting the [lock screen event](../../../../../basic-functions/basic-services-kit/arkts-apis/process-and-thread-communication/system-common-events/document.md#common_event_screen_locked) to ensure security.

#### \[h2\]OH\_Huks\_ChallengeType

enum OH\_Huks\_ChallengeType

**Description**

Enumerates the types of the challenge generated when a key is used.

**Since**: 9

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_CHALLENGE\_TYPE\_NORMAL = 0 | Normal challenge, which is of 32 bytes by default. |
| OH\_HUKS\_CHALLENGE\_TYPE\_CUSTOM = 1 | Custom challenge, which supports one-time authentication for multiple keys. The valid value of a custom challenge is of 8 bytes. |
| OH\_HUKS\_CHALLENGE\_TYPE\_NONE = 2 | Challenge is not required. |

**Reference:**

[OH\_Huks\_ChallengePosition](#oh_huks_challengeposition)

#### \[h2\]OH\_Huks\_UserAuthMode

enum OH\_Huks\_UserAuthMode

**Description**

Enumerates the user authentication modes in key access control.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_USER\_AUTH\_MODE\_LOCAL = 0 | Local authentication. |
| OH\_HUKS\_USER\_AUTH\_MODE\_COAUTH = 1 | Cross-device collaborative authentication. |

#### \[h2\]OH\_Huks\_ChallengePosition

enum OH\_Huks\_ChallengePosition

**Description**

Enumerates the positions of the 8-byte valid value in a custom challenge generated.

**Since**: 9

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_CHALLENGE\_POS\_0 = 0 | Bytes 0 to 7. |
| OH\_HUKS\_CHALLENGE\_POS\_1 | Bytes 8 to 15. |
| OH\_HUKS\_CHALLENGE\_POS\_2 | Bytes 16 to 23. |
| OH\_HUKS\_CHALLENGE\_POS\_3 | Bytes 24 to 31. |

#### \[h2\]OH\_Huks\_SecureSignType

enum OH\_Huks\_SecureSignType

**Description**

Enumerates the signature types of the key generated or imported.

**Since**: 9

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_SECURE\_SIGN\_WITH\_AUTHINFO = 1 | The signature carries authentication information. This field is specified when a key is generated or imported. When the key is used for signing, the data will be added with the authentication information and then be signed. Note: The carried authentication information includes identity information. You need to describe the purpose, retention policy, and destruction method of the identity information in the privacy statement. |

#### \[h2\]OH\_Huks\_KeyClassType

enum OH\_Huks\_KeyClassType

**Description**

Key type.

**Since**: 22

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_KEY\_CLASS\_DEFAULT = 0 | Default type. The key is stored in HUKS. |
| OH\_HUKS\_KEY\_CLASS\_EXTENSION = 1 | The key is stored in the external encryption provider. |

#### \[h2\]OH\_Huks\_KeyWrapType

enum OH\_Huks\_KeyWrapType

**Description**

Enumerates the wrap type of the key generated or imported.

**Since**: 20

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_KEY\_WRAP\_TYPE\_HUK\_BASED = 2 | Wrap type of the unique hardware key. |

#### \[h2\]OH\_Huks\_Tag

enum OH\_Huks\_Tag

**Description**

Enumerates the tags contained in a parameter set.

1 to 200: key parameter tag values.

301 to 500: tag values related to access control and authentication of key usage.

501 to 600: tag values related to key authentication.

601 to 1000: reserved values for other types of tag values.

1001 to 9999: extended tag values.

11000 to 12000: reserved values.

20001 to N: reserved tag values.

**Since**: 9

| Enum | Description |
| :-- | :-- |
| OH\_HUKS\_TAG\_ALGORITHM = OH\_HUKS\_TAG\_TYPE\_UINT | 1 | Algorithm type. |
| OH\_HUKS\_TAG\_PURPOSE = OH\_HUKS\_TAG\_TYPE\_UINT | 2 | Key purpose. |
| OH\_HUKS\_TAG\_KEY\_SIZE = OH\_HUKS\_TAG\_TYPE\_UINT | 3 | Key length. |
| OH\_HUKS\_TAG\_DIGEST = OH\_HUKS\_TAG\_TYPE\_UINT | 4 | Digest algorithm. |
| OH\_HUKS\_TAG\_PADDING = OH\_HUKS\_TAG\_TYPE\_UINT | 5 | Padding algorithm. |
| OH\_HUKS\_TAG\_BLOCK\_MODE = OH\_HUKS\_TAG\_TYPE\_UINT | 6 | Cipher mode. |
| OH\_HUKS\_TAG\_KEY\_TYPE = OH\_HUKS\_TAG\_TYPE\_UINT | 7 | Key type. |
| OH\_HUKS\_TAG\_ASSOCIATED\_DATA = OH\_HUKS\_TAG\_TYPE\_BYTES | 8 | Associated authentication data. |
| OH\_HUKS\_TAG\_NONCE = OH\_HUKS\_TAG\_TYPE\_BYTES | 9 | **NONCE** field for key encryption and decryption. |
| OH\_HUKS\_TAG\_IV = OH\_HUKS\_TAG\_TYPE\_BYTES | 10 | Initialized vector (IV). |
| OH\_HUKS\_TAG\_INFO = OH\_HUKS\_TAG\_TYPE\_BYTES | 11 | Information generated during key derivation. |
| OH\_HUKS\_TAG\_SALT = OH\_HUKS\_TAG\_TYPE\_BYTES | 12 | Salt value used for key derivation. |
| OH\_HUKS\_TAG\_ITERATION = OH\_HUKS\_TAG\_TYPE\_UINT | 14 | Number of iterations for key derivation. |
| OH\_HUKS\_TAG\_KEY\_GENERATE\_TYPE = OH\_HUKS\_TAG\_TYPE\_UINT | 15 | Type of the generated key. For details, see [OH\_Huks\_KeyGenerateType](#oh_huks_keygeneratetype). |
| OH\_HUKS\_TAG\_AGREE\_ALG = OH\_HUKS\_TAG\_TYPE\_UINT | 19 | Algorithm used in key agreement. |
| OH\_HUKS\_TAG\_AGREE\_PUBLIC\_KEY\_IS\_KEY\_ALIAS = OH\_HUKS\_TAG\_TYPE\_BOOL | 20 | Alias of the public key used for key agreement. |
| OH\_HUKS\_TAG\_AGREE\_PRIVATE\_KEY\_ALIAS = OH\_HUKS\_TAG\_TYPE\_BYTES | 21 | Alias of the private key used for key agreement. |
| OH\_HUKS\_TAG\_AGREE\_PUBLIC\_KEY = OH\_HUKS\_TAG\_TYPE\_BYTES | 22 | Public key used for key agreement. |
| OH\_HUKS\_TAG\_KEY\_ALIAS = OH\_HUKS\_TAG\_TYPE\_BYTES | 23 | Key alias. |
| OH\_HUKS\_TAG\_DERIVE\_KEY\_SIZE = OH\_HUKS\_TAG\_TYPE\_UINT | 24 | Size of the derived key. |
| OH\_HUKS\_TAG\_IMPORT\_KEY\_TYPE = OH\_HUKS\_TAG\_TYPE\_UINT | 25 | Type of the key to import. For details, see [OH\_Huks\_ImportKeyType](#oh_huks_importkeytype). |
| OH\_HUKS\_TAG\_UNWRAP\_ALGORITHM\_SUITE = OH\_HUKS\_TAG\_TYPE\_UINT | 26 | Algorithm suite used for importing a key in ciphertext. |
| OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG = OH\_HUKS\_TAG\_TYPE\_UINT | 29 | Storage type of the derived key or key produced after key agreement. It is a value of [OH\_Huks\_KeyStorageType](#oh_huks_keystoragetype). |
| OH\_HUKS\_TAG\_RSA\_PSS\_SALT\_LEN\_TYPE = OH\_HUKS\_TAG\_TYPE\_UINT | 30 | Salt length type when the PSS padding mode is used with the RSA algorithm. |
| OH\_HUKS\_TAG\_ALL\_USERS = OH\_HUKS\_TAG\_TYPE\_BOOL | 301 | All users in the multi-user scenario. |
| OH\_HUKS\_TAG\_USER\_ID = OH\_HUKS\_TAG\_TYPE\_UINT | 302 | Multi-user ID. |
| OH\_HUKS\_TAG\_NO\_AUTH\_REQUIRED = OH\_HUKS\_TAG\_TYPE\_BOOL | 303 | Whether key access control is required. |
| OH\_HUKS\_TAG\_USER\_AUTH\_TYPE = OH\_HUKS\_TAG\_TYPE\_UINT | 304 | User authentication type in key access control. |
| OH\_HUKS\_TAG\_AUTH\_TIMEOUT = OH\_HUKS\_TAG\_TYPE\_UINT | 305 | Timeout duration for key access. |
| OH\_HUKS\_TAG\_AUTH\_TOKEN = OH\_HUKS\_TAG\_TYPE\_BYTES | 306 | Authentication token for the key. |
| OH\_HUKS\_TAG\_KEY\_AUTH\_ACCESS\_TYPE = OH\_HUKS\_TAG\_TYPE\_UINT | 307 | Key access control type, which must be set together with the user authentication type. It is a value of [OH\_Huks\_AuthAccessType](#oh_huks_authaccesstype). |
| OH\_HUKS\_TAG\_KEY\_SECURE\_SIGN\_TYPE = OH\_HUKS\_TAG\_TYPE\_UINT | 308 | Signature type of the key generated or imported. |
| OH\_HUKS\_TAG\_CHALLENGE\_TYPE = OH\_HUKS\_TAG\_TYPE\_UINT | 309 | Challenge type, which is a value of [OH\_Huks\_ChallengeType](#oh_huks_challengetype). |
| OH\_HUKS\_TAG\_CHALLENGE\_POS = OH\_HUKS\_TAG\_TYPE\_UINT | 310 | Position of the 8-byte valid value in a custom challenge. For details, see [OH\_Huks\_ChallengePosition](#oh_huks_challengeposition). |
| OH\_HUKS\_TAG\_KEY\_AUTH\_PURPOSE = OH\_HUKS\_TAG\_TYPE\_UINT | 311 | Type of the key authentication purpose. |
| OH\_HUKS\_TAG\_AUTH\_STORAGE\_LEVEL = OH\_HUKS\_TAG\_TYPE\_UINT | 316 | 
Security levels for storing the key. For details, see [OH\_Huks\_AuthStorageLevel](#oh_huks_authstoragelevel).

**Since**: 11

 |
| OH\_HUKS\_TAG\_USER\_AUTH\_MODE = OH\_HUKS\_TAG\_TYPE\_UINT | 319 | 

User authentication mode in key access control. For details, see [OH\_Huks\_UserAuthMode](#oh_huks_userauthmode).

**Since**: 12

 |
| OH\_HUKS\_TAG\_ATTESTATION\_CHALLENGE = OH\_HUKS\_TAG\_TYPE\_BYTES | 501 | Challenge value used in the attestation. |
| OH\_HUKS\_TAG\_ATTESTATION\_APPLICATION\_ID = OH\_HUKS\_TAG\_TYPE\_BYTES | 502 | ID of the application, to which the key belongs, in key attestation. |
| OH\_HUKS\_TAG\_ATTESTATION\_ID\_ALIAS = OH\_HUKS\_TAG\_TYPE\_BYTES | 511 | Alias used in key attestation. |
| OH\_HUKS\_TAG\_ATTESTATION\_ID\_SEC\_LEVEL\_INFO = OH\_HUKS\_TAG\_TYPE\_BYTES | 514 | Security level used in key attestation. |
| OH\_HUKS\_TAG\_ATTESTATION\_ID\_VERSION\_INFO = OH\_HUKS\_TAG\_TYPE\_BYTES | 515 | Version information used in key attestation. |
| OH\_HUKS\_TAG\_KEY\_OVERRIDE = OH\_HUKS\_TAG\_TYPE\_BOOL | 520 | 

Whether to overwrite the key with the same name.

**Since**: 20

 |
| OH\_HUKS\_TAG\_AE\_TAG\_LEN = OH\_HUKS\_TAG\_TYPE\_UINT | 521 | 

**AEAD** length in CCM mode.

**Since**: 22

 |
| OH\_HUKS\_TAG\_KEY\_CLASS = OH\_HUKS\_TAG\_TYPE\_UINT | 522 | 

Key type, which is used to distinguish the key managed by HUKS on the device from the key stored in an external device.

**Since**: 22

 |
| OH\_HUKS\_TAG\_IS\_KEY\_ALIAS = OH\_HUKS\_TAG\_TYPE\_BOOL | 1001 | Whether it is a key alias. |
| OH\_HUKS\_TAG\_KEY\_STORAGE\_FLAG = OH\_HUKS\_TAG\_TYPE\_UINT | 1002 | Key storage mode. For details, see [OH\_Huks\_KeyStorageType](#oh_huks_keystoragetype). |
| OH\_HUKS\_TAG\_IS\_ALLOWED\_WRAP = OH\_HUKS\_TAG\_TYPE\_BOOL | 1003 | Whether to allow the key to be wrapped. |
| OH\_HUKS\_TAG\_KEY\_WRAP\_TYPE = OH\_HUKS\_TAG\_TYPE\_UINT | 1004 | Key wrap type. |
| OH\_HUKS\_TAG\_KEY\_AUTH\_ID = OH\_HUKS\_TAG\_TYPE\_BYTES | 1005 | Authentication ID. |
| OH\_HUKS\_TAG\_KEY\_ROLE = OH\_HUKS\_TAG\_TYPE\_UINT | 1006 | Role of the key. |
| OH\_HUKS\_TAG\_KEY\_FLAG = OH\_HUKS\_TAG\_TYPE\_UINT | 1007 | Key flag. For details, see [OH\_Huks\_KeyFlag](#oh_huks_keyflag). |
| OH\_HUKS\_TAG\_IS\_ASYNCHRONIZED = OH\_HUKS\_TAG\_TYPE\_UINT | 1008 | Whether the invocation is asynchronous. |
| OH\_HUKS\_TAG\_KEY\_DOMAIN = OH\_HUKS\_TAG\_TYPE\_UINT | 1011 | Key domain. |
| OH\_HUKS\_TAG\_IS\_DEVICE\_PASSWORD\_SET = OH\_HUKS\_TAG\_TYPE\_BOOL | 1012 | 

Whether the key is accessible only when the user sets a lock screen password.

**True** indicates that the key can be generated and used only when a password is set.

**Since**: 11

 |
| OH\_HUKS\_TAG\_AE\_TAG = OH\_HUKS\_TAG\_TYPE\_BYTES | 10009 | AEAD in GCM mode. |
| OH\_HUKS\_TAG\_SYMMETRIC\_KEY\_DATA = OH\_HUKS\_TAG\_TYPE\_BYTES | 20001 | Symmetric key data. |
| OH\_HUKS\_TAG\_ASYMMETRIC\_PUBLIC\_KEY\_DATA = OH\_HUKS\_TAG\_TYPE\_BYTES | 20002 | Public key data of the asymmetric key pair. |
| OH\_HUKS\_TAG\_ASYMMETRIC\_PRIVATE\_KEY\_DATA = OH\_HUKS\_TAG\_TYPE\_BYTES | 20003 | Private key data of the asymmetric key pair. |
