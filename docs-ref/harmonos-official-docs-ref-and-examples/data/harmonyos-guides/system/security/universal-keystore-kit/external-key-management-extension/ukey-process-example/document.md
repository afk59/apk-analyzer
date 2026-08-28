# Ukey Process Example

#### Development Modes

Currently, the following development modes are available for two-way SSL authentication:

## Browser Uses System ArkWeb Capabilities and a Custom Client

1.  The application on the device calls the certificate management capability to open the certificate selection dialog box, waits for the user to select a certificate, and obtains the [keyUri](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-certmanagerdialog#certreference22) as the resource ID.
    
2.  The application listens to the PIN authentication callback, processes the event, and calls the certificate management capability to open the PIN authentication dialog box.
    
3.  The certificate management capability returns the authentication result to the application on the device, and the application returns the result to the ArkWeb component.
    

## Browser Uses a Custom Web Component and a Custom Client

1.  The application on the device calls the certificate management capability to open the certificate selection dialog box, waits for the user to select a certificate, obtains the [keyUri](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-certmanagerdialog#certreference22) as the resource ID, and transparently passes it to the **Web** component.
    
2.  The **Web** component obtains the certificate data through certificate management, uses the [keyUri](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-certmanagerdialog#certreference22) as the resource ID to call the resource opening API of the HUKS, and queries the PIN authentication status.
    
3.  Perform the following operations based on the authentication result:
    
    -   If the authentication is not performed, the application on the device needs to start PIN authentication. In this case, the application receives the authentication request, processes the event, and calls the certificate management capability to open the PIN authentication dialog box. After obtaining the authentication result, the application returns the result to the **Web** component and then performs the authenticated process.
    -   If the authentication is successful, the **Web** component can directly call the [initSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksinitsession9)/[updateSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksupdatesession9)/[finishSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksfinishsession9) APIs of HUKS for signing.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/VvfR0Mz7RI-U96ebDw0Ywg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062013Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D78A33468A686700C951AF3C021DE4A101028A820A0973D6F9E93B744226A943)

To call the three-stage capabilities of the underlying extension, the parameters passed must contain [OH\_HUKS\_TAG\_KEY\_CLASS](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-type-h#oh_huks_tag), with its value set to [OH\_HUKS\_KEY\_CLASS\_EXTENSION](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-type-h#oh_huks_keyclasstype).

#### Example

The following is an example of using the system capability for two-way SSL authentication in a browser.

1.  The application on the device calls the certificate management capability to open the certificate selection dialog box [certificateManagerDialog.openAuthorizeDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-certmanagerdialog#certificatemanagerdialogopenauthorizedialog22) and waits for the user to select a certificate.
    
    import { certificateManagerDialog, certificateManager } from '@kit.DeviceCertificateKit';
    import { BusinessError } from '@kit.BasicservicesKit';
    import { common } from '@kit.AbilityKit';
    import { UIContext } from '@kit.ArkUI';
    
    /\* context is application context information, which is obtained by the caller. The context here is only an example. \*/
    let context: common.Context = new UIContext().getHostContext() as common.Context;
    let certTypes: Array<certificateManagerDialog.CertificateType> = \[
      certificateManagerDialog.CertificateType.CREDENTIAL\_USER,
      certificateManagerDialog.CertificateType.CREDENTIAL\_APP,
      certificateManagerDialog.CertificateType.CREDENTIAL\_UKEY
    \];
    let certPurpose: certificateManager.CertificatePurpose = certificateManager.CertificatePurpose.PURPOSE\_DEFAULT;
    let authorizeRequest: certificateManagerDialog.AuthorizeRequest = { certTypes: certTypes, certPurpose: certPurpose };
    try {
      certificateManagerDialog.openAuthorizeDialog(context, authorizeRequest).then((certReference: certificateManagerDialog.CertReference) => {
        /\* Record the keyUri obtained in the certificate selection dialog box for future use.\*/
        let keyUri = certReference.keyUri;
        console.info(\`Succeeded in opening authorize dialog.\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to open authorize dialog. Code: ${err.code}, message: ${err.message}\`);
      });
    } catch (err) {
      let error = err as BusinessError;
      console.error(\`Failed to open authorize dialog. Code: ${error.code}, message: ${error.message}\`);
    }
    
2.  The **Web** component parses the certificate, calls the HUKS to open the resource, and queries the PIN authentication status.
    
    First, call the NDK API of certificate management, OH\_CertManager\_GetUkeyCertificate\](../../reference/apis-device-certificate-kit/capi-cm-native-api-h.md#oh\_certmanager\_getukeycertificate), to parse the certificate selected by the user and obtain the corresponding certificate data.
    
    Next, use **keyUri** selected by the user as the resource ID to call the HUKS NDK API, [OH\_Huks\_OpenResource](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-external-crypto-api-h#oh_huks_openresource) to open the resource.
    
    Finally, call the HUKS NDK API [OH\_Huks\_GetUkeyPinAuthState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-external-crypto-api-h#oh_huks_getukeypinauthstate) to query the PIN authentication status.
    
    #include "huks/native\_huks\_external\_crypto\_api.h"
    #include "huks/native\_huks\_param.h"
    #include <device\_certificate/certmanager/cm\_native\_api.h>
    #include <device\_certificate/certmanager/cm\_native\_type.h>
    #include "napi/native\_api.h"
    #include <string.h>
    
    /\* 1. Call the NDK API of certificate management to parse the certificate selected by the user and obtain the corresponding certificate data. \*/
    static napi\_value GetUkeyCert(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value argv\[1\] = { nullptr };
        napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
        if (argc != 1) {
            return nullptr;
        }
        /\* Obtain the keyUri length. \*/
        size\_t length = 0;
        napi\_get\_value\_string\_utf8(env, argv\[0\], nullptr, 0, &length);
        /\* Obtain the value of keyUri.\*/
        char \*keyUriBuffer = static\_cast<char\*>(malloc(length + 1));
        size\_t result = 0;
        napi\_get\_value\_string\_utf8(env, argv\[0\], keyUriBuffer, length + 1, &result);
        OH\_CM\_Blob keyUri = { static\_cast<uint32\_t>(length + 1), (uint8\_t\*)keyUriBuffer };
    
        /\* Define input parameter UkeyInfo. \*/
        OH\_CM\_UkeyInfo ukeyInfo = { OH\_CM\_CERT\_PURPOSE\_SIGN }; /\* USB credential attributes. The value is omitted here. \*/
    
        /\* Obtain the Ukey certificate details corresponding to keyUri. \*/
        OH\_CM\_CredentialDetailList credentialList = { 0, nullptr };
        int32\_t ret = OH\_CertManager\_GetUkeyCertificate(&keyUri, &ukeyInfo, &credentialList);
    
        /\* Release the memory after the call is complete. \*/
        OH\_CertManager\_FreeUkeyCertificate(&credentialList);
        free(keyUriBuffer);
        /\* Return the call result. \*/
        napi\_value retNapi;
        napi\_create\_int32(env, ret, &retNapi);
        return retNapi;
    }
    
    /\* 2. Call the NDK API of HUKS to open the resource based on the keyUri selected by the user as resourceId. \*/
    OH\_Huks\_Result InitParamSet(struct OH\_Huks\_ExternalCryptoParamSet \*\*paramSet,
        const struct OH\_Huks\_ExternalCryptoParam \*params, uint32\_t paramCount)
    {
        OH\_Huks\_Result ret = OH\_Huks\_InitExternalCryptoParamSet(paramSet);
        if (ret.errorCode != OH\_HUKS\_SUCCESS) {
            return ret;
        }
        ret = OH\_Huks\_AddExternalCryptoParams(\*paramSet, params, paramCount);
        if (ret.errorCode != OH\_HUKS\_SUCCESS) {
            OH\_Huks\_FreeExternalCryptoParamSet(paramSet);
            return ret;
        }
        ret = OH\_Huks\_BuildExternalCryptoParamSet(paramSet);
        if (ret.errorCode != OH\_HUKS\_SUCCESS) {
            OH\_Huks\_FreeExternalCryptoParamSet(paramSet);
            return ret;
        }
        return ret;
    }
    
    static struct OH\_Huks\_ExternalCryptoParam g\_openResourceParamsTest\[\] = {};
    
    static napi\_value OpenResource(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value argv\[1\] = { nullptr };
        napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
        if (argc != 1) {
            return nullptr;
        }
        /\* Obtain the keyUri length. \*/
        size\_t length = 0;
        napi\_get\_value\_string\_utf8(env, argv\[0\], nullptr, 0, &length);
        /\* Obtain the value of keyUri.\*/
        char \*keyUriBuffer = static\_cast<char\*>(malloc(length + 1));
        size\_t result = 0;
        napi\_get\_value\_string\_utf8(env, argv\[0\], keyUriBuffer, length + 1, &result);
        OH\_Huks\_Blob resourceId = {.size = static\_cast<uint32\_t>(length), .data = (uint8\_t\*)keyUriBuffer};
    
        struct OH\_Huks\_ExternalCryptoParamSet \*openResourceParamSet = nullptr;
        OH\_Huks\_Result ohResult;
        do {
            ohResult = InitParamSet(&openResourceParamSet, g\_openResourceParamsTest,
                sizeof(g\_openResourceParamsTest) / sizeof(OH\_Huks\_ExternalCryptoParam));
            if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
                break;
            }
            ohResult = OH\_Huks\_OpenResource(&resourceId, openResourceParamSet);
            if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
                break;
            }
        } while (0);
        free(keyUriBuffer);
        OH\_Huks\_FreeExternalCryptoParamSet(&openResourceParamSet);
    
        OH\_Huks\_Result res = OH\_Huks\_OpenResource(&resourceId, openResourceParamSet);
        napi\_value ret;
        napi\_create\_int32(env, res.errorCode, &ret);
        return ret;
    }
    
    /\* 3. Call the NDK API of the HUKS to query the PIN authentication status. \*/
    static struct OH\_Huks\_ExternalCryptoParam g\_getPinStateParamsTest\[\] = {};
    
    static napi\_value GetUkeyPinAuthState(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value argv\[1\] = { nullptr };
        napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
        if (argc != 1) {
            return nullptr;
        }
        /\* Obtain the keyUri length. \*/
        size\_t length = 0;
        napi\_get\_value\_string\_utf8(env, argv\[0\], nullptr, 0, &length);
        /\* Obtain the value of keyUri.\*/
        char \*keyUriBuffer = static\_cast<char\*>(malloc(length + 1));
        size\_t result = 0;
        napi\_get\_value\_string\_utf8(env, argv\[0\], keyUriBuffer, length + 1, &result);
        OH\_Huks\_Blob resourceId = {.size = static\_cast<uint32\_t>(length), .data = (uint8\_t\*)keyUriBuffer};
    
        struct OH\_Huks\_ExternalCryptoParamSet \*pinStateParamSet = nullptr;
        OH\_Huks\_ExternalPinAuthState authState = OH\_HUKS\_EXT\_CRYPTO\_PIN\_NO\_AUTH;
        OH\_Huks\_Result ohResult;
        do {
            ohResult = InitParamSet(&pinStateParamSet, g\_getPinStateParamsTest,
                sizeof(g\_getPinStateParamsTest) / sizeof(OH\_Huks\_ExternalCryptoParam));
            if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
                break;
            }
            ohResult = OH\_Huks\_GetUkeyPinAuthState(&resourceId, pinStateParamSet, &authState);
            if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
                break;
            }
        } while (0);
        free(keyUriBuffer);
        OH\_Huks\_FreeExternalCryptoParamSet(&pinStateParamSet);
    
        napi\_value ret;
        napi\_create\_int32(env, ohResult.errorCode, &ret);
        return ret;
    }
    
    /\* 4. Define and register APIs. \*/
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            { "getUkeyCert", nullptr, GetUkeyCert, nullptr, nullptr, nullptr, napi\_default, nullptr },
            { "openResource", nullptr, OpenResource, nullptr, nullptr, nullptr, napi\_default, nullptr },
            { "getUkeyPinAuthState", nullptr, GetUkeyPinAuthState, nullptr, nullptr, nullptr, napi\_default, nullptr },
        };
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    
    static napi\_module demoModule = {
        .nm\_version =1,
        .nm\_flags = 0,
        .nm\_filename = nullptr,
        .nm\_register\_func = Init,
        .nm\_modname = "hello",
        .nm\_priv = ((void\*)0),
        .reserved = { 0 },
    };
    extern "C" \_\_attribute\_\_((constructor)) void RegisterHelloModule(void)
    {
        napi\_module\_register(&demoModule);
    }
    
    The corresponding d.ts API declaration is as follows:
    
    export function getUkeyCert(keyUri: string): number;
    
    export function openResource(keyUri: string): number;
    
    export function getUkeyPinAuthState(keyUri: string): number;
    
    The API call method is as follows:
    
    import testNapi from "libentry.so";
    @Entry
    @Component
    struct Index {
        /\* Obtain the value through the certificate dialog box API.\*/
        @State keyUri: string = 'Hello World';
        build() {
            Row() {
            Column() {
                Text('Hello World')
                .fontSize(50)
                .fontWeight(FontWeight.Bold)
                .onClick(() => {
                    testNapi.getUkeyCert(keyUri);
                    testNapi.openResource(keyUri);
                    testNapi.getUkeyPinAuthState(keyUri);
                })
            }
            .width('100%')
            }
            .height('100%')
        }
    }
    
3.  Perform the following operations based on the authentication result:
    
    If the authentication is not performed, the application needs to start PIN authentication. In this case, the device application receives the authentication request, processes the event, and calls the certificate management capability to open the PIN authentication dialog box [certificateManagerDialog.openUkeyAuthDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-certmanagerdialog#certificatemanagerdialogopenukeyauthdialog22). After obtaining the authentication result, the application returns the result to the **Web** component and then performs the authenticated process.
    
    /\* Open the PIN authentication dialog box through certificate management. \*/
    import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { common } from '@kit.AbilityKit';
    import { UIContext } from '@kit.ArkUI';
    
    /\* context is application context information, which is obtained by the caller. The context here is only an example. \*/
    let context: common.Context = new UIContext().getHostContext() as common.Context;
    /\* keyUri is the unique identifier of the credential. The value has been recorded in step 1. The value here is only an example. \*/
    let keyUri: string = "testKeyAlias";
    let ukeyAuthRequest: certificateManagerDialog.UkeyAuthRequest = { keyUri: keyUri };
    try {
      certificateManagerDialog.openUkeyAuthDialog(context, ukeyAuthRequest)
        .then(() => {
          console.info(\`Succeeded in opening ukey authorization dialog.\`);
        }).catch((err: BusinessError) => {
          console.error(\`Failed to open ukey authorization dialog. Code: ${err.code}, message: ${err.message}\`);
        });
    } catch (err) {
      let error = err as BusinessError;
      console.error(\`Failed to open ukey authorization dialog. Code: ${error.code}, message: ${error.message}\`);
    }
    
    If the authentication is successful, the **Web** component can directly call the three-stage HUKS APIs for signing.
    
    /\* Call the three-stage HUKS APIs to obtain the signed data.\*/
    #include "huks/native\_huks\_api.h"
    #include "huks/native\_huks\_param.h"
    #include "napi/native\_api.h"
    #include <string.h>
    
    OH\_Huks\_Result InitParamSet(struct OH\_Huks\_ParamSet \*\*paramSet,
        const struct OH\_Huks\_Param \*params, uint32\_t paramCount)
    {
        OH\_Huks\_Result ret = OH\_Huks\_InitParamSet(paramSet);
        if (ret.errorCode != OH\_HUKS\_SUCCESS) {
            return ret;
        }
        ret = OH\_Huks\_AddParams(\*paramSet, params, paramCount);
        if (ret.errorCode != OH\_HUKS\_SUCCESS) {
            OH\_Huks\_FreeParamSet(paramSet);
            return ret;
        }
        ret = OH\_Huks\_BuildParamSet(paramSet);
        if (ret.errorCode != OH\_HUKS\_SUCCESS) {
            OH\_Huks\_FreeParamSet(paramSet);
            return ret;
        }
        return ret;
    }
    
    static struct OH\_Huks\_Param g\_signParamsTest\[\] = {
        {
            .tag = OH\_HUKS\_TAG\_ALGORITHM,
            .uint32Param = OH\_HUKS\_ALG\_RSA
        }, {
            .tag = OH\_HUKS\_TAG\_PURPOSE,
            .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_SIGN
        }, {
            .tag = OH\_HUKS\_TAG\_KEY\_SIZE,
            .uint32Param = OH\_HUKS\_RSA\_KEY\_SIZE\_2048
        }, {
            .tag = OH\_HUKS\_TAG\_PADDING,
            .uint32Param = OH\_HUKS\_PADDING\_PSS
        }, {
            .tag = OH\_HUKS\_TAG\_DIGEST,
            .uint32Param = OH\_HUKS\_DIGEST\_SHA384
        }, {
            .tag = OH\_HUKS\_TAG\_KEY\_CLASS,
            .uint32Param = OH\_HUKS\_KEY\_CLASS\_EXTENSION
        }
    };
    
    static const uint32\_t RSA\_COMMON\_SIZE = 1024;
    static const char \*DATA\_TO\_SIGN = "testData";
    // The value of keyAlias can be obtained by referring to the method of obtaining the value of resourceId in step 2. The value of keyAlias here is only an example.
    static const char \*KEY\_ALIAS = "testKeyAlias";
    
    static napi\_value Sign(napi\_env env, napi\_callback\_info info)
    {
        // Assume that \*\*g\_keyAlias\*\* is the obtained resource ID.
        struct OH\_Huks\_Blob keyAlias = {
            (uint32\_t)strlen(KEY\_ALIAS),
            (uint8\_t \*)KEY\_ALIAS
        };
        struct OH\_Huks\_Blob inData = {
            (uint32\_t)strlen(DATA\_TO\_SIGN),
            (uint8\_t \*)DATA\_TO\_SIGN
        };
        struct OH\_Huks\_ParamSet \*signParamSet = nullptr;
        OH\_Huks\_Result ohResult;
        do {
            ohResult = InitParamSet(&signParamSet, g\_signParamsTest, sizeof(g\_signParamsTest) / sizeof(OH\_Huks\_Param));
            if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
                break;
            }
            // Init
            uint8\_t handleS\[sizeof(uint64\_t)\] = {0};
            struct OH\_Huks\_Blob handleSign = { (uint32\_t)sizeof(uint64\_t), handleS };
            ohResult = OH\_Huks\_InitSession(&keyAlias, signParamSet, &handleSign, nullptr);
            if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
                break;
            }
            // Finish
            uint8\_t outDataS\[RSA\_COMMON\_SIZE\] = {0};
            struct OH\_Huks\_Blob outDataSign = { RSA\_COMMON\_SIZE, outDataS };
            ohResult = OH\_Huks\_FinishSession(&handleSign, signParamSet, &inData, &outDataSign);
            if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
                break;
            }
        } while (0);
        OH\_Huks\_FreeParamSet(&signParamSet);
        
        napi\_value ret;
        napi\_create\_int32(env, ohResult.errorCode, &ret);
        return ret;
    }
