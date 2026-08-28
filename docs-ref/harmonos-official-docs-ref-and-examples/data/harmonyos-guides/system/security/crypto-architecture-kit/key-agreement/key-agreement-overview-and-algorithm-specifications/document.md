# Key Agreement Overview and Algorithm Specifications

Key agreement allows two or more parties to jointly establish a shared key in a non-secure environment.

This topic describes the key agreement algorithms and specifications supported by the system.

#### ECDH

The Crypto framework provides a variety of Elliptic Curve Diffie–Hellman key exchange (ECDH) capabilities.

When creating a key agreement instance, you need to specify the algorithm specifications in a string parameter, as listed in the table below.

| Asymmetric Key Algorithm | String Parameter | API Version |
| :-- | :-- | :-- |
| ECC | ECC224 | 9+ |
| ECC | ECC256 | 9+ |
| ECC | ECC384 | 9+ |
| ECC | ECC521 | 9+ |
| ECC | ECC\_BrainPoolP160r1 | 11+ |
| ECC | ECC\_BrainPoolP160t1 | 11+ |
| ECC | ECC\_BrainPoolP192r1 | 11+ |
| ECC | ECC\_BrainPoolP192t1 | 11+ |
| ECC | ECC\_BrainPoolP224r1 | 11+ |
| ECC | ECC\_BrainPoolP224t1 | 11+ |
| ECC | ECC\_BrainPoolP256r1 | 11+ |
| ECC | ECC\_BrainPoolP256t1 | 11+ |
| ECC | ECC\_BrainPoolP320r1 | 11+ |
| ECC | ECC\_BrainPoolP320t1 | 11+ |
| ECC | ECC\_BrainPoolP384r1 | 11+ |
| ECC | ECC\_BrainPoolP384t1 | 11+ |
| ECC | ECC\_BrainPoolP512r1 | 11+ |
| ECC | ECC\_BrainPoolP512t1 | 11+ |
| ECC | ECC\_Secp256k1 | 14+ |
| ECC | ECC | 10+ |

As indicated by the last row in the preceding table, you can specify the ECDH key type without the key length and curve name to ensure compatibility with the key generated based on the key parameter. In this case, the key agreement operation varies depending on the actual key length.

#### X25519

The crypto framework provides X25519 key agreement capabilities.

When creating a key agreement instance, you need to specify the algorithm specifications in a string parameter, as listed in the table below.

| Asymmetric Key Algorithm | String Parameter | API Version |
| :-- | :-- | :-- |
| X25519 | X25519 | 11+ |

#### DH

The Crypto framework provides Diffie–Hellman key exchange (DH) key agreement capabilities.

When creating a key agreement instance, you need to specify the algorithm specifications in a string parameter, as listed in the table below.

| Asymmetric Key Algorithm | String Parameter | API Version |
| :-- | :-- | :-- |
| DH | DH\_modp1536 | 11+ |
| DH | DH\_modp2048 | 11+ |
| DH | DH\_modp3072 | 11+ |
| DH | DH\_modp4096 | 11+ |
| DH | DH\_modp6144 | 11+ |
| DH | DH\_modp8192 | 11+ |
| DH | DH\_ffdhe2048 | 11+ |
| DH | DH\_ffdhe3072 | 11+ |
| DH | DH\_ffdhe4096 | 11+ |
| DH | DH\_ffdhe6144 | 11+ |
| DH | DH\_ffdhe8192 | 11+ |
| DH | DH | 11+ |

As indicated by the last row in the preceding table, you can specify the DH key type without the named DH group to ensure compatibility with the key generated based on the key parameter. In this case, the key agreement result is determined by the key passed in. In addition, unnamed DH groups are supported.
