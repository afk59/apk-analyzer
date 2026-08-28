# CMAC (ArkTS)

Cipher-based Message Authentication Code (CMAC) is a type of message authentication code (MAC) based on block ciphers. Currently, it supports 3DES.

#### How to Develop

**Key Generation**

1\. Obtain the parameters for key generation.

2\. Call [generateKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksgeneratekeyitem9) to generate a 128-bit key.

Alternatively, you can import a key. For details about the specifications, see [Supported Algorithms](../../../key-generation-and-import/key-import/key-import-overview-and-algorithm-specifications/document.md#supported-algorithms).

**CMAC Generation**

1.  Obtain CMAC algorithm parameter settings.
2.  Call [initSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksinitsession9) to initialize the key session and obtain the session handle.
3.  Call [finishSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksfinishsession9) to end the key session and obtain the MAC data.

_/\*_
\* Perform CMAC operation using promise-based APIs.
 _\*/_
**import** { huks } **from** '@kit.UniversalKeystoreKit';

**let** cmacKeyAlias = 'test\_cmac';
**let** handle: number;
**let** plainText = '123456';
**let** IV = '12345678';
**let** macData: Uint8Array;

**function** **StringToUint8Array**(str: String) {
  **let** arr: number\[\] = **new** Array();
  **for** (**let** i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  **return** **new** Uint8Array(arr);
}

**function** **Uint8ArrayToString**(fileData: Uint8Array) {
  **let** dataString = '';
  **for** (**let** i = 0; i < fileData.length; i++) {
    dataString += String.fromCharCode(fileData\[i\]);
  }
  **return** dataString;
}

**function** **GenerateKeyProperties**() {
  **const** properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_3DES
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_3DES\_KEY\_SIZE\_128
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_MAC
  }\];
  **return** properties;
}

**function** **GetCmacProperties**() {
  **const** properties: Array<huks.HuksParam> = \[{
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_CMAC
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_3DES\_KEY\_SIZE\_128
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_MAC
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_CBC
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_PADDING,
    value: huks.HuksKeyPadding.HUKS\_PADDING\_ISO\_IEC\_9797\_1
  }, {
    tag: huks.HuksTag.HUKS\_TAG\_IV,
    value: StringToUint8Array(IV)
  }\];
  **return** properties;
}

**async** **function** **GenerateCmacKey**() {
 _/\*_
  \* 1.1 Obtain the parameters for key generation.
  _\*/_
  **let** genProperties = GenerateKeyProperties();
  **let** options: huks.HuksOptions = {
    properties: genProperties
  }
 _/\*_
  \* 1.2 Call generateKeyItem to generate a key.
  _\*/_
  **await** huks.generateKeyItem(cmacKeyAlias, options)
    .then((data) => {
      console.info(\`promise: generate cmac key success\`);
    }).catch((error: Error) => {
      console.error(\`promise: generate cmac key failed, ${JSON.stringify(error)}\`);
    })
}

**async** **function** **CmacData**() {
 _/\*_
  \* 2.1 Obtain CMAC algorithm parameter settings.
  _\*/_
  **let** cmacProperties = GetCmacProperties();
  **let** options: huks.HuksOptions = {
    properties: cmacProperties,
    inData: StringToUint8Array(plainText)
  }
 _/\*_
  \* 2.2 Call initSession to obtain a session handle.
  _\*/_
  **await** huks.initSession(cmacKeyAlias, options)
    .then((data) => {
      handle = data.handle;
  }).catch((error: Error) => {
    console.error(\`promise: init EncryptData failed, ${JSON.stringify(error)}\`);
  })
 _/\*_
  \* 2.3 Call finishSession to obtain the CMAC result.
  _\*/_
  **await** huks.finishSession(handle, options)
    .then((data) => {
      console.info(\`promise: cmac data success, data is \` + Uint8ArrayToString(data.outData **as** Uint8Array));
      macData = data.outData **as** Uint8Array;
    }).catch((error: Error) => {
      console.error(\`promise: cmac data failed, ${JSON.stringify(error)}\`);
    })
}
