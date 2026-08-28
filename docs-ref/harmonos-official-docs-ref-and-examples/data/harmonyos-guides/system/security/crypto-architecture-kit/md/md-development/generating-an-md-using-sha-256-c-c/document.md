# Generating an MD Using SHA-256 (C/C++)

For details about the algorithm specifications, see [Supported Algorithms and Specifications](../../md-overview-and-algorithm-specifications/document.md#supported-algorithms-and-specifications).

#### Adding the Dynamic Library in the CMake Script

target\_link\_libraries(entry PUBLIC libohcrypto.so)

#### How to Develop

During the MD operation, you can [pass in all the data at a time](#generating-an-md-by-passing-in-full-data) or [pass in data by segment](#generating-an-md-by-passing-in-data-by-segment). For the same piece of data, the result will be the same no matter how the data is passed. Use the appropriate method based on the data size.

The following provides examples of MD operations with different data passing methods.

## Generating an MD by Passing In Full Data

1.  Call [OH\_CryptoDigest\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-digest-h#oh_cryptodigest_create) with the MD algorithm **SHA256** to generate an MD operation instance (**OH\_CryptoDigest**).
    
2.  Call [OH\_CryptoDigest\_Update](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-digest-h#oh_cryptodigest_update) to pass in the data for generating an MD. The amount of data to be passed in by a single **OH\_CryptoDigest\_Update()** operation is not limited.
    
3.  Call [OH\_CryptoDigest\_Final](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-digest-h#oh_cryptodigest_final) to generate an MD.
    
4.  Call [OH\_CryptoDigest\_GetLength](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-digest-h#oh_cryptodigest_getlength) to obtain the MD length, in bytes.
    
5.  Call [OH\_DigestCrypto\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-digest-h#oh_digestcrypto_destroy) to destroy the **OH\_CryptoDigest** instance.
    

-   **Example**

#include "CryptoArchitectureKit/crypto\_common.h"
#include "CryptoArchitectureKit/crypto\_digest.h"
#include <string.h>

static OH\_Crypto\_ErrCode doTestMd()
{
    OH\_Crypto\_ErrCode ret;
    OH\_CryptoDigest \*ctx = nullptr;
    char \*testData = const\_cast<char \*>("0123456789");
    Crypto\_DataBlob in = {.data = (uint8\_t \*)(testData), .len = strlen(testData)};
    Crypto\_DataBlob out = {.data = nullptr, .len = 0};
    int mdLen = 0;
    ret = OH\_CryptoDigest\_Create("SHA256", &ctx);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }
    do {
        ret = OH\_CryptoDigest\_Update(ctx, &in);
        if (ret != CRYPTO\_SUCCESS) {
            break;
        }
        ret = OH\_CryptoDigest\_Final(ctx, &out);
        if (ret != CRYPTO\_SUCCESS) {
            break;
        }
        mdLen = OH\_CryptoDigest\_GetLength(ctx);
    } while (0);
    OH\_Crypto\_FreeDataBlob(&out);
    OH\_DigestCrypto\_Destroy(ctx);
    return ret;
}

## Generating an MD by Passing In Data by Segment

1.  Call [OH\_CryptoDigest\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-digest-h#oh_cryptodigest_create) with the MD algorithm **SHA256** to generate an MD operation instance (**OH\_CryptoDigest**).
    
2.  Call [OH\_CryptoDigest\_Update](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-digest-h#oh_cryptodigest_update) multiple times to pass in 20 bytes each time.
    
3.  Call [OH\_CryptoDigest\_Final](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-digest-h#oh_cryptodigest_final) to generate an MD.
    
4.  Call [OH\_CryptoDigest\_GetLength](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-digest-h#oh_cryptodigest_getlength) to obtain the MD length, in bytes.
    
5.  Call [OH\_DigestCrypto\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-digest-h#oh_digestcrypto_destroy) to destroy the **OH\_CryptoDigest** instance.
    

-   **Example**

#include <stdlib.h>
#include "CryptoArchitectureKit/crypto\_common.h"
#include "CryptoArchitectureKit/crypto\_digest.h"
#define OH\_CRYPTO\_DIGEST\_DATA\_MAX (1024 \* 1024 \* 100)

static OH\_Crypto\_ErrCode doLoopMd()
{
    OH\_Crypto\_ErrCode ret;
    OH\_CryptoDigest \*ctx = nullptr;
    uint8\_t \*testData = (uint8\_t \*)malloc(OH\_CRYPTO\_DIGEST\_DATA\_MAX);
    if (testData == nullptr) {
        return CRYPTO\_MEMORY\_ERROR;
    }
    Crypto\_DataBlob out = {.data = nullptr, .len = 0};
    int mdLen = 0;
    int isBlockSize = 20;
    int offset = 0;

    ret = OH\_CryptoDigest\_Create("SHA256", &ctx);
    if (ret != CRYPTO\_SUCCESS) {
        free(testData);
        return ret;
    }
    do {
        for (int i = 0; i < 640 / isBlockSize; i++) {
            Crypto\_DataBlob in = {.data = reinterpret\_cast<uint8\_t \*>(testData + offset),
                                .len = static\_cast<size\_t>(isBlockSize)};
            ret = OH\_CryptoDigest\_Update(ctx, &in);
            if (ret != CRYPTO\_SUCCESS) {
                break;
            }
            offset += isBlockSize;
        }
        ret = OH\_CryptoDigest\_Final(ctx, &out);
        if (ret != CRYPTO\_SUCCESS) {
            break;
        }
        mdLen = OH\_CryptoDigest\_GetLength(ctx);
    } while (0);
    OH\_Crypto\_FreeDataBlob(&out);
    OH\_DigestCrypto\_Destroy(ctx);
    free(testData);
    return ret;
}
