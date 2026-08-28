# Key Agreement Using ECDH (C/C++)

For details about the algorithm specifications, see [ECDH](../../key-agreement-overview-and-algorithm-specifications/document.md#ecdh).

#### How to Develop

1.  Call [OH\_CryptoAsymKeyGenerator\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_create), [OH\_CryptoAsymKeyGenerator\_Generate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_generate), and [OH\_CryptoAsymKeyGenerator\_Convert](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_convert) to generate a 256-bit asymmetric key (**keyPair**) of the ECC type.
    
    For details about how to generate an ECC asymmetric key pair, see the following example. To learn more, see [ECC](../../../key-generation-and-conversion/key-generation-and-conversion-specifications/asymmetric-key-generation-and-conversion-specifications/document.md#ecc) and [Randomly Generating an Asymmetric Key Pair](../../../key-generation-and-conversion/key-generation-and-conversion-development/randomly-generating-an-asymmetric-key-pair-c-c/document.md). There may be differences between the input parameters in the reference documents and those in the following example.
    
2.  Call [OH\_CryptoKeyAgreement\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-key-agreement-h#oh_cryptokeyagreement_create) and specify the string parameter **ECC256** to create a key protocol generator of the ECC type with the key length of 256 bits.
    
3.  Call [OH\_CryptoKeyAgreement\_GenerateSecret](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-key-agreement-h#oh_cryptokeyagreement_generatesecret) to perform key agreement based on the passed private key (**keyPair.priKey**) and public key (**keyPair.pubKey**) and return the shared key.
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include "CryptoArchitectureKit/crypto\_key\_agreement.h"
#include <stdio.h>
#include <cstring>

static OH\_Crypto\_ErrCode doTestEcdhKeyAgreement()
{
    // The public and private key pair data is transferred from an external system.
    uint8\_t pubKeyArray\[\] = {48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7,
                            3, 66, 0, 4, 83, 96, 142, 9, 86, 214, 126, 106, 247, 233, 92, 125, 4, 128, 138, 105, 246,
                            162, 215, 71, 81, 58, 202, 121, 26, 105, 211, 55, 130, 45, 236, 143, 55, 16, 248, 75, 167,
                            160, 167, 106, 2, 152, 243, 44, 68, 66, 0, 167, 99, 92, 235, 215, 159, 239, 28, 106, 124,
                            171, 34, 145, 124, 174, 57, 92};
    uint8\_t priKeyArray\[\] = {48, 49, 2, 1, 1, 4, 32, 115, 56, 137, 35, 207, 0, 60, 191, 90, 61, 136, 105, 210, 16,
                            27, 4, 171, 57, 10, 61, 123, 40, 189, 28, 34, 207, 236, 22, 45, 223, 10, 189, 160, 10, 6,
                            8, 42, 134, 72, 206, 61, 3, 1, 7};

    // Create an ECC key generator.
    OH\_CryptoAsymKeyGenerator \*eccGen = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoAsymKeyGenerator\_Create("ECC256", &eccGen);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // Key pair A passed from an external system.
    Crypto\_DataBlob pubKeyBlob = {pubKeyArray, sizeof(pubKeyArray)};
    Crypto\_DataBlob priKeyBlob = {priKeyArray, sizeof(priKeyArray)};
    OH\_CryptoKeyPair \*keyPairA = nullptr;
    ret = OH\_CryptoAsymKeyGenerator\_Convert(eccGen, CRYPTO\_DER, &pubKeyBlob, &priKeyBlob, &keyPairA);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeyGenerator\_Destroy(eccGen);
        return ret;
    }

    // Key pair B generated internally.
    OH\_CryptoKeyPair \*keyPairB = nullptr;
    ret = OH\_CryptoAsymKeyGenerator\_Generate(eccGen, &keyPairB);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKeyPair\_Destroy(keyPairA);
        OH\_CryptoAsymKeyGenerator\_Destroy(eccGen);
        return ret;
    }

    // Create a key agreement generator.
    OH\_CryptoKeyAgreement \*eccKeyAgreement = nullptr;
    ret = OH\_CryptoKeyAgreement\_Create("ECC256", &eccKeyAgreement);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKeyPair\_Destroy(keyPairA);
        OH\_CryptoKeyPair\_Destroy(keyPairB);
        OH\_CryptoAsymKeyGenerator\_Destroy(eccGen);
        return ret;
    }

    // Use the public key of A and the private key of B to perform key agreement.
    OH\_CryptoPrivKey \*privKeyB = OH\_CryptoKeyPair\_GetPrivKey(keyPairB);
    OH\_CryptoPubKey \*pubKeyA = OH\_CryptoKeyPair\_GetPubKey(keyPairA);
    Crypto\_DataBlob secret1 = { 0 };
    ret = OH\_CryptoKeyAgreement\_GenerateSecret(eccKeyAgreement, privKeyB, pubKeyA, &secret1);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKeyAgreement\_Destroy(eccKeyAgreement);
        OH\_CryptoKeyPair\_Destroy(keyPairA);
        OH\_CryptoKeyPair\_Destroy(keyPairB);
        OH\_CryptoAsymKeyGenerator\_Destroy(eccGen);
        return ret;
    }

    // Use the private key of A and the public key of B to perform key agreement.
    OH\_CryptoPrivKey \*privKeyA = OH\_CryptoKeyPair\_GetPrivKey(keyPairA);
    OH\_CryptoPubKey \*pubKeyB = OH\_CryptoKeyPair\_GetPubKey(keyPairB);
    Crypto\_DataBlob secret2 = { 0 };
    ret = OH\_CryptoKeyAgreement\_GenerateSecret(eccKeyAgreement, privKeyA, pubKeyB, &secret2);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_Crypto\_FreeDataBlob(&secret1);
        OH\_CryptoKeyAgreement\_Destroy(eccKeyAgreement);
        OH\_CryptoKeyPair\_Destroy(keyPairA);
        OH\_CryptoKeyPair\_Destroy(keyPairB);
        OH\_CryptoAsymKeyGenerator\_Destroy(eccGen);
        return ret;
    }

    // Compare the secrets.
    if ((secret1.len == secret2.len) &&
        (memcmp(secret1.data, secret2.data, secret1.len) == 0)) {
        printf("ecdh success\\n");
    } else {
        printf("ecdh result is not equal\\n");
        ret = CRYPTO\_OPERTION\_ERROR;
    }

    // Free resources.
    OH\_Crypto\_FreeDataBlob(&secret1);
    OH\_Crypto\_FreeDataBlob(&secret2);
    OH\_CryptoKeyAgreement\_Destroy(eccKeyAgreement);
    OH\_CryptoKeyPair\_Destroy(keyPairA);
    OH\_CryptoKeyPair\_Destroy(keyPairB);
    OH\_CryptoAsymKeyGenerator\_Destroy(eccGen);
    return ret;
}
