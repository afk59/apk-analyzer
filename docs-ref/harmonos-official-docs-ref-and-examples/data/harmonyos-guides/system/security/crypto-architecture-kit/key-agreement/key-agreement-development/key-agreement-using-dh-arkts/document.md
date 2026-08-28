# Key Agreement Using DH (ArkTS)

For details about the algorithm specifications, see [DH](../../key-agreement-overview-and-algorithm-specifications/document.md#dh).

#### How to Develop

1.  Call [cryptoFramework.createAsyKeyGenerator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreateasykeygenerator) and [AsyKeyGenerator.generateKeyPair](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#generatekeypair-1) to generate an asymmetric key pair (**KeyPair**) that uses the DH key algorithm and the well-known security prime group modp1536.
    
    In addition to the example in this topic, [DH](../../../key-generation-and-conversion/key-generation-and-conversion-specifications/asymmetric-key-generation-and-conversion-specifications/document.md#dh) and [Randomly Generating an Asymmetric Key Pair](../../../key-generation-and-conversion/key-generation-and-conversion-development/randomly-generating-an-asymmetric-key-pair-arkts/document.md) may help you better understand how to generate a DH asymmetric key pair. Note that the input parameters in the reference documents may be different from those in the example below.
    
2.  Call [cryptoFramework.createKeyAgreement](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreatekeyagreement) with the string parameter **'DH\_modp1536'** to create a key agreement (**KeyAgreement**) that uses the DH key algorithm and the well-known security prime group modp1536.
    
3.  Call [KeyAgreement.generateSecret](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#generatesecret-1) to perform key agreement with the specified private key (**KeyPair.priKey**) and public key (**KeyPair.pubKey**), and return the shared secret.
    

-   Example (using asynchronous APIs):
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    
    async function dhAwait() {
      let keyGen = cryptoFramework.createAsyKeyGenerator('DH\_modp1536');
      // Randomly generate public-private key pair A.
      let keyPairA = await keyGen.generateKeyPair();
      // Randomly generate public-private key pair B with the same specifications.
      let keyPairB = await keyGen.generateKeyPair();
      let keyAgreement = cryptoFramework.createKeyAgreement('DH\_modp1536');
      // Use the public key of A and the private key of B to perform key agreement.
      let secret1 = await keyAgreement.generateSecret(keyPairB.priKey, keyPairA.pubKey);
      // Use the private key of A and the public key of B to perform key agreement.
      let secret2 = await keyAgreement.generateSecret(keyPairA.priKey, keyPairB.pubKey);
      // The two key agreement results should be the same.
      if (secret1.data.toString() === secret2.data.toString()) {
        console.info('DH success');
        console.info('DH output is ' + secret1.data);
      } else {
        console.error('DH result is not equal');
      }
    }
    
-   Example (using synchronous APIs):
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    
    function dhAgreementSync() {
      let keyGen = cryptoFramework.createAsyKeyGenerator('DH\_modp1536');
      // Randomly generate public-private key pair A.
      let keyPairA = keyGen.generateKeyPairSync();
      // Randomly generate public-private key pair B with the same specifications.
      let keyPairB = keyGen.generateKeyPairSync();
      let keyAgreement = cryptoFramework.createKeyAgreement('DH\_modp1536');
      // Use the public key of A and the private key of B to perform key agreement.
      let secret1 = keyAgreement.generateSecretSync(keyPairB.priKey, keyPairA.pubKey);
      // Use the private key of A and the public key of B to perform key agreement.
      let secret2 = keyAgreement.generateSecretSync(keyPairA.priKey, keyPairB.pubKey);
      // The two key agreement results should be the same.
      if (secret1.data.toString() === secret2.data.toString()) {
        console.info('DH success');
        console.info('DH output is ' + secret1.data);
      } else {
        console.error('DH result is not equal');
      }
    }
