# Generating a CMAC (C/C++)

A block cipher (such as AES) and a key are used to generate an authentication code, which verifies that a message has not been alerted during transmission.

#### How to Develop

In the **update** API call, you can [pass in full data](#generating-a-cmac-by-passing-in-full-data) or [pass in data by segment](#generating-a-cmac-by-passing-in-data-by-segment). The same data will produce the same result no matter how the data is passed. Use the appropriate method based on the data size.

The following provides examples of CMAC operations with different data passing methods.

## Generating a CMAC by Passing in Full Data

1.  Call [OH\_CryptoSymKeyGenerator\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_create) and [OH\_CryptoSymKeyGenerator\_Generate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-sym-key-h#oh_cryptosymkeygenerator_generate) to generate a symmetric key (**symKey**) with the key algorithm being AES-128.
    
2.  Call [OH\_CryptoMac\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_create) and specify the string parameter **CMAC** to create a MAC generator with the CMAC algorithm.
    
3.  Call [OH\_CryptoMac\_SetParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_setparam) and specify **CRYPTO\_MAC\_CIPHER\_NAME\_STR** to set the block cipher algorithm name.
    
4.  Call [OH\_CryptoMac\_Init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_init) and specify the shared symmetric key (**symKey**) to initialize the MAC object.
    
5.  Call [OH\_CryptoMac\_Update](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_update) to pass in the data.
    
6.  Call [OH\_CryptoMac\_Final](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_final) to obtain the MAC generation result.
    
7.  Call [OH\_CryptoMac\_GetLength](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_getlength) to obtain the length of the MAC, in bytes.
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include <stdio.h>
#include <string.h>

static OH\_CryptoSymKey \*GenerateAesKey(const char \*algoName)
{
    OH\_CryptoSymKeyGenerator \*keyGen = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoSymKeyGenerator\_Create(algoName, &keyGen);
    if (ret != CRYPTO\_SUCCESS) {
        return nullptr;
    }
    OH\_CryptoSymKey \*keyCtx = nullptr;
    ret = OH\_CryptoSymKeyGenerator\_Generate(keyGen, &keyCtx);
    OH\_CryptoSymKeyGenerator\_Destroy(keyGen);
    if (ret != CRYPTO\_SUCCESS) {
        return nullptr;
    }
    return keyCtx;
}

static OH\_Crypto\_ErrCode doTestCmacOnce()
{
    // Generate an AES-128 key.
    OH\_CryptoSymKey \*keyCtx = GenerateAesKey("AES128");
    if (keyCtx == nullptr) {
        return CRYPTO\_OPERTION\_ERROR;
    }

    // Create a CMAC generator.
    OH\_CryptoMac \*ctx = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoMac\_Create("CMAC", &ctx);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoSymKey\_Destroy(keyCtx);
        return ret;
    }

    // Set the block cipher algorithm name to AES128.
    const char \*cipherName = "AES128";
    Crypto\_DataBlob cipherNameData = {
        .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(cipherName)),
        .len = strlen(cipherName)
    };
    ret = OH\_CryptoMac\_SetParam(ctx, CRYPTO\_MAC\_CIPHER\_NAME\_STR, &cipherNameData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoMac\_Destroy(ctx);
        OH\_CryptoSymKey\_Destroy(keyCtx);
        return ret;
    }

    // Initialize the CMAC object.
    ret = OH\_CryptoMac\_Init(ctx, keyCtx);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoMac\_Destroy(ctx);
        OH\_CryptoSymKey\_Destroy(keyCtx);
        return ret;
    }

    // Pass in full data.
    const char \*message = "cmacTestMessage";
    Crypto\_DataBlob input = {
        .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(message)),
        .len = strlen(message)
    };
    ret = OH\_CryptoMac\_Update(ctx, &input);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoMac\_Destroy(ctx);
        OH\_CryptoSymKey\_Destroy(keyCtx);
        return ret;
    }

    // Finalize CMAC generation and obtain the result.
    Crypto\_DataBlob out = {0};
    ret = OH\_CryptoMac\_Final(ctx, &out);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoMac\_Destroy(ctx);
        OH\_CryptoSymKey\_Destroy(keyCtx);
        return ret;
    }

    // Obtain the length of the CMAC value.
    uint32\_t macLen = 0;
    ret = OH\_CryptoMac\_GetLength(ctx, &macLen);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_Crypto\_FreeDataBlob(&out);
        OH\_CryptoMac\_Destroy(ctx);
        OH\_CryptoSymKey\_Destroy(keyCtx);
        return ret;
    }

    printf("CMAC calculation success, length: %u\\n", macLen);

    // Free resources.
    OH\_Crypto\_FreeDataBlob(&out);
    OH\_CryptoMac\_Destroy(ctx);
    OH\_CryptoSymKey\_Destroy(keyCtx);
    return CRYPTO\_SUCCESS;
}

