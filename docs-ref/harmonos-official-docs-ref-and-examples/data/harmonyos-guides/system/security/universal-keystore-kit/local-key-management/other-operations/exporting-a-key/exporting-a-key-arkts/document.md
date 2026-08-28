# Exporting a Key (ArkTS)

This topic walks you through on how to export the public key of a persistently stored asymmetric key. Currently, HUKS supports export of the ECC, RSA, Ed25519, X25519, and SM2 public keys.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/E8ydaSahQBelO_UXL7F_dQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062012Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A30FAE92A45A76D829E91C748DFC39027B3A530CF70484DF57F326AE0936A693)

Lite wearables support export of only the RSA public keys.

#### How to Develop

1.  Specify the key alias. For details about the naming rules, see [Key Generation Overview and Algorithm Specifications](../../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md).
    
2.  Use [exportKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksexportkeyitem9) to export the key based on the specified **keyAlias** and **options**. **options** is a reserved parameter and is left empty currently.
    
3.  In the [HuksReturnResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksreturnresult9) object returned, the public key is in the **outData** field in the DER format defined in X.509. For details about the format, see [Public Key Material Format](../../../basic-concepts-of-local-key-management/document.md#public-key-material-format).
    

import { huks } from '@kit.UniversalKeystoreKit';

/\* 1. Set the key alias. \*/
let keyAlias = 'keyAlias';
/\* Leave options empty. \*/
let emptyOptions: huks.HuksOptions = {
properties: \[\]
};

let properties1: huks.HuksParam\[\] = \[
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

let huksOptions: huks.HuksOptions = {
  properties: properties1,
  inData: new Uint8Array(\[\])
}

/\* 3. Generate a key. \*/
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

async function publicGenKeyFunc(keyAlias: string, huksOptions: huks.HuksOptions): Promise<string> {
  console.info(\`enter promise generateKeyItem\`);
  try {
    await generateKeyItem(keyAlias, huksOptions)
      .then((data) => {
        console.info(\`promise: generateKeyItem success, data = ${JSON.stringify(data)}\`);
      })
      .catch((error: Error) => {
        console.error(\`promise: generateKeyItem failed, ${JSON.stringify(error)}\`);
      });
    return 'Success';
  } catch (error) {
    console.error(\`promise: generateKeyItem input arg invalid, ${JSON.stringify(error)}\`);
    return 'Failed';
  }
}

async function testGenKey(): Promise<string> {
  let ret = await publicGenKeyFunc(keyAlias, huksOptions);
  return ret;
}

function check(): string {
  try {
    /\* 1. Generate a key. \*/
    testGenKey()
    /\* 2. Export the key. \*/
    huks.exportKeyItem(keyAlias, emptyOptions, (error, data) => {
      if (error) {
        console.error(\`callback: exportKeyItem failed, \` + error);
      } else {
        console.info(\`callback: exportKeyItem success, data = ${JSON.stringify(data)}\`);
      }
    });
    return 'Success';
  } catch (error) {
    console.error(\`callback: exportKeyItem input arg invalid, ${JSON.stringify(error)}\`);
    return 'Failed';
  }
}
