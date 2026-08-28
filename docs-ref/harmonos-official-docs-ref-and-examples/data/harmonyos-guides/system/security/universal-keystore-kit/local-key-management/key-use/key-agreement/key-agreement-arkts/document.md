# Key Agreement (ArkTS)

This topic uses X25519, DH, and ECDH as an example to demonstrate how to perform key agreement for HUKS-managed keys. For details about the scenarios and supported algorithm specifications, see [Supported Algorithms](../key-agreement-overview-and-algorithm-specifications/document.md#supported-algorithms).

#### How to Develop

**Key Generation**

Generate an asymmetric key for device A and device B each. For details, see [Key Generation](../../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md) or [Key Import](../../../key-generation-and-import/key-import/key-import-overview-and-algorithm-specifications/document.md).

(Optional) You can specify the [HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-type-h#oh_huks_keystoragetype) parameter when generating a key to decide if HUKS manages the resulting key from the key agreement process.

-   If this tag is set to **HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS**, the shared secret is managed by HUKS. That is, the shared secret is always in a secure environment throughout its lifecycle.
    
-   If this tag is set to **HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED**, the shared secret generated will be returned to the caller for management. That is, service side ensures the key security.
    
-   If this tag is not set, the shared secret generated can be either managed by HUKS or returned to the caller for management. The key protection mode can be set in the subsequent key agreement on the service side.
    

**Key Export**

Export the public key of the asymmetric key pair of device A and device B. For details, see [Key Export](../../../other-operations/exporting-a-key/exporting-a-key-arkts/document.md).

**Key Agreement**

Perform key agreement using the public key of the peer device and private key of the local device (that is, public key of device B and private key of device A for device A, and public key of device A and private key of device B for device B) to produce a shared secret.

During key agreement, you can set **HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG** (optional) to specify how the shared secret generated is managed.

| Key Generation | Key Agreement | Specifications |
| :-- | :-- | :-- |
| HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | The key is managed by HUKS. |
| HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | The key is returned to the caller for management. |
| The tag is not set. | HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | The key is managed by HUKS. |
| The tag is not set. | HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | The key is returned to the caller for management. |
| The tag is not set. | The tag is not set. | The key is returned to the caller for management. |

Note: The tag value set in key agreement should not conflict with the tag value set in key generation. The above table lists only valid settings.

**Key Deletion**

Delete the keys from device A and device B when the keys are not required. For details, see [Deleting a Key](../../../key-deletion/deleting-a-key-arkts/document.md).

#### Development Cases

The following uses the X25519, DH, and ECDH keys as examples for key agreement.

## X25519 asymmetric key agreement example

Prepare the X25519 key agreement materials.

/\*
 \* Agree on an X25519 key using promise-based APIs.
 \*/
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

function stringToUint8Array(str: string) {
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

/\*
 \* Set the key alias and encapsulate the key property set.
 \*/
let srcKeyAliasFirst = 'AgreeX25519KeyFirstAlias';
let srcKeyAliasSecond = 'AgreeX25519KeySecondAlias';
let agreeX25519InData = 'AgreeX25519TestIndata';
let finishOutData: Uint8Array;
let handle: number;
let exportKey: Uint8Array;
let exportKeyFirst: Uint8Array;
let exportKeySecond: Uint8Array;
/\* Set the parameter set used for generating the key. \*/
let properties: huks.HuksParam\[\] = \[{
  tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
  value: huks.HuksKeyAlg.HUKS\_ALG\_X25519,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
  value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_AGREE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
  value: huks.HuksKeySize.HUKS\_CURVE25519\_KEY\_SIZE\_256,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
  value: huks.HuksKeyDigest.HUKS\_DIGEST\_NONE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_PADDING,
  value: huks.HuksKeyPadding.HUKS\_PADDING\_NONE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
  value: huks.HuksCipherMode.HUKS\_MODE\_CBC,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG,
  value: huks.HuksKeyStorageType.HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS,
}
\];
let huksOptions: huks.HuksOptions = {
  properties: properties,
  inData: new Uint8Array(\[\])
}
/\* Set the parameter set for the first key agreement. \*/
const finishProperties: huks.HuksParam\[\] = \[{
  tag: huks.HuksTag.HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG,
  value: huks.HuksKeyStorageType.HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_IS\_KEY\_ALIAS,
  value: true
}, {
  tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
  value: huks.HuksKeyAlg.HUKS\_ALG\_AES,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
  value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_256,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
  value:
  huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT |
  huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
  value: huks.HuksKeyDigest.HUKS\_DIGEST\_NONE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_PADDING,
  value: huks.HuksKeyPadding.HUKS\_PADDING\_NONE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
  value: huks.HuksCipherMode.HUKS\_MODE\_ECB,
}
\];
let finishOptionsFirst: huks.HuksOptions = {
  properties: \[
    ...finishProperties, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_ALIAS,
    value: stringToUint8Array(srcKeyAliasFirst + 'final'),
  }\],
  inData: stringToUint8Array(agreeX25519InData)
}
/\* Set the parameter set for the second key agreement. \*/
let finishOptionsSecond: huks.HuksOptions = {
  properties: \[
    ...finishProperties, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_ALIAS,
    value: stringToUint8Array(srcKeyAliasSecond + 'final'),
  }\],
  inData: stringToUint8Array(agreeX25519InData)
}

Perform key agreement.

/\* Generate a key. \*/
async function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter generateKeyItem');
  try {
    await huks.generateKeyItem(keyAlias, huksOptions)
      .then(() => {
        console.info(\`promise: generateKeyItem success\`);
      }).catch((error: BusinessError) => {
        console.error(\`promise: generateKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}\`);
      })
  } catch (error) {
    console.error(\`promise: generateKeyItem input arg invalid\`);
  }
}

/\* Initializes a key session. This function returns a session handle (mandatory) and a challenge value (optional). \*/
async function initSession(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter initSession');
  try {
    await huks.initSession(keyAlias, huksOptions)
      .then((data) => {
        handle = data.handle;
        console.info(\`promise: initSession success\`);
      }).catch((error: BusinessError) => {
        console.error(\`promise: initSession failed, errCode : ${error.code}, errMsg : ${error.message}\`);
      })
  } catch (error) {
    console.error(\`promise: initSession input arg invalid\`);
  }
}

/\* Call updateSession multiple times to process data by segment and output the processed data. \*/
async function updateSession(handle: number, huksOptions: huks.HuksOptions) {
  console.info('promise: enter updateSession');
  try {
    await huks.updateSession(handle, huksOptions)
      .then((data) => {
        console.info(\`promise: updateSession success, data is \` + uint8ArrayToString(data.outData as Uint8Array));
      }).catch((error: BusinessError) => {
        console.error(\`promise: updateSession failed, errCode : ${error.code}, errMsg : ${error.message}\`);
      })
  } catch (error) {
    console.error(\`promise: updateSession input arg invalid\`);
  }
}

/\* Finish the key session to output the shared secret key. \*/
async function finishSession(handle: number, huksOptions: huks.HuksOptions) {
  console.info('promise: enter finishSession');
  try {
    await huks.finishSession(handle, huksOptions)
      .then((data) => {
        finishOutData = data.outData as Uint8Array;
        console.info(\`promise: finishSession success, data is \` + uint8ArrayToString(data.outData as Uint8Array));
      }).catch((error: BusinessError) => {
        console.error(\`promise: finishSession failed, errCode : ${error.code}, errMsg : ${error.message}\`);
      })
  } catch (error) {
    console.error(\`promise: finishSession input arg invalid\`);
  }
}

/\* Export a key. \*/
async function exportKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter exportKeyItem');
  try {
    await huks.exportKeyItem(keyAlias, huksOptions)
      .then((data) => {
        exportKey = data.outData as Uint8Array;
        console.info(\`promise: exportKey success, data is \` + uint8ArrayToString(data.outData as Uint8Array));
      }).catch((error: BusinessError) => {
        console.error(\`promise: exportKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}\`);
      })
  } catch (error) {
    console.error(\`promise: exportKeyItem input arg invalid\`);
  }
}

/\* Delete the keys. \*/
async function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter deleteKeyItem');
  try {
    await huks.deleteKeyItem(keyAlias, huksOptions)
      .then(() => {
        console.info(\`promise: deleteKeyItem success\`);
      }).catch((error: BusinessError) => {
        console.error(\`promise: deleteKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}\`);
      })
  } catch (error) {
    console.error(\`promise: deleteKeyItem input arg invalid\`);
  }
}

async function testAgree() {
  /\* 1. Set the key alias srcKeyAliasFirst for device A and srcKeyAliasSecond for device B, and parameters for generating the key pairs. \*/
  /\* 2. Generate an asymmetric key pair for device A. \*/
  await generateKeyItem(srcKeyAliasFirst, huksOptions);
  /\* 3. Generate an asymmetric key pair for device B. \*/
  await generateKeyItem(srcKeyAliasSecond, huksOptions);
  /\* 4. Export the public keys of the key pairs of device A and device B. \*/
  await exportKeyItem(srcKeyAliasFirst, huksOptions);
  exportKeyFirst = exportKey;
  await exportKeyItem(srcKeyAliasSecond, huksOptions);
  exportKeySecond = exportKey;
  /\* 5. Perform key agreement (Init-Update-Finish) for device A. \*/
  await initSession(srcKeyAliasFirst, huksOptions);
  huksOptions.inData = exportKeySecond;
  await updateSession(handle, huksOptions);
  await finishSession(handle, finishOptionsFirst);
  /\* 6. Perform key agreement (Init-Update-Finish) for device B. \*/
  await initSession(srcKeyAliasSecond, huksOptions);
  huksOptions.inData = exportKeyFirst;
  await updateSession(handle, huksOptions);
  await finishSession(handle, finishOptionsSecond);
  /\* 7. Delete the keys on device A and device B. \*/
  await deleteKeyItem(srcKeyAliasFirst, huksOptions);
  await deleteKeyItem(srcKeyAliasSecond, huksOptions);
}

## DH key agreement example

/\*
 \* Agree on a DH key using promise-based APIs.
 \*/
import { huks } from '@kit.UniversalKeystoreKit';

function stringToUint8Array(str: string) {
  let arr: number\[\] = \[\];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function uint8ArrayToBigInt(arr: Uint8Array): bigint {
  let i = 0;
  const byteMax: bigint = BigInt('0x100');
  let result: bigint = BigInt('0');
  while (i < arr.length) {
    result = result \* byteMax;
    result = result + BigInt(arr\[i\]);
    i += 1;
  }
  return result;
}

const dhAgree: huks.HuksParam\[\] = \[{
  tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
  value: huks.HuksKeyAlg.HUKS\_ALG\_DH,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
  value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_AGREE,
}\];
const dh2048Agree: huks.HuksParam\[\] = \[
  ...dhAgree, {
  tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
  value: huks.HuksKeySize.HUKS\_DH\_KEY\_SIZE\_2048,
}\];
const dhGenOptions: huks.HuksOptions = {
  properties: dh2048Agree,
  inData: new Uint8Array(\[\])
};
const emptyOptions: huks.HuksOptions = {
  properties: \[\],
  inData: new Uint8Array(\[\])
};

async function huksDhAgreeExportKey(keyAlias: string,
  peerPubKey: huks.HuksReturnResult): Promise<huks.HuksReturnResult> {
  const initHandle = await huks.initSession(keyAlias, dhGenOptions);
  const dhAgreeUpdateBobPubKey: huks.HuksOptions = {
    properties: \[
      ...dh2048Agree, {
      tag: huks.HuksTag.HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG,
      value: huks.HuksKeyStorageType.HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED,
    }\],
    inData: peerPubKey.outData
  };
  await huks.updateSession(initHandle.handle, dhAgreeUpdateBobPubKey);
  return await huks.finishSession(initHandle.handle, emptyOptions);
}

async function huksDhAgreeExportTest(
  aliasA: string, aliasB: string,
  pubKeyA: huks.HuksReturnResult, pubKeyB: huks.HuksReturnResult) {

  const agreedKeyFromAlice = await huksDhAgreeExportKey(aliasA, pubKeyB);
  console.info(\`ok! agreedKeyFromAlice export is 0x${uint8ArrayToBigInt(agreedKeyFromAlice.outData).toString(16)}\`);

  const agreedKeyFromBob = await huksDhAgreeExportKey(aliasB, pubKeyA);
  console.info(\`ok! agreedKeyFromBob export is 0x${uint8ArrayToBigInt(agreedKeyFromBob.outData).toString(16)}\`);
}

async function huksDhAgreeInHuks(keyAlias: string, peerPubKey: huks.HuksReturnResult,
  aliasAgreedKey: string): Promise<huks.HuksReturnResult> {
  const onlyUsedInHuks: huks.HuksParam\[\] = \[{
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_STORAGE\_FLAG,
    value: huks.HuksKeyStorageType.HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS,
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG,
    value: huks.HuksKeyStorageType.HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS,
  }\];
  const dhAgreeInit: huks.HuksOptions = {
    properties: \[
      ...dhAgree,
      { tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE, value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_256, },
      ...onlyUsedInHuks\],
    inData: new Uint8Array(\[\])
  };
  const dhAgreeFinishParams: huks.HuksParam\[\] = \[
    ...onlyUsedInHuks,
    { tag: huks.HuksTag.HUKS\_TAG\_IS\_KEY\_ALIAS, value: true },
    { tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM, value: huks.HuksKeyAlg.HUKS\_ALG\_AES },
    { tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE, value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_256 },
    {
      tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT | huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT
    }
  \];

  const handle = await huks.initSession(keyAlias, dhAgreeInit);
  const dhAgreeUpdatePubKey: huks.HuksOptions = {
    properties: \[...dhAgree, ...onlyUsedInHuks\],
    inData: peerPubKey.outData
  };
  await huks.updateSession(handle.handle, dhAgreeUpdatePubKey);
  const dhAgreeAliceFinnish: huks.HuksOptions = {
    properties: \[...dhAgreeFinishParams, {
      tag: huks.HuksTag.HUKS\_TAG\_KEY\_ALIAS, value: stringToUint8Array(aliasAgreedKey)
    }\], inData: new Uint8Array(\[\])
  };
  return await huks.finishSession(handle.handle, dhAgreeAliceFinnish);
}

async function huksDhAgreeInHuksTest(
  aliasA: string, aliasB: string,
  pubKeyA: huks.HuksReturnResult, pubKeyB: huks.HuksReturnResult,
  aliasAgreedKeyFromA: string, aliasAgreedKeyFromB: string) {

  const finishAliceResult = await huksDhAgreeInHuks(aliasA, pubKeyB, aliasAgreedKeyFromA);
  console.info(\`ok! finishAliceResult in huks is 0x${uint8ArrayToBigInt(finishAliceResult.outData).toString(16)}\`);
  const aliceAgreedExist = await huks.isKeyItemExist(aliasAgreedKeyFromA, emptyOptions);
  console.info(\`ok! aliceAgreedExist in huks is ${aliceAgreedExist}\`);

  const finishBobResult = await huksDhAgreeInHuks(aliasB, pubKeyA, aliasAgreedKeyFromB);
  console.info(\`ok! finishBobResult in huks is 0x${uint8ArrayToBigInt(finishBobResult.outData).toString(16)}\`);
  const bobAgreedExist = await huks.isKeyItemExist(aliasAgreedKeyFromB, emptyOptions);
  console.info(\`ok! bobAgreedExist in huks is ${bobAgreedExist}\`);

  await huks.deleteKeyItem(aliasAgreedKeyFromA, emptyOptions);
  await huks.deleteKeyItem(aliasAgreedKeyFromB, emptyOptions);
}

async function huksDhAgreeTest() {
  const aliasAlice = 'alice';
  const aliasBob = 'bob';

  /\* Call generateKeyItem to generate a key with alias of alice and a key with alias of bob. \*/
  await huks.generateKeyItem(aliasAlice, dhGenOptions);
  await huks.generateKeyItem(aliasBob, dhGenOptions);

  /\* Export the public keys of asymmetric key pairs alice and bob. \*/
  const pubKeyAlice = await huks.exportKeyItem(aliasAlice, emptyOptions);
  const pubKeyBob = await huks.exportKeyItem(aliasBob, emptyOptions);

  /\* Perform key agreement and return the shared secret generated to the caller for management. \*/
  await huksDhAgreeExportTest(aliasAlice, aliasBob, pubKeyAlice, pubKeyBob);

  /\* Perform key agreement and let HUKS manage the shared secret generated. \*/
  await huksDhAgreeInHuksTest(aliasAlice, aliasBob, pubKeyAlice, pubKeyBob, 'agreedKeyFromAlice', 'agreedKeyFromBob');

  await huks.deleteKeyItem(aliasAlice, emptyOptions);
  await huks.deleteKeyItem(aliasBob, emptyOptions);
}

## ECDH Key Agreement

Prepare the ECDH key agreement materials.

/\*
 \* Agree on an ECDH key using promise-based APIs.
 \*/
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

function stringToUint8Array(str: string) {
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

/\*
 \* Set the key alias and encapsulate the key property set.
 \*/
let srcKeyAliasFirst = 'AgreeECDHKeyFirstAlias';
let srcKeyAliasSecond = 'AgreeECDHKeySecondAlias';
let agreeECDHInData = 'AgreeECDHTestIndata';
let finishOutData: Uint8Array;
let handle: number;
let exportKey: Uint8Array;
let exportKeyFirst: Uint8Array;
let exportKeySecond: Uint8Array;
/\* Set the parameter set used for generating the key. \*/
let properties: huks.HuksParam\[\] = \[{
  tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
  value: huks.HuksKeyAlg.HUKS\_ALG\_ECC,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
  value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_AGREE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
  value: huks.HuksKeySize.HUKS\_ECC\_KEY\_SIZE\_256,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
  value: huks.HuksKeyDigest.HUKS\_DIGEST\_NONE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_PADDING,
  value: huks.HuksKeyPadding.HUKS\_PADDING\_NONE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
  value: huks.HuksCipherMode.HUKS\_MODE\_CBC,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG,
  value: huks.HuksKeyStorageType.HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS,
}
\]
let huksOptions: huks.HuksOptions = {
  properties: properties,
  inData: new Uint8Array(\[\])
}
/\* Set the parameter set for the first key agreement. \*/
const finishProperties: huks.HuksParam\[\] = \[{
  tag: huks.HuksTag.HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG,
  value: huks.HuksKeyStorageType.HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_IS\_KEY\_ALIAS,
  value: true
}, {
  tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
  value: huks.HuksKeyAlg.HUKS\_ALG\_ECDH,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
  value: huks.HuksKeySize.HUKS\_ECC\_KEY\_SIZE\_256,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
  value:
  huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT |
  huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
  value: huks.HuksKeyDigest.HUKS\_DIGEST\_NONE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_PADDING,
  value: huks.HuksKeyPadding.HUKS\_PADDING\_NONE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
  value: huks.HuksCipherMode.HUKS\_MODE\_CBC,
}
\];
let finishOptionsFirst: huks.HuksOptions = {
  properties: \[
    ...finishProperties, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_ALIAS,
    value: stringToUint8Array(srcKeyAliasFirst + 'final'),
  }\],
  inData: stringToUint8Array(agreeECDHInData)
}
/\* Set the parameter set for the second key agreement. \*/
let finishOptionsSecond: huks.HuksOptions = {
  properties: \[
    ...finishProperties, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_ALIAS,
    value: stringToUint8Array(srcKeyAliasSecond + 'final'),
  }\],
  inData: stringToUint8Array(agreeECDHInData)
}

Perform key agreement.

/\* Generate a key. \*/
async function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter generateKeyItem');
  try {
    await huks.generateKeyItem(keyAlias, huksOptions)
      .then(() => {
        console.info(\`promise: generateKeyItem success\`);
      }).catch((error: BusinessError) => {
        console.error(\`promise: generateKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}\`);
      })
  } catch (error) {
    console.error(\`promise: generateKeyItem input arg invalid\`);
  }
}

/\* Initializes a key session. This function returns a session handle (mandatory) and a challenge value (optional). \*/
async function initSession(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter initSession');
  try {
    await huks.initSession(keyAlias, huksOptions)
      .then((data) => {
        handle = data.handle;
        console.info(\`promise: initSession success\`);
      }).catch((error: BusinessError) => {
        console.error(\`promise: initSession failed, errCode : ${error.code}, errMsg : ${error.message}\`);
      })
  } catch (error) {
    console.error(\`promise: initSession input arg invalid\`);
  }
}

/\* Call updateSession multiple times to process data by segment and output the processed data. \*/
async function updateSession(handle: number, huksOptions: huks.HuksOptions) {
  console.info('promise: enter updateSession');
  try {
    await huks.updateSession(handle, huksOptions)
      .then((data) => {
        console.info(\`promise: updateSession success, data is \` + uint8ArrayToString(data.outData as Uint8Array));
      }).catch((error: BusinessError) => {
        console.error(\`promise: updateSession failed, errCode : ${error.code}, errMsg : ${error.message}\`);
      })
  } catch (error) {
    console.error(\`promise: updateSession input arg invalid\`);
  }
}

/\* Finish the key session to output the shared secret key. \*/
async function finishSession(handle: number, huksOptions: huks.HuksOptions) {
  console.info('promise: enter finishSession');
  try {
    await huks.finishSession(handle, huksOptions)
      .then((data) => {
        finishOutData = data.outData as Uint8Array;
        console.info(\`promise: finishSession success, data is \` + uint8ArrayToString(data.outData as Uint8Array));
      }).catch((error: BusinessError) => {
        console.error(\`promise: finishSession failed, errCode : ${error.code}, errMsg : ${error.message}\`);
      })
  } catch (error) {
    console.error(\`promise: finishSession input arg invalid\`);
  }
}

/\* Export a key. \*/
async function exportKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter exportKeyItem');
  try {
    await huks.exportKeyItem(keyAlias, huksOptions)
      .then((data) => {
        exportKey = data.outData as Uint8Array;
        console.info(\`promise: exportKey success, data is \` + uint8ArrayToString(data.outData as Uint8Array));
      }).catch((error: BusinessError) => {
        console.error(\`promise: exportKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}\`);
      })
  } catch (error) {
    console.error(\`promise: exportKeyItem input arg invalid\`);
  }
}

/\* Delete the keys. \*/
async function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter deleteKeyItem');
  try {
    await huks.deleteKeyItem(keyAlias, huksOptions)
      .then(() => {
        console.info(\`promise: deleteKeyItem success\`);
      }).catch((error: BusinessError) => {
        console.error(\`promise: deleteKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}\`);
      })
  } catch (error) {
    console.error(\`promise: deleteKeyItem input arg invalid\`);
  }
}

async function testAgree() {
  /\* 1. Set the key alias srcKeyAliasFirst for device A and srcKeyAliasSecond for device B, and parameters for generating the key pairs. \*/
  /\* 2. Generate an asymmetric key pair for device A. \*/
  await generateKeyItem(srcKeyAliasFirst, huksOptions);
  /\* 3. Generate an asymmetric key pair for device B. \*/
  await generateKeyItem(srcKeyAliasSecond, huksOptions);
  /\* 4. Export the public keys of the key pairs of device A and device B. \*/
  await exportKeyItem(srcKeyAliasFirst, huksOptions);
  exportKeyFirst = exportKey;
  await exportKeyItem(srcKeyAliasSecond, huksOptions);
  exportKeySecond = exportKey;
  /\* 5. Perform key agreement (Init-Update-Finish) for device A. \*/
  await initSession(srcKeyAliasFirst, huksOptions);
  huksOptions.inData = exportKeySecond;
  await updateSession(handle, huksOptions);
  await finishSession(handle, finishOptionsFirst);
  /\* 6. Perform key agreement (Init-Update-Finish) for device B. \*/
  await initSession(srcKeyAliasSecond, huksOptions);
  huksOptions.inData = exportKeyFirst;
  await updateSession(handle, huksOptions);
  await finishSession(handle, finishOptionsSecond);
  /\* 7. Delete the keys on device A and device B. \*/
  await deleteKeyItem(srcKeyAliasFirst, huksOptions);
  await deleteKeyItem(srcKeyAliasSecond, huksOptions);
}
