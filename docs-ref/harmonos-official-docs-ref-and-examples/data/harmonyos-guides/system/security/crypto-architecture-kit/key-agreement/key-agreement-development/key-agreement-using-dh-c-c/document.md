# Key Agreement Using DH (C/C++)

For details about the algorithm specifications, see [DH](../../key-agreement-overview-and-algorithm-specifications/document.md#dh).

#### How to Develop

1.  Call [OH\_CryptoAsymKeyGenerator\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_create) and [OH\_CryptoAsymKeyGenerator\_Generate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-asym-key-h#oh_cryptoasymkeygenerator_generate) to generate an asymmetric key (**keyPair**) of the DH\_modp1536 type.
    
    For details about how to generate a DH asymmetric key pair, see the following example. To learn more, see [DH](../../../key-generation-and-conversion/key-generation-and-conversion-specifications/asymmetric-key-generation-and-conversion-specifications/document.md#dh) and [Randomly Generating an Asymmetric Key Pair](../../../key-generation-and-conversion/key-generation-and-conversion-development/randomly-generating-an-asymmetric-key-pair-c-c/document.md). There may be differences between the input parameters in the reference documents and those in the following example.
    
2.  Call [OH\_CryptoKeyAgreement\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-key-agreement-h#oh_cryptokeyagreement_create) and specify the string parameter **DH\_modp1536** to create a key protocol generator of the DH\_modp1536 type.
    
3.  Call [OH\_CryptoKeyAgreement\_GenerateSecret](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-crypto-key-agreement-h#oh_cryptokeyagreement_generatesecret) to perform key agreement based on the passed private key (**keyPair.priKey**) and public key (**keyPair.pubKey**) and return the shared key.
    

#include "CryptoArchitectureKit/crypto\_architecture\_kit.h"
#include "CryptoArchitectureKit/crypto\_key\_agreement.h"
#include <stdio.h>
#include <cstring>

static OH\_Crypto\_ErrCode doTestDHKeyAgreement()
{
    // Create a DH key generator.
    OH\_CryptoAsymKeyGenerator \*dhGen = nullptr;
    OH\_Crypto\_ErrCode ret = OH\_CryptoAsymKeyGenerator\_Create("DH\_modp1536", &dhGen);
    if (ret != CRYPTO\_SUCCESS) {
        return ret;
    }

    // Generate public-private key pair A.
    OH\_CryptoKeyPair \*keyPairA = nullptr;
    ret = OH\_CryptoAsymKeyGenerator\_Generate(dhGen, &keyPairA);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoAsymKeyGenerator\_Destroy(dhGen);
        return ret;
    }

    // Generate public-private key pair B.
    OH\_CryptoKeyPair \*keyPairB = nullptr;
    ret = OH\_CryptoAsymKeyGenerator\_Generate(dhGen, &keyPairB);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKeyPair\_Destroy(keyPairA);
        OH\_CryptoAsymKeyGenerator\_Destroy(dhGen);
        return ret;
    }

    // Create a key agreement generator.
    OH\_CryptoKeyAgreement \*dhKeyAgreement = nullptr;
    ret = OH\_CryptoKeyAgreement\_Create("DH\_modp1536", &dhKeyAgreement);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKeyPair\_Destroy(keyPairA);
        OH\_CryptoKeyPair\_Destroy(keyPairB);
        OH\_CryptoAsymKeyGenerator\_Destroy(dhGen);
        return ret;
    }

    // Use the public key of A and the private key of B to perform key agreement.
    OH\_CryptoPrivKey \*privKeyB = OH\_CryptoKeyPair\_GetPrivKey(keyPairB);
    OH\_CryptoPubKey \*pubKeyA = OH\_CryptoKeyPair\_GetPubKey(keyPairA);
    Crypto\_DataBlob secret1 = { 0 };
    ret = OH\_CryptoKeyAgreement\_GenerateSecret(dhKeyAgreement, privKeyB, pubKeyA, &secret1);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_CryptoKeyAgreement\_Destroy(dhKeyAgreement);
        OH\_CryptoKeyPair\_Destroy(keyPairA);
        OH\_CryptoKeyPair\_Destroy(keyPairB);
        OH\_CryptoAsymKeyGenerator\_Destroy(dhGen);
        return ret;
    }

    // Use the public key of B and the private key of A to perform key agreement.
    OH\_CryptoPrivKey \*privKeyA = OH\_CryptoKeyPair\_GetPrivKey(keyPairA);
    OH\_CryptoPubKey \*pubKeyB = OH\_CryptoKeyPair\_GetPubKey(keyPairB);
    Crypto\_DataBlob secret2 = { 0 };
    ret = OH\_CryptoKeyAgreement\_GenerateSecret(dhKeyAgreement, privKeyA, pubKeyB, &secret2);
    if (ret != CRYPTO\_SUCCESS) {
        OH\_Crypto\_FreeDataBlob(&secret1);
        OH\_CryptoKeyAgreement\_Destroy(dhKeyAgreement);
        OH\_CryptoKeyPair\_Destroy(keyPairA);
        OH\_CryptoKeyPair\_Destroy(keyPairB);
        OH\_CryptoAsymKeyGenerator\_Destroy(dhGen);
        return ret;
    }

    // Compare the secrets.
    if ((secret1.len == secret2.len) &&
        (memcmp(secret1.data, secret2.data, secret1.len) == 0)) {
        printf("dh success\\n");
    } else {
        printf("dh result is not equal\\n");
        ret = CRYPTO\_OPERTION\_ERROR;
    }

    // Free resources.
    OH\_Crypto\_FreeDataBlob(&secret1);
    OH\_Crypto\_FreeDataBlob(&secret2);
    OH\_CryptoKeyAgreement\_Destroy(dhKeyAgreement);
    OH\_CryptoKeyPair\_Destroy(keyPairA);
    OH\_CryptoKeyPair\_Destroy(keyPairB);
    OH\_CryptoAsymKeyGenerator\_Destroy(dhGen);
    return ret;
}
