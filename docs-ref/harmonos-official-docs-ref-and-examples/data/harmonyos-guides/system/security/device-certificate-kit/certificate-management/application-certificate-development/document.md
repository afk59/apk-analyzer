# Application Certificate Development

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/Mx_3KNgBQMq4JkbsCADVcw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9AB9F6099B5D86F365B13973F0113C53287904D83ADF44C59FB6F3530F26478E)

The SDK of API version 11 or later must be used.

#### Scenarios

1.  Typical scenarios:
    
    -   Install an application certificate.
    -   Obtain an application certificate.
    -   Use an application certificate to sign or verify data.
    -   Uninstall an application certificate.
2.  Before installation, you need to know the algorithm types and the combinations of the signing and signature verification parameters supported by certificate management.
    
    -   Certificate management depends on the [Universal Keystore Kit](../../../universal-keystore-kit/about-this-kit/document.md) (HUKS) to install certificates and use the keys in the certificates for signing and signature verification.
    -   The algorithms supported by certificate management are a subset of HUKS cipher algorithm specifications. Currently, only the private certificates using the RSA, ECC, and SM2 algorithms can be installed and used.
    -   For details about the parameter combinations supported by signing and signature verification, see the description of RSA, ECC, and SM2 in [Signing and Signature Verification Overview and Algorithm Specifications](../../../universal-keystore-kit/local-key-management/key-use/signing-and-signature-verification/signing-and-signature-verification-overview-and-algorithm-specifications/document.md).

#### Available APIs

For details about the APIs, see [@ohos.security.certManager (Certificate Management Module)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-certmanager).

The following table describes the commonly used APIs.

| Instance | API | Description |
| :-- | :-- | :-- |
| certificateManager | installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string, callback: AsyncCallback<CMResult>) : void | Installs an application certificate. This API uses an asynchronous callback to return the result. |
| certificateManager | installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string) : Promise<CMResult> | Installs an application certificate. This API uses a promise to return the result. |
| certificateManager | installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string, level: AuthStorageLevel) : Promise<CMResult>18+ | Installs an application certificate and specifies the certificate storage level. This API uses a promise to return the result. |
| certificateManager | getPrivateCertificate(keyUri: string, callback: AsyncCallback<CMResult>) : void | Obtains an application certificate. This API uses an asynchronous callback to return the result. |
| certificateManager | getPrivateCertificate(keyUri: string) : Promise<CMResult> | Obtains an application certificate. This API uses a promise to return the result. |
| certificateManager | uninstallPrivateCertificate(keyUri: string, callback: AsyncCallback<void>) : void | Uninstalls an application certificate. This API uses an asynchronous callback to return the result. |
| certificateManager | uninstallPrivateCertificate(keyUri: string) : Promise<void> | Uninstalls an application certificate. This API uses a promise to return the result. |
| certificateManager | init(authUri: string, spec: CMSignatureSpec, callback: AsyncCallback<CMHandle>) : void | Initializes the signing or signature verification operation. This API uses an asynchronous callback to return the result. |
| certificateManager | init(authUri: string, spec: CMSignatureSpec) : Promise<CMHandle> | Initializes signing or signature verification. This API uses a promise to return the result. |
| certificateManager | update(handle: Uint8Array, data: Uint8Array, callback: AsyncCallback<void>) : void | Updates the data to be signed or verified. This API uses an asynchronous callback to return the result. |
| certificateManager | update(handle: Uint8Array, data: Uint8Array) : Promise<void> | Updates the data to be signed or verified. This API uses a promise to return the result. |
| certificateManager | finish(handle: Uint8Array, callback: AsyncCallback<CMResult>) : void | Finishes the signing operation. This API uses an asynchronous callback to return the result. |
| certificateManager | finish(handle: Uint8Array, signature: Uint8Array, callback: AsyncCallback<CMResult>) : void | Finishes the signing operation. This API uses an asynchronous callback to return the result. |
| certificateManager | finish(handle: Uint8Array, signature?: Uint8Array) : Promise<CMResult> | Finishes signing or signature verification. This API uses a promise to return the result. |
| certificateManager | abort(handle: Uint8Array, callback: AsyncCallback<void>) : void | Aborts signing or signature verification. This API uses a callback to return the result. |
| certificateManager | abort(handle: Uint8Array) : Promise<void> | Aborts signing or signature verification. This API uses a promise to return the result. |

#### How to Develop

