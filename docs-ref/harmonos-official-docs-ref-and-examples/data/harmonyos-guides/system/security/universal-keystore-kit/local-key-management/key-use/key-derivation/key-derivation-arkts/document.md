# Key Derivation (ArkTS)

This topic walks you through on how to derive a key using PBKDF2 and HKDF256. For details about the scenarios and supported algorithm specifications, see [Supported Algorithms](../key-derivation-overview-and-algorithm-specifications/document.md#supported-algorithms).

#### How to Develop

**Key Generation**

1.  Specify the key alias. For details about the naming rules, see [Key Generation Overview and Algorithm Specifications](../../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md).
    
2.  Initialize the key property set. You can set **HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG** (optional) to specify how the key derived from this key is managed.
    
    -   If this tag is set to **HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS**, the derived key is managed by HUKS. That is, the derived key is always in a secure environment throughout its lifecycle.
        
    -   If this tag is set to **HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED**, the derived key will be returned to the caller for management. That is, the service side ensures the key security.
        
    -   If this tag is not set, the derived key can be either managed by HUKS or returned to the caller for management. The key protection mode can be set in the subsequent key derivation on the service side.
        
3.  Use [generateKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksgeneratekeyitem9) to generate a key. For details, see [Key Generation](../../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md).
    

Alternatively, you can [import a key](../../../key-generation-and-import/key-import/key-import-overview-and-algorithm-specifications/document.md).

**Key Derivation**

1.  Obtain the key alias and set the **HuksOptions** parameter.
    
    You can set **HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG** to specify how the derived key is managed.
    
    | Key Generation | Key Derivation | Specifications |
    | :-- | :-- | :-- |
    | HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | The key is managed by HUKS. |
    | HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | The key is returned to the caller for management. |
    | The tag is not set. | HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | The key is managed by HUKS. |
    | The tag is not set. | HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | The key is returned to the caller for management. |
    | The tag is not set. | The tag is not set. | The key is returned to the caller for management. |
    
    Note: The tag value set in key derivation should not conflict with the tag value set in key generation. The above table lists only valid settings.
    
2.  Use [initSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksinitsession9) to initialize a key session. The session handle is returned after the initialization.
    
3.  Use [updateSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksupdatesession9) to process data.
    
4.  Use [finishSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksfinishsession9) to derive a key.
    

**Key Deletion**

Use [deleteKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksdeletekeyitem9) to delete the key that is not required. For details, see [Deleting a Key](../../../key-deletion/deleting-a-key-arkts/document.md).

#### Development Cases

## HKDF

Prepare the HKDF key derivation material.

/\*
 \* Derive an HKDF key using promise-based APIs.
 \*/
import { huks } from '@kit.UniversalKeystoreKit';

/\*
 \* Set the key alias and encapsulate the key property set.
 \*/
let srcKeyAlias = 'hkdf\_Key';
let deriveHkdfInData = 'deriveHkdfTestIndata';
let handle: number;
let finishOutData: Uint8Array;
let huksKeyDeriveKeySize = 32;
/\* Set the parameter set used for key generation. \*/
let properties: huks.HuksParam\[\] = \[
  {
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_AES,
  }, {
  tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
  value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DERIVE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
  value: huks.HuksKeyDigest.HUKS\_DIGEST\_SHA256,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
  value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_128,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG,
  value: huks.HuksKeyStorageType.HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS,
}\];

let huksOptions: huks.HuksOptions = {
  properties: properties,
  inData: new Uint8Array(\[\])
}
/\* Set the parameter set used for init(). \*/
let initProperties: huks.HuksParam\[\] = \[{
  tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
  value: huks.HuksKeyAlg.HUKS\_ALG\_HKDF,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
  value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DERIVE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
  value: huks.HuksKeyDigest.HUKS\_DIGEST\_SHA256,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DERIVE\_KEY\_SIZE,
  value: huksKeyDeriveKeySize,
}\];

let initOptions: huks.HuksOptions = {
  properties: initProperties,
  inData: new Uint8Array(\[\])
}
/\* Set the parameter set used for finish(). \*/
let finishProperties: huks.HuksParam\[\] = \[{
  tag: huks.HuksTag.HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG,
  value: huks.HuksKeyStorageType.HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_IS\_KEY\_ALIAS,
  value: true,
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
  tag: huks.HuksTag.HUKS\_TAG\_KEY\_ALIAS,
  value: stringToUint8Array(srcKeyAlias),
}, {
  tag: huks.HuksTag.HUKS\_TAG\_PADDING,
  value: huks.HuksKeyPadding.HUKS\_PADDING\_NONE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
  value: huks.HuksCipherMode.HUKS\_MODE\_ECB,
}\];
let finishOptions: huks.HuksOptions = {
  properties: finishProperties,
  inData: new Uint8Array(\[\])
}

function stringToUint8Array(str: String) {
  let arr: number\[\] = \[\];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

class ThrowObject {
  public isThrow = false;
}

Derive a key.

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
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: generateKeyItem input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

function initSession(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
  return new Promise<huks.HuksSessionHandle>((resolve, reject) => {
    try {
      huks.initSession(keyAlias, huksOptions, (error, data) => {
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

async function publicInitFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info(\`enter promise doInit\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await initSession(keyAlias, huksOptions, throwObject)
      .then((data) => {
        console.info(\`promise: doInit success, data = ${JSON.stringify(data)}\`);
        handle = data.handle;
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: doInit failed, ${JSON.stringify(error)}\`);
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: doInit input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

function updateSession(handle: number, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
  return new Promise<huks.HuksOptions>((resolve, reject) => {
    try {
      huks.updateSession(handle, huksOptions, (error, data) => {
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

async function publicUpdateFunc(handle: number, huksOptions: huks.HuksOptions) {
  console.info(\`enter promise doUpdate\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await updateSession(handle, huksOptions, throwObject)
      .then((data) => {
        console.info(\`promise: doUpdate success, data = ${JSON.stringify(data)}\`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: doUpdate failed, ${JSON.stringify(error)}\`);
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: doUpdate input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

function finishSession(handle: number, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
  return new Promise<huks.HuksReturnResult>((resolve, reject) => {
    try {
      huks.finishSession(handle, huksOptions, (error, data) => {
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

async function publicFinishFunc(handle: number, huksOptions: huks.HuksOptions) {
  console.info(\`enter promise doFinish\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await finishSession(handle, huksOptions, throwObject)
      .then((data) => {
        finishOutData = data.outData as Uint8Array;
        console.info(\`promise: doFinish success, data = ${JSON.stringify(data)}\`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: doFinish failed, ${JSON.stringify(error)}\`);
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: doFinish input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
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
      throwObject.isThrow = true;
      throw (error as Error);
    }
  });
}

async function publicDeleteKeyFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info(\`enter promise deleteKeyItem\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await deleteKeyItem(keyAlias, huksOptions, throwObject)
      .then((data) => {
        console.info(\`promise: deleteKeyItem key success, data = ${JSON.stringify(data)}\`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: deleteKeyItem failed, ${JSON.stringify(error)}\`);
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: deleteKeyItem input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

async function testDerive() {
  /\* Generate a key. \*/
  await publicGenKeyFunc(srcKeyAlias, huksOptions);
  /\* Perform key derivation. \*/
  await publicInitFunc(srcKeyAlias, initOptions);
  initOptions.inData = stringToUint8Array(deriveHkdfInData);
  await publicUpdateFunc(handle, initOptions);
  await publicFinishFunc(handle, finishOptions);
  await publicDeleteKeyFunc(srcKeyAlias, huksOptions);
}

## PBKDF2

Prepare the PBKDF2 key derivation material.

/\*
 \* Derive a PBKDF2 key using promise-based APIs.
 \*/
import { huks } from '@kit.UniversalKeystoreKit';

/\*
 \* Set the key alias and encapsulate the key property set.
 \*/
let srcKeyAlias = 'pbkdf2\_Key';
let salt = 'mySalt';
let iterationCount = 10000;
let derivedKeySize = 32;
let handle: number;
let finishOutData: Uint8Array;

/\* Set the parameter set used for key generation. \*/
let properties: huks.HuksParam\[\] = \[
  {
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_AES,
  }, {
  tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
  value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DERIVE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
  value: huks.HuksKeyDigest.HUKS\_DIGEST\_SHA256,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
  value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_256,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG,
  value: huks.HuksKeyStorageType.HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS,
}
\];

let huksOptions: huks.HuksOptions = {
  properties: properties,
  inData: new Uint8Array(\[\])
}

/\* Set the parameter set used for init(). \*/
let initProperties: huks.HuksParam\[\] = \[
  {
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_PBKDF2,
  }, {
  tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
  value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DERIVE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
  value: huks.HuksKeyDigest.HUKS\_DIGEST\_SHA256,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DERIVE\_KEY\_SIZE,
  value: derivedKeySize,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_ITERATION,
  value: iterationCount,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_SALT,
  value: stringToUint8Array(salt),
}
\];

let initOptions: huks.HuksOptions = {
  properties: initProperties,
  inData: new Uint8Array(\[\])
}

/\* Set the parameter set used for finish(). \*/
let finishProperties: huks.HuksParam\[\] = \[
  {
    tag: huks.HuksTag.HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG,
    value: huks.HuksKeyStorageType.HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS,
  }, {
  tag: huks.HuksTag.HUKS\_TAG\_IS\_KEY\_ALIAS,
  value: true,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
  value: huks.HuksKeyAlg.HUKS\_ALG\_AES,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
  value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_256,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
  value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT | huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
  value: huks.HuksKeyDigest.HUKS\_DIGEST\_NONE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_KEY\_ALIAS,
  value: stringToUint8Array(srcKeyAlias),
}, {
  tag: huks.HuksTag.HUKS\_TAG\_PADDING,
  value: huks.HuksKeyPadding.HUKS\_PADDING\_NONE,
}, {
  tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
  value: huks.HuksCipherMode.HUKS\_MODE\_ECB,
}
\];

let finishOptions: huks.HuksOptions = {
  properties: finishProperties,
  inData: new Uint8Array(\[\])
}

function stringToUint8Array(str: String) {
  let arr: number\[\] = \[\];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

class ThrowObject {
  public isThrow = false;
}

Derive a key.

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
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: generateKeyItem input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

function initSession(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
  return new Promise<huks.HuksSessionHandle>((resolve, reject) => {
    try {
      huks.initSession(keyAlias, huksOptions, (error, data) => {
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

async function publicInitFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info(\`enter promise doInit\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await initSession(keyAlias, huksOptions, throwObject)
      .then((data) => {
        console.info(\`promise: doInit success, data = ${JSON.stringify(data)}\`);
        handle = data.handle;
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: doInit failed, ${JSON.stringify(error)}\`);
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: doInit input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

function updateSession(handle: number, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
  return new Promise<huks.HuksOptions>((resolve, reject) => {
    try {
      huks.updateSession(handle, huksOptions, (error, data) => {
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

async function publicUpdateFunc(handle: number, huksOptions: huks.HuksOptions) {
  console.info(\`enter promise doUpdate\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await updateSession(handle, huksOptions, throwObject)
      .then((data) => {
        console.info(\`promise: doUpdate success, data = ${JSON.stringify(data)}\`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: doUpdate failed, ${JSON.stringify(error)}\`);
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: doUpdate input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

function finishSession(handle: number, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
  return new Promise<huks.HuksReturnResult>((resolve, reject) => {
    try {
      huks.finishSession(handle, huksOptions, (error, data) => {
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

async function publicFinishFunc(handle: number, huksOptions: huks.HuksOptions) {
  console.info(\`enter promise doFinish\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await finishSession(handle, huksOptions, throwObject)
      .then((data) => {
        finishOutData = data.outData as Uint8Array;
        console.info(\`promise: doFinish success, data = ${JSON.stringify(data)}\`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: doFinish failed, ${JSON.stringify(error)}\`);
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: doFinish input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
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
      throwObject.isThrow = true;
      throw (error as Error);
    }
  });
}

async function publicDeleteKeyFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info(\`enter promise deleteKeyItem\`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await deleteKeyItem(keyAlias, huksOptions, throwObject)
      .then((data) => {
        console.info(\`promise: deleteKeyItem key success, data = ${JSON.stringify(data)}\`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(\`promise: deleteKeyItem failed, ${JSON.stringify(error)}\`);
          throw (error as Error);
        }
      });
  } catch (error) {
    console.error(\`promise: deleteKeyItem input arg invalid, ${JSON.stringify(error)}\`);
    throw (error as Error);
  }
}

async function testDerive() {
  /\* Generate a key. \*/
  await publicGenKeyFunc(srcKeyAlias, huksOptions);
  /\* Perform key derivation. \*/
  await publicInitFunc(srcKeyAlias, initOptions);
  await publicUpdateFunc(handle, initOptions);
  await publicFinishFunc(handle, finishOptions);
  await publicDeleteKeyFunc(srcKeyAlias, huksOptions);
}
