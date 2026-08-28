# Refined Key Access Control Development

As an extension of the access control based on user identity authentication, the refined key access control provides fine-grained access control capabilities via secondary identity authentication based on biometric features and lock screen passwords. You can set whether identity authentication is required for a key in one or more scenarios such as encryption, decryption, signing, signature verification, key agreement, and key derivation.

For example, a service needs to use a HUKS key to encrypt the account password information. In this scenario, identity authentication is not required in encryption but required in decryption. To achieve this purpose, you can use the refined access control feature provided by HUKS.

To implement this feature, you only need to set **HuksTag** to **HUKS\_TAG\_KEY\_AUTH\_PURPOSE**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/5OvBubxsTlGd6G16JWMNPw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062011Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7338F4FA089148B0EA85107BDA697A2466A8E332703C9E142ADF46D36544822A)

For symmetric encryption and decryption, only the AES/CBC, AES/GCM, and SM4/CBC modes support fine-grained access control.

#### How to Develop

## Key Generation and Data Encryption

import { huks } from '@kit.UniversalKeystoreKit';
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

const KEY\_ALIAS = 'test\_sm4\_key\_alias';
const CIPHER\_IN\_DATA = 'Hks\_SM4\_Cipher\_Test\_101010101010101010110\_string'; // Plaintext
const IV = '1234567890123456'; // Initialization vector
const AUTH\_TYPE = userAuth.UserAuthType.PIN; // Authentication type: PIN
const AUTH\_TRUST\_LEVEL = userAuth.AuthTrustLevel.ATL1; // Authentication trust level

let sessionHandle = 0; // Session handle
let challenge: Uint8Array; // Challenge value
let authToken: Uint8Array; // Authentication token
let encryptedData: Uint8Array; // Ciphertext after encryption
let decryptedData: Uint8Array; // Plaintext after decryption

class ThrowObject {
  public isThrow: boolean = false;
}

function stringToUint8Array(str: string): Uint8Array {
  let arr: number\[\] = \[\];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

/\* Step 1: Key generation module \*/
const KEY\_GENERATION\_PROPERTIES: huks.HuksParam\[\] = \[
  {
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_SM4,
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT | huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT,
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_SM4\_KEY\_SIZE\_128,
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_CBC,
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_PADDING,
    value: huks.HuksKeyPadding.HUKS\_PADDING\_NONE,
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_USER\_AUTH\_TYPE,
    value: huks.HuksUserAuthType.HUKS\_USER\_AUTH\_TYPE\_PIN
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_AUTH\_ACCESS\_TYPE,
    value: huks.HuksAuthAccessType.HUKS\_AUTH\_ACCESS\_INVALID\_CLEAR\_PASSWORD
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_CHALLENGE\_TYPE,
    value: huks.HuksChallengeType.HUKS\_CHALLENGE\_TYPE\_NORMAL
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_AUTH\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT
  }
\];

function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject): Promise<void> {
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
      const err = error instanceof Error ? error : new Error(String(error));
      throw err;
    }
  });
}

