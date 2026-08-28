# Key Derivation Using Scrypt (C/C++)

For details about the corresponding algorithm specifications, see [Scrypt](../key-derivation-overview-and-algorithm-specifications/document.md#scrypt).

#### How to Develop

1.  Call [OH\_CryptoKdfParams\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdfparams_create) and specify the string parameter **SCRYPT** to create a key derivation parameter object.
    
2.  Call [OH\_CryptoKdfParams\_SetParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdfparams_setparam) to set the parameters required by SCRYPT.
    

When a key derivation failure occurs, check whether the following parameters are set:

-   **CRYPTO\_KDF\_KEY\_DATABLOB**: original password used to generate the derived key.
-   **CRYPTO\_KDF\_SALT\_DATABLOB**: salt value.
-   **CRYPTO\_KDF\_SCRYPT\_N\_UINT64**: CPU/memory overhead, which must be a power of 2.
-   **CRYPTO\_KDF\_SCRYPT\_R\_UINT64**: block size, which affects the degree of parallelism.
-   **CRYPTO\_KDF\_SCRYPT\_P\_UINT64**: parallelization.
-   **CRYPTO\_KDF\_SCRYPT\_MAX\_MEM\_UINT64**: maximum memory limit (bytes).

1.  Call [OH\_CryptoKdf\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdf_create) and specify the string parameter **SCRYPT** to create a key derivation function object.
    
2.  Call [OH\_CryptoKdf\_Derive](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdf_derive) and specify the byte length of the target key.
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include "CryptoArchitectureKit/crypto\_kdf.h"
#include <stdio.h>
#include <cstring>

static OH\_Crypto\_ErrCode doTestScrypt()
{
    // Create a SCRYPT parameter object.
    OH\_CryptoKdfParams \*params = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoKdfParams\_Create("SCRYPT", &params);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // Set the password.
    const char \*password = "123456";
    Crypto\_DataBlob passwordBlob = {
        .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(password)),
        .len = strlen(password)
    };
    ret = OH\_CryptoKdfParams\_SetParam(params, CRYPTO\_KDF\_KEY\_DATABLOB, &passwordBlob);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKdfParams\_Destroy(params);
        return ret;
    }

    // Set the salt value.
    const char \*salt = "saltstring";
    Crypto\_DataBlob saltBlob = {
        .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(salt)),
        .len = strlen(salt)
    };
    ret = OH\_CryptoKdfParams\_SetParam(params, CRYPTO\_KDF\_SALT\_DATABLOB, &saltBlob);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKdfParams\_Destroy(params);
        return ret;
    }

    // Set SCRYPT parameters.
    uint64\_t n = 1024; // CPU/memory overhead.
    uint64\_t r = 8; // Block size.
    uint64\_t p = 16; // Parallelization.
    uint64\_t maxMem = 1067008; // Maximum memory limit (bytes).

    Crypto\_DataBlob nData = {
        .data = reinterpret\_cast<uint8\_t \*>(&n),
        .len = sizeof(uint64\_t)
    };
    Crypto\_DataBlob rData = {
        .data = reinterpret\_cast<uint8\_t \*>(&r),
        .len = sizeof(uint64\_t)
    };
    Crypto\_DataBlob pData = {
        .data = reinterpret\_cast<uint8\_t \*>(&p),
        .len = sizeof(uint64\_t)
    };
    Crypto\_DataBlob maxMemData = {
        .data = reinterpret\_cast<uint8\_t \*>(&maxMem),
        .len = sizeof(uint64\_t)
    };

    ret = OH\_CryptoKdfParams\_SetParam(params, CRYPTO\_KDF\_SCRYPT\_N\_UINT64, &nData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKdfParams\_Destroy(params);
        return ret;
    }
    ret = OH\_CryptoKdfParams\_SetParam(params, CRYPTO\_KDF\_SCRYPT\_R\_UINT64, &rData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKdfParams\_Destroy(params);
        return ret;
    }
    ret = OH\_CryptoKdfParams\_SetParam(params, CRYPTO\_KDF\_SCRYPT\_P\_UINT64, &pData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKdfParams\_Destroy(params);
        return ret;
    }
    ret = OH\_CryptoKdfParams\_SetParam(params, CRYPTO\_KDF\_SCRYPT\_MAX\_MEM\_UINT64, &maxMemData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKdfParams\_Destroy(params);
        return ret;
    }

    // Create a key derivation function object.
    OH\_CryptoKdf \*kdfCtx = nullptr;
    ret = OH\_CryptoKdf\_Create("SCRYPT", &kdfCtx);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKdfParams\_Destroy(params);
        return ret;
    }

    // Derive a key.
    Crypto\_DataBlob out = {0};
    uint32\_t keyLength = 32; // Generate a 32-byte key.
    ret = OH\_CryptoKdf\_Derive(kdfCtx, params, keyLength, &out);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKdf\_Destroy(kdfCtx);
        OH\_CryptoKdfParams\_Destroy(params);
        return ret;
    }

    printf("Derived key length: %u\\n", out.len);

    // Free resources.
    OH\_Crypto\_FreeDataBlob(&out);
    OH\_CryptoKdf\_Destroy(kdfCtx);
    OH\_CryptoKdfParams\_Destroy(params);
    return CRYPTO\_SUCCESS;
}
