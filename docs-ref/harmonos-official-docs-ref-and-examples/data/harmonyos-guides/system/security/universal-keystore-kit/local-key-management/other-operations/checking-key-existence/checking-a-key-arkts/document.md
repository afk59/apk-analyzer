# Checking a Key (ArkTS)

Check whether a key exists.

#### How to Develop

1.  Specify the key alias. For details about the naming rules, see [Key Generation Overview and Algorithm Specifications](../../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md).
    
2.  Initialize the key property set to specify [the property tags of keys](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#hukstag). When a single key is queried, **TAG** can be empty.
    
3.  Use [hasKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#hukshaskeyitem11) to check whether the key exists.
    

import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'test\_key';
let isKeyExist: Boolean;

let generateProperties: huks.HuksParam\[\] = \[
  {
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_DH
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_AGREE
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_DH\_KEY\_SIZE\_2048
  }
\];

let generateHuksOptions: huks.HuksOptions = {
  properties: generateProperties,
  inData: new Uint8Array(\[\])
}

/\* 1. Generate a key. \*/
function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  return new Promise<void>((resolve, reject) => {
    try {
      huks.generateKeyItem(keyAlias, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throw (error as Error);
    }
  });
}

async function generateKey(keyAlias: string, huksOptions: huks.HuksOptions): Promise<void> {
  console.info(\`enter promise generateKeyItem\`);
  await generateKeyItem(keyAlias, huksOptions);
  console.info(\`promise: generateKeyItem success\`);
}

/\* 2. Check whether the key exists. \*/
let huksOptions: huks.HuksOptions = {
  properties: \[\]
}

function hasKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  return new Promise<boolean>((resolve, reject) => {
    try {
      huks.hasKeyItem(keyAlias, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data.valueOf());
        }
      });
    } catch (error) {
      throw (error as Error);
    }
  });
}

async function checkKeyExistence(keyAlias: string, huksOptions: huks.HuksOptions): Promise<boolean> {
  console.info(\`enter promise hasKeyItem\`);
  const exists = await hasKeyItem(keyAlias, huksOptions);
  console.info(\`promise: hasKeyItem success, isKeyExist = ${exists}\`);
  return exists;
}

async function executeCheckKey(): Promise<string> {
  try {
    /\* 1. Generate a key. \*/
    await generateKey(keyAlias, generateHuksOptions);

    /\* 2. Check whether the key exists. \*/
    isKeyExist = await checkKeyExistence(keyAlias, huksOptions);

    console.info(\`Key check completed, isKeyExist = ${isKeyExist}\`);
    return 'Success';
  } catch (error) {
    console.error(\`Key check failed: ${JSON.stringify(error)}\`);
    return 'Failed';
  }
}