/\* Generate an SM4 key. \*/
async function step1GenerateKey(): Promise<void> {
  const generateOptions: huks.HuksOptions = {
    properties: KEY\_GENERATION\_PROPERTIES,
    inData: new Uint8Array(\[\])
  };

  let throwObject: ThrowObject = { isThrow: true };
  try {
    await generateKeyItem(KEY\_ALIAS, generateOptions, throwObject)
      .then((data) => {
        console.info(\`Key generated successfully: ${JSON.stringify(data)}\`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          const err = error instanceof Error ? error : new Error(String(error));
          throw err;
        } else {
          console.error(\`Failed to generate the key: ${JSON.stringify(error)}\`);
        }
      });
  } catch (error) {
    console.error(\`Invalid key generation parameter: ${JSON.stringify(error)}\`);
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }
}

/\* Step 2: Encryption module \*/
const ENCRYPTION\_PROPERTIES: huks.HuksParam\[\] = \[
  {
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_SM4,
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT,
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_SM4\_KEY\_SIZE\_128,
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_PADDING,
    value: huks.HuksKeyPadding.HUKS\_PADDING\_NONE,
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_CBC,
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_IV,
    value: stringToUint8Array(IV),
  }
\];

function initEncryptSession(keyAlias: string, huksOptions: huks.HuksOptions,
  throwObject: ThrowObject): Promise<huks.HuksSessionHandle> {
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
      const err = error instanceof Error ? error : new Error(String(error));
      throw err;
    }
  });
}

function finishEncryptSession(handle: number, huksOptions: huks.HuksOptions,
  throwObject: ThrowObject): Promise<huks.HuksReturnResult> {
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
      const err = error instanceof Error ? error : new Error(String(error));
      throw err;
    }
  });
}

/\* Encrypt data. \*/
async function step2EncryptData(): Promise<void> {
  const encryptOptions: huks.HuksOptions = {
    properties: ENCRYPTION\_PROPERTIES,
    inData: new Uint8Array(\[\])
  };

  /\* Initialize the encryption session. \*/
  let throwObject: ThrowObject = { isThrow: true };
  try {
    await initEncryptSession(KEY\_ALIAS, encryptOptions, throwObject)
      .then((data) => {
        console.info(\`Encryption session initialized successfully: ${JSON.stringify(data)}\`);
        sessionHandle = data.handle as number;
        challenge = data.challenge as Uint8Array;
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          const err = error instanceof Error ? error : new Error(String(error));
          throw err;
        } else {
          console.error(\`Failed to initialize the encryption session: ${JSON.stringify(error)}\`);
        }
      });
  } catch (error) {
    console.error(\`Invalid initialization parameters for the encryption session: ${JSON.stringify(error)}\`);
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }

  /\* Execute the encryption operation. \*/
  encryptOptions.inData = stringToUint8Array(CIPHER\_IN\_DATA);
  throwObject = { isThrow: true };
  try {
    await finishEncryptSession(sessionHandle, encryptOptions, throwObject)
      .then((data) => {
        encryptedData = data.outData as Uint8Array;
        console.info(\`Data encrypted successfully: ${JSON.stringify(data)}\`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          const err = error instanceof Error ? error : new Error(String(error));
          throw err;
        } else {
          console.error(\`Data encryption failed: ${JSON.stringify(error)}\`);
        }
      });
  } catch (error) {
    console.error(\`Invalid data encryption parameter: ${JSON.stringify(error)}\`);
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }
}

## User Authentication

/\* Step 3: User authentication module \*/
function performUserAuthentication(huksChallenge: Uint8Array): void {
  /\* Set authentication parameters. \*/
  const authTypeList: userAuth.UserAuthType\[\] = \[AUTH\_TYPE\];
  const authParam: userAuth.AuthParam = {
    challenge: huksChallenge,
    authType: authTypeList,
    authTrustLevel: AUTH\_TRUST\_LEVEL
  };

  const widgetParam: userAuth.WidgetParam = {
    title: 'PIN',
  };

  /\* Obtain the authentication instance. \*/
  let auth: userAuth.UserAuthInstance;
  try {
    auth = userAuth.getUserAuthInstance(authParam, widgetParam);
    console.info('Authentication instance obtained successfully.');
  } catch (error) {
    console.error('Failed to obtain the authentication instance: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }

  /\* Subscribe to the authentication result. \*/
  try {
    auth.on('result', {
      onResult(result) {
        console.info('User authentication succeeded. Token obtained: ' + JSON.stringify(result));
        authToken = result.token;
        step32CompleteDecryption();
      }
    });
    console.info('Subscription to the authentication result succeeded.');
  } catch (error) {
    console.error('Failed to subscribe to the authentication result: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }

  try {
    auth.start();
    console.info('The authentication process has been started. Waiting for the user to enter the PIN...');
  } catch (error) {
    console.error('Failed to start authentication: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }
}

## Data Decryption and Verification

/\* Step 4: Decryption module \*/
const DECRYPTION\_PROPERTIES: huks.HuksParam\[\] = \[
  {
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_SM4,
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT,
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_SM4\_KEY\_SIZE\_128,
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_PADDING,
    value: huks.HuksKeyPadding.HUKS\_PADDING\_NONE,
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_CBC,
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_IV,
    value: stringToUint8Array(IV),
  }
\];

function initDecryptSession(keyAlias: string, huksOptions: huks.HuksOptions,
  throwObject: ThrowObject): Promise<huks.HuksSessionHandle> {
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
      const err = error instanceof Error ? error : new Error(String(error));
      throw err;
    }
  });
}

function finishDecryptSession(handle: number, huksOptions: huks.HuksOptions, token: Uint8Array,
  throwObject: ThrowObject): Promise<huks.HuksReturnResult> {
  return new Promise<huks.HuksReturnResult>((resolve, reject) => {
    try {
      huks.finishSession(handle, huksOptions, token, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throwObject.isThrow = true;
      const err = error instanceof Error ? error : new Error(String(error));
      throw err;
    }
  });
}

/\* Initialize the decryption session and trigger user authentication. \*/
async function step31DecryptionAndAuth(): Promise<void> {

  const decryptOptions: huks.HuksOptions = {
    properties: DECRYPTION\_PROPERTIES,
    inData: new Uint8Array(\[\])
  };

  /\* Initialize the decryption session and obtain the challenge value. \*/
  let throwObject: ThrowObject = { isThrow: true };
  try {
    await initDecryptSession(KEY\_ALIAS, decryptOptions, throwObject)
      .then((data) => {
        console.info(\`Decryption session initialized successfully: ${JSON.stringify(data)}\`);
        sessionHandle = data.handle as number;
        challenge = data.challenge as Uint8Array;
        console.info('Challenge value obtained: ' + challenge.toString());

        /\* Trigger the user authentication process. \*/
        performUserAuthentication(challenge);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          const err = error instanceof Error ? error : new Error(String(error));
          throw err;
        } else {
          console.error(\`Failed to initialize the decryption session: ${JSON.stringify(error)}\`);
        }
      });
  } catch (error) {
    console.error(\`Invalid initialization parameters for the decryption session: ${JSON.stringify(error)}\`);
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }
}

/\* Complete the decryption. \*/
async function step32CompleteDecryption(): Promise<void> {
  const decryptOptions: huks.HuksOptions = {
    properties: DECRYPTION\_PROPERTIES,
    inData: encryptedData // Use the previously encrypted ciphertext.
  };

  let throwObject: ThrowObject = { isThrow: true };
  try {
    await finishDecryptSession(sessionHandle, decryptOptions, authToken, throwObject)
      .then((data) => {
        decryptedData = data.outData as Uint8Array;
        console.info(\`Data decrypted successfully: ${JSON.stringify(data)}\`);

        /\* Verify the decryption result. \*/
        const originalData = stringToUint8Array(CIPHER\_IN\_DATA);
        if (decryptedData.toString() === originalData.toString()) {
          console.info('Decryption verification succeeded. The decrypted data is the same as the source plaintext.');
        } else {
          console.error ('Decryption verification failed. The decrypted data is different from the source plaintext.');
        }
      })
      .catch((error: BusinessError) => {
        if (throwObject.isThrow) {
          const err = error instanceof Error ? error : new Error(String(error));
          throw err;
        } else {
          console.error(\`Data decryption failed: ${JSON.stringify(error)}\`);
        }
      });
  } catch (error) {
    console.error(\`Invalid data decryption parameter: ${JSON.stringify(error)}\`);
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }
}

/\* Main function: Execute the complete SM4 encryption and decryption process. \*/
async function main(): Promise<void> {
    /\* Step 1: Generate a key. \*/
    await step1GenerateKey();
    /\* Step 2: Encrypt data. \*/
    await step2EncryptData();
    /\* Step 3: Initialize decryption and perform user authentication. \*/
    await step31DecryptionAndAuth();
}
