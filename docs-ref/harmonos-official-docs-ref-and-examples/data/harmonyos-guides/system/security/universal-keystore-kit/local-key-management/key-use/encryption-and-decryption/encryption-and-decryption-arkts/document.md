# Encryption and Decryption (ArkTS)

This topic uses AES-128, RSA-2048, and SM2 as examples to describe the encryption and decryption workflows. For details about the scenarios and supported algorithms, see [Supported Algorithms](../encryption-and-decryption-overview-and-algorithm-specifications/document.md#supported-algorithms).

#### How to Develop

**Key Generation**

1.  Specify the key alias. For details about the naming rules, see [Key Generation Overview and Algorithm Specifications](../../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md).
    
2.  Initialize the key property set.
    
3.  Use [generateKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksgeneratekeyitem9) to generate a key. For details, see [Key Generation](../../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md).
    

Alternatively, you can [import a key](../../../key-generation-and-import/key-import/key-import-overview-and-algorithm-specifications/document.md).

**Encryption**

1.  Obtain the key alias.
    
2.  Obtain the data to be encrypted.
    
3.  Use [HuksParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksparam) to set encryption algorithm parameters.
    
    The parameters to be configured vary with the algorithm used.
    
    -   If the AES algorithm is used for encryption, the block mode is CBC, and the padding mode is PKCS7, the **IV** parameter is mandatory. For details, see [AES/CBC/PKCS7](#aescbcpkcs7).
    -   If the AES algorithm is used for encryption and the block mode is GCM, the **NONCE** and **AAD** parameters are optional. For details, see [AES/GCM/NoPadding](#aesgcmnopadding).
    -   If the AES algorithm is used for encryption and the block mode is CCM, the **NONCE** and **AAD** parameters are optional. For details, see [AES/CCM/NoPadding](#aesccmnopadding).
    -   If the RSA algorithm is used for encryption, the corresponding block mode, padding mode, and digest algorithm must be selected. For details, see [RSA/ECB/PKCS1\_V1\_5](#rsaecbpkcs1_v1_5) and [RSA/ECB/OAEP/SHA256](#rsaecboaepsha256).
    -   If the SM2 algorithm is used for encryption, the digest algorithm must be SM3. For details, see [SM2](#sm2).
    
    For details about the specifications, see [Encryption and Decryption Overview and Algorithm Specifications](../encryption-and-decryption-overview-and-algorithm-specifications/document.md).
    
4.  Use [initSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksinitsession9) to initialize a key session. The session handle is returned after the initialization.
    
5.  Use [finishSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksfinishsession9) with the session handle to obtain the ciphertext.
    

**Decryption**

1.  Obtain the key alias.
    
2.  Obtain the ciphertext to be decrypted.
    
3.  Use [HuksParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksparam) to set decryption algorithm parameters.
    
    The parameters to be configured vary with the algorithm used.
    
    -   If the AES algorithm and GCM block mode are used for decryption, **NONCE** and **AEAD** are mandatory and **AAD** is optional. For details, see [AES/GCM/NoPadding](#aesgcmnopadding).
    -   The requirements for the parameters in the other development cases are the same as those in the encryption.
    
    For details about the specifications, see [Encryption and Decryption Overview and Algorithm Specifications](../encryption-and-decryption-overview-and-algorithm-specifications/document.md).
    
4.  Use [initSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksinitsession9) to initialize a key session. The session handle is returned after the initialization.
    
5.  Use [finishSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksfinishsession9) to obtain the data decrypted.
    

**Key Deletion**

Use [deleteKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksdeletekeyitem9) to delete the key that is not required. For details, see [Deleting a Key](../../../key-deletion/deleting-a-key-arkts/document.md).

#### Development Cases

## AES/CBC/PKCS7

/\*
 \* The following uses AES/CBC/PKCS7 with promise-based APIs.
 \*/
import { huks } from '@kit.UniversalKeystoreKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from "@kit.BasicServicesKit";

let aesKeyAlias = 'test\_aesKeyAlias';
let handle: number;
let plainText = '123456';
let IV = cryptoFramework.createRandom().generateRandomSync(12).data;
let cipherData: Uint8Array;

function StringToUint8Array(str: string) {
  let arr: number\[\] = new Array();
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function Uint8ArrayToString(fileData: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < fileData.length; i++) {
    dataString += String.fromCharCode(fileData\[i\]);
  }
  return dataString;
}

function GetAesGenerateProperties() {
  let properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_AES
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_128
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT |
    huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT
  }\];
  return properties;
}

function GetAesEncryptProperties() {
  let properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_AES
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_128
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PADDING,
    value: huks.HuksKeyPadding.HUKS\_PADDING\_PKCS7
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_CBC
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_IV,
    value: IV
  }\];
  return properties;
}

function GetAesDecryptProperties() {
  let properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_AES
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_128
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PADDING,
    value: huks.HuksKeyPadding.HUKS\_PADDING\_PKCS7
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_CBC
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_IV,
    value: IV
  }\];
  return properties;
}

async function GenerateAesKey() {
  /\*
   \* Simulate the key generation scenario.
   \* 1. Set the key alias.
   \*/
  /\*
   \* 2. Obtain the parameters for key generation.
   \*/
  let genProperties = GetAesGenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  }
  /\*
   \* 3. Call generateKeyItem.
   \*/
  await huks.generateKeyItem(aesKeyAlias, options)
    .then(() => {
      console.info(\`promise: generate AES Key success\`);
    }).catch((error: BusinessError) => {
      console.error(\`promise: generate AES Key failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function EncryptData() {
  /\*
   \* Simulate the encryption scenario.
   \* 1. Obtain the key alias.
   \*/
  /\*
   \* 2. Obtain the data to be encrypted.
   \*/
  /\*
   \* 3. Obtain the algorithm parameters for encryption.
   \*/
  let encryptProperties = GetAesEncryptProperties();
  let options: huks.HuksOptions = {
    properties: encryptProperties,
    inData: StringToUint8Array(plainText)
  }
  /\*
   \* 4. Call initSession to obtain a session handle.
   \*/
  await huks.initSession(aesKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(\`promise: init EncryptData failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
  /\*
   \* 5. Call finishSession to obtain the ciphertext.
   \*/
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(\`promise: encrypt data success, data is \` + Uint8ArrayToString(data.outData as Uint8Array));
      cipherData = data.outData as Uint8Array;
    }).catch((error: BusinessError) => {
      console.error(\`promise: encrypt data failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function DecryptData() {
  /\*
   \* Simulate the decryption scenario.
   \* 1. Obtain the key alias.
   \*/
  /\*
   \* 2. Obtain the ciphertext to be decrypted.
   \*/
  /\*
   \* 3. Obtain the algorithm parameters for decryption.
   \*/
  let decryptOptions = GetAesDecryptProperties()
  let options: huks.HuksOptions = {
    properties: decryptOptions,
    inData: cipherData
  }
  /\*
   \* 4. Call initSession to obtain a session handle.
   \*/
  await huks.initSession(aesKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(\`promise: init DecryptData failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
  /\*
   \* 5. Call finishSession to obtain the decrypted data.
   \*/
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(\`promise: decrypt data success, data is \` + Uint8ArrayToString(data.outData as Uint8Array));
    }).catch((error: BusinessError) => {
      console.error(\`promise: decrypt data failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function DeleteKey() {
  /\*
   \* Simulate the key deletion scenario.
   \* 1. Obtain the key alias.
   \*/
  let emptyOptions: huks.HuksOptions = {
    properties: \[\]
  }
  /\*
   \* 2. Call deleteKeyItem to delete the key.
   \*/
  await huks.deleteKeyItem(aesKeyAlias, emptyOptions)
    .then(() => {
      console.info(\`promise: delete data success\`);
    }).catch((error: BusinessError) => {
      console.error(\`promise: delete data failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function TestEncryptDecrypt() {
  await GenerateAesKey();
  await EncryptData();
  await DecryptData();
  await DeleteKey();
}

## AES/GCM/NoPadding

/\*
 \* The following uses AES/GCM/NoPadding with promise-based APIs.
 \*/
import { huks } from '@kit.UniversalKeystoreKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from "@kit.BasicServicesKit";

let aesKeyAlias = 'test\_aesKeyAlias';
let handle: number;
let plainText = '123456';
let cipherData: Uint8Array;
let AAD = '1234567890123456';
let NONCE = cryptoFramework.createRandom().generateRandomSync(12).data;

function StringToUint8Array(str: string) {
  let arr: number\[\] = new Array();
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function Uint8ArrayToString(fileData: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < fileData.length; i++) {
    dataString += String.fromCharCode(fileData\[i\]);
  }
  return dataString;
}

function GetAesGenerateProperties() {
  let properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_AES
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_128
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT |
    huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT
  }\];
  return properties;
}

function GetAesGcmEncryptProperties() {
  let properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_AES
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_128
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PADDING,
    value: huks.HuksKeyPadding.HUKS\_PADDING\_NONE
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_GCM
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_NONCE,
    value: NONCE
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_ASSOCIATED\_DATA,
    value: StringToUint8Array(AAD)
  }\];
  return properties;
}

function GetAesGcmDecryptProperties(cipherData: Uint8Array) {
  let properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_AES
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_128
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PADDING,
    value: huks.HuksKeyPadding.HUKS\_PADDING\_NONE
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_GCM
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_NONCE,
    value: NONCE
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_ASSOCIATED\_DATA,
    value: StringToUint8Array(AAD)
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_AE\_TAG,
    value: cipherData.slice(cipherData.length - 16)
  }\];
  return properties;
}

async function GenerateAesKey() {
  /\*
   \* Simulate the key generation scenario.
   \* 1. Set the key alias.
   \*/
  /\*
   \* 2. Obtain the parameters for key generation.
   \*/
  let genProperties = GetAesGenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  }
  /\*
   \* 3. Call generateKeyItem.
   \*/
  await huks.generateKeyItem(aesKeyAlias, options)
    .then(() => {
      console.info(\`promise: generate AES Key success\`);
    }).catch((error: BusinessError) => {
      console.error(\`promise: generate AES Key failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function EncryptData() {
  /\*
   \* Simulate the encryption scenario.
   \* 1. Obtain the key alias.
   \*/
  /\*
   \* 2. Obtain the data to be encrypted.
   \*/
  /\*
   \* 3. Obtain the algorithm parameters for encryption.
   \*/
  let encryptProperties = GetAesGcmEncryptProperties();
  let options: huks.HuksOptions = {
    properties: encryptProperties,
    inData: StringToUint8Array(plainText)
  }
  /\*
   \* 4. Call initSession to obtain a session handle.
   \*/
  await huks.initSession(aesKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(\`promise: init EncryptDataGcm failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
  /\*
   \* 5. Call finishSession to obtain the ciphertext.
   \*/
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(\`promise: encrypt data success, data is \` + Uint8ArrayToString(data.outData as Uint8Array));
      cipherData = data.outData as Uint8Array;
    }).catch((error: BusinessError) => {
      console.error(\`promise: encrypt data failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function DecryptData() {
  /\*
   \* Simulate the decryption scenario.
   \* 1. Obtain the key alias.
   \*/
  /\*
   \* 2. Obtain the ciphertext to be decrypted.
   \*/
  /\*
   \* 3. Obtain the algorithm parameters for decryption.
   \*/
  let decryptOptions = GetAesGcmDecryptProperties(cipherData)
  let options: huks.HuksOptions = {
    properties: decryptOptions,
    inData: cipherData.slice(0, cipherData.length - 16)
  }
  /\*
   \* 4. Call initSession to obtain a session handle.
   \*/
  await huks.initSession(aesKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(\`promise: init DecryptDataGcm failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
  /\*
   \* 5. Call finishSession to obtain the decrypted data.
   \*/
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(\`promise: decrypt data success, data is \` + Uint8ArrayToString(data.outData as Uint8Array));
    }).catch((error: BusinessError) => {
      console.error(\`promise: decrypt data failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function DeleteKey() {
  /\*
   \* Simulate the key deletion scenario.
   \* 1. Obtain the key alias.
   \*/
  let emptyOptions: huks.HuksOptions = {
    properties: \[\]
  }
  /\*
   \* 2. Call deleteKeyItem to delete the key.
   \*/
  await huks.deleteKeyItem(aesKeyAlias, emptyOptions)
    .then(() => {
      console.info(\`promise: delete data success\`);
    }).catch((error: BusinessError) => {
      console.error(\`promise: delete data failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function TestEncryptDecrypt() {
  await GenerateAesKey();
  await EncryptData();
  await DecryptData();
  await DeleteKey();
}

## AES/CCM/NoPadding

/\*
 \* The following uses AES/CCM/NoPadding with promise-based APIs as an example.
 \*/
import { huks } from '@kit.UniversalKeystoreKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from "@kit.BasicServicesKit";

let aesKeyAlias = 'test\_aesCcmKeyAlias';
let handle: number;
let plainText = '123456';
let cipherData: Uint8Array;
let AAD = '1234567890123456';
let NONCE = cryptoFramework.createRandom().generateRandomSync(12).data;
let aeadTagLen = 14;

function StringToUint8Array(str: string) {
  let arr: number\[\] = new Array();
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function Uint8ArrayToString(fileData: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < fileData.length; i++) {
    dataString += String.fromCharCode(fileData\[i\]);
  }
  return dataString;
}

function GetAesGenerateProperties() {
  let properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_AES
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_128
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT |
    huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT
  }\];
  return properties;
}

function GetAesCcmEncryptProperties() {
  let properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_AES
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_128
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PADDING,
    value: huks.HuksKeyPadding.HUKS\_PADDING\_NONE
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_CCM
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_NONCE,
    value: NONCE
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_ASSOCIATED\_DATA,
    value: StringToUint8Array(AAD)
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_AE\_TAG\_LEN,
    value: aeadTagLen
  }\];
  return properties;
}

function GetAesCcmDecryptProperties(cipherData: Uint8Array) {
  let properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_AES
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_128
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PADDING,
    value: huks.HuksKeyPadding.HUKS\_PADDING\_NONE
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_CCM
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_NONCE,
    value: NONCE
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_ASSOCIATED\_DATA,
    value: StringToUint8Array(AAD)
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_AE\_TAG,
    value: cipherData.slice(cipherData.length - aeadTagLen)
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_AE\_TAG\_LEN,
    value: aeadTagLen
  }\];
  return properties;
}

async function GenerateAesKey() {
  /\*
   \* Simulate the key generation scenario.
   \* 1. Set the key alias.
   \*/
  /\*
   \* 2. Obtain the parameters for key generation.
   \*/
  let genProperties = GetAesGenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  }
  /\*
   \* 3. Call generateKeyItem.
   \*/
  await huks.generateKeyItem(aesKeyAlias, options)
    .then(() => {
      console.info(\`promise: generate AES Key success\`);
    }).catch((error: BusinessError) => {
      console.error(\`promise: generate AES Key failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function EncryptData() {
  /\*
   \* Simulate the encryption scenario.
   \* 1. Obtain the key alias.
   \*/
  /\*
   \* 2. Obtain the data to be encrypted.
   \*/
  /\*
   \* 3. Obtain the algorithm parameters for encryption.
   \*/
  let encryptProperties = GetAesCcmEncryptProperties();
  let options: huks.HuksOptions = {
    properties: encryptProperties,
    inData: StringToUint8Array(plainText)
  }
  /\*
   \* 4. Call initSession to obtain a session handle.
   \*/
  await huks.initSession(aesKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(\`promise: init EncryptDataCcm failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
  /\*
   \* 5. Call finishSession to obtain the ciphertext.
   \*/
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(\`promise: encrypt data success, data is \` + Uint8ArrayToString(data.outData as Uint8Array));
      cipherData = data.outData as Uint8Array;
    }).catch((error: BusinessError) => {
      console.error(\`promise: encrypt data failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function DecryptData() {
  /\*
   \* Simulate the decryption scenario.
   \* 1. Obtain the key alias.
   \*/
  /\*
   \* 2. Obtain the ciphertext to be decrypted.
   \*/
  /\*
   \* 3. Obtain the algorithm parameters for decryption.
   \*/
  let decryptOptions = GetAesCcmDecryptProperties(cipherData)
  let options: huks.HuksOptions = {
    properties: decryptOptions,
    inData: cipherData.slice(0, cipherData.length - aeadTagLen)
  }
  /\*
   \* 4. Call initSession to obtain a session handle.
   \*/
  await huks.initSession(aesKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(\`promise: init DecryptDataCcm failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
  /\*
   \* 5. Call finishSession to obtain the decrypted data.
   \*/
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(\`promise: decrypt data success, data is \` + Uint8ArrayToString(data.outData as Uint8Array));
    }).catch((error: BusinessError) => {
      console.error(\`promise: decrypt data failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function DeleteKey() {
  /\*
   \* Simulate the key deletion scenario.
   \* 1. Obtain the key alias.
   \*/
  let emptyOptions: huks.HuksOptions = {
    properties: \[\]
  }
  /\*
   \* 2. Call deleteKeyItem to delete the key.
   \*/
  await huks.deleteKeyItem(aesKeyAlias, emptyOptions)
    .then(() => {
      console.info(\`promise: delete data success\`);
    }).catch((error: BusinessError) => {
      console.error(\`promise: delete data failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function TestEncryptDecrypt() {
  await GenerateAesKey();
  await EncryptData();
  await DecryptData();
  await DeleteKey();
}

## RSA/ECB/PKCS1\_V1\_5

/\*
 \* The following uses RSA/ECB/PKCS1\_V1\_5 with promise-based APIs.
 \*/
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from "@kit.BasicServicesKit";

let rsaKeyAlias = 'test\_rsaKeyAlias';
let handle: number;
let plainText = '123456';
let cipherData: Uint8Array;

function StringToUint8Array(str: string) {
  let arr: number\[\] = new Array();
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function Uint8ArrayToString(fileData: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < fileData.length; i++) {
    dataString += String.fromCharCode(fileData\[i\]);
  }
  return dataString;
}

function GetRsaGenerateProperties() {
  let properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_RSA
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_RSA\_KEY\_SIZE\_2048
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT |
    huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT
  }\];
  return properties;
}

function GetRsaEncryptProperties() {
  let properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_RSA
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_RSA\_KEY\_SIZE\_2048
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PADDING,
    value: huks.HuksKeyPadding.HUKS\_PADDING\_PKCS1\_V1\_5
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_ECB
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
    value: huks.HuksKeyDigest.HUKS\_DIGEST\_NONE
  }\];
  return properties;
}

function GetRsaDecryptProperties() {
  let properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_RSA
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_RSA\_KEY\_SIZE\_2048
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PADDING,
    value: huks.HuksKeyPadding.HUKS\_PADDING\_PKCS1\_V1\_5
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_ECB
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
    value: huks.HuksKeyDigest.HUKS\_DIGEST\_NONE
  }\];
  return properties;
}

async function GenerateRsaKey() {
  /\*
   \* Simulate the key generation scenario.
   \* 1. Set the key alias.
   \*/
  /\*
   \* 2. Obtain the parameters for key generation.
   \*/
  let genProperties = GetRsaGenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  }
  /\*
   \* 3. Call generateKeyItem.
   \*/
  await huks.generateKeyItem(rsaKeyAlias, options)
    .then(() => {
      console.info(\`promise: generate RSA Key success\`);
    }).catch((error: BusinessError) => {
      console.error(\`promise: generate RSA Key failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function EncryptData() {
  /\*
   \* Simulate the encryption scenario.
   \* 1. Obtain the key alias.
   \*/
  /\*
   \* 2. Obtain the data to be encrypted.
   \*/
  /\*
   \* 3. Obtain the algorithm parameters for encryption.
   \*/
  let encryptProperties = GetRsaEncryptProperties();
  let options: huks.HuksOptions = {
    properties: encryptProperties,
    inData: StringToUint8Array(plainText)
  }
  /\*
   \* 4. Call initSession to obtain a session handle.
   \*/
  await huks.initSession(rsaKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(\`promise: init EncryptDataRsa failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
  /\*
   \* 5. Call finishSession to obtain the ciphertext.
   \*/
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(\`promise: encrypt data success, data is \` + Uint8ArrayToString(data.outData as Uint8Array));
      cipherData = data.outData as Uint8Array;
    }).catch((error: BusinessError) => {
      console.error(\`promise: encrypt data failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function DecryptData() {
  /\*
   \* Simulate the decryption scenario.
   \* 1. Obtain the key alias.
   \*/
  /\*
   \* 2. Obtain the ciphertext to be decrypted.
   \*/
  /\*
   \* 3. Obtain the algorithm parameters for decryption.
   \*/
  let decryptOptions = GetRsaDecryptProperties()
  let options: huks.HuksOptions = {
    properties: decryptOptions,
    inData: cipherData
  }
  /\*
   \* 4. Call initSession to obtain a session handle.
   \*/
  await huks.initSession(rsaKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(\`promise: init DecryptDataRsa failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
  /\*
   \* 5. Call finishSession to obtain the decrypted data.
   \*/
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(\`promise: decrypt data success, data is \` + Uint8ArrayToString(data.outData as Uint8Array));
    }).catch((error: BusinessError) => {
      console.error(\`promise: decrypt data failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function DeleteKey() {
  /\*
   \* Simulate the key deletion scenario.
   \* 1. Obtain the key alias.
   \*/
  let emptyOptions: huks.HuksOptions = {
    properties: \[\]
  }
  /\*
   \* 2. Call deleteKeyItem to delete the key.
   \*/
  await huks.deleteKeyItem(rsaKeyAlias, emptyOptions)
    .then(() => {
      console.info(\`promise: delete data success\`);
    }).catch((error: BusinessError) => {
      console.error(\`promise: delete data failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function TestEncryptDecrypt()
{
  await GenerateRsaKey();
  await EncryptData();
  await DecryptData();
  await DeleteKey();
}

## RSA/ECB/OAEP/SHA256

/\*
 \* The following uses RSA/ECB/OAEP/SHA-256 with promise-based APIs.
 \*/
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from "@kit.BasicServicesKit";

let rsaKeyAlias = 'test\_rsaKeyAlias';
let handle: number;
let plainText = '123456';
let cipherData: Uint8Array;

function StringToUint8Array(str: string) {
  let arr: number\[\] = new Array();
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function Uint8ArrayToString(fileData: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < fileData.length; i++) {
    dataString += String.fromCharCode(fileData\[i\]);
  }
  return dataString;
}

function GetRsaGenerateProperties() {
  let properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_RSA
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_RSA\_KEY\_SIZE\_2048
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT |
    huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT
  }\];
  return properties;
}

function GetRsaEncryptProperties() {
  let properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_RSA
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_RSA\_KEY\_SIZE\_2048
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PADDING,
    value: huks.HuksKeyPadding.HUKS\_PADDING\_OAEP
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_ECB
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
    value: huks.HuksKeyDigest.HUKS\_DIGEST\_SHA256
  }\];
  return properties;
}

function GetRsaDecryptProperties() {
  let properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_RSA
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_RSA\_KEY\_SIZE\_2048
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PADDING,
    value: huks.HuksKeyPadding.HUKS\_PADDING\_OAEP
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_ECB
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
    value: huks.HuksKeyDigest.HUKS\_DIGEST\_SHA256
  }\];
  return properties;
}

async function GenerateRsaKey() {
  /\*
   \* Simulate the key generation scenario.
   \* 1. Set the key alias.
   \*/
  /\*
   \* 2. Obtain the parameters for key generation.
   \*/
  let genProperties = GetRsaGenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  }
  /\*
   \* 3. Call generateKeyItem.
   \*/
  await huks.generateKeyItem(rsaKeyAlias, options)
    .then(() => {
      console.info(\`promise: generate RSA Key success\`);
    }).catch((error: BusinessError) => {
      console.error(\`promise: generate RSA Key failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function EncryptData() {
  /\*
   \* Simulate the encryption scenario.
   \* 1. Obtain the key alias.
   \*/
  /\*
   \* 2. Obtain the data to be encrypted.
   \*/
  /\*
   \* 3. Obtain the algorithm parameters for encryption.
   \*/
  let encryptProperties = GetRsaEncryptProperties();
  let options: huks.HuksOptions = {
    properties: encryptProperties,
    inData: StringToUint8Array(plainText)
  }
  /\*
   \* 4. Call initSession to obtain a session handle.
   \*/
  await huks.initSession(rsaKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(\`promise: init EncryptDataRsa failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
  /\*
   \* 5. Call finishSession to obtain the ciphertext.
   \*/
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(\`promise: encrypt data success, data is \` + Uint8ArrayToString(data.outData as Uint8Array));
      cipherData = data.outData as Uint8Array;
    }).catch((error: BusinessError) => {
      console.error(\`promise: encrypt data failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function DecryptData() {
  /\*
   \* Simulate the decryption scenario.
   \* 1. Obtain the key alias.
   \*/
  /\*
   \* 2. Obtain the ciphertext to be decrypted.
   \*/
  /\*
   \* 3. Obtain the algorithm parameters for decryption.
   \*/
  let decryptOptions = GetRsaDecryptProperties()
  let options: huks.HuksOptions = {
    properties: decryptOptions,
    inData: cipherData
  }
  /\*
   \* 4. Call initSession to obtain a session handle.
   \*/
  await huks.initSession(rsaKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(\`promise: init DecryptDataRsa failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
  /\*
   \* 5. Call finishSession to obtain the decrypted data.
   \*/
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(\`promise: decrypt data success, data is \` + Uint8ArrayToString(data.outData as Uint8Array));
    }).catch((error: BusinessError) => {
      console.error(\`promise: decrypt data failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function DeleteKey() {
  /\*
   \* Simulate the key deletion scenario.
   \* 1. Obtain the key alias.
   \*/
  let emptyOptions: huks.HuksOptions = {
    properties: \[\]
  }
  /\*
   \* 2. Call deleteKeyItem to delete the key.
   \*/
  await huks.deleteKeyItem(rsaKeyAlias, emptyOptions)
    .then((data) => {
      console.info(\`promise: delete data success\`);
    }).catch((error: BusinessError) => {
      console.error(\`promise: delete data failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function TestEncryptDecrypt() {
  await GenerateRsaKey();
  await EncryptData();
  await DecryptData();
  await DeleteKey();
}

## SM2

/\*
 \* The following uses SM2 with promise-based APIs.
 \*/
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from "@kit.BasicServicesKit";

let sm2KeyAlias = 'test\_sm2KeyAlias';
let handle: number;
let plainText = '123456';
let cipherData: Uint8Array;

function StringToUint8Array(str: string) {
  let arr: number\[\] = new Array();
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function Uint8ArrayToString(fileData: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < fileData.length; i++) {
    dataString += String.fromCharCode(fileData\[i\]);
  }
  return dataString;
}

function GetSm2GenerateProperties() {
  let properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_SM2
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_SM2\_KEY\_SIZE\_256
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT |
    huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT
  }\];
  return properties;
}

function GetSm2EncryptProperties() {
  let properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_SM2
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_SM2\_KEY\_SIZE\_256
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
    value: huks.HuksKeyDigest.HUKS\_DIGEST\_SM3
  }\];
  return properties;
}

function GetSm2DecryptProperties() {
  let properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_SM2
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_SM2\_KEY\_SIZE\_256
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
    value: huks.HuksKeyDigest.HUKS\_DIGEST\_SM3
  }\];
  return properties;
}

async function GenerateSm2Key() {
  /\*
   \* Simulate the key generation scenario.
   \* 1. Set the key alias.
   \*/
  /\*
   \* 2. Obtain the parameters for key generation.
   \*/
  let genProperties = GetSm2GenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  }
  /\*
   \* 3. Call generateKeyItem.
   \*/
  await huks.generateKeyItem(sm2KeyAlias, options)
    .then(() => {
      console.info(\`promise: generate SM2 Key success\`);
    }).catch((error: BusinessError) => {
      console.error(\`promise: generate SM2 Key failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function EncryptDataSm2() {
  /\*
   \* Simulate the encryption scenario.
   \* 1. Obtain the key alias.
   \*/
  /\*
   \* 2. Obtain the data to be encrypted.
   \*/
  /\*
   \* 3. Obtain the algorithm parameters for encryption.
   \*/
  let encryptProperties = GetSm2EncryptProperties();
  let options: huks.HuksOptions = {
    properties: encryptProperties,
    inData: StringToUint8Array(plainText)
  }
  /\*
   \* 4. Call initSession to obtain a session handle.
   \*/
  await huks.initSession(sm2KeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(\`promise: init EncryptDataSm2 failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
  /\*
   \* 5. Call finishSession to obtain the ciphertext.
   \*/
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(\`promise: encrypt data success, data is \` + Uint8ArrayToString(data.outData as Uint8Array));
      cipherData = data.outData as Uint8Array;
    }).catch((error: BusinessError) => {
      console.error(\`promise: encrypt data failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function DecryptDataSm2() {
  /\*
   \* Simulate the decryption scenario.
   \* 1. Obtain the key alias.
   \*/
  /\*
   \* 2. Obtain the ciphertext to be decrypted.
   \*/
  /\*
   \* 3. Obtain the algorithm parameters for decryption.
   \*/
  let decryptOptions = GetSm2DecryptProperties()
  let options: huks.HuksOptions = {
    properties: decryptOptions,
    inData: cipherData
  }
  /\*
   \* 4. Call initSession to obtain a session handle.
   \*/
  await huks.initSession(sm2KeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(\`promise: init DecryptDataSm2 failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
  /\*
   \* 5. Call finishSession to obtain the decrypted data.
   \*/
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(\`promise: decrypt data success, data is \` + Uint8ArrayToString(data.outData as Uint8Array));
    }).catch((error: BusinessError) => {
      console.error(\`promise: decrypt data failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function DeleteKey() {
  /\*
   \* Simulate the key deletion scenario.
   \* 1. Obtain the key alias.
   \*/
  let emptyOptions: huks.HuksOptions = {
    properties: \[\]
  }
  /\*
   \* 2. Call deleteKeyItem to delete the key.
   \*/
  await huks.deleteKeyItem(sm2KeyAlias, emptyOptions)
    .then(() => {
      console.info(\`promise: delete data success\`);
    }).catch((error: BusinessError) => {
      console.error(\`promise: delete data failed, errCode : ${error.code}, errMsg : ${error.message}\`);
    })
}

async function TestEncryptDecrypt() {
  await GenerateSm2Key();
  await EncryptDataSm2();
  await DecryptDataSm2();
  await DeleteKey();
}
