# Key Derivation Using Scrypt (ArkTS)

For details about the corresponding algorithm specifications, see [Scrypt](../key-derivation-overview-and-algorithm-specifications/document.md#scrypt).

#### How to Develop

1.  Create an [ScryptSpec](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#scryptspec18) object and use it as a parameter for key derivation.
    
    **ScryptSpec** is a child class of [KdfSpec](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#kdfspec11). You need to specify the following:
    
    -   **algName**: algorithm to use, which is **'SCRYPT'**.
        
    -   **passphrase**: original password used to generate the derived key.
        
        If the string type is used, pass in the data used for key derivation instead of the string type such as HexString or base64. In addition, ensure that the string is encoded in UTF-8 format. Otherwise, the derived key may be different from what you expected.
        
    -   **salt**: salt value.
        
    -   **n**: number of iterations. The value must be a positive integer.
        
    -   **p**: parallelization parameter. The value must be a positive integer.
        
    -   **r**: block size. The value must be a positive integer.
        
    -   **maxMemory**: maximum memory size. The value must be a positive integer.
        
    -   **keySize**: length of the key to derive, in bytes. The value must be a positive integer.
        
2.  Call [cryptoFramework.createKdf](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreatekdf11) with the string parameter set to **'SCRYPT'** to create a key derivation function object (**Kdf**) with the scrypt algorithm.
    
3.  Call [Kdf.generateSecret](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#generatesecret11) with the **SCRYPT** object to generate a derived key.
    
    The following table lists how **Kdf.generateSecret** delivers the return value.
    
    | API | Return Mode |
    | :-- | :-- |
    | generateSecret(params: KdfSpec, callback: AsyncCallback<DataBlob>): void | This API uses an asynchronous callback to return the result. |
    | generateSecret(params: KdfSpec): Promise<DataBlob> | This API uses a promise to return the result. |
    | generateSecretSync(params: KdfSpec): DataBlob | This API returns the result synchronously. |
    

-   Return the result using **await**:
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    async function ScryptAwait() {
      try {
        let spec: cryptoFramework.ScryptSpec = {
          algName: 'SCRYPT',
          salt: new Uint8Array(16),
          passphrase: "password",
          n:1024,
          p:16,
          r:8,
          maxMemory:1024 \* 16 \* 8 \* 10, //n \* p \* r \* 10
          keySize: 64
        };
        let kdf = cryptoFramework.createKdf('SCRYPT');
        let secret = await kdf.generateSecret(spec);
        console.info("key derivation output is " + secret.data);
      } catch(error) {
        let e: BusinessError = error as BusinessError;
        console.error('key derivation failed, errCode: ' + e.code + ', errMsg: ' + e.message);
      }
    }
    
-   Return the result using a promise:
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function ScryptPromise() {
      let spec: cryptoFramework.ScryptSpec = {
        algName: 'SCRYPT',
        passphrase: '123456',
        salt: new Uint8Array(16),
        n:1024,
        p:16,
        r:8,
        maxMemory:1024 \* 16 \* 8 \* 10, //n \* p \* r \* 10
        keySize: 64
      };
      let kdf = cryptoFramework.createKdf('SCRYPT');
      let kdfPromise = kdf.generateSecret(spec);
      kdfPromise.then((secret) => {
        console.info("key derivation output is " + secret.data);
      }).catch((error: BusinessError) => {
        console.error("key derivation error.");
      });
    }
    
-   Return the result synchronously:
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function kdfSync() {
      try {
        let spec: cryptoFramework.ScryptSpec = {
          algName: 'SCRYPT',
          passphrase: '123456',
          salt: new Uint8Array(16),
          n:1024,
          p:16,
          r:8,
          maxMemory:1024 \* 16 \* 8 \* 10, //n \* p \* r \* 10
          keySize: 64
        };
        let kdf = cryptoFramework.createKdf('SCRYPT');
        let secret = kdf.generateSecretSync(spec);
        console.info("\[Sync\]key derivation output is " + secret.data);
      } catch(error) {
        let e: BusinessError = error as BusinessError;
        console.error('key derivation failed, errCode: ' + e.code + ', errMsg: ' + e.message);
      }
    }