## Generating a CMAC by Passing in Data by Segment

Unlike the first method, this one requires calling [OH\_CryptoMac\_Update](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-mac-h#oh_cryptomac_update) multiple times to process segmented data.

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include <stdio.h>
#include <string.h>

static OH\_CryptoSymKey \*GenerateAesKey(const char \*algoName)
{
    OH\_CryptoSymKeyGenerator \*keyGen = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoSymKeyGenerator\_Create(algoName, &keyGen);
    if (ret != CRYPTO\_SUCCESS) {
        return nullptr;
    }
    OH\_CryptoSymKey \*keyCtx = nullptr;
    ret = OH\_CryptoSymKeyGenerator\_Generate(keyGen, &keyCtx);
    OH\_CryptoSymKeyGenerator\_Destroy(keyGen);
    if (ret != CRYPTO\_SUCCESS) {
        return nullptr;
    }
    return keyCtx;
}

static OH\_Crypto\_ErrCode doTestCmacBySegments()
{
    // Generate an AES-128 key.
    OH\_CryptoSymKey \*keyCtx = GenerateAesKey("AES128");
    if (keyCtx == nullptr) {
        return CRYPTO\_OPERTION\_ERROR;
    }

    // Create a CMAC generator.
    OH\_CryptoMac \*ctx = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoMac\_Create("CMAC", &ctx);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoSymKey\_Destroy(keyCtx);
        return ret;
    }

    // Set the block cipher algorithm name to AES128.
    const char \*cipherName = "AES128";
    Crypto\_DataBlob cipherNameData = {
        .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(cipherName)),
        .len = strlen(cipherName)
    };
    ret = OH\_CryptoMac\_SetParam(ctx, CRYPTO\_MAC\_CIPHER\_NAME\_STR, &cipherNameData);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoMac\_Destroy(ctx);
        OH\_CryptoSymKey\_Destroy(keyCtx);
        return ret;
    }

    // Initialize the CMAC object.
    ret = OH\_CryptoMac\_Init(ctx, keyCtx);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoMac\_Destroy(ctx);
        OH\_CryptoSymKey\_Destroy(keyCtx);
        return ret;
    }

    // Pass in data by segment.
    const char \*message = "aaaaa.....bbbbb.....ccccc.....ddddd.....eee";
    size\_t messageLen = strlen(message);
    size\_t segmentSize = 20; // Divide the data into segments of 20 bytes each.

    for (size\_t i = 0; i < messageLen; i += segmentSize) {
        size\_t currentSize = (i + segmentSize <= messageLen) ? segmentSize : (messageLen - i);
        Crypto\_DataBlob segment = {
            .data = reinterpret\_cast<uint8\_t \*>(const\_cast<char \*>(message + i)),
            .len = currentSize
        };
        ret = OH\_CryptoMac\_Update(ctx, &segment);
        if (ret != CRYPTO\_SUCCESS) {
            OH\_CryptoMac\_Destroy(ctx);
            OH\_CryptoSymKey\_Destroy(keyCtx);
            return ret;
        }
    }

    // Finalize CMAC generation and obtain the result.
    Crypto\_DataBlob out = {0};
    ret = OH\_CryptoMac\_Final(ctx, &out);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoMac\_Destroy(ctx);
        OH\_CryptoSymKey\_Destroy(keyCtx);
        return ret;
    }

    // Obtain the length of the CMAC value.
    uint32\_t macLen = 0;
    ret = OH\_CryptoMac\_GetLength(ctx, &macLen);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_Crypto\_FreeDataBlob(&out);
        OH\_CryptoMac\_Destroy(ctx);
        OH\_CryptoSymKey\_Destroy(keyCtx);
        return ret;
    }

    printf("CMAC calculation success, length: %u\\n", macLen);

    // Free resources.
    OH\_Crypto\_FreeDataBlob(&out);
    OH\_CryptoMac\_Destroy(ctx);
    OH\_CryptoSymKey\_Destroy(keyCtx);
    return CRYPTO\_SUCCESS;
}
