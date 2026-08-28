# Key Derivation Using PBKDF2 (C/C++)

For details about the corresponding algorithm specifications, see [PBKDF2](../key-derivation-overview-and-algorithm-specifications/document.md#pbkdf2).

#### How to Develop

1.  Call [OH\_CryptoKdfParams\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdfparams_create) and specify the string parameter **PBKDF2** to create a key derivation parameter object.
    
2.  Call [OH\_CryptoKdfParams\_SetParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdfparams_setparam) to set the parameters required by PBKDF2. Example:
    
    -   **CRYPTO\_KDF\_KEY\_DATABLOB**: original password used to generate the derived key.
    -   **CRYPTO\_KDF\_SALT\_DATABLOB**: salt value.
    -   **CRYPTO\_KDF\_ITER\_COUNT\_INT**: number of iterations. The value must be a positive integer.
3.  Call [OH\_CryptoKdf\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdf_create) and specify the string parameter **PBKDF2|SHA256** to create a key derivation function object.
    
4.  Call [OH\_CryptoKdf\_Derive](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdf_derive) and specify the byte length of the target key.
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include <stdio.h>
#include <string.h>

static OH\_Crypto\_ErrCode doTestPbkdf2()
{
    // Create a PBKDF2 parameter object.
    OH\_CryptoKdfParams \*params = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoKdfParams\_Create("PBKDF2", &params);
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

    // Set the number of iterations.
    int iterations = 10000;
    Crypto\_DataBlob iterationsBlob = {
        .data = reinterpret\_cast<uint8\_t \*>(&iterations),
        .len = sizeof(int)
    };
    ret = OH\_CryptoKdfParams\_SetParam(params, CRYPTO\_KDF\_ITER\_COUNT\_INT, &iterationsBlob);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKdfParams\_Destroy(params);
        return ret;
    }

    // Create a key derivation function object.
    OH\_CryptoKdf \*kdfCtx = nullptr;
    ret = OH\_CryptoKdf\_Create("PBKDF2|SHA256", &kdfCtx);
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
