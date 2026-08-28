# Generating a Key (ArkTS)

This topic walks you through on how to randomly generate a key with the DH algorithm. For details about the scenarios and supported algorithms, see [Supported Algorithms](../key-generation-overview-and-algorithm-specifications/document.md#supported-algorithms).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/NzKwbmO7TTuvYGeHYiowEg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062010Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0B1D816A5B032C5D9355BA79F7C2CC4EA77036B86430723F4B78A1CC18E4FF1)

Key aliases must not contain sensitive information, such as personal data.

#### How to Develop

1.  Specify the key alias. For details about the naming rules, see [Key Generation Overview and Algorithm Specifications](../key-generation-overview-and-algorithm-specifications/document.md).
    
2.  Initialize the key property set.
    
    -   Encapsulate key properties in [HuksParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksparam) and use a **HuksParam** array to assign values to the **properties** field of [HuksOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksoptions).
    -   The key property set must contain [HuksKeyAlg](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#hukskeyalg), [HuksKeySize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#hukskeysize), and [HuksKeyPurpose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#hukskeypurpose). That is, the **HUKS\_TAG\_ALGORITHM**, **HUKS\_TAG\_PURPOSE**, and **HUKS\_TAG\_KEY\_SIZE** tags are mandatory.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/JCw5vJ_FSkyKstfJHiPbag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062010Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C86E825958363CC9B1055DCBC9B11099AD472B8F9E2DC0308090B045A68E905A)
    
    A key can have only one purpose, and the purpose specified during key generation must match the key purpose during usage. Otherwise, an exception occurs.
    
3.  Use [generateKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksgeneratekeyitem9) to generate a key based on the key alias and key properties specified.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/rl_mAB8CRISeZIE3_RPlNg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062010Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3EDE9A14FA4955B76092B9D559B52C51C3E38BCFEA28F5F6641AEB2826627AAB)

If the service uses the same key alias to call the HUKS API to generate a key again, HUKS will generate a new key and overwrite the historical key file.

import { huks } from '@kit.UniversalKeystoreKit';

/\* 1. Set the key alias. \*/
let keyAlias = 'dh\_key';
/\* 2. Initialize the key property set. \*/
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
    console.error(\`promise: generateKeyItem input arg invalid, \` + JSON.stringify(error));
    return 'Failed';
  }
}

async function testGenKey(): Promise<string> {
  let ret = await publicGenKeyFunc(keyAlias, huksOptions);
  return ret;
}
