# Key Derivation Using X963KDF (C/C++)

From API version 22, the crypto algorithm library supports key derivation with X963KDF.

For details about the corresponding algorithm specifications, see [X963KDF](../key-derivation-overview-and-algorithm-specifications/document.md#x963kdf).

#### How to Develop

1.  Call [OH\_CryptoKdfParams\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdfparams_create) and specify the string parameter **X963KDF** to create a key derivation parameter object.
    
2.  Call [OH\_CryptoKdfParams\_SetParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdfparams_setparam) to set the parameters required by X963KDF. Example:
    
    -   **CRYPTO\_KDF\_KEY\_DATABLOB**: original key material used to generate a derived key.
    -   **CRYPTO\_KDF\_INFO\_DATABLOB**: (optional) application-specific information.
3.  Call [OH\_CryptoKdf\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdf_create) and specify the string parameter **X963KDF|SHA256** to create a key derivation function object.
    
4.  Call [OH\_CryptoKdf\_Derive](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdf_derive) and specify the byte length of the target key.
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include <stdio.h>
#include <string.h>

static OH\_Crypto\_ErrCode doTestX963Kdf()
{
    // Create a X963KDF parameter object.
    OH\_CryptoKdfParams \*params = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoKdfParams\_Create("X963KDF", &params);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // Set the original key material.
    const char \*keyData = "012345678901234567890123456789";
    Crypto\_DataBlob key = {
        .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(keyData)),
        .len = strlen(keyData)
    };
    ret = OH\_CryptoKdfParams\_SetParam(params, CRYPTO\_KDF\_KEY\_DATABLOB, &key);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKdfParams\_Destroy(params);
        return ret;
    }

    // Set application-specific information.
    const char \*infoData = "infostring";
    Crypto\_DataBlob info = {
        .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(infoData)),
        .len = strlen(infoData)
    };
    ret = OH\_CryptoKdfParams\_SetParam(params, CRYPTO\_KDF\_INFO\_DATABLOB, &info);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKdfParams\_Destroy(params);
        return ret;
    }

    // Create a key derivation function object.
    OH\_CryptoKdf \*kdfCtx = nullptr;
    ret = OH\_CryptoKdf\_Create("X963KDF|SHA256", &kdfCtx);
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
