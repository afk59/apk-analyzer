# Password-based Transaction Authentication

#### Use Cases

In the password-based transaction authentication scenario, the created digital shield password can be used to authenticate the transaction information, and the signature verification function provided by Universal Keystore Kit can be used to check whether transaction information has been tampered with, thereby enhancing security of the entire transaction process.

#### Restrictions

Currently, this function is supported only on phones.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/aSqv9nArSUqu6EGSQ17tCA/en-us_image_0000002515114407.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE00C10357BE0ECC22634A66818F8F7818489E9A4D5399CBFF39903C55DCA737 "Click to enlarge")

#### API Description

For details about the API, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-arktsapi-errcode-trusted-auth).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[procContentAuthentication](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-trusted-auth-api#section1381398185415)(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise<AuthToken>

 | 

Processes transaction information.

 |

#### Development Procedure

1.  Import the huks module, trustedAuthentication module, and dependent modules.
    
    import { resourceManager } from '@kit.LocalizationKit'
    import { huks } from '@kit.UniversalKeystoreKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { trustedAuthentication } from '@kit.DeviceSecurityKit';
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { common } from '@kit.AbilityKit';
    import { util } from '@kit.ArkTS';
    
2.  Before initiating transaction authentication, retrieve the **authID** value obtained during [digital shield password setup](../digital-shield-password-management/setting-the-digital-shield-password/document.md) from the server for the current account.
3.  Initialize the signature session. For details, please refer to [Signing and Signature Verification](../../../universal-keystore-kit/local-key-management/key-use/signing-and-signature-verification/signing-and-signature-verification-arkts/document.md) of Universal Keystore Kit.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/z5mVCh2lT9m4B_9Lk32aVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A63BFE692896A8AF396885A3906560AFB6B787E3F9454D1A46D773198E2434C)
    
    -   When setting the signature key, set **tag: huks.HuksTag.HUKS\_TAG\_KEY\_SECURE\_SIGN\_TYPE** to **huks.HuksSecureSignType.HUKS\_SECURE\_SIGN\_WITH\_AUTHINFO** in the key property set, to perform signature verification on the attached transaction information.
    
      // Example of setting signature key properties.
      let properties: Array<huks.HuksParam> = \[{
        tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
        value: huks.HuksKeyAlg.HUKS\_ALG\_ECC
      }, {
        tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
        value: huks.HuksKeySize.HUKS\_AES\_KEY\_SIZE\_256
      }, {
        tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
        value: huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_SIGN
      }, {
        tag: huks.HuksTag.HUKS\_TAG\_DIGEST,
        value: huks.HuksKeyDigest.HUKS\_DIGEST\_SHA256
      }, 
      // Indicates that signature authentication is performed on the attached transaction information.
      {
        tag: huks.HuksTag.HUKS\_TAG\_KEY\_SECURE\_SIGN\_TYPE,
        value: huks.HuksSecureSignType.HUKS\_SECURE\_SIGN\_WITH\_AUTHINFO
      }\];
    
4.  Call the transaction authentication API to initiate a password-based transaction authentication request. After the password is authenticated, the **authToken** carrying the transaction information hash is obtained.
    
    async function ContentVerifyByPwd(challenge: Uint8Array, context: common.UIAbilityContext):Promise<trustedAuthentication.AuthToken> {
      try {
        const authID: bigint = 11842183505170721246n;// In actual use, replace the value with the **authID** of the account obtained from the server.
        const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
        const fileData : Uint8Array = await resourceMgr.getRawFileContent('test\_logo\_rgba.png'); // In actual use, replace the value with the name of the app logo image to be displayed on the TUI.
        const reqParams:trustedAuthentication.AuthReqParams = {
          reqType: trustedAuthentication.AuthType.AUTH\_TYPE\_TUI\_PIN,
          authContent: \["User: John xx", "Account: 95588180804408xxxx", "Transaction amount: 1000000000"\],// Replace the value with the actual transaction information. Each element in the array occupies one line in the transaction information on the screen.
        }
        const buffer = fileData.buffer;
        const label:trustedAuthentication.TUILable = {
          image: buffer as ArrayBuffer,
          title: "Password-based Transaction Authentication",
        }
        const result = await trustedAuthentication.procContentAuthentication(challenge, authID, reqParams, label);
        return result;
      } catch (err) {  
       hilog.error(0x0000, 'testTag', \`Failed to procContentAuthentication, code:${err.code}, message:${err.message}\`);
       throw new Error('Content verify by password failed:' + (err as BusinessError).message);
     }
    }
    const rand = cryptoFramework.createRandom();
    const len: number = 32;
    const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;// In actual use, replace the value with the challenge obtained from Universal Keystore Kit during session initialization.
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const authToken: trustedAuthentication.AuthToken = await ContentVerifyByPwd(challenge, context);
    
5.  Perform signature verification on the **authToken** data of the transaction information by referring to [ECC/SHA-256/Signature type with authentication information](../../../universal-keystore-kit/local-key-management/key-use/signing-and-signature-verification/signing-and-signature-verification-arkts/document.md#eccsha-256signature-type-with-authentication-information) of Universal Keystore Kit. Then end the session.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/E702zpXBRV-54qxAWVDA1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71A16FF77342570FB236F971393DE7C16340BA0D16FDEB0085F495896619146B)
    
    The input transaction information during transaction authentication is in the following format:
    
    // Example transaction information.
    authContent: \["User: John xx", "Account: 95588180804408xxxx", "Transaction amount: 1000000000"\];
    
    Since **inputData** for signature verification by Universal Keystore Kit is a Uint8Array, you need to combine all the elements in the transaction information using **\\n** and then convert the result from UTF-8 into a Uint8Array.
    
    function encodeUtf8(s: string): number\[\] {
      const encoder = new util.TextEncoder();
    
      const dest = new Uint8Array(s.length \* 4);
      const result = encoder.encodeIntoUint8Array(s, dest);
      const encodedBytes = dest.subarray(0, result.written);
      return Array.from(encodedBytes);
    };
    // Signature verification data transferred by the app to Universal Keystore Kit.
    let str = "User: John xx\\nAccount: 95588180804408xxxx\\nTransaction amount: 1000000000";
    const utf8Bytes = new Uint8Array(encodeUtf8(str));
    
6.  Verify the signature data by referring to [Signing and Signature Verification](../../../universal-keystore-kit/local-key-management/key-use/signing-and-signature-verification/signing-and-signature-verification-arkts/document.md) of Universal Keystore Kit. If the signature verification is successful, the bank transfer can be completed for the corresponding account.
