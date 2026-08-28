# Key Agreement Using X25519 (C/C++)

For details about the algorithm specifications, see [X25519](../../key-agreement-overview-and-algorithm-specifications/document.md#x25519).

#### How to Develop

1.  Call [OH\_CryptoAsymKeyGenerator\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_create), [OH\_CryptoAsymKeyGenerator\_Generate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_generate), and [OH\_CryptoAsymKeyGenerator\_Convert](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_convert) to generate an asymmetric key (**keyPair**) of the X25519 type.
    
    For details about how to generate an X25519 asymmetric key pair, see the following example. To learn more, see [X25519](../../../key-generation-and-conversion/key-generation-and-conversion-specifications/asymmetric-key-generation-and-conversion-specifications/document.md#x25519) and [Randomly Generating an Asymmetric Key Pair](../../../key-generation-and-conversion/key-generation-and-conversion-development/randomly-generating-an-asymmetric-key-pair-c-c/document.md). There may be differences between the input parameters in the reference documents and those in the following example.
    
2.  Call [OH\_CryptoKeyAgreement\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-key-agreement-h#oh_cryptokeyagreement_create) and specify the string parameter **X25519** to create a key protocol generator of the X25519 type.
    
3.  Call [OH\_CryptoKeyAgreement\_GenerateSecret](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-key-agreement-h#oh_cryptokeyagreement_generatesecret) to perform key agreement based on the passed private key (**keyPair.priKey**) and public key (**keyPair.pubKey**) and return the shared key.
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include "CryptoArchitectureKit/crypto\_key\_agreement.h"
#include <stdio.h>
#include <cstring>

static OH\_Crypto\_ErrCode doTestX25519KeyAgreement()
{
    uint8\_t pubKeyArray\[\] = {48, 42, 48, 5, 6, 3, 43, 101, 110, 3, 33, 0, 36, 98, 216, 106, 74, 99, 179, 203, 81, 145,
                             147, 101, 139, 57, 74, 225, 119, 196, 207, 0, 50, 232, 93, 147, 188, 21, 225, 228, 54, 251,
                             230, 52};
    uint8\_t priKeyArray\[\] = {48, 46, 2, 1, 0, 48, 5, 6, 3, 43, 101, 110, 4, 34, 4, 32, 112, 65, 156, 73, 65, 89, 183,
                             39, 119, 229, 110, 12, 192, 237, 186, 153, 21, 122, 28, 176, 248, 108, 22, 242, 239, 179,
                             106, 175, 85, 65, 214, 90};
    // Create an X25519 key generator.
    OH\_CryptoAsymKeyGenerator \*x25519Gen = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoAsymKeyGenerator\_Create("X25519", &x25519Gen);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // Key pair A passed from an external system.
    Crypto\_DataBlob pubKeyBlob = {pubKeyArray, sizeof(pubKeyArray)};
    Crypto\_DataBlob priKeyBlob = {priKeyArray, sizeof(priKeyArray)};
    OH\_CryptoKeyPair \*keyPairA = nullptr;
    ret = OH\_CryptoAsymKeyGenerator\_Convert(x25519Gen, CRYPTO\_DER, &pubKeyBlob, &priKeyBlob, &keyPairA);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeyGenerator\_Destroy(x25519Gen);
        return ret;
    }

    // Key pair B generated internally.
    OH\_CryptoKeyPair \*keyPairB = nullptr;
    ret = OH\_CryptoAsymKeyGenerator\_Generate(x25519Gen, &keyPairB);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKeyPair\_Destroy(keyPairA);
        OH\_CryptoAsymKeyGenerator\_Destroy(x25519Gen);
        return ret;
    }

    // Create a key agreement generator.
    OH\_CryptoKeyAgreement \*x25519KeyAgreement = nullptr;
    ret = OH\_CryptoKeyAgreement\_Create("X25519", &x25519KeyAgreement);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKeyPair\_Destroy(keyPairA);
        OH\_CryptoKeyPair\_Destroy(keyPairB);
        OH\_CryptoAsymKeyGenerator\_Destroy(x25519Gen);
        return ret;
    }

    // Use the public key of A and the private key of B to perform key agreement.
    OH\_CryptoPrivKey \*privKeyB = OH\_CryptoKeyPair\_GetPrivKey(keyPairB);
    OH\_CryptoPubKey \*pubKeyA = OH\_CryptoKeyPair\_GetPubKey(keyPairA);
    Crypto\_DataBlob secret1 = {0};
    ret = OH\_CryptoKeyAgreement\_GenerateSecret(x25519KeyAgreement, privKeyB, pubKeyA, &secret1);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKeyAgreement\_Destroy(x25519KeyAgreement);
        OH\_CryptoKeyPair\_Destroy(keyPairA);
        OH\_CryptoKeyPair\_Destroy(keyPairB);
        OH\_CryptoAsymKeyGenerator\_Destroy(x25519Gen);
        return ret;
    }

    // Use the private key of A and the public key of B to perform key agreement.
    OH\_CryptoPrivKey \*privKeyA = OH\_CryptoKeyPair\_GetPrivKey(keyPairA);
    OH\_CryptoPubKey \*pubKeyB = OH\_CryptoKeyPair\_GetPubKey(keyPairB);
    Crypto\_DataBlob secret2 = {0};
    ret = OH\_CryptoKeyAgreement\_GenerateSecret(x25519KeyAgreement, privKeyA, pubKeyB, &secret2);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_Crypto\_FreeDataBlob(&secret1);
        OH\_CryptoKeyAgreement\_Destroy(x25519KeyAgreement);
        OH\_CryptoKeyPair\_Destroy(keyPairA);
        OH\_CryptoKeyPair\_Destroy(keyPairB);
        OH\_CryptoAsymKeyGenerator\_Destroy(x25519Gen);
        return ret;
    }

    // Compare the secrets.
    if ((secret1.len == secret2.len) && (memcmp(secret1.data, secret2.data, secret1.len) == 0)) {
        printf("x25519 success\\n");
    } else {
        printf("x25519 result is not equal\\n");
        ret = CRYPTO\_OPERTION\_ERROR;
    }

    // Free resources.
    OH\_Crypto\_FreeDataBlob(&secret1);
    OH\_Crypto\_FreeDataBlob(&secret2);
    OH\_CryptoKeyAgreement\_Destroy(x25519KeyAgreement);
    OH\_CryptoKeyPair\_Destroy(keyPairA);
    OH\_CryptoKeyPair\_Destroy(keyPairB);
    OH\_CryptoAsymKeyGenerator\_Destroy(x25519Gen);
    return ret;
}
