# Deleting a Key (ArkTS)

To ensure data security, delete the key that is no longer required.

#### How to Develop

For example, delete a 256-bit HKDF key.

1.  Specify the key alias. For details about the naming rules, see [Key Generation Overview and Algorithm Specifications](../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md).
    
2.  Initialize the key property set to specify the properties for deleting the key. If a single key or non-group key is deleted, this set can be left empty.
    
3.  Use [deleteKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksdeletekeyitem9) to delete the key.
    

/\*
 \* Delete a 256-bit HKDF key. This example uses promise-based APIs.
 \*/
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'test\_Key';

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
  try {
    await generateKeyItem(keyAlias, huksOptions);
    console.info(\`promise: generateKeyItem success\`);
  } catch (error) {
    console.error(\`promise: generateKeyItem failed, ${JSON.stringify(error)}\`);
  }
}

/\* 2. Delete the key. \*/
let deleteHuksOptions: huks.HuksOptions = {
  properties: \[\]
}

function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  return new Promise<void>((resolve, reject) => {
    try {
      huks.deleteKeyItem(keyAlias, huksOptions, (error, data) => {
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

async function deleteKey(keyAlias: string, huksOptions: huks.HuksOptions): Promise<void> {
  console.info(\`enter promise deleteKeyItem\`);
  try {
    await deleteKeyItem(keyAlias, huksOptions);
    console.info(\`promise: deleteKeyItem success\`);
  } catch (error) {
    console.error(\`promise: deleteKeyItem failed, ${JSON.stringify(error)}\`);
  }
}

async function executeKeyLifecycle(): Promise<string> {
  try {
    /\* 1. Generate a key. \*/
    console.info('start generateKey...');
    await generateKey(keyAlias, generateHuksOptions);
    console.info('end generateKey...');

    /\* 2. Delete the key. \*/
    console.info('start deleteKey...');
    await deleteKey(keyAlias, deleteHuksOptions);
    console.info('end deleteKey...');

    console.info('Key lifecycle completed successfully');
    return 'Success';
  } catch (error) {
    console.error(\`Key lifecycle failed: ${JSON.stringify(error)}\`);
    return 'Failed';
  }
}
