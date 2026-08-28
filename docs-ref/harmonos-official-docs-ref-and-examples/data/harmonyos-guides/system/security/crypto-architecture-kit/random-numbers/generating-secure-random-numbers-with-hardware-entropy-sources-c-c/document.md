# Generating Secure Random Numbers with Hardware Entropy Sources (C/C++)

From API version 21, you can generate secure random number with hardware entropy sources.

Random numbers are used to generate temporary session keys and asymmetric encryption algorithm keys. In encryption and decryption, a secure random number generator must feature randomness, unrepeatability, and unpredictability.

A stronger entropy source makes random numbers harder to predict or replicate, achieving true randomness.

You need to call the [HUKS](../../../universal-keystore-kit/about-this-kit/document.md) APIs to implement the hardware entropy source.

You can call APIs to:

-   Generate a secure random number of the specified length and use it to generate a key.
    
-   Enable the hardware entropy source.
    
-   Generate a series of random sequences based on a seed.
    

It will be helpful if you have basic knowledge of encryption and decryption and understand the following basic concepts:

-   **Internal state**
    
    A value in the random number generator memory. The same internal state produces a random number of the same sequence.
    
-   **Random seed**
    
    A number used to initialize the internal state of a pseudorandom number generator. The random number generator generates a series of random sequences based on the seeds.
    
    In the OpenSSL implementation, the internal state of the random number generator changes continuously. Therefore, the generated random number sequences are different even if the same seed is used.
    

#### Supported Algorithms and Specifications

After the hardware entropy source is set, use the **RAND\_priv\_bytes** API of OpenSSL to generate secure random numbers.

| Algorithm | Length (Byte) |
| :-- | :-- |
| CTR\_DRBG | \[1, INT\_MAX\] |

#### How to Develop

1.  Call [OH\_CryptoRand\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-rand-h#oh_cryptorand_create) to create a random number generator.
    
2.  Call [OH\_CryptoRand\_EnableHardwareEntropy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-rand-h#oh_cryptorand_enablehardwareentropy) to enable the hardware entropy source.
    
3.  (Optional) Call [OH\_CryptoRand\_SetSeed](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-rand-h#oh_cryptorand_setseed) to set a seed for the random number generator.
    
4.  Call [OH\_CryptoRand\_GenerateRandom](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-rand-h#oh_cryptorand_generaterandom) to generate a secure random number of the given length. The length of the random number to generate ranges from **1** to **INT\_MAX**, in bytes.
    
5.  Call [OH\_CryptoRand\_GetAlgoName](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-rand-h#oh_cryptorand_getalgoname) to obtain the algorithm name used by the random number generator.
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include <stdio.h>

static OH\_Crypto\_ErrCode doTestRandomNumber()
{
    // Create a random number generator.
    OH\_CryptoRand \*rand = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoRand\_Create(&rand);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // Enable the hardware entropy source.
    ret = OH\_CryptoRand\_EnableHardwareEntropy(rand);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoRand\_Destroy(rand);
        return ret;
    }

    // (Optional) Set the random seed.
    uint8\_t seedData\[12\] = {0x25, 0x65, 0x58, 0x89, 0x85, 0x55, 0x66, 0x77, 0x88, 0x99, 0x11, 0x22};
    Crypto\_DataBlob seed = {
        .data = seedData,
        .len = sizeof(seedData)
    };
    ret = OH\_CryptoRand\_SetSeed(rand, &seed);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoRand\_Destroy(rand);
        return ret;
    }

    // Generate a random number of the given length.
    Crypto\_DataBlob out = {0};
    uint32\_t randomLength = 24; // Generate a 24-byte random number.
    ret = OH\_CryptoRand\_GenerateRandom(rand, randomLength, &out);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoRand\_Destroy(rand);
        return ret;
    }

    // Obtain and print the algorithm name of the random number generator.
    const char \*algoName = OH\_CryptoRand\_GetAlgoName(rand);
    if (algoName != nullptr) {
        printf("Random number generator algorithm: %s\\n", algoName);
    }

    printf("Generated random number length: %u\\n", out.len);

    // Free resources.
    OH\_Crypto\_FreeDataBlob(&out);
    OH\_CryptoRand\_Destroy(rand);
    return CRYPTO\_SUCCESS;
}
