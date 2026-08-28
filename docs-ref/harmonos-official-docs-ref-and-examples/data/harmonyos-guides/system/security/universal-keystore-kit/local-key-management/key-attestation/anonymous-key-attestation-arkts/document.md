# Anonymous Key Attestation (ArkTS)

Ensure network connection during the operation.

#### How to Develop

1.  Specify the key alias. For details about the naming rules, see [Key Generation Overview and Algorithm Specifications](../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md).
    
2.  Initializes a parameter set.
    
    The **properties** field in [HuksOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksoptions) must contain [HUKS\_TAG\_ATTESTATION\_CHALLENGE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#hukstag). Optional parameters include [HUKS\_TAG\_ATTESTATION\_ID\_VERSION\_INFO](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#hukstag) and [HUKS\_TAG\_ATTESTATION\_ID\_ALIAS](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#hukstag).
    
3.  Generate an asymmetric key. For details, see [Key Generation](../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md).
    
4.  Use [anonAttestKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksanonattestkeyitem11) with the key alias and parameter set to perform key attestation.
    

#### Development Case

/\*
 \* Perform anonymous key attestation. This example uses promise-based APIs.
 \*/
import { huks } from '@kit.UniversalKeystoreKit';

/\* 1. Set the key alias. \*/
let keyAliasString = 'key anon attest';
let aliasString = keyAliasString;
let aliasUint8 = stringToUint8Array(keyAliasString);
let securityLevel = stringToUint8Array('sec\_level');
let challenge = stringToUint8Array('challenge\_data');
let versionInfo = stringToUint8Array('version\_info');
let anonAttestCertChain: string\[\];

class ThrowObject {
  public isThrow: boolean = false;
}

/\* Encapsulate the key parameter set. \*/
let genKeyProperties: huks.HuksParam\[\] = \[
  {
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_RSA
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_RSA\_KEY\_SIZE\_2048
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_VERIFY
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
    value: huks.HuksKeyDigest.HUKS\_DIGEST\_SHA256
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_PADDING,
    value: huks.HuksKeyPadding.HUKS\_PADDING\_PSS
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_GENERATE\_TYPE,
    value: huks.HuksKeyGenerateType.HUKS\_KEY\_GENERATE\_TYPE\_DEFAULT
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_ECB
  }
\]
let genOptions: huks.HuksOptions = {
  properties: genKeyProperties
};

/\* 2. Encapsulate the parameter set for key attestation. \*/
let anonAttestKeyProperties: huks.HuksParam\[\] = \[
  {
    tag: huks.HuksTag.HUKS\_TAG\_ATTESTATION\_ID\_SEC\_LEVEL\_INFO,
    value: securityLevel
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_ATTESTATION\_CHALLENGE,
    value: challenge
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_ATTESTATION\_ID\_VERSION\_INFO,
    value: versionInfo
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_ATTESTATION\_ID\_ALIAS,
    value: aliasUint8
  }
\]
let huksOptions: huks.HuksOptions = {
  properties: anonAttestKeyProperties
};

function stringToUint8Array(str: string) {
  let arr: number\[\] = \[\];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
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
      throwObject.isThrow = true;
      throw (error as Error);
    }
  });
}

/\* 3. Generate a key. \*/
async function publicGenKeyFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info(\`enter promise generateKeyItem\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await generateKeyItem(keyAlias, huksOptions, throwObject)
      .then((data) => {
        console.info(\`promise: generateKeyItem success, data = ${JSON.stringify(data)}\`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: generateKeyItem failed, ${JSON.stringify(error)}\`);
        }
      });
  } catch (error) {
    console.error(\`promise: generateKeyItem input arg invalid, ${JSON.stringify(error)}\`);
  }
}

/\* 4. Attest the key. \*/
function anonAttestKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
  return new Promise<huks.HuksReturnResult>((resolve, reject) => {
    try {
      huks.anonAttestKeyItem(keyAlias, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throwObject.isThrow = true;
      throw (error as Error);
    }
  });
}

async function publicAnonAttestKey(keyAlias: string, huksOptions: huks.HuksOptions): Promise<string> {
  console.info(\`enter promise anonAttestKeyItem\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await anonAttestKeyItem(keyAlias, huksOptions, throwObject)
      .then((data) => {
        console.info(\`promise: anonAttestKeyItem success, data = ${JSON.stringify(data)}\`);
        if (data !== null && data.certChains !== null) {
          anonAttestCertChain = data.certChains as string\[\];
        }
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: anonAttestKeyItem failed, ${JSON.stringify(error)}\`);
        }
      });
    return 'Success';
  } catch (error) {
    console.error(\`promise: anonAttestKeyItem input arg invalid, ${JSON.stringify(error)}\`);
    return 'Failed';
  }
}

async function anonAttestKeyTest(): Promise<string> {
  await publicGenKeyFunc(aliasString, genOptions);
  let ret = await publicAnonAttestKey(aliasString, huksOptions);
  console.info('anon attest certChain data: ' + anonAttestCertChain)
  return ret;
}
