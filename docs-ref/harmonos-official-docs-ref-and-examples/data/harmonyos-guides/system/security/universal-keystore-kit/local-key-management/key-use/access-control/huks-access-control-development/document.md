# HUKS Access Control Development

For details about scenarios and related concepts, see [HUKS Access Control Overview](../huks-access-control-overview/document.md).

#### How to Develop

## Generating a Key

Specify the fingerprint access control type and related properties.

When a key is generated or imported, set [HuksUserAuthType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksuserauthtype9), [HuksAuthAccessType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksauthaccesstype9), and [HuksChallengeType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#hukschallengetype9).

import { huks } from '@kit.UniversalKeystoreKit';
import { userAuth } from '@kit.UserAuthenticationKit';

const KEY\_ALIAS = 'test\_sm4\_key\_alias';
const IV = '1234567890123456';
const CIPHER\_IN\_DATA = 'Hks\_SM4\_Cipher\_Test\_101010101010101010110\_string';
const AUTH\_TYPE = userAuth.UserAuthType.PIN;
const AUTH\_TRUST\_LEVEL = userAuth.AuthTrustLevel.ATL1;

let sessionHandle: number;
let challenge: Uint8Array;
let authToken: Uint8Array;
let encryptedData: Uint8Array;

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
    value: huks.HuksKeyAlg.HUKS\_ALG\_SM4
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_ENCRYPT | huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_DECRYPT
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
  }
\];

/\* Generate a key. \*/
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
        console.info('Key generated successfully.');
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          const err = error instanceof Error ? error : new Error(String(error));
          throw err;
        } else {
          console.error('Failed to generate the key: ' + JSON.stringify(error));
        }
      });
  } catch (error) {
    console.error('Incorrect key generation parameter: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }
}

/\* Step 2: Initialize the session module. Initialize the encryption session and obtain the challenge value. \*/
const INIT\_SESSION\_PROPERTIES: huks.HuksParam\[\] = \[
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
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_CBC,
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_PADDING,
    value: huks.HuksKeyPadding.HUKS\_PADDING\_NONE,
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_IV,
    value: stringToUint8Array(IV),
  }
\];

/\* Initialize the session. \*/
function initSession(keyAlias: string, huksOptions: huks.HuksOptions,
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

/\* Initialize a session and obtain the challenge value. \*/
async function step2InitSession(): Promise<void> {
  const initOptions: huks.HuksOptions = {
    properties: INIT\_SESSION\_PROPERTIES,
    inData: new Uint8Array(\[\])
  };

  let throwObject: ThrowObject = { isThrow: true };
  try {
    await initSession(KEY\_ALIAS, initOptions, throwObject)
      .then((data) => {
        sessionHandle = data.handle;
        challenge = data.challenge as Uint8Array;
        console.info('Session initialized successfully. Challenge value: ' + challenge.toString());
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          const err = error instanceof Error ? error : new Error(String(error));
          throw err;
        } else {
          console.error('Session initialization failed: ' + JSON.stringify(error));
        }
      });
  } catch (error) {
    console.error('Session initialization parameter error: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }
}

## Obtaining an Authorization Token Through PIN Authentication

/\* Step 3: User authentication module - Obtain an authorization token through PIN authentication. \*/
/\* Executes user authentication. \*/
function performUserAuthentication(huksChallenge: Uint8Array): void {
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
    console.info('Authentication instance created successfully.');
  } catch (error) {
    console.error('Failed to create the authentication instance: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }

  /\* Subscribe to the authentication result. \*/
  try {
    auth.on('result', {
      onResult(result) {
        console.info('User authenticated successfully. Token obtained.');
        authToken = result.token;
        step4EncryptWithToken();
      }
    });
    console.info('Subscription to the authentication result succeeded.');
  } catch (error) {
    console.error('Failed to subscribe to the authentication result: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }

  /\* Start authentication. \*/
  try {
    auth.start();
    console.info('Waiting for the user to enter the PIN.');
  } catch (error) {
    console.error('Failed to start authentication: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }
}

## Encryption Using the Authentication Token

/\* Step 4: Encryption operation module - Use the authentication token to perform the encryption operation. \*/
/\* Set the encryption parameters. \*/
const ENCRYPT\_PROPERTIES: huks.HuksParam\[\] = \[
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

/\* Update the session. \*/
function updateSession(handle: number, huksOptions: huks.HuksOptions, token: Uint8Array,
  throwObject: ThrowObject): Promise<huks.HuksReturnResult> {
  return new Promise<huks.HuksReturnResult>((resolve, reject) => {
    try {
      huks.updateSession(handle, huksOptions, token, (error, data) => {
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

/\* Complete the session. \*/
function finishSession(handle: number, huksOptions: huks.HuksOptions, token: Uint8Array,
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

/\* Use the authentication token for encryption. \*/
async function step4EncryptWithToken(): Promise<void> {
  const encryptOptions: huks.HuksOptions = {
    properties: ENCRYPT\_PROPERTIES,
    inData: stringToUint8Array(CIPHER\_IN\_DATA)
  };

  /\* Update the session and pass the authentication token. \*/
  let throwObject: ThrowObject = { isThrow: true };
  try {
    await updateSession(sessionHandle, encryptOptions, authToken, throwObject)
      .then((data) => {
        console.info('Session updated successfully.');
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          const err = error instanceof Error ? error : new Error(String(error));
          throw err;
        } else {
          console.error('Session update failed: ' + JSON.stringify(error));
        }
      });
  } catch (error) {
    console.error('Session update parameter error: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }

  /\* Complete the session and pass the authentication token. \*/
  throwObject = { isThrow: false };
  try {
    await finishSession(sessionHandle, encryptOptions, authToken, throwObject)
      .then((data) => {
        encryptedData = data.outData as Uint8Array;
        console.info('Encryption completed.');

        /\* Verify the encryption result. \*/
        const originalData = stringToUint8Array(CIPHER\_IN\_DATA);
        if (encryptedData.toString() === originalData.toString()) {
          console.error('Encryption verification failed. The encrypted data is the same as the source data.');
        } else {
          console.info('Encryption verification succeeded. Data has been correctly encrypted.');
        }
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          const err = error instanceof Error ? error : new Error(String(error));
          throw err;
        } else {
          console.error('Session completion failed: ' + JSON.stringify(error));
        }
      });
  } catch (error) {
    console.error('Session completion parameter error: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }
}

/\* Main process entry - Execute the key generation, authentication, and encryption process. \*/
async function main(): Promise<void> {
  await step1GenerateKey();
  await step2InitSession();
  performUserAuthentication(challenge);
}
