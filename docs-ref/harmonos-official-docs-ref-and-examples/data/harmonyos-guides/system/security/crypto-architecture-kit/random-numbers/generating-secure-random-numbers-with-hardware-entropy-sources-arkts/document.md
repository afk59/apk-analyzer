# Generating Secure Random Numbers with Hardware Entropy Sources (ArkTS)

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

1.  Call [cryptoFramework.createRandom](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreaterandom) to create a **Random** instance.
    
2.  Call [cryptoFramework.enableHardwareEntropy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#enablehardwareentropy21) to enable the hardware entropy source.
    
3.  (Optional) Call [Random.setSeed](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#setseed) to set a seed for the random number generator.
    
4.  Call [Random.generateRandom](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#generaterandom) or [Random.generateRandomSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#generaterandomsync10) to generate a secure random number.
    
    The length of the random number to generate ranges from **1** to **INT\_MAX**, in bytes.
    

-   Return the result using **await**:
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    
    async function doRand() {
      let rand = cryptoFramework.createRandom();
      rand.enableHardwareEntropy();
      let seed = new Uint8Array(\[1, 2, 3\]);
      rand.setSeed({ data: seed });
      let len = 12;
      let randOutput = await rand.generateRandom(len);
      console.info('rand output:' + randOutput.data);
    }
    
-   Return the result synchronously:
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function doRandBySync() {
      let rand = cryptoFramework.createRandom();
      rand.enableHardwareEntropy();
      let len = 24; // Generate a 24-byte random number.
      try {
        let randData = rand.generateRandomSync(len);
        if (randData.data.length !== 0) {
          console.info("\[Sync\]: rand result: " + randData.data);
        } else {
          console.error("\[Sync\]: get rand result fail!");
        }
      } catch (error) {
        let e: BusinessError = error as BusinessError;
        console.error(\`do rand failed, ${e.code}, ${e.message}\`);
      }
    }
