# Key Derivation Using HKDF (ArkTS)

For details about the corresponding algorithm specifications, see [HKDF](../key-derivation-overview-and-algorithm-specifications/document.md#hkdf).

#### How to Develop

1.  Create a [HKDFSpec](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#hkdfspec12) object and use it as a parameter for key derivation.
    
    **HKDFSpec** is a child class of [KdfSpec](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#kdfspec11). You need to specify the following:
    
    -   **algName**: algorithm to use, which is **'HKDF'**.
        
    -   **key**: original key material.
        
        If **key** is of the string type, pass in the data used for key derivation instead of the string type such as HexString or base64. In addition, ensure that the string is encoded in UTF-8 format. Otherwise, the derived key may be different from what you expected.
        
    -   **salt**: salt value.
        
    -   **info**: optional context and application information used to extend the short key. This parameter can be empty.
        
    -   **keySize**: length of the key to derive, in bytes. The value must be a positive integer.
        
2.  Call [cryptoFramework.createKdf](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreatekdf11) with the string parameter **'HKDF|SHA256|EXTRACT\_AND\_EXPAND'** to create a key derivation function object (**Kdf**). The key derivation algorithm is **HKDF**, HMAC algorithm is **SHA256**, and mode is **EXTRACT\_AND\_EXPAND**.
    
3.  Call [Kdf.generateSecret](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#generatesecret11) with the **HKDFSpec** object to generate a derived key.
    
    The following table lists how **Kdf.generateSecret** delivers the return value.
    
    | API | Return Mode |
    | :-- | :-- |
    | generateSecret(params: KdfSpec, callback: AsyncCallback<DataBlob>): void | This API uses an asynchronous callback to return the result. |
    | generateSecret(params: KdfSpec): Promise<DataBlob> | This API uses a promise to return the result. |
    | generateSecretSync(params: KdfSpec): DataBlob | This API returns the result synchronously. |
    

-   Return the result using **await**:
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    import { buffer } from '@kit.ArkTS';
    
    async function kdfAwait() {
      let keyData = new Uint8Array(buffer.from("012345678901234567890123456789", "utf-8").buffer);
      let saltData = new Uint8Array(buffer.from("0123456789", "utf-8").buffer);
      let infoData = new Uint8Array(buffer.from("infostring", "utf-8").buffer);
      let spec: cryptoFramework.HKDFSpec = {
        algName: 'HKDF',
        key: keyData,
        salt: saltData,
        info: infoData,
        keySize: 32
      };
      let kdf = cryptoFramework.createKdf('HKDF|SHA256|EXTRACT\_AND\_EXPAND');
      let secret = await kdf.generateSecret(spec);
      console.info("key derivation output is " + secret.data);
    }
    
-   Return the result using a promise:
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { buffer } from '@kit.ArkTS';
    
    function kdfPromise() {
      let keyData = new Uint8Array(buffer.from("012345678901234567890123456789", "utf-8").buffer);
      let saltData = new Uint8Array(buffer.from("0123456789", "utf-8").buffer);
      let infoData = new Uint8Array(buffer.from("infostring", "utf-8").buffer);
      let spec: cryptoFramework.HKDFSpec = {
        algName: 'HKDF',
        key: keyData,
        salt: saltData,
        info: infoData,
        keySize: 32
      };
      let kdf = cryptoFramework.createKdf('HKDF|SHA256|EXTRACT\_AND\_EXPAND');
      let kdfPromise = kdf.generateSecret(spec);
      kdfPromise.then((secret) => {
        console.info("key derivation output is " + secret.data);
      }).catch((error: BusinessError) => {
        console.error("key derivation error.");
      });
    }
    
-   Return the result synchronously:
    
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    import { buffer } from '@kit.ArkTS';
    
    function kdfSync() {
      let keyData = new Uint8Array(buffer.from("012345678901234567890123456789", "utf-8").buffer);
      let saltData = new Uint8Array(buffer.from("0123456789", "utf-8").buffer);
      let infoData = new Uint8Array(buffer.from("infostring", "utf-8").buffer);
      let spec: cryptoFramework.HKDFSpec = {
        algName: 'HKDF',
        key: keyData,
        salt: saltData,
        info: infoData,
        keySize: 32
      };
      let kdf = cryptoFramework.createKdf('HKDF|SHA256|EXTRACT\_AND\_EXPAND');
      let secret = kdf.generateSecretSync(spec);
      console.info("\[Sync\]key derivation output is " + secret.data);
    }
