# Key Derivation Using PBKDF2 (ArkTS)

For details about the corresponding algorithm specifications, see [PBKDF2](../key-derivation-overview-and-algorithm-specifications/document.md#pbkdf2).

#### How to Develop

1.  Create a [PBKDF2Spec](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#pbkdf2spec11) object and use it as a parameter for key derivation.
    
    **PBKDF2Spec** is a child class of [KdfSpec](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#kdfspec11). You need to specify the following:
    
    -   **algName**: algorithm to use, which is **'PBKDF2'**.
        
    -   **password**: original password used to generate the derived key.
        
        If **key** is of the string type, pass in the data used for key derivation instead of the string type such as HexString or base64. In addition, ensure that the string is encoded in UTF-8 format. Otherwise, the derived key may be different from what you expected.
        
    -   **salt**: specifies the salt value.
        
    -   **iterations**: number of iterations. The value must be a positive integer.
        
    -   **keySize**: length of the key to derive, in bytes. The value must be a positive integer.
        
2.  Call [cryptoFramework.createKdf](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreatekdf11) with the string parameter **'PBKDF2|SHA256'** to create a **Kdf** object. The key derivation algorithm is **PBKDF2**, and HMAC algorithm is **SHA256**.
    
3.  Call [Kdf.generateSecret](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#generatesecret11) with the **PBKDF2Spec** object to generate a derived key.
    
    The following table lists how **Kdf.generateSecret** delivers the return value.
    
    | API | Return Mode |
    | :-- | :-- |
    | generateSecret(params: KdfSpec, callback: AsyncCallback<DataBlob>): void | This API uses an asynchronous callback to return the result. |
    | generateSecret(params: KdfSpec): Promise<DataBlob> | This API uses a promise to return the result. |
    | generateSecretSync(params: KdfSpec): DataBlob | This API returns the result synchronously. |
    

-   Return the result using **await**:
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    
    async function kdfAwait() {
      let spec: cryptoFramework.PBKDF2Spec = {
        algName: 'PBKDF2',
        password: '123456',
        salt: new Uint8Array(16),
        iterations: 10000,
        keySize: 32
      };
      let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');
      let secret = await kdf.generateSecret(spec);
      console.info("key derivation output is " + secret.data);
    }
    
-   Return the result using a promise:
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function kdfPromise() {
      let spec: cryptoFramework.PBKDF2Spec = {
        algName: 'PBKDF2',
        password: '123456',
        salt: new Uint8Array(16),
        iterations: 10000,
        keySize: 32
      };
      let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');
      let kdfPromise = kdf.generateSecret(spec);
      kdfPromise.then((secret) => {
        console.info("key derivation output is " + secret.data);
      }).catch((error: BusinessError) => {
        console.error("key derivation error.");
      });
    }
    
-   Return the result synchronously:
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    
    function kdfSync() {
      let spec: cryptoFramework.PBKDF2Spec = {
        algName: 'PBKDF2',
        password: '123456',
        salt: new Uint8Array(16),
        iterations: 10000,
        keySize: 32
      };
      let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');
      let secret = kdf.generateSecretSync(spec);
      console.info("\[Sync\]key derivation output is " + secret.data);
    }