1.  Request and declare permissions.
    
    Required permission: **ohos.permission.ACCESS\_CERT\_MANAGER**
    
    For details about how to request permissions, see [Workflow for Requesting Permissions](../../../application-access-control/application-permission-management/requesting-application-permissions/workflow-for-requesting-permissions/document.md).
    
    For details about how to declare permissions, see [Declaring Permissions](../../../application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).
    
2.  Import the required module.
    
    import { certificateManager } from '@kit.DeviceCertificateKit';
    
3.  Install an application certificate, obtain the certificate, use it to sign and verify data. Then, uninstall the certificate.
    
    import { certificateManager } from '@kit.DeviceCertificateKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { util } from '@kit.ArkTS';
    
    async function privateCredSample() {
      /\* The data of the certificate to be installed must be assigned based on the service. The data in this example is not the real certificate data. \*/
      let keystoreBase64Str = 'MIIMJgIBAzCCC+AGCSqGSIb3DQEHAaCCC9EEggvNMIILyTCCBW4GCSqGSIb3DQEH' +
        // ...
        'G615kxCjeS6uixCHuij3pgQUhHiChcSeohRPrVkVPSPmYr9tjAYCAgQA';
      /\* Convert credential data to Uint8Array, where the credential data is in DER format \*/
      let keystore: Uint8Array = new util.Base64Helper().decodeSync(keystoreBase64Str);
    
      /\* Keystore password of the certificate to be installed. \*/
      let keystorePwd: string = 'huawei';
      let appKeyUri: string = '';
      try {
        /\* Install an application certificate. \*/
        const res: certificateManager.CMResult = await certificateManager.installPrivateCertificate(keystore, keystorePwd, 'testPriCredential');
        appKeyUri = (res.uri != undefined) ? res.uri : '';
        console.info(\`InstallPrivateCertificate success appKeyUri: ${appKeyUri}\`);
      } catch (err) {
        let e: BusinessError = err as BusinessError;
        console.error(\`Failed to install private certificate. Code: ${e.code}, message: ${e.message}\`);
      }
    
      try {
        /\* Obtain the application certificate. \*/
        let res: certificateManager.CMResult = await certificateManager.getPrivateCertificate(appKeyUri);
        if (res === undefined || res.credential == undefined) {
          console.error('The result of getting private certificate is undefined.');
        } else {
          let credential = res.credential;
          console.info('Succeeded in getting private certificate.');
        }
      } catch (err) {
        console.error(\`Failed to get private certificate. Code: ${err.code}, message: ${err.message}\`);
      }
    
      try {
        /\* srcData is the data to be signed and verified. \*/
        let srcData: Uint8Array = new Uint8Array(\[
          0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01,
        \]);
    
        /\* Construct the parameters used for signing. \*/
        const signSpec: certificateManager.CMSignatureSpec = {
          purpose: certificateManager.CmKeyPurpose.CM\_KEY\_PURPOSE\_SIGN,
          padding: certificateManager.CmKeyPadding.CM\_PADDING\_PSS,
          digest: certificateManager.CmKeyDigest.CM\_DIGEST\_SHA256
        };
    
        /\* Generate a signature. \*/
        const signHandle: certificateManager.CMHandle = await certificateManager.init(appKeyUri, signSpec);
        await certificateManager.update(signHandle.handle, srcData);
        const signResult: certificateManager.CMResult = await certificateManager.finish(signHandle.handle);
    
        /\* Construct the parameters for signature verification. \*/
        const verifySpec: certificateManager.CMSignatureSpec = {
          purpose: certificateManager.CmKeyPurpose.CM\_KEY\_PURPOSE\_VERIFY,
          padding: certificateManager.CmKeyPadding.CM\_PADDING\_PSS,
          digest: certificateManager.CmKeyDigest.CM\_DIGEST\_SHA256
        };
    
        /\*\* Verify the signature. \*/
        const verifyHandle: certificateManager.CMHandle = await certificateManager.init(appKeyUri, verifySpec);
        await certificateManager.update(verifyHandle.handle, srcData);
        const verifyResult = await certificateManager.finish(verifyHandle.handle, signResult.outData);
        console.info('Succeeded in signing and verifying.');
      } catch (err) {
        let e: BusinessError = err as BusinessError;
        console.error(\`Failed to sign or verify. Code: ${e.code}, message: ${e.message}\`);
      }
    
      try {
        /\* Uninstall the application certificate. \*/
        await certificateManager.uninstallPrivateCertificate(appKeyUri);
      } catch (err) {
        let e: BusinessError = err as BusinessError;
        console.error(\`Failed to uninstall private certificate. Code: ${e.code}, message: ${e.message}\`);
      }
    }
