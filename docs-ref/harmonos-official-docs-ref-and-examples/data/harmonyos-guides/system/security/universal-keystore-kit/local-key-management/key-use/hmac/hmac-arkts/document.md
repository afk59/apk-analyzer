# HMAC (ArkTS)

Hash-based Message Authentication Code (HMAC) is a specific type of message authentication code (MAC) involving a cryptographic hash function and a secret cryptographic key. For details about the scenarios and supported algorithm specifications, see [HMAC Overview and Algorithm Specifications](../hmac-overview-and-algorithm-specifications/document.md).

#### How to Develop

**Key Generation**

1.  Specify the key alias. For details about the naming rules, see [Key Generation Overview and Algorithm Specifications](../../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md).
    
2.  Initialize the key property set.
    
3.  Use [generateKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksgeneratekeyitem9) to generate a key. For details about the HMAC specifications supported, see [Supported Algorithms](../../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md#supported-algorithms).
    

You can also import a key. For details about the supported algorithms, see [Supported Algorithms](../../../key-generation-and-import/key-import/key-import-overview-and-algorithm-specifications/document.md#supported-algorithms).

**HMAC Generation**

1.  Obtain the key alias.
    
2.  Obtains the data to be calculated.
    
3.  Use [initSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksinitsession9) to initialize a key session. The session handle is returned after the initialization.
    
4.  Use [finishSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksfinishsession9) to obtain the hashed data.
    

/\*
 \* Perform HMAC calculation using promise-based APIs.
 \*/
import { huks } from '@kit.UniversalKeystoreKit';

let hmacKeyAlias = 'test\_HMAC';
let handle: number;
let plainText = '123456';
let hashData: Uint8Array;

function stringToUint8Array(str: String) {
  let arr: number\[\] = \[\];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function uint8ArrayToString(fileData: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < fileData.length; i++) {
    dataString += String.fromCharCode(fileData\[i\]);
  }
  return dataString;
}

function getHMACProperties() {
  const properties: huks.HuksParam\[\] = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_HMAC
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_256
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_MAC
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
    value: huks.HuksKeyDigest.HUKS\_DIGEST\_SHA384,
  }\];
  return properties;
}

/\* 1. Generate an HMAC key. \*/
async function generateHMACKey() {
  let options: huks.HuksOptions = {
    properties: getHMACProperties()
  };

  await huks.generateKeyItem(hmacKeyAlias, options)
    .then((data) => {
      console.info(\`promise: generate HMAC Key success\`);
    }).catch((error: Error) => {
      console.error(\`promise: generate HMAC Key failed, ${JSON.stringify(error)}\`);
      throw (error as Error);
    })
}
/\* 2. Perform HMAC calculation. \*/
async function hMACData() {
  let options: huks.HuksOptions = {
    properties: getHMACProperties(),
    inData: stringToUint8Array(plainText)
  }

  await huks.initSession(hmacKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: Error) => {
      console.error(\`promise: init session failed, ${JSON.stringify(error)}\`);
      throw (error as Error);
    })

  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(\`promise: HMAC data success, data is \` + uint8ArrayToString(data.outData as Uint8Array));
      hashData = data.outData as Uint8Array;
    }).catch((error: Error) => {
      console.error(\`promise: HMAC data failed, ${JSON.stringify(error)}\`);
      throw (error as Error);
    })
}

async function executeHMAC() {
  await generateHMACKey();
  await hMACData();
}
